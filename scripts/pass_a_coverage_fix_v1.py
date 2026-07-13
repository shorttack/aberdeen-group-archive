#!/usr/bin/env python3
"""
pass_a_coverage_fix_v1.py

Minimal Pass A structural pass for the pptx6 ingest: restore 100%
verification_method coverage on _master_observations.csv by normalizing any
bare-blank verification_method to 'unverified' (archival-ingest v20 Section
17.2 rule 4 / 16.2 Check 6). Does NOT touch non-blank rows, does NOT fabricate
prediction-outcome links (the new studies' actual-outcome rows are legitimately
[DEFERRED] and owned by Phase 3 / Pass C). Backup + QUOTE_ALL; dry-run default.
"""
import csv, sys, shutil, datetime
from pathlib import Path

MASTER = Path.home()/"Desktop"/"Archive"/"aberdeen-group-archive"/"_master_observations.csv"
COMMIT = "--commit" in sys.argv
TS = datetime.datetime.now(datetime.UTC).strftime("%Y%m%dT%H%M%SZ")

with open(MASTER, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f); header = r.fieldnames; rows = list(r)

assert "verification_method" in header, "verification_method column missing"

fixed = 0
for row in rows:
    v = (row.get("verification_method") or "").strip().lower()
    if v in ("", "unknown", "n/a", "tbd"):
        if (row.get("verification_method") or "").strip() != "unverified":
            row["verification_method"] = "unverified"; fixed += 1

blanks_after = sum(1 for row in rows if not (row.get("verification_method") or "").strip())
print(f"MODE: {'COMMIT' if COMMIT else 'DRY-RUN'} (stamp {TS})")
print(f"rows: {len(rows)}  normalized_to_unverified: {fixed}  blanks_after: {blanks_after}")

if COMMIT:
    shutil.copy2(MASTER, MASTER.with_name(MASTER.name + f".bak_pass_a_cov_{TS}"))
    with open(MASTER, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        for row in rows:
            w.writerow([row.get(c,"") for c in header])
    print("wrote:", MASTER)
else:
    print("DRY-RUN only — pass --commit to write.")
