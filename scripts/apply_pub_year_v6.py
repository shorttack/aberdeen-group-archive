#!/usr/bin/env python3
"""
apply_pub_year_v6.py
====================

Apply the 350 pub_year fills from pub_year_candidates_v6.csv to the local
master studies CSV.

Source of truth:
    ~/Desktop/Archive/archive_masters/_master_studies.csv

Strategy:
    For every row in pub_year_candidates_v6.csv whose `proposed_pub_year`
    is non-empty, find the matching `study_id` in _master_studies.csv and
    overwrite its `date` field with `YYYY-01-01` (ISO year-only convention).

Safety:
    * Dry run by default. Use --commit to actually write.
    * Auto-backup live CSV before writing: _master_studies.csv.bak_pub_year_v6_<UTC timestamp>
    * Verify every v6 study_id exists in the master before any write.
    * Pre/post row-count parity check.
    * Diff preview (first 10 changes) printed in dry-run mode.

Where this script lives
-----------------------
On Pete's Mac:
    ~/Desktop/Archive/scripts/apply_pub_year_v6.py

In the archive repo (committed copy):
    shorttack/aberdeen-group-archive/scripts/apply_pub_year_v6.py

Usage
-----
    cd ~/Desktop/Archive
    python3 scripts/apply_pub_year_v6.py                          # dry run
    python3 scripts/apply_pub_year_v6.py --commit                 # write changes

Outputs (written to --out-dir, default CWD)
-------------------------------------------
    pub_year_apply_v6_dryrun.txt    (dry run report)
    pub_year_apply_v6_applied.txt   (after --commit; full audit trail)

Author: Pete Kastner / agent (BlueBridge Group)
"""

from __future__ import annotations

import argparse
import csv
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


# ---------------------------------------------------------------------------
# Path discovery
# ---------------------------------------------------------------------------

def find_master_studies(explicit: str | None) -> Path | None:
    """Locate _master_studies.csv (local truth, NOT GitHub)."""
    if explicit:
        p = Path(explicit).expanduser().resolve()
        return p if p.exists() else None
    env = os.environ.get("MASTER_STUDIES_CSV")
    if env:
        p = Path(env).expanduser().resolve()
        if p.exists():
            return p
    home = Path.home()
    p = home / "Desktop" / "Archive" / "archive_masters" / "_master_studies.csv"
    return p.resolve() if p.exists() else None


