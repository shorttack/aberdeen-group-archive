# Kastner IT Research Archive — Decisions Log

This file records curatorial decisions, data-hygiene actions, and structural choices made during the life of the archive. Entries are appended; nothing is rewritten in place. Each entry is timestamped and references the tarball backup taken before any mutation.

Companion files:
- [`README.md`](./README.md) — archive overview and quickstart
- [`CHANGELOG.md`](./CHANGELOG.md) — semver release history (if present)
- This file — full curatorial reasoning behind those releases

---

## v1.4 — 2026-05-23 / 2026-05-24

**Theme**: Weekend ingest of 490 new studies, two data-hygiene fixes, companion-wiki build.

### 2026-05-24 17:30 EDT — "32 missing studies" investigation: closed, none missing

**Context.** During v1.4 planning, the operator flagged "32 missing studies" as an open item from the 2026-05-23 ingest. Investigation across all seven bucket logs (mode1 buckets A–E, mode2 existing, phase1 progress) found **36 lines matching `FAIL|ERROR`**. Detailed inspection showed **all 36 are MuPDF library warnings** of the form:

- `MuPDF error: format error: cmsOpenProfileFromMem failed` — cosmetic ICC color-profile warning
- `MuPDF error: format error: No default Layer config` — optional-content layer warning

Both are non-fatal stderr messages emitted by MuPDF when *opening* a PDF; text extraction proceeds normally afterward. Counts by bucket:

| Bucket | total "error" lines | MuPDF noise | real errors |
|---|---:|---:|---:|
| A | 2 | 2 | 0 |
| D | 24 | 24 | 0 |
| E | 10 | 10 | 0 |

**No Python tracebacks, no exceptions, no `failed to process` lines across any log.**

**Disposition.** All 494 prepared folders ingested successfully (493 OK + 1 not-ready). The "32" was a phantom count; no studies are missing. Investigation closed. No action taken.

### 2026-05-24 13:00 EDT — Case-collision merge across entity & technology masters

**Context.** During v1.4 master regeneration we detected duplicate slug rows differing only in case (e.g. `JAVA` vs `java`, `Sun Microsystems` vs `sun microsystems`). The pre-merge masters had 1,443 studies; the deduped run produced 1,434 — a 9-row reduction.

**Action.** A case-folding merge was performed on the entity and technology caches; the canonical form (typically the first-seen capitalization or the one already in the deduped cache) was kept. The collision merge produced the following master counts:

| File | Pre-merge | Post-merge | Δ |
|---|---:|---:|---:|
| `_master_studies.csv` | 1,443 | 1,434 | −9 |
| `_master_entities.csv` | — | 3,207 | — |
| `_master_technologies.csv` | — | 4,313 | — |
| `_master_observations.csv` | — | 23,605 | — |

**Backup**: pre-merge tarball captured in the standard masters tarball cadence (`archive_masters_tarball`).

**Verify-then-write status.** ✅ Confirmed downstream. The vault built from the cleaned masters disambiguates remaining case-similar pairs at the slug layer (e.g. `java.md` / `java-2.md`) per the v3/v4 vault builder.

### 2026-05-24 19:38 EDT — Java/PDA carve-out (Option A: merge `java` → `JAVA`, drop misfiled row)

**Context.** The case-merge surfaced a second-order problem: `_master_technologies.csv` contained a row with `tech_id="java"` whose body content was clearly Java programming-language data (vendor "Sun Microsystems / Oracle", era "1.0 (initial release 1995)", notes citing Java 21 LTS) — but whose `tech_name` field said **"PDA (personal digital assistant)"**. The misfile likely originated upstream of master regeneration (an entity- or technology-extraction step that crossed a wire when two distinct tech rows were merged).

A separate `tech_id="JAVA"` row (uppercase) already existed in the master, correctly labeled "Java Programming Language", and is the canonical Java entry. PDA is already represented as `tech_id="pda"`, `tech_id="pda-hardware"`, and `tech_id="pda-mobile-devices"`.

**Option chosen: A — merge `java` → `JAVA` across reference tables, drop the misfiled row.** Rationale: creating a corrected lowercase `java` row would re-introduce a case collision identical to the one just merged. The uppercase `JAVA` row already contains the canonical Java metadata; the misfiled row's content is redundant with it.

**Script**: `fix_java_pda_carveout_v1.py` (dry-run-then-write; tar backup before any mutation; atomic .tmp+rename writes).

