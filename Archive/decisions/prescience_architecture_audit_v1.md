# Prescience Architecture Audit (§11v / D6)

**Date:** 2026-06-15 (Monday, 15:45 EDT)
**Auditor:** Computer (read-only)
**Scope:** GitHub `shorttack/aberdeen-group-archive` main branch; Mac filesystem drift covered by checksum hand-off
**Trigger:** Pete — "It behooves us to tackle §11v Prescience Architecture Audit (D6) before building out more on an unknown structure."
**Method:** Read-only inspection of repo state, master CSVs, driver source, and rollup outputs. No writes to masters.

---

## Top-line verdict

**Foundation is structurally sound but operationally drifted.** The prescience master has clean referential integrity (zero orphan IDs, zero duplicates), populated provenance, and passes G3b monotonicity. **However:** three undocumented row classes exist (preseed_skip, cloud parse-fail in-band, sonar parse-fail split), the `model` column conflates models with sentinel markers, scorer-version naming is ad-hoc, the promote script that produced 50% of the master is not in version control, and the v3 spec for short-horizon scoring does not anticipate any of these row classes.

**Recommendation: 4 must-fix items before driver v8 is written. 6 should-fix items can land in parallel.**

---

## File inventory (as of `a77d52c4` on main)

### Master files at repo root

| File | Size (bytes) | Rows | Notes |
|---|---|---|---|
| `_master_observations.csv` | 9,925,499 | 23,926 | Observation entity table; **17 cols, NO prescience score columns** |
| `_master_prescience_scores.csv` | 6,435,437 | 8,440 | Prescience scores; **11 cols**; THIS is what v3 spec extends |
| `_master_studies.csv` | 2,009,904 | — | Study entity table |
| `_master_entities.csv` | — | — | Not deep-audited (out of scope) |
| `_master_technologies.csv` | — | — | Not deep-audited |
| `_master_codes.csv` | — | — | Not deep-audited |
| `_master_entity_studies.csv` / `_master_tech_studies.csv` / `_master_entity_field_conflicts.csv` | — | — | Junction/audit tables |

### Stray prescience artifacts at repo root (FINDING F1)

- `prescience_scores_pass_c_cloud_v1.csv` (2,439,387 bytes) — appears to be a frozen snapshot from Pass C cloud run. Not the master. Risk: future readers may treat it as authoritative.
- `model_prescience_scoring_finding_v1.md` — undated decision-class doc at repo root, not under `Archive/decisions/`
- `readme_prescience.md` — undated readme at repo root
- `master_entities.csv`, `master_studies.csv`, `master_technologies.csv` — duplicate-named files without the `_` prefix. Almost certainly legacy/stale; needs verification before deletion.

### Driver and tooling scripts (`scripts/`)

| Script | Purpose | In version control? |
|---|---|---|
| `run_prescience_pass_c_v5.py` | Old driver | yes (kept for archaeology) |
| `run_prescience_pass_c_v6.py` | Tier A driver | yes |
| `run_prescience_pass_c_v7.py` | Tier B driver (network-hardened) | yes (commit `bec0398d`) |
| `prescience_acceptance_gates_v1.py` | Gates v1 (single-score) | yes |
| `roll_up_prescience_to_master_v3.py` | Master rollup | yes |
| `audit_prescience_runs_v1.py` | Run auditor | yes |
| `run_prescience_calibration_v3..v7.py` | Calibration runners (qwen + cloud + sonar) | yes |
| **`promote_pass_c_to_master_v1.py`** | **Pass C → master promotion** | **NOT IN REPO** (workspace + Mac only) |

**FINDING F2 (must-fix before v8):** The promote script that materialized 50% of the current master (cloud_v1 → 4,082 rows, sonar_v1 → 4,358 rows) is not in version control. Patched in-session (5-line fix to preserve CSV-borne provenance over CLI defaults) but never committed. Driver v8 will need a v2 promote script; without v1 in-repo, the diff history is opaque.

---

## Dimension 1 — Schema reality vs spec

### `_master_prescience_scores.csv` — 11 columns

