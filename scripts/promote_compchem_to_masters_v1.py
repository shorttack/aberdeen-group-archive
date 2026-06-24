#!/usr/bin/env python3
"""
promote_compchem_to_masters_v1.py

Promote the CompChem 1989 study-local CSVs into the archive masters so Phase 1
can pick them up on next rebuild.

Source:  ~/Desktop/Archive/aberdeen-group-archive/project_examples/conflicting-trends-computational-chemistry-fe5c31/data/*.csv
Target:  ~/Desktop/Archive/aberdeen-group-archive/_master_*.csv

What gets appended (with dedupe-skip on primary key):
  studies:        +1 row     (PK: study_id)
  entities:       +24 rows   (PK: entity_id; skip if already in master)
  technologies:   +10 rows   (PK: tech_id; skip if already in master)
  observations:   +64 rows   (PK: obs_id)
  codes:          +31 rows   (PK: code_id; skip if already in master)
  entity_studies: +24 pairs  (PK: entity_id+study_id; skip if already in master)
  tech_studies:   +10 pairs  (PK: tech_id+study_id; skip if already in master)

Dedupe collisions are logged to a sidecar:
  ~/Desktop/Archive/aberdeen-group-archive/promote_compchem_v1_collisions.txt

Schema reconciliation (study CSV → master):
  - entities: drop the study CSV's trailing `study_id` column (master has 8 cols, study has 9)
  - technologies: drop the study CSV's trailing `study_id` column (master has 8, study has 9)
  - observations: pad study CSV's 12 cols out to master's 17 by inserting:
        verification_method (pos 9 in master, after `confidence`)  -> blank
        collection (pos 13)                                        -> blank
        thread_tag (pos 14)                                        -> blank
        section (pos 15)                                           -> blank
        legacy_obs_id (pos 16)                                     -> blank

All writes:
  - Backup before write: _master_<table>.csv.bak_promote_compchem_<utc-stamp>
  - csv.QUOTE_ALL on every write
  - Dry-run default; --commit to actually write
  - Row count delta printed (before/after) for every master
"""
import csv, shutil, datetime, sys
from pathlib import Path

ARCHIVE_MASTERS = Path.home() / "Desktop/Archive/aberdeen-group-archive"
STUDY_DATA = Path.home() / "Desktop/Archive/aberdeen-group-archive/project_examples/conflicting-trends-computational-chemistry-fe5c31/data"

STUDY_ID = "conflicting-trends-computational-chemistry-fe5c31"

COMMIT = "--commit" in sys.argv
TS = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

# ---------------------------------------------------------------- #
# Master schemas (column order, exact, verified against repo blobs) #
# ---------------------------------------------------------------- #
MASTER_SCHEMAS = {
    "_master_studies.csv": [
        "study_id","title","author","date","type","subject_domain","methodology",
        "source_file","abstract","license","importance","importance_rationale",
        "relevance","relevance_rationale","prescience","prescience_rationale",
    ],
    "_master_entities.csv": [
        "entity_id","entity_name","entity_type","sector","status","successor",
        "years_active","notes",
    ],
    "_master_technologies.csv": [
        "tech_id","tech_name","category","vendor","era","lifecycle_at_study",
        "lifecycle_current","notes",
    ],
    "_master_observations.csv": [
        "obs_id","study_id","entity_id","tech_id","observation_type","year_observed",
        "metric_name","metric_value","confidence","verification_method",
        "methodology_code","source_page","notes","collection","thread_tag","section",
        "legacy_obs_id",
    ],
    "_master_codes.csv": [
        "code_id","code_type","label","definition",
    ],
    "_master_entity_studies.csv": [
        "entity_id","study_id",
    ],
    "_master_tech_studies.csv": [
        "tech_id","study_id",
    ],
}

# Primary keys used for dedupe (skip-append on collision)
PK = {
    "_master_studies.csv":         ("study_id",),
    "_master_entities.csv":        ("entity_id",),
    "_master_technologies.csv":    ("tech_id",),
    "_master_observations.csv":    ("obs_id",),
    "_master_codes.csv":           ("code_id",),
    "_master_entity_studies.csv":  ("entity_id","study_id"),
    "_master_tech_studies.csv":    ("tech_id","study_id"),
}

# ----------------------------------- #
# Helpers                              #
# ----------------------------------- #
def read_csv_dict(path):
    """Returns (header, rows) where rows is list[dict]."""
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        return reader.fieldnames, rows

