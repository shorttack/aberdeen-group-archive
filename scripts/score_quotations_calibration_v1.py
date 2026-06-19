#!/usr/bin/env python3
"""
score_quotations_calibration_v1.py — v1.8.0 A/B calibration harness.

Purpose
-------
Score each row in the v1.8.0 highlight-reel calibration set with BOTH pipelines,
then compare verdicts to decide whether Pipeline 2 (quote-alone, cheap) is good
enough to be the default for the full corpus, or Pipeline 1 (full article body)
is required for signal.

Pipeline 1 (P1, expensive): full article body + quote + immediate_context
Pipeline 2 (P2, cheap):     quote + immediate_context only (no article body)

Both pipelines use the same horizon-aware system+user prompt template and the
same Perplexity cloud API (sonar-reasoning-pro), so the only varying input is
whether the article body is included. Bucket agreement (Rule A) tells us
whether the body context materially changes the verdict.

Calibration set
---------------
Rows that are SIMULTANEOUSLY:
  1. P1-scorable in `pipeline_1_routing_v1.json`
     (i.e. routed to SH-3y / SH-5y / LH; excludes prefilter_skip + admit-orphan)
  2. Have analyst-authored truth: non-empty `prescience_score` AND non-empty
     `accuracy_outcome` in `kastner_quotes_clean.csv`

This is the "230 quote highlight reel" (per `highlight_reel.md` banner)
intersected with what's actually scorable in v1.8.0. Expected size: ~170 rows.

Outputs (under kastner-author/quotations/)
------------------------------------------
- calibration_ab_v1.csv  — one row per scored quote with both verdicts, agreement flag
- calibration_ab_v1_report.md — markdown report: P1 vs P2 distributions, agreement
                                rate, Rule-A bucket transition matrix, accuracy
                                vs analyst truth, top disagreements with text
- calibration_ab_v1.jsonl — append-only per-call audit log (one line per API call)

Rule A bucketing (matches kastner-archive-pipeline §"Verdict rules"):
  raw_score >= 3.5 → high
  raw_score >= 2.0 → medium
  else            → low
(Pass C uses 0-5 integer scores; -1 = parse-fail. We use the same rubric.)

Cost ceiling
------------
Default is dry-run (no API calls; reports calibration-set membership only).
With --commit, runs ~170 rows × 2 pipelines = ~340 API calls. At
sonar-reasoning-pro ~$0.05/call that's ~$17, well under Pete's $500 ceiling.
Hard cap `MAX_API_CALLS` (default 400) aborts before runaway.

Resume safety
-------------
calibration_ab_v1.jsonl is append-only. On resume, every (row_id, pipeline)
pair already in the JSONL is skipped, so a partial run can be completed
without re-paying for scored rows.

Versioning / paths
------------------
Mac-only. Reads from local clone at:
  ~/Desktop/Archive/aberdeen-group-archive/kastner-author/quotations/

Producer/consumer contract verified pre-commit (Gotcha 9):
  pipeline_1_routing_v1.json — routing_tuples[].{article_id, headline_norm,
    horizon_label, horizon_int, csv_row_ids[]}; top-level routing_tuple_count,
    summary_by_label, admit_orphan_row_ids
  article_corpus_v1.json — articles[].{source, source_idx, headline,
    headline_norm, body, body_chars, date}
  kastner_quotes_clean.csv — 18 cols: row_id, article_seq, date, headline,
    publication, author, content_type, kastner_quotation, immediate_context,
    is_predictive, prescience_score, prescience_rationale,
    forecast_horizon_years, theme, decade, accuracy_outcome, verdict_rationale,
    verdict_sources. NO `reject` column. Truth set = rows with non-empty
    prescience_score AND non-empty accuracy_outcome.

v1: 2026-06-19 AM-3 (post-Q1-triage)
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

OUT_CSV = QUOTATIONS / "calibration_ab_v1.csv"
OUT_JSONL = QUOTATIONS / "calibration_ab_v1.jsonl"
OUT_REPORT = QUOTATIONS / "calibration_ab_v1_report.md"

# ---------- API ----------
API_URL = "https://api.perplexity.ai/chat/completions"
MODEL = "sonar-reasoning-pro"
MAX_RETRIES = 3
REQUEST_TIMEOUT = 90
RETRY_BACKOFF = 2
MAX_API_CALLS = 400  # hard cost cap (~$20 at $0.05/call)
SSL_CTX = ssl.create_default_context()

# ---------- prompt ----------
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
    """Pass C verdict rule. Score -1 = parse_fail."""
    if score < 0:
        return "parse_fail"
    if score >= 4:    # 4 or 5 → high
        return "high"
    if score >= 2:    # 2 or 3 → medium
        return "medium"
    return "low"      # 0 or 1


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
    raise RuntimeError(
        "PERPLEXITY_API_KEY not found in ~/.config/adoptex/perplexity.env"
    )


def load_csv_by_row_id() -> dict[str, dict]:
    """Return {row_id: row_dict} for kastner_quotes_clean.csv."""
    if not CSV_PATH.exists():
        sys.exit(f"FATAL: {CSV_PATH} not found")
    with open(CSV_PATH, newline="") as f:
        return {r["row_id"]: r for r in csv.DictReader(f)}


def load_corpus_by_article_id() -> dict[str, dict]:
    """Return {article_id ('source-source_idx'): article_dict}."""
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
    """Read JSONL and return set of (row_id, pipeline) pairs already scored OK."""
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
    """One API call. Returns dict with prescience_score, confidence, rationale,
    parse_ok, elapsed_sec, raw_response, error."""
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": 1200,
        "temperature": 0.1,
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


# ---------- calibration-set builder ----------
def build_calibration_set(csv_rows: dict, routing: dict) -> list[dict]:
    """Return list of {row_id, article_id, horizon_label, horizon_int} for
    rows that are (a) P1-scorable (routed to SH-3y/SH-5y/LH, non-orphan) AND
    (b) have analyst truth (non-empty prescience_score AND accuracy_outcome).
    """
    # Step 1: scorable tuples (one row may appear in >1 tuple via range
    # horizons; we keep ALL (row_id, horizon_label) variants so calibration
    # captures the multi-horizon case)
    scorable = []  # list of (row_id, article_id, horizon_label, horizon_int)
    for t in routing["routing_tuples"]:
        if t["article_id"].startswith("admit-orphan-"):
            continue
        if t["horizon_label"] == "prefilter_skip":
            continue
        for rid in t["csv_row_ids"]:
            scorable.append({
                "row_id": str(rid),
                "article_id": t["article_id"],
                "horizon_label": t["horizon_label"],
                "horizon_int": t["horizon_int"],
            })

    # Step 2: filter by analyst truth
    out = []
    for s in scorable:
        rid = s["row_id"]
        row = csv_rows.get(rid)
        if not row:
            continue
        if not row.get("prescience_score", "").strip():
            continue
        if not row.get("accuracy_outcome", "").strip():
            continue
        out.append(s)
    return out


# ---------- report writer ----------
def write_report(records: list[dict], csv_rows: dict, calibration_set: list[dict]) -> None:
    """records = list of all completed score dicts (both pipelines per row).
    Writes calibration_ab_v1.csv + calibration_ab_v1_report.md.
    """
    # Group by row_id
    by_row = defaultdict(dict)  # row_id -> {"P1": rec, "P2": rec}
    for r in records:
        if r.get("parse_ok") != "true":
            continue
        by_row[str(r["row_id"])][r["pipeline"]] = r

    # CSV output: one row per quote with both verdicts side-by-side
    fieldnames = [
        "row_id", "horizon_label", "horizon_int",
        "headline", "publication", "date",
        "kastner_quotation",
        "analyst_prescience_score", "analyst_accuracy_outcome",
        "score_p1", "bucket_p1", "confidence_p1", "rationale_p1",
        "score_p2", "bucket_p2", "confidence_p2", "rationale_p2",
        "buckets_agree", "p1_minus_p2",
    ]
    rows_out = []
    n_agree = 0
    n_both = 0
    bucket_pair_counter = Counter()
    for cs in calibration_set:
        rid = cs["row_id"]
        pair = by_row.get(rid, {})
        p1 = pair.get("P1")
        p2 = pair.get("P2")
        if not (p1 and p2):
            continue
        n_both += 1
        b1 = rule_a_bucket(p1["prescience_score"])
        b2 = rule_a_bucket(p2["prescience_score"])
        agree = (b1 == b2)
        if agree:
            n_agree += 1
        bucket_pair_counter[(b1, b2)] += 1
        csv_row = csv_rows[rid]
        rows_out.append({
            "row_id": rid,
            "horizon_label": cs["horizon_label"],
            "horizon_int": cs["horizon_int"],
            "headline": csv_row.get("headline", ""),
            "publication": csv_row.get("publication", ""),
            "date": csv_row.get("date", ""),
            "kastner_quotation": csv_row.get("kastner_quotation", ""),
            "analyst_prescience_score": csv_row.get("prescience_score", ""),
            "analyst_accuracy_outcome": csv_row.get("accuracy_outcome", ""),
            "score_p1": p1["prescience_score"],
            "bucket_p1": b1,
            "confidence_p1": p1["confidence"],
            "rationale_p1": p1["rationale"],
            "score_p2": p2["prescience_score"],
            "bucket_p2": b2,
            "confidence_p2": p2["confidence"],
            "rationale_p2": p2["rationale"],
            "buckets_agree": "true" if agree else "false",
            "p1_minus_p2": p1["prescience_score"] - p2["prescience_score"],
        })

    with open(OUT_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        w.writeheader()
        for r in rows_out:
            w.writerow(r)

    # Markdown report
    agreement_pct = (100.0 * n_agree / n_both) if n_both else 0.0
    p1_counts = Counter(r["bucket_p1"] for r in rows_out)
    p2_counts = Counter(r["bucket_p2"] for r in rows_out)
    md = []
    md.append("# v1.8.0 calibration A/B report")
    md.append(f"\nGenerated: {dt.datetime.utcnow().isoformat()}Z\n")
    md.append(f"- Calibration set size (P1-scorable ∩ analyst-truth): **{len(calibration_set)}**")
    md.append(f"- Both pipelines scored: **{n_both}**")
    md.append(f"- Bucket agreement (Rule A: high/medium/low): **{n_agree} / {n_both} = {agreement_pct:.1f}%**")
    md.append(f"\nVerdict: " + (
        "**Pipeline 2 (quote-alone) is good enough — use as default for full corpus.**"
        if agreement_pct >= 80.0 else
        "**Pipeline 1 (full article body) materially changes verdicts — keep article body in production scoring.**"
    ))
    md.append("\n## Bucket distributions\n")
    md.append("| Bucket | P1 (full article) | P2 (quote only) |")
    md.append("|---|---:|---:|")
    for b in ("high", "medium", "low", "parse_fail"):
        md.append(f"| {b} | {p1_counts.get(b, 0)} | {p2_counts.get(b, 0)} |")
    md.append("\n## Bucket transition matrix (P1 → P2)\n")
    md.append("| P1 \\ P2 | high | medium | low | parse_fail |")
    md.append("|---|---:|---:|---:|---:|")
    for b1 in ("high", "medium", "low", "parse_fail"):
        cells = [str(bucket_pair_counter.get((b1, b2), 0)) for b2 in ("high", "medium", "low", "parse_fail")]
        md.append(f"| {b1} | " + " | ".join(cells) + " |")
    md.append("\n## Largest disagreements (|P1 - P2| ≥ 2)\n")
    big = sorted([r for r in rows_out if abs(r["p1_minus_p2"]) >= 2],
                 key=lambda r: -abs(r["p1_minus_p2"]))[:10]
    if not big:
        md.append("_(none)_")
    else:
        for r in big:
            md.append(f"\n### row_id={r['row_id']} ({r['horizon_label']}, P1={r['score_p1']} {r['bucket_p1']} / P2={r['score_p2']} {r['bucket_p2']})")
            md.append(f"\n**Headline:** {r['headline']} ({r['publication']}, {r['date']})")
            md.append(f"\n**Quote:** {r['kastner_quotation'][:400]}{'...' if len(r['kastner_quotation']) > 400 else ''}")
            md.append(f"\n- P1 rationale: {r['rationale_p1'][:300]}")
            md.append(f"\n- P2 rationale: {r['rationale_p2'][:300]}")
    OUT_REPORT.write_text("\n".join(md))


# ---------- main ----------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--commit", action="store_true",
                    help="Run API calls. Default is dry-run (calibration-set membership only).")
    ap.add_argument("--limit", type=int, default=0,
                    help="If >0, score at most this many ROWS (each row = 2 API calls). 0 = no limit (up to MAX_API_CALLS).")
    ap.add_argument("--horizon", choices=["SH-3y", "SH-5y", "LH"], default=None,
                    help="If set, restrict calibration set to one horizon bucket.")
    args = ap.parse_args()

    print(f"v1.8.0 calibration A/B harness")
    print(f"Mode: {'COMMIT (API calls)' if args.commit else 'DRY-RUN'}")
    print(f"=" * 70)

    # Load substrate
    csv_rows = load_csv_by_row_id()
    corpus = load_corpus_by_article_id()
    routing = load_routing()
    print(f"CSV rows:           {len(csv_rows):>6}")
    print(f"Corpus articles:    {len(corpus):>6}")
    print(f"Routing tuples:     {routing['routing_tuple_count']:>6}")
    print(f"Summary by label:   {routing['summary_by_label']}")

    # Build calibration set
    cset = build_calibration_set(csv_rows, routing)
    if args.horizon:
        cset = [c for c in cset if c["horizon_label"] == args.horizon]
        print(f"Horizon filter: {args.horizon}")
    horizon_counts = Counter(c["horizon_label"] for c in cset)
    print(f"\nCalibration set size: {len(cset)} (rows scorable AND with analyst truth)")
    print(f"  by horizon:  {dict(horizon_counts)}")

    # Resume
    already = load_already_scored()
    print(f"Already scored (resume): {len(already)} (row_id, pipeline) pairs in JSONL")

    todo = []
    for cs in cset:
        rid = cs["row_id"]
        if (rid, "P1") not in already:
            todo.append(("P1", cs))
        if (rid, "P2") not in already:
            todo.append(("P2", cs))
    print(f"To-do API calls: {len(todo)} ({len(todo) // 2} rows × 2 pipelines, minus resumed)")

    if args.limit and args.limit > 0:
        # limit by ROWS, not calls; one row needs both P1 and P2
        limited_rids = set()
        limited = []
        for pipeline, cs in todo:
            if len(limited_rids) >= args.limit and cs["row_id"] not in limited_rids:
                continue
            limited.append((pipeline, cs))
            limited_rids.add(cs["row_id"])
        todo = limited
        print(f"After --limit {args.limit}: {len(todo)} calls ({len(limited_rids)} rows)")

    if len(todo) > MAX_API_CALLS:
        print(f"\nFATAL: {len(todo)} planned calls exceeds MAX_API_CALLS={MAX_API_CALLS} cost cap.")
        print(f"  Use --limit or raise MAX_API_CALLS deliberately.")
        return 1

    est_cost = len(todo) * 0.05
    print(f"\nEstimated cost: ${est_cost:.2f} ({len(todo)} calls @ ~$0.05)")

    if not args.commit:
        # Preview a few rows
        print(f"\nDRY-RUN preview (first 3 to-do calls):")
        for pipeline, cs in todo[:3]:
            row = csv_rows[cs["row_id"]]
            print(f"  row_id={cs['row_id']:>5} {pipeline} {cs['horizon_label']} | {row['headline'][:60]}")
        print(f"\nPass --commit to run the API calls.")
        return 0

    # Commit path: load API key, iterate, append JSONL
    api_key = load_api_key()
    print(f"\nAPI key loaded. Starting {len(todo)} calls...")
    print(f"Append-only JSONL: {OUT_JSONL}\n")

    completed_records = []
    # Pre-load existing JSONL into completed_records for the final report
    if OUT_JSONL.exists():
        for line in OUT_JSONL.read_text().splitlines():
            line = line.strip()
            if line:
                try:
                    completed_records.append(json.loads(line))
                except Exception:
                    pass

    for i, (pipeline, cs) in enumerate(todo, 1):
        rid = cs["row_id"]
        row = csv_rows[rid]
        article = corpus.get(cs["article_id"])
        body = (article or {}).get("body", "") if pipeline == "P1" else ""
        template = USER_TEMPLATE_P1 if pipeline == "P1" else USER_TEMPLATE_P2
        prompt = template.format(
            row_id=rid,
            publication=row.get("publication", ""),
            date=row.get("date", ""),
            headline=row.get("headline", ""),
            horizon_label=cs["horizon_label"],
            horizon_int=cs["horizon_int"],
            quote=row.get("kastner_quotation", ""),
            immediate_context=row.get("immediate_context", ""),
            article_body=body[:30000] if pipeline == "P1" else "",  # safety cap
        )
        t0 = time.monotonic()
        rec = score_call(api_key, rid, pipeline, prompt)
        rec["horizon_label"] = cs["horizon_label"]
        rec["article_id"] = cs["article_id"]
        rec["model"] = MODEL
        rec["ts"] = dt.datetime.utcnow().isoformat() + "Z"
        append_jsonl(rec)
        completed_records.append(rec)
        bucket = rule_a_bucket(rec["prescience_score"]) if rec["parse_ok"] == "true" else "FAIL"
        print(f"  [{i:>3}/{len(todo)}] row={rid:>5} {pipeline} {cs['horizon_label']:>5} → score={rec['prescience_score']:>2} {bucket:>10} conf={rec['confidence']} ({rec['elapsed_sec']}s)")
        # Pace: don't hammer
        time.sleep(0.5)

    print(f"\nWriting report + CSV ...")
    write_report(completed_records, csv_rows, cset)
    print(f"  wrote {OUT_CSV} ({OUT_CSV.stat().st_size:,} bytes)")
    print(f"  wrote {OUT_REPORT} ({OUT_REPORT.stat().st_size:,} bytes)")
    print(f"  appended {OUT_JSONL} ({OUT_JSONL.stat().st_size:,} bytes)")
    print(f"\nDone. Open the report:")
    print(f"  open {OUT_REPORT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
