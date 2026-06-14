# Decision: Qwen 3.5 27B MLX Failed Pass C Calibration — Sonar Remains Primary

**Date**: 2026-06-14
**Author**: Pete Kastner (operator) + Perplexity Computer (agent)
**Status**: DECIDED
**Supersedes**: 2026-06-14 decision to adopt 1-5 scale for v7 calibration (still valid, but moot — v7 itself was a dead branch)
**Related artifacts**:
- `Perplexity_Only/WORKING_DIRS_MAP_2026_06_14.md`
- `scripts/audit_abandoned_qwen_run_v1.py` + `audit_abandoned_qwen_*.csv`/`.md`
- `scripts/compute_qwen_master_kappa_v1.py` + `qwen_master_kappa_*_v1.csv`/`.md`
- `scripts/compute_qwen_master_kappa_v2.py` + `qwen_master_kappa_v2_*.csv`/`.md`
- `Perplexity_Only/prescience_score_prompt_v2.md` (canonical 0-5 prompt, unchanged)

---

## TL;DR

Qwen 3.5 27B MLX cannot replace Sonar/Claude as the Pass C prescience scorer. After exhausting every reasonable calibration correction, the best achievable quadratic-weighted Cohen's κ vs Sonar is **0.331**, far below the 0.70 gate.

**Decisions**:

1. **Short-term (effective immediately)**: Sonar (`sonar-reasoning-pro`) remains the primary Pass C ordinal scorer. Claude Sonnet 4.6 stays as the second-opinion scorer for high-stakes obs. The remaining ~21,500 unscored obs in `_master_observations.csv` will be scored by Sonar via the existing cloud pipeline.

2. **Medium-term (this week or next)**: Re-evaluate at least one alternative local LLM against the **locked Qwen-vs-Sonar paired fixture** (`scripts/qwen_master_kappa_v2_paired.csv`, n=1,041 pairs of obs both scored on the 1-5 scale). Candidates worth testing: Llama 3.3 70B, DeepSeek R1 distill (32B or 70B), Mistral Large. Gate 0 in `local-model-upgrade-gates` applies — paper review and Perplexity_Only/OLLAMA_GOTCHAS.md read before pull.

3. **Documented but not adopted (Path 2)**: Hybrid pipeline where Qwen runs the `is_non_claim()` pre-filter + abstention detection, and Sonar scores the remaining commit-eligible obs. Saves ~31% of Sonar API volume. Available as a cost optimization if/when Sonar spend becomes a budget pressure. Not pursued now because Sonar volume is already manageable.

4. **Qwen 27B is not retired** — it continues to serve Phase 3 wiki generation, kw_ask synthesis, summarization, and `is_non_claim()` filtering. The failure is specific to ordinal prescience scoring, not to the model's general utility.

---

## Evidence summary

### v1 raw kappa (no corrections)

| Comparison | n (1-5 only) | Quadratic-weighted κ |
|---|---|---|
| Qwen vs Sonar  | 1,041 | **0.2379** |
| Qwen vs Claude | 36 (statistically too small) | 0.1227 |

### v2 calibration variants (Qwen vs Sonar only)

| Variant | n | κ | Exact-match | Off-by-1 | Off-by ≥2 |
|---|---|---|---|---|---|
| A. Raw 5-class | 1,041 | **0.2379** | 30.4% | 49.8% | 19.8% |
| B. Qwen−1 offset shift | 1,041 | **0.3308** | 51.0% | 36.2% | 12.8% |
| C. Tier-bucket (low/mid/high) | 1,041 | **0.2393** | 66.2% | — | — |
| D. Best linear shift (−1) | 1,041 | **0.3308** | — | — | — |

**None pass the 0.70 gate. None even pass 0.60 (substantial agreement).** Best achievable across all tested variants: 0.331.

### Abstention pattern (informational, excluded from κ)

| Pattern | Count |
|---|---|
| Both abstained (Qwen=0 AND Sonar=0) | 810 |
| Only Sonar abstained (Qwen committed) | **795** |
| Only Qwen abstained (Sonar committed) | 9 |

Sonar abstains **88× more often** than Qwen on the same obs set. This is the root structural difference.

### Score-distribution asymmetry on the overlap

| Score | Qwen freq (overlap) | Sonar freq (overlap) |
|---|---|---|
| 0 (cannot assess) | 650 (27%) | 1,324 (56%) |
| 1 (wrong) | 68 | 6 |
| 2 (mostly wrong) | 63 | 52 |
| 3 (partial) | 36 | 306 |
| 4 (largely prescient) | 869 | 644 |
| 5 (remarkably prescient) | 688 | 42 |

Qwen lives in {4, 5}. Sonar lives in {3, 4} with heavy 0-abstention. They are not scoring the same construct.

---

## Why this happened (root cause)

Sonar and Qwen are performing **different cognitive tasks** under the same prompt:

