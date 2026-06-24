#!/usr/bin/env python3
"""
apply_passb_reconcile_v2.py
============================

v2 (2026-06-13): upgraded DECtp importance_rationale and relevance_rationale
to cite the actual presenters (Olsen, Glorioso, Hughes), the actual methodology
(debit-credit benchmark), and the four-pillar framing tied to 2026 practice.
No other rows changed from v1.

v1 history:

Pass B reconciliation — resolve the 4 [DEFERRED] prescience rows and fix the
DECtp empty-importance/empty-relevance silent ingest bug.

Updates 5 rows in `_master_studies.csv` using REPLACE-by-study_id pattern.
Touches only these 7 columns per row: importance, importance_rationale,
relevance, relevance_rationale, prescience, prescience_rationale.

Per kastner-archive-pipeline skill invariants:
  - csv.QUOTE_ALL on write
  - timestamped backup before write
  - dry-run default; --commit opt-in
  - row count preserved (1452 in, 1452 out)
  - column count preserved (16 in, 16 out)

Per archival-ingest §16 (CSV Validation Gate):
  - importance ∈ {high, medium, low}
  - relevance ∈ {high, medium, low}
  - prescience ∈ {high, medium, low, not-applicable, [DEFERRED]}
  - All values are lowercase
  - License field on every row remains "CC-BY-4.0"

Usage:
    python3 apply_passb_reconcile_v2.py                 # dry-run
    python3 apply_passb_reconcile_v2.py --commit        # write

Author: agent
Date:   2026-06-13
"""

import csv
import datetime
import shutil
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ARCHIVE_DIR = Path.home() / "Desktop" / "Archive" / "aberdeen-group-archive"
MASTER      = ARCHIVE_DIR / "_master_studies.csv"
MANIFEST    = Path(__file__).parent / "_master_studies_passb_reconcile_v2.csv"

UPDATE_COLS = [
    "importance",
    "importance_rationale",
    "relevance",
    "relevance_rationale",
    "prescience",
    "prescience_rationale",
]

EXPECTED_TARGETS = {
    "dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836",
    "oracle-data-warehousing-launch-multimedia-spatial-d63644",
    "crossroads-launch-front-back-office-integration-508c58",
    "crossroads-june-1997-launch-variant-cut-caea12",
    "tandem-himalayan-airport-commercial-tpc-c-0b1c60",
}

VALID_IMPORTANCE = {"high", "medium", "low"}
VALID_RELEVANCE  = {"high", "medium", "low"}
VALID_PRESCIENCE = {"high", "medium", "low", "not-applicable", "[DEFERRED]"}

# ---------------------------------------------------------------------------
# Load manifest
# ---------------------------------------------------------------------------

def load_manifest(path: Path) -> dict[str, dict[str, str]]:
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        manifest = {}
        for row in reader:
            sid = row["study_id"]
            manifest[sid] = {k: row[k] for k in UPDATE_COLS}
    return manifest

# ---------------------------------------------------------------------------
# Pre-flight validation (gate before write)
# ---------------------------------------------------------------------------

def validate_manifest(manifest: dict[str, dict[str, str]]) -> list[str]:
    errs = []
    target_set = set(manifest.keys())
    if target_set != EXPECTED_TARGETS:
        missing = EXPECTED_TARGETS - target_set
        extra   = target_set - EXPECTED_TARGETS
        if missing:
            errs.append(f"Manifest missing expected study_ids: {missing}")
        if extra:
            errs.append(f"Manifest has unexpected study_ids: {extra}")
    for sid, row in manifest.items():
        if row["importance"] not in VALID_IMPORTANCE:
            errs.append(f"{sid}: invalid importance={row['importance']!r}")
        if row["relevance"] not in VALID_RELEVANCE:
            errs.append(f"{sid}: invalid relevance={row['relevance']!r}")
        if row["prescience"] not in VALID_PRESCIENCE:
            errs.append(f"{sid}: invalid prescience={row['prescience']!r}")
        for col in ("importance_rationale", "relevance_rationale", "prescience_rationale"):
            if not row[col].strip():
                errs.append(f"{sid}: empty {col}")
    return errs

