# Kastner Archive — Canonical Pipeline

**Source of truth** for which Phase 1–6 scripts to run, and how.
**Last locked:** 2026-07-08 (end-to-end validated via the 2026-07-07/08 overnight run + resume).

Supersedes `DAILY_INGEST_RUNBOOK.md` (which named pre-SH v2/v4/v1 versions that
overwrite SH content) and any per-phase runbook fragments that pre-date the
2026-06-30 v2.0 SH release.

## TL;DR

**Run this** (from Mac Terminal, not `pc bash`):

```bash
bash ~/Desktop/Archive/scripts/pipeline_canonical_v1.sh --commit
```

That's it. The orchestrator locks the canonical version per phase, runs them in
order (with the Phase 0 regression audit gating between Phase 2 and Phase 3),
tees every phase's stdout+stderr to a timestamped log dir, and emits a
STATUS_OK / STATUS_FAIL file plus a macOS notification at the end.

Default is `--commit`-off (dry-run) — you must pass `--commit` to actually
execute the phases.

## Canonical version per phase

Locked as of 2026-07-08 after end-to-end validation:

| Phase | Script | Purpose | Time | SH-aware? |
|:-:|---|---|---:|:-:|
| 1 | `01_load_csvs_v3.py` | Read masters (incl. `_master_prescience_short_horizon.csv`); derive `pub_year`, prescience rollups, occurrence counts; write 13 parquets to `<wiki>/build_workspace/` | ~2 s | ✓ |
| 2 | `02_build_data_layer_v5.py` | Promote parquets to `<wiki>/data/`; create `<wiki>/db/kastner.duckdb` with **32 views** including 5 SH views (`v_prescience_sh`, `v_observations_with_sh`, `v_studies_with_sh_verdicts`, `v_sh_3y_distribution`, `v_sh_5y_distribution`) | ~1 s | ✓ |
| 0 | `07_audit_masters_v1.py` | Regression harness — three probes gate Phase 3: alias-collision ratio floor, tech ID-vs-name congruence, DEC/Compaq/HP successor-bleed. Exit 0/1/2 = pass/alert/fail. | ~1 s | — |
| 3 | `03_generate_vault_v3.py` | Render `<wiki>/wiki/**/*.md` pages incl. 3y/5y verdicts on gradeable study pages via tier-1 LLM (`qwen3.5:27b-mlx` from `_llm_helper_v4`) | **~3 h** | ✓ |
| 4 | `04_generate_indices_v6.py` | Home/decade/collection/prescient/codes indices + 5 Bases files. Uses `_llm_helper_v4`. | ~1 s | — |
| 5 | `05_compute_embeddings_v3.py` | Re-embed ~10.8 K pages with **bge-m3** (1024-dim) via Ollama. Writes `<wiki>/data/embeddings.parquet`. **v4 is the rejected qwen3-embedding:8b candidate — do NOT run v4.** | ~15–19 min | passive |
| 6 | `06_emit_scaffolding_v2.py` | README + AGENTS.md + chat-starter.md + Makefile + `.gitignore` + `scripts/verify.py` + `scripts/semantic_search.py`. Templates include the "Short-horizon prescience" section. | <1 s | ✓ |

**Superseded (do not use):**

- `01_load_csvs_v2.py` — pre-SH; ignores `_master_prescience_short_horizon.csv`
- `02_build_data_layer_v4.py` — pre-SH; missing 5 SH views
- `03_generate_vault_v2.py` — pre-SH; overwrites SH content in study pages
- `04_generate_indices_v2/v3/v4/v5.py` — earlier `_llm_helper` chains
- `05_compute_embeddings_v4.py` — rejected qwen3-embedding:8b candidate (2026-07-01 A/B test)
- `06_emit_scaffolding_v1/v3/v4/v5.py` — pre-SH templates OR different-lineage lineage
- Older `_llm_helper_v1/v2/v3.py` — outdated model tokens

These live in `scripts/build/_legacy/` (or should be moved there next session
per the forever-archive principle).

## Orchestrator flags

`pipeline_canonical_v1.sh` accepts:

