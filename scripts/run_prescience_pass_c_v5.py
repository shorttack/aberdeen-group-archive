#!/usr/bin/env python3
"""
Pass C Cloud Prescience Scoring — v5

Scores 3,661 observations from 492 prepared studies using the Perplexity API
(Sonnet-class model) for prescience (0-5) and confidence (1-3).

Versioning: v1=local Qwen attempts, v2=κ=0.853 cloud baseline, v3=multi-model
calibration, v4=local 27b-mlx production attempt (failed), v4.1/v4.2=35b-mlx
test (failed). v5 = first true production cloud runner using Perplexity API.

Inputs:
  ~/.config/adoptex/perplexity.env  OR  /tmp/perplexity.env  (PERPLEXITY_API_KEY=...)
  ~/Desktop/Archive/archive_masters/_master_observations.csv  (master truth)
  ~/Desktop/Archive/prepared/                                 (492 prepared studies)
  ~/Desktop/Archive/prescience_scores_pass_c_cloud_v1.csv     (100 pilot rows, existing)

Outputs:
  ~/Desktop/Archive/prescience_scores_pass_c_cloud_v1.csv     (extended, 3,761 total)
  ~/Desktop/Archive/logs/pass_c_cloud_v1_checkpoint.jsonl     (per-obs append log)
  ~/Desktop/Archive/logs/pass_c_cloud_v1_prefiltered.jsonl    (rule-based skips audit)
  ~/Desktop/Archive/logs/pass_c_cloud_v1_failures.jsonl       (parse failures)
  ~/Desktop/Archive/logs/pass_c_cloud_v1_run_report.md        (final summary)

Pre-filter rules (no API call needed):
  R1: metric_value contains "==> picture [" and "intentionally omitted <==" → score=-1
  R2: metric_value is purely a figure caption like "**Figure N: ...**"      → score=-1
  R3: study_id == "junenews-fc15cc"                                          → score=-1
  R4: metric_value is the study-summary template containing "==> picture"   → score=-1

Resume:
  If output CSV exists, the script reads all obs_ids already scored and skips them.

Usage:
  python3 ~/Desktop/Archive/scripts/run_prescience_pass_c_v5.py
  python3 ~/Desktop/Archive/scripts/run_prescience_pass_c_v5.py --dry-run
  python3 ~/Desktop/Archive/scripts/run_prescience_pass_c_v5.py --limit 10
"""

import argparse
import csv
import datetime as dt
import json
import os
import re
import sys
import time
from pathlib import Path

# stdlib + certifi for SSL cert verification on macOS Python
import ssl
import urllib.request
import urllib.error
try:
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    SSL_CTX = ssl.create_default_context()

# ---- Configuration ----------------------------------------------------------

ARCH = Path.home() / "Desktop" / "Archive"
MASTERS = ARCH / "archive_masters"
PREPARED = ARCH / "prepared"
LOGS = ARCH / "logs"
SCRIPTS = ARCH / "scripts"

PILOT_CSV = ARCH / "prescience_scores_pass_c_cloud_v1.csv"
OUTPUT_CSV = ARCH / "prescience_scores_pass_c_cloud_v1.csv"  # same file — we extend it
CHECKPOINT = LOGS / "pass_c_cloud_v1_checkpoint.jsonl"
PREFILTER_LOG = LOGS / "pass_c_cloud_v1_prefiltered.jsonl"
FAILURE_LOG = LOGS / "pass_c_cloud_v1_failures.jsonl"
REPORT = LOGS / "pass_c_cloud_v1_run_report.md"

# Perplexity API — sonar-reasoning-pro for historical reasoning quality
API_URL = "https://api.perplexity.ai/chat/completions"
MODEL = "sonar-reasoning-pro"
MODEL_TAG = "sonar-reasoning-pro"  # honest model name in CSV (was 'claude-sonnet-4.6' in pilot)

# Pacing
REQUEST_TIMEOUT = 60
SLEEP_BETWEEN = 0.3   # seconds between API calls
MAX_RETRIES = 3
RETRY_BACKOFF = 3.0   # seconds, doubles per retry

