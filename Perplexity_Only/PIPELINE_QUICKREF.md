# PIPELINE_QUICKREF.md — Pipeline Commands & Expected Behaviors

> **READ THIS FILE before kicking off any phase of the build pipeline.**
> Every command below is the exact form that has worked in production
> sessions. Variants and "improvements" have repeatedly broken things —
> follow the patterns documented here unless you are explicitly changing
> the pipeline contract.

**Last updated:** 2026-06-12 (§11u-cont Pass B Completion).
**Pipeline reference:** `kastner-archive-pipeline` v1.2.

---

## The six phases (with the M:N refactor)

| phase | script | role | typical runtime |
|---|---|---|---|
| 1 | `01_load_csvs_v2.py` | Load 7 masters into DuckDB, write manifest | ~5 sec |
| 2 | `02_build_data_layer_v4.py` | Build 27 views, promote 12 parquets | ~10 sec |
| 3 | `03_generate_vault_v2.py` | LLM-synthesize every wiki page (studies, entities, technologies, topics) | **~3-4 hours** on Pass B-sized batches |
| 4 | `04_generate_indices_v6.py` | Build cross-reference indices, Dataview queries | ~30 sec |
| 5 | `05_compute_embeddings_v3.py` | Embed all pages with bge-m3 (1024-dim, 6-col schema) | ~15 min |
| 6 | `06_emit_scaffolding_v4.py` | Refresh README, AGENTS.md, chat-starter.md, .base files | ~30 sec |

**Phase 1+2** = "data layer" (cheap, idempotent, run whenever masters change).
**Phase 3-6** = "wiki content + embeddings" (expensive, run after Pass B-sized data changes).

---

## Apply-script pattern (merge new content into masters)

The contract for any masters-modifying script:

1. **Dry-run by default.** No `--commit` flag = print preview, write nothing.
2. **Read all 7 masters first, validate column counts** against `MASTERS_NOTES.md`.
3. **Dedupe by `id` against the existing master**, append only new.
4. **Write M:N pairs** to `_master_entity_studies.csv` and `_master_tech_studies.csv` separately from the entity/tech masters.
5. **Backup before write.** Naming: `<master>.bak_<context>_YYYYMMDDTHHMMSSZ`. The full backup tree typically goes into `archive_masters_pre_<context>_YYYYMMDDTHHMMSSZ/`.
6. **Promote per-study schemas** to master schemas as needed (e.g. obs 12 → 17 col by injecting `verification_method`, `collection`, etc.).

**Reference implementation:** `scripts/apply_passb_transcripts_v2.py` (commit `0391dabf`). This is the script to copy when writing the next apply script.

---

## Phase 1 + 2 (data layer rebuild)

```bash
cd ~/Desktop/Archive
python3 scripts/build/01_load_csvs_v2.py \
  --archive ~/Desktop/Archive/archive_masters \
  --wiki ~/Repos/kastner-aberdeen-wiki
python3 scripts/build/02_build_data_layer_v4.py \
  --wiki ~/Repos/kastner-aberdeen-wiki
```

**Expected output:** manifest at `~/Repos/kastner-aberdeen-wiki/db/manifest.json`, `kastner.duckdb` file refreshed, 12 parquets at `~/Repos/kastner-aberdeen-wiki/db/parquet/`, 27 views built.

---

## Shape audit (post-Phase-2)

```bash
duckdb ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb -c "
SELECT
  (SELECT COUNT(*) FROM v_studies)             AS studies,
  (SELECT COUNT(*) FROM v_observations)        AS observations,
  (SELECT COUNT(*) FROM v_entities)            AS entities,
  (SELECT COUNT(*) FROM v_technologies)        AS technologies,
  (SELECT COUNT(*) FROM v_studies_with_high_prescience) AS high_prescience_studies,
  (MAX(pub_year) // 10) - (MIN(pub_year) // 10) + 1 AS decades_covered
FROM v_studies;
"
```

**Gotcha — integer division:** DuckDB's `/` operator returns DOUBLE. The
`(MAX(pub_year) / 10) - (MIN(pub_year) / 10) + 1` form returns
`38.something` for a 1965-2003 range, which looks plausible but is wrong.
**Use `//` for integer division.** Correct answer for 1965-2003 is 6
(decades 1960s, 1970s, 1980s, 1990s, 2000s — wait, that's 5; add 1 for
the inclusive count). Math is `(2000 // 10) - (1960 // 10) + 1 = 200 - 196 + 1 = 5`,
actually 5. If your audit returns 6 with `//`, check the actual min/max
pub_year; the corpus may extend further than you think.

**Baseline (as of 2026-06-12 §11u-cont Pass B):**

| metric | value |
|---|---:|
| studies | 1452 |
| observations | 23926 |
| entities | 3276 |
| technologies | 4361 |
| `v_studies_with_high_prescience` | 124 |
| `decades_covered` | 6 |

---

## Phase 3 (wiki generation — the long one)

