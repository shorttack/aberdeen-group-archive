# codes.csv Schema Migration — 2026-04-24

Migrated 70 studies from 11 non-canonical `codes.csv` schemas to the v18
canonical 4-column schema: `code_id, code_type, label, definition`.

## Variant distribution (pre-migration)
| Variant | Count |
|---|---|
| `(code, description)` | 10 |
| `(code_id, code_label, code_description, applies_to)` | 10 |
| `(code, category, description)` | 9 |
| `(code_id, code_type, code_value, label, description)` | 9 |
| `(code_id, code_type, code_value, description, study_id)` | 9 |
| `(code_id, code_type, description)` | 5 |
| `(code, label, domain, description)` | 5 |
| `(code, label, description)` | 4 |
| `(code, label, category, description)` | 4 |
| `(code, label, description, category)` | 4 |
| `(code_id, scheme, code, label, description)` | 1 |
| **Total migrated** | **70** |

Plus 605 already-canonical studies = **675 studies, 100% canonical**.

## Mapping rules
- `code_id` ← `code_value` (if present) / `code` / existing `code_id` / `code_label`
- `code_type` ← `code_type` / `category` / `scheme` / `domain` / `applies_to` (defaults to `observation_type` when absent)
- `label` ← `label` / `code_label` (auto-title-cased from code_id if both absent)
- `definition` ← `definition` / `description` / `code_description`

## Safety verification
Pre-migration dry-run confirmed 0 observations.csv references would be orphaned by the migration (every `obs.observation_type` value resolves to a migrated `code_id`). Post-migration ref-int audit confirms Layer A = 0 failures (unchanged from 102a39d).

## Residual 30 audit failures (unchanged)
Still the 10 alt-schema entity/technology studies from the prior audit. Those are orthogonal to codes.csv and require separate entities/technologies migration (not this pass).

## Rollback
Original files backed up under `_audits/codes_migration_backup/<study>/codes.csv`.