CSV_FIELDS = [
    "obs_id", "prescience_score", "confidence", "rationale",
    "model", "scored_at", "elapsed_sec", "parse_ok",
]


# ---- Pre-filter -------------------------------------------------------------

PICTURE_RE = re.compile(r"==>\s*picture\s*\[.*?\]\s*intentionally omitted\s*<==", re.IGNORECASE)
FIGURE_ONLY_RE = re.compile(r"^\s*\*\*?Figure\s+\d+[:\.]?[^*]*\*\*?\s*$", re.IGNORECASE)
JUNENEWS_STUDY = "junenews-fc15cc"


def classify_prefilter(row: dict) -> tuple[bool, str]:
    """Return (is_prefiltered, reason) without making an API call."""
    mv = (row.get("metric_value") or "").strip()
    study_id = row.get("study_id") or ""

    if study_id == JUNENEWS_STUDY:
        return True, "Pre-filter: junenews-fc15cc study excluded per operator rule."
    if PICTURE_RE.search(mv):
        return True, "Pre-filter: image content preserved in archive images, no textual claim to score."
    if FIGURE_ONLY_RE.match(mv):
        return True, "Pre-filter: figure caption only."
    # Picture-text dumps that wrap chart content
    if "----- Start of picture text -----" in mv:
        return True, "Pre-filter: picture-text dump, image content preserved separately."
    return False, ""


# ---- Prompt -----------------------------------------------------------------

SYSTEM_PROMPT = """You are a technology industry historian specializing in enterprise IT trends from 1998-2026. You assess historical industry-analyst claims for prescience: did the claim's prediction or characterization hold up over time?

You read one Aberdeen Group observation at a time. You return a strict JSON object — nothing else. No prose before or after. No markdown fences. No commentary.

Your assessment must be grounded in widely-documented technology history. If you genuinely don't know what happened, score conservatively and say so in the rationale."""

USER_TEMPLATE = """Score this Aberdeen Group observation for prescience.

Study: {study_title}
Published: {publication_year}
Observation ID: {obs_id}
Observation type: {observation_type}
Section: {section}
Claim:

{metric_value}

---

Scoring rubric (0-5):
- 5 = Remarkably prescient. The specific prediction or pattern played out essentially as stated; widely confirmed by 2010-2026.
- 4 = Largely prescient. Direction correct; magnitudes or timing somewhat off.
- 3 = Partially right. Some elements held up, others didn't, or the claim was mixed.
- 2 = Mostly wrong. The trend went a different direction than implied.
- 1 = Wrong. The claim was contradicted by what actually happened.
- 0 = Cannot assess. The claim is too vague, too narrow, or you lack reliable knowledge to judge.

Confidence (1-3) in YOUR assessment:
- 3 = High — this is well-documented industry history I know well.
- 2 = Medium — I have reasonable evidence but could be missing nuance.
- 1 = Low — limited knowledge of this specific subdomain.

Return exactly this JSON object — no other text:

{{
  "obs_id": "{obs_id}",
  "prescience_score": <0-5 integer>,
  "confidence": <1-3 integer>,
  "rationale": "<2-3 sentences citing what actually happened from publication through 2026. Reference specific developments, adoption rates, or technologies by name.>"
}}"""


def build_user_prompt(row: dict, study_title: str) -> str:
    return USER_TEMPLATE.format(
        study_title=study_title or row.get("study_id", ""),
        publication_year=row.get("year_observed") or "unknown",
        obs_id=row["obs_id"],
        observation_type=row.get("observation_type") or "unspecified",
        section=row.get("section") or row.get("source_page") or "unspecified",
        metric_value=row.get("metric_value") or "",
    )


# ---- API call ---------------------------------------------------------------

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
        "PERPLEXITY_API_KEY not found in ~/.config/adoptex/perplexity.env or /tmp/perplexity.env"
    )


