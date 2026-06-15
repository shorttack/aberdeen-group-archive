# Decision: §11v D6 Audit Cleanup — F2/F3/F4/F6/F7 landed

**Date:** 2026-06-15 (Monday, 15:55 EDT)
**Session:** §11v — Prescience Architecture Audit (D6) cleanup
**Status:** LANDED (atomic batch commit)
**Author:** Pete Kastner + Computer
**Trigger:** Pete — "all my recommendations" after audit doc presented 6 action items

---

## Summary

Six §11v audit items closed in one atomic batch. Master `_master_prescience_scores.csv` grew from 11 → 12 columns; scorer_version + source_pass enums unified; 12 cloud parse-fails retagged; promote script committed to version control; preseed_skip SH treatment documented.

**No API calls. No row count changes. Score/confidence/rationale/scored_at/elapsed_sec untouched.**

---

## Items closed

### F2 — Promote script committed to version control

Committed `scripts/promote_pass_c_to_master_v1.py` with the 5-line CSV-provenance-preservation patch applied. Patch preserves row-borne `scorer_version` and `source_pass` over CLI-default values — required for Tier A retag (parse-fail tagging) and now for future row-class-marker preservation. Patch attribution in inline comment: commit `c587fee6`, 2026-06-15 ~05:00 EDT inline-fix.

### F3 — `row_class` column added

12th column added to `_master_prescience_scores.csv`. Enum: `{scored, parse_fail, prefilter, preseed_skip}`. Distribution after backfill:

| row_class | count | derived from |
|---|---|---|
| `scored` | 8,119 | default case (everything not below) |
| `preseed_skip` | 253 | `model = preseed_skip_v1` |
| `parse_fail` | 64 | (52 sonar `pass_c_sonar_v1_parse_fail`) + (12 cloud `parse_ok=false`) |
| `prefilter` | 4 | `source_pass = pass_c_prefilter_v1` |
| **total** | **8,440** | |

**Future row_class values reserved** for short-horizon scoring (per v3 SH spec):
- `pending` — window not elapsed; score = -2
- `no_anchor` — anchor resolution hard-fail; score = -1

The `model` column is now restricted to actual ML model names (`sonar-reasoning-pro`, `claude-sonnet-4.6`, `preseed_skip_v1`). The `preseed_skip_v1` value in `model` remains for backward compatibility; row_class is the canonical signal going forward. Driver v8 MUST NOT write sentinel values into `model`.

### F4 — Unified scorer_version naming

Convention: `pass_<phase>_<source>_<v>`. Backfill:

| Old | New | Rows |
|---|---|---|
| `cloud_v1` | `pass_c_cloud_v1` | 4,082 |
| `v6` | `pass_c_sonar_v6` | 4,358 |

Future scorer_version values follow the same pattern (`pass_c_sonar_sh_v1` etc.).

### F6 — Cloud parse-fail retag

12 rows retagged: `source_pass` `pass_c_cloud` → `pass_c_cloud_parse_fail`. All had `parse_ok=false` and rationale starting with "Parse failed after 3 retries". Now consistent with sonar parse-fail convention (`pass_c_sonar_v1_parse_fail`).

Updated source_pass distribution:

| source_pass | count |
|---|---|
| `pass_c_sonar_v1` | 4,302 |
| `pass_c_cloud` | 4,070 (was 4,082; 12 moved out) |
| `pass_c_sonar_v1_parse_fail` | 52 |
| `pass_c_cloud_parse_fail` | 12 (new) |
| `pass_c_prefilter_v1` | 4 |

### F7 — preseed_skip SH treatment

**Decision: score preseed_skip rows normally in short-horizon scoring.**

Rationale: preseed_skip status was a one-time long-horizon decision (Pete 2026-06-13, preserving in-thread Pass B prescience). It says nothing about whether a 3y or 5y window has elapsed for those observations. The 253 preseed_skip rows have valid `obs_id`, valid `study_id`, valid anchor sources — they are scoreable along the SH axis.

Driver v8 reads `_master_observations.csv` for the corpus, not `_master_prescience_scores.csv`. The preseed_skip status lives only in the prescience master; the observations master doesn't know about it. v8 naturally scores them. No special-casing required.

