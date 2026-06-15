# Decision: Short-Horizon Prescience Scoring (3y + 5y) — Spec Locked

**Date:** 2026-06-15 (Monday, 11:31-12:14 EDT)
**Session:** §11v — Prescience Architecture Extension
**Status:** SPEC LOCKED — Phase 0 design in progress
**Supersedes:** decisions_log_entry_2026_06_15_short_horizon_prescience_v1.md
**Author:** Pete Kastner + Computer

---

## Summary

Pete authorized adding short-horizon prescience scoring (both 3-year and 5-year windows) to the Aberdeen archive, alongside the existing all-time score. After two rounds of Socratic exchange that materially improved the spec, the architecture and definitional convention are now locked.

## Dialog narrative (preserved as part of the decision)

### Round 1 — Pete's original five questions, answered:

| # | Question | Decision |
|---|---|---|
| 1 | 3-year or 5-year window? | Both — bracket the analyst horizon |
| 2 | `-2` score for "too short to evaluate"? | Yes |
| 3 | Run concurrent with Tier B/C/D or wait? | Wait — finish all-time sweep first |
| 4 | Memoir scoring anchor | Event year (year being narrated) |
| 5 | Cost ceiling $250-300? | Approved |

### Round 2 — Pete's architecture question:

> "Could 3 AND 5-year results be done in one API call with two results (packaged to be split into 2 calculations)?"

Computer confirmed yes, and proposed combined-call architecture:
- Single API call produces JSON with both scores
- Adds `windows_diverge` boolean and `divergence_note` string for long-runner detection
- Cuts cost from ~$576 (dual-pass) to ~$288 (single-pass) — back inside Pete's original ceiling
- Methodologically superior: same evidence base reasoning for both windows in one `<think>` pass

### Round 3 — Pete's window-definition question:

> "What exactly does three years (five years) mean in time? Is January 2022 to December 2025 a 'three year window'? Let's do what researchers would expect. I have no stake in the outcome, so I favor scientific rigor."

Computer initially proposed excluding obs_year from the window (anchor_year+1 through anchor_year+N). Pete pushed back with the Anthropic IPO test case:

> "If in January 2026 I was quoted 'Anthropic will IPO within three years' that happened in June 2026 and would be excluded! as in the observation year. That's not right. Prove me wrong, please."

Pete was correct. Computer's original convention came from IMF/OECD macroeconomic forecasting (where forecasts are *about* specific future periods, so obs_year evidence is contemporaneous). Aberdeen observations are mostly **duration-bounded predictions** ("X will happen within N years") where the clock starts at utterance. Excluding obs_year would:
- Methodologically penalize Anthropic-style "within 3 years" calls that pay off quickly
- Create spurious January-vs-December asymmetry
- Violate face-value semantics of "within N years"

Convention corrected to include obs_year. Pete acknowledged the `-2` edge case for current-year obs but noted:

> "I don't like your Anthropic = -2 but I will live with it. 99% of the archive is history and well beyond any windows. I won't be making many public, quotable future calls, so waiting out the window to score is a fool's errand."

Pete's final word:

> "Lock the spec, update decisions, greenlight. [I am enjoying this]"

---

## LOCKED SPEC

### Anchor year resolution

For each observation, resolve a single integer `anchor_year`:

