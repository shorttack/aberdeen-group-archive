# Kastner Collection — Master Index

**Release:** v1.0.0 — May 1, 2026  
**Skill:** v19 (archival-ingest)  
**Last full-corpus refresh:** 2026-05-21 (post DEC longitudinal package)  
**Audit status:** Layer A / B / C — **0 / 0 / 0 failures** across 680 audited studies

## Summary

| Metric | Count |
|---|---|
| Total studies (Frictionless Data Packages) | **950** |
| Total observations | **19,773** |
| Master entity rows | **9,510** |
| Master technology rows | **7,853** |
| Unique entities (deduped cache) | **3,298** |
| Unique technologies (deduped cache) | **4,388** |
| Kastner quotations (`kastner_quotes_clean.csv`) | **1,087 rows across 676 canonical seqs** (max `article_seq=678`) |
| Date range | 1979 – 2026 |
| Web verifications | Complete (v16 → v19) |

**Per-collection breakdown**

| Collection | Studies | Observations |
|---|---:|---:|
| `kastner-author/` (top-level) | 205 | n/a |
| `kastner-author/dct/` | 76 | n/a |
| `kastner-author/employer/aberdeen-group/` | 29 | 609 |
| `kastner-author/employer/stratus-computer/` | 11 | 66 |
| `kastner-author/employer/DEC/` | 5 | 153 |
| `kastner-author/employer/arthur-d-little/` | 3 | 71 |
| `kastner-author/employer/phi-computer-services/` | 2 | 59 |
| `kastner-author/employer/obian-group/` | 1 | 5 |
| **kastner-author total** | **347** | **7,210** |
| **other-authors total** | **475** | **7,532** |
| **Archive total** | **950** | **19,773** |

**Prescience distribution** (across all 950 studies)

| Rating | Studies |
|---|---:|
| high | 475 |
| medium | 276 |
| low | 72 |
| not-applicable | 126 |
| (deferred) | 0 |

**Authoritative sources**
- `_master_studies.csv` — one row per study package
- `_master_entities.csv` — per-study entity rows across all studies
- `_master_technologies.csv` — per-study technology rows across all studies
- `_master_observations.csv` — all observations pooled
- `_known_entities.csv` / `_known_technologies.csv` — repo-root deduplicated caches
- `_collection_stats.csv` — per-study counts and ratings
- `kastner-author/quotations/kastner_quotes_clean.csv` — Kastner press / media quotation corpus (13 cols, §16 CSV gate enforced)

> The historical Archive 1–7 tables and changelog entries below are **preserved
> for provenance**. Their per-study counts and totals reflect the state of the
> archive at earlier points in time (April 10–19, 2026 and earlier). For the
> current authoritative state, use the figures above and the `_master_*.csv`
> files.

## Archive 1 — Kastner Research (11 studies)

| # | Study ID | Type | Date | Obs |
|---|---|---|---|---|
| 1 | `1996-electronic-commerce-25d31b` | white-paper | 1996 | 18 |
| 2 | `2001-hp-compaq-kastner-insight1-d6dc38` | expert-report | 2001-09-06 | 18 |
| 3 | `2004-05dell-storage-profile-editpk-05170-3c00b1` | case-analysis | 2004-05 | 20 |
| 4 | `2010-intel-ia-continuum-wp-1-2-fc5653` | white-paper | 2010 | 28 |
| 5 | `amd-profile01-64e43b` | white-paper | 2002-02 | 17 |
| 6 | `auditor-report-4-43ad9b` | benchmark | 2004-04 | 21 |
| 7 | `computerworld-ilm-article-15f604` | expert-report | 2004-07-29 | 16 |
| 8 | `copy-of-hp-camera-lab-journal-prod-c103f6` | case-analysis | 2001-12-05 | 16 |
| 9 | `dct-oct.-4-hot-topic-b61c0d` | topic-analysis | 2003-10 | 17 |
| 10 | `dell-ars-white-paper-prod-7-11m-c60434` | white-paper | 2003-07 | 21 |
| 11 | `dell-sd2-final-d6e78c` | white-paper | 2003-2004 | 15 |

## Archive 2 — Kastner Research (9 studies)

| # | Study ID | Type | Date | Obs |
|---|---|---|---|---|
| 12 | `desktop-virtualization-roi---aberdeen-8fa168` | benchmark | 2011-09 | 28 |
| 13 | `goremote-profile-5-2a-8fa814` | market-study | 2003-09 | 25 |
| 14 | `hp-can-boost-soa-offerings-with-acquisit-48e07e` | market-study | 2006-07-31 | 23 |
| 15 | `hp-compaq-kastner-insight1-a5a4e0` | expert-report | 2001-09-06 | 20 |
| 16 | `ibm-+-webify-=-industry-soa-application--97733a` | market-study | 2006-08-03 | 16 |
| 17 | `iha-full-report---draft-jul-28-41de81` | market-study | 2003-07-28 | 30 |
| 18 | `intel-2010-vpro-daily-globe-42697e` | expert-report | 2010-02-04 | 23 |
| 19 | `intel-centrino-pk-8ecf9a` | expert-report | 2003-03-01 | 20 |
| 20 | `intel-consumer-lt-10-5-03-580af7` | expert-report | 2003-10-05 | 22 |

## Archive 3 — Kastner Research (10 studies)

| # | Study ID | Type | Date | Obs |
|---|---|---|---|---|
| 21 | `intel-ia2004-pk4-kc-edits-de9c37` | white-paper | 2003-07 | 25 |
| 22 | `intel-infiband-wp--edit-psk-5-22f-a2c551` | white-paper | 2002-05 | 22 |
| 23 | `intelitaniummfewp1[1]-773ea2` | white-paper | 2004-03 | 36 |
| 24 | `ma-unisyswipro-rs-3747-36dd33` | market-study | 2006-12-18 | 17 |
| 25 | `mirror-image-profile-v2-(050404)-e7eb95` | case-analysis | 2004-05 | 20 |
| 26 | `oracleroiwhitepaperprod-7023c3` | white-paper | 2001-06 | 23 |
| 27 | `outsourcing-application-development-and--59d651` | benchmark | 2006-11 | 35 |
| 28 | `perspective-041304-e4be4c` | topic-analysis | 2004-04-13 | 20 |
| 29 | `sars2-hot-topic-cf91d4` | topic-analysis | 2003-04 | 25 |
| 30 | `snap-appliances-snapshot-10-15pk-f183fe` | case-analysis | 2003 | 21 |

## Archive 4 — Kastner Research (3 studies)

| # | Study ID | Type | Date | Obs |
|---|---|---|---|---|
| 31 | `technology-themes-ee5ba4` | topic-analysis | 2003-2004 | 21 |
| 32 | `the-business-value-in-it-outsourcing-7d5f23` | white-paper | 2006-05-25 | 18 |
| 33 | `webex--taking-conferencing-to-the-busine-5b8109` | case-analysis | 2002-04 | 22 |

## Archive 5 — Kastner Mixed (11 studies)

Includes memoirs, benchmarks, white papers, and one personality profile. Spans 1994–2025.

| # | Study ID | Type | Date | Obs |
|---|---|---|---|---|
| 34 | `dubtech-1996-29d4f9` | memoir | 1996-03-23 | 8 |
| 35 | `ft-mitfor~1-a56a9d` | white-paper | 1995-10 | 25 |
| 36 | `ibm-rs6000-midran~1-88f049` | benchmark | 1995 | 32 |
| 37 | `management-skills-learned-1969-3e75d0` | memoir | 2025-01 | 20 |
| 38 | `psk-misc-speech-agendas-5965a3` | white-paper | 1996-06 | 16 |
| 39 | `psk-personality-profile-2000-8be0a6` | memoir | 2001-07-17 | 25 |
| 40 | `rdbms-for-ibm-powera~1-7a44be` | benchmark | 1996-01-23 | 46 |
| 41 | `sequent-592620` | market-study | 1994 | 31 |
| 42 | `sequent-sap-sequen~1-7f70e4` | benchmark | 1996 | 16 |
| 43 | `software-market-safegu~1-ea7453` | white-paper | 1995 | 31 |
| 44 | `translating-early-skills-and-experiences-15bb2d` | memoir | 2025-01 | 17 |

## Archive 6 — Casale Research (6 studies, other-authors/)

Research by Aberdeen co-founder Charles T. Casale. Executive Vice President columns from 1983 and one AI-generated biographical profile.

| # | Study ID | Type | Date | Obs |
|---|---|---|---|---|
| 45 | `casale-evp-2-79187c` | market-study | 1983-01-04 | 15 |
| 46 | `casale-evp-3-b2b933` | market-study | 1983-01-05 | 18 |
| 47 | `casale-evp-4-9bd4e6` | market-study | 1983-01-06 | 25 |
| 48 | `casale-evp-5-aa8f2a` | market-study | 1983-01-07 | 21 |
| 49 | `casale-evp-7-215359` | market-study | 1983-04-05 | 21 |
| 50 | `charles-t-casale-influence-cdfb3f` | ai-response | 2024-12-03 | 20 |

## Archive 7 — NTI Video Report Workbooks (8 studies, kastner-author/)

Co-authored by Peter Kastner, John Logan, and Thomas Willmott for NTI (Network Technology International), 1993. Market studies based on video report workbooks covering open systems, PCs, operating systems, development tools, RDBMS, mainframes, midrange servers, and client-server computing.

| # | Study ID | Type | Date | Obs |
|---|---|---|---|---|
| 51 | `nti-2-open-systems-1dd3af` | market-study | 1993-01 | 29 |
| 52 | `nti-3-pc-and-ws-1993-17d49b` | market-study | 1993-02 | 29 |
| 53 | `nti-4-nextgen-os-timing-1993-a45049` | market-study | 1993-02 | 30 |
| 54 | `nti-5-development-toolsets-0e71c5` | market-study | 1993-04 | 30 |
| 55 | `nti-6-rdbms-technology-48f4aa` | market-study | 1993-04 | 30 |
| 56 | `nti-9-mainframe-role-1993-77fc40` | market-study | 1993-05 | 29 |
| 57 | `nti-11-distributed-midrange-servers-1993-dedd19` | market-study | 1993-08 | 30 |
| 58 | `nti-12-client-server-goals-1993-15a519` | market-study | 1993-07 | 30 |

