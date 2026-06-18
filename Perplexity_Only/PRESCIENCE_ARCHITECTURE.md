# PRESCIENCE_ARCHITECTURE.md — The Map

> **Purpose:** the canonical reference for "what files, what schemas, what flows, what lags." Read this before touching anything prescience-related. If you cannot answer "where does this number come from" from this doc alone, the doc is wrong — fix it.

**Status:** rev2 architectural map (companion to `Archive/decisions/prescience_architecture_audit_v1.md`, the 2026-06-15 findings report). All four ship-gate findings (F2/F3/F6/F7) closed by commits `7935aec7` and `5f945dd9` on 2026-06-18; see §7.
**Audit date:** 2026-06-18 (Thursday, §11v D6). **rev2:** 2026-06-18 PM (F2/F3/F6/F7 all closed).
**Scope:** every file, script, and view that touches the `prescience` column or `_master_prescience_scores.csv`.
**Gates:** v1.7.0 ship — F2/F3/F6/F7 closed; MASTERS_NOTES v3 + RELEASE_NOTES_v1_7_0 still pending.

---

## TL;DR — the 30-second mental model

Prescience lives at **two grains** in this archive:

1. **Observation-grain scores** (1-5 + `-1` sentinel) in `_master_prescience_scores.csv`. Produced by Pass C scorers (Cloud, Sonar, Qwen). One row per scored observation.
2. **Study-grain verdict** (`high` / `medium` / `low` / `not-applicable`) in `_master_studies.csv` columns `prescience` + `prescience_rationale`. Produced by Rule A rollup OR by hand (player rebuttal).

Phase 1 of the build pipeline **joins** these two grains into `v_studies`:
- The **authored** verdict survives as `study_prescience_enum` (pass-through, NOT recomputed — see Gotcha 10 in skill).
- The **computed** rollup appears alongside as `prescience_mean` / `prescience_max` / `prescience_obs_count`.

Two ways the authored verdict gets written:

- **Path A — scorer-is-judge.** Rule A math over observation scores → write `prescience` enum → sync to repo.
- **Path B — player rebuttal.** Pete authors verdict + rationale directly, scorer math preserved alongside but ignored for the verdict.

The system has accumulated **lag points** (places where files diverge from each other in time). Section 6 enumerates them; section 7 maps the cleanup.

---

## 1. The file inventory

### 1.1 The seven masters (canonical row-level truth)

Live on Mac at `~/Desktop/Archive/archive_masters/`. Mirror at repo root (NOT under `master_csvs/`).

| File | Rows | Cols | Prescience role |
|---|---|---|---|
| `_master_studies.csv` | 1,453 | 16 | Holds `prescience` enum + `prescience_rationale` — **Path A/B output** |
| `_master_observations.csv` | 23,926 | 17 | obs_id source of truth; no score column here |
| `_master_prescience_scores.csv` | 8,440 | 11 | **Pass C output, study-attached** — one row per scored obs |
| `_master_entities.csv` | 3,276 | 8 | No prescience |
| `_master_technologies.csv` | 4,361 | 8 | No prescience |
| `_master_codes.csv` | 1,293 | 4 | No prescience |
| `_master_entity_studies.csv` / `_master_tech_studies.csv` | 3,876 / 5,375 | 2 / 2 | M:N joins; no prescience |

### 1.2 The three-file Pass C architecture (memorize this — see skill §Pass C)

| # | Path | Cols | Role |
|---|---|---|---|
| **File 1** | `~/Desktop/Archive/prescience_scores_pass_c_cloud_v1.csv` | 8 | **Live v5 output.** Read+write target. |
| **File 2** | `~/Desktop/Archive/archive_masters/_master_prescience_scores.csv` | 11 | **Study-attached master.** Append-only from File 1 via promote. **Authoritative for queries.** |
| **File 3** | `~/Desktop/Archive/aberdeen-group-archive/prescience_scores_pass_c_cloud_v1.csv` | 8 | **Repo snapshot.** Stale by hundreds of rows. Do NOT query. |

