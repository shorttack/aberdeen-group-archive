#!/usr/bin/env python3
"""
score_quotations_corpus_v1.py — v1.8.0 full-corpus prescience scorer.

Strategy (from §11w calibration, 2026-06-19):
  - Default pipeline = P2 (quote-only). Lighter, faster, more epistemically
    honest on generic-claim quotes than P1.
  - P1 (article-grounded) invoked ONLY as tiebreaker on uncertain mediums:
    P2_bucket == "medium" AND P2_confidence <= 2 AND P2 parse_ok.
  - Resolution: higher-confidence verdict wins; tie → P2.

Lifts proven blocks verbatim from score_quotations_calibration_v2.py:
  - SSL/certifi context
  - score_call() retry + parse logic
  - JSONL append-resume (skips parse_ok="true" records only)
  - prompt templates (P1 with article body, P2 quote-alone)
  - rule_a_bucket()
  - csv/corpus/routing loaders

Inputs (all Mac-local):
  ~/Desktop/Archive/aberdeen-group-archive/kastner-author/quotations/
    kastner_quotes_clean.csv      (1208 × 18, NO reject column)
    pipeline_1_routing_v1.json    (292 tuples, 220 P1-scorable)
    article_corpus_v1.json        (179 articles)
  ~/.config/adoptex/perplexity.env   (PERPLEXITY_API_KEY=...)

Outputs:
  quotations_corpus_v1.csv          one row per scored quote
  quotations_corpus_v1.jsonl        append-only audit (resume-safe)
  quotations_corpus_v1_report.md    distributions, tiebreaker rate, parse-fails

CLI:
  --commit              required for actual API calls (default = dry-run)
  --dry-run             explicit dry-run (default behavior)
  --limit N             cap total API calls (counts P2 + P1_tiebreak)
  --horizon LABEL       restrict to SH-3y / SH-5y / LH
  --row-id ID           score a single row (debug; bypasses MAX_API_CALLS)
  --skip-tiebreak       run P2 only (pure-P2 baseline)
  --force-tiebreak      run P1 on every P2-medium regardless of confidence

Cost envelope (full corpus, ~220 rows):
  ~220 P2 calls + ~18 P1 tiebreaker calls ≈ $12, ~65 min wall.
  Hard cap: MAX_API_CALLS=500 (~$25).
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

# ---------- paths (Mac local) ----------
HOME = Path.home()
ARCHIVE = HOME / "Desktop/Archive/aberdeen-group-archive"
QUOTATIONS = ARCHIVE / "kastner-author/quotations"

CSV_PATH = QUOTATIONS / "kastner_quotes_clean.csv"
CORPUS_JSON = QUOTATIONS / "article_corpus_v1.json"
ROUTING_JSON = QUOTATIONS / "pipeline_1_routing_v1.json"

OUT_CSV = QUOTATIONS / "quotations_corpus_v1.csv"
OUT_JSONL = QUOTATIONS / "quotations_corpus_v1.jsonl"
OUT_REPORT = QUOTATIONS / "quotations_corpus_v1_report.md"

# ---------- API ----------
API_URL = "https://api.perplexity.ai/chat/completions"
MODEL = "sonar-reasoning-pro"
MAX_RETRIES = 3
REQUEST_TIMEOUT = 90
RETRY_BACKOFF = 2
MAX_API_CALLS = 500  # ~$25 worst case
TEMPERATURE = 0.1
MAX_TOKENS = 1200
INTER_CALL_SLEEP = 0.5

# certifi for SSL cert verification on macOS Python (mirrors calibration v2)
try:
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    SSL_CTX = ssl.create_default_context()

# ---------- scoring constants ----------
SCORE_MIN = -1
SCORE_MAX = 5
CONFIDENCE_MIN = 1
CONFIDENCE_MAX = 3
BUCKET_HIGH_MIN = 4
BUCKET_MEDIUM_MIN = 2

# ---------- tiebreaker policy ----------
TIEBREAK_BUCKET = "medium"
TIEBREAK_MAX_CONFIDENCE = 2
TIEBREAK_REQUIRES_PARSE_OK = True

# ---------- prompts (verbatim from calibration v2) ----------
SYSTEM_PROMPT = """You are a technology industry historian specializing in enterprise IT trends from 1980-2026. You assess historical industry-analyst claims for prescience: did the claim's prediction or characterization hold up over time?

You return a strict JSON object — nothing else. No prose before or after. No markdown fences. No commentary.