- **Sonar (`sonar-reasoning-pro`)** is web-grounded. Its "I know what happened from 1998-2026" is supported by retrievals. When it cannot retrieve supporting evidence for a specific claim, it correctly abstains (score=0). When it commits, its assessments are critical and concentrated in the middle of the rubric (3 and 4).
- **Qwen 3.5 27B MLX** is a frozen LLM. Its "I know what happened from 1998-2026" is its training data, which has broad coverage but no retrieval-based verification step. It rarely abstains (only 27% on the overlap, vs Sonar's 56%) and commits to high scores (4 and 5) more readily.

This is structural, not a prompt bug. The Aberdeen prescience-scoring task is **knowledge-retrieval intensive** — many claims hinge on facts a base LLM may or may not have memorized accurately. Web-grounded scoring is the right tool. Frozen-LLM scoring produces a different (looser, more confident, more positive) judgment by design.

The same prompt (`prescience_score_prompt_v2.md`) was used for both Qwen and Sonar/Claude. The disagreement is not prompt drift.

---

## Why the salvage path was correct to try

The decision to audit and recover the 309 abandoned May 26 Qwen working dirs (`_pass_c_abandoned_runs/20260526/`) was correct and cheap:

- Found 2,723 valid Qwen scores with 100% parse_ok
- Discovered 2,722 obs overlap with the master Sonar/Claude rows
- Produced a 1,041-obs paired calibration set that did not exist before
- This paired set is **now a locked fixture** for any future local-model evaluation — we can drop a new candidate's scores in and immediately compute κ apples-to-apples

The salvage cost us ~30 minutes and gave us a permanent evaluation artifact. The earlier morning's mistake (writing v5/v6/v7 calibration drivers from scratch instead of finding the 574 working dirs first) was the only real waste.

---

## Why each path was considered

### Path 1 (Sonar primary) — adopted short-term

Pros:
- Sonar already produced 3,661 rows with known quality and the canonical prompt
- Cloud pipeline is operational, no new infrastructure
- Highest κ available against itself (Sonar is the reference)
- Web grounding is the right mechanism for the task

Cons:
- API cost per obs > local Qwen
- External dependency on Perplexity Sonar availability
- Remaining ~21,500 obs at Sonar throughput will take ~real time (estimate to be benchmarked)

### Path 2 (Qwen pre-filter + Sonar scorer) — documented, not adopted

Pros:
- Saves ~31% of Sonar API volume (the abstention-eligible obs)
- Qwen is already validated for `is_non_claim()` and abstention via the 650/27% concordance on Sonar=0 obs
- Cheap to add later

Cons:
- Adds pipeline complexity (two scorers in series)
- Failure modes are harder to debug
- Not needed until Sonar volume becomes a budget issue
- Defer until either (a) cost pressure exists, or (b) the Path 3 evaluation gives us a better local model that makes the hybrid pointless

### Path 3 (try a different local model) — adopted medium-term

Pros:
- The 1,041-obs paired fixture is now permanent and reusable
- Cheap to evaluate any new candidate (audit → score → compute κ, ~1 hour per candidate)
- Possible a stronger local model passes the gate

Cons:
- Each candidate requires a Pass C smoke-run to produce its score set on the same obs (overnight per candidate)
- Risk of repeating the structural failure: if web grounding is what's required, no frozen LLM will work

Order of candidates to evaluate:
1. **Llama 3.3 70B** — known strong on factual recall, has a tradition of being calibrated
2. **DeepSeek R1 distill 70B** — reasoning-strong, may handle ordinal judgment better
3. **Mistral Large 2** — different family, useful as a sanity check

---

## What stays unchanged

- `prescience_score_prompt_v2.md` is **not** edited. The prompt is fine; the scorer choice is the variable.
- The 3,829 Sonar+Claude rows in `_master_prescience_scores.csv` remain authoritative.
- The 2,723 abandoned Qwen rows stay in `_pass_c_abandoned_runs/20260526/` — **do not move them to master.** They are the locked evaluation fixture, not production data.
- The 0-5 scale (1-5 + 0 abstain + −1 pre-filter) is canonical. Earlier same-session decision about adopting "1-5" was a misread of the master distribution; the prompt v2 file is the truth.
- `is_non_claim()` filter (in v3 calibration driver) remains in use, regardless of which scorer runs.

---

## What changes immediately

1. **Sonar Pass C run plan** for the remaining ~21,500 obs: TBD by next session. Need to scope batches, cost ceilings, and rate limits.
2. **`Perplexity_Only/OLLAMA_GOTCHAS.md`** gets G3 added: "Frozen-LLM ordinal scoring underperforms web-grounded scoring on prescience tasks. Qwen 3.5 27B MLX: max κ 0.331 vs Sonar after best calibration. Do not substitute frozen LLMs for grounded scorers on prescience scoring."
3. **`local-model-upgrade-gates` skill** Gate 0 update: locks `scripts/qwen_master_kappa_v2_paired.csv` (1,041 obs) as the official Pass C scoring fixture. Any new candidate runs the same obs through `prescience_score_prompt_v2.md`, then `compute_qwen_master_kappa_v2.py` produces apples-to-apples comparison. Pass gate: κ ≥ 0.70 raw OR κ ≥ 0.70 after at most ±1 shift.
4. **`kastner-archive-pipeline` skill** Gotcha 13 ("check working dirs first") stays as written from earlier this session.

---

## Open questions for next session

- **Exactly how many obs remain unscored?** Currently estimated ~21,500 (= ~23,927 in observations master − 2,722 already scored − a few hundred edge cases). Need a precise count and a Sonar batching plan.
- **Sonar Pass C cost per obs?** Need to benchmark with a small live batch (50 obs) and extrapolate.
- **Rate-limit constraints?** Sonar has per-minute and per-day caps; need a plan that respects them without stretching wall-time to months.
- **Should the v2 paired CSV be promoted from `scripts/` to `Perplexity_Only/` as a top-level fixture?** Probably yes — it's a calibration reference, not a one-off output. Mark it locked.

---

## Provenance / reproducibility

Run on Mac at ~/Desktop/Archive/aberdeen-group-archive:
```bash
python3 scripts/audit_abandoned_qwen_run_v1.py
python3 scripts/compute_qwen_master_kappa_v1.py
python3 scripts/compute_qwen_master_kappa_v2.py
```

Each emits the artifacts listed in "Related artifacts" above. Numbers in this decision are taken verbatim from the 2026-06-14 17:05 UTC run.

*Authored by agent 2026-06-14 13:08 EDT per Pete's instruction "write up the decision: Path 1 short-term, Path 3 medium-term, document Path 2 as an option".*
