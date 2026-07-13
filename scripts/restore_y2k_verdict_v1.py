#!/usr/bin/env python3
"""
restore_y2k_verdict_v1.py

The y2k study (199x-y2k-live-dead-wounded-platforms-835ea1) was authored with
prescience=high (Path B: verdict reasoned from knowledge, 19 gradeable
platform-survival predictions). Rule-A verdict writer overwrote it with
not-applicable because Pass C legitimately skipped the study (it saw the
placeholder not-applicable in the master at score time). This restores the
authored high verdict + rationale from the study package into _master_studies.csv.

Backup + QUOTE_ALL + dry-run default.
"""
import csv, sys, shutil, datetime
from pathlib import Path

REPO = Path.home()/"Desktop"/"Archive"/"aberdeen-group-archive"
MASTER = REPO/"_master_studies.csv"
PKG = REPO/"kastner-author"/"199x-y2k-live-dead-wounded-platforms-835ea1"/"data"/"studies.csv"
SID = "199x-y2k-live-dead-wounded-platforms-835ea1"
COMMIT = "--commit" in sys.argv
TS = datetime.datetime.now(datetime.UTC).strftime("%Y%m%dT%H%M%SZ")

pkg = list(csv.DictReader(open(PKG, encoding="utf-8")))[0]
authored_p = pkg["prescience"]
authored_r = pkg["prescience_rationale"]
assert authored_p == "high", f"expected authored high, got {authored_p!r}"

with open(MASTER, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f); header = r.fieldnames; rows = list(r)

hit = None
for row in rows:
    if row["study_id"] == SID:
        hit = row; break
assert hit is not None, "y2k row not found in master"

old_p, old_r = hit["prescience"], hit["prescience_rationale"]
hit["prescience"] = authored_p
hit["prescience_rationale"] = authored_r

print(f"MODE: {'COMMIT' if COMMIT else 'DRY-RUN'} (stamp {TS})")
print(f"  prescience: {old_p!r} -> {authored_p!r}")
print(f"  rationale : {old_r[:60]!r} -> {authored_r[:60]!r}")

if COMMIT:
    shutil.copy2(MASTER, MASTER.with_name(MASTER.name + f".bak_y2k_verdict_{TS}"))
    with open(MASTER, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        for row in rows:
            w.writerow([row.get(c,"") for c in header])
    print("wrote:", MASTER)
else:
    print("DRY-RUN only — pass --commit to write.")
