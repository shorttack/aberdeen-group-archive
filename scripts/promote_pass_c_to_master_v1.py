#!/usr/bin/env python3
"""
promote_pass_c_to_master_v1.py
==============================

Promote rows from the LIVE Pass C output CSV (file 1) into the archive repo root
prescience scores CSV (file 2, which is v3's input).

File 1: ~/Desktop/Archive/prescience_scores_pass_c_cloud_v1.csv
        cols: obs_id, prescience_score, confidence, rationale, model,
              scored_at, elapsed_sec, parse_ok                          (8)

File 2: ~/Desktop/Archive/aberdeen-group-archive/_master_prescience_scores.csv
        cols: obs_id, study_id, model, prescience_score, confidence,
              rationale, scored_at, scorer_version, source_pass,
              elapsed_sec, parse_ok                                     (11)

Derived columns for file 2:
  study_id        : looked up from _master_observations.csv (obs_id -> study_id)
  scorer_version  : default 'pass_c_cloud_v1' (override with --scorer-version)
  source_pass     : default 'C'              (override with --source-pass)

Behavior:
  - Append-only. Existing rows in file 2 are never modified.
  - Dedupe on obs_id: any obs_id already present in file 2 is SKIPPED.
  - Backs up file 2 before any write.
  - --dry-run prints counts and a sample of would-be-appended rows.
  - --commit performs the write.

Usage:
    python3 promote_pass_c_to_master_v1.py --dry-run
    python3 promote_pass_c_to_master_v1.py --commit

Exit codes:
    0 success (dry-run or commit)
    1 input validation failure
    2 obs_id without study_id mapping (will list offenders)
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import shutil
import sys
from pathlib import Path

HOME = Path.home()
ARCH = HOME / "Desktop" / "Archive"
REPO = ARCH / "aberdeen-group-archive"
ARCH_MASTERS = ARCH / "aberdeen-group-archive"

FILE1 = ARCH / "prescience_scores_pass_c_cloud_v1.csv"
FILE2 = ARCH_MASTERS / "_master_prescience_scores.csv"
OBS_MASTER = ARCH_MASTERS / "_master_observations.csv"

FILE2_COLS = [
    "obs_id", "study_id", "model", "prescience_score", "confidence",
    "rationale", "scored_at", "scorer_version", "source_pass",
    "elapsed_sec", "parse_ok",
]


def load_obs_to_study(path: Path) -> dict[str, str]:
    """obs_id -> study_id from the observation master."""
    m: dict[str, str] = {}
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        if "obs_id" not in r.fieldnames or "study_id" not in r.fieldnames:
            sys.stderr.write(
                f"FATAL: {path} missing obs_id or study_id. "
                f"Fields: {r.fieldnames}\n"
            )
            sys.exit(1)
        for row in r:
            oid = row["obs_id"]
            sid = row["study_id"]
            if oid and sid:
                m[oid] = sid
    return m


def load_existing_obs_ids(path: Path) -> set[str]:
    s: set[str] = set()
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            oid = row.get("obs_id")
            if oid:
                s.add(oid)
    return s


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--commit", action="store_true")
    ap.add_argument("--scorer-version", default="pass_c_cloud_v1")
    ap.add_argument("--source-pass", default="C")
    ap.add_argument("--sample", type=int, default=5,
                    help="Rows to preview in dry-run")
    args = ap.parse_args()

    if args.dry_run == args.commit:
        sys.stderr.write("Pick exactly one of --dry-run or --commit.\n")
        return 1

    for p in (FILE1, FILE2, OBS_MASTER):
        if not p.exists():
            sys.stderr.write(f"FATAL: missing {p}\n")
            return 1

    obs_to_study = load_obs_to_study(OBS_MASTER)
    existing = load_existing_obs_ids(FILE2)

    new_rows: list[dict[str, str]] = []
    missing_study: list[str] = []
    skipped_existing = 0
    seen_in_file1 = 0

    with open(FILE1, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        f1_fields = r.fieldnames or []
        required = {"obs_id", "prescience_score", "confidence", "rationale",
                    "model", "scored_at", "elapsed_sec", "parse_ok"}
        if not required.issubset(set(f1_fields)):
            sys.stderr.write(
                f"FATAL: file 1 missing columns. Have: {f1_fields}\n"
            )
            return 1
        for row in r:
            seen_in_file1 += 1
            oid = row["obs_id"]
            if not oid:
                continue
            if oid in existing:
                skipped_existing += 1
                continue
            sid = obs_to_study.get(oid)
            if not sid:
                missing_study.append(oid)
                continue
            new_rows.append({
                "obs_id":           oid,
                "study_id":         sid,
                "model":            row["model"],
                "prescience_score": row["prescience_score"],
                "confidence":       row["confidence"],
                "rationale":        row["rationale"],
                "scored_at":        row["scored_at"],
                # Preserve provenance carried in the CSV (Tier A retag, parse-fail tagging,
                # row-class markers). Fall back to CLI defaults only when row is empty.
                # Patch applied 2026-06-15 (§11v audit F2); originally inline-fixed by Pete
                # during Tier A promote (commit c587fee6, 2026-06-15 ~05:00 EDT).
                "scorer_version":   row.get("scorer_version") or args.scorer_version,
                "source_pass":      row.get("source_pass") or args.source_pass,
                "elapsed_sec":      row["elapsed_sec"],
                "parse_ok":         row["parse_ok"],
            })

    print(f"file1 rows scanned   : {seen_in_file1}")
    print(f"file2 rows existing  : {len(existing)}")
    print(f"would skip (dupe oid): {skipped_existing}")
    print(f"would append (new)   : {len(new_rows)}")
    print(f"missing study_id     : {len(missing_study)}")

    if missing_study:
        sys.stderr.write(
            "FATAL: the following obs_ids in file 1 have no study_id in "
            "_master_observations.csv:\n"
        )
        for oid in missing_study[:25]:
            sys.stderr.write(f"  {oid}\n")
        if len(missing_study) > 25:
            sys.stderr.write(f"  ... and {len(missing_study) - 25} more\n")
        return 2

    if args.dry_run:
        print("\n--- sample (would append) ---")
        for row in new_rows[: args.sample]:
            print({k: row[k] for k in ("obs_id", "study_id",
                                       "prescience_score", "scorer_version",
                                       "source_pass")})
        # per-study count of new rows (helps confirm the 57 we care about)
        by_study: dict[str, int] = {}
        for row in new_rows:
            by_study[row["study_id"]] = by_study.get(row["study_id"], 0) + 1
        print("\n--- new rows by study_id (top 20) ---")
        for sid, n in sorted(by_study.items(), key=lambda kv: -kv[1])[:20]:
            print(f"  {n:5d}  {sid}")
        print("\nDRY RUN — no files written.")
        return 0

    # COMMIT
    ts = dt.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    backup = FILE2.with_suffix(FILE2.suffix + f".bak_pre_promote_{ts}")
    shutil.copy2(FILE2, backup)
    print(f"backup: {backup}")

    # Append
    with open(FILE2, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FILE2_COLS, quoting=csv.QUOTE_ALL)
        for row in new_rows:
            w.writerow(row)

    print(f"appended {len(new_rows)} rows to {FILE2}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
