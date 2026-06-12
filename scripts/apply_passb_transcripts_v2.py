#!/usr/bin/env python3
"""apply_passb_transcripts_v2.py — Pass B transcript batch apply, schema-correct.

Changes vs v1:
  - SKIPS studies REPLACE (already applied to Mac at 2026-06-12 17:18:13Z;
    backup exists at _master_studies.csv.bak_passb_transcripts_replace_20260612T171813Z)
  - entities/technologies: dedupe by id, APPEND only new ids using 8-col master
    schema (drop per-study study_id column, keep canonical notes)
  - entity_studies / tech_studies M:N join tables: APPEND new (id, study_id)
    pairs from the batch after dedupe against existing pairs
  - observations: same 12-col -> 17-col promote as v1

Master schemas on Mac (source of truth, NOT documented in archival-ingest v20):
  _master_studies.csv         16 cols
  _master_entities.csv         8 cols  (entity_id, entity_name, entity_type,
                                        sector, status, successor,
                                        years_active, notes) — NO study_id
  _master_technologies.csv     8 cols  (tech_id, tech_name, category, vendor,
                                        era, lifecycle_at_study,
                                        lifecycle_current, notes) — NO study_id
  _master_observations.csv    17 cols  (v20 superset)
  _master_entity_studies.csv   2 cols  (entity_id, study_id) — M:N join
  _master_tech_studies.csv     2 cols  (tech_id, study_id)   — M:N join

Per-study batch CSVs we ship are 9-col entities/techs (WITH study_id) and
12-col observations. This script bridges that schema to the master schema.

Invariants:
  - csv.QUOTE_ALL on every write (§16.5)
  - UTC-timestamped backups before any write
  - Dry-run default; --commit opt-in
  - Row-parity reporting (master rows before/after)
"""
import csv
import shutil
import datetime
import sys
from pathlib import Path

ARCHIVE = Path.home() / "Desktop/Archive/archive_masters"

# Master files
M_ENTITIES        = ARCHIVE / "_master_entities.csv"
M_TECHS           = ARCHIVE / "_master_technologies.csv"
M_OBSERVATIONS    = ARCHIVE / "_master_observations.csv"
M_ENTITY_STUDIES  = ARCHIVE / "_master_entity_studies.csv"
M_TECH_STUDIES    = ARCHIVE / "_master_tech_studies.csv"

# Batch files (shipped to Mac at ~/Desktop/Archive/passb_batch/)
BATCH_DIR = Path.home() / "Desktop/Archive/passb_batch"
B_ENTITIES        = BATCH_DIR / "batch_entities_APPEND_v1.csv"
B_TECHS           = BATCH_DIR / "batch_technologies_APPEND_v1.csv"
B_OBSERVATIONS    = BATCH_DIR / "batch_observations_APPEND_v1.csv"

# Expected master schemas (8 cols ent/tech; 17 cols obs)
ENT_MASTER_COLS = ["entity_id", "entity_name", "entity_type", "sector",
                   "status", "successor", "years_active", "notes"]
TECH_MASTER_COLS = ["tech_id", "tech_name", "category", "vendor", "era",
                    "lifecycle_at_study", "lifecycle_current", "notes"]
OBS_MASTER_COLS = ["obs_id", "study_id", "entity_id", "tech_id",
                   "observation_type", "year_observed", "metric_name",
                   "metric_value", "confidence", "verification_method",
                   "methodology_code", "source_page", "notes", "collection",
                   "thread_tag", "section", "legacy_obs_id"]

# Per-study batch schemas
ENT_BATCH_COLS = ["entity_id", "entity_name", "entity_type", "sector",
                  "status", "successor", "years_active", "study_id", "notes"]
TECH_BATCH_COLS = ["tech_id", "tech_name", "category", "vendor", "era",
                   "lifecycle_at_study", "lifecycle_current", "study_id", "notes"]
OBS_BATCH_COLS = ["obs_id", "study_id", "entity_id", "tech_id",
                  "observation_type", "year_observed", "metric_name",
                  "metric_value", "confidence", "methodology_code",
                  "source_page", "notes"]


def utc_stamp():
    return datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")


def read_csv_rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
    return header, rows


