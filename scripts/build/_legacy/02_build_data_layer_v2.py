#!/usr/bin/env python3
"""
02_build_data_layer_v2.py — Phase 2: Parquet → DuckDB (v1.5)

v2 corrections vs v1:
  - v2 Phase 1 emits staging parquet with friendly names (studies.parquet,
    entities.parquet, …) — no rename map needed
  - Adds entity_studies, tech_studies, codes, collection_stats_agg
  - Views use real column names (entity_name not canonical_name, pub_year
    derived in Phase 1, study_prescience_enum split from obs prescience)
  - Adds v_codes, v_entity_studies, v_tech_studies, v_collection_overview
  - v_high_holistic_prescience exposes the STUDY-LEVEL enum (high/medium/...)
    separately from obs-level numeric scores

Usage:
  python3 02_build_data_layer_v2.py --wiki ~/Desktop/kastner_wiki
"""
from __future__ import annotations
import argparse
import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import duckdb
except ImportError:
    sys.exit("ERROR: duckdb required. pip3 install duckdb")


# Staging file names that Phase 1 v2 emits (already friendly names)
PROMOTE = [
    "studies", "entities", "technologies", "observations",
    "prescience_scores", "known_entities", "known_technologies",
    "collection_stats", "collection_stats_agg",
    "codes", "entity_studies", "tech_studies",
]