| # | Column | Type observed | Domain observed | v3 spec calls for | Status |
|---|---|---|---|---|---|
| 1 | `obs_id` | str | non-empty | preserved | ✓ |
| 2 | `study_id` | str | non-empty | preserved | ✓ |
| 3 | `model` | str | `{sonar-reasoning-pro, claude-sonnet-4.6, preseed_skip_v1}` | **add tagging for sonar-pro** | ⚠ category error (see F3) |
| 4 | `prescience_score` | int \| empty | `{-1,0,1,2,3,4,5,EMPTY}` | extend with `-2`; add 5 more score cols | ✓ extends cleanly |
| 5 | `confidence` | int \| empty | `{1,2,3,EMPTY}` | int 1-3 | ✓ matches v3 |
| 6 | `rationale` | str | non-empty everywhere | preserved | ✓ |
| 7 | `scored_at` | ISO8601 | all 2026; no empties | preserved | ✓ |
| 8 | `scorer_version` | str | `{cloud_v1, v6}` | extend with `pass_c_sonar_sh_v1` | ⚠ naming drift (see F4) |
| 9 | `source_pass` | str | `{pass_c_cloud, pass_c_sonar_v1, pass_c_sonar_v1_parse_fail, pass_c_prefilter_v1}` | extend with 4 SH variants | ✓ extends cleanly |
| 10 | `elapsed_sec` | float-str | `0.0` on 1,110 rows | preserved | ⚠ 1,106 cloud rows have `0.0` (no timing — see F5) |
| 11 | `parse_ok` | str-bool | `{true, false}`; 64 false / 8,376 true | preserved | ⚠ 12-row inconsistency (see F6) |

### MASTERS_NOTES.md schema entry status

Not audited in detail — `MASTERS_NOTES.md` not fetched. **Recommendation:** before driver v8 lands, cross-reference MASTERS_NOTES.md against the 11 columns actually present and reconcile.

---

## Dimension 2 — Scorer-version × source_pass taxonomy

```
scorer_version          rows
  cloud_v1               4,082
  v6                     4,358

source_pass             rows
  pass_c_cloud           4,082
  pass_c_sonar_v1        4,302
  pass_c_sonar_v1_parse_fail  52
  pass_c_prefilter_v1        4

Cross:
  v6 + pass_c_sonar_v1            4,302
  cloud_v1 + pass_c_cloud         4,082
  v6 + pass_c_sonar_v1_parse_fail    52
  v6 + pass_c_prefilter_v1            4
```

**FINDING F4 (should-fix):** `scorer_version` values are `cloud_v1` and `v6` — incompatible naming conventions. Cloud uses `<source>_<v>` pattern; Sonar uses raw `v<N>` pattern. v3 spec introduces a third pattern: `pass_c_sonar_sh_v1`. With v8 about to add SH columns, this drift will compound.

**Recommendation:** adopt unified convention `pass_<phase>_<source>_<v>` (e.g., `pass_c_cloud_v1`, `pass_c_sonar_v6`, `pass_c_sonar_sh_v1`). Backfill existing rows in a single one-shot pass (cheap; non-API).

---

## Dimension 3 — Score distribution

### Overall (n=8,440)

| Score | Count | % | Interpretation |
|---|---|---|---|
| `-1` | 852 | 10.1% | prefilter + parse-fail + (some cloud parse-fails inline) |
| `0` | 3,746 | **44.4%** | wrong / not-a-claim — dominant class |
| `1` | 134 | 1.6% | rare — model avoids weak-correct |
| `2` | 345 | 4.1% | weak-correct |
| `3` | 805 | 9.5% | moderately prescient |
| `4` | 1,703 | **20.2%** | strongly prescient — second-largest |
| `5` | 602 | 7.1% | transformative |
| EMPTY | 253 | 3.0% | **preseed_skip rows (see F7)** |

**Pattern:** bimodal — 44% are 0, 20% are 4. The middle (1-3) is sparse (15%). Consistent with "model reaches strong verdicts; rarely hedges in the middle." Not necessarily a problem; the prompt instructs decisive scoring. Worth verifying calibration sample lands similarly.

### By source_pass (compressed)

| Source pass | n | Score profile |
|---|---|---|
| `pass_c_cloud` | 4,082 | -1: 796, 0: 1,752, 1: 14, 2: 68, 3: 355, 4: 775, 5: 69, EMPTY: 253 |
| `pass_c_sonar_v1` | 4,302 | 0: 1,994, 1: 120, 2: 277, 3: 450, 4: 928, 5: 533 (NO -1, NO empties) |
| `pass_c_sonar_v1_parse_fail` | 52 | -1: 52 |
| `pass_c_prefilter_v1` | 4 | -1: 4 |

