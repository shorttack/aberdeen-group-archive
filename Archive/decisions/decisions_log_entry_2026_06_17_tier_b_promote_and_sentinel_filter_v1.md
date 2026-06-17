# Decisions Log — 2026-06-17 — Tier B Promote + Phase 1 v3 Sentinel Filter
**Session:** §11v continuation 6
**Status:** Tier B promoted, archive rebuilt, wiki regen running

## Context

Yesterday closed with Tier B Pass C complete (8,645 rows, 33.9h run). Today's three-step plan:
1. Review Tier B
2. Push to archive
3. Generate wikis

All three steps executed, plus an unplanned but critical Phase 1 patch.

## Decision 1: Tier B prefilter sentinel handling

**Context:** Tier B output contains 56 rows with `prescience_score=-1` and `source_pass=pass_c_prefilter_v1`. These are figure captions / picture-text OCR dumps that the prefilter rejected before sending to Sonar — NOT API refusals.

**Decision (Option A from yesterday):** Stay as `-1`. The `source_pass` column carries the semantic — `pass_c_prefilter_v1` vs `pass_c_sonar_v1` vs `pass_c_sonar_v1_parse_fail` disambiguates the reason.

**Sentinel taxonomy now locked across all passes:**

| Value | Meaning | Pass |
|---|---|---|
| 0-5 | Valid score | normal |
| -1 | parse_fail (SH) OR prefilter_excluded (Tier B) | `source_pass` disambiguates |
| -2 | pending (reserved, unused) | — |
| -99 | content_unrecoverable (Sonar refusal, post-hoc reclass) | SH only |

## Decision 2: Master location canonical — archive_masters/ writes, repo root mirrors

**Trigger:** Two `_master_prescience_scores.csv` files at identical size (6,606,996 bytes) before Tier B promote — needed canonical determination.

**SHA audit findings:**

| Master | archive_masters/ | repo root | Status |
|---|---|---|---|
| `_master_codes.csv` | SAME | SAME | aligned |
| `_master_entities.csv` | SAME | SAME | aligned |
| `_master_entity_field_conflicts.csv` | SAME | SAME | aligned |
| `_master_entity_studies.csv` | SAME | SAME | aligned |
| **`_master_observations.csv`** | **9427887d** | **83f97b38** | **DIFFER** (repo has SH extension) |
| `_master_prescience_scores.csv` | SAME | SAME | aligned (pre-promote) |
| **`_master_studies.csv`** | **2c381222** | **4976305f** | **DIFFER** (repo newer) |
| `_master_tech_studies.csv` | SAME | SAME | aligned |
| `_master_technologies.csv` | SAME | SAME | aligned |

**Decision:** `archive_masters/` is the canonical write target (scripts write here; `.bak` history lives here). Repo root is the canonical synced mirror (committed to GitHub; what `reconcile_masters_mac_to_repo_v2.py` produces).

The two DIFFER cases (`_master_observations.csv`, `_master_studies.csv`) represent recent repo-side edits (SH extend) that haven't been reconciled back to `archive_masters/`. Separate reconcile track logged as backlog.

**Full audit:** `Archive/decisions/decisions_log_entry_2026_06_17_master_location_audit_v1.md` (commit `b2c45f39`).

## Decision 3: Tier B promote (D3 preauth granted)

**Dry-run:** 8,645 candidate rows / 8,440 existing / 0 dupe collisions / 0 missing study_id. Top study_ids: memoir chapters (vol 1 ch10, ch04, ch05), SOA, longitudinals — consistent with the unscored backlog.

**Pre-promote SHA** (both locations identical): `72098b36db4718723e28c944e79e01c16d2d257efe888f924990953af6f9a2b9`

**Promote command:**
```
python3 scripts/promote_pass_c_to_master_v1.py \
  --commit \
  --scorer-version pass_c_v6_cloud_pplx_sonar \
  --source-pass pass_c_v6_tier_b
```

**Result:**
- 8,645 rows appended
- Backup: `archive_masters/_master_prescience_scores.csv.bak_pre_promote_20260617T101531Z`
- Post-promote SHA: `0840e327309312a13a2869c7ecf28411a1f142f5c564d5f9c296403fe21f842f`
- Row count: 17,087 (header + 17,086 data)

**Reconcile to repo:** `cp archive_masters/_master_prescience_scores.csv aberdeen-group-archive/_master_prescience_scores.csv` — both locations now SHA `0840e327...`.

**Repo commit:** `a1661603` (push bypassed PR/signature rules per admin override; normal for this archive).

## Decision 4: Phase 1 v3 — sentinel filter at ingest (the unplanned but critical patch)

**Trigger:** Before kicking off wiki regen, Pete asked: "Are the build scripts changed to reflect the new prescience columns?"

