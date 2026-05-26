# Aberdeen Archive Master CSV Schemas — Actual (v1)

**Date frozen**: 2026-05-26
**Source of truth**: `head -1` of each master in `/Users/scott/Desktop/Archive/archive_masters/`
**Purpose**: This is the schema reference for the wiki v1.5 rebuild. Earlier
guesses (in `references/csv-schema.md` from the wiki-builder skill) were
inaccurate on multiple columns. Trust this file.

---

## Master inventory (with row counts at v1.5)

| File | Rows | Used by wiki v1.5? |
|---|---:|---|
| `_master_studies.csv` | 1,434 | YES — drives `wiki/studies/` |
| `_master_entities.csv` | 3,207 | YES — drives `wiki/entities/` |
| `_master_technologies.csv` | 4,312 | YES — drives `wiki/technologies/` |
| `_master_observations.csv` | 23,605 | YES — embedded in study/entity/tech pages |
| `_master_prescience_scores.csv` | 2,723 | YES (NEW v1.5) — Pass C obs-level scores |
| `_known_entities.csv` | 3,300 | YES — provenance + alias enrichment |
| `_known_technologies.csv` | 4,371 | YES — provenance + alias enrichment |
| `_collection_stats.csv` | 947 | YES — aggregated to per-collection rows |
| `_master_codes.csv` | 1,293 | YES (NEW v1.5) — methodology code dictionary |
| `_master_entity_studies.csv` | 3,682 | YES — used to derive `occurrence_count` |
| `_master_tech_studies.csv` | 5,253 | YES — used to derive `occurrence_count` |
| `_master_entity_canonicalization_TODO.csv` | 141 | NO — operational |
| `_master_entity_field_conflicts.csv` | 3,711 | NO — operational |
| `_master_tech_canonicalization_TODO.csv` | 265 | NO — operational |
| `_master_tech_field_conflicts.csv` | 4,972 | NO — operational |

---

## Column schemas (column order = file order)

### `_master_studies.csv`
```
study_id, title, author, date, type, subject_domain, methodology,
source_file, abstract, license, importance, importance_rationale,
relevance, relevance_rationale, prescience, prescience_rationale
```

- `date` is ISO `YYYY-MM-DD` (e.g. `2000-01-01`). **Derive `pub_year` as `int(date[:4])`.**
- `type` is collection-like enum (e.g. `employer-record`, `aberdeen-research`, `kastner-author`, `video-transcript`, `memoir`, `dct`).
- `importance` / `relevance` / `prescience` are STRING enums: `high` | `medium` | `low` | `not-applicable`. These are study-level holistic ratings from the ingest, **distinct from** the Pass C obs-level `prescience_score` 0-5 in `_master_prescience_scores.csv`.
- `*_rationale` columns are paired one-liners explaining the rating.
- `license` is typically `CC-BY-4.0`.

### `_master_entities.csv`
```
entity_id, entity_name, entity_type, sector, status, successor,
years_active, notes
```

- `entity_name` is the canonical display name. **There is no `canonical_name` column.**
- `entity_type` examples: `company`, `person`, `industry`, `government-agency`, `consortium`.
- `status` examples: `active`, `dissolved`, `acquired`, `defunct`, `merged`.
- `successor` is the slug of the surviving entity if status ≠ active.
- `years_active` is a free-text range (e.g. `1976-`, `1968-2003`).
- **No `occurrence_count` column.** Derived from `_master_entity_studies.csv` row counts.

### `_master_technologies.csv`
```
tech_id, tech_name, category, vendor, era, lifecycle_at_study,
lifecycle_current, notes
```

- `tech_name` is canonical (no `canonical_name`).
- `category` examples: `database`, `os`, `cpu`, `protocol`, `application`, `framework`.
- `vendor` is an `entity_id` (cross-references `_master_entities.csv`) or blank.
- `era` examples: `mainframe`, `mini`, `pc`, `client-server`, `web`, `cloud`, `mobile`, `ai`.
- `lifecycle_at_study` / `lifecycle_current` enum: `emerging`, `growing`, `mature`, `declining`, `obsolete`.
- **No `occurrence_count`.** Derived from `_master_tech_studies.csv`.