def score_obs(api_key: str, row: dict, study_title: str) -> dict:
    """Call API once, parse JSON response. Return dict with score/confidence/rationale/parse_ok."""
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(row, study_title)},
        ],
        "max_tokens": 1200,  # reasoning models emit <think> block before answer; need headroom
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
            # Reasoning models emit <think>...</think> before the answer — strip it
            content = re.sub(r"<think>.*?</think>\s*", "", content, flags=re.DOTALL)
            content = content.strip()
            # Strip markdown fences if any
            if content.startswith("```"):
                content = re.sub(r"^```[a-zA-Z]*\n", "", content)
                content = re.sub(r"\n```\s*$", "", content)
            # Last-resort: extract first JSON object from content if model added prose
            if not content.startswith("{"):
                m = re.search(r"\{[^{}]*\"prescience_score\"[^{}]*\}", content, flags=re.DOTALL)
                if m:
                    content = m.group(0)
            parsed = json.loads(content)
            return {
                "prescience_score": int(parsed["prescience_score"]),
                "confidence": int(parsed["confidence"]),
                "rationale": str(parsed["rationale"]),
                "elapsed_sec": f"{elapsed:.2f}",
                "parse_ok": "true",
                "raw_response": content,
            }
        except (urllib.error.HTTPError, urllib.error.URLError, json.JSONDecodeError, KeyError, ValueError) as e:
            last_err = e
            if attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_BACKOFF * (2 ** attempt))

    elapsed = time.monotonic() - start
    return {
        "prescience_score": -1,
        "confidence": 1,
        "rationale": f"Parse failed after {MAX_RETRIES} retries: {type(last_err).__name__}: {str(last_err)[:200]}",
        "elapsed_sec": f"{elapsed:.2f}",
        "parse_ok": "false",
        "raw_response": "",
    }


# ---- I/O --------------------------------------------------------------------

def load_master_obs():
    rows = []
    with open(MASTERS / "_master_observations.csv", newline="") as f:
        rdr = csv.DictReader(f)
        for row in rdr:
            rows.append(row)
    return rows


def load_master_studies_titles():
    """Best-effort: load study titles from _master_studies.csv (assumes 'title' column)."""
    titles = {}
    path = MASTERS / "_master_studies.csv"
    if not path.exists():
        return titles
    with open(path, newline="") as f:
        rdr = csv.DictReader(f)
        for row in rdr:
            sid = row.get("study_id") or row.get("id")
            ttl = row.get("title") or ""
            if sid:
                titles[sid] = ttl
    return titles


def load_already_scored() -> set:
    """Read obs_ids already in the output CSV (pilot + any prior partial run)."""
    if not OUTPUT_CSV.exists():
        return set()
    done = set()
    with open(OUTPUT_CSV, newline="") as f:
        rdr = csv.DictReader(f)
        for row in rdr:
            done.add(row["obs_id"])
    return done


def append_csv_row(row_out: dict):
    write_header = not OUTPUT_CSV.exists() or OUTPUT_CSV.stat().st_size == 0
    with open(OUTPUT_CSV, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS, quoting=csv.QUOTE_ALL)
        if write_header:
            w.writeheader()
        w.writerow(row_out)


def append_jsonl(path: Path, obj: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(obj) + "\n")


