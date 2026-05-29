#!/usr/bin/env python3
"""
run_prescience_pass_c_v4_2.py — Pass C v4.1 with model + study filtering

Adds three things over v4.1 (v4):
  1. --model FLAG: override the default qwen3.5:27b-mlx for smoke-tests against
     other local Ollama models (e.g., qwen3.5:35b-mlx).
  2. --study-ids FLAG: comma-separated list of study_ids to filter; all other
     observations are skipped. Used for calibration / smoke-test runs.
  3. raw_response capture in failures.jsonl: when validation rejects a row, the
     full raw model output is preserved (truncated at 2000 chars) so we can
     diagnose drift patterns without re-running.

Per-model output isolation:
  When --model is non-default OR --tag is given, output paths get a slug
  suffix so a 35b run doesn't clobber the 27b run:
    prescience_scores_pass_c_v4_2__qwen3_5_35b_mlx.csv
    /tmp/pass_c_v4_2__qwen3_5_35b_mlx_checkpoint.jsonl
    /tmp/pass_c_v4_2__qwen3_5_35b_mlx_failures.jsonl

Behavior unchanged from v4.1 otherwise:
  - Reads _master_observations.csv directly (full corpus)
  - Same prompt v2 (κ=0.853 calibrated)
  - Same decoding (temp 0.2, num_ctx 8192, num_predict 400, json format)
  - Same tolerant validator (confidence defaults to 1 on miss; score is hard)
  - Same atomic writes, same QUOTE_ALL, same resume logic
  - --commit is implied; this is read-only on masters

Run (Mac) — DeFranco + warehouseautomation smoke test with 35b-mlx:
  cd ~/Desktop/Archive
  nohup python3 scripts/run_prescience_pass_c_v4_2.py \
    --model qwen3.5:35b-mlx \
    --study-ids 01-difranco-report-on-aberdeen-group-res-444a19,ra-warehouseautomation-3867-89c99f \
    > logs/pass_c_v4_2_35b_smoke.log 2>&1 &
  echo $! > /tmp/pass_c_v4_2_35b_smoke.pid
  tail -f logs/pass_c_v4_2_35b_smoke.log

Forever-archive principle preserved: every failure carries its raw_response.
"""

import argparse
import csv
import json
import os
import re
import sys
import time
import string
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

# -------- Defaults --------
HOME = Path.home()
ARCHIVE = HOME / "Desktop/Archive"
MASTERS = ARCHIVE / "archive_masters"
MASTER_OBS = MASTERS / "_master_observations.csv"
MASTER_STU = MASTERS / "_master_studies.csv"
PROMPT_FILE = ARCHIVE / "prescience_score_prompt_v2.md"
LOG_DIR = ARCHIVE / "logs"

OLLAMA_URL = "http://localhost:11434/api/chat"
DEFAULT_MODEL = "qwen3.5:27b-mlx"
PROMPT_VERSION = "v2"

DECODING = {
    "temperature": 0.2,
    "num_ctx": 8192,
    "num_predict": 400,
}
KEEP_ALIVE = "30m"
THINK = False

PROGRESS_EVERY = 25  # tighter for short smoke runs
HTTP_TIMEOUT = 180   # 35b is slower; widen the per-call ceiling
HTTP_RETRIES = 2


# -------- Path slugging --------
def model_slug(model_name: str) -> str:
    """Turn 'qwen3.5:35b-mlx' into 'qwen3_5_35b_mlx' for filenames."""
    return re.sub(r"[^a-zA-Z0-9]+", "_", model_name).strip("_").lower()


def compute_paths(model: str, tag: str | None) -> dict:
    """Output paths. If model != default OR tag given, suffix with slug."""
    base_csv = "prescience_scores_pass_c_v4_2"
    base_tmp = "pass_c_v4_2"
    suffix = ""
    if model != DEFAULT_MODEL or tag:
        parts = [model_slug(model)]
        if tag:
            parts.append(re.sub(r"[^a-zA-Z0-9]+", "_", tag).strip("_").lower())
        suffix = "__" + "__".join(parts)
    return {
        "output_csv": ARCHIVE / f"{base_csv}{suffix}.csv",
        "checkpoint": Path(f"/tmp/{base_tmp}{suffix}_checkpoint.jsonl"),
        "failures":   Path(f"/tmp/{base_tmp}{suffix}_failures.jsonl"),
    }


# -------- Prompt loading (unchanged from v4.1) --------
def load_prompt():
    text = PROMPT_FILE.read_text(encoding="utf-8")
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
            if line.strip() == "---":
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


# -------- Master loading (unchanged) --------
def load_studies_context():
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


