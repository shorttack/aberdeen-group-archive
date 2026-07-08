---
name: kastner-archive-pipeline
description: "Operating Pete Kastner's Aberdeen archive pipeline — modifying master CSVs, applying row-level backfills, rebuilding the DuckDB + parquet layer, refreshing the wiki markdown + embeddings, and running/rolling-up Pass C prescience scoring. Use when asked to add a column to a master, backfill values, correct rows, rebuild the wiki or DuckDB, regenerate parquets or wiki pages, refresh scaffolding docs, re-embed, fix archive shape numbers, run Pass C, roll up Pass C verdicts, or diagnose 'Pass C says 0 to process'. Codifies SIX-phase pipeline, shape-audit query, stale-embeddings gotcha, canonical Pass C paths. v1.7 (2026-06-13 §11v cont 5): v_studies bucket-type column is `type`, NOT `collection_type` (KW Console BinderError fix); Gotcha 12 added; archive masters live at repo root, NOT under `master_csvs/` (clarified). v1.6 retained: Phase 1 preserves authored prescience enum; v_studies exposes `study_prescience_enum`/`study_prescience_rationale`; iCloud trap obsolete since 2026-06-01."
metadata:
  author: pete-kastner
  version: '1.7'
---

# Kastner Archive Pipeline

## When to Use This Skill

Activate whenever the task involves modifying the master CSVs in Pete's Aberdeen archive and propagating those changes through to the live wiki. Specifically:

- "Add a column to `_master_studies.csv`" (or any master)
- "Backfill missing `<column>` values"
- "Correct these rows in the master"
- "Rebuild the DuckDB" / "Refresh the wiki" / "Regenerate the parquets"
- "Re-run Phase 1 + Phase 2"
- "Regenerate the wiki pages" / "Refresh the README" / "Re-embed the wiki"
- "Fix the archive shape numbers" / "`kw ask` is returning stale counts"
- Adding a generated study (memoir, methodology demo, theme overview) that needs to appear in `kw ask` results
- Anything that touches a CSV under `~/Desktop/Archive/archive_masters/`

**Do not activate for**:
- One-time ingest of new study files (use `archival-ingest` skill instead)
- A fresh full wiki build from scratch (use `kastner-wiki-builder` skill instead)
- GitHub commit operations standalone (use `kastner-github` skill — this skill defers to that one for EOD shipping)

## The Three Locations (memorize this)

The single biggest source of confusion in this archive is that **three different directories look like wikis**. Only one is the live query target.

| # | Path on Mac (`scott`) | Role | Status |
|---|---|---|---|
| 1 | `~/Desktop/Archive/archive_masters/` | **Source of truth.** The master CSVs (`_master_studies.csv`, `_master_entities.csv`, `_master_technologies.csv`, `_master_observations.csv`, etc.) | **READ + WRITE here for masters edits** |
| 2 | `~/Repos/kastner-aberdeen-wiki/` | **Live working wiki.** Contains enriched parquets in `data/` and the live DuckDB at `db/kastner.duckdb`. This is what `kw ask` queries. Migrated here from `~/Desktop/kastner_wiki/` on 2026-06-01 to escape the iCloud Desktop trap. | **READ for verification; WRITTEN BY Phase 1+2** |
| 3 | `~/Desktop/kastner_wiki/` | **DELETED 2026-06-01.** Former live wiki location. | **DO NOT USE — does not exist.** |

There is also a fourth path that appears in old runbooks:

| # | Path | Role | Status |
|---|---|---|---|
| 4 | `~/Desktop/Archive/kastner_duckdb_build/` | Temp output dir from `build_duckdb_only_v3.py` | **DO NOT use for masters-edit rebuilds.** This script does NOT derive `pub_year` and produces unenriched parquets that break the live wiki if promoted. |

**Verification rule**: when running any `duckdb` sanity check after a rebuild, the path MUST be `~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb`. Do NOT use the old `~/Desktop/kastner_wiki/` path — it was deleted on 2026-06-01 and any query against it will fail with `IO Error: Cannot open file`.

## Scripts (where they live)

Scripts on the Mac live in **`~/Desktop/Archive/scripts/`** with this layout (mirrors the archive repo at `shorttack/aberdeen-group-archive/scripts/` after the 2026-06-01 §11j cleanup):

- **`scripts/build/`** — the 6 canonical pipeline phase scripts + `_llm_helper_v1.py`. Run pipeline phases from here.
- **`scripts/build/_legacy/`** — superseded pipeline versions (do not run).
- **`scripts/`** (flat root) — canonical one-off utilities at current versions (apply_*, extract_*, migrate_*, pre_filter_*, roll_up_*, route_*, run_prescience_*, etc.).
- **`scripts/_legacy/`** — superseded one-offs (do not run).

Forever-archive principle: nothing is deleted; legacy versions are visibility-segregated only.

| Script | Phase | What it does |
|---|---|---|
| `01_load_csvs_v2.py` | Phase 1 | Reads masters from `--archive`, derives enriched columns (`pub_year`, prescience rollups, occurrence counts, joins), writes 12 parquets to `<wiki>/build_workspace/` and logs to `build_manifest.json` |
| `02_build_data_layer_v4.py` | Phase 2 | Promotes parquets from `build_workspace/` to `<wiki>/data/`, creates `<wiki>/db/kastner.duckdb` with 27 `v_*` views. **v4 (2026-05-31) fixes the v3 decade-bucket bug** — DuckDB's `/` operator on INTEGER returns DOUBLE, so v3's `(CAST(pub_year AS INTEGER) / 10) * 10 || 's'` produced `'1972.0s'` strings instead of `'1970s'`. v4 uses the integer-division operator `//`. |
| `03_generate_vault_v2.py` | Phase 3 | Writes wiki markdown pages under `<wiki>/wiki/` |
| `04_generate_indices_v2.py` | Phase 4 | Indices, Bases, Dataview queries |
| `05_compute_embeddings_v3.py` | Phase 5 | Embeds pages with **bge-m3 (1024-dim)** via Ollama. v3 (2026-05-31) emits the full `kw_ask.py`-compatible 6-column schema `(page_path, page_type, slug, title, vector, dim)`; the prior v2 emitted a 4-column schema that crashed `kw_ask` (see Gotcha 9). v2 had switched from nomic-embed-text to bge-m3; v3 keeps bge-m3 and fixes the schema contract. Default model is overridable via `--model`. |
| `06_emit_scaffolding_v1.py` | Phase 6 | AGENTS.md, chat-starter, README |
| `build_duckdb_only_v3.py` | (partial) | **AVOID for masters-edit rebuilds.** Loads tables only; does NOT derive `pub_year` or other enriched cols |

