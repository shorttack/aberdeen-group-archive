#!/usr/bin/env python3
"""
run_prescience_pass_c_v4.py — Corpus-wide local prescience scoring
(v4.1 — tolerant validator: missing/invalid confidence defaults to 1 + flagged in rationale)

Pass C v4: Score EVERY observation in _master_observations.csv with local
qwen3.5:27b-mlx via Ollama. No bucket filter, no shape filter.

Architecture decision (2026-05-29):
  - Pass C v1 (cloud LLM) scored the full corpus and left scores in master.
  - Pass C v2/v3 attempted to filter to "scoreable" predictions only,
    motivated by cloud LLM cost. That's the wrong tradeoff for local.
  - Local Qwen costs no credits. The forever-archive principle says:
    score everything, slice later. Filtering away costs us irretrievable
    signal; keeping all scores preserves drift analysis (v1 cloud vs Qwen)
    across the full ~23,605 observations.

Inputs:
  - ~/Desktop/Archive/archive_masters/_master_observations.csv  (all obs)
  - ~/Desktop/Archive/archive_masters/_master_studies.csv       (title + pub_year context)
  - ~/Desktop/Archive/prescience_score_prompt_v2.md              (κ=0.853 calibrated)

Outputs:
  - ~/Desktop/Archive/prescience_scores_pass_c_v4.csv
      header: obs_id, study_id, prescience_score, confidence, rationale, model, prompt_version, ts_utc
      atomic .tmp + os.replace on every flush, csv.QUOTE_ALL
  - /tmp/pass_c_v4_checkpoint.jsonl
      one JSON line per completed obs_id (for resume)
  - /tmp/pass_c_v4_failures.jsonl
      one JSON line per failure (parse error, validation error, HTTP error)

Behavior:
  - Resume-safe: skip obs_ids already in checkpoint
  - Atomic writes via .tmp + os.replace
  - csv.QUOTE_ALL on every CSV write
  - Progress: print every 50 obs with rate + ETA
  - On failure: log to failures.jsonl, set score=-1, continue

Decoding (matches calibration):
  - model: qwen3.5:27b-mlx
  - think: False
  - keep_alive: 30m
  - num_ctx: 8192
  - num_predict: 400
  - temperature: 0.2

Run (Mac):
  cd ~/Desktop/Archive
  nohup python3 scripts/run_prescience_pass_c_v4.py > logs/pass_c_v4.log 2>&1 &
  echo $! > /tmp/pass_c_v4.pid
  tail -f logs/pass_c_v4.log

Resume after interruption: just re-run the same command. Checkpoint handles dedup.
"""

import csv
import json
import os
import sys
import time
import string
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

# -------- Config --------
HOME = Path.home()
ARCHIVE = HOME / "Desktop/Archive"
MASTERS = ARCHIVE / "archive_masters"
MASTER_OBS = MASTERS / "_master_observations.csv"
MASTER_STU = MASTERS / "_master_studies.csv"
PROMPT_FILE = ARCHIVE / "prescience_score_prompt_v2.md"

OUTPUT_CSV = ARCHIVE / "prescience_scores_pass_c_v4.csv"
CHECKPOINT = Path("/tmp/pass_c_v4_checkpoint.jsonl")
FAILURES = Path("/tmp/pass_c_v4_failures.jsonl")
LOG_DIR = ARCHIVE / "logs"

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3.5:27b-mlx"
PROMPT_VERSION = "v2"

DECODING = {
    "temperature": 0.2,
    "num_ctx": 8192,
    "num_predict": 400,
}
KEEP_ALIVE = "30m"
THINK = False

PROGRESS_EVERY = 50
HTTP_TIMEOUT = 120  # seconds per call
HTTP_RETRIES = 2     # one retry per row on network errors


