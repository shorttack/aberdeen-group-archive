#!/usr/bin/env python3
"""
run_prescience_calibration_v3.py
=================================
Three-way prescience-scoring calibration for v1.5 Bucket A Pass C.

v3 changes (perf):
  - think=False  (Qwen 3.5 thinking-off mode; eliminates hidden think traces
    that were 95% of output tokens at 13 tok/sec)
  - num_predict=400  (cap rationale length; no runaway)
  - keep_alive='30m'  (model stays resident between calls)
  - num_ctx=8192  (down from 32768 — single obs only needs ~1K tokens)

v2 change: user template uses $var (string.Template) not {var} (str.format)
to avoid collision with the literal { } in the JSON example block.

Reads:
  - prepared/<study>/data/observations.csv
  - prescience_score_prompt_v2.md (system + user templates, $var syntax)
  - manifest.json (for study_title, publication_year)

Calls:
  - Ollama API at http://localhost:11434/api/generate
  - Models: qwen3.5:27b-mlx, qwen3.5:35b-mlx (sequential, not parallel — 48 GB RAM)

Emits:
  - working/prescience_scores_27b_v1.csv
  - working/prescience_scores_35b_v1.csv
  - working/calibration_log_v1.jsonl  (per-call timing, raw response, parse status)

The cloud (Claude) pass is generated separately via the agent — its CSV is
written to working/prescience_scores_cloud_v1.csv for comparison.

Filtering:
  - Skips observations whose metric_value is a markdown header
    (starts with '#', or wrapped in ** with no claim content)
  - Skips observations whose metric_value is < 40 chars (likely a fragment)

Atomic writes:
  - All CSVs written to .tmp then os.replace()
  - Log appended (JSONL is naturally append-safe)

Usage:
  python3 run_prescience_calibration_v3.py \\
    --study /Users/scott/Desktop/Archive/prepared/ra-warehouseautomation-3867-89c99f \\
    --prompt /Users/scott/Desktop/Archive/prescience_score_prompt_v2.md \\
    --models qwen3.5:27b-mlx,qwen3.5:35b-mlx
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

OLLAMA_URL = "http://localhost:11434/api/generate"
QUOTE_ALL = csv.QUOTE_ALL

# ---------- filtering ----------

HEADER_RE = re.compile(r"^\s*#{1,6}\s+")
BOLD_HEADER_RE = re.compile(r"^\s*\*\*.{1,80}\*\*\s*$")

def is_non_claim(metric_value: str) -> tuple[bool, str]:
    """Return (skip, reason)."""
    if not metric_value or not metric_value.strip():
        return True, "empty"
    v = metric_value.strip()
    # Strip markdown bold/italic wrappers for length check
    stripped = re.sub(r"[*_#`]+", "", v).strip()
    if len(stripped) < 40:
        return True, f"too_short({len(stripped)}chars)"
    if HEADER_RE.match(v):
        return True, "markdown_header"
    if BOLD_HEADER_RE.match(v) and "." not in v:
        return True, "bold_header_no_sentence"
    return False, ""

# ---------- prompt loading ----------

def split_prompt(prompt_md: str) -> tuple[str, str]:
    """Split the prompt file into (system, user_template).

    Convention: '## SYSTEM PROMPT' and '## USER PROMPT TEMPLATE' headers.
    """
    sys_match = re.search(r"##\s+SYSTEM PROMPT\s*\n(.*?)(?=\n##\s|\Z)", prompt_md, re.DOTALL)
    user_match = re.search(r"##\s+USER PROMPT TEMPLATE\s*\n(.*?)\Z", prompt_md, re.DOTALL)
    if not sys_match or not user_match:
        sys.exit("ERROR: prompt file missing '## SYSTEM PROMPT' or '## USER PROMPT TEMPLATE' headers")
    return sys_match.group(1).strip(), user_match.group(1).strip()

# ---------- ollama call ----------

def call_ollama(model: str, system: str, prompt: str, timeout: int = 300) -> tuple[str, float, dict]:
    """Call Ollama /api/generate. Returns (response_text, elapsed_sec, raw_meta)."""
    payload = {
        "model": model,
        "system": system,
        "prompt": prompt,
        "stream": False,
        "think": False,            # disable Qwen 3.5 thinking traces
        "keep_alive": "30m",       # keep model resident in VRAM
        "options": {
            "temperature": 0.2,
            "num_ctx": 8192,        # right-sized for single-obs prompts
            "num_predict": 400,     # cap rationale; prevent runaway
        },
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    elapsed = time.time() - t0
    return body.get("response", ""), elapsed, {
        "eval_count": body.get("eval_count"),
        "eval_duration": body.get("eval_duration"),
        "prompt_eval_count": body.get("prompt_eval_count"),
        "total_duration": body.get("total_duration"),
    }

# ---------- response parsing ----------

JSON_FENCE_RE = re.compile(r"```(?:json)?\s*(\{.*?\})\s*```", re.DOTALL)
JSON_BARE_RE = re.compile(r"(\{[^{}]*\"prescience_score\"[^{}]*\})", re.DOTALL)

def parse_score(response_text: str, obs_id: str) -> dict | None:
    """Extract the JSON object from the model's response."""
    if not response_text:
        return None
    # Try fenced first
    m = JSON_FENCE_RE.search(response_text)
    if m:
        candidate = m.group(1)
    else:
        # Bare JSON
        m = JSON_BARE_RE.search(response_text)
        if m:
            candidate = m.group(1)
        else:
            # Last resort: find the outermost braces
            start = response_text.find("{")
            end = response_text.rfind("}")
            if start < 0 or end < 0 or end <= start:
                return None
            candidate = response_text[start:end + 1]
    try:
        obj = json.loads(candidate)
    except json.JSONDecodeError:
        return None
    # Coerce required fields
    try:
        return {
            "obs_id": obj.get("obs_id", obs_id),
            "prescience_score": int(obj.get("prescience_score", -1)),
            "confidence": int(obj.get("confidence", -1)),
            "rationale": str(obj.get("rationale", ""))[:2000],
        }
    except (TypeError, ValueError):
        return None

