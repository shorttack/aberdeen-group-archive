#!/usr/bin/env python3
"""
survey_mac_state_v1.py

Read-only survey of the Mac archive state. Confirms:
  1. Where the pipeline phase scripts live + their mtimes
  2. Which masters were touched by the CompChem promote (backup files present?)
  3. Live DuckDB view shape (post Phase 1+2 from earlier today)
  4. Wiki directory state — does CompChem already have any pages? When was last Phase 3 run?
  5. Embeddings parquet age + row count (proxy for last Phase 5 run)
  6. Scaffolding doc ages (proxy for last Phase 6 run)
  7. Git status of both repos (any uncommitted Mac-side work?)

Read-only. No writes, no rebuilds, no API calls.
"""
import os, subprocess, csv, datetime, sys
from pathlib import Path

ARCHIVE_MASTERS = Path.home() / "Desktop/Archive/aberdeen-group-archive"
WIKI_REPO       = Path.home() / "Repos/kastner-aberdeen-wiki"
ARCHIVE_REPO    = Path.home() / "Desktop/Archive/aberdeen-group-archive"
SCRIPTS_DIR     = Path.home() / "Desktop/Archive/scripts"
LOGS_DIR        = Path.home() / "Desktop/Archive/logs"

COMPCHEM_STUDY_ID = "conflicting-trends-computational-chemistry-fe5c31"

def section(title):
    print()
    print("=" * 70)
    print(f"  {title}")
    print("=" * 70)

def ts(epoch):
    return datetime.datetime.fromtimestamp(epoch).strftime("%Y-%m-%d %H:%M:%S")

def age_human(epoch):
    delta = datetime.datetime.now().timestamp() - epoch
    if delta < 60:        return f"{int(delta)}s ago"
    if delta < 3600:      return f"{int(delta/60)}m ago"
    if delta < 86400:     return f"{int(delta/3600)}h ago"
    return f"{int(delta/86400)}d ago"

def file_info(p):
    if not p.exists():
        return f"  [MISSING] {p}"
    st = p.stat()
    return f"  {p}\n    size={st.st_size:>12,}  mtime={ts(st.st_mtime)}  ({age_human(st.st_mtime)})"

