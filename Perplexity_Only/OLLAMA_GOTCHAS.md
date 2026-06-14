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

## G2. `num_predict` defense in depth

Even with `think:false`, give thinking-model families at least 512 `num_predict` tokens. They are biased toward verbose prefaces.

---

## G2. Prompt scale must match production master scale

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

Aberdeen's canonical scale is **1-5** (with -1 and 0 reserved for pre-filter markers). Anything else is a bug.

**History:**
- 2026-06-02 §11q: Pass C scoring fixture written at 0-100. Never compared to actual master values until calibration ran.
- 2026-06-14 09:16 EDT: Re-discovered when Pass C v2 calibration v6 produced kappa=0.000 four runs in a row despite Qwen producing well-distributed valid output. Pete picked B1 (1-5 wins). Fixture v2 written. v7 driver rewritten.

**Defense-in-depth:** When evaluating any new scoring workload, the first 5 minutes goes to "what does the existing data say the scale is?" — not "what does the skill file say the scale is?".
