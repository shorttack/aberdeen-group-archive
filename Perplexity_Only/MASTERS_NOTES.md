# MASTERS_NOTES.md — Permanent Archive Notes (v2)

This file documents the conventions, history, and known gotchas of the
master CSV files at `~/Desktop/Archive/archive_masters/`. Keep it
adjacent to the masters; it is the authoritative reference for anyone
(human or agent) who needs to understand how the data is structured.

> **READ THIS FILE BEFORE TOUCHING ANY MASTER CSV.** Every agent context
> loading skill or starting a new day MUST consult this document first.
> The master schemas DIFFER from the per-study schemas documented in the
> `archival-ingest` v20 skill — assuming they match has caused multiple
> failed apply scripts (the most recent example: 2026-06-12 §11u-cont
> v1 apply script crashed because it assumed per-study 9-col entities
> would merge into a 9-col master, when the master is 8-col + a separate
> M:N join table).

**Last updated:** 2026-06-12, after Pass B transcript merge (§11u-cont).
**Supersedes:** MASTERS_NOTES.md v1 dated 2026-05-24 (which documented
a stale schema before the 2026-05-26 M:N refactor).

---

## The seven masters

Yes, seven — not five. The 2026-05-26 refactor split the entity-study
and tech-study relationships into separate M:N join tables, deduplicating
entities and technologies at the same time. MASTERS_NOTES v1 documented
only the pre-refactor five-table model and was the proximate cause of
the 2026-06-12 v1 apply script crash.

| File | Rows (2026-06-12) | Cols | Primary key | Notes |
|---|---|---|---|---|
| `_master_studies.csv` | 1,452 | 16 | `study_id` | One row per ingested study |
| `_master_entities.csv` | 3,276 | 8 | `entity_id` (globally unique) | Entities deduplicated across studies; NO `study_id` column |
| `_master_technologies.csv` | 4,361 | 8 | `tech_id` (globally unique) | Technologies deduplicated across studies; NO `study_id` column |
| `_master_observations.csv` | 23,926 | 17 | `obs_id` (globally unique) | Each obs belongs to one study via `study_id` column |
| `_master_codes.csv` | 1,293 | 4 | `code_id` | Codes are **global** — no study_id column |
| `_master_entity_studies.csv` | 3,876 | 2 | `(entity_id, study_id)` | **M:N join table** — entity↔study pairs |
| `_master_tech_studies.csv` | 5,375 | 2 | `(tech_id, study_id)` | **M:N join table** — tech↔study pairs |

Two additional support files alongside the masters (not authoritative,
but referenced by Phase 1 of the build pipeline):

| File | Rows | Cols | Purpose |
|---|---|---|---|
| `_master_prescience_scores.csv` | 3,761 | 11 | Per-observation prescience scoring (Pass C output) |
| `_master_collection_stats.csv` | 947 | 12 | Per-study collection statistics |

And the cross-session reuse caches (NOT in master schema, but referenced
during ingest):

| File | Rows | Cols | Purpose |
|---|---|---|---|
| `_known_entities.csv` | 3,300 | 9 | Cross-study entity reuse cache (HAS study_id) |
| `_known_technologies.csv` | 4,371 | 9 | Cross-study tech reuse cache (HAS study_id) |

> **Critical distinction:** `_known_entities.csv` (the reuse cache) HAS a
> `study_id` column because it tracks first-seen-in-study. The master
> `_master_entities.csv` does NOT have `study_id` — it's deduplicated.
> The M:N relationships are in `_master_entity_studies.csv`.

---

## Header schemas (CANONICAL — agents must match these exactly)

### `_master_studies.csv` — 16 columns

```
study_id, title, author, date, type, subject_domain, methodology,
source_file, abstract, license, importance, importance_rationale,
relevance, relevance_rationale, prescience, prescience_rationale
```

### `_master_entities.csv` — 8 columns (no study_id)

```
entity_id, entity_name, entity_type, sector, status, successor,
years_active, notes
```

### `_master_technologies.csv` — 8 columns (no study_id)

```
tech_id, tech_name, category, vendor, era, lifecycle_at_study,
lifecycle_current, notes
```

### `_master_observations.csv` — 17 columns (v20 superset)

```
obs_id, study_id, entity_id, tech_id, observation_type, year_observed,
metric_name, metric_value, confidence, verification_method,
methodology_code, source_page, notes, collection, thread_tag, section,
legacy_obs_id
```

Four columns extend beyond the 12-column per-study `observations.csv`:

