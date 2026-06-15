# Short-Horizon Prescience Combined-Call Prompt v1

**Status:** DRAFT (Phase 0). Locked semantics; copy text pending review.
**Companion:** `decisions_log_entry_2026_06_15_short_horizon_prescience_v2.md`
**Use:** Single Sonar API call per observation produces BOTH 3y and 5y scores from a single evidence base.

---

## Design constraints

1. **One call → two scores.** Halves cost vs separate calls; guarantees same evidence base.
2. **Windows include anchor year.** 3y = `[A, A+3]`, 5y = `[A, A+5]`.
3. **Both windows must be elapsed.** Driver short-circuits when either is pending (no API call when at least one needs `-2`; see "pending handling" below).
4. **windows_diverge** is a model-asserted boolean: TRUE iff the model's evidence implies different outcomes within the 3y vs 5y windows (e.g. forecast realized in year 4).
5. **Score scale:** `0` wrong / `1-5` scaled-correct / `-1` reserved for prefilter / `-2` reserved for pending. The model MUST NOT output `-1` or `-2`.
6. **Strict JSON output.** No prose outside the JSON object.

---

## Pending handling (driver-side, not model-side)

Before invoking the model:

```
elapsed_3y = today_year > anchor_year + 3
elapsed_5y = today_year > anchor_year + 5

if not elapsed_3y and not elapsed_5y:
    # Both pending — write two -2 rows; SKIP API call
    write_pending(3); write_pending(5); continue
elif not elapsed_5y:  # 3y elapsed, 5y pending
    # Score 3y only via single-horizon prompt variant; -2 the 5y
    ...
else:
    # Both elapsed — combined call
    ...
```

For Tier B/C/D sweeps the dominant case is **both elapsed** (anchor ≤ 2020). The single-horizon variant is needed only for anchors 2021-2022 (3y elapsed, 5y pending).

---

## System prompt (combined, both windows elapsed)

```
You are an expert technology-industry analyst evaluating the prescience of a
historical observation against what actually happened in two time windows.

INPUTS
- Observation: a claim, forecast, or assertion made at anchor_year A.
- Anchor year A: the year the observation was made (or, for memoirs, the year
  the narrated event occurred).
- Two windows to evaluate INDEPENDENTLY:
    * 3-year window: calendar years [A, A+3] inclusive (4 years).
    * 5-year window: calendar years [A, A+5] inclusive (6 years).
- Both windows are fully elapsed; you may rely on facts known as of today.

TASK
For EACH window, return a prescience score on this scale:
   5 — strongly correct, specific, ahead of consensus, low ambiguity
   4 — correct in substance with minor caveats
   3 — partially correct; right direction, wrong magnitude or timing inside window
   2 — weakly correct; some alignment but mostly off
   1 — barely defensible; mostly wrong
   0 — wrong, contradicted by what happened in this window

Then return windows_diverge=true iff the evidence inside [A, A+3] would lead to
a materially different score than the evidence inside [A, A+5] (e.g. the
forecast was wrong in 3y but vindicated by year 4 or 5). If you set
windows_diverge=true, supply a one-sentence divergence_note that names the
inflection point.

RULES
- Do NOT output -1 or -2; those are reserved for pipeline use.
- Confidence is an integer in {1, 2, 3} (1=low, 2=medium, 3=high) reflecting evidence quality, not score magnitude. Matches existing Tier A/B convention.
- Rationale must cite at least one specific event, dataset, or company action
  inside the relevant window. No generic hedges.
- Output strict JSON, no commentary outside the object.

OUTPUT SCHEMA
{
  "prescience_3y":   <int 0..5>,
  "confidence_3y":   <int 1..3>,
  "rationale_3y":    "<<= 280 chars, cite at least one window-bound fact>",
  "prescience_5y":   <int 0..5>,
  "confidence_5y":   <int 1..3>,
  "rationale_5y":    "<<= 280 chars, cite at least one window-bound fact>",
  "windows_diverge": <bool>,
  "divergence_note": "<empty string if windows_diverge=false; else <= 200 chars>"
}
```

---

## User message template (combined)

```
OBSERVATION (anchor_year=A={anchor_year}, source={anchor_source}):
{obs_text}

CONTEXT
- Study: {study_title} ({study_type}, published {published_at})
- Entity/Technology focus: {entity_or_tech}

WINDOWS TO SCORE
- 3y: [{A}, {A_plus_3}]   inclusive
- 5y: [{A}, {A_plus_5}]   inclusive

Return ONLY the JSON object specified.
```

---

## System prompt (3y only, 5y pending — anchors 2021-2022 today)

Identical to the combined prompt with the following diff:

- TASK block: "Return a 3-year prescience score only. The 5-year window has not yet elapsed and will be scored later."
- OUTPUT SCHEMA reduces to:
  ```
  { "prescience_3y": <int 0..5>,
    "confidence_3y": <int 1..3>,
    "rationale_3y":  "<...>" }
  ```
- Driver fills the 5y columns with the pending shape (`score=-2`, `confidence=NULL`, `rationale="window_not_elapsed:5y:cutoff_<Y>"`).

---

## Model + token budgeting

**Model:** `sonar-pro` (confirmed by Pete; no downgrade from Tier A/B sonar; needed for reliable JSON adherence in combined-call output).


- Combined prompt + obs + context: ~700-900 input tokens typical.
- Combined output: 6 fields × ~60 tokens avg + JSON overhead ≈ 450-700 output tokens.
- **Driver v8 max_tokens: 2000** (raised from v7's 1200 to absorb both rationales + divergence_note without truncation).

---

## Parse failure handling (carry forward from Tier A)

Driver writes raw response to `raw_response` column. Post-run retagger flips
`scorer_version` → `pass_c_sonar_sh_v1_parse_fail` for any row whose JSON does
not validate against the schema above. Parse-fail rows are NOT promoted to
master in the first pass; they go back into a retry queue.

---

## Resolved (v3 spec lock)

- Field names: 14 cols, see `masters_notes_sh_schema_entry_v1.md`.
- Single combined `scored_at_sh` timestamp (both windows scored in same call).
- `divergence_note` empty-string (never null) for CSV uniformity.
- G8 threshold: `windows_diverge` rate 2-25% PASS; >25% HARD FAIL; <2% flag.
- `windows_diverge` is **model-asserted**; promote script computes mechanical cross-check `(|3y-5y|>=2)`; G-gate flags mismatches for hand review.