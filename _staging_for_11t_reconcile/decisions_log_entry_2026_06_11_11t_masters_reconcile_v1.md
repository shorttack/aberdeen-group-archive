## §11t Mac↔repo masters reconcile (2026-06-11 PM EDT)

**Date:** 2026-06-11 (Thursday) PM EDT
**Trigger:** During DECtp Pass B observation extraction (option 4 from new-day menu), an mtime check on `~/Desktop/Archive/archive_masters/` showed most masters dated 2026-05-24 — much earlier than work documented in late May / early June. Pete raised the concern: "I am very concerned we have multiple sets of CSV files that are getting out of sync."
**Outcome:** DECtp Pass B halted. Five-master reconcile Mac→repo executed as one atomic commit with pre-reconcile backup tree preserved by Git Data API blob-sha reference.

### Discovery and diagnostic chain

Three read-only audit passes built the picture, each shipped to the repo before running on Mac per the script-delivery protocol:

1. **Cheat-sheet recovery.** Located `decisions/canonical_layout_decision_v1.md` confirming `~/Desktop/Archive/archive_masters/` as canonical source of truth (STATUS QUO).

2. **`audit_mac_vs_repo_v1.py`** (repo commit `71ed3165`). Read-only row/col/sha256 comparison of 8 master + known CSVs. Results:

   | File | Mac | Repo | Status |
   |---|---|---|---|
   | `_master_studies.csv` | 1,435r × 16c | 1,435r × 16c | IN_SYNC (today's DECtp study row) |
   | `_master_observations.csv` | 23,605r × 17c | 19,773r × 15c | BOTH_DELTA |
   | `_master_entities.csv` | 3,207r × 8c | 9,510r × 9c | BOTH_DELTA |
   | `_master_technologies.csv` | 4,312r × 8c | 7,854r × 9c | BOTH_DELTA |
   | `_master_codes.csv` | 1,293r × 4c | 23,991r × 4c | ROW_DELTA |
   | `_master_entity_field_conflicts.csv` | 3,711r × 5c | (absent) | MISSING_REPO |
   | `_known_entities.csv` | 3,300r × 9c | 3,298r × 9c | ROW_DELTA (negligible) |
   | `_known_technologies.csv` | 4,371r × 9c | 4,388r × 9c | ROW_DELTA (negligible) |

   Audit CSV output: `~/Desktop/Archive/_audit_mac_vs_repo_20260612T005318Z.csv`.

3. **Repo git log on contested masters** (via `gh api /repos/.../commits?path=...`). All four contested masters last touched between 2026-05-21 (`11670e87` — "Add DEC longitudinal archival study") and 2026-05-26 (`0d48d9a8` — "Catalina" handle, added computational-chemistry). **All repo writes pre-date the v20 obs_id Universal Normalizer run on 2026-05-24 14:16 EDT** documented in MASTERS_NOTES.md and `archival-ingest` v20 §20.5.

4. **`audit_schema_and_overlap_v1.py`** (repo commit `187be686`). Read-only schema-column-name diff + key-set overlap on the three contested non-observations masters:

   **Schema diff (decisive):**
   - `_master_entities.csv`: repo has `study_id` column that Mac lacks → repo is **one-row-per-(entity_id, study_id)** denormalized form; Mac is **normalized one-row-per-entity_id**.
   - `_master_technologies.csv`: same pattern. Repo has `study_id`.
   - `_master_codes.csv`: same 4 columns on both sides; difference is row-count only.

   **Key overlap:**
   | File | Mac unique keys | Repo unique keys | In both | Mac-only | Repo-only |
   |---|---|---|---|---|---|
   | entities | 3,207 | 3,298 | 3,180 | 27 | 118 |
   | technologies | 4,312 | 4,389 | 4,304 | 8 | 85 |
   | codes | 1,293 | 1,338 | 1,115 | 178 | 223 |

   **Sample interpretation:**
   - Mac-only entities (`digex`, `digital-island`, `ent-avaya-001`, `ent-dr-003`, `ent-dyf-001`) are post-May-21 broadband/ISP additions + the post-cleanup canonical `ent-*-NNN` ID pattern.
   - Repo-only entities (`3COM`, `ABERDEEN-GROUP`, `AMERICAN-SOFTWARE`, `ATT-GIS`, `CRAY-RESEARCH`) are uppercase pre-cleanup IDs that exist on the Mac in lowercase form — products of the documented May 24 case-merge cleanup (`Archive_legacy_2026_May/archive_masters_pre_case_merge_backup/` is the smoking gun).
   - Repo-only codes (` MRO)`, ` old email)`, ` scalability improvements`) are broken codes with leading whitespace — Mac cleanup removed these.
   - Shared sample rows confirm content equivalence on the common columns; the repo's only added information per row is the `study_id` cell.

   Overlap JSON output: `~/Desktop/Archive/_audit_schema_overlap_20260612T005802Z.json`.

### Decision: Mac is canonical on all 5 drifted files

Justification:

1. **Single-writer invariant.** Pete confirmed (2026-06-11 21:06 EDT) iPad has no GitHub/Archive access; Computer runs only on the Desktop Mac. Therefore the only path for the repo to have post-Mac state is implausible — no merge concern.

2. **Documented v20 reference state.** Mac `_master_observations.csv` at 23,605 × 17 with the post-v20 verification_method distribution (ingest-extraction: 21,427 / web-source: 1,193 / outcome-linkage: 860 / unverified: 79 / placeholder: 16 / cross-reference: 30) matches `archival-ingest` v20 §20.5 exactly. The repo at 19,773 × 15 is the documented pre-v20 reference state per §17.5.

3. **Documented case-merge backup.** `Archive_legacy_2026_May/archive_masters_pre_case_merge_backup/` proves the uppercase→lowercase entity_id cleanup was a deliberate Mac-side operation. The 118 repo-only uppercase entity_ids are aliases of existing lowercase Mac entities, not new data.

4. **Pete confirmation on codes.** "We rebuilt/extended codes at some point" — explains the 23,991 → 1,293 collapse + 178 new codes.

5. **Schema simplification is correct.** Phase 1+2 pipeline (`01_load_csvs_v2.py`) reconstructs entity↔study linkage from `_master_observations.csv` which has both `entity_id` and `study_id` per row. The `study_id` column on `_master_entities.csv` / `_master_technologies.csv` is redundant; dropping it in the May 24 cleanup was correct.

Pete confirmed reconcile path: "I think you propose a reasonable path forward."

### Per-file reconcile plan executed

All five files ship Mac → repo. The repo's pre-reconcile blobs are preserved inside the same atomic commit at `archive_masters_pre_reconcile_<UTCstamp>Z/` via Git Data API tree entries that point at the existing blob shas (no re-upload needed).

| Repo path | Operation | New blob source | Pre-reconcile blob preserved at |
|---|---|---|---|
| `_master_observations.csv` | UPDATE (overwrite) | Mac `~/Desktop/Archive/archive_masters/_master_observations.csv` (23,605×17) | `archive_masters_pre_reconcile_<UTCstamp>Z/_master_observations.csv` |
| `_master_entities.csv` | UPDATE (overwrite) | Mac (3,207×8 normalized) | `archive_masters_pre_reconcile_<UTCstamp>Z/_master_entities.csv` |
| `_master_technologies.csv` | UPDATE (overwrite) | Mac (4,312×8 normalized) | `archive_masters_pre_reconcile_<UTCstamp>Z/_master_technologies.csv` |
| `_master_codes.csv` | UPDATE (overwrite) | Mac (1,293×4 rebuilt) | `archive_masters_pre_reconcile_<UTCstamp>Z/_master_codes.csv` |
| `_master_entity_field_conflicts.csv` | CREATE | Mac (3,711×5 diagnostic) | n/a (Mac-only artifact, no pre-state to preserve) |

**Not touched in this reconcile:**
- `_master_studies.csv` — already IN_SYNC.
- `_known_entities.csv` (Mac +2 rows) and `_known_technologies.csv` (repo +17 rows) — cache files with negligible drift, deferred to a separate look. The slight repo-ahead on `_known_technologies.csv` is mildly surprising under the single-writer invariant but is small enough that it could reflect intra-session cache churn between Phase 1 runs.

### Rollback paths (recorded for the record, per Pete 2026-06-11 21:06 EDT)

Three independent rollback layers exist:

1. **GitHub history.** Each reconciled file's pre-reconcile blob sha is captured in the audit JSON (`_audit_schema_overlap_20260612T005802Z.json`) and in this commit's backup tree. The repo's pre-reconcile state lived on `origin/main` at commit `187be686`. To revert: `git revert <reconcile-commit-sha>` or restore from backup tree paths.
2. **TimeMachine.** Pete has at least two TimeMachine backups predating tonight's reconcile.
3. **Mac local files.** This reconcile is push-only Mac→repo. Mac `archive_masters/` is untouched.

### Files committed in this atomic batch

12 file changes, one commit:

1. `_master_observations.csv` (overwrite, ~8.5 MB after schema expansion)
2. `_master_entities.csv` (overwrite)
3. `_master_technologies.csv` (overwrite)
4. `_master_codes.csv` (overwrite)
5. `_master_entity_field_conflicts.csv` (create)
6. `archive_masters_pre_reconcile_<UTCstamp>Z/_master_observations.csv` (create, refs repo's pre-reconcile blob)
7. `archive_masters_pre_reconcile_<UTCstamp>Z/_master_entities.csv` (create, refs repo's pre-reconcile blob)
8. `archive_masters_pre_reconcile_<UTCstamp>Z/_master_technologies.csv` (create, refs repo's pre-reconcile blob)
9. `archive_masters_pre_reconcile_<UTCstamp>Z/_master_codes.csv` (create, refs repo's pre-reconcile blob)
10. `archive_masters_pre_reconcile_<UTCstamp>Z/_README.md` (create, documents what's in the backup tree + rollback instructions)
11. `WORKLIST.md` (refresh — adds §11t entry to Done this session + updates Last updated header)
12. `_decisions_log.md` (append this entry)

### Phase 1+2 rebuild status

**NOT run as part of this reconcile.** The reconcile is repo-side only. Mac `archive_masters/` is unchanged, so `~/Desktop/kastner_wiki/` (live wiki DuckDB) is unaffected. The next time Phase 1+2 runs from Mac it will read the same Mac masters it has been reading all along; no rebuild is triggered by this push.

**Deferred to next session:**
- DECtp Pass B observation extraction (option 4 from new-day menu, halted to perform this reconcile).
- DECtp ingest script (`ingest_dectp_observations_v1.py`) needs upgrade from the 15-col schema it was drafted against to the 17-col canonical schema before any use. Add `section` (from chart label tag in source MD) + `legacy_obs_id` (empty for greenfield rows).

### Lessons codified

- The repo's mtime alone is not a sufficient drift signal — the repo can be silently behind for weeks if a downstream pipeline (Phase 1+2 on Mac) reads only Mac-side files. **Run `audit_mac_vs_repo_v1.py` at session start whenever any masters-touching work is planned.** Schedule as a recurring sanity check.
- Schema-column drift is more dangerous than row-count drift. The 8c vs 9c on entities/technologies would have caused `01_load_csvs_v2.py` to fail-or-misread silently if the repo's denormalized form had ever been pulled to Mac. The single-writer invariant has been protecting us.
- The "extra column on repo" pattern is the canonical signature of the May 24 namespace cleanup. If we ever see it again on a different table, this is the lookup pattern to apply.

### Rebuild + ship preview (next session)

When DECtp Pass B resumes:
1. Upgrade `ingest_dectp_observations_v1.py` to 17-col schema.
2. Dry-run on Mac against the now-reconciled state.
3. Apply with `--commit` (adds 26 new observations).
4. Phase 1+2 rebuild on Mac.
5. Phase 3-6 if downstream wiki/embeddings need refresh per Workflow C decision tree.
6. EOD commit ships updated masters + the regenerated wiki content if Phase 3-6 ran.

### Artifacts created during this session

- `/home/user/workspace/audit_mac_vs_repo_v1.py` (repo `scripts/`, commit `71ed3165`)
- `/home/user/workspace/audit_schema_and_overlap_v1.py` (repo `scripts/`, commit `187be686`)
- `/home/user/workspace/canonical_layout_decision_v1.md` (cheat-sheet recovery, already in `decisions/`)
- `/home/user/workspace/ingest_dectp_observations_v1.py` (workspace only, **NEEDS 17-col upgrade before use** — not shipped)
- `/home/user/workspace/dectp_observations_delta_v1.csv` (workspace only, **invalidated by schema upgrade requirement** — not shipped)
- `/home/user/workspace/decisions_log_entry_2026_06_11_11t_masters_reconcile_v1.md` (this entry, ships in this commit)
- `/home/user/workspace/reconcile_masters_mac_to_repo_v1.py` (ships in repo `scripts/` as part of this commit)

### Mac-side audit outputs (not committed; reproducible from scripts)

- `~/Desktop/Archive/_audit_mac_vs_repo_20260612T005318Z.csv`
- `~/Desktop/Archive/_audit_schema_overlap_20260612T005802Z.json`

---
