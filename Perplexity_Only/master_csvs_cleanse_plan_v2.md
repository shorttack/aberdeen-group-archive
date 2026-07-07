# Kastner Archive — Master CSVs Cleanse Plan v2

**Author:** Perplexity Computer (assistant)
**Date drafted:** 2026-07-07 (v1 authored AM; v2 revised after Q&A + `CANONICAL_IDS.md` discovery)
**Supersedes:** `master_csvs_cleanse_plan_v1.md` (workspace only; not committed)
**Target repo:** `shorttack/aberdeen-group-archive`
**Masters live at:** repo root (`_master_*.csv`) per §11v cont 5 — NOT under `archive_masters/`. Mac mirror: `~/Desktop/Archive/archive_masters/` (both paths point at the same file set per today's `bash` verification).
**Live DuckDB probed:** `~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb`
**Session tie-in:** `WORKLIST_2026_07_07.md` (workspace + mirror); this plan is the source of truth for the sequence; the WORKLIST tracks completion.

---

## 0. Locked decisions from Pete (2026-07-07 AM)

| # | Question | Decision |
|---|---|---|
| Q1 | Canonical-slug convention | **Honor `Perplexity_Only/CANONICAL_IDS.md` as-is.** Fully-qualified form wins where already documented (`microsoft-corporation`, `oracle-corporation`, `sap-ag`, `sybase-inc`, `hewlett-packard`, `silicon-graphics`, `informix-software`, `tandem-computers`, `compaq-computer`, `apple-computer`, `sun-microsystems`, `peter-s-kastner`). Short form only where already short (`ibm`, `dec`, `aol`, `idc`, `ups`, `ent-att`, `ent-vantive`, `aberdeen-group`). No doc rewrites. |
| Q2 | SAP handling | `sap-ag` is the survivor. `entity_name = "SAP AG"`. `successor = "SAP SE (2014 rebranding)"`. All ENT-* placeholders + the bare `sap` row collapse in. `sap-america` and `sap-america-utilities` STAY as separate rows (subsidiaries). |
| Q3 | Study-scoped IDs (`eNN-NN`, `tNN-NN`, `enc-03`, `ENT-XXX-NNN`, `TECH-XXX-NNN`) | **Merge into canonical.** Not first-class entities. Join tables re-point during merge. Exception: rows whose `entity_name` genuinely disagrees with any canonical row get promoted to a proper canonical slug in the same pass. |
| Q4 | `notes` concat delimiter | `\n---\n` (approved). **KW Notes render script must be patched** so rendered wiki pages translate this delimiter into a visible separator rather than an inadvertent `<hr>` inside a paragraph. Patch queued as backlog item. |
| Q5 | Sentinel for unresolved rows | Plain string `Deferred Review` (no brackets). Also translate existing `[DEFERRED]` and `[REVIEW]` sentinels during Phase E. |
| Q6 | Phase F (regression harness) timing | **Build NOW, before Phase A.** Renamed to **Phase 0**. Wired into `scripts/build/07_audit_masters_v1.py` and shell-called at end of Phase 2 (`02_build_data_layer_v5.py`). |
| Q7 | Session shape | Start with `kastner-new-day` WORKLIST. Phases 3-6 (Workflow C) deferred overnight. |
| Q8 (post-CANONICAL_IDS discovery) | Overnight scope | **Full Workflow C (Phases 3+4+5+6).** ~3.5 h. README shape reflects the merge. |
| Q9 (post-CANONICAL_IDS discovery) | SAP alias resolution | Merge `sap-ag` + all `ENT-SAP*` + `ENT-BO-002` + `ENT-IRP-003` + bare `sap` → survivor `sap-ag`. Keep `sap-america` and `sap-america-utilities` separate. Expected row-count Δ on `_master_entities.csv` = **−6**. |
| Q10 (post-CANONICAL_IDS discovery) | Phase 0 script placement | **`scripts/build/07_audit_masters_v1.py`; runs at end of Phase 2 as part of the pipeline contract.** |

---

## 1. Findings that motivate this plan (unchanged from v1)

Evidence from 2026-07-07 AM read-only DuckDB probes.

### 1.1 Alias / duplicate-ID collisions (the SAP-study blocker)

- **Entities:** 3,293 rows → 2,905 distinct normalized names ⇒ **~388 duplicate identities.**
- **Technologies:** 4,376 rows → 4,048 distinct normalized names ⇒ **~328 duplicate identities.**
- Top offenders (entities): Oracle 13 IDs · IBM (short) 12 IDs · Microsoft 11 IDs · SAP 8 IDs · DEC 7 IDs · HP 7 IDs · Sybase 6 · Novell 6 · Compaq 6 · Intel 5 · EMC 5 · AMD 5.

### 1.2 Metadata bleed on `_master_entities.csv` — "Compaq → HP" successor fanout

Not the paraphrased "Microsoft → Siemens Nixdorf" — the literal Siemens-Nixdorf misattribution is on **Informix**. But the same class of bug hits Microsoft, Intel, Sybase, and Yahoo with **"Compaq (…) then HP (…)"** successor strings that belong on DEC-family studies.

Confirmed rows requiring fix:

| entity_id | occ | Wrong field(s) | Correct value |
|---|---:|---|---|
| `informix-software` | 7 | `successor = "Siemens-Nixdorf"` | `successor = "IBM (2001)"`; `status = "acquired"` |
| `microsoft` | 116 | `successor = "HP Inc. / Hewlett Packard Enterprise"`; `status = "restructured"` | `status = "active"`; `successor = null` |
| `microsoft-corporation` | 17 | `status = "acquired"`; `successor = "Oracle Corporation (1995)"` | `status = "active"`; `successor = null` |
| `intel` | 50 | `successor = "Compaq (1998) then HP (2002)"` | `status = "active"`; `successor = null` |
| `sybase` | 15 | `entity_type = "marketing-services"`; `successor = "Compaq (1997); then HP (2002); ..."` | `entity_type = "software-vendor"`; `successor = "SAP AG (2010, $5.8B)"` |
| `yahoo` | 3 | `successor = "HP Inc. / HPE (2015 split)"` | `successor = "Verizon Media (2017) → Apollo Global Mgmt (2021)"` |

Cheap detection probe (used by both Phase 0 harness and Phase B candidate generator):

```sql
SELECT entity_id, entity_name, successor
FROM v_entities
WHERE successor ILIKE '%Compaq%' AND successor ILIKE '%HP%'
  AND entity_name NOT ILIKE '%DEC%'
  AND entity_name NOT ILIKE '%Digital Equipment%'
  AND entity_name NOT ILIKE '%Compaq%'
  AND entity_name NOT ILIKE '%Tandem%'
  AND entity_name NOT ILIKE '%HP%'
  AND entity_name NOT ILIKE '%Hewlett%'
  AND entity_name NOT ILIKE '%EDS%'
  AND entity_name NOT ILIKE '%3Com%'
  AND entity_name NOT ILIKE '%Palm%'
  AND entity_name NOT ILIKE '%Cray%'
ORDER BY occurrence_count DESC;
```

### 1.3 Mislabeled tech rows (`tech_id` disagrees with `tech_name`)

Confirmed via read-only query. All 8 shown; more will appear when the congruence probe runs against the full 4,376-row set.

| tech_id | tech_name (stored) | Correct disposition |
|---|---|---|
| `data-mining` | Service-Oriented Architecture (SOA) | Row is really an SOA row; canonical SOA slug is `service-oriented-architecture` — this row DELETES; a real `data-mining` row exists elsewhere |
| `microsoft-backoffice` | NUMA (Non-Uniform Memory Access) | RENAME to `numa` |
| `sun-ultrasparc` | Enterprise Information Integration (EII) | RENAME to `enterprise-information-integration` |
| `audio-conferencing` | Online Transaction Processing (OLTP) | Row is really OLTP; DELETE (a real `oltp` row exists per `CANONICAL_IDS.md`) |
| `webex-training-center` | Microsoft Cluster Server (MSCS/Wolfpack) | RENAME to `ms-cluster-server` (canonical) |
| `titanium` | Intel Itanium 64-bit processor | RENAME to `itanium` |
| `t2-04` | NUMA | RENAME to `numa` (study-scoped ID collapse) |
| `tech-01` | Relational OLAP (ROLAP) | RENAME to `rolap` (study-scoped ID collapse) |

### 1.4 Placeholder-ID families still present

- `ENT-XXX-NNN` / `TECH-XXX-NNN` — Pass B ingest placeholders (largest collision source)
- `eNN-NN` / `tNN-NN` — 75 entity, 117 tech study-scoped IDs
- `MICROSOFT-SQL`, `enc-03` — case-inconsistent Pass B carryover

### 1.5 `[DEFERRED]` / `[REVIEW]` legacy sentinels

**281 entity rows** carry these strings in `status` or `successor`. Migrated to `Deferred Review` in Phase E.

---

## 2. Non-negotiables (unchanged from v1)

1. Masters at repo root are truth; parquets and DuckDB are derived.
2. Dry-run first; `--commit` opt-in on every script.
3. Timestamped `.bak` per script per master; `csv.QUOTE_ALL` on write.
4. Versioned scripts (`_v1..vN`); never overwrite.
5. Pete reviews candidates CSV before any merge writes.
6. Shape audit before + after every rebuild, into `_decisions_log.md`.
7. Workflow C mandatory when entity/tech merges reshape the archive.
8. Never rewrite an obs_id or a study_id.
9. `v_studies.type` (not `collection_type`); `v_studies.study_prescience_enum` (not `prescience`).
10. **NEW (Q4)**: All merges preserving `notes` use `\n---\n` as concat delimiter. KW Notes renderer must be patched to translate this to a visible separator before it can render inside a paragraph as `<hr>`.
11. **NEW (Q5)**: Any unresolved metadata cell uses `Deferred Review` as sentinel (no brackets).
12. **NEW (Q10)**: `scripts/build/07_audit_masters_v1.py` runs at end of Phase 2. Baseline captured on the pre-Phase-A archive. Alert thresholds fail loudly if a future ingest regresses.

---

## 3. Phased execution (session order, revised)

### Phase 0 — Regression harness (BUILT TODAY, BEFORE PHASES A/B/C)

**Script:** `scripts/build/07_audit_masters_v1.py`
**Runs:** at end of `02_build_data_layer_v5.py`, or manually
**Exit code:** 0 = pass, 1 = warn (regression), 2 = fail (hard threshold)
**Baseline:** captured today into `Perplexity_Only/audit_masters_baseline.json`

Three probes:

1. **Alias-collision ratio floor**
   - Metric: `distinct_norm_names / total_rows` for `v_entities` and `v_technologies`
   - Baseline captured *before* today's cleanse (worst case) so first Phase-A/B/C run shows an improvement, not a regression
   - Threshold: alert if ratio drops >0.02 from baseline in either view
2. **ID-vs-name congruence** (tech only; entity IDs are noisy by design)
   - Row-level: for each row, compute `norm_id = lower(re.sub('[^A-Za-z0-9]','',tech_id))` and `norm_name = lower(re.sub('[^A-Za-z0-9]','',tech_name))`. Flag row if neither is a substring of the other.
   - Baseline: current mislabels are grandfathered in an allow-list (`Perplexity_Only/audit_masters_baseline.json` field `tech_congruence_grandfathered`). Alert only on NEW mislabels.
3. **Successor-bleed detector**
   - Rule: `entity_name` doesn't match {DEC, Digital Equipment, Compaq, Tandem, HP, Hewlett, EDS, 3Com, Palm, Cray} AND `successor` contains BOTH "Compaq" AND "HP"
   - Baseline: current bleeds grandfathered by `entity_id` in `entity_successor_bleed_grandfathered`. Alert only on NEW ones.

**Deliverable this session:** shipped script + baseline JSON. Wired into Phase 2 by adding a subprocess call at the tail of `02_build_data_layer_v5.py`.

### Phase A — Tech mislabel repair

**Candidates file:** `tech_mislabel_candidates_v1.csv`
Columns: `tech_id, tech_name, category, vendor, occurrence_count, disposition, proposed_new_tech_id, proposed_new_tech_name, source_rule, confidence, review_notes`
Dispositions: `RENAME_ID` (change tech_id, keep row) · `DELETE_ROW` (row is dupe of another; canonical row exists elsewhere) · `NO_ACTION` (row is a false positive) · `Deferred Review`

**Apply script:** `apply_tech_mislabel_v1.py`
Writes: `_master_technologies.csv` (rename or drop rows) + `_master_tech_studies.csv` (re-point tech_id from alias → canonical, dedupe on `(tech_id, study_id)`)
Row-count assertion: printed before/after, DELETE_ROWs explicit in output.

### Phase B — Entity metadata bleed fix

**Candidates file:** `entity_metadata_candidates_v1.csv`
Columns: `entity_id, entity_name, current_entity_type, current_sector, current_status, current_successor, proposed_entity_type, proposed_sector, proposed_status, proposed_successor, source_rule, confidence, review_notes`

Three source rules:
- `compaq_hp_successor_bleed` (§1.2 probe)
- `siemens_bleed` (`successor ILIKE '%Siemens%'` AND name not in Siemens family)
- `known_active_marked_dead` (short curated list of majors that must be `status='active'`, `successor=null`)

**Apply script:** `apply_entity_metadata_v1.py`
Writes: `_master_entities.csv` ONLY. Row count MUST be unchanged (hard assert). Only the 4 fields (`entity_type, sector, status, successor`) can change per row.

### Phase C-narrow — SAP cluster only

**Alias map:** `entity_alias_map_v1_sap_only.csv`
Columns: `alias_entity_id, canonical_entity_id, canonical_entity_name, canonical_successor, disposition, confidence, review_notes`

SAP-family rows (from live query today):

| alias_entity_id | occ | disposition |
|---|---:|---|
| `sap-ag` | 27 | **CANONICAL SURVIVOR** (row keeps this ID) |
| `sap` | 17 | MERGE_INTO `sap-ag` |
| `ENT-SAP` | 1 | MERGE_INTO `sap-ag` |
| `ENT-BO-002` | 1 | MERGE_INTO `sap-ag` |
| `ENT-IRP-003` | 0 | MERGE_INTO `sap-ag` |
| `ENT-SAP-001` | 0 | MERGE_INTO `sap-ag` |
| `sap-america` | 3 | **KEEP** (subsidiary) |
| `sap-america-utilities` | 0 | **KEEP** (utilities-vertical subsidiary) |
| `paul-wahl-sap` | 0 | **KEEP** (person entity, not the company) |

**Apply script:** `apply_entity_aliases_v1_sap.py`
Writes: `_master_entities.csv` (Δ = −5 rows: 6 aliases merged into `sap-ag` = 5 deletions) + `_master_entity_studies.csv` (re-point + dedupe)

Post-merge survivor fields:
- `entity_id = "sap-ag"`
- `entity_name = "SAP AG"`
- `entity_type = "corporation"`
- `sector = "enterprise-resource-planning"`
- `status = "active (renamed SAP SE)"`
- `successor = "SAP SE (2014 rebranding)"`
- `years_active` = merged from highest-occ non-null (`sap-ag` if non-null, else fall back)
- `notes` = concat of all non-null alias notes with `\n---\n` delimiter

Row-count expectations printed by apply script:
- `_master_entities.csv`: 3293 → 3288 (Δ −5)
- `_master_entity_studies.csv`: 3900 → 3900 − (dedup delta). Every study that has both `sap` and `sap-ag` in the join table becomes one row. Empirically ~10 studies mention both, so expect ~3890.

### Phase D — Full tech alias sweep (DEFERRED, next session)

Same pattern as C but ~130 clusters, ~328 aliases. Not in scope today.

### Phase C-broad — Full entity alias sweep (DEFERRED, next session)

Same pattern as C-narrow but ~150 clusters, ~388 aliases. Not in scope today.

### Phase E — `[DEFERRED]` → `Deferred Review` migration (DEFERRED, next session)

281 rows. Not in scope today.

### Phase F (was Phase 0 in v1; now built as Phase 0 in the pipeline) — DONE this session.

---

## 4. Session sequence (2026-07-07)

1. **Update plan v2** (this doc) ✓
2. **Build Phase 0 harness + baseline JSON** — `07_audit_masters_v1.py` in workspace, shipped via `gh api PUT` to `scripts/build/`
3. **Build Phase A candidates + apply script** — dry-run-ready
4. **Build Phase B candidates + apply script** — dry-run-ready
5. **Build Phase C-narrow SAP alias map + apply script** — dry-run-ready
6. **Update WORKLIST_2026_07_07.md** with completed items + Mac-side runbook
7. **EOD commit** — one batch per repo per `kastner-github` skill
8. **Overnight (Pete on Mac)** — full Workflow C: Phase 1 → Phase 2 (audit) → Phase 3 → Phase 4 → Phase 5 → Phase 6 with `caffeinate` + `tee`

## 5. Mac-side runbook (what Pete runs after `git pull`)

```bash
cd ~/Desktop/Archive/aberdeen-group-archive
git pull

# Copy scripts to their runtime locations
cp scripts/build/07_audit_masters_v1.py     ~/Desktop/Archive/scripts/build/
cp scripts/apply_tech_mislabel_v1.py        ~/Desktop/Archive/scripts/
cp scripts/apply_entity_metadata_v1.py      ~/Desktop/Archive/scripts/
cp scripts/apply_entity_aliases_v1_sap.py   ~/Desktop/Archive/scripts/
cp Perplexity_Only/audit_masters_baseline.json  ~/Desktop/Archive/Perplexity_Only/

# Copy candidates CSVs (source of truth for the edits)
cp tech_mislabel_candidates_v1.csv          ~/Desktop/Archive/
cp entity_metadata_candidates_v1.csv        ~/Desktop/Archive/
cp entity_alias_map_v1_sap_only.csv         ~/Desktop/Archive/

# Shape audit BEFORE
duckdb ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb -c "
SELECT
  (SELECT COUNT(*) FROM v_studies) AS studies,
  (SELECT COUNT(*) FROM v_observations) AS observations,
  (SELECT COUNT(*) FROM v_entities) AS entities,
  (SELECT COUNT(*) FROM v_technologies) AS technologies,
  (SELECT COUNT(*) FROM v_studies_with_high_prescience) AS high_prescience;
"

# Phase A dry-run then --commit
cd ~/Desktop/Archive
python3 scripts/apply_tech_mislabel_v1.py
# ...review output...
python3 scripts/apply_tech_mislabel_v1.py --commit

# Phase B dry-run then --commit
python3 scripts/apply_entity_metadata_v1.py
python3 scripts/apply_entity_metadata_v1.py --commit

# Phase C-narrow (SAP) dry-run then --commit
python3 scripts/apply_entity_aliases_v1_sap.py
python3 scripts/apply_entity_aliases_v1_sap.py --commit

# Phase 1+2 rebuild (this triggers Phase 0 audit at the tail)
python3 scripts/build/01_load_csvs_v3.py --archive ~/Desktop/Archive/archive_masters --wiki ~/Repos/kastner-aberdeen-wiki
python3 scripts/build/02_build_data_layer_v5.py --wiki ~/Repos/kastner-aberdeen-wiki
# Phase 0 audit runs at the end of Phase 2; expect no NEW alerts (existing bleeds are grandfathered).

# Shape audit AFTER (paste both into _decisions_log.md)
duckdb ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb -c "..." # same query as above

# Overnight Workflow C
caffeinate -i bash -c '
  set -e
  python3 scripts/build/03_generate_vault_v3.py --wiki ~/Repos/kastner-aberdeen-wiki 2>&1 | tee logs/phase3_20260707.log
  python3 scripts/build/04_generate_indices_v6.py --wiki ~/Repos/kastner-aberdeen-wiki 2>&1 | tee logs/phase4_20260707.log
  python3 scripts/build/05_compute_embeddings_v3.py --wiki ~/Repos/kastner-aberdeen-wiki 2>&1 | tee logs/phase5_20260707.log
  python3 scripts/build/06_emit_scaffolding_v2.py --wiki ~/Repos/kastner-aberdeen-wiki 2>&1 | tee logs/phase6_20260707.log
'
```

## 6. Not in scope today (bookkeeping)

- Phase D / Phase C-broad / Phase E — deferred to next session
- `CANONICAL_IDS.md` backfill for new canonical slugs discovered this session — deferred
- KW Notes render patch for `\n---\n` delimiter — deferred, WORKLIST backlog item added
- `wiki/_redirects.md` for the SAP aliases — small enough to fold into the overnight batch (Pete decides; script emits redirect suggestions)