# -------- Prompt loading --------
def load_prompt():
    """Parse prescience_score_prompt_v2.md into (system, user_template).

    File structure (verified 2026-05-29):
      ## SYSTEM PROMPT
      <system prose>
      ---
      ## USER PROMPT TEMPLATE
      <user template with $study_title, $publication_year, $obs_id,
       $observation_type, $section, $metric_value>
    """
    text = PROMPT_FILE.read_text(encoding="utf-8")
    # Split on ## headers
    parts = {}
    current_key = None
    current_buf = []
    for line in text.splitlines():
        if line.startswith("## SYSTEM PROMPT"):
            if current_key:
                parts[current_key] = "\n".join(current_buf).strip()
            current_key = "system"
            current_buf = []
        elif line.startswith("## USER PROMPT TEMPLATE"):
            if current_key:
                parts[current_key] = "\n".join(current_buf).strip()
            current_key = "user"
            current_buf = []
        elif current_key:
            # Skip the horizontal rules between sections
            if line.strip() == "---":
                # ends a section
                if current_key:
                    parts[current_key] = "\n".join(current_buf).strip()
                    current_key = None
                    current_buf = []
                continue
            current_buf.append(line)
    if current_key:
        parts[current_key] = "\n".join(current_buf).strip()

    if "system" not in parts or "user" not in parts:
        raise RuntimeError(
            f"Could not parse prompt file {PROMPT_FILE}. "
            f"Got sections: {list(parts.keys())}"
        )
    return parts["system"], string.Template(parts["user"])


