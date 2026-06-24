#!/usr/bin/env python3
"""
ingest_transcript_studies_v1.py

§11u-cont Pass A — Manifest-driven ingest of N new transcript study rows into
_master_studies.csv. Designed for the 17 Kastner-on-camera transcripts
(2026-06-12 batch) but generalized so future transcript batches use the same
mechanism: drop a manifest CSV with the master_studies schema, run dry-run,
review, then --commit.

Behavior:
  - Reads --master (_master_studies.csv) and --manifest (manifest CSV matching
    the master schema exactly, 16 columns in the canonical order).
  - Validates: column-order match, manifest study_ids unique, no manifest
    study_id collides with an existing master study_id, no manifest source_file
    collides with an existing master source_file.
  - Appends manifest rows to the master.
  - Writes a timestamped backup before mutating (`.bak_<reason>_<utc>Z`).
  - Default mode is DRY-RUN. Pass --commit to actually write.
  - All writes use csv.QUOTE_ALL (per archive §16.5).
  - Reports row-count delta and prints first/last appended study_id.

Usage (Mac):
  python3 ~/Desktop/Archive/scripts/ingest_transcript_studies_v1.py \\
    --master ~/Desktop/Archive/aberdeen-group-archive/_master_studies.csv \\
    --manifest ~/Desktop/Archive/scripts/transcript_manifest_v1.csv

  python3 ~/Desktop/Archive/scripts/ingest_transcript_studies_v1.py \\
    --master ~/Desktop/Archive/aberdeen-group-archive/_master_studies.csv \\
    --manifest ~/Desktop/Archive/scripts/transcript_manifest_v1.csv \\
    --commit

After --commit, run Phase 1 + Phase 2 to refresh the live DuckDB:
  python3 ~/Desktop/Archive/scripts/build/01_load_csvs_v2.py \\
    --archive ~/Desktop/Archive/aberdeen-group-archive \\
    --wiki ~/Repos/kastner-aberdeen-wiki
  python3 ~/Desktop/Archive/scripts/build/02_build_data_layer_v4.py \\
    --wiki ~/Repos/kastner-aberdeen-wiki

Author: Sandbox agent + Pete Kastner
Date:   2026-06-12
Version: v1
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import shutil
import sys
from pathlib import Path

EXPECTED_HEADER = [
    "study_id",
    "title",
    "author",
    "date",
    "type",
    "subject_domain",
    "methodology",
    "source_file",
    "abstract",
    "license",
    "importance",
    "importance_rationale",
    "relevance",
    "relevance_rationale",
    "prescience",
    "prescience_rationale",
]

REASON_SLUG = "ingest_transcript_studies"


def utc_stamp() -> str:
    """UTC timestamp in compact form: YYYYMMDDTHHMMSSZ."""
    # Avoids datetime.utcnow() DeprecationWarning by using timezone-aware now.
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def read_csv_dict(path: Path) -> tuple[list[str], list[dict]]:
    """Read a CSV file; return (header, list of row-dicts). Preserves order."""
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        header = list(reader.fieldnames or [])
        rows = list(reader)
    return header, rows


def validate_header(label: str, header: list[str]) -> None:
    """Header must match EXPECTED_HEADER exactly (order + names)."""
    if header != EXPECTED_HEADER:
        print(f"ERROR: {label} header does not match canonical master_studies schema.")
        print(f"  Expected ({len(EXPECTED_HEADER)} cols): {EXPECTED_HEADER}")
        print(f"  Got      ({len(header)} cols): {header}")
        sys.exit(2)


def validate_no_collisions(
    master_rows: list[dict], manifest_rows: list[dict]
) -> None:
    """
    Enforce three invariants:
      1. Manifest study_ids are unique within the manifest.
      2. No manifest study_id collides with an existing master study_id.
      3. No manifest source_file collides with an existing master source_file.
    """
    # 1. Manifest internal uniqueness
    manifest_ids = [r["study_id"] for r in manifest_rows]
    dup_ids = {x for x in manifest_ids if manifest_ids.count(x) > 1}
    if dup_ids:
        print(f"ERROR: Duplicate study_id within manifest: {sorted(dup_ids)}")
        sys.exit(3)

    manifest_sfs = [r["source_file"] for r in manifest_rows]
    dup_sfs = {x for x in manifest_sfs if manifest_sfs.count(x) > 1}
    if dup_sfs:
        print(f"ERROR: Duplicate source_file within manifest: {sorted(dup_sfs)}")
        sys.exit(3)

    # 2. Master-vs-manifest study_id collision
    master_ids = {r["study_id"] for r in master_rows}
    coll_ids = sorted(set(manifest_ids) & master_ids)
    if coll_ids:
        print(f"ERROR: Manifest study_id(s) already in master:")
        for sid in coll_ids:
            print(f"  - {sid}")
        sys.exit(4)

    # 3. Master-vs-manifest source_file collision
    master_sfs = {r["source_file"] for r in master_rows}
    coll_sfs = sorted(set(manifest_sfs) & master_sfs)
    if coll_sfs:
        print(f"ERROR: Manifest source_file(s) already in master:")
        for sf in coll_sfs:
            print(f"  - {sf}")
        sys.exit(5)


def make_backup(master_path: Path, reason: str) -> Path:
    """Copy master CSV to .bak_<reason>_<utc>Z sibling. Return the backup path."""
    stamp = utc_stamp()
    bak = master_path.with_name(f"{master_path.name}.bak_{reason}_{stamp}")
    shutil.copy2(master_path, bak)
    return bak


def write_master(master_path: Path, header: list[str], rows: list[dict]) -> None:
    """Write master with csv.QUOTE_ALL. Use the canonical header order."""
    with open(master_path, "w", newline="") as f:
        w = csv.DictWriter(
            f, fieldnames=header, quoting=csv.QUOTE_ALL, extrasaction="raise"
        )
        w.writeheader()
        for r in rows:
            w.writerow(r)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Append manifest rows to _master_studies.csv."
    )
    ap.add_argument(
        "--master",
        type=Path,
        required=True,
        help="Path to _master_studies.csv (the file to mutate).",
    )
    ap.add_argument(
        "--manifest",
        type=Path,
        required=True,
        help="Path to manifest CSV (must match master_studies schema exactly).",
    )
    ap.add_argument(
        "--commit",
        action="store_true",
        help="Actually write. Without this flag, runs as a dry-run only.",
    )
    args = ap.parse_args()

    if not args.master.is_file():
        print(f"ERROR: master not found: {args.master}")
        return 10
    if not args.manifest.is_file():
        print(f"ERROR: manifest not found: {args.manifest}")
        return 11

    # ---- Read both ----
    print(f"Reading master:   {args.master}")
    master_header, master_rows = read_csv_dict(args.master)
    print(f"  rows: {len(master_rows)}, cols: {len(master_header)}")

    print(f"Reading manifest: {args.manifest}")
    manifest_header, manifest_rows = read_csv_dict(args.manifest)
    print(f"  rows: {len(manifest_rows)}, cols: {len(manifest_header)}")

    # ---- Validate ----
    validate_header("master", master_header)
    validate_header("manifest", manifest_header)
    validate_no_collisions(master_rows, manifest_rows)
    print("Validation: PASS (schema match, no study_id or source_file collisions)")

    # ---- Build new master ----
    new_rows = master_rows + manifest_rows
    expected_total = len(master_rows) + len(manifest_rows)
    if len(new_rows) != expected_total:
        print(
            f"ERROR: row-count arithmetic failed: "
            f"{len(master_rows)} + {len(manifest_rows)} != {len(new_rows)}"
        )
        return 20

    print()
    print(f"Mode: {'COMMIT' if args.commit else 'DRY-RUN'}")
    print(f"  master before: {len(master_rows)} rows")
    print(f"  manifest:      +{len(manifest_rows)} rows")
    print(f"  master after:  {len(new_rows)} rows")
    print(f"  first appended study_id: {manifest_rows[0]['study_id']}")
    print(f"  last  appended study_id: {manifest_rows[-1]['study_id']}")

    if not args.commit:
        print()
        print("DRY-RUN only — no files written. Pass --commit to apply.")
        return 0

    # ---- Backup, then write ----
    bak = make_backup(args.master, REASON_SLUG)
    print(f"Backup written: {bak}")

    write_master(args.master, EXPECTED_HEADER, new_rows)
    print(f"Wrote: {args.master}")

    # ---- Read-back verification ----
    _, verify_rows = read_csv_dict(args.master)
    if len(verify_rows) != expected_total:
        print(
            f"ERROR: post-write read-back row count mismatch: "
            f"expected {expected_total}, got {len(verify_rows)}"
        )
        return 21
    tail_ids = {r["study_id"] for r in verify_rows[-len(manifest_rows):]}
    manifest_ids = {r["study_id"] for r in manifest_rows}
    if tail_ids != manifest_ids:
        print("ERROR: post-write read-back tail study_ids do not match manifest.")
        print(f"  expected: {sorted(manifest_ids)}")
        print(f"  got:      {sorted(tail_ids)}")
        return 22
    print(f"Read-back verification: PASS ({len(verify_rows)} rows, tail matches manifest)")

    print()
    print("Next steps:")
    print("  1. Run Phase 1 (01_load_csvs_v2.py) to derive enriched parquets.")
    print("  2. Run Phase 2 (02_build_data_layer_v4.py) to rebuild DuckDB views.")
    print("  3. Run the shape audit and confirm studies count = master row count.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