VIEW_SQL = [
    # ---------- core tables as views ----------
    ("v_studies",              "SELECT * FROM read_parquet('{data}/studies.parquet')"),
    ("v_entities",             "SELECT * FROM read_parquet('{data}/entities.parquet')"),
    ("v_technologies",         "SELECT * FROM read_parquet('{data}/technologies.parquet')"),
    ("v_observations",         "SELECT * FROM read_parquet('{data}/observations.parquet')"),
    ("v_prescience_raw",       "SELECT * FROM read_parquet('{data}/prescience_scores.parquet')"),
    ("v_known_entities",       "SELECT * FROM read_parquet('{data}/known_entities.parquet')"),
    ("v_known_technologies",   "SELECT * FROM read_parquet('{data}/known_technologies.parquet')"),
    ("v_collection_stats",     "SELECT * FROM read_parquet('{data}/collection_stats.parquet')"),
    ("v_collection_overview",  "SELECT * FROM read_parquet('{data}/collection_stats_agg.parquet')"),
    ("v_codes",                "SELECT * FROM read_parquet('{data}/codes.parquet')"),
    ("v_entity_studies",       "SELECT * FROM read_parquet('{data}/entity_studies.parquet')"),
    ("v_tech_studies",         "SELECT * FROM read_parquet('{data}/tech_studies.parquet')"),

    # ---------- prescience: obs-level numeric (Pass C) ----------
    ("v_observations_with_prescience", """
        SELECT * FROM v_observations
        WHERE prescience_score IS NOT NULL
    """),
    ("v_studies_with_prescience", """
        SELECT * FROM v_studies
        WHERE prescience_obs_count > 0
    """),
    ("v_top_prescient_studies", """
        SELECT study_id, title, author, pub_year, type,
               prescience_max, prescience_mean, prescience_obs_count,
               study_prescience_enum
        FROM v_studies
        WHERE prescience_max = 5
        ORDER BY prescience_mean DESC NULLS LAST, prescience_obs_count DESC
    """),
    ("v_studies_with_high_prescience", """
        SELECT study_id, title, author, pub_year, type,
               prescience_max, prescience_mean, prescience_obs_count
        FROM v_studies
        WHERE prescience_max >= 4
        ORDER BY prescience_max DESC, prescience_mean DESC NULLS LAST
    """),
    ("v_prescience_by_decade", """
        SELECT
            CAST(pub_year / 10 * 10 AS INTEGER) || 's' AS decade,
            COUNT(*) FILTER (WHERE prescience_max >= 4) AS high_prescience_studies,
            COUNT(*) FILTER (WHERE prescience_obs_count > 0) AS studies_scored,
            COUNT(*) AS studies_total
        FROM v_studies
        WHERE pub_year IS NOT NULL
        GROUP BY decade
        ORDER BY decade
    """),
    ("v_low_confidence_prescience", """
        SELECT obs_id, study_id, prescience_score, prescience_confidence,
               prescience_rationale
        FROM v_observations
        WHERE prescience_confidence = 1
        ORDER BY study_id, obs_id
    """),

    # ---------- prescience: STUDY-LEVEL enum (high/medium/low/n-a) ----------
    ("v_high_holistic_prescience", """
        SELECT study_id, title, author, pub_year, type,
               study_prescience_enum, study_prescience_rationale,
               prescience_max, prescience_mean
        FROM v_studies
        WHERE study_prescience_enum = 'high'
        ORDER BY pub_year, study_id
    """),
    ("v_holistic_prescience_distribution", """
        SELECT study_prescience_enum, COUNT(*) AS n_studies
        FROM v_studies
        GROUP BY study_prescience_enum
        ORDER BY n_studies DESC
    """),

    # ---------- general navigation ----------
    ("v_studies_by_decade", """
        SELECT
            CAST(pub_year / 10 * 10 AS INTEGER) || 's' AS decade,
            COUNT(*) AS studies
        FROM v_studies
        WHERE pub_year IS NOT NULL
        GROUP BY decade
        ORDER BY decade
    """),
    ("v_entities_with_observation_count", """
        SELECT entity_id, entity_name, entity_type, sector, status,
               years_active, occurrence_count
        FROM v_entities
        ORDER BY occurrence_count DESC NULLS LAST
    """),
    ("v_technologies_by_lifecycle", """
        SELECT tech_id, tech_name, category, vendor, era,
               lifecycle_at_study, lifecycle_current, occurrence_count
        FROM v_technologies
        ORDER BY occurrence_count DESC NULLS LAST
    """),
    ("v_observations_by_year", """
        SELECT year_observed, COUNT(*) AS obs_count
        FROM v_observations
        WHERE year_observed IS NOT NULL AND year_observed != ''
        GROUP BY year_observed
        ORDER BY year_observed
    """),

    # ---------- codes dictionary ----------
    ("v_codes_by_type", """
        SELECT code_type, COUNT(*) AS n_codes
        FROM v_codes
        GROUP BY code_type
        ORDER BY n_codes DESC
    """),
    ("v_methodology_codes", """
        SELECT code_id, label, definition
        FROM v_codes
        WHERE code_type = 'methodology'
        ORDER BY code_id
    """),
    ("v_technology_category_codes", """
        SELECT code_id, label, definition
        FROM v_codes
        WHERE code_type = 'technology-category'
        ORDER BY code_id
    """),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki", required=True)
    args = ap.parse_args()

    wiki = Path(args.wiki).resolve()
    staging = wiki / "data" / "_validated"
    data = wiki / "data"
    db_dir = wiki / "db"
    db_dir.mkdir(parents=True, exist_ok=True)

    if not staging.exists():
        sys.exit(f"HALT: staging missing — run Phase 1 first. ({staging})")

    # Promote: copy staging files to data/ (already friendly names in v2)
    for name in PROMOTE:
        src = staging / f"{name}.parquet"
        if not src.exists():
            sys.exit(f"HALT: missing staging file {src}")
        shutil.copy2(src, data / f"{name}.parquet")
        print(f"  [promote] {src.name} → data/")

    # Build DuckDB
    db_path = db_dir / "kastner.duckdb"
    if db_path.exists():
        db_path.unlink()
    con = duckdb.connect(str(db_path))
    rowcounts: dict[str, int] = {}
    for name, sql_tmpl in VIEW_SQL:
        sql = sql_tmpl.format(data=str(data).replace("'", "''"))
        try:
            con.execute(f"CREATE OR REPLACE VIEW {name} AS {sql}")
            n = con.execute(f"SELECT COUNT(*) FROM {name}").fetchone()[0]
            rowcounts[name] = int(n)
            print(f"  [view] {name}: {n} rows")
        except Exception as e:
            print(f"  [ERR] view {name} failed: {e}", file=sys.stderr)
            con.close()
            sys.exit(2)
    con.close()

    # Manifest
    manifest_path = wiki / "build_manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    manifest["phase_2"] = {
        "phase": 2,
        "phase_name": "build_data_layer",
        "version": "v2",
        "ran_at": datetime.now(timezone.utc).isoformat(),
        "duckdb_path": str(db_path.relative_to(wiki)),
        "view_rowcounts": rowcounts,
    }
    tmp = manifest_path.with_suffix(".json.tmp")
    with open(tmp, "w") as f:
        json.dump(manifest, f, indent=2, sort_keys=True, default=str)
    os.replace(tmp, manifest_path)
    print(f"\n✓ Phase 2 complete: {db_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
