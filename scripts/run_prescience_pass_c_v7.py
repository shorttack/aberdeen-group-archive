#!/usr/bin/env python3
"""
Pass C Cloud Prescience Scoring — v7

Successor to v6. ONLY change vs v6: repoint MASTERS from the retired
`~/Desktop/Archive/archive_masters/` directory to the live masters location
`~/Desktop/Archive/aberdeen-group-archive/` (masters moved to repo root
2026-06-24). SCORER_VERSION bumped v6 -> v7. All scope/resume/prompt logic
is byte-identical to v6.

--- v6 changes (carried forward) ---
Successor to v5. Key changes:
  • Scope expanded from 492 "prepared" studies to ALL unscored observations
    across the master_observations file (or arbitrary --input-manifest CSV).
  • Resume now reads the canonical master (_master_prescience_scores.csv) PLUS
    optional secondary output CSV, AND skips preseed_b rows.
  • Skips observations whose parent study has prescience='not-applicable' per
    _master_studies.csv (saves API calls on out-of-scope studies).
  • CSV headers match _master_prescience_scores.csv (11 columns) directly.
  • Writes source_pass='pass_c_sonar_v1' on every API-scored row.
  • Writes source_pass='pass_c_prefilter_v1' on rule-based skips.
  • --input-manifest <file.csv> lets you score an arbitrary subset
    (calibration sample, Tier A batch, Tier B batch, etc.) without
    touching the full master loop.
  • --output <file.csv> separates per-batch output from the master.
    Merge is a separate step.

Versioning history:
  v1=local Qwen attempts; v2=κ=0.853 cloud baseline; v3=multi-model calibration;
  v4=local 27b-mlx production (failed); v4.1/v4.2=35b-mlx test (failed);
  v5=first cloud production runner (492 prepared studies); v6=expanded scope
  + master-aware resume; v7=MASTERS path fix (archive_masters retired ->
  aberdeen-group-archive repo root).

Usage:
  # Calibration: 100 obs
  python3 run_prescience_pass_c_v6.py \\
    --input-manifest /Users/scott/Desktop/Archive/prescience_calibration_sample_v1.csv \\
    --output /Users/scott/Desktop/Archive/pass_c_v6_calibration_results.csv \\
    --limit 10  # dry cost probe first
  
  # Full unscored sweep against master
  python3 run_prescience_pass_c_v6.py \\
    --output /Users/scott/Desktop/Archive/pass_c_v6_tier_a.csv \\
    --limit 5000
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
MASTERS = ARCH / "aberdeen-group-archive"
LOGS = ARCH / "logs"

MASTER_OBS = MASTERS / "_master_observations.csv"
MASTER_STUDIES = MASTERS / "_master_studies.csv"
MASTER_PRESCIENCE = MASTERS / "_master_prescience_scores.csv"

API_URL = "https://api.perplexity.ai/chat/completions"
MODEL = "sonar-reasoning-pro"
MODEL_TAG = "sonar-reasoning-pro"
SCORER_VERSION = "v7"
SOURCE_PASS_API = "pass_c_sonar_v1"
SOURCE_PASS_PREFILTER = "pass_c_prefilter_v1"

REQUEST_TIMEOUT = 60
SLEEP_BETWEEN = 0.3
MAX_RETRIES = 3
RETRY_BACKOFF = 3.0

# Output schema matches _master_prescience_scores.csv exactly
CSV_FIELDS = [
    "obs_id", "study_id", "model", "prescience_score", "confidence",
    "rationale", "scored_at", "scorer_version", "source_pass",
    "elapsed_sec", "parse_ok",
]

# ---- Pre-filter (unchanged from v5) -----------------------------------------

PICTURE_RE = re.compile(r"==>\s*picture\s*\[.*?\]\s*intentionally omitted\s*<==", re.IGNORECASE)
FIGURE_ONLY_RE = re.compile(r"^\s*\*\*?Figure\s+\d+[:\.]?[^*]*\*\*?\s*$", re.IGNORECASE)
JUNENEWS_STUDY = "junenews-fc15cc"


def classify_prefilter(row: dict) -> tuple[bool, str]:
    mv = (row.get("metric_value") or "").strip()
    study_id = row.get("study_id") or ""
    if study_id == JUNENEWS_STUDY:
        return True, "Pre-filter: junenews-fc15cc study excluded per operator rule."
    if PICTURE_RE.search(mv):
        return True, "Pre-filter: image content preserved in archive images, no textual claim to score."
    if FIGURE_ONLY_RE.match(mv):
        return True, "Pre-filter: figure caption only."
    if "----- Start of picture text -----" in mv:
        return True, "Pre-filter: picture-text dump, image content preserved separately."
    return False, ""

# ---- Prompt (verbatim from v5 — DO NOT MODIFY) ------------------------------

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

# ---- API call (unchanged from v5) -------------------------------------------

def load_api_key() -> str:
    for candidate in [
        Path.home() / ".config" / "adoptex" / "perplexity.env",
        Path("/tmp/perplexity.env"),
    ]:
        if candidate.exists():
            for line in candidate.read_text().splitlines():
                if line.startswith("PERPLEXITY_API_KEY="):
                    return line.split("=", 1)[1].strip()
    raise RuntimeError("PERPLEXITY_API_KEY not found")


def score_obs(api_key: str, row: dict, study_title: str) -> dict:
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(row, study_title)},
        ],
        "max_tokens": 1200,
        "temperature": 0.1,
    }
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
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
            content = re.sub(r"<think>.*?</think>\s*", "", content, flags=re.DOTALL)
            content = content.strip()
            if content.startswith("```"):
                content = re.sub(r"^```[a-zA-Z]*\n", "", content)
                content = re.sub(r"\n```\s*$", "", content)
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

def load_master_obs(path: Path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def load_study_meta():
    """Returns {study_id: {title, prescience}}."""
    out = {}
    if not MASTER_STUDIES.exists():
        return out
    with open(MASTER_STUDIES, newline="") as f:
        for row in csv.DictReader(f):
            sid = row.get("study_id") or row.get("id")
            if sid:
                out[sid] = {
                    "title": row.get("title", ""),
                    "prescience": row.get("prescience", ""),
                }
    return out


def load_already_scored(master_csv: Path, secondary_csv: Path = None) -> set:
    """Read obs_ids from canonical master + any secondary output. Skip preseed_b too
    so we don't redundantly call the API for those."""
    done = set()
    for p in [master_csv, secondary_csv]:
        if p and p.exists():
            with open(p, newline="") as f:
                for r in csv.DictReader(f):
                    # Skip if has a numeric score OR is preseed_b OR is prefiltered
                    if r.get("prescience_score") or r.get("source_pass") in ("preseed_b", SOURCE_PASS_PREFILTER):
                        done.add(r["obs_id"])
    return done


