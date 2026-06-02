# §11q — Qwen 3.6-27B (MLX) upgrade pack

**Date:** 2026-06-02
**WORKLIST item:** §11q
**Scope:** Replace the local Pass C scorer + Phase 3 entity/tech summarizer
model from `qwen3.5:27b-mlx` to `qwen3.6:27b-mlx`, consolidating the model
name into a single source of truth (`_llm_helper_v2.LOCAL_MODEL`).

## Why

- Qwen 3.6-27B is a new Apache 2.0 release: ~+18% on BenchLM, ~+13% on
  agentic tasks vs Qwen 3.5-27B (per release notes).
- MLX-native build exists on Ollama at `qwen3.6:27b-mlx` (~20 GB),
  preserving Apple-Silicon-native matmul paths. Honors Pete's three
  constraints: "abort if no MLX", "do not sacrifice KW retrieval
  accuracy", and his original Q8-ish tag intent (MLX at ~20 GB sits in
  the same accuracy tier as Q8 GGUF at ~30 GB but with better quant
  fidelity).
- Old model `qwen3.5:27b-mlx` stays installed for a 7-day rollback
  window; nothing is removed by this pack.

## What this pack contains

| File | Repo path | Role |
|---|---|---|
| `change_local_model_v1.sh` | `scripts/` | One-shot installer: pre-flights Ollama, aborts if no MLX, pulls model, smoke-tests |
| `change_local_model_v1_README.md` | `scripts/` | This file |
| `_llm_helper_v2.py` | `scripts/build/` | Single source of truth for `LOCAL_MODEL`; superset API of v1 |
| `04_generate_indices_v4.py` | `scripts/build/` | Imports `LOCAL_MODEL` instead of hardcoding (was Gotcha 9 risk) |
| `06_emit_scaffolding_v2.py` | `scripts/build/` | Template substitution: `__LOCAL_MODEL__` sentinel replaced at write time |
| `pre_filter_scoreable_obs_v5.py` | `scripts/` | `scorer_version_target` built from helper; output filenames bumped to v5 |
| `run_prescience_calibration_v4.py` | `scripts/` | `--models` argparse default bumped to 3.6 line (both 27b and 35b) |

**Not changed in this pack** (but flagged for follow-up):

- `scripts/kw_ask.py` in `shorttack/kastner-aberdeen-wiki` — the daily-driver
  query tool. Hardcodes `DEFAULT_LLM = "qwen3.5:27b-mlx"` at line 39. Pete
  may want this updated too — but it's a different repo with a different
  release cadence, and the wiki repo currently has no `_llm_helper` to
  import from. Decision deferred to Pete.
- `bin/kw` in the wiki repo — only doc comments reference the model name.
- `05_compute_embeddings_v3.py` — uses `bge-m3` for retrieval embeddings;
  completely orthogonal to this change. KW retrieval accuracy is NOT
  affected by the Qwen swap (synthesis only).

## Install sequence (Pete-runs)

```bash
# 1. Pull the new pack
cd ~/Desktop/Archive/aberdeen-group-archive
git pull

# 2. Copy the install script + new versions into your working dir
cp scripts/change_local_model_v1.sh             ~/Desktop/Archive/scripts/
cp scripts/build/_llm_helper_v2.py              ~/Desktop/Archive/scripts/build/
cp scripts/build/04_generate_indices_v4.py      ~/Desktop/Archive/scripts/build/
cp scripts/build/06_emit_scaffolding_v2.py      ~/Desktop/Archive/scripts/build/
cp scripts/pre_filter_scoreable_obs_v5.py       ~/Desktop/Archive/scripts/
cp scripts/run_prescience_calibration_v4.py     ~/Desktop/Archive/scripts/

# 3. Dry-run the installer (verifies registry, daemon, disk, OLD model present)
bash ~/Desktop/Archive/scripts/change_local_model_v1.sh

# 4. If dry-run passes, commit:
bash ~/Desktop/Archive/scripts/change_local_model_v1.sh --commit
#    Pulls ~20 GB; takes 5-30 min depending on bandwidth
#    Smoke-tests the model with a 1-token generation
#    Does NOT remove qwen3.5:27b-mlx
```