**Pre-mutation backup**: `/Users/scott/Desktop/Archive/archive_masters_backup_pre_java_fix_20260524_193807.tar.gz` (5.2 MB).

**Action.** 91 rows re-pointed and 1 row dropped:

| File | lowercase `java` rows pre | uppercase `JAVA` rows pre | post-merge upper count | dupe rows collapsed |
|---|---:|---:|---:|---:|
| `_master_observations.csv` | 54 | 2 | 56 | 0 |
| `_master_tech_studies.csv` | 28 | 1 | 29 | 0 |
| `_master_tech_field_conflicts.csv` | 7 | 0 | 7 | 0 |
| `_known_technologies.csv` | 1 | 1 | 1 | 1 |
| `_master_technologies.csv` | 1 (dropped) | 1 (kept) | 1 | — |

Master technology row count: **4,313 → 4,312**.

**Verify-then-write status.** ✅ Post-write greps confirm:
- 0 rows in `_master_technologies.csv` matching `^"java",`
- 1 row matching `^"JAVA",`
- 0 residual `"PDA (personal digital assistant)"` strings in `_master_technologies.csv`
- File line count = 4,313 (4,312 data rows + 1 header)

### 2026-05-23 / 2026-05-24 — Weekend bucket ingest (+490 studies)

**Mode**: Bucket-classifier-driven ingest using `archival-ingest` skill v20.

**Buckets processed**:
- mode1 buckets A, B, C, D, E (new material classified by content type)
- mode2 existing (re-evaluation of already-archived material)

**Disposition** (494 prepared folders): 493 OK + 1 not-ready. See "32 missing studies" entry above for the full investigation of the apparent fail count.

**Physical landing**: 493 of the 494 new studies are physically located in `prepared/` as of v1.4 release, fully registered in the masters and indexed in the companion wiki but not yet classified into `kastner-author/`, `other-authors/`, or `employer/*` subtrees. Promotion is a **v1.5 backlog item**.

**Prescience scoring**: All 370 of the newly-ingested studies marked as `[DEFERRED]` in `prescience` pending the Pass C scoring run, also a **v1.5 backlog item**.

### 2026-05-24 — Companion wiki (Kastner Aberdeen Wiki) v3/v4 build

**Output**: 8,960-page Obsidian vault at `../kastner_wiki/` (relative to `aberdeen-group-archive/`).

**Pages**:
- 1,434 study pages
- 3,207 entity pages
- 4,313 tech pages
- + index, dashboard, README, AGENTS.md, chat-starter.md, Bases

**Wikilinks**: 3,682 study→entity links + 5,253 study→technology links (emitted explicitly by the v4 builder so Dataview reverse-lookups work on entity and technology pages).

**Builder skill**: `kastner-wiki-builder` (custom user skill). v3 introduced explicit study→entity/tech wikilink emission; v4 removed empty Dataview blocks for observations (no observation pages exist in the vault) and replaced them with obs counts plus DuckDB SQL hints.

**Slug disambiguation**: One case-collision survived to the wiki layer and was disambiguated at slug emission time: `java.md` (Java Programming Language, the surviving uppercase `JAVA` master row) and `java-2.md` (a remnant pointing at PDA content prior to the master fix). The `java-2.md` page will resolve correctly on the next vault rebuild after a fresh DuckDB load against the v1.4 masters (deferred Pass C work).

**Backup**: `/Users/scott/Desktop/Archive/kastner_wiki_backup_v1.4_20260524_193848.tar.gz` (2.1 MB, 8,985 tarball entries = 8,960 pages + directories).

**DuckDB state at v1.4**: DuckDB build trails masters by one generation (still shows 3,242 entities / 4,337 techs). Per operator decision this is acceptable — the vault was built from the cleaned masters, and Pass C scoring (v1.5) will trigger a natural DuckDB rebuild against the v1.4 masters.

---

### 2026-05-25 — Model selection for Bucket A Pass C prescience scoring

**Decision**: Qwen 3.5 27B-MLX, run locally on M4 Pro Mac mini, is the production scorer for Bucket A Pass C prescience scoring. 35B-MLX dropped from production; cloud (Claude Sonnet 4.6) retained as low-confidence reviewer only.

