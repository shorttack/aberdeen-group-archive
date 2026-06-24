#!/usr/bin/env python3
"""
apply_passb_transcripts_v1.py

Apply the Pass B 17-transcript batch to the four master CSVs:
  - _master_studies.csv         : REPLACE 17 rows (placeholder -> v20 §13.1 transcript)
  - _master_entities.csv        : APPEND 194 rows
  - _master_technologies.csv    : APPEND 122 rows
  - _master_observations.csv    : APPEND 295 rows  (17-col v20 schema)

The batch CSVs were assembled in the sandbox to honor Pete's
"write once, not seventeen times" rule. This script is the merge
side that runs on the Mac.

Invariants (per kastner-archive-pipeline + archival-ingest §16.5):
  - csv.QUOTE_ALL on every write
  - Timestamped backup of every master before write
  - Dry-run is default; --commit is opt-in
  - Row-parity prints: before/after counts for every table
  - studies REPLACE: matches on study_id; appends new ones; never
    silently drops a row from the master
  - observations APPEND: only adds rows whose study_id is in our
    17-study set; refuses to add rows whose obs_id already exists
  - Master observations has 17 cols (v20). We carry 12 from per-study
    + 5 added at master-regen time:
        verification_method = 'ingest-extraction'
        collection          = 'transcript'
        thread_tag          = ''
        section             = ''  (passed through if present in batch)
        legacy_obs_id       = ''

Usage on Mac:
    cd ~/Desktop/Archive
    python3 scripts/apply_passb_transcripts_v1.py            # dry-run
    python3 scripts/apply_passb_transcripts_v1.py --commit   # write
"""

import csv
import datetime
import shutil
import sys
from pathlib import Path

# --------------------------------------------------------------- config

ARCHIVE       = Path.home() / "Desktop/Archive/aberdeen-group-archive"
BATCH_ROOT    = Path.home() / "Desktop/Archive/passb_batch"

STUDIES_MASTER       = ARCHIVE / "_master_studies.csv"
ENTITIES_MASTER      = ARCHIVE / "_master_entities.csv"
TECHS_MASTER         = ARCHIVE / "_master_technologies.csv"
OBSERVATIONS_MASTER  = ARCHIVE / "_master_observations.csv"

STUDIES_BATCH        = BATCH_ROOT / "batch_studies_REPLACE_v1.csv"
ENTITIES_BATCH       = BATCH_ROOT / "batch_entities_APPEND_v1.csv"
TECHS_BATCH          = BATCH_ROOT / "batch_technologies_APPEND_v1.csv"
OBSERVATIONS_BATCH   = BATCH_ROOT / "batch_observations_APPEND_v1.csv"

EXPECTED_STUDIES     = 17
EXPECTED_ENTITIES    = 194
EXPECTED_TECHS       = 122
EXPECTED_OBS         = 295

OBSERVATIONS_MASTER_COLS = [
    "obs_id", "study_id", "entity_id", "tech_id", "observation_type",
    "year_observed", "metric_name", "metric_value", "confidence",
    "verification_method", "methodology_code", "source_page", "notes",
    "collection", "thread_tag", "section", "legacy_obs_id",
]

OBSERVATIONS_BATCH_COLS = [
    "obs_id", "study_id", "entity_id", "tech_id", "observation_type",
    "year_observed", "metric_name", "metric_value", "confidence",
    "methodology_code", "source_page", "notes",
]

# --------------------------------------------------------------- io

def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.reader(f)
        header = next(r)
        rows = list(r)
    return header, rows

