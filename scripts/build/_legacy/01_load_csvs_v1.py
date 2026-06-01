#!/usr/bin/env python3
"""
01_load_csvs_v1.py — Phase 1: Load + validate master CSVs (v1.5)

Reads all 8 master CSVs (the v1.4 seven + new _master_prescience_scores.csv),
validates row counts and required columns, dedupes obvious row-collisions,
and writes a Phase 1 summary into the wiki repo's build_manifest.json.

v1.5 delta vs v1: adds _master_prescience_scores.csv as required input.
Prescience scores joined to observations.csv on obs_id, then aggregated up
to study_id (max + mean) for the studies dataframe.

Usage:
  python3 01_load_csvs_v1.py \\
      --archive ~/Desktop/Archive/aberdeen-group-archive \\
      --wiki    ~/Desktop/kastner_wiki

Outputs:
  {wiki}/build_manifest.json — appends "phase_1" key with counts
  {wiki}/data/_validated/*.parquet (eight files; staging for Phase 2)

Forever-archive: §16.5 csv.QUOTE_ALL on any rewrite; atomic .tmp + os.replace.
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

# (filename, min_rows, halt_threshold, required_cols)
MASTER_SCHEMAS = {
    "_master_studies.csv": (
        900, 500,
        ["study_id", "title", "type", "pub_year", "source_file"],
    ),
    "_master_entities.csv": (
        3000, 2000,
        ["entity_id", "canonical_name", "occurrence_count"],
    ),
    "_master_technologies.csv": (
        4000, 3000,
        ["tech_id", "canonical_name", "occurrence_count"],
    ),
    "_master_observations.csv": (
        25000, 20000,
        ["obs_id", "study_id", "metric_value"],
    ),
    "_known_entities.csv": (
        100, 50,
        ["entity_id", "canonical_name"],
    ),
    "_known_technologies.csv": (
        100, 50,
        ["tech_id", "canonical_name"],
    ),
    "_collection_stats.csv": (
        5, 3,
        ["collection", "study_count"],
    ),
    # v1.5 new master
    "_master_prescience_scores.csv": (
        2000, 1000,
        ["obs_id", "study_id", "model", "prescience_score",
         "confidence", "rationale", "scorer_version", "source_pass"],
    ),
}


def atomic_write_json(path: Path, obj: dict) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True, default=str)
    os.replace(tmp, path)


def validate_csv(path: Path, min_rows: int, halt: int,
                 required_cols: list[str]) -> tuple[pd.DataFrame, dict]:
    if not path.exists():
        sys.exit(f"HALT: missing required master CSV: {path}")

    df = pd.read_csv(path, dtype=str, keep_default_na=False)
    n = len(df)
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        sys.exit(f"HALT: {path.name} missing required columns: {missing}")
    if n < halt:
        sys.exit(f"HALT: {path.name} has {n} rows < halt threshold {halt}")
    warn = n < min_rows
    return df, {
        "file": path.name, "rows": n, "cols": len(df.columns),
        "warning_below_expected": warn,
        "warning_threshold": min_rows,
    }


def dedupe_by(df: pd.DataFrame, key: str, name: str) -> tuple[pd.DataFrame, int]:
    before = len(df)
    df2 = df.drop_duplicates(subset=[key], keep="first").reset_index(drop=True)
    dropped = before - len(df2)
    if dropped:
        print(f"  [dedup] {name}: dropped {dropped} duplicate {key} rows")
    return df2, dropped


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive", required=True,
                    help="aberdeen-group-archive checkout root")
    ap.add_argument("--wiki", required=True,
                    help="kastner_wiki output dir (created if missing)")
    args = ap.parse_args()

    archive = Path(args.archive).resolve()
    wiki = Path(args.wiki).resolve()
    masters_dir = archive / "archive_masters"

    if not masters_dir.exists():
        # Fallback: some checkouts have masters at root
        masters_dir = archive
    print(f"Archive masters dir: {masters_dir}")
    print(f"Wiki output dir:     {wiki}")

    wiki.mkdir(parents=True, exist_ok=True)
    staging = wiki / "data" / "_validated"
    staging.mkdir(parents=True, exist_ok=True)

    summary = {
        "phase": 1,
        "phase_name": "load_csvs",
        "ran_at": datetime.now(timezone.utc).isoformat(),
        "archive": str(archive),
        "files": [],
        "dedup_drops": {},
    }

    dfs: dict[str, pd.DataFrame] = {}
    for fname, (min_rows, halt, cols) in MASTER_SCHEMAS.items():
        df, meta = validate_csv(masters_dir / fname, min_rows, halt, cols)
        if meta["warning_below_expected"]:
            print(f"  [WARN] {fname}: {meta['rows']} rows < expected {min_rows}")
        else:
            print(f"  [ok]   {fname}: {meta['rows']} rows")
        # Dedupe primary keys per file
        dedupe_key = {
            "_master_studies.csv": "study_id",
            "_master_entities.csv": "entity_id",
            "_master_technologies.csv": "tech_id",
            "_master_observations.csv": "obs_id",
            "_known_entities.csv": "entity_id",
            "_known_technologies.csv": "tech_id",
            "_master_prescience_scores.csv": "obs_id",
        }.get(fname)
        if dedupe_key and dedupe_key in df.columns:
            df, dropped = dedupe_by(df, dedupe_key, fname)
            summary["dedup_drops"][fname] = dropped
        dfs[fname] = df
        meta["rows_after_dedup"] = len(df)
        summary["files"].append(meta)

    # ---- v1.5 prescience join + study-level aggregation ----
    obs = dfs["_master_observations.csv"]
    psc = dfs["_master_prescience_scores.csv"]
    # Coerce prescience_score numeric for aggregation
    psc["prescience_score_num"] = pd.to_numeric(
        psc["prescience_score"], errors="coerce")
    psc["confidence_num"] = pd.to_numeric(
        psc["confidence"], errors="coerce")

    # Per-study aggregate (max + mean of prescience, count of scored obs)
    study_psc = (
        psc.groupby("study_id")
           .agg(
               prescience_max=("prescience_score_num", "max"),
               prescience_mean=("prescience_score_num", "mean"),
               prescience_obs_count=("obs_id", "count"),
               confidence_mean=("confidence_num", "mean"),
           )
           .reset_index()
    )
    summary["prescience_study_coverage"] = len(study_psc)
    summary["prescience_obs_coverage"] = len(psc)

    studies = dfs["_master_studies.csv"].merge(
        study_psc, on="study_id", how="left")
    studies["has_prescience"] = studies["prescience_obs_count"].notna()
    print(f"  [join] studies with prescience: "
          f"{studies['has_prescience'].sum()}/{len(studies)}")

    dfs["_master_studies.csv"] = studies

    # Also bind per-obs prescience back to observations for downstream pages
    obs_with_psc = obs.merge(
        psc[["obs_id", "prescience_score_num", "confidence_num",
             "rationale", "scorer_version", "source_pass"]],
        on="obs_id", how="left",
    )
    obs_with_psc.rename(columns={
        "prescience_score_num": "prescience_score",
        "confidence_num": "prescience_confidence",
        "rationale": "prescience_rationale",
    }, inplace=True)
    dfs["_master_observations.csv"] = obs_with_psc

    # ---- Write staging Parquet ----
    for fname, df in dfs.items():
        # Drop helper cols before writing the prescience file itself
        out_name = fname.replace(".csv", ".parquet")
        out_path = staging / out_name
        df.to_parquet(out_path, index=False)
        print(f"  [write] {out_name} — {len(df)} rows")

    # ---- Append to build_manifest.json ----
    manifest_path = wiki / "build_manifest.json"
    if manifest_path.exists():
        with open(manifest_path) as f:
            manifest = json.load(f)
    else:
        manifest = {"build_started_at": summary["ran_at"],
                    "builder_version": "v1.5"}
    manifest["phase_1"] = summary
    atomic_write_json(manifest_path, manifest)

    print(f"\nPhase 1 complete. Staging: {staging}")
    print(f"Build manifest: {manifest_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
