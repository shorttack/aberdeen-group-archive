# Log — 2026-06-14 (Sunday) — §11v Tier A Launch

## Session timing
- Resumed from compaction ~15:14 EDT
- Tier A sample built + pushed: 15:16 EDT (commit `d2f6abb7`)
- Background run launched: ~15:24 EDT (PID 73051)
- Decisions + log written: 15:29 EDT

## Sequence of events

| Time (EDT) | Event |
|---|---|
| 15:14 | Pete reports `FileNotFoundError` on Tier A driver run (sample not yet built) |
| 15:15 | Computer diagnoses: previous turn ended awaiting "build 5,000?" confirmation; Pete ran ahead |
| 15:16 | Pete: "yes, build 5,000" — Computer builds 5,000-obs stratified sample (25 buckets, seed 20260614, excludes 99 cal100 obs) |
| 15:16 | Push to repo fails first attempt (base64 too large for argv); succeeds via stdin payloads → commit `d2f6abb7` on main |
| 15:18 | Pete: `git pull origin main` — divergent branches; Computer offers merge vs hard-reset paths |
| 15:20 | Pete: stuck in `vi` editor; Computer provides `Esc :q! Enter` escape |
| 15:23 | Pete: "screwing up due to lack of firm direction" — Computer pivots to firm prescriptive direction |
| 15:23 | Driver foreground run: loaded 5,000 obs, applied filters (642 not-applicable, 3,829 already-scored), 4 pre-filter writes, started 4,354 API calls; Pete Ctrl-C'd during first call |
| 15:24 | Background `nohup` launch — PID 73051 |
| 15:29 | Pete: "write decisions and log" |

## Driver state at launch

- Input: `Perplexity_Only/prescience_tier_a_sample_v1.csv` (5,000 obs)
- After --skip-not-applicable: 4,358 candidates
- Already-scored/preseed/prefiltered in baseline: 3,829
- Pre-filter (R1–R4) writes: 4
- API calls pending: 4,354
- Expected wall: ~12.5 hours @ 8.66s/obs avg

## Costs

- Total API spend since June 1: $3.00 (pre-Tier A)
- Projected Tier A worst-case: 4,354 × $0.03 = $130
- Realistic: $50–100
- Credit ceiling: 200,000 (well under)

## Lessons captured

1. **Premature execution**: Pete ran the driver before Computer built the sample. Computer should have either built proactively when Pete confirmed "yes, build 5,000" the first time, or been clearer that build+push was required before driver invocation.
2. **Firm direction wins**: Pete explicitly requested firmer prescriptive direction. Background `nohup` block + monitoring commands worked. Apply going forward: when launching long-running ops, give exact copy-paste blocks, not optional alternatives.
3. **Divergent branch trap**: Pete's Mac had local commits ahead of origin. Default pull behavior in git ≥2.30 refuses to merge without explicit `--no-rebase` / `--rebase` / `--ff-only` flag. Note for future Mac runbooks: prefer `git pull --no-rebase` to avoid the prompt.
4. **vi escape gotcha**: Pete ended up in vi after `git pull` (likely auto-launched for merge commit message). Document `Esc :q! Enter` in DAILY_INGEST_RUNBOOK.

## Files staged this session (workspace)

- `/home/user/workspace/prescience_tier_a_sample_v1.csv` — 5,000 obs, 2.7 MB (pushed to repo)
- `/home/user/workspace/decisions_log_entry_2026_06_14_tier_a_launch_v1.md`
- `/home/user/workspace/log_entry_2026_06_14_tier_a_launch_v1.md`

## Next actions

- Pete monitors PID 73051 (optional) via `tail -f ~/Desktop/Archive/logs/tier_a_run.log`
- Tomorrow morning: Pete reports row count and tail of log → Computer runs `prescience_acceptance_gates_v1.py --gates tier_a`
- If gates pass: promote to master via `promote_pass_c_to_master_v1.py`
- EOD batch commit still pending (WORKLIST edits, /tmp/worklist_append.txt content, stashed _master_studies.csv changes, delete decision for scripts/roll_up_prescience_v3.py)

## Open commitments

- Decisions entry committed to `Archive/decisions/`
- Log entry committed to `Archive/logs/`
- Both will land via tomorrow morning's batch commit alongside Tier A results