**Invariant for promote-to-master:** when an obs_id has BOTH (a) a `row_class=preseed_skip` long-horizon row and (b) a new SH row with `row_class=scored`, both are preserved as separate rows distinguished by `scorer_version` (`pass_c_sonar_v6` vs `pass_c_sonar_sh_v1`). The master allows multiple rows per obs_id when they differ in scorer_version. (Already implicit in the current schema — no obs_id has more than one row today, but the design accommodates it.)

### F5 — Deferred (Pete: skip)

1,110 rows with `elapsed_sec=0.0` (1,106 cloud + 4 prefilter) left as-is. Purely cosmetic; no functional impact. Can be revisited if throughput-by-source analytics ever matter.

---

## What was NOT changed

- Row count: **8,440** (unchanged)
- obs_id set: **identical** (zero adds, zero removes)
- `prescience_score`, `confidence`, `rationale`, `scored_at`, `elapsed_sec`: **untouched**
- `_master_observations.csv`: **untouched** (this cleanup is prescience-master-only)
- `_master_studies.csv`: **untouched**

---

## Schema (post-cleanup)

`_master_prescience_scores.csv` — **12 columns**:

```
obs_id, study_id, model, prescience_score, confidence, rationale,
scored_at, scorer_version, source_pass, elapsed_sec, parse_ok,
row_class
```

Enums (closed sets, as of this commit):

- `row_class`: `{scored, parse_fail, prefilter, preseed_skip}` — extends with `{pending, no_anchor}` when SH lands
- `scorer_version`: `{pass_c_cloud_v1, pass_c_sonar_v6}` — extends with `{pass_c_sonar_sh_v1, pass_c_sonar_sh_v1_parse_fail}` when SH lands
- `source_pass`: `{pass_c_cloud, pass_c_cloud_parse_fail, pass_c_sonar_v1, pass_c_sonar_v1_parse_fail, pass_c_prefilter_v1}` — extends with `{pass_c_sh_combined, pass_c_sh_3y_only, pass_c_sh_pending, pass_c_sh_no_anchor}` when SH lands
- `model`: `{sonar-reasoning-pro, claude-sonnet-4.6, preseed_skip_v1}` — extends with `{sonar-pro}` when SH lands; v8 MUST NOT add sentinel values

---

## v3 SH spec — what changes downstream

The §11v cleanup gives v3 SH spec a cleaner foundation. Specifically:

1. **v3 schema entry (`masters_notes_sh_schema_entry_v1.md`)** — 14 new SH columns still append cleanly. No change.
2. **Driver v8 spec** — should reference `row_class` column instead of inferring from `model`. Update queued.
3. **Acceptance Gates v2** — G1 schema invariants now check `row_class` enum membership. Update queued.

Both updates are doc-only; defer to a follow-up commit once v8 code begins.

---

## Pre-flight verification (workspace, before commit)

Backfill ran via `audit_d6/backfill_master_presc_v1.py`. All invariants PASS:

- row count: 8,440 unchanged ✓
- obs_id set: identical ✓
- score=5 count: unchanged ✓
- total rationale length: unchanged ✓
- row_class enum closed: ✓
- scorer_version enum closed: ✓
- source_pass enum closed: ✓
- 12 cloud parse-fails moved: ✓
- output SHA256: `72098b36db4718723e28c944e79e01c16d2d257efe888f924990953af6f9a2b9`

---

## Mac pull required

After this commit lands, Pete runs on Mac:

```bash
cd ~/Desktop/Archive/aberdeen-group-archive
git pull --no-rebase origin main
```

Then sync `~/Desktop/Archive/archive_masters/` to match (Mac drift check confirmed it's a separate copy of the same file):

```bash
cp ~/Desktop/Archive/aberdeen-group-archive/_master_prescience_scores.csv \
   ~/Desktop/Archive/archive_masters/_master_prescience_scores.csv
shasum -a 256 ~/Desktop/Archive/archive_masters/_master_prescience_scores.csv
# Expected: 72098b36db4718723e28c944e79e01c16d2d257efe888f924990953af6f9a2b9
```

---

## Cross-references

- `Archive/decisions/prescience_architecture_audit_v1.md` (audit, commit `1559d41a`)
- `Archive/decisions/decisions_log_entry_2026_06_15_short_horizon_prescience_v3.md` (v3 SH spec)
- `scripts/promote_pass_c_to_master_v1.py` (this commit, with F2 patch)
- Workspace verification artifact: `audit_d6/backfill_master_presc_v1.py`
