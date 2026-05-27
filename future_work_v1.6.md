# v1.6 Backlog

**Created:** 2026-05-27
**Target release:** v1.6

This file captures items deferred from prior releases that are scoped for the v1.6 cycle. Items here have been investigated enough to be actionable but were intentionally pushed out of v1.5.x to keep that release tight.

---

## 1. Fix the pub_year date parser in `01_load_csvs_v2.py`

**Origin:** v1.5.1 pub_year backfill (v6, 2026-05-27) — discovered the original Phase 1 loader was responsible for 350 of the 1,434 studies having null `pub_year` even when source data carried a parseable year.

**Two failure modes identified:**

1. **Plain-English date strings in `_master_studies.csv`'s `date` column** silently fail to parse. Examples observed:
   - `June 2001`
   - `November 2006`
   - `May 1997`
   - `April 13, 2004`
   The current parser expects ISO-ish forms (`YYYY-MM-DD`, `YYYY-MM`, `YYYY`); freeform month+year and month+day+year strings get dropped to null.

2. **`f-4q04-*` filename patterns** are not recognized by the qcode extractor. The `1q05`, `2q06`, etc. patterns work; the `f-` prefix variant (Aberdeen "fast" research format) is unhandled.

**Resolution path:**
- Add a freeform-date fallback to the `derive_pub_year` step in `01_load_csvs_v2.py` — `dateutil.parser.parse(value, fuzzy=True)` with a year-range sanity check (1970–2026).
- Extend the qcode regex to match `f-?[1-4]q\d{2}` in addition to the current `[1-4]q\d{2}`.
- After patching, re-run Phase 1+2 against the current masters. Expected: zero new derived years (since v6/v6.1 already filled the gaps), but the parser becomes resilient for future ingest.

**Acceptance:**
- Unit test exercising all four plain-English forms above + an `f-4q04-...` filename → all yield correct years
- Phase 1 logs `1434/1434 resolved; 0 missing` against current masters
- Note added to `_decisions_log.md` under v1.6 entry

---

## 2. Full filename-vs-text year audit ("choice b" from v6 review)

**Origin:** v1.5.1 v6.1 corrections (2026-05-27). Four rows had `pub_year` values outside the 1970–2026 plausible range (1904, 1905×2, 2030) and were trivially caught by a range filter and hand-corrected. But this only catches glaringly-bad values. **Silent misparses inside the plausible range remain undetected.**

**Specific risk:** the v2 extractor (text-grep, earliest-year-in-file) could have picked an OCR artifact, a page number, a copyright footer year, or a quoted historical year and assigned it as `pub_year`, even when the filename's qcode (`2q03`, `4q06`, etc.) or MMDDYY suffix disagrees.

**Resolution path:**
- For every row in `_master_studies.csv` where the study_id contains a qcode or MMDDYY pattern, derive the filename-implied year independently
- Compare against `pub_year`. Flag disagreements > 1 year (allow ±1 year for end-of-quarter edge cases)
- Emit `pub_year_audit_v1.csv` with: study_id, filename_year, text_pub_year, delta, sample_filename_pattern
- Pete reviews flagged rows, decides each
- Apply corrections via a `apply_pub_year_v6_2.py` (same dry-run / `--commit` pattern as v6.1)

**Acceptance:**
- Audit CSV emitted with all suspect rows
- Pete reviews; corrections applied or each row is annotated "filename-vs-text disagreement reviewed and accepted"
- Note added to `_decisions_log.md`

---

## 3. Fix the `v_studies_by_decade` view

**Origin:** v1.5.1 pub_year work (2026-05-27). Spotted during routine decade-rollup verification.

**Current behavior (wrong):** view returns 38 rows — one per distinct year — with the year as a string with `'s'` appended (`'2003s'`, `'2004s'`, etc.). The intent was a decade bucket (`'2000s'`, `'2010s'`).

**Likely SQL bug:** something like `pub_year || 's' AS decade` instead of `((pub_year/10)*10) || 's' AS decade`.

**Resolution path:**
- Find the view definition in `02_build_data_layer_v2.py`
- Patch to `((CAST(pub_year AS INTEGER)/10)*10) || 's'` (or equivalent DuckDB-native form)
- Re-run Phase 2 (`02_build_data_layer_v2.py`)
- Verify: `SELECT decade, COUNT(*) FROM v_studies_by_decade GROUP BY decade ORDER BY decade;` returns ~6 rows (1970s, 1980s, 1990s, 2000s, 2010s, 2020s)

**Downstream impact:** any Dataview query or wiki page that uses `v_studies_by_decade` is currently meaningless. Check `decades/*.md` and any `kw ask` decade prompts after the fix.

**Acceptance:**
- View returns 6 rows (one per decade)
- Decade overview pages in `wiki/decades/` render correctly against the fixed view
- Note added to `_decisions_log.md`

---

## Cross-references

- v6 application: `apply_pub_year_v6.py` (`scripts/`), audit at `pub_year_apply_v6_applied.txt`
- v6.1 corrections: `apply_pub_year_v6_1.py` (`scripts/`), audit at `pub_year_apply_v6_1_applied.txt`
- v6 candidates CSV: `pub_year_candidates_v6.csv` (workspace)
- Backups: `_master_studies.csv.bak_pub_year_v6_20260527T163250Z`, `.bak_pub_year_v6_1_20260527T182420Z`
