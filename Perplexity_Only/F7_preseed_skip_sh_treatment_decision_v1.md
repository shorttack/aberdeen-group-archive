# F7 Resolution — Preseed-Skip Treatment in Short-Horizon Scoring

**Decision date:** 2026-06-18.
**Decided by:** Pete Kastner.
**Option chosen:** **A** — score preseed-skip observations normally in SH.
**Scope:** Driver v8 (`run_prescience_short_horizon_v8.py`) and any successor.

---

## Decision

When driver v8 scores short-horizon prescience (3-year and 5-year windows) and encounters an observation whose long-horizon Pass C row is `model='preseed_skip_v1'`, **v8 scores the observation normally**. The preseed-skip flag is **long-horizon-only**; it does not carry forward to SH windows.

## Rationale

The 253 preseed-skip rows were created on 2026-06-13 to preserve Pete's in-thread Pass B prescience verdicts from being overwritten by Pass C re-scoring. That preservation decision was specifically about **long-horizon** judgment: outcomes observed years after the prediction.

Short-horizon scoring asks a fundamentally different question: did the prediction come true within 3 (or 5) years of being made? That question is mechanical — it depends on outcome observability inside the window, not on Pete's domain judgment about long-horizon accuracy. The two horizons are independent signals.

If SH scoring later disagrees with the preseed long-horizon verdict, that disagreement is **informative**, not a bug. It tells us the prediction's accuracy was time-dependent — correct in the short term and wrong in the long term, or vice versa.

## Operational rules for driver v8

1. **Do NOT exclude preseed rows from the SH input set.** They flow through the standard observation selection logic.
2. **Each preseed observation gets new SH rows** in `_master_prescience_scores.csv` with `row_class='scored'` (or `parse_fail`/`prefilter_skip` per the standard path), `model=<actual SH model>`, `source_pass='pass_c_sh_3y'` or `'pass_c_sh_5y'`, etc.
3. **The original preseed-skip row stays** in the master untouched — it remains the canonical long-horizon record.
4. **Result: 253 preseed observations produce up to 506 new SH rows** (253 × 2 horizons), plus the 253 original preseed rows persist. Total rows after F7 = current 8,440 + new SH writes (varies by selection scope).

## What this means for downstream queries

| Question | Query |
|---|---|
| "What's the long-horizon verdict for obs X?" | Filter on the row where `row_class='scored'` AND `source_pass NOT LIKE 'pass_c_sh%'` (or the explicit preseed row if no Pass C run). |
| "What's the 3-year SH verdict for obs X?" | Filter on the row where `source_pass='pass_c_sh_3y'`. |
| "Which observations had a preseed long-horizon judgment?" | Filter on `model='preseed_skip_v1'` (or, post-F3, `row_class='preseed_skip'`). |
| "Where do long-horizon and SH verdicts disagree?" | Cross-reference the two `prescience_score` values per `obs_id`. |

## What this means for Rule A rollup

Rule A (defined in `Perplexity_Only/PRESCIENCE_ARCHITECTURE.md` §4) computes the **study-level** verdict from observation-level scores. The rule currently filters on `prescience_score != -1`, which excludes both the `-1` sentinel rows AND the EMPTY-score preseed rows (since EMPTY is excluded by the `!= -1` semantics in Python — preseed rows have empty score, which fails the int comparison and gets filtered out via the `IS NOT NULL`-equivalent in the actual rollup script).

**With F7 in place**, Phase 1 should compute SH study-level rollups separately:

```python
# Long-horizon rollup (unchanged)
lh_scores = [r.prescience_score for r in scores
             if r.study_id == target
             and r.prescience_score not in (-1, None, '')
             and not r.source_pass.startswith('pass_c_sh')]

# Short-horizon rollups (new, per horizon)
sh_3y_scores = [r.prescience_score for r in scores
                if r.study_id == target
                and r.prescience_score not in (-1, None, '')
                and r.source_pass == 'pass_c_sh_3y']

sh_5y_scores = [r.prescience_score for r in scores
                if r.study_id == target
                and r.prescience_score not in (-1, None, '')
                and r.source_pass == 'pass_c_sh_5y']
```

This produces three parallel verdicts per study (long-horizon, 3y SH, 5y SH), exposed in `v_studies` as `study_prescience_enum`, `study_prescience_enum_3y`, `study_prescience_enum_5y` (or similar naming — to be confirmed when v8 lands).

## What this means for v_studies and kw ask

After F7 + v8 land, `v_studies_with_high_prescience` continues to filter on the long-horizon enum (`study_prescience_enum='high'`). New views like `v_studies_with_high_prescience_3y` and `v_studies_with_high_prescience_5y` get added.

`kw ask` queries about "high-prescience studies" should disambiguate horizon. Default behavior: long-horizon (preserves backward compatibility with v1.6.2 numbers). Explicit modifiers: "high-prescience at 3 years" or "high-prescience at 5 years".

## Documentation updates required

| File | Update |
|---|---|
| `Perplexity_Only/MASTERS_NOTES.md` | Add row_class column entry; document preseed_skip rows; document SH source_pass values (`pass_c_sh_3y`, `pass_c_sh_5y`, `pass_c_sh_parse_fail`, `pass_c_sh_prefilter`) |
| `Perplexity_Only/PRESCIENCE_ARCHITECTURE.md` | Rev2 §2.1 (add row_class column); §3 (Path A/B unchanged, but note SH horizon parallelism); §7 (mark F7 closed) |
| `Perplexity_Only/PASS_C_V2_QWEN_FULL_RESCORE_PLAN_v1.md` | v8 spec section: preseed-skip rows participate normally; emit `pass_c_sh_3y` / `pass_c_sh_5y` source_pass values |
| `RELEASE_NOTES_v1_7_0.md` (new) | Headline four-finding closure |

## What's explicitly out of scope

- **Re-scoring the 253 preseed rows for long horizon.** That decision (2026-06-13) stands. Pete's preserved judgment is the long-horizon record.
- **Adding a `preseed_skip_sh` row class.** Option C was rejected — it would compound the row-class proliferation problem F3 just solved.
- **Disambiguating which preseed studies are "Bill Wallet-collaborated" vs. solo-Pete-authored.** Not relevant to horizon treatment; preserved separately in `_master_player_rebuttals.csv` provenance.

---

**Maintained by:** Perplexity Computer.
**Pairs with:** F3 (`add_row_class_to_prescience_scores_v1.py`), F6 (`retag_cloud_parse_fails_v1.py`), F2 (promote script commit), Driver v8 spec.