**For a typical masters-edit refresh, only Phase 1 and Phase 2 need to run** to update the DuckDB. **But Phases 3-6 are NOT optional if `kw ask` results need to reflect the change** — the wiki markdown pages, scaffolding docs (README, AGENTS.md, chat-starter.md), and the bge-m3 embedding index are downstream of Phases 1+2 and will silently report stale numbers if not refreshed. See Workflow C below for the decision tree, and Gotcha 7 for the stale-embeddings failure mode that prompted version 1.1 of this skill.

## Workflow A: Adding a column to a master CSV

Use when Pete asks "add a `<colname>` column to `_master_<table>.csv`".

### Step 1: Confirm scope

Ask if not specified:
- Which master? (`_master_studies.csv`, `_master_entities.csv`, `_master_technologies.csv`, `_master_observations.csv`)
- Column name? Column type? (`int`, `varchar`, `date` — ISO `YYYY-MM-DD` string)
- Default value? (empty string, `NULL`, `0`, a computed value, etc.)
- Source: is the column derived from existing data, populated from an external file, or hand-filled by Pete?

### Step 2: Write the column-add script

Path: `/home/user/workspace/add_<colname>_to_<table>_v1.py`

Pattern (mandatory):
```python
import csv, shutil, datetime, sys
from pathlib import Path

ARCHIVE = Path.home() / "Desktop/Archive/archive_masters"
MASTER  = ARCHIVE / "_master_<table>.csv"
COL     = "<colname>"
DEFAULT = ""  # or whatever

commit = "--commit" in sys.argv

# read
with open(MASTER, newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows   = list(reader)

if COL in header:
    sys.exit(f"Column '{COL}' already exists. Aborting.")

# backup before any write
ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
bak = MASTER.with_suffix(f".csv.bak_add_{COL}_{ts}")
shutil.copy2(MASTER, bak)
print(f"Backup: {bak}")

# add column
header.append(COL)
for r in rows:
    r.append(DEFAULT)

print(f"Mode: {'COMMIT' if commit else 'DRY-RUN'}")
print(f"Rows: {len(rows)}, cols: {len(header)-1} -> {len(header)}")

if commit:
    with open(MASTER, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)  # mandatory per §16.5
        w.writerow(header)
        w.writerows(rows)
    print(f"Wrote: {MASTER}")
else:
    print("DRY-RUN only — pass --commit to write.")
```

**Mandatory invariants** (do not skip):
- `csv.QUOTE_ALL` on every write (Excel-touched CSVs are not trusted; we own format)
- Backup before write, timestamp in UTC, suffix `.bak_<reason>_<utc-stamp>`
- Dry-run is default; `--commit` is opt-in
- Row count preserved (`len(rows)` before == after); print both
- Column count delta = +1 (print before/after)

### Step 3: Ship the script to Pete

Per `kastner-github` skill protocol:
1. Save to `/home/user/workspace/add_<colname>_to_<table>_v1.py`
2. Commit to `shorttack/aberdeen-group-archive/scripts/add_<colname>_to_<table>_v1.py` via `gh api PUT` (sandbox)
3. Tell Pete to `git pull` and `cp scripts/add_<colname>_to_<table>_v1.py ~/Desktop/Archive/scripts/`
4. Pete runs `python3 ~/Desktop/Archive/scripts/add_<colname>_to_<table>_v1.py` (dry-run) → paste output → `--commit` after agent approves

### Step 4: Rebuild the live data layer

After Pete confirms the masters edit committed, run **Phase 1 + Phase 2**:

```bash
python3 ~/Desktop/Archive/scripts/build/01_load_csvs_v2.py \
  --archive ~/Desktop/Archive/archive_masters \
  --wiki ~/Repos/kastner-aberdeen-wiki

python3 ~/Desktop/Archive/scripts/build/02_build_data_layer_v4.py \
  --wiki ~/Repos/kastner-aberdeen-wiki
```

Look for:
- Phase 1: `loaded _master_<table>.csv: N rows, M cols` — confirm `M` is +1 from previous run
- Phase 2: `[view] v_<table>: N rows` — confirm row count unchanged

### Step 5: Verify

```bash
duckdb ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb -c \
  "SELECT '<colname>' AS col, COUNT(*) AS total, COUNT(<colname>) AS non_null, \
   COUNT(*) - COUNT(<colname>) AS null_count FROM v_<table>;"
```

Sanity: `total` matches expected row count for the table, `non_null` reflects what was actually populated. If the column is meant to be filled later, `null_count` should equal `total`.

### Step 6: If the column needs Phase 1 derivation logic

If the new column is meant to be **derived** (e.g., `pub_year` from filename + date string), the column add in Step 2 is just the storage. You also need to:
1. Patch `01_load_csvs_v2.py` to compute the value during Phase 1
2. Ship the patched script via the same protocol (versioned: `01_load_csvs_v3.py`)
3. Re-run Phase 1+2

**Defer this to a separate backlog item** if the derivation logic is non-trivial — first ship the empty column, then a backfill script (Workflow B), then optionally fold the logic into Phase 1.

## Workflow C decision tree (which phases to run)

Before committing to a rebuild, decide what changed and what needs refreshing. **Always run the shape audit (below) before AND after** so the delta is visible.

