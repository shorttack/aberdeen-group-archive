# Workload 4 Bakeoff — Pete's Blind Ranking

**Run:** `20260906T220000Z`  
**Ranking date:** 2026-09-07  
**Fixture:** `DB_LONGITUDINAL_DOSSIER_v2.md`  
**Gold reference:** deferred (Option B)  
**Ranking basis:** Kastner voice, factual fidelity, thesis discipline, and narrative usefulness

## Blind ranking

1. **A**
2. **B**
3. **C**
4. **E**
5. **D**

Pete's assessment:

> For serious research, each model (except D) brings a perspective and facts that a multi-model synthesis could master.

## Pete's qualitative comments

- **A:** "excellent. minor, trivial edits needed. weak close. good voice of Pete. Like other candidates, conflated 1970-2005 as a 'decade'"
- **B:** "line 13 'we' incorrect. Good enough. Less nuance than A. Fewer words."
- **C:** "First sentence factually wrong. AI writing is obvious. Good research coverage. Fair writing."
- **D:** "Short, misguided, fails"
- **E:** "Focus is on Pete, nor content. Fact errors."

## Revealed mapping

| Rank | Blind ID | Contestant | Runtime/model |
|---:|:---:|---|---|
| 1 | A | `ollama-q36-mlx` | Ollama `qwen3.6:35b-mlx` |
| 2 | B | `ollama-q36-a3b` | Ollama `qwen3.6:35b-a3b` |
| 3 | C | `pplx` | Hybrid `pplx-computer-qwen-3-6-35b-a3b-mlx-20260709` |
| 4 | E | `cloud` | Perplexity Computer cloud frontier/default |
| 5 | D | `ollama` | Ollama `qwen3.5:27b-mlx` incumbent |

## Strict pre-filter caveat

No contestant passed every mechanical pre-filter. The human ranking therefore evaluates narrative quality, not full fixture compliance.

| Contestant | Words | Length | Sidecar | Coverage | Strict result |
|---|---:|:---:|:---:|---:|:---:|
| Cloud | 1,900 | Fail | Pass | 0.3500 | Fail |
| PPLX Hybrid | 2,253 | Pass | Fail | 0.7714 | Fail |
| Ollama Qwen 3.5 27B | 777 | Fail | Fail | 0.8077 | Fail |
| Ollama Qwen 3.6 35B A3B | 2,137 | Pass | Fail | 0.0132 | Fail |
| Ollama Qwen 3.6 35B MLX | 1,984 | Fail by 16 words | Fail | 0.0000 | Fail |

The result separates two questions:

1. **Which model produced the best Kastner-voice narrative?** Ollama Qwen 3.6 35B MLX.
2. **Which model followed the complete output protocol?** None.

## Lane C decision

- **Provisional narrative-drafting default:** Ollama `qwen3.6:35b-mlx`.
- **Secondary drafting/critique pool:** Ollama `qwen3.6:35b-a3b`, PPLX Hybrid Qwen 3.6 35B, and cloud frontier/default.
- **Remove from Lane C narrative contention:** Ollama `qwen3.5:27b-mlx`. Its fifth-place, 777-word response is not competitive for serious long-form narrative drafting. This finding does not change its status in other workloads without their own fixture results.
- **Serious-research workflow:** generate independent perspectives from the top four, then synthesize. Do not collapse the result into a single-model-only policy; Pete found distinct factual and analytical value in A, B, C, and E.
- **Structured compliance:** treat sidecar generation and citation-anchor enforcement as a separate deterministic or validation pass. Requiring a narrative model to solve voice, synthesis, exact YAML schema, and sentence-level anchor density simultaneously distorted the bakeoff.

## M5 Pro rerun

After the 64 GB M5 Pro cutover:

1. Re-run the same locked dossier and narrative prompt.
2. Retain Ollama `qwen3.6:35b-mlx` as the M4 baseline to beat.
3. Add any newly viable 40–70B MLX candidate that clears Gates 0–2.
4. Retain the four-model synthesis question: drafting winner, complementary factual perspectives, and final synthesis quality.
5. Evaluate structured sidecar and anchor compliance separately from Pete's blind narrative ranking.
