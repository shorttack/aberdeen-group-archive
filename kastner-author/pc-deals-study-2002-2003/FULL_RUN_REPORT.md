# expand-pc-deals — Full Run Report

**Date:** 2026-06-27
**Prepared for:** Peter S. Kastner
**Scope:** 50 PC Deals DCT studies re-extracted (model-grade reading), `-mx` parallel set

---

## What ran

The DCT directory holds 76 studies. Subtracting the 3 smoke-test studies leaves
73. Of those, **23 are practice/admin/marketing/memoir docs** (PITAS template,
supplier list, webinar announcements, DCEIT practice docs, company snapshots,
memoirs) — not PC Deals price tracking — and were **skipped** per your call. The
remaining **50** PC Deals studies (weeklies + business-pc-deals editions +
processor/business price series + notebook/lineup + shipments/replacement
market) were re-extracted.

Five extraction agents ran in parallel, each the model-grade extraction brain
reading the faithful B-side source text between `## Original Document Text` and
`## Frictionless Data Package Metadata`. archival-ingest v20 supplied only the
packaging skeleton.

---

## Headline result

**The faithful read produces FEWER but real observations** — because the A-side
was heavily padded with truncated fragments. This is the loss-mode fix working
exactly as designed.

| Metric | A-side | B-side |
|---|---|---|
| Total observation rows | 1,014 | **725** |
| — of which junk (frag + placeholder + phantom) | **299** | **0** |
| — real content | 715 | **725** |
| FK links (entity + tech) | 911 | **1,113** |
| L1 front-sliced fragments | 288 | **0** |
| L3 placeholders / boilerplate | 8 | **0** |
| L6 phantom actual-outcome rows | 3 | **0** |

The B-side has **slightly more faithful observations than the A-side had real
ones** (725 vs 715), with every fragment, placeholder, and phantom removed, and
**+202 foreign-key links** densifying the relational graph.

---

## Why the count dropped (worked example)

`dct-weekly-2003-01-12`: A-side **23 rows → B-side 10**. The A-side's 23 included:

- **8 truncated fragments** (rows 8-15), all mislabeled "Price point highlighted",
  each a sentence sliced mid-word: "bout low-to-mid-range PCs...", "aq are the
  brands...", "hines out for under $750...", "g, CD-ROM upgrades...". These are
  window-sliced duplicates of the clean rows 1-7.
- **2 fragment forecasts** ("will be paying than the same configuration...")
  miscast as `viability-prediction`.
- **2 phantom `actual-outcome` rows** — generic boilerplate ("Jan 2003 pricing
  pattern visible in PC Deals corpus...") that assert nothing.

The B-side's 10 rows are the correct faithful reading: 7 retailer buying-tip
facts + 3 grounded technology/positioning assessments, all complete and
attributed. **The drop is the repair.**

Conversely, the dense-table studies the A-side *under*-extracted went **up**:
fujitsu-notebook-lineup 8→18, amd-athlon-weekly-prices 12→20,
cmp-pc-replacement-survey 4→10, corp-notebooks-jan-2003 11→15.

---

## Quality gate

All 50 studies pass the v20 CSV Validation Gate — **0 failures**:

- Column counts correct (studies 16, entities 9, technologies 9, observations 12)
- All controlled-vocabulary fields valid (license, importance, relevance,
  prescience, confidence)
- `csv.QUOTE_ALL` enforced on every write
- obs_id format `{study_id}-mx-OBS-{NNN}`, no duplicates
- Full foreign-key integrity — every entity_id and tech_id resolves
  (2 mis-columned rows caught and fixed during extraction: a `compaq` and a
  `sony` that had landed in `tech_id`)
- Frictionless `datapackage.json` + `codes.csv` generated per study

Corpus totals: **725 observations, 442 entity rows, 242 technology rows** across
50 studies.

---

## Combined with the smoke test

| | Studies | B-side obs |
|---|---|---|
| Smoke test (3) | 3 | 291 |
| Full run (50) | 50 | 725 |
| **PC Deals total** | **53** | **1,016** |

53 of the 76 DCT studies are now re-extracted under expand-pc-deals. The 23
non-PC-Deals docs remain on the A-side untouched.

---

## What stays on your Mac (deliverable boundary)

- Masters merge (versioned/suffixed — old and `-mx` rows coexist for live A:B)
- Pass C prescience scoring + roll-up
- Wiki rebuild + re-embedding
- Report rewrite (A-side vs. B-side)

All 50 `-mx` packages + this report are staged on the Mac at
`/tmp/expand_pc_deals_full/` for a one-line move into
`~/Desktop/Archive/Perplexity_Only/` once the workspace handshake is back.