| What changed | Phase 1+2 | Phase 3 (pages) | Phase 4 (indices) | Phase 5 (embed) | Phase 6 (scaffolding) |
|---|:---:|:---:|:---:|:---:|:---:|
| Added a column to a master | ✓ | — | — | — | — |
| Backfilled values in an existing column (no new rows) | ✓ | — | — | — | — |
| Backfill exposed in `kw ask` (e.g., pub_year affects decade pages) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Added rows to a master (new study, new entity, new tech) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Edited an individual wiki page by hand | — | — | — | ✓ | — |
| README / AGENTS.md / chat-starter.md show stale counts | — | — | — | — | ✓ |
| Added a generated study (memoir, methodology demo, theme overview) | — | ✓ | ✓ | ✓ | — |
| Full wiki refresh after version bump | ✓ | ✓ | ✓ | ✓ | ✓ |

**Rule of thumb**: if the answer to "would `kw ask` give a different answer after this change?" is yes, you need Phase 5 (re-embed). If the answer to "would the README count change?" is yes, you need Phase 6. If you don't know, run all six.

## Shape audit (mandatory before and after every rebuild)

The canonical archive-shape query — paste the output into every EOD decisions log entry. Any future `kw ask` answer that quotes different numbers is provably stale.

```bash
duckdb ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb -c "
SELECT 
  (SELECT COUNT(*) FROM v_studies) AS studies,
  (SELECT COUNT(*) FROM v_observations) AS observations,
  (SELECT COUNT(*) FROM v_entities) AS entities,
  (SELECT COUNT(*) FROM v_technologies) AS technologies,
  (SELECT COUNT(*) FROM v_studies WHERE pub_year IS NOT NULL) AS studies_with_pub_year,
  (SELECT COUNT(DISTINCT (CAST(pub_year AS INTEGER)//10)*10) FROM v_studies WHERE pub_year IS NOT NULL) AS decades_covered,
  (SELECT COUNT(*) FROM v_studies_with_high_prescience) AS high_prescience_studies;
"
```

Expected baseline as of 2026-06-13 (post-v1.6.1 + Pass B reconcile):
- studies: 1452
- observations: 23926
- entities: 3276
- technologies: 4361
- studies_with_pub_year: 1452
- decades_covered: 6 (when using integer-division `//`; the DOUBLE-arithmetic bug below produces 38)
- high_prescience_studies: 125 (124 pre-dectp; +1 after Pass B reconcile applies)

Prior baseline (2026-05-27 post-v6+v6.1, pre-v1.6 release): 1434 studies / 23605 obs / 3207 ent / 4312 tech / 109 high-prescience.

If any of these numbers differ wildly from prior session's audit, something is wrong. If the audit matches but `kw ask` returns different numbers, the embeddings are stale (run Phase 5).

## Workflow B: Row-level data backfill or correction

Use when Pete asks "fill missing `<col>` values" or "correct these rows" — the canonical example being the 2026-05-27 pub_year backfill.

### Step 1: Diagnose

Confirm in the live DuckDB before touching anything:
```bash
duckdb ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb -c \
  "SELECT COUNT(*) AS total, \
          COUNT(<col>) AS populated, \
          COUNT(*) - COUNT(<col>) AS missing \
   FROM v_<table>;"
```

Also check the master directly (the live view might be a derivation; the master is truth):
```bash
duckdb -c "SELECT COUNT(*), COUNT(<col>) FROM read_csv_auto('~/Desktop/Archive/archive_masters/_master_<table>.csv');"
```

If the counts disagree, the column is derived in Phase 1 — fix the masters, the derivation will catch up.

### Step 2: Extract candidates

Build an extractor script (e.g., `extract_<col>_candidates_v1.py`) that produces a candidates CSV:
- Columns: `<row_id>, current_value, proposed_value, source, confidence`
- `source` indicates extraction rule (filename pattern, raw-text grep, hand-fill, etc.)
- `confidence` lets Pete sort review by trust level

Save to `/home/user/workspace/<col>_candidates_v1.csv`. Bump version on every iteration.

### Step 3: Pete reviews

Pete typically opens the candidates CSV in Numbers, hand-edits, and returns a vN file. Read it back with `numbers-parser` if needed.

### Step 4: Apply

Write `apply_<col>_v<N>.py` following the same invariants as Workflow A Step 2 (backup, QUOTE_ALL, dry-run default, row-parity check). Apply to the master, not the parquet:

```python
MASTER = Path.home() / "Desktop/Archive/archive_masters/_master_<table>.csv"
CANDIDATES = "/path/to/<col>_candidates_v<N>.csv"
```

Audit trail: write `pub_year_apply_v<N>_applied.txt` listing every change with old → new values.

### Step 5: Rebuild + verify

Same Phase 1 + Phase 2 sequence as Workflow A Step 4. Verify the missing-count is now zero (or whatever the target was).

If a sanity range applies (e.g., dates must be in [1970, 2026]), run a range query too:
```bash
duckdb ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb -c \
  "SELECT <col>, COUNT(*) FROM v_<table> \
   WHERE <col> < <min> OR <col> > <max> GROUP BY <col>;"
```
Expected: zero rows.

**Then consult the Workflow C decision tree** — does the backfill affect anything `kw ask` retrieves or anything the README counts? If yes, run Phases 3-6 as well. The pub_year backfill on 2026-05-27 SKIPPED this step and as a result `kw ask` still quotes pre-v6 study counts hours later — the canonical example of why Workflow C exists.

## Workflow C: Refreshing wiki content + embeddings from updated DuckDB

Use when Phase 1+2 have already run (DuckDB is current) but `kw ask`, README, AGENTS.md, chat-starter, decade pages, or individual study/entity/tech pages still reflect the old state.

### Step 1: Confirm scope

Run the shape audit (above). Then ask:
- Did the masters change in a way that affects page content (new rows, changed pub_year, new prescience scores)?
- Did the masters change in a way that affects archive-level counts (README/AGENTS.md/chat-starter)?
- Are there hand-authored pages that need to appear in retrieval (e.g., a new methodology-demo study with zero observations)?

