# Pre-Pass-B Snapshot — 2026-06-12 17:25:45 UTC

Snapshot of the 6 master CSVs immediately before the Pass B v2 merge
(commit `2a151bed` and the masters commit that follows).

Files here are the **pre-merge state** — what the masters looked like
just before `apply_passb_transcripts_v2.py --commit` ran.

| file | source backup name | timestamp |
|---|---|---|
| `_master_studies.csv` | `.bak_passb_transcripts_replace_20260612T171813Z` | step 1 of apply script (17:18:13Z) |
| `_master_entities.csv` | `.bak_passb_v2_entities_20260612T172545Z` | step 2 (17:25:45Z) |
| `_master_technologies.csv` | `.bak_passb_v2_techs_20260612T172545Z` | step 2 (17:25:45Z) |
| `_master_observations.csv` | `.bak_passb_v2_observations_20260612T172545Z` | step 2 (17:25:45Z) |
| `_master_entity_studies.csv` | `.bak_passb_v2_entity_studies_20260612T172545Z` | step 2 (17:25:45Z) |
| `_master_tech_studies.csv` | `.bak_passb_v2_tech_studies_20260612T172545Z` | step 2 (17:25:45Z) |

The studies file has an earlier timestamp because the apply script
runs the studies REPLACE first (step 1), then the entity/tech/obs
APPENDs (step 2). All six backups together represent the complete
pre-merge state.

Restore procedure (if ever needed): copy each file from this directory
back to the parent directory, then re-run Phase 1+2 to rebuild the
data layer.
