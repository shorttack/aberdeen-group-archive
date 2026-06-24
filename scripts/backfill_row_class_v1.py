#!/usr/bin/env python3
"""
backfill_row_class_v1.py — F3b backfill / rename for _master_prescience_scores.csv

Closes the gap discovered 2026-06-18 PM-2 during v1.7.0 Mac-side cutover:
the master already had `row_class` (F3 applied earlier) but ~half of rows
were NULL because new Pass C runs (sonar_v1 expansions, prefilter v6) landed
AFTER the original F3 backfill. Also reconciles enum drift: the 4 pre-existing
`row_class='prefilter'` rows are renamed to `prefilter_skip` to match the
canonical {scored, parse_fail, prefilter_skip, preseed_skip, no_anchor, pending}
spec shipped in PRESCIENCE_ARCHITECTURE rev2 and MASTERS_NOTES v3.

Touches (predicted 2026-06-18 PM-2 from repo blob 6877259e):
  rename:   4 rows row_class='prefilter'      -> 'prefilter_skip'
  backfill: 8589 sonar rows (parse_ok=true)   -> 'scored'
  backfill: 52   sonar rows (parse_ok=false)  -> 'parse_fail'
  backfill: 4    prefilter v6 rows (score=-1) -> 'prefilter_skip'
  -----------------------------------------------------
  total mutations: 8649  (rows added/removed: 0)

Invariants:
  - csv.QUOTE_ALL on write
  - UTC-stamped backup before write
  - dry-run default, --commit opt-in
  - row count preserved
  - prints classification distribution before + after
  - never reclassifies rows that already have a valid non-empty row_class
    (other than the explicit 'prefilter' -> 'prefilter_skip' rename)
"""

import csv
import shutil
import datetime
import sys
from pathlib import Path
from collections import Counter

ARCHIVE = Path.home() / "Desktop/Archive/aberdeen-group-archive"
MASTER  = ARCHIVE / "_master_prescience_scores.csv"

# Canonical enum (per PRESCIENCE_ARCHITECTURE rev2 / MASTERS_NOTES v3)
VALID = {"scored", "parse_fail", "prefilter_skip", "preseed_skip", "no_anchor", "pending"}

# Enum drift: legacy token -> canonical
RENAME = {"prefilter": "prefilter_skip"}

commit = "--commit" in sys.argv


def classify(row):
    """Derive row_class for a row whose row_class is empty/None.
    Returns the canonical token or None if the row can't be classified.
    """
    sp = (row.get("source_pass") or "").strip()
    ps = (row.get("prescience_score") or "").strip()
    po = (row.get("parse_ok") or "").strip().lower()

    # Prefilter rows (any scorer): score=-1, parse_ok=true, source_pass starts with pass_c_prefilter
    if sp.startswith("pass_c_prefilter"):
        return "prefilter_skip"

    # Explicit *_parse_fail source_pass takes precedence
    if sp.endswith("_parse_fail"):
        return "parse_fail"

    # Parse failure by parse_ok flag
    if po == "false":
        return "parse_fail"

    # Score=-1 with parse_ok=true means prefilter (we caught the explicit
    # prefilter source_pass above; this is a defensive fallthrough)
    if ps == "-1" and po == "true":
        return "prefilter_skip"

    # Empty score with no other signal — preseed skip
    if ps == "":
        return "preseed_skip"

    # Has a numeric score >= 0
    try:
        v = float(ps)
        if v >= 0:
            return "scored"
    except ValueError:
        pass

    return None  # caller decides what to do with unclassifiable rows


def main():
    if not MASTER.exists():
        sys.exit(f"ERROR: {MASTER} not found")

    with open(MASTER, newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    if "row_class" not in header:
        sys.exit("ERROR: row_class column not present. Run add_row_class_to_prescience_scores_v1.py first.")

    rc_idx = header.index("row_class")
    n_cols = len(header)
    n_rows_before = len(rows)

    # Build row dicts for clarity
    def as_dict(r):
        return {header[i]: r[i] if i < len(r) else "" for i in range(n_cols)}

    # Before snapshot
    before = Counter()
    for r in rows:
        rc = (r[rc_idx] if rc_idx < len(r) else "").strip()
        before[rc or "<NULL>"] += 1

    # Apply mutations
    n_renamed = 0
    n_backfilled = 0
    n_unclassified = 0
    unclassified_samples = []

    for r in rows:
        # Pad short rows defensively
        while len(r) < n_cols:
            r.append("")
        cur = (r[rc_idx] or "").strip()

        if cur in RENAME:
            r[rc_idx] = RENAME[cur]
            n_renamed += 1
            continue

        if cur == "":
            d = as_dict(r)
            new_rc = classify(d)
            if new_rc is None:
                n_unclassified += 1
                if len(unclassified_samples) < 5:
                    unclassified_samples.append({
                        "obs_id": d.get("obs_id"),
                        "source_pass": d.get("source_pass"),
                        "prescience_score": d.get("prescience_score"),
                        "parse_ok": d.get("parse_ok"),
                    })
                continue
            if new_rc not in VALID:
                sys.exit(f"INTERNAL ERROR: classifier produced non-canonical token {new_rc!r}")
            r[rc_idx] = new_rc
            n_backfilled += 1
            continue

        if cur not in VALID:
            sys.exit(f"ERROR: row has non-canonical row_class {cur!r} not in RENAME map. obs_id={as_dict(r).get('obs_id')!r}")

    # After snapshot
    after = Counter()
    for r in rows:
        rc = (r[rc_idx] if rc_idx < len(r) else "").strip()
        after[rc or "<NULL>"] += 1

    # Row parity check
    n_rows_after = len(rows)
    assert n_rows_before == n_rows_after, f"row count drift {n_rows_before} -> {n_rows_after}"

    # Report
    print(f"Master:           {MASTER}")
    print(f"Rows (before):    {n_rows_before}")
    print(f"Rows (after):     {n_rows_after}  (parity OK)")
    print(f"Columns:          {n_cols}")
    print()
    print("row_class distribution BEFORE:")
    for k, v in sorted(before.items()):
        print(f"  {k:20s} | {v}")
    print()
    print("row_class distribution AFTER:")
    for k, v in sorted(after.items()):
        print(f"  {k:20s} | {v}")
    print()
    print(f"Mutations:")
    print(f"  renamed         (prefilter -> prefilter_skip): {n_renamed}")
    print(f"  backfilled      (NULL -> classified):           {n_backfilled}")
    print(f"  unclassifiable  (NULL, kept NULL):              {n_unclassified}")
    if unclassified_samples:
        print(f"  unclassifiable samples:")
        for s in unclassified_samples:
            print(f"    {s}")
    print()
    print(f"Mode: {'COMMIT' if commit else 'DRY-RUN'}")

    if not commit:
        print("DRY-RUN only. Pass --commit to write.")
        return 0

    if n_unclassified > 0:
        sys.exit(f"ERROR: {n_unclassified} rows could not be classified. Aborting commit. Investigate samples above.")

    # Backup
    ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    bak = MASTER.with_suffix(f".csv.bak_backfill_row_class_{ts}")
    shutil.copy2(MASTER, bak)
    print(f"Backup written: {bak}")

    # Write
    with open(MASTER, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        w.writerows(rows)
    print(f"Wrote: {MASTER}")
    print(f"Mutations applied: {n_renamed + n_backfilled}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