### Step 2: Run the affected phases

In order. Each is independently re-runnable.

```bash
# Phase 3 — regenerate wiki/*.md pages (study, entity, tech, decade, theme, collection)
python3 ~/Desktop/Archive/scripts/build/03_generate_vault_v2.py --wiki ~/Repos/kastner-aberdeen-wiki

# Phase 4 — indices, Dataview, Bases
python3 ~/Desktop/Archive/scripts/build/04_generate_indices_v2.py --wiki ~/Repos/kastner-aberdeen-wiki

# Phase 5 — re-embed (bge-m3 1024-dim via Ollama; `ollama pull bge-m3` ~1.2 GB)
python3 ~/Desktop/Archive/scripts/build/05_compute_embeddings_v3.py --wiki ~/Repos/kastner-aberdeen-wiki

# Phase 6 — README, AGENTS.md, chat-starter.md (scaffolding)
python3 ~/Desktop/Archive/scripts/build/06_emit_scaffolding_v1.py --wiki ~/Repos/kastner-aberdeen-wiki
```

**Time budget**:
- Phase 3: ~30 sec for stub pages only; **up to ~3 hours (180 min) for full tier-1 LLM regeneration on the ~1,434-study v1.6 corpus** — empirically measured 2026-05-31 (09:06:08 → 12:05:20). Plan unattended runs around this; tee + caffeinate are mandatory. Consult `kastner-wiki-builder` skill §8 for tier-1 details and any flags that may suppress tier-1 work for fast iterations.
- Phase 4: <30 sec (empirically 1 sec on the 2026-05-31 run)
- Phase 5: **~14-15 min for re-embed of ~10,300 pages (v1.6 corpus, bge-m3 1024-dim)**; was ~12 min on the v1.4 ~8,500-page corpus. Rate scales roughly linearly with page count.
- Phase 6: <30 sec

### Step 3: Validate `kw ask` reflects the change

Ask the same question that exposed stale numbers (e.g., "what is the shape of the Kastner archive") and confirm the response now matches the shape audit. If not, Phase 5 didn't re-embed the changed pages.

### Step 4: For hand-authored generated studies

If adding a new wiki page that isn't derived from the masters (e.g., a methodology explainer study with `observation_count = 0`):
1. Hand-author the markdown at `~/Repos/kastner-aberdeen-wiki/wiki/studies/<slug>.md` with frontmatter matching `kastner-wiki-builder` skill §9 conventions
2. Skip Phase 3 (would overwrite the hand-authored page) UNLESS the page is also represented in the masters
3. Run Phase 5 (re-embed) so `kw ask` can retrieve it
4. Optionally Phase 4 if it should appear in indices
5. Add an entry to `_master_studies.csv` if it should appear in `v_studies` counts — but flag it with a `synthetic: true` field or similar so it's distinguishable from ingested studies

### Step 5: iCloud trap (HISTORICAL — obsolete since 2026-06-01)

**Status: not an active risk.** The live wiki was migrated from `~/Desktop/kastner_wiki/` to `~/Repos/kastner-aberdeen-wiki/` on 2026-06-01 specifically to escape iCloud Drive's "Desktop & Documents" sync. `~/Repos/` is not iCloud-synced.

The historical failure mode: iCloud would rename mid-flight files written by Phase 5 to `... 2.md` and corrupt the working tree. This cost a full Phase 5 run in pre-migration days.

Keep this section as archaeology. If Pete ever moves the wiki back under `~/Desktop/`, this risk reactivates. Detailed history in `kastner-github` skill under "The iCloud Desktop trap".

## The pipeline gotchas (lessons earned the hard way)

### Gotcha 1: build_duckdb_only_v3.py is not Phase 1

This script loads CSVs into a fresh DuckDB but **does not run derivation logic**. It produces parquets at `~/Desktop/Archive/kastner_duckdb_build/data/` that **lack** `pub_year`, prescience rollups, and occurrence counts. **Never promote these parquets to `~/Repos/kastner-aberdeen-wiki/data/`.** The wiki will break.

**Rule**: after any masters edit, the correct rebuild is `01_load_csvs_v2.py` → `02_build_data_layer_v4.py`. Not `build_duckdb_only_v3.py`.

### Gotcha 2: The wiki path migrated 2026-06-01 — old `~/Desktop/` path is dead

Until 2026-06-01 the live wiki lived at `~/Desktop/kastner_wiki/`. On that date it was migrated to `~/Repos/kastner-aberdeen-wiki/` to escape iCloud Desktop sync corruption, and the Desktop copy was deleted. Any command that still references `~/Desktop/kastner_wiki/` will fail with `IO Error: Cannot open file`.

**Rule**: every `duckdb` query, every `--wiki` argument, every Phase 1-6 invocation uses `~/Repos/kastner-aberdeen-wiki/`. Always. The repo at `~/Repos/kastner-aberdeen-wiki/` is BOTH the live working wiki AND the GitHub clone — Phase 2 writes the DuckDB there, and `git push` ships releases from the same tree.

### Gotcha 3: The `v_*` views read from absolute paths

Phase 2 creates views like:
```sql
CREATE VIEW v_studies AS
  SELECT * FROM read_parquet('/Users/scott/Repos/kastner-aberdeen-wiki/data/studies.parquet');
```
The path inside the view is **hardcoded absolute**. If you copy `kastner.duckdb` to a different machine or directory, the views will return errors. The DB file alone is not portable; the `data/` directory must be at the path the views expect.

**Rule**: do not copy or move `kastner.duckdb` independently of `data/`. Always treat `<wiki>/db/kastner.duckdb` + `<wiki>/data/*.parquet` as a single atomic unit.

### Gotcha 4: The masters are truth, not the parquets

If a masters CSV says X and the parquet says Y after a rebuild, the parquet is wrong. Re-run Phase 1. The masters are the only thing committed to GitHub at row-level granularity; the parquets are derived artifacts.

**Rule**: edits go to `~/Desktop/Archive/archive_masters/*.csv`. Never edit parquets directly. Never edit the DuckDB tables directly via `UPDATE` SQL.