### `_master_observations.csv`
```
obs_id, study_id, entity_id, tech_id, observation_type, year_observed,
metric_name, metric_value, confidence, verification_method,
methodology_code, source_page, notes, collection, thread_tag, section,
legacy_obs_id
```

- `obs_id` format: `<study_id>-OBS-NNN`.
- `entity_id` and `tech_id` are EITHER populated, neither, or both (observation can attach to either dimension).
- `year_observed` is `int` (e.g. `2003`); can differ from study `pub_year`.
- `metric_value` is the free-text payload.
- `confidence` enum: `high` | `medium` | `low`.
- `methodology_code` links to `_master_codes.csv`.
- `legacy_obs_id` preserves pre-v20 obs_id values (Universal Normalizer trail).

### `_master_prescience_scores.csv` (NEW v1.5)
```
obs_id, study_id, model, prescience_score, confidence, rationale,
scored_at, scorer_version, source_pass, elapsed_sec, parse_ok
```

- `prescience_score` integer `0..5` (0=non-predictive, 5=highly prescient).
- `confidence` integer `1..3` (1=low/cloud-sweep needed, 3=high).
- `source_pass` enum: `pass_c` | `cloud_review`.
- Joins to `_master_observations.csv` on `obs_id`.

### `_known_entities.csv`
```
entity_id, entity_name, entity_type, sector, status, successor,
years_active, notes, source_studies
```

- Superset of `_master_entities.csv` — entities ever seen, with a `source_studies` semicolon-joined list of where they first appeared.

### `_known_technologies.csv`
Same as `_known_entities.csv` shape, technologies version.

### `_master_codes.csv` (NEW exposure in v1.5)
```
code_id, code_type, label, definition
```

- `code_type` examples: `technology-category`, `methodology`, `observation-type`, `confidence-level`, `verification-method`, `lifecycle-state`.
- `code_id` is the slug-form used by other masters (e.g. `_master_observations.csv`'s `methodology_code` column).
- `label` is the human display string; `definition` is one sentence.

### `_master_entity_studies.csv`
```
entity_id, study_id
```
Two-column join table. Used to derive `occurrence_count` per entity = count distinct study_id per entity_id.

### `_master_tech_studies.csv`
```
tech_id, study_id
```
Same shape, technology side.

### `_collection_stats.csv`
```
collection, study_id, title, date, author, n_entities, n_technologies,
n_observations, n_codes, importance, relevance, prescience
```

- **Per-study rows, not per-collection.** Each study can appear in multiple
  collections.
- Aggregate to per-collection counts for the wiki collection overviews:
  `GROUP BY collection → COUNT(study_id) AS study_count, SUM(n_entities), ...`

---

## Derived columns we materialize in Phase 1

| Column | Derived from | Carried in staging parquet |
|---|---|---|
| `studies.pub_year` (int) | `studies.date` first 4 chars | YES |
| `entities.occurrence_count` (int) | `_master_entity_studies.csv` group by entity_id | YES |
| `technologies.occurrence_count` (int) | `_master_tech_studies.csv` group by tech_id | YES |
| `studies.prescience_max` (float) | obs-level scores joined on study_id, max | YES |
| `studies.prescience_mean` (float) | obs-level scores joined on study_id, mean | YES |
| `studies.prescience_obs_count` (int) | count obs with score per study | YES |
| `observations.prescience_score` (float) | join `_master_prescience_scores.csv` on obs_id | YES |
| `observations.prescience_confidence` (int) | same join | YES |
| `observations.prescience_rationale` (str) | same join | YES |
| `collection_stats_agg` (table) | `_collection_stats.csv` GROUP BY collection | YES (new parquet) |

---

## Naming cleanup (v1.5)

To avoid confusion between the two prescience signals:

- **Study-level enum** (`high`/`medium`/`low`/`not-applicable`):
  carried as `study_prescience_enum` and `study_prescience_rationale`.
  These come from the original ingest, study-as-a-whole rating.
- **Obs-level numeric** (`0..5`, with confidence `1..3`):
  carried as `prescience_score`, `prescience_confidence`,
  `prescience_rationale` on observations; aggregated to
  `prescience_max`/`mean`/`obs_count` on studies.

Both surface in the wiki — study-level enum in frontmatter, obs-level numerics
in frontmatter AND in `_prescient.md` index AND in DuckDB.
