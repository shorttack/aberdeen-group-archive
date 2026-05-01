# Changelog

All notable changes to the Aberdeen Group Research Archive are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] — 2026-05-01

First tagged release. The archive is now feature-complete for its initial
charter: 822 studies spanning 1979–2026, fully audited at three layers, with
employer-scoped organization for Peter S. Kastner's career corpus.

### Added (release prep — May 1, 2026)
- `LICENSE` — CC-BY-4.0 for structured artifacts; original source content
  remains property of respective rights holders.
- `CITATION.cff` — academic citation file (CFF 1.2.0).
- `CHANGELOG.md` — this file.
- `_archive/` — historical container for superseded files; contains
  `ARCHIVAL_SKILL-11.md`, `ARCHIVAL_SKILL-12.md`, `ARCHIVAL_SKILL-13.md`
  (predecessors of `_skills/archival-ingest/SKILL.md` v18).

### Changed (release prep — May 1, 2026)
- `README.md` — full rewrite reflecting current 822-study state, employer-
  scoped layout, prescience distribution, Aberdeen Category Creator roster,
  pandas + DuckDB quickstart, and three-layer audit overview
  (commit `a7731ed`).
- `_MASTER_INDEX.md` — Summary block refreshed to current totals
  (822 studies / 14,742 observations / 7,834 entity rows / 6,269 tech rows
  / 3,198 unique entities / 4,054 unique technologies / 1,087 quote rows).
  Historical Archive 1–7 tables retained for provenance.
- `_checkpoint.json` — refreshed from batch-0 numbers (14 / 689) to current
  v1.0 state with per-collection and per-employer breakdowns.
- `_skills/archival-ingest/SKILL.md` — updated from v17 to v18 (commit
  `e6ecd41`); adds DCT collection type, `.xls`/`.xlsx` ingestion support,
  canonical retailer + PCmaker entity_id tables.

### Fixed (deferred-work cleanup — April 25, 2026, commit `b9a1012`)
- Layer-B alt-schema remediation across 10 legacy studies converted from
  pre-v18 schemas to canonical 9-column entities/technologies CSVs:
  `cacustsell98-3b53c6`, `docucorp-3c562a`,
  `kastner-ie-v-andersen-expert-report-3de98a`,
  `safeway-damages-report-draft-b502f4`,
  `aberdeen-1995-digital-linkworks`, `aberdeen-1995-digital-objectbroker`,
  `aberdeen-1995-ibm-as400-sap-r3`, `aberdeen-1995-ibm-db2-common-server`,
  `aberdeen-1995-intersolv-virtual-data-warehouse`,
  `aberdeen-1995-limd-technology`. IDs slugified, observations rewritten,
  non-canonical columns merged into `notes` as `key=value` pairs.
- Entity dedup: `aberdeen-group-inc` → `aberdeen-group` (218 obs rewrites);
  `dana-gardner-yankee` → `dana-gardner`;
  `analyst-fletcher-chris` → `christopher-fletcher`.
- `assembler.py` `validate()` now tolerates missing `codes.csv`
  (`_load_csv` returns `[]` for missing files; `validate()` skips
  `codes.csv` checks when absent and reports missing required CSVs as
  soft errors). New md5: `69b08b8b84fa6d204724f5842ef57585`.

### Audit status
Layer A (per-study referential integrity), Layer B (CSV write validation
gate), and Layer C (cross-study cache integrity): **0 failures across 680
audited studies**.

---

## Unreleased history (working batches, prior to v1.0 tag)

The dataset was built up through a sequence of ingestion batches. Each batch
was committed independently; this section summarizes them in chronological
order. Commit hashes link the change to the git log.

### Batch 8 — Kastner @ Arthur D. Little + PHI Computer Services (commit `5460363`, 2026-04-25)
5 new studies under two new employer subdirectories:
- `arthur-d-little/` (1972–1979): public-safety 9-1-1 / CAD systems;
  commercial engagements; ASE/ASEP two-way power-line communications
- `phi-computer-services/` (1969–1972 + 1995): PSD brochure + Kastner
  engagements; Wang Labs *Riding the Runaway Horse* retrospective.

### Aberdeen content batches 4–7 + Tim Minahan kudos (commits `bebf5d1`, `97bc6de`, `90dd215`, `d07eba7`, `8fdfe87`, 2026-04-25)
Aberdeen corporate collateral: AAS launch package + 2001 corporate collateral;
AAS operational playbooks + sales tools; workshop qualifying questions + 2001
success stories + proposal templates + Kastner retainer strategy deck;
practice definitions compendium (Jan 2000) + productization / pricing /
survey research program (2000–2001). Tim Minahan added to the Category
Creator roster (Supply Chain Management / e-Procurement / e-Sourcing).