### Gotcha 5: Backup paths and naming convention

Every masters edit produces a backup. Convention:
- `_master_<table>.csv.bak_<reason>_<utc-stamp>Z`
- `<utc-stamp>` = `YYYYMMDDTHHMMSS`
- Reason is short and slug-style: `add_year_observed`, `pub_year_v6`, `pub_year_v6_1`, etc.

These backups stay in `archive_masters/` alongside the live file. On EOD commit, they are NOT typically committed to GitHub (they live locally on Pete's Mac); only the live master goes up. If a backup MUST be preserved in version control, mirror it under `archive_masters_pre_<change>_<utc-stamp>Z/<filename>` in the same EOD batch commit (see `kastner-github` skill).

### Gotcha 6: Versioning is mandatory

Per Pete's standing rule:
- Every script gets `_v1` from creation, bumped on every change
- Every candidates / audit CSV gets `_vN`
- Apply scripts get `apply_<col>_v<N>.py` matching the candidates version

Never overwrite a `_v1`. If you'd edit it, save as `_v2`.

### Gotcha 7: Stale embeddings silently lie

**Failure mode**: Phase 1+2 update the DuckDB views with the correct row counts. But the wiki markdown pages and the bge-m3 embedding index still encode the PRE-edit content. `kw ask` retrieves real pages (so the citations look authoritative), but the retrieved text contains old numbers. The LLM synthesizes a confident answer that is provably wrong against the live DuckDB.

**How this happened on 2026-05-27**: v6 + v6.1 pub_year backfill ran. Phase 1+2 rebuilt cleanly. `v_studies` correctly reported 1,434 studies, 23,605 observations. But the `wiki/README.md` (written at v1.4 build time) still claimed 933 studies. Embeddings still pointed at the v1.4 README. `kw ask "what is the shape of the Kastner archive"` returned "933 studies, 19,175 observations" with high confidence and three retrieval citations.

**Detection**: any time the shape-audit output disagrees with what `kw ask` says, the embeddings are stale. Build the habit of running the shape audit before AND after every session and pasting it into the decisions log entry.

**Resolution**: Workflow C. Phase 5 + Phase 6 minimum, ideally Phases 3-6 to also refresh the per-page counts that show up in study/entity/tech body text.

### Gotcha 8: Phase 6 scaffolding overwrites README and AGENTS.md

Phase 6 (`06_emit_scaffolding_v1.py`) regenerates `README.md`, `AGENTS.md`, and `chat-starter.md` **from templates**. Any hand-edits to those files between builds are lost.

**Mitigations**:
- If you need a hand-authored note in those docs, put it in a section the template preserves (consult `kastner-wiki-builder` skill §5 Phase 6 for template structure)
- Or store the hand-authored content in a separate file (`wiki/_notes/<topic>.md`) and reference it from the templated docs

**Rule**: assume `README.md`, `AGENTS.md`, `chat-starter.md` are regenerated artifacts, not hand-edited docs.

### Gotcha 10: Phase 1 PRESERVES the authored prescience enum — it does NOT recompute from observation mean

**Failure mode (mine, 2026-06-13 §11v cont 2)**: I told Pete that if he authored `prescience=high` in `_master_studies.csv` but the underlying observation scores averaged below 3.5, Phase 1 would "overwrite" his authored verdict with the math-derived value. **This is wrong.** Phase 1 reads the `prescience` column from `_master_studies.csv` and passes it through as `study_prescience_enum` in `v_studies`. The `prescience_mean` / `prescience_max` / `prescience_obs_count` columns are computed *alongside* it, not in place of it.

**Canonical proof (2026-06-13)**: Plaza DECtp transcript — authored `prescience=high` with a player-rebuttal rationale; underlying 26 scored observations averaged 0.46. After Phase 1+2 rebuild, `v_studies_with_high_prescience` increased by 2 rows (Plaza was one of them) and Plaza's `study_prescience_enum` was `high` with `prescience_mean` = 0.46 displayed alongside. The authored verdict survived.

**Architectural meaning**: this is what makes Path B (player rebuttal) work. The scorer's math is preserved in `prescience_mean` for transparency, but the human-authored verdict in `prescience` is what drives `v_studies_with_high_prescience` and `kw ask`. **Do not re-derive `prescience` from `prescience_mean` in Phase 1 logic** — that would break Path B and silently overwrite every rebuttal.

**Rule**: when explaining what Phase 1 does, the `prescience` column is **pass-through, not recomputed**. The math columns are additive context, not a replacement.

### Gotcha 11: v_studies column names — `study_prescience_enum`, not `prescience`

**Failure mode (2026-06-13 §11v cont 2)**: after Phase 1+2, ran `SELECT prescience FROM v_studies WHERE ...` and got `Binder Error: Referenced column "prescience" not found in FROM clause`. The `v_studies` view exposes the prescience metadata under **different column names** than the raw master CSV.

**Mapping**:

| Raw master (`_master_studies.csv`) column | `v_studies` view column |
|---|---|
| `prescience` (the authored enum: high/medium/low/not-applicable) | `study_prescience_enum` |
| `prescience_rationale` (the prose explanation) | `study_prescience_rationale` |
| `collection_type` / bucket type (memoir, video-transcript, dct, etc.) | **`type`** (NOT `collection_type` — see Gotcha 12) |
| — (computed from `_master_prescience_scores.csv`) | `prescience_mean` |
| — (computed) | `prescience_max` |
| — (computed) | `prescience_obs_count` |

**Rule**: when querying `v_studies` for prescience-related data, use `study_prescience_enum` and `study_prescience_rationale`. When reading the master CSV directly with `read_csv_auto`, use `prescience` and `prescience_rationale`. The view `v_studies_with_high_prescience` filters on `study_prescience_enum = 'high'` — that filter respects the authored verdict per Gotcha 10.

**Discovery query that works** (verifies all 5 transcript verdicts):
```sql
SELECT study_id, study_prescience_enum, prescience_mean, prescience_obs_count
FROM v_studies
WHERE study_id IN ('dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836',
                   'tandem-himalayan-airport-commercial-tpc-c-0b1c60', ...)
ORDER BY study_id;
```

### Gotcha 12: v_studies bucket-type column is `type`, NOT `collection_type`

**Failure mode (2026-06-13 §11v cont 5)**: KW Console v1's `list_studies()` query selected `collection_type` from `v_studies`. First browse-by-type click crashed with `BinderException: Referenced column "collection_type" not found in FROM clause`. Pete's `DESCRIBE v_studies` output (pasted into the chat) showed the actual column is named **`type`**.

**Why this happens**: the master CSV may use `collection_type` as the column header (per the six Kastner collection types: video-transcript, memoir, employer-record, ai-response, technology-topic, dct), but Phase 2's view-creation SQL renames or aliases this to `type` in `v_studies`. Likely a legacy short-name from early pipeline versions.

**Authoritative column list for `v_studies` (verified 2026-06-13 via `DESCRIBE v_studies`)**:
```
study_id, title, author, date, type, subject_domain, methodology,
source_file, abstract, license, importance, importance_rationale,
relevance, relevance_rationale, study_prescience_enum,
study_prescience_rationale, pub_year, prescience_max, prescience_mean,
prescience_obs_count
```
(20 columns total.)

**Rule**: any code that queries `v_studies` for the bucket-type column uses `type`, not `collection_type`. When in doubt, run `DESCRIBE v_studies` first — never assume column names from the master CSV transfer unchanged.

**Companion check for the other views**: if downstream code browses `v_entities` or `v_technologies` by type and hits a similar BinderError, run `DESCRIBE v_<view>` and confirm the column name before patching the SQL. The aliasing rule may or may not be consistent across views — verify per-view, don't assume.

### Gotcha 9: Producer/consumer schema drift — verify the contract empirically, never trust docstrings

**Failure mode**: Phase N emits a data file (parquet, CSV, JSON). Phase N+M (or a downstream script like `kw_ask.py`, `semantic_search.py`, a wiki page generator) reads that file expecting a specific schema. Producer and consumer were written at different times by different intents. The producer's docstring says one thing about the schema; the consumer assumes another. **The contract is never verified empirically before commit.** Output looks fine in isolation (producer runs clean, file is written), but the consumer fails at first read.

**Canonical example (2026-05-31)**: `05_compute_embeddings_v2.py` emitted columns `(path, slug, embedding, dim)`. Its docstring claimed *"embeddings.parquet schema unchanged"* — wrong; the v1.4 schema had been `(page_path, page_type, slug, title, vector, dim)`. `kw_ask.py` (the primary consumer, used by Pete daily) was still coded against the v1.4 schema and crashed on first query with `Binder Error: Referenced column "vector" not found in FROM clause`. Phase 5 v2 ran clean. Phase 5 v2's tests (whatever they were) didn't include a `kw_ask.py` retrieval. The schema drift sat hidden until the first user query — today, after a 17-min Phase 5 run — forced a full Phase 5 v3 + re-run.

**Detection rule**: any time a producer script claims its output schema or format, **read the consumer's first query against that file and verify by name that every column it references actually exists in the producer's output**. If they don't match, the producer is wrong (or the consumer is wrong, but you have to know before you ship).

**Mandatory pre-commit verification** for any pipeline phase that writes a file consumed by another script:
1. List the columns/fields the producer writes (read the `to_parquet()`, `to_csv()`, `json.dump()` call site)
2. List the columns/fields each consumer reads (grep for `SELECT`, `df[`, `row[`, `record[` in every consumer script)
3. Diff the two lists. **Every consumer reference must have a producer source.** Renames count as breaking changes; new columns added by the producer are OK; columns removed by the producer that are referenced by a consumer are bugs.
4. If the producer docstring claims the schema, validate the docstring against the actual code. Stale docstrings are a leading indicator of this gotcha.

**Why this matters more in this archive than most projects**: the Kastner pipeline has many small scripts produced over multiple sessions by multiple agents. There's no test harness that runs producer + consumer together. The first detection of schema drift is always a user query failure — expensive in wall-clock and credits.

**Rule**: creators of contractual code MUST verify with consumers before committing. Never ship a producer whose docstring claims a schema the consumer doesn't match.

## Quick command reference

| Action | Command |
|---|---|
| Verify masters column count | `duckdb -c "SELECT * FROM read_csv_auto('~/Desktop/Archive/archive_masters/_master_studies.csv') LIMIT 1;"` |
| Verify live DuckDB | `duckdb ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb -c "SELECT COUNT(*) FROM v_studies;"` |
| **Shape audit (run before AND after every rebuild)** | See "Shape audit" section above |
| Phase 1 (derive) | `python3 ~/Desktop/Archive/scripts/build/01_load_csvs_v2.py --archive ~/Desktop/Archive/archive_masters --wiki ~/Repos/kastner-aberdeen-wiki` |
| Phase 2 (DuckDB) | `python3 ~/Desktop/Archive/scripts/build/02_build_data_layer_v4.py --wiki ~/Repos/kastner-aberdeen-wiki` |
| Phase 3 (pages) | `python3 ~/Desktop/Archive/scripts/build/03_generate_vault_v2.py --wiki ~/Repos/kastner-aberdeen-wiki` |
| Phase 4 (indices) | `python3 ~/Desktop/Archive/scripts/build/04_generate_indices_v2.py --wiki ~/Repos/kastner-aberdeen-wiki` |
| Phase 5 (embed) | `python3 ~/Desktop/Archive/scripts/build/05_compute_embeddings_v3.py --wiki ~/Repos/kastner-aberdeen-wiki` (v3 emits `kw_ask.py`-compatible 6-column schema; see Gotcha 9) |
| Phase 6 (scaffolding) | `python3 ~/Desktop/Archive/scripts/build/06_emit_scaffolding_v1.py --wiki ~/Repos/kastner-aberdeen-wiki` |
| List `v_*` views | `duckdb ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb -c "SHOW TABLES;"` (DuckDB shows views here too) |
| Check Phase 1 manifest | `cat ~/Repos/kastner-aberdeen-wiki/build_manifest.json` |
| Validate kw ask matches shape | `kw ask "what is the shape of the Kastner archive"` then compare to shape-audit numbers |

## End-of-day shipping

After Phase 1 + Phase 2 succeed and verification passes, route through `kastner-github` skill for the EOD batch commit. Typical artifacts:

1. The updated `archive_masters/_master_<table>.csv`
2. A backup tree entry under `archive_masters_pre_<change>_<utc-stamp>Z/_master_<table>.csv`
3. New scripts under `scripts/`
4. Candidates CSV (if it represents a source of truth for the change, like `pub_year_candidates_v6.csv`)
5. Audit trail (`<col>_apply_v<N>_applied.txt`)
6. `WORKLIST.md` refresh — edit today's dated workspace file `WORKLIST_<YYYY_MM_DD>.md`, then re-mirror to `/home/user/workspace/WORKLIST.md` so the two are byte-identical. The EOD commit writes the undated mirror to the repo as `WORKLIST.md` (see `kastner-github` skill EOD step 3 for the full mirror rule A)
7. `_decisions_log.md` append — **must include the shape-audit output** (before + after)
8. `future_work_v<N>.md` (if items deferred)

**Repo path layout** (important — the repo flattens the Mac directory):
- Mac: `~/Desktop/Archive/archive_masters/_master_studies.csv`
- Repo: **`/_master_studies.csv`** (repo root, NOT under an `archive_masters/` subdirectory)
- Backups go to `archive_masters_pre_<change>_<utc-stamp>Z/_master_<table>.csv` at repo root

One commit to `shorttack/aberdeen-group-archive`. If Workflow C ran (Phases 3-6), the regenerated wiki pages, scaffolding docs, and embeddings parquet typically need to ship to `shorttack/kastner-aberdeen-wiki` too — that repo IS the live working wiki at `~/Repos/kastner-aberdeen-wiki/` (since the 2026-06-01 path migration), so a `git push` from that tree both updates the public release AND captures the latest local state in version control.

## Cross-skill handoffs

- **For the GitHub commit mechanics**: defer to `kastner-github` skill (Git Data API patterns, large-blob handling, sha-match invariants)
- **For ingesting new study files**: defer to `archival-ingest` skill (Pass A/B/C, observation extraction)
- **For full wiki rebuild from scratch**: defer to `kastner-wiki-builder` skill (Phases 3-6 templates, tier-1 LLM rules, frontmatter conventions, page-size caps)
- **For wiki markdown regeneration after a masters edit**: Workflow C of this skill handles routine refreshes; consult `kastner-wiki-builder` for template details if pages emit incorrectly

## Pre-flight checklist (run through this before any masters edit)

1. Did I run the **shape audit** to capture the current baseline? (Output goes in the EOD decisions log entry.)
2. Am I editing a master CSV at `~/Desktop/Archive/archive_masters/`? (Yes → continue; No → wrong path)
3. Is the script versioned `_v1`+ from the start?
4. Does the script default to dry-run with `--commit` as opt-in?
5. Does the script use `csv.QUOTE_ALL` on write?
6. Does the script write a backup `_master_<table>.csv.bak_<reason>_<utc-stamp>` BEFORE the write?
7. Does the script preserve row count and report it?
8. After the edit, am I running Phase 1 (`01_load_csvs_v2.py`) and Phase 2 (`02_build_data_layer_v4.py`)?
9. **Did I consult the Workflow C decision tree** to determine whether Phases 3-6 also need to run? (If `kw ask` results matter, the answer is usually yes.)
10. Am I verifying against `~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb` (not the deleted `~/Desktop/kastner_wiki/` path)?
11. Did I run the **shape audit again** after the rebuild and confirm the delta matches expectations?
12. If Phase 5 ran, did I confirm `kw ask` returns updated numbers?
13. Have I delivered the script via the repo (`scripts/<file>` → `git pull` → `cp`), not the file panel?
14. Is the EOD shipping handed off to `kastner-github` skill (no per-file commits during the session)?
15. Does the EOD `_decisions_log.md` entry include both shape-audit outputs (before + after)?
16. **Producer/consumer contract check** (see Gotcha 9): if I touched a script that writes a file consumed by another script (parquet, CSV, JSON), did I grep every consumer for every column reference and confirm each one exists in the producer's output? Did I diff the producer's docstring against the actual code? **No script that writes a contractual artifact ships without this verification.**

## Pass C: three-file architecture + diagnosis tree (v1.5)

Pass C (cloud-API prescience scoring) data lives in **three files**, not two. Two sessions burned ~80 min on 2026-06-13 (§11v + §11v cont 2) discovering this. Read this section before running anything Pass C-related.

### The three-file architecture

| File | Path | Cols | Purpose |
|---|---|---|---|
| **File 1** | `~/Desktop/Archive/prescience_scores_pass_c_cloud_v1.csv` | 8 | Live v5 output. v5 reads (dedup) + writes. **Authoritative for scores.** |
| **File 2** | `~/Desktop/Archive/archive_masters/_master_prescience_scores.csv` | 11 | Studies-attached score master. Adds `study_id`, `scorer_version=cloud_v1`, `source_pass=pass_c_cloud`. Append-only from File 1 via promote script. |
| **File 3** | `~/Desktop/Archive/aberdeen-group-archive/prescience_scores_pass_c_cloud_v1.csv` | 8 | Repo snapshot. Stale by hundreds of rows. DO NOT query for scoring decisions. |

For **verdicts** (the `prescience` column in studies master): **`~/Desktop/Archive/archive_masters/_master_studies.csv` is canonical.** The repo copy (`~/Desktop/Archive/aberdeen-group-archive/_master_studies.csv`) is downstream, synced via `sync_studies_verdicts_repo_from_archive_masters_v2.py`.

### Canonical Pass C paths

| Artifact | Path | Notes |
|---|---|---|
| Runner | `~/Desktop/Archive/aberdeen-group-archive/scripts/run_prescience_pass_c_v5.py` | Active |
| Promote (File 1 → File 2) | `~/Desktop/Archive/aberdeen-group-archive/scripts/promote_pass_c_to_master_v1.py` | Active. Append-only, dedupes on `obs_id`. |
| Sync (archive_masters → repo) | `~/Desktop/Archive/aberdeen-group-archive/scripts/sync_studies_verdicts_repo_from_archive_masters_v2.py` | Active. v2 syncs `prescience` + `prescience_rationale` only (v1 synced all 6 verdict cols, superseded). |
| Roll-up v3 | `scripts/v3_obsolete/roll_up_prescience_v3.py` | **DEPRECATED 2026-06-13.** Read File 2; only flipped `[DEFERRED]`. Replaced by manual write + sync. |
| Master obs (v5 reads) | `~/Desktop/Archive/archive_masters/_master_observations.csv` | NOT repo copy |
| Scope whitelist | `~/Desktop/Archive/prepared/<study_id>/` | `os.listdir(PREPARED)`; empty dir OK |
| Logs | `~/Desktop/Archive/logs/pass_c_cloud_v1_*.{md,jsonl}` | run report, failures, prefilter audit |
| API key | `~/.config/adoptex/perplexity.env` | sonar-reasoning-pro |

### Current workflow (2026-06-13 onward, post-v3-deprecation)

**Path A — scorer-is-judge, math-driven:**

1. Score: `python3 scripts/run_prescience_pass_c_v5.py` (writes File 1)
2. Promote: `python3 scripts/promote_pass_c_to_master_v1.py --commit --scorer-version cloud_v1 --source-pass pass_c_cloud` (File 1 → File 2)
3. Compute verdict (Rule A, below) over File 2 rows for the study_id
4. Write verdict into `~/Desktop/Archive/archive_masters/_master_studies.csv`
5. Sync to repo: `python3 scripts/sync_studies_verdicts_repo_from_archive_masters_v2.py --commit`

**Path B — player rebuttal overrides scorer:**

1. Steps 1+2 above (still record raw scores in File 2)
2. Author rebuttal note at `kastner-author/notes/<study_id>_prescience_rationale_<date>.md`
3. Author verdict + rationale directly in archive_masters' `prescience` and `prescience_rationale` columns
4. Sync to repo (step 5 above)
5. Scorer-is-judge satisfied: the player's argument is recorded alongside the verdict

### v5 quirks

1. **`obs in 492 prepared studies` is a hardcoded string literal** at line 333. Ignore it. Trust `prepared studies on disk: N`.
2. **`load_already_scored()` reads File 1 only.** Never File 2 or 3.
3. **No `--study-ids` flag.** Scope via `prepared/` directory membership.
4. **Prefilter is rule-based.** Prefiltered obs go to File 1 with empty `prescience_score`. They count toward `n_total`, not `n_used`.

### Verdict rules (Rule A)

```
used = [s for s in pass_c_scores if s != -1]   # -1 = prefiltered

if len(used) == 0:
    verdict = 'not-applicable'
elif sum(used)/len(used) >= 3.5: verdict = 'high'
elif sum(used)/len(used) >= 2.0: verdict = 'medium'
else:                            verdict = 'low'
```

### Diagnosis tree: "0 to process"

Walk in order.

**Step 1 — study_id in `~/Desktop/Archive/prepared/`?**
```bash
ls -d ~/Desktop/Archive/prepared/<study_id>
```
If missing: `mkdir -p ~/Desktop/Archive/prepared/<study_id>`.

**Step 2 — obs exist in `_master_observations.csv`?**
```bash
python3 -c "import csv; print(sum(1 for r in csv.DictReader(open('/Users/scott/Desktop/Archive/archive_masters/_master_observations.csv')) if r['study_id']=='<study_id>'))"
```
If 0: run Pass B ingest first.

**Step 3 — already scored in File 1?**
```bash
python3 -c "
import csv
target = {r['obs_id'] for r in csv.DictReader(open('/Users/scott/Desktop/Archive/archive_masters/_master_observations.csv')) if r['study_id'] == '<study_id>'}
hits = sum(1 for r in csv.DictReader(open('/Users/scott/Desktop/Archive/prescience_scores_pass_c_cloud_v1.csv')) if r['obs_id'] in target)
print(f'in File 1: {hits} / {len(target)}')
"
```
If all present: skip v5; compute verdict (Step 4), then Path A or B above.

**Step 4 — compute verdict directly** (no API call needed): use Rule A above.

### Pass C gotchas

- **Three files, not two.** File 1 (live), File 2 (study-attached, lags), File 3 (repo, very stale). The 2026-06-13 sessions assumed two and burned hours.
- **`[DEFERRED]` studies may already be scored.** Always check File 1 first (Step 3). The 2026-06-13 §11v session burned credits planning an API run for 5 studies that turned out fully scored (4 all-prefiltered = not-applicable; 1 with 26 scored obs = low).
- **v3 is deprecated.** It read File 2 (which lagged File 1) and only flipped `[DEFERRED]`. Replaced by `promote_pass_c_to_master_v1.py` + manual write + `sync_studies_verdicts_repo_from_archive_masters_v2.py`. v3 sits in `scripts/v3_obsolete/`.
- **Existing File 2 rows use `scorer_version=cloud_v1` and `source_pass=pass_c_cloud`**, not the runner's defaults. Pass these explicitly when promoting.
- **Repo `_master_studies.csv` is downstream of `archive_masters/_master_studies.csv`.** Edit archive_masters, then sync. Never edit the repo copy directly.
- **The hardcoded `492` label in v5** doesn't update when you add prepared/ dirs. Trust `prepared studies on disk: N` instead.

The companion runbook lives at `~/Desktop/Archive/aberdeen-group-archive/Perplexity_Only/PASS_C_RUNBOOK.md`. Skill and runbook must stay in sync.
