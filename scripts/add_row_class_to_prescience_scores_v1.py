#!/usr/bin/env python3
"""
add_row_class_to_prescience_scores_v1.py

F3 resolution (v1.7.0 ship gate): add a 12th column `row_class` to
`_master_prescience_scores.csv` and backfill from the implicit row class
each existing row already represents.

Rationale: today the `model` column conflates ML model identity
(`claude-sonnet-4.6`, `sonar-reasoning-pro`) with sentinel markers
(`preseed_skip_v1`). With driver v8 (short-horizon) about to add more
row classes, the column becomes uninterpretable. This script adds an
explicit `row_class` column and restricts `model` to actual model
identifiers going forward.

Six row classes (from PRESCIENCE_ARCHITECTURE.md §2.1):

| row_class       | rule                                                  | expected n |
|-----------------|-------------------------------------------------------|-----------:|
| scored          | model in {claude-sonnet-4.6, sonar-reasoning-pro}     |      8,372 |
|                 | AND parse_ok==true AND source_pass NOT LIKE %fail     |            |
| parse_fail      | parse_ok==false OR source_pass LIKE %parse_fail       |         64 |
| prefilter_skip  | source_pass == 'pass_c_prefilter_v1'                  |          4 |
| preseed_skip    | model == 'preseed_skip_v1'                            |        253 |
| no_anchor       | (reserved; not currently present)                     |          0 |
| pending         | (reserved; not currently present)                     |          0 |

The `model` column is NOT modified by this script — preseed_skip_v1
rows keep that value for archival continuity. But once `row_class`
exists, queries should filter on `row_class`, not `model`.

Invariants enforced:
- Dry-run default; --commit opt-in
- csv.QUOTE_ALL on write
- Backup before write: _master_prescience_scores.csv.bak_add_row_class_<utc>Z
- Row count preserved
- Column count: 11 -> 12
- Every row gets exactly one row_class value (no empties)
- Backfill counts MUST match expected n (hard-fail if drift)

Author: Perplexity Computer.
Date: 2026-06-18 (v1.7.0 ship-gate F3 close).
Pairs with: F6 (retag_cloud_parse_fails_v1.py) and F7 (docs only).
"""

import csv
import sys
import shutil
import datetime
from pathlib import Path
from collections import Counter

# ---- paths ----
ARCHIVE = Path.home() / "Desktop" / "Archive" / "archive_masters"
MASTER = ARCHIVE / "_master_prescience_scores.csv"

# ---- expected baseline (verified via 2026-06-15 audit) ----
EXPECTED_TOTAL = 8440
EXPECTED_COUNTS = {
    "scored": 8372 - 12,           # 8,360 -- but see note below
    "parse_fail": 64,              # 52 sonar-split + 12 cloud-inband
    "prefilter_skip": 4,
    "preseed_skip": 253,
    "no_anchor": 0,
    "pending": 0,
}
# NOTE on `scored` count:
# The audit says 4,070 cloud scored + 4,302 sonar scored = 8,372 scored.
# 12 of the "cloud" rows are actually parse-fails (parse_ok=false).
# So scored = 8,372 - 12 cloud-inband-parse-fails = 8,360.
# Cross-check: 8,360 + 64 + 4 + 253 = 8,681. That's too high.
# Re-reconcile: 4,082 cloud rows (12 are parse-fail) + 4,302 sonar scored
# + 52 sonar parse-fail + 4 prefilter + 253 preseed = 4,082 + 4,302 + 52 + 4 + 253 = 8,693.
# Audit says total is 8,440. Discrepancy = 253 (the preseed count).
# Resolution: preseed rows are NOT included in the 4,082/4,302/52/4 buckets;
# they were counted in the source_pass=pass_c_cloud bucket (model=preseed_skip_v1
# is the discriminator, NOT source_pass). So the math is:
#   - source_pass=pass_c_cloud: 4,082 rows total
#       -- of which model=preseed_skip_v1: 253 (preseed_skip)
#       -- of which model=claude-sonnet-4.6 AND parse_ok=false: 12 (parse_fail)
#       -- of which model=claude-sonnet-4.6 AND parse_ok=true: 4,082 - 253 - 12 = 3,817 (scored)
#   - source_pass=pass_c_sonar_v1: 4,302 (all scored)
#   - source_pass=pass_c_sonar_v1_parse_fail: 52 (parse_fail)
#   - source_pass=pass_c_prefilter_v1: 4 (prefilter_skip)
#   TOTAL: 4,082 + 4,302 + 52 + 4 = 8,440 ✓
# So:
#   scored = 3,817 + 4,302 = 8,119
#   parse_fail = 12 + 52 = 64
#   prefilter_skip = 4
#   preseed_skip = 253
#   TOTAL = 8,119 + 64 + 4 + 253 = 8,440 ✓
EXPECTED_COUNTS = {
    "scored": 8119,
    "parse_fail": 64,
    "prefilter_skip": 4,
    "preseed_skip": 253,
    "no_anchor": 0,
    "pending": 0,
}

