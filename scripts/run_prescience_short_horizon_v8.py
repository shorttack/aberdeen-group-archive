#!/usr/bin/env python3
"""
Short-Horizon Prescience Driver — v8

Successor to v7 (run_prescience_pass_c_v7.py). Adds short-horizon (3y + 5y)
prescience scoring per the v3 spec locked 2026-06-15.

Companion docs (workspace):
  - decisions_log_entry_2026_06_15_short_horizon_prescience_v3.md  (SPEC v3)
  - anchor_year_resolver_v2.py                                     (resolver module)
  - short_horizon_prompt_v1.md                                     (prompt design)
  - driver_v8_spec_v1.md                                           (this file's spec)
  - short_horizon_acceptance_gates_v2_spec.md                      (G1-G10)

Key v8 behaviors:
  • Pre-API anchor resolution + window-elapsed short-circuit (no API for pending)
  • Single combined API call per obs → 6 score fields + windows_diverge + note
  • Variant 3y-only prompt for anchor in [today_year-5, today_year-4] (3y elapsed,
    5y still pending). Today (2026): anchors 2021-2022.
  • 14 new output columns (SH-prefixed timestamps + provenance)
  • Inherits v7 network hardening: REQUEST_TIMEOUT=120, MAX_RETRIES=5, full
    exception tuple, exponential backoff
  • Resume-on-restart via --resume (reads existing output, skips obs_id seen)
  • TODAY_YEAR is a constant (not datetime.now().year) for run-stability across
    day boundaries — bump manually each scoring cycle

Score scale (SH columns):
  -2 = window not elapsed (pending; no API call)
  -1 = pre-filter / no_anchor / parse_fail
   0 = wrong
   1..5 = scaled prescient

Usage:
  # Smoke test (10-row fixture covering all 4 paths)
  python3 run_prescience_short_horizon_v8.py \
    --input  smoke_fixture_v1.csv \
    --studies _master_studies.csv \
    --output smoke_v8_results.csv \
    --limit 10

  # Calibration (100-obs stratified sample, anchor ≤ 2020)
  python3 run_prescience_short_horizon_v8.py \
    --input  sh_calibration_sample_v1.csv \
    --studies _master_studies.csv \
    --output sh_calibration_results.csv \
    --resume

  # Full sweep (after GO/NO-GO)
  python3 run_prescience_short_horizon_v8.py \
    --input  _master_observations.csv \
    --studies _master_studies.csv \
    --output sh_full_sweep_results.csv \
    --resume
"""

from __future__ import annotations

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

# anchor_year_resolver_v2 must be importable from the run directory.
# v2 aligns field names to actual master schemas:
#   obs.year_observed  (not obs_date)
#   study.date         (not published_at)
# Backward-compat fallbacks preserved for enriched calibration CSVs.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from anchor_year_resolver_v2 import (
    AnchorResolutionError,
    resolve_anchor_year,
    window_bounds,
    is_window_elapsed,
    cutoff_year,
    pending_rationale,
)

# ---- Configuration ----------------------------------------------------------

ARCH = Path.home() / "Desktop" / "Archive"
LOGS = ARCH / "logs"

API_URL = "https://api.perplexity.ai/chat/completions"

TODAY_YEAR        = 2026                       # EXPLICIT constant; bump manually
MODEL             = "sonar-pro"                # v3 confirmed (Pete: no downgrade)
MODEL_TAG         = "sonar-pro"
SCORER_VERSION    = "pass_c_sonar_sh_v1"
SCORER_PARSE_FAIL = "pass_c_sonar_sh_v1_parse_fail"

REQUEST_TIMEOUT   = 120                        # v7 hardening
MAX_RETRIES       = 5                          # v7 hardening
RETRY_BACKOFF     = 3.0
MAX_TOKENS        = 2000                       # combined output budget
TEMPERATURE       = 0.0                        # deterministic
SLEEP_BETWEEN     = 0.3

