# Decision: Launch Tier A Prescience Bulk Scoring Run

**Date:** 2026-06-14 (Sunday)
**Session:** §11v continued — Prescience Calibration → Tier A
**Status:** RUNNING (PID 73051, started ~15:24 EDT)
**Author:** Pete Kastner + Computer

---

## Context

Prescience master rebuild committed earlier today (commit `aef5cc83`: 3,761→4,082 rows on main). Remaining work: score 19,844 unscored observations across 941 studies, using Sonar Reasoning Pro via API (NOT Claude — explicit user directive to minimize cost).

Strategy gates established:
- 200,000 credit ceiling + API costs
- Resumable driver required
- Programmatic G2c+G5 drift checks replace human accuracy gate (Pete: "not sure I want to be the accuracy gate")
- Salvage trustworthy runs only — "Salvaging garbage yields a contaminated prescience pool"

## Calibration phase (completed earlier today)

100-obs stratified calibration sample (cal100) across 16 macro buckets, 92 distinct studies. Driver v6 with:
- Master-aware resume logic
- `--input-manifest` / `--output` / `--skip-not-applicable` flags
- 11-column schema matching baseline
- `source_pass` tagging (`pass_c_sonar_v1`, `pass_c_prefilter_v1`, `preseed_b`)
- Pre-filter rules R1–R4 (omitted pictures, figure captions, junenews-fc15cc, picture text blocks)

**Calibration results (cal100):**
- Wall: 12.9 min · 8.66s/obs avg · 6.81s median · 42.81s max
- Parse OK: 100% ✓
- Distinct scores: 6 ✓
- Max concentration: 57% ✓
- Distribution drift chi-sq vs 3,829-row baseline: 0.74 ✓
- Rationale median: 637ch ✓ / min: 334ch ✓
- Refusal rate: 57% (vs G4 patched threshold 55%) — marginal, but **baseline-adjusted = below 67% apples-to-apples**, so model is actually more selective than baseline
- Confidence drift: 0.25 ✓
- Total cost since June 1: $3.00 (includes ALL prior work + cal100)

**Verdict:** 8/9 gates pass; G4 defensible vs baseline. Cleared for Tier A.

## Tier A sample construction

- **Target:** 5,000 obs
- **Stratification:** 25 macro buckets, proportional with floor 50 / ceiling 1500
- **Random seed:** 20260614
- **Exclusions:** 99 cal100 obs already scored
- **Final:** 5,000 obs · 882 distinct studies
- **File:** `Perplexity_Only/prescience_tier_a_sample_v1.csv` (commit `d2f6abb7` on main)

Bucket allocation top 5:
- market-research: 1,165 / 4,678 available
- employer-internal: 576 / 2,355
- other: 457 / 1,883
- memoir: 390 / 1,619
- white-paper: 388 / 1,612

## Launch decision

After cal100 verdict + cost projection ($50–100 worst case for 19,844 sweep), Pete approved Tier A go.

Driver invocation issues hit:
1. First attempt: `FileNotFoundError` — Tier A file not built yet (Computer awaiting "yes, build 5,000" confirmation; Pete ran ahead)
2. After build + push: divergent branches on `git pull` (local commits not on origin); resolved via merge after vi editor escape
3. Pulled clean `d2f6abb7`; foreground run launched, Ctrl-C'd during first API call (terminal noise concern)
4. **Final launch: backgrounded with `nohup`, PID 73051**

## Operational state

- **PID:** 73051
- **Log:** `~/Desktop/Archive/logs/tier_a_run.log`
- **PID file:** `~/Desktop/Archive/logs/tier_a.pid`
- **Output:** `~/Desktop/Archive/pass_c_v6_tier_a_results.csv`
- **Scope:** 4,354 API calls + 4 pre-filter (target ~4,358 rows)
- **Expected wall:** ~12.5 hours at 8.66s/obs
- **Resumable:** yes (writes incrementally; resume logic respects baseline master)

## Acceptance plan (post-completion)

After Pete reports completion, Computer runs:
```bash
python3 prescience_acceptance_gates_v1.py \
  --batch ~/Desktop/Archive/pass_c_v6_tier_a_results.csv \
  --gates tier_a
```

Gates G1–G6 evaluated. If pass: promote to `_master_prescience_scores.csv` via `promote_pass_c_to_master_v1.py`. If fail: diagnose drift, decide whether to retry or escalate to manual review.

## Open backlog (Mac WORKLIST appendix, not yet committed)

- G4 calibration threshold tuning (raise to 60% permanently — current 55% is too tight against 67% baseline)
- Data hygiene audit: empty/bare `metric_value` rows (R5 pre-filter rule candidate)
- G4 vs baseline reconciliation note in PASS_C_RUNBOOK
- Type taxonomy hygiene: 137 case-variant types in `_master_studies.csv`
- preseed_b schema convention documentation in MASTERS_NOTES.md
- §11v PRESCIENCE ARCHITECTURE AUDIT (D6) — gates v1.7.0

## References

- Commit `aef5cc83`: Rebuild prescience master 3,761→4,082 rows
- Commit `b249408a`: Stage Pass C v6 driver + acceptance gates + calibration sample
- Commit `86398de3`: probe-2026-06-14 branch: 10-obs probe
- Commit `9b734bf6`: probe-2026-06-14 branch: 100-obs calibration results
- Commit `d2f6abb7`: Stage Tier A 5,000-obs stratified prescience sample
