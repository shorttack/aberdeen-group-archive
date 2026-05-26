#!/usr/bin/env python3
"""
01_load_csvs_v2.py — Phase 1: Load + validate master CSVs (v1.5)

v2 corrections vs v1:
  - Use ACTUAL column names from frozen schema (references/csv-schema-actual-v1.md):
    * entities/techs use `entity_name`/`tech_name`, NOT `canonical_name`
    * studies have no `pub_year` — derived from `date` (ISO YYYY-MM-DD)
    * no `occurrence_count` column — derived from join tables
    * collection_stats is per-study, not per-collection — aggregated here
  - Load 11 masters total (was 8):
    * + _master_entity_studies.csv (join)
    * + _master_tech_studies.csv  (join)
    * + _master_codes.csv         (dictionary, NEW v1.5 surface)
  - Materialize derived columns and emit them in staging parquet

Usage:
  python3 01_load_csvs_v2.py \\
      --archive ~/Desktop/Archive/archive_masters \\
      --wiki    ~/Desktop/kastner_wiki
"""
from __future__ import annotations
import argparse
import csv
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    sys.exit("ERROR: pandas required. pip3 install pandas pyarrow")

QUOTE_ALL = csv.QUOTE_ALL

# (filename, halt_threshold, required_cols)
MASTER_SCHEMAS = {
    "_master_studies.csv": (
        500,
        ["study_id", "title", "author", "date", "type", "subject_domain",
         "importance", "relevance", "prescience"],
    ),
    "_master_entities.csv": (
        2000,
        ["entity_id", "entity_name", "entity_type"],
    ),
    "_master_technologies.csv": (
        3000,
        ["tech_id", "tech_name", "category"],
    ),
    "_master_observations.csv": (
        20000,
        ["obs_id", "study_id", "observation_type", "year_observed",
         "metric_name", "metric_value", "confidence"],
    ),
    "_master_prescience_scores.csv": (
        1000,
        ["obs_id", "study_id", "model", "prescience_score",
         "confidence", "rationale", "scorer_version", "source_pass"],
    ),
    "_known_entities.csv": (
        50,
        ["entity_id", "entity_name"],
    ),
    "_known_technologies.csv": (
        50,
        ["tech_id", "tech_name"],
    ),
    "_collection_stats.csv": (
        3,
        ["collection", "study_id", "n_observations"],
    ),
    "_master_codes.csv": (
        100,
        ["code_id", "code_type", "label", "definition"],
    ),
    "_master_entity_studies.csv": (
        500,
        ["entity_id", "study_id"],
    ),
    "_master_tech_studies.csv": (
        500,
        ["tech_id", "study_id"],
    ),
}


def atomic_write_json(path: Path, obj: dict) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True, default=str)
    os.replace(tmp, path)


def load_master(archive: Path, filename: str, halt: int,
                required_cols: list[str]) -> tuple[pd.DataFrame, dict]:
    path = archive / filename
    if not path.exists():
        sys.exit(f"HALT: missing required master CSV: {path}")
    df = pd.read_csv(path, dtype=str, keep_default_na=False, na_values=[""])
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        sys.exit(f"HALT: {filename} missing required columns: {missing}\n"
                 f"  Actual columns: {list(df.columns)}")
    n = len(df)
    if n < halt:
        sys.exit(f"HALT: {filename} has {n} rows (< {halt})")
    return df, {"file": filename, "rows": n, "cols": len(df.columns)}