# 14 new SH columns, locked in v3 spec
SH_FIELDS = [
    "obs_id", "study_id",
    "prescience_3y", "confidence_3y", "rationale_3y",
    "prescience_5y", "confidence_5y", "rationale_5y",
    "windows_diverge", "divergence_note",
    "anchor_year", "anchor_source",
    "scored_at_sh", "scorer_version_sh", "source_pass_sh",
    "raw_response_sh",
]

# source_pass_sh enum
SP_COMBINED  = "pass_c_sh_combined"
SP_3Y_ONLY   = "pass_c_sh_3y_only"
SP_PENDING   = "pass_c_sh_pending"
SP_NO_ANCHOR = "pass_c_sh_no_anchor"

# ---- Prompts (v1, locked) ---------------------------------------------------

SYSTEM_PROMPT_COMBINED = """You are an expert technology-industry analyst evaluating the prescience of a historical observation against what actually happened in two time windows.

INPUTS
- Observation: a claim, forecast, or assertion made at anchor_year A.
- Anchor year A: the year the observation was made (or, for memoirs, the year the narrated event occurred).
- Two windows to evaluate INDEPENDENTLY:
    * 3-year window: calendar years [A, A+3] inclusive (4 years).
    * 5-year window: calendar years [A, A+5] inclusive (6 years).
- Both windows are fully elapsed; you may rely on facts known as of today.

TASK
For EACH window, return a prescience score on this scale:
   5 — strongly correct, specific, ahead of consensus, low ambiguity
   4 — correct in substance with minor caveats
   3 — partially correct; right direction, wrong magnitude or timing inside window
   2 — weakly correct; some alignment but mostly off
   1 — barely defensible; mostly wrong
   0 — wrong, contradicted by what happened in this window

Then return windows_diverge=true iff the evidence inside [A, A+3] would lead to a materially different score than the evidence inside [A, A+5] (e.g. the forecast was wrong in 3y but vindicated by year 4 or 5). If you set windows_diverge=true, supply a one-sentence divergence_note that names the inflection point.

RULES
- Do NOT output -1 or -2; those are reserved for pipeline use.
- Confidence is an integer in {1, 2, 3} (1=low, 2=medium, 3=high) reflecting evidence quality, not score magnitude.
- Rationale must cite at least one specific event, dataset, or company action inside the relevant window. No generic hedges.
- For the 3y score, use evidence about events in [A, A+3]. For the 5y score, use evidence about events in [A, A+5]. Evidence after A+5 may be in your training data but MUST NOT influence either score. Reason about each window independently, then identify whether they diverge.
- Output strict JSON, no commentary outside the object.

OUTPUT SCHEMA
{
  "prescience_3y":   <int 0..5>,
  "confidence_3y":   <int 1..3>,
  "rationale_3y":    "<<= 280 chars, cite at least one window-bound fact>",
  "prescience_5y":   <int 0..5>,
  "confidence_5y":   <int 1..3>,
  "rationale_5y":    "<<= 280 chars, cite at least one window-bound fact>",
  "windows_diverge": <bool>,
  "divergence_note": "<empty string if windows_diverge=false; else <= 200 chars>"
}"""

SYSTEM_PROMPT_3Y_ONLY = """You are an expert technology-industry analyst evaluating the prescience of a historical observation against what actually happened.

INPUTS
- Observation: a claim, forecast, or assertion made at anchor_year A.
- Anchor year A: the year the observation was made (or, for memoirs, the year the narrated event occurred).
- One window to evaluate:
    * 3-year window: calendar years [A, A+3] inclusive (4 years).
- The 3y window is fully elapsed; the 5y window has not yet elapsed and will be scored later.

TASK
Return a 3-year prescience score on this scale:
   5 — strongly correct, specific, ahead of consensus, low ambiguity
   4 — correct in substance with minor caveats
   3 — partially correct; right direction, wrong magnitude or timing inside window
   2 — weakly correct; some alignment but mostly off
   1 — barely defensible; mostly wrong
   0 — wrong, contradicted by what happened in this window

RULES
- Do NOT output -1 or -2; those are reserved for pipeline use.
- Confidence is an integer in {1, 2, 3} (1=low, 2=medium, 3=high) reflecting evidence quality, not score magnitude.
- Rationale must cite at least one specific event, dataset, or company action inside [A, A+3]. No generic hedges.
- Evidence after A+3 may be in your training data but MUST NOT influence the score.
- Output strict JSON, no commentary outside the object.

OUTPUT SCHEMA
{
  "prescience_3y": <int 0..5>,
  "confidence_3y": <int 1..3>,
  "rationale_3y":  "<<= 280 chars, cite at least one window-bound fact>"
}"""

