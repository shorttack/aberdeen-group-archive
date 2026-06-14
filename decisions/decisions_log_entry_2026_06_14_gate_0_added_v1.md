# Decision: Add Gate 0 to local-model-upgrade-gates skill (v1.0 → v1.1)

**Date:** 2026-06-14
**Session:** §11v continued
**Trigger:** Pete escalation — agent re-discovered Qwen 3.x `think:false` requirement ~2 weeks after first finding it, wasting all 30 calibration v5 obs (parse_ok=false). The four-gate skill was designed to prevent §11q-style waste from skipping evidence reading, but had no formal hook for institutional-memory recall.

## Decision
Insert Gate 0 ("Read the gotchas ledger") as the first gate in `local-model-upgrade-gates` skill. Bump version 1.0 → 1.1.

## What Gate 0 requires
Before any benchmark reading, the agent MUST:
1. Fetch `Perplexity_Only/OLLAMA_GOTCHAS.md` from `shorttack/aberdeen-group-archive`.
2. Read every G-entry end-to-end.
3. For each G-entry whose `Affected models` matches the candidate's family, hold the symptom + fix in working context.
4. Pre-apply documented fixes to Gate 3 fixture predictions and Gate 4 A/B harness payloads.

## Stop-conditions
- A G-entry explicitly bans the family for an in-scope workload.
- Candidate tag matches a known-broken tag in any G-entry.

## Cost
60 seconds. Cheaper than any other gate. Cheaper than re-discovering even one landmine.

## Why this exists separately from Gate 1
Gate 1 is open-web evidence reading (independent benchmarks). Gate 0 is closed-loop institutional memory (our own ledger). The two are categorically different sources — Kaitchup will never document our specific Ollama HTTP payload quirks, and our ledger will never have benchmark scores. Conflating them would lose either signal.

## File anchoring decision
OLLAMA_GOTCHAS.md lives in the **archive repo** (`Perplexity_Only/`), NOT inside the skill's `references/`. Rationale:
- The repo file is fetched by name from Mac, sandbox, and any future session without loading this skill.
- New gotchas can be added by any session that hits one, without forcing a skill version bump.
- Future skills that aren't model-evaluation-specific can also reference it (e.g., daily ingest skill could read it before any LLM call).
- Skill files describe process; landmine ledgers describe data. They evolve at different rates.

## Companion changes
- Description field updated to mention Gate 0.
- Quick Reference table gets Gate 0 row.
- "Four Gates" heading renamed to "Five Gates".
- Anti-Patterns section gains "Don't skip Gate 0" entry referencing the 2026-06-14 v5 calibration disaster.
- Changelog field added to metadata.

## Repo location
- `decisions/decisions_log_entry_2026_06_14_gate_0_added_v1.md` (this file)
- Skill itself is in the user-scoped skill library (skill_id `0fda0938-7ab8-4670-838a-70b19bcb4b49`), not in the repo.

## Sequence of automatic standing-rule entries today
1. PASS_C_V2_QWEN_FULL_RESCORE_PLAN_v1 + decision + log (08:11 + 08:28)
2. Calibration manifest + log update (08:34)
3. Calibration driver v5 + log update (08:35)
4. v5b fix + log update (08:53)
5. OLLAMA_GOTCHAS.md + decision + log (08:54)
6. **Gate 0 skill update + decision + log (this entry)**
