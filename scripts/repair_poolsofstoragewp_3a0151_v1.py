#!/usr/bin/env python3
"""
repair_poolsofstoragewp_3a0151_v1.py

Repairs the ingest-corrupted metadata for study `poolsofstoragewp-3a0151`
in Pete Kastner's Aberdeen archive masters.

ROOT CAUSE
----------
The source PDF's first line was an image placeholder:
    "==> picture [442 x 39] intentionally omitted <=="
The ingest pipeline captured that placeholder as the title/abstract seed
instead of the real document text a few lines below. Downstream this produced:
  - a slugged title "Poolsofstoragewp (Aberdeen, 1988)"
  - a wrong date 1988-01-01 (real: May 2004)
  - an abstract falsely claiming "original text lost ... during ingest"
    (the full text is intact at prepared/.../source/_raw_text.txt, 4146 words)
  - type=benchmark (real: an executive white paper / industry-analysis)
  - all 12 observations mis-tagged tech_id=windows (real: storage-management;
    the paper is entirely about storage pools / ILM, nothing about Windows)
  - no entity link on the 12 observations (real author: aberdeen-group)

GROUND TRUTH is the recovered source at:
    ~/Desktop/Archive/prepared/poolsofstoragewp-3a0151/source/original_text.md
    "The Best Path to ILM Is Through Pools of Storage",
    "An Executive White Paper May 2004", Aberdeen Group, underwritten by Maxtor.

SCOPE (full repair, per Pete 2026-07-09)
----------------------------------------
File 1  _master_studies.csv       : fix title, date, type, abstract on 1 row
File 2  _master_observations.csv  : retag 12 obs tech_id windows->storage-management,
                                    set entity_id=aberdeen-group

NOTE: _master_entities.csv and _master_technologies.csv have NO study_id column;
study<->entity/tech linkage is expressed purely through _master_observations.csv.
`aberdeen-group`, `maxtor`, `storage-management` already exist as rows in those
masters, so no entity/tech rows need to be added. Only the observation links change.

pub_year is DERIVED by Phase 1 from `date`, so it auto-corrects (1988->2004) on rebuild.
Prescience scores/verdict are unchanged (already Pass-C scored: low, mean 1.22).

INVARIANTS (per kastner-archive-pipeline skill)
-----------------------------------------------
  - dry-run default; --commit to write
  - timestamped backup before every write (.bak_repair_poolsofstoragewp_<utc>)
  - csv.QUOTE_ALL on write
  - row count preserved and reported per file
  - column count preserved and reported per file
"""
import csv, shutil, datetime, sys
from pathlib import Path

ARCHIVE = Path.home() / "Desktop/Archive/aberdeen-group-archive"
STUDIES = ARCHIVE / "_master_studies.csv"
OBS     = ARCHIVE / "_master_observations.csv"
STUDY_ID = "poolsofstoragewp-3a0151"

COMMIT = "--commit" in sys.argv
TS = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

# ---- Ground-truth values recovered from source/original_text.md ----
NEW_TITLE = "The Best Path to ILM Is Through Pools of Storage"
NEW_DATE  = "2004-05-01"   # "An Executive White Paper May 2004"
NEW_TYPE  = "white-paper"
NEW_ABSTRACT = (
    "Aberdeen Group executive white paper (May 2004), underwritten by Maxtor "
    "Corporation, arguing that the best near-term path to information life cycle "
    "management (ILM) is a logical four-pool storage model: online (OLTP/high-activity "
    "DSS on FC/SCSI), midline (capacity-oriented enterprise-class ATA disk for active "
    "fixed/reference and compliance data at ~25% of FC/SCSI cost), nearline "
    "(disk-to-disk-to-tape backup), and offline (offsite tape for disaster recovery). "
    "Aberdeen projects ~45% annual compounded storage growth, notes midline storage at "
    "roughly $9/GB versus ~$30/GB for FC/SCSI arrays, and prescribes a six-step, "
    "five-year migration toward ILM, concluding that cross-application enterprise-wide "
    "ILM software is three to five years away (major deployments expected by ~2008)."
)

NEW_ENTITY_ID = "aberdeen-group"   # author of the research; observations are Aberdeen findings
NEW_TECH_ID   = "storage-management"
OLD_TECH_ID   = "windows"

