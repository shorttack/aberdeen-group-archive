# Local Model Inventory — Mac mini M4 Pro

**As of:** 2026-09-06
**Host:** Mac mini M4 Pro, 48 GB unified memory
**Purpose:** Authoritative record of local models installed on this Mac, indexed against the Workload 4 bakeoff contestants and the M5 Pro re-baseline scheduled for October 2026.

This file is the reference the M5 Pro re-baseline will diff against — a clean-install audit sheet for the local-model surface. It also documents the current storage split and the planned relocation to `/Volumes/Hub/Models`.

---

## Ollama store

**Root:** `~/.ollama/models`
**Total on disk:** 67 GB (2,193 blob files)
**Server:** Homebrew `ollama` LaunchAgent on `http://localhost:11434` (see `Perplexity_Only/start_perplexity_computer_v1.sh`)

| Tag | Size | Role | Bakeoff contestant |
|---|--:|---|---|
| `bge-m3:latest` | 1.16 GB | Wiki embeddings for `kw ask` retrieval | – |
| `qwen3-embedding:8b` | 4.68 GB | Alternate embedding model | – |
| `qwen3.5:27b-mlx` | 19.76 GB | **Incumbent** — `_llm_helper_v4.py` `LOCAL_MODEL` | `ollama` (Qwen 3.5 27B MLX, current Lane A/B/C incumbent) |
| `qwen3.6:35b-a3b` | 23.94 GB | Qwen 3.6 35B active-3B, non-MLX build | `ollama-qwen3.6-a3b` |
| `qwen3.6:35b-mlx` | 21.91 GB | Qwen 3.6 35B MLX build | `ollama-qwen3.6-mlx` |

**Ollama subtotal for bakeoff-eligible models:** 65.61 GB (three Qwen tags).

---

## Perplexity / Hugging Face cache

**Root:** `~/.cache/huggingface/hub`
**Total on disk:** 39 GB
**Governed by:** HF Hub library (`HF_HOME` / `TRANSFORMERS_CACHE` env vars can relocate)

| Repo | Size | Role | Bakeoff contestant |
|---|--:|---|---|
| `perplexity-ai/pplx-computer-qwen-3-6-35b-a3b-mlx-20260709` | 18 GB | **PPLX Hybrid runtime model** — 4-bit, dated snapshot; the model the Perplexity Mac app runs in Hybrid mode | `pplx` (PPLX Qwen 3.6 35B via Hybrid) |
| `mlx-community/Qwen3.6-35B-A3B-4bit` | 19 GB | Community MLX build of the same Qwen 3.6 base; not runtime-hosted | – (candidate for future direct-MLX bakeoff) |
| `datalab-to/surya-ocr-2-gguf` | 1.4 GB | Surya OCR — unrelated to bakeoff | – |
| `datalab-to/surya_layout2` | 135 MB | Surya layout — unrelated to bakeoff | – |

**HF subtotal for bakeoff-eligible models:** 18 GB (PPLX only; community MLX is a spare).

---

## Total footprint

**Combined:** 106 GB across two stores.

The two stores intentionally use different formats — Ollama's content-addressed blobs + manifest tree is not compatible with the HF Hub snapshot/symlink layout. Even for the same base model (Qwen 3.6 35B), the on-disk bytes differ; there is no shared-copy path without one runtime accepting the other's format, which neither does today. The relocation plan below therefore keeps two stores but co-locates them under a single parent for backup, audit, and disk-quota clarity.

---

## Relocation plan — `/Volumes/Hub/Models`

**Target volume:** `/Volumes/Hub` — 1.8 TB, 1.8 TB free as of 2026-09-06.
**Target parent:** `/Volumes/Hub/Models` (already exists, empty).

**Layout after relocation:**

```
/Volumes/Hub/Models/
├── ollama/           <- OLLAMA_MODELS points here; replaces ~/.ollama/models
└── huggingface/      <- HF_HOME points here; replaces ~/.cache/huggingface
```

**Approved:** 2026-09-06 (Pete). Execution deferred until:

1. Pete signs off on the migration procedure (below).
2. The Ollama LaunchAgent and the Perplexity app are both stopped.
3. Current bakeoff dispatches complete (nothing mid-run).

**Migration procedure (draft — not yet executed):**