USER_TEMPLATE_COMBINED = """OBSERVATION (anchor_year=A={anchor_year}, source={anchor_source}):
{obs_text}

CONTEXT
- Study: {study_title} ({study_type}, published {published_at})
- Observation type: {observation_type}
- Section: {section}

WINDOWS TO SCORE
- 3y: [{A}, {A_plus_3}]   inclusive
- 5y: [{A}, {A_plus_5}]   inclusive

Return ONLY the JSON object specified."""

USER_TEMPLATE_3Y_ONLY = """OBSERVATION (anchor_year=A={anchor_year}, source={anchor_source}):
{obs_text}

CONTEXT
- Study: {study_title} ({study_type}, published {published_at})
- Observation type: {observation_type}
- Section: {section}

WINDOW TO SCORE
- 3y: [{A}, {A_plus_3}]   inclusive

(The 5y window is not yet elapsed and will be scored later.)

Return ONLY the JSON object specified."""


def build_user_prompt(row: dict, study_row: dict, anchor_year: int,
                       anchor_source: str, combined: bool) -> str:
    a3 = anchor_year + 3
    a5 = anchor_year + 5
    template = USER_TEMPLATE_COMBINED if combined else USER_TEMPLATE_3Y_ONLY
    # study.date is canonical; study.published_at is legacy fallback for
    # enriched calibration CSVs that pre-renamed the field.
    published_at = (study_row.get("date")
                    or study_row.get("published_at")
                    or "unknown")
    return template.format(
        anchor_year=anchor_year,
        anchor_source=anchor_source,
        A=anchor_year,
        A_plus_3=a3,
        A_plus_5=a5,
        obs_text=row.get("metric_value") or "",
        study_title=study_row.get("title") or row.get("study_id", ""),
        study_type=study_row.get("type") or "unspecified",
        published_at=published_at,
        observation_type=row.get("observation_type") or "unspecified",
        section=row.get("section") or row.get("source_page") or "unspecified",
    )

# ---- API call (v7 network hardening preserved) ------------------------------

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


def _extract_json(content: str) -> str:
    """Strip <think> blocks, code fences, surrounding prose; return JSON substring."""
    content = re.sub(r"<think>.*?</think>\s*", "", content, flags=re.DOTALL).strip()
    if content.startswith("```"):
        content = re.sub(r"^```[a-zA-Z]*\n", "", content)
        content = re.sub(r"\n```\s*$", "", content)
    content = content.strip()
    if not content.startswith("{"):
        m = re.search(r"\{.*\}", content, flags=re.DOTALL)
        if m:
            content = m.group(0)
    return content


def call_sonar(api_key: str, system_prompt: str, user_prompt: str) -> tuple[dict, str, float, str]:
    """Returns (parsed_json_or_empty, raw_response, elapsed_sec, error_or_empty)."""
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt},
        ],
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE,
    }
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )

    start = time.monotonic()
    last_err = None
    raw = ""
    for attempt in range(MAX_RETRIES):
        try:
            with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT, context=SSL_CTX) as resp:
                body = resp.read().decode("utf-8")
            elapsed = time.monotonic() - start
            data = json.loads(body)
            content = data["choices"][0]["message"]["content"].strip()
            raw = content
            content = _extract_json(content)
            parsed = json.loads(content)
            return (parsed, raw, elapsed, "")
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError,
                json.JSONDecodeError, KeyError, ValueError) as e:
            last_err = e
            if attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_BACKOFF * (2 ** attempt))

    elapsed = time.monotonic() - start
    return ({}, raw, elapsed,
            f"{type(last_err).__name__}: {str(last_err)[:200]}")


