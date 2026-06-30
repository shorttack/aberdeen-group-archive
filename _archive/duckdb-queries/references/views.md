# kastner.duckdb — 27 views

All `main.<name>`, all VIEW, all read-only. Verified 2026-06-27 via the
`Perplexity bridge v2` connector `duckdb_tables`. Use `duckdb_describe <view>`
(connector) or `DESCRIBE <view>` (CLI) to see columns before querying.

## Core entities
- `v_studies` — one row per study; the spine. Baseline COUNT ≈ 1454.
- `v_observations` — extracted observations across all studies.
- `v_entities` — companies/people/orgs referenced.
- `v_technologies` — technologies referenced.
- `v_codes` — methodology / classification codes.

## Counts & enrichment
- `v_entities_with_observation_count` — entities with their observation tallies.
- `v_observations_by_year` — observations bucketed by year.
- `v_studies_by_decade` — studies bucketed by decade.

## Prescience layer
- `v_top_prescient_studies` — ranked most-prescient studies.
- `v_studies_with_high_prescience` — studies above the high-prescience threshold.
- `v_studies_with_prescience` — studies joined to their prescience scores.
- `v_observations_with_prescience` — observations joined to prescience.
- `v_high_holistic_prescience` — high holistic-prescience rows.
- `v_holistic_prescience_distribution` — distribution of holistic prescience.
- `v_low_confidence_prescience` — low-confidence prescience rows (audit/QA).
- `v_prescience_raw` — raw prescience scores.
- `v_prescience_by_decade` — prescience aggregated by decade.

## Relationship (M:N) views
- `v_entity_studies` — entity ↔ study pairs.
- `v_tech_studies` — technology ↔ study pairs.

## Known-set sidecars
- `v_known_entities` — canonical known-entity registry.
- `v_known_technologies` — canonical known-technology registry.

## Code / classification views
- `v_codes_by_type` — codes grouped by type.
- `v_methodology_codes` — methodology codes.
- `v_technology_category_codes` — technology-category codes.

## Technology lifecycle
- `v_technologies_by_lifecycle` — technologies grouped by lifecycle stage.

## Collection overview
- `v_collection_overview` — high-level collection summary.
- `v_collection_stats` — per-collection statistics.

Notes:
- `v_studies` exposes `study_prescience_enum` / `study_prescience_rationale`
  (authored enum preserved by Phase 1).
- For bucket TYPE on studies the column is `type`, NOT `collection_type`.
