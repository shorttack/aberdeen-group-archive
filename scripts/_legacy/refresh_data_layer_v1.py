#!/usr/bin/env python3
"""Surgical refresh of the wiki data layer (Parquet + DuckDB) from current archive masters.

Pass A v2 propagation:
- Adds new columns to observations.parquet: verification_method (and preserves thread_tag)
- Adds new column to studies.parquet: collection (preserved if already present)
- Picks up new studies (IBM Longitudinal, Oracle Longitudinal, Enterprise AI Arc)
- Picks up Pass A v2 prediction lifts in confidence column
- Rebuilds kastner.duckdb with the same view catalog

Does NOT touch:
- Obsidian vault (handled by separate add_new_study_stubs.py)
- embeddings.parquet (existing embeddings still valid for unchanged pages)
- build_manifest.json (updated separately)
"""
import csv, sys, json
from pathlib import Path

import duckdb
import pandas as pd

WIKI_ROOT = Path("/home/user/workspace/kastner-aberdeen-wiki")
ARCHIVE_ROOT = Path("/home/user/workspace/aberdeen-group-archive")
DATA_DIR = WIKI_ROOT / "data"
DB_PATH = WIKI_ROOT / "db" / "kastner.duckdb"

csv.field_size_limit(sys.maxsize)


def load_csv_as_dataframe(path: Path) -> pd.DataFrame:
    """Load a master CSV preserving column ordering and treating all cells as strings."""
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
    # Pad short rows / truncate long rows to the header width to guard against drift
    fixed = []
    for r in rows:
        if len(r) < len(header):
            r = r + [""] * (len(header) - len(r))
        elif len(r) > len(header):
            r = r[: len(header)]
        fixed.append(r)
    df = pd.DataFrame(fixed, columns=header)
    # Force everything to string to match prior Parquet schema (all VARCHAR)
    for c in df.columns:
        df[c] = df[c].astype("string").fillna("")
    return df


def write_parquet(df: pd.DataFrame, out_path: Path) -> int:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(out_path, index=False)
    return len(df)


def rebuild_duckdb(db_path: Path, data_dir: Path) -> dict:
    if db_path.exists():
        db_path.unlink()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    con = duckdb.connect(str(db_path))

    # Base tables from parquet
    table_files = {
        "studies": "studies.parquet",
        "entities": "entities.parquet",
        "technologies": "technologies.parquet",
        "observations": "observations.parquet",
        "known_entities": "known_entities.parquet",
        "known_technologies": "known_technologies.parquet",
        "collection_stats": "collection_stats.parquet",
    }
    counts = {}
    for table, fn in table_files.items():
        p = data_dir / fn
        if not p.exists():
            print(f"  WARN: {fn} missing; skipping table {table}")
            continue
        con.execute(
            f"CREATE TABLE {table} AS SELECT * FROM read_parquet('{p}')"
        )
        counts[table] = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]

    # Views (replay the canonical catalog)
    views = {
        "entities_with_observation_count": """
            SELECT e.entity_id, e.entity_name, e.entity_type, e.sector,
                   COUNT(DISTINCT o.study_id) AS study_count,
                   COUNT(o.obs_id) AS obs_count
            FROM known_entities e
            LEFT JOIN observations o ON o.entity_id = e.entity_id
            GROUP BY e.entity_id, e.entity_name, e.entity_type, e.sector
            ORDER BY obs_count DESC
        """,
        "technologies_with_observation_count": """
            SELECT t.tech_id, t.tech_name, t.vendor, t.category,
                   COUNT(DISTINCT o.study_id) AS study_count,
                   COUNT(o.obs_id) AS obs_count
            FROM known_technologies t
            LEFT JOIN observations o ON o.tech_id = t.tech_id
            GROUP BY t.tech_id, t.tech_name, t.vendor, t.category
            ORDER BY obs_count DESC
        """,
        "importance_summary": """
            SELECT importance, COUNT(*) AS study_count
            FROM studies GROUP BY importance ORDER BY study_count DESC
        """,
        "prescience_summary": """
            SELECT prescience, COUNT(*) AS study_count
            FROM studies GROUP BY prescience ORDER BY study_count DESC
        """,
        "kastner_authored_studies": """
            SELECT * FROM studies WHERE LOWER(author) LIKE '%kastner%'
        """,
        "observations_by_year": """
            SELECT year_observed, COUNT(*) AS obs_count
            FROM observations
            WHERE year_observed IS NOT NULL AND year_observed != ''
            GROUP BY year_observed ORDER BY year_observed
        """,
        "studies_by_decade": """
            SELECT CAST(SUBSTRING(date, 1, 3) || '0s' AS VARCHAR) AS decade,
                   COUNT(*) AS study_count
            FROM studies
            WHERE date IS NOT NULL AND date != ''
            GROUP BY decade ORDER BY decade
        """,
        "studies_with_high_prescience": """
            SELECT study_id, title, author, date, prescience, prescience_rationale, importance
            FROM studies WHERE prescience = 'high' ORDER BY date
        """,
        "top_vendors_by_mentions": """
            SELECT vendor, COUNT(*) AS tech_rows
            FROM technologies
            WHERE vendor IS NOT NULL AND vendor != ''
            GROUP BY vendor ORDER BY tech_rows DESC LIMIT 50
        """,
        "volume_1_chapters": """
            SELECT * FROM studies WHERE study_id LIKE 'volume-1-%' ORDER BY study_id
        """,
        # NEW: Pass A v2 visibility
        "verification_method_distribution": """
            SELECT verification_method, COUNT(*) AS obs_count
            FROM observations
            WHERE verification_method IS NOT NULL AND verification_method != ''
            GROUP BY verification_method ORDER BY obs_count DESC
        """,
        "viability_predictions_status": """
            SELECT confidence, COUNT(*) AS pred_count
            FROM observations
            WHERE observation_type = 'viability-prediction'
            GROUP BY confidence ORDER BY pred_count DESC
        """,
    }
    for name, sql in views.items():
        con.execute(f"CREATE VIEW {name} AS {sql}")
    con.close()
    return counts


