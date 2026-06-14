# Pass C v2 — Clean-Slate Full Qwen Rescore Plan

**Created:** 2026-06-14 AM (§11v cont 7, new day session)
**Status:** APPROVED by Pete. Calibration test build is next.
**Owner:** Pete Kastner
**Companion docs to create:** `decisions_log_entry_2026_06_14_pass_c_v2_clean_slate_v1.md`

---

## Why this exists (one paragraph)

The prescience scoring substrate in the repo (`_master_prescience_scores.csv`, 3,761 rows) covers only **15.7% of the 23,926 obs in `_master_observations.csv`** (corpus invariant: one row per obs). The "124 high-prescience studies" claim in v1.6 release notes was computed against this 15.7%-covered substrate. Coverage breakdown: 3,661 rows Sonar Pro + 100 rows Claude Sonnet 4.6, spanning 492 distinct studies of 1,452 total. Buckets C+D (~1,126 studies) were deferred per v1.6 backlog and never run. The 17 new transcripts (295 obs from v1.6.1) have zero scores. Pete's instinct ("it used to be simple") was correct — coverage is incomplete and provenance is fractured across two cloud scorers.

**Decision (Pete, 2026-06-14 ~08:08 EDT):** Clean-slate full Qwen Pass C rescore of all ~24,221 obs in a new subdirectory. Old files untouched. Repo is the safety net for rollback. Calibration test of 30 obs (10 from each batch) precedes the full run.

---

## Architectural principles

1. **One row per obs.** Every row in `_master_observations.csv` (currently 23,926; will be ~24,221 after the 17-transcript obs are merged if not already) must have exactly one row in `_master_prescience_scores.csv`. Composite key: `obs_id`.
2. **One scorer.** Qwen 3.5 27B-MLX via Ollama on M4 Pro Mac mini. Validated at kappa 0.853 vs. Claude reference in `model_prescience_scoring_finding_v1.md` (2026-05-25).
3. **One prompt version.** Pinned hash in run manifest. New prompt v3 — TBD whether identical to current prompt or refined.
4. **Append-only spool with checkpointing.** Restart-safe per `obs_id`. No double-scoring, no skipped rows.
5. **Phase 2.5 hard gate.** After v2 ships clean, codify into `kastner-archive-pipeline` skill: Pass C must run on any unscored obs before Phase 3 wiki regen.

---

## Three batches in the current substrate

| Batch | Model | Studies | Obs | Status |
|---|---|---|---|---|
| 1 | sonar-reasoning-pro | 479 distinct (incl. 17 overlap with Batch 2) | 3,661 | In repo, dates 2026-05-29 to 2026-05-30 |
| 2 | claude-sonnet-4.6 | 30 distinct (17 overlap with Batch 1) | 100 | In repo, same dates |
| 3 | none yet (Qwen-target) | 17 transcripts | 295 | NOT in repo, NOT in master, in obs master since 2026-06-12 |

Total scored: 3,761 obs / 492 studies. Total corpus: 23,926 obs / 1,452 studies. **Gap: ~20,165 obs / 960 studies unscored.**

---

## Calibration test (30 obs) — build first

### Sample design

- **10 obs from Batch 1** (random sample from the 3,661 Sonar Pro rows, fixed seed)
- **10 obs from Batch 2** (random sample from the 100 Claude Sonnet 4.6 rows, fixed seed)
- **10 obs from Batch 3** (random sample from the 295 transcript obs in `_master_observations.csv`, fixed seed)

### Sample manifest

