#!/usr/bin/env python3
"""apply_appdev_lifecycle_repair_v2.py

Repair the vendor labels on the TWO technology records that the agent's App-Dev
dossier ingest INTRODUCED as new rows (java, eclipse) in _master_technologies.csv.

Scope decision (2026-07-15, Pete): fix only records the ingest created. Forensics
against _master_technologies.csv.bak_merge_six_20260714T220205Z confirmed:
  - java     = NEW row created by the ingest (Case B) -> fix
  - eclipse  = NEW row created by the ingest (Case B) -> fix
  - powerbuilder = PRE-EXISTING archive data, untouched by the ingest (Case C)
       -> LEFT ALONE as a separate Pete-owned curation decision. NOT in this script.

VALUE-ONLY edits, exactly 2 rows / 1 field each. No column add/remove, no row
count change, no relocation. Honors hard master-CSV rules: dry-run default,
timestamped backup, QUOTE_ALL, row/col parity assertion, audit sidecar.

Changes:
  java.vendor     'Sun Microsystems' -> 'Oracle (formerly Sun Microsystems)'
  eclipse.vendor  'IBM (open-source)' -> 'Eclipse Foundation (originally IBM)'
"""
import csv, shutil, datetime, sys
from pathlib import Path

MASTER = Path.home() / "Desktop/Archive/aberdeen-group-archive/_master_technologies.csv"

# (tech_id, field, expected_old_value, new_value)
EDITS = [
    ("java", "vendor",
     "Sun Microsystems",
     "Oracle (formerly Sun Microsystems)"),
    ("eclipse", "vendor",
     "IBM (open-source)",
     "Eclipse Foundation (originally IBM)"),
]

commit = "--commit" in sys.argv

with open(MASTER, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

id_idx = header.index("tech_id")
col_idx = {c: i for i, c in enumerate(header)}
n_rows_before, n_cols_before = len(rows), len(header)

by_id = {}
for r in rows:
    by_id.setdefault(r[id_idx], []).append(r)

applied, problems = [], []
for tech_id, field, old_expected, new_val in EDITS:
    if tech_id not in by_id:
        problems.append("tech_id " + repr(tech_id) + " not found"); continue
    if len(by_id[tech_id]) != 1:
        problems.append("tech_id " + repr(tech_id) + " has " + str(len(by_id[tech_id])) + " rows (expected 1)"); continue
    row = by_id[tech_id][0]
    ci = col_idx[field]
    cur = row[ci]
    if cur == new_val:
        applied.append("[skip already-correct] " + tech_id + "." + field); continue
    if cur != old_expected:
        problems.append(tech_id + "." + field + ": current != expected\n     current : " + repr(cur) + "\n     expected: " + repr(old_expected))
        continue
    row[ci] = new_val
    applied.append(tech_id + "." + field + ": " + repr(old_expected) + " -> " + repr(new_val))

print("Master:", MASTER)
print("Rows:", n_rows_before, " Cols:", n_cols_before)
print("Mode:", "COMMIT" if commit else "DRY-RUN")
print("\nPlanned/applied edits:")
for a in applied:
    print("  " + a)
if problems:
    print("\nPROBLEMS (no write will occur):")
    for p in problems:
        print("  " + p)
    sys.exit("\nAborting: resolve mismatches above before committing.")

assert len(rows) == n_rows_before, "row count changed!"
assert len(header) == n_cols_before, "column count changed!"

if commit:
    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    bak = MASTER.with_suffix(".csv.bak_appdev_lifecycle_" + ts)
    shutil.copy2(MASTER, bak)
    with open(MASTER, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        w.writerows(rows)
    audit = MASTER.with_suffix(".csv.applied_appdev_lifecycle_" + ts + ".txt")
    audit.write_text("apply_appdev_lifecycle_repair_v2.py  " + ts + "\nbackup: " + bak.name + "\n\n" + "\n".join(applied) + "\n")
    print("\nBackup:", bak.name)
    print("Audit: ", audit.name)
    print("WROTE", MASTER.name, "(" + str(len(rows)) + " rows, " + str(len(header)) + " cols)")
else:
    print("\nDRY-RUN only — pass --commit to write.")
