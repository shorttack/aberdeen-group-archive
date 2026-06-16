# §11v Phase 0 — Calibration GREEN + ≤2015 Sweep Launched

**Date**: 2026-06-16 AM
**Session**: §11v Phase 0 calibration kickoff
**Status**: Calibration COMPLETE / GREEN-LIGHT; full ≤2015 sweep LAUNCHED, ETA ~5:30 PM ET

## Sequence (06:32 → 07:32 ET)

### 1. New-day setup
- Fetched canonical `WORKLIST.md` from `origin/main`, mirrored to `WORKLIST_2026_06_16.md`.
- Carry-forward: 105 open items preserved across 9 sections; +1 new "§11v Phase 0 CALIBRATION RUN" item added to Next up.

### 2. Calibration sample built
- `build_sh_calibration_sample_v1.py` → `Perplexity_Only/sh_calibration_sample_v1.csv`
- 100 obs, 20 buckets, seed 20260615
- 18,243 eligible (after 5,000 Tier A exclusions + 683 anchor>2020 drops); per-bucket distribution top-heavy on topic-viewpoint(11) / profile-case(7) / market-research(6) / other(6) / memoir(6)
- 0 Tier A/B overlap, all anchors ≤ 2020

### 3. Calibration driver run
- Dry-run: 100/100 classified `combined` (both 3y + 5y elapsed), 0 no_anchor
- Real run: **100 OK / 0 fail in 6.9 min, 14.4/min throughput, zero retries**
- Output: `Perplexity_Only/sh_calibration_results.csv`

### 4. G1-G10 gates
- **HARD fails: 0** — exit 0
- Soft flags: 1 (G8b model-vs-mechanical 76% — read as healthy signal given G9/G10 corroboration)
- Per-gate summary:
  - G1 schema PASS — 0 invariant violations
  - G2a/b/c distribution PASS on both windows (3y mean 2.63, 5y mean 2.64)
  - G3 monotonicity PASS — high-score rows show higher confidence
  - G4 rationale presence PASS — 100% / 100%
  - G5 accuracy DEFERRED — no human truth file
  - G6 source labeling PASS — 0 off-vocab
  - G7 pending PASS — 0% on both windows (expected from sample filter)
  - G8a divergence PASS — 24%
  - G8b model-vs-mechanical FLAG (soft) — 76%
  - G9 chronological monotonicity PASS — 91.7%
  - G10 trajectory plausibility PASS — 80 stable / 19 both-wrong / 1 late-vindication

### 5. Schema extension
- `_master_observations.csv` extended 17 → 31 cols
- Pre-extend SHA: `9427887d6710a6deae3a72d8e55f5152b3792982db92325585ec992341018b6d`
- Post-extend SHA: `83f97b38e49ca9e1b2738197ea3a1b63c1bae87b1ac4a07a3e9f72af43674bb6`
- Backup: `~/Desktop/Archive/archive_masters/_master_observations.csv.bak_pre_sh_extend_20260616T071946Z` (SHA matches pre-extend)
- Size: 9,925,499 → 10,930,621 bytes (+1,005,122 = 14 empty cols × 23,926 rows + commas/quotes)
- All invariants PASS: row count preserved, baseline column values byte-identical, all 14 SH cols empty

### 6. Sweep eligibility inventory
`count_eligible_le_2015_v1.py` (commit `409c86e9`):
- Total obs: 23,926
- Excluded Tier A+B: 15,000
- No anchor: 0 (study.date fallback caught all)
- Dropped anchor>2020: 229
- **Eligible anchor≤2020: 8,697**
- **Eligible anchor≤2018: 8,665**
- **Eligible anchor≤2015: 8,659  ← TARGET (chosen)**
- Anchor source mix within eligible pool: 73.7% `year_observed` / 26.3% `study_date` (resolver v2 fallback saved 2,288 obs)

### 7. Manifest build
- `Perplexity_Only/sh_sweep_le_2015_manifest_v1.csv` — 8,659 obs (header + body), 31 cols (carries empty SH cols from post-extend master)
- Dry-run against driver v8: 8,659 / 8,659 classified `combined`, 0 pathologies

### 8. Sweep launch
- PID **59349** launched 07:32 ET via nohup
- Background, `--resume` enabled
- Output: `Perplexity_Only/sh_sweep_le_2015_results.csv` (per-batch sidecar — NOT the master)
- Log: `~/Desktop/Archive/logs/sh_sweep_le_2015_run.log`
- ETA at 14.4/min: ~10 hours → ~17:30 ET tonight

## Cost trajectory

| Phase | Calls | Wall time | Est cost |
|---|---|---|---|
| Calibration | 100 | 6.9 min | <$5 |
| Sweep ≤2015 | 8,659 | ~10h | $340-430 |
| **Total Phase 0** | 8,759 | ~10h | $345-435 |

Ceiling raised to $500 mid-session (Pete approval at 07:29). Comfortable headroom.

## Decisions made

- **Calibration verdict: GREEN-LIGHT** — 0 HARD fails. G8b 76% read as healthy signal (Sonar beating naive mechanical baseline), corroborated by G9 91.7% and G10's 80% stable cluster.
- **Sweep cutoff: anchor ≤ 2015** — chosen over ≤2018 because the natural age distribution drops off after 2015 (only 6 obs gained between 2015 and 2018 cutoffs). 11-year minimum elapsed outcome window provides strongest defensible ground truth.
- **Cost ceiling: $500** — raised from $250-300 to accommodate full sweep without subsampling.
- **Concurrency: sequential** — driver v8 single-threaded matches the v7 hardening that survived Tier B's 5K+ calls. Don't change engines mid-production.
- **Both jobs concurrent on Sonar account** — Tier B PID 2163 + SH PID 59349 share the API quota. If throughput drops materially we can re-evaluate.

## Open / Next

- Monitor both runs via `check_tier_b_v1.sh` and `check_sh_sweep_v1.sh` (committed this session).
- After SH sweep completes: re-run `sh_gates_v2.py` on the full 8,659-row results to confirm distribution stays clean at scale.
- After both runs complete: design Path A vs Path B merge → which SH scores propagate into `_master_observations.csv`, which stay in the sidecar, and how the `windows_diverge` column resolves into the master prescience enum.
- §11v PRESCIENCE ARCHITECTURE AUDIT (D6) still gates v1.7.0 release. Phase 0 completion does not unblock it.

## Refs

- Spec: `Archive/decisions/decisions_log_entry_2026_06_15_short_horizon_prescience_v3.md`
- Yesterday's build log: `Archive/logs/log_entry_2026_06_15_phase0_followon_v1.md`
- Calibration gates report: `Perplexity_Only/sh_calibration_gates_report.md`
- Calibration JSON: `Perplexity_Only/sh_calibration_gates_report.json`
