#!/usr/bin/env python3
"""
reembed_single_page_v1.py

Surgical re-embedding of a single wiki page into data/embeddings.parquet,
without re-running the full Phase 5 across all ~10,400 pages.

Use case:
  - A wiki page on disk was updated AFTER Phase 5 read its inputs (race)
  - kw_ask retrieves the page-id but the embedding encodes stale content
  - Need to refresh just the affected row(s) of embeddings.parquet

Schema contract (per Gotcha 9, kastner-archive-pipeline skill):
  embeddings.parquet has 6 columns produced by 05_compute_embeddings_v3.py:
    page_path : varchar  e.g. "wiki/studies/study-...-v2-0cdf49.md"
    page_type : varchar  e.g. "study", "entity", "technology", "code", "theme"
    slug      : varchar  e.g. "study-2026-kastner-prescience-methodology-demo-v2-0cdf49"
    title     : varchar  parsed from YAML frontmatter
    vector    : list<float>  1024-dim bge-m3
    dim       : int      1024

Defaults:
  - dry-run unless --commit
  - bge-m3 via Ollama (matches Phase 5 v3 default)
  - atomic write: tmpfile + rename
  - row-parity check: total row count must be unchanged (delta = 0)

Usage:
  python3 reembed_single_page_v1.py <slug>            # dry-run
  python3 reembed_single_page_v1.py <slug> --commit   # write

Example:
  python3 reembed_single_page_v1.py study-2026-kastner-prescience-methodology-demo-v2-0cdf49 --commit
"""
import sys, json, shutil, datetime, subprocess
from pathlib import Path

WIKI = Path.home() / "Repos/kastner-aberdeen-wiki"
WIKI_DIR = WIKI / "wiki"
EMB_PARQUET = WIKI / "data/embeddings.parquet"

OLLAMA_MODEL = "bge-m3"
EXPECTED_DIM = 1024

def usage():
    print(__doc__, file=sys.stderr)
    sys.exit(2)

if len(sys.argv) < 2:
    usage()

slug_arg = sys.argv[1]
commit = "--commit" in sys.argv

# 1. locate the on-disk file
import glob
matches = []
for pt in ("studies", "entities", "technologies", "codes", "themes", "decades", "collections", "notes"):
    p = WIKI_DIR / pt / f"{slug_arg}.md"
    if p.exists():
        matches.append((pt, p))

# also try without leading page-type prefix
if not matches:
    for pt in ("studies", "entities", "technologies", "codes", "themes", "decades", "collections", "notes"):
        for p in (WIKI_DIR / pt).glob(f"*{slug_arg}*.md"):
            matches.append((pt, p))

if not matches:
    sys.exit(f"ERROR: no on-disk file found for slug '{slug_arg}'")
if len(matches) > 1:
    print("Multiple matches:")
    for pt, p in matches: print(f"  {pt}/{p.name}")
    sys.exit("ERROR: slug ambiguous; refine.")

page_type_dir, page_path_abs = matches[0]
page_path_rel = str(page_path_abs.relative_to(WIKI))

# 2. read the page; parse frontmatter for title; build embedding input
content_full = page_path_abs.read_text(encoding="utf-8")

def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    fm_raw = text[4:end]
    body = text[end+5:]
    fm = {}
    for line in fm_raw.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body

fm, body = parse_frontmatter(content_full)
title = fm.get("title", slug_arg)
page_type = fm.get("page_type", page_type_dir.rstrip("s"))  # studies -> study

# Phase 5 v3 embeds the FULL page text (frontmatter + body). Match that.
embed_input = content_full

print(f"Page:      {page_path_rel}")
print(f"Slug:      {slug_arg}")
print(f"page_type: {page_type}")
print(f"Title:     {title}")
print(f"Mtime:     {datetime.datetime.fromtimestamp(page_path_abs.stat().st_mtime).isoformat()}")
print(f"Bytes:     {len(content_full)}")
print(f"Mode:      {'COMMIT' if commit else 'DRY-RUN'}")

# 3. read existing parquet, verify schema and locate target row(s)
import duckdb
con = duckdb.connect(":memory:")
schema = con.execute(f"DESCRIBE SELECT * FROM read_parquet('{EMB_PARQUET}')").fetchall()
schema_cols = [c[0] for c in schema]
EXPECTED_COLS = ["page_path", "page_type", "slug", "title", "vector", "dim"]
if schema_cols != EXPECTED_COLS:
    sys.exit(f"SCHEMA MISMATCH\n  expected: {EXPECTED_COLS}\n  actual:   {schema_cols}")