def derive_pub_year(date_str: str) -> int | None:
    if not date_str or pd.isna(date_str):
        return None
    s = str(date_str).strip()
    if len(s) >= 4 and s[:4].isdigit():
        try:
            return int(s[:4])
        except ValueError:
            return None
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive", required=True,
                    help="Path to archive_masters/ directory")
    ap.add_argument("--wiki", required=True,
                    help="Wiki output directory")
    args = ap.parse_args()

    archive = Path(args.archive).resolve()
    wiki = Path(args.wiki).resolve()
    print(f"Archive masters dir: {archive}")
    print(f"Wiki output dir:     {wiki}")

    staging = wiki / "data" / "_validated"
    staging.mkdir(parents=True, exist_ok=True)

    summaries: dict[str, dict] = {}
    frames: dict[str, pd.DataFrame] = {}

    for fname, (halt, cols) in MASTER_SCHEMAS.items():
        df, summ = load_master(archive, fname, halt, cols)
        frames[fname] = df
        summaries[fname] = summ
        print(f"  loaded {fname}: {summ['rows']} rows, {summ['cols']} cols")

    studies = frames["_master_studies.csv"].copy()
    entities = frames["_master_entities.csv"].copy()
    techs = frames["_master_technologies.csv"].copy()
    obs = frames["_master_observations.csv"].copy()
    presc = frames["_master_prescience_scores.csv"].copy()
    known_e = frames["_known_entities.csv"].copy()
    known_t = frames["_known_technologies.csv"].copy()
    coll = frames["_collection_stats.csv"].copy()
    codes = frames["_master_codes.csv"].copy()
    e_studies = frames["_master_entity_studies.csv"].copy()
    t_studies = frames["_master_tech_studies.csv"].copy()

    # ---- Derive studies.pub_year from studies.date ----
    studies["pub_year"] = studies["date"].apply(derive_pub_year)
    n_no_year = int(studies["pub_year"].isna().sum())
    print(f"  derived pub_year — {len(studies) - n_no_year}/{len(studies)} "
          f"resolved; {n_no_year} missing")

    # Rename study-level prescience enum so it doesn't collide with obs-level
    studies = studies.rename(columns={
        "prescience": "study_prescience_enum",
        "prescience_rationale": "study_prescience_rationale",
    })

    # ---- Derive occurrence_count for entities ----
    e_occ = (e_studies.groupby("entity_id", as_index=False)
             .agg(occurrence_count=("study_id", "nunique")))
    entities = entities.merge(e_occ, on="entity_id", how="left")
    entities["occurrence_count"] = entities["occurrence_count"].fillna(0).astype(int)
    print(f"  derived entities.occurrence_count — top1={entities['occurrence_count'].max()}, "
          f"median={int(entities['occurrence_count'].median())}, "
          f"zero={(entities['occurrence_count']==0).sum()}")

    # ---- Derive occurrence_count for technologies ----
    t_occ = (t_studies.groupby("tech_id", as_index=False)
             .agg(occurrence_count=("study_id", "nunique")))
    techs = techs.merge(t_occ, on="tech_id", how="left")
    techs["occurrence_count"] = techs["occurrence_count"].fillna(0).astype(int)
    print(f"  derived techs.occurrence_count — top1={techs['occurrence_count'].max()}, "
          f"median={int(techs['occurrence_count'].median())}, "
          f"zero={(techs['occurrence_count']==0).sum()}")

    # ---- Join prescience scores onto observations ----
    psc = presc[["obs_id", "prescience_score", "confidence", "rationale",
                 "scorer_version", "source_pass"]].rename(columns={
        "confidence": "prescience_confidence",
        "rationale": "prescience_rationale",
    })
    # Coerce score and confidence to numeric
    psc["prescience_score"] = pd.to_numeric(psc["prescience_score"], errors="coerce")
    psc["prescience_confidence"] = pd.to_numeric(psc["prescience_confidence"], errors="coerce")
    obs = obs.merge(psc, on="obs_id", how="left")
    n_scored = int(obs["prescience_score"].notna().sum())
    print(f"  joined prescience to observations — {n_scored}/{len(obs)} obs scored")

    # ---- Aggregate obs-level prescience back up to study-level ----
    study_psc = (obs.dropna(subset=["prescience_score"])
                    .groupby("study_id", as_index=False)
                    .agg(prescience_max=("prescience_score", "max"),
                         prescience_mean=("prescience_score", "mean"),
                         prescience_obs_count=("prescience_score", "size")))
    studies = studies.merge(study_psc, on="study_id", how="left")
    studies["prescience_obs_count"] = studies["prescience_obs_count"].fillna(0).astype(int)
    n_studies_scored = int((studies["prescience_obs_count"] > 0).sum())
    print(f"  rolled up obs prescience to studies — "
          f"{n_studies_scored}/{len(studies)} studies have ≥1 scored obs")

    # ---- Aggregate collection_stats to per-collection ----
    coll["n_entities"] = pd.to_numeric(coll["n_entities"], errors="coerce").fillna(0)
    coll["n_technologies"] = pd.to_numeric(coll["n_technologies"], errors="coerce").fillna(0)
    coll["n_observations"] = pd.to_numeric(coll["n_observations"], errors="coerce").fillna(0)
    coll["n_codes"] = pd.to_numeric(coll.get("n_codes", 0), errors="coerce").fillna(0)
    coll_agg = (coll.groupby("collection", as_index=False)
                .agg(study_count=("study_id", "nunique"),
                     n_entities_sum=("n_entities", "sum"),
                     n_technologies_sum=("n_technologies", "sum"),
                     n_observations_sum=("n_observations", "sum"),
                     n_codes_sum=("n_codes", "sum")))
    print(f"  aggregated collection_stats — {len(coll_agg)} unique collections")

    # ---- Write staging parquet ----
    out_specs = [
        ("studies", studies),
        ("entities", entities),
        ("technologies", techs),
        ("observations", obs),
        ("prescience_scores", presc),
        ("known_entities", known_e),
        ("known_technologies", known_t),
        ("collection_stats", coll),
        ("collection_stats_agg", coll_agg),
        ("codes", codes),
        ("entity_studies", e_studies),
        ("tech_studies", t_studies),
    ]
    parquet_written = []
    for name, df in out_specs:
        out = staging / f"{name}.parquet"
        df.to_parquet(out, index=False)
        parquet_written.append({"name": name, "rows": len(df),
                                 "cols": len(df.columns)})
        print(f"  wrote {out.name}: {len(df)} rows")

    # ---- Build manifest ----
    manifest_path = wiki / "build_manifest.json"
    manifest = {}
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
    manifest["phase_1"] = {
        "phase": 1,
        "phase_name": "load_csvs",
        "version": "v2",
        "ran_at": datetime.now(timezone.utc).isoformat(),
        "archive_masters": str(archive),
        "wiki": str(wiki),
        "masters_loaded": summaries,
        "derived": {
            "studies_with_pub_year": int(studies["pub_year"].notna().sum()),
            "studies_with_prescience_obs": int((studies["prescience_obs_count"] > 0).sum()),
            "obs_with_prescience_score": int(obs["prescience_score"].notna().sum()),
            "entities_with_occurrences": int((entities["occurrence_count"] > 0).sum()),
            "techs_with_occurrences": int((techs["occurrence_count"] > 0).sum()),
            "collections_aggregated": len(coll_agg),
        },
        "parquet_written": parquet_written,
    }
    atomic_write_json(manifest_path, manifest)
    print(f"\n✓ Phase 1 complete. Manifest: {manifest_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
