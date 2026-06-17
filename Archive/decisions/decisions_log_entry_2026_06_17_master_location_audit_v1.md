# Master Location Audit — Pre-Tier-B-Promote
**Date:** 2026-06-17
**Session:** §11v continuation (Tier B promote prep)
**Trigger:** Two `_master_prescience_scores.csv` files at identical size (6,606,996 bytes) — needed canonical determination before promote.

## Audit Findings

### SHA comparison across all masters (archive_masters/ vs repo root)

| File | archive_masters/ | repo root | Status |
|---|---|---|---|
| `_master_codes.csv` | 1780f7af | 1780f7af | SAME |
| `_master_entities.csv` | 059545cc | 059545cc | SAME |
| `_master_entity_field_conflicts.csv` | b8a8e833 | b8a8e833 | SAME |
| `_master_entity_studies.csv` | 79cb9e54 | 79cb9e54 | SAME |
| `_master_observations.csv` | **9427887d** | **83f97b38** | **DIFFER** |
| `_master_prescience_scores.csv` | 72098b36 | 72098b36 | SAME |
| `_master_studies.csv` | **2c381222** | **4976305f** | **DIFFER** |
| `_master_tech_studies.csv` | 41d945ec | 41d945ec | SAME |
| `_master_technologies.csv` | f3a388a2 | f3a388a2 | SAME |

archive_masters/-only (no repo equivalent — working files):
- `_master_entity_canonicalization_TODO.csv`
- `_master_tech_canonicalization_TODO.csv`
- `_master_tech_field_conflicts.csv`
- `_master_studies.csv.bak_pre_passC_dectp_20260613T151325Z.csv`

No repo-only masters.

### Script references to `archive_masters`

- `scripts/quarantine_pass_c_run_v1.sh` — quarantines `archive_masters/_master_prescience_scores.csv`
- `scripts/reconcile_masters_mac_to_repo_v2.py` — ships 5 masters from `~/Desktop/Archive/archive_masters/` → repo (Mac→repo direction confirmed)
- `scripts/apply_year_observed_v2.py` — writes backup to `archive_masters_pre_year_observed_apply_<ts>/`

## Decision

**`~/Desktop/Archive/archive_masters/` is the canonical Mac-side working/write target.**
- Scripts (including `promote_pass_c_to_master_v1.py`) write here.
- `.bak` history lives here.
- `reconcile_masters_mac_to_repo_v2.py` is the one-way sync Mac→repo.

**`~/Desktop/Archive/aberdeen-group-archive/_master_*.csv` is the canonical synced mirror.**
- Repo root per `kastner-archive-pipeline` skill v1.7 Gotcha 12.
- Updated by reconcile script after batch operations.
- This is what gets committed/pushed to GitHub.

## Observed Divergences Explained

Two masters DIFFER between locations:

1. **`_master_observations.csv`** — Repo has the SH extension (31 cols, post-`sh_extend` from yesterday). archive_masters/ is the pre-SH state from Jun 12. This is because the SH extend was applied to the repo working copy directly; archive_masters/ has not been re-reconciled since.

2. **`_master_studies.csv`** — Similar pattern. Repo has newer edits not yet reflected in archive_masters/.

**Implication:** archive_masters/ is *behind* repo for these two files. Before any operation that reads from archive_masters/ for these tables, must reconcile FROM repo back TO archive_masters/ (reverse direction of normal flow), OR operate directly on the repo copy.

For Tier B prescience promote specifically: the two prescience_scores.csv files are byte-identical (`72098b36...`), so the promote script can safely write to archive_masters/ and then reconcile forward to repo.

## Tier B Promote Path Forward

1. Stage Tier B CSV at script's hardcoded input: `cp ~/Desktop/Archive/pass_c_v6_tier_b_results.csv ~/Desktop/Archive/prescience_scores_pass_c_cloud_v1.csv`
2. Run `promote_pass_c_to_master_v1.py --dry-run` (writes to archive_masters/_master_prescience_scores.csv preview)
3. Inspect dry-run output (8,645 candidate rows, expect all new obs_ids — no overlap with existing 19,815 rows since Tier B was filtered to exclude already-scored)
4. **Pete preauth gate (D3)** for `--commit` since this is a production master move
5. Run `--commit` → archive_masters/_master_prescience_scores.csv grows by ~8,645 rows
6. SHA-check archive_masters/ post-promote
7. Reconcile to repo: copy archive_masters/_master_prescience_scores.csv → aberdeen-group-archive/_master_prescience_scores.csv
8. Commit to repo with provenance message
9. Then resume divergence reconciliation for observations + studies (separate track)

## Action Items Logged

- [ ] Tier B promote (above 9 steps)
- [ ] **Separately**: reconcile observations + studies divergences (repo→archive_masters/ for these two files, or rerun forward sync after next major archive_masters/ edit)
- [ ] Update `kastner-archive-pipeline` skill: clarify that archive_masters/ is the Mac-side write target and repo is the synced mirror, with reconcile_masters_mac_to_repo_v2.py as the bridge

## Status

**RESOLVED.** archive_masters/ is canonical write target; repo root is canonical synced mirror. Safe to proceed with Tier B promote.