def iter_observations(study_filter: set[str] | None):
    """Yield rows from _master_observations.csv. If study_filter is a non-empty
    set, only yield rows whose study_id is in the set."""
    with open(MASTER_OBS, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            if study_filter:
                sid = row.get("study_id", "").strip()
                if sid not in study_filter:
                    continue
            yield row


def count_observations(study_filter: set[str] | None) -> int:
    """Count rows matching the (optional) study filter."""
    if not study_filter:
        n = 0
        with open(MASTER_OBS, encoding="utf-8") as f:
            for _ in f:
                n += 1
        return max(0, n - 1)
    n = 0
    with open(MASTER_OBS, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            if row.get("study_id", "").strip() in study_filter:
                n += 1
    return n


# -------- Checkpoint / failures (raw_response added) --------
def load_checkpoint(path: Path):
    done = set()
    if not path.exists():
        return done
    with open(path, encoding="utf-8") as f:
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


def checkpoint_append(path: Path, obs_id: str, status: str):
    rec = {
        "obs_id": obs_id,
        "status": status,
        "ts_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")


def failure_append(path: Path, obs_id: str, reason: str, detail: str,
                   raw_response: str | None = None,
                   study_id: str = "", model: str = ""):
    """v4.2: now captures raw_response so we can diagnose drift offline."""
    rec = {
        "obs_id": obs_id,
        "study_id": study_id,
        "model": model,
        "reason": reason,
        "detail": detail[:500],
        "raw_response": (raw_response or "")[:2000],
        "ts_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")


# -------- Output CSV (atomic + QUOTE_ALL) --------
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


def ensure_output_csv(path: Path):
    if path.exists():
        return
    tmp = path.with_suffix(".csv.tmp")
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(OUTPUT_HEADER)
    os.replace(tmp, path)


def output_append(path: Path, row_dict: dict):
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow([row_dict.get(c, "") for c in OUTPUT_HEADER])


# -------- Ollama call (model + raw_response capture) --------
class OllamaCallError(RuntimeError):
    """Carries raw_response if we got far enough to receive content."""
    def __init__(self, message: str, raw: str | None = None):
        super().__init__(message)
        self.raw = raw


def call_ollama(model: str, system_prompt: str, user_prompt: str) -> tuple[dict, str]:
    """Send chat request to local Ollama.

    Returns (parsed_json_dict, raw_content_string).
    Raises OllamaCallError on HTTP failure or non-JSON model output;
    the error carries .raw with the raw content when available.
    """
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "stream": False,
        "think": THINK,
        "keep_alive": KEEP_ALIVE,
        "options": DECODING,
        "format": "json",
    }
    body = json.dumps(payload).encode("utf-8")
    last_err = None
    last_raw = None
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
            last_raw = content
            if not content:
                raise OllamaCallError("Empty model content", raw=content)
            stripped = content.strip()
            if stripped.startswith("```"):
                lines = stripped.splitlines()
                if lines and lines[0].startswith("```"):
                    lines = lines[1:]
                if lines and lines[-1].strip().startswith("```"):
                    lines = lines[:-1]
                stripped = "\n".join(lines).strip()
            try:
                parsed = json.loads(stripped)
            except json.JSONDecodeError as je:
                raise OllamaCallError(f"Model output not JSON: {je}", raw=content)
            return parsed, content
        except (urllib.error.URLError, TimeoutError, OllamaCallError, json.JSONDecodeError) as e:
            last_err = e
            if isinstance(e, OllamaCallError) and e.raw is not None:
                last_raw = e.raw
            if attempt < HTTP_RETRIES:
                time.sleep(1.0 * (attempt + 1))
                continue
            raise OllamaCallError(
                f"Ollama call failed after {HTTP_RETRIES+1} attempts: {e}",
                raw=last_raw,
            ) from e


# -------- Per-row scoring (unchanged validator semantics from v4.1) --------
def build_claim_text(obs_row: dict) -> str:
    mv = (obs_row.get("metric_value") or "").strip()
    notes = (obs_row.get("notes") or "").strip()
    if not mv and not notes:
        return ""
    if not mv:
        return notes
    if not notes or notes in mv:
        return mv
    if notes == "Validated from prepared observation seed list and source text.":
        return mv
    return f"{mv}\n\n[Notes] {notes}"


class ScoringError(ValueError):
    """Carries raw_response so failures.jsonl can capture it."""
    def __init__(self, message: str, raw: str | None = None):
        super().__init__(message)
        self.raw = raw


def score_one(model: str, obs_row: dict, studies_ctx: dict,
              system_prompt: str, user_tmpl) -> dict:
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

    parsed, raw_content = call_ollama(model, system_prompt, user_prompt)

    score = parsed.get("prescience_score")
    conf = parsed.get("confidence")
    rationale = parsed.get("rationale", "") or ""

    if isinstance(score, bool):
        raise ScoringError(f"prescience_score is bool, not int: {score!r}", raw=raw_content)
    if isinstance(score, float) and score.is_integer():
        score = int(score)
    if not isinstance(score, int) or score < 0 or score > 5:
        raise ScoringError(
            f"prescience_score out of range or wrong type: {score!r}",
            raw=raw_content,
        )

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
        "model": model,
        "prompt_version": PROMPT_VERSION,
        "ts_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


# -------- CLI --------
def parse_args(argv=None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Pass C v4.2 — corpus-wide (or filtered) local prescience scoring",
    )
    p.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Ollama model name (default: {DEFAULT_MODEL})",
    )
    p.add_argument(
        "--study-ids",
        default="",
        help="Comma-separated study_ids to filter (default: empty = full corpus)",
    )
    p.add_argument(
        "--tag",
        default=None,
        help="Optional tag appended to output filenames (e.g., 'smoke', 'sweep1')",
    )
    return p.parse_args(argv)