**Method**: Two-phase evaluation. Phase 1 — speeds-and-feeds web research confirmed both Qwen MLX variants viable on 48 GB unified memory. Phase 2 — three-way calibration on `ra-warehouseautomation-3867-89c99f` (93 obs / 68 scoreable) with identical rubric and locked generation parameters (`think: false`, `keep_alive: 30m`, `num_ctx: 8192`, `num_predict: 400`).

**Decisive evidence**: 27B agreed with cloud at Cohen's kappa **0.853** (near-perfect) and **100% within-1 agreement**. 35B agreed with cloud at kappa **0.515** (moderate) and inflated four non-claims (OBS-057, OBS-074, OBS-087, OBS-091) as scoreable — a discipline failure that would corrupt prescience rankings across 124 studies. 35B's 5.2× speed advantage was insufficient to overcome the quality gap.

**Full memo**: [`model_prescience_scoring_finding_v1.md`](./model_prescience_scoring_finding_v1.md) — methodology, per-model stats, pairwise agreement tables, reproducibility manifest, caveats.

**Calibration artifacts** (preserved at `prepared/ra-warehouseautomation-3867-89c99f/working/`):
- `prescience_scores_qwen3_5_27b-mlx_v1.csv`
- `prescience_scores_qwen3_5_35b-mlx_v1.csv`
- `prescience_scores_cloud_v1.csv`
- `comparison_summary_v1.md`, `comparison_table_v1.csv`, `calibration_log_v1.jsonl`

**Production parameters locked in**: `run_prescience_calibration_v3.py`, `ollama_qwen_install_runbook_v1.md` (Nov 2026 refresh checklist included), `CALIBRATION_README_v1.md`.

---

## Versioning conventions

- All mutation scripts versioned `_v1`, `_v2`, … from creation; bump on every revision.
- Every mutation is preceded by a tar backup of the affected directory, named with timestamp and reason.
- Verify-then-write: every script supports dry-run; commits are gated behind `--write` or equivalent.
- Atomic CSV writes: `.tmp` file + `os.replace()`; never edit in place.
- Excel is not trusted for CSV edits in this archive — Python with `csv.writer(quoting=QUOTE_ALL)` is the only sanctioned write path (per §16.5 of the ingest skill).

## 2026-05-25 · year_observed backfill (Pass 1: copyright anchor)

**Trigger:** Pete's observation that "the original Aberdeen text will have a
year next to Copyright at the end of document." This is the strongest
date signal available locally and does not require LLM inference.

**Scope (Pass 1):**
* Column: `_master_observations.year_observed`
* Pre-state: 3,153 / 23,605 rows missing (13.4%)
* Confidence band selected: `very_high` only (copyright-year anchor matched
  in last 5 KB of `prepared/<study_id>/source/original_text.md`)
* Rows updated: **698**
* Post-state: 2,455 / 23,605 rows still missing (10.4%)

**Method:**
1. `extract_missing_dates_v3.py` scanned all observation-bearing studies
   for `Copyright YYYY [...] Aberdeen` (or looser `(c) YYYY` / `© YYYY`)
   in the document tail. Produced `proposed_year_observed_v3.csv` with
   per-row candidates and confidence ladder.
2. Pete manually spot-checked `very_high` rows in Excel and confirmed
   the regex was honest (no false positives from quoted vendor logos
   or other in-body copyright notices).
3. `apply_year_observed_v1.py` ran in two stages: preview-only first
   (zero master changes), then `--apply` with backup + atomic write.

**Provenance tag on updated rows:**
`local_date_extraction_v3_copyright_anchor`

**Audit:**
* Backup: `archive_masters_pre_year_observed_apply_20260525_211909Z/_master_observations.csv`
* Audit log: `v1.5_workspace/year_observed_apply_audit_v1.csv`
  (columns: obs_id, old_value, new_value, study_id, source_snippet,
   provenance_tag, applied_at_utc)
* Rollback (if ever needed):
  `cp <backup_path> <masters_path>`

**Confidence ladder (preserved for future passes):**

| Label | Definition | Rows | Status |
|---|---|---|---|
| very_high | Copyright-year anchor matched at study tail | 698 | **APPLIED 2026-05-25** |
| high | Year in same sentence as observation_text anchor, multiple hits | 941 | Pending Pass 2 |
| medium | Year in same sentence as anchor, single hit | 1,058 | Pending Pass 2 |
| low | Most-common year in doc, no anchor proximity | 207 | Pending Pass 3 (manual) |
| none | No year found, or source file missing | 249 | Pending Pass 3 (manual / from PDF) |