- `verification_method` — added by Pass A v1 (§17 of archival-ingest); see ID conventions below
- `collection` — inherited from the parent study's collection type (`transcript`, `dct`, `memoir`, etc.)
- `thread_tag` — preserved from legacy column promotion (Section 19.4 of archival-ingest)
- `section` — free-text section/heading reference from source document
- `legacy_obs_id` — audit-trail column added by §21 obs_id Universal Normalizer on 2026-05-24

### `_master_codes.csv` — 4 columns

```
code_id, code_type, label, definition
```

### `_master_entity_studies.csv` — 2 columns (M:N join)

```
entity_id, study_id
```

### `_master_tech_studies.csv` — 2 columns (M:N join)

```
tech_id, study_id
```

All masters are written with `csv.QUOTE_ALL` and UTF-8 (§16.5 of the
`archival-ingest` skill). Use Python's `csv.DictReader` or `csv.reader`
to read them — `awk -F,` will mis-parse rows with commas inside quoted
fields.

---

## Per-study CSVs differ from master schemas

This is the gotcha that broke `apply_passb_transcripts_v1.py` on
2026-06-12. **Per-study CSVs and master CSVs have different schemas:**

| Table | Per-study CSV (in `<study_id>/data/`) | Master CSV |
|---|---|---|
| studies | 16 cols | 16 cols (identical) |
| entities | **9 cols** (includes `study_id`) | **8 cols** (no `study_id`) |
| technologies | **9 cols** (includes `study_id`) | **8 cols** (no `study_id`) |
| observations | **12 cols** | **17 cols** (5 master-only) |
| codes | 4 cols | 4 cols (identical) |

When merging per-study CSVs into the masters, the correct flow is:

1. **Entities** — for each new `entity_id` not in `_master_entities.csv`, append a row with the 8-col schema (drop `study_id`). Always append the `(entity_id, study_id)` pair to `_master_entity_studies.csv`.
2. **Technologies** — same pattern as entities.
3. **Observations** — promote 12-col → 17-col by adding `verification_method` (default `ingest-extraction`), `collection` (inherit from study), and empty `thread_tag`, `section`, `legacy_obs_id`.