# ---------- main ----------

def atomic_write_csv(path: Path, rows: list[dict], header: list[str]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header, quoting=QUOTE_ALL)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in header})
    os.replace(tmp, path)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--study", required=True, help="Path to prepared/<study>/ directory")
    ap.add_argument("--prompt", required=True, help="Path to prescience_score_prompt_v1.md")
    ap.add_argument("--models", default="qwen3.5:27b-mlx,qwen3.5:35b-mlx",
                    help="Comma-separated Ollama model tags")
    ap.add_argument("--limit", type=int, default=0, help="Limit number of obs (0=all)")
    ap.add_argument("--dry-run", action="store_true", help="Filter + print plan, no model calls")
    args = ap.parse_args()

    study_dir = Path(args.study).resolve()
    if not study_dir.is_dir():
        sys.exit(f"ERROR: study dir not found: {study_dir}")

    obs_csv = study_dir / "data" / "observations.csv"
    manifest_path = study_dir / "manifest.json"
    working_dir = study_dir / "working"
    working_dir.mkdir(exist_ok=True)

    prompt_md = Path(args.prompt).read_text(encoding="utf-8")
    system_prompt, user_template = split_prompt(prompt_md)

    # Manifest for study-level fields
    study_title = study_dir.name
    publication_year = "unknown"
    if manifest_path.exists():
        try:
            m = json.loads(manifest_path.read_text(encoding="utf-8"))
            study_title = m.get("title") or m.get("study_title") or study_title
            publication_year = str(m.get("publication_year") or m.get("year") or publication_year)
        except json.JSONDecodeError:
            pass

    # Load observations
    with open(obs_csv, encoding="utf-8") as f:
        all_obs = list(csv.DictReader(f))

    # Filter
    scoreable = []
    skipped = []
    for row in all_obs:
        skip, reason = is_non_claim(row.get("metric_value", ""))
        if skip:
            skipped.append({"obs_id": row.get("obs_id"), "reason": reason})
        else:
            scoreable.append(row)

    if args.limit > 0:
        scoreable = scoreable[: args.limit]

    print(f"Study: {study_title}")
    print(f"Total observations: {len(all_obs)}")
    print(f"Skipped (non-claim): {len(skipped)}")
    print(f"Scoreable: {len(scoreable)}")
    print(f"Models: {args.models}")

    if args.dry_run:
        print("\n--- DRY RUN: skipped rows ---")
        for s in skipped[:20]:
            print(f"  {s['obs_id']}: {s['reason']}")
        return

    log_path = working_dir / "calibration_log_v1.jsonl"
    log_f = open(log_path, "a", encoding="utf-8")

    models = [m.strip() for m in args.models.split(",") if m.strip()]
    header = ["obs_id", "prescience_score", "confidence", "rationale",
              "model", "scored_at", "elapsed_sec", "parse_ok"]

    for model in models:
        slug = model.replace(":", "_").replace("/", "_").replace(".", "_")
        out_csv = working_dir / f"prescience_scores_{slug}_v1.csv"
        results: list[dict] = []
        print(f"\n=== {model} ===")
        for i, row in enumerate(scoreable, 1):
            obs_id = row["obs_id"]
            # Use string.Template ($var) instead of str.format ({var})
            # to avoid collisions with the literal { } characters in the
            # JSON example block of the prompt template.
            tmpl = string.Template(user_template)
            user_prompt = tmpl.safe_substitute(
                study_title=study_title,
                publication_year=publication_year,
                obs_id=obs_id,
                observation_type=row.get("observation_type", ""),
                section=row.get("section", "") or row.get("source_page", ""),
                metric_value=row.get("metric_value", ""),
            )
            t_start = time.time()
            try:
                resp_text, elapsed, meta = call_ollama(model, system_prompt, user_prompt)
                err = None
            except urllib.error.URLError as e:
                resp_text, elapsed, meta = "", time.time() - t_start, {}
                err = str(e)

            parsed = parse_score(resp_text, obs_id) if resp_text else None
            parse_ok = parsed is not None

            scored_at = datetime.now(timezone.utc).isoformat()
            if parsed:
                results.append({
                    **parsed,
                    "model": model,
                    "scored_at": scored_at,
                    "elapsed_sec": f"{elapsed:.2f}",
                    "parse_ok": "true",
                })
            else:
                results.append({
                    "obs_id": obs_id,
                    "prescience_score": "",
                    "confidence": "",
                    "rationale": "",
                    "model": model,
                    "scored_at": scored_at,
                    "elapsed_sec": f"{elapsed:.2f}",
                    "parse_ok": "false",
                })

            log_f.write(json.dumps({
                "obs_id": obs_id,
                "model": model,
                "elapsed_sec": elapsed,
                "parse_ok": parse_ok,
                "error": err,
                "raw_response": resp_text[:4000],
                "meta": meta,
            }) + "\n")
            log_f.flush()

            print(f"  [{i:>3}/{len(scoreable)}] {obs_id}  "
                  f"score={parsed['prescience_score'] if parsed else '?'}  "
                  f"{elapsed:.1f}s  parse_ok={parse_ok}")

            # Write incrementally every 10 obs so we don't lose progress
            if i % 10 == 0:
                atomic_write_csv(out_csv, results, header)

        atomic_write_csv(out_csv, results, header)
        print(f"  -> wrote {out_csv}")

    log_f.close()
    print(f"\nLog: {log_path}")
    print("Done. Generate cloud pass separately and place at:")
    print(f"  {working_dir}/prescience_scores_cloud_v1.csv")

if __name__ == "__main__":
    main()