def _coerce_int(v, default=None):
    try:
        return int(v)
    except (TypeError, ValueError):
        return default


def _coerce_bool(v) -> bool:
    if isinstance(v, bool):
        return v
    if isinstance(v, str):
        return v.strip().lower() in ("true", "1", "yes")
    return False


def validate_combined(parsed: dict) -> tuple[bool, dict]:
    """Schema-validate a combined-call response. Returns (ok, normalized)."""
    if not isinstance(parsed, dict):
        return False, {}
    p3 = _coerce_int(parsed.get("prescience_3y"))
    c3 = _coerce_int(parsed.get("confidence_3y"))
    r3 = parsed.get("rationale_3y")
    p5 = _coerce_int(parsed.get("prescience_5y"))
    c5 = _coerce_int(parsed.get("confidence_5y"))
    r5 = parsed.get("rationale_5y")
    wd = parsed.get("windows_diverge")
    dn = parsed.get("divergence_note", "")
    if any(x is None for x in (p3, c3, p5, c5)):
        return False, {}
    if not (0 <= p3 <= 5 and 0 <= p5 <= 5):
        return False, {}
    if not (1 <= c3 <= 3 and 1 <= c5 <= 3):
        return False, {}
    if not isinstance(r3, str) or not isinstance(r5, str):
        return False, {}
    if wd is None:
        return False, {}
    return True, {
        "prescience_3y": p3, "confidence_3y": c3, "rationale_3y": r3,
        "prescience_5y": p5, "confidence_5y": c5, "rationale_5y": r5,
        "windows_diverge": _coerce_bool(wd),
        "divergence_note": str(dn or ""),
    }


def validate_3y_only(parsed: dict) -> tuple[bool, dict]:
    if not isinstance(parsed, dict):
        return False, {}
    p3 = _coerce_int(parsed.get("prescience_3y"))
    c3 = _coerce_int(parsed.get("confidence_3y"))
    r3 = parsed.get("rationale_3y")
    if p3 is None or c3 is None:
        return False, {}
    if not (0 <= p3 <= 5 and 1 <= c3 <= 3):
        return False, {}
    if not isinstance(r3, str):
        return False, {}
    return True, {
        "prescience_3y": p3, "confidence_3y": c3, "rationale_3y": r3,
    }

# ---- I/O --------------------------------------------------------------------

def load_csv(path: Path) -> list[dict]:
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def load_study_meta(studies_csv: Path) -> dict:
    out = {}
    if not studies_csv.exists():
        return out
    with open(studies_csv, newline="") as f:
        for r in csv.DictReader(f):
            sid = r.get("study_id") or r.get("id")
            if sid:
                out[sid] = r
    return out


def load_already_scored(output_csv: Path) -> set:
    """Resume: skip any obs_id already present in the output."""
    done = set()
    if output_csv.exists() and output_csv.stat().st_size > 0:
        with open(output_csv, newline="") as f:
            for r in csv.DictReader(f):
                oid = r.get("obs_id")
                if oid:
                    done.add(oid)
    return done


def append_csv_row(path: Path, row_out: dict):
    write_header = not path.exists() or path.stat().st_size == 0
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=SH_FIELDS, quoting=csv.QUOTE_ALL)
        if write_header:
            w.writeheader()
        w.writerow(row_out)


def append_jsonl(path: Path, obj: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(obj) + "\n")

# ---- Row builders -----------------------------------------------------------

def _now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _empty_sh_row(obs_id: str, study_id: str) -> dict:
    return {k: "" for k in SH_FIELDS} | {"obs_id": obs_id, "study_id": study_id}