# ---------------------------------------------------------------------------
# Apply
# ---------------------------------------------------------------------------

def main():
    commit = "--commit" in sys.argv

    if not MASTER.exists():
        sys.exit(f"FATAL: master not found: {MASTER}")
    if not MANIFEST.exists():
        sys.exit(f"FATAL: manifest not found: {MANIFEST}")

    print(f"Mode:     {'COMMIT' if commit else 'DRY-RUN'}")
    print(f"Master:   {MASTER}")
    print(f"Manifest: {MANIFEST}")
    print()

    # Load
    manifest = load_manifest(MANIFEST)
    errs = validate_manifest(manifest)
    if errs:
        print("Manifest validation FAILED:")
        for e in errs:
            print(f"  - {e}")
        sys.exit(1)
    print(f"Manifest valid: {len(manifest)} rows, all enum values OK")

    # Read master
    with open(MASTER, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    if "study_id" not in header:
        sys.exit("FATAL: master missing study_id column")
    col_idx = {c: i for i, c in enumerate(header)}
    sid_idx = col_idx["study_id"]

    print(f"Master rows BEFORE: {len(rows)} (header: {len(header)} cols)")

    # Apply
    applied = []
    not_found = set(manifest.keys())
    for r in rows:
        sid = r[sid_idx]
        if sid in manifest:
            before = {c: r[col_idx[c]] for c in UPDATE_COLS}
            for c in UPDATE_COLS:
                r[col_idx[c]] = manifest[sid][c]
            after = {c: r[col_idx[c]] for c in UPDATE_COLS}
            applied.append((sid, before, after))
            not_found.discard(sid)

    print(f"Rows updated:       {len(applied)}")
    if not_found:
        print(f"  WARNING — study_ids in manifest but not in master: {not_found}")

    print(f"Master rows AFTER:  {len(rows)} (header: {len(header)} cols)")

    # Per-row preview
    print()
    print("=" * 78)
    print("PER-ROW CHANGES")
    print("=" * 78)
    for sid, before, after in applied:
        print(f"\n  {sid}")
        for c in ("importance", "relevance", "prescience"):
            if before[c] != after[c]:
                print(f"    {c:12s}: {before[c]!r} -> {after[c]!r}")
            else:
                print(f"    {c:12s}: {after[c]!r} (unchanged)")

    # Invariant: row count preserved
    if len(rows) != 1452:
        sys.exit(f"FATAL: row count drift — expected 1452, got {len(rows)}")
    if len(header) != 16:
        sys.exit(f"FATAL: column count drift — expected 16, got {len(header)}")
    if len(applied) != 5:
        sys.exit(f"FATAL: expected 5 applies, got {len(applied)}")

    if not commit:
        print()
        print("DRY-RUN only — pass --commit to write.")
        return

    # Backup
    ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    bak = MASTER.with_suffix(f".csv.bak_passb_reconcile_v2_{ts}")
    shutil.copy2(MASTER, bak)
    print(f"\nBackup: {bak}")

    # Write
    with open(MASTER, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        w.writerows(rows)
    print(f"Wrote:  {MASTER}")

    # Audit trail
    audit = MASTER.parent / f"passb_reconcile_v2_applied_{ts}.txt"
    with open(audit, "w", encoding="utf-8") as f:
        f.write(f"Pass B reconciliation v2 applied {ts}\n")
        f.write(f"Master: {MASTER}\n")
        f.write(f"Backup: {bak}\n")
        f.write(f"Rows updated: {len(applied)}\n\n")
        for sid, before, after in applied:
            f.write(f"{sid}\n")
            for c in UPDATE_COLS:
                if before[c] != after[c]:
                    f.write(f"  {c}: {before[c]!r} -> {after[c]!r}\n")
            f.write("\n")
    print(f"Audit:  {audit}")

if __name__ == "__main__":
    main()
