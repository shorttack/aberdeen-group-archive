# Aberdeen Group Research Archive — v2.0

**"Full-Corpus Multi-Horizon Prescience"** · 2026-06-30

The current corpus: **1,504 studies · 24,842 observations · 3,293 entity rows · 4,376 technology rows · 876 high-prescience studies** (`v_studies_with_high_prescience`, `prescience_max ≥ 4`), spanning **1979–2026** across **6 decades**.

These are the live counts from the v2.0 DuckDB data layer (`v_studies` and companions). Per-subdirectory and per-section numbers elsewhere may lag the masters — when in doubt, `_master_*.csv` is truth.

---

## What's new in v2.0

v2.0 is the largest analytical release since v1.0. Two headline deliverables anchor it.

### 1. Full-corpus 3-year and 5-year prescience

Every gradeable observation in the archive now carries a short-horizon (SH) prescience read at **two fixed windows — 3 years and 5 years after the observation's anchor year** — alongside the existing holistic verdict. This is the first release in which the multi-horizon read covers the *whole* gradeable corpus rather than a tranche.

- **New SH master**: `_master_prescience_short_horizon.csv` — **17,030 rows** (one per gradeable observation), columns `obs_id, study_id, prescience_3y, prescience_5y` plus confidence and anchor-year metadata.
- **Study-level SH verdicts**: **792 studies** now carry author-curated `prescience_3y_enum` / `prescience_5y_enum` (+ rationale) columns, rolled up from the observation-level SH scores via Rule A. The studies master grew from 16 to **20 columns** to hold them.
- **3-year distribution** (792 studies): high **522** · medium **264** · low **4** · not-applicable **1** · pending **1**.
- **5-year distribution** (792 studies): high **518** · medium **268** · low **4** · not-applicable **1** · pending **1**.

The two horizons are deliberately close — most Aberdeen forecasts that came true did so within five years — but the 3y-vs-5y delta is itself a signal: studies whose 3y read is *medium* and 5y read is *high* were early but directionally correct, a pattern the new `v_observations_with_sh` view surfaces via the `windows_diverge` flag.

**New DuckDB views (Phase 2 `02_build_data_layer_v5.py`)**:
- `v_prescience_sh` — the raw 17,030-row SH master.
- `v_studies_with_sh_verdicts` — the 792 studies with their 3y/5y enums.
- `v_observations_with_sh` — observations left-joined to their 3y/5y scores + `windows_diverge`.
- `v_sh_3y_distribution` / `v_sh_5y_distribution` — the distribution tables above.

`v_studies` now exposes `prescience_3y_enum`, `prescience_3y_rationale`, `prescience_5y_enum`, `prescience_5y_rationale` (20 columns total) — they flow through the existing pass-through automatically.

### 2. The v9 confabulation fix

The SH sweep ran **16,232 cloud-API scoring calls**. The v9 scorer corrects a confabulation failure mode in which the model, asked to score an observation against a horizon window that had **not yet elapsed**, would fabricate a confident retrospective verdict rather than abstain. v9 enforces the **window-not-elapsed sentinel (`-2`)** at the chokepoint: an observation whose 3y or 5y window extends past the present is scored `-2` and excluded from the verdict mean, never confabulated.

The net data-quality result across the full SH sweep was clean: **2 of 13,885 scored SH calls** reduced to a `-1` parse-reject (retained as sentinels, not silently dropped):
- `aberdeen-1995-universal-servers-rdbms-technology-next-decade-OBS-006`
- `nospra~1-bd7d6a-OBS-017`

Sentinel taxonomy for the SH master: **`-1`** = prefiltered / parse-reject; **`-2`** = window not elapsed. Both are excluded from verdict means by Rule A.

### 3. PC Deals per-SKU price journeys