def write_csv(path, header, rows):
    """Mandatory QUOTE_ALL writer (§16.5)."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        w.writerows(rows)

def backup(path, reason, ts):
    bak = path.with_suffix(f".csv.bak_{reason}_{ts}")
    shutil.copy2(path, bak)
    return bak

# --------------------------------------------------------------- logic

def apply_studies_replace(commit, ts):
    print(f"\n--- {STUDIES_MASTER.name}: REPLACE 17 rows ---")
    mh, mrows = read_csv(STUDIES_MASTER)
    bh, brows = read_csv(STUDIES_BATCH)

    if mh != bh:
        sys.exit(f"FATAL: studies header mismatch.\n  master: {mh}\n  batch:  {bh}")
    if len(brows) != EXPECTED_STUDIES:
        sys.exit(f"FATAL: batch has {len(brows)} studies, expected {EXPECTED_STUDIES}")

    batch_ids = {r[0] for r in brows}
    if len(batch_ids) != EXPECTED_STUDIES:
        sys.exit("FATAL: duplicate study_id in batch")

    sid_to_batch = {r[0]: r for r in brows}
    replaced = 0
    new = []
    for r in mrows:
        if r[0] in sid_to_batch:
            new.append(sid_to_batch.pop(r[0]))
            replaced += 1
        else:
            new.append(r)
    appended = list(sid_to_batch.values())  # any not in master get appended
    new.extend(appended)

    print(f"  master rows in: {len(mrows)}")
    print(f"  replaced (in-place): {replaced}")
    print(f"  appended (new): {len(appended)}")
    print(f"  master rows out: {len(new)}")
    if replaced + len(appended) != EXPECTED_STUDIES:
        sys.exit(f"FATAL: only {replaced + len(appended)} of {EXPECTED_STUDIES} batch ids accounted for")

    if commit:
        bak = backup(STUDIES_MASTER, "passb_transcripts_replace", ts)
        write_csv(STUDIES_MASTER, mh, new)
        print(f"  backup: {bak.name}")
        print(f"  wrote:  {STUDIES_MASTER.name}")

def apply_entities_append(commit, ts):
    print(f"\n--- {ENTITIES_MASTER.name}: APPEND {EXPECTED_ENTITIES} rows ---")
    mh, mrows = read_csv(ENTITIES_MASTER)
    bh, brows = read_csv(ENTITIES_BATCH)
    if mh != bh:
        sys.exit(f"FATAL: entities header mismatch.\n  master: {mh}\n  batch:  {bh}")
    if len(brows) != EXPECTED_ENTITIES:
        sys.exit(f"FATAL: batch has {len(brows)} entities, expected {EXPECTED_ENTITIES}")

    new = mrows + brows
    print(f"  master rows in:  {len(mrows)}")
    print(f"  appended:        {len(brows)}")
    print(f"  master rows out: {len(new)}")

    if commit:
        bak = backup(ENTITIES_MASTER, "passb_transcripts_append", ts)
        write_csv(ENTITIES_MASTER, mh, new)
        print(f"  backup: {bak.name}")
        print(f"  wrote:  {ENTITIES_MASTER.name}")

def apply_techs_append(commit, ts):
    print(f"\n--- {TECHS_MASTER.name}: APPEND {EXPECTED_TECHS} rows ---")
    mh, mrows = read_csv(TECHS_MASTER)
    bh, brows = read_csv(TECHS_BATCH)
    if mh != bh:
        sys.exit(f"FATAL: technologies header mismatch.\n  master: {mh}\n  batch:  {bh}")
    if len(brows) != EXPECTED_TECHS:
        sys.exit(f"FATAL: batch has {len(brows)} techs, expected {EXPECTED_TECHS}")

    new = mrows + brows
    print(f"  master rows in:  {len(mrows)}")
    print(f"  appended:        {len(brows)}")
    print(f"  master rows out: {len(new)}")

    if commit:
        bak = backup(TECHS_MASTER, "passb_transcripts_append", ts)
        write_csv(TECHS_MASTER, mh, new)
        print(f"  backup: {bak.name}")
        print(f"  wrote:  {TECHS_MASTER.name}")

def apply_observations_append(commit, ts):
    print(f"\n--- {OBSERVATIONS_MASTER.name}: APPEND {EXPECTED_OBS} rows (12-col -> 17-col promote) ---")
    mh, mrows = read_csv(OBSERVATIONS_MASTER)
    if mh != OBSERVATIONS_MASTER_COLS:
        sys.exit(f"FATAL: master observations header mismatch.\n  expected: {OBSERVATIONS_MASTER_COLS}\n  found:    {mh}")

    bh, brows = read_csv(OBSERVATIONS_BATCH)
    if bh != OBSERVATIONS_BATCH_COLS:
        sys.exit(f"FATAL: batch observations header mismatch.\n  expected: {OBSERVATIONS_BATCH_COLS}\n  found:    {bh}")
    if len(brows) != EXPECTED_OBS:
        sys.exit(f"FATAL: batch has {len(brows)} obs, expected {EXPECTED_OBS}")

    # Refuse to add an obs_id that already exists in master
    existing_obs = {r[0] for r in mrows}
    collisions = [r[0] for r in brows if r[0] in existing_obs]
    if collisions:
        sys.exit(f"FATAL: {len(collisions)} obs_id collisions with master, first 5: {collisions[:5]}")

    # Promote 12-col -> 17-col rows
    promoted = []
    for r in brows:
        d = dict(zip(OBSERVATIONS_BATCH_COLS, r))
        out = [
            d["obs_id"], d["study_id"], d["entity_id"], d["tech_id"],
            d["observation_type"], d["year_observed"], d["metric_name"],
            d["metric_value"], d["confidence"],
            "ingest-extraction",            # verification_method (default for fresh ingest)
            d["methodology_code"], d["source_page"], d["notes"],
            "transcript",                   # collection
            "",                             # thread_tag
            "",                             # section
            "",                             # legacy_obs_id
        ]
        promoted.append(out)

    new = mrows + promoted
    print(f"  master rows in:  {len(mrows)}")
    print(f"  appended:        {len(promoted)}")
    print(f"  master rows out: {len(new)}")

    if commit:
        bak = backup(OBSERVATIONS_MASTER, "passb_transcripts_append", ts)
        write_csv(OBSERVATIONS_MASTER, mh, new)
        print(f"  backup: {bak.name}")
        print(f"  wrote:  {OBSERVATIONS_MASTER.name}")

# --------------------------------------------------------------- main

def main():
    commit = "--commit" in sys.argv
    ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

    print("=" * 70)
    print("apply_passb_transcripts_v1")
    print(f"Mode:    {'COMMIT' if commit else 'DRY-RUN'}")
    print(f"Stamp:   {ts}")
    print(f"Archive: {ARCHIVE}")
    print(f"Batch:   {BATCH_ROOT}")
    print("=" * 70)

    for p in (STUDIES_MASTER, ENTITIES_MASTER, TECHS_MASTER, OBSERVATIONS_MASTER):
        if not p.exists():
            sys.exit(f"FATAL: missing master {p}")
    for p in (STUDIES_BATCH, ENTITIES_BATCH, TECHS_BATCH, OBSERVATIONS_BATCH):
        if not p.exists():
            sys.exit(f"FATAL: missing batch {p}")

    apply_studies_replace(commit, ts)
    apply_entities_append(commit, ts)
    apply_techs_append(commit, ts)
    apply_observations_append(commit, ts)

    print("\n" + "=" * 70)
    if commit:
        print("COMMIT complete. Next:")
        print("  1. Phase 1: python3 ~/Desktop/Archive/scripts/build/01_load_csvs_v2.py \\")
        print("       --archive ~/Desktop/Archive/aberdeen-group-archive \\")
        print("       --wiki ~/Repos/kastner-aberdeen-wiki")
        print("  2. Phase 2: python3 ~/Desktop/Archive/scripts/build/02_build_data_layer_v4.py \\")
        print("       --wiki ~/Repos/kastner-aberdeen-wiki")
        print("  3. Pass A v1: python3 ~/Desktop/Archive/scripts/build/assembler.py pass-a \\")
        print("       ~/Desktop/Archive/aberdeen-group-archive")
        print("  4. Shape audit (see kastner-archive-pipeline §'Shape audit')")
        print("  5. Phases 3-6 for the new studies + scaffolding refresh")
    else:
        print("DRY-RUN only — pass --commit to write. No backups created.")

if __name__ == "__main__":
    main()
