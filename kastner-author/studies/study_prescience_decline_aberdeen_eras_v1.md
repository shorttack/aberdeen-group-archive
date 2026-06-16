---
title: "Prescience Decline Across Aberdeen Eras: A Self-Referential Analysis of the 1972–2015 Archive"
author: "Peter S. Kastner"
date: "2026-06-16"
collection: "archive-meta"
type: "archive-meta"
methodology: "self-referential prescience aggregation"
subject_domain: ["technology-industry-history", "research-methodology", "prescience-scoring"]
license: "CC BY 4.0"
status: "draft — results pending SH sweep completion (~2026-06-16 PM)"
sources:
  - "Perplexity_Only/sh_sweep_le_2015_results.csv (PID 59349, 8,659 obs, anchor ≤ 2015)"
  - "_master_observations.csv (post-SH-extend, 23,926 rows × 31 cols, SHA 83f97b38…)"
  - "_master_studies.csv (1,452 entries)"
  - "Archive/decisions/hypothesis_analyst_quality_decline_v1.md (pre-registered hypothesis, 2026-06-16 08:47 ET)"
  - "Archive/decisions/decisions_log_entry_2026_06_15_short_horizon_prescience_v3.md (SH spec v3)"
---

# Prescience Decline Across Aberdeen Eras

## Abstract

This study tests whether the prescience of Aberdeen Group research observations declines monotonically across the firm's eras (1972–2015), and whether observation-level methodology rigor correlates with prescience independent of era. Using the short-horizon prescience scores produced by the 2026-06-16 Sonar Pro sweep against the Aberdeen archive (8,659 observations anchored ≤2015, scored on both 3-year and 5-year outcome windows), we run two complementary tests: an anchor-decade aggregation and a methodology-code aggregation. The era-vs-elapsed-time confound is addressed by restricting the primary comparison to observations with elapsed-time ≥ 15 years (anchor ≤ 2011). Author-level analysis is deliberately deferred to a separate forthcoming study.

**Status**: The methodology, hypothesis, and test specifications were committed to the archive **before** the sweep completed (see `hypothesis_analyst_quality_decline_v1.md`, committed 2026-06-16 08:47 ET; sweep PID 59349 launched 07:32 ET, ETA ~17:30 ET tonight). The results section is currently a placeholder pending sweep completion.

## Hypothesis

The mean prescience of an Aberdeen observation depends on **analyst quality and methodology rigor**, not only on **elapsed time since publication**. Within the same elapsed-time band, earlier-era analysts (and analysts using primary-research methodologies) will produce systematically more prescient observations than later-era analysts (and analysts relying on survey or press-trade methods).

This hypothesis was raised by Pete Kastner during the SH sweep mid-run (08:47 ET) after observing that the 11.3%-checkpoint mean prescience had drifted upward (+0.34 / +0.43 on 3y / 5y respectively) from the calibration sample baseline. The alternative explanation under test is **elapsed-time crystallization** — older observations have more elapsed outcome time, so a competent scorer can verdict them with higher confidence regardless of the underlying analyst's skill.

## Background

Aberdeen Group's research output evolved markedly across its 1972–2015 history:

- **1980s–1990s**: smaller analyst pool, deeper hands-on enterprise experience, longer analyst tenure, primary-research-driven case studies, customers paying premium for original work.
- **2000s+**: broader survey-driven model, more analysts, faster cycle, more vendor-sponsored work, higher emphasis on volume of published reports.

If observable prescience tracks this evolution, the archive carries a measurable signal of its own methodological history.

## Methods

### Data

- **Primary source**: `Perplexity_Only/sh_sweep_le_2015_results.csv` produced by `scripts/run_prescience_short_horizon_v8.py` against 8,659 observations.
- **Join key**: `obs_id` (results) ↔ `obs_id` (`_master_observations.csv`) for `methodology_code` and `study_id`.
- **Anchor source**: `anchor_year` column in results CSV (resolved by `anchor_year_resolver_v2`; 73.7% from `obs.year_observed`, 26.3% from `study.date` fallback).
- **Score columns**: `prescience_3y` and `prescience_5y`, both on the locked canonical 0–5 scale (per `decisions_log_entry_2026_06_14_prescience_scale_1_5_v1.md` and SH spec v3).
- **Parse-fail handling**: rows with `prescience_3y == -1` or `prescience_5y == -1` are excluded from all aggregations (sentinel value for `parse_fail:schema_mismatch`; observed rate <1% in calibration and early sweep checkpoints).

