# Perplexity_Only/

This directory holds context files intended specifically for AI agents
(Perplexity Computer, Claude Code, Codex, and any other LLM-driven
collaborator) that work on this archive. Files here are NOT part of the
research dataset and are NOT exported to Zenodo's primary data manifest;
they exist solely to give agents the operational context they need to
avoid repeating mistakes from prior sessions.

## Why this directory exists

Across multiple sessions in May and June 2026, Perplexity Computer
repeatedly tripped over conventions that were obvious to Pete but
invisible to a fresh agent context — most notably:

- The `_master_entities.csv` / `_master_technologies.csv` schema is
  8-col globally-deduped WITHOUT `study_id`, while the per-study
  `entities.csv` / `technologies.csv` produced by the `archival-ingest`
  v20 pipeline are 9-col WITH `study_id`. M:N relationships live in
  separate join tables. This was the root cause of the 2026-06-12 v1
  apply script crash.
- The wiki migrated from `~/Desktop/kastner_wiki/` to
  `~/Repos/kastner-aberdeen-wiki/` on 2026-06-01.
- The canonical observation ID format is `<study_id>-OBS-NNN`, not
  `<study_id>.NNN`, since the §21 Universal Normalizer landed
  2026-05-24.

Mixing this kind of agent-context documentation into the human-facing
`archive_masters/` directory is noisy and easy to overlook. Keeping it
in `Perplexity_Only/` makes it explicit and easy to surface from skills
and start-of-day routines.

## Contents

| file | purpose |
|---|---|
| `MASTERS_NOTES.md` | **The authoritative reference for the seven master CSVs.** Schema, ID conventions, history of breaking changes, known deferred work. ALL agents MUST read this before any masters edit. |
| `CANONICAL_IDS.md` | Authoritative cache of canonical `entity_id` and `tech_id` values, with the common-mistake variants that have been caught in prior sessions (`att-corporation` → `ent-att`, `ibm-powerpc` → `powerpc`, etc.). Consult before assigning any ID during extraction. |
| `PIPELINE_QUICKREF.md` | Six-phase pipeline commands (load → data layer → vault → indices → embeddings → scaffolding), apply-script contract, shape-audit query (with the `//` integer-division fix), and a catalog of "things to NEVER do." |
| `OLLAMA_STATE.md` | Installed local models, the `_llm_helper_v4.py` pin (qwen3.5:27b-mlx), how to verify Ollama is actually serving, and the "stale ollama window" gotcha. |
| `README.md` | This file. |

## How agents should use this directory

**At thread-start / day-start:**
1. Fetch all four reference files from `Perplexity_Only/` (via `gh api repos/shorttack/aberdeen-group-archive/contents/Perplexity_Only/<file>` from the sandbox, or read directly from `~/Desktop/Archive/Perplexity_Only/` on the Mac).
2. Summarize into working context: `MASTERS_NOTES.md` schema + deferred work, `CANONICAL_IDS.md` anti-pattern table, `PIPELINE_QUICKREF.md` "never do" list, `OLLAMA_STATE.md` current pin.
3. Only then proceed with whatever the user asked.

**Before any masters edit:**
1. Re-read `MASTERS_NOTES.md` schema section. Confirm:
   - Entity/tech masters are 8-col globally-deduped, no `study_id`.
   - Observation master is 17 cols.
   - Canonical obs_id is `<study_id>-OBS-NNN`.
   - The two M:N join tables exist and must be updated together with entity/tech changes.
2. Cross-check any new entity/tech IDs against `CANONICAL_IDS.md` — DO NOT use any variant from the "Common mistakes" column.
3. Use the `apply_passb_transcripts_v2.py` pattern (commit `0391dabf`) as a reference template for merge scripts.

**After any masters edit:**
1. Run the §11v shape audit per `PIPELINE_QUICKREF.md` (with `//` not `/` for `decades_covered`).
2. Verify backup files were created (named `*.bak_<context>_YYYYMMDDTHHMMSSZ`).
3. Update `MASTERS_NOTES.md` history section if the change affects schema or conventions.
4. Update `CANONICAL_IDS.md` if a new repeat-offender ID variant was caught and patched.

**Before swapping any local model:**
1. Read `OLLAMA_STATE.md`.
2. Run the formal `local-model-upgrade-gates` skill (4-gate evaluation).
3. Do NOT change `_llm_helper_v4.py` mid-pipeline.

## What does NOT belong here

- Research data (goes in `archive_masters/`)
- Per-study packages (go in `passb_output/`, `passa_output/`, etc.)
- Build scripts (go in `scripts/`)
- Wiki source files (live in `~/Repos/kastner-aberdeen-wiki/`)
- Decision-log entries (go in `_decisions_log.md` or `decisions/`)

This directory is for *agent operating context only*.

---

**Maintained by:** Pete Kastner (human) + Perplexity Computer (agent).
**Created:** 2026-06-12 (§11u-cont Pass B Completion Commit, Release v1.6.1).