def write_csv_dict(path, header, rows):
    """QUOTE_ALL write with explicit header order."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL,
                           extrasaction="ignore")
        w.writeheader()
        for r in rows:
            # Ensure every column key exists (blank if missing)
            row = {k: r.get(k, "") for k in header}
            w.writerow(row)

def backup(master_path):
    bak = master_path.with_name(master_path.name + f".bak_promote_compchem_{TS}")
    shutil.copy2(master_path, bak)
    return bak

def existing_keys(rows, key_cols):
    """Return set of tuple-keys from existing master rows."""
    return {tuple(r.get(c,"") for c in key_cols) for r in rows}

# ----------------------------------- #
# Loaders for study-local CSVs        #
# ----------------------------------- #
def load_compchem_studies():
    _, rows = read_csv_dict(STUDY_DATA / "studies.csv")
    return rows

def load_compchem_entities():
    """Drop the trailing study_id col -> 8-col master shape."""
    _, rows = read_csv_dict(STUDY_DATA / "entities.csv")
    out = []
    for r in rows:
        m = {k: r.get(k,"") for k in MASTER_SCHEMAS["_master_entities.csv"]}
        out.append(m)
    return out, rows  # also return raw for entity_studies pairs

def load_compchem_technologies():
    """Drop the trailing study_id col -> 8-col master shape."""
    _, rows = read_csv_dict(STUDY_DATA / "technologies.csv")
    out = []
    for r in rows:
        m = {k: r.get(k,"") for k in MASTER_SCHEMAS["_master_technologies.csv"]}
        out.append(m)
    return out, rows  # also return raw for tech_studies pairs

def load_compchem_observations():
    """Pad 12-col study shape -> 17-col master shape (5 blank cols added)."""
    _, rows = read_csv_dict(STUDY_DATA / "observations.csv")
    out = []
    for r in rows:
        m = {k: r.get(k,"") for k in MASTER_SCHEMAS["_master_observations.csv"]}
        # study CSV doesn't carry these; leave blank
        for c in ("verification_method","collection","thread_tag","section","legacy_obs_id"):
            m[c] = ""
        out.append(m)
    return out

def load_compchem_codes():
    _, rows = read_csv_dict(STUDY_DATA / "codes.csv")
    return rows

def derive_entity_studies(entities_raw):
    """Pairs: (entity_id, study_id) from study-local entities."""
    return [{"entity_id": r["entity_id"], "study_id": r["study_id"]} for r in entities_raw]

def derive_tech_studies(techs_raw):
    """Pairs: (tech_id, study_id) from study-local technologies."""
    return [{"tech_id": r["tech_id"], "study_id": r["study_id"]} for r in techs_raw]

# ----------------------------------- #
# Per-master promote                  #
# ----------------------------------- #
def promote(master_name, new_rows, collisions_log):
    master_path = ARCHIVE_MASTERS / master_name
    header = MASTER_SCHEMAS[master_name]
    keys = PK[master_name]

    # Read existing master
    with open(master_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        existing_rows = list(reader)
        master_header = reader.fieldnames or []

    # Sanity check master header matches our schema (warn on mismatch — DO NOT proceed)
    if master_header != header:
        print(f"  SCHEMA MISMATCH on {master_name}!")
        print(f"    master header: {master_header}")
        print(f"    expected:      {header}")
        print(f"  ABORTING this master (script needs to be updated).")
        return None

    before_count = len(existing_rows)
    existing_key_set = existing_keys(existing_rows, keys)

    # Filter new_rows: skip those whose PK already exists
    to_append = []
    skipped = []
    for r in new_rows:
        k = tuple(r.get(c,"") for c in keys)
        if k in existing_key_set:
            skipped.append((master_name, k))
        else:
            to_append.append(r)
            existing_key_set.add(k)  # also dedupe within new_rows itself

    after_count = before_count + len(to_append)

    print(f"  {master_name}: before={before_count}  to_append={len(to_append)}  "
          f"skipped(dedupe)={len(skipped)}  after={after_count}")

    for s in skipped:
        collisions_log.append(s)

    if COMMIT:
        bak = backup(master_path)
        print(f"    backup: {bak.name}")
        # Append new rows
        combined = existing_rows + to_append
        write_csv_dict(master_path, header, combined)
        print(f"    wrote:  {master_path.name}  ({after_count} rows)")
    else:
        print(f"    DRY-RUN — no write")

    return {"before": before_count, "appended": len(to_append),
            "skipped": len(skipped), "after": after_count}

# ----------------------------------- #
# Main                                #
# ----------------------------------- #
def main():
    print(f"=== promote_compchem_to_masters_v1 ===")
    print(f"Mode: {'COMMIT' if COMMIT else 'DRY-RUN'}")
    print(f"UTC stamp: {TS}")
    print(f"Source: {STUDY_DATA}")
    print(f"Target: {ARCHIVE_MASTERS}")
    print()

    # Pre-flight: source dir must exist
    if not STUDY_DATA.exists():
        sys.exit(f"FATAL: source dir not found: {STUDY_DATA}")
    if not ARCHIVE_MASTERS.exists():
        sys.exit(f"FATAL: target dir not found: {ARCHIVE_MASTERS}")

    # Pre-flight: required study CSVs
    for fn in ("studies.csv","entities.csv","technologies.csv","observations.csv","codes.csv"):
        if not (STUDY_DATA / fn).exists():
            sys.exit(f"FATAL: missing source CSV: {STUDY_DATA / fn}")

    # Pre-flight: master CSVs must exist
    for m in MASTER_SCHEMAS:
        if not (ARCHIVE_MASTERS / m).exists():
            sys.exit(f"FATAL: missing master: {ARCHIVE_MASTERS / m}")

    # Load study-local rows
    studies      = load_compchem_studies()
    entities, entities_raw = load_compchem_entities()
    techs,    techs_raw    = load_compchem_technologies()
    observations = load_compchem_observations()
    codes        = load_compchem_codes()
    ent_studies  = derive_entity_studies(entities_raw)
    tech_studies = derive_tech_studies(techs_raw)

    print(f"Loaded CompChem study-local rows:")
    print(f"  studies:        {len(studies)}")
    print(f"  entities:       {len(entities)}")
    print(f"  technologies:   {len(techs)}")
    print(f"  observations:   {len(observations)}")
    print(f"  codes:          {len(codes)}")
    print(f"  entity_studies: {len(ent_studies)}")
    print(f"  tech_studies:   {len(tech_studies)}")
    print()

    # Sanity: every row should reference the CompChem study_id
    for r in studies:
        if r["study_id"] != STUDY_ID:
            sys.exit(f"FATAL: studies.csv has unexpected study_id: {r['study_id']}")
    for r in observations:
        if r["study_id"] != STUDY_ID:
            sys.exit(f"FATAL: obs row has unexpected study_id: {r['study_id']}")

    print(f"Per-master promote (in dependency order):")
    print()

    collisions = []
    results = {}
    results["studies"]        = promote("_master_studies.csv",        studies,      collisions)
    results["entities"]       = promote("_master_entities.csv",       entities,     collisions)
    results["technologies"]   = promote("_master_technologies.csv",   techs,        collisions)
    results["observations"]   = promote("_master_observations.csv",   observations, collisions)
    results["codes"]          = promote("_master_codes.csv",          codes,        collisions)
    results["entity_studies"] = promote("_master_entity_studies.csv", ent_studies,  collisions)
    results["tech_studies"]   = promote("_master_tech_studies.csv",   tech_studies, collisions)

    print()
    print(f"=== summary ===")
    for k,v in results.items():
        if v is None:
            print(f"  {k}: ABORTED (schema mismatch)")
        else:
            print(f"  {k}: +{v['appended']} appended, {v['skipped']} skipped (dedupe), "
                  f"{v['before']} -> {v['after']}")

    # Write collisions sidecar
    if collisions:
        sidecar = ARCHIVE_MASTERS / f"promote_compchem_v1_collisions.txt"
        if COMMIT:
            with open(sidecar, "w", encoding="utf-8") as f:
                f.write(f"# Dedupe-skip collisions from promote_compchem_to_masters_v1.py\n")
                f.write(f"# UTC stamp: {TS}\n")
                f.write(f"# total: {len(collisions)}\n\n")
                for master, key in collisions:
                    f.write(f"{master}\t{key}\n")
            print(f"  collisions sidecar: {sidecar.name}")
        else:
            print(f"  (DRY-RUN: would write {len(collisions)} collisions to "
                  f"{sidecar.name})")
    else:
        print(f"  no dedupe collisions")

    if not COMMIT:
        print()
        print("DRY-RUN ONLY — pass --commit to actually write.")

if __name__ == "__main__":
    main()
