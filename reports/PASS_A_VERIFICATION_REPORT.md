# Pass A — Verification Improvements Summary

Date: 2026-05-20  
Operator: Computer (automated, no LLM)  
Scope: Master + 946 per-study observations.csv files

## What changed

### 1. Cleared all [REVIEW] markers (56 rows)
- 50 `unknown [REVIEW]` and 6 `[REVIEW]` confidence labels eliminated
- Triage rules:
  - Empty-notes / open-question rows → `low` (16 rows)
  - Self-attested outcome with archive narrative support → `partially-verified` (4 rows)
  - Predictions with notes lacking outcome linkage → `medium` (14 rows)
  - Observations with metric_value and notes but no external verification → `medium` (22 rows)

### 2. Built prediction↔outcome join table
- Output: `_prediction_outcome_links.csv` (3,245 links)
- Coverage: 1,422 of 1,684 viability-predictions (84.4%) now linked to ≥1 outcome
- Match-method distribution:
  - `entity+tech` (strongest): 436 predictions
  - `study+tech`: 429 predictions  
  - `study-only` (weakest): 496 predictions
  - `tech-only`: 61 predictions
  - Unmatched: 262 predictions (studies with zero `actual-outcome` rows)

### 3. Lifted prediction confidence from outcome linkage
- 690 viability-predictions promoted (only when strictly stronger than original):
  - → `verified`: 590 (strong entity+tech or study+tech match to verified outcome)
  - → `partially-verified`: 90 (weak match or partial-outcome match)
  - → `refuted`: 10 (matched to refuted outcome)
- Conservative rule: never demote. Original `high` confidence retained if no outcome adjudication exists.

### 4. Added `verification_method` column
- Inserted after `confidence` in master + all 946 per-study CSVs
- Taxonomy:
  - `web-source` (1,207 rows / 6.1%) — Phase 3 verified outcomes
  - `outcome-linkage` (847 rows / 4.3%) — Pass A predictions lifted from matched outcomes
  - `archival-primary` — Kastner primary source (memoir, transcript, employer record)
  - `cross-reference` (4 rows) — explicit cross-study citation
  - `ingest-extraction` (17,475 rows / 89.0%) — default, confidence assigned at ingest from source text
  - `unverified` (79 rows) — confidence='low' with no other evidence path
  - `placeholder` (16 rows) — REVIEW-cleared rows downgraded to low

## Headline metrics

### Viability-prediction verification rate
- **Before Pass A**: 85 / 1,684 = 5.0% verified-or-partial
- **After Pass A**: 766 / 1,684 = **45.5% verified-or-partial**
- Lift: +681 rows mechanically linked, no new external evidence

### Refutation rate (predictions)
- Before: 3 refuted / 1,684 = 0.18%
- After: 13 refuted / 1,684 = 0.77%
- Newly surfaced refutations are predictions whose matched outcome was already tagged `refuted` but not propagated upstream

### Confidence distribution (master, all observations)
| Level | Count | % |
|---|---|---|
| high | 14,239 | 72.5% |
| medium | 2,611 | 13.3% |
| verified | 2,434 | 12.4% |
| partially-verified | 204 | 1.0% |
| low | 96 | 0.5% |
| refuted | 39 | 0.2% |
| blank | 5 | 0.0% |
| TOTAL | 19,628 | 100.0% |

### What Pass A does NOT do
- No new external evidence introduced
- No LLM used
- No re-verification of `actual-outcome` confidence — those stand as Phase 3 left them
- 262 predictions in outcome-less studies remain unlinked (genuinely unverifiable from archive alone)

## Provenance files generated
- `_prediction_outcome_links.csv` — join table (3,245 rows, committed to archive root)
- `_pass_a_review_triage.json` — per-row REVIEW triage decisions
- `_pass_a_prediction_lifts.json` — per-row confidence-lift log
- `PASS_A_VERIFICATION_REPORT.md` — this document
