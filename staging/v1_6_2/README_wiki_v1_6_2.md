# Kastner Aberdeen Wiki — v1.6.2

Local-first research environment derived from the [aberdeen-group-archive](https://github.com/shorttack/aberdeen-group-archive)
master CSVs. Built by `kastner-wiki-builder` skill v2.

## Corpus shape (v1.6.2, 2026-06-17)

- **1,452** studies · **23,926** observations · **3,276** entities · **4,361** technologies
- **10,382** wiki pages (1,452 study + 3,276 entity + 4,361 tech + 1,293 code + 33 decade/theme/collection/index)
- **10,438** embedding rows (bge-m3, 1024-dim)
- **5,597** study→entity wikilinks · **11,050** study→technology wikilinks
- Prescience verdicts (`study_prescience_enum`): **498** high · **330** medium · **276** low · **346** n/a · 1 deferred · 1 unrated
- Decades covered: 6 (1970s–2020s)

## What's new in v1.6.2

- **Multi-horizon prescience** — 3-year and 5-year prescience results promoted into the masters. Observations with a prescience score grew from 3,829 (v1.6.1) to **15,924**. Authored `prescience='high'` studies grew from 125 to **498**.
- **Sentinel-aware Phase 1** — `01_load_csvs_v3.py` drops `prescience_score < 0` sentinel rows at the chokepoint before joins (908 sentinels filtered on the v1.6.2 build).
- **`v_studies_with_high_prescience`** view returns **498** rows, filtered on the **authored** `study_prescience_enum = 'high'`, not the math. Player-rebuttal path (Path B) is now canonical: authored verdicts win over scorer math; the math is preserved alongside in `prescience_mean` / `prescience_max` / `prescience_obs_count` for transparency.
- **Tier B promote** — 8,645 previously-prefiltered observations restored into the prescience scoring pool.
- **Full Phase 3-6 rebuild** on `qwen3.5:27b-mlx` (local Ollama, MLX engine). Embeddings re-emitted on bge-m3.

## Quick start

1. Open `wiki/` as an Obsidian vault.
2. Open `wiki/_index.md` and follow links.
3. From terminal: `kw ask "your question"` (uses bge-m3 embeddings + qwen3.5:27b-mlx synthesis).
4. From SQL: `duckdb db/kastner.duckdb` then `SELECT * FROM v_studies_with_high_prescience LIMIT 20`.

## File map

| Path | What |
|---|---|
| `wiki/` | Obsidian vault root — open this in Obsidian |
| `data/*.parquet` | Columnar copies of master CSVs |
| `data/embeddings.parquet` | bge-m3 1024-dim embedding index (10,438 rows) |
| `db/kastner.duckdb` | Pre-built DuckDB with 27 named views |
| `db/queries/*.sql` | Reusable query examples |
| `scripts/build/01..06_*.py` | Six-phase rebuild pipeline |
| `scripts/semantic_search.py` | Local cosine-sim search |
| `build_manifest.json` | What was built, when, with what counts |
| `AGENTS.md` | LLM primer |
| `chat-starter.md` | Pre-warmed prompts |

## Rebuild

```bash
python3 scripts/build/01_load_csvs_v3.py --archive ~/Desktop/Archive/archive_masters --wiki .
python3 scripts/build/02_build_data_layer_v4.py --wiki .
python3 scripts/build/03_generate_vault_v2.py --wiki .
python3 scripts/build/04_generate_indices_v2.py --wiki .
python3 scripts/build/05_compute_embeddings_v3.py --wiki .
python3 scripts/build/06_emit_scaffolding_v1.py --wiki .
```

Time budget for the full chain on M4 Pro Mac mini: ~9 hours (Phase 3 tier-1 LLM passes dominate). Phase 1+2 alone: <1 minute. Phase 5 alone: ~15 minutes.

## Companion archive

[shorttack/aberdeen-group-archive](https://github.com/shorttack/aberdeen-group-archive) — the source-of-truth master CSVs, study packages, and full release notes. This wiki is a derived artifact; the archive is canonical.

## Provenance

- Built: 2026-06-17 17:50 EDT
- Model (Phase 3 LLM): `qwen3.5:27b-mlx` via local Ollama
- Model (Phase 5 embeddings): `bge-m3:latest` (1024-dim) via local Ollama
- Builder skill: `kastner-wiki-builder` v2
- Pipeline skill: `kastner-archive-pipeline` v1.7