Your assessment must be grounded in widely-documented technology history. If you genuinely don't know what happened, score conservatively and say so in the rationale."""

USER_TEMPLATE_P1 = """Score this analyst quotation for prescience.

Source: Peter S. Kastner, {publication} ({date})
Headline: {headline}
Forecast horizon: {horizon_label} ({horizon_int} years)

QUOTE (the claim to be scored):
{quote}

IMMEDIATE CONTEXT (surrounding sentences from the original article):
{immediate_context}

FULL ARTICLE BODY (for additional context — score the QUOTE, not the article):
{article_body}

---

Scoring rubric (0-5):
- 5 = Remarkably prescient. The specific prediction or pattern played out essentially as stated; widely confirmed by 2010-2026.
- 4 = Largely prescient. Direction correct; magnitudes or timing somewhat off.
- 3 = Partially right. Some elements held up, others didn't, or the claim was mixed.
- 2 = Mostly wrong. The trend went a different direction than implied.
- 1 = Wrong. The claim was contradicted by what actually happened.
- 0 = Cannot assess. The claim is too vague, too narrow, or you lack reliable knowledge to judge.

Score the QUOTE relative to its declared horizon (a 3-year forecast is judged at ~3 years post-publication; a long-horizon claim gets a longer window).

Confidence (1-3):
- 3 = High — this is well-documented industry history I know well.
- 2 = Medium — I have reasonable evidence but could be missing nuance.
- 1 = Low — limited knowledge of this specific subdomain.

Return exactly this JSON object — no other text:

{{
  "row_id": "{row_id}",
  "pipeline": "P1",
  "prescience_score": <0-5 integer>,
  "confidence": <1-3 integer>,
  "rationale": "<2-3 sentences citing what actually happened from publication through 2026. Reference specific developments, adoption rates, or technologies by name.>"
}}"""

USER_TEMPLATE_P2 = """Score this analyst quotation for prescience.

Source: Peter S. Kastner, {publication} ({date})
Headline: {headline}
Forecast horizon: {horizon_label} ({horizon_int} years)

QUOTE (the claim to be scored):
{quote}

IMMEDIATE CONTEXT (surrounding sentences from the original article):
{immediate_context}

---

Scoring rubric (0-5):
- 5 = Remarkably prescient. The specific prediction or pattern played out essentially as stated; widely confirmed by 2010-2026.
- 4 = Largely prescient. Direction correct; magnitudes or timing somewhat off.
- 3 = Partially right. Some elements held up, others didn't, or the claim was mixed.
- 2 = Mostly wrong. The trend went a different direction than implied.
- 1 = Wrong. The claim was contradicted by what actually happened.
- 0 = Cannot assess. The claim is too vague, too narrow, or you lack reliable knowledge to judge.

Score the QUOTE relative to its declared horizon (a 3-year forecast is judged at ~3 years post-publication; a long-horizon claim gets a longer window).

Confidence (1-3):
- 3 = High — this is well-documented industry history I know well.
- 2 = Medium — I have reasonable evidence but could be missing nuance.
- 1 = Low — limited knowledge of this specific subdomain.

Return exactly this JSON object — no other text:

{{
  "row_id": "{row_id}",
  "pipeline": "P2",
  "prescience_score": <0-5 integer>,
  "confidence": <1-3 integer>,
  "rationale": "<2-3 sentences citing what actually happened from publication through 2026. Reference specific developments, adoption rates, or technologies by name.>"
}}"""


# ---------- Rule A bucketing ----------
def rule_a_bucket(score: int) -> str:
    if score < 0:
        return "parse_fail"
    if score >= BUCKET_HIGH_MIN:
        return "high"
    if score >= BUCKET_MEDIUM_MIN:
        return "medium"
    return "low"


# ---------- loaders ----------
def load_api_key() -> str:
    for candidate in [
        Path.home() / ".config" / "adoptex" / "perplexity.env",
        Path("/tmp/perplexity.env"),
    ]:
        if candidate.exists():
            for line in candidate.read_text().splitlines():
                if line.startswith("PERPLEXITY_API_KEY="):
                    return line.split("=", 1)[1].strip()
    raise RuntimeError("PERPLEXITY_API_KEY not found in ~/.config/adoptex/perplexity.env")


def load_csv_by_row_id() -> dict[str, dict]:
    if not CSV_PATH.exists():
        sys.exit(f"FATAL: {CSV_PATH} not found")
    with open(CSV_PATH, newline="") as f:
        return {r["row_id"]: r for r in csv.DictReader(f)}


