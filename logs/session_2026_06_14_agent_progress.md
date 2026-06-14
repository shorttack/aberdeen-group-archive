# Agent Progress Log — 2026-06-14

Running log of agent actions and findings during the §11v cont 7 session. Append-only. New entries at the bottom.

---

## 07:18 EDT — New day setup

- Loaded `kastner-new-day` skill.
- Fetched canonical `WORKLIST.md` from `aberdeen-group-archive` origin/main (sha `3ab82447`).
- Wrote `WORKLIST_2026_06_14.md` to workspace + undated mirror.
- Pre-edit audit: 8 sections / 99 open items / 28 closed.
- Edited 2 sections: `**Last updated:**` line + `## Done this session` header.
- Post-edit audit unchanged (8 / 99 / 28). Nothing lost.
- Today's focus: §11v PRESCIENCE ARCHITECTURE AUDIT (D6).

## 07:30 EDT — Pete launches D6 audit dialog

- Pete: repo prescience master is very stale. Same on Mac. Head rows all Sonar model. Asked architectural questions:
  - Q1: What file contains new Qwen obs on Mac?
  - Q2: Should master prescience be a canonical subset of master observations?
- Pete recalled batch composition: ~965 studies Batch 1 (Sonar), ~20/469 Batch 2 (Claude), 0 of 17 Batch 3.

## 07:42 EDT — Flowchart-fix decision

- Pete: "keeping prescience scoring up to date is a flaw in your flowchart."
- Agent proposed Phase 2.5 hard-gate between masters merge and Phase 3.
- Pete accepted: "hard gate and condensed phases 1-6 run together."

## 07:45–07:53 EDT — Spool / batch reconstruction

- Mac `_master_prescience_scores.csv`: 4,083 lines.
- Mac spool `prescience_scores_pass_c_cloud_v1.csv`: 2.5 MB, mtime Jun 13 11:30.
- Mac spool backup `bak_pre_dectp_preseed_20260613T151325Z`: 3,762 rows, May 30 15:30.
- Pete confirmed: Batch 1 (~14,500 rows) was **never** in the spool — done by LLM prior to May 20.
- Found new artifacts on Mac:
  - `archive_masters/_master_prescience_scores.csv.bak_pre_promote_20260613T175046Z`
  - `aberdeen-group-archive/_master_studies.csv.bak_pre_prescience_sync_20260613T181126Z`
  - 621 abandoned-run files under `_pass_c_abandoned_runs/20260526/`

## 07:54 EDT — Repo master read

- Fetched repo `_master_prescience_scores.csv` via `gh api -H Accept:application/vnd.github.raw`. **3,762 rows.** 11-col schema.
- Model distribution: 3,661 `sonar-reasoning-pro` + 100 `claude-sonnet-4.6` + 1 unknown.
- Coverage: 492 distinct studies / 1,452 total (33.9% studies, 15.7% obs).
- Scoring window: 2026-05-29 to 2026-05-30 only.
- 17-study overlap between Sonar and Claude (the calibration set).

## 07:57 EDT — Pete corrects batch mapping

- Pete: 492 distinct = Batch 2 (not Batch 1 as agent had labeled).
- Pete: architectural invariant is "one row per observation = ~24,600."
- Reconstruction: 14,500 / 969 was the v1.5 **plan**, not the actual production.

## 07:58 EDT — Release v1.5.0 / v1.6 verbiage check

- Pete pointed to repo release notes for v1.0.
- Fetched all 8 releases. v1.5.0 release notes explicit: "production Bucket A+B run against the full corpus is **queued for v1.6**" and "Bucket C + D prescience scoring (~1,126 studies)" listed in v1.6 backlog item #2.
- `model_prescience_scoring_finding_v1.md`: Qwen 27b-mlx at kappa 0.853 vs. Claude reference (50-obs calibration on `ra-warehouseautomation`).

## 08:04 EDT — Pete approves clean-slate

- Pete: "Clean-slate in a new subdirectory is cleanly recoverable to our current (poor) condition. We have a backed up Repo. Yes, we should do that."
- Wall-time tolerance: weeks (UPS protected).

## 08:08 EDT — Plan ratified, calibration approved

- Pete chose: rescore the 295 (no surgical promote). Build the 30-obs calibration test first.
- Pete asked for shorter responses.

