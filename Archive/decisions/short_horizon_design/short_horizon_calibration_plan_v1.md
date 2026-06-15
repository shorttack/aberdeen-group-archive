# Short-Horizon Calibration Sample Plan v1

**Status:** DRAFT (Phase 0). Pre-sweep gate.
**Cost:** ~$1.20 (100 obs × combined-call rate).

---

## Goal

Validate driver v8 + combined-call prompt + gates v2 on a 100-obs sample BEFORE committing $250-300 to a full corpus sweep.

---

## Sample construction

### Anchor constraint
All 100 obs must have `anchor_year ≤ 2020` so **both** windows are elapsed (per strict rule today 2026-06-15: 5y cutoff anchor ≤ 2020).

### Strata (25 buckets × 4 obs each = 100)
Reuse the same 25-bucket stratification used for Tier A. Buckets are defined by `(type, decade)` or `(collection, decade)` — pull the exact bucket definitions from the Tier A sample-construction script and filter each bucket to `anchor_year ≤ 2020` before sampling.

If a bucket has < 4 eligible obs after filter, draw what's available and over-sample adjacent buckets to hit n=100.

### Selection method
- Random seed: `20260615` (today's date)
- Sampling: simple random WITHOUT replacement within each bucket
- Exclude obs already in Tier A and Tier B results (no double-scoring; calibration cohort independent of sweep cohorts)

### Required columns in sample CSV
`obs_id, obs_text, obs_date, period_start_year, study_id, study_title, study_type, study_published_at, entity_focus, tech_focus`

Plus a placeholder column `human_verdict_3y`, `human_verdict_5y` — to be filled by Pete or programmatic proxy BEFORE running G5.

---

## Pre-flight checks (before API calls)

1. `python3 anchor_year_resolver_v1.py` → self-test PASS
2. Confirm every row resolves to an anchor_year ≤ 2020 (run resolver across sample, fail loudly otherwise)
3. Confirm no obs_id overlap with `prescience_tier_a_sample_v1.csv` or `prescience_tier_b_sample_v1.csv`

---

## Run

```bash
python3 driver_v8.py \
  --input  prescience_calibration_sh_sample_v1.csv \
  --studies _master_studies.csv \
  --output calibration_sh_results_v1.csv \
  --resume \
  --limit 100
```

Expect ~12-20 minutes wall time at Tier A throughput.

---

## Validation

Run `gates_v2.py --input calibration_sh_results_v1.csv --report calibration_sh_gates_v1.json`.

### MUST PASS (block sweep if any fails)
- G1 schema
- G6 source-pass labeling
- G7 pending rate ≤ 5% (calibration is anchor ≤ 2020, so any pending = bug)
- G8 diverge rate ≤ 25%

### Hand inspection (Pete, ~30 min)
Pete reviews:
- 10 random scored rows (full rationale)
- All `windows_diverge = TRUE` rows
- All `source_pass_sh = parse_fail` rows
- Distribution chart: 3y vs 5y score crosstab (Δ histogram)

Pete's GO/NO-GO is binary. NO-GO → debug + rerun calibration. GO → sweep authorized.

---

## Calibration-set provenance for G5

G5 requires known-correct human verdicts. Options ranked by realism:

1. **Reuse existing Pass C long-horizon scores as proxy.** Cheap, immediate. Weakness: long-horizon score on a 2018 obs incorporates evidence through 2026, not through 2023 (3y) or 2025 (5y). Use only as a directional sanity check, not strict accuracy.
2. **Pete hand-scores 25-40 of the 100.** ~2-3 hours of his time. Highest fidelity. Pete declined to be "the accuracy gate" generally, but a one-time calibration pass is different from ongoing review.
3. **External LLM as adjudicator.** A second model (e.g. Claude Opus) scores the same 100 obs with identical prompt; treat agreement-rate as ground-truth proxy. Adds ~$5 cost. Worth it.

**Recommendation:** Combine #1 (free directional baseline) + #3 (cheap adjudicator) for initial G5. Defer #2 unless #1+#3 produce ambiguous result.

---

## Deliverables out of calibration

1. `calibration_sh_results_v1.csv` (100 rows, full v8 output)
2. `calibration_sh_gates_v1.json` (G1-G10 report)
3. `calibration_sh_hand_review_v1.md` (Pete's notes from 30-min review)
4. GO/NO-GO decision in `Archive/decisions/decisions_log_entry_<date>_sh_calibration_v1.md`

---

## Cost ledger

| Phase | API cost | Pete time |
|---|---|---|
| Build sample | $0 | 0 |
| Resolver self-test | $0 | 0 |
| Driver v8 smoke (10 rows) | ~$0.12 | 5 min |
| Calibration sweep (100 rows) | ~$1.20 | 0 |
| Adjudicator pass (Claude Opus, 100 rows) | ~$5 | 0 |
| Hand review | $0 | 30 min |
| **Calibration total** | **~$6.50** | **35 min** |
| Full sweep (if GO) | ~$288 | 0 |

Calibration is < 2.5% of full-sweep cost. No reason to skip it.