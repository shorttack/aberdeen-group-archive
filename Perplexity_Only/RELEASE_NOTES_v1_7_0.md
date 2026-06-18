# Release Notes — v1.7.0

**Release date:** 2026-06-18 (pending Mac-side dry-run + commit confirmation)
**Theme:** Prescience-architecture cleanup — four-finding closure
**Status:** Doc reconciliation complete; Mac-side script runs pending

---

## Headline

The 2026-06-15 prescience-architecture audit identified **four ship-gate findings (F2, F3, F6, F7)** plus six should-fix items. v1.7.0 closes **all four ship-gate findings** in a single coordinated change set. The remaining six (F1, F4, F5, F8, F9, F10) are non-gating and will land in subsequent point releases.

This is a **schema-and-discipline release**, not a corpus release. No new studies were ingested. The corpus shape stays at v1.6.2: 1,453 studies / 23,926 observations / 3,276 entities / 4,361 technologies / 865 high-prescience studies.

What changes:
1. **`_master_prescience_scores.csv` grows from 11 → 12 columns** (new `row_class` discriminator)
2. **12 cloud parse-fails retagged** from `source_pass='pass_c_cloud'` to `source_pass='pass_c_cloud_parse_fail'`
3. **`promote_pass_c_to_master_v1.py` in repo** matches Mac active copy (§11v provenance-preservation patch)
4. **Short-horizon (SH) `source_pass` taxonomy locked in** for driver v8 (`pass_c_sh_3y`, `pass_c_sh_5y`, `pass_c_sh_parse_fail`)
5. **Preseed-skip SH treatment defined** (Pete's F7 Option A: score normally; parallel verdicts; informative disagreement with long-horizon is expected and useful)

---

## The four findings — what closed, why it matters

### F2 — `promote_pass_c_to_master_v1.py` in version control

**Symptom:** The script that promotes Pass C scorer output (File 1) into the study-attached master (File 2) lived only on Pete's Mac and in workspace drafts. The repo copy at `scripts/promote_pass_c_to_master_v1.py` was a **stale pre-patch version** (lines 151-152 had no provenance fallback). The Mac active copy at `~/Desktop/Archive/scripts/promote_pass_c_to_master_v1.py` had the §11v audit F2 patch (commit c587fee6, 2026-06-15 ~05:00 EDT), which preserves CSV-carried `scorer_version` and `source_pass` values (used by Tier A retag, parse-fail tagging, and row-class markers), falling back to CLI defaults only when the row is empty.

**Risk:** Re-running the repo copy would have silently overwritten Tier A retag provenance with `cloud_v1` / `C` CLI defaults, contaminating audit trails for the ~57 Tier A rows.

**Fix:** Committed Mac active copy (211 lines, F2 patch present) verbatim to repo. Repo and Mac now byte-aligned. Commit [`7935aec7`](https://github.com/shorttack/aberdeen-group-archive/commit/7935aec7b15200132c649e48e1f4632f133ae9c8).

**Diff vs. previous repo copy:** lines 151-152 (2 lines, hardcoded CLI defaults) → lines 151-156 (6 lines: 4-line provenance comment + 2 lines with `row.get(...) or args.<flag>` fallback).

### F3 — `model` column conflated ML model identity with row-class sentinel

**Symptom:** The `model` column in `_master_prescience_scores.csv` carried real model names (`claude-sonnet-4.6`, `sonar-reasoning-pro`) for scored rows but also carried the structural sentinel `preseed_skip_v1` for 253 preseed rows. Downstream consumers had to disambiguate by joining columns 3+4+9 (`model` + `prescience_score` + `source_pass`) — error-prone and easy to forget.

**Risk:** Misclassification under any future schema change. Future analyses asking "which model did we use" had to filter out the sentinel manually; future analyses asking "how many parse-fails" had to know that two different `source_pass` values both meant the same thing (F6 below).

**Fix:** Added 12th column **`row_class`** as the explicit structural discriminator. Enum:

| `row_class` | Expected n | Identification rule |
|---|---|---|
| `scored` | 8,119 | `prescience_score IN (0,1,2,3,4,5)` |
| `parse_fail` | 64 | `parse_ok='false'` (12 cloud + 52 sonar) |
| `prefilter_skip` | 4 | `source_pass='pass_c_prefilter_v1'` (sentinel -1) |
| `preseed_skip` | 253 | `model='preseed_skip_v1'`, score+conf empty |
| `no_anchor` | reserved | Driver v8 marker for unanchorable SH claims |
| `pending` | 0 today | New obs added but not yet scored |
| **Total** | **8,440** | |

**Migration script:** `scripts/add_row_class_to_prescience_scores_v1.py` (committed in [`5f945dd9`](https://github.com/shorttack/aberdeen-group-archive/commit/5f945dd97461dde813043ae3620b5b8fcfe648bd)). Dry-run default. **Hard-fails on UNKNOWN class or count drift** (sum of classes must equal row count). Backup convention: `.bak_add_row_class_<utc>Z`. `csv.QUOTE_ALL` on write.

**Forward compatibility:** Driver v8 writes `row_class` from day 1. Consumers should query `row_class` rather than disambiguating columns 3+4+9.

### F6 — Cloud parse-fails in-band vs. sonar parse-fails split

**Symptom:** Asymmetry in how parse failures were tagged. Sonar parse-fails got a dedicated `source_pass='pass_c_sonar_v1_parse_fail'` (52 rows). Cloud parse-fails stayed in-band with `source_pass='pass_c_cloud'` AND `parse_ok='false'` (12 rows). Queries asking "give me all parse-fails" had to know to OR-join two patterns.

**Risk:** Easy to miss the 12 cloud parse-fails in audit queries. The asymmetry would compound as more scorers were added.

**Fix:** Retag those 12 cloud rows: `source_pass` → `'pass_c_cloud_parse_fail'`. `parse_ok` unchanged (still `'false'`). After this, **all parse-fails are queryable as `source_pass LIKE '%_parse_fail'`** OR (better, post-F3) **`row_class='parse_fail'`**.

**Migration script:** `scripts/retag_cloud_parse_fails_v1.py` (committed in [`5f945dd9`](https://github.com/shorttack/aberdeen-group-archive/commit/5f945dd97461dde813043ae3620b5b8fcfe648bd)). Touches exactly 12 rows. **Must run AFTER F3** (so the row_class column is already present and the retag doesn't drift the classifier's expected counts mid-flight). Dry-run default; backup; QUOTE_ALL.

**Forward compatibility:** Driver v8 writes SH parse-fails to `source_pass='pass_c_sh_parse_fail'` from day 1. The asymmetry is fully closed.

### F7 — Preseed-skip rows undocumented in SH driver v8 spec

**Symptom:** The 253 preseed-skip rows (Pass B preseed: `model='preseed_skip_v1'`, score and confidence empty, `source_pass='preseed_b'`) had defined behavior for long-horizon scoring (skipped — they were authored upstream during Pass B). But the SH (3-year and 5-year short-horizon) driver v8 spec didn't say what to do with them. Three plausible options:

- **Option A:** Score them normally in SH. Long-horizon retains preseed; SH produces a parallel verdict. Informative disagreement with long-horizon is expected and useful (it surfaces score-vs-rebuttal divergence at the short-horizon scale).
- **Option B:** Skip them in SH too. Preserve preseed semantics across horizons.
- **Option C:** New row class for SH-only preseed.

**Pete's decision (2026-06-18): Option A.** Driver v8 scores preseed-skip rows normally in SH. Long-horizon preseed semantics unchanged.

**Migration:** No data migration — this is a driver v8 spec lock-in. v8 reads preseed-skip rows on its input list like any other obs and writes a fresh row with `source_pass='pass_c_sh_3y'` or `'pass_c_sh_5y'`.

**Rule A SH rollup spec** (canonical query):

```sql
SELECT study_id,
       AVG(CASE WHEN prescience_score >= 0 THEN prescience_score END) AS mean_sh
FROM read_csv_auto('~/Desktop/Archive/archive_masters/_master_prescience_scores.csv')
WHERE source_pass IN ('pass_c_sh_3y', 'pass_c_sh_5y')
  AND prescience_score >= 0
GROUP BY study_id;
-- Rule A thresholds: >= 3.5 high, >= 2.0 medium, else low; len(used)=0 -> not-applicable
```

**Doc artifact:** `Perplexity_Only/F7_preseed_skip_sh_treatment_decision_v1.md` (committed in [`5f945dd9`](https://github.com/shorttack/aberdeen-group-archive/commit/5f945dd97461dde813043ae3620b5b8fcfe648bd)).

---

## Documents updated

| Doc | Change |
|---|---|
| `Perplexity_Only/MASTERS_NOTES.md` | v2 → **v3.** New 12-column schema entry for `_master_prescience_scores.csv`; preseed_b note extended with row_class cross-reference; new SH conventions block. |
| `Perplexity_Only/PRESCIENCE_ARCHITECTURE.md` | v1 → **rev2.** §1.3 promote script status flipped to CLOSED `7935aec7`; §2.1 schema 11 → 12 cols + row-class table now shows all 6 classes modeled; §7 cleanup map updated with closure commits; rev2 changelog appended. |
| `Perplexity_Only/F7_preseed_skip_sh_treatment_decision_v1.md` | **New.** Decision doc with downstream query patterns and Rule A SH rollup spec. |

## Scripts added

| Script | Role |
|---|---|
| `scripts/add_row_class_to_prescience_scores_v1.py` | F3 backfill: classifier + add 12th column (251 lines) |
| `scripts/retag_cloud_parse_fails_v1.py` | F6 retag: exactly-12-row touch (154 lines) |
| `scripts/promote_pass_c_to_master_v1.py` | F2: Mac active copy promoted to repo (211 lines, replacing stale 207-line version) |

## Six should-fix items (NOT in v1.7.0)

These remain open and will land in subsequent point releases. None gate v1.7.0.

| # | Finding | Severity |
|---|---|---|
| F1 | Stray prescience artifacts at repo root (should move to subdirs) | Should-fix |
| F4 | `scorer_version` naming drift (`cloud_v1` vs `v6`) | Should-fix |
| F5 | 1,106 cloud rows have `elapsed_sec='0.0'` (no timing recorded) | Should-fix |
| F8 | `pass_c_prefilter_v1` source_pass not yet modeled in driver v8 spec | Should-fix |
| F9 | (see audit doc) | Should-fix |
| F10 | (see audit doc) | Should-fix |

Full findings list and rationale: `Archive/decisions/prescience_architecture_audit_v1.md` (2026-06-15).

---

## Pre-flight for the v1.7.0 cutover (Mac-side)

1. **`git pull`** the archive repo to receive the four commits (`7935aec7` + `5f945dd9`).
2. **Copy F3 + F6 scripts** to active scripts dir:
   ```
   cp aberdeen-group-archive/scripts/add_row_class_to_prescience_scores_v1.py ~/Desktop/Archive/scripts/
   cp aberdeen-group-archive/scripts/retag_cloud_parse_fails_v1.py ~/Desktop/Archive/scripts/
   ```
3. **F3 dry-run** (no flags, dry-run is default):
   ```
   python3 ~/Desktop/Archive/scripts/add_row_class_to_prescience_scores_v1.py
   ```
   Expected output: scored=8119, parse_fail=64, prefilter_skip=4, preseed_skip=253, total=8,440. UNKNOWN=0.
4. **Review F3 dry-run output, paste here.** If numbers drift, halt and investigate (the master may have been edited since the spec was set).
5. **F3 commit:**
   ```
   python3 ~/Desktop/Archive/scripts/add_row_class_to_prescience_scores_v1.py --commit
   ```
6. **F6 dry-run:**
   ```
   python3 ~/Desktop/Archive/scripts/retag_cloud_parse_fails_v1.py
   ```
   Expected: exactly 12 rows touched.
7. **F6 commit:**
   ```
   python3 ~/Desktop/Archive/scripts/retag_cloud_parse_fails_v1.py --commit
   ```
8. **Phase 1+2 rebuild** to refresh DuckDB views:
   ```
   python3 ~/Desktop/Archive/scripts/build/01_load_csvs_v3.py --archive ~/Desktop/Archive/archive_masters --wiki ~/Repos/kastner-aberdeen-wiki
   python3 ~/Desktop/Archive/scripts/build/02_build_data_layer_v4.py --wiki ~/Repos/kastner-aberdeen-wiki
   ```
9. **Shape audit** (kastner-archive-pipeline skill §Shape audit). Expected: no change from v1.6.2 baseline (1,453 / 23,926 / 3,276 / 4,361 / 865 high-prescience).
10. **Phase 5 surgical re-embed** of the three changed Perplexity_Only docs:
    - `MASTERS_NOTES.md`
    - `PRESCIENCE_ARCHITECTURE.md`
    - `F7_preseed_skip_sh_treatment_decision_v1.md`
11. **Tag v1.7.0** in repo (annotated tag with these release notes); update GitHub release.

---

## What is NOT in v1.7.0

- No new studies ingested.
- No corpus shape change (still 1,453 / 23,926 / 3,276 / 4,361 / 865).
- No DuckDB view schema change. `v_studies` columns unchanged.
- No `kw ask` retrieval behavior change.
- Driver v8 itself is NOT released in v1.7.0 — only its schema contract is locked in. v8 ships in a later release once the SH gates are evaluated.
- F1, F4, F5, F8, F9, F10 remain open (see audit doc).
- Pass C scoring on 17 new transcripts is still pending (~30-60 min when run).

---

## Commit lineage

| Commit | Repo | Contents |
|---|---|---|
| [`0f5c9d71`](https://github.com/shorttack/aberdeen-group-archive/commit/0f5c9d71) | aberdeen-group-archive | Initial `Perplexity_Only/PRESCIENCE_ARCHITECTURE.md` (v1 architectural map) |
| [`7935aec7`](https://github.com/shorttack/aberdeen-group-archive/commit/7935aec7b15200132c649e48e1f4632f133ae9c8) | aberdeen-group-archive | **F2:** patched `promote_pass_c_to_master_v1.py` to match Mac active copy |
| [`5f945dd9`](https://github.com/shorttack/aberdeen-group-archive/commit/5f945dd97461dde813043ae3620b5b8fcfe648bd) | aberdeen-group-archive | **F3 + F6 + F7:** row_class migration script + retag script + SH treatment decision doc |
| _pending_ | aberdeen-group-archive | **v3 + rev2:** MASTERS_NOTES v3 + PRESCIENCE_ARCHITECTURE rev2 + this RELEASE_NOTES |

---

## Cross-references

- Audit findings report: [`Archive/decisions/prescience_architecture_audit_v1.md`](Archive/decisions/prescience_architecture_audit_v1.md) (2026-06-15)
- Architectural map: [`Perplexity_Only/PRESCIENCE_ARCHITECTURE.md`](Perplexity_Only/PRESCIENCE_ARCHITECTURE.md) (rev2)
- Schema reference: [`Perplexity_Only/MASTERS_NOTES.md`](Perplexity_Only/MASTERS_NOTES.md) (v3)
- F7 decision: [`Perplexity_Only/F7_preseed_skip_sh_treatment_decision_v1.md`](Perplexity_Only/F7_preseed_skip_sh_treatment_decision_v1.md)
- Pipeline skill: `kastner-archive-pipeline` v1.7

---

**Maintained by:** Pete Kastner + Perplexity Computer.