def load_corpus_by_article_id() -> dict[str, dict]:
    if not CORPUS_JSON.exists():
        sys.exit(f"FATAL: {CORPUS_JSON} not found")
    payload = json.loads(CORPUS_JSON.read_text())
    out = {}
    for a in payload["articles"]:
        article_id = f"{a.get('source')}-{a.get('source_idx')}"
        out[article_id] = a
    return out


def load_routing() -> dict:
    if not ROUTING_JSON.exists():
        sys.exit(f"FATAL: {ROUTING_JSON} not found — run route_quotations_to_horizon_v2.py --commit first")
    return json.loads(ROUTING_JSON.read_text())


def load_already_scored() -> set[tuple[str, str]]:
    """Read JSONL and return set of (row_id, pipeline) pairs already scored OK.

    Only parse_ok='true' records are considered "done". Failed records will
    be retried on resume.
    """
    if not OUT_JSONL.exists():
        return set()
    done = set()
    for line in OUT_JSONL.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
            if rec.get("parse_ok") == "true":
                done.add((str(rec["row_id"]), rec["pipeline"]))
        except Exception:
            continue
    return done


# ---------- API ----------
def score_call(api_key: str, row_id: str, pipeline: str, prompt: str) -> dict:
    """One API call with retry. Returns score dict."""
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE,
    }
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    start = time.monotonic()
    last_err = None
    for attempt in range(MAX_RETRIES):
        try:
            with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT, context=SSL_CTX) as resp:
                body = resp.read().decode("utf-8")
            elapsed = time.monotonic() - start
            data = json.loads(body)
            content = data["choices"][0]["message"]["content"].strip()
            content = re.sub(r"<think>.*?</think>\s*", "", content, flags=re.DOTALL).strip()
            if content.startswith("```"):
                content = re.sub(r"^```[a-zA-Z]*\n", "", content)
                content = re.sub(r"\n```\s*$", "", content)
            if not content.startswith("{"):
                m = re.search(r"\{[^{}]*\"prescience_score\"[^{}]*\}", content, flags=re.DOTALL)
                if m:
                    content = m.group(0)
            parsed = json.loads(content)
            return {
                "row_id": row_id,
                "pipeline": pipeline,
                "prescience_score": int(parsed["prescience_score"]),
                "confidence": int(parsed["confidence"]),
                "rationale": str(parsed["rationale"]),
                "elapsed_sec": f"{elapsed:.2f}",
                "parse_ok": "true",
                "raw_response": content,
                "error": "",
            }
        except (urllib.error.HTTPError, urllib.error.URLError,
                json.JSONDecodeError, KeyError, ValueError) as e:
            last_err = e
            if attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_BACKOFF * (2 ** attempt))
    elapsed = time.monotonic() - start
    return {
        "row_id": row_id,
        "pipeline": pipeline,
        "prescience_score": -1,
        "confidence": 1,
        "rationale": f"Parse failed after {MAX_RETRIES} retries: {type(last_err).__name__}: {str(last_err)[:200]}",
        "elapsed_sec": f"{elapsed:.2f}",
        "parse_ok": "false",
        "raw_response": "",
        "error": str(last_err)[:300],
    }


def append_jsonl(rec: dict) -> None:
    with open(OUT_JSONL, "a") as f:
        f.write(json.dumps(rec) + "\n")


# ---------- work-queue builder ----------
def build_work_queue(csv_rows: dict, routing: dict, horizon_filter: str | None = None,
                     row_id_filter: str | None = None) -> list[dict]:
    """Return list of {row_id, article_id, horizon_label, horizon_int} for
    every P1-scorable (routed, non-orphan, non-prefilter-skip) tuple.

    Unlike calibration, no analyst-truth filter — the full corpus run scores
    every P1-scorable row, with or without analyst adjudication.
    """
    out = []
    seen = set()  # dedupe (row_id, horizon_label) — same row may appear in multiple tuples
    for t in routing["routing_tuples"]:
        if t["article_id"].startswith("admit-orphan-"):
            continue
        if t["horizon_label"] == "prefilter_skip":
            continue
        if horizon_filter and t["horizon_label"] != horizon_filter:
            continue
        for rid in t["csv_row_ids"]:
            rid = str(rid)
            if row_id_filter and rid != row_id_filter:
                continue
            key = (rid, t["horizon_label"])
            if key in seen:
                continue
            if rid not in csv_rows:
                continue  # row missing from CSV — skip silently
            seen.add(key)
            out.append({
                "row_id": rid,
                "article_id": t["article_id"],
                "horizon_label": t["horizon_label"],
                "horizon_int": t["horizon_int"],
            })
    return out


