# Short-Horizon Acceptance Gates v2

**Status:** DRAFT (Phase 0). Two-score-column aware.
**Predecessor:** Tier A gates (single-score `prescience` column), G1-G9 in `/tmp/tier_a/gates.py`.

---

## Conventions

- "per-score" gates run TWICE: once on `prescience_3y` cohort, once on `prescience_5y` cohort.
- "joint" gates use both columns simultaneously.
- "elapsed cohort" excludes `score = -2` rows from numerator AND denominator unless gate explicitly says otherwise.
- "scored cohort" excludes `-2`, `-1`, and empty/parse-fail rows.
- Pass threshold defaults to "warn but don't block" unless marked **HARD**. Pete is the final gate (per "I am not the accuracy gate" → programmatic G2c+G5 substitutes).

---

## G1 — Schema integrity **HARD**

All required new columns present and typed correctly. Pending rows have `score=-2 + confidence="" + rationale matches "window_not_elapsed:Ny:cutoff_YYYY"`. No-anchor rows have `score=-1 + rationale matches "no_anchor:.*"`.

PASS iff: 0 rows fail schema validation.

---

## G2 — Score distribution sanity (per-score, scored cohort)

### G2a Mean
3y mean ∈ [1.5, 3.5]; 5y mean ∈ [1.5, 3.5]. (Tier A baseline: mean ≈ 2.0 on 5,000 obs.)

### G2b Mode
Mode is not 0 AND not 5. (Both extremes dominating signals a degenerate run.)

### G2c Class balance ratio
`max_class / min_nonzero_class ≤ 4.0`. Tier A long-horizon gate value: 1.10. New 3y/5y baseline unknown — flag, don't block, on first calibration run; lock threshold after.

---

## G3 — Confidence distribution (per-score, scored cohort)

Confidence is int 1-3 (Tier A/B convention).

### G3a Class presence
All three confidence levels (1, 2, 3) appear at least once per horizon. If only 2 or 3 appears, model is refusing to mark anything low-confidence (uncalibrated).

### G3b Score-confidence monotonicity
Mean confidence at score=5 ≥ mean confidence at score=0. (Strong "wrong" verdicts should be as confident as strong "right" verdicts; if not, model is hedging on bad news.)

---

## G4 — Rationale quality (per-score, sampled)

Sample 50 scored rows per horizon. Each rationale must:
- be non-empty, ≥ 40 chars
- contain at least one 4-digit year matching the window `[A, A+N]`
- not contain hedging-only phrases ("likely", "possibly", "perhaps") without a concrete anchor fact

PASS iff: ≥ 90% of sampled rationales pass all three checks (raised from Tier A G4=55% per Pete's open backlog item).

---

## G5 — Programmatic accuracy floor **HARD**

For a held-out 100-obs calibration set with known-correct human verdicts (will need pre-build), per-score:
- 3y: % matching ≥ 65%
- 5y: % matching ≥ 65%

If calibration set not yet built: G5 marked DEFERRED in calibration report; full sweep gated on building it.

---

## G6 — Source-pass labeling **HARD**

Every row has exactly one `source_pass_sh` value from the locked set:
`{pass_c_sh_combined, pass_c_sh_3y_only, pass_c_sh_pending, pass_c_sh_no_anchor, pass_c_sonar_sh_v1_parse_fail}`.

PASS iff: 0 rows with empty or off-vocab `source_pass_sh`.

---

## G7 — Pending rate (joint, full cohort)

`pending_rate_3y = count(prescience_3y = -2) / total_rows`
`pending_rate_5y = count(prescience_5y = -2) / total_rows`

Expected today (anchors distributed Tier A-style):
- 3y pending rate: rows with anchor ∈ {2023, 2024, 2025, 2026} / total — likely 8-15% of recent corpus
- 5y pending rate: rows with anchor ∈ {2021..2026} / total — likely 15-25%

Flag (don't block) if either exceeds 35% — indicates corpus is heavily recent and short-horizon scoring is premature.

---

## G8 — windows_diverge rate AND model-vs-mechanical agreement (joint, both-elapsed cohort)

Of rows where both 3y and 5y are scored (not -1, not -2, not parse-fail):

### G8a Rate
`diverge_rate = count(windows_diverge = TRUE) / both_elapsed_count`

| diverge_rate | Verdict |
|---|---|
| < 2%   | Flag: model under-asserting divergence |
| 2-25%  | PASS |
| > 25%  | **HARD FAIL**: model over-asserting; review prompt before promote |

### G8b Model-vs-mechanical agreement (NEW v3)
Mechanical flag computed by promote script: `windows_diverge_mechanical = (|prescience_3y - prescience_5y| >= 2)`.

Agreement = `count(windows_diverge == windows_diverge_mechanical) / both_elapsed_count`.

| agreement | Verdict |
|---|---|
| ≥ 80%   | PASS |
| 60-80%  | Flag: produce mismatch report (`windows_diverge=TRUE, mechanical=FALSE` and vice versa) for hand review |
| < 60%   | Flag HARD: model's qualitative judgment systematically diverges from score arithmetic — investigate before promote |

Mismatches are NOT errors — they're the qualitatively interesting cases (e.g. model sees inflection at year 4 but final scores agree). The G8b report lists them; Pete decides whether to keep, retag, or re-prompt.

---

## G9 — Chronological monotonicity (joint, both-elapsed cohort)

For each `windows_diverge = TRUE` row, the divergence note must name a year strictly between `A+1` and `A+5` (i.e. the inflection point lies inside one of the windows).

PASS iff: ≥ 90% of diverge=TRUE rows have a parseable inflection year in `[A+1, A+5]`.

---

## G10 — Score-trajectory plausibility (joint, both-elapsed cohort)

Computed (not asked of model): for each both-elapsed row, classify into:

| 3y | 5y | label |
|---|---|---|
| 0 | 0 | both_wrong |
| 0 | ≥1 | late_vindication |
| ≥1 | 0 | reversal |
| ≥1 | ≥1, &#124;Δ&#124;≤1 | stable |
| ≥1 | ≥1, &#124;Δ&#124;≥2 | shift |

Expected rough distribution: stable ≫ both_wrong > shift > late_vindication > reversal.

Flag (don't block): reversal > 10% (suggests forecasts that "looked right" by 3y systematically failed by 5y — possible but worth Pete's eyes).

---

## Output

`gates_v2.py --input tier_X_results.csv --report tier_X_gates_report.json`

Report shape:
```
{
  "gate": "G2a_3y", "value": 2.13, "status": "PASS", "threshold": "[1.5, 3.5]"
  ...
}
```

Hard fails exit nonzero. Promote script reads the report and refuses to merge if any HARD gate failed.