```bash
caffeinate -is python3 \
  ~/Desktop/Archive/scripts/build/03_generate_vault_v2.py \
  --wiki ~/Repos/kastner-aberdeen-wiki \
  > ~/Desktop/phase3_<context>_$(date -u +%Y%m%dT%H%M%S).log 2>&1 &
```

**Best practice:** always launch under `caffeinate -is` so the Mac
doesn't sleep mid-run. Always redirect stdout+stderr to a timestamped
log. Always background with `&` so the terminal stays usable.

**Monitoring while it runs:**

```bash
# Is it alive?
ps aux | grep 03_generate | grep -v grep

# How far through? (newest pages first)
ls -lt ~/Repos/kastner-aberdeen-wiki/wiki/technologies | head -5
ls -lt ~/Repos/kastner-aberdeen-wiki/wiki/entities | head -5
ls -lt ~/Repos/kastner-aberdeen-wiki/wiki/studies | head -5

# Total page count (rough completion gauge)
find ~/Repos/kastner-aberdeen-wiki/wiki -name "*.md" -newer <log-file> | wc -l
```

**Generation order:** studies → entities → technologies → topics → indices. Alphabetical within each section. Use the alphabetical position of the most-recent write to estimate progress.

**Gotcha — empty log file:** Python stdout is buffered. `tail -f` on the
Phase 3 log may show zero lines for the first 30-60 minutes even though
the process is healthy. **Trust the filesystem mtimes, not the log.** If
mtimes are advancing, the process is fine. If you want unbuffered output
in the future, prefix with `python3 -u` (`-u` for unbuffered stdout).

**LLM dependency:** Phase 3 calls `_llm_helper_v4.py`, which is pinned to
**qwen3.5:27b-mlx** via Ollama. See `OLLAMA_STATE.md` for the full model
state. Do not swap models mid-pipeline.

---

## Phases 4, 5, 6 (post-Phase-3)

```bash
# Phase 4 — indices (~30 sec)
python3 ~/Desktop/Archive/scripts/build/04_generate_indices_v6.py \
  --wiki ~/Repos/kastner-aberdeen-wiki

# Phase 5 — embeddings (~15 min, bge-m3 1024-dim)
python3 ~/Desktop/Archive/scripts/build/05_compute_embeddings_v3.py \
  --wiki ~/Repos/kastner-aberdeen-wiki

# Phase 6 — scaffolding (~30 sec)
python3 ~/Desktop/Archive/scripts/build/06_emit_scaffolding_v4.py \
  --wiki ~/Repos/kastner-aberdeen-wiki
```

**Phase 5 gotcha:** The schema is **6-col** (per the 2026-05-31 v3 fix):
`page_path, page_kind, page_id, chunk_idx, chunk_text, embedding`. Older
docs may show a different schema — trust the script, not the docs.

---

## When to run what

| trigger | run |
|---|---|
| Per-row backfill on a single master | Phase 1+2 only |
| New observations only (no new studies/entities/techs) | Phase 1+2, then Phase 4+5+6 (skip Phase 3 — no new pages) |
| New studies AND new entities/techs (Pass B-sized batch) | All six phases |
| Skill or scaffolding-only change | Phase 6 only |
| Embedding model swap | Phase 5+6 |
| Full rebuild from scratch | All six, but expect ~5-6 hours |

---

## Verification after a full Phase 3-6 run

```bash
# 1. Shape audit (see above) — confirm counts match expectations
# 2. Embedding count check (NOTE: path is data/embeddings.parquet, NOT db/parquet/)
duckdb -c \
  "SELECT COUNT(*) FROM read_parquet('/Users/scott/Repos/kastner-aberdeen-wiki/data/embeddings.parquet');"
# 3. Stale embeddings check (see §11v "stale embeddings gotcha")
duckdb ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb -c "
  WITH wiki_pages AS (
    SELECT REPLACE(page_path, '.md', '') AS page_path FROM read_parquet('...')
  )
  SELECT COUNT(*) FROM wiki_pages WHERE ...
"
# 4. AGENTS.md and chat-starter.md show updated study/obs/ent/tech counts
grep -E "^(- studies|- observations|- entities|- technologies):" \
  ~/Repos/kastner-aberdeen-wiki/chat-starter.md
```

---

## Things to NEVER do

- ❌ Run an apply script without dry-run first.
- ❌ Edit `_master_entities.csv` or `_master_technologies.csv` without also updating the M:N join tables.
- ❌ Assume per-study CSV columns match master columns. They DON'T — see `MASTERS_NOTES.md`.
- ❌ Use `/` instead of `//` in the shape audit decade math.
- ❌ Kill a Phase 3 process because the log is empty. Trust mtimes.
- ❌ Swap Ollama models mid-pipeline. Pin in `_llm_helper_v4.py` and stick with it.
- ❌ Commit master CSVs without backups in the same commit (or in the same backup tree).

---

**Maintained by:** Pete Kastner + Perplexity Computer.
**Pairs with:** `MASTERS_NOTES.md` (schema), `CANONICAL_IDS.md` (ID cache), `OLLAMA_STATE.md` (model state).