## Prescience Highlights — Kastner Quotations Corpus

Standout forward-looking calls from the `kastner-author/quotations/` corpus (`kastner_quotes_clean.csv`). These are quotes where Kastner publicly predicted a specific technology outcome years before it occurred.

| Row | Seq | Date | Publication | Prediction | Validated |
|---|---|---|---|---|---|
| 383 | 423 | 2003-10-24 | CIOUpdate (Allen Bernard) | IBM Project eLiza / "computing on demand" autonomic system management as the driver behind IBM's 10,000-hire push — framed autonomic computing as the strategic pivot for heterogeneous enterprise IT management | Autonomic/self-managing systems became foundational to cloud operations (AWS auto-scaling, Kubernetes self-healing, AIOps) |
| 840 | 489 | 2003-11-17 | CNN/Money (Paul R. La Monica) | Video iPod as Microsoft Portable Media Center creates market pressure | Video iPod launched October 2005 — ~2 years out |
| 841 | 489 | 2003-11-17 | CNN/Money (Paul R. La Monica) | "Transforming the iPod into a smartphone…a new product category, where industry standards have not been set" | iPhone announced January 2007, shipped June 2007 — 3 years and 5 months before launch |

All three quotes carry `prescience_score=[DEFERRED]` pending formal Phase 3 rating but are flagged here as the highest-signal forecasts in the quotations corpus to date.

## Notes

- `Dell_SD2_FINAL.pdf` in Archive-4 is a duplicate of Archive-1 — skipped
- `Enterprise Integration webinar.ppt` in Archive-2 — unsupported format, skipped
- `hp-compaq-kastner-insight1` appears in Archives 1 and 2 from different source files
- `AAPL1990.doc` — confirmed duplicate of existing study, skipped
- `1992-TPC-benchmarks-OLTP.docx` — confirmed duplicate of existing study, skipped
- Archive 5 contained one non-Kastner-authored study (`psk-personality-profile-2000-8be0a6`, a 16PF assessment) — retained in kastner-author/ as it is about Kastner
- Archive 6 (Casale) studies filed under `other-authors/` per user direction
- Archive 7 (NTI) dates are 1993, not 1990-91 as initially estimated by user — confirmed from document content

---

## Changelog

### April 19, 2026 — Run 1+2 Backfill (5 prescience-score rows + 6 seq-196 [REVIEW] headline replacements)

**Scope:** Targeted backfill of 11 rows flagged during post-Batch-27 corpus scan. No new rows; only in-place field edits. CSV row count unchanged at 1069.

- **Run 1 — full analytical scoring for 5 empty-prescience rows** (row_ids 415, 441, 450, 455, 467). All five rows had populated `kastner_quotation` and `immediate_context` but empty `is_predictive` / `prescience_score` / `prescience_rationale` / `forecast_horizon_years` from earlier ingestion passes. Scored based on quote content and post-hoc outcome verification:
  - **row 415 seq 450** (Electronic News / Ry Crozier / 2003-11-14, 'Australia Ponders the Future of WiFi and 3G') — 'urban WiFi crash of 2004' prediction, aligned with newly-captured seq 670 Sutherland 5-row series. Scored `is_predictive=yes`, `prescience_score=medium`, `forecast_horizon_years=1-3`. Rationale: directionally correct on 2.4 GHz saturation but mitigated by 802.11g/n + 5 GHz dual-band + controller-based RF management, not a public 'crash' event.
  - **row 441 seq 471** (InternetNews.com / Michael Hickins / 2006-05-01, 'Can Caspio Penetrate the Enterprise On Demand?') — Caspio Bridge ease-of-use quip. Scored `is_predictive=no`, `prescience_score=not-applicable`, `forecast_horizon_years=0`.
  - **row 450 seq 482** (CNN/Money / Eric Hellweg / 2003-05-21, 'Tech Investor: Deflation, the dropping dollar, and tech') — Moore's Law / tech-deflation thesis. Scored `is_predictive=yes`, `prescience_score=high`, `forecast_horizon_years=5-10`. Rationale: compute/storage/bandwidth unit-cost declines continued with rising tech revenue and margins.
  - **row 455 seq 485** (Seattle Times / Kim Peterson / 2003-11-18, 'Comdex 2003: Sun Microsystems sets new, aggressive strategy') — Sun Opteron diversification necessary for customer retention. Scored `is_predictive=yes`, `prescience_score=high`, `forecast_horizon_years=5`. Rationale: AMD-based Sun Fire x64 helped hold accounts mid-2000s but broader SPARC/Solaris decline culminated in 2010 Oracle acquisition.
  - **row 467 seq 494** (NYT / Howard Millman / 2003-04-17, 'Customers Tire of Excuses for Rebates That Never Arrive') — 'tawdry strategy' characterization. Scored `is_predictive=no`, `prescience_score=not-applicable`, `forecast_horizon_years=0`.