def append_csv_row(path: Path, row_out: dict):
    write_header = not path.exists() or path.stat().st_size == 0
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS, quoting=csv.QUOTE_ALL)
        if write_header:
            w.writeheader()
        w.writerow(row_out)


def append_jsonl(path: Path, obj: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(obj) + "\n")

# ---- Main -------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-manifest", type=str, default=None,
                    help="CSV of obs rows to score (defaults to all unscored from master_obs)")
    ap.add_argument("--output", type=str, required=True,
                    help="Output CSV path (per-batch, NOT the master)")
    ap.add_argument("--dry-run", action="store_true", help="Count work, no API calls")
    ap.add_argument("--limit", type=int, default=0, help="Stop after N API calls")
    ap.add_argument("--skip-not-applicable", action="store_true", default=True,
                    help="Skip obs whose study has prescience='not-applicable'")
    args = ap.parse_args()

    LOGS.mkdir(parents=True, exist_ok=True)
    output_csv = Path(args.output)
    checkpoint = LOGS / f"{output_csv.stem}_checkpoint.jsonl"
    prefilter_log = LOGS / f"{output_csv.stem}_prefiltered.jsonl"
    failure_log = LOGS / f"{output_csv.stem}_failures.jsonl"
    report = LOGS / f"{output_csv.stem}_report.md"

    api_key = load_api_key()
    print(f"[setup] api key loaded ({len(api_key)} chars)")
    print(f"[setup] model: {MODEL}")
    print(f"[setup] output: {output_csv}")

    # Input scope
    if args.input_manifest:
        rows = load_master_obs(Path(args.input_manifest))
        print(f"[scope] input manifest: {len(rows)} rows from {args.input_manifest}")
    else:
        rows = load_master_obs(MASTER_OBS)
        print(f"[scope] master_obs: {len(rows)} rows")

    study_meta = load_study_meta()
    print(f"[setup] studies meta loaded: {len(study_meta)}")

    # Filter not-applicable studies
    if args.skip_not_applicable:
        before = len(rows)
        rows = [r for r in rows
                if study_meta.get(r["study_id"], {}).get("prescience") not in
                ("not-applicable", "n/a", "na")]
        print(f"[scope] after not-applicable filter: {len(rows)} (excluded {before - len(rows)})")

    # Resume: skip already-scored from master AND this batch's output
    already = load_already_scored(MASTER_PRESCIENCE, output_csv)
    print(f"[scope] already-scored/preseed/prefiltered: {len(already)}")

    todo = [r for r in rows if r["obs_id"] not in already]
    print(f"[scope] todo: {len(todo)}")

    # Prefilter
    prefilter_rows, api_rows = [], []
    for r in todo:
        is_pre, reason = classify_prefilter(r)
        if is_pre:
            prefilter_rows.append((r, reason))
        else:
            api_rows.append(r)
    print(f"[scope] prefilter (free): {len(prefilter_rows)}")
    print(f"[scope] requires API: {len(api_rows)}")

    if args.dry_run:
        print("[dry-run] exiting before API calls")
        return

    if args.limit:
        api_rows = api_rows[:args.limit]
        print(f"[limit] capped to {args.limit} API calls")

    now_utc = lambda: dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # 1. Prefilter
    print(f"[prefilter] writing {len(prefilter_rows)} rows...")
    for r, reason in prefilter_rows:
        append_csv_row(output_csv, {
            "obs_id": r["obs_id"],
            "study_id": r["study_id"],
            "model": MODEL_TAG,
            "prescience_score": "-1",
            "confidence": "1",
            "rationale": reason,
            "scored_at": now_utc(),
            "scorer_version": SCORER_VERSION,
            "source_pass": SOURCE_PASS_PREFILTER,
            "elapsed_sec": "0.0",
            "parse_ok": "true",
        })
        append_jsonl(prefilter_log, {"obs_id": r["obs_id"], "reason": reason})
    print(f"[prefilter] done")

    # 2. API rows
    print(f"[api] starting {len(api_rows)} calls...")
    t_start = time.monotonic()
    for i, r in enumerate(api_rows, 1):
        study_title = study_meta.get(r["study_id"], {}).get("title") or r["study_id"]
        result = score_obs(api_key, r, study_title)
        append_csv_row(output_csv, {
            "obs_id": r["obs_id"],
            "study_id": r["study_id"],
            "model": MODEL_TAG,
            "prescience_score": str(result["prescience_score"]),
            "confidence": str(result["confidence"]),
            "rationale": result["rationale"],
            "scored_at": now_utc(),
            "scorer_version": SCORER_VERSION,
            "source_pass": SOURCE_PASS_API,
            "elapsed_sec": result["elapsed_sec"],
            "parse_ok": result["parse_ok"],
        })
        append_jsonl(checkpoint, {
            "obs_id": r["obs_id"], "score": result["prescience_score"],
            "confidence": result["confidence"], "parse_ok": result["parse_ok"],
            "elapsed_sec": result["elapsed_sec"],
        })
        if result["parse_ok"] == "false":
            append_jsonl(failure_log, {
                "obs_id": r["obs_id"], "rationale": result["rationale"],
                "raw": result["raw_response"][:1000],
            })
        if i % 25 == 0:
            elapsed_min = (time.monotonic() - t_start) / 60
            rate = i / elapsed_min if elapsed_min > 0 else 0
            remaining = (len(api_rows) - i) / rate if rate > 0 else 0
            print(f"[api] {i}/{len(api_rows)} | {elapsed_min:.1f}m | {rate:.1f}/min | ~{remaining:.0f}m left")
        time.sleep(SLEEP_BETWEEN)

    total_min = (time.monotonic() - t_start) / 60
    print(f"[done] {len(api_rows)} API calls in {total_min:.1f}m")
    with open(report, "w") as f:
        f.write(f"# Pass C v6 Run Report\n\n")
        f.write(f"Completed: {dt.datetime.now(dt.timezone.utc).isoformat()}\n\n")
        f.write(f"- Prefilter: {len(prefilter_rows)}\n")
        f.write(f"- API: {len(api_rows)}\n")
        f.write(f"- Wall: {total_min:.1f}m\n")
        f.write(f"- Model: {MODEL}\n")
        f.write(f"- Output: {output_csv}\n")
    print(f"[report] {report}")


if __name__ == "__main__":
    main()
