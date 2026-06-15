# MASTERS_NOTES.md — Schema Entry (PROPOSED INSERT)

**Status:** DRAFT (Phase 0). Insert into `MASTERS_NOTES.md` under existing `_master_observations.csv` section.

---

## `_master_observations.csv` — short-horizon prescience columns

**Added:** 2026-06-15 (Phase 0 spec lock)
**Driver:** `driver_v8.py` (forthcoming) under `scorer_version_sh = pass_c_sonar_sh_v1`
**Spec:** `Archive/decisions/decisions_log_entry_2026_06_15_short_horizon_prescience_v2.md`
**Resolver:** `anchor_year_resolver_v1.py`

### Convention

Adds **14 columns** (v2 doc said 11; v3 keeps `anchor_source` and `raw_response_sh` per Pete; drops `legacy_sh_id` reservation per YAGNI). Column block appended to end of `_master_observations.csv` after existing long-horizon prescience columns.

| # | Column | Type | Domain | Notes |
|---|---|---|---|---|
| 1 | `prescience_3y` | int | `{-2,-1,0,1,2,3,4,5}` | `-2`=window not elapsed, `-1`=prefilter/no_anchor, `0`=wrong, `1-5`=scaled |
| 2 | `confidence_3y` | int \| "" | `1..3` or `""` | int 1-3 (Tier A/B convention); NULL (empty) iff `prescience_3y ∈ {-2, -1}` |
| 3 | `rationale_3y` | str | free text or `window_not_elapsed:3y:cutoff_YYYY` or `no_anchor:<msg>` | ≤ 280 chars when scored |
| 4 | `prescience_5y` | int | same as 3y | independent of `prescience_3y` |
| 5 | `confidence_5y` | int \| "" | same as 3y | independent of `confidence_3y` |
| 6 | `rationale_5y` | str | same as 3y | independent of `rationale_3y` |
| 7 | `windows_diverge` | bool \| "" | `{True, False, ""}` | TRUE iff model asserts 3y vs 5y materially differ; "" for non-both-elapsed rows |
| 8 | `divergence_note` | str | free text or `""` | empty string when `windows_diverge` ∈ {False, ""}; ≤ 200 chars otherwise |
| 9 | `anchor_year` | int | `[1900, 2100]` | resolved per precedence order in resolver module |
| 10 | `anchor_source` | str | `{obs_date, memoir_period_start, study_published_at}` | audit field for resolver outcome |
| 11 | `scored_at_sh` | ISO8601 | UTC timestamp | single timestamp per row even if combined call |
| 12 | `scorer_version_sh` | str | `pass_c_sonar_sh_v1` \| `pass_c_sonar_sh_v1_parse_fail` | extend with version bumps |
| 13 | `source_pass_sh` | str | `{pass_c_sh_combined, pass_c_sh_3y_only, pass_c_sh_pending, pass_c_sh_no_anchor}` | records which code path produced the row |
| 14 | `raw_response_sh` | str \| "" | raw API response | empty for pending/no_anchor rows; preserved for parse-fail retry |

### Invariants (enforced by G1)

1. `prescience_3y = -2 ⇒ confidence_3y = "" AND rationale_3y matches "^window_not_elapsed:3y:cutoff_\d{4}$"`
2. `prescience_5y = -2 ⇒ confidence_5y = "" AND rationale_5y matches "^window_not_elapsed:5y:cutoff_\d{4}$"`
3. `prescience_3y = -1 ⇒ rationale_3y starts with "no_anchor:"` (same for 5y)
4. `windows_diverge = True ⇒ prescience_3y AND prescience_5y both in {0..5} AND divergence_note non-empty`
5. `source_pass_sh = pass_c_sh_pending ⇒ prescience_3y = -2 AND prescience_5y = -2`
6. `source_pass_sh = pass_c_sh_no_anchor ⇒ prescience_3y = -1 AND prescience_5y = -1`
7. Long-horizon `prescience` column (existing) is INDEPENDENT — short-horizon columns do not overwrite or reference it.

### Independence from long-horizon

Short-horizon and long-horizon are **two independent scoring runs** against the same obs corpus. A row can have any combination of (long-horizon scored / unscored) × (short-horizon scored / pending / no-anchor). Promote scripts for SH must NOT touch long-horizon columns, and vice versa.

### Derived view (for DuckDB / wiki)

`v_short_horizon_obs` view exposes:

```sql
SELECT
  obs_id,
  prescience_3y, prescience_5y,
  windows_diverge,
  anchor_year, anchor_source,
  CASE
    WHEN prescience_3y < 0 OR prescience_5y < 0 THEN 'unscored'
    WHEN prescience_3y = 0 AND prescience_5y = 0 THEN 'both_wrong'
    WHEN prescience_3y = 0 AND prescience_5y >= 1 THEN 'late_vindication'
    WHEN prescience_3y >= 1 AND prescience_5y = 0 THEN 'reversal'
    WHEN abs(prescience_3y - prescience_5y) <= 1 THEN 'stable'
    ELSE 'shift'
  END AS score_trajectory
FROM _master_observations
WHERE scorer_version_sh IS NOT NULL;
```

---

## Resolved (v3 spec lock)

- Column order: append to end of master (no interleaving with long-horizon cols).
- `legacy_sh_id`: dropped (YAGNI; short-horizon is greenfield).
- `score_trajectory`: DuckDB view only, not physical master column.
- `windows_diverge_mechanical`: computed by promote script for G8b cross-check; NOT persisted as a master column (recomputable from `prescience_3y`/`prescience_5y`).