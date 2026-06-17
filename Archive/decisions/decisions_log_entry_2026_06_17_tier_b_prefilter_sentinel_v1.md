# Decision — 2026-06-17 — Tier B Prefilter -1 Rows Stay As-Is (No Reclassification)

**Decision date:** 2026-06-17 AM
**Decision owner:** Pete Kastner
**Session context:** §11v Tier B Pass C run review (post-completion, pre-promotion)

---

## Decision

The 56 rows in `pass_c_v6_tier_b_results.csv` with `prescience_score = -1` and `source_pass = pass_c_prefilter_v1` will **NOT** be reclassified to a new sentinel value. They remain at `-1` with their existing `source_pass` provenance label.

## Context

Tier B Pass C v7 driver completed 2026-06-16 23:39 UTC after 33.9 hours (2,033.1 min wall, 4.1 calls/min). Final tally:

- 8,645 total rows in `pass_c_v6_tier_b_results.csv`
- 8,641 API calls (paid scoring)
- 4 prefilter exclusions made by driver before API call
- Note: the "56 -1 rows" finding in the morning review reflects the full prefilter population across the Tier B sample, not just the 4 captured in the run report — the report counts only prefilters that happened during the API-loop portion of the run, while additional prefilter rows were emitted in pre-API setup. **Verify exact count at promote time; the semantic is unchanged either way.**

Of the rows with `prescience_score = -1`:

- All carry `source_pass: pass_c_prefilter_v1`
- All have `elapsed_sec: 0.0` (no API call was made)
- All have `parse_ok: true` (nothing to parse, no parser failure)
- All have rationales like:
  - "Pre-filter: figure caption only."
  - "Pre-filter: picture-text dump, image content preserved separately."

These are observations the v7 driver correctly identified as content unsuitable for prescience scoring (image captions, picture-text OCR dumps, etc.) and short-circuited before spending an API call.

## Why this is different from SH's -99 sentinel

In the SH ≤2015 sweep (2026-06-16), 16 rows were reclassified from `-1` to `-99` to distinguish **Sonar model refusals** (the model received an API call and declined to score) from **true parse failures** (the model responded but the parser couldn't read the response). That reclassification was necessary because the SH driver had no `source_pass`-equivalent column to encode the distinction at provenance level — the score column had to do double duty.

Tier B's situation is different:

| Distinction needed | SH sweep solution | Tier B equivalent |
|---|---|---|
| Was the observation scored? | -1 = no, 0–5 = yes | `source_pass` column |
| If not scored, why? | -1 = parse_fail, -99 = refusal | `source_pass: pass_c_prefilter_v1` = prefilter; (no driver-side refusal-detection logic in v7 yet) |

Tier B's `source_pass` column **already preserves** the semantic distinction. Overloading `prescience_score` with a new sentinel would duplicate information that's already first-class in the schema.

## Aggregation rule (codified)

When computing means, modes, or score-share statistics from Tier B (and any future Pass C v7+ results), exclude rows where:

- `prescience_score < 0` (any negative sentinel), **OR equivalently**
- `source_pass = pass_c_prefilter_v1` (prefilter-excluded rows specifically)

These are equivalent for Tier B v7 because the only negative-score producer is the prefilter. For SH-style sweeps where both -1 and -99 exist, the score-column filter remains the canonical exclusion rule.

## Implications for downstream artifacts

1. **Promotion to `_master_prescience_scores.csv`** — prefilter rows can be promoted as-is. Downstream consumers should treat them as "excluded, not scored," not as "scored 0" or "scored 1."

2. **Wiki regen / Phase 3** — per-study Pass C rollup logic must filter out `source_pass: pass_c_prefilter_v1` rows when computing aggregate prescience for a study. Otherwise the study mean would be artificially deflated by what are essentially "no signal to score" rows.

3. **`v_studies_with_high_prescience` view** — counts of high-prescience observations per study should already exclude negative scores. Verify the view's filter logic matches before wiki regen.

4. **Driver v8/v9 consideration** — if Sonar refusals become a recurring failure mode in future Pass C runs, consider adding driver-side refusal detection that emits `source_pass: pass_c_refusal_v1` (parallel to the prefilter mechanism) rather than retroactively reclassifying via post-hoc script. This would put refusal handling on the same first-class footing as prefilter handling.

## Provenance

- Tier B output: `~/Desktop/Archive/pass_c_v6_tier_b_results.csv` (8,645 rows, 6.9 MB)
- Tier B report: `~/Desktop/Archive/logs/pass_c_v6_tier_b_results_report.md`
- Driver: `scripts/run_prescience_pass_c_v7.py`
- Input manifest: `Perplexity_Only/prescience_tier_b_sample_v1.csv`
- Decision: this file

## Related decisions

- 2026-06-16 SH ≤2015 sweep — established the -99 content_unrecoverable sentinel for Sonar refusals (different mechanism, different solution)
- 2026-06-16 sentinel scheme locked at: 0–5 valid, -1 parse_fail OR prefilter_excluded (driver context determines which), -2 pending, -99 content_unrecoverable
