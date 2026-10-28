# PENDING-CHANGES — FLORIDA System Archive

**Purpose.** A cache of new evidence and the edits it requires, so that corrections are applied in scheduled sweeps rather than one at a time. Established August 23, 2026 at Kastner's direction, on the reasoning that per-item propagation across eight papers is expensive and error-prone, while batched propagation is cheap and auditable.

**Status: 0 blockers, 2 pending items (row 24 standing reading task; row 79 testimony-date correction awaiting Kastner confirmation), 81 applied entries, 2 retired. Full sweep applied October 28, 2026 to GitHub copies; Mac-only targets listed in § 5 await a second pass.**
Last updated: October 28, 2026. Full sweep of all rows applied to the GitHub copies (see § 5). Prior update, October 27, 2026. The IRLM reading in row 59 was verified in direction against IBM documentation (rows 76–78 added; row 59 promoted to P2). Kastner's technical reading of the two-processor limit was recorded and assessed in PRESENTMENT-1993-FINDINGS.md § 2.3a. Mac was offline when the review was done; rows were applied by script. No published-paper sweep was performed. Prior update, October 26, 2026. The 1993 Leon County grand jury presentment was received and filed, and rows 55–71 were added for the sweep. Four new request tracks were sent the same day (rows 72–75). Per Kastner's decision of October 26, rows 55 (architecture causation) and 57 ($5.1M upgrade figure) are **not** immediate-fix exceptions and wait for the sweep. No published-paper sweep was performed. Prior update, September 23, 2026: Gmail reconciliation added rows 50–53 and applied operational-register update 54.

---

## Operating protocol

**On receiving new information** — a records response, a document, an observation, a correction — the agent does three things and stops:

1. Files the source material (PDF, OCR, extraction) where it belongs.
2. Writes a findings note if the material warrants analysis.
3. **Appends a row here.** It does not edit the published papers.

**On an explicit sweep instruction** — "run the pending changes," "do the sweep" — the agent works the table top to bottom in one pass, marks each row applied with a date, and reports what it could not resolve.

**Exception.** A factual error that would mislead a reader who opens the file today gets fixed immediately and logged as applied. Everything else waits.

**Rows never get deleted.** Applied rows move to § 5 with their date. The log is a record of how the archive's claims changed and when, which is itself archival material.

---

## 0. RESOLVED 2026-09-06 — was: two divergent copies of the corpus

**Status: RESOLVED. Investigation revealed the blocker as originally written was partially false.** The Mac copies were the only extant copies of the six published papers; no "session workspace" copy with CourtListener repairs actually existed anywhere in the workspace or in the branched-context generated assets. The July 28 repair was **claimed complete in the log but never landed in a durable artifact**. The 16 casetext links (not 15 as logged) were still live in the Mac papers because that was the only place the papers lived.

