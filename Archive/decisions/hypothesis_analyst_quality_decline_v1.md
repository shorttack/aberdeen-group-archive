# Hypothesis: Analyst-Quality Decline Across Aberdeen Eras

**Raised**: 2026-06-16 08:47 EDT
**By**: Pete Kastner (mid-SH-sweep observation)
**Status**: HYPOTHESIS — testable against `Perplexity_Only/sh_sweep_le_2015_results.csv` once PID 59349 completes (~17:30 ET tonight)
**Refs**: `Archive/logs/log_entry_2026_06_16_sh_calibration_and_sweep_launch_v1.md` (sweep launch); `Archive/decisions/decisions_log_entry_2026_06_15_short_horizon_prescience_v3.md` (SH spec v3)

---

## Trigger

At the 11.3% checkpoint of the SH ≤2015 sweep (978/8,659 obs scored), mean prescience had climbed from the calibration baseline (3y mean 2.63, 5y mean 2.64) to (3y mean ~3.20, 5y mean ~3.30) — a +0.34 / +0.43 shift. The agent initially attributed this to **anchor age** (older obs have more elapsed outcome time → more legible verdicts → higher Sonar confidence). Pete proposed an alternative or complementary explanation:

> **"Older obs are showing more high-prescience — another hypothesis is the early analysts were more qualified."**

The Aberdeen authorship history fits this shape:

- **1980s–1990s Aberdeen**: smaller analyst pool, deeper hands-on enterprise experience, longer tenure, less marketing-driven research, customers paying premium for original primary research.
- **2000s+ Aberdeen**: broader survey-driven model, more analysts, faster cycle, more vendor-sponsored work.

If the qualification hypothesis holds, the prescience signal should appear in the analyst dimension and the methodology dimension — not only in the era dimension.

---

## Hypothesis statement

The mean prescience of an Aberdeen observation depends on **analyst quality and methodology rigor**, not only on **elapsed time since publication**. Within the same elapsed-time band, earlier-era analysts (and analysts using primary-research methodologies) will produce systematically more prescient observations than later-era analysts (and analysts relying on survey or press-trade methods).

---

## Three tests (all run against post-sweep CSV)

### Test 1 — Anchor-decade mean prescience
Bin the 8,659 results by decade of `anchor_year` and compute mean `prescience_3y` and `prescience_5y` per decade. The hypothesis predicts **monotonic decline** as decade walks forward:

| anchor decade | predicted direction |
|---|---|
| 1970s | highest |
| 1980s | ↓ |
| 1990s | ↓ |
| 2000s | ↓ |
| 2010–2015 | lowest |

Sharpness of the decline is the signal — a flat profile or a U-shape disconfirms.

### Test 2 — Author-level prescience (most decisive)
Join `Perplexity_Only/sh_sweep_le_2015_results.csv` ⨝ `_master_observations.csv` ⨝ `_master_studies.csv` on `study_id`. Aggregate by `_master_studies.author`, restrict to authors with **≥10 obs in the sweep**, rank by mean prescience (3y and 5y separately).

Predictions:
- Top of the ranking skews to early-Aberdeen names (Kastner, Yphantis, et al.).
- Bottom of the ranking skews to late-era survey shops / vendor-sponsored work.
- The author-level variance within an era should be comparable to the cross-era variance — if so, methodology and individual capability matter as much as the era itself.

This is the most decisive test because it isolates **analyst effects** from **era effects**.

### Test 3 — Methodology-code prescience
`_master_observations.csv.methodology_code` distinguishes the rigor of the underlying research. Compute mean prescience grouped by methodology class:

- **Primary research / case study methods** (high effort, low volume) — predicted highest.
- **Survey-based methods** (medium effort, high volume) — predicted middle.
- **Press / press-trade methods** (lowest effort) — predicted lowest.

If methodology trumps era (i.e., a primary-research obs from 2012 outperforms a survey-based obs from 1985), that strengthens the qualification hypothesis — analysts choosing harder methods are also more capable.

---

## Confound: elapsed-time crystallization

The ≤2015 cutoff selects for obs where outcomes have had time to crystallize. **Older eras get a longer crystallization window than 2010–2015 obs**, so even a random scorer would assign higher confidence to older obs simply because more is known about what happened next.

To disentangle era effect from elapsed-time effect, two approaches:

**Approach A — Regression** (more sophisticated)
Fit `prescience ~ anchor_decade + (today - anchor_year)` and inspect coefficients. The era coefficients should remain significant after controlling for elapsed time if the qualification hypothesis holds.

**Approach B — Restricted comparison** (simpler, preferred for first cut)
Restrict the comparison to obs where elapsed time ≥ 15 years (i.e., anchor_year ≤ 2011). This drops the 2010–2015 cohort entirely and leaves only obs with comparable crystallization windows. The era comparison within the surviving pool is then clean.

Preference: **Approach B for the first cut.** Simpler, fewer assumptions, plenty of statistical power left after the cohort drop.

---

## Operational notes

- All three tests are **read-only queries** against the post-sweep CSV. No new API calls.
- Tests 1 and 3 can be run as ad-hoc Python scripts. Test 2 requires a join script that respects the existing master schemas.
- Pete's author identification depends on `_master_studies.author` being clean. Spot-check author normalization (e.g., "P. Kastner" vs "Peter Kastner" vs "Kastner") before ranking — collation noise will fragment a single analyst's body of work across multiple ranked rows.
- If the hypothesis confirms, it has implications for the §11v PRESCIENCE ARCHITECTURE AUDIT (D6) — the master `prescience` enum could carry an analyst-quality covariate, and the prescience pool weighting could account for it.

## Next steps after sweep completes

1. Drop CSV into a notebook or `tests/hypothesis_analyst_quality_decline_v1.py`.
2. Run Test 1 (decade bins) first — quickest to interpret.
3. Run Test 3 (methodology) second — narrows the mechanism.
4. Run Test 2 (author ranking) last — needs the most data hygiene work.
5. If results support the hypothesis, raise a follow-on decision item for v1.7+ on whether the master `prescience` model should incorporate an analyst-quality covariate.

## Refs

- Sweep manifest: `Perplexity_Only/sh_sweep_le_2015_manifest_v1.csv` (8,659 obs, anchor ≤ 2015)
- Sweep results (in-flight): `Perplexity_Only/sh_sweep_le_2015_results.csv` (PID 59349)
- Calibration results: `Perplexity_Only/sh_calibration_results.csv` (100 obs, anchor ≤ 2020)
- Calibration gates report: `Perplexity_Only/sh_calibration_gates_report.md`