# ---- Main loop --------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="Apply prefilter, count work, don't call API")
    ap.add_argument("--limit", type=int, default=0, help="Stop after N API calls (for cost probing)")
    args = ap.parse_args()

    LOGS.mkdir(parents=True, exist_ok=True)

    api_key = load_api_key()
    print(f"[setup] api key loaded ({len(api_key)} chars)")

    print("[setup] loading master observations...")
    master = load_master_obs()
    print(f"[setup] master_obs rows: {len(master)}")

    prepared = set(os.listdir(PREPARED)) if PREPARED.exists() else set()
    print(f"[setup] prepared studies on disk: {len(prepared)}")

    titles = load_master_studies_titles()
    print(f"[setup] study titles loaded: {len(titles)}")

    # Work scope: obs in prepared studies
    in_scope = [r for r in master if r["study_id"] in prepared]
    print(f"[scope] obs in 492 prepared studies: {len(in_scope)}")

    already = load_already_scored()
    print(f"[scope] obs already scored (pilot + resume): {len(already)}")

    todo = [r for r in in_scope if r["obs_id"] not in already]
    print(f"[scope] obs to process this run: {len(todo)}")

    # Split into prefilter vs API
    prefilter_rows, api_rows = [], []
    for r in todo:
        is_pre, reason = classify_prefilter(r)
        if is_pre:
            prefilter_rows.append((r, reason))
        else:
            api_rows.append(r)
    print(f"[scope] prefilter (no API call): {len(prefilter_rows)}")
    print(f"[scope] requires API call:       {len(api_rows)}")

    if args.dry_run:
        print("[dry-run] exiting before any API calls")
        return

    if args.limit:
        api_rows = api_rows[:args.limit]
        print(f"[limit] capped to first {args.limit} API calls")

    now_utc = lambda: dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # 1. Write all prefilter rows first (fast, free)
    print(f"[prefilter] writing {len(prefilter_rows)} prefilter rows...")
    for r, reason in prefilter_rows:
        out = {
            "obs_id": r["obs_id"],
            "prescience_score": "-1",
            "confidence": "1",
            "rationale": reason,
            "model": MODEL_TAG,
            "scored_at": now_utc(),
            "elapsed_sec": "0.0",
            "parse_ok": "true",
        }
        append_csv_row(out)
        append_jsonl(PREFILTER_LOG, {"obs_id": r["obs_id"], "reason": reason})
    print(f"[prefilter] done")

    # 2. Process API rows
    print(f"[api] starting {len(api_rows)} API calls...")
    t_start = time.monotonic()
    for i, r in enumerate(api_rows, 1):
        study_title = titles.get(r["study_id"]) or r["study_id"]
        result = score_obs(api_key, r, study_title)

        out = {
            "obs_id": r["obs_id"],
            "prescience_score": str(result["prescience_score"]),
            "confidence": str(result["confidence"]),
            "rationale": result["rationale"],
            "model": MODEL_TAG,
            "scored_at": now_utc(),
            "elapsed_sec": result["elapsed_sec"],
            "parse_ok": result["parse_ok"],
        }
        append_csv_row(out)
        append_jsonl(CHECKPOINT, {
            "obs_id": r["obs_id"],
            "score": result["prescience_score"],
            "confidence": result["confidence"],
            "parse_ok": result["parse_ok"],
            "elapsed_sec": result["elapsed_sec"],
        })
        if result["parse_ok"] == "false":
            append_jsonl(FAILURE_LOG, {
                "obs_id": r["obs_id"],
                "rationale": result["rationale"],
                "raw": result["raw_response"][:1000],
            })

        # Progress every 25
        if i % 25 == 0:
            elapsed_min = (time.monotonic() - t_start) / 60
            rate = i / elapsed_min if elapsed_min > 0 else 0
            remaining = (len(api_rows) - i) / rate if rate > 0 else 0
            print(f"[api] {i}/{len(api_rows)} | {elapsed_min:.1f}m elapsed | {rate:.1f}/min | ~{remaining:.0f}m remaining")

        time.sleep(SLEEP_BETWEEN)

    total_min = (time.monotonic() - t_start) / 60
    print(f"[done] {len(api_rows)} API calls in {total_min:.1f} min")
    write_report(prefilter_rows, api_rows, total_min)


def write_report(prefilter_rows, api_rows, total_min):
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT, "w") as f:
        f.write(f"# Pass C Cloud v1 Run Report\n\n")
        f.write(f"Completed: {dt.datetime.now(dt.timezone.utc).isoformat()}\n\n")
        f.write(f"- Prefilter rows: {len(prefilter_rows)}\n")
        f.write(f"- API rows: {len(api_rows)}\n")
        f.write(f"- Wall time: {total_min:.1f} min\n")
        f.write(f"- Model: {MODEL} (tagged as {MODEL_TAG} in CSV)\n")
    print(f"[report] wrote {REPORT}")


if __name__ == "__main__":
    main()
