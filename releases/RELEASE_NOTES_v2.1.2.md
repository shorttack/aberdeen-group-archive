# Aberdeen Archive v2.1.2 — Release Metadata Correction

**Type:** Patch release. Metadata only — no data, schema, or scoring change from v2.1 / v2.1.1.

## Why this release exists

The v2.1.1 release published a Zenodo record whose archival metadata
(`.zenodo.json`, `CITATION.cff`) had not been bumped from v2.0. This release
brings the Zenodo- and citation-facing metadata in line with the current
archive and supersedes the stale record going forward.

## What changed

- `.zenodo.json` and `CITATION.cff`: `version` → **2.1.1/2.1.2**, `date-released`
  updated, internal tag id updated, and the `preferred-citation` block aligned.
- Description/abstract wording brought in line with the current README (neutral,
  product-facing engineering language; e.g. "window-elapsed validation" for the
  short-horizon scorer). Hardcoded corpus counts replaced with a pointer to the
  generated [`ARCHIVE_STATS.md`](../ARCHIVE_STATS.md) so metadata cannot go stale.

## Unchanged

- All `_master_*.csv` and per-study Frictionless packages — byte-identical to v2.1.
- Studies master remains 20 columns; per-study `studies.csv` remains 16 columns.
- Long-horizon and short-horizon (3y/5y) prescience surfaces unchanged.
- Concept DOI series continues via Zenodo (10.5281/zenodo.20245076).