**Investigation:** `01_load_csvs_v2.py` does `pd.to_numeric(..., errors="coerce")` on `prescience_score`. The sentinel values `-1` and `-99` are valid numbers and would pass through, then corrupt:
- `prescience_mean` (line 209): dragged down by negative values
- `prescience_obs_count` (line 210): inflated (counts sentinels as scored)
- `v_observations_with_prescience` view (Phase 2): would include sentinel rows
- Per-obs page tables (Phase 3): would show literal `-1` / `-99` in markdown

**Sentinel count in master at audit time:** **908 rows with score < 0** (much higher than expected ~72; included 784 historical `pass_c_cloud` -1 rows from pre-§11v passes, 64 from SH parse-fail + sonar-v1 origins, 12 from `pass_c_cloud_parse_fail`, 8 from Tier B `pass_c_prefilter_v1`).

**Decision (after considering scoping options):** Drop ALL `prescience_score < 0` rows at Phase 1 ingest, regardless of provenance. Single chokepoint. Master CSV retains all rows for audit (source_pass + scorer_version preserve the reason); only the wiki views are filtered.

**Implementation:** `01_load_csvs_v3.py`. Filter added immediately after master read, before any joins/aggregations. Reports filtered count to stdout and to `build_manifest.json` (`prescience_rows_filtered_as_sentinels`).

**Repo commit:** `27a2f9d7` (sandbox → repo via gh API tree-commit pattern).

**No Phase 2 patch needed** — study-level views read sentinel-clean parquets from Phase 1. Obs-level `v_observations_with_prescience` view's `IS NOT NULL` filter is now sentinel-clean because the parquet itself has no negative scores.

## Outcomes — shape audit

**Before Phase 1 v3 + Phase 2 rebuild** (pre-Tier-B baseline):
- studies: 1,452
- observations: 23,926
- high_prescience studies: 126
- obs_with_prescience: 3,829

**After:**
- studies: 1,452 (unchanged)
- observations: 23,926 (unchanged)
- high_prescience studies: **865** (+739)
- obs_with_prescience: **15,924** (+12,095)

**Phase 1 v3 stdout (final lines):**
```
sentinel filter — dropped 908 prescience rows with score < 0; 16177/17085 retained
derived pub_year — 1452/1452 resolved; 0 missing
joined prescience to observations — 15924/23926 obs scored
rolled up obs prescience to studies — 1108/1452 studies have ≥1 scored obs
```

## Decision 5 — DEFERRED: prescience "high study" definition

**Open question raised:** `v_studies_with_high_prescience` uses `prescience_max >= 4` (any single obs scored 4+ flips the study to "high"). With Tier B, 865/1,452 (60%) of studies now qualify — feels high.

Sanity breakdown:
```
pmax_ge_4   : 865    (any obs 4+)
pmax_5      : 614    (any obs 5)
pmean_ge_35 : 115    (study average 3.5+)
scored      : 1108   (any scored obs)
```

The strict-mean definition (115) is close to the prior baseline of 125. The any-max definition (865) is what surged with Tier B.

**Decision deferred:** Keep current `prescience_max >= 4` filter for now (Phase 3-6 regen uses it). Open a separate decision in a future session on whether to:
- Tighten to `prescience_mean >= 3.5`
- Add a parallel `v_studies_with_mean_high_prescience` view
- Re-document the existing definition with the Tier B context

**Backlog item:** Prescience "high study" definitional review post-Tier-B.

## What ran today (commits, in order)

1. `092bf65b` — Tier B prefilter sentinel decision doc (yesterday's EOD work pulled in this session)
2. `a1661603` — `_master_prescience_scores.csv` Tier B promote (+8,645 rows, 8,440→17,085 data)
3. `b2c45f39` — master location audit decision
4. `27a2f9d7` — `01_load_csvs_v3.py` sentinel filter at ingest

## In progress at EOD

Phases 3-6 running unattended under `caffeinate -dim`:
- Phase 3: ~3h tier-1 LLM regen (1,452 studies)
- Phase 4: <30s indices
- Phase 5: ~14-15 min embeddings (bge-m3, 1024-dim)
- Phase 6: <30s scaffolding (README, AGENTS.md, chat-starter.md)

Final shape audit + `kw ask` verification + EOD commit batch pending phase completion.

## Backlog (newly opened or pending)

- Prescience "high study" definitional review (Decision 5 above)
- Reconcile `_master_observations.csv` and `_master_studies.csv` divergence (archive_masters/ behind repo)
- Findings doc commit (`study_findings_prescience_decline_aberdeen_eras_v1.md`) — pending Pete sign-off
- Driver v9: bake -99 sentinel natively
- Methodology code normalization pass (492 codes)
- 16-obs archive-hygiene pass (use SH refusal manifest)
- archival-ingest skill v21 — register `archive-meta` 7th collection
- §11v PRESCIENCE ARCHITECTURE AUDIT (D6) — gates v1.7.0 release
- T2 / Kastner-accuracy study (separate future)
- `_master_player_rebuttals.csv` move-to-root (D3 preauth required)
- F1/F8/F10 audit items
- Tier C/D planning
- `kastner-archive-pipeline` skill v1.8 — record the sentinel-at-ingest pattern as Gotcha 13
