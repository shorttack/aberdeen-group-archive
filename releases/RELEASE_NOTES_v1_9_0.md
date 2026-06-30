# v1.9.0 — Substrate silent-loss recovery + CompChem exemplar ingest

**Released:** 2026-06-22
**Predecessor:** v1.7.0 (2026-06-18) — Multi-Horizon Prescience: row_class discipline + cloud parse-fail retag
**Archive HEAD at release:** `a02c23f1` (`shorttack/aberdeen-group-archive`)
**Wiki HEAD at release:** `97355369` (`shorttack/kastner-aberdeen-wiki`)

This release rolls together two distinct workstreams completed since v1.7.0:

1. **v1.8.0 substrate work** (2026-06-19): silent-loss recovery into `kastner_quotes_clean.csv`, plus a substrate-cap finding that closes the cheap recovery work on `pdf_format_mismatch` rows.
2. **CompChem exemplar ingest** (2026-06-22): first ingest into the new `project_examples/` top-level directory — Charles T. Casale's 1989 *Conflicting Trends In Computational Chemistry*, the first Aberdeen full-length market research report.

The v1.8.0 work was never independently tagged; this release consolidates it with the CompChem landing.

---

## Highlights

- **Quotations corpus expanded +121 rows** (1087 → 1208) via R1 medium-confidence headline-probe silent-loss recovery, all reviewed by Pete in Numbers using the canonical reject-column contract.
- **Pipeline 1 / Pipeline 2 / total** post-apply: 464 / 744 / 1208 (partition math GREEN).
- **Article corpus** grew from 105 to 179 articles (60 RTF + 119 PDF; +74 net-new PDF articles surfaced from previously-unclaimed segments).
- **Substrate-cap finding**: 410 of 437 residual `pdf_format_mismatch` rows (93.8%) are source-document gaps, not code gaps — Pipeline 1 effective ceiling ~470-480 rows; remainder requires a separate source-PDF scouting workstream.
- **Reject-column semantics** locked as canonical for all v1.8.0+ Numbers-review workflows: any non-whitespace character = reject; blank/None/whitespace = admit.
- **CompChem exemplar** lands in new `project_examples/` directory: 1 study, 24 entities, 10 technologies, 64 observations, 31 codes, 165 extracted figures.

---

## v1.8.0 substrate work (2026-06-19 session)

### Silent-loss recovery (shipped)

- `scripts/discover_unindexed_kastner_quotes_v2.py` (`4316f9d8`) — single-rule R1 headline-probe discovery, 24-column output (reject + 18 canonical + 5 provenance).
- Dry-run surfaced 125 candidates; Pete's Numbers review yielded 121 admit / 4 reject.
- `scripts/apply_unindexed_quotes_v3.py --commit` (`67d88731`) — admitted 121 rows to `kastner_quotes_clean.csv`, csv.QUOTE_ALL write, row-parity verified, timestamped backup written.
- `scripts/union_article_corpus_v1.py` re-run produced the +89 Pipeline 1 / +32 Pipeline 2 split.

### F4 substrate-cap finding (the residual 437 `pdf_format_mismatch` rows)

`scripts/diagnose_pdf_format_mismatch_v4.py` (`28b9239c`) classified every row across 7 failure modes:

| Bucket | Count | Pct | Disposition |
|---|---:|---:|---|
| F4 `not_in_pdf` | 278 | 63.6% | **Terminal** — PDF doesn't contain the article |
| F0b `headline_also_not_in_pdf` | 132 | 30.2% | **Terminal** — PDF doesn't contain the article |
| F0a `headline_in_unclaimed_norm_gap` | 17 | 3.9% | **Salvageable** (fuzzy-match) |
| F6 `detector_saw_different_title` | 7 | 1.6% | **Pete-review** |
| F3 `headline_in_body_detector_missed` | 2 | 0.5% | **Salvageable** |
| F1 `detector_grabbed_midsentence` | 1 | 0.2% | **Salvageable** |
| **Total** | **437** | 100% | 410 terminal + 20 salvageable + 7 Pete-review |

**Conclusion**: 93.8% terminal means further code work against the substrate is dead end. The 410-row remainder is deferred to a future source-document scouting workstream (Wayback Machine, third-party archives, publication libraries). Cheap recovery is done.

### Canonical rule established

**Reject-column semantics** (Pete, verbatim): *"Add a reject column. Any non-space or null character in that row means reject."*

```python
reject_raw = row.get("reject") or ""
is_rejected = bool(reject_raw.strip())  # any non-whitespace = reject
```

Numbers coerces empty cells inconsistently across saves; this contract makes the admit semantic robust. Applies to all future v1.8.0+ Numbers-review CSV apply scripts.

### Lessons reinforced

- **Gotcha 9 (producer/consumer schema drift)** bit again — v1 diagnostic read `partition_reason` but the union script writes `pipeline_route_reason`. Grep the producer's actual write call before authoring any consumer that reads it. ~45 minutes of debugging would have been avoided by 5 minutes of grep.
- Multi-edit batches with long blocks still fail silently in the sandbox `edit` tool; use single edits or 2-3 small edits per call.

---

## CompChem exemplar ingest (2026-06-22 session)

First study landed in the new `project_examples/` top-level directory:

`project_examples/conflicting-trends-computational-chemistry-fe5c31/`

