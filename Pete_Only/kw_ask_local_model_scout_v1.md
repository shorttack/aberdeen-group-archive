# kw_ask Local Model Scout — ~27–32B class, MLX-native

**Scope:** Best local model for **kw_ask synthesis only** (not Phase 3, not Pass C). Footprint band: ~27–32B class to match the current `qwen3.5:27b-mlx` pin (~20GB). Scouting pass only — no pull, no fixtures, no commits. Status quo wins ties.

## What kw_ask actually needs (locked Gate 2 mapping)
- **Primary:** faithful extractive Q&A over retrieved bge-m3 passages; citation discipline (cite passage IDs that appear in input, never invent).
- **Secondary:** concise prose; refuse when context is insufficient.
- **Does NOT matter:** math, coding, agentic tool use, multimodality, long thinking traces.

This is the crucial reframe: kw_ask is **retrieval-grounded** (passages are in the prompt), unlike Pass C which is knowledge-retrieval-intensive. So G3 (frozen-LLM-fails-prescience) does NOT apply here — the evidence is supplied in-context. A strong extractor that follows instructions and doesn't fabricate is what wins.

## Gate 0 — gotchas ledger (read, relevant entries)
- **G1 (applies to any Qwen 3.x):** thinking mode silently eats the token budget; `response` comes back empty with `done_reason="length"`. Any Qwen candidate MUST run with top-level `"think": false` + the `thinking`-field fallback. This is a maintenance tax on every Qwen option.
- **G2a:** give thinking-family models ≥512 `num_predict`.
- **G3:** does NOT apply to kw_ask (grounded task). Noted so we don't mis-import the Pass C verdict.

## Candidate shortlist (ranked for kw_ask)

| Rank | Model | Footprint | Citation behavior | Instruction-following | Thinking-mode tax | MLX-native? | Verdict for kw_ask |
|---|---|---|---|---|---|---|---|
| — | **qwen3.5:27b-mlx (incumbent)** | ~20GB | prompt-engineered (works today) | IFEval **95.0%**, leads open-source ([Awesome Agents](https://awesomeagents.ai/leaderboards/instruction-following-leaderboard/)) | Yes — needs `think:false` (G1) | Yes | **Status quo. Strong baseline.** |
| 1 | **Gemma 3 27B** | ~14GB Q4 | prompt-engineered | competitive on non-agentic tasks; Gemma 4 31B beats Qwen3.6 on this class ([Kaitchup](https://kaitchup.substack.com/p/qwen36-27b-vs-qwen35-27b-vs-gemma)) | **None** (no thinking trap) | check tag | **Top alternative.** No G1 tax, big KV-cache headroom, 128K context ([InsiderLLM](https://insiderllm.com/guides/best-local-llms-rag/)) |
| 2 | **Command R 35B** | ~19GB Q4 | **native inline citations** — only local model that does this without prompt-engineering ([InsiderLLM](https://insiderllm.com/guides/best-local-llms-rag/), [LLMversus](https://llmversus.com/llm/best-for/best-llm-for-rag)) | strong grounded generation | None | **likely no MLX — abort rule** | **Best-on-paper for citations, BUT: CC-BY-NC license (non-commercial only) + MLX availability unverified.** |
| 3 | **Qwen3.6 27B** | ~17–20GB | prompt-engineered | **IFBench significantly WORSE than 3.5** ([Kaitchup](https://kaitchup.substack.com/p/qwen36-27b-vs-qwen35-27b-vs-gemma)) | Yes (G1) | Yes | **No-go** — already failed Track A Gate 1; the regression is in exactly the dimension kw_ask needs. |

## The key tension
- **Pure quality-on-paper for citations → Command R 35B.** It's the only local model with *native* citation grounding; everyone else hallucinates sources 17–33% of the time without prompt engineering ([InsiderLLM](https://insiderllm.com/guides/best-local-llms-rag/)). BUT two hard blockers: (1) **CC-BY-NC license** — non-commercial only, may not fit the archive's posture; (2) **MLX availability unconfirmed** — your standing rule is *abort if no MLX*.
- **Lowest-risk real upgrade → Gemma 3 27B (or Gemma 4 31B).** Smaller footprint, no thinking-mode tax (removes the G1 maintenance surface entirely), competitive instruction-following on non-agentic tasks. The catch: it's prompt-engineered citations like the incumbent, so the *upside over qwen3.5* is "drops the G1 tax + frees RAM," not "better extraction."
- **Incumbent is genuinely hard to beat.** qwen3.5:27b leads open-source IFEval at 95.0%. For an extractive, instruction-following task, that's the exact strength that matters. Status-quo-wins-ties is doing real work here.

## Recommendation (scouting verdict)
If you want to spend any fixture time, the **one** candidate worth a Gate 3/4 run is **Gemma 3 27B / Gemma 4 31B** — and only because eliminating the Qwen thinking-mode tax (G1) is a standing maintenance win, not because benchmarks promise better extraction. **Command R 35B** is the citation-quality leader but is gated by license + MLX availability; verify both before it earns a fixture slot. **Qwen3.6 is out** (Track A precedent). Absent a clear win, the incumbent stays.

## What I have NOT done (awaiting your call)
- No Ollama tag verification for MLX availability on any candidate.
- No Gate 3 fixture predictions, no Gate 4 pull.
- No commits.