The PC Deals weekly-bulletin corpus (the `-mx` v2 agent-as-extraction-brain tier) gains **per-SKU price journeys**: individual hardware SKUs are tracked across successive weekly bulletins so a single processor, drive, or system can be followed as its street price moves week over week. The L7 extraction produced **249 per-SKU journeys**, turning a flat run of pricing bulletins into longitudinal price-history series suitable for trend analysis.

---

## Pipeline changes

- **Phase 1 → `01_load_csvs_v3.py`**: reads `_master_prescience_short_horizon.csv` (registered in `MASTER_SCHEMAS`, `halt=False` so an absent file doesn't crash early builds), writes `short_horizon.parquet`, coerces SH scores to numeric.
- **Phase 2 → `02_build_data_layer_v5.py`**: promotes `short_horizon`, registers the five SH views above (guarded so a missing parquet doesn't crash Phase 2).
- **Phase 3 → `03_generate_vault_v3.py`**: study pages render SH verdicts in frontmatter and a "Short-horizon prescience" body section, so bge-m3 embeds them and `kw ask` can retrieve 3y/5y answers; the tier-1 prompt also receives the 3y/5y context.
- **Phase 6 → `06_emit_scaffolding_v2.py`**: README title bumped to the SH release; "What's new" SH block; AGENTS.md SH query recipes (`v_studies_with_sh_verdicts`, `v_sh_3y_distribution`, `v_observations_with_sh`); chat-starter prompts for 3y-high / 5y-high / 3y-vs-5y distribution; `verify.py` extended with the four SH views.
- **New scripts** (repo `scripts/`): `merge_sh_scores_to_master_v1.py` (builds the 17,030-row SH master), `apply_sh_study_verdicts_v1.py` (writes 3y/5y study enums, 16→20 cols).

## Data layer — shape audit

Identical before and after the SH integration, as expected (the SH work added columns and views, not studies or observations):

```
studies                 1504
observations           24842
entities                3293
technologies            4376
studies_with_pub_year   1504
decades_covered            6
high_prescience          876
```

SH-specific:
```
v_prescience_sh             17030 rows
v_studies_with_sh_verdicts    792 studies
```

## Companion wiki

The Kastner Aberdeen Wiki is rebuilt against the v2.0 masters and tagged in lockstep (`shorttack/kastner-aberdeen-wiki`):
- bge-m3 (1024-dim) re-embed of **10,862 pages** (Phase 5).
- Study pages now carry the short-horizon prescience section, so `kw ask` answers 3y/5y questions from real retrieved text.
- `kw ask` validation passed: "which studies were prescient at 3 years" surfaces a real 3y verdict (Object-Oriented Three-Tier-Plus 1996 — high, mean 3.92). Note: `kw ask` retrieval cites exemplars, not the full population; the ground-truth count (522 high at 3y) lives in `v_studies_with_sh_verdicts`.

## Prior releases

- **v1.9.0** (2026-06-22): Substrate silent-loss recovery + CompChem 1989 exemplar.
- **v1.7.0** (2026-06-18): Multi-horizon prescience groundwork; `row_class` backfill.
- **v1.6.2** (2026-06-17): Tier B promote; observation-level scores 3,829 → 15,924.
- **v1.6.1** (2026-06-13): Pass B reconcile; Path B player rebuttal (Plaza DECtp).
- **v1.6** (2026-05-31): Full 1,400+ study content; initial Pass C cloud scoring.
- **v1.4.0** (2026-05-23): +490 studies from the May 2026 weekend bucket pass.

Full curatorial decision history is in [`_decisions_log.md`](./_decisions_log.md). Version history is in [`CHANGELOG.md`](./CHANGELOG.md).

## License & citation

Structured artifacts (CSVs, descriptors, code, schemas, READMEs) are released under **CC-BY-4.0** — see [`LICENSE`](./LICENSE). Original source content remains the property of its respective rights holders. Cite via [`CITATION.cff`](./CITATION.cff) or:

> Kastner, Peter S. (2026). *Kastner IT Research Archive*, version 2.0. Licensed under CC-BY-4.0. DOI: 10.5281/zenodo.20245076.