**Author:** Charles T. Casale (Aberdeen Group co-founder)
**Title:** *Conflicting Trends In Computational Chemistry*
**Date:** Researched 1988, published January 1989 (cover of recovered copy reads May 1989 — likely reprint; canonical date `1989-01`)
**Significance:** First Aberdeen Group full-length market research report. One of very few recovered. Exemplar of the firm's founding methodology.

### Package contents (175 files in one commit)

| Component | Detail |
|---|---|
| `studies.csv` | 1 row (importance `high`, relevance `medium`, prescience `[DEFERRED]`) |
| `entities.csv` | 24 rows — Aberdeen principals (Casale, Kastner, Logan), Aberdeen Group, 7 software vendors (BioDesign, BIOSYM, Chemical Design, MDL, Polygen, QCPE, Tripos), 13 hardware vendors (Alliant, Apollo, Ardent, Convex, Cray, DEC, E&S, FPS, IBM, Multiflow, SGI, Star, Stellar) |
| `technologies.csv` | 10 rows — computational chemistry domain, molecular modeling, quantum chemistry codes, minisupercomputer, supercomputer, graphics workstation, supermini, mainframe, IBM PC RT, array processor |
| `observations.csv` | 64 rows — 1988 market sizing ($237M total, $27M software, $210M hardware), Aberdeen's CAD/CAM-vs-FEA scenario call (FEA-like), cyclic computing momentum thesis, IBM "sleeper" prediction, DEC dominance baseline (80% of installations 1983-87), per-vendor revenues + customer counts, three-line conflict framework, Spoke-Node-Ring topology |
| `codes.csv` | 31 rows (auto-generated) |
| `datapackage.json` | Frictionless descriptor |
| `schema/schema_org.json` | Google Dataset Search-compatible |
| `README.md` | Human-readable guide |
| `scripts/demo_analysis.py` | Runnable template |
| `source/original_text.md` | Raw OCR'd text + CSV metadata appendix |
| `images/` | **165 embedded figures** extracted via PyMuPDF |

### Notable observations captured

- 1988 worldwide computational chemistry market: **$237M combined** (software $27M, hardware $210M); software up 65% YoY.
- Hardware market shares: workstations 41.4%, minisupers 25.6%, superminis 16.7%, supers 7.1%, mainframes 4.0%.
- ~2,000 active practitioners worldwide across ~350 sites.
- Aberdeen's billion-dollar threshold prediction: 1993.
- **Pivotal scenario call**: CAD/CAM-like (single-digit billions) vs FEA-like (double-digit millions, protracted losses then high profits) — Aberdeen bets closer to FEA pattern.
- **IBM "sleeper" thesis**: gearing up for a lengthy assault on technical markets, with explicit execution-risk hedge ("distinct risk that IBM will not stay the course").
- **Cyclic momentum thesis**: refused to call one winning platform; predicted year-to-year revenue mix variation of 15-40% per segment with 10+ pp swings around 35% average growth.
- **Vendor-level financials**: Multiflow $15M / $42M VC across 3 rounds; Stellar $12.7M / $48M VC; MDL $25M / 1,100 PC customers; etc.

### Source PDF

Original PDF (168 pages, 8.5 MB, ABBYY FineReader OCR) committed to private repo `shorttack/kastner-restricted-sources` at `aberdeen-1989/CompChem.pdf` (commit `33a52bf3`).

### Pre-flight verification (archival-ingest v20)

- All 5 CSV validation gate checks PASS (plain-text, column-count, enum, QUOTE_ALL, abstract sanity).
- All assembler validations PASS (24 entities resolve, 10 technologies resolve, 64 observations have valid FKs).
- Phase 2 derivative regeneration successful (codes.csv, datapackage.json, schema_org.json, README.md, original_text.md, demo_analysis.py).
- Reuse cache updated: 24 entities + 10 technologies added.

---

## Commits in this release

### `shorttack/aberdeen-group-archive`

- v1.8.0 substrate work (silent-loss + F4 diagnostic): `64f67364`, `4316f9d8`, `f39b4298`, `67d88731`, `a87607d2`, `4bad6c6d`, `edf4864d`, `28b9239c`
- Mac MCP Bridge architecture docs (deferred build): `976bc833`
- **CompChem exemplar (this session)**: `a02c23f1` — 175 files in one tree commit

### `shorttack/kastner-restricted-sources` (private)

- CompChem source PDF: `33a52bf3`

### `shorttack/kastner-aberdeen-wiki`

- HEAD at `97355369` (Friday quotations corpus). No wiki regen in this release — `kastner_quotes_clean.csv` apply happened on Pete's Mac and will sync at EOD; CompChem study lives in `project_examples/` (outside the master CSVs), so wiki regen is not required.

---

## Carry-forward

- **A-step format-mismatch review** (27-row review CSV — 17 F0a + 7 F6 + 2 F3 + 1 F1): queued. Expected Pipeline 1 ceiling post-A-step: ~480 rows.
- **Mac MCP Bridge Phase 0 scaffolding**: docs landed in v1.8.0 prep; build deferred per WORKLIST §22.
- **Source-PDF scouting** (410 terminal pdf_format_mismatch rows): deferred future workstream — Wayback Machine, third-party archives, publication libraries.

---

_Owner: Pete Kastner. Release notes drafted by sandbox agent 2026-06-22._