## 08:11 EDT — Plan committed to repo

- Wrote `PASS_C_V2_QWEN_FULL_RESCORE_PLAN_v1.md` to workspace (200 lines).
- Committed to `Perplexity_Only/` at commit `75509f35`.

## 08:28 EDT — Pete flags missing automation

- Pete: agent should automatically (1) write decision summaries to `decisions/`, (2) keep a session progress log under `logs/`.
- Writing both retroactively for this session.

## NEXT — Build 30-obs calibration sample manifest


## 08:34 — Calibration sample built

- Ran `build_calibration_30_sample.py` → `calibration_30_obs_v1.csv`
- Seed: 20260614 (reproducible)
- Pool sizes: B1=3,661 obs / B2=100 obs / B3=552 obs from 35 transcript-matching unscored studies
- Output: 30 rows (10 each from Batches 1/2/3), header + 9 cols
- Sanity: split 10/10/10 confirmed; year range 1905–2007 (transcript-heavy)
- Next: ship to `Perplexity_Only/` in repo, then write calibration driver v5

## 08:35 — Calibration driver v5 written

- `run_prescience_calibration_v5_qwen_30obs.py` (360 lines, py_compile OK)
- Reads `Perplexity_Only/calibration_30_obs_v1.csv` on Mac under `~/Desktop/Archive/pass_c_v2/`
- Scorer: `qwen3.5:27b-mlx` via Ollama HTTP (temp=0.0, num_predict=256)
- 12-col v2 schema (adds `prompt_hash`)
- Append-only spool `calibration_v5_qwen_spool.jsonl` → restart-safe per obs_id
- Quadratic-weighted Cohen's kappa, 5 bins (0-19/20-39/40-59/60-79/80-100)
- Gate: kappa_B1 >= 0.7 AND kappa_B2 >= 0.7 → GO for full rescue
- Outputs: scores CSV + JSONL spool + `calibration_report_v5.md` with go/no-go
- B3 obs scored for inspection only (no prior scores → no kappa)
- Does NOT overwrite v4
- Mac path: `~/Desktop/Archive/pass_c_v2/Perplexity_Only/`

## 08:53 — v5 failed: Qwen 3.5 thinking-model trap

- All 28 obs returned empty `response` field; `done_reason=length`; 256-token budget consumed entirely by CoT in `thinking` field
- Root cause: Qwen 3.5 27B-MLX is a thinking model; Ollama exposes CoT in separate `thinking` key
- Fix: add `"think": false` to API payload, bump `num_predict` 256 → 512, fall back to `thinking` if `response` empty
- Patched script in place (still scripts/run_prescience_calibration_v5_qwen_30obs.py)
- Scorer version bumped to `pass_c_v2_calib_v5b` so spool rows are distinguishable
- Pete must delete the failed spool before re-running: `rm ~/Desktop/Archive/pass_c_v2/Perplexity_Only/calibration_v5_qwen_spool.jsonl`

## 08:54 — Pete escalation: lost institutional memory

- Pete: "You told me about think:false two weeks ago and then forgot it. THAT IS WHY I KEEP INSISTING YOU DOCUMENT DECISIONS IN WAYS THAT YOU CAN RECOVER YOUR MEMORY."
- Mea culpa. Documented in THREE durable locations:
  1. Long-term memory (memory_update) — two entries (gotcha + capture preference)
  2. `Perplexity_Only/OLLAMA_GOTCHAS.md` (new file, G1 covers Qwen 3.x think:false)
  3. To-add: `local-model-upgrade-gates` user skill should reference G1 as a hard precheck

## 08:55 — Gate 0 added to local-model-upgrade-gates skill (v1.0 → v1.1)

- New first gate: read `Perplexity_Only/OLLAMA_GOTCHAS.md` before any benchmark work
- Cost: 60 sec. Stop-conditions defined. Output requirements defined.
- Skill saved back to user library (skill_id `0fda0938-7ab8-4670-838a-70b19bcb4b49`, v1.1)
- Description, Quick Reference table, Anti-Patterns, and metadata all updated
- New companion-files section points to repo-anchored OLLAMA_GOTCHAS.md as the source of truth
- Decision summary: `decisions_log_entry_2026_06_14_gate_0_added_v1.md`

