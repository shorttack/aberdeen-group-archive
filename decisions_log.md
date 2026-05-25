

## 2026-05-25 · year_observed backfill (Pass 1: copyright anchor)

**Trigger:** Pete's observation that "the original Aberdeen text will have a
year next to Copyright at the end of document." This is the strongest
date signal available locally and does not require LLM inference.

**Scope (Pass 1):**
* Column: `_master_observations.year_observed`
* Pre-state: 3,153 / 23,605 rows missing (13.4%)
* Confidence band selected: `very_high` only (copyright-year anchor matched
  in last 5 KB of `prepared/<study_id>/source/original_text.md`)
* Rows updated: **698**
* Post-state: 2,455 / 23,605 rows still missing (10.4%)

**Method:**
1. `extract_missing_dates_v3.py` scanned all observation-bearing studies
   for `Copyright YYYY [...] Aberdeen` (or looser `(c) YYYY` / `© YYYY`)
   in the document tail. Produced `proposed_year_observed_v3.csv` with
   per-row candidates and confidence ladder.
2. Pete manually spot-checked `very_high` rows in Excel and confirmed
   the regex was honest (no false positives from quoted vendor logos
   or other in-body copyright notices).
3. `apply_year_observed_v1.py` ran in two stages: preview-only first
   (zero master changes), then `--apply` with backup + atomic write.

**Provenance tag on updated rows:**
`local_date_extraction_v3_copyright_anchor`

**Audit:**
* Backup: `archive_masters_pre_year_observed_apply_20260525_211909Z/_master_observations.csv`
* Audit log: `v1.5_workspace/year_observed_apply_audit_v1.csv`
  (columns: obs_id, old_value, new_value, study_id, source_snippet,
   provenance_tag, applied_at_utc)
* Rollback (if ever needed):
  `cp <backup_path> <masters_path>`

**Confidence ladder (preserved for future passes):**

| Label | Definition | Rows | Status |
|---|---|---|---|
| very_high | Copyright-year anchor matched at study tail | 698 | **APPLIED 2026-05-25** |
| high | Year in same sentence as observation_text anchor, multiple hits | 941 | Pending Pass 2 |
| medium | Year in same sentence as anchor, single hit | 1,058 | Pending Pass 2 |
| low | Most-common year in doc, no anchor proximity | 207 | Pending Pass 3 (manual) |
| none | No year found, or source file missing | 249 | Pending Pass 3 (manual / from PDF) |

**Next decision point:** Pass 2 strategy for the `high` + `medium` rows
(~1,999). Options under consideration:
* Stricter regex requiring near-anchor + within sentence-of-claim
* LLM-assisted review against the source snippet
* Manual Excel pass

**Forever-archive note:** The 698 rows now carry both the new
`year_observed` value AND, via the audit log, the evidence snippet and
provenance tag that produced them. Future researchers can always
verify provenance.