def write_csv_quote_all(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        w.writerows(rows)


def assert_header(actual, expected, label):
    if actual != expected:
        print(f"FATAL: {label} header mismatch.")
        print(f"  actual:   {actual}")
        print(f"  expected: {expected}")
        sys.exit(2)


def main():
    commit = "--commit" in sys.argv
    ts = utc_stamp()

    print("=" * 72)
    print("apply_passb_transcripts_v2.py")
    print(f"Mode: {'COMMIT' if commit else 'DRY-RUN'}")
    print(f"UTC stamp: {ts}")
    print("=" * 72)

    # Sanity: archive + batch dirs exist
    for p in [ARCHIVE, BATCH_DIR]:
        if not p.is_dir():
            sys.exit(f"FATAL: directory not found: {p}")

    # ------------------------------------------------------------------
    # Load masters
    # ------------------------------------------------------------------
    ent_h, ent_rows = read_csv_rows(M_ENTITIES)
    tech_h, tech_rows = read_csv_rows(M_TECHS)
    obs_h, obs_rows = read_csv_rows(M_OBSERVATIONS)
    es_h, es_rows = read_csv_rows(M_ENTITY_STUDIES)
    ts_h, ts_rows = read_csv_rows(M_TECH_STUDIES)

    assert_header(ent_h, ENT_MASTER_COLS, "_master_entities.csv")
    assert_header(tech_h, TECH_MASTER_COLS, "_master_technologies.csv")
    assert_header(obs_h, OBS_MASTER_COLS, "_master_observations.csv")
    # join-table headers we trust as-is (2 cols each)
    if es_h != ["entity_id", "study_id"]:
        sys.exit(f"FATAL: _master_entity_studies.csv header = {es_h}")
    if ts_h != ["tech_id", "study_id"]:
        sys.exit(f"FATAL: _master_tech_studies.csv header = {ts_h}")

    print(f"\nMaster shape (before):")
    print(f"  entities:        {len(ent_rows):>6} rows × {len(ent_h)} cols")
    print(f"  technologies:    {len(tech_rows):>6} rows × {len(tech_h)} cols")
    print(f"  observations:    {len(obs_rows):>6} rows × {len(obs_h)} cols")
    print(f"  entity_studies:  {len(es_rows):>6} rows × {len(es_h)} cols")
    print(f"  tech_studies:    {len(ts_rows):>6} rows × {len(ts_h)} cols")

    # ------------------------------------------------------------------
    # Load batches
    # ------------------------------------------------------------------
    be_h, be_rows = read_csv_rows(B_ENTITIES)
    bt_h, bt_rows = read_csv_rows(B_TECHS)
    bo_h, bo_rows = read_csv_rows(B_OBSERVATIONS)

    assert_header(be_h, ENT_BATCH_COLS, "batch_entities_APPEND_v1.csv")
    assert_header(bt_h, TECH_BATCH_COLS, "batch_technologies_APPEND_v1.csv")
    assert_header(bo_h, OBS_BATCH_COLS, "batch_observations_APPEND_v1.csv")

    print(f"\nBatch input:")
    print(f"  batch_entities:      {len(be_rows):>4} rows (9-col)")
    print(f"  batch_technologies:  {len(bt_rows):>4} rows (9-col)")
    print(f"  batch_observations:  {len(bo_rows):>4} rows (12-col)")

    # ------------------------------------------------------------------
    # ENTITIES: dedupe by entity_id; APPEND new only
    # ------------------------------------------------------------------
    existing_ent_ids = {r[0] for r in ent_rows}
    new_ent_rows = []
    seen_new = set()
    for r in be_rows:
        eid = r[0]
        if eid in existing_ent_ids:
            continue
        if eid in seen_new:
            continue  # batch had multiple rows for same new id; take first
        seen_new.add(eid)
        # Drop study_id (col 7 in 9-col batch); 8-col master schema
        master_row = [r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[8]]
        new_ent_rows.append(master_row)

    print(f"\nEntities:")
    print(f"  batch unique ids:    {len({r[0] for r in be_rows})}")
    print(f"  already in master:   {len({r[0] for r in be_rows}) - len(new_ent_rows)}")
    print(f"  new to append:       {len(new_ent_rows)}")

    # entity_studies pairs from batch (entity_id, study_id) — dedupe vs existing
    existing_es_pairs = {(r[0], r[1]) for r in es_rows}
    new_es_pairs = []
    seen_es = set()
    for r in be_rows:
        pair = (r[0], r[7])  # entity_id, study_id
        if pair in existing_es_pairs or pair in seen_es:
            continue
        seen_es.add(pair)
        new_es_pairs.append([pair[0], pair[1]])

    print(f"  new (eid,sid) pairs: {len(new_es_pairs)}  -> _master_entity_studies.csv")

    # ------------------------------------------------------------------
    # TECHNOLOGIES: dedupe by tech_id; APPEND new only
    # ------------------------------------------------------------------
    existing_tech_ids = {r[0] for r in tech_rows}
    new_tech_rows = []
    seen_new_t = set()
    for r in bt_rows:
        tid = r[0]
        if tid in existing_tech_ids:
            continue
        if tid in seen_new_t:
            continue
        seen_new_t.add(tid)
        master_row = [r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[8]]
        new_tech_rows.append(master_row)

    print(f"\nTechnologies:")
    print(f"  batch unique ids:    {len({r[0] for r in bt_rows})}")
    print(f"  already in master:   {len({r[0] for r in bt_rows}) - len(new_tech_rows)}")
    print(f"  new to append:       {len(new_tech_rows)}")

    existing_ts_pairs = {(r[0], r[1]) for r in ts_rows}
    new_ts_pairs = []
    seen_ts = set()
    for r in bt_rows:
        pair = (r[0], r[7])  # tech_id, study_id
        if pair in existing_ts_pairs or pair in seen_ts:
            continue
        seen_ts.add(pair)
        new_ts_pairs.append([pair[0], pair[1]])

    print(f"  new (tid,sid) pairs: {len(new_ts_pairs)}  -> _master_tech_studies.csv")

    # ------------------------------------------------------------------
    # OBSERVATIONS: 12-col -> 17-col promote
    # ------------------------------------------------------------------
    existing_obs_ids = {r[0] for r in obs_rows}
    new_obs_rows = []
    dup_obs = []
    for r in bo_rows:
        if r[0] in existing_obs_ids:
            dup_obs.append(r[0])
            continue
        # 12-col batch:
        #   0:obs_id 1:study_id 2:entity_id 3:tech_id 4:observation_type
        #   5:year_observed 6:metric_name 7:metric_value 8:confidence
        #   9:methodology_code 10:source_page 11:notes
        # 17-col master:
        #   0:obs_id 1:study_id 2:entity_id 3:tech_id 4:observation_type
        #   5:year_observed 6:metric_name 7:metric_value 8:confidence
        #   9:verification_method  10:methodology_code 11:source_page
        #   12:notes 13:collection 14:thread_tag 15:section 16:legacy_obs_id
        master_row = [
            r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8],
            "ingest-extraction",  # verification_method default (§17.1)
            r[9],                  # methodology_code
            r[10],                 # source_page
            r[11],                 # notes
            "transcript",          # collection (v20 §13.1)
            "",                    # thread_tag
            "",                    # section
            "",                    # legacy_obs_id (canonical from birth)
        ]
        new_obs_rows.append(master_row)

    print(f"\nObservations:")
    print(f"  batch rows:          {len(bo_rows)}")
    print(f"  already in master:   {len(dup_obs)}")
    print(f"  new to append:       {len(new_obs_rows)}")
    if dup_obs:
        print(f"  WARNING: duplicate obs_ids: {dup_obs[:5]}{'...' if len(dup_obs)>5 else ''}")

    # ------------------------------------------------------------------
    # Compose final tables
    # ------------------------------------------------------------------
    ent_final  = ent_rows + new_ent_rows
    tech_final = tech_rows + new_tech_rows
    obs_final  = obs_rows + new_obs_rows
    es_final   = es_rows + new_es_pairs
    ts_final   = ts_rows + new_ts_pairs

    print(f"\nMaster shape (after):")
    print(f"  entities:        {len(ent_final):>6} rows  (+{len(new_ent_rows)})")
    print(f"  technologies:    {len(tech_final):>6} rows  (+{len(new_tech_rows)})")
    print(f"  observations:    {len(obs_final):>6} rows  (+{len(new_obs_rows)})")
    print(f"  entity_studies:  {len(es_final):>6} rows  (+{len(new_es_pairs)})")
    print(f"  tech_studies:    {len(ts_final):>6} rows  (+{len(new_ts_pairs)})")

    if not commit:
        print("\nDRY-RUN — no files written. Re-run with --commit to apply.")
        return

    # ------------------------------------------------------------------
    # COMMIT: backup + write
    # ------------------------------------------------------------------
    print("\nWriting files...")
    for src, label in [
        (M_ENTITIES,       "entities"),
        (M_TECHS,          "techs"),
        (M_OBSERVATIONS,   "observations"),
        (M_ENTITY_STUDIES, "entity_studies"),
        (M_TECH_STUDIES,   "tech_studies"),
    ]:
        bak = src.with_suffix(f".csv.bak_passb_v2_{label}_{ts}")
        shutil.copy2(src, bak)
        print(f"  backup: {bak.name}")

    write_csv_quote_all(M_ENTITIES,       ENT_MASTER_COLS,  ent_final)
    write_csv_quote_all(M_TECHS,          TECH_MASTER_COLS, tech_final)
    write_csv_quote_all(M_OBSERVATIONS,   OBS_MASTER_COLS,  obs_final)
    write_csv_quote_all(M_ENTITY_STUDIES, ["entity_id", "study_id"], es_final)
    write_csv_quote_all(M_TECH_STUDIES,   ["tech_id",   "study_id"], ts_final)

    print("  wrote: _master_entities.csv")
    print("  wrote: _master_technologies.csv")
    print("  wrote: _master_observations.csv")
    print("  wrote: _master_entity_studies.csv")
    print("  wrote: _master_tech_studies.csv")
    print("\nDONE. Next: re-run Phase 1 + Phase 2.")


if __name__ == "__main__":
    main()
