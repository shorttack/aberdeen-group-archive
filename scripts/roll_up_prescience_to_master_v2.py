#!/usr/bin/env python3
"""
roll_up_prescience_to_master_v2.py
====================================
Concatenate per-study Pass C v2 CSVs into the 8th master:
  _master_prescience_scores.csv

v2 differences vs v1 (2026-05-29):
  - Reads working/prescience_scores_27b_passC_v2.csv  (v2 runner output)
  - Reads working/prescience_scores_cloud_review_v2.csv  (cloud reviewer v2)
  - Same 11-column Option α schema (locked 2026-05-25 — DO NOT CHANGE)
  - Same atomic-write + backup pattern
  - Joins against v1.5 _master_observations.csv (17-col v20 schema) for sanity
    checks only — does not modify it

Schema (Option α — locked 2026-05-25):
  obs_id, study_id, model, prescience_score, confidence, rationale,
  scored_at, scorer_version, source_pass, elapsed_sec, parse_ok

Behavior:
  1. Snapshot existing master (if any) to archive_masters_pre_prescience_rollup_v2_<ts>/
  2. Glob all per-study CSVs across --root
  3. Concatenate (deduplicate on (obs_id, model, scorer_version, scored_at))
  4. Cross-check obs_ids against _master_observations.csv (warn on mismatches)
  5. Write _master_prescience_scores.csv with QUOTE_ALL, atomic
  6. Diff: rows added vs. previous master

§16.5 compliant. Forever-archive safe.

NOTE: The pre-v2 abandoned _master_prescience_scores.csv (if any) was
quarantined to _pass_c_abandoned_runs/20260526/ on 2026-05-29. This v2 rollup
starts from an empty master.

Usage:
  python3 roll_up_prescience_to_master_v2.py \\
      --root /Users/scott/Desktop/Archive/prepared \\
      --masters-dir /Users/scott/Desktop/Archive/archive_masters

  # dry-run: print what would be written, don't touch master
  python3 roll_up_prescience_to_master_v2.py --root ... --masters-dir ... --dry-run
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
OBSERVATIONS_MASTER = "_master_observations.csv"

HEADER = [
    "obs_id", "study_id", "model",
    "prescience_score", "confidence", "rationale",
    "scored_at", "scorer_version", "source_pass",
    "elapsed_sec", "parse_ok",
]

# v2 globs (bumped from v1)
PER_STUDY_GLOBS = [
    "working/prescience_scores_27b_passC_v2.csv",
    "working/prescience_scores_cloud_review_v2.csv",
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


def load_obs_master_ids(masters_dir: Path) -> set[str]:
    """Load canonical obs_ids from _master_observations.csv for cross-check."""
    p = masters_dir / OBSERVATIONS_MASTER
    if not p.exists():
        return set()
    ids = set()
    with open(p, encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            oid = row.get("obs_id", "")
            if oid:
                ids.add(oid)
    return ids


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

    # 3. Cross-check obs_ids against _master_observations.csv (v1.5 17-col)
    canonical_obs_ids = load_obs_master_ids(masters_dir)
    if canonical_obs_ids:
        prescience_ids = {r.get("obs_id", "") for r in deduped if r.get("obs_id")}
        orphans = prescience_ids - canonical_obs_ids
        print(f"Cross-check vs {OBSERVATIONS_MASTER}: "
              f"{len(canonical_obs_ids)} canonical obs_ids, "
              f"{len(prescience_ids)} scored obs_ids, "
              f"{len(orphans)} orphans (not in observations master)")
        if orphans:
            print(f"  WARN: {min(5, len(orphans))} sample orphan obs_ids:")
            for oid in list(orphans)[:5]:
                print(f"    - {oid}")
    else:
        print(f"  [info] no {OBSERVATIONS_MASTER} found in masters-dir; "
              f"skipping cross-check")

    # 4. Compare to existing master
    master_path = masters_dir / MASTER_FILENAME
    prev_count = 0
    if master_path.exists():
        prev = load_csv(master_path)
        prev_count = len(prev)
        print(f"Existing master rows: {prev_count}")
    else:
        print(f"No existing master at {master_path} (will create)")

    # Parse-rate summary for the dedup'd set
    if deduped:
        ok = sum(1 for r in deduped if r.get("parse_ok") == "true")
        pct = 100.0 * ok / len(deduped)
        print(f"Parse OK: {ok}/{len(deduped)} ({pct:.1f}%)")

    if args.dry_run:
        print("\nDRY RUN: would write")
        print(f"  → {master_path}  ({len(deduped)} rows)")
        return 0

    # 5. Backup existing master
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%SZ")
    if master_path.exists():
        backup_dir = masters_dir.parent / f"archive_masters_pre_prescience_rollup_v2_{ts}"
        backup_dir.mkdir(exist_ok=True)
        shutil.copy2(master_path, backup_dir / MASTER_FILENAME)
        print(f"Backup: {backup_dir / MASTER_FILENAME}")

    # 6. Write
    atomic_write_csv(master_path, deduped, HEADER)
    print(f"\n✓ Wrote {master_path}")
    print(f"  Rows: {len(deduped)} (delta vs previous: +{len(deduped) - prev_count})")

    # 7. Verify
    written = load_csv(master_path)
    if len(written) != len(deduped):
        sys.exit(f"VERIFY FAIL: wrote {len(deduped)} but read back {len(written)}")
    print(f"✓ Verified: read-back row count matches ({len(written)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