## Verify the refactor works (recommended before any production run)

After the install completes, sanity-check that the consumer scripts import
the helper cleanly:

```bash
cd ~/Desktop/Archive/scripts/build
python3 -c "from _llm_helper_v2 import LOCAL_MODEL, scorer_version_target; print(LOCAL_MODEL, scorer_version_target('passC_v2'))"
# Expected: qwen3.6:27b-mlx qwen3.6:27b-mlx_passC_v2
```

Then dry-run each refactored consumer:

```bash
cd ~/Desktop/Archive/scripts
python3 pre_filter_scoreable_obs_v5.py --root /Users/scott/Desktop/Archive/prepared --dry-run 2>&1 | head -20
# Should print: [pre_filter v5] ... (no warning about helper missing)
# And ETA line should reference qwen3.6:27b-mlx, not 3.5

python3 run_prescience_calibration_v4.py --help 2>&1 | grep models
# Should show: --models default qwen3.6:27b-mlx,qwen3.6:35b-mlx
```

For Phase 4 + Phase 6, the safest validation is a full Workflow C rerun
(see `kastner-archive-pipeline` skill). At minimum:

```bash
python3 ~/Desktop/Archive/scripts/build/06_emit_scaffolding_v2.py --wiki ~/Desktop/kastner_wiki
# Then verify: grep qwen ~/Desktop/kastner_wiki/README.md
# Expected: qwen3.6:27b-mlx (NOT qwen3.5:27b-mlx)
```

## Rollback (within 7 days, before 2026-06-09)

Two ways:

### A) Per-script (preserves the new helper structure)

Edit `~/Desktop/Archive/scripts/build/_llm_helper_v2.py`:

```python
LOCAL_MODEL = "qwen3.5:27b-mlx"   # was qwen3.6:27b-mlx
```

All five consumer scripts will pick it up on next run. The old model is
still installed; nothing else needs to change.

### B) Full revert to v1 scripts (preserves nothing)

```bash
cd ~/Desktop/Archive/scripts/build
mv _llm_helper_v2.py _llm_helper_v2.py.disabled
# Re-copy v1 from the repo:
cp ~/Desktop/Archive/aberdeen-group-archive/scripts/build/_llm_helper_v1.py .
# Etc. for other scripts. (More effort; only use if helper v2 breaks something.)
```

## After 7 days of stable use (~2026-06-09)

Free ~20 GB of disk:

```bash
ollama rm qwen3.5:27b-mlx
```

**Only run this command if KW ask quality and Pass C scoring quality are
confirmed acceptable on the new model.** Once removed, rolling back
requires re-pulling 20 GB.

## Standing-rule honors checklist

- [x] **"I run commands"** — script never auto-commits anything; Pete runs
      the install manually with explicit `--commit` flag.
- [x] **"Abort if no MLX"** — pre-flight 3 in the installer checks the
      Ollama registry HTML for the `qwen3.6:27b-mlx` tag literal and exits
      non-zero if absent. No silent fall-through to a GGUF variant.
- [x] **"Keep both for a week"** — installer never calls `ollama rm`; the
      7-day cleanup command is in the README's manual-action section only.
- [x] **"Do not sacrifice KW retrieval accuracy"** — bge-m3 (the retrieval
      embedding model) is untouched. Only the synthesis LLM swaps.
- [x] **Forever archive** — every refactored script is a new version
      (`_v2`, `_v4`, `_v5`); no existing `_v1`/`_v3`/`_v4` is overwritten
      or moved to `_legacy/`. Pete promotes via cp; deprecation timing is
      Pete's call.
- [x] **Gotcha 9** — every consumer that emits the model name into a
      generated artifact now imports `LOCAL_MODEL` from the single helper.
      No more docstring/runtime drift.
- [x] **Pete's INTJ rule** — see "Why" + "Standing-rule honors" + this
      decisions log entry: every assertion has a reasoning paragraph
      behind it.
