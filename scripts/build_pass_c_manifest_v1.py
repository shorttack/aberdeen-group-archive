#!/usr/bin/env python3
"""build_pass_c_manifest_v1.py
Extract the 145 observations belonging to the six new synthetic studies from
_master_observations.csv into a manifest CSV for run_prescience_pass_c_v7 --input-manifest.

Writes the FULL 17-column master rows (v7 reads metric_value directly from the
manifest — the documented trap is a manifest that lacks the claim text).
QUOTE_ALL. Read-only against the master (only writes the manifest file).
"""
import csv, os

ARCHIVE = os.path.expanduser("~/Desktop/Archive/aberdeen-group-archive")
MASTER = os.path.join(ARCHIVE, "_master_observations.csv")
OUT = os.path.expanduser("~/Desktop/Archive/pass_c_v7_six_manifest.csv")

SIX = {
    "2026-kastner-compaq-dell-pc-clones-split",
    "2026-kastner-compaq-long-fall-demise",
    "2026-kastner-sap-r3-hana-longitudinal",
    "2026-kastner-fault-tolerant-wars",
    "2026-kastner-database-decade-rdbms",
    "2026-kastner-appdev-tools-gui-cade",
}

with open(MASTER, newline="", encoding="utf-8") as f:
    r = csv.reader(f)
    header = next(r)
    sidx = header.index("study_id")
    rows = [row for row in r if row[sidx] in SIX]

with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(header)
    w.writerows(rows)

# per-study tally
from collections import Counter
c = Counter(row[sidx] for row in rows)
print(f"manifest: {len(rows)} rows -> {OUT}")
for sid in sorted(SIX):
    print(f"  {c.get(sid,0):>3}  {sid}")
assert len(rows) == 145, f"expected 145, got {len(rows)}"
print("OK: 145 rows, full 17-col schema, QUOTE_ALL")