## 09:04 — v5b kappa=0.000 → root cause + v6 fix

- v5b RAN (think:false worked, all 28 obs returned valid JSON, real scores 0-95)
- Kappa 0.000 / NO-GO not a Qwen failure: v1 manifest builder pulled `notes` column ("Validated from prepared observation seed list...") into `claim_text` instead of `metric_value`. Qwen scored 28 identical boilerplate strings, not 28 distinct observations.
- Additional issue: ~60% of Sonar's "Batch 1" rows are pre-filter markers (score=-1 or 0, "image only" / "no claim" verdicts). Cannot ground-truth Qwen.
- v2 manifest builder fixes both:
  1. claim_text = metric_value (fallback metric_name)
  2. B1/B2 pools filter to prior score > 0 only
- v2 pool sizes: B1=1187 (was 3661), B2=62 (was 100), B3=3390 transcript-matching unscored obs with non-empty claims
- v6 driver: reads v2 manifest, filters score<=0 from kappa pairs as defense-in-depth, does NOT overwrite v5b
- Sample real claim: "Best in class manufacturers are more than twice as likely as other manufacturers..."

## 09:07 — v6 mis-shipped: still pointed at v5 files

- My multi-edit to v6 driver lost 6 of 8 substitutions; v6 still wrote to v5 spool/scores/report and printed [v5].
- Pete's run "resumed" from v5b's spool (28 entries) and exited in 2 sec without scoring v2 manifest.
- Fixed in place with sed; verified no v5 references remain except the SCORER_VERSION historical comment which I also bumped to v6.
- Pete needs to ALSO delete the v5b artifacts before re-running, since v6's spool is now a different filename.

## 09:11 — v6 was reading v1 manifest, not v2

- Identical Qwen scores to v5b run = obvious tell that v6 was reading the same input
- Root cause: same lost-multi-edit batch from 08:55. MANIFEST_CSV stayed at calibration_30_obs_v1.csv. The sed sweep only matched `calibration_v5_*` patterns, not the manifest filename.
- Fixed: MANIFEST_CSV → calibration_30_obs_v2.csv, docstring updated, full grep verified no v1/v5 leakage.
- LESSON FOR ME: when patching a critical config block, always grep ALL old-version tokens after the multi-edit, not just the obvious print banners.

## 09:18 — Scale architectural decision: B1 (1-5 wins)

- v6 kappa=0.000 root cause not v6 bug: Qwen on 0-100, master on 1-5
- Three options surfaced; Pete: "B1. I was happy with that distribution."
- v7 driver: prompt rubric, validation, bin_score, kappa all on 1-5
- Pass C fixture in local-model-upgrade-gates skill rescaled to 1-5 (v2)
- OLLAMA_GOTCHAS.md G2 added: "scale must match master"
- Decision summary: decisions/decisions_log_entry_2026_06_14_prescience_scale_1_5_v1.md
- Master rows untouched, no schema migration
- Tier mapping: 1-2=low, 3=medium, 4=high, 5=exceptional
- v1.7.0 release notes will need to make the scale explicit (deferred)

## 09:22 — v7 calibration run: NO-GO
- v7 (1-5 scale) kappa B1=0.091, B2=−0.269 across 30-obs manifest. Still NO-GO.
- SARS hot-topic obs root cause: manifest fed Qwen `"~100 cases/day"` alone (just metric_value), not the full row context.
- Confidence emitted 4,5 — out-of-rubric (canonical is 1-3, not 1-5).

## 11:47 — Pivot: "v1 Pass C passed Kappa we are failing on"
- Pete signaled there's an earlier-generation Pass C apparatus that already worked.
- Found `prescience_score_prompt_v2.md` on Mac (NOT in repo) — canonical 0-5 rubric, authored 2026-05-25.
- This is the source of truth. v2 fixture rescale to 1-5 was a misread of master distribution: 0 is "cannot assess", not a placeholder.

## 11:53 — Working dirs map: 574 LIVE + 309 ABANDONED
- Pete's screenshot revealed multiple working dirs across the Mac.
- Mapped: 574 live dirs under `~/Desktop/Archive/prepared/` and 309 abandoned dirs under `~/Desktop/Archive/_pass_c_abandoned_runs/20260526/prepared/`.
- Saved `WORKING_DIRS_MAP_2026_06_14.md` to Perplexity_Only/ (Pete: "Stop and save this map. It's gold.").