# ---------- prompt builder ----------
def build_prompt(pipeline: str, row: dict, work_item: dict, article: dict | None) -> str:
    body = (article or {}).get("body", "") if pipeline == "P1" else ""
    template = USER_TEMPLATE_P1 if pipeline == "P1" else USER_TEMPLATE_P2
    return template.format(
        row_id=work_item["row_id"],
        publication=row.get("publication", ""),
        date=row.get("date", ""),
        headline=row.get("headline", ""),
        horizon_label=work_item["horizon_label"],
        horizon_int=work_item["horizon_int"],
        quote=row.get("kastner_quotation", ""),
        immediate_context=row.get("immediate_context", ""),
        article_body=body[:30000] if pipeline == "P1" else "",
    )


# ---------- tiebreaker predicate ----------
def needs_tiebreaker(p2_rec: dict, force: bool = False) -> bool:
    """Return True iff P2 result warrants a P1 tiebreaker call."""
    if p2_rec.get("parse_ok") != "true":
        return False  # cannot tiebreak a parse_fail
    bucket = rule_a_bucket(p2_rec["prescience_score"])
    if force:
        return bucket == TIEBREAK_BUCKET
    return (
        bucket == TIEBREAK_BUCKET
        and int(p2_rec["confidence"]) <= TIEBREAK_MAX_CONFIDENCE
    )


# ---------- final-verdict resolver ----------
def resolve_final(p2_rec: dict, p1_rec: dict | None) -> dict:
    """Return final verdict dict: {final_score, final_confidence, final_bucket,
    final_pipeline, final_rationale, tiebreaker_invoked}.
    """
    p2_ok = p2_rec.get("parse_ok") == "true"
    if p1_rec is None:
        # No tiebreaker invoked
        if not p2_ok:
            return {
                "final_score": -1,
                "final_confidence": 1,
                "final_bucket": "human_review",
                "final_pipeline": "human_review",
                "final_rationale": p2_rec.get("rationale", ""),
                "tiebreaker_invoked": False,
            }
        return {
            "final_score": p2_rec["prescience_score"],
            "final_confidence": p2_rec["confidence"],
            "final_bucket": rule_a_bucket(p2_rec["prescience_score"]),
            "final_pipeline": "P2",
            "final_rationale": p2_rec["rationale"],
            "tiebreaker_invoked": False,
        }
    # Tiebreaker invoked
    p1_ok = p1_rec.get("parse_ok") == "true"
    if not p2_ok and not p1_ok:
        return {
            "final_score": -1,
            "final_confidence": 1,
            "final_bucket": "human_review",
            "final_pipeline": "human_review",
            "final_rationale": "both pipelines parse_fail",
            "tiebreaker_invoked": True,
        }
    if not p1_ok:
        # P1 failed; fall back to P2
        return {
            "final_score": p2_rec["prescience_score"],
            "final_confidence": p2_rec["confidence"],
            "final_bucket": rule_a_bucket(p2_rec["prescience_score"]),
            "final_pipeline": "P2_p1_fail",
            "final_rationale": p2_rec["rationale"],
            "tiebreaker_invoked": True,
        }
    # Both OK — higher confidence wins; tie → P2 (default)
    if int(p1_rec["confidence"]) > int(p2_rec["confidence"]):
        winner, winner_label = p1_rec, "P1_tiebreak"
    else:
        winner, winner_label = p2_rec, "P2"
    return {
        "final_score": winner["prescience_score"],
        "final_confidence": winner["confidence"],
        "final_bucket": rule_a_bucket(winner["prescience_score"]),
        "final_pipeline": winner_label,
        "final_rationale": winner["rationale"],
        "tiebreaker_invoked": True,
    }