def row_no_anchor(obs_id: str, study_id: str, err: str) -> dict:
    msg = f"no_anchor:{err}"
    row = _empty_sh_row(obs_id, study_id)
    row.update({
        "prescience_3y": "-1", "confidence_3y": "", "rationale_3y": msg,
        "prescience_5y": "-1", "confidence_5y": "", "rationale_5y": msg,
        "windows_diverge": "", "divergence_note": "",
        "anchor_year": "", "anchor_source": "",
        "scored_at_sh": _now_utc(),
        "scorer_version_sh": SCORER_VERSION,
        "source_pass_sh": SP_NO_ANCHOR,
        "raw_response_sh": "",
    })
    return row


def row_both_pending(obs_id: str, study_id: str, anchor_year: int,
                     anchor_source: str) -> dict:
    row = _empty_sh_row(obs_id, study_id)
    row.update({
        "prescience_3y": "-2", "confidence_3y": "",
        "rationale_3y": pending_rationale(3, TODAY_YEAR),
        "prescience_5y": "-2", "confidence_5y": "",
        "rationale_5y": pending_rationale(5, TODAY_YEAR),
        "windows_diverge": "", "divergence_note": "",
        "anchor_year": str(anchor_year), "anchor_source": anchor_source,
        "scored_at_sh": _now_utc(),
        "scorer_version_sh": SCORER_VERSION,
        "source_pass_sh": SP_PENDING,
        "raw_response_sh": "",
    })
    return row


def row_combined_ok(obs_id: str, study_id: str, anchor_year: int,
                    anchor_source: str, norm: dict, raw: str) -> dict:
    row = _empty_sh_row(obs_id, study_id)
    row.update({
        "prescience_3y": str(norm["prescience_3y"]),
        "confidence_3y": str(norm["confidence_3y"]),
        "rationale_3y":  norm["rationale_3y"],
        "prescience_5y": str(norm["prescience_5y"]),
        "confidence_5y": str(norm["confidence_5y"]),
        "rationale_5y":  norm["rationale_5y"],
        "windows_diverge": "true" if norm["windows_diverge"] else "false",
        "divergence_note": norm["divergence_note"],
        "anchor_year": str(anchor_year), "anchor_source": anchor_source,
        "scored_at_sh": _now_utc(),
        "scorer_version_sh": SCORER_VERSION,
        "source_pass_sh": SP_COMBINED,
        "raw_response_sh": raw,
    })
    return row


def row_3y_only_ok(obs_id: str, study_id: str, anchor_year: int,
                   anchor_source: str, norm: dict, raw: str) -> dict:
    row = _empty_sh_row(obs_id, study_id)
    row.update({
        "prescience_3y": str(norm["prescience_3y"]),
        "confidence_3y": str(norm["confidence_3y"]),
        "rationale_3y":  norm["rationale_3y"],
        "prescience_5y": "-2", "confidence_5y": "",
        "rationale_5y": pending_rationale(5, TODAY_YEAR),
        "windows_diverge": "", "divergence_note": "",
        "anchor_year": str(anchor_year), "anchor_source": anchor_source,
        "scored_at_sh": _now_utc(),
        "scorer_version_sh": SCORER_VERSION,
        "source_pass_sh": SP_3Y_ONLY,
        "raw_response_sh": raw,
    })
    return row


def row_parse_fail(obs_id: str, study_id: str, anchor_year: int,
                   anchor_source: str, source_pass: str, raw: str,
                   err: str) -> dict:
    """Tier-A pattern: tag scorer_version with _parse_fail, preserve raw for retry."""
    msg = f"parse_fail:{err}" if err else "parse_fail:schema_mismatch"
    row = _empty_sh_row(obs_id, study_id)
    row.update({
        "prescience_3y": "-1", "confidence_3y": "", "rationale_3y": msg,
        "prescience_5y": "-1", "confidence_5y": "", "rationale_5y": msg,
        "windows_diverge": "", "divergence_note": "",
        "anchor_year": str(anchor_year) if anchor_year else "",
        "anchor_source": anchor_source,
        "scored_at_sh": _now_utc(),
        "scorer_version_sh": SCORER_PARSE_FAIL,
        "source_pass_sh": source_pass,
        "raw_response_sh": raw,
    })
    return row