**Resolution September 6, 2026:**
1. Pulled all six affected papers from Mac to sandbox for edit.
2. Verified `https://casetext.com/case/state-dhrs-v-eds-federal-corp` returns HTTP 410 Gone on direct browser HEAD (the earlier session's claim was correct on this).
3. Located a stable public copy at `https://openjurist.org/631/so2d/353` (openjurist.org, full opinion text of *State, Dept. of Health & Rehabilitative Services v. E.D.S. Federal Corp.*, 631 So. 2d 353 (Fla. 1st DCA 1994), No. 92-4068).
4. Substituted all 16 occurrences across all six papers.
5. Mirrored the full opinion into the archive at `sources/courts/state-dhrs-v-eds-federal-631-so2d-353.md` so no future dead link kills the citation.
6. Pushed all six edited papers and the mirror back to the Mac.

**Original blocker table (retained for the historical record):**

| | `~/Desktop/Archive/FLORIDA/` (Mac) | Claimed "session workspace" |
|---|---|---|
| The six papers + README | Present | **Not actually present** |
| `SOURCES.md`, `COLLECTION-PLAN.md`, `FLORIDA-records-requests-drafts.md` | Absent | Present |
| Casetext links repaired to CourtListener | No — 16 casetext links across 6 files, all HTTP 410 | **No** — no such repaired copy existed |
| § 4a growth analysis and § 7 strengthening | Applied August 23 | N/A |

See row 48 for the archive-reliability observation this resolution produced.

---

## 1. How to read the table

- **Source** — where the evidence came from. `12581 ¶44` means Auditor General Report No. 12581, printed paragraph 44.
- **Targets** — files needing edit. `ALL` means every published paper plus README.
- **Priority** — `P1` a claim currently in print is wrong; `P2` a claim is under-supported or imprecise; `P3` additive, nothing currently wrong.

---

## 2. Pending

### Corrections to claims currently in print

| # | Change | Source | Targets | Priority |
|---|---|---|---|---|
### New documentary facts to propagate

| # | Change | Source | Targets | Priority |
|---|---|---|---|---|
| 24 | **Eight freely published Auditor General reports mirrored** — 2011-141, 2013-005, 2014-196, 2017-009, 2019-022 (FLORIDA System IT audits), 2011-082 and 2013-182 (Northwood Shared Resource Center data centre), 2016-046. **None has been read.** 2013-005 is contemporaneous with ITN 03F12GC1 and the best remaining substitute for the lost as-built figures; the two data-centre audits are the best candidates for hardware and disaster-recovery detail. | Mirrored August 21 | SOURCES, COLLECTION-PLAN; read before next sweep | **P2** — **standing reading task; not an edit** |
| 36b | **Legal fees on the EDS lawsuit as of March 17, 1993: $189,347.** ¶58. Small dollar figure but the first attested legal-cost data point for the litigation the archive has. | 12061 ¶58 | Main report Appendix B, memoir | P3 |
| 36c | **Kastner synthesis, September 5, 2026 — the exit sequence, not merely late compliance.** Setting the ¶57 record beside what the archive already establishes about the capacity-assumption error EDS discovered internally in March 1991 (established in the Webster arbitration, unknown to the auditor in 1992–93), the pattern reads as a deliberate multi-quarter exit sequence rather than as a failing performance under strain: (a) **March 1991** — EDS internally discovers the transaction-volume error underpinning its own bid sizing; (b) **January 30, 1991 – May 12, 1992** — 16 months of Department requests for benchmark/capacity data that EDS did not satisfy; (c) **October 4, 1991** — MOU signed, released EDS from evidence of successful tests for implementation stages already completed, waived liquidated damages for benchmark-test delays, and stated its purpose as "the amicable termination of the contractual relationship" — meaning the exit was being planned in writing seven months after the internal discovery; (d) **April 1992** — one benchmark data submission, the only one before departure; (e) **May 31, 1992** — EDS ceases participation; (f) **August 21, 1992** — EDS files suit for $46.5M. Six weeks between departure and complaint suggests a substantial period of pre-drafting. The auditor could not see this pattern in 1992–93 because the March 1991 internal discovery did not surface until Webster. **Recorded as analyst synthesis linking documented items across multiple sources; label as such in any paper that quotes it.** Sequence is documented; the *intent* it suggests is inference. The distinction has to travel with the argument. | 12061 ¶57; Webster arbitration record (via 12581 § litigation and 13043); Kastner synthesis September 5, 2026 | Main report § 5, § 6, memoir, lessons study | **P2** |
<!-- irlm-correction-2026-10-27 -->

| 79 | **Testimony date in the memoir layer contradicts the documentary record.** Study 5b4524 and memoir vol. 1 ch. 9 date Kastner's Tallahassee protest testimony to "c. 1990–1991" / "the early 1990s" and say his expert-witness career began in 1992. The Unisys protests ran from the June 1988 specification protest (88-2942BID) through the award protest decided by recommended order in March 1989 (89-0003BID); the testimony therefore fell between December 1988 and early 1989. Surfaced by `kw ask` on 2026-10-28 after the IMS refresh. On sweep: correct the dates in the 5b4524 abstract and source text, `_master_studies.csv` abstract, and memoir ch. 9; label the 1992 date as the start of the paid expert-witness practice, not the first testimony. Kastner to confirm from recollection before edit. | DOAH 88-2942BID; 89-0003BID (recommended order March 1989); FLORIDA main report § 2; kw ask output 2026-10-28 | 5b4524 package (abstract, source texts); `_master_studies.csv`; Kastner Memoir vol. 1 ch. 9; wiki pages (regenerate) | P2 |

### Records-request state

| # | Change | Source | Targets | Priority |
|---|---|---|---|---|
---

## 3. Open questions this evidence raises

Not edits. Research leads generated by the new material.

1. **Who was the third bidder on RFP 88-74-BC?** The DOAH record or the procurement file should name it.
2. **When did the 3090 reach 600J, and who paid?** IBM allowed conversion to 600J only from a 600S or 600E, so the machine was doubled in engine count first. The APD file had to approve federal participation in each hardware increment.
3. **What does Report 12061 say at ¶¶49–59?** It is the first documentation of the capacity failure, two years before the press.
4. **Do the Report 12581 workpapers still exist?** Asked of the Auditor General August 21. If yes, they hold the measurement data behind the 95 percent figure and the only route is a Legislative Auditing Committee petition.
5. **Does Report 2013-005 or either Northwood data-centre audit carry the as-built figures lost with ITN 03F12GC1?** Unread. Cheapest open lead in the project.
6. **Was the $5.1 million upgrade the 1993 grand jury examined the same transaction as anything in the audit record?** The 1995 upgrade cost $5,438,079.75 — different transaction, two years later. Note the resemblance; build nothing on it.

---

## 4. Standing items not arising from new evidence

| # | Item | Status |
|---|---|---|
| S1 | Annals manuscript is ~8,700 words against an 8,000 ceiling; the unmade 700-word trim would come from the afterlife and academic-void sections | Shelved at Kastner's direction |
| S2 | Nothing from this session has been pushed to `shorttack/aberdeen-group-archive` | Open |
| S3 | Whether the §§ 3 and 4 amendments were incorporated before the July 28 federal FOIA requests went out | Unresolved; check sent mail |
| S4 | OTA report is OTA-BP-CIT-47, April 1988, not "OTA-881203, December 1988" | Corrected in main report and README July 28; **verify propagation to SOURCES, CHRONOLOGY, Empty Center** |

---

## 5. Applied

### 2026-10-28 — Full sweep (Kastner direction: all rows), GitHub copies, Mac offline

Scope: every row in § 2 as of October 28, 2026, applied to the files present in `shorttack/aberdeen-group-archive` `FLORIDA/` and the 5b4524 study package. The Mac was offline; GitHub was current through the October 26 evening commit and the October 27 patch was re-applied byte-identically before the sweep. **Targets not on GitHub were not guessed at:** CHRONOLOGY, As-Built Topology, Three Seconds, Whose Model, Cost Reconciliation, Operating Conditions, Consistency Audit, Remembered by Auditors, the memoir, kastner-unisys-protest-analysis, and the workload-assumption concept page. If those files exist on the Mac, the rows below that name them need a second pass there; if they do not exist, the references in this log are stale. Each revised paper carries a dated revision note at its head. Verification: every anchor matched on first pass; no 'statewide grand jury' or '$5.1M' remains outside correction notes (searched).

| Row | Applied to | Not reached / follow-up |
|---|---|---|
| 4 | README § 4 (12,000 terminals / 11 districts and 16,000 devices / 15 districts separated by unit and year); main report already carried fifteen districts | topology paper not on GitHub |
| 6 | README § 4 and main report § 4a use 'hosted on'; main report 'absorbing the communications overhead' retained as analysis |  |
| 7 | main report § 2 | CHRONOLOGY not on GitHub |
| 8 | Webster Addendum Part II; main report § 2 (arbitration dates) | CHRONOLOGY not on GitHub |
| 9 | main report § 8a | CHRONOLOGY not on GitHub |
| 10 | main report § 2 | CHRONOLOGY not on GitHub |
| 11 | main report § 8a (full itemization incl. liquidated damages); One Model not changed (no settlement table) |  |
| 12 | main report § 8, Unisys Protests § 3.4, COLLECTION-PLAN § 1.6 — third bidder identified as CSX Technology (presentment ¶11) |  |
| 13 | main report § 8a; Unisys Protests § 3.4 |  |
| 14 | main report § 8a (already in § 7) |  |
| 15 | main report § 8a and Appendix B | CHRONOLOGY not on GitHub |
| 16 | main report Appendix A.2; Making It Workable Table 2 and text; README § 4; One Model Lesson 9 |  |
| 17 | README open technical questions (host at each generation) | topology paper not on GitHub |
| 18 | README § 4 and open questions | topology paper not on GitHub |
| 19 | main report § 8a; Unisys Protests § 3.4 | memoir not on GitHub |
| 20 | main report § 8a; Unisys Protests § 3.4, with the do-not-overstate qualifier | memoir not on GitHub |
| 21 | SOURCES (11178/11619/12061/13256 row); main report § 8 already carried | CHRONOLOGY not on GitHub |
| 22 | main report § 8a |  |
| 23 | main report § 8a |  |
| 25 | main report § 8 (DCF negative, custodians re-ranked) |  |
| 26 | main report § 8a; Unisys Protests § 3.4 | memoir not on GitHub |
| 27 | main report § 2, § 3, Appendix A item 7, Appendix B item 3 | CHRONOLOGY, memoir not on GitHub |
| 28 | main report § 8a |  |
| 30 | main report Appendix A.2 and § 8a; Making It Workable Table 2 | CHRONOLOGY not on GitHub |
| 31 | main report § 5; COLLECTION-PLAN § 1.6 (MOU as target) | memoir not on GitHub |
| 32 | main report § 4a; README § 4 | topology paper not on GitHub |
| 33 | main report § 4 (exposure qualifier) |  |
| 34 | main report § 8a and Appendix B |  |
| 35 | main report § 8a | memoir not on GitHub |
| 36 | main report § 5 | memoir not on GitHub |
| 38 | main report § 8; README documents list — paper side now applied |  |
| 39 | main report § 8a | topology paper, memoir not on GitHub |
| 40 | main report § 8a (flagged as untested; not quoted as a frame) |  |
| 41 | main report § 8a | memoir not on GitHub |
| 49 | Study package 5b4524: source texts (3), README, datapackage.json, schema_org.json, studies/entities/observations/technologies CSVs — 46 substitutions, `ibm-db2` → `ibm-ims`, correction note added | Masters, wiki page, and embeddings regenerate on the Mac; confirm `ibm-ims` matches the master technology ID; Database longitudinal dossier not on GitHub |
| 50 | main report § 8 |  |
| 51 | main report § 8; README documents list |  |
| 52 | DOAH-2026-09-06-FINDINGS.md (correction banner, three passages superseded) | COLLECTION-PLAN § 2.1 update banner retained; derivative claims elsewhere not found by search |
| 53 | Already carried in REQUESTS-AWAITING-RESPONSE; no paper asserted the contrary |  |
| 55 | README § 1 (three-link chain, heading changed); main report § 2; Empty Center § 6 table | Whose Model, Three Seconds not on GitHub |
| 56 | main report § 2 and § 5; Webster Addendum Part II; Making It Workable item 7; COLLECTION-PLAN § 1.6 — both dates (Oct. 4 per 12061, 'on or about Oct. 18' per presentment) carried | Cost Reconciliation not on GitHub |
| 57 | main report § 1, § 3, Appendix A item 7 and A.2, Appendix B item 3; Making It Workable item 7 and Table 2; Unisys Protests timeline and § 3.3; One Model Lesson 9 | Cost Reconciliation not on GitHub |
| 58 | main report § 4a; README § 4 and open questions | As-Built Topology, CHRONOLOGY not on GitHub |
| 59 | README open questions (answered in direction); main report § 4a | Three Seconds, Whose Model, concept page not on GitHub |
| 60 | README § 3 guard; main report § 3 | Three Seconds, Whose Model, Consistency Audit not on GitHub; {UP} has no SNAP/SHOT passage needing a guard |
| 61 | main report § 2 (Oct. 1989, May 7 1990, Mar.–Apr. 1991, July 1 1991, June 1–2 1992 rows) | CHRONOLOGY, Operating Conditions not on GitHub |
| 62 | main report § 4 | Cost Reconciliation not on GitHub |
| 63 | main report § 8a | Cost Reconciliation not on GitHub |
| 64 | One Model Lesson 12; One Bad RFP | Remembered by Auditors not on GitHub |
| 65 | Empty Center § 6 |  |
| 66 | Making It Workable text (Zingale's six causes) | Operating Conditions not on GitHub |
| 67 | Unisys Protests § 3.4 | kastner-unisys-protest-analysis not on GitHub |
| 68 | COLLECTION-PLAN § 1.6 (targets); memoir package not changed — outside FLORIDA papers' scope per the row |  |
| 69 | main report § 3 (citation rule stated, outcomes paired); Unisys Protests; One Model; Empty Center; Making It Workable — every presentment cite reads 'the presentment states (¶N)' or 'the grand jury found' |  |
| 70 | README documents list and primary-documents table; COLLECTION-PLAN § 1.6; request logs already current |  |
| 71 | main report § 1, § 2, § 8, Appendix A; Making It Workable; Unisys Protests; Webster Addendum; README; SOURCES; COLLECTION-PLAN § 1.6 — no paper now calls it a statewide grand jury except in correction notes | records-request drafts v16 retain the pre-October reasoning as history; not rewritten |
| 72 | Request logs already current (REQUESTS-AWAITING-RESPONSE, Oct. 26); {CP} § 1.6 |  |
| 73 | Request logs already current |  |
| 74 | Request logs already current; COLLECTION-PLAN § 1.6 |  |
| 75 | Request logs already current |  |
| 76 | main report § 4a; README § 4 and open questions | Three Seconds, Whose Model, As-Built Topology, CHRONOLOGY, concept page not on GitHub |
| 77 | main report § 2; Unisys Protests timeline; One Model § 9; SOURCES; mirror created `sources/courts/state-v-mitchell-1st-dca-1996.md` | Knowledge-page flag retires on next wiki refresh |
| 78 | README open questions; COLLECTION-PLAN § 1.6 item 6; no paper prints MIPS (verified by search) | As-Built Topology not on GitHub |
| 5 | — | Already applied Aug 23 (main report Appendix A) and in records-request drafts v16 item 6; COLLECTION-PLAN § 1.5b carries it. Nothing further to apply; retiring. |


### 2026-09-23: Gmail-verified operational register refresh

| Row | What was applied | Files touched |
|---|---|---|
| 54 | Refreshed seven request tracks from Gmail. Genuine waiting list: HHS, DCF P260649-082226, DCF P257878-072926. Auditor General complete; original DCF procurement answered; DOAH closed; Leon County and USDA answered negatively. Saved USDA PDF and relevant email evidence without identity-document images or signed URLs. Preserved historical letters, added explicit overrides/corrections, and kept unsent/unverified work distinct from awaiting-response work. | FLORIDA-records-requests-drafts.md v16; REQUESTS-AWAITING-RESPONSE-2026-09-23.md; sources/records-requests/; PDFs/records-requests/ |

### 2026-09-06 — Plan B sweep: P1 paper corrections + support-file updates

**Scope:** P1 rows applied to published papers; collection-plan/records-request rows applied to support files. P2 and P3 paper rows deliberately deferred. Executed by three Claude Opus 5 subagents (one per paper group) plus direct orchestrator edits to support files.

| Row | What was applied | Files touched |
|---|---|---|
| **29** (P1) | **The RFP DID specify a quantified performance standard.** Response within 1–8 seconds at ≥95% of the time, sampled every 15 min at a randomly selected day/workstation monthly; ≥97% availability over consecutive 30-day periods (12061 ¶51). The archive's inference-from-silence was wrong and each paper now says so explicitly. Argument relocated from "no standard existed" to "the standard existed and was never enforced." | Main paper §§ 1, 5, 7, 8 + Appendices A.2–A.4, B.1–B.4; lessons study Lessons 7/8/8a + § 2 + A3 + D1 + § 9; Empty Center § 1 + § 8; Addendum (new correction section) |
| **1** (P1) | **Attribution of the 95/100 percent CPU utilization figure.** Reattributed from "the Auditor General measured" to an October 11, 1994 report by an independent consultant hired by the Department; the 65 percent comparison identified as industry data the Department obtained. | Main paper § 2 chronology + § 3 + Appendix A.2; lessons study chronology + Lesson 7 + B2 + § 9 + attribution note; Empty Center § 1; Addendum |
| **2** (P1) | **Cost floor.** $245.3M / 128 percent superseded by **$310,621,339** through FY 1996-97 (Department's own estimate, 13287 p. 14), an overrun of roughly 188 percent on the $107,658,141 bid. Appendix B rebuilt rather than patched. | Main paper § 1 + Appendix B.1–B.4; lessons study § 1 + A6 + Conclusion Five. **Skipped on Empty Center and Addendum** — neither carries the superseded figure |
| **36a** (P1) | **October 4, 1991 MOU, full documented terms from 12061 ¶57.** All four terms recorded: test deferred until after IBM hardware upgrades; EDS released from evidence of successful tests for already-completed stages; liquidated damages waived for benchmark delay; revised response times to be jointly developed and never were before the May 31, 1992 termination. EDS's allegation that the MOU released it from the response-time standard, the stated "amicable termination" purpose, and the auditor's "legal effect … unknown and currently the subject of litigation" all carried. Appendix A gap table corrected — the MOU's terms are reproduced in ¶57 even though the document itself is not. | Main paper § 5 (two new paragraphs) + § 7 + Appendix A.4; Addendum (new section) |
| **43** | Report No. 10983 (AFDC Operational Performance Audit, named at 11178 ¶53) added as a future Auditor General ask with draft text | COLLECTION-PLAN § 1.5a; records-requests § 8 |
| **44** | FSA-1988 programming pool overlap recorded as an open research question | COLLECTION-PLAN new § 7 |
| **46** | DOAH null return logged; file destroyed under 1998 routine retention; instruction not to re-request | COLLECTION-PLAN § 2.1; records-requests § 7 + responses table |
| **47** | Remaining plausible custodians for Unisys bid documents recorded | COLLECTION-PLAN § 2.1; records-requests § 7 |
| **48** | **Archive-reliability standard added to the README.** New subsection "A second worked example — log entries about work done are claims, not facts," recording the July 28 phantom repair and establishing that the archive's operational record is held to the same evidentiary standard as its documentary record | README "The evidentiary standard used here" |
| **38** (partial) | Correction that 11178 and 11619 are not systems audits and do not carry a pre-FLORIDA operational baseline | COLLECTION-PLAN § 1.5. **Paper-side portion still pending** |

**Also applied, not from a numbered row:** the casetext→CourtListener substitution was re-pointed from openjurist.org to `courtlistener.com/opinion/1895493/` (16 occurrences, six papers) so the papers match what `SOURCES.md` had recorded since July 28. The openjurist URL used in the morning's blocker fix was replaced. The mirrored opinion at `sources/courts/state-dhrs-v-eds-federal-631-so2d-353.md` now names CourtListener as primary with openjurist as the fetch source.

**Verified on the Mac after push:** zero openjurist references in papers; CourtListener present at 7/3/3/1/1/1 across the six; $310,621,339 present in main paper and lessons study; the 1–8 second standard present and cited to ¶51.

**Subagent SWEEP flags carried forward (not blockers, worth knowing):**
1. Report 12061 **paraphrases** the contract's performance language rather than quoting it. The papers attribute the standard to the auditor's account; the RFP text itself remains unrecovered. Any future claim quoting the contract verbatim needs the RFP.
2. The Addendum still lists Reports 12581 and 13043 as not yet obtained. True no longer; outside the four P1 rows so left for a future pass.

### 2026-09-06 — § 0 blocker resolved, casetext→openjurist repair

- **What was applied:** substituted `https://casetext.com/case/state-dhrs-v-eds-federal-corp` (HTTP 410 Gone) with `https://openjurist.org/631/so2d/353` across all 6 published papers carrying the citation. 16 substitutions in total.
- **Files touched:** Addendum (Webster) [1]; Making It Workable [1]; One Bad RFP Away [1]; The Empty Center [3]; The FLORIDA System (main report) [7]; The Unisys Protests [3].
- **New source added:** `sources/courts/state-dhrs-v-eds-federal-631-so2d-353.md` — full opinion text mirrored from openjurist.org, September 6, 2026, so any future breakage of the openjurist URL does not orphan the citation.
- **Verification:** `grep -c casetext ~/Desktop/Archive/FLORIDA/*.md` returns 0 hits in published papers after push.
- **Not resolved by this action:** the underlying archive-reliability question (row 48). That remains a pending row.


| # | Change | Applied | Where |
|---|---|---|---|
| A1 | § 4a "What the machine actually grew into" — 12,000-to-16,000 growth, two-host configuration, bid-to-delivered processor gap, utilization figures reframed as application-host-only | Aug 23, 2026 | Main report, Mac copy |
| A2 | § 7 "Sizing risk was unowned" strengthened with the fixed-price-bundled-hardware mechanism, the settlement equipment evidence, and the caseload concession | Aug 23, 2026 | Main report, Mac copy |
| A3 | § 8 open items rewritten — 12581 and 13043 marked obtained with the attribution caveat; 11178/11619/12061 added | Aug 23, 2026 | Main report, Mac copy |
| A4 | Appendix A note that 12581 and 13043 are now in hand and the tables not yet revised against them | Aug 23, 2026 | Main report, Mac copy |
| A5 | Appendix A gap table no longer cites Report 12581 workpapers as an obtainable source | Aug 23, 2026 | Main report, Mac copy |

---

*Maintained at `~/Desktop/Archive/FLORIDA/PENDING-CHANGES.md`. Working scaffolding — exclude from any GitHub push unless the decision is made to publish the archive's own revision history, which would be defensible.*

## Retired 2026-09-06 (per Kastner direction)

- **Row 42 (was P2) — 12061 Finding #9 / 11178 BVS citation discrepancy.** Kastner: "I have no immediate interest in pursuing claims record accuracy. Drop this." Not applied to any paper; simply retired.
- **Row 45 (was P3) — 11619 "MAJOR NEW DEVELOPMENT" org unit sight-check.** Kastner: "I see no reason to pursue further." Retired.