print(f"Schema:    OK ({len(schema_cols)} cols, matches Phase 5 v3 contract)")

before = con.execute(f"SELECT COUNT(*) FROM read_parquet('{EMB_PARQUET}')").fetchone()[0]
hits = con.execute(
    f"SELECT page_path, page_type, slug, title, dim FROM read_parquet('{EMB_PARQUET}') WHERE slug = ?",
    [slug_arg],
).fetchall()
print(f"Rows total: {before}")
print(f"Hits for slug: {len(hits)}")
for h in hits:
    print(f"  existing: page_path={h[0]}, page_type={h[1]}, dim={h[4]}")

if len(hits) == 0:
    sys.exit(f"ERROR: no existing row for slug '{slug_arg}'. Use full Phase 5 for new insertions.")
if len(hits) > 1:
    sys.exit(f"ERROR: {len(hits)} rows match slug. Refusing surgical edit; use full Phase 5.")

# 4. compute new embedding via Ollama
print("Computing embedding via Ollama bge-m3...")
r = subprocess.run(
    ["curl", "-s", "http://localhost:11434/api/embeddings",
     "-d", json.dumps({"model": OLLAMA_MODEL, "prompt": embed_input})],
    capture_output=True, text=True,
)
if r.returncode != 0:
    sys.exit(f"curl failed: {r.stderr}")
resp = json.loads(r.stdout)
if "embedding" not in resp:
    sys.exit(f"Ollama response missing 'embedding': {resp}")
vec = resp["embedding"]
if len(vec) != EXPECTED_DIM:
    sys.exit(f"DIM MISMATCH: got {len(vec)}, expected {EXPECTED_DIM}")
print(f"Embedding: {len(vec)}-dim, first 3 floats = [{vec[0]:.4f}, {vec[1]:.4f}, {vec[2]:.4f}]")

if not commit:
    print("\nDRY-RUN — pass --commit to write the new embedding into the parquet.")
    sys.exit(0)

# 5. backup
ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
bak = EMB_PARQUET.with_suffix(f".parquet.bak_reembed_{slug_arg[:40]}_{ts}")
shutil.copy2(EMB_PARQUET, bak)
print(f"Backup:    {bak}")

# 6. surgical update via DuckDB COPY (build new parquet, replace atomically)
tmp_out = EMB_PARQUET.with_suffix(".parquet.tmp_reembed")

# build the new row as a single-row table via SQL parameter
# duckdb supports list literals; build the vector list explicitly
vec_sql = "[" + ", ".join(f"{v:.10e}" for v in vec) + "]"

con.execute(f"""
COPY (
    SELECT page_path, page_type, slug, title, vector, dim
    FROM read_parquet('{EMB_PARQUET}')
    WHERE slug != ?
    UNION ALL
    SELECT
        '{page_path_rel}' AS page_path,
        '{page_type}' AS page_type,
        '{slug_arg}' AS slug,
        ? AS title,
        {vec_sql}::FLOAT[] AS vector,
        {EXPECTED_DIM} AS dim
) TO '{tmp_out}' (FORMAT PARQUET);
""", [slug_arg, title])

# verify row count parity
after = con.execute(f"SELECT COUNT(*) FROM read_parquet('{tmp_out}')").fetchone()[0]
if after != before:
    tmp_out.unlink()
    sys.exit(f"ROW COUNT PARITY FAILED: before={before}, after={after}, delta={after-before} (expected 0)")
print(f"Rows after: {after} (delta {after-before:+d}, expected +0)")

# verify the new row landed
new_hit = con.execute(
    f"SELECT page_path, page_type, slug, title, dim FROM read_parquet('{tmp_out}') WHERE slug = ?",
    [slug_arg],
).fetchall()
if len(new_hit) != 1:
    tmp_out.unlink()
    sys.exit(f"VERIFY FAILED: {len(new_hit)} rows for slug in new parquet (expected 1)")
print(f"Verify:    new row present, page_path={new_hit[0][0]}, dim={new_hit[0][4]}")

# atomic swap
tmp_out.replace(EMB_PARQUET)
print(f"Wrote:     {EMB_PARQUET}")
print("DONE.")
