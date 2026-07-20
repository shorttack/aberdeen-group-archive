# Aberdeen Archive v2.1 — Complete Long-Horizon Prescience Scoring

**Data/scoring release. No schema change** (studies master stays 20 columns; master CSV count unchanged).

## Headline

The long-horizon (holistic) Pass C prescience scoring is now **complete across the corpus**. A full backlog sweep scored the previously-unscored gradeable observations, and study-level verdicts were recomputed by Rule A on the now-complete score set.

This **recalibrated the holistic verdict distribution materially**: the `study_prescience_enum = 'high'` surface fell sharply from its v2.0 level, because many earlier "high" verdicts rested on partial (sampled) scoring and did not survive full evaluation. The scorer makes the call — verdicts are not hand-overridden. The 24 memoir chapters (`type = memoir`) retain their curated verdicts and were excluded from the recompute.

## What changed

- **Complete backlog scoring** — every gradeable observation now carries a long-horizon prescience score.
- **Verdicts recomputed** (Rule A, zeros kept in the mean, memoir chapters protected).
- **v2.0 short-horizon (3y/5y) layer unchanged.**

## Counts single source of truth

This release also fixes a maintenance problem: corpus counts used to be hard-coded in prose in many places and went stale every rebuild. As of v2.1, **all counts live in one generated file — [`ARCHIVE_STATS.md`](../ARCHIVE_STATS.md)** — written by `scripts/generate_archive_stats.py` from the live DuckDB and refreshed automatically on every committed pipeline run. The README and these notes link to it rather than quoting numbers inline.

**→ For all current counts (studies, observations, entities, technologies, prescience surfaces, embedding pages), see [`ARCHIVE_STATS.md`](../ARCHIVE_STATS.md).**

## Prescience surfaces (unchanged semantics)

Three surfaces in `v_studies`, measuring different things:
- `study_prescience_enum` — Rule-A mean verdict (holistic headline).
- `prescience_max ≥ 4` (loose, `v_studies_with_high_prescience`) — any obs scored 4–5.
- `prescience_mean ≥ 3.5` (tight) — strictest mean threshold.

Exact current counts for all three: `ARCHIVE_STATS.md`.