**Observation:** Sonar Pass C produced 7.7x more `5` verdicts than Cloud (533 vs 69) on similar-sized cohorts. This is a substantial scoring-distribution difference between models for the same observation pool. Could indicate (a) different stratification (Tier A sampled higher-quality obs), (b) model bias, or (c) prompt-version drift. **Flag for hand investigation before SH scoring** — if Sonar scores too high, SH scores will inherit the bias.

---

## Dimension 4 — Confidence distribution

```
Overall (excluding 253 empty preseed rows):
  conf=1   1,183  (14.5%)
  conf=2   1,446  (17.7%)
  conf=3   5,558  (67.9%)

G3b monotonicity check:
  Mean confidence at score=5: 2.98
  Mean confidence at score=0: 2.64
  → PASS (5 ≥ 0)
```

### By score (informative)

```
score=-1: conf=1 always (852 rows)        — prefilter/parse_fail convention
score=0:  conf 1/2/3 = 325/692/2729      — mostly high-confidence "wrong"
score=1:  conf 2/3   = 21/113            — high confidence even on weak score (unusual)
score=2:  conf 1/2/3 = 4/110/231
score=3:  conf 1/2/3 = 2/347/456
score=4:  conf 2/3   = 265/1438          — high confidence
score=5:  conf 2/3   = 11/591            — overwhelmingly confidence=3
```

**Observation:** confidence=3 dominates (68% of scored rows). Slightly concerning — suggests model rarely admits uncertainty. Not blocking but worth a calibration note: **expect SH scoring to inherit this pattern. If G3a (class presence) is added as a HARD gate, it may fail on natural runs even when the data is good.** Adjust gate threshold accordingly.

---

## Dimension 5 — Rationale quality (spot-check)

Random sample, 3 per source_pass (seed 20260615):

| Source pass | mean len | range | empty | Quality verdict |
|---|---|---|---|---|
| `pass_c_cloud` | 505 chars | 32-1,259 | 0 | substantive; specific years/vendors cited |
| `pass_c_sonar_v1` | 654 chars | 264-1,248 | 0 | substantive; richer than cloud avg |
| `pass_c_sonar_v1_parse_fail` | 94 chars | 88-107 | 0 | structured tag: "Parse failed after 3 retries: ..." ✓ |
| `pass_c_prefilter_v1` | 58 chars | 32-66 | 0 | structured tag: "Pre-filter: figure caption only." ✓ |

**Verdict: rationale quality is solid across all source_passes.** No empty rationales anywhere in the master. Tagged short rationales (prefilter, parse-fail) are intentional and machine-parseable. Substantive rationales (cloud, sonar) cite concrete years, vendors, and technology trajectories.

---

## Dimension 6 — Provenance integrity

```
scored_at_empty:      0       (all 8,440 rows have a timestamp)
scored_at_malformed:  0       (all start 19xx/20xx)
scored_at year dist:  2026: 8440  (entire master scored in current calendar year)
elapsed_sec_empty:    0
elapsed_sec_zero:     1,110   (1,106 pass_c_cloud + 4 pass_c_prefilter)
parse_ok_empty:       0
parse_ok_dist:        true: 8,376  false: 64
obs_id_empty:         0
study_id_empty:       0
model_empty:          0
```

**Verdict:** core provenance is clean. Timestamps present everywhere. obs_id/study_id never empty.

**FINDING F5 (informational):** 1,106 cloud-pass rows have `elapsed_sec=0.0` — cloud driver did not track per-row timing. The 4 prefilter rows likewise. Not a bug but a provenance gap. Should be backfilled with `NULL` or `nan` if we ever want to compute throughput by source.

---

## Dimension 7 — Mac ↔ GitHub drift

**Computer cannot inspect Mac filesystem directly.** Hand-off block for Pete (run on Mac, paste output back):

