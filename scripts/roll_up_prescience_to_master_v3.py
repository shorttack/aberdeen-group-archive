#!/usr/bin/env python3
"""
roll_up_prescience_to_master_v3.py
====================================
Roll up the flat Pass C cloud CSV into the 8th master:
  _master_prescience_scores.csv

v3 differences vs v2 (2026-05-30):
  - Reads ONE flat CSV (~/Desktop/Archive/prescience_scores_pass_c_cloud_v1.csv)
    instead of per-study working/ CSVs
  - Maps 8-col cloud schema → 11-col Option α schema
  - Derives study_id by stripping -OBS-NNN suffix from obs_id
  - Sets scorer_version="cloud_v1" and source_pass="pass_c_cloud" for all rows
  - Same atomic-write + backup pattern as v2
  - Same 11-col Option α schema (LOCKED 2026-05-25)

Schema (Option α — locked 2026-05-25):
  obs_id, study_id, model, prescience_score, confidence, rationale,
  scored_at, scorer_version, source_pass, elapsed_sec, parse_ok

Cloud CSV schema (8 cols):
  obs_id, prescience_score, confidence, rationale, model, scored_at,
  elapsed_sec, parse_ok

Behavior:
  1. Load flat cloud CSV
  2. Map columns + derive study_id + add scorer_version/source_pass
  3. Cross-check obs_ids against _master_observations.csv (warn on orphans)
  4. Snapshot existing master (if any) to archive_masters_pre_prescience_rollup_v3_<ts>/
  5. Write _master_prescience_scores.csv with QUOTE_ALL, atomic
  6. Verify read-back row count

§16.5 compliant. Forever-archive safe.

Usage:
  python3 roll_up_prescience_to_master_v3.py \\
      --cloud-csv /Users/scott/Desktop/Archive/prescience_scores_pass_c_cloud_v1.csv \\
      --masters-dir /Users/scott/Desktop/Archive/archive_masters

  # dry-run: print what would be written, don't touch master
  python3 roll_up_prescience_to_master_v3.py \\
      --cloud-csv ... --masters-dir ... --dry-run
"""
from __future__ import annotations
import argparse
import csv
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

QUOTE_ALL = csv.QUOTE_ALL

MASTER_FILENAME = "_master_prescience_scores.csv"
OBSERVATIONS_MASTER = "_master_observations.csv"

# Option α — locked 2026-05-25 — DO NOT CHANGE
HEADER = [
    "obs_id", "study_id", "model",
    "prescience_score", "confidence", "rationale",
    "scored_at", "scorer_version", "source_pass",
    "elapsed_sec", "parse_ok",
]

SCORER_VERSION = "cloud_v1"
SOURCE_PASS = "pass_c_cloud"

# Regex to strip -OBS-NNN from obs_id to derive study_id
OBS_SUFFIX_RE = re.compile(r"-OBS-\d+$")


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


def derive_study_id(obs_id: str) -> str:
    """Strip -OBS-NNN suffix to get study_id."""
    return OBS_SUFFIX_RE.sub("", obs_id)


def map_cloud_row(cloud_row: dict) -> dict:
    """Map an 8-col cloud CSV row to an 11-col Option α row."""
    obs_id = cloud_row.get("obs_id", "")
    return {
        "obs_id":           obs_id,
        "study_id":         derive_study_id(obs_id),
        "model":            cloud_row.get("model", ""),
        "prescience_score": cloud_row.get("prescience_score", ""),
        "confidence":       cloud_row.get("confidence", ""),
        "rationale":        cloud_row.get("rationale", ""),
        "scored_at":        cloud_row.get("scored_at", ""),
        "scorer_version":   SCORER_VERSION,
        "source_pass":      SOURCE_PASS,
        "elapsed_sec":      cloud_row.get("elapsed_sec", ""),
        "parse_ok":         cloud_row.get("parse_ok", ""),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cloud-csv", required=True,
                    help="Path to prescience_scores_pass_c_cloud_v1.csv")
    ap.add_argument("--masters-dir", required=True,
                    help="Directory containing _master_*.csv files")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cloud_csv = Path(args.cloud_csv).resolve()
    masters_dir = Path(args.masters_dir).resolve()
    if not cloud_csv.is_file():
        sys.exit(f"ERROR: --cloud-csv not a file: {cloud_csv}")
    if not masters_dir.is_dir():
        sys.exit(f"ERROR: --masters-dir not a directory: {masters_dir}")

    # 1. Load flat cloud CSV
    print(f"Loading cloud CSV: {cloud_csv}")
    cloud_rows = load_csv(cloud_csv)
    print(f"Cloud rows loaded: {len(cloud_rows)}")

    # 2. Map to Option α schema
    mapped: list[dict] = [map_cloud_row(r) for r in cloud_rows if r.get("obs_id")]
    print(f"Mapped rows: {len(mapped)}")

    # Sanity check on study_id derivation
    sample_studies = sorted({r["study_id"] for r in mapped})
    print(f"Distinct study_ids derived: {len(sample_studies)}")
    print(f"  First 3: {sample_studies[:3]}")
    print(f"  Last 3:  {sample_studies[-3:]}")

    # 3. Cross-check obs_ids against _master_observations.csv
    canonical_obs_ids = load_obs_master_ids(masters_dir)
    if canonical_obs_ids:
        prescience_ids = {r["obs_id"] for r in mapped if r["obs_id"]}
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

    # Parse-rate summary
    if mapped:
        ok = sum(1 for r in mapped if r.get("parse_ok") == "true")
        pct = 100.0 * ok / len(mapped)
        print(f"Parse OK: {ok}/{len(mapped)} ({pct:.1f}%)")

    # Score distribution
    score_counts: dict[str, int] = {}
    for r in mapped:
        s = r.get("prescience_score", "")
        score_counts[s] = score_counts.get(s, 0) + 1
    print("Score distribution:")
    for s in sorted(score_counts.keys()):
        print(f"  {s!r}: {score_counts[s]}")

    if args.dry_run:
        print("\nDRY RUN: would write")
        print(f"  → {master_path}  ({len(mapped)} rows)")
        return 0

    # 5. Backup existing master
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%SZ")
    if master_path.exists():
        backup_dir = masters_dir.parent / f"archive_masters_pre_prescience_rollup_v3_{ts}"
        backup_dir.mkdir(exist_ok=True)
        shutil.copy2(master_path, backup_dir / MASTER_FILENAME)
        print(f"Backup: {backup_dir / MASTER_FILENAME}")

    # 6. Write
    atomic_write_csv(master_path, mapped, HEADER)
    print(f"\n✓ Wrote {master_path}")
    print(f"  Rows: {len(mapped)} (delta vs previous: +{len(mapped) - prev_count})")

    # 7. Verify
    written = load_csv(master_path)
    if len(written) != len(mapped):
        sys.exit(f"VERIFY FAIL: wrote {len(mapped)} but read back {len(written)}")
    print(f"✓ Verified: read-back row count matches ({len(written)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