def find_v6_csv(explicit: str | None) -> Path | None:
    if explicit:
        p = Path(explicit).expanduser().resolve()
        return p if p.exists() else None
    # Look in CWD first
    for c in [
        Path.cwd() / "pub_year_candidates_v6.csv",
        Path.home() / "Desktop" / "Archive" / "pub_year_candidates_v6.csv",
    ]:
        if c.exists():
            return c.resolve()
    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Apply v6 pub_year fills to local _master_studies.csv"
    )
    ap.add_argument("--master", help="Path to _master_studies.csv (default: ~/Desktop/Archive/archive_masters/_master_studies.csv)")
    ap.add_argument("--v6",     help="Path to pub_year_candidates_v6.csv (default: CWD or ~/Desktop/Archive/)")
    ap.add_argument("--out-dir", default=".",
                    help="Directory for report files (default: CWD)")
    ap.add_argument("--commit", action="store_true",
                    help="Actually write the changes (default: dry-run only)")
    args = ap.parse_args()

    master_path = find_master_studies(args.master)
    if master_path is None:
        print("ERROR: cannot locate _master_studies.csv.", file=sys.stderr)
        print("Expected: ~/Desktop/Archive/archive_masters/_master_studies.csv", file=sys.stderr)
        return 2

    v6_path = find_v6_csv(args.v6)
    if v6_path is None:
        print("ERROR: cannot locate pub_year_candidates_v6.csv.", file=sys.stderr)
        return 2

    out_dir = Path(args.out_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    report_name = "pub_year_apply_v6_applied.txt" if args.commit else "pub_year_apply_v6_dryrun.txt"
    report_path = out_dir / report_name

    mode = "COMMIT" if args.commit else "DRY-RUN"
    print(f"Mode:        {mode}")
    print(f"Master CSV:  {master_path}")
    print(f"v6 input:    {v6_path}")
    print(f"Report:      {report_path}")
    print()

    # Load v6 candidates
    with open(v6_path, encoding="utf-8") as f:
        v6_rows = list(csv.DictReader(f))

    # Build patch map: study_id -> year (int)
    patches: dict[str, int] = {}
    for r in v6_rows:
        sid = r["study_id"].strip()
        y = r.get("proposed_pub_year", "").strip()
        if not y:
            continue
        try:
            patches[sid] = int(float(y))  # tolerate "2005" or "2005.0"
        except ValueError:
            print(f"WARN: skipping {sid} — bad year value {y!r}", file=sys.stderr)

    print(f"v6 patches to apply: {len(patches)}")

    # Load master CSV
    with open(master_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        master_rows = list(reader)
        fieldnames = reader.fieldnames

    pre_row_count = len(master_rows)
    print(f"Master rows (pre):   {pre_row_count}")

    if "study_id" not in fieldnames or "date" not in fieldnames:
        print(f"ERROR: master CSV missing required columns. Got: {fieldnames}", file=sys.stderr)
        return 2

    # Verify every v6 study_id exists in master
    master_by_id = {r["study_id"]: r for r in master_rows}
    missing = [sid for sid in patches if sid not in master_by_id]
    if missing:
        print(f"ERROR: {len(missing)} v6 study_ids NOT FOUND in master CSV. Aborting.", file=sys.stderr)
        for sid in missing[:20]:
            print(f"  - {sid}", file=sys.stderr)
        if len(missing) > 20:
            print(f"  ... and {len(missing) - 20} more", file=sys.stderr)
        return 3

    # Build change list
    changes: list[dict] = []  # {study_id, old_date, new_date}
    for sid, year in patches.items():
        row = master_by_id[sid]
        old = row["date"] or ""
        new = f"{year}-01-01"
        if old == new:
            continue  # no-op
        changes.append({"study_id": sid, "old_date": old, "new_date": new})

    print(f"Net changes:         {len(changes)}")
    print()

    # Diff preview (first 10)
    preview_lines = ["First 10 changes (diff preview):"]
    for c in changes[:10]:
        preview_lines.append(
            f"  {c['study_id']:55s}  {c['old_date']!r:25s}  ->  {c['new_date']!r}"
        )
    print("\n".join(preview_lines))

    # Categorize old_date for audit
    from collections import Counter
    old_categories = Counter()
    for c in changes:
        old = c["old_date"]
        if not old:
            old_categories["empty"] += 1
        elif len(old) == 10 and old[4] == "-" and old[7] == "-":
            old_categories["was_ISO_YYYY-MM-DD"] += 1
        else:
            old_categories["was_freeform_string"] += 1
    print()
    print("Old-date categories being overwritten:")
    for k, v in old_categories.most_common():
        print(f"  {k:25s}  {v:4d}")

    if not args.commit:
        # Write dry-run report
        report_lines = [
            "=" * 70,
            "pub_year v6 apply — DRY RUN",
            f"Run at:       {datetime.now(timezone.utc).isoformat()}",
            f"Master CSV:   {master_path}",
            f"v6 input:     {v6_path}",
            "=" * 70,
            f"v6 patches:           {len(patches)}",
            f"Master rows (pre):    {pre_row_count}",
            f"Net changes:          {len(changes)}",
            "",
            "Old-date categories:",
        ]
        for k, v in old_categories.most_common():
            report_lines.append(f"  {k:25s}  {v:4d}")
        report_lines.append("")
        report_lines.append("All changes:")
        for c in changes:
            report_lines.append(
                f"  {c['study_id']:55s}  {c['old_date']!r:25s}  ->  {c['new_date']!r}"
            )
        report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

        print()
        print(f"Wrote dry-run report: {report_path}")
        print()
        print("Dry run complete. Inspect the report, then re-run with --commit to apply.")
        return 0

    # --- COMMIT path ---

    # Backup
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup_path = master_path.with_suffix(f".csv.bak_pub_year_v6_{ts}")
    shutil.copy2(master_path, backup_path)
    print(f"Backup written: {backup_path}")

    # Apply
    for c in changes:
        master_by_id[c["study_id"]]["date"] = c["new_date"]

    # Write atomically: write to temp, then rename
    tmp_path = master_path.with_suffix(f".csv.tmp_pub_year_v6_{ts}")
    with open(tmp_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for r in master_rows:
            w.writerow(r)

    # Parity check on temp before swap
    with open(tmp_path, encoding="utf-8") as f:
        post_rows = list(csv.DictReader(f))
    post_row_count = len(post_rows)
    if post_row_count != pre_row_count:
        print(f"ERROR: row-count mismatch! pre={pre_row_count} post={post_row_count}", file=sys.stderr)
        print(f"Temp file kept at: {tmp_path}", file=sys.stderr)
        print(f"Live master untouched.", file=sys.stderr)
        return 4

    # Swap
    os.replace(tmp_path, master_path)
    print(f"Wrote: {master_path}  (rows: {pre_row_count} -> {post_row_count})")

    # Final report
    report_lines = [
        "=" * 70,
        "pub_year v6 apply — COMMITTED",
        f"Run at:       {datetime.now(timezone.utc).isoformat()}",
        f"Master CSV:   {master_path}",
        f"v6 input:     {v6_path}",
        f"Backup:       {backup_path}",
        "=" * 70,
        f"Rows pre/post:        {pre_row_count} / {post_row_count}",
        f"v6 patches:           {len(patches)}",
        f"Net changes applied:  {len(changes)}",
        "",
        "Old-date categories overwritten:",
    ]
    for k, v in old_categories.most_common():
        report_lines.append(f"  {k:25s}  {v:4d}")
    report_lines.append("")
    report_lines.append("Full audit trail (study_id -> old | new):")
    for c in changes:
        report_lines.append(
            f"  {c['study_id']:55s}  {c['old_date']!r:25s}  ->  {c['new_date']!r}"
        )
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print(f"Wrote audit trail: {report_path}")

    print()
    print("DONE. Next: rebuild masters/DuckDB to regenerate v_studies.pub_year.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
