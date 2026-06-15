# Decision: Short-Horizon Prescience Scoring (3y + 5y) — Spec Locked v3

**Date:** 2026-06-15 (Monday, 11:31 EDT spec lock → 15:15 EDT Phase 0 reconciliation)
**Session:** §11v — Prescience Architecture Extension
**Status:** SPEC LOCKED v3 — Phase 0 deliverables drafted; awaiting Tier B completion before any API calls
**Supersedes:**
- `decisions_log_entry_2026_06_15_short_horizon_prescience_v1.md`
- `decisions_log_entry_2026_06_15_short_horizon_prescience_v2.md` (committed to repo `cf4225f3`)

**Author:** Pete Kastner + Computer

---

## Summary

Pete authorized adding short-horizon prescience scoring (3y AND 5y, combined single-call) to the Aberdeen archive alongside the existing all-time score. v2 locked the spec; v3 reconciles Phase 0 draft deliverables back into the decision doc, resolves four open asks (sonar-pro confirmed, confidence type, anchor_source kept, windows_diverge dual-source, column count), and locks the strict window-elapsed rule.

## v3 changes vs v2 (reconciliation)

| # | Item | v2 | v3 |
|---|---|---|---|
| 1 | Model | unspecified | **sonar-pro** (no downgrade; Pete confirmed) |
| 2 | Confidence column type | conflict (`int 1-3` in schema, float assumed elsewhere) | **int 1-3** — matches existing Tier A/B convention exactly |
| 3 | Window-elapsed rule | "anchor ≤ 2022 / ≤ 2020" implied | **STRICT: `today_year > anchor_year + horizon`** (rationale below) |
| 4 | Pending row shape | not specified | **`score=-2, confidence="", rationale="window_not_elapsed:Ny:cutoff_YYYY"`, no API call** |
| 5 | windows_diverge logic | "set by model when \|3y-5y\|≥2 OR sign flip" (mechanical) | **DUAL: model asserts + post-hoc mechanical cross-check + G-gate flags mismatches** |
| 6 | anchor_source column | not present | **kept** (audit value; Pete's call) |
| 7 | raw_response_sh column | not present | **kept** (parse-fail retry; Tier A had 52 parse failures, 1.2%) |
| 8 | legacy_sh_id reservation | not present | **dropped** (YAGNI; greenfield scoring has no legacy IDs to normalize) |
| 9 | Total new columns | 11 | **14** |
| 10 | Calibration timing | "after all-time complete" | **after Tier B completes specifically** (no parallel thrash with PID 2163) |

---

## Dialog narrative (preserved as part of the decision)

### Round 1 — Pete's original five questions

| # | Question | Decision |
|---|---|---|
| 1 | 3y or 5y window? | Both — bracket the analyst horizon |
| 2 | `-2` score for "too short to evaluate"? | Yes |
| 3 | Concurrent with Tier B/C/D or wait? | Wait — finish all-time sweep first |
| 4 | Memoir scoring anchor | Event year (year being narrated) |
| 5 | Cost ceiling $250-300? | Approved |

### Round 2 — Combined-call architecture

Pete: "Could 3 AND 5-year results be done in one API call with two results?"

Computer confirmed. Combined call cuts cost ~$576 → ~$288, methodologically superior (same evidence base reasoning for both windows in one `<think>` pass), enables `windows_diverge` detection in a single response.

### Round 3 — Window-definition rigor

Pete pushed back on Computer's initial "exclude obs_year" convention with the Anthropic IPO test case (obs January 2026 → event June 2026 should NOT be excluded). Pete was correct. Aberdeen observations are duration-bounded predictions ("within N years") where the clock starts at utterance — not period-targeted forecasts like IMF macro projections. Convention corrected to **include obs_year**. Pete's final: "Lock the spec, update decisions, greenlight."

### Round 4 — Phase 0 reconciliation (this v3 doc)

Computer drafted six Phase 0 deliverables (resolver module, prompt, driver v8 spec, gates v2 spec, calibration plan, MASTERS_NOTES schema entry). Self-test on the resolver surfaced a spec ambiguity in the window-elapsed cutoff. Pete's three resolutions (sonar-pro, anchor_source keep, calibration after Tier B) plus the four prior locks now consolidated here.

---

## LOCKED SPEC v3

### Anchor year resolution

Per `anchor_year_resolver_v1.py` (workspace, self-test PASS):

1. `obs_date` year (if present)
2. `period_start_year` (ONLY when `study.type == 'memoir'`)
3. `study.published_at` year
4. **Hard fail** → `AnchorResolutionError` → driver tags row `score=-1, rationale="no_anchor:<msg>", source_pass_sh="pass_c_sh_no_anchor"`

Resolved year stored in `anchor_year`; provenance in `anchor_source` ∈ `{obs_date, memoir_period_start, study_published_at}`.

### Window definition (BOTH include anchor year)

- **3y:** `[anchor_year, anchor_year + 3]` inclusive (4 calendar years)
- **5y:** `[anchor_year, anchor_year + 5]` inclusive (6 calendar years)

### `-2` rule — STRICT

```
elapsed iff today_year > anchor_year + horizon
```

Today (2026-06-15) cutoffs:
- 3y: anchor ≤ 2022 scoreable; anchor ≥ 2023 → `-2`
- 5y: anchor ≤ 2020 scoreable; anchor ≥ 2021 → `-2`

Rationale: a window whose final year is the current calendar year is not yet complete; scoring it before December 31 would mix elapsed and non-elapsed evidence. Strict rule treats the full final year as "must be in the past" before scoring.

### Pending row shape (driver short-circuits, NO API call)

```
prescience_Ny  = -2
confidence_Ny  = ""
rationale_Ny   = "window_not_elapsed:Ny:cutoff_YYYY"
```

Both-pending rows: `source_pass_sh = "pass_c_sh_pending"`. Cost: $0 per row.

### Combined-call architecture (sonar-pro)

Single API call per observation when at least one window is elapsed. JSON output:

```json
{
  "prescience_3y":   <int -2|0..5>,
  "confidence_3y":   <int 1..3>,
  "rationale_3y":    "<str>",
  "prescience_5y":   <int -2|0..5>,
  "confidence_5y":   <int 1..3>,
  "rationale_5y":    "<str>",
  "windows_diverge": <bool>,
  "divergence_note": "<str, empty unless windows_diverge=true>"
}
```

Model is asked to assert `windows_diverge` based on evidence (not score arithmetic). Post-hoc cross-check: mechanical flag `windows_diverge_mechanical = (|3y - 5y| >= 2)` computed by promote script. G-gate flags mismatches between model-asserted and mechanical for hand review. Both signals preserved.

### Score scale

- `-2` = window not elapsed (pending, no API call)
- `-1` = pre-filter / no_anchor / parse_fail
- `0` = wrong
- `1..5` = scaled prescient (5 = transformative)

### Memoir handling

`anchor_year` = event year being narrated, NOT memoir publication year. DECtp Plaza Hotel chapter (events 1979, written 2025) → anchor_year = 1979.

### Evidence cutoff in system prompt

The prompt explicitly instructs:
> For the 3y score, use evidence about events in `[anchor_year, anchor_year+3]`. For the 5y score, use evidence about events in `[anchor_year, anchor_year+5]`. Evidence after `anchor_year+5` may be in your training data but MUST NOT influence either score. Reason about each window independently, then identify whether they diverge.

Full prompt in `short_horizon_prompt_v1.md`.

---

## Schema — 14 new columns on `_master_observations.csv`

| # | Column | Type | Notes |
|---|---|---|---|
| 1 | `prescience_3y` | int | `{-2,-1,0..5}` |
| 2 | `confidence_3y` | int \| "" | `1..3` or empty for -2/-1 rows |
| 3 | `rationale_3y` | str | scored: model text; pending: `window_not_elapsed:3y:cutoff_YYYY`; no-anchor: `no_anchor:<msg>` |
| 4 | `prescience_5y` | int | same domain as 3y |
| 5 | `confidence_5y` | int \| "" | same as 3y |
| 6 | `rationale_5y` | str | same as 3y |
| 7 | `windows_diverge` | bool \| "" | model-asserted; "" for non-both-elapsed rows |
| 8 | `divergence_note` | str | empty unless `windows_diverge=true` |
| 9 | `anchor_year` | int | resolved year |
| 10 | `anchor_source` | str | `{obs_date, memoir_period_start, study_published_at}` |
| 11 | `scored_at_sh` | ISO8601 | UTC timestamp |
| 12 | `scorer_version_sh` | str | `pass_c_sonar_sh_v1` \| `pass_c_sonar_sh_v1_parse_fail` |
| 13 | `source_pass_sh` | str | `{pass_c_sh_combined, pass_c_sh_3y_only, pass_c_sh_pending, pass_c_sh_no_anchor}` |
| 14 | `raw_response_sh` | str \| "" | raw API response (empty for pending/no_anchor); preserves parse-fail rows for retry |

**Dropped from v2 draft:** `legacy_sh_id` reservation (YAGNI — short-horizon is greenfield).

**Independence invariant:** SH columns NEVER overwrite or reference the existing long-horizon `prescience`/`confidence`/`rationale` columns. The two scoring runs are independent.

`score_trajectory` (stable/late_vindication/reversal/shift/both_wrong) lives in DuckDB view `v_short_horizon_obs`, NOT as a physical master column. Consistent with Pete's "keep computed cheap" pattern.

Full schema entry in `masters_notes_sh_schema_entry_v1.md`.

---

## Acceptance Gates v2

Profile `short_horizon_combined`. G1-G10 in `short_horizon_acceptance_gates_v2_spec.md`:

- **G1** schema integrity (HARD)
- **G2a-c** score distribution per-horizon
- **G3a-b** confidence range + score-confidence monotonicity (adjusted for int 1-3 scale)
- **G4** rationale quality (≥ 90% must cite year inside window)
- **G5** programmatic accuracy floor ≥ 65% per horizon on calibration set (HARD)
- **G6** source-pass labeling (HARD)
- **G7** pending-rate sanity
- **G8** windows_diverge rate (HARD FAIL > 25%; flag < 2%)
- **G9** chronological monotonicity for diverge=true rows
- **G10** score-trajectory plausibility (reversal > 10% → flag)

Promote script reads G-report; refuses to merge if any HARD gate failed.

---

## Driver v8

Spec: `driver_v8_spec_v1.md`. Inherits v7 network hardening (timeout 120, retries 5, full exception tuple). New:

- Imports `anchor_year_resolver_v1`
- Pre-API resolution + pending short-circuit
- Combined-call prompt + JSON schema
- `max_tokens` 1200 → 2000
- 14 new output columns
- `MODEL = "sonar-pro"`, `TEMPERATURE = 0.0`
- `TODAY_YEAR = 2026` as explicit constant (NOT `datetime.now().year`) for run-stability across day boundaries

---

## Calibration plan

`short_horizon_calibration_plan_v1.md`. 100-obs stratified sample, anchor ≤ 2020 (both windows elapsed). Run AFTER Tier B completes (Pete: "no thrashing"). Cost ~$6.50 (calibration + Claude Opus adjudicator for G5 proxy). Pete GO/NO-GO gates the full sweep.

---

## Sequencing (v3 locked)

1. **Tier B in progress** (PID 2163, ~28h remaining as of 2026-06-15 ~15:00 EDT)
2. Tier C, Tier D
3. All-time master complete (~24K rows)
4. **SH calibration** (100 obs, ~$6.50)
5. Pete review + GO/NO-GO
6. **SH full sweep** (combined call, ~$288, ~24K rows)
7. Promote 14 new columns + build `v_short_horizon_obs` DuckDB view

---

## Cost ceiling (revised)

- Calibration: ~$6.50
- Full sweep: ~$288
- **Total: ~$294.50** — within Pete's $250-300 ceiling (plus ~5% buffer for retry pass)

---

## Phase 0 deliverables (drafted in workspace, this session)

1. ✓ This decision document (v3, supersedes v2)
2. ✓ `anchor_year_resolver_v1.py` — self-test PASS
3. ✓ `short_horizon_prompt_v1.md` — combined + 3y-only prompts
4. ✓ `driver_v8_spec_v1.md` — full spec, no code yet
5. ✓ `masters_notes_sh_schema_entry_v1.md` — 14-column convention
6. ✓ `short_horizon_acceptance_gates_v2_spec.md` — G1-G10
7. ✓ `short_horizon_calibration_plan_v1.md` — 100-obs plan + GO/NO-GO

**NOT in Phase 0:** API calls. Pete's authorization is design only.

---

## Pete's authorizations (verbatim, this session)

- "Save this dialog as a decision. You have permission to do the architecture and design work."
- "Lock the spec, update decisions, greenlight."
- "Keep the locked spec as-is. No change." (on score_trajectory column proposal)
- "1 sonar pro. Why downgrade? 2 your choice. 3 wait so no thrashing. 4 update Pete's design MD to v2." (Phase 0 reconciliation asks)

Scope: Phase 0 design deliverables. Does NOT extend to API calls.

---

## Cross-references

- `Archive/decisions/5_year_prescience_proposal_v1.md` (original analysis)
- `Archive/decisions/decisions_log_entry_2026_06_15_short_horizon_prescience_v1.md` (superseded)
- `Archive/decisions/decisions_log_entry_2026_06_15_short_horizon_prescience_v2.md` (superseded, repo commit `cf4225f3`)
- `_master_observations.csv` (current 8,440 rows scored, all-time only)
- `scripts/run_prescience_pass_c_v7.py` (current driver, all-time, network-hardened)
- Tier B in progress: PID 2163, output `~/Desktop/Archive/pass_c_v6_tier_b_results.csv`