```bash
# Master file drift check
M=~/Desktop/Archive/aberdeen-group-archive
cd "$M"
echo "=== Repo HEAD ==="
git rev-parse HEAD
echo ""
echo "=== Master prescience: row count + SHA256 ==="
wc -l _master_prescience_scores.csv
shasum -a 256 _master_prescience_scores.csv
echo ""
echo "=== Master observations: row count + SHA256 ==="
wc -l _master_observations.csv
shasum -a 256 _master_observations.csv
echo ""
echo "=== Source-pass distribution (Mac side) ==="
python3 -c "import csv; from collections import Counter; r=csv.DictReader(open('_master_prescience_scores.csv')); print(Counter(x['source_pass'] for x in r))"
echo ""
echo "=== archive_masters/ dir SHA256 of same files ==="
shasum -a 256 ~/Desktop/Archive/archive_masters/_master_prescience_scores.csv 2>/dev/null
shasum -a 256 ~/Desktop/Archive/archive_masters/_master_observations.csv 2>/dev/null
```

**Expected GitHub state (verify against):**

| File | Rows (incl header) | SHA256 |
|---|---|---|
| `_master_prescience_scores.csv` | 8,441 | `feccd914f8585f21ada943071e1f802640c6fa95bc252cd5f0459bcc011a161d` |
| `_master_observations.csv` | 23,927 | `9427887d6710a6deae3a72d8e55f5152b3792982db92325585ec992341018b6d` |
| Expected source_pass distribution | — | `{pass_c_cloud: 4082, pass_c_sonar_v1: 4302, pass_c_sonar_v1_parse_fail: 52, pass_c_prefilter_v1: 4}` |

If SHA matches → drift = zero. If not → diff inspection required before v8.

---

## Dimension 8 — Cross-references and row-class invariants

### obs_id integrity (clean)

- `obs_id` in prescience NOT in observations: **0** ✓
- `obs_id` in observations NOT in prescience: **15,486** (unscored backlog — Tier B in flight covers 10K, rest is Tier C/D)
- Duplicate obs_id in prescience master: **0** ✓

### Row classes actually present (FINDING F3, F7, F8)

The master holds **five distinct row classes**, but the v3 spec models only three (`scored`, `pending`, `no_anchor`):

| Class | n | Identification | v3 spec parallel |
|---|---|---|---|
| **Scored (cloud)** | 4,082-12 = **4,070** | `model=claude-sonnet-4.6` AND `parse_ok=true` (after fixing F6) | `pass_c_sh_combined` |
| **Scored (sonar)** | **4,302** | `source_pass=pass_c_sonar_v1` | `pass_c_sh_combined` |
| **Parse-fail (sonar, retagged)** | **52** | `source_pass=pass_c_sonar_v1_parse_fail` | `pass_c_sonar_sh_v1_parse_fail` |
| **Parse-fail (cloud, in-band)** | **12** | `source_pass=pass_c_cloud` AND `parse_ok=false` | ⚠ unmodeled |
| **Pre-filter** | **4** | `source_pass=pass_c_prefilter_v1` | ⚠ unmodeled in v3 (deferred?) |
| **Preseed-skip** | **253** | `model=preseed_skip_v1`, score+conf empty | ⚠ unmodeled in v3 |

**FINDING F3 (must-fix before v8):** the `model` column conflates ML model identity with row-class marker. `preseed_skip_v1` is not a model — it's a sentinel for "Pete's 2026-06-13 decision to preserve in-thread Pass B prescience." Driver v8 will further pollute this column if not addressed. **Recommendation:** add an explicit `row_class` column to the master (one of `scored`, `parse_fail`, `prefilter_skip`, `preseed_skip`, `no_anchor`, `pending`) and keep `model` strictly for ML model names.

**FINDING F6 (must-fix before v8):** parse-fails are handled inconsistently across passes. Sonar parse-fails were split into their own `source_pass=pass_c_sonar_v1_parse_fail` (52 rows). Cloud parse-fails were left in `source_pass=pass_c_cloud` with `parse_ok=false` (12 rows). Same problem, two conventions. **Recommendation:** retag the 12 cloud parse-fails to `source_pass=pass_c_cloud_parse_fail` (or unified convention) in a one-shot pass. Driver v8 should write parse-fails to a dedicated SH parse-fail source_pass from the start.

**FINDING F7 (must-fix before v8):** 253 preseed_skip rows are an undocumented row class. They have empty score/confidence, populated rationale (`preseed_skip: in-thread Pass B prescience preserved per Pete 2026-06-13`), and `parse_ok=true` (misleading — nothing was parsed). The v3 spec for SH does NOT address preseed rows. **Question for Pete:** should SH scoring (a) skip preseed rows entirely, (b) score them normally (their in-thread Pass B verdict is long-horizon, not short), or (c) treat them as a new class? Recommend (b) — SH is an independent run; preseed status is irrelevant to whether a 3y/5y window has elapsed.

