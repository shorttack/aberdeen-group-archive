#!/usr/bin/env python3
"""
route_low_confidence_v2.py
============================
Async cloud reviewer for Pass C v2 confidence==1 rows.

v2 differences vs v1 (2026-05-29):
  - Reads working/prescience_scores_27b_passC_v2.csv (v2 runner output)
  - Writes per-study working/prescience_scores_cloud_review_v2.csv on --apply
  - Queue file at root/pass_c_cloud_review_queue_v2.csv
  - Results file at root/pass_c_cloud_review_results_v2.csv
  - Otherwise identical to v1 logic

Runs AFTER Pass C v2 completes. Per the Model Prescience Scoring Finding (decision §5
item 3): any 27B output where confidence==1 gets a second-pass score from cloud
(Claude). Calibration showed ~2 of 68 rows hit this, so cost is bounded.

This script does NOT call the cloud directly — it produces a work queue file
that the agent (Computer) processes in a subsequent session, returning a CSV
that gets dropped into each study's working/prescience_scores_cloud_review_v2.csv.

Workflow:
  1. Sweep prepared/<study>/working/prescience_scores_27b_passC_v2.csv files
  2. Filter rows where confidence == 1 (or 0 — total non-claim per cloud)
  3. Emit pass_c_cloud_review_queue_v2.csv at --root with the obs payload
     the cloud needs (study_id, obs_id, observation_type, section, metric_value,
     study_title, publication_year, 27b_score, 27b_confidence, 27b_rationale)
  4. Computer then runs the cloud scoring in-session, writes results to
     <root>/pass_c_cloud_review_results_v2.csv with the standard 11-column schema
  5. --apply splits the results CSV back into per-study
     prescience_scores_cloud_review_v2.csv files so the rollup picks them up.

Usage:
  # build the queue
  python3 route_low_confidence_v2.py \\
      --root /Users/scott/Desktop/Archive/prepared \\
      --build-queue

  # (agent fills pass_c_cloud_review_results_v2.csv)

  # apply results back to per-study files
  python3 route_low_confidence_v2.py \\
      --root /Users/scott/Desktop/Archive/prepared \\
      --apply

  # one-shot: build queue and print summary only
  python3 route_low_confidence_v2.py --root ... --build-queue --dry-run
"""
from __future__ import annotations
import argparse
import csv
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

QUOTE_ALL = csv.QUOTE_ALL

PASS_C_GLOB = "working/prescience_scores_27b_passC_v2.csv"
QUEUE_FILENAME = "pass_c_cloud_review_queue_v2.csv"
RESULTS_FILENAME = "pass_c_cloud_review_results_v2.csv"
PER_STUDY_CLOUD_FILENAME = "prescience_scores_cloud_review_v2.csv"

QUEUE_HEADER = [
    "study_id", "obs_id", "study_title", "publication_year",
    "observation_type", "section", "metric_value",
    "27b_score", "27b_confidence", "27b_rationale",
]

RESULT_HEADER = [
    "obs_id", "study_id", "model",
    "prescience_score", "confidence", "rationale",
    "scored_at", "scorer_version", "source_pass",
    "elapsed_sec", "parse_ok",
]


def atomic_write_csv(path: Path, rows: list[dict], header: list[str]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header, quoting=QUOTE_ALL,
                           extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    os.replace(tmp, path)


def load_csv(path: Path) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def study_meta(study_dir: Path) -> tuple[str, str]:
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


def obs_lookup(study_dir: Path) -> dict[str, dict]:
    """Map obs_id → full observation row (for context fields)."""
    p = study_dir / "data" / "observations.csv"
    if not p.exists():
        return {}
    out = {}
    for row in load_csv(p):
        out[row.get("obs_id", "")] = row
    return out


def build_queue(root: Path, dry_run: bool) -> int:
    queue: list[dict] = []
    n_studies_seen = 0
    for study_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        pass_c_csv = study_dir / PASS_C_GLOB
        if not pass_c_csv.exists():
            continue
        n_studies_seen += 1
        title, year = study_meta(study_dir)
        obs_map = obs_lookup(study_dir)
        for row in load_csv(pass_c_csv):
            if row.get("parse_ok") != "true":
                continue
            try:
                conf = int(row.get("confidence", "9"))
            except ValueError:
                continue
            if conf > 1:
                continue
            obs_id = row.get("obs_id", "")
            obs = obs_map.get(obs_id, {})
            queue.append({
                "study_id": row.get("study_id", study_dir.name),
                "obs_id": obs_id,
                "study_title": title,
                "publication_year": year,
                "observation_type": obs.get("observation_type", ""),
                "section": obs.get("section", "") or obs.get("source_page", ""),
                "metric_value": obs.get("metric_value", ""),
                "27b_score": row.get("prescience_score", ""),
                "27b_confidence": row.get("confidence", ""),
                "27b_rationale": row.get("rationale", ""),
            })

    print(f"Studies with Pass C v2 output: {n_studies_seen}")
    print(f"Confidence==1 rows queued: {len(queue)}")

    if dry_run:
        print("DRY RUN — queue not written")
        return 0

    out = root / QUEUE_FILENAME
    atomic_write_csv(out, queue, QUEUE_HEADER)
    print(f"✓ Queue written: {out}")
    print(f"\nNext step: hand this file to Computer to run cloud scoring.")
    print(f"Computer writes results back to: {root / RESULTS_FILENAME}")
    print(f"Then run: python3 route_low_confidence_v2.py --root {root} --apply")
    return 0


def apply_results(root: Path) -> int:
    results_csv = root / RESULTS_FILENAME
    if not results_csv.exists():
        sys.exit(f"ERROR: results file not found: {results_csv}\n"
                 f"Run --build-queue first and have Computer fill the results.")
    rows = load_csv(results_csv)
    print(f"Cloud review results loaded: {len(rows)}")

    by_study: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        sid = r.get("study_id", "")
        if sid:
            by_study[sid].append(r)

    written = 0
    for sid, sid_rows in by_study.items():
        study_dir = root / sid
        if not study_dir.is_dir():
            print(f"  [warn] study dir missing: {sid}")
            continue
        working = study_dir / "working"
        working.mkdir(exist_ok=True)
        out = working / PER_STUDY_CLOUD_FILENAME
        atomic_write_csv(out, sid_rows, RESULT_HEADER)
        print(f"  ✓ {sid}: {len(sid_rows)} cloud review rows → {out.name}")
        written += 1

    print(f"\nWrote {written} per-study cloud-review CSVs.")
    print("Next step: rerun roll_up_prescience_to_master_v2.py to merge.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True,
                    help="Root containing prepared/<study>/ dirs")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--build-queue", action="store_true",
                      help="Sweep Pass C v2 output, emit cloud review queue")
    mode.add_argument("--apply", action="store_true",
                      help="Apply cloud review results back to per-study files")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        sys.exit(f"ERROR: not a directory: {root}")

    if args.build_queue:
        return build_queue(root, args.dry_run)
    if args.apply:
        return apply_results(root)
    return 0


if __name__ == "__main__":
    sys.exit(main())