**Next decision point:** Pass 2 strategy for the `high` + `medium` rows
(~1,999). Options under consideration:
* Stricter regex requiring near-anchor + within sentence-of-claim
* LLM-assisted review against the source snippet
* Manual Excel pass

**Forever-archive note:** The 698 rows now carry both the new
`year_observed` value AND, via the audit log, the evidence snippet and
provenance tag that produced them. Future researchers can always
verify provenance.
---

## 2026-05-25 — Bucket A Pass C Kickoff Scope & Schema (v1.5)

**Decision recorded by**: Pete Kastner (Adoptex LLC) with Computer
**Status**: Locked — kickoff cleared
**Cross-references**: `model_prescience_scoring_finding_v1.md`,
`bucket_a_model_decision_template_v1.md`, `pass_c_kickoff_runbook_v1.md`

### Scope

Bucket A Pass C is defined as **every study directory under
`/Users/scott/Desktop/Archive/prepared/`** that contains a
`data/observations.csv` file. No further filter by study_type or naming
convention — the prepared/ directory is the authoritative selector.

Expected scope: ~124 studies, ~70–100 scoreable observations per study after the
non-claim pre-filter.

### Pre-filter (frozen)

The pre-filter that ran during calibration is now codified in
`scripts/pre_filter_scoreable_obs_v1.py`. Rules (no changes vs calibration):

