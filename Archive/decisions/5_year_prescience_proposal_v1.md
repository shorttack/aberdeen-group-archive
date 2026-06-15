# 5-Year Prescience Score — Proposal & Analysis

**Author:** Computer (for Pete Kastner)
**Date:** 2026-06-15
**Context:** Aberdeen archive prescience scoring methodology
**Status:** Proposal for discussion — not yet implemented

---

## TL;DR

**Yes, add a 5-year prescience score (`prescience_5y`) alongside the existing observation-to-today score (`prescience`).** The research community will find the 5-year window substantially more useful for three reasons:

1. **It matches how analysts actually work.** Forecasting horizons of 18 months to 5 years are the bread and butter of industry research; 20-50 year retrospectives are interesting but rare in practice.
2. **It separates "useful foresight" from "lucky long bets."** A call that paid off in 4 years is genuinely actionable; a call that paid off in 25 years is statistically indistinguishable from broken-clock-right.
3. **It enables comparison across decades.** Right now a 1995 observation is being judged against 31 years of subsequent history while a 2020 observation has only 6. Normalizing to a fixed 5-year window puts every analyst call on the same scoring footing.

The proposal is **additive, not replacement.** Keep the existing all-time score (it's already computed and is publishable history). Add the 5-year score for analytical utility.

---

## Current state

The Aberdeen archive prescience master (`_master_prescience_scores.csv`, 8,440 rows as of 2026-06-15) scores each observation on a 0-5 scale where:

- The scorer (Sonar Reasoning Pro, Claude Sonnet 4.6, or human author) is asked to judge: **"Did this prediction or recommendation prove correct in light of everything that happened between the observation date and today (2026)?"**
- Score 5 = unambiguously prescient, played out as predicted, transformative call
- Score 0 = wrong, off-topic, or unscoreable
- Score -1 = pre-filter rejection (image content, figure caption, etc.)

**The implicit horizon is "observation date to 2026."** For a 1979 Prime Computer note that's 47 years. For a 2024 AI observation that's 2 years. These are not comparable.

---

## The 5-year score concept

Add a new column: `prescience_5y` with the same 0-5 scale, asked of the same content, but with the question reframed:

> "Within FIVE YEARS of the observation date, did this prediction or recommendation prove correct in light of what happened in that window?"

For a 1979 observation, the scoring evidence base is bounded by 1979-1984. The scorer is asked to ignore everything after 1984 (or weight it as confirmatory only).

### Why 5 years specifically

- **Analyst forecasting norms:** Gartner Magic Quadrants are 5-year outlooks. Forrester Wave reports cite 3-5 year horizons. Aberdeen's own legacy work (Sectoral Reports, Vendor Profiles) was sold on the premise that the guidance would be relevant through the buyer's next infrastructure refresh — typically 3-5 years.
- **Tech adoption S-curves:** Most enterprise tech moves from "early adopter" to "early majority" in 4-7 years (Rogers diffusion, Moore's chasm-crossing). A 5-year window catches whether the adoption curve actually started.
- **Memory and accountability:** Five years is long enough that the call was non-trivial, short enough that the analyst was still in the same role and could be held accountable. Twenty-year retrospectives are interesting; five-year ones are evaluable.
- **Causality:** The longer the window, the more confounders (M&A, regulatory shifts, recessions, new technologies). Five years keeps the causal chain auditable.

### What 5-year scoring changes

| Aspect | All-time score (current) | 5-year score (proposed) |
|---|---|---|
| Question | Was this right by 2026? | Was this right by obs_date + 5 years? |
| Evidence base | Everything since observation | Strictly bounded window |
| Best-case call type | Civilizational bets | Actionable analyst calls |
| Penalizes | Slow plays that took >5 yr | Lucky long-runners |
| Comparable across eras | No (uneven horizons) | Yes (fixed window) |
| Audit difficulty | High (whole post-obs history) | Moderate (5-yr window) |

### What does NOT change

- The observation text itself
- The 0-5 score scale
- The confidence (1-3) scale
- The source_pass tagging convention
- The rationale field structure
- The scorer model (Sonar Reasoning Pro for v7+)
- The acceptance gates (G1-G6 still apply per-column)

---

## Schema impact

### Option A: Two columns side-by-side (recommended)

Add to `_master_prescience_scores.csv`:

```
obs_id, study_id, model, prescience_score, confidence, rationale,
scored_at, scorer_version, source_pass, elapsed_sec, parse_ok,
prescience_5y, confidence_5y, rationale_5y, scored_at_5y       ← NEW
```

- Existing all-time score is **preserved unchanged** for every row already scored
- New 5-year columns populate as you run the dedicated 5-year pass
- Empty values legal during transition

### Option B: Separate master file

Create `_master_prescience_scores_5y.csv` with the 5-year scores only, joined on `obs_id`.

- Pro: keeps the current master untouched; simpler for analytics that don't want the 5-year view
- Con: another file to keep in sync; doubles the join surface for the wiki and DuckDB layer

**Recommendation: Option A.** The cost of a few empty columns is trivial; the cost of two-file sync drift is real. The wiki builder, DuckDB queries, and `v_studies` view can all expose 5-year as optional columns.

---

## Cost & operational impact

### Per-row cost
- 5-year pass is a separate API call per obs (same Sonar Reasoning Pro)
- ~$0.012 per scored obs (Tier A actual) × 8,440 = **~$100 for the existing master**
- Plus ~$100 for Tier B once complete (~10,000 more obs)
- **Total 5-year sweep cost projection: ~$200-250**

### Throughput
- Same 5.7 calls/min as v7 driver
- 8,440 obs × 9s avg = ~22 hours wall time for the existing master
- Tier B 10,000 obs = ~29 hours
- Combined: ~50 hours, runnable across 3-4 overnight sessions

### Code changes
- New driver flag: `--scoring-mode {all-time, 5y}` (default `all-time`)
- New system prompt block for 5-year framing (insert obs_date + 5 in the prompt)
- New target column for output (`prescience_5y` instead of `prescience_score`)
- New gates profile (`tier_5y`) since the distribution will look different
- Promote script learns about the new columns

Estimated effort: 4-6 hours of coding + a calibration cal100-equivalent run before any Tier-scale work.

---

## Research community desirability

### For working analysts (Gartner, Forrester, IDC, in-house corp strat)
**High desirability.** The 5-year score directly answers the question they get paid to ask: "Is this analyst's forecast useful for my 2-5 year planning cycle?" The all-time score answers an interesting but less actionable question.

### For academic researchers (technology forecasting, business history)
**High desirability.** Innovation-diffusion literature (Rogers, Bass, Christensen) is built on 3-7 year diffusion windows. A 5-year prescience corpus aligns directly with their existing instruments. The Aberdeen archive becomes a publishable dataset for forecasting-accuracy meta-analysis.

### For the analyst community itself (Aberdeen alumni, industry peers)
**Very high desirability.** A 5-year score is a fair self-assessment yardstick: "Within the planning horizon I was asked to forecast, was I right?" The all-time score sometimes rewards or punishes things outside the analyst's commissioned window, which feels unfair on both ends (lucky long bets and unlucky slow plays).

### For Pete's broader project goals
- **Memoir credibility:** "I was right within 5 years on X% of calls, and right eventually on Y%" is a sharper story than just "right eventually."
- **Methodology paper potential:** A two-column prescience scoring methodology (short-horizon + long-horizon) is itself a publishable contribution.
- **AI-readiness training data:** If you ever fine-tune an LLM on the archive, 5-year prescience labels are higher signal than all-time (less confounded by post-hoc rationalization).

### For Bill Wallet & co-authors
Mixed-but-mostly-positive. Likely opens debate on whether 3 years or 7 years is the right window (defensible answers exist for each). Worth piloting on the existing 8,440-row master before committing to the 19,844-obs sweep.

---

## Risks and counter-arguments

### Risk 1: Scorer can't ignore future information
Even told to evaluate "by 1984 only," the model knows what happened by 2026 and may leak that into the 5-year score. Mitigation: include explicit evidence-cutoff instructions in the system prompt; spot-check 50 rows manually; compare 5-year vs all-time score distributions for telltale patterns (if they're identical, the 5-year framing failed).

### Risk 2: Some observations don't fit a 5-year window
A 1979 observation about "the future of computing" is inherently long-horizon. Forcing a 5-year score creates noise. Mitigation: allow a -2 score meaning "5-year window too short for this observation type" (separate from -1 pre-filter and 0 wrong/refusal).

### Risk 3: Doubles maintenance burden
Two scores means two scoring passes, two backfill workflows, two sets of gates. Mitigation: build the 5-year pass once on the existing master, then make it part of standard onboarding for new studies. Same gates apply with adjusted thresholds.

### Risk 4: Confuses end-users
"Which score do I cite?" Mitigation: documentation. Default to 5-year for forward-looking analytics, all-time for historical-record analytics. Wiki templates should display both side-by-side with brief explanations.

### Counter-argument: "Just use observation date + filter post-hoc"
You could compute a pseudo-5-year score from the all-time score by examining what evidence the scorer cited and rejecting evidence after obs_date + 5. **Why this fails:** the existing rationales are not structured to cite dates of evidence, so you can't reliably know which evidence is within the 5-year window. Re-scoring with the constrained question is cleaner.

---

## Recommended next steps

If you decide to pursue this:

### Phase 0 — Design (1 day)
- Lock the 5-year system prompt
- Add `-2` score convention if you want it
- Document the new schema columns in `MASTERS_NOTES.md`

### Phase 1 — Calibration (1 day)
- Pull a 100-obs sample stratified the same way as cal100
- Score in 5-year mode with v7-derived `v8` driver
- Compare 5-year vs all-time distributions — should differ visibly but not pathologically
- Spot-check 25 rows manually to verify the model is actually constraining its evidence

### Phase 2 — Full sweep on existing master (~22 hours)
- Score all 8,440 obs in 5-year mode
- Run dedicated 5-year gates profile
- Promote to master as new columns

### Phase 3 — Pipeline integration (1 day)
- Wiki templates display both scores
- DuckDB views expose both via `study_prescience_5y_enum` alongside existing `study_prescience_enum`
- Pass C runbook documents both modes

### Phase 4 — Analysis & publication (open-ended)
- Compute "5-year accuracy by decade" rollup
- Compute "long-runner premium" (5y score vs all-time delta by study)
- Draft a methodology note for archive consumers

---

## Specific Aberdeen archive considerations

A few wrinkles that matter for the Aberdeen corpus specifically:

1. **Aberdeen's research cycle was 3-5 years.** Most reports were sold with implicit 3-year refresh cycles. A 3-year prescience score might actually map *better* to Aberdeen's commissioned horizon than 5-year. Consider piloting both 3-year and 5-year and seeing which yields cleaner distributions.

2. **Memoir content is post-hoc.** Volume 1 chapters were written 2025-2026 looking backward. A 5-year score on a memoir observation is asking "in the 5 years after the *event being described* (e.g., 1985 Stratus fault-tolerant era), did the memoir's interpretation prove right?" That's a coherent question but worth flagging in the prompt.

3. **DCT studies have multiple dates.** DCT (vendor/category) studies were updated yearly. Should the 5-year window run from initial publication, last revision, or some weighted midpoint? Recommend: use `study.published_at` (initial) for the prescience anchor.

4. **Press-news observations are inherently short-cycle.** A 1995 ComputerWorld news item about an IBM announcement is already a near-term call. 5-year scoring is the natural fit; all-time scoring is mildly absurd for this content type.

5. **Player rebuttals are time-stamped.** The `_master_player_rebuttals.csv` mechanism already has scorer-time vs observation-time distinction. The 5-year score reinforces this discipline.

---

## My recommendation

**Build it.** The cost is modest (~$200, ~50 hours wall, ~1-2 weeks of coding/runs). The research-community value is high. The methodological elegance — fixed-horizon scoring on a 50-year corpus — is novel enough to be publishable as its own contribution to forecasting-accuracy literature.

**Pilot first** on 100 obs in cal100-style format before committing to the full sweep. If the 5-year distribution looks distinctly different from all-time (which is the whole point), you've validated the methodology. If they look identical, the prompt isn't constraining the model and you need to iterate.

**Keep both scores.** All-time is publishable history; 5-year is publishable analytics.

---

## Open questions for Pete

1. **3-year or 5-year window?** Or both? (Bracketing forecasts can be valuable.)
2. **`-2` score for "too short to evaluate"** — yes or no?
3. **Run 5-year pass concurrent with Tier B/C/D**, or wait until full archive is all-time scored?
4. **Memoir scoring anchor:** event date or memoir publication date?
5. **Acceptable cost ceiling for the 5-year sweep:** is $250-300 in budget?

---

## Sources & references

- Diffusion of Innovations (Rogers, 1962/2003) — 4-7 year adoption windows
- Crossing the Chasm (Moore, 1991) — early-majority transition timing
- Gartner Magic Quadrant methodology — 5-year forward outlook
- Forrester Wave methodology — 3-5 year strategic horizon
- Aberdeen historical methodology: 3-year report refresh cycle
- Internal: `_master_prescience_scores.csv` (8,440 rows, 2026-06-15)
- Internal: cal100 calibration results (`9b734bf6` on main)
- Internal: Tier A acceptance gates report (`prescience_acceptance_gates_v1.py`)