### Test 1 — Anchor-decade mean prescience

Bin observations by `floor(anchor_year / 10) * 10` and compute, per decade:

- N observations
- Mean `prescience_3y` (with 95% CI via bootstrap, B=1000)
- Mean `prescience_5y` (with 95% CI)
- Standard deviation within decade
- Divergence rate (`windows_diverge == true`)

**Decision rule**: If the means decline monotonically from the 1970s through the 2010–2015 cohort, and the 95% CIs do not overlap between adjacent decades, the test supports the hypothesis.

### Test 3 — Methodology-code mean prescience

Group observations by `methodology_code` and roll up to three rigor tiers:

- **Primary** — case studies, interviews, hands-on benchmarks (highest effort).
- **Survey** — questionnaire-based research (medium effort).
- **Press / press-trade** — sourced from trade press, secondary citations (lowest effort).

The exact mapping of `methodology_code` values to tiers will be derived from the codes present in the sweep, audited for completeness, and documented in this study's results section.

Compute per tier: N, mean `prescience_3y`, mean `prescience_5y`, divergence rate. Decision rule mirrors Test 1.

### Confound control — Approach B (restricted comparison)

The ≤2015 anchor cutoff means that the youngest cohort (2010–2015) has only 11–16 years of elapsed outcome time, while the 1970s cohort has 50+ years. A naive scorer would assign higher confidence to older obs simply because more is known about what happened next.

**Primary analysis** restricts Tests 1 and 3 to `anchor_year ≤ 2011` (≥15 years elapsed). This drops the 2010–2015 cohort entirely and leaves a comparison pool where elapsed-time variance is bounded but not eliminated.

**Secondary analysis** repeats Tests 1 and 3 on the full ≤2015 pool, with the youngest cohort flagged. Comparing the two analyses quantifies how much of the era effect is era-vs-crystallization.

### Author-level analysis deferred

Test 2 from the hypothesis document (per-author prescience ranking) is **explicitly out of scope** for this study. Author normalization across the 1,452 studies (handling "P. Kastner" / "Peter Kastner" / "Kastner" variants) requires a separate hygiene pass that is not blocking for the era-and-methodology question. A follow-on study — *Kastner Accuracy: Individual-Analyst Prescience Calibration Across the Aberdeen Archive* — is planned for after this one.

## Results

**[TBD — pending SH sweep completion, ETA ~2026-06-16 17:30 ET]**

### Test 1 results — Anchor-decade

| Decade | N | Mean 3y | 95% CI 3y | Mean 5y | 95% CI 5y | Divergence |
|---|---|---|---|---|---|---|
| 1970s | TBD | TBD | TBD | TBD | TBD | TBD |
| 1980s | TBD | TBD | TBD | TBD | TBD | TBD |
| 1990s | TBD | TBD | TBD | TBD | TBD | TBD |
| 2000s | TBD | TBD | TBD | TBD | TBD | TBD |
| 2010–2015 | TBD | TBD | TBD | TBD | TBD | TBD |

[Primary analysis: restricted to anchor ≤ 2011]
[Secondary analysis: full ≤2015 pool]

### Test 3 results — Methodology rigor

| Tier | Methodology codes | N | Mean 3y | Mean 5y | Divergence |
|---|---|---|---|---|---|
| Primary | TBD | TBD | TBD | TBD | TBD |
| Survey | TBD | TBD | TBD | TBD | TBD |
| Press/Trade | TBD | TBD | TBD | TBD | TBD |

### Cross-test pattern

[TBD — does methodology effect persist within each decade? does decade effect persist within each methodology tier? if yes to both, both are real signals; if methodology dominates, era is largely a proxy for methodology mix.]

## Discussion

**[TBD — pending results]**

Anticipated discussion points:

