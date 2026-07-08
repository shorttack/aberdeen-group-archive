
---

## 2026-07-07 -- Master-CSV cleanse + full SH pipeline rebuild (overnight, completed 2026-07-08 04:15 UTC)

**Session:** solo agent (Perplexity Computer) + Pete on Mac. Cleanse phases A/B/C committed at 18:54:29Z; pipeline Phases 1+2+audit landed at 18:54:32Z; Phase 3 was interrupted at ~21:00 UTC by a power failure; resumed via `overnight_v3_resume.sh` at 21:31:22Z and completed all Phases 3-6 at 04:15:51 UTC on 2026-07-08.

### Shape audit -- BEFORE (pre-cleanse, 2026-07-07T18:54:29Z)

```
studies  observations  entities  technologies  studies_with_pub_year  decades  high_prescience
1504     24842         3293      4376          1504                   6        876
```

### Shape audit -- MID (post-cleanse + post-Phase-1+2, 2026-07-07T18:54:32Z)

```
studies  observations  entities  technologies  studies_with_pub_year  decades  high_prescience
1504     24842         3288      4368          1504                   6        876
```

Delta: entities -5 (SAP alias merge), technologies -8 (tech mislabel merges). studies + observations + high_prescience unchanged as expected.

### Shape audit -- AFTER (post-Phase-3-through-6, 2026-07-08T04:15:51Z)

```
studies  observations  entities  technologies  studies_with_pub_year  decades  high_prescience  sh_scores  sh_verdicts
1504     24842         3288      4368          1504                   6        876              17030      792
```