The procedure is delivered as a script (`migrate_models_to_hub.sh` — to be written just before execution) with an **explicit pre-flight pause** at the very top. The pause requires the operator to close listed applications and services BEFORE any file operation runs. This prevents the classic failure mode of an app or LaunchAgent holding open file handles on a source directory during rsync, which produces silently truncated copies or half-migrated states that only surface hours later during a bakeoff run.

**Pre-flight pause (Step 0, blocking):**

The script's first action is to print the following, then exit unless the operator re-invokes it with `PREFLIGHT_ACKNOWLEDGED=1`:

```
=========================================================================
  PRE-FLIGHT — CLOSE THESE APPLICATIONS AND SERVICES BEFORE PROCEEDING
=========================================================================

  1. Perplexity Mac app        (holds the ~/.cache/huggingface PPLX model)
  2. VPN client                (any traffic through the model directories
                                 during rsync is a risk; safer to close)
  3. Ollama                    (this script will stop it in Step 1, but if
                                 you have `ollama` invocations running in
                                 any Terminal, cancel them first)
  4. Any Terminal running      grep for these in your shells:
     kw ask / _llm_helper /       - kw ask
     Phase 3 gen /                 - _llm_helper_v4.py
     Pass C /                      - phase3_wiki_gen
     bakeoff dispatch              - pass_c
                                    - run_bakeoff.sh

  Any of the above holding open file handles on
     ~/.ollama/models  or  ~/.cache/huggingface
  during rsync will produce a silently truncated copy.

  When everything above is closed, re-invoke:
     PREFLIGHT_ACKNOWLEDGED=1 bash migrate_models_to_hub.sh

=========================================================================
```

**Numbered steps (run only after PREFLIGHT_ACKNOWLEDGED=1):**

1. Stop Ollama: `launchctl bootout gui/$(id -u)/homebrew.mxcl.ollama`. Poll `pgrep -f ollama` until empty (up to 15 s).
2. Confirm Perplexity app is not running: `pgrep -f "Perplexity"` should return nothing.
3. Verify neither store has open file handles: `lsof +D ~/.ollama/models`, `lsof +D ~/.cache/huggingface`. Both should be empty. If not, exit with the offending PIDs printed — do not proceed.
4. `rsync -aH --info=progress2 ~/.ollama/models/ /Volumes/Hub/Models/ollama/`
5. `rsync -aH --info=progress2 ~/.cache/huggingface/ /Volumes/Hub/Models/huggingface/`
6. Set `OLLAMA_MODELS=/Volumes/Hub/Models/ollama` in `~/.zshenv` and the Homebrew Ollama LaunchAgent plist.
7. Set `HF_HOME=/Volumes/Hub/Models/huggingface` in `~/.zshenv` and export from any relevant Python venv.
8. Restart Ollama: `launchctl kickstart -k gui/$(id -u)/homebrew.mxcl.ollama`. Poll `curl -sS http://localhost:11434/api/tags` until it returns 200.
9. Verify: `ollama list` should show the same models; a bakeoff dry-run against `qwen3.5:27b-mlx` should behave identically.
10. Only after all verification: `rm -rf ~/.ollama/models ~/.cache/huggingface/hub` (or leave in place and reclaim later — the volume has 500 GB free).
11. Restart the Perplexity Mac app; verify PPLX Hybrid still resolves the local model. If not, the app may keep its own reference to `~/.cache/huggingface` that has to be re-pointed via preferences.
12. Restart VPN if it was in use.

**Rollback:** the sources are not deleted until step 10, so any failure between steps 4 and 9 rolls back by unsetting the env vars and restarting the services.

**Risk noted:** step 11 is the one uncertainty — Perplexity's model resolution may be app-internal and not respect `HF_HOME`. If that's the case, the PPLX model needs to stay at `~/.cache/huggingface` and only the Ollama store relocates. Bakeoff still runs identically; the "single parent" outcome is partial. That determination is made empirically at migration time, not in advance.

---

## Update cadence

Re-generate this inventory:
- Before every bakeoff run (config drift check).
- After every `ollama pull` or new HF model download.
- At the M5 Pro cutover (October 2026) — mandatory baseline.
- Any time `_llm_helper.LOCAL_MODEL` changes.

A regeneration script is not written yet; the current commands are documented above in the "Ollama store" and "Perplexity / Hugging Face cache" sections and can be run ad-hoc.