The reference apply script that does this correctly is
`scripts/apply_passb_transcripts_v2.py` in the archive repo (2026-06-12,
[commit 0391dabf](https://github.com/shorttack/aberdeen-group-archive/commit/0391dabf6cc67df77f81cd3af7c9b131c448a67e)).
Use it as a template for any future batch merge.

---

## ID conventions (CANONICAL as of v20 §21)

### Canonical observation ID format

**`<study_id>-OBS-NNN`** — uppercase `OBS`, hyphen separators, 3-digit
zero-padded suffix. The §21 obs_id Universal Normalizer (ran 2026-05-24)
unified all legacy variants into this shape.

Examples:
- `cnbc-sars-electronics-supply-chain-impact-92deff-OBS-001`
- `informix-universal-server-launch-object-relational-fb2cd4-OBS-053`
- `dec-blue-monday-internal-sales-training-dectp-vs-ibm-0021cc-OBS-042`

Letter-suffix variants (`-OBS-NNNa`) are valid for legacy clones but
NEVER generated for new observations. The §21 normalizer maps 13 legacy
shapes into the canonical format — see §21 of `archival-ingest` v20 for
the full bucket catalog.

### Canonical entity / tech ID format

**Lowercase, hyphen-separated, single global namespace.** No `OBS`-style
serial suffix; entities and techs are deduplicated across studies.

Examples:
- `peter-s-kastner`, `aberdeen-group`, `dec`, `ibm`, `oracle-corporation`
- `enterprise-application-integration-eai`, `client-server`, `tpc-c`

The reuse cache (`_known_entities.csv`, `_known_technologies.csv`) is
the source of truth for canonical IDs during ingest. Always check the
cache first; never generate a new entity_id for a known entity.

### Legacy obs_id formats (still readable)

Pre-§21 observation IDs in 13 legacy shapes (bare numeric, T-prefix,
S-prefix, D-prefix, OBS-prefix-no-study, etc.) have all been rewritten
by the v20 §21 normalizer. The original value is preserved in the
`legacy_obs_id` column for audit. Currently:

- 21,527 of 23,926 obs_ids are in canonical `<study_id>-OBS-NNN` form
- 2,399 remain in non-canonical legacy form (pre-§21, deferred to future normalizer pass)

If you ever see a non-canonical obs_id in newly-ingested data, **the
ingest pipeline is generating wrong IDs** — fix the source before
running the normalizer again.

---

## Code conventions

`code_id` values are lowercased, hyphen-separated tokens. The cleanup
script enforces:

- Lowercase (`ABERDEEN-SURVEY` → `aberdeen-survey`)
- Whitespace runs collapse to a single hyphen
- Multiple consecutive hyphens collapse to one
- Leading/trailing whitespace stripped
- Rows whose `code_id` (after stripping) starts with a non-alphanumeric
  character are **dropped as garbage**
- Rows whose `code_id` contains structural punctuation (`()[]{}<>;:!?"'`)
  are dropped as garbage
- For each canonical `code_id`, the row with the **longest definition** is
  kept; ties broken by longest label

`methodology_code` in observations is a foreign key into `codes.code_id`
and is canonicalized in the same way. A non-empty `methodology_code` in
observations that has no matching row in `codes` is an FK orphan — the
verify step will flag it.

---

## Referential integrity

After any merge, all foreign keys must resolve:

- `observations.entity_id` matches `entity_id` in `_master_entities.csv`, OR is empty
- `observations.tech_id` matches `tech_id` in `_master_technologies.csv`, OR is empty
- `observations.methodology_code` matches `code_id` in `_master_codes.csv`, OR is empty
- `observations.study_id` matches `study_id` in `_master_studies.csv`
- `_master_entity_studies.csv` `(entity_id, study_id)` pairs reference valid rows in both parent tables
- `_master_tech_studies.csv` `(tech_id, study_id)` pairs reference valid rows in both parent tables

After any batch merge, run the canonical shape audit (kastner-archive-pipeline
skill §"Shape audit") and verify zero orphans.

---

## Per-study mirrors

Every study has a per-study CSV bundle in two locations:

- **Prepared (sandbox-generated)**: `~/Desktop/Archive/prepared/<study-id>/data/{studies,entities,technologies,observations,codes}.csv`
- **Repo (committed to GitHub)**: `~/Desktop/Archive/aberdeen-group-archive/<collection>/<study-id>/data/...`

These mirrors are subsets of the masters (only rows where `study_id`
matches the directory). The schemas differ from the masters (see
"Per-study CSVs differ from master schemas" above).

> **Never edit a per-study CSV without also updating the master**, or
> your next consolidation will silently revert your changes.

---

## Locations: where each artifact lives

The archive lives across multiple paths on Pete's Mac. Confusing them is
a leading cause of agent error. Memorize this table.

| # | Path on Mac (user `scott`) | Role | Status |
|---|---|---|---|
| 1 | `~/Desktop/Archive/archive_masters/` | **Source of truth.** All 7 master CSVs live here. | **READ + WRITE here for masters edits** |
| 2 | `~/Repos/kastner-aberdeen-wiki/` | **Live working wiki.** Contains enriched parquets in `data/` and live DuckDB at `db/kastner.duckdb`. This is what `kw ask` queries. | **READ for verification; WRITTEN BY Phase 1+2** |
| 3 | `~/Desktop/kastner_wiki/` | **DELETED 2026-06-01.** Former live wiki path; migrated to `~/Repos/` to escape iCloud Desktop trap. | **DO NOT USE — does not exist** |
| 4 | `~/Desktop/Archive/aberdeen-group-archive/` | Local clone of `shorttack/aberdeen-group-archive`. Used for `git pull` to receive scripts. | **READ ONLY — never edit masters here** |
| 5 | `~/Desktop/Archive/scripts/` | Build scripts (Phase 1-6 in `build/`, one-offs at root). | **READ to execute; commit changes via repo** |
| 6 | `~/Desktop/Archive/passb_batch/` | Inbox for batch CSVs being merged into masters. | **Receives shipped batch files** |

**Verification rule**: when running any `duckdb` sanity check after a
rebuild, the path MUST be `~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb`.
The `~/Desktop/kastner_wiki/` path no longer exists. The
`~/Desktop/Archive/kastner_duckdb_build/` path produces unenriched
parquets and breaks the live wiki — never use it for masters-edit rebuilds.

---

## Technology notes conflicts

When the upstream Phase-2 consolidator detected multiple rows for the same
`(tech_id, study_id)` that differed **only** in the `notes` column, it left
them all in place. The cleanup script resolves these by keeping the row
with the longer `notes` value (richer notes = more useful).

If rows differ in non-notes fields (e.g. different `category` or `era`),
they are left alone for manual review — they represent genuine data
conflicts, not artifacts.

---

## History

| Date | Event |
|---|---|
| 2024-Q4 / 2025-Q1 | Pre-v19 ingests produced bare and pseudo-namespaced obs_ids |
| 2025-Q2 onward | v19 ingest writes globally-unique obs_ids (`<study-id>-OBS-NNN`) |
| 2026-05-23 | `run_phase2_and_masters.py` consolidated 494 study dirs into masters; 9 study dupes detected and removed |
| 2026-05-24 | `namespace_legacy_ids.py` rewrote ~500 legacy IDs, canonicalized codes (24K → ~2.2K rows), resolved tech notes conflicts, verified FK integrity |
| 2026-05-24 | §21 obs_id Universal Normalizer (`fix_v2_residuals_v3.py`) unified 13 legacy obs_id shapes into canonical `<study_id>-OBS-NNN`; added `legacy_obs_id` audit column. Backup at `archive_masters_pre_fix_v3_backup/20260524_141559/` |
| 2026-05-26 | **M:N refactor.** Entities and technologies deduplicated to global namespace; `_master_entity_studies.csv` and `_master_tech_studies.csv` join tables introduced. Reduced `_master_entities.csv` from ~11,800 rows to ~3,200; `_master_technologies.csv` from ~8,930 to ~4,300. |
| 2026-05-27 | `pub_year` backfill (v6 + v6.1) — derived from filename + date string for 1,434 studies. Phase 1+2 v4 fix: integer-divide for decade buckets (`//` not `/` — DuckDB `/` returns DOUBLE on INTEGER). |
| 2026-05-31 | Phase 5 v3 schema fix: bge-m3 embeddings emit 6-col schema `(page_path, page_type, slug, title, vector, dim)` for `kw_ask.py` compatibility (v2 had 4-col schema that crashed consumers). |
| 2026-06-01 | Live wiki migrated from `~/Desktop/kastner_wiki/` to `~/Repos/kastner-aberdeen-wiki/` to escape iCloud Desktop sync corruption. Desktop copy deleted. |
| 2026-06-11 | §11t masters reconciliation: 11 placeholder transcript rows seeded for §11u-cont Pass B batch |
| 2026-06-12 | **§11u-cont Pass B transcript merge.** 17 transcripts ingested via custom apply script. studies REPLACE (17 rows); entities APPEND (+69 of 132 unique IDs; 63 reused from cache); technologies APPEND (+49 of 98); observations APPEND (+295); entity_studies APPEND (+194 pairs); tech_studies APPEND (+122 pairs). All §16 GREEN. Backup at `archive_masters/*.csv.bak_passb_v2_*_20260612T172545Z` |

---

## Known deferred work

- **2,399 non-canonical obs_ids remain.** The §21 obs_id Universal Normalizer's 2026-05-24 run unified 21,527 of 23,926 rows; 2,399 in legacy non-canonical shapes (post-cleanup drift from cross-collection ingests) await a re-run. See `archival-ingest` v20 §21.
- **Entity canonicalization.** `DEC`, `Digital`, `Digital Equipment Corp`, and `Digital Equipment Corporation` are separate rows today. Deferred — requires controlled vocabulary or fuzzy-match pass with manual review.
- **One empty entities.csv.** Study `adp-ase-meters-75c4c2` has an empty `data/entities.csv`. Not corruption — a study that legitimately has no extracted entities — but worth re-checking the source PDF.
- **Source-page reverse lookup.** Many observations have `source_page` but no easy way to jump from a master row back to the source PDF page. Building a Bates-style index is on the wiki backlog.
- **`_llm_helper_v4.py` model pin.** Currently `qwen3.5:27b-mlx`. `qwen3.6:27b-mlx` is installed but not yet evaluated per `local-model-upgrade-gates` skill. Future-work item.

---

## See also

- `_skills/archival-ingest/SKILL.md` — v20 ingest skill; §13.1 transcripts, §16 CSV gate, §17 Pass A, §19 schema normalization, §21 obs_id Universal Normalizer
- `kastner-archive-pipeline` skill — pipeline operation (Phases 1-6, shape audit, gotchas)
- `kastner-github` skill — Git Data API patterns, EOD batch commit protocol
- `kastner-new-day` skill — session-start orientation
- `_decisions_log.md` — chronological decision history (this file's history table summarizes; the decisions log has full per-session detail)
- `WORKLIST.md` — current and recent session worklists
