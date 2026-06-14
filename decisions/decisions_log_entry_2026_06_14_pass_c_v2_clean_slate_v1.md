# Decisions Log Entry — Pass C v2 Clean-Slate Qwen Rescore (D6)

**Date:** 2026-06-14 AM (EDT)
**Session:** §11v cont 7 (new day)
**Status:** Decision locked. Calibration build in progress.

---

## Context

D6 prescience architecture audit (raised 2026-06-13 PM) opened with Pete's instinct: *"It used to be simple. Now, I don't think I can explain the process or the files used."* Today's session converted that instinct into a verified finding.

## Finding

The repo `_master_prescience_scores.csv` contains **3,761 rows** covering **15.7% of obs** (3,761 / 23,926) and **33.9% of studies** (492 / 1,452). Distribution:

- **3,661 rows** model = `sonar-reasoning-pro` (Batch 1)
- **100 rows** model = `claude-sonnet-4.6` (Batch 2)
- Scoring dates: 2026-05-29 to 2026-05-30 only
- 17 studies overlap between the two models (calibration set)

Release v1.5.0 release notes (2026-05-29) stated production Buckets A+B Pass C was "**queued for v1.6**." Release v1.6 release notes (2026-05-31) asserted "**124 high-prescience studies** (Pass C, `prescience_max ≥ 4`)" — but that number was computed against the 3,761-row substrate, not the corpus. v1.6 backlog item #2 (Buckets C+D, ~1,126 studies) was deferred and **never run**.

The 17 new transcripts (v1.6.1, 2026-06-13) added 295 obs to `_master_observations.csv` with **zero prescience scoring** in the repo.

**Pete's recollection of "Batch 1 ≈ 14,500 rows for ~969 studies" was the v1.5.0 _plan_ for Buckets A+B, not the actual production output.** Reconstruction: the 2026-05-30 Pass C run produced 3,761 rows total (per `logs/pass_c_cloud_v1_run_report.md` showing "API rows: 336" for one segment of that day). The plan was never completed; the release notes shipped declaring it done.

## Architectural invariant (Pete, this session)

> "We need one row per observation = ~24,600"

Composite key: `obs_id`. Foreign-key constraint into `_master_observations.csv`. Current state violates the invariant by ~20,165 rows.

## Decision

**Clean-slate full Qwen Pass C rescore of all ~24,221 obs.** Pete's words:

> "Clean-slate in a new subdirectory is cleanly recoverable to our current (poor) condition. We have a backed up Repo. Yes, we should do that. Costs no credits. Not bothering me. Can run for hours."

Subsequently revised wall-time tolerance to **weeks**.

## Approach

1. **Calibration test first.** 30 obs (10 from Batch 1 / 10 from Batch 2 / 10 from Batch 3) scored by Qwen 27b-mlx, compared against existing Sonar / Claude scores (Batches 1+2) and Pete's judgment (Batch 3). Three kappa numbers. Go/no-go gate at kappa ≥ 0.7.
2. **Full run in new subdirectory** `~/Desktop/Archive/pass_c_v2/`. Old files (Mac and repo) untouched during the run. Restart-safe per `obs_id` via checkpoint JSONL.
3. **One scorer, one prompt, one corpus.** Qwen 3.5 27B-MLX (calibration-validated at kappa 0.853 vs. cloud per `model_prescience_scoring_finding_v1.md`). Prompt v3 hash-pinned in run manifest.
4. **Promotion is a separate, later session.** After Pete validates v2 output, replace `_master_prescience_scores.csv` (with `bak_pre_qwen_v2_promote_<ts>` backup), re-run Phase 1+2+3 once. Wiki reflects full corpus.
5. **The "124 high-prescience studies" number will move.** Whatever Qwen says across 24,221 obs is the truthful number. Release notes for v1.7.0 must explain the delta.

## Architectural consequence (D6 deliverable)

**Phase 2.5 hard-gate** to be codified into `kastner-archive-pipeline` skill after v2 ships clean:

```
Pass A → Pass B → masters merge + commit
  → Phase 1+2
    → Phase 2.5 (Pass C on unscored obs) ← HARD GATE
      → append + commit
        → Phase 3 (wiki emit)
          → Phase 4-6
```

Gate query:
```sql
SELECT count(*) FROM observations o
LEFT JOIN prescience_scores p ON p.obs_id = o.obs_id
WHERE p.obs_id IS NULL;
```

If count > 0 → HALT Phase 3. Operator must run Pass C or explicitly waive via `--skip-pass-c-gate "reason"` (logged here).

## Files affected (this decision)

- **New:** `Perplexity_Only/PASS_C_V2_QWEN_FULL_RESCORE_PLAN_v1.md` (commit `75509f35`)
- **New (this entry):** `decisions/decisions_log_entry_2026_06_14_pass_c_v2_clean_slate_v1.md`
- **New (running log):** `logs/session_2026_06_14_agent_progress.md`
- **Existing (untouched):** `_master_prescience_scores.csv`, all Pass C scripts, all spool files
- **Pending (next):** `calibration_30_obs_v1.csv`, `run_prescience_calibration_v5_qwen_30obs.py`

## Approvals

- Pete Kastner, 2026-06-14 ~08:08 EDT — clean-slate approved
- Pete Kastner, 2026-06-14 ~08:10 EDT — re-score the 295 (no surgical promote), build the 30
- Pete Kastner, 2026-06-14 ~08:18 EDT — plan saved to `Perplexity_Only/` confirmed

---

_Owner: Pete Kastner. Logged 2026-06-14 AM session._