# Ollama Gotchas — Pete Kastner Archive

Living doc. Anything that has cost us >1 hour of debugging goes here. Read at the start of any session that touches Ollama, MLX, or local LLM scoring.

---

## G1. Qwen 3.x thinking models silently eat the token budget

**Affected models:** `qwen3.5:27b-mlx`, `qwen3.6:27b-mlx`, `qwen3.5:35b-mlx` — and almost certainly any future `qwen3.x:*` release.

**Symptom:** `/api/generate` returns `200 OK`. `response` field is empty string. `done_reason` is `"length"`. The `thinking` field contains a long chain-of-thought that consumed the entire `num_predict` budget before any user-facing token was emitted.

**Root cause:** Qwen 3.x models default to "thinking mode" in Ollama. CoT goes to the `thinking` key, answer goes to the `response` key. If CoT exhausts `num_predict`, you get nothing in `response`.

**Fix:** Set `"think": false` at the **TOP LEVEL** of the request body, NOT inside `options`:

```json
{
  "model": "qwen3.5:27b-mlx",
  "prompt": "...",
  "stream": false,
  "think": false,
  "options": {"temperature": 0.0, "num_predict": 512}
}
```

**Defensive code pattern:** also fall back to `thinking` field if `response` is empty, in case some future caller forgets `think:false`:

```python
text = (body.get("response") or "").strip()
if not text:
    text = (body.get("thinking") or "").strip()
```

**History:**
- ~2026-05-30: Discovered during initial Qwen calibration work. Documented in chat only. LOST.
- 2026-06-14 08:53 EDT: Re-discovered during Pass C v2 calibration v5. All 30 obs returned parse_ok=false. Pete: "You told me about think:false two weeks ago and then forgot it." Documented HERE so it cannot be lost again.

**Verification command (paste and run any time):**
```bash
curl -s http://localhost:11434/api/generate -d '{
  "model":"qwen3.5:27b-mlx","prompt":"Reply with JSON only: {\"x\":1}",
  "stream":false,"think":false,"options":{"temperature":0.0,"num_predict":128}
}' | python3 -c "import json,sys;d=json.load(sys.stdin);print('response=',repr(d.get('response'))[:120]);print('done_reason=',d.get('done_reason'))"
```
Expect: `response='{"x":1}'  done_reason=stop`.

---

## G2a. `num_predict` defense in depth

Even with `think:false`, give thinking-model families at least 512 `num_predict` tokens. They are biased toward verbose prefaces.

---

## G2b. Prompt scale must match production master scale

**Affected workloads:** any scoring task where ground truth already exists in `_master_prescience_scores.csv` (or any future master with numeric judgments).

**Symptom:** Calibration kappa returns 0.000 or near-zero despite the candidate model producing valid, well-distributed numeric output. Inspection shows the candidate scoring on a different numeric range than the master.

**Root cause:** Multiple "rubric definitions" exist (locked fixture file, scorer prompt template, master data) and they don't agree on the integer range. Quadratic kappa across mismatched scales collapses pairs into the maximum-disagreement corner of the confusion matrix → kappa ≈ 0.

**Fix:** The **production master is the source of truth for scoring scale**. Always:
1. Read 5-10 sample rows from `_master_prescience_scores.csv` BEFORE writing any scorer prompt.
2. Look at the `prescience_score` column distribution: `awk -F'","' '$3=="<model>" {print $4}' file.csv | sort | uniq -c`.
3. Match the new scorer's prompt rubric and validation range to the observed integers EXACTLY.
4. If the locked fixture in any skill disagrees with the master, the **master wins**. Bump the fixture, document the rescale decision, do NOT touch the master rows.

**Pre-flight check (paste before writing any scorer):**

```bash
# Get scale distribution per model in current master
awk -F'","' '$3=="sonar-reasoning-pro" {print $4}' /tmp/repo_master_prescience.csv | sort | uniq -c | head
awk -F'","' '$3=="claude-sonnet-4.6"   {print $4}' /tmp/repo_master_prescience.csv | sort | uniq -c | head
```

Aberdeen's canonical scale is **0-5** per `prescience_score_prompt_v2.md`: 1-5 = substantive judgment, 0 = cannot assess, −1 = pre-filter non-claim marker (set by `is_non_claim()` upstream, not by the scorer). For kappa computation, use ordinal label set {1,2,3,4,5} and exclude 0 and −1 as abstention. Anything else is a bug.