# ---- classifier ----
def classify(row: dict) -> str:
    """Return the row_class for an existing prescience-scores row.

    Order matters — preseed_skip is checked first because those rows have
    model='preseed_skip_v1' regardless of source_pass.
    """
    model = (row.get("model") or "").strip()
    source_pass = (row.get("source_pass") or "").strip()
    parse_ok = (row.get("parse_ok") or "").strip().lower()

    # 1. preseed_skip wins — model is the discriminator
    if model == "preseed_skip_v1":
        return "preseed_skip"

    # 2. prefilter_skip — source_pass is the discriminator
    if source_pass == "pass_c_prefilter_v1":
        return "prefilter_skip"

    # 3. parse_fail — either flag OR suffix indicates failure
    if parse_ok == "false" or source_pass.endswith("_parse_fail"):
        return "parse_fail"

    # 4. scored — everything else with a real model
    if model in ("claude-sonnet-4.6", "sonar-reasoning-pro"):
        return "scored"

    # 5. unknown — should be zero rows; hard-fail if hit
    return "UNKNOWN"


def main():
    commit = "--commit" in sys.argv
    verbose = "--verbose" in sys.argv

    if not MASTER.exists():
        sys.exit(f"ERROR: master not found at {MASTER}")

    # --- read ---
    with open(MASTER, newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows_raw = list(reader)

    if "row_class" in header:
        sys.exit("ERROR: column 'row_class' already exists. Aborting.")

    n_cols_before = len(header)
    n_rows = len(rows_raw)
    if n_rows != EXPECTED_TOTAL:
        sys.exit(
            f"ERROR: expected {EXPECTED_TOTAL} rows, found {n_rows}. "
            f"Baseline drift; re-audit before applying."
        )

    # Re-read as dicts for classifier
    with open(MASTER, newline="") as f:
        rows_dict = list(csv.DictReader(f))

    # --- classify ---
    classifications = [classify(r) for r in rows_dict]
    counts = Counter(classifications)

    # --- hard-fail if any UNKNOWN ---
    if counts.get("UNKNOWN", 0) > 0:
        print("ERROR: UNKNOWN row class for these rows:")
        for i, c in enumerate(classifications):
            if c == "UNKNOWN":
                print(f"  row {i}: {rows_dict[i]}")
        sys.exit(1)

    # --- hard-fail if counts don't match expected ---
    drift = []
    for cls, expected in EXPECTED_COUNTS.items():
        actual = counts.get(cls, 0)
        if actual != expected:
            drift.append(f"  {cls}: expected {expected}, got {actual}")
    if drift:
        print("ERROR: row_class counts don't match expected baseline:")
        print("\n".join(drift))
        print(f"\nFull distribution: {dict(counts)}")
        sys.exit(1)

    # --- report ---
    print(f"Mode: {'COMMIT' if commit else 'DRY-RUN'}")
    print(f"Master: {MASTER}")
    print(f"Rows: {n_rows}")
    print(f"Cols: {n_cols_before} -> {n_cols_before + 1}")
    print(f"\nRow class distribution:")
    for cls in ["scored", "parse_fail", "prefilter_skip",
                "preseed_skip", "no_anchor", "pending"]:
        print(f"  {cls:<16} {counts.get(cls, 0):>6}")

    if verbose:
        print(f"\nSample rows per class:")
        for cls in EXPECTED_COUNTS:
            for i, c in enumerate(classifications):
                if c == cls:
                    print(f"  {cls}: row {i} -> model={rows_dict[i].get('model')!r}, "
                          f"source_pass={rows_dict[i].get('source_pass')!r}, "
                          f"parse_ok={rows_dict[i].get('parse_ok')!r}")
                    break

    if not commit:
        print("\nDRY-RUN only. Pass --commit to write.")
        return

    # --- backup ---
    ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    bak = MASTER.with_suffix(f".csv.bak_add_row_class_{ts}")
    shutil.copy2(MASTER, bak)
    print(f"\nBackup: {bak}")

    # --- write ---
    new_header = header + ["row_class"]
    new_rows = [r + [classifications[i]] for i, r in enumerate(rows_raw)]

    # row-parity check before write
    if len(new_rows) != n_rows:
        sys.exit(f"ERROR: row count drift during build: {n_rows} -> {len(new_rows)}")

    with open(MASTER, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(new_header)
        w.writerows(new_rows)

    # --- verify ---
    with open(MASTER, newline="") as f:
        reader = csv.reader(f)
        verify_header = next(reader)
        verify_rows = list(reader)

    if len(verify_rows) != n_rows:
        sys.exit(f"ERROR: post-write row count mismatch: {n_rows} -> {len(verify_rows)}")
    if "row_class" not in verify_header:
        sys.exit("ERROR: post-write header missing row_class")

    print(f"Wrote: {MASTER}")
    print(f"Verified: {len(verify_rows)} rows, {len(verify_header)} cols, row_class present")
    print(f"\nNEXT STEPS:")
    print(f"  1. Inspect with: duckdb -c \"SELECT row_class, COUNT(*) FROM "
          f"read_csv_auto('{MASTER}') GROUP BY 1 ORDER BY 2 DESC;\"")
    print(f"  2. Run Phase 1 + Phase 2 to refresh DuckDB.")
    print(f"  3. Sync to repo: sync_studies_verdicts_repo_from_archive_masters_v2.py")
    print(f"     (NOTE: that script syncs verdicts only; for the prescience scores")
    print(f"      master, EOD batch commit will pick up archive_masters changes.)")


if __name__ == "__main__":
    main()