| Flag | Effect |
|---|---|
| _no flag_ | Dry-run — prints the plan and each phase's command; makes NO changes |
| `--commit` | Execute all phases |
| `--only 1,2,0` | Run only the listed phases (comma-separated numbers). Dry-run still applies unless `--commit`. |
| `--skip 3,5` | Skip the listed phases. |
| `--resume-from N` | Skip everything before Phase N in `PHASE_ORDER=(1 2 0 3 4 5 6)`. Replaces the previous `overnight_v3_resume.sh` pattern. |
| `-h` / `--help` | Print the docstring header. |

Examples:

```bash
# Full pipeline, dry-run first, then commit
bash pipeline_canonical_v1.sh
bash pipeline_canonical_v1.sh --commit

# Resume from Phase 3 after a Phase 3 crash (previously overnight_v3_resume.sh)
bash pipeline_canonical_v1.sh --commit --resume-from 3

# Just rebuild the DuckDB (masters + parquets + views), no wiki regen
bash pipeline_canonical_v1.sh --commit --only 1,2,0

# Cheap iterative test — skip the 3-hour Phase 3 and the 15-min Phase 5
bash pipeline_canonical_v1.sh --commit --skip 3,5
```

## What the orchestrator does that the old `overnight_v2.sh` / `overnight_v3_resume.sh` did not

1. **Locks canonical versions in one file** — future accidental invocation of
   pre-SH scripts is now impossible if you use the orchestrator.
2. **Unified logging** — everything under
   `~/Desktop/Archive/logs/pipeline_<UTC>/phase_N_<script>.log`. Also writes
   `shape_audit_BEFORE.txt` and `shape_audit_AFTER.txt` for paste-ready
   `_decisions_log.md` entries.
3. **`--only` / `--skip` / `--resume-from`** — three ways to run subsets of
   the pipeline. Replaces the pattern of having a separate `_resume` script
   for every failure scenario.
4. **Idempotent** — every phase is safe to re-run against completed state.
   Phase 1/2 rebuild deterministically from masters; Phase 3-6 overwrite
   their outputs.
5. **Preflight validation** — verifies every canonical script exists before
   starting. If you accidentally moved one to `_legacy/`, you'll find out at
   preflight, not at Phase 3 after 2 hours.

## Cleanse phases (Phase A/B/C) are OUT of scope for this orchestrator

The one-off `apply_tech_mislabel_v1.py`, `apply_entity_metadata_v1.py`, and
`apply_entity_aliases_v1_sap.py` are cleanse operations, not pipeline phases.
They run BEFORE the pipeline. When needed, invoke them directly from
`~/Desktop/Archive/scripts/` (their runtime location).

The old `overnight_v2.sh` fused cleanse + pipeline into one script because
they always ran together during the 2026-07-07 SAP-unblock cleanse.
`pipeline_canonical_v1.sh` deliberately does NOT include cleanse phases —
running the pipeline should not touch masters. If you need a combined
cleanse-then-pipeline flow, invoke the cleanse scripts first, then run the
pipeline.

## Where the canonical scripts live

- **Mac runtime:** `~/Desktop/Archive/scripts/build/` (with legacy versions in
  `_legacy/` subdirectory — same layout as the repo)
- **Repo:** `shorttack/aberdeen-group-archive/scripts/build/` (public)

The orchestrator itself lives at:
- **Mac runtime:** `~/Desktop/Archive/scripts/pipeline_canonical_v1.sh`
- **Repo:** `shorttack/aberdeen-group-archive/scripts/pipeline_canonical_v1.sh`

## Cross-references

- `kastner-archive-pipeline` skill Workflow C names the Phase 1-6 sequence
  but currently points at the pre-SH versions (needs v1.8 patch).
- `Perplexity_Only/CANONICAL_IDS.md` governs entity/tech slugs; independent
  of pipeline versioning.
- `Perplexity_Only/MASTERS_NOTES.md` governs master CSV schemas.
- Shape audit format is codified in the orchestrator (`shape_audit()` function)
  and matches the skill's Shape Audit section.