- empty/whitespace metric_value → skip "empty"
- <40 chars after stripping markdown wrappers → skip "too_short(Nchars)"
- markdown header (^# / ^## / etc.) → skip "markdown_header"
- bare bold wrapper with no period → skip "bold_header_no_sentence"

### Production scorer (frozen by Finding memo)

Model: **qwen3.5:27b-mlx** (local Ollama, M4 Pro)
Generation params: `think=false`, `keep_alive=30m`, `num_ctx=8192`,
`num_predict=400`, `temperature=0.2`
Prompt: `prescience_score_prompt_v2.md` (unchanged from calibration)

### Cloud reviewer (async)

Rows where 27B reports `confidence == 1` are routed asynchronously to cloud
(Claude) for a second-pass score, **after** Pass C completes. Mechanism:
`scripts/route_low_confidence_v1.py --build-queue` builds a work queue;
Computer (agent) processes the queue in a follow-up session and returns
results; `--apply` splits results back to per-study files. The local 45-hour
run is never blocked by cloud availability.

### Output schema (Option α — separate master)

Pass C scores land in a **new 8th master**: `_master_prescience_scores.csv`.
The existing `_master_observations.csv` (17 cols + legacy_obs_id) is **not
modified** by Pass C.

Schema (11 columns):

| Column | Type | Notes |
|---|---|---|
| `obs_id` | string | Foreign key to `_master_observations.csv` |
| `study_id` | string | Foreign key to `_master_studies.csv` |
| `model` | string | e.g. `qwen3.5:27b-mlx` or `claude-sonnet-4.6` |
| `prescience_score` | int 0–5 | empty when parse_ok=false |
| `confidence` | int 1–3 | empty when parse_ok=false |
| `rationale` | string | truncated to 2000 chars |
| `scored_at` | ISO8601 UTC | per-row timestamp |
| `scorer_version` | string | e.g. `qwen3.5:27b-mlx_passC_v1` |
| `source_pass` | string | `pass_c` or `pass_c_cloud_review` |
| `elapsed_sec` | float | per-row Ollama call wall time |
| `parse_ok` | "true"/"false" | JSON parse success |

Rationale for Option α (vs. adding columns to `_master_observations.csv`):

1. The obs master is stable and just gained the legacy_obs_id audit column at
   v1.4. Every Pass C rerun would force a full obs-master rewrite, risking
   §16.5 quoting drift.
2. Multiple scorers (27B, cloud review, future calibration reruns) all
   need to coexist; a separate prescience master holds many rows per obs_id
   cleanly via (obs_id, model, scored_at).
3. Adding Buckets B–F prescience later (different rubrics) requires no
   schema change to the obs master — they just append to the prescience
   master with different `scorer_version` values.
4. Joining is a one-line DuckDB or pandas merge on `obs_id`.

### Checkpointing & crash recovery

`scripts/run_prescience_pass_c_v1.py` maintains
`/Users/scott/Desktop/Archive/prepared/pass_c_checkpoint_v1.json` with:
`completed_studies[]`, `in_progress {study_id, last_obs_idx}`,
`started_at`, `last_update`, `total_obs_scored`, `total_parse_failures`,
`scorer_version`.

Restart behavior: skip completed studies, resume in-progress study from
`last_obs_idx + 1`. Per-study CSV is incrementally flushed every 5 obs to
disk via QUOTE_ALL atomic write.

### Thermal management

`--throttle-every 10 --throttle-seconds 5` (defaults). 5-second pause every
10 observations to give the M4 Pro thermal envelope room across the
~45-hour run. Tunable per Pete's preference.

### Success criteria

1. ≥95% of scoreable observations across all studies produce parse_ok=true
2. Checkpoint advances monotonically (no regressions)
3. No data loss on simulated crash (kill -9 mid-study, restart, no
   duplicate or missing scores)
4. `_master_prescience_scores.csv` round-trips through DuckDB and the
   wiki rebuild without quoting errors
5. Mean elapsed_sec per obs stays within 1.5× of calibration baseline
   (15.35 s) sustained over 8+ hours

### Estimated wall clock

Calibration: 15.35 s/obs at 68 obs = ~17.5 min/study
Projected for 124 studies × ~75 scoreable mean = ~9,300 obs
At 15.35 s/obs + 5 s throttle every 10 = ~16 s/obs effective
= ~9,300 × 16 / 3600 = **~41 hours pure compute**

Add ~10% buffer for thermal slowdown and resume overhead → **~45 hours**.

### Forever-archive notes

This decision memo is a forever-archive document. The Finding memo
(`model_prescience_scoring_finding_v1.md`) explains *why* 27B; this entry
explains *how* Pass C is operationalized. If the schema is later changed,
preserve the v1 master file alongside the new one and append a new entry
here — never overwrite.



## 2026-05-25 — Pass C scope narrow: Bucket A + B only

**Context.** The `pre_filter_scoreable_obs_v1.py` dry-run across
`/Users/scott/Desktop/Archive/prepared/` returned **494 studies / 3,833 total
observations / 3,253 scoreable** — far larger than the planned ~124-study
scope. At 16 s/obs effective throughput on `qwen3.5:27b-mlx`, an all-buckets
run is ~14.5 hrs of dedicated compute. More importantly, it would score
non-report material (press releases, TOCs, research agendas) where prescience
scoring is not meaningful.

**Decision.** Restrict Pass C to **Bucket A (benchmark reports, 20-30pp) and
Bucket B (executive summaries, 2-6pp)** — the observation-dense report
formats curated by the operator at ingest time. Buckets C / D / E (press
releases, TOCs/indexes, research agendas/calendars) are **excluded** from
prescience scoring.

**Source of truth.** Each prepared study's `manifest.json` carries the
operator-assigned `bucket` field (written by `prepare_for_ingest.py --bucket
A|B|...`). Pass C reads this field — not the classifier's `predicted_bucket`
— to determine inclusion.

**Implementation.**
- New script: `pre_filter_scoreable_obs_v2.py` adds `--bucket-filter A,B`.
- v2 emits a new `_bucket_audit_v2.csv` at the root of `prepared/` listing
  every study with its assigned bucket, predicted bucket, kept-or-not,
  observation counts, and `no_manifest` flag.
- `working/scoreable_obs_v1.csv` filenames are unchanged so the v1 Pass C
  runner (`run_prescience_pass_c_v1.py`) needs no modification — it simply
  encounters only Bucket A+B studies because Buckets C/D/E never get their
  `scoreable_obs_v1.csv` regenerated.

**Studies without a manifest** (`UNKNOWN` bucket) are filtered out and
flagged for manual review in `_bucket_audit_v2.csv`. This is a forever-
archive principle — never silently include or exclude. Operator decides
whether to back-fill manifests or accept exclusion.

**Estimated cost.** TBD after the v2 audit dry-run on the Mac. Working
estimate: 1,800-2,200 scoreable obs → ~8-10 hrs at 16 s/obs.

**Reversal cost.** Zero. Adding a bucket back later is one re-run of v2 with
a wider `--bucket-filter` — observations are immutable, scoring is additive
to `_master_prescience_scores.csv`.

**Files committed this round.**
- `scripts/pre_filter_scoreable_obs_v2.py`
- `scripts/pre_filter_scoreable_obs_v2_README.md`
- Appended this entry to `_decisions_log.md`
