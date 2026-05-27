#!/usr/bin/env python3
"""
apply_pub_year_v6_1.py
======================

v6.1 corrections patch — fixes 4 known-bad pub_year rows that slipped
through v2's first/last-10-lines extractor (misparsed nonsensical years
1904, 1905, 2030 instead of the obvious filename-derived years).

Targets:
    dell-services-kastner-051904-a25a59              1904 -> 2004
    1q06-ff-bp-retail-transportation-081905a-192432  1905 -> 2006
    f-4q05-bp-intl-logistics-081905a-31c05c          1905 -> 2005
    1q05-pss-fieldservices-020305a-fa2797            2030 -> 2005

Patches the local master: ~/Desktop/Archive/archive_masters/_master_studies.csv

Safety: same pattern as apply_pub_year_v6.py — backup, dry-run by default,
parity check, atomic swap.

Run order after --commit:
    1. python3 ~/Desktop/Archive/scripts/01_load_csvs_v2.py --archive ... --wiki ...
    2. python3 ~/Desktop/Archive/scripts/02_build_data_layer_v2.py --wiki ...
    3. Verify: SELECT COUNT(*) FROM v_studies WHERE pub_year < 1970 OR pub_year > 2027;

Where this script lives
-----------------------
~/Desktop/Archive/scripts/apply_pub_year_v6_1.py

Usage
-----
    cd ~/Desktop/Archive
    python3 scripts/apply_pub_year_v6_1.py           # dry run
    python3 scripts/apply_pub_year_v6_1.py --commit  # apply

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


# Hand-curated corrections. Format: study_id -> (old_pub_year_for_audit, new_year)
CORRECTIONS: dict[str, tuple[int, int]] = {
    "dell-services-kastner-051904-a25a59":             (1904, 2004),
    "1q06-ff-bp-retail-transportation-081905a-192432": (1905, 2006),
    "f-4q05-bp-intl-logistics-081905a-31c05c":         (1905, 2005),
    "1q05-pss-fieldservices-020305a-fa2797":           (2030, 2005),
}


def find_master_studies(explicit: str | None) -> Path | None:
    if explicit:
        p = Path(explicit).expanduser().resolve()
        return p if p.exists() else None
    env = os.environ.get("MASTER_STUDIES_CSV")
    if env:
        p = Path(env).expanduser().resolve()
        if p.exists():
            return p
    p = Path.home() / "Desktop" / "Archive" / "archive_masters" / "_master_studies.csv"
    return p.resolve() if p.exists() else None


def main() -> int:
    ap = argparse.ArgumentParser(description="Apply v6.1 corrections to _master_studies.csv")
    ap.add_argument("--master", help="Path to _master_studies.csv (default: auto-detect)")
    ap.add_argument("--out-dir", default=".",
                    help="Directory for audit report (default: CWD)")
    ap.add_argument("--commit", action="store_true",
                    help="Actually write the changes (default: dry-run only)")
    args = ap.parse_args()

    master_path = find_master_studies(args.master)
    if master_path is None:
        print("ERROR: cannot locate _master_studies.csv.", file=sys.stderr)
        return 2

    out_dir = Path(args.out_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    report_name = "pub_year_apply_v6_1_applied.txt" if args.commit else "pub_year_apply_v6_1_dryrun.txt"
    report_path = out_dir / report_name

    mode = "COMMIT" if args.commit else "DRY-RUN"
    print(f"Mode:       {mode}")
    print(f"Master CSV: {master_path}")
    print(f"Report:     {report_path}")
    print()

    # Load master
    with open(master_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        master_rows = list(reader)
        fieldnames = reader.fieldnames

    pre_count = len(master_rows)
    print(f"Master rows (pre): {pre_count}")

    by_id = {r["study_id"]: r for r in master_rows}

    # Verify every correction targets an existing row + the current date matches expected old year
    issues = []
    changes = []
    for sid, (old_year, new_year) in CORRECTIONS.items():
        if sid not in by_id:
            issues.append(f"NOT FOUND: {sid}")
            continue
        current_date = by_id[sid]["date"] or ""
        expected_old = f"{old_year}-01-01"
        new_date = f"{new_year}-01-01"
        if current_date != expected_old:
            issues.append(
                f"MISMATCH: {sid} — current date {current_date!r}, expected {expected_old!r} "
                f"(continuing with overwrite to {new_date!r})"
            )
        changes.append({"study_id": sid, "old_date": current_date, "new_date": new_date})

    if any(i.startswith("NOT FOUND") for i in issues):
        print("ERROR: corrections target study_ids missing from master:", file=sys.stderr)
        for i in issues:
            print(f"  {i}", file=sys.stderr)
        return 3

    print(f"Corrections to apply: {len(changes)}")
    if issues:
        print("Soft warnings:")
        for i in issues:
            print(f"  {i}")
    print()

    print("Diff preview:")
    for c in changes:
        print(f"  {c['study_id']:55s}  {c['old_date']!r:14s}  ->  {c['new_date']!r}")
    print()

    if not args.commit:
        lines = [
            "=" * 70,
            "pub_year v6.1 corrections — DRY RUN",
            f"Run at:     {datetime.now(timezone.utc).isoformat()}",
            f"Master CSV: {master_path}",
            "=" * 70,
            f"Corrections: {len(changes)}",
            "",
        ]
        for c in changes:
            lines.append(f"  {c['study_id']:55s}  {c['old_date']!r:14s}  ->  {c['new_date']!r}")
        if issues:
            lines.append("")
            lines.append("Soft warnings:")
            for i in issues:
                lines.append(f"  {i}")
        report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"Wrote dry-run report: {report_path}")
        print("Re-run with --commit to apply.")
        return 0

    # --- COMMIT path ---
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup_path = master_path.with_suffix(f".csv.bak_pub_year_v6_1_{ts}")
    shutil.copy2(master_path, backup_path)
    print(f"Backup written: {backup_path}")

    for c in changes:
        by_id[c["study_id"]]["date"] = c["new_date"]

    tmp_path = master_path.with_suffix(f".csv.tmp_pub_year_v6_1_{ts}")
    with open(tmp_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for r in master_rows:
            w.writerow(r)

    with open(tmp_path, encoding="utf-8") as f:
        post_rows = list(csv.DictReader(f))
    post_count = len(post_rows)
    if post_count != pre_count:
        print(f"ERROR: row-count mismatch! pre={pre_count} post={post_count}", file=sys.stderr)
        print(f"Temp file kept at: {tmp_path}", file=sys.stderr)
        return 4

    os.replace(tmp_path, master_path)
    print(f"Wrote: {master_path}  (rows: {pre_count} -> {post_count})")

    lines = [
        "=" * 70,
        "pub_year v6.1 corrections — COMMITTED",
        f"Run at:     {datetime.now(timezone.utc).isoformat()}",
        f"Master CSV: {master_path}",
        f"Backup:     {backup_path}",
        "=" * 70,
        f"Rows pre/post:   {pre_count} / {post_count}",
        f"Changes applied: {len(changes)}",
        "",
        "Audit trail:",
    ]
    for c in changes:
        lines.append(f"  {c['study_id']:55s}  {c['old_date']!r:14s}  ->  {c['new_date']!r}")
    if issues:
        lines.append("")
        lines.append("Soft warnings encountered (corrections still applied):")
        for i in issues:
            lines.append(f"  {i}")
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote audit trail: {report_path}")

    print()
    print("DONE. Next: rerun Phase 1 + Phase 2 to refresh parquets + DuckDB views.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
