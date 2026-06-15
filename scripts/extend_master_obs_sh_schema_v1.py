#!/usr/bin/env python3
"""
extend_master_obs_sh_schema_v1.py — Append 14 short-horizon columns to
_master_observations.csv as empty fields. RUNS BEFORE PROMOTE.

Spec: masters_notes_sh_schema_entry_v1.md
Locked v3: decisions_log_entry_2026_06_15_short_horizon_prescience_v3.md

What this does:
  1. Read _master_observations.csv (17 cols today)
  2. Add the 14 SH columns to the header (appended to the right of legacy_obs_id)
  3. Write empty values for every existing row in the new columns
  4. Atomic write: temp file + rename + SHA256 of before/after
  5. Strict invariant: row count UNCHANGED; obs_id set UNCHANGED;
     pre-existing column values UNCHANGED byte-for-byte

What this does NOT do:
  - Fill values (that's the promote_sh script's job, after calibration GO)
  - Touch _master_prescience_scores.csv (separate file, separate concern)
  - Modify _master_studies.csv

Pre-flight (asserted before write):
  - --master path exists and is readable
  - 17 expected baseline columns present (matches current v20 schema)
  - No SH columns already present (idempotency check — will refuse to extend twice)
  - --backup path either doesn't exist or --force is set

Post-flight (asserted after write):
  - New file has 17 + 14 = 31 columns
  - New file has same row count as input
  - obs_id values in same order, byte-identical to input
  - Pre-existing columns produce identical byte-for-byte dump when filtered

Usage:
  # Dry run (audits only, no write)
  python3 extend_master_obs_sh_schema_v1.py \
    --master ~/Desktop/Archive/aberdeen-group-archive/_master_observations.csv \
    --dry-run

  # Real extend (writes backup + extended master)
  python3 extend_master_obs_sh_schema_v1.py \
    --master ~/Desktop/Archive/aberdeen-group-archive/_master_observations.csv \
    --backup ~/Desktop/Archive/aberdeen-group-archive/_master_observations.csv.pre_sh_schema_bak
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import os
import shutil
import sys
import tempfile
from pathlib import Path

BASELINE_COLS = [
    "obs_id", "study_id", "entity_id", "tech_id",
    "observation_type", "year_observed", "metric_name", "metric_value",
    "confidence", "verification_method", "methodology_code",
    "source_page", "notes", "collection", "thread_tag", "section",
    "legacy_obs_id",
]

SH_COLS = [
    "prescience_3y", "confidence_3y", "rationale_3y",
    "prescience_5y", "confidence_5y", "rationale_5y",
    "windows_diverge", "divergence_note",
    "anchor_year", "anchor_source",
    "scored_at_sh", "scorer_version_sh", "source_pass_sh",
    "raw_response_sh",
]

assert len(SH_COLS) == 14, "spec says 14 SH cols"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def read_header_and_rows(path: Path) -> tuple[list[str], list[dict]]:
    with open(path, newline="") as f:
        rdr = csv.DictReader(f)
        return list(rdr.fieldnames or []), list(rdr)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--master", required=True,
                    help="Path to _master_observations.csv")
    ap.add_argument("--backup", default=None,
                    help="Backup destination (refuses to overwrite unless --force)")
    ap.add_argument("--force", action="store_true",
                    help="Allow backup overwrite")
    ap.add_argument("--dry-run", action="store_true",
                    help="Audit only; no write")
    args = ap.parse_args()

    master = Path(args.master).expanduser()
    if not master.exists():
        sys.exit(f"[fail] master not found: {master}")

    # SHA before
    sha_before = sha256_file(master)
    size_before = master.stat().st_size
    print(f"[pre] {master}")
    print(f"[pre] sha256: {sha_before}")
    print(f"[pre] size:   {size_before} bytes")

    header, rows = read_header_and_rows(master)
    print(f"[pre] cols: {len(header)}  rows: {len(rows)}")

    # Baseline schema check
    if header != BASELINE_COLS:
        # Tolerate quoted-vs-unquoted as long as content is identical
        if set(header) != set(BASELINE_COLS):
            sys.exit(f"[fail] baseline schema mismatch.\n"
                     f"  expected: {BASELINE_COLS}\n"
                     f"  got:      {header}")
        else:
            print(f"[warn] column ORDER differs from canonical; will preserve "
                  f"existing order")

    # Idempotency check
    overlap = set(header) & set(SH_COLS)
    if overlap:
        sys.exit(f"[fail] SH columns already present: {overlap}.\n"
                 f"[fail] Refusing to extend twice. Inspect file or use --force "
                 f"(NOT IMPLEMENTED — manual review required).")

    new_header = header + SH_COLS
    print(f"[plan] new col count: {len(new_header)} ({len(header)} + {len(SH_COLS)})")
    print(f"[plan] new columns appended (right of {header[-1]}):")
    for i, c in enumerate(SH_COLS, 1):
        print(f"  {i:2d}. {c}")

    if args.dry_run:
        print("[dry-run] exiting before write")
        return

    if args.backup:
        backup_path = Path(args.backup).expanduser()
        if backup_path.exists() and not args.force:
            sys.exit(f"[fail] backup exists: {backup_path}. Use --force to overwrite.")
        shutil.copy2(master, backup_path)
        sha_backup = sha256_file(backup_path)
        assert sha_backup == sha_before, "backup mismatch"
        print(f"[backup] {backup_path}  sha={sha_backup}")
    else:
        print("[warn] no --backup specified; you should make one manually")

    # Atomic write: tempfile in same directory, then rename
    tmp_fd, tmp_name = tempfile.mkstemp(prefix=".sh_extend_", suffix=".csv",
                                        dir=str(master.parent))
    os.close(tmp_fd)
    tmp_path = Path(tmp_name)
    empty_sh = {c: "" for c in SH_COLS}
    try:
        with open(tmp_path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=new_header, quoting=csv.QUOTE_ALL)
            w.writeheader()
            for r in rows:
                # Preserve existing fields verbatim; add empty SH cols
                out = {c: r.get(c, "") for c in header}
                out.update(empty_sh)
                w.writerow(out)
        os.replace(tmp_path, master)
    except Exception:
        if tmp_path.exists():
            tmp_path.unlink()
        raise

    # Post-flight verification
    sha_after = sha256_file(master)
    size_after = master.stat().st_size
    new_header2, rows2 = read_header_and_rows(master)
    print(f"[post] sha256: {sha_after}")
    print(f"[post] size:   {size_after} bytes (Δ {size_after - size_before:+d})")
    print(f"[post] cols:   {len(new_header2)}  rows: {len(rows2)}")

    # Invariants
    if len(rows2) != len(rows):
        sys.exit(f"[FAIL] row count changed: {len(rows)} → {len(rows2)}")
    if new_header2 != new_header:
        sys.exit(f"[FAIL] header mismatch post-write")
    # obs_id order preserved
    ids_before = [r["obs_id"] for r in rows]
    ids_after = [r["obs_id"] for r in rows2]
    if ids_before != ids_after:
        sys.exit(f"[FAIL] obs_id order/values changed")
    # Pre-existing columns byte-identical
    for i, (r_old, r_new) in enumerate(zip(rows, rows2)):
        for c in header:
            if r_old.get(c, "") != r_new.get(c, ""):
                sys.exit(f"[FAIL] row {i} col {c}: "
                         f"{r_old.get(c)!r} → {r_new.get(c)!r}")
        for c in SH_COLS:
            if r_new.get(c, "") != "":
                sys.exit(f"[FAIL] row {i} SH col {c} non-empty: "
                         f"{r_new.get(c)!r}")
    print(f"[ok] all invariants pass")
    print(f"[done] master extended: {len(rows)} rows × {len(new_header)} cols")


if __name__ == "__main__":
    main()