# ---- Main -------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", type=str, required=True,
                    help="CSV of obs rows to score")
    ap.add_argument("--studies", type=str, required=True,
                    help="_master_studies.csv path")
    ap.add_argument("--output", type=str, required=True,
                    help="Output CSV path (per-batch, NOT the master)")
    ap.add_argument("--resume", action="store_true",
                    help="Skip obs_id already present in --output")
    ap.add_argument("--dry-run", action="store_true",
                    help="Resolve anchors + classify paths; no API calls")
    ap.add_argument("--limit", type=int, default=0,
                    help="Stop after N API calls (path classification still runs)")
    args = ap.parse_args()

    LOGS.mkdir(parents=True, exist_ok=True)
    output_csv = Path(args.output)
    checkpoint    = LOGS / f"{output_csv.stem}_checkpoint.jsonl"
    failure_log   = LOGS / f"{output_csv.stem}_failures.jsonl"
    no_anchor_log = LOGS / f"{output_csv.stem}_no_anchor.jsonl"
    report        = LOGS / f"{output_csv.stem}_report.md"

    print(f"[setup] TODAY_YEAR={TODAY_YEAR}")
    print(f"[setup] cutoffs: 3y anchor≤{cutoff_year(3,TODAY_YEAR)} / "
          f"5y anchor≤{cutoff_year(5,TODAY_YEAR)}")
    print(f"[setup] model: {MODEL}  scorer_version: {SCORER_VERSION}")
    print(f"[setup] output: {output_csv}")

    rows = load_csv(Path(args.input))
    print(f"[scope] input: {len(rows)} rows")

    studies = load_study_meta(Path(args.studies))
    print(f"[setup] studies meta: {len(studies)} entries")

    already = load_already_scored(output_csv) if args.resume else set()
    if args.resume:
        print(f"[resume] already in output: {len(already)}")
        rows = [r for r in rows if r.get("obs_id") not in already]
        print(f"[resume] todo: {len(rows)}")

    # Classify paths (no API calls in this loop)
    path_pending, path_3y_only, path_combined, path_no_anchor = [], [], [], []
    for r in rows:
        obs_id = r.get("obs_id") or ""
        study_id = r.get("study_id") or ""
        study_row = studies.get(study_id, {})
        try:
            anchor = resolve_anchor_year(r, study_row)
        except AnchorResolutionError as e:
            path_no_anchor.append((r, str(e)))
            continue
        e3 = is_window_elapsed(anchor.year, 3, TODAY_YEAR)
        e5 = is_window_elapsed(anchor.year, 5, TODAY_YEAR)
        if not e3 and not e5:
            path_pending.append((r, anchor))
        elif e3 and not e5:
            path_3y_only.append((r, anchor))
        else:
            path_combined.append((r, anchor))

    print(f"[classify] combined (both elapsed): {len(path_combined)}")
    print(f"[classify] 3y_only (5y pending):    {len(path_3y_only)}")
    print(f"[classify] both pending (no API):   {len(path_pending)}")
    print(f"[classify] no_anchor (no API):      {len(path_no_anchor)}")

    if args.dry_run:
        print("[dry-run] exiting before API calls")
        return

    api_key = load_api_key()
    print(f"[setup] api key loaded ({len(api_key)} chars)")

    # 1. Write no-API paths first (cheap, deterministic)
    for r, err in path_no_anchor:
        append_csv_row(output_csv, row_no_anchor(r["obs_id"], r["study_id"], err))
        append_jsonl(no_anchor_log, {"obs_id": r["obs_id"], "err": err})
    print(f"[no_anchor] wrote {len(path_no_anchor)}")

    for r, anchor in path_pending:
        append_csv_row(output_csv,
                       row_both_pending(r["obs_id"], r["study_id"],
                                        anchor.year, anchor.source))
    print(f"[pending] wrote {len(path_pending)}")

    # 2. API paths (combined first, then 3y_only)
    api_queue = [("combined", r, a) for r, a in path_combined] + \
                [("3y_only",  r, a) for r, a in path_3y_only]
    if args.limit:
        api_queue = api_queue[:args.limit]
        print(f"[limit] capped to {args.limit} API calls")

    print(f"[api] starting {len(api_queue)} calls...")
    t_start = time.monotonic()
    n_ok = n_fail = 0

    for i, (mode, r, anchor) in enumerate(api_queue, 1):
        obs_id = r["obs_id"]
        study_id = r["study_id"]
        study_row = studies.get(study_id, {})
        combined = (mode == "combined")
        sys_prompt = SYSTEM_PROMPT_COMBINED if combined else SYSTEM_PROMPT_3Y_ONLY
        usr_prompt = build_user_prompt(r, study_row, anchor.year, anchor.source, combined)

        parsed, raw, elapsed, err = call_sonar(api_key, sys_prompt, usr_prompt)

        if err or not parsed:
            out = row_parse_fail(obs_id, study_id, anchor.year, anchor.source,
                                 SP_COMBINED if combined else SP_3Y_ONLY, raw, err)
            n_fail += 1
            append_jsonl(failure_log, {
                "obs_id": obs_id, "mode": mode, "err": err,
                "raw_head": raw[:400],
            })
        else:
            if combined:
                ok, norm = validate_combined(parsed)
            else:
                ok, norm = validate_3y_only(parsed)
            if not ok:
                out = row_parse_fail(obs_id, study_id, anchor.year, anchor.source,
                                     SP_COMBINED if combined else SP_3Y_ONLY, raw,
                                     "schema_mismatch")
                n_fail += 1
                append_jsonl(failure_log, {
                    "obs_id": obs_id, "mode": mode, "err": "schema_mismatch",
                    "raw_head": raw[:400],
                })
            else:
                if combined:
                    out = row_combined_ok(obs_id, study_id, anchor.year,
                                          anchor.source, norm, raw)
                else:
                    out = row_3y_only_ok(obs_id, study_id, anchor.year,
                                         anchor.source, norm, raw)
                n_ok += 1
                append_jsonl(checkpoint, {
                    "obs_id": obs_id, "mode": mode,
                    "p3": norm.get("prescience_3y"),
                    "p5": norm.get("prescience_5y", -2),
                    "wd": norm.get("windows_diverge", ""),
                    "elapsed_sec": f"{elapsed:.2f}",
                })

        append_csv_row(output_csv, out)

        if i % 25 == 0:
            elapsed_min = (time.monotonic() - t_start) / 60
            rate = i / elapsed_min if elapsed_min > 0 else 0
            remaining = (len(api_queue) - i) / rate if rate > 0 else 0
            print(f"[api] {i}/{len(api_queue)} | ok={n_ok} fail={n_fail} | "
                  f"{elapsed_min:.1f}m | {rate:.1f}/min | ~{remaining:.0f}m left")
        time.sleep(SLEEP_BETWEEN)

    total_min = (time.monotonic() - t_start) / 60
    print(f"[done] api: {n_ok} ok / {n_fail} fail in {total_min:.1f}m")

    with open(report, "w") as f:
        f.write(f"# Short-Horizon Driver v8 Run Report\n\n")
        f.write(f"Completed: {dt.datetime.now(dt.timezone.utc).isoformat()}\n\n")
        f.write(f"- TODAY_YEAR: {TODAY_YEAR}\n")
        f.write(f"- Model: {MODEL}\n")
        f.write(f"- Output: {output_csv}\n\n")
        f.write(f"## Path classification\n\n")
        f.write(f"- combined (both elapsed): {len(path_combined)}\n")
        f.write(f"- 3y_only (5y pending):    {len(path_3y_only)}\n")
        f.write(f"- both pending (no API):   {len(path_pending)}\n")
        f.write(f"- no_anchor (no API):      {len(path_no_anchor)}\n\n")
        f.write(f"## API results\n\n")
        f.write(f"- Calls attempted: {len(api_queue)}\n")
        f.write(f"- Parse OK: {n_ok}\n")
        f.write(f"- Parse fail: {n_fail}\n")
        f.write(f"- Wall: {total_min:.1f}m\n")
    print(f"[report] {report}")


if __name__ == "__main__":
    main()
