#!/usr/bin/env python3
"""
verify_embeddings_schema_v1.py

Standalone, read-only schema guard for the wiki's embeddings parquet.

Context (Gotcha 9, kastner-archive-pipeline skill): 05_compute_embeddings_v2.py
once shipped a 4-column schema (path, slug, embedding, dim) that silently broke
kw_ask.py, which expected the canonical 6-column contract
(page_path, page_type, slug, title, vector, dim). The break was invisible until
a live user query crashed with a raw duckdb BinderException.

This script re-checks that contract defensively, any time it's run:
  - opens data/embeddings.parquet read-only (pyarrow if available, else duckdb)
  - asserts the column list is EXACTLY the expected 6, in any order
  - exits 0 with a short OK message if the schema matches
  - exits non-zero with a readable, actionable message if it does not

Usage:
    python3 verify_embeddings_schema_v1.py [--wiki /path/to/kastner-aberdeen-wiki]

Exit codes:
    0  schema OK
    1  file not found
    2  schema mismatch (missing and/or unexpected columns)
    3  could not read the parquet with either available engine
"""

import argparse
import sys
from pathlib import Path

EXPECTED_COLUMNS = {"page_path", "page_type", "slug", "title", "vector", "dim"}


def get_columns_pyarrow(parquet_path: Path):
    import pyarrow.parquet as pq

    schema = pq.read_schema(str(parquet_path))
    return set(schema.names)


def get_columns_duckdb(parquet_path: Path):
    import duckdb

    con = duckdb.connect(database=":memory:", read_only=False)
    try:
        rows = con.execute(
            "DESCRIBE SELECT * FROM read_parquet(?)", [str(parquet_path)]
        ).fetchall()
        return {r[0] for r in rows}
    finally:
        con.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--wiki",
        default=str(Path.home() / "Repos" / "kastner-aberdeen-wiki"),
        help="Path to the wiki repo root (default: ~/Repos/kastner-aberdeen-wiki)",
    )
    parser.add_argument(
        "--parquet",
        default=None,
        help="Explicit path to embeddings.parquet (overrides --wiki-derived default)",
    )
    args = parser.parse_args()

    parquet_path = (
        Path(args.parquet)
        if args.parquet
        else Path(args.wiki) / "data" / "embeddings.parquet"
    )

    if not parquet_path.exists():
        print(f"[FAIL] embeddings parquet not found at: {parquet_path}")
        print("       Nothing to verify. Has Phase 5 (05_compute_embeddings_v3.py) run yet?")
        sys.exit(1)

    actual_columns = None
    engine_used = None
    errors = []

    try:
        actual_columns = get_columns_pyarrow(parquet_path)
        engine_used = "pyarrow"
    except Exception as e:  # pragma: no cover - fallback path
        errors.append(f"pyarrow: {e}")

    if actual_columns is None:
        try:
            actual_columns = get_columns_duckdb(parquet_path)
            engine_used = "duckdb"
        except Exception as e:  # pragma: no cover - fallback path
            errors.append(f"duckdb: {e}")

    if actual_columns is None:
        print(f"[FAIL] Could not read {parquet_path} with pyarrow or duckdb.")
        for err in errors:
            print(f"       {err}")
        sys.exit(3)

    missing = EXPECTED_COLUMNS - actual_columns
    unexpected = actual_columns - EXPECTED_COLUMNS

    if not missing and not unexpected:
        print(
            f"[OK] {parquet_path} schema matches the expected 6-column contract "
            f"(read via {engine_used}): {sorted(EXPECTED_COLUMNS)}"
        )
        sys.exit(0)

    print(f"[FAIL] Schema drift detected in {parquet_path} (read via {engine_used}).")
    print(f"       Expected columns: {sorted(EXPECTED_COLUMNS)}")
    print(f"       Actual columns:   {sorted(actual_columns)}")
    if missing:
        print(f"       MISSING: {sorted(missing)}")
    if unexpected:
        print(f"       UNEXPECTED (extra): {sorted(unexpected)}")
    print(
        "       This is the Gotcha 9 failure mode — kw_ask.py and other consumers "
        "expect (page_path, page_type, slug, title, vector, dim) exactly. "
        "Re-run Phase 5 (05_compute_embeddings_v3.py), which is known to emit the "
        "correct 6-column schema, or patch whichever producer wrote this file."
    )
    sys.exit(2)


if __name__ == "__main__":
    main()