def run(cmd, cwd=None):
    """Run a command, return (stdout, stderr, returncode)."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True,
                                cwd=cwd, timeout=30)
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except Exception as e:
        return "", str(e), -1

# -----------------------------------------------------------------
section("1. Pipeline phase scripts")
# -----------------------------------------------------------------
BUILD_DIR = SCRIPTS_DIR / "build"
expected = [
    "01_load_csvs_v2.py",
    "02_build_data_layer_v4.py",
    "03_generate_vault_v2.py",
    "04_generate_indices_v2.py",
    "05_compute_embeddings_v3.py",
    "06_emit_scaffolding_v1.py",
]
print(f"Looking in: {BUILD_DIR}")
print()
for script in expected:
    p = BUILD_DIR / script
    print(file_info(p))

# -----------------------------------------------------------------
section("2. CompChem promote — backup files present?")
# -----------------------------------------------------------------
backups = sorted(ARCHIVE_MASTERS.glob("*.bak_promote_compchem_*"))
if not backups:
    print("  NONE FOUND — promote may not have run, or backups were cleaned.")
else:
    print(f"  Found {len(backups)} backups:")
    for b in backups:
        print(f"    {b.name}  ({ts(b.stat().st_mtime)})")

print()
collisions = ARCHIVE_MASTERS / "promote_compchem_v1_collisions.txt"
print("Collisions sidecar:")
print(file_info(collisions))

# -----------------------------------------------------------------
section("3. Master CSV row counts (truth)")
# -----------------------------------------------------------------
masters = [
    "_master_studies.csv",
    "_master_entities.csv",
    "_master_technologies.csv",
    "_master_observations.csv",
    "_master_codes.csv",
    "_master_entity_studies.csv",
    "_master_tech_studies.csv",
]
for m in masters:
    p = ARCHIVE_MASTERS / m
    if not p.exists():
        print(f"  [MISSING] {p}")
        continue
    n = sum(1 for _ in open(p, encoding="utf-8")) - 1  # minus header
    print(f"  {m:<35} {n:>7,} rows   mtime={ts(p.stat().st_mtime)}")

# -----------------------------------------------------------------
section("4. CompChem study presence in masters (spot check)")
# -----------------------------------------------------------------
studies_csv = ARCHIVE_MASTERS / "_master_studies.csv"
if studies_csv.exists():
    found = False
    with open(studies_csv, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("study_id") == COMPCHEM_STUDY_ID:
                found = True
                print(f"  ✓ Found CompChem in _master_studies.csv:")
                print(f"    study_id:  {row['study_id']}")
                print(f"    title:     {row.get('title','')[:80]}")
                print(f"    author:    {row.get('author','')}")
                print(f"    date:      {row.get('date','')}")
                print(f"    type:      {row.get('type','')}")
                print(f"    prescience: {row.get('prescience','')}")
                break
    if not found:
        print(f"  ✗ CompChem study_id NOT found in masters — promote may have failed.")

obs_csv = ARCHIVE_MASTERS / "_master_observations.csv"
if obs_csv.exists():
    n_compchem_obs = 0
    with open(obs_csv, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("study_id") == COMPCHEM_STUDY_ID:
                n_compchem_obs += 1
    print(f"  CompChem observations in master: {n_compchem_obs} (expect 64)")

# -----------------------------------------------------------------
section("5. Live DuckDB view shape")
# -----------------------------------------------------------------
db_path = WIKI_REPO / "db/kastner.duckdb"
print(file_info(db_path))
print()
if db_path.exists():
    query = """
    SELECT
      (SELECT COUNT(*) FROM v_studies) AS studies,
      (SELECT COUNT(*) FROM v_observations) AS observations,
      (SELECT COUNT(*) FROM v_entities) AS entities,
      (SELECT COUNT(*) FROM v_technologies) AS technologies,
      (SELECT COUNT(*) FROM v_studies_with_high_prescience) AS high_prescience
    """
    out, err, _ = run(f'duckdb {db_path} -csv -c "{query}"')
    if out:
        print("  Shape (live DuckDB views):")
        for line in out.splitlines():
            print(f"    {line}")
    if err:
        print(f"  stderr: {err}")

    # CompChem check via view
    print()
    print("  CompChem study visible in v_studies?")
    q2 = f"SELECT study_id, title, pub_year, study_prescience_enum FROM v_studies WHERE study_id = '{COMPCHEM_STUDY_ID}';"
    out2, err2, _ = run(f'duckdb {db_path} -csv -c "{q2}"')
    if out2:
        for line in out2.splitlines():
            print(f"    {line}")

# -----------------------------------------------------------------
section("6. Wiki vault — does CompChem already have a study page?")
# -----------------------------------------------------------------
wiki_dir = WIKI_REPO / "wiki"
print(f"Wiki root: {wiki_dir}")
study_md = wiki_dir / "studies" / f"{COMPCHEM_STUDY_ID}.md"
print(file_info(study_md))

# Newest + oldest study page mtime (proxy for Phase 3 run cadence)
studies_pages = list((wiki_dir / "studies").glob("*.md")) if (wiki_dir/"studies").exists() else []
if studies_pages:
    mtimes = [(p.stat().st_mtime, p.name) for p in studies_pages]
    mtimes.sort()
    oldest = mtimes[0]
    newest = mtimes[-1]
    print(f"  Total study pages: {len(studies_pages)}")
    print(f"  Oldest: {oldest[1]}  {ts(oldest[0])}  ({age_human(oldest[0])})")
    print(f"  Newest: {newest[1]}  {ts(newest[0])}  ({age_human(newest[0])})")

# -----------------------------------------------------------------
section("7. Phase 5 — embeddings parquet")
# -----------------------------------------------------------------
emb = WIKI_REPO / "embeddings.parquet"
if not emb.exists():
    emb = WIKI_REPO / "data" / "embeddings.parquet"
print(file_info(emb))
if emb.exists():
    out, err, _ = run(f'duckdb -csv -c "SELECT COUNT(*) FROM read_parquet(\'{emb}\');"')
    if out:
        print(f"  Row count: {out.splitlines()[-1]}")

# -----------------------------------------------------------------
section("8. Phase 6 — scaffolding doc ages")
# -----------------------------------------------------------------
for doc in ["README.md", "AGENTS.md", "chat-starter.md"]:
    print(file_info(WIKI_REPO / doc))

# -----------------------------------------------------------------
section("9. Git status — uncommitted Mac-side work")
# -----------------------------------------------------------------
for repo_name, repo_path in [
    ("aberdeen-group-archive", ARCHIVE_REPO),
    ("kastner-aberdeen-wiki",  WIKI_REPO),
]:
    print(f"\n  Repo: {repo_name} ({repo_path})")
    if not repo_path.exists():
        print(f"    [MISSING repo dir]")
        continue
    out, err, _ = run("git status --porcelain", cwd=repo_path)
    if not out:
        print("    clean working tree")
    else:
        # Count lines, show first 10
        lines = out.splitlines()
        print(f"    {len(lines)} uncommitted changes (showing first 10):")
        for line in lines[:10]:
            print(f"      {line}")

    out, err, _ = run("git log -1 --format='%h %ci %s'", cwd=repo_path)
    if out:
        print(f"    HEAD: {out}")

# -----------------------------------------------------------------
section("10. Phase 3 log presence (proxy for last unattended run)")
# -----------------------------------------------------------------
if LOGS_DIR.exists():
    p3_logs = sorted(LOGS_DIR.glob("phase3_*.log"), key=lambda p: p.stat().st_mtime)
    if p3_logs:
        print(f"  Phase 3 logs in {LOGS_DIR}:")
        for log in p3_logs[-5:]:
            print(f"    {log.name}  ({ts(log.stat().st_mtime)})")
    else:
        print(f"  No phase3_*.log found in {LOGS_DIR}")
else:
    print(f"  {LOGS_DIR} does not exist yet")

print()
print("=" * 70)
print("  Survey complete.")
print("=" * 70)
