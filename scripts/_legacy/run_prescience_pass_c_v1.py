#!/usr/bin/env python3
"""
run_prescience_pass_c_v1.py
=============================
Bucket A Pass C — production prescience scoring across all studies under
/Users/scott/Desktop/Archive/prepared/.

Per the Model Prescience Scoring Finding (kappa 0.853 vs Cloud):
  - Production scorer: qwen3.5:27b-mlx (local Ollama on M4 Pro)
  - think=False, keep_alive=30m, num_ctx=8192, num_predict=400, temperature=0.2
  - Cloud reviewer for confidence==1 rows runs ASYNC (separate script after Pass C)

Pipeline per study:
  1. Read working/scoreable_obs_v1.csv (from pre_filter_scoreable_obs_v1.py)
     If missing, run the filter inline (lazy).
  2. For each scoreable obs, call Ollama with the v2 prompt
  3. Parse JSON response → prescience_score (0-5), confidence (1-3), rationale
  4. Atomically append to working/prescience_scores_27b_passC_v1.csv
  5. Update checkpoint after every successful study

Crash recovery:
  - Checkpoint file at <root>/pass_c_checkpoint_v1.json
    Tracks: completed_studies[], in_progress (study + last_obs_idx),
            started_at, last_update, total_obs_scored
  - On restart: skip completed studies, resume in-progress study from last_obs_idx

Heat / throttle:
  - Sleep 5s every 10 obs (gentle on M4 Pro thermal envelope over 45 hrs)
  - Configurable via --throttle-every / --throttle-seconds

Output schema (per study CSV, also Option α master schema):
  obs_id, study_id, model, prescience_score, confidence, rationale,
  scored_at, scorer_version, source_pass, elapsed_sec, parse_ok

§16.5: all CSV writes use QUOTE_ALL + atomic .tmp + os.replace.

Usage:
  # full run (resumes from checkpoint if present)
  python3 run_prescience_pass_c_v1.py \\
      --root /Users/scott/Desktop/Archive/prepared \\
      --prompt /Users/scott/Desktop/Archive/prescience_score_prompt_v2.md

  # dry-run plan (no Ollama calls, no writes)
  python3 run_prescience_pass_c_v1.py --root ... --prompt ... --dry-run

  # test on N studies
  python3 run_prescience_pass_c_v1.py --root ... --prompt ... --max-studies 2

  # force restart (delete checkpoint first)
  rm /Users/scott/Desktop/Archive/prepared/pass_c_checkpoint_v1.json
"""
from __future__ import annotations
import argparse
import csv
import json
import os
import re
import string
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

# Reuse the filter from pre_filter_scoreable_obs_v1 if installed alongside
HEADER_RE = re.compile(r"^\s*#{1,6}\s+")
BOLD_HEADER_RE = re.compile(r"^\s*\*\*.{1,80}\*\*\s*$")
QUOTE_ALL = csv.QUOTE_ALL

OLLAMA_URL = "http://localhost:11434/api/generate"
SCORER_VERSION = "qwen3.5:27b-mlx_passC_v1"
SOURCE_PASS = "pass_c"
MODEL_DEFAULT = "qwen3.5:27b-mlx"

JSON_FENCE_RE = re.compile(r"```(?:json)?\s*(\{.*?\})\s*```", re.DOTALL)
JSON_BARE_RE = re.compile(r"(\{[^{}]*\"prescience_score\"[^{}]*\})", re.DOTALL)

OUTPUT_HEADER = [
    "obs_id", "study_id", "model",
    "prescience_score", "confidence", "rationale",
    "scored_at", "scorer_version", "source_pass",
    "elapsed_sec", "parse_ok",
]


# ----------------- filter (mirror of pre_filter script) -----------------

def is_non_claim(metric_value: str) -> tuple[bool, str]:
    if not metric_value or not metric_value.strip():
        return True, "empty"
    v = metric_value.strip()
    stripped = re.sub(r"[*_#`]+", "", v).strip()
    if len(stripped) < 40:
        return True, f"too_short({len(stripped)}chars)"
    if HEADER_RE.match(v):
        return True, "markdown_header"
    if BOLD_HEADER_RE.match(v) and "." not in v:
        return True, "bold_header_no_sentence"
    return False, ""


# ----------------- prompt loading -----------------

