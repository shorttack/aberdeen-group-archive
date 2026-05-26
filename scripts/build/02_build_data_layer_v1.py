#!/usr/bin/env python3
"""
02_build_data_layer_v1.py — Phase 2: Parquet + DuckDB (v1.5)

Promotes the Phase-1 staging Parquet into data/, then creates db/kastner.duckdb
with ~18 named views. v1.5 adds prescience-aware views.

Usage:
  python3 02_build_data_layer_v1.py --wiki ~/Desktop/kastner_wiki

v1.5 new/changed views:
  v_studies_with_prescience            — full studies + max/mean prescience
  v_top_prescient_studies              — studies with at least one obs scored 5
  v_prescience_by_decade               — count of >=4 prescient obs per decade
  v_prescience_by_collection           — same per collection
  v_studies_with_high_prescience       — backwards-compat alias (kept for v1 pages)
  v_observations_with_prescience       — obs joined with score+rationale
  v_low_confidence_prescience          — for the cloud reviewer queue
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


VIEW_SQL = [
    # ---------- core (existing v1.4 catalog, lightly renamed v_*) ----------
    ("v_studies", """
        SELECT * FROM read_parquet('{data}/studies.parquet')
    """),
    ("v_entities", """
        SELECT * FROM read_parquet('{data}/entities.parquet')
    """),
    ("v_technologies", """
        SELECT * FROM read_parquet('{data}/technologies.parquet')
    """),
    ("v_observations", """
        SELECT * FROM read_parquet('{data}/observations.parquet')
    """),
    ("v_known_entities", """
        SELECT * FROM read_parquet('{data}/known_entities.parquet')
    """),
    ("v_known_technologies", """
        SELECT * FROM read_parquet('{data}/known_technologies.parquet')
    """),
    ("v_collection_stats", """
        SELECT * FROM read_parquet('{data}/collection_stats.parquet')
    """),
    ("v_prescience_raw", """
        SELECT * FROM read_parquet('{data}/prescience_scores.parquet')
    """),
    # ---------- v1.5 prescience views ----------
    ("v_studies_with_prescience", """
        SELECT
            s.*,
            ROUND(CAST(s.prescience_mean AS DOUBLE), 2) AS prescience_mean_round
        FROM v_studies s
        WHERE s.has_prescience = TRUE
    """),
    ("v_top_prescient_studies", """
        SELECT * FROM v_studies_with_prescience
        WHERE prescience_max = 5
        ORDER BY prescience_mean DESC NULLS LAST, prescience_obs_count DESC
    """),
    ("v_prescience_by_decade", """
        SELECT
            CAST(CAST(pub_year AS INTEGER) / 10 * 10 AS VARCHAR) || 's' AS decade,
            COUNT(*) FILTER (WHERE prescience_max >= 4) AS high_prescience_studies,
            COUNT(*) FILTER (WHERE prescience_max IS NOT NULL) AS studies_scored
        FROM v_studies
        WHERE pub_year IS NOT NULL AND pub_year != '' AND pub_year != 'unknown'
        GROUP BY decade
        ORDER BY decade
    """),
    ("v_observations_with_prescience", """
        SELECT * FROM v_observations
        WHERE prescience_score IS NOT NULL
    """),
    ("v_low_confidence_prescience", """
        SELECT obs_id, study_id, prescience_score, prescience_confidence,
               prescience_rationale
        FROM v_observations
        WHERE prescience_confidence = 1
        ORDER BY study_id, obs_id
    """),
    # ---------- v1.4 carryovers expressed against v1.5 data ----------
    ("v_studies_with_high_prescience", """
        SELECT * FROM v_studies WHERE prescience_max >= 4
    """),
    ("v_studies_by_decade", """
        SELECT
            CAST(CAST(pub_year AS INTEGER) / 10 * 10 AS VARCHAR) || 's' AS decade,
            COUNT(*) AS studies
        FROM v_studies
        WHERE pub_year IS NOT NULL AND pub_year != '' AND pub_year != 'unknown'
        GROUP BY decade
        ORDER BY decade
    """),
    ("v_entities_with_observation_count", """
        SELECT entity_id, canonical_name,
               CAST(occurrence_count AS INTEGER) AS occurrence_count
        FROM v_entities
        ORDER BY occurrence_count DESC NULLS LAST
    """),
    ("v_technologies_by_lifecycle", """
        SELECT tech_id, canonical_name,
               CAST(occurrence_count AS INTEGER) AS occurrence_count
        FROM v_technologies
        ORDER BY occurrence_count DESC NULLS LAST
    """),
    ("v_observations_by_year", """
        SELECT s.pub_year, COUNT(*) AS obs_count
        FROM v_observations o
        JOIN v_studies s ON s.study_id = o.study_id
        WHERE s.pub_year IS NOT NULL AND s.pub_year != ''
        GROUP BY s.pub_year
        ORDER BY s.pub_year
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

    # ---- Promote staging → data/ with canonical names ----
    rename_map = {
        "_master_studies.parquet":              "studies.parquet",
        "_master_entities.parquet":             "entities.parquet",
        "_master_technologies.parquet":         "technologies.parquet",
        "_master_observations.parquet":         "observations.parquet",
        "_known_entities.parquet":              "known_entities.parquet",
        "_known_technologies.parquet":          "known_technologies.parquet",
        "_collection_stats.parquet":            "collection_stats.parquet",
        "_master_prescience_scores.parquet":    "prescience_scores.parquet",
    }
    for src_name, dst_name in rename_map.items():
        src = staging / src_name
        if not src.exists():
            sys.exit(f"HALT: missing staging file {src}")
        shutil.copy2(src, data / dst_name)
        print(f"  [promote] {src_name} → data/{dst_name}")

    # ---- Build DuckDB ----
    db_path = db_dir / "kastner.duckdb"
    if db_path.exists():
        db_path.unlink()  # full rebuild

    con = duckdb.connect(str(db_path))
    rowcounts: dict[str, int] = {}
    for view_name, sql in VIEW_SQL:
        formatted = sql.format(data=str(data))
        try:
            con.execute(f"CREATE OR REPLACE VIEW {view_name} AS {formatted}")
            n = con.execute(f"SELECT COUNT(*) FROM {view_name}").fetchone()[0]
            rowcounts[view_name] = n
            print(f"  [view]    {view_name:<40s}  rows={n}")
        except Exception as e:
            sys.exit(f"HALT: view {view_name} failed: {e}")

    con.close()

    # ---- Append to manifest ----
    manifest_path = wiki / "build_manifest.json"
    with open(manifest_path) as f:
        manifest = json.load(f)
    manifest["phase_2"] = {
        "phase": 2,
        "phase_name": "build_data_layer",
        "ran_at": datetime.now(timezone.utc).isoformat(),
        "duckdb_path": str(db_path.relative_to(wiki)),
        "view_rowcounts": rowcounts,
    }
    tmp = manifest_path.with_suffix(".json.tmp")
    with open(tmp, "w") as f:
        json.dump(manifest, f, indent=2, sort_keys=True, default=str)
    os.replace(tmp, manifest_path)

    print(f"\nPhase 2 complete. DuckDB: {db_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
