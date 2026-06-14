# Decision: Establish OLLAMA_GOTCHAS.md as durable record of local-LLM landmines

**Date:** 2026-06-14
**Session:** §11v continued
**Trigger:** Pete observed agent had previously discovered the Qwen 3.x `think:false` requirement ~2 weeks ago but lost it; the same bug re-surfaced and consumed time during Pass C v2 calibration v5 (all 30 obs returned empty `response`, parse_ok=false).

## Decision
Establish `Perplexity_Only/OLLAMA_GOTCHAS.md` as the canonical, append-only, machine-readable record of Ollama / local-LLM gotchas. Any landmine that has cost >1 hour gets entered with: symptom, root cause, fix, verification command, and a `History` section logging discovery + re-discovery dates.

## Rationale
- Chat history is ephemeral across sessions.
- Skill files capture process, not landmines.
- Memory entries are not always loaded into context.
- A flat markdown file in `Perplexity_Only/` is fetched by name and grep-able from every Mac session.

## First entry: G1
Qwen 3.x models (qwen3.5:27b-mlx, qwen3.6:27b-mlx, qwen3.5:35b-mlx) default to thinking mode in Ollama. `/api/generate` requires `"think": false` at the TOP LEVEL of the request body, NOT inside `options`. Without it, `num_predict` is consumed by CoT in the `thinking` field, `response` is empty, `done_reason` is `length`. Defense-in-depth: fall back to `thinking` field if `response` empty.

## Companion updates
1. `memory_update` — two long-term memory entries (gotcha + general preference).
2. `local-model-upgrade-gates` user skill — add a Gate 0 precheck step that reads `Perplexity_Only/OLLAMA_GOTCHAS.md` before evaluating any new local model.

## Repo location
- `Perplexity_Only/OLLAMA_GOTCHAS.md`
- `decisions/decisions_log_entry_2026_06_14_ollama_gotchas_doc_v1.md`

## Standing rule (Pete, this session)
Decisions of this magnitude get written to `decisions/` automatically (per standing rule established 08:28 today). Progress entries get appended to `logs/session_*.md` automatically.
