# OLLAMA_STATE.md — Local LLM Models, Pins, and Operational Notes

> **READ THIS FILE before swapping any Ollama model or touching `_llm_helper_v4.py`.**
> Local model swaps mid-pipeline have repeatedly broken Phase 3 in
> hard-to-diagnose ways. The pin in `_llm_helper_v4.py` is deliberate.

**Last updated:** 2026-06-12 (§11u-cont Pass B Completion).
**Pairs with:** `local-model-upgrade-gates` skill (the formal upgrade-evaluation flow).

---

## Installed models (as of 2026-06-12)

| model | size | role | installed |
|---|---:|---|---|
| **`qwen3.5:27b-mlx`** | 19 GB | **Active pipeline LLM** (Phase 3 wiki generation, kw_ask synthesis, Pass C scoring) | Pinned in `_llm_helper_v4.py` |
| `qwen3.5:35b-mlx` | 21 GB | Reserved — evaluated against 27b, not chosen | Available |
| `qwen3.6:27b-mlx` | 19 GB | Available but NOT pinned. Pulled 2026-06-03; evaluated 2026-06-02 per §11q lesson and rejected for production use until full gate-4 evaluation completes | Available |
| `bge-m3:latest` | 1.2 GB | **Phase 5 embeddings** (1024-dim, 6-col schema) | Pinned in `05_compute_embeddings_v3.py` |

---

## Why qwen3.5:27b-mlx and not qwen3.6 or 35b

**3.5:27b vs 3.6:27b:** Per the §11q lesson (2026-06-02), pulling 20 GB of qwen3.6
and refactoring `_llm_helper_v4.py` consumed ~4 hours of debugging time because
the new model's output schema for structured JSON was subtly different. The
`local-model-upgrade-gates` skill now formalizes a 4-gate evaluation flow
(paper review → fixture-locked benchmark → cost/quality delta → integration
test) that any model swap MUST pass before changing the pin.

**3.5:27b vs 3.5:35b:** The 35b variant produces marginally better prose but
is 3.2x slower per page in Phase 3. On a 1452-study corpus that translates
to roughly an extra 6-8 hours of wall-clock Phase 3 time. Not worth the
quality bump for the use case (synthetic wiki pages where the structured
data is the ground truth and the prose is decorative).

---

## How to verify Ollama is actually serving

The single most common time-waste in this archive: thinking Ollama is
running when it's not, or running against the wrong model, or running
in a stale terminal window from a prior session.

```bash
# 1. Is the daemon running?
curl -s http://localhost:11434/api/tags | python3 -m json.tool | head -30

# Expected: JSON listing all installed models with their digests and sizes.
# If you get "Connection refused" → Ollama daemon is not running.
# Start it with: ollama serve   (in a separate terminal, leave running)

# 2. What models are loaded into VRAM right now?
ollama ps

# Expected: a row for each model currently warm. If empty, the next
# inference call will cold-start (adds ~30 sec latency for 27b models).
# If you see an unexpected model, kill it: ollama stop <model>

# 3. What is _llm_helper_v4.py actually using?
grep -E "^(LOCAL_MODEL|MODEL_NAME|OLLAMA_MODEL)" \
  ~/Desktop/Archive/scripts/build/_llm_helper_v4.py

# Expected: LOCAL_MODEL = "qwen3.5:27b-mlx" (or whatever the current pin is).
# If this doesn't match what `ollama ps` shows after a phase starts,
# stop the pipeline — something is wrong.
```

---

## `_llm_helper_v4.py` pin

The pin lives at:

```
~/Desktop/Archive/scripts/build/_llm_helper_v4.py
```

The line to grep is `LOCAL_MODEL = "qwen3.5:27b-mlx"`. Do not change this
during a Phase 3 run. If you need to change it:

1. Phase 3 must be fully complete (`ps aux | grep 03_generate | grep -v grep` returns empty).
2. The new model must have passed the `local-model-upgrade-gates` 4-gate flow.
3. The skill `local-model-upgrade-gates` must be reloaded before swapping.
4. Phase 3-6 must be re-run end-to-end after the swap (don't partial-run).

---

## Phase-by-phase model usage

| phase | model | call pattern |
|---|---|---|
| 1 (load) | None | DuckDB only |
| 2 (data layer) | None | DuckDB only |
| 3 (vault gen) | **qwen3.5:27b-mlx** | One generation per page (study, entity, technology, topic) |
| 4 (indices) | None | DuckDB + filesystem only |
| 5 (embeddings) | **bge-m3** | One embedding per chunk |
| 6 (scaffolding) | None | Filesystem only |

`kw_ask` (the chat-starter natural-language query tool) also uses
qwen3.5:27b-mlx via the same `_llm_helper_v4.py`.

---

## Performance baselines (Pass B, 2026-06-12)

- Phase 3 total runtime: started 1:53 PM EDT, completed roughly 6:00-7:00 PM EDT → **4-5 hours** for a 1452-study corpus.
- Per-tech-page average: ~3-4 seconds (technologies are the bulk of generation time).
- Per-entity-page average: ~2-3 seconds (entities have less generated prose).
- Per-study-page average: ~5-7 seconds (longest, most cross-references).
- Phase 5 embeddings: **17 minutes for 10,437 pages** (measured 2026-06-13 AM, post-Pass B). Throughput ~10 pages/sec via bge-m3.

These numbers are on an M4 Pro Mac mini with 48 GB RAM. Mileage will vary
on different hardware.

---

## The "stale ollama window" gotcha

**Symptom:** `ollama ps` shows a model running but the new pipeline call
hangs or returns weird outputs.

**Cause:** A prior session left an `ollama` process running with stale
context, possibly pointed at a different model than the current pin.

**Fix:**
```bash
# Stop everything Ollama knows about
ollama stop $(ollama ps --no-header | awk '{print $1}')

# Verify nothing is running
ollama ps

# Then start the new pipeline phase fresh
```

This bit us on 2026-06-12 with PIDs 16849 (1:40 PM duplicate) racing
PID 19483 (1:53 PM correct kickoff). Lesson: always verify `ollama ps`
is empty (or shows ONLY the model you want) before starting Phase 3.

---

## When in doubt

1. **Check the pin** in `_llm_helper_v4.py`.
2. **Check `ollama ps`** matches the pin.
3. **Check the daemon** with `curl localhost:11434/api/tags`.
4. **Trust mtimes, not logs** (Python stdout buffering will lie to you).

---

**Maintained by:** Pete Kastner + Perplexity Computer.
**Pairs with:** `MASTERS_NOTES.md`, `PIPELINE_QUICKREF.md`, `CANONICAL_IDS.md`, and the `local-model-upgrade-gates` skill.