- **Run 2 — [REVIEW] replacement for 6 seq-196 rows** (row_ids 480, 481, 484, 485, 486, 487). Rows previously had `headline`, `publication`, and `author` populated as `[REVIEW]` placeholders, while `is_predictive` / `prescience_score` / `prescience_rationale` / `forecast_horizon_years` were already filled from earlier passes. Source identification completed for three article groups:
  - **rows 480, 481 — Dell diversification into consumer electronics.** Content (Dell Inc. renaming reference, TVs/MP3 players focus, Kastner EVP/CRO Aberdeen Group title) matches [New York Times 2003-09-26 'Dell Decides to Diversify Into Consumer Electronics' by Barnaby J. Feder](https://www.nytimes.com/2003/09/26/business/technology-dell-decides-to-diversify-into-consumer-electronics.html). CSV date 2003-08-01 predates NYT publication — date discrepancy retained. Set `headline='Dell Decides to Diversify Into Consumer Electronics [UNVERIFIED]'`, `publication='The New York Times [UNVERIFIED]'`, `author='Barnaby J. Feder [UNVERIFIED]'`.
  - **rows 484, 485, 486 — Dell asset-recovery program with Tod Arbogast.** [ProQuest Austin Business Journal article by Stacey Higginbotham 'Dell seeks more money from computer castoffs' (April 2003)](https://www.proquest.com/trade-journals/dell-seeks-more-money-computer-castoffs/docview/218361401/se-2) confirmed NOT the Kastner-quoting source. Original Computerworld article could not be pinned in 3-4 targeted searches. Best-available attribution retained: `headline='Dell Pushes Asset-Recovery Program for Corporate IT [UNVERIFIED]'`, `publication='Computerworld [UNVERIFIED]'`, `author='[UNVERIFIED]'`.
  - **row 487 — Dell modular/blade-server strategy.** Related coverage at [InfoWorld 2003-02-28 'Dell packs full blade performance into half the space'](https://www.infoworld.com/article/2226437/dell-packs-full-blade-performance-into-half-the-space.html) is a product review without the Kastner 'flexibility and agility' quote. Exact source not confirmed. Set `headline="Dell's Modular Server Strategy and the PowerEdge 1655MC [UNVERIFIED]"`, `publication='Computerworld [UNVERIFIED]'`, `author='[UNVERIFIED]'`.
- CSV: **1069 rows, 13 cols** (unchanged); max `article_seq=671`, max row_id=1069. All 11 touched rows pass v17 validation gate (plain-text / 13-col / enum / QUOTE_ALL / content integrity). Zero `[REVIEW]` placeholders remain in `headline` / `publication` / `author` fields across the corpus.
- **Backup**: `kastner_quotes_clean.csv.bak_run1and2` created pre-edit.

### April 19, 2026 — Carry-Forward Cleanup (seq 181 headline normalization + row 708 headline cleanup)

**Scope:** Addresses two explicit carry-forward flags documented in prior batches. No new rows; only in-place field edits. CSV row count unchanged at 1069.

- **Fix 1 — seq 181 headline & date normalization (3 rows: row_ids 345, 346, 347).** Flagged for review at the close of Batch 27 after F9 (Janal Kalis blog repost) indicated the MIT Technology Review / David H. Freedman / Feb 2004 article is canonically titled 'Gadgets in the Superchip Age', not 'The Incredible Shrinking Gadget' as previously recorded. Verified against the live MIT Technology Review archive at `technologyreview.com/2004/02/01/101770/gadgets-in-the-superchip-age/`, which confirms canonical title **'Gadgets in the Superchip Age'** and canonical publication date **2004-02-01** (not 2004-01-30). The article contains all three Kastner quotes previously captured: cellphone multi-frequency architecture, 'drive a new cycle of cell-phone buying', and 'HAL from 2001 but a lot closer'. Applied in-place edits to all 3 rows: `headline` → 'Gadgets in the Superchip Age', `date` → '2004-02-01'. All other fields (publication, author, quotations, contexts, prescience ratings) unchanged.
- **Fix 2 — row 708 headline cleanup (seq 361 final remnant).** Row 708 was left in place at the close of Batch 26 as the single unresolvable rump of the seq-361 mis-blob (empty `kastner_quotation`, `immediate_context`, and all downstream analytical fields; no quote content available to reassign to a source article). The row previously displayed the bogus mis-blob fragment headline 'book w/AMD Processor, 2GB Memory, 160GB Hard Drive (Model # EME627) - $198.00 * [Wal-'. Headline normalized to **'[EMPTY-REMNANT seq-361 mis-blob]'** to reflect its true status as a permanent empty-content remnant. All analytical fields remain empty; `article_seq` remains 361; `publication` remains 'Kastner Blog'; `author` remains 'Peter S. Kastner'; `content_type` remains 'blog-post'. No change to row count or row_id continuity.
- CSV: **1069 rows, 13 cols** (unchanged); max `article_seq=671`, max row_id=1069. All touched rows pass QUOTE_ALL / 13-col / content_type / is_predictive / prescience_score enum validation. Empty is_predictive/prescience on row 708 is permitted for this specific empty-content remnant (documented permanent exception).
- **Corpus closure status:** With this carry-forward pass, the two standing flags from Batch 26-27 are resolved. The seq-361 mis-blob cleanup arc is now fully closed — 35 rows reassigned to canonical seqs across Batches 23-26, and the sole remaining rump (row 708) is now correctly labeled as an empty-content remnant rather than carrying misleading orphan headline text.

### April 19, 2026 — Batch 27 Quotations Update (10 mixed Intel/Wi-Fi webarchives; 12 new rows across 5 canonical seqs 667-671)

**Scope:** 10 webarchives (mostly Intel-focused) — InternetNews Singer Intel Grantsdale 2004 / EnterpriseITPlanet Grantsdale sibling syndication (skip) / Network Computing Dunn Intel Prescott (CMP-sibling syndication of seq 666, skip) / Wi-Fi Planet Joyce Intel Centrino 2003 / Intelligent Enterprise Schwartz-Leon open-source databases 2004 / Washington Technology 1996 Internet-Networking (no Kastner, skip) / Wi-Fi Planet Sutherland Wi-Fi End Nigh 2003 / iTKO-Aberdeen webinar promo page (skip) / Janal Kalis blog repost of MIT Tech Review Freedman 2004 (duplicate of seq 181, skip) / Washington Times Kellner Jobs-health 2009 — spanning 2003-2009.

- **Appended rows (12 new, row_ids 1058-1069):**
  - **seq 667** (F1) InternetNews.com / Michael Singer / 2004-06-17 'Intel's Grantsdale: Kick the Tires First' — 1 row on 915/925 chipsets and integrated 3D graphics for low-end workstations.
  - **seq 668** (F4) Wi-Fi Planet / Erin Joyce / 2003-03-12 'Intel's New Wireless Platform: Centrino' — **4-row internal series** covering 'biggest announcement of the year' + 20-22%→30% notebook share forecast + road-warrior battery life + 'lighting a match' platform-branding thesis.
  - **seq 669** (F5) Intelligent Enterprise / Susana Schwartz & Mark Leon / 2004-05 — 1 row on open-source databases recommended for Java/Web apps, with Aberdeen market-sizing ($400M embedded / $150M mobile-desktop / $100M high-perf cache). First open-source-database row in the corpus.
  - **seq 670** (F7) Wi-Fi Planet / Ed Sutherland / 2003-11-04 'Is the Wi-Fi End Nigh?' — **5-row internal series** covering Aberdeen's 'Urban Wi-Fi Crash of 2004' report: Starbucks-latte interference scenario + 300k-400k APs/month shipment rate + 'end of the Wi-Fi world is imminent' + 3-channel 802.11b/g root cause + hardware-replacement-cycle requirement.
  - **seq 671** (F10) Washington Times / Mark Kellner / 2009-01-14 'Jobs health stirs tech world, and with reason' — 1 row. **First Facebook-sourced quote in the corpus** — Kastner's Facebook status on Jobs's medical leave ('watching Apple stock crater as poor Steve Jobs takes an LOA') as re-quoted by the Washington Times technology blogger.
- **Files skipped in Batch 27**: F2 (EnterpriseITPlanet same-author internet.com sibling syndication of F1 Singer/Grantsdale), F3 (Network Computing Dunn Prescott — CMP-sibling syndication of Batch-26 seq 666), F6 (Washington Technology 1996 Internet piece — zero Kastner mentions), F8 (iTKO webinar promotional landing page — no quote text, per Batch 4 gated-whitepaper precedent), F9 (Janal Kalis blog repost of MIT Tech Review Freedman 'Gadgets in the Superchip Age' — already captured at seq 181 rows 345-347 under 'The Incredible Shrinking Gadget').
- **5 new canonical seqs**: 667, 668, 669, 670, 671. With 2 internal multi-row series (seq 668 = 4 rows, seq 670 = 5 rows), 12 paragraph-level quotes distribute across 5 canonical article seqs.
- CSV now **1069 rows, 13 cols**; max `article_seq=671`, max row_id=1069. All Batch 27-scope rows pass QUOTE_ALL / 13-col / content_type / is_predictive / prescience_score enum validation.
- **Notable Batch 27 artifacts:**
  - First Facebook-sourced corpus entry (seq 671) — expands captured-medium range to include social-media attribution channels (classified as `blog-post` content-type consistent with Washington Times blog hosting context).
  - Aberdeen 'Urban Wi-Fi Crash of 2004' now documented across 2 independent publications (seq 621 Inc. magazine / Greenleaf + new seq 670 Wi-Fi Planet / Sutherland) with 6+ total quote rows — among the most thoroughly cross-published Aberdeen reports in the corpus.
  - Centrino launch corpus now spans 3 viewpoints: Kastner's own InformationWeek column (seq 121), third-party enthusiast press (new seq 668 Wi-Fi Planet), and third-party general press (seq 654 US News, reassigned from seq-361 mis-blob in Batch 25).
  - Headline-review candidate flagged for seq 181 — F9 suggests canonical MIT Technology Review print title may be 'Gadgets in the Superchip Age' rather than 'The Incredible Shrinking Gadget' as currently recorded. No edit made; flagged for future normalization pass.

### April 19, 2026 — Batch 26 Quotations Update (10 Intel webarchives; seq 361 mis-blob FINAL resolution — 35 of 36 rows)

**Scope:** 10 Intel-focused webarchives — InfoWorld Margulius Intel-competitor 2003 / InternetNews Marer WiMax 2004 / PC World hyperthreading P4 (IDG syndication, skip) / Computerworld AU hyperthreading P4 (IDG syndication, skip) / Computerworld Krazit hyperthreading P4 canonical 2002 / MarketWatch Kraeuter Intel Q1 2003 / NewsFactor Long Intel vPro SMB 2008 / InfoWorld Margulius Intel-turns-35 2003 / InformationWeek Dunn Intel Prescott P4 2004 / ZDNet UK Broersma Intel-Aberdeen-attack-AMD (adjacent coverage, skip) — spanning 2002-2008.

- **Seq 361 FINAL cleanup (16 rows, 692-707)** — Batch 26 resolves all remaining deferred rows of the seq-361 mis-blob, each previously mis-stamped to 'book w/AMD Processor... / Kastner Blog / no date':
  - **Row 692** worldwide semiconductor capacity fluctuations → F1 InfoWorld / David L. Margulius / 2003-07-18 'Intel or a competitor inside?'. **New seq 660.**
  - **Row 693** telcos disappointed since the Internet crash → F2 InternetNews.com / Eva Marer / 2004-01-22 'Intel Preps for WiMax Chips'. **New seq 661.**
  - **Rows 694, 695, 696** P4 3.06-GHz hyperthreading / MS Word spell-check / Photoshop-video multithreading → F5 Computerworld / Tom Krazit (IDG News Service) / 2002-10-28 'Intel readies hyperthreading Pentium 4'. **MERGED as new seq 662** (3-row internal merge).
  - **Row 697** economic picture looks increasingly clouded → F6 MarketWatch / Chris Kraeuter / 2003-04-15 'Intel shares gain on results, outlook'. **New seq 663.**
  - **Rows 698, 699, 700, 701, 702** Intel vPro outside-firewall + remote manageability + quad/dual-core + TCO $500/$1,000 per PC per year → F7 NewsFactor Network / Mark Long / 2008-09-23 'Intel Targets SMBs With Revamped vPro'. **MERGED as new seq 664** (5-row internal merge — corpus record).
  - **Row 703** 'number of speed bumps per year has decreased' → F8 InfoWorld / David L. Margulius / 2003-07-18 'Intel turns 35: Now what?'. **New seq 665.**
  - **Rows 704, 705, 706, 707** Intel Prescott P4 aggressive pricing + 300mm wafer advantage + '99.9% of consumer users don’t need 64-bit parts today' → F9 InformationWeek / Darrell Dunn / 2004-02-02 'Intel Unveils Next-Generation Pentium 4 Processors'. **MERGED as new seq 666** (4-row internal merge).
- **Zero new appended rows.** All quote content in this batch matches existing deferred mis-blob rows; no new source articles contribute additional Kastner material beyond what is being reassigned.
- **Files skipped in Batch 26**: F3 (PC World IDG-syndication of F5 Krazit piece), F4 (Computerworld Australia IDG-syndication of F5), F10 (ZDNet UK Broersma 2002-03-27 coverage of AMD-GHz Equivalency report — adjacent coverage of the same story captured at seq 659 in Batch 25; does not quote Kastner by name).
- **7 new canonical seqs**: 660-666. With 3 internal row merges (694=695=696, 698=699=700=701=702, 704=705=706=707), 16 source rows collapse to 7 canonical seqs.
- **Row 708 NOT reassigned** — this row has empty `kastner_quotation`, `immediate_context`, and all downstream analytical fields; cannot be reassigned without content to match against a source article. Left at seq 361 as a permanent empty-content remnant.
- CSV: **1057 rows, 13 cols** (unchanged row count); max `article_seq=666`, max row_id=1057. All Batch 26-scope rows pass QUOTE_ALL / 13-col / content_type / is_predictive / prescience_score enum validation.
- **Mis-blob tally (FINAL):** Seq 109 FULLY RESOLVED (Batches 19-22, 25 of 25 rows). **Seq 361 effectively FULLY RESOLVED** (Batches 23-26, 35 of 36 rows reassigned; row 708 is an empty-content remnant). Four older prior mis-blobs cleaned (seqs 196/194/104/106-partial). The corpus-wide mis-blob debt is now substantively cleared.

### April 19, 2026 — Batch 25 Quotations Update (Informix/Intel webarchives + 1 PDF; seq 361 mis-blob continued)

**Scope:** 9 webarchives + 1 PDF — InformationWeek TechSearch results page (skip) / InformationWeek Foley Informix Crafts / InformationWeek Foley Informix Meets Database Deadline / Computerworld Norway Osterud Informix / Intel/IBM DB2 9.7 Ascentium marketing PDF (skip) / ExtremeTech Catalina588/Kastner Stars ratings / US News Rae-Dupree Intel wireless / Electronic News Murphy Intel-Sun / DesignTechnica TechSpot AMD GHz Equivalency / CRN Clancy Intel Internet Leap — spanning 1994-2009.

- **Seq 361 cleanup continued (9 rows)** — Batch 25 resolves rows 683-691, all previously mis-stamped to 'book w/AMD Processor... / Kastner Blog / no date':
  - **Row 683** Informix "didn't think Informix would ever get this out of the lab" → F3 InformationWeek John Foley 1996-10-14 'Informix Meets Database Deadline'. **New seq 652.**
  - **Row 684** Informix "quite invisible in the market" → F4 Computerworld Norway / Margrete Osterud / 1994-11-13 'Informix på vei mot teten'. **New seq 653.**
  - **Rows 685, 686** Intel wireless bet / home broadband → F7 US News / Janet Rae-Dupree / 2003-05-12 'Intel bets big on making wireless'. **MERGED as new seq 654** (2-row internal merge).
  - **Rows 687, 688, 689, 690** Intel Itanium 2 performance / 'segmenting seven ways to Sunday' → F8 Electronic News / Tom Murphy / 2002-06-10 'Intel comes out swinging at Sun'. **MERGED as new seq 655** (4-row internal merge).
  - **Row 691** Intel Internet leap / Field-of-Dreams → F10 CRN / Heather Clancy / 1999-04-23 'Intel Initiates Big Internet Leap'. **New seq 656.**
- **New articles (3 appended rows, row_ids 1055-1057):**
  - **seq 657** (F2) InformationWeek / John Foley / 1996-11-18 'Informix Crafts Web Architecture' — Kastner on Informix's Universal Server web-integration strategy.
  - **seq 658** (F6) ExtremeTech forum / Catalina588 / Peter S. Kastner / 2009-04-10 — authored-column defending Intel's new Stars CPU ratings system as a clearer consumer metric than raw clock speed. Second known Kastner-authored column in the corpus (Catalina588 handle precedent).
  - **seq 659** (F9) DesignTechnica via TechSpot / 2002-03-28 'Analyst stands by AMD-bashing report' — Kastner's on-record defense of Aberdeen's controversial Intel-funded 'AMD Gigahertz Equivalency' report.
- **Files skipped in Batch 25**: F1 (InformationWeek TechSearch search-results listing page — not an article, 0 Kastner content), F5 (Intel/IBM DB2 9.7 Ascentium marketing PDF — 0 Kastner; quotes belong to Schiefer/Ellis/Vella/Laws).
- **Remaining seq 361 mis-blob: 17 rows still deferred** (692-708). Known topics: semiconductor capacity (692), telcos post-Internet-crash (693), Intel 3.06-GHz P4 (694), Word/Photoshop multithreading (695, 696), economic outlook (697), remote-worker/firewall security — GRIC theme (698, 699), Intel vPro quad/dual-core TCO (700-702), Intel chip speed-bumps (703-706), 64-bit consumer need (707), row 708.
- CSV now **1057 rows, 13 cols**; max `article_seq=659`. All Batch 25-scope rows pass QUOTE_ALL / 13-col / content_type / is_predictive / prescience_score enum validation.
- **Mis-blob tally (updated):** Seq 109 FULLY RESOLVED (Batches 19-22). **Seq 361: 19 of 36 rows resolved (Batches 23-25); 17 rows remain deferred.** Four older prior mis-blobs cleaned (seqs 196/194/104/106-partial).

### April 19, 2026 — Batch 24 Quotations Update (IBM/Itanium/64-bit webarchives; seq 361 mis-blob continued)

**Scope:** 10 webarchives — 2 ZDNet UK (Shankland Itanium reprints) / Computerworld Brewin IBM Wi-Fi printer / SearchCIO IBM-NT-Linux / InformationWeek IBM-MSFT NT clusters 1999 / CNET Shankland Itanium / PCWorld Brewin reprint / Wired IDC predictions 2002 / AMD.com Kastner authored 64-bit column / InformationWeek CA-Platinum 1999 — spanning 1999-2004.

- **Seq 361 cleanup continued (4 rows)** — Batch 24 resolves rows 679-682, all previously mis-stamped to 'book w/AMD Processor... / Kastner Blog / no date':
  - **Row 679** 'IBM had to have a strong Intel 32-bit and 64-bit product line...' → CNET News.com Stephen Shankland 2003-04-29 'IBM's Itanium Server Goes on Sale'. **MERGED into existing seq 142** (row 290 already captures the lead quote from this article).
  - **Row 680** 'IBM's Itanium support trails that of rival Hewlett-Packard, which is betting the company on Itanium' → same Shankland article, continuation quote. **MERGED into seq 142.**
  - **Row 681** 'Our research shows an increasing number of enterprise customers are not only embracing NT-based clustering...' → F5 InformationWeek Stuart J. Johnston 1999-05-21 'IBM, Microsoft Team On NT Clusters'. **New seq 646.**
  - **Row 682** 'CA hasn't been a major player in the data warehousing space...' → F10 InformationWeek Beth Davis 1999-07-19 'Next Computer Associates'. **New seq 647.**
- **New articles (4 appended rows, row_ids 1051-1054):**
  - **seq 648** (F2) ZDNet UK / 2003-04-30 — syndication of Shankland Itanium piece (distinct syndicated republishing of seq 142).
  - **seq 649** (F4) SearchCIO (TechTarget) / Kate Evans-Correia / 2004-02-11 'IBM, ISVs lure NT users with Linux' — Kastner skeptical of mass NT-to-Linux migration.
  - **seq 650** (F8) Wired News / Elisa Batista / 2002-12-23 'IDC: Tech Bucks, Hack Threats Up' — Kastner pegs IT spending growth at 3% vs IDC's 6%+ forecast.
  - **seq 651** (F9) AMD.com / Peter S. Kastner / 2003-09-23 'Industry Analyst Visionaries: 64-bit Computing' — authored-column format; extended first-person forecast of consumer 64-bit adoption through 2010.
- **Headline correction on seq 644 row 1049** (Batch 23 Brewin row): updated from 'IBM introduces "plug-and-print" wireless LAN adapter' to canonical 'IBM unveils Wi-Fi network printer adapter, dismisses Dell printer plans' (Computerworld articleId=79704 canonical title confirmed by F3 this batch).
- **Files skipped in Batch 24**: F1 (ZDNet UK print-version of F2 — same Shankland article), F3 (canonical Computerworld Brewin — already at seq 644 from Batch 23; this batch only used F3 to confirm canonical headline), F6 (CNET original — already at seq 142 row 290), F7 (PCWorld IDG-syndication of F3 Brewin piece).
- **Remaining seq 361 mis-blob: 26 rows still deferred** (683-708). Known topics: Informix (683, 684), field-of-dreams retail (685), home broadband/wireless (686), Itanium 2 performance vs Sun (687-691), semiconductor capacity (692), telco Internet-crash (693), 3-GHz P4 (694), Word/Photoshop multithreading (695, 696), economic outlook (697), remote-worker security (698, 699), Intel vPro (700-702), Intel chip speed-bumps (703-706), 64-bit consumer need (707), row 708.
- CSV now **1054 rows, 13 cols**; max `article_seq=651`. All Batch 24-scope rows pass QUOTE_ALL / 13-col / content_type / is_predictive / prescience_score enum validation.
- **Mis-blob tally (updated):** Seq 109 FULLY RESOLVED (Batches 19-22). **Seq 361: 10 of 36 rows resolved (Batches 23-24); 26 rows remain deferred.** Four older prior mis-blobs cleaned (seqs 196/194/104/106-partial).

### April 19, 2026 — Batch 23 Quotations Update (HP/IBM webarchives; seq 361 mis-blob partial resolution)

**Scope:** 10 webarchives — CNET Skulltrail (skip) / CRN HP Q1 / NetworkWorld HP-Compaq / CNN/Money HP consumer push / Advisor IBM-Linux / Computing IBM-Java / Wi-Fi Technology Forum IBM printer adapter / Onlypunjab TechNewsWorld IBM Power / 2 MarketWatch IBM Q2 2003 earnings — spanning 1996-2004. **Discovered a new mis-blob at seq 361** (36 rows with bogus 'book w/AMD Processor, 2GB Memory, 160GB Hard Drive' headline, pub='Kastner Blog', empty date). Six of the 36 seq-361 rows (673-678) map directly to Batch 23 source articles and are re-attributed.

- **Seq 361 partial cleanup (6 rows)** — Batch 23 resolves rows 673-678, previously mis-stamped to 'book w/AMD Processor... / Kastner Blog / no date':
  - **Row 673** 'I would expect [at the] end of October-November rolling out...' → F3 HP-Compaq chip away at to-do list (Deni Connor / 2002-08-19 / Network World). **New seq 637.**
  - **Row 674** 'Users need to understand...Linux operating system platform partners...' → F5 IBM and Linux: A Murky Future Ahead? (DataBased Advisor / 2003, date unverified, assigned 2003-01-01). **New seq 638.**
  - **Row 675** ''IBM has too many platforms. But it's on the right track.'' → F6 IBM embraces Java as key to platform compatibility (Newmedia / 1996-10-30 / Computing UK). **New seq 639.**
  - **Row 676** 'No one today considers designing a new product by designing the processor...' → F8 IBM Opens, Customizes Power Chips (TechNewsWorld via Onlypunjab / 2004-04-01). **New seq 640.**
  - **Row 677** 'There's technology that could make this work now...' → same F8 TechNewsWorld article, continuation quote. **New seq 641.**
  - **Row 678** 'It was a fairly sober report...no joy in Armonk...' → F9 IBM reports earnings, sales boost (Mike Tarsala / 2003-07-16 / MarketWatch). **New seq 642.**
- **New articles (3 appended rows, row_ids 1048-1050):**
  - **seq 643** (F2) CRN / Craig Zarley / 2003-02-25 'HP Turns A Profit On PCs' — includes toner-competition + rumored Dell-printer-entry quote (distinct CRN article from seq 633 Fordahl Feb 26 piece).
  - **seq 644** (F7) Computerworld / Bob Brewin / 2003-03-25 'IBM introduces "plug-and-print" wireless LAN adapter' — distinct Computerworld article from seq 196 (Tom Krazit / same day / Dell printer launch piece), same 'material player' Kastner quote syndicated from a single interview.
  - **seq 645** (F10) MarketWatch / Mike Tarsala / 2003-07-17 'IBM shares fall following Q2 earnings' — day-after follow-up on IBM Q2 2003 results; same Kastner 'sober report / no joy in Armonk' quote republished.
- **Files skipped in Batch 23**: F1 (CNET Skulltrail user review 2008 — 0 Kastner, same file as Batch 22 F3 skip), F4 (CNN/Money La Monica 2003-08-13 — already at row 448 seq 481).
- **Remaining seq 361 mis-blob: 30 rows still deferred** (679-708). Topics include Itanium, NT clustering, CA/Computer Associates, Informix, 3-GHz P4, Intel vPro, various analyst-commentary snippets. Future batches to resolve as matching source articles surface.
- CSV now **1050 rows, 13 cols**; max `article_seq=645`. All Batch 23-scope rows pass QUOTE_ALL / 13-col / content_type / is_predictive / prescience_score enum validation.
- **Mis-blob tally (updated):** Seq 109 FULLY RESOLVED (Batches 19-22). **Seq 361 NEW mis-blob identified — 6 of 36 rows resolved in Batch 23; 30 rows remain deferred.** Four older prior mis-blobs cleaned (seqs 196/194/104/106-partial).

### April 19, 2026 — Batch 22 Quotations Update (Mixed webarchives, seq 109 mis-blob FULLY RESOLVED)

**Scope:** 10 webarchives — High Tech Monday / High-tech depreciation / CNET / HON-Linux / FCW multimedia / HP price-cut / HP Forbes / HP Reinvented / HP Hurd / HP Revenue Shortfall — spanning 1996-2008. **Milestone: the seq-109 mis-blob (first identified in Batch 18) is now FULLY RESOLVED.** The final 4 deferred rows (237, 238, 239, 240) are re-attributed to their true source articles — all 25 originally mis-stamped rows have been reassigned across Batches 19-22 (6 + 5 + 10 + 4 = 25). Plus 3 genuinely new articles.

- **Seq 109 FINAL cleanup (4 rows)** — Batch 22 resolves rows 237-240, previously mis-stamped to "Will Microsoft Play Nice Now? / 2002-11-20 / Lisa Gill":
  - Row 237 "cut-and-dried applications / Linux comparatively inexpensive" → **seq 630**, HON Industries Furnished With Linux / Larry Barrett / 2002-11-01 / eWeek (F4).
  - Row 238 "11% price drop is believable" → **seq 631**, HP cuts prices on some Intel-based servers 11% to 31% / Todd R. Weiss / 2002-02-13 / Computerworld (F6). Date corrected (2002-11-20 → 2002-02-13).
  - Row 239 "careful of competing too closely with partners such as EDS" → **seq 632**, HP Reinvented / Beth Bacheldor & Martin J. Garvey / 2002-05-13 / InformationWeek (F8). Magazine feature (`magazine-article`).
  - Row 240 "third-party toner cartridges / Dell entering printer business" → **seq 633**, HP Shares Sink On Revenue Shortfall / Matthew Fordahl / 2003-02-26 / CRN (F10). Both clauses appear together in the F10 article (Dell-branded printers launched 3 weeks later, March 21, 2003 — Kastner’s "widely rumored" call validated within the quarter).
- **Seq 109 mis-blob FULLY RESOLVED** — all 25 originally mis-attributed rows (216-240) reassigned across Batches 19-22. Seq 109 now holds only its legitimate content (row 1033 from the true "Will Microsoft Play Nice Now?" article, added in Batch 19). The 5-batch cleanup arc that began in Batch 18 is now complete.
- **+3 net-new rows** (row_id 1045-1047):
  - **seq 634** (F1 High Tech Monday Update / PR Newswire / Dow Jones Newswires source / 2003-04-07) — "schedule slippages / major supply chain disruptions" SARS impact analysis (new syndication outlet for the Apr 2003 SARS coverage cluster at seqs 122-141; PR Newswire/Dow Jones attribution distinct from prior captures).
  - **seq 635** (F2 High-tech groups hoping for IT depreciation incentive / Patrick Thibodeau / 2003-01-06 / Computerworld) — "two-year window / delay purchases" depreciation-bonus paradox quote (distinct from the Jan 13, 2003 Thibodeau Computerworld piece at seq 117).
  - **seq 636** (F7 HP Expects 20% EPS Jump Next Year / Pinnacor staff / 2003-12-10 / Forbes.com) — "combine two low-profit segments / drive each other's sales" analyst-day reaction (same Kastner quote as row 335/seq 173 USA Today coverage of same HP analyst-day; Forbes.com recorded as distinct Pinnacor syndication outlet per prior-batch precedent).
- **Files skipped in Batch 22**: F3 (CNET user review of Intel i7-965, 2008 — 0 Kastner), F5 (FCW 1996 multimedia/RDBMS piece — 0 Kastner), F9 (eWeek HP-Hurd appointment 2005-03-29 — 0 Kastner on captured page).
- CSV now **1047 rows, 13 cols**; max `article_seq=636`. All Batch 22-scope rows pass QUOTE_ALL / 13-col / content_type / is_predictive / prescience_score enum validation.
- **Mis-blob tally (final):** Four prior mis-blobs cleaned (seqs 196/194/104/106-partial). **Seq 109 mis-blob FULLY RESOLVED** — 25 of 25 rows resolved across Batches 19-22. No new mis-blobs discovered in Batch 22. The corpus-wide mis-blob debt identified across Batches 14-18 is now fully cleared.

### April 19, 2026 — Batch 21 Quotations Update (Mixed webarchives, seq 109 MAJOR mis-blob resolution)

**Scope:** 10 webarchives (Gateway / H-P / Dell / CRN Fed rate / Wi-Fi) spanning 2001-2004 mainstream and trade press. **Largest single seq-109 cleanup to date**: 10 of the 14 remaining mis-attributed rows (227-236) resolved to their true source articles. Plus 3 new rows across 3 distinct articles, and a headline correction on an existing seq.

- **Seq 109 cleanup MAJOR (10 rows)** — Batch 21 resolves rows 227-236, previously mis-stamped to "Will Microsoft Play Nice Now? / 2002-11-20 / Lisa Gill":
  - Row 227 "re-create the PC miracle of the 1990s" → **seq 623**, Gateway gets in the digital camera picture / Rex Crum / 2003-08-28 / CBS MarketWatch (F1).
  - Row 228 "eMachines built a foundation at the big-box retailers" → **seq 624**, Gateway refines target with new PCs / Rex Crum / 2004-06-28 / CBS MarketWatch (F2).
  - Row 229 "Gateway is taking a disruptive approach with these two new wireless APs" → **seq 625**, Gateway Ends the WLAN Flim-Flam / Gateway press release / 2004-04-06 / FreshNews.com (F4).
  - Row 230 "long way to go" (singular) HP post-Compaq integration → **seq 626**, H-P plunges on Q1 revenue miss / Rex Crum / 2003-02-26 / CBS MarketWatch (F6).
  - Row 231 "long ways to go" (plural) HP cost-cutting earnings → **seq 627**, H-P profit rises 49% on cost cuts / Rex Crum / 2003-02-25 / CBS MarketWatch (F7).
  - Row 232 "Profits continue to outpace revenue growth... Dell is leading the industry" → **seq 628**, Hardware stocks eke out gain after Dell report / Rex Crum / 2003-08-15 / CBS MarketWatch (F8).
  - Rows 233-236 (Fed aggressive rate cutting / world markets adjust / Maybe says Kastner / broadband wide segment) → **seq 629**, Hi-Tech Execs: Fed Rate Cut Was a Necessary Move / CRN / 2001-09-17 (F10). Four rows resolve to the same source article, consistent with the original mis-blob pattern.
- **Row 234 content repair** — row 234 "It will take the world markets some days to adjust to last Tuesday's tragedies" was previously truncated; expanded to the full quote per F10 archive.
- **Headline correction on seq 193** — rows 365 and 366 (Washington Post Mike Musgrove Wi-Fi piece, 2004-04-25): headline corrected from "Working Without Wires" to **"Here, There, WiFi Anywhere"** per F9 archive. All other metadata unchanged.
- **+3 net-new rows** (row_id 1042-1044):
  - **seq 626** (F6 H-P plunges on Q1) — "third-party toner... the golden egg" quote on HP printer-supply revenue model.
  - **seq 627** (F7 H-P profit rises 49%) — same "golden egg" quote appearing in the syndicated Feb 25/26 earnings coverage.
  - **seq 628** (F8 Hardware stocks eke out gain) — "This is a very good quarter, again, for Dell" Kastner endorsement.
- **Files skipped in Batch 21**: F3 (Gateway-stocks-up — 0 Kastner mentions), F5 (SMH "Google rival" reprint of seq 446 ECT original), F9 (Here-There-WiFi-Anywhere — quotes already in seq 193; used only for headline confirmation).
- CSV now **1044 rows, 13 cols**; max `article_seq=629`. All Batch 21-scope rows pass QUOTE_ALL / 13-col / content_type / is_predictive / prescience_score enum validation.
- **Mis-blob tally (updated):** Four prior mis-blobs cleaned (seqs 196/194/104/106-partial). **Seq 109 now near-complete** — **21 of 25 rows resolved** across Batches 19-21 (6 + 5 + 10); **only 4 rows remain deferred** (rows 237-240 — Linux/NT, HP pricing, HP-EDS outsourcing, HP printer-toner/Dell-printer-entry). No new mis-blobs discovered in Batch 21.

### April 19, 2026 — Batch 20 Quotations Update (Mixed webarchives, seq 109 mis-blob resolution continued)

**Scope:** 10 webarchives spanning 1995-2004 mainstream and trade press. Primary impact: five more seq-109 mis-blob rows (222-226) resolved to their true source articles. Plus three genuinely new articles: a 1995 InformationWeek software-security piece, a 2003 Inc. staff blog on urban Wi-Fi congestion, and a 2004 Gateway Wireless DVD PR Newswire release.

- **Seq 109 cleanup continued (5 more rows)** — Batch 20 resolves rows 222-226, previously mis-stamped to "Will Microsoft Play Nice Now? / 2002-11-20 / Lisa Gill":
  - Row 222 "Cables and bulky tubes / move a TV" → **seq 615**, Flat-screen TV Unleashed / David LaGesse / 2004-04-12 / U.S. News & World Report (F2).
  - Row 223 "odds that WiMax gets off the ground" → **seq 616**, Wi-Fi Where You Want It / Christine Y. Chen / 2004-02-23 / Fortune (F3).
  - Row 224 "Linux 6 to 9 percent POS market" → **seq 617**, Fresh Ideas for POS / Hospitality Technology / 2004-03-01 (F4).
  - Row 225 "eMachines shelf space big boost" → **seq 618**, Gateway buys rival for $235m / Scott Morrison / 2004-01-30 / Financial Times (F7).
  - Row 226 "boxed in by Dell / H-P big-box" → **seq 619**, Gateway gains 15% on $235M eMachines deal / Rex Crum / 2004-01-30 / CBS MarketWatch (F10).
- **Remaining seq 109 mis-blob (deferred): rows 227-240** — 14 rows still cover Gateway continuation quotes, HP/Compaq earnings, Dell earnings, post-9/11 Fed rate cut / recovery piece, broadband policy, HP pricing, HP-EDS outsourcing, HP printer cartridges. No Batch 20 files cover these subjects.
- **+4 net-new rows** (row_id 1038-1041):
  - **seq 620** (F1 Finding The Key To Software Security / Edward Cone / 1995-10-02 / InformationWeek) — "[The key] is a pain in the neck, and everybody hates it" (highly prescient re: dongle-based software protection failing on UX grounds, ultimately displaced by online activation and SaaS).
  - **seq 621** (F6 Fresh Inc. staff blog / Clint Greenleaf / 2003-10-23 / Inc.) — two quotes: the "mobility benefits vs. inherent limitations" diagnosis and the "real solution is political" spectrum-policy call. Both highly prescient — validated by the 2014-2020 FCC U-NII and 6 GHz spectrum unlocks that enabled Wi-Fi 5/6/6E.
  - **seq 622** (F8 Gateway Debuts Wireless Connected DVD / PR Newswire / 2004-03-11) — rare first-person Kastner endorsement quote embedded in a vendor press release.
- **Files skipped in Batch 20**: F5 (In This Issue archive dup of F4), F9 (Worldwide Videotex / Gale Group aggregator dup of F8).
- CSV now **1041 rows, 13 cols**; max `article_seq=622`. All Batch 20-scope rows pass QUOTE_ALL / 13-col / content_type / is_predictive / prescience_score enum validation.
- **Mis-blob tally (updated):** Four prior mis-blobs cleaned (seqs 196/194/104/106-partial). **Seq 109 now further cleaned** — **11 of 25 rows resolved** (6 in Batch 19 + 5 in Batch 20); **14 rows still deferred** (rows 227-240). No new mis-blobs discovered in Batch 20.

### April 19, 2026 — Batch 19 Quotations Update (Mixed webarchives, seq 109 partial mis-blob resolution)

**Scope:** 10 webarchives mixing E-Commerce Times Special Reports (F1-F3), Telephony Online (F4), ECT News (F5), CDW Editorial (F6-F7), ExtremeTech (F8), Automotive Design & Production / BNET (F9-F10). Primary impact: the seq-109 mis-blob deferred from Batch 18 is partially resolved.

- **Seq 109 partial cleanup (6 of 25 rows)** — Batch 19 files pinpoint the true source articles for rows 216-221 previously mis-stamped to "Will Microsoft Play Nice Now? / 2002-11-20 / Lisa Gill":
  - Row 216 "negative ROI / 10-year program" → **seq 610**, Who Pays for Tech Innovation? / Lisa Gill / 2002-10-07 (F1).
  - Row 217 "applications in military / medical research / all fields of science" → **seq 611**, IBM Dominates Supercomputer List / Keith Regan / 2004-06-21 (F3). Content repaired (was a garbled article header).
  - Rows 218, 219 (relational-database-in-memory / 64-bit as the future) → **seq 612**, Processor Market Evolving / CDW Editorial / 2004-06 (F7).
  - Rows 220, 221 (fixed dollars/engineers / top-end workstation) → **seq 613**, Faster And Faster Go the Workstations / Larry Gould / 2003-07 / Automotive Design & Production (F10). Row 221 content expanded from fragment.
- **Seq 109 TRUE content recovered** — F2 is the article the seq-109 label was meant to reference. Row 1033 (new) captures the actual Kastner quote: "They never had a really strong case to begin with, particularly from the consumer's standpoint" — predicting limited antitrust-remedy outcomes for the non-settling states.
- **Remaining seq 109 mis-blob (deferred): rows 222-240** — 19 rows still span 10+ unidentified articles covering Sharp Aquos wireless TV, WiMax, Linux POS, eMachines/Gateway acquisition, HP post-Compaq earnings, Dell earnings, post-9/11 Fed rate cuts, broadband policy, HP pricing, HP outsourcing/EDS, HP printer cartridges. No Batch 19 files cover these subjects. Continues to await future source webarchives.
- **Minor date correction** — row 1020 (seq 604 / Microsoft Says No to Compromise): 2002-06-20 → 2002-06-21 per F5 archive.
- **5 new rows added** (rows 1033-1037) across 4 seqs:
  - seq 109 — F2 Will MS Play Nice / Lisa Gill / 2002-11-20: "strong case / political visibility" antitrust quote.
  - seq 612 — F7 CDW Processor Market: "darn good 32-bit server" (Opteron strategic win) and "two-way Itanium = four-way Xeon / database license" (per-socket licensing economics) — two new rows.
  - seq 613 — F10 Workstations: "three major trends" (mobile / high-end 32-bit / Itanium) framework.
  - seq 614 — F4 Telephony Online / Vincent Ryan / 2001-09-24 (new publication): "$30/hour for full-motion video" post-9/11 video-conferencing economics — highly prescient precursor to Zoom-era UCaaS.
- **Files skipped in Batch 19**: F6 (byte-identical duplicate of F7), F8 (ExtremeTech Windows Home Server, 0 Kastner mentions), F9 (BNET aggregator copy of F10).
- CSV now **1037 rows, 13 cols**; max `article_seq=614`. All Batch 19-scope rows pass QUOTE_ALL / 13-col / content_type / is_predictive / prescience_score enum validation.
- **Mis-blob tally (updated):** Four prior mis-blobs cleaned (seqs 196/194/104/106-partial). **Seq 109 now partially cleaned** — 6 of 25 rows resolved; 19 remain deferred. No new mis-blobs discovered in Batch 19.

### April 19, 2026 — Batch 18 Quotations Update (E-Commerce Times Special Reports 2001-2004)

**Scope:** 10 E-Commerce Times Special Reports webarchives covering Kastner commentary on IE security, Dell branding and build-to-order, lean 2002 e-commerce, future computers, Microsoft Passport, IT rebates, the future microchip marketplace, enterprise expansion, and interactive TV — by Elizabeth Millard, Bob Woods, Lou Hirsh, Teri Robinson, and Keith Regan.

- **Fourth mis-blob cleanup (seq 106 partial)** — rows 207 and 208 (`article_seq=106` / The Future Microchip Marketplace / 2002-10-03 / Teri Robinson) had quotes whose true origins were different articles. Row 207 ("impulse among vendors will be to grab business as a hedge") re-attributed to **seq 608**, What To Expect When You're Expanding - Again / Keith Regan / 2003-04-09 (File 9). Row 208 (broadband-makes-TV-unnecessary paraphrase) re-attributed to **seq 609**, Whatever Happened to Interactive TV? / Lou Hirsh / 2002-06-25 (File 10). Rows 202-206, 209, 210 remain correctly stamped to seq 106.
- **Row 214 content repair** — row 214 (previously seq 109 / Will Microsoft Play Nice Now?) carried a Brancheau quote that had been mis-attributed to Kastner since original ingest. Replaced with the correct Kastner ITV paraphrase from F10 ("The Aberdeen Group's Kastner added that ITV capabilities will have to be included with future television sets...") and re-stamped to seq 609.
- **Row 215 re-attribution** — row 215 (the "Right now, people are not going to [alter] their TVs" direct Kastner quote) re-attributed from seq 109 to seq 609 (F10, Whatever Happened to Interactive TV?).
- **Deferred: larger seq 109 mis-blob** — rows 216-240 in seq 109 span unrelated articles (64-bit/Itanium, IBM supercomputer list, Linux retail POS, eMachines/Gateway, HP/Compaq merger earnings, Dell earnings, Fed rate cuts, broadband rollout, HP printer cartridges). This is a 5th mis-blob, requiring a dedicated future cleanup pass. Out of Batch 18 scope; flagged for Batch 19+ follow-up.
- **7 new rows added** (rows 1026-1032) across 4 new seqs (605, 606, 607, 608) plus 1 existing seq (145, appended):
  - seq 605 — New IE Flaw Piles on Pressure for Microsoft Patch / Elizabeth Millard / 2004-01-31 (File 1): "functionality creeping through micro patch process" and "impossible to have it be perfect" quotes.
  - seq 606 — How Future Computers Will Change E-Commerce / Lou Hirsh / 2002-09-30 (File 5): "turtleneck sweaters" personalization quote.
  - seq 607 — Microsoft Passport: Like It or Not / Teri Robinson / 2002-06-25 (File 6): "bated breath" and "14 times" quotes on federated-identity demand.
  - seq 145 (append) — The Fine Print of IT Rebates / Elizabeth Millard / 2003-06-13 (File 7): "car dealers / sticker price" rebate-as-price-discrimination quote.
  - seq 608 — What To Expect When You're Expanding - Again / Keith Regan / 2003-04-09 (File 9): "stars align / pent-up demand" IT-spend recovery quote.
- CSV now **1032 rows, 13 cols**; max `article_seq=609`. All Batch 18-scope rows pass QUOTE_ALL / 13-col / content_type / is_predictive / prescience_score enum validation.
- **Mis-blob tally:** Four `article_seq` mis-blobs cleaned across Batches 14-18: seq 196 (Batch 14), seq 194 (Batch 16), seq 104 (Batch 17), seq 106 partial (Batch 18). One larger mis-blob (seq 109, rows 216-240) remains and is deferred to a future batch.

### April 19, 2026 — Batch 17 Quotations Update (E-Commerce Times Intel/MS/Dell 2002-2004)

**Scope:** 10 E-Commerce Times webarchives (Files 1-10) spanning Intel, Microsoft, Dell, and broadband regulation coverage 2002-2004 by Teri Robinson, Staff Writer, Helen Gallagher, Jennifer LeClaire, Elizabeth Millard, and Tiernan Ray.

- **seq-104 cleanup (third mis-blob discovered)** — rows 192-198 (`article_seq=104`) were mis-labeled to "HP Shares Rise After Merger / Teri Robinson / 2002-05-06." Rows 189, 190, 191 are genuinely that article (no change). Rows 192-198 re-attributed to 3 true source articles:
  - Rows 192-194 → **seq 600**, "Microsoft Judge Stakes Out Scope of Settlement" / Staff Writer / 2002-05-16 (File 2).
  - Row 195 → **seq 184** (merged into existing cluster), "Microsoft Patches IE Security Flaws" / Helen Gallagher / 2004-02-03 (File 3).
  - Rows 196-198 → **seq 601**, "New Broadband Legislation Revives Old Debate" / Jennifer LeClaire / 2002-05-03 (File 5). Row 197's empty quote populated with the true "regulated very carefully" direct quote.
- **seq-184 headline correction** — rows 352, 353, 354 headline "IE Fix Reflects Ongoing Security Battle" → "Microsoft Patches IE Security Flaws" (true headline from File 3 webarchive).
- **Row 280 mis-attribution fix (critical)** — row 280 (seq 137) had a quote by Gartner's Smith mis-attributed to Kastner ("You didn't need to wait for Win2003 to deploy .NET"). Replaced with the real Kastner quote from the same article: "brash youth / young adult phase" re Windows Server 2003 maturity.
- **Row 1019 correction** — the "ferocious" Intel chip-production quote added in Batch 16 (attributed to "Intel Abandons Web Hosting" / 2002-06-19) was actually first published in Batch 17 File 1 ("Intel Forecasts Dimmer Second Quarter" / Teri Robinson / 2002-06-07). Re-attributed to File 1 at **new seq 602**.
- **6 new rows added** (rows 1020-1025) across 2 new seqs (603, 604) plus 4 existing seqs (105, 137, 144, 601):
  - seq 604 — Microsoft Says No to Compromise / Teri Robinson / 2002-06-20 (File 4): "Windows chopped up / simply reaffirm" prediction about Kollar-Kotelly ruling.
  - seq 601 — Broadband Legislation (File 5): "strong have gotten stronger" (merges into the cleaned-up cluster).
  - seq 105 — Revised Dell Q2 Outlook (File 6): "good news for shareholders but does not signal an end" — Dell individual strength vs. broad PC-industry weakness.
  - seq 137 — Windows Server 2003 (File 8): "feel confident putting this in production" — enterprise-adoption endorsement.
  - seq 144 — Windows Updates (File 9): "Microsoft is getting a bum rap" — defense of aggressive patch cadence.
  - seq 603 — Microsoft Unhurt by MyDoom Attack / Elizabeth Millard / 2004-02-04 (File 10): "adept at being prepared for emergencies" quote.
- CSV now **1025 rows, 13 cols**; max `article_seq=604`. All Batch 17-scope rows pass QUOTE_ALL / 13-col / content_type / is_predictive / prescience_score enum validation.
- **Mis-blob tally:** Three `article_seq` mis-blobs have now been cleaned up across Batches 14-17: seq 196 (Batch 14), seq 194 (Batch 16), seq 104 (Batch 17). All three followed the same pattern — a cluster of 7-28 rows stamped with one headline while the quotes came from multiple distinct E-Commerce Times articles.

### April 19, 2026 — Batch 16 Quotations Update (E-Commerce Times 2002-2004)

**Scope:** 10 E-Commerce Times webarchives (Files 1-10), mostly Kastner market commentary for 2002-2004 E-Commerce Times pieces by Keith Regan, Elizabeth Millard, Teri Robinson, Tim McDonald, and Jennifer LeClaire.

- **seq-194 cleanup (second mis-blob discovered)** — rows 368-375 (`article_seq=194`) were all incorrectly stamped "US Aims for Fastest Supercomputer Title / Elizabeth Millard / 2004-05-13" but the actual quotes came from 5 different E-Commerce Times articles spanning 2002-2004. Structurally identical to the seq-196 mis-blob cleaned up in Batch 14. All 8 rows re-attributed to their true source articles; new seqs 592-596 assigned. Row 368's empty quote/prediction fields populated with the true "silent friends" quote from the MS-EU Ruling article.
- **seq-196 [REVIEW] remainder cleared** — row 494 (the last remaining `[REVIEW]` from Batch 14's seq-196 cleanup) re-attributed to its true source: Batch 16 File 1, "IBM Lands Navy Supercomputer Deal / Keith Regan / 2004-07-27" — the actual origin article of the entire seq-196 mis-blob. Moved to seq 591.
- **6 new rows added** (rows 1014-1019) across 6 seqs (591, 595, 596, 597, 598, 599):
  - seq 591 — IBM Lands Navy Supercomputer Deal / Keith Regan / 2004-07-27 (File 1): "That's no longer the case" price-competition quote.
  - seq 595 — Dell Posts Q2 Profit, Predicts Q3 Growth / Jennifer LeClaire / 2002-08-16 (File 6): "consistently make money and gain market share."
  - seq 596 — HP Posts Higher Profit on Weak Sales / Keith Regan / 2003-02-26 (File 8): "paring costs for only a finite period" prediction.
  - seq 597 — US Aims for Fastest Supercomputer Title / Elizabeth Millard / 2004-05-13 (File 2): "handy for military applications" — the ONE true Kastner quote from the article that seq 194 had been incorrectly scattering 8 rows across.
  - seq 598 — Hitachi, NEC Join To Challenge Cisco / Elizabeth Millard / 2004-06-25 (File 7): "Cisco understands routers… well in hand" prediction.
  - seq 599 — Intel Abandons Web Hosting Service / Teri Robinson / 2002-06-19 (File 10): Intel's "ferocious" chip-production rate quote.
- **File 9** (HP Shares Rise After Merger, Teri Robinson, 2002-05-06) → already correctly attributed in existing rows 189, 190 (seq 104). No new rows.
- CSV now **1019 rows, 13 cols**; max `article_seq=599`. All Batch 16-scope rows pass QUOTE_ALL / 13-col / content_type / is_predictive / prescience_score enum validation.
- **Pre-existing corpus note:** 160 rows across the broader corpus (predating Batch 16) still have empty `is_predictive` and `prescience_score` fields — a legacy data gap unrelated to Batch 16, flagged for a future corpus-wide backfill pass.

### April 19, 2026 — Batch 15 Quotations Update (Dell/Intel/Cisco 2003-2004)

- **9 new rows added** (rows 1005-1013) across seqs 585-590 plus 2 supplements to seq 121:
  - **seq 589** (3 rows) — Aberdeen Perspective PDF "Dell, Oracle & Linux: Your Next SAP Platform?" by Peter S. Kastner, 2004-04-28. Predicts Linux clusters on 2-4-way x86 would displace the ~10,000 Y2K-era RISC-Unix SAP installations; benchmarks a 2-node Dell 6650 cluster at 9-16% faster than 8-way RISC SMP for one-third the cost. (`authored-column`.)
  - **seq 590** (1 row) — Computerworld "Dell, Oracle tout alliance on enterprise server systems" by Patrick Thibodeau, 2003-04-02. Kastner on how the Dell+Oracle+Linux announcement legitimizes Linux "good enough to run two companies that are north of $10 billion dollars."
  - **seq 586** (1 new row + attribution fix) — CRN / VARBusiness "Don't Count Intel Out" by Carolyn A. April, 2003-06-02. Adds the direct "put a new pony into the race" quote. Row 489 (from seq-196 cleanup) moved into this seq with author upgraded from `[REVIEW]` to Carolyn A. April.
  - **seq 121** (2 supplemental rows) — InformationWeek / InternetWeek "Don't Panic! Intel's New Centrino..." by Peter S. Kastner, 2003-03-24. Adds the "most important introduction Intel will make in 2003 / Mark down March 12th" framing and the "Centrino notebooks — and the wireless network they work best in — should become one of the standard IT infrastructure building blocks" call.
  - **seq 588** (2 new rows + attribution fix) — E-Commerce Times "Cisco Readies Huge Fast Router" by Elizabeth Millard, 2004-05-24. Adds the "they have the situation well in hand" and the VoIP / developing-country Internet-growth drivers quotes. Rows 491, 492, 493 (from seq-196 cleanup) moved into this seq with author corrected to Elizabeth Millard and date to 2004-05-24 — the source-code-leak and CRS-1 passages are in fact a single article.

- **7 attribution corrections** applied to existing rows using Batch 15 primary sources as ground truth:
  - Row 476 (seq 196 → seq 156) — merged into existing MarketWatch Q2 cluster (row 309); date 2003-08-15 → 2003-08-14.
  - Rows 471, 488 (seq 196 → seq 585) — **re-attributed from Forbes.com to MarketWatch / Rex Crum, 2003-11-14, "Dell's shares ease in aftermath of Q3 earnings report".** The Forbes attribution in the seq-196 cleanup batch was incorrect; File 5 establishes MarketWatch as the true source.
  - Row 489 (seq 196 → seq 586) — author `[REVIEW]` → Carolyn A. April; publication refined to "CRN / VARBusiness"; headline standardized to "Don't Count Intel Out".
  - Row 490 (seq 196 → seq 587) — publication "E-Commerce Times [REVIEW]" → "E-Commerce Times"; author `[REVIEW]` → Lisa Gill; date 2003-01-01 → 2002-12-30; headline → "Report: Global Chip Sales Grow at Snail's Pace". `[REVIEW]` flag cleared.
  - Rows 491, 492 (seq 196 → seq 588) — author Keith Regan → Elizabeth Millard; date 2004-05-25 → 2004-05-24; headline → "Cisco Readies Huge Fast Router".
  - Row 493 (seq 196 → seq 588) — author `[REVIEW]` → Elizabeth Millard; date 2004-05-17 → 2004-05-24; consolidated with the HFR article.
- 2 files skipped as duplicate captures: File 3 (stripped Dell-Oracle Computerworld), File 6 (short-form Don't Count Intel Out).
- File 4 (MarketWatch Dell Q2) produced no new rows — its Kastner quote was already at row 309; used only to correct row 476's date and re-seq.
- CSV now **1013 rows, 13 cols**; max `article_seq=590`. All rows pass QUOTE_ALL / 13-col / enum validation.
- Remaining `[REVIEW]` flags in the corpus are now confined to seq-196 rows 480, 481, 484-487, 494 (Dell diversification / asset-recovery / modular-server / supercomputing passages whose source articles are still not in hand).

### April 19, 2026 — seq-196 Cleanup Batch

- **26 mis-labeled rows re-attributed.** Rows 462, 468, 471-494 (`article_seq=196`), previously all stamped "IBM Lands Navy Supercomputer Deal / E-Commerce Times / Keith Regan / 2004-07-27," split across their true 2003-2005 source articles via verbatim quote match against the Batch 14 webarchive extracts and corroborating web research:
  - Row 462 → TechNewsWorld, Jay Lyman, 2004-06-08, "AMD's Semprons Spare Athlon from Low-End Market"
  - Row 468 → Aberdeen Group report (Kastner), 2003-06-01, "Why You Need To Replace Those Windows 98 And NT Machines" (`authored-column`)
  - Rows 471, 488 → Forbes.com, Pinnacor / AFX News, 2003-11-14, "Dell 3Q Net Up 21%"
  - Rows 472-474 → ServerWatch, Clint Boulton, 2004-06-08, "Dell Debuts 64-bit Itanium Server"
  - Row 475 → PC World, Tom Krazit (IDG), 2002-08-15, "Dell Drops Windows From Some PCs"
  - Row 476 → MarketWatch, Rex Crum, 2003-08-15, "Dell buoyed by growth outlook"
  - Rows 477-479, 482, 483 → Computerworld, Tom Krazit (IDG), 2003-03-25, "Dell launches personal and workgroup printers"
  - Row 489 → CRN (Computer Reseller News), 2003-06-02, faster Xeon/Itanium chips piece
  - Rows 491, 492 → E-Commerce Times, Keith Regan, 2004-05-25, Cisco CRS-1 Huge Fast Router
  - Row 493 → E-Commerce Times, 2004-05-17, "Cisco Probes Potential Source Code Leak"
  - Rows 480, 481, 484-487, 490, 494 → publication/author fields flagged `[REVIEW]` with best-effort date and content_type; browser-based URL verification was cancelled per user instruction, so these are deferred to a future targeted pass.
- **Row count unchanged.** Edits in place (columns: date, headline, publication, author, content_type). `kastner_quotation`, `immediate_context`, `is_predictive`, and prescience fields preserved as-is.
- **Cleanup debt cleared.** `_skipped_sources.md` seq-196 debt entry replaced with this re-attribution table.
- CSV remains **1004 rows, 13 cols**, max `article_seq=584`. All rows pass QUOTE_ALL / 13-col / enum validation.

### April 19, 2026 — Batch 14 Quotations Update

- **NYT 1981 attribution fix** — rows 469 & 470 (`article_seq=196`) previously mis-labeled "IBM Lands Navy Supercomputer Deal / E-Commerce Times / Keith Regan / 2004-07-27" re-attributed to the correct source: *The New York Times*, 1981-03-20, "Defense Industry Gearing Up" by Pamela G. Hollie. Kastner quoted as "government market planner for Prime Computer Inc. of Natick, Mass." Row 470's broken Quote-1 fragment ("anufacturing is becoming increasingly important…") replaced with Quote 2 ("Weapons are more sophisticated…Missiles have to be smart enough to fly from here to Moscow at 100 feet above the ground without human intervention."). These are the earliest dated Kastner quotations now in the quotations corpus (Prime Computer era, 10 years before his Aberdeen co-founding).
- **2 new rows added** (rows 1003, 1004 / seqs 583, 584):
  - DC Velocity Feb 2003 "Soft growth seen for software" — Kastner Aberdeen newsletter excerpt forecasting 4% 2003 worldwide IT-spending growth with a prescient read on post-war/oil CEO caution.
  - Digital / NCI 1997-03-24 StrongARM Reference Design press release — Kastner quoted on the joint Digital-StrongARM + NCI NC Access platform for network computers.
- **Known cleanup debt** — `article_seq=196` still holds 28 rows mis-labeled to the same IBM/E-Commerce Times headline. Rows 469, 470 corrected in this batch; the other 26 rows (462, 468, 471-494) span ~7 distinct 2003-2005 source articles (Forbes Dell 3Q, ServerWatch Itanium, PC World Windows-drop, MarketWatch Dell growth, Computerworld Dell printers, asset-recovery/Cisco router passages) and are deferred to a dedicated cleanup batch.
- CSV now **1004 rows, 13 cols**; max `article_seq=584`. All rows pass QUOTE_ALL / 13-col / enum validation.

### April 10, 2026 — Archives 5, 6, 7 Added (25 new studies)

**Archive 5** (11 studies): Mixed Kastner collection including memoirs, IBM sales training benchmarks, white papers, and a personality profile. Notable items: RS/6000 RDBMS sales training deck (1995), Power Academy RDBMS competitive analysis (1996), two career memoirs (2025), and a 16PF psychometric assessment (2001).

**Archive 6** (6 studies, Casale): Charles T. Casale's Executive Vice President columns from Aberdeen Group's 1983 newsletter, covering minicomputer billings, corporate growth dynamics, hypergrowth P&Ls, balance sheets, and quarterly financial cycles. Plus one AI-generated biographical profile.

**Archive 7** (8 studies, NTI): Video report workbooks co-authored by Peter Kastner, John Logan, and Thomas Willmott for NTI in 1993. Covers the open systems transition, PC/workstation market, next-gen operating systems, development toolsets, RDBMS technology, mainframe role, distributed midrange servers, and client-server computing goals. These are historically valuable as comprehensive surveys of enterprise IT during the Unix/client-server transition era.

**Pipeline updates:**
- All 25 new studies processed with v16 three-phase pipeline
- Entity/technology reuse caches grew from 174 → 275 entities, 330 → 508 technologies
- Web verification completed for all new entities, technologies, and predictions
- All `[DEFERRED]` fields backfilled to zero across Archives 5–7

### April 10, 2026 — Skill v16 Reprocessing (Archives 1–4)

**Scope:** 33 studies across 4 archives (34 source files, 1 duplicate skipped, 1 unsupported format skipped)

**Pipeline changes (v16 vs. prior versions):**

| Feature | v14/v15 (prior) | v16 (current) |
|---|---|---|
| Architecture | Monolithic (v14) or partial scripting (v15) | Three-phase: AI extraction → scripted assembly → deferred web verification |
| Assembler | Inline AI generation of all derivative files | Bundled `scripts/assembler.py` handles Steps 7–12 at zero credit cost |
| Entity/tech reuse | None — each study extracted independently | Cross-study cache (`_known_entities.csv`, `_known_technologies.csv`) carried across all studies |
| Web verification | Inline during extraction (expensive, inconsistent) | Deferred Phase 3 batch with incremental `_web_cache.json` persisting across sessions |
| Raw text preservation | Not saved | `source/_raw_text.txt` saved for every study, enabling re-assembly without re-extraction |
| Batch validation | Manual spot checks | `assembler.py validate` checks referential integrity, code coverage, and completeness per batch |

**What changed in the repo:**

- **18 existing studies updated** — CSVs rewritten with v16 schema (importance/relevance/prescience ratings + rationales, `[DEFERRED]` backfill from Phase 3 web verification, standardized observation types and methodology codes). Derivative files (README.md, datapackage.json, schema_org.json, demo_analysis.py, original_text.md) regenerated by the assembler. Raw text added to `source/_raw_text.txt`.
- **15 new studies added** — 14 to `kastner-author/`, 1 to `other-authors/` (Dick Csaplar, Desktop Virtualization ROI)
- **Master indices regenerated** — `_master_studies.csv`, `_master_entities.csv`, `_master_technologies.csv`, `_collection_stats.csv` now cover all v16-processed studies alongside the existing repository studies
- **Caches added to repo root** — `_known_entities.csv`, `_known_technologies.csv`, `_web_cache.json`

**Phase 3 web verification highlights (Archives 1–4):**

- 168 entities verified: 52 active, 48 acquired, 11 dissolved, 9 renamed/reorganized, 6 merged, 42 persons/standards bodies/other
- 349 technologies verified: lifecycle_current assigned (active, discontinued, end-of-life, evolved, legacy-supported, mature, succeeded, standard-current, standard-superseded)
- 39 predictions verified: 22 confirmed, 11 partially verified, 6 refuted
- Notable refutations: Itanium 7x performance gain (never achieved), Xeon-Itanium cost parity (Common Platform Architecture scrapped 2005), Consumer LaGrande/TXT adoption (remained enterprise-only), WiFi hotspot paid-subscription model (collapsed; free WiFi dominated by 2008)
- Notable prescience: SARS supply chain fragility (2003, validated by COVID-19), AMD GHz-equivalency abandonment, HP consumer camera exit, SSD datacenter adoption, CDN market consolidation

**Quality notes:**

- 3 referential integrity errors caught and fixed during validation (AMD entity cross-reference, HP-Mercury tech/entity confusion, Eclipsys entity reference)
- 24 residual `[DEFERRED]` values (mostly persons with no public record) converted to `unknown [REVIEW]` per v16 spec
- 1 content-level duplicate detected and skipped (`Dell_SD2_FINAL.pdf` in Archive-4 matched Archive-1)
