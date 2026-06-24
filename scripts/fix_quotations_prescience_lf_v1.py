#!/usr/bin/env python3
"""
fix_quotations_prescience_lf_v1.py

Rewrite _master_quotations_prescience.csv with LF line endings and QUOTE_ALL.
No cell values are changed.
"""
from __future__ import annotations

import csv
import datetime as dt
import shutil
from pathlib import Path


def main() -> int:
    master = Path.home() / "Desktop/Archive/aberdeen-group-archive/_master_quotations_prescience.csv"
    stamp = dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")
    backup = master.with_suffix(f".csv.bak_lf_rewrite_{stamp}")

    raw_before = master.read_bytes()
    with master.open(newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    shutil.copy2(master, backup)
    with master.open("w", newline="\n") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=fieldnames,
            quoting=csv.QUOTE_ALL,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)

    raw_after = master.read_bytes()
    print(f"Rows: {len(rows)}")
    print(f"Columns: {len(fieldnames)}")
    print(f"CRLF before: {raw_before.count(b'\\r\\n')}")
    print(f"CRLF after: {raw_after.count(b'\\r\\n')}")
    print(f"Backup: {backup}")
    print("QUOTATIONS_PRESCIENCE_LF_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