# -------- Main --------
def main():
    args = parse_args()

    model = args.model
    study_filter: set[str] | None = None
    if args.study_ids.strip():
        study_filter = {s.strip() for s in args.study_ids.split(",") if s.strip()}

    paths = compute_paths(model, args.tag)
    output_csv = paths["output_csv"]
    checkpoint = paths["checkpoint"]
    failures = paths["failures"]

    for p in (MASTER_OBS, MASTER_STU, PROMPT_FILE):
        if not p.exists():
            sys.exit(f"FATAL: required file missing: {p}")
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    print("=== Pass C v4.2 — local prescience scoring ===")
    print(f"  model:               {model}")
    print(f"  prompt:              {PROMPT_FILE} ({PROMPT_VERSION})")
    print(f"  study_filter:        {sorted(study_filter) if study_filter else '(none — full corpus)'}")
    print(f"  output:              {output_csv}")
    print(f"  checkpoint:          {checkpoint}")
    print(f"  failures:            {failures}")
    print()

    print("Loading prompt template...")
    system_prompt, user_tmpl = load_prompt()
    print(f"  system_prompt: {len(system_prompt)} chars")
    print(f"  user_template: {len(user_tmpl.template)} chars")

    print("Loading studies context...")
    studies_ctx = load_studies_context()
    print(f"  studies loaded: {len(studies_ctx):,}")

    print("Loading checkpoint...")
    done = load_checkpoint(checkpoint)
    print(f"  already scored: {len(done):,}")

    print("Counting observations matching filter...")
    total = count_observations(study_filter)
    remaining = total - len(done)
    print(f"  total observations: {total:,}")
    print(f"  remaining to score: {remaining:,}")

    ensure_output_csv(output_csv)

    print()
    print("Starting scoring loop. Ctrl-C to abort; restart re-uses checkpoint.")
    print()

    t0 = time.time()
    n_scored = 0
    n_failed = 0

    for obs_row in iter_observations(study_filter):
        obs_id = obs_row.get("obs_id", "").strip()
        if not obs_id:
            continue
        if obs_id in done:
            continue

        try:
            result = score_one(model, obs_row, studies_ctx, system_prompt, user_tmpl)
            output_append(output_csv, result)
            checkpoint_append(checkpoint, obs_id, "ok")
            n_scored += 1
        except (ScoringError, OllamaCallError) as e:
            raw = getattr(e, "raw", None)
            failure_append(
                failures,
                obs_id,
                type(e).__name__,
                str(e),
                raw_response=raw,
                study_id=obs_row.get("study_id", ""),
                model=model,
            )
            output_append(output_csv, {
                "obs_id": obs_id,
                "study_id": obs_row.get("study_id", ""),
                "prescience_score": -1,
                "confidence": -1,
                "rationale": f"FAILED: {type(e).__name__}: {str(e)[:200]}",
                "model": model,
                "prompt_version": PROMPT_VERSION,
                "ts_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            })
            checkpoint_append(checkpoint, obs_id, "failed")
            n_failed += 1
        except Exception as e:  # noqa: BLE001
            # unexpected — capture without raw_response
            failure_append(
                failures,
                obs_id,
                type(e).__name__,
                str(e),
                raw_response=None,
                study_id=obs_row.get("study_id", ""),
                model=model,
            )
            output_append(output_csv, {
                "obs_id": obs_id,
                "study_id": obs_row.get("study_id", ""),
                "prescience_score": -1,
                "confidence": -1,
                "rationale": f"FAILED: {type(e).__name__}: {str(e)[:200]}",
                "model": model,
                "prompt_version": PROMPT_VERSION,
                "ts_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            })
            checkpoint_append(checkpoint, obs_id, "failed")
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
                f"ETA={eta_hr:.2f}h "
                f"obs={obs_id}",
                flush=True,
            )

    elapsed = time.time() - t0
    print()
    print("=== Pass C v4.2 complete ===")
    print(f"  model:            {model}")
    print(f"  scored this run:  {n_scored:,}")
    print(f"  failed this run:  {n_failed:,}")
    print(f"  total in scope:   {total:,}")
    print(f"  total in output:  {len(done) + n_scored + n_failed:,}")
    print(f"  elapsed:          {elapsed/3600:.2f}h")
    print(f"  output:           {output_csv}")
    if n_failed > 0:
        print(f"  failures log:     {failures}")


if __name__ == "__main__":
    main()
