# §11v Phase 0 Follow-on — Calibration + Gates + Schema Extender

**Date**: 2026-06-15
**Commit**: `b57026f1` on `shorttack/aberdeen-group-archive` main
**Parent**: `81773d85` (Driver v8 + resolver v1)

## What landed

| File | LOC | Status |
|---|---|---|
| `scripts/build_sh_calibration_sample_v1.py` | 315 | NEW |
| `scripts/sh_gates_v2.py` | 502 | NEW |
| `scripts/extend_master_obs_sh_schema_v1.py` | 208 | NEW |
| `scripts/anchor_year_resolver_v2.py` | 178 | NEW (replaces v1) |
| `scripts/run_prescience_short_horizon_v8.py` | +13 / -4 | MOD (imports v2, uses study.date) |

## Field-name discovery (this segment)

Inspected live masters. Two field names in v1 were wrong:

- `_master_observations.csv` field is `year_observed`, **not** `obs_date`
- `_master_studies.csv` field is `date`, **not** `published_at`
- 100% of 1,452 studies have parseable year in `date` (1,335 YYYY-MM-DD, 60 YYYY-MM, 47 YYYY, 10 messy-with-year)
- Pete confirmed: "we have to use Date from master_studies. Many pubs had no date and I had to enter manually"

**Resolver v2 fix**: canonical field first, legacy fallback second, regex year-search inside any string (1900–2100). v1 retained on disk but no code should import it.

## Calibration eligibility math (live data)

- 23,926 total obs
- 5,000 excluded (already in Tier A)
- 683 dropped (anchor > 2020)
- 0 dropped (no anchor — study.date fallback catches all)
- **18,243 eligible** → 100-obs stratified draw trivial

## Test results

| Script | Test | Outcome |
|---|---|---|
| `build_sh_calibration_sample_v1.py` | Live masters | 100 rows, 20 buckets, 0 Tier A overlap |
| `sh_gates_v2.py` | Synthetic 100-row | 0 HARD fails, all 10 gates exercised, exit 0 |
| `extend_master_obs_sh_schema_v1.py` | Synthetic 5-row (17 → 31 cols) | All invariants pass; idempotency refusal works |
| `anchor_year_resolver_v2.py` | Self-test (Mac) | PASS |
| `run_prescience_short_horizon_v8.py` | Offline path tests | All 4 paths exercised (combined / 3y_only / pending / no_anchor) |

## Schema extender behavior

- 17 baseline cols → 31 cols (append 14 SH cols to the right of `legacy_obs_id`)
- Atomic write (tempfile + `os.replace`)
- SHA256 before/after, size delta logged
- Refuses to extend twice (idempotency check on baseline schema)
- Post-write invariants: row count unchanged, obs_id order byte-identical, pre-existing column values byte-identical, all SH cols empty
- Requires explicit `--backup` path (warns if omitted)

## Open

- Driver v8 has **not** been launched.
- Tier B PID 2163 still running on Mac (~28h remaining as of 4:20 PM EDT).
- Calibration GO/NO-GO run is the next gate.

## Refs

- Spec: `Archive/decisions/decisions_log_entry_2026_06_15_short_horizon_prescience_v3.md`
- Gates: `Archive/decisions/short_horizon_design/short_horizon_acceptance_gates_v2_spec.md`
- Schema: `Archive/decisions/short_horizon_design/masters_notes_sh_schema_entry_v1.md`
- Driver: `Archive/decisions/short_horizon_design/driver_v8_spec_v1.md`