- Magnitude of any era effect vs. methodology effect.
- Whether the youngest cohort (2010–2015) shows a discontinuity that suggests an Aberdeen business-model inflection point.
- Comparison to the calibration sample baseline (3y mean 2.63, 5y mean 2.64) — does the ≤2015 pool sit measurably above it, and is the gap explained by era, methodology, or elapsed time?
- Implications for the §11v PRESCIENCE ARCHITECTURE AUDIT (D6) — should the master `prescience` enum carry an era-or-methodology covariate?
- Honest limits: this is a single-scorer (Sonar Pro) verdict; G5 human-truth gate was deferred in the calibration; any systematic Sonar bias toward older content would inflate the era effect.

## Limitations

1. **Single-scorer** — All prescience verdicts come from one Sonar Pro pass. No human-truth fixture was scored in calibration (G5 deferred).
2. **Anchor resolution mix** — 26.3% of observations use the `study.date` fallback, which Pete manually entered for many studies. Date-entry errors will appear as anchor-year noise.
3. **Methodology-code completeness** — Not all observations carry a non-empty `methodology_code`. Observations with empty codes are excluded from Test 3 (count to be reported in results).
4. **Survivorship bias** — The archive itself is a curated subset of Aberdeen's total output. Observations from less-curated regions of the archive may be systematically different.
5. **Elapsed-time confound** — Approach B mitigates but does not eliminate. The ≤2011 restricted comparison is the cleanest cut available without further sweeping.

## Conclusion

**[TBD — pending results]**

## Observations

This study's verdicts are themselves observations contributing to the archive. The following observation rows will be added to `_master_observations.csv` upon study finalization:

| obs_id | type | year_observed | metric_name | metric_value | confidence | methodology | rationale |
|---|---|---|---|---|---|---|---|
| (study_id)-OBS-001 | era_prescience_trend | 2026 | decade_decline_slope | TBD | TBD | self_ref_aggregation | TBD |
| (study_id)-OBS-002 | methodology_prescience_gap | 2026 | primary_vs_press_gap | TBD | TBD | self_ref_aggregation | TBD |
| (study_id)-OBS-003 | era_methodology_interaction | 2026 | interaction_strength | TBD | TBD | self_ref_aggregation | TBD |
| (study_id)-OBS-004 | elapsed_time_residual | 2026 | era_effect_after_control | TBD | TBD | self_ref_aggregation | TBD |

Exact `study_id` will be assigned during ingest; rows will be wired through `_master_entity_studies.csv` and `_master_tech_studies.csv` as appropriate.

## Reproduction

To reproduce the results in this study after the SH sweep completes:

```bash
cd ~/Desktop/Archive/aberdeen-group-archive
python3 scripts/run_quality_decline_tests_v1.py \
  --results Perplexity_Only/sh_sweep_le_2015_results.csv \
  --obs _master_observations.csv \
  --studies _master_studies.csv \
  --output Perplexity_Only/study_prescience_decline_results_v1.json \
  --md Perplexity_Only/study_prescience_decline_results_v1.md
```

The `run_quality_decline_tests_v1.py` script will be authored after the sweep completes, committed to `scripts/`, and referenced from this study's bibliography. The script's output JSON + Markdown will populate the [TBD] sections of this document, and the final study will be committed as a versioned snapshot.

## References

- `Archive/decisions/hypothesis_analyst_quality_decline_v1.md` (pre-registered hypothesis, commit `9ef87947`)
- `Archive/decisions/decisions_log_entry_2026_06_15_short_horizon_prescience_v3.md` (SH spec v3)
- `Archive/decisions/short_horizon_design/short_horizon_acceptance_gates_v2_spec.md` (G1-G10 gates)
- `Archive/decisions/decisions_log_entry_2026_06_14_prescience_scale_1_5_v1.md` (canonical 0–5 scale)
- `Archive/logs/log_entry_2026_06_16_sh_calibration_and_sweep_launch_v1.md` (sweep launch session log)
- `scripts/run_prescience_short_horizon_v8.py` (sweep driver)
- `scripts/anchor_year_resolver_v2.py` (anchor resolution module)
- `scripts/sh_gates_v2.py` (acceptance gates)
- `scripts/run_quality_decline_tests_v1.py` (to be authored post-sweep)