def main():
    print("=== Phase 1: Load master CSVs from archive ===")
    masters = {
        "studies": ARCHIVE_ROOT / "_master_studies.csv",
        "entities": ARCHIVE_ROOT / "_master_entities.csv",
        "technologies": ARCHIVE_ROOT / "_master_technologies.csv",
        "observations": ARCHIVE_ROOT / "_master_observations.csv",
        "known_entities": ARCHIVE_ROOT / "_known_entities.csv",
        "known_technologies": ARCHIVE_ROOT / "_known_technologies.csv",
    }
    dfs = {}
    for k, p in masters.items():
        dfs[k] = load_csv_as_dataframe(p)
        print(f"  loaded {k}: {len(dfs[k])} rows, cols={list(dfs[k].columns)}")

    # collection_stats may not exist; if present, refresh it; otherwise carry over
    cs_csv = ARCHIVE_ROOT / "_collection_stats.csv"
    if cs_csv.exists():
        dfs["collection_stats"] = load_csv_as_dataframe(cs_csv)
        print(f"  loaded collection_stats: {len(dfs['collection_stats'])} rows")
    else:
        print("  collection_stats source CSV missing; preserving existing parquet")

    print("\n=== Phase 2: Emit Parquet files ===")
    parquet_targets = {
        "studies": DATA_DIR / "studies.parquet",
        "entities": DATA_DIR / "entities.parquet",
        "technologies": DATA_DIR / "technologies.parquet",
        "observations": DATA_DIR / "observations.parquet",
        "known_entities": DATA_DIR / "known_entities.parquet",
        "known_technologies": DATA_DIR / "known_technologies.parquet",
    }
    if "collection_stats" in dfs:
        parquet_targets["collection_stats"] = DATA_DIR / "collection_stats.parquet"

    parquet_counts = {}
    for k, out in parquet_targets.items():
        n = write_parquet(dfs[k], out)
        parquet_counts[k] = n
        print(f"  wrote {out.name}: {n} rows")

    print("\n=== Phase 3: Rebuild kastner.duckdb ===")
    db_counts = rebuild_duckdb(DB_PATH, DATA_DIR)
    print(f"  duckdb built at {DB_PATH}")
    for t, n in db_counts.items():
        print(f"    table {t}: {n} rows")

    # Spot-check key views
    print("\n=== Phase 4: View spot-checks ===")
    con = duckdb.connect(str(DB_PATH), read_only=True)
    for v in [
        "studies_with_high_prescience",
        "entities_with_observation_count",
        "technologies_with_observation_count",
        "verification_method_distribution",
        "viability_predictions_status",
        "observations_by_year",
    ]:
        n = con.execute(f"SELECT COUNT(*) FROM {v}").fetchone()[0]
        print(f"  {v}: {n} rows")
    print("\n  verification_method distribution:")
    for r in con.execute(
        "SELECT * FROM verification_method_distribution"
    ).fetchall():
        print(f"    {r[0]}: {r[1]}")
    print("\n  viability-prediction confidence distribution:")
    for r in con.execute(
        "SELECT * FROM viability_predictions_status"
    ).fetchall():
        print(f"    {r[0]}: {r[1]}")
    con.close()

    print("\nDone.")


if __name__ == "__main__":
    main()