def split_prompt(prompt_md: str) -> tuple[str, str]:
    sys_match = re.search(r"##\s+SYSTEM PROMPT\s*\n(.*?)(?=\n##\s|\Z)",
                          prompt_md, re.DOTALL)
    user_match = re.search(r"##\s+USER PROMPT TEMPLATE\s*\n(.*?)\Z",
                           prompt_md, re.DOTALL)
    if not sys_match or not user_match:
        sys.exit("ERROR: prompt file missing required headers")
    return sys_match.group(1).strip(), user_match.group(1).strip()


# ----------------- ollama -----------------

def call_ollama(model: str, system: str, prompt: str,
                timeout: int = 300) -> tuple[str, float, dict, str | None]:
    payload = {
        "model": model,
        "system": system,
        "prompt": prompt,
        "stream": False,
        "think": False,
        "keep_alive": "30m",
        "options": {
            "temperature": 0.2,
            "num_ctx": 8192,
            "num_predict": 400,
        },
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_URL, data=data,
        headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        return "", time.time() - t0, {}, str(e)
    except Exception as e:
        return "", time.time() - t0, {}, f"{type(e).__name__}: {e}"
    elapsed = time.time() - t0
    return body.get("response", ""), elapsed, {
        "eval_count": body.get("eval_count"),
        "prompt_eval_count": body.get("prompt_eval_count"),
        "total_duration": body.get("total_duration"),
    }, None


# ----------------- parsing -----------------

def parse_score(response_text: str, obs_id: str) -> dict | None:
    if not response_text:
        return None
    m = JSON_FENCE_RE.search(response_text)
    candidate = m.group(1) if m else None
    if not candidate:
        m = JSON_BARE_RE.search(response_text)
        candidate = m.group(1) if m else None
    if not candidate:
        start = response_text.find("{")
        end = response_text.rfind("}")
        if start < 0 or end <= start:
            return None
        candidate = response_text[start:end + 1]
    try:
        obj = json.loads(candidate)
    except json.JSONDecodeError:
        return None
    try:
        return {
            "obs_id": obj.get("obs_id", obs_id),
            "prescience_score": int(obj.get("prescience_score", -1)),
            "confidence": int(obj.get("confidence", -1)),
            "rationale": str(obj.get("rationale", ""))[:2000],
        }
    except (TypeError, ValueError):
        return None


# ----------------- atomic IO -----------------

def atomic_write_csv(path: Path, rows: list[dict], header: list[str]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header, quoting=QUOTE_ALL,
                           extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    os.replace(tmp, path)


def atomic_write_json(path: Path, obj: dict) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True)
    os.replace(tmp, path)


# ----------------- checkpoint -----------------

def load_checkpoint(path: Path) -> dict:
    if not path.exists():
        return {
            "completed_studies": [],
            "in_progress": None,
            "started_at": datetime.now(timezone.utc).isoformat(),
            "last_update": datetime.now(timezone.utc).isoformat(),
            "total_obs_scored": 0,
            "total_parse_failures": 0,
            "scorer_version": SCORER_VERSION,
        }
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_checkpoint(path: Path, ckpt: dict) -> None:
    ckpt["last_update"] = datetime.now(timezone.utc).isoformat()
    atomic_write_json(path, ckpt)


# ----------------- per-study scoring -----------------

def load_scoreable(study_dir: Path) -> tuple[list[dict], list[str]]:
    """Return (scoreable_rows, fieldnames). Lazy-runs filter if cache missing."""
    cached = study_dir / "working" / "scoreable_obs_v1.csv"
    if cached.exists():
        with open(cached, encoding="utf-8") as f:
            r = csv.DictReader(f)
            rows = list(r)
            return rows, r.fieldnames or []

    obs_csv = study_dir / "data" / "observations.csv"
    if not obs_csv.exists():
        return [], []
    with open(obs_csv, encoding="utf-8") as f:
        r = csv.DictReader(f)
        all_rows = list(r)
        fieldnames = r.fieldnames or []
    scoreable = []
    for row in all_rows:
        skip, _ = is_non_claim(row.get("metric_value", ""))
        if not skip:
            scoreable.append(row)
    return scoreable, fieldnames


def study_manifest(study_dir: Path) -> tuple[str, str]:
    """Return (study_title, publication_year_str)."""
    mp = study_dir / "manifest.json"
    title = study_dir.name
    year = "unknown"
    if mp.exists():
        try:
            m = json.loads(mp.read_text(encoding="utf-8"))
            title = m.get("title") or m.get("study_title") or title
            year = str(m.get("publication_year") or m.get("year") or year)
        except json.JSONDecodeError:
            pass
    return title, year


def score_study(study_dir: Path, model: str, system_prompt: str,
                user_template: str, ckpt: dict, ckpt_path: Path,
                throttle_every: int, throttle_seconds: float,
                dry_run: bool) -> tuple[int, int]:
    """Score one study. Returns (n_scored, n_parse_failures)."""
    study_id = study_dir.name
    scoreable, _ = load_scoreable(study_dir)
    if not scoreable:
        print(f"  [skip] {study_id}: no scoreable observations")
        return 0, 0

    working_dir = study_dir / "working"
    working_dir.mkdir(exist_ok=True)
    out_csv = working_dir / "prescience_scores_27b_passC_v1.csv"
    log_path = working_dir / "pass_c_log_v1.jsonl"

    # Resume mid-study: if checkpoint says this study is in progress, start
    # from last_obs_idx + 1
    start_idx = 0
    existing_results: list[dict] = []
    if ckpt.get("in_progress", {}) and ckpt["in_progress"].get("study_id") == study_id:
        start_idx = int(ckpt["in_progress"].get("last_obs_idx", -1)) + 1
        if out_csv.exists():
            with open(out_csv, encoding="utf-8") as f:
                existing_results = list(csv.DictReader(f))
        print(f"  [resume] {study_id}: starting from obs index {start_idx}")

    study_title, pub_year = study_manifest(study_dir)
    print(f"  → {study_id}  ({len(scoreable)} obs, pub_year={pub_year})")

    if dry_run:
        return len(scoreable), 0

    results = existing_results
    parse_failures = 0
    log_f = open(log_path, "a", encoding="utf-8")

    try:
        for i in range(start_idx, len(scoreable)):
            row = scoreable[i]
            obs_id = row["obs_id"]
            tmpl = string.Template(user_template)
            user_prompt = tmpl.safe_substitute(
                study_title=study_title,
                publication_year=pub_year,
                obs_id=obs_id,
                observation_type=row.get("observation_type", ""),
                section=row.get("section", "") or row.get("source_page", ""),
                metric_value=row.get("metric_value", ""),
            )

            resp_text, elapsed, meta, err = call_ollama(
                model, system_prompt, user_prompt)
            parsed = parse_score(resp_text, obs_id)
            parse_ok = parsed is not None
            scored_at = datetime.now(timezone.utc).isoformat()

            if parsed:
                results.append({
                    "obs_id": obs_id,
                    "study_id": study_id,
                    "model": model,
                    "prescience_score": parsed["prescience_score"],
                    "confidence": parsed["confidence"],
                    "rationale": parsed["rationale"],
                    "scored_at": scored_at,
                    "scorer_version": SCORER_VERSION,
                    "source_pass": SOURCE_PASS,
                    "elapsed_sec": f"{elapsed:.2f}",
                    "parse_ok": "true",
                })
            else:
                parse_failures += 1
                results.append({
                    "obs_id": obs_id,
                    "study_id": study_id,
                    "model": model,
                    "prescience_score": "",
                    "confidence": "",
                    "rationale": "",
                    "scored_at": scored_at,
                    "scorer_version": SCORER_VERSION,
                    "source_pass": SOURCE_PASS,
                    "elapsed_sec": f"{elapsed:.2f}",
                    "parse_ok": "false",
                })

            log_f.write(json.dumps({
                "obs_id": obs_id,
                "study_id": study_id,
                "model": model,
                "elapsed_sec": elapsed,
                "parse_ok": parse_ok,
                "error": err,
                "raw_response": (resp_text or "")[:4000],
                "meta": meta,
            }) + "\n")
            log_f.flush()

            score_str = parsed["prescience_score"] if parsed else "?"
            print(f"    [{i + 1:>3}/{len(scoreable)}] {obs_id}  "
                  f"score={score_str}  {elapsed:.1f}s  ok={parse_ok}"
                  + (f"  ERR={err[:60]}" if err else ""))

            # incremental persistence
            if (i + 1) % 5 == 0 or (i + 1) == len(scoreable):
                atomic_write_csv(out_csv, results, OUTPUT_HEADER)
                ckpt["in_progress"] = {
                    "study_id": study_id, "last_obs_idx": i,
                    "n_scoreable": len(scoreable),
                }
                ckpt["total_obs_scored"] = ckpt.get("total_obs_scored", 0) + (
                    1 if (i + 1) % 5 != 0 else 5)  # rough; recomputed at end
                save_checkpoint(ckpt_path, ckpt)

            # heat / thermal throttle
            if throttle_every > 0 and (i + 1) % throttle_every == 0:
                time.sleep(throttle_seconds)
    finally:
        log_f.close()
        atomic_write_csv(out_csv, results, OUTPUT_HEADER)

    return len(scoreable) - start_idx, parse_failures


# ----------------- main -----------------

def list_studies(root: Path) -> list[Path]:
    return sorted(p for p in root.iterdir()
                  if p.is_dir() and not p.name.startswith(".")
                  and (p / "data" / "observations.csv").exists())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True,
                    help="Root containing prepared/<study>/ dirs")
    ap.add_argument("--prompt", required=True,
                    help="Path to prescience_score_prompt_v2.md")
    ap.add_argument("--model", default=MODEL_DEFAULT)
    ap.add_argument("--max-studies", type=int, default=0,
                    help="Score at most N studies (0 = all)")
    ap.add_argument("--throttle-every", type=int, default=10,
                    help="Sleep every N obs (0 = no throttle)")
    ap.add_argument("--throttle-seconds", type=float, default=5.0)
    ap.add_argument("--dry-run", action="store_true",
                    help="List studies + scoreable counts, no Ollama calls")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        sys.exit(f"ERROR: not a directory: {root}")

    prompt_md = Path(args.prompt).read_text(encoding="utf-8")
    system_prompt, user_template = split_prompt(prompt_md)

    ckpt_path = root / "pass_c_checkpoint_v1.json"
    ckpt = load_checkpoint(ckpt_path)
    completed = set(ckpt.get("completed_studies", []))

    studies = list_studies(root)
    print(f"Pass C — root={root}")
    print(f"Model: {args.model}")
    print(f"Studies discovered: {len(studies)}")
    print(f"Already completed (per checkpoint): {len(completed)}")
    pending = [s for s in studies if s.name not in completed]
    print(f"Pending: {len(pending)}")
    if args.max_studies > 0:
        pending = pending[:args.max_studies]
        print(f"--max-studies={args.max_studies} → running {len(pending)}")

    if args.dry_run:
        total_obs = 0
        for s in pending:
            sc, _ = load_scoreable(s)
            total_obs += len(sc)
            print(f"  {s.name}: {len(sc)} scoreable")
        print(f"\nDRY RUN: {len(pending)} studies, {total_obs} obs total")
        print(f"At 15 s/obs: ~{total_obs * 15 / 3600:.1f} hours")
        return 0

    grand_scored = 0
    grand_failures = 0
    t_start = time.time()
    for idx, study_dir in enumerate(pending, 1):
        print(f"\n[{idx}/{len(pending)}] elapsed={(time.time() - t_start) / 60:.1f}min  "
              f"scored_so_far={grand_scored}")
        try:
            n_scored, n_fail = score_study(
                study_dir, args.model, system_prompt, user_template,
                ckpt, ckpt_path,
                args.throttle_every, args.throttle_seconds,
                dry_run=False)
        except KeyboardInterrupt:
            print("\n[interrupt] checkpoint saved; safe to restart")
            save_checkpoint(ckpt_path, ckpt)
            return 130
        except Exception as e:
            print(f"  [ERROR] {study_dir.name}: {e}")
            save_checkpoint(ckpt_path, ckpt)
            continue

        grand_scored += n_scored
        grand_failures += n_fail
        completed.add(study_dir.name)
        ckpt["completed_studies"] = sorted(completed)
        ckpt["in_progress"] = None
        ckpt["total_parse_failures"] = ckpt.get("total_parse_failures", 0) + n_fail
        save_checkpoint(ckpt_path, ckpt)

    print(f"\n=== Pass C complete ===")
    print(f"Studies completed this run: {len(pending)}")
    print(f"Observations scored: {grand_scored}")
    print(f"Parse failures: {grand_failures}")
    print(f"Wall clock: {(time.time() - t_start) / 60:.1f} min")
    print(f"Checkpoint: {ckpt_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