# ---------- report writer ----------
def write_outputs(work_queue: list[dict], csv_rows: dict, corpus: dict,
                  p2_by_row: dict, p1_by_row: dict) -> None:
    """Write final CSV + markdown report.

    p2_by_row: {row_id: p2_rec}
    p1_by_row: {row_id: p1_rec}  (only for rows that got tiebreaker)
    """
    fieldnames = [
        "row_id", "article_id", "horizon_label", "horizon_int",
        "analyst", "headline", "publication", "date", "quote",
        "p2_score", "p2_confidence", "p2_bucket", "p2_rationale",
        "p2_elapsed_sec", "p2_parse_ok",
        "tiebreaker_invoked",
        "p1_score", "p1_confidence", "p1_bucket", "p1_rationale",
        "p1_elapsed_sec", "p1_parse_ok",
        "final_score", "final_confidence", "final_bucket",
        "final_pipeline", "final_rationale",
    ]
    rows_out = []
    n_p2 = 0
    n_tiebreak = 0
    n_p2_only_medium = 0  # P2 mediums that did NOT get tiebreaker (conf >= 3)
    final_bucket_counter = Counter()
    final_pipeline_counter = Counter()
    p2_bucket_counter = Counter()
    p1_flip_count = 0  # of tiebreaker subset, how often final != P2
    parse_fails = []

    for w in work_queue:
        rid = w["row_id"]
        p2 = p2_by_row.get(rid)
        if p2 is None:
            continue  # never scored (shouldn't happen unless --limit cut it)
        n_p2 += 1
        p2_bucket = rule_a_bucket(p2["prescience_score"]) if p2.get("parse_ok") == "true" else "parse_fail"
        p2_bucket_counter[p2_bucket] += 1
        if p2.get("parse_ok") != "true":
            parse_fails.append((rid, "P2", p2.get("error", "")))

        p1 = p1_by_row.get(rid)
        if p1 is not None:
            n_tiebreak += 1
            if p1.get("parse_ok") != "true":
                parse_fails.append((rid, "P1_tiebreak", p1.get("error", "")))
        elif p2_bucket == "medium":
            # P2-medium NOT tiebroken means conf>=3 (or --skip-tiebreak)
            n_p2_only_medium += 1

        final = resolve_final(p2, p1)
        final_bucket_counter[final["final_bucket"]] += 1
        final_pipeline_counter[final["final_pipeline"]] += 1
        if p1 is not None and final["final_pipeline"].startswith("P1"):
            p1_flip_count += 1

        row = csv_rows[rid]
        rows_out.append({
            "row_id": rid,
            "article_id": w["article_id"],
            "horizon_label": w["horizon_label"],
            "horizon_int": w["horizon_int"],
            "analyst": row.get("analyst", ""),
            "headline": row.get("headline", ""),
            "publication": row.get("publication", ""),
            "date": row.get("date", ""),
            "quote": row.get("kastner_quotation", ""),
            "p2_score": p2["prescience_score"],
            "p2_confidence": p2["confidence"],
            "p2_bucket": p2_bucket,
            "p2_rationale": p2["rationale"][:1500],
            "p2_elapsed_sec": p2["elapsed_sec"],
            "p2_parse_ok": p2["parse_ok"],
            "tiebreaker_invoked": "true" if p1 is not None else "false",
            "p1_score": p1["prescience_score"] if p1 else "",
            "p1_confidence": p1["confidence"] if p1 else "",
            "p1_bucket": rule_a_bucket(p1["prescience_score"]) if (p1 and p1.get("parse_ok") == "true") else ("parse_fail" if p1 else ""),
            "p1_rationale": (p1["rationale"][:1500] if p1 else ""),
            "p1_elapsed_sec": p1["elapsed_sec"] if p1 else "",
            "p1_parse_ok": p1["parse_ok"] if p1 else "",
            "final_score": final["final_score"],
            "final_confidence": final["final_confidence"],
            "final_bucket": final["final_bucket"],
            "final_pipeline": final["final_pipeline"],
            "final_rationale": final["final_rationale"][:1500],
        })

    with open(OUT_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        w.writeheader()
        for r in rows_out:
            w.writerow(r)

    # Markdown report
    md = []
    md.append("# v1.8.0 quotations corpus — prescience scoring report")
    md.append(f"\nGenerated: {dt.datetime.now(dt.timezone.utc).isoformat()}\n")
    md.append("## Run metadata\n")
    md.append(f"- Model: `{MODEL}`")
    md.append(f"- Strategy: P2 default, P1 tiebreaker on (bucket=medium AND confidence≤2)")
    md.append(f"- Rows scored: **{n_p2}**")
    md.append(f"- Tiebreakers invoked: **{n_tiebreak}**")
    if n_p2:
        md.append(f"- Tiebreaker rate: {100.0 * n_tiebreak / n_p2:.1f}% of rows")
    md.append(f"- P2-medium NOT tiebroken (confidence=3): {n_p2_only_medium}")
    md.append(f"- Parse-fails total: {len(parse_fails)}")

    md.append("\n## Final-bucket distribution\n")
    md.append("| Bucket | Count |")
    md.append("|---|---:|")
    for b in ("high", "medium", "low", "parse_fail", "human_review"):
        md.append(f"| {b} | {final_bucket_counter.get(b, 0)} |")

    md.append("\n## Final-pipeline mix\n")
    md.append("| Pipeline | Count |")
    md.append("|---|---:|")
    for p in ("P2", "P1_tiebreak", "P2_p1_fail", "human_review"):
        md.append(f"| {p} | {final_pipeline_counter.get(p, 0)} |")

    md.append("\n## P2 bucket distribution (pre-tiebreak)\n")
    md.append("| Bucket | Count |")
    md.append("|---|---:|")
    for b in ("high", "medium", "low", "parse_fail"):
        md.append(f"| {b} | {p2_bucket_counter.get(b, 0)} |")

    md.append("\n## Tiebreaker effectiveness\n")
    if n_tiebreak:
        md.append(f"- Of {n_tiebreak} tiebreakers invoked, P1 won (changed final verdict) on **{p1_flip_count}** rows = {100.0 * p1_flip_count / n_tiebreak:.1f}%")
    else:
        md.append("_(no tiebreakers invoked)_")

    if parse_fails:
        md.append("\n## Parse-fail roll-up\n")
        md.append("| row_id | pipeline | error |")
        md.append("|---|---|---|")
        for rid, pipe, err in parse_fails[:50]:
            err_short = err.replace("|", "/").replace("\n", " ")[:120]
            md.append(f"| {rid} | {pipe} | {err_short} |")

    # Top-20 high-confidence prescient
    high_conf_high = sorted(
        [r for r in rows_out if r["final_bucket"] == "high" and r["final_confidence"] == 3],
        key=lambda r: (-int(r["final_score"]), r["row_id"]),
    )[:20]
    md.append("\n## Top 20 high-confidence prescient rows (final_bucket=high, conf=3)\n")
    if high_conf_high:
        md.append("| row_id | score | horizon | headline | publication | date |")
        md.append("|---|---:|---|---|---|---|")
        for r in high_conf_high:
            md.append(f"| {r['row_id']} | {r['final_score']} | {r['horizon_label']} | {r['headline'][:60]} | {r['publication']} | {r['date']} |")
    else:
        md.append("_(none)_")

    # Top-20 high-confidence non-prescient
    high_conf_low = sorted(
        [r for r in rows_out if r["final_bucket"] == "low" and r["final_confidence"] == 3],
        key=lambda r: (int(r["final_score"]), r["row_id"]),
    )[:20]
    md.append("\n## Top 20 high-confidence non-prescient rows (final_bucket=low, conf=3)\n")
    if high_conf_low:
        md.append("| row_id | score | horizon | headline | publication | date |")
        md.append("|---|---:|---|---|---|---|")
        for r in high_conf_low:
            md.append(f"| {r['row_id']} | {r['final_score']} | {r['horizon_label']} | {r['headline'][:60]} | {r['publication']} | {r['date']} |")
    else:
        md.append("_(none)_")

    # Tiebreaker disagreements
    tiebreak_rows = [r for r in rows_out if r["tiebreaker_invoked"] == "true" and r["final_pipeline"].startswith("P1")]
    md.append(f"\n## Tiebreaker flips (P1 changed verdict, {len(tiebreak_rows)} rows)\n")
    if tiebreak_rows:
        md.append("| row_id | P2 (b/conf) | P1 (b/conf) | final | headline |")
        md.append("|---|---|---|---|---|")
        for r in tiebreak_rows:
            md.append(
                f"| {r['row_id']} | {r['p2_bucket']}/{r['p2_confidence']} "
                f"| {r['p1_bucket']}/{r['p1_confidence']} "
                f"| {r['final_bucket']} | {r['headline'][:50]} |"
            )
    else:
        md.append("_(none)_")

    OUT_REPORT.write_text("\n".join(md))


# ---------- main ----------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--commit", action="store_true",
                    help="Make actual API calls. Default is dry-run.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Explicit dry-run (same as default).")
    ap.add_argument("--limit", type=int, default=0,
                    help="Cap total API calls (P2 + P1_tiebreak combined). 0 = no limit.")
    ap.add_argument("--horizon", choices=["SH-3y", "SH-5y", "LH"], default=None,
                    help="Restrict to one horizon bucket.")
    ap.add_argument("--row-id", type=str, default=None,
                    help="Score one row only (debug; bypasses MAX_API_CALLS).")
    ap.add_argument("--skip-tiebreak", action="store_true",
                    help="Run P2 only; never invoke P1.")
    ap.add_argument("--force-tiebreak", action="store_true",
                    help="Invoke P1 on every P2-medium regardless of confidence.")
    args = ap.parse_args()

    if args.commit and args.dry_run:
        sys.exit("FATAL: --commit and --dry-run are mutually exclusive.")
    if args.skip_tiebreak and args.force_tiebreak:
        sys.exit("FATAL: --skip-tiebreak and --force-tiebreak are mutually exclusive.")
    commit = bool(args.commit) and not args.dry_run

    print("v1.8.0 quotations corpus prescience scorer")
    print(f"Mode: {'COMMIT (API calls)' if commit else 'DRY-RUN (no API calls)'}")
    print(f"Tiebreak: " + (
        "DISABLED (--skip-tiebreak)" if args.skip_tiebreak else
        "FORCED on all P2-mediums (--force-tiebreak)" if args.force_tiebreak else
        f"P2 bucket=medium AND confidence≤{TIEBREAK_MAX_CONFIDENCE}"
    ))
    print("=" * 70)

    csv_rows = load_csv_by_row_id()
    corpus = load_corpus_by_article_id()
    routing = load_routing()
    print(f"CSV rows:           {len(csv_rows):>6}")
    print(f"Corpus articles:    {len(corpus):>6}")
    print(f"Routing tuples:     {routing.get('routing_tuple_count', len(routing['routing_tuples'])):>6}")
    print(f"Summary by label:   {routing.get('summary_by_label', {})}")

    work_queue = build_work_queue(
        csv_rows, routing,
        horizon_filter=args.horizon,
        row_id_filter=args.row_id,
    )
    horizon_counts = Counter(w["horizon_label"] for w in work_queue)
    print(f"\nWork queue size:    {len(work_queue)} P1-scorable rows")
    print(f"  by horizon:       {dict(horizon_counts)}")

    already = load_already_scored()
    p2_resumed = sum(1 for (r, p) in already if p == "P2")
    p1_resumed = sum(1 for (r, p) in already if p == "P1_tiebreak")
    print(f"\nResume state (parse_ok=true records in JSONL):")
    print(f"  P2 already scored:           {p2_resumed}")
    print(f"  P1_tiebreak already scored:  {p1_resumed}")

    # Phase A: Plan P2 calls
    p2_todo = []
    for w in work_queue:
        if (w["row_id"], "P2") not in already:
            p2_todo.append(w)
    print(f"\nPhase A (P2 default):  {len(p2_todo)} new calls planned")

    # Apply --limit if set: cap total calls across both phases
    # We don't know P1 calls until P2 results come in; for planning, use
    # calibration estimate of ~8% tiebreaker rate for cost projection.
    est_p1_tiebreak = 0
    if not args.skip_tiebreak:
        # rough estimate for dry-run; actual will vary
        est_p1_tiebreak = max(1, int(len(p2_todo) * 0.10))
    est_total_calls = len(p2_todo) + est_p1_tiebreak

    if args.limit and args.limit > 0:
        if est_total_calls > args.limit:
            # cap p2_todo such that p2_todo + est_p1_tiebreak <= limit
            # since tiebreak depends on results, just cap p2_todo to limit
            # and stop early if we exceed during commit phase
            print(f"  --limit {args.limit} applied; will stop when total calls hit cap")
        # actual enforcement happens in commit loop

    print(f"\nEstimated calls:   {est_total_calls} (P2: {len(p2_todo)}, P1_tiebreak ~10% estimate: {est_p1_tiebreak})")
    print(f"Estimated cost:    ${est_total_calls * 0.05:.2f}")
    print(f"Estimated wall:    ~{est_total_calls * 17 / 60:.1f} min (at ~17s/call avg)")

    if not commit:
        print(f"\nDRY-RUN preview (first 3 P2 calls):")
        for w in p2_todo[:3]:
            row = csv_rows[w["row_id"]]
            print(f"  row_id={w['row_id']:>5} P2 {w['horizon_label']} | {row['headline'][:60]}")
        print(f"\nPass --commit to run the API calls.")
        return 0

    # Pre-flight: hard cap
    if est_total_calls > MAX_API_CALLS:
        print(f"\nFATAL: estimated {est_total_calls} calls exceeds MAX_API_CALLS={MAX_API_CALLS}.")
        print(f"  Use --limit or raise MAX_API_CALLS deliberately.")
        return 1

    # Commit path
    api_key = load_api_key()
    print(f"\nAPI key loaded. Starting Phase A (P2 default)...")
    print(f"Append-only JSONL: {OUT_JSONL}\n")

    # Track in-memory p2/p1 results for later resolver (also resumed from JSONL)
    p2_by_row: dict[str, dict] = {}
    p1_by_row: dict[str, dict] = {}
    if OUT_JSONL.exists():
        for line in OUT_JSONL.read_text().splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                if rec.get("parse_ok") != "true":
                    continue
                rid = str(rec["row_id"])
                if rec["pipeline"] == "P2":
                    p2_by_row[rid] = rec
                elif rec["pipeline"] == "P1_tiebreak":
                    p1_by_row[rid] = rec
            except Exception:
                continue

    call_count = 0

    # --- Phase A: P2 ---
    for i, w in enumerate(p2_todo, 1):
        if args.limit and call_count >= args.limit:
            print(f"\n[stopped: --limit {args.limit} hit during Phase A]")
            break
        rid = w["row_id"]
        row = csv_rows[rid]
        article = corpus.get(w["article_id"])
        prompt = build_prompt("P2", row, w, article)
        rec = score_call(api_key, rid, "P2", prompt)
        rec["horizon_label"] = w["horizon_label"]
        rec["article_id"] = w["article_id"]
        rec["model"] = MODEL
        rec["ts"] = dt.datetime.now(dt.timezone.utc).isoformat()
        append_jsonl(rec)
        if rec["parse_ok"] == "true":
            p2_by_row[rid] = rec
        bucket = rule_a_bucket(rec["prescience_score"]) if rec["parse_ok"] == "true" else "FAIL"
        print(f"  [A {i:>3}/{len(p2_todo)}] row={rid:>5} P2 {w['horizon_label']:>5} → score={rec['prescience_score']:>2} {bucket:>10} conf={rec['confidence']} ({rec['elapsed_sec']}s)")
        call_count += 1
        time.sleep(INTER_CALL_SLEEP)

    # --- Phase B: P1 tiebreakers ---
    if args.skip_tiebreak:
        print(f"\nPhase B SKIPPED (--skip-tiebreak)")
        tiebreak_queue = []
    else:
        tiebreak_queue = []
        for w in work_queue:
            rid = w["row_id"]
            p2 = p2_by_row.get(rid)
            if not p2:
                continue  # P2 not yet scored (limit cut, parse_fail, etc.)
            if (rid, "P1_tiebreak") in already:
                continue  # already tiebroken
            if needs_tiebreaker(p2, force=args.force_tiebreak):
                tiebreak_queue.append(w)
        print(f"\nPhase B (P1 tiebreakers): {len(tiebreak_queue)} rows queued")
        for i, w in enumerate(tiebreak_queue, 1):
            if args.limit and call_count >= args.limit:
                print(f"\n[stopped: --limit {args.limit} hit during Phase B]")
                break
            rid = w["row_id"]
            row = csv_rows[rid]
            article = corpus.get(w["article_id"])
            prompt = build_prompt("P1", row, w, article)
            rec = score_call(api_key, rid, "P1_tiebreak", prompt)
            rec["horizon_label"] = w["horizon_label"]
            rec["article_id"] = w["article_id"]
            rec["model"] = MODEL
            rec["ts"] = dt.datetime.now(dt.timezone.utc).isoformat()
            append_jsonl(rec)
            if rec["parse_ok"] == "true":
                p1_by_row[rid] = rec
            bucket = rule_a_bucket(rec["prescience_score"]) if rec["parse_ok"] == "true" else "FAIL"
            print(f"  [B {i:>3}/{len(tiebreak_queue)}] row={rid:>5} P1 {w['horizon_label']:>5} → score={rec['prescience_score']:>2} {bucket:>10} conf={rec['confidence']} ({rec['elapsed_sec']}s)")
            call_count += 1
            time.sleep(INTER_CALL_SLEEP)

    # --- Phase C: write outputs ---
    print(f"\nPhase C: writing CSV + report ...")
    write_outputs(work_queue, csv_rows, corpus, p2_by_row, p1_by_row)
    print(f"  wrote {OUT_CSV} ({OUT_CSV.stat().st_size:,} bytes)")
    print(f"  wrote {OUT_REPORT} ({OUT_REPORT.stat().st_size:,} bytes)")
    print(f"  appended {OUT_JSONL} ({OUT_JSONL.stat().st_size:,} bytes)")
    print(f"\nTotal API calls this run: {call_count}")
    print(f"\nDone. Open the report:")
    print(f"  open {OUT_REPORT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
