# Decision: Add Short-Horizon Prescience Scoring (3-Year + 5-Year)

**Date:** 2026-06-15 (Monday, 11:31-11:49 EDT)
**Session:** §11v — Prescience Architecture Extension
**Status:** APPROVED — Design phase authorized
**Author:** Pete Kastner + Computer

---

## Trigger

Mid-session (Tier B running in background, ~5% complete), Pete raised a methodology question:

> "Prescience scores from date of Observation to today. What if we added a new '5-year prescience' score that the timeline to a more reasonable analyst 5-year future window? Desirability for research community?"

Computer produced a full proposal (`5_year_prescience_proposal_v1.md` shared as asset `0c7110ab-20e4-4a30-bf3f-0e4010af4b9d`) and Pete answered the 5 open questions.

## Decisions (Pete's verdict)

| # | Question | Decision |
|---|---|---|
| 1 | 3-year or 5-year window? | **Both** — bracket the analyst horizon |
| 2 | `-2` score for "too short to evaluate"? | **Yes** — adds honest "this obs predates evaluable evidence within window" signal |
| 3 | Run concurrent with Tier B/C/D or wait? | **Wait** — finish all-time sweep first, then short-horizon pass on the complete corpus |
| 4 | Memoir scoring anchor | **Event date** (year being narrated, not memoir publication date) |
| 5 | Cost ceiling $250-300? | **Acceptable** — budget approved |

> "Save this dialog as a decision. You have permission to do the architecture and design work."

Pete granted authorization for Computer to proceed with architecture and design (Phase 0 in proposal terminology) without waiting for further explicit go-ahead on each step.

## What's now in scope (architecture/design)

### Schema extensions to `_master_prescience_scores.csv`
New columns (added side-by-side with existing all-time scoring):

```
prescience_3y, confidence_3y, rationale_3y, scored_at_3y
prescience_5y, confidence_5y, rationale_5y, scored_at_5y
```

Total: 8 new columns, 19 column master.

### Score scale extension
- **-2** = "5-year (or 3-year) window predates evaluable evidence within window" (new convention)
- **-1** = pre-filter skip (existing convention)
- **0** = wrong, off-topic, refusal (existing)
- **1-5** = scaled prescience verdict (existing)

A row may have `prescience_5y=-2` while still carrying a valid `prescience_score=5` (long-runner that paid off eventually but couldn't be evaluated within 5 years).

### Memoir anchor rule
For memoir content (`type=memoir`), the scoring date anchor is **the event year being narrated**, not the memoir publication date. The driver must extract this from the observation's `period_start_year` or equivalent metadata. If neither exists, fall back to `study.published_at`.

This is consistent with Pete's framing: memoirs document past events; the prescience question is whether the *event's interpretation* held up within 3/5 years of the event, not within 3/5 years of writing the memoir.

### Sequencing
1. Tier B completes (in progress, PID 2163, ~28h remaining)
2. Tier C planned and run (~5,000 more obs)
3. Tier D planned and run (remaining ~486 obs)
4. **THEN** short-horizon pass begins on the complete ~24,000-row all-time scored master
5. 3-year pass first (smaller window = stricter test of methodology)
6. 5-year pass second (re-validate calibration)
7. Promote both to master as new columns

### Driver evolution
- v7 = network-hardened all-time scorer (current, running Tier B)
- v8 (TBD) = short-horizon scorer with `--horizon {3y, 5y}` flag, new prompt block, new column targets

### Acceptance gates
- New gates profile: `short_horizon_3y`, `short_horizon_5y`
- Compare 3y vs 5y distributions (they should differ visibly — refusal rate higher for 3y, score-5 lower for 3y)
- Compare both vs all-time (3y and 5y should be more conservative)
- Add G7 (new gate): **"-2 rate"** — flags if too many or too few obs are being marked "too short to evaluate"

### Cost projection
- Existing 8,440 master + Tier B 10K + Tier C/D 5K = ~24,000 obs at completion
- 3-year pass: ~24,000 × $0.012 = $288
- 5-year pass: ~24,000 × $0.012 = $288
- **Combined: ~$576** — exceeds the $250-300 ceiling Pete approved for "the 5-year sweep"

**ESCALATION NEEDED**: The $250-300 ceiling Pete approved likely contemplated 5-year only or a smaller corpus. Running BOTH 3-year and 5-year on the full ~24K corpus is ~$576. Options:
- (a) Increase budget to ~$600 for both passes
- (b) Do 3-year + 5-year only on calibration + Tier A (~9,500 obs = ~$228 total) and decide on full sweep later
- (c) Do 5-year only on full corpus, 3-year only on calibration + Tier A
- Computer will flag this to Pete before any short-horizon API calls are made.

## Phase 0 (design) deliverables — Computer producing

1. **System prompt template** for 3-year and 5-year framing (single shared template with parameterized window)
2. **Driver v8 spec** — new flags, new columns, new gates profile
3. **Calibration sample plan** — 100 obs cal100-equivalent for short-horizon
4. **MASTERS_NOTES.md proposed entry** documenting the new columns and `-2` convention
5. **Memoir anchor extraction logic** — concrete Python for `obs_date` resolution
6. **Cost gate** — explicit confirmation needed before short-horizon API calls

## Standing context (unchanged)

- D3 active: production master moves require preauthorization
- Sonar Reasoning Pro NOT Claude (cost minimization)
- Programmatic gates NOT human spot-check
- 200,000 credit ceiling + API costs
- Tier A complete, master at 8,440 rows
- Tier B running PID 2163

## Pete's authorization (verbatim)

> "Save this dialog as a decision. You have permission to do the architecture and design work."

Scope: Phase 0 design deliverables above. Does NOT include short-horizon API calls (still gated on Pete's confirmation after cost question resolved).

## Files

- `/home/user/workspace/5_year_prescience_proposal_v1.md` — original proposal
- `/home/user/workspace/decisions_log_entry_2026_06_15_short_horizon_prescience_v1.md` — this decision
- Future: `/home/user/workspace/short_horizon_design_v1.md` — Phase 0 design doc
- Future: scripts/run_prescience_pass_c_v8.py — short-horizon driver
- Future: scripts/prescience_acceptance_gates_v2.py — with G7 -2 gate
