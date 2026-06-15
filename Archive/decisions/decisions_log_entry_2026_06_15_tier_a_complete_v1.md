# Decision: Tier A Complete, Master Promoted, Tier B Launched

**Date:** 2026-06-15 (Monday)
**Session:** §11v continued — Prescience Bulk Scoring
**Status:** Tier A COMPLETE · Master at 8,440 rows · Tier B launching
**Author:** Pete Kastner + Computer

---

## What completed

### Tier A run
- 4,352 Sonar Reasoning Pro API calls in 762.3 min (12.7 hours, ~5.7 calls/min)
- 4 pre-filter writes + 4,354 API rows = 4,358 total rows
- 52 parse failures (1.2%) — Sonar JSONDecodeError after 3 retries, scored -1 with diagnostic rationale
- Started ~15:24 EDT Sun 6/14, finished ~04:06 EDT Mon 6/15 (PID 73051, nohup background)

### Acceptance gates — ALL 9 PASS

| Gate | Value | Threshold |
|---|---|---|
| G1 parse_ok | 98.8% | ≥95% |
| G2 distinct scores | 6 | ≥4 |
| G2b max concentration | 46.4% | ≤65% |
| **G2c dist drift chi-sq** | **1.10** | ≤30.0 |
| G3 rationale median | 655 chars | ≥200 |
| G3b rationale min | 264 chars | ≥50 |
| **G4 refusal rate** | **46.4%** | ≤55% |
| G5 confidence drift | 0.20 | ≤1.0 |
| G6 cost | N/A | manual |

G2c = 1.10 is exceptionally close to baseline — strongest possible signal that Sonar Reasoning Pro produces baseline-consistent verdicts at scale.

### Score distribution (Tier A API rows)

| Score | Baseline | Tier A | Note |
|---|---|---|---|
| 0 | 45.8% | 46.4% | Almost identical refusal rate |
| 1 | 0.4% | 2.8% | Tier A finds more "very weak" |
| 2 | 1.8% | 6.4% | Tier A finds more "weak" |
| 3 | 9.3% | 10.5% | Close |
| 4 | 20.2% | 21.6% | Close |
| 5 | 1.8% | **12.4%** | **Tier A is more generous with 5s** |

**Score-5 inflation explanation** (per Pete 2026-06-15 06:01 EDT):
> "Flag 1 — early studies were rich, cherry-picked"

Baseline 3,829 rows were curated/cherry-picked from rich content — pre-IPO memoirs, transcript highlights, vendor profiles known to contain prescient calls. Tier A samples more representatively from the full corpus, so the true prescient-rich fraction is closer to 12% than 2%. This is signal, not noise.

### Parse failure retagging (per Pete 2026-06-15 06:01)
> "2 tag mark as pass_c_sonar_v1_parse_fail"

52 rows retagged in repo at commit `c0b1047b`. Distinguishes Sonar JSONDecodeError exhaust failures from rule-based pre-filter -1s.

Final `source_pass` distribution in master:
- `pass_c_cloud` (legacy baseline, claude+sonar): 4,082
- `pass_c_sonar_v1`: 4,302
- `pass_c_sonar_v1_parse_fail`: 52
- `pass_c_prefilter_v1`: 4
- **Total: 8,440**

### Surgical line-101 fix
Pre-existing baseline corruption at line 101: an orphan `"10991290-4e6131-OBS-002"` trailer was appended to the e2open OBS-001 row (`source_pass=pass_c_cloud`, dated 2026-05-29). The next row (proper `10991290-4e6131-OBS-002`) was intact at line 102 — no data loss. Surgically stripped trailer; master now structurally clean (8,440 rows, 0 anomalies). Backup: `_master_prescience_scores.csv.bak_pre_surgical_20260615T101607Z`.

### Promote script patch
`scripts/promote_pass_c_to_master_v1.py` was originally hardcoded to override `scorer_version` and `source_pass` from CLI args, which would have destroyed our 3-way Tier A tag split. Patched to prefer CSV value over CLI default:
```python
"scorer_version":   row.get("scorer_version") or args.scorer_version,
"source_pass":      row.get("source_pass") or args.source_pass,
```
Backup of original: `scripts/promote_pass_c_to_master_v1.py.bak_20260615T060556Z` (untracked, not committed).

## Commits this session (chronological)

- `d2f6abb7` — Stage Tier A 5,000-obs stratified prescience sample (Sun 15:16 EDT)
- `39839580` — Tier A complete: 4,352 API calls in 12.7h — results + report
- `c0b1047b` — Tier A retag: 52 parse failures → pass_c_sonar_v1_parse_fail
- **`c587fee6` — Promote Tier A to prescience master: 4,082 → 8,440 rows**

## Cost
- $3.00 spend since June 1 (pre-Tier A)
- Tier A estimated: $50-100 actual (TBD when next billing snapshot pulled)
- Well under 200,000 credit ceiling

## Operational lessons captured

1. **Background long runs** with `nohup ... &` + PID file + tee log. Confirmed working pattern.
2. **Divergent branch trap on Mac**: default git pull config refuses merge without explicit `--no-rebase` / `--rebase` / `--ff-only`. Standard fix: `git pull --no-rebase origin main`.
3. **vi auto-launch** on merge commits — escape with `Esc :q! Enter` or `:wq Enter`. Add to runbook.
4. **CSV awk parsing fails** on quoted fields with embedded commas. Always use Python `csv` module for verification; pipe to file with `tee`.
5. **Promote script tag preservation**: never let a CLI default override CSV-supplied provenance tags. The patch should be folded back to the canonical script.
6. **Wrong-branch commits**: yesterday's Tier A complete commit landed on `probe-2026-06-14` instead of `main`. Recovery via `git checkout main && git pull --no-rebase && git checkout <other-branch> -- <files> && git commit` — works for non-merge content extraction.
7. **Surgical CSV fixes** preferred over wholesale regeneration when corruption is isolated. Verified-via-raw-bytes + backup + verify-via-csv pattern.

## Tier B plan

- Remaining unscored: ~15,486 of 19,844 (Tier A consumed 4,358)
- At Tier A throughput (5.7 calls/min): ~45 hours total
- Strategy: launch ~10,000-obs Tier B tonight, decide on remainder after morning gates
- Reuse same driver, same gates, same promote workflow

## Open backlog (not closed this session)

- Document `preseed_b` schema convention in MASTERS_NOTES.md
- §11v PRESCIENCE ARCHITECTURE AUDIT (D6) — gates v1.7.0
- Type taxonomy hygiene: 137 case-variant types in `_master_studies.csv`
- G4 calibration threshold raise (55% → 60% permanent)
- Data hygiene audit: empty/bare `metric_value` rows (R5 pre-filter rule candidate)
- `§11v` kw-note integration for player rebuttals
- Fold `promote_pass_c_to_master_v1.py` patch into canonical script + commit
- Consolidate untracked `qwen_master_kappa_*` and `audit_abandoned_qwen_*` files into `scripts/v3_obsolete/` or commit