**Self-correction note (2026-06-14 12:00 EDT)**: An earlier same-day note claimed the canonical scale was 1-5 because the master distribution showed 1710× score=0 looked like a placeholder. It is not a placeholder — 0 is a legitimate "cannot assess" verdict per the prompt rubric. The prompt file is the source of truth, not the inferred distribution.

**History:**
- 2026-06-02 §11q: Pass C scoring fixture written at 0-100. Never compared to actual master values until calibration ran.
- 2026-06-14 09:16 EDT: Re-discovered when Pass C v2 calibration v6 produced kappa=0.000 four runs in a row despite Qwen producing well-distributed valid output. Pete picked B1 (1-5 wins). Fixture v2 written. v7 driver rewritten.
- 2026-06-14 12:00 EDT: Found `prescience_score_prompt_v2.md` on Mac (canonical 0-5 rubric authored May 25 2026). 1-5 "decision" was a misread of distribution. Corrected.

**Defense-in-depth:** When evaluating any new scoring workload, the first 5 minutes goes to "what does the existing prompt file say the scale is?" — and the master distribution must agree with the prompt, not the other way around.

---

## G3. Frozen-LLM scoring underperforms web-grounded scoring on prescience tasks

**Affected workloads:** any task asking a local LLM to make an ordinal historical-accuracy judgment from training-data priors alone.

**Symptom:** Local model and grounded baseline both produce well-formed scores on the same prompt, but quadratic-weighted Cohen's kappa stays below 0.40 no matter what calibration correction is applied (linear shift, tier-bucketing, offset removal). Score distributions diverge: the frozen LLM concentrates on the top of the scale, the grounded model concentrates in the middle with heavy abstention.

**Root cause:** The two models are doing different cognitive tasks under the same prompt. The grounded model (e.g. `sonar-reasoning-pro`) retrieves evidence and abstains (score=0) when it can't verify. The frozen LLM commits a score from its weights without verification. Prescience scoring is **knowledge-retrieval intensive** — without grounding, the LLM defaults to optimistic-prior commitments. This is structural to the model class, not a prompt bug. No amount of prompt anchoring changes it.

**Quantitative evidence (Qwen 3.5 27B MLX vs `sonar-reasoning-pro`, 2026-06-14):**
- n = 1,041 obs both scored on 1-5 by both models
- Raw quadratic-weighted κ = 0.238
- After Qwen−1 offset shift: κ = 0.331 (best variant)
- Tier-bucket (low/mid/high) κ = 0.239
- All variants fail 0.70 gate; all fail 0.60 substantial threshold
- Abstention asymmetry: Sonar abstained 795× where Qwen committed; Qwen abstained 9× where Sonar committed
- Score distribution: Qwen lives in {4,5}, Sonar lives in {3,4} with heavy 0

**Fix:** Do not substitute frozen LLMs for grounded scorers on ordinal historical-accuracy tasks. Use grounded models (Sonar, future search-augmented LLMs) for the scoring step. Frozen LLMs are still appropriate for upstream filtering (`is_non_claim()`), summarization, generation, and any task where retrieval is not load-bearing.

**When to revisit:**
- A new local model is search-augmented at inference (not just RAG-on-top — actual web retrieval in the loop)
- A new family-of-model evaluation against the locked 1,041-obs paired fixture (`scripts/qwen_master_kappa_v2_paired.csv`) yields κ ≥ 0.70 raw or κ ≥ 0.70 after at most ±1 shift

**Locked evaluation fixture:** `scripts/qwen_master_kappa_v2_paired.csv` (1,041 obs, Qwen vs Sonar, both 1-5). Any new candidate scores those same obs through `prescience_score_prompt_v2.md`, then `scripts/compute_qwen_master_kappa_v2.py` produces apples-to-apples comparison.

**History:**
- 2026-05-26: Initial Qwen 27B Pass C attempt abandoned for agent-quality reasons (not investigated at the time).
- 2026-06-14: Salvage audit recovered 2,723 Qwen scores from `_pass_c_abandoned_runs/20260526/`. Computing κ vs Sonar/Claude master gave the numbers above. Decision recorded at `decisions/decisions_log_entry_2026_06_14_qwen27b_calibration_failed_v1.md`.