# -------- Master loading --------
def load_studies_context():
    """Return {study_id: {'title': str, 'pub_year': str}}."""
    out = {}
    with open(MASTER_STU, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            sid = row.get("study_id", "").strip()
            if not sid:
                continue
            out[sid] = {
                "title": row.get("title", "") or "",
                "pub_year": row.get("pub_year", "") or "",
            }
    return out


def iter_observations():
    """Yield dicts for every row in _master_observations.csv, in file order."""
    with open(MASTER_OBS, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            yield row


def count_observations():
    """Count rows in _master_observations.csv (cheap line count minus header)."""
    n = 0
    with open(MASTER_OBS, encoding="utf-8") as f:
        for _ in f:
            n += 1
    return max(0, n - 1)


# -------- Checkpoint --------
def load_checkpoint():
    """Return set of obs_ids already scored (from JSONL checkpoint)."""
    done = set()
    if not CHECKPOINT.exists():
        return done
    with open(CHECKPOINT, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                if "obs_id" in rec:
                    done.add(rec["obs_id"])
            except json.JSONDecodeError:
                pass
    return done


def checkpoint_append(obs_id, status):
    """Atomic-ish append to checkpoint JSONL."""
    rec = {
        "obs_id": obs_id,
        "status": status,
        "ts_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    with open(CHECKPOINT, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")


def failure_append(obs_id, reason, detail):
    rec = {
        "obs_id": obs_id,
        "reason": reason,
        "detail": detail[:500],
        "ts_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    with open(FAILURES, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")


# -------- Output CSV (atomic writes) --------
OUTPUT_HEADER = [
    "obs_id",
    "study_id",
    "prescience_score",
    "confidence",
    "rationale",
    "model",
    "prompt_version",
    "ts_utc",
]


def ensure_output_csv():
    """Create output CSV with header if it doesn't exist."""
    if OUTPUT_CSV.exists():
        return
    tmp = OUTPUT_CSV.with_suffix(".csv.tmp")
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(OUTPUT_HEADER)
    os.replace(tmp, OUTPUT_CSV)


def output_append(row_dict):
    """Append one row to output CSV. Not atomic per-row (would be O(n^2)) — we
    rely on csv flush + the checkpoint as the source of truth for resume.
    """
    with open(OUTPUT_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow([row_dict.get(c, "") for c in OUTPUT_HEADER])


# -------- Ollama call --------
def call_ollama(system_prompt, user_prompt):
    """Send chat request to local Ollama. Return parsed JSON dict from model.

    Raises:
      RuntimeError on HTTP failure (after retries) or non-JSON model output.
    """
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "stream": False,
        "think": THINK,
        "keep_alive": KEEP_ALIVE,
        "options": DECODING,
        "format": "json",  # ask Ollama for JSON-mode
    }
    body = json.dumps(payload).encode("utf-8")
    last_err = None
    for attempt in range(HTTP_RETRIES + 1):
        try:
            req = urllib.request.Request(
                OLLAMA_URL,
                data=body,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
                raw = resp.read().decode("utf-8")
            outer = json.loads(raw)
            content = outer.get("message", {}).get("content", "")
            if not content:
                raise RuntimeError("Empty model content")
            # Strip optional ```json fences just in case
            stripped = content.strip()
            if stripped.startswith("```"):
                # remove first fence line and trailing ```
                lines = stripped.splitlines()
                if lines and lines[0].startswith("```"):
                    lines = lines[1:]
                if lines and lines[-1].strip().startswith("```"):
                    lines = lines[:-1]
                stripped = "\n".join(lines).strip()
            return json.loads(stripped)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, RuntimeError) as e:
            last_err = e
            if attempt < HTTP_RETRIES:
                time.sleep(1.0 * (attempt + 1))
                continue
            raise RuntimeError(f"Ollama call failed after {HTTP_RETRIES+1} attempts: {e}") from e


# -------- Per-row scoring --------
def build_claim_text(obs_row):
    """Combine metric_value + notes for the model's claim field."""
    mv = (obs_row.get("metric_value") or "").strip()
    notes = (obs_row.get("notes") or "").strip()
    if not mv and not notes:
        return ""
    if not mv:
        return notes
    if not notes or notes in mv:
        return mv
    # Avoid duplicating common boilerplate notes
    if notes == "Validated from prepared observation seed list and source text.":
        return mv
    return f"{mv}\n\n[Notes] {notes}"


def score_one(obs_row, studies_ctx, system_prompt, user_tmpl):
    obs_id = obs_row.get("obs_id", "").strip()
    study_id = obs_row.get("study_id", "").strip()
    stu = studies_ctx.get(study_id, {"title": "", "pub_year": ""})
    claim = build_claim_text(obs_row)

    user_prompt = user_tmpl.safe_substitute(
        study_title=stu["title"] or "(unknown)",
        publication_year=stu["pub_year"] or "(unknown)",
        obs_id=obs_id,
        observation_type=obs_row.get("observation_type", "") or "(unspecified)",
        section=obs_row.get("section", "") or "(unspecified)",
        metric_value=claim or "(no claim text)",
    )

    parsed = call_ollama(system_prompt, user_prompt)

    # Validate — tolerant mode (v4.1)
    # Score is required and must be a valid int in [0,5].
    # Confidence is optional: if missing/None/out-of-range, default to 1 and flag in rationale.
    # Rationale is optional: empty string is accepted.
    score = parsed.get("prescience_score")
    conf = parsed.get("confidence")
    rationale = parsed.get("rationale", "") or ""

    # Score is hard-required
    if isinstance(score, bool):
        raise ValueError(f"prescience_score is bool, not int: {score!r}")
    if isinstance(score, float) and score.is_integer():
        score = int(score)
    if not isinstance(score, int) or score < 0 or score > 5:
        raise ValueError(f"prescience_score out of range or wrong type: {score!r}")

    # Confidence is soft — accept missing/invalid with default
    conf_flag = ""
    if isinstance(conf, bool):
        conf_flag = f" [conf-flag: was bool {conf!r}, defaulted to 1]"
        conf = 1
    elif isinstance(conf, float) and conf.is_integer():
        conf = int(conf)
    if not isinstance(conf, int) or conf < 1 or conf > 3:
        conf_flag = f" [conf-flag: was {conf!r}, defaulted to 1]"
        conf = 1

    return {
        "obs_id": obs_id,
        "study_id": study_id,
        "prescience_score": score,
        "confidence": conf,
        "rationale": (rationale + conf_flag).strip(),
        "model": MODEL,
        "prompt_version": PROMPT_VERSION,
        "ts_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


# -------- Main --------
def main():
    # Preflight
    for p in (MASTER_OBS, MASTER_STU, PROMPT_FILE):
        if not p.exists():
            sys.exit(f"FATAL: required file missing: {p}")
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    print(f"=== Pass C v4 — Corpus-wide local prescience scoring ===")
    print(f"  master_observations: {MASTER_OBS}")
    print(f"  master_studies:      {MASTER_STU}")
    print(f"  prompt:              {PROMPT_FILE} ({PROMPT_VERSION})")
    print(f"  model:               {MODEL}")
    print(f"  output:              {OUTPUT_CSV}")
    print(f"  checkpoint:          {CHECKPOINT}")
    print(f"  failures:            {FAILURES}")
    print()

    print("Loading prompt template...")
    system_prompt, user_tmpl = load_prompt()
    print(f"  system_prompt: {len(system_prompt)} chars")
    print(f"  user_template: {len(user_tmpl.template)} chars")

    print("Loading studies context...")
    studies_ctx = load_studies_context()
    print(f"  studies loaded: {len(studies_ctx):,}")

    print("Loading checkpoint...")
    done = load_checkpoint()
    print(f"  already scored: {len(done):,}")

    print("Counting observations...")
    total = count_observations()
    remaining = total - len(done)
    print(f"  total observations: {total:,}")
    print(f"  remaining to score: {remaining:,}")

    ensure_output_csv()

    print()
    print("Starting scoring loop. Ctrl-C to abort; restart re-uses checkpoint.")
    print()

    t0 = time.time()
    n_scored = 0
    n_failed = 0
    last_progress_t = t0

    for obs_row in iter_observations():
        obs_id = obs_row.get("obs_id", "").strip()
        if not obs_id:
            continue
        if obs_id in done:
            continue

        try:
            result = score_one(obs_row, studies_ctx, system_prompt, user_tmpl)
            output_append(result)
            checkpoint_append(obs_id, "ok")
            n_scored += 1
        except Exception as e:
            failure_append(obs_id, type(e).__name__, str(e))
            # Still write a sentinel row so output CSV row count tracks attempts
            output_append({
                "obs_id": obs_id,
                "study_id": obs_row.get("study_id", ""),
                "prescience_score": -1,
                "confidence": -1,
                "rationale": f"FAILED: {type(e).__name__}: {str(e)[:200]}",
                "model": MODEL,
                "prompt_version": PROMPT_VERSION,
                "ts_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            })
            checkpoint_append(obs_id, "failed")
            n_failed += 1

        done_count = len(done) + n_scored + n_failed
        if (n_scored + n_failed) % PROGRESS_EVERY == 0:
            elapsed = time.time() - t0
            rate = (n_scored + n_failed) / elapsed if elapsed > 0 else 0
            remaining_now = total - done_count
            eta_sec = remaining_now / rate if rate > 0 else 0
            eta_hr = eta_sec / 3600
            print(
                f"[{done_count:>6,}/{total:,}] "
                f"scored={n_scored:,} failed={n_failed:,} "
                f"rate={rate:.2f}/s "
                f"ETA={eta_hr:.1f}h "
                f"obs={obs_id}",
                flush=True,
            )
            last_progress_t = time.time()

    elapsed = time.time() - t0
    print()
    print("=== Pass C v4 complete ===")
    print(f"  scored this run:  {n_scored:,}")
    print(f"  failed this run:  {n_failed:,}")
    print(f"  total in master:  {total:,}")
    print(f"  total in output:  {len(done) + n_scored + n_failed:,}")
    print(f"  elapsed:          {elapsed/3600:.2f}h")
    print(f"  output:           {OUTPUT_CSV}")
    if n_failed > 0:
        print(f"  failures log:     {FAILURES}")


if __name__ == "__main__":
    main()
