# E-Class Admitted Orphans — Accept-as-Cited Disposition

**Status:** Final disposition documentation. Written 2026-07-25 (overnight AUTO batch, worklist item L98).

## Class definition

"E-class" orphans are rows that were **P1-admitted** into the archive (i.e., they
passed Pass 1 structural admission and carry valid canonical IDs, provenance, and
schema-conformant fields) but whose **headline content is cited inside the body
text of other corpus articles**, rather than being independently archived as a
standalone article/study of their own.

In other words: these rows are not orphaned in the sense of being incomplete or
invalid — they are orphaned only in the sense that no standalone article file
exists for them in the corpus. Their content is not lost; it is preserved
verbatim as a citation inside whichever other article(s) originally quoted or
referenced the headline.

## The 8 admitted rows in this class

| row_id (rid) |
|---|
| 199 |
| 374 |
| 426 |
| 458 |
| 780 |
| 1020 |
| 1045 |
| 1181 |

Eight rows total. All eight were reviewed and confirmed P1-admitted with their
headline text traceable to a citing passage in at least one other corpus
article's body.

## Disposition: accept-as-cited

The disposition for all 8 rids above is **accept-as-cited**:

- No standalone article/study page will be archived for these 8 rows.
- Their headline content remains preserved via the citing article(s) that
  already reference them in-body — this is treated as sufficient provenance
  and preservation for archive purposes.
- These rows remain in the master with their existing P1-admitted status;
  no master CSV edit is made as part of this documentation (per the
  overnight batch guardrails, no `_master_*.csv` file is touched by this
  action — this file is a documentation-only record of a disposition
  decision that was already made prior to this session).
- Future ingestion passes should treat these 8 rids as **closed** —
  they do not need re-review or re-attempted standalone archiving unless
  Pete explicitly reopens the question.

## Rationale

Archiving a standalone article for content that is already fully captured
as an in-body citation elsewhere in the corpus would create redundant,
near-duplicate records without adding retrievable information. The
accept-as-cited disposition keeps the corpus lean while preserving full
traceability: anyone searching for the headline content will still find it,
just via the citing article rather than a dedicated page.

## Scope note

This document is a record of disposition only. It does not itself change
any master CSV, DuckDB view, or wiki page. If Pete later decides any of
these 8 rids warrant a standalone page after all, that is a separate,
explicitly-authorized action — not implied or triggered by this file.

---

**Maintained by:** Pete Kastner + Perplexity Computer.
**Related:** `CANONICAL_IDS.md` (ID conventions), `_decisions_log.md` (disposition history).
