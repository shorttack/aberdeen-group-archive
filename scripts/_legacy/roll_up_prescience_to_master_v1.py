#!/usr/bin/env python3
"""
roll_up_prescience_to_master_v1.py
====================================
Concatenate per-study Pass C CSVs into the 8th master:
  _master_prescience_scores.csv

Schema (Option α — locked 2026-05-25):
  obs_id, study_id, model, prescience_score, confidence, rationale,
  scored_at, scorer_version, source_pass, elapsed_sec, parse_ok

Input: prepared/<study>/working/prescience_scores_27b_passC_v1.csv
       (also picks up cloud reviewer outputs:
        prescience_scores_cloud_review_v1.csv — same schema)

Behavior:
  1. Snapshot existing master to archive_masters_pre_<change>_<ts>Z/
  2. Glob all per-study CSVs across --root
  3. Concatenate (deduplicate on (obs_id, model, scorer_version, scored_at))
  4. Write _master_prescience_scores.csv with QUOTE_ALL, atomic
  5. Diff: rows added vs. previous master

§16.5 compliant. Forever-archive safe.

Usage:
  python3 roll_up_prescience_to_master_v1.py \\
      --root /Users/scott/Desktop/Archive/prepared \\
      --masters-dir /Users/scott/Desktop/Archive/archive_masters

  # dry-run: print what would be written, don't touch master
  python3 roll_up_prescience_to_master_v1.py --root ... --masters-dir ... --dry-run
"""
from __future__ import annotations
import argparse
import csv
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

QUOTE_ALL = csv.QUOTE_ALL

MASTER_FILENAME = "_master_prescience_scores.csv"
HEADER = [
    "obs_id", "study_id", "model",
    "prescience_score", "confidence", "rationale",
    "scored_at", "scorer_version", "source_pass",
    "elapsed_sec", "parse_ok",
]

PER_STUDY_GLOBS = [
    "working/prescience_scores_27b_passC_v1.csv",
    "working/prescience_scores_cloud_review_v1.csv",
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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True,
                    help="Root containing prepared/<study>/working/...")
    ap.add_argument("--masters-dir", required=True,
                    help="Directory containing _master_*.csv files")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    masters_dir = Path(args.masters_dir).resolve()
    if not root.is_dir() or not masters_dir.is_dir():
        sys.exit("ERROR: --root or --masters-dir not a directory")

    # 1. Gather all per-study CSVs
    rows: list[dict] = []
    sources_found = 0
    for study_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        for sub in PER_STUDY_GLOBS:
            p = study_dir / sub
            if p.exists():
                sources_found += 1
                rows.extend(load_csv(p))

    print(f"Per-study CSV files found: {sources_found}")
    print(f"Rows loaded: {len(rows)}")

    # 2. Deduplicate on (obs_id, model, scorer_version, scored_at)
    seen = set()
    deduped: list[dict] = []
    for r in rows:
        key = (r.get("obs_id"), r.get("model"),
               r.get("scorer_version"), r.get("scored_at"))
        if key in seen:
            continue
        seen.add(key)
        deduped.append(r)
    print(f"After dedup: {len(deduped)}")

    # 3. Compare to existing master
    master_path = masters_dir / MASTER_FILENAME
    prev_count = 0
    if master_path.exists():
        prev = load_csv(master_path)
        prev_count = len(prev)
        print(f"Existing master rows: {prev_count}")
    else:
        print(f"No existing master at {master_path} (will create)")

    if args.dry_run:
        print("\nDRY RUN: would write")
        print(f"  → {master_path}  ({len(deduped)} rows)")
        return 0

    # 4. Backup existing master
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%SZ")
    if master_path.exists():
        backup_dir = masters_dir.parent / f"archive_masters_pre_prescience_rollup_{ts}"
        backup_dir.mkdir(exist_ok=True)
        shutil.copy2(master_path, backup_dir / MASTER_FILENAME)
        print(f"Backup: {backup_dir / MASTER_FILENAME}")

    # 5. Write
    atomic_write_csv(master_path, deduped, HEADER)
    print(f"\n✓ Wrote {master_path}")
    print(f"  Rows: {len(deduped)} (delta vs previous: +{len(deduped) - prev_count})")

    # 6. Verify
    written = load_csv(master_path)
    if len(written) != len(deduped):
        sys.exit(f"VERIFY FAIL: wrote {len(deduped)} but read back {len(written)}")
    print(f"✓ Verified: read-back row count matches ({len(written)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
