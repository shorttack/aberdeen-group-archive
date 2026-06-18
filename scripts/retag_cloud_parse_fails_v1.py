#!/usr/bin/env python3
"""
retag_cloud_parse_fails_v1.py

F6 resolution (v1.7.0 ship gate): retag the 12 cloud parse-fails so
their `source_pass` matches the sonar parse-fail convention.

Before:
  - 52 rows: source_pass='pass_c_sonar_v1_parse_fail', parse_ok=true (split)
  - 12 rows: source_pass='pass_c_cloud', parse_ok=false (in-band)

After:
  - 52 rows: source_pass='pass_c_sonar_v1_parse_fail' (unchanged)
  - 12 rows: source_pass='pass_c_cloud_parse_fail', parse_ok=false (retagged)

Rationale: every "how many parse failures?" query today needs
`parse_ok=false OR source_pass LIKE '%parse_fail'`. After F6, the
source_pass column alone is sufficient. Driver v8 will write SH
parse-fails to `pass_c_sh_parse_fail` from day 1.

Note: F6 does NOT change `parse_ok` — the 12 cloud rows keep
parse_ok=false because that IS still accurate (parsing did fail).
After F3 (row_class), parse_ok becomes informational rather than
load-bearing in queries.

ORDER OF OPERATIONS: run AFTER F3 (add_row_class_to_prescience_scores_v1.py)
so the row_class column is already present when this script runs.
The row_class for these 12 rows is 'parse_fail' (unchanged by retag).

Invariants enforced:
- Dry-run default; --commit opt-in
- csv.QUOTE_ALL on write
- Backup before write: _master_prescience_scores.csv.bak_retag_cloud_pf_<utc>Z
- Row count preserved (exactly 8,440)
- Exactly 12 rows touched (hard-fail if drift)
- No other columns modified

Author: Perplexity Computer.
Date: 2026-06-18 (v1.7.0 ship-gate F6 close).
Pairs with: F3 (add_row_class) and F7 (docs only).
"""

import csv
import sys
import shutil
import datetime
from pathlib import Path

ARCHIVE = Path.home() / "Desktop" / "Archive" / "archive_masters"
MASTER = ARCHIVE / "_master_prescience_scores.csv"

EXPECTED_TOTAL = 8440
EXPECTED_TOUCH = 12

OLD_SP = "pass_c_cloud"
NEW_SP = "pass_c_cloud_parse_fail"


def main():
    commit = "--commit" in sys.argv

    if not MASTER.exists():
        sys.exit(f"ERROR: master not found at {MASTER}")

    # --- read ---
    with open(MASTER, newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    if "parse_ok" not in header or "source_pass" not in header:
        sys.exit("ERROR: master missing parse_ok or source_pass column")

    n_rows = len(rows)
    if n_rows != EXPECTED_TOTAL:
        sys.exit(f"ERROR: expected {EXPECTED_TOTAL} rows, found {n_rows}")

    sp_idx = header.index("source_pass")
    po_idx = header.index("parse_ok")

    # --- identify targets ---
    targets = []
    for i, r in enumerate(rows):
        if r[sp_idx] == OLD_SP and r[po_idx].strip().lower() == "false":
            targets.append(i)

    n_touched = len(targets)
    print(f"Mode: {'COMMIT' if commit else 'DRY-RUN'}")
    print(f"Master: {MASTER}")
    print(f"Total rows: {n_rows}")
    print(f"Rows to retag: {n_touched} (expected {EXPECTED_TOUCH})")
    print(f"  rule: source_pass='{OLD_SP}' AND parse_ok='false'")
    print(f"  action: source_pass -> '{NEW_SP}' (parse_ok unchanged)")

    if n_touched != EXPECTED_TOUCH:
        sys.exit(
            f"ERROR: expected to touch {EXPECTED_TOUCH} rows, found {n_touched}. "
            f"Baseline drift; re-audit before applying."
        )

    print(f"\nTarget row indices (0-based): {targets}")
    if not commit:
        # Show preview of first 3 targets
        print(f"\nPreview (first 3 of {n_touched}):")
        for i in targets[:3]:
            r = rows[i]
            obs_id_idx = header.index("obs_id") if "obs_id" in header else None
            obs_id = r[obs_id_idx] if obs_id_idx is not None else "(no obs_id col)"
            print(f"  row {i}: obs_id={obs_id!r}, source_pass={r[sp_idx]!r} -> {NEW_SP!r}")
        print("\nDRY-RUN only. Pass --commit to write.")
        return

    # --- apply ---
    for i in targets:
        rows[i][sp_idx] = NEW_SP

    # --- backup ---
    ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    bak = MASTER.with_suffix(f".csv.bak_retag_cloud_pf_{ts}")
    shutil.copy2(MASTER, bak)
    print(f"\nBackup: {bak}")

    # --- write ---
    with open(MASTER, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        w.writerows(rows)

    # --- verify ---
    with open(MASTER, newline="") as f:
        reader = csv.reader(f)
        v_header = next(reader)
        v_rows = list(reader)

    if len(v_rows) != n_rows:
        sys.exit(f"ERROR: post-write row count mismatch: {n_rows} -> {len(v_rows)}")

    v_sp_idx = v_header.index("source_pass")
    v_count = sum(1 for r in v_rows if r[v_sp_idx] == NEW_SP)
    if v_count != EXPECTED_TOUCH:
        sys.exit(f"ERROR: post-write '{NEW_SP}' count: {v_count}, expected {EXPECTED_TOUCH}")

    print(f"Wrote: {MASTER}")
    print(f"Verified: {len(v_rows)} rows total; {v_count} rows now '{NEW_SP}'")
    print(f"\nNEXT STEPS:")
    print(f"  1. Distribution check:")
    print(f"     duckdb -c \"SELECT source_pass, COUNT(*) FROM "
          f"read_csv_auto('{MASTER}') GROUP BY 1 ORDER BY 2 DESC;\"")
    print(f"  2. Run Phase 1 + Phase 2 to refresh DuckDB.")


if __name__ == "__main__":
    main()
