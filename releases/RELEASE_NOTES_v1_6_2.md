# Release v1.6.2 — Multi-Horizon Prescience

**Date**: 2026-06-17
**Prior tag**: v1.6.1 (archive) / v1.6 (wiki)
**Corpus**: unchanged from v1.6 — 1,452 studies, 23,926 observations, 3,276 entities, 4,361 technologies

## Headline

**New 3-year and 5-year prescience results added. No new studies.**

The v1.6 release shipped first-pass prescience scores from the Pass C cloud run (sonar-reasoning-pro). v1.6.2 promotes a substantially larger pool of scored observations into the masters by lifting the Tier B prefilter sentinel, applying the obs_id Universal Normalizer (v20), and resolving the historical Pass C three-file architecture lag.

Net effect on the prescience surface:

| Metric | v1.6.1 | v1.6.2 | Delta |
|---|---:|---:|---:|
| Total observations | 23,926 | 23,926 | — |
| Observations with prescience score | 3,829 | **15,924** | **+12,095** |
| Authored `prescience='high'` studies | 125 | **498** | **+373** |
| `prescience_max ≥ 4` observation-derived | 126 | **865** | **+739** |
| `prescience_mean ≥ 3.5` studies | (n/a) | **115** | — |
| `pmax = 5` studies | (n/a) | **614** | — |

Verdict distribution (`study_prescience_enum`, v1.6.2):

| Verdict | Studies |
|---|---:|
| high | 498 |
| medium | 330 |
| low | 276 |
| not-applicable | 346 |
| [DEFERRED] | 1 |
| (unrated) | 1 |

Two distinct "high" populations are now exposed and the project is consciously holding the definitional split open as a backlog item:

- **498** — author-curated verdicts (`study_prescience_enum = 'high'`); the canonical surface for the `v_studies_with_high_prescience` view and for `kw ask` retrieval.
- **865** — observation-derived (`prescience_max ≥ 4`); a looser surface useful for discovering studies whose single most-prescient observation crossed the bar even if the body of work didn't.
- **115** — observation-derived (`prescience_mean ≥ 3.5`); a tighter math-anchored surface.

All three are exposed in `v_studies` so downstream researchers can pick the threshold appropriate to their question.

## What changed

### Data
- **Tier B promote** — 8,645 previously-prefiltered observations restored into `_master_prescience_scores.csv` (8,440 → 17,085 rows)
- **Sentinel filter at ingest** — Phase 1 (`01_load_csvs_v3.py`) now drops `prescience_score < 0` sentinel rows at the chokepoint, preventing parse-fail, prefilter-excluded, and content-unrecoverable markers from polluting downstream rollups. 908 sentinel rows dropped on the v1.6.2 build (756 historical pass_c_cloud + 64 SH parse-fails + 12 pass_c_cloud_parse_fail + 8 Tier B prefilter + 60 other). Sentinel taxonomy: `-1` parse_fail or prefilter_excluded (disambiguated by `source_pass`); `-99` content_unrecoverable.
- **Pass C three-file architecture** documented in the `kastner-archive-pipeline` skill — File 1 (`prescience_scores_pass_c_cloud_v1.csv`, live), File 2 (`_master_prescience_scores.csv`, studies-attached), File 3 (repo snapshot, stale). All scoring decisions read File 2; the repo copy is for distribution only.

### Pipeline
- **Phase 1 v3** (`01_load_csvs_v3.py`) — single-chokepoint sentinel filter applied before joins
- **`promote_pass_c_to_master_v1.py`** — append-only, dedupes on `obs_id`, explicit `scorer_version=cloud_v1` and `source_pass=pass_c_cloud`
- **`sync_studies_verdicts_repo_from_archive_masters_v2.py`** — narrows sync to `prescience` + `prescience_rationale` columns
- `roll_up_prescience_v3.py` **deprecated** — relocated to `scripts/v3_obsolete/`; replaced by manual verdict write + sync

### Wiki
- Full Phase 3-6 rebuild on `qwen3.5:27b-mlx` (local Ollama, MLX engine)
- Studies pages: 1,452 (tier-1 LLM regeneration for 865 high-prescience pages; tier-2 templates for the remainder)
- Entity pages: 3,276 · Technology pages: 4,361 · Code pages: 1,293 · Decade/Theme/Collection pages: 33
- Total pages: **10,382**
- Embedding index re-emitted on `bge-m3` (1024-dim): 10,438 rows

### Schema
- `_master_observations.csv` extended with `legacy_obs_id` audit column (17 cols total) — v20 of the obs_id Universal Normalizer (13-bucket classifier-driven repair of legacy IDs).

## Architectural decision: player rebuttal path

v1.6.2 codifies **Path B** — when the math-derived prescience verdict and the author's domain judgment diverge, Phase 1 preserves the **authored** `prescience` enum in `study_prescience_enum` and exposes the math alongside as `prescience_mean` / `prescience_max` / `prescience_obs_count` for transparency. The `v_studies_with_high_prescience` view filters on the authored verdict, not the math. Canonical example: Plaza DECtp transcript (authored `high`, mean 0.46) — see `dectp_prescience_rationale_2026_06_13.md`.

## Backlog (deferred)

- Definitional review of high-prescience threshold (authored 498 vs max-anchored 865 vs mean-anchored 115)
- Regenerate `study-2026-kastner-prescience-methodology-demo-0cdf48` against v1.6.2 corpus (current prose still references pre-Tier-B numbers in places; one inline sed-patched, full rewrite needed)
- Reconcile observations/studies divergence between archive_masters and repo
- 5-year prescience proposal (`5_year_prescience_proposal_v1.md`)
- Prescience decline across Aberdeen eras findings doc (`study_findings_prescience_decline_aberdeen_eras_v1.md`)
- Methodology code normalization (492 codes)
- 16-obs archive-hygiene pass (SH refusal manifest)
- `archival-ingest` skill v21 — register archive-meta as 7th collection
- §11v Prescience Architecture Audit (D6) — gates v1.7.0

## Provenance

- Phase 1 v3 commit: `27a2f9d7`
- Tier B promote commit: `a1661603`
- Master location audit decision: `b2c45f39`
- Sentinel filter decision + log: `40d5bc9c`
- Phase 3-6 monitor: `7e85eaee`
- Pipeline rebuild log: `~/Desktop/Archive/logs/phase5to6_20260617T213255Z.log`

## DOI

Existing Zenodo DOI: [10.5281/zenodo.20245076](https://doi.org/10.5281/zenodo.20245076) — auto-mints a v1.6.2 minor on publish.
