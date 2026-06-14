# Prescience Bulk Scoring Runbook v1

**Date authored:** 2026-06-14
**Author:** Pete Kastner (with Computer)
**Status:** STAGED — driver patched, gates programmatic, calibration ready to run
**Baseline master:** `_master_prescience_scores.csv` @ commit `aef5cc83` (4,082 rows; 3,829 numeric + 253 preseed_b)

---

## Scope

- **Total observations:** 23,926
- **Already scored or skip-marked:** 4,082 (17%)
- **Unscored:** 19,844 (83%) across 941 studies
- **In-scope for Pass C scoring** (after excluding studies with `prescience = not-applicable`): **17,200** across ~750 studies
- **Out-of-scope** (skip): 2,644 obs whose parent study is `prescience = not-applicable` (e.g., internal sales collateral, vendor brochures, employer records with no predictions)

---

## Execution model

- **Driver:** `run_prescience_pass_c_v6.py` — runs on Mac, calls Perplexity API directly. Computer does NOT call APIs.
- **Scorer:** `sonar-reasoning-pro` (per Pete 2026-06-14 strategy — NOT Claude).
- **Ceiling:** 200,000 credits + API costs (Pete 2026-06-14). Programmatic check via G6.
- **Prompt:** canonical `prescience_score_prompt_v2.md` on Mac.
  - SHA256: `f8c1e07469d8fce3148ad7c53f3ebb7f02fa312d8e0b724f6912808923385d29`
  - Authored 2026-05-25.
  - Scale: 0-5 canonical (0 = cannot assess; -1 = pre-filter non-claim marker).
- **Output schema:** must match repo master headers:
  `obs_id, study_id, model, prescience_score, confidence, rationale, scored_at, scorer_version, source_pass, elapsed_sec, parse_ok`
- **`source_pass` tags:**
  - `pass_c_sonar_v1` — API-scored rows
  - `pass_c_prefilter_v1` — rule-based skips (image/figure caption/junenews)
  - `preseed_b` — existing preseeded rows (skipped, not re-scored)
- **Resume safety:** v6 reads `_master_prescience_scores.csv` AND the batch output CSV; skips any obs with numeric score or preseed_b or pass_c_prefilter_v1 tag.
- **Out-of-scope filter:** v6 reads `_master_studies.csv` and skips obs whose study has `prescience='not-applicable'` (~2,644 obs).

---

## Phase 1 — Calibration (100 obs)

### Sample
- **File:** `prescience_calibration_sample_v1.csv` (workspace)
- **Size:** 100 obs
- **Strata:** 16 macro buckets covering all study types
  - employer-internal: 12
  - market-research: 11
  - white-paper: 10
  - profile-case: 11
  - topic-viewpoint: 9
  - press-trade: 9
  - memoir: 8
  - other: 5
  - consulting-advisory: 4
  - engineering-tech, presentation, vendor-marketing, product, dct, transcript, ai-response: 3 each
- **Study-size strata within each bucket:** small (<10 obs), medium (10-30), large (>30) — proportional
- **Distinct studies sampled:** 92
- **Seed:** `random.seed(42)` (reproducible)

### Cost dry-run
Before running all 100, score the FIRST 10 obs only. Estimate:
- Total input tokens × Sonar Pro input price
- Total output tokens × Sonar Pro output price
- Wall-clock per obs
- Extrapolate to 100 → 5,000 → 19,844

If 10-obs dry-run cost projection for 19,844 is unreasonable, stop and discuss.

### Acceptance gates (programmatic — `prescience_acceptance_gates_v1.py`)

| Gate | Threshold | Failure → |
|---|---|---|
| **G1: parse_ok rate** | ≥ 95% | Diagnose JSON parsing; fix driver before bulk |
| **G2: distinct scores** | ≥ 3 distinct values in 0-5 range | Re-examine prompt; possible prior bias |
| **G2b: max concentration** | No single score > 70% of batch | Distribution collapse |
| **G2c: distribution drift** | chi-sq vs baseline (3,829 numeric rows) ≤ 50.0 | Sonar Pro scoring fundamentally different from prior runs |
| **G3: rationale median** | ≥ 200 chars | Prompt may be truncating; model may be lazy |
| **G3b: rationale min** | ≥ 50 chars | Empty rationales |
| **G4: refusal rate** | score=0 rate ≤ 5% on calibration (raised to 55% on bulk; baseline=46%) | Sample skew or prompt issue |
| **G5: confidence drift** | chi-sq vs baseline confidence dist ≤ 1.0 | Model confidence calibration off |
| **G6: cost per obs** | ≤ 2,000 credits/obs (= 200K ceiling / 100 obs) | Renegotiate or reduce scope |

