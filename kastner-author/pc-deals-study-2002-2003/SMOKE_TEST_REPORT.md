# expand-pc-deals — Smoke Test Report

**Date:** 2026-06-27
**Prepared for:** Peter S. Kastner
**Scope:** 3-study proof run before committing to the full ~44-study re-ingest

---

## The premise, in one sentence

A year of LLM progress means re-reading the same DCT studies with a far better
model recovers facts, structure, and reasoning that the original scripted
ingest silently dropped — so we are re-paying the ingest cost to buy back
fidelity, not just schema-compliance.

The extraction brain this time is the agent (model-grade reading). The
archival-ingest v20 skill contributes only the packaging skeleton: the 5-CSV
schema, `datapackage.json`, the directory layout, and the obs_id format. New
rows are written with a `-mx` suffix so they sit **parallel** to the originals
for live A:B comparison in DuckDB — nothing is overwritten.

---

## What was tested

| Study (`-mx`) | Source | A-side obs | B-side obs |
|---|---|---|---|
| dct-weekly-2003-06-08-mx | June 8 Update.doc (155 lines) | 25 | 25 |
| dct-weekly-2002-12-01-mx | Dec 1 Update.doc (107 lines) | 15 | 17 |
| dct-access-pc-deals-2002-2003-mx | access PC Deals.xls (2,154 rows) | 122 | 249 |
| **Total** | | **162** | **291** |

Two weekly commentary docs (the prose loss modes) and one large aggregate
spreadsheet (the over-aggregation loss mode) — chosen to exercise every defect
class at once.

---

## Headline result

**Observations: 162 → 291 (+80%).** Every known loss mode went to zero, and the
relational graph got dramatically denser.

| Defect (loss mode) | A-side | B-side |
|---|---|---|
| Truncated window-fragments (L1) | 14 | **0** |
| Placeholder / quota-padding rows (L3) | 3 | **0** |
| Phantom technology rows (L5) | 1 | **0** |
| Type-miscast forecasts (L6) | 1 | **0** |
| Lossy over-aggregation (L7) | 122 monthly averages | **249 per-SKU journeys** |
| Low-confidence filler | 3 | **0** |

**Foreign-key links (entity + tech): 144 → 549 (+405).** Every Access price
journey now carries a real PCmaker entity_id *and* a real CPU tech_id; the old
aggregation had only 105 entity links and 14 tech links across the whole set.

---

## Three things the old ingest lost that the re-read recovered

1. **Reasoning, not just data.** The Compaq Presario S4000 suffix taxonomy —
   NX = retail, T = Intel P4 Hyper-Threading custom, Z = AMD Athlon custom,
   V/J = lower-end variants — was captured as 5 discrete topic-insight rows,
   along with the line-proliferation rationale (HT vs. non-HT split). This was
   *entirely absent* A-side; the scripted ingest saw a price table and missed
   the analysis.

2. **A fabricated fact, corrected.** The A-side carried a phantom
   "Intel Pentium 4-M (Mobile)" technology row that does not appear in the
   source. It was removed and replaced with the real Pentium M the document
   actually discusses.

3. **Hygiene the aggregation masked.** VPR Matrix house-brand variants
   (Best Buy / VPR / vprMatrix) collapsed to one canonical entity, and source
   CPU typos (Althon, Penitum, "2800 +") were normalized for tech_id matching
   while the raw strings stay preserved inside each journey value.

---

## Per-SKU journeys (the L7 fix)

The Access rebuild replaced 122 monthly averages with **249 per-SKU price
journeys**. Each journey records first/last/min/max price, the price delta over
the tracking window, the channels it appeared in, and its CPU — turning a
flattened monthly roll-up back into a per-product price history.

This is an **intentional departure** from archival-ingest v20 §13.6 rule #1
("for aggregate files of 2,000+ rows, always aggregate"), made per your option-1
decision. Full row-level source data remains preserved. This departure is the
core of the L7 fix and is codified in the new skill.

---

## Quality gate

All three studies pass the v20 CSV Validation Gate:

- Column counts correct — studies 16, entities 9, technologies 9, observations 12
- All controlled-vocabulary fields valid (license, importance, relevance, prescience, confidence)
- `csv.QUOTE_ALL` enforced on every write
- obs_id format `{study_id}-OBS-{NNN}`, no duplicates
- Full foreign-key integrity — every entity_id and tech_id resolves
  (2 mis-columned rows in the Dec 1 study were caught and fixed)
- Frictionless `datapackage.json` + `codes.csv` generated per study

---

## What stays on your Mac (deliverable boundary)

My output ends at validated CSVs + the A:B comparison. These remain your
well-proven local jobs, to keep credit cost down:

- Masters merge (versioned/suffixed — old and `-mx` rows coexist)
- Pass C prescience scoring
- Wiki rebuild + re-embedding
- Report rewrite (A-side vs. B-side)

---

## The ask

**Go / no-go on the remaining ~41 studies?** Same workflow: extract → validate →
A:B, `-mx` suffix kept parallel. On GO, I save the `expand-pc-deals` skill to
your library (drafted and validating clean) and proceed through the batch.

Two open decisions:

1. **Skill name** — you asked for `expand_pc_deals`, but skill names disallow
   underscores. The drafted skill is `expand-pc-deals` (hyphens). OK to keep?
2. **Archive backup location** — the Mac-side workspace is currently unset, so
   writes to `~/Desktop/Archive/Perplexity_Only/` are blocked. Either set the pc
   workspace to `~/Desktop/Archive` (or a parent), or I stage to `/tmp` on the
   Mac for you to move with one command.