1. If obs has explicit `obs_date` field (rare): use year component
2. Else if study has `period_start_year` AND `type=memoir`: use that (memoir event year, per Pete's Round 1 decision)
3. Else if study has `published_at`: use year component
4. Else: **hard fail** — surface in prefilter for manual review

### Window definition

**3-year window:** `[anchor_year, anchor_year + 3]` inclusive
**5-year window:** `[anchor_year, anchor_year + 5]` inclusive

Both windows INCLUDE the anchor year itself.

Examples:
- obs anchored 1995 → 3y window = 1995-1998 (4 calendar years), 5y window = 1995-2000 (6 calendar years)
- obs anchored 2026 (current year) → 3y window = 2026-2029, 5y window = 2026-2031
- obs anchored 1979 (DECtp memoir) → 3y window = 1979-1982, 5y window = 1979-1984

### `-2` scoring rule (window not elapsed)

Score `-2` ONLY when the window's final year has not yet completed.

Today (2026-06-15):
- Last fully-elapsed year = 2025
- 3y cutoff: anchor_year ≤ 2022 → scoreable; anchor_year ≥ 2023 → `-2`
- 5y cutoff: anchor_year ≤ 2020 → scoreable; anchor_year ≥ 2021 → `-2`

This is the strictest defensible rule (no partial-window scoring). Pete accepted that some current-year obs (like the hypothetical Anthropic 2026 example) get tagged `-2` for now and become scoreable in 2030 — acceptable because the archive is 99% history.

### Combined-call architecture

Single Sonar Reasoning Pro API call per observation. Both 3y and 5y scores produced in one structured JSON response.

Required output fields:
```json
{
  "prescience_3y": int (-2 to 5),
  "confidence_3y": int (1-3),
  "rationale_3y": str (target 200-800 chars),
  "prescience_5y": int (-2 to 5),
  "confidence_5y": int (1-3),
  "rationale_5y": str (target 200-800 chars),
  "windows_diverge": bool,
  "divergence_note": str (empty unless |3y - 5y| >= 2)
}
```

`windows_diverge=true` is set by the model when the 3y and 5y verdicts differ by ≥2 points OR when one is `-2` and the other is positive. `divergence_note` documents *what happened between years 3 and 5* (e.g., "Adoption inflected late; the call was directionally right early but only materially validated in year 4-5.").

### Score scale (extended)

- **-2** = window not yet elapsed (new convention)
- **-1** = pre-filter skip (existing; figure caption, omitted image, etc.)
- **0** = wrong, off-topic, refusal (existing)
- **1** = very weak / mostly wrong
- **2** = weak / partly right
- **3** = moderately prescient
- **4** = strongly prescient
- **5** = transformative call, unambiguously prescient

### Memoir handling

For `type=memoir` observations, the anchor year is the **event year being narrated**, NOT the memoir's publication year. This was Pete's Round 1 decision (#4) and is preserved.

Memoir example: DECtp Plaza Hotel chapter narrates 1979 events. Memoir was written 2025. anchor_year = 1979. 3y window = 1979-1982. 5y window = 1979-1984.

### Evidence cutoff in system prompt

The prompt must explicitly include both year-bounded cutoffs:

> "For the 3-year score: evaluate using evidence about what happened between {anchor_year}-01-01 and {anchor_year+3}-12-31. Reason about whether the observation's claim, prediction, or recommendation was vindicated within that window.
>
> For the 5-year score: evaluate using evidence between {anchor_year}-01-01 and {anchor_year+5}-12-31. The 5-year window extends the 3-year window by two more years.
>
> Important: evidence available after {anchor_year+5}-12-31 may be in your training data but must NOT influence either score. Reason about each window independently, then identify whether they diverge."

### Schema additions to `_master_prescience_scores.csv`

```
prescience_3y          int       -2 to 5 (window not elapsed = -2)
confidence_3y          int       1-3
rationale_3y           str       
prescience_5y          int       -2 to 5
confidence_5y          int       1-3
rationale_5y           str
windows_diverge        bool      true if |3y - 5y| >= 2 OR one is -2 and other positive
divergence_note        str       populated only when windows_diverge=true
anchor_year            int       integer year used as scoring anchor
scored_at_sh           str       ISO timestamp of short-horizon scoring run
scorer_version_sh      str       e.g., 'v8'
source_pass_sh         str       e.g., 'pass_d_combined_v1'
```

Eleven new columns total. Brings master from 11 cols to 22 cols.

### Driver v8 (combined short-horizon)

Successor to v7 (network-hardened all-time scorer). Key changes:
- New `--scoring-mode short-horizon-combined` flag (only mode in v8)
- New system prompt block with window cutoffs interpolated
- New JSON schema requirement (8 required fields vs v7's 3)
- New target columns
- Anchor year resolution logic (3-tier fallback with hard-fail)
- `-2` auto-assignment for obs where window's final year > current year
- `max_tokens` bumped 1200 → 2000 to accommodate dual rationales

### Acceptance gates v2

New profile `short_horizon_combined`. All existing gates G1-G6 apply per-score-column (so 2x). Plus new gates:

- **G7 `-2` rate sanity:** flag if `-2` rate differs from expected (~5% for 3y, ~8% for 5y based on anchor_year distribution)
- **G8 windows_diverge rate sanity:** expect 10-25% of obs to have meaningful 3y/5y divergence; flag if <5% (model is collapsing windows) or >40% (model is over-distinguishing)
- **G9 chronological monotonicity:** `prescience_5y` should equal `prescience_3y` OR be one step closer to "validated" in most cases. Flag if 5y < 3y in more than 10% of rows (would indicate model is contradicting itself).

### Sequencing

1. Tier B completes (in progress, ~28h remaining)
2. Tier C planned and run
3. Tier D planned and run
4. **All-time master complete** (~24,000 rows)
5. Short-horizon Phase 1: 100-obs cal-equivalent calibration
6. Short-horizon Phase 2: full corpus combined-call sweep
7. Promote both new score columns + 9 metadata columns to master

### Cost (revised under combined-call architecture)

- Combined 3y+5y on full ~24K corpus: ~$288 (one call per obs)
- Plus calibration (~100 obs): ~$2
- **Total: ~$290** — within Pete's original $250-300 ceiling

### Out of scope (Pete confirmed)

- Anniversary-date precision (year-resolution only)
- Month-resolution windows for high-precision obs
- 1-year or 10-year additional windows (just 3y and 5y for now)
- Backfilling obs that auto-tag `-2` later (re-score in future years if needed)

---

## What Computer will produce in Phase 0

1. ✓ This decision document (locking spec)
2. Combined-call system prompt (parameterized for window cutoffs)
3. Driver v8 spec (TBD, includes anchor year resolution + window math + `-2` auto-tag)
4. MASTERS_NOTES.md proposed schema entry (22-column convention)
5. Acceptance gates v2 spec (G1-G9, two-score-column aware)
6. Calibration sample plan (100 obs, stratified, anchored 2020 or earlier so 5y is scoreable)
7. Anchor-year resolution module (Python, with hard-fail surface)
8. Cost-gate one-pager (confirms $290 vs $300 ceiling before any API calls)

NOT in Phase 0: actual API calls. Pete's authorization is for design only; short-horizon scoring waits until full all-time master is complete (Tier B/C/D done).

---

## Pete's authorizations (verbatim, this session)

- "Save this dialog as a decision. You have permission to do the architecture and design work."
- "Lock the spec, update decisions, greenlight."

Scope: Phase 0 design deliverables. Does NOT extend to API calls.

## Cross-references

- `Archive/decisions/5_year_prescience_proposal_v1.md` (original analysis)
- `Archive/decisions/decisions_log_entry_2026_06_15_short_horizon_prescience_v1.md` (v1 of this decision, now superseded)
- `_master_prescience_scores.csv` (current 8,440 rows, all-time only)
- `scripts/run_prescience_pass_c_v7.py` (current driver, all-time, network-hardened)
- Tier B in progress: PID 2163, output `~/Desktop/Archive/pass_c_v6_tier_b_results.csv`