DuckDB shape is stable across MID and AFTER (as expected -- Phases 3-6 don't touch masters or DuckDB shape). SH data is live: `v_prescience_sh = 17030` observation-level scores, `v_studies_with_sh_verdicts = 792` studies with 3y/5y verdicts.

### Phase A -- Tech mislabel repair

Applied 8 MERGE_INTO rows via `apply_tech_mislabel_v1.py --commit`. Backups: `_master_technologies.csv.bak_phase_a_tech_mislabel_20260707T185429Z` + `_master_tech_studies.csv.bak_phase_a_tech_mislabel_20260707T185429Z`. Audit: `tech_mislabel_apply_v1_applied_20260707T185429Z.txt`.

Merges committed:
- `data-mining` -> `service-oriented-architecture`
- `microsoft-backoffice` -> `numa-architecture`
- `sun-ultrasparc` -> `enterprise-information-integration`
- `audio-conferencing` -> `oltp`
- `webex-training-center` -> `ms-cluster-server`
- `titanium` -> `itanium`
- `t2-04` -> `numa-architecture`
- `tech-01` -> `rolap`

Row deltas: `_master_technologies.csv` 4376 -> 4368 (delta -8); `_master_tech_studies.csv` 5389 -> 5389 (43 rewrites, 0 dedups).

### Phase B -- Entity metadata bleed fix

Applied 10 rows via `apply_entity_metadata_v1.py --commit`. Backup: `_master_entities.csv.bak_phase_b_entity_metadata_20260707T185429Z`. Audit: `entity_metadata_apply_v1_applied_20260707T185429Z.txt`. Row count unchanged (3293), 23 field-level changes.

Fixes committed:
- `informix-software`: successor Siemens-Nixdorf -> IBM (2001, $1B); status [DEFERRED] -> acquired; entity_type -> software-vendor; sector -> Database software.
- `microsoft`: successor "HP Inc. / Hewlett Packard Enterprise" -> null; status restructured -> active.
- `microsoft-corporation`: successor "Oracle Corporation (1995)" -> null; status acquired -> active.
- `intel`: successor "Compaq (1998) then HP (2002)" -> null; status operating -> active.
- `intel-corporation`: successor [DEFERRED] -> null.
- `sybase`: entity_type marketing-services -> software-vendor; successor "Compaq/HP/HPE-NonStop" -> SAP AG (2010, $5.8B); status dissolved -> acquired.
- `yahoo`: successor "HP Inc. / HPE (2015 split)" -> Verizon Media (2017) then Apollo Global Management (2021).
- `stratus-technologies`: successor "Compaq (1998) then HP (2002)" -> null; status normalized.
- `oracle-corporation`: successor "Accrue Software then JDA Software" -> null; status acquired -> active; entity_type "Enterprise Customer" -> software-vendor.
- `ENT-S3-001`: sector "Computing Hardware / IT Services" -> Software; status Acquired -> Active; successor "Compaq (1998); HP (2002)" -> null.

### Phase C-narrow -- SAP cluster merge

Applied via `apply_entity_aliases_v1_sap.py --commit`. Backups: `_master_entities.csv.bak_phase_c_sap_alias_20260707T185429Z` + `_master_entity_studies.csv.bak_phase_c_sap_alias_20260707T185429Z`. Audit: `entity_aliases_sap_apply_v1_applied_20260707T185429Z.txt`.

Survivor: `sap-ag` (per CANONICAL_IDS.md). Merged in: `sap`, `ENT-SAP`, `ENT-SAP-001`, `ENT-BO-002`, `ENT-IRP-003`. Kept separate: `sap-america`, `sap-america-utilities`, `paul-wahl-sap`. Notes concat delimiter `\n---\n` per Pete's Q4 (2026-07-07 AM).

Row deltas: `_master_entities.csv` 3293 -> 3288 (delta -5); `_master_entity_studies.csv` 3900 -> 3900 (19 rewrites, 0 dedups).

### Phase 0 audit -- ALL PROBES PASS

`07_audit_masters_v1.py` report at `logs/wiki_rebuild_20260707T185429Z/07_audit_report.md`:

- **Probe 1 (alias-collision ratio)**: entities 0.8822 -> 0.8829 (+0.0007, improvement); tech 0.9250 -> 0.9265 (+0.0015, improvement). Both moved above baseline.
- **Probe 2 (tech ID-vs-name congruence)**: 1577 grandfathered -> 1569 current; **0 NEW violators**; 8 cleared from grandfather set (all Phase A merges detected).
- **Probe 3 (successor-bleed)**: 4 grandfathered -> **0 current**; **0 NEW bleeders**; all 4 originals cleared (`ENT-S3-001`, `intel`, `stratus-technologies`, `sybase`).

Result: `PASS: no alerts or failures`. The regression harness is working as designed.

### Pipeline rebuild -- SH chain (canonical for v2.0 + this session)

- Phase 1 (`01_load_csvs_v3.py`, SH-aware): loaded 12 masters incl. `_master_prescience_short_horizon.csv` (17030 rows). Wrote `short_horizon.parquet` alongside the other 12 parquets. Completed in ~2 sec.
- Phase 2 (`02_build_data_layer_v5.py`, adds SH views): 32 views total; 5 new SH views (`v_prescience_sh`, `v_observations_with_sh`, `v_studies_with_sh_verdicts`, `v_sh_3y_distribution`, `v_sh_5y_distribution`). Completed in ~1 sec.
- Phase 3 (`03_generate_vault_v3.py`, SH-aware page rendering): originally interrupted by power failure at ~21:00 UTC; resumed and completed via `overnight_v3_resume.sh`. ~6.5h tier-1 LLM regeneration via `qwen3.5:27b-mlx`. All 1504 study pages carry `prescience_3y_enum` frontmatter; 792 gradeable studies carry a "Short-horizon prescience" body section (matches `v_studies_with_sh_verdicts` exactly).
- Phase 4 (`04_generate_indices_v6.py`): index, decade, collection, prescient, codes pages + 5 Bases files. ~1 sec.
- Phase 5 (`05_compute_embeddings_v3.py`, bge-m3 1024-dim): 10862 pages re-embedded in ~18 min. Live index at `data/embeddings.parquet`.
- Phase 6 (`06_emit_scaffolding_v2.py`, SH-aware README): README + AGENTS.md + chat-starter.md + Makefile + .gitignore + verify.py + semantic_search.py. `.gitignore` unchanged from prior state (no Gotcha 8 regression).

### Post-completion verification

- **Idempotency check** (in `overnight_v3_resume.sh`): confirmed 0 Phase A aliases remaining in `v_technologies`, 0 Phase C SAP aliases remaining in `v_entities`. Informix successor now `IBM (2001, $1B)`; Microsoft successor now `NULL`; SAP-AG successor now `SAP SE (2014 rebranding)`.
- **Wiki study pages**: 1504 pages with `prescience_3y_enum` frontmatter (100%); 792 with "Short-horizon prescience" body section (matches `v_studies_with_sh_verdicts` exactly).
- **`kw ask` sanity check**: `kw_ask.py` currently crashes with `ModuleNotFoundError: No module named 'duckdb'` when invoked from Pete's non-login shell (`/Users/scott/bin/kw`). Not a data issue; the Python environment `kw` uses lost its duckdb dependency at some point. Backlog item added for repair; does not block EOD commit.
- **Notes-dir pre-commit check**: `kw pending` reports `wiki/notes/ is clean` -- no uncommitted notes to fold in.

### Interruption + resume timeline

- 14:54 EDT (18:54Z): `overnight_v2.sh` started. Phases A/B/C committed by 14:54:29 EDT. Phases 1+2+0 audit finished by 14:54:32 EDT. Phase 3 started.
- ~17:00 EDT (21:00Z): power failure. Phase 3 was mid-run.
- 17:26 EDT (21:26Z): Pete restarted `overnight_v2.sh`. Failed at Phase A DRYRUN with "row count Δ=0, expected -8" -- misleading error because the cleanse was already applied.
- 17:31 EDT (21:31Z): Pete ran `overnight_v3_resume.sh` (new script that skips A/B/C and starts from Phase 3, with an idempotency check). All Phases 3-6 completed cleanly at 00:15 EDT / 04:15Z.

### Deferred to next session

- Fix `kw_ask.py` Python environment (duckdb import path); this session's shape audits used the raw duckdb CLI so the data was verified, but `kw ask` retrieval is currently non-functional.
- Add idempotency detection to `apply_*_v1.py` scripts so re-running a completed cleanse fails with a clear "already applied, nothing to do" message instead of the current "unexpected row-count delta" error. Ship as `apply_*_v2.py` per the versioning invariant.
- Patch `kastner-archive-pipeline` skill v1.7 -> v1.8: correct the "Three Locations" table (archive_masters/ was retired 2026-06-24; the canonical masters path is now `~/Desktop/Archive/aberdeen-group-archive/`), document candidates-CSV runtime location (alongside masters at repo root), document the SH pipeline chain vs the pre-SH chain and when to use each.
- Phase D (full tech alias sweep, ~130 clusters, ~328 aliases), Phase C-broad (full entity alias sweep, ~150 clusters, ~388 aliases), Phase E (`[DEFERRED]`/`[REVIEW]` -> `Deferred Review` sentinel migration on 281 entity rows).

### Log locations (for reference)

- Original run (Phase A/B/C + Phase 1+2 + audit + interrupted Phase 3): `~/Desktop/Archive/logs/wiki_rebuild_20260707T185429Z/`
- Resume run (Phase 3 restart through Phase 6): `~/Desktop/Archive/logs/wiki_rebuild_resume_20260707T213122Z/`
- Status file: `~/Desktop/Archive/logs/OVERNIGHT_STATUS_20260707T213122Z.OK`
