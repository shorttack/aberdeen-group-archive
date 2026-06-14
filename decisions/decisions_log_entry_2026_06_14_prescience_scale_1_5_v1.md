# Decision: Canonical Aberdeen prescience scale is 1-5 (B1 over B2/B3)

**Date:** 2026-06-14
**Session:** §11v continued, ~09:18 EDT
**Trigger:** During Pass C v2 calibration v6, Qwen scored on 0-100 (as the prompt rubric instructed) while the production master `_master_prescience_scores.csv` already contained Sonar (3,661 rows) and Claude (100 rows) scores on a 1-5 integer scale. Kappa returned 0.000 across multiple runs. Architectural inconsistency surfaced.

## Three options surfaced
- **B1 (chosen):** Adopt 1-5 (master wins). Existing master rows untouched. Rewrite Qwen prompt + locked Pass C fixture + driver to 1-5.
- **B2 (rejected):** Adopt 0-100 (fixture wins). Linear-map existing 1-5 master rows to 0-100. Mutates 3,761 existing rows.
- **B3 (rejected):** Store both scales. Schema churn (two new columns), most defensive but adds long-tail complexity.

## Decision rationale (Pete)
"B1. I was happy with that distribution."

The master is the source of truth for what Aberdeen has already been told the scoring means. The Pass C fixture (locked in `local-model-upgrade-gates` skill, v1, 2026-06-02) was aspirational and didn't match the actual production data. The 1-5 scale is more interpretable for the player-rebuttal workflow Pete runs.

## Scope of changes
1. **`scripts/run_prescience_calibration_v7_qwen_30obs.py`** — new driver, does NOT overwrite v5b/v6. Prompt rubric, validation range (1-5), bin_score function, kappa binning all aligned to 1-5.
2. **`local-model-upgrade-gates/assets/fixtures/pass_c_scoring.md`** — bumped to v2. System prompt, tier mapping, pass criteria, bonus check, anti-fixture rules all updated. Version history added.
3. **`Perplexity_Only/OLLAMA_GOTCHAS.md`** — added G2: "Prompt scale must match production master scale". Includes the pre-flight check command.
4. **No master CSV mutations.** Existing Sonar+Claude rows are unchanged.
5. **Full ~24,221-obs rescore (when it ships)** will produce 1-5 integer scores, compatible with existing rows, no schema migration needed.

## Tier mapping for 1-5 (new canonical)
| Score | Tier | Meaning |
|---|---|---|
| 1 | low | Wrong / contradicted by events |
| 2 | low | Partially wrong; missed key dynamics |
| 3 | medium | Mixed / ordinary forecasting |
| 4 | high | Substantially correct with lead time |
| 5 | exceptional | Strikingly correct, non-obvious framing |

Tier `low` covers both score 1 and score 2 — collapses the failure space so downstream `GROUP BY tier` queries don't over-split rare bad scores.

## Calibration gate (unchanged)
- B1 (Qwen vs Sonar) kappa >= 0.70
- B2 (Qwen vs Claude) kappa >= 0.70

Both required to GO for full ~24,221-obs Qwen rescore.

## Downstream implications
- **v1.7.0 release notes** must explicitly state the prescience scale is 1-5 (the v1.5/v1.6 notes implied 0-100 in the "124 high-prescience studies" framing). The 124 count is rows where score >= 4 on the 1-5 scale — that number stays valid.
- **Wiki prescience displays** continue showing 1-5 integers.
- **Player-rebuttal workflow** unchanged.

## Repo location
- `decisions/decisions_log_entry_2026_06_14_prescience_scale_1_5_v1.md` (this file)
- `Perplexity_Only/OLLAMA_GOTCHAS.md` (G2 entry)
- `scripts/run_prescience_calibration_v7_qwen_30obs.py`
- Skill update: `local-model-upgrade-gates` user library (skill_id `0fda0938-7ab8-4670-838a-70b19bcb4b49`), fixture v2.

## Standing rules followed
- Big decision → `decisions/` (this file)
- Progress → `logs/session_2026_06_14_agent_progress.md` (appended below)