**Rule:** for scores, File 2 is canonical. For verdicts, `_master_studies.csv` (archive_masters copy) is canonical. The repo copy is downstream of both.

### 1.3 Driver and tooling scripts (`scripts/`)

Active versions only (legacy under `scripts/_legacy/` and `scripts/v3_obsolete/`):

| Script | Role | In repo? |
|---|---|---|
| `run_prescience_pass_c_v5.py` | Cloud driver (sonar-reasoning-pro) | ✓ |
| `run_prescience_pass_c_v6.py` | Tier A driver | ✓ |
| `run_prescience_pass_c_v7.py` | Tier B driver (network-hardened) | ✓ |
| `run_prescience_short_horizon_v8.py` | **SH driver (gated by this audit)** | ✓ (skeleton) |
| `prescience_acceptance_gates_v1.py` | G1-G10 gate scorer | ✓ |
| `roll_up_prescience_to_master_v3.py` | Master rollup (deprecated; see §3.3) | ✓ but `_obsolete` |
| `audit_prescience_runs_v1.py` | Run auditor | ✓ |
| `pre_filter_scoreable_obs_v4..v7.py` | Pre-filter (figure captions, etc.) | ✓ |
| `add_player_rebuttal_v1.py` | Path B authoring tool | ✓ |
| **`promote_pass_c_to_master_v1.py`** | **File 1 → File 2 append (with provenance preservation patch §11v F2)** | ✓ **F2 CLOSED 2026-06-18** ([`7935aec7`](https://github.com/shorttack/aberdeen-group-archive/commit/7935aec7b15200132c649e48e1f4632f133ae9c8)) — repo now matches Mac active copy (211 lines) |
| `sync_studies_verdicts_repo_from_archive_masters_v2.py` | archive_masters → repo verdict sync | ✓ |

### 1.4 Calibration and quality artifacts (`Perplexity_Only/`)

| File | Purpose |
|---|---|
| `prescience_calibration_sample_v1.csv` | Stratified 100-obs anchor sample (≤ 2020 cutoff) |
| `prescience_tier_a_sample_v1.csv` / `_tier_b_sample_v1.csv` | Tier sample lists for v6/v7 runs |
| `pass_c_v6_tier_a_results.csv` / `_report.md` | Tier A run output + report |
| `master_prescience_scores_DELTA_2026_05_31_to_2026_06_14.csv` | Delta audit between snapshots |
| `BULK_SCORING_RUNBOOK.md` | Operational runbook for bulk Pass C runs |
| `MASTERS_NOTES.md` | Canonical master schemas |
| `PIPELINE_QUICKREF.md` | Six-phase command cheat sheet |

### 1.5 Stray artifacts at repo root (F1 — should-fix)

- `prescience_scores_pass_c_cloud_v1.csv` (repo copy = File 3, stale)
- `readme_prescience.md` (undated, repo root — should move to `Archive/`)
- `model_prescience_scoring_finding_v1.md` (undated, repo root — should move to `Archive/decisions/`)
- `master_entities.csv`, `master_studies.csv`, `master_technologies.csv` (no `_` prefix — almost certainly stale duplicates)

---

## 2. Schemas

### 2.1 `_master_prescience_scores.csv` (File 2) — 12 columns (post-F3)

rev2 note: column #12 `row_class` added 2026-06-18 by `add_row_class_to_prescience_scores_v1.py` ([`5f945dd9`](https://github.com/shorttack/aberdeen-group-archive/commit/5f945dd97461dde813043ae3620b5b8fcfe648bd)). Backfilled from existing columns; classifier hard-fails on UNKNOWN class.

| # | Column | Type | Domain | Notes |
|---|---|---|---|---|
| 1 | `obs_id` | str | unique, non-empty | FK to `_master_observations.csv` |
| 2 | `study_id` | str | non-empty | FK to `_master_studies.csv` |
| 3 | `model` | str | `{claude-sonnet-4.6, sonar-reasoning-pro, preseed_skip_v1}` | F3 partially closed: `row_class` (col 12) is now the structural discriminator; `model` still carries `preseed_skip_v1` historically (driver v8 will write real model names + use `row_class` instead) |
| 4 | `prescience_score` | int \| empty | `{-1, 0, 1, 2, 3, 4, 5, EMPTY}` | `-1` = prefilter/parse_fail sentinel; EMPTY = preseed_skip |
| 5 | `confidence` | int \| empty | `{1, 2, 3, EMPTY}` | EMPTY only on preseed rows |
| 6 | `rationale` | str | non-empty everywhere | substantive on scored rows; tagged on prefilter/parse_fail |
| 7 | `scored_at` | ISO8601 | all 2026 | no empties |
| 8 | `scorer_version` | str | `{cloud_v1, v6}` | ⚠ F4: naming drift |
| 9 | `source_pass` | str | `{pass_c_cloud, pass_c_cloud_parse_fail, pass_c_sonar_v1, pass_c_sonar_v1_parse_fail, pass_c_prefilter_v1, preseed_b, pass_c_sh_3y, pass_c_sh_5y, pass_c_sh_parse_fail}` | F6 closed 2026-06-18: 12 cloud parse-fails retagged to `pass_c_cloud_parse_fail`. SH values reserved for driver v8. |
| 10 | `elapsed_sec` | float-str | mostly populated; 1,110 zeros | ⚠ F5: 1,106 cloud rows have `0.0` (no timing) |
| 11 | `parse_ok` | bool-str | `{true, false}` | 8,376 true / 64 false |
| 12 | `row_class` | enum | `{scored, parse_fail, prefilter_skip, preseed_skip, no_anchor, pending}` | **F3 column** — structural discriminator. Backfilled from columns 3+4+9. `no_anchor` reserved for SH driver v8 (a scored obs whose claim has no anchorable year for 3y/5y horizons). |

**Row classes (post-F3 backfill, all 6 modeled):**

| `row_class` | Expected n | Identification rule | Driver v8 SH behavior |
|---|---|---|---|
| `scored` | 8,119 | `prescience_score IN (0,1,2,3,4,5)` | Re-scored normally |
| `parse_fail` | 64 | `parse_ok='false'` (12 cloud + 52 sonar) | Re-scored normally; SH parse-fails write `source_pass=pass_c_sh_parse_fail` |
| `prefilter_skip` | 4 | `source_pass='pass_c_prefilter_v1'` (sentinel -1) | Re-prefiltered; sentinel preserved |
| `preseed_skip` | 253 | `model='preseed_skip_v1'`, score+conf empty | **F7 closed: scored normally in SH.** Long-horizon retains preseed; SH produces parallel verdict (informative disagreement expected) |
| `no_anchor` | reserved | Driver v8 marker | Skipped by SH (no year to anchor) |
| `pending` | 0 today | New obs added but not yet scored | n/a |
| **Total** | **8,440** | | |

**Backfill provenance:** see `scripts/add_row_class_to_prescience_scores_v1.py`. Backup convention `.bak_add_row_class_<utc>Z`. Hard-fails on UNKNOWN class or sum-of-classes ≠ row count.

### 2.2 `_master_studies.csv` — prescience columns

| Column | Domain | Phase 1 behavior |
|---|---|---|
| `prescience` | `{high, medium, low, not-applicable, EMPTY/'[DEFERRED]'}` | **Pass-through** — NOT recomputed from scores. The authored verdict survives. |
| `prescience_rationale` | str | Pass-through |

### 2.3 `v_studies` view (Phase 2 output, queried by `kw ask`)

Authoritative column names (verified via `DESCRIBE v_studies` 2026-06-13):

```
study_id, title, author, date, type, subject_domain, methodology,
source_file, abstract, license, importance, importance_rationale,
relevance, relevance_rationale, study_prescience_enum,
study_prescience_rationale, pub_year, prescience_max, prescience_mean,
prescience_obs_count
```

**Mapping from raw master to view (Gotcha 11):**

| Raw `_master_studies.csv` | `v_studies` |
|---|---|
| `prescience` | `study_prescience_enum` |
| `prescience_rationale` | `study_prescience_rationale` |
| `collection_type` / `type` | **`type`** (not `collection_type` — see Gotcha 12) |
| — (computed from File 2) | `prescience_mean`, `prescience_max`, `prescience_obs_count` |

**Downstream view:** `v_studies_with_high_prescience` filters on `study_prescience_enum = 'high'`. As of 2026-06-18 post-v1.6.2: **865 rows**.

---

## 3. The two paths

### 3.1 Path A — Scorer-is-judge (math-driven verdict)

```
                ┌─────────────────────────┐
                │ _master_observations.csv│ (truth: obs_id, study_id, claim text)
                └────────────┬────────────┘
                             │
                             ▼
            ┌─────────────────────────────────────────┐
            │ ~/Desktop/Archive/prepared/<study_id>/  │ (scope whitelist)
            └────────────────────┬────────────────────┘
                                 │
                                 ▼
            ┌─────────────────────────────────────────┐
            │ run_prescience_pass_c_v5.py (or v6/v7)  │
            │   • reads File 1 for already-scored      │
            │   • API call: sonar-reasoning-pro        │
            │   • writes scores + rationales           │
            └────────────────────┬────────────────────┘
                                 │
                                 ▼
            ┌─────────────────────────────────────────┐
            │ File 1: prescience_scores_pass_c_       │ (8-col live)
            │   cloud_v1.csv (~/Desktop/Archive/)     │
            └────────────────────┬────────────────────┘
                                 │ promote_pass_c_to_master_v1.py
                                 │ (append-only, dedupe on obs_id,
                                 │  --scorer-version cloud_v1
                                 │  --source-pass pass_c_cloud)
                                 ▼
            ┌─────────────────────────────────────────┐
            │ File 2: _master_prescience_scores.csv   │ (11-col study-attached)
            │   (~/Desktop/Archive/archive_masters/)  │
            └────────────────────┬────────────────────┘
                                 │ Rule A:
                                 │   used = [s for s in scores if s != -1]
                                 │   if len(used)==0:        not-applicable
                                 │   elif mean(used) >= 3.5: high
                                 │   elif mean(used) >= 2.0: medium
                                 │   else:                   low
                                 ▼
            ┌─────────────────────────────────────────┐
            │ _master_studies.csv `prescience` column │ (verdict written)
            │   (~/Desktop/Archive/archive_masters/)  │
            └────────────────────┬────────────────────┘
                                 │ sync_studies_verdicts_repo_from_
                                 │ archive_masters_v2.py --commit
                                 ▼
            ┌─────────────────────────────────────────┐
            │ Repo: _master_studies.csv (downstream)  │
            │   shorttack/aberdeen-group-archive      │
            └────────────────────┬────────────────────┘
                                 │ Phase 1 (01_load_csvs_v2.py)
                                 │   reads `prescience` AS-IS (pass-through)
                                 │   joins File 2 for mean/max/count
                                 ▼
            ┌─────────────────────────────────────────┐
            │ v_studies.study_prescience_enum          │ (live, kw ask reads here)
            │ v_studies_with_high_prescience           │
            └─────────────────────────────────────────┘
```

### 3.2 Path B — Player rebuttal (human override)

Identical to Path A through promote (scores still recorded for transparency). Then:

```
            ┌─────────────────────────────────────────┐
            │ File 2: _master_prescience_scores.csv   │ (scores recorded)
            └────────────────────┬────────────────────┘
                                 │ math says "low" — but Pete disagrees
                                 ▼
            ┌─────────────────────────────────────────┐
            │ kastner-author/notes/<study_id>_        │ (rebuttal rationale)
            │   prescience_rationale_<date>.md        │
            └────────────────────┬────────────────────┘
                                 │ Pete writes verdict + rationale
                                 │ directly into archive_masters
                                 ▼
            ┌─────────────────────────────────────────┐
            │ _master_studies.csv `prescience`=high   │
            │ `prescience_rationale`=<rebuttal text>  │
            └────────────────────┬────────────────────┘
                                 │ + add_player_rebuttal_v1.py
                                 │   writes audit row to
                                 │   _master_player_rebuttals.csv
                                 ▼
            ┌─────────────────────────────────────────┐
            │ sync_studies_verdicts_repo_from_        │
            │   archive_masters_v2.py --commit        │
            └────────────────────┬────────────────────┘
                                 ▼
                            (same Phase 1 join)
            ┌─────────────────────────────────────────┐
            │ v_studies.study_prescience_enum = high   │ (rebuttal wins)
            │ v_studies.prescience_mean = 0.46         │ (math preserved)
            │ v_studies_with_high_prescience += 1     │
            └─────────────────────────────────────────┘
```

**Why Path B works:** Phase 1 does NOT recompute `prescience` from `prescience_mean`. The authored verdict is pass-through. The math survives in adjacent columns for transparency. **Canonical proof:** Plaza DECtp transcript (2026-06-13) — authored `high` with rebuttal; underlying 26 scored obs averaged 0.46. After rebuild: `study_prescience_enum=high`, `prescience_mean=0.46`, row appeared in `v_studies_with_high_prescience`. The math is not lost; the verdict is not overwritten.

---

## 4. The Rule A rollup (canonical math)

```python
def rollup(pass_c_scores: list[int]) -> str:
    used = [s for s in pass_c_scores if s != -1]   # -1 = prefilter/parse_fail
    if len(used) == 0:
        return 'not-applicable'
    mean = sum(used) / len(used)
    if mean >= 3.5: return 'high'
    if mean >= 2.0: return 'medium'
    return 'low'
```

**Inputs:** all rows from `_master_prescience_scores.csv` WHERE `study_id == <target>` AND `prescience_score IS NOT EMPTY`.
**Excluded:** preseed_skip rows (empty score). Pre-filter and parse-fail rows participate as `-1` and are then filtered out by `used`.
**Output:** one of `{high, medium, low, not-applicable}`.
**Written to:** `_master_studies.csv` column `prescience`.

**Edge cases:**
- Zero observations scored AND zero unscored: `not-applicable`. (Methodology-demo synthetic studies hit this.)
- All scored obs are `-1`: `not-applicable` (empty `used`).
- Mixed `-1` + real scores: `-1`s drop, mean computed over real scores only.

---

## 5. Phase-1 join contract

`01_load_csvs_v2.py` is the **only** place the two grains meet at build time. It does three things relevant to prescience:

1. **Read `_master_studies.csv`** — preserve `prescience` enum verbatim.
2. **Read `_master_prescience_scores.csv`** — group by `study_id`, filter `prescience_score != -1 AND prescience_score IS NOT NULL`, compute `mean`, `max`, `count`.
3. **Join on `study_id`** — produce 12 enriched parquets, including `studies.parquet` with both authored and computed cols side-by-side.

Phase 2 (`02_build_data_layer_v4.py`) then exposes these as:
- `v_studies.study_prescience_enum` ← raw `prescience` column
- `v_studies.study_prescience_rationale` ← raw `prescience_rationale` column
- `v_studies.prescience_mean / _max / _obs_count` ← computed
- `v_studies_with_high_prescience` ← filter on `study_prescience_enum = 'high'`

**Invariant:** changing Phase 1 to recompute `prescience` from scores would break Path B silently. Do not refactor Phase 1 without revisiting this contract.

---

## 6. Lag points (where the system gets out of sync)

These are the eight places where two files that should agree can diverge in time. Every one of these has bitten a session.

| # | Lag point | Files | Mitigation |
|---|---|---|---|
| **L1** | **File 1 → File 2** | `prescience_scores_pass_c_cloud_v1.csv` → `_master_prescience_scores.csv` | Run `promote_pass_c_to_master_v1.py --commit` after every scorer run |
| **L2** | **File 2 → File 3 (repo)** | `archive_masters/_master_prescience_scores.csv` → repo root | EOD batch commit; File 3 will lag intra-session |
| **L3** | **Scores → Verdict** | File 2 (rolled up) → `_master_studies.csv` `prescience` | Manual write per study after Rule A; `roll_up_prescience_to_master_v3.py` is deprecated |
| **L4** | **archive_masters → repo** | `archive_masters/_master_studies.csv` → repo root copy | `sync_studies_verdicts_repo_from_archive_masters_v2.py --commit` |
| **L5** | **Masters → DuckDB** | Edited CSV → `v_studies` view via parquet | Re-run Phase 1+2 |
| **L6** | **DuckDB → Wiki pages** | `v_studies` → `wiki/studies/*.md` | Re-run Phase 3 (~3-4 hr tier-1 LLM) |
| **L7** | **Wiki pages → Embeddings** | `wiki/*.md` → `data/embeddings.parquet` | Re-run Phase 5 (~15 min) — Phase 5 reads file list at start; mid-flight edits race |
| **L8** | **DuckDB → Scaffolding** | `v_studies` counts → `README.md` / `AGENTS.md` / `chat-starter.md` | Re-run Phase 6; `kw ask` retrieves from embeddings, so L7 covers most of this |

**The 2026-05-27 canonical failure:** pub_year backfill ran. L5 caught up (Phase 1+2). L6-L8 did NOT run. `kw ask "shape of archive"` returned pre-backfill counts with citation confidence for hours. → **Gotcha 7 in the skill.**

**The 2026-06-18 canonical failure (this session):** Phase 5 captured the auto-stub page (L6 output) before the hand-authored page landed on disk via `git pull`. L7 had embedded the stale page. Surgical `reembed_single_page_v1.py` fixed it.

---

## 7. Cleanup map (v1.7.0 ship gate — ALL FOUR CLOSED 2026-06-18)

From the 2026-06-15 findings report, four items gated v1.7.0. All closed in commits `7935aec7` (F2) and `5f945dd9` (F3/F6/F7) on 2026-06-18.

| # | Finding | Action taken | Closure commit |
|---|---|---|---|
| **F2** | `promote_pass_c_to_master_v1.py` not in version control (Mac active copy had §11v provenance-preservation patch; repo copy was stale pre-patch version) | Committed Mac active copy (211 lines, F2 patch preserves `row.get("scorer_version")` and `row.get("source_pass")` with CLI defaults as fallback) to `scripts/`; repo now matches Mac | [`7935aec7`](https://github.com/shorttack/aberdeen-group-archive/commit/7935aec7b15200132c649e48e1f4632f133ae9c8) |
| **F3** | `model` column conflated ML model + row-class sentinel | Added 12th column `row_class` to File 2 (enum: scored / parse_fail / prefilter_skip / preseed_skip / no_anchor / pending). Backfill classifier hard-fails on UNKNOWN class or count drift. Expected counts: 8119 / 64 / 4 / 253 / 0 / 0 = 8,440. | [`5f945dd9`](https://github.com/shorttack/aberdeen-group-archive/commit/5f945dd97461dde813043ae3620b5b8fcfe648bd) |
| **F6** | Cloud parse-fails in-band (`source_pass='pass_c_cloud'` + `parse_ok='false'`) vs. sonar parse-fails split out to `pass_c_sonar_v1_parse_fail` | Retag 12 cloud rows: `source_pass` → `'pass_c_cloud_parse_fail'`. `parse_ok` unchanged. Script must run AFTER F3 (row_class must already be present). Driver v8 writes SH parse-fails to `pass_c_sh_parse_fail` from day 1. | [`5f945dd9`](https://github.com/shorttack/aberdeen-group-archive/commit/5f945dd97461dde813043ae3620b5b8fcfe648bd) |
| **F7** | 253 preseed_skip rows were undocumented in SH driver v8 spec | **Pete decision (2026-06-18): Option A — score normally in SH.** Preseed remains long-horizon-only. Driver v8 emits parallel SH verdicts; informative disagreement with long-horizon is expected and shows score-vs-rebuttal divergence. Rule A SH rollup uses only `source_pass IN (pass_c_sh_3y, pass_c_sh_5y) AND prescience_score >= 0`. | [`5f945dd9`](https://github.com/shorttack/aberdeen-group-archive/commit/5f945dd97461dde813043ae3620b5b8fcfe648bd) — see `Perplexity_Only/F7_preseed_skip_sh_treatment_decision_v1.md` |

**Remaining (should-fix, can land in parallel post-v1.7.0):** F1, F4, F5, F8, F9, F10.

**v1.7.0 ship gate status (2026-06-18 PM):** ✅ F2 closed. ✅ F3 closed. ✅ F6 closed. ✅ F7 closed. ✅ This doc reconciles (rev2). ⏳ MASTERS_NOTES.md v3 + RELEASE_NOTES_v1_7_0.md pending.

---

## 8. Quick-reference: "where does X live?"

| If you want… | Look here |
|---|---|
| The current verdict for a study | `_master_studies.csv` column `prescience` (archive_masters copy) OR `v_studies.study_prescience_enum` |
| The raw observation scores | `_master_prescience_scores.csv` (File 2) |
| The live scorer output (intra-session) | `prescience_scores_pass_c_cloud_v1.csv` (File 1) |
| The 5-year history of a player rebuttal | `kastner-author/notes/*_prescience_rationale_*.md` + `_master_player_rebuttals.csv` |
| What the math says (ignoring rebuttals) | `v_studies.prescience_mean / _max / _obs_count` |
| Which studies are high-prescience | `v_studies_with_high_prescience` (865 as of v1.6.2, 2026-06-18) |
| The rules that map scores → verdict | §4 above (Rule A) |
| How Phase 1 joins the two grains | §5 above |
| Where things lag | §6 above |
| What's broken structurally | §7 above + `Archive/decisions/prescience_architecture_audit_v1.md` |
| Pass C diagnosis tree | `kastner-archive-pipeline` skill §Pass C |

---

## 9. Cross-references

- **Findings report:** `Archive/decisions/prescience_architecture_audit_v1.md` (2026-06-15)
- **Pass C runbook:** `Perplexity_Only/PASS_C_V2_QWEN_FULL_RESCORE_PLAN_v1.md`, `Perplexity_Only/PRESCIENCE_BULK_SCORING_RUNBOOK_v1.md`
- **Schemas:** `Perplexity_Only/MASTERS_NOTES.md` (v2, 2026-06-12)
- **Pipeline commands:** `Perplexity_Only/PIPELINE_QUICKREF.md`
- **Player rebuttal SOP:** `PLAYER_REBUTTAL_PROCESS.md` (workspace; ships separately)
- **Skill:** `kastner-archive-pipeline` v1.7 (Gotchas 10, 11, 12; §Pass C three-file architecture)

---

**Maintained by:** Pete Kastner + Perplexity Computer.
**Next refresh trigger:** any of {File 2 schema change, new row class added beyond the six enum values, Path B convention change, Phase 1 join logic touched, SH driver v8 sentinel taxonomy expanded beyond `pass_c_sh_3y` / `pass_c_sh_5y` / `pass_c_sh_parse_fail`}.

**rev2 changelog (2026-06-18 PM):**
- Status header → rev2; F2/F3/F6/F7 closure referenced inline
- §1.3 promote script status: NOT IN REPO → CLOSED `7935aec7`
- §2.1 schema: 11 cols → 12 cols, added `row_class` row, row-class table now shows all 6 classes modeled (no more ⚠ flags), `source_pass` domain extended with `pass_c_cloud_parse_fail` / `preseed_b` / SH values
- §7 cleanup map: action column → action-taken column with closure commits
- §9 next-refresh trigger updated
