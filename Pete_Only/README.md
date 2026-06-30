# Pete_Only/

Pete's personal day-to-day bucket in the Aberdeen archive repo.

This directory holds files **Pete** personally wants close at hand — scouting writeups, decision memos, quick-reference notes, and convenience artifacts that should travel with the repo across machines but don't belong in either:

- `Perplexity_Only/` — the agent-context bucket (gotchas ledger, masters notes, canonical IDs, pipeline quickref, Ollama state), OR
- the public research dataset (masters, wiki, studies).

**Distinction:**
- `Perplexity_Only/` = what the agent must read before touching masters/pipeline/models.
- `Pete_Only/` = what Pete wants to find quickly. Human-facing, not pipeline-load-bearing.

Created 2026-06-30.

## Contents

- `kw_ask_local_model_scout_v1.md` — scouting writeup: best local model for kw_ask queries (~27-32B class). Verdict: incumbent `qwen3.5:27b-mlx` stays; Gemma 3 27B / Gemma 4 31B is the only fixture-worthy candidate; Command R 35B blocked on license + MLX. (2026-06-30)