**FINDING F8 (should-fix):** the 4 `pass_c_prefilter_v1` rows (figure captions, image dumps) score `-1`. v3 spec says `-1` is reserved for prefilter/no_anchor/parse_fail. Consistent. But: the prefilter row class isn't explicitly modeled in v3. **Recommendation:** driver v8 should re-prefilter at SH time (figure captions don't change between long-horizon and short-horizon runs) and write to `source_pass=pass_c_sh_prefilter`.

---

## Cross-cutting findings (recap)

| # | Finding | Severity | Resolution |
|---|---|---|---|
| **F1** | Stray prescience files at repo root (`prescience_scores_pass_c_cloud_v1.csv`, `readme_prescience.md`, `model_prescience_scoring_finding_v1.md`, `master_*.csv` duplicates) | should-fix | Move to `_archive/` or `Archive/decisions/`; document or delete duplicates |
| **F2** | Promote script `promote_pass_c_to_master_v1.py` not in version control | **must-fix before v8** | Commit the patched workspace version to `scripts/`; tag commit message with the 5-line preserve-CSV-provenance patch description |
| **F3** | `model` column conflates ML model identity with row-class markers | **must-fix before v8** | Add explicit `row_class` column; restrict `model` to model names only |
| **F4** | Scorer-version naming drift (`cloud_v1` vs `v6` vs proposed `pass_c_sonar_sh_v1`) | should-fix | Adopt unified `pass_<phase>_<source>_<v>` convention; one-shot backfill |
| **F5** | 1,110 rows with `elapsed_sec=0.0` (cloud + prefilter) | informational | Optional backfill to `NULL`/empty for clearer "no timing" semantics |
| **F6** | Parse-fail handling inconsistent (cloud in-band, sonar split out) | **must-fix before v8** | Retag 12 cloud parse-fails; driver v8 writes SH parse-fails to dedicated source_pass from day 1 |
| **F7** | 253 preseed_skip rows are an undocumented row class | **must-fix before v8** | Decide SH treatment (score normally vs skip); document row class in MASTERS_NOTES |
| **F8** | Prefilter row class not explicitly modeled in v3 SH spec | should-fix | Add `pass_c_sh_prefilter` to v3 source_pass enum; re-prefilter at SH scoring time |
| **F9** | Sonar produced 7.7x more `5` verdicts than Cloud on similar-sized cohorts | informational | Hand-investigate before SH sweep; calibration sample should expose if SH inherits bias |
| **F10** | MASTERS_NOTES.md not deep-audited in this pass | should-fix | Separate pass to reconcile MASTERS_NOTES against the 11 cols actually present |

---

## Pre-v8 must-fix checklist (4 items)

Before driver v8 lands and short-horizon scoring writes new rows:

1. **F2** Commit the workspace promote script to `scripts/` (v1, with patch).
2. **F3** Decide row-class column design (`row_class` vs reusing `source_pass` more strictly); update v3 spec.
3. **F6** Retag 12 cloud parse-fails for consistency. Decide SH parse-fail convention up front.
4. **F7** Decide preseed_skip treatment for SH scoring (Pete decision). Document.

These are cheap (hours, not days). After they land, v8 has a clean structural foundation.

---

## Out of scope for this audit

- DuckDB views (`v_studies`, etc.) — not audited; covered by `kastner-archive-pipeline` skill
- Wiki regeneration logic — separate concern
- `_master_observations.csv` semantic integrity (entity_id, tech_id references) — separate audit if needed
- Embeddings / nomic-embed index — separate concern
- Other masters (`_master_entities.csv`, `_master_studies.csv`) — only touched if needed by F2/F3/F7

---

## Pete's action items (numbered for tracking)

1. Run the Mac drift check block above; paste output back to verify F7-region SHA match
2. Decide F3 (`row_class` column? Yes/No)
3. Decide F7 (SH scoring of preseed_skip rows: score normally / skip / new class)
4. Confirm F4 unified naming convention adoption (or veto)
5. Authorize F2 commit of workspace promote script (Mac copy is current)
6. Authorize F6 cloud parse-fail retag (12 rows; surgical; non-API)

Once 1-6 are answered, Computer drafts the cleanup commits and proceeds to driver v8.