### Mixed batches 1–3 + Stratus + Photos (commits `017a61a`, `3c057a6`, `65eae0c`, `a9412c7`, 2026-04-25)
Mixed: UIT15P Kastner-at-CA, PSA Category Created, Linuxcare, Oracle Apps
World, Sarbanes-Oxley Pt 2, Intel 64-bit Tipping Point + Hofferberth/Fletcher
category-creation credits. Aberdeen Twelve Vital Hours Sessions + Unisys-
Florida HRS expert witness memoir. Stratus Computer employer batch (11
studies + 18 Kastner quotes). Photo batch (10 Kastner artifacts: DubTech
1996, Bill Gates, Jimmy Carter, CA Sport Fisher, Kate Polaroid, DEC
brochure, podium keynote, 1989 Unix quote, PSK-10 collection).

### codes.csv schema migration + ref-int audit + masters rebuild (commits `8e9078b`, `9bcce50`, `102a39d`, 2026-04-25)
70 studies normalized to canonical v18 codes.csv schema. v18 referential-
integrity audit auto-fixes drove failures from 2,194 → 30. Master CSVs
rebuilt post-remediation.

### Prescience Phase 3 (commit `85b1a56`, 2026-04-25)
All 230 deferred-review quotes resolved. Final prescience distribution:
high=394, medium=250, low=67, not-applicable=110.

### Batches 19–26 (commits `3d908a4`, `df85d1b`, `4d409cf`, `888e0d6`, `7e42be3`, `960f18d`, `6c92fc6`, `ffbaf68`, 2026-04-24/25)
~80 studies covering early Aberdeen press (1982–2002); Kastner Stratus-era
items; DEC/CA/Compaq/Citrix/Apple coverage; DEC TP debit-credit corpus +
Aberdeen DOPS/decision-support; Stratus 1981 launch + HP MFASC'92 + Aberdeen
Land O'Lakes/NCR-OLTP + USA Today Pentium-FDIV/Itanium; Korean + Norway
translations of Aberdeen Open OLTP, NCR/AT&T WSJ ad, NCR 3000 cabinet,
Oracle/AT&T-NCR 1993 seminar tour; pre-Aberdeen Stratus 1987-CW + NCR
System 3000/TopEND brochures + AT&T WorldMark 1995 WSJ ad + 2002 WSJ
McWilliams private-label PCs + Charlotte Observer back-to-school +
Oracle-NCR Pittsburgh seminar letter; Stratus-era corpus (9 other-authors
+ 1 kastner-author); final batch 26 (+11 studies).

### Identity / attribution corrections (commits `5c15928`, `1ec7c75`, 2026-04-24)
- PKRS attribution corrected: Rick Saia (not Russ Craig).
- JRL identity corrected: John R. Logan (Aberdeen co-founder/chairman),
  not John R. Lewis.

### Batches 13–18 + Phase 3 backfills (commits `cc02f6d`, `9742065`, `6f11fd4`, `0425e65`, `198aadd`, `de5f770`, `4aa4ec4`, `aef721b`, 2026-04-21/24)
~60 webarchive / PDF / transcript studies including BusinessWeek/Grow 2005
rebate primary source, Macworld/eWEEK/Computerworld/Transmeta block, USA
Today/InformationWeek/InternetNews/NewsFactor/Vitria/Warranty Week,
Washington Times Chrome OS / SARS / Rebate / Windows 2000 / WebEx /
Centrino / ITV / Google Profile / YouTube vPro, plus Phase 3 deferred-
web-verification backfill across the corpus.

### Webarchive batches (commits `599964c`, `6145c74`, `44b32c7`, `f54c50b`, `e2b4a60`, `618c685`, `68765a6`, `09e7b13`, `a09b76b`, `80709e0`, `fd0dd23`, `9a26c81`, 2026-04-20/21)
Twelve batches (~100 studies) of Kastner press / vendor / blog / mixed-topic
webarchives, including IIARF PDF, rebates / SARS / Gateway / Sabre /
Salesforce / WDI / MA-Chamber speech, letters S–T, Technology-News-Hardware.

### Pre-v18 historical activity (April 10–19, 2026)
Earlier batches established Archives 1–7 (33 studies in Archives 1–4, plus
25 new in Archives 5–7), the v16 three-phase pipeline (AI extraction →
scripted assembly → deferred web verification), bundled assembler module,
entity reuse cache, incremental web verification cache, and the Kastner
quotation corpus (`kastner_quotes_clean.csv`). See `_MASTER_INDEX.md`
"Changelog" section for the full historical narrative preserved from
that period.

---

## [0.x] — March 13, 2026 (initial commit)

Original archive: 14 Aberdeen Group studies (1995–1996), 689 observations,
184 unique entities, 271 unique technologies, 0 validation errors. Captured
in `_checkpoint.json` prior to the v1.0 refresh; this state is the seed of
the project.