Sandbox produces a CSV: `calibration_30_obs_v1.csv` with columns:
- `obs_id`
- `study_id`
- `batch` (1 / 2 / 3)
- `existing_score` (Sonar score for Batch 1, Claude score for Batch 2, NULL for Batch 3)
- `existing_model` (`sonar-reasoning-pro` / `claude-sonnet-4.6` / `none`)
- `claim_text` (the obs text being scored)
- `study_title` (context for Pete's spot-check)

### Calibration run

- Driver: `run_prescience_calibration_v5_qwen_30obs.py` (new — does not overwrite v4)
- Inputs: `calibration_30_obs_v1.csv`, Qwen 27b-mlx via Ollama
- Outputs: `calibration_results_v5.csv` (same 30 obs × Qwen scores), `calibration_report_v5.md` (3 kappa numbers + per-obs comparison table)
- Expected runtime: ~5 min on Mac (30 obs × ~10 sec/obs)

### Decision gate after calibration

- **All three kappas ≥ 0.7:** proceed to full run.
- **Any kappa < 0.7:** stop, debug prompt, re-calibrate before committing to a multi-day full run.

---

## Full run (after calibration passes)

### Outputs (all in new subdir on Mac)

```
~/Desktop/Archive/pass_c_v2/
├── run_manifest_v1.md              # what / why / when / model / prompt hash
├── prescience_scores_qwen_v2.csv   # the new spool (one row per scored obs)
├── checkpoint_v2.jsonl             # restart-safe per-obs ledger
├── failures_v2.jsonl               # any obs that failed parsing
├── run_report_v2.md                # populated at completion
└── logs/
    └── run_v2.log                  # full stdout/stderr
```

### Driver

`run_prescience_pass_c_v6_qwen_full.py` (new — does not overwrite v5).

### Schema (12 cols, +1 vs. v1)

```
obs_id, study_id, model, prescience_score, confidence, rationale,
scored_at, scorer_version, source_pass, elapsed_sec, parse_ok, prompt_hash
```

`prompt_hash` is new — locks reproducibility.

### Process contract

```
1. Load _master_observations.csv (~24,221 rows).
2. For each obs:
   a. If obs_id is in checkpoint_v2.jsonl → skip (idempotent restart).
   b. Build prompt v3 with claim_text + study context.
   c. Call Qwen 27b-mlx via Ollama, parse JSON response.
   d. On success: append row to prescience_scores_qwen_v2.csv + checkpoint.
   e. On failure: append to failures_v2.jsonl + checkpoint with parse_ok=False.
3. Every 100 obs: flush + print rate (obs/sec) and ETA.
4. On completion: emit run_report_v2.md with totals + score distribution.
```

### Time budget

- Pete-approved tolerance: **weeks** ("Can run for hours" → revised to "weeks").
- Estimate at projected throughput (~13 tok/sec, ~10 sec/obs): **~67 hours single-threaded**.
- UPS protects against power blips. Checkpoint protects against everything else.

---

## Recovery contract

- **Old files untouched during run.** `_master_prescience_scores.csv` (Mac and repo) remains at current state.
- **Repo not committed to during run.** Sandbox does not commit anything until Pete authorizes promotion.
- **Promotion (separate session, after Pete validates v2):** ship `pass_c_v2/prescience_scores_qwen_v2.csv` to repo, replace `_master_prescience_scores.csv` (with `bak_pre_qwen_v2_promote_<ts>` backup), re-run Phase 1+2+3 once. Wiki then reflects the full corpus.
- **The 124 high-prescience claim will move.** Whatever the new number is, that's truthful. Document delta in v1.7.0 release notes.

---

## Phase 2.5 hard-gate (D6 audit deliverable)

After v2 ships clean, codify in `kastner-archive-pipeline` skill v1.7 → v1.8:

```
Pass A → Pass B → masters merge + commit
  → Phase 1+2 (load + data layer)
  → **Phase 2.5: Pass C on any unscored obs** ← HARD GATE
    → append to _master_prescience_scores.csv + commit
      → Phase 3 (wiki emit)
        → Phase 4-6
```

Gate query:
```sql
SELECT count(*) FROM observations o
LEFT JOIN prescience_scores p ON p.obs_id = o.obs_id
WHERE p.obs_id IS NULL;
```

If count > 0 → HALT. Operator must either run Pass C or explicitly waive via `--skip-pass-c-gate "reason"` (logged to decisions). Default is HALT.

---

## Next concrete actions (in order)

1. **Build calibration sample manifest** (`calibration_30_obs_v1.csv`) in sandbox.
   - Fetch repo `_master_prescience_scores.csv` (already in `/tmp/repo_master_prescience.csv`).
   - Fetch repo `_master_observations.csv` for Batch 3 obs_ids (the 295 from 17 transcripts).
   - Random sample 10 / 10 / 10 with fixed seed.
   - Output to workspace: `calibration_30_obs_v1.csv`.

2. **Write calibration driver** `run_prescience_calibration_v5_qwen_30obs.py` to workspace.

3. **Pete reviews both files in workspace.**

4. **Ship to Mac** via `kastner-github` script-delivery protocol:
   - Commit to `aberdeen-group-archive/scripts/` and `aberdeen-group-archive/pass_c_v2/`
   - Pete `git pull` on Mac, `cp` into `~/Desktop/Archive/scripts/` and `~/Desktop/Archive/pass_c_v2/`

5. **Pete runs calibration on Mac.** ~5 min.

6. **Review calibration_report_v5.md together.** Decide go / no-go.

7. **If go:** write `run_prescience_pass_c_v6_qwen_full.py`, ship, Pete kicks off full run.

8. **Full run completes (~1 week).** Pete pings sandbox session for promotion workflow.

---

## Open questions (deferred until calibration passes)

- **Prompt v3 contents** — identical to v5 driver prompt or refined? Decision after seeing calibration kappas.
- **Subdirectory name** — Pete preference: `pass_c_v2/` (short) or `pass_c_v2_qwen_full_run/` (descriptive). Defaulting to `pass_c_v2/` unless Pete overrides.
- **Pre-filter or no pre-filter?** v1 used `pre_filter_scoreable_obs_v7.py` to drop "unscoreable" obs (figure captions, methodology framing). Under the one-row-per-obs invariant, those should still get rows with `prescience_score = 0` or `model = "pre-filter-skip"`. Decision: include all obs, let Qwen assign 0 where appropriate. Pre-filter becomes optional / advisory only.

---

## Risks acknowledged

1. **Qwen kappa may not reproduce 0.853 across the full corpus.** The original calibration was 50 obs on one study (`ra-warehouseautomation`). Cross-genre validity is what the 30-obs test is for.
2. **Prompt v3 may need iteration.** First calibration pass might fail; budget for 1-2 prompt revisions before full kickoff.
3. **The 124 high-prescience number will change.** Possibly significantly. Release notes must explain the delta.
4. **17 transcripts merge state.** Need to verify Batch 3's 295 obs are actually in Mac `_master_observations.csv` already (per §11u-cont Pass B closeout, they should be — masters merge commit `ce3262f3` on 2026-06-13).

---

_Owner: Pete Kastner. Plan ratified 2026-06-14 ~08:08 EDT. Calibration build is next action._