**Manual spot-check gate REMOVED** per Pete 2026-06-14 ("not sure I want to be the accuracy gate"). Replaced by G2c distribution drift + G5 confidence drift against 3,829-row baseline.

### Calibration deliverable
- File: `pass_c_v6_calibration_results.csv` (driver writes this on Mac)
- Schema: matches `_master_prescience_scores.csv` exactly (11 cols)
- Pete pastes contents or pushes to a branch; Computer runs `prescience_acceptance_gates_v1.py` and returns PASS/FAIL verdict

---

## Phase 2 — Tier A (5,000 obs) — GATED

**Precondition:** ALL Phase 1 gates pass.

### Sample construction
- Stratified across same 16 macro buckets (proportional to remaining-unscored counts after calibration)
- Within each bucket, stratified by study size
- Spread across all 92+ distinct studies — aim for breadth before depth
- Do NOT re-pick obs already scored in calibration

### Execution
- Cloud LLM driver scores 5,000 rows
- Driver writes results to a CSV matching the master schema
- Commit cadence: end-of-batch (per Pete: 5,000-row commit cadence)

### Acceptance gates (re-run G1-G5 on the 5,000)
- Same thresholds as Phase 1
- Plus **G7 (drift check):** score distribution shape on Tier A within ±10% per-bucket of Phase 1 calibration shape. Significant drift → stop, investigate.
- Plus **G8 (cost actual vs estimate):** within ±20% of Phase 1 extrapolation. >20% over → stop, renegotiate scope.

### Commit
- Append 5,000 new rows to `_master_prescience_scores.csv` → 9,082 total
- Single batch commit to `main` with manifest
- Update `Perplexity_Only/MASTERS_NOTES.md` with Tier A delta summary

---

## Phase 3 — Tier B (remaining 12,200 obs) — GATED

**Precondition:** ALL Tier A gates pass.

### Execution
- Run in 5,000-row sub-batches (≈3 sub-batches: 5,000 + 5,000 + 2,200)
- Each sub-batch ends with a commit
- Drift check after each sub-batch (G7 vs accumulated baseline)

### Final state
- `_master_prescience_scores.csv` grows from 4,082 → ~21,282 rows
- 2,644 not-applicable obs remain unscored (correctly out-of-scope)
- Bring delta: `Perplexity_Only/master_prescience_scores_BULK_2026_06_14.csv` (forensic record)

---

## Phase 4 — Post-scoring

1. **Pass C verdict roll-up** (per `kastner-archive-pipeline` skill) against full 23,926-obs master
2. **Wiki regen** (Phase 3 of pipeline) — pages now have prescience scores in YAML frontmatter
3. **Embeddings refresh** (re-embed wiki pages where prescience changed)
4. **DuckDB rebuild**
5. **v1.7.0 release gates re-evaluated** (§11v PRESCIENCE ARCHITECTURE AUDIT can finally close)

---

## Open items — RESOLVED 2026-06-14

1. ~~Sonar Pro Pass C driver~~ → v5 existed, v6 patched (`run_prescience_pass_c_v6.py`)
2. ~~Cost ceiling~~ → 200,000 credits + API costs (Pete)
3. ~~Resume safety~~ → v6 reads master + batch; skips numeric/preseed_b/prefilter
4. ~~Spot-check workflow~~ → REMOVED, replaced by G2c+G5 programmatic drift checks
5. **Type taxonomy hygiene** → BACKLOG (137 case-variants in `_master_studies.csv`)

---

## Artifacts ready in workspace

| File | Purpose |
|---|---|
| `prescience_calibration_sample_v1.csv` | 100-obs stratified calibration sample (Phase 1 input) |
| `unscored_obs_inventory_v1.csv` | 19,844 unscored obs with study metadata (Tier A/B source) |
| `PRESCIENCE_BULK_SCORING_RUNBOOK_v1.md` | This document |

---

## Decision log entry (to be appended to `_decisions_log.md`)

```
## 2026-06-14 — Prescience bulk scoring plan staged

- Master rebuilt at aef5cc83: 4,082 rows (3,829 numeric + 253 preseed_b)
- Unscored: 19,844 / Scorable: 17,200 / Out-of-scope: 2,644
- Phase 1 calibration: 100 obs stratified across 16 macro buckets
- Phases 2-3: 5,000 + (5,000 + 5,000 + 2,200) tiered with G1-G8 gates
- Driver: Pete cloud (Sonar Pro), NOT Computer-managed
- Decision pending: cost ceiling, driver existence/resume-safety
```
