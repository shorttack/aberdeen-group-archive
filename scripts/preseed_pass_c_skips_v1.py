#!/usr/bin/env python3
"""
preseed_pass_c_skips_v1.py

Pre-seeds prescience_scores_pass_c_cloud_v1.csv with no-op rows for the 253
observations from the 16 skip-studies (yesterday's transcripts minus the 2
DECtp studies). This causes run_prescience_pass_c_v5.py's resume logic
(load_already_scored) to skip them, so Pass C only API-calls the 68 DECtp obs.

INPUTS:
  /tmp/skip_obs_ids.csv                                  (253 rows, obs_id,study_id)
  ~/Desktop/Archive/prescience_scores_pass_c_cloud_v1.csv (existing 3,761 rows)
  ~/Desktop/Archive/archive_masters/_master_studies.csv  (for in-thread prescience preservation)

OUTPUTS (backups + append):
  ~/Desktop/Archive/prescience_scores_pass_c_cloud_v1.csv.bak_pre_dectp_preseed_<UTC>.csv
  ~/Desktop/Archive/archive_masters/_master_studies.csv.bak_pre_passC_dectp_<UTC>.csv
  ~/Desktop/Archive/prescience_scores_pass_c_cloud_v1.csv  (extended +253 rows = 4,014)

Preseed row schema (matches existing output CSV header):
  obs_id              : <study_id>-OBS-NNN
  prescience_score    : ""  (no numeric — these are skips, not scores)
  confidence          : ""
  rationale           : "preseed_skip: in-thread Pass B prescience preserved per Pete 2026-06-13"
  model               : "preseed_skip_v1"
  scored_at           : <run UTC timestamp>
  elapsed_sec         : "0.0"
  parse_ok            : "true"

csv.QUOTE_ALL per archival-ingest v20 §16.

Usage:
  python3 preseed_pass_c_skips_v1.py --dry-run   # report row counts + first/last preseed rows
  python3 preseed_pass_c_skips_v1.py --apply     # do the backups + append
"""

import argparse
import csv
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ARCHIVE = Path.home() / "Desktop" / "Archive"
MASTERS = ARCHIVE / "archive_masters"
PASS_C_CSV = ARCHIVE / "prescience_scores_pass_c_cloud_v1.csv"
MASTER_STUDIES = MASTERS / "_master_studies.csv"
SKIP_OBS_FILE = Path("/tmp/skip_obs_ids.csv")

HEADER = ["obs_id", "prescience_score", "confidence", "rationale",
          "model", "scored_at", "elapsed_sec", "parse_ok"]

PRESEED_RATIONALE = "preseed_skip: in-thread Pass B prescience preserved per Pete 2026-06-13"
PRESEED_MODEL = "preseed_skip_v1"


def utc_stamp():
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def load_skip_obs_ids():
    """Read /tmp/skip_obs_ids.csv (headerless: obs_id,study_id)."""
    if not SKIP_OBS_FILE.exists():
        sys.exit(f"ERROR: {SKIP_OBS_FILE} not found. Regenerate via duckdb query.")
    out = []
    with SKIP_OBS_FILE.open(newline="", encoding="utf-8") as f:
        rdr = csv.reader(f)
        for row in rdr:
            if len(row) >= 1 and row[0].strip():
                out.append(row[0].strip())
    return out


def load_existing_obs_ids():
    """Read obs_id column from existing Pass C CSV."""
    if not PASS_C_CSV.exists():
        sys.exit(f"ERROR: {PASS_C_CSV} not found.")
    out = set()
    with PASS_C_CSV.open(newline="", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        for row in rdr:
            out.add(row["obs_id"])
    return out


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    apply_ = args.apply

    stamp = utc_stamp()
    print(f"=== preseed_pass_c_skips_v1.py ({'APPLY' if apply_ else 'DRY-RUN'}) ===")
    print(f"timestamp: {stamp}")
    print(f"Pass C CSV: {PASS_C_CSV}")
    print(f"Master studies: {MASTER_STUDIES}")
    print(f"Skip obs file: {SKIP_OBS_FILE}")

    skip_ids = load_skip_obs_ids()
    print(f"skip obs_ids loaded: {len(skip_ids)}")

    existing = load_existing_obs_ids()
    print(f"existing rows in Pass C CSV: {len(existing)}")

    # Identify new vs already-present
    new_ids = [oid for oid in skip_ids if oid not in existing]
    dup_ids = [oid for oid in skip_ids if oid in existing]
    print(f"  already present (would skip): {len(dup_ids)}")
    print(f"  to append: {len(new_ids)}")

    if dup_ids:
        print(f"  sample dups: {dup_ids[:3]}")

    if new_ids:
        print(f"  sample new (first 3):")
        for oid in new_ids[:3]:
            print(f"    {oid}")
        print(f"  sample new (last 2):")
        for oid in new_ids[-2:]:
            print(f"    {oid}")

    if not apply_:
        print()
        print("Re-run with --apply to: backup both CSVs + append new preseed rows.")
        return 0

    # --- APPLY ---
    # 1. Backup Pass C CSV
    bak_passc = PASS_C_CSV.with_suffix(f".csv.bak_pre_dectp_preseed_{stamp}.csv")
    shutil.copy2(PASS_C_CSV, bak_passc)
    print(f"backed up Pass C CSV -> {bak_passc}")

    # 2. Backup master studies
    bak_studies = MASTER_STUDIES.with_suffix(f".csv.bak_pre_passC_dectp_{stamp}.csv")
    shutil.copy2(MASTER_STUDIES, bak_studies)
    print(f"backed up _master_studies.csv -> {bak_studies}")

    # 3. Append preseed rows
    scored_at = datetime.now(timezone.utc).isoformat()
    appended = 0
    with PASS_C_CSV.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HEADER, quoting=csv.QUOTE_ALL)
        for oid in new_ids:
            w.writerow({
                "obs_id": oid,
                "prescience_score": "",
                "confidence": "",
                "rationale": PRESEED_RATIONALE,
                "model": PRESEED_MODEL,
                "scored_at": scored_at,
                "elapsed_sec": "0.0",
                "parse_ok": "true",
            })
            appended += 1
    print(f"appended {appended} preseed rows")

    # 4. Verify
    final = load_existing_obs_ids()
    print(f"final row count in Pass C CSV (unique obs_ids): {len(final)}")
    print(f"expected: {len(existing) + appended}")
    if len(final) != len(existing) + appended:
        print("WARN: row-count mismatch — investigate duplicates.")

    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