def backup(path):
    bak = path.with_suffix(path.suffix + f".bak_repair_poolsofstoragewp_{TS}")
    shutil.copy2(path, bak)
    print(f"  backup: {bak.name}")
    return bak

def read_csv(path):
    with open(path, newline="") as f:
        rdr = csv.reader(f)
        header = next(rdr)
        rows = list(rdr)
    return header, rows

def write_csv(path, header, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        w.writerows(rows)

print(f"Mode: {'COMMIT' if COMMIT else 'DRY-RUN'}   utc={TS}")
print("=" * 70)

# ============ FILE 1: _master_studies.csv ============
print("\n[1] _master_studies.csv")
h, rows = read_csv(STUDIES)
idx = {c: i for i, c in enumerate(h)}
for col in ("study_id", "title", "date", "type", "abstract"):
    if col not in idx:
        sys.exit(f"FATAL: column '{col}' missing from studies header {h}")

n_before = len(rows)
target = [r for r in rows if r[idx["study_id"]] == STUDY_ID]
if len(target) != 1:
    sys.exit(f"FATAL: expected exactly 1 studies row for {STUDY_ID}, found {len(target)}")
r = target[0]
print(f"  BEFORE title   : {r[idx['title']]!r}")
print(f"  BEFORE date    : {r[idx['date']]!r}")
print(f"  BEFORE type    : {r[idx['type']]!r}")
print(f"  BEFORE abstract: {r[idx['abstract']][:90]!r}...")
r[idx["title"]]    = NEW_TITLE
r[idx["date"]]     = NEW_DATE
r[idx["type"]]     = NEW_TYPE
r[idx["abstract"]] = NEW_ABSTRACT
print(f"  AFTER  title   : {r[idx['title']]!r}")
print(f"  AFTER  date    : {r[idx['date']]!r}")
print(f"  AFTER  type    : {r[idx['type']]!r}")
print(f"  AFTER  abstract: {r[idx['abstract']][:90]!r}...")
print(f"  rows: {n_before} -> {len(rows)} (parity {'OK' if n_before==len(rows) else 'FAIL'}); cols: {len(h)}")

# ============ FILE 2: _master_observations.csv ============
print("\n[2] _master_observations.csv")
h2, rows2 = read_csv(OBS)
idx2 = {c: i for i, c in enumerate(h2)}
for col in ("study_id", "entity_id", "tech_id", "obs_id"):
    if col not in idx2:
        sys.exit(f"FATAL: column '{col}' missing from obs header {h2}")

n2_before = len(rows2)
touched = 0
tech_changed = 0
ent_changed = 0
for row in rows2:
    if row[idx2["study_id"]] != STUDY_ID:
        continue
    touched += 1
    if row[idx2["tech_id"]] == OLD_TECH_ID:
        row[idx2["tech_id"]] = NEW_TECH_ID
        tech_changed += 1
    if row[idx2["entity_id"]] != NEW_ENTITY_ID:
        row[idx2["entity_id"]] = NEW_ENTITY_ID
        ent_changed += 1
print(f"  obs rows for study : {touched} (expected 12)")
print(f"  tech_id {OLD_TECH_ID}->{NEW_TECH_ID} : {tech_changed}")
print(f"  entity_id -> {NEW_ENTITY_ID}   : {ent_changed}")
print(f"  rows: {n2_before} -> {len(rows2)} (parity {'OK' if n2_before==len(rows2) else 'FAIL'}); cols: {len(h2)}")

if touched != 12:
    sys.exit(f"FATAL: expected 12 obs rows for {STUDY_ID}, touched {touched}")

# ============ WRITE ============
print("\n" + "=" * 70)
if COMMIT:
    backup(STUDIES); write_csv(STUDIES, h, rows); print(f"  wrote {STUDIES.name}")
    backup(OBS);     write_csv(OBS, h2, rows2);   print(f"  wrote {OBS.name}")
    print("\nCOMMIT complete. Next: rebuild Phase 1+2 (pub_year re-derives to 2004),")
    print("then Phases 3-6 so kw ask reflects the repair.")
else:
    print("DRY-RUN only. Re-run with --commit to write both masters.")