## 12:01 — May 26 abandon = agent-quality event
- Pete clarified: the abandon was triggered by firing the Agent + Pro→Max downgrade, not by methodology failure.
- Implication: the 2,723 Qwen scores in `_pass_c_abandoned_runs/` may be salvageable for calibration.

## 12:54 — Audit verdict: SALVAGE
- `audit_abandoned_qwen_run_v1.py`: 2,723 rows, 100% parse_ok, single model (Qwen 3.5 27B MLX), 2,722 obs overlap with master.
- Score distribution: lives in {4,5}. Plausibly the same prompt apparatus as v2 prompt file.

## 12:58 — Kappa v1
- `compute_qwen_master_kappa_v1.py`: κ(Qwen vs Sonar) = 0.2379 on n=1,041 paired obs (both scored 1-5).
- κ(Qwen vs Claude) = 0.1227 on n=36 (small overlap).
- Confusion matrix revealed +1 systematic offset (Qwen scores ~1 point higher than Sonar) AND Sonar abstention dominance.

## 13:05 — Kappa v2: all variants fail 0.70
- `compute_qwen_master_kappa_v2.py` ran four variants:
  - A. Raw 5-class: κ = 0.2379, exact-match 30.4%
  - B. Qwen−1 offset shift: κ = 0.3308, exact-match 51.0% (best)
  - C. Tier-bucket (low/mid/high): κ = 0.2393, exact-match 66.2%
  - D. Best linear shift (−1): κ = 0.3308
- Abstention: both=810, qwen-only=9, sonar-only=795 (88× asymmetry).
- All variants fail 0.70 gate; all fail 0.60 substantial threshold.
- **NO-GO for full Qwen rescore confirmed.**

## 13:08 — Decision: three-path strategy
- **Path 1 (short-term, effective immediately):** Sonar (`sonar-reasoning-pro`) remains primary Pass C scorer. Continue Sonar/Claude for remaining ~21,500 obs via cloud pipeline.
- **Path 2 (documented, not adopted):** Qwen pre-filter + Sonar scorer hybrid. Save ~31% Sonar API volume. Available when cost becomes pressure.
- **Path 3 (medium-term):** Re-evaluate Llama 3.3 70B / DeepSeek R1 70B / Mistral Large 2 against locked 1,041-obs fixture.
- Qwen 27B kept for Phase 3 wiki gen, kw_ask synthesis, summarization, `is_non_claim()` filtering.
- Decision committed: `decisions/decisions_log_entry_2026_06_14_qwen27b_calibration_failed_v1.md` (commit `95e0595b`).

## 13:14 — Why Qwen failed structurally
- Sonar (web-grounded) abstains when it can't verify (score=0). Qwen (frozen LLM) commits from training-data priors.
- Two different cognitive tasks under the same prompt. Prescience scoring is knowledge-retrieval intensive.
- Without grounding, frozen LLM defaults to optimistic-prior commitments. NOT fixable via prompt anchoring.
- Documented as G3 in `Perplexity_Only/OLLAMA_GOTCHAS.md`.

## 13:20 — Follow-on commits (this turn)
- OLLAMA_GOTCHAS.md: G2 split into G2a (`num_predict`) and G2b (scale-must-match-master); G3 added (frozen-LLM scoring underperforms grounded).
- `local-model-upgrade-gates` skill: pass_c_scoring.md rewritten to v3 (canonical 0-5 + Layer 2 paired-fixture lock at 1,041 obs); SKILL.md updated with Qwen failure baseline (κ_max=0.331) and frozen-LLM anti-pattern; decision log bundled into `references/`.
- Session log: today's full arc captured here.

## Commits shipped today (chronological)
- `49d0c392` (segment start)
- `2d80c66d` v7 driver (1-5 scale)
- `51f9873c` working dirs map v1
- `accf7e8e` map v2 (CSV drift note)
- `91765ea6` map v3 (May 26 cause)
- `b292c986` audit script
- `583cd584` kappa v1
- `8309e0c0` kappa v2
- `95e0595b` Qwen calibration failed decision + three-path strategy
- **(pending this turn)** OLLAMA_GOTCHAS G3 + session log + skill v1.3
