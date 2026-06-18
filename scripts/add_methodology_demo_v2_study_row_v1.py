#!/usr/bin/env python3
"""
add_methodology_demo_v2_study_row_v1.py

Appends one row to ~/Desktop/Archive/archive_masters/_master_studies.csv
for the v2.0 methodology demo (study_id = 2026-kastner-prescience-methodology-demo-v2-0cdf49).

Invariants (per kastner-archive-pipeline skill):
  - csv.QUOTE_ALL on write
  - timestamped backup before write
  - dry-run by default; --commit to write
  - print row count before/after; must be +1
  - aborts if study_id already exists
"""
import csv, shutil, datetime, sys
from pathlib import Path

ARCHIVE = Path.home() / "Desktop/Archive/archive_masters"
MASTER  = ARCHIVE / "_master_studies.csv"

NEW_STUDY_ID = "2026-kastner-prescience-methodology-demo-v2-0cdf49"

NEW_ROW = {
    "study_id": NEW_STUDY_ID,
    "title": "A Worked Example: Quantifying Analyst Prescience Using the Kastner IT Research Archive (v2.0 \u2014 Multi-Horizon)",
    "author": "Peter S. Kastner (subject/reviewer) and Perplexity Computer (methodology architect)",
    "date": "2026-06-18",
    "type": "topic-analysis",
    "subject_domain": "research-methodology",
    "methodology": "industry-analysis,attribution-modeling,multi-horizon-scoring,sensitivity-analysis,primary-source-triangulation,reproducibility-framework",
    "source_file": "kastner-author/2026-kastner-prescience-methodology-demo-v2-0cdf49/source/original_text.md",
    "abstract": "Methodology v2.0 regeneration of the 2026-05-16 worked example, rebuilt against the v1.6.2 Kastner archive corpus (1,452 studies / 23,926 observations / 865 studies with prescience_max \u2265 4). Adds per-observation multi-horizon prescience scoring (score_overall, score_3yr, score_5yr) shipped in v1.6.2 of _master_prescience_scores.csv, with a new \u00a73.6 (multi-horizon methodology) and \u00a75.4 (horizon-decomposed attribution: overall / 3yr / 5yr / beyond-5yr). v1.0 dollar figures retained for reference; v2.0 dollar figures marked TBD pending Pete-authored recompute. Lead-time scoring (previously subjective \u00a74) is now data-derivable from horizon columns, de-subjectivizing one of the four attribution dimensions.",
    "license": "CC-BY-4.0",
    "importance": "high",
    "importance_rationale": "Supersedes v1.0 as canonical methodology-demonstration study against the v1.6.2 corpus. Demonstrates per-observation multi-horizon scoring \u2014 the principal v1.6.2 schema addition \u2014 in a real attribution worked example. Preserves v1.0 as historical record (separate study row, not overwritten).",
    "relevance": "high",
    "relevance_rationale": "Methodology is immediately reusable for any structured analyst archive with multi-horizon scoring (3yr/5yr/overall). Provides replication appendix with v_studies_with_high_prescience DuckDB queries and Python code keyed to v1.6.2 view column names (study_prescience_enum, study_prescience_rationale).",
    "prescience": "not-applicable",
    "prescience_rationale": "This study is a methodology-demonstration retrospective, not a forecast. It quantifies past prescience rather than making new predictions.",
}

# expected column order from the master header (verified 2026-06-18 via gh API blob)
EXPECTED_COLS = [
    "study_id","title","author","date","type","subject_domain","methodology",
    "source_file","abstract","license","importance","importance_rationale",
    "relevance","relevance_rationale","prescience","prescience_rationale",
]

commit = "--commit" in sys.argv

# read
with open(MASTER, newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows   = list(reader)

if header != EXPECTED_COLS:
    sys.exit(f"Header mismatch.\n  expected: {EXPECTED_COLS}\n  actual:   {header}\nAborting.")

# duplicate check
existing_ids = {r[0] for r in rows}
if NEW_STUDY_ID in existing_ids:
    sys.exit(f"study_id '{NEW_STUDY_ID}' already exists in master. Aborting.")

before = len(rows)

# backup
ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
bak = MASTER.with_suffix(f".csv.bak_add_methodology_demo_v2_{ts}")

# build new row in column order
new_row = [NEW_ROW[c] for c in EXPECTED_COLS]
rows.append(new_row)

after = len(rows)

print(f"Mode:   {'COMMIT' if commit else 'DRY-RUN'}")
print(f"Master: {MASTER}")
print(f"Rows:   {before} -> {after}  (delta +{after-before}, expected +1)")
print(f"Cols:   {len(header)}  (unchanged)")
print(f"New study_id: {NEW_STUDY_ID}")

if after - before != 1:
    sys.exit("Row delta is not +1. Aborting before any write.")

if commit:
    shutil.copy2(MASTER, bak)
    print(f"Backup: {bak}")
    with open(MASTER, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        w.writerows(rows)
    print(f"Wrote:  {MASTER}")
    print("DONE.")
else:
    print("DRY-RUN only \u2014 pass --commit to write.")
