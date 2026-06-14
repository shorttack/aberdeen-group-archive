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
