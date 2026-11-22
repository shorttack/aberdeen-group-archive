# PENDING-CHANGES — FLORIDA System Archive

**Purpose.** A cache of new evidence and the edits it requires, so that corrections are applied in scheduled sweeps rather than one at a time. Established August 23, 2026 at Kastner's direction, on the reasoning that per-item propagation across eight papers is expensive and error-prone, while batched propagation is cheap and auditable.

**Status: 0 blockers, 42 pending items (row 24 standing reading task; rows 36b and 36c; rows 79–89 from the capacity brief and rows 90–107 from the 1992 EDS complaint, both logged November 21, 2026; rows 111–119 from the DCF ITN 03F12GC1 production and DCS-ANALYSIS.md, logged November 22, 2026; row 120, testimony-date correction awaiting Kastner confirmation, logged October 28, 2026 as row 79 and renumbered November 22, 2026), 83 applied entries (rows 108–110, transcript corrections, November 21, 2026), 2 retired. Rows marked † depend on OCR not yet citation-verified; sweep precondition is an image check. Full sweep applied October 28, 2026 to GitHub copies; Mac-only targets listed in § 5 await a second pass.**
Last updated: November 22, 2026. Row 120 added when merging the GitHub copy: the October 28 testimony-date item (GitHub commit cd9bc10d, originally row 79), renumbered because row 79 is the capacity brief. Rows 111–113 added from the DCF production under P257878-072926 (ITN 03F12GC1 procurement file): the Mar. 8, 2013 intent to award to Deloitte, the recovered ITN citation, and closing the request. Rows 114–119 added from DCS-ANALYSIS.md § 5 items A–F (A→114, B→115, C→116, F→117, E→118, D→119), with quotations checked against the run text. Previously updated November 21, 2026. Rows 79–89 appended from CAPACITY-OVER-TIME-BRIEF-2026-10-29.md (rows 80–85 are the brief's § 6 proposals; 79 and 86–89 from its § 1 and § 5). Row 108 applied: p. 44 "600J" correction to the complaint OCR transcript (transcript only; no paper edited). Row 109 applied: p. 43 signature page corrected from Kastner's reading of the paper page; row 101 updated. Row 110 applied: eleven misreads corrected from the full verification run; row 107 now reads H1246. Earlier the same day, rows 90–107 added from EDS v. HRS complaint (Leon Cir. Ct. 1992 CA 003618, filed Aug. 21, 1992; OCR run run_20261121t161910Z_prod); findings in EDS-v-HRS-1992-COMPLAINT-FINDINGS.md. Prior update, October 28, 2026. Full sweep of all rows applied to the GitHub copies (see § 5). Prior update, October 27, 2026. The IRLM reading in row 59 was verified in direction against IBM documentation (rows 76–78 added; row 59 promoted to P2). Kastner's technical reading of the two-processor limit was recorded and assessed in PRESENTMENT-1993-FINDINGS.md § 2.3a. Mac was offline when the review was done; rows were applied by script. No published-paper sweep was performed. Prior update, October 26, 2026. The 1993 Leon County grand jury presentment was received and filed, and rows 55–71 were added for the sweep. Four new request tracks were sent the same day (rows 72–75). Per Kastner's decision of October 26, rows 55 (architecture causation) and 57 ($5.1M upgrade figure) are **not** immediate-fix exceptions and wait for the sweep. No published-paper sweep was performed. Prior update, September 23, 2026: Gmail reconciliation added rows 50–53 and applied operational-register update 54.

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
| 90 | **The MOU has been recovered.** Wherever the signed October 4, 1991 MOU is called unrecovered or a records target, mark it acquired and cite Compl. Exh. B. Keep 12061 ¶57 as the auditor's summary of the document, not as the only source of its terms | Compl. Exh. B pp. 44–49 | main report App. A gap table ("signed document … remains unrecovered"); COLLECTION-PLAN § 1.6; NEXT-RECORDS-REQUESTS item 2; PRESENTMENT-1993-FINDINGS § records list; README documents list; SOURCES | P2 |
| 91 | **One date for the MOU.** The MOU is dated **October 4, 1991**. **Amendment One** is dated "as of October 18, 1991" and changes only the installation sequence: either unit by Nov. 4, the other by Nov. 20. Stop carrying the two dates as alternatives. Say that the presentment's "on or about October 18" (¶49) most likely refers to the amended instrument (inference) | Compl. Exh. B p. 44; Amendment One p. 52; presentment ¶49 | main report § 2 timeline (Oct. 1991 row) and § 5; Processor Capacity paper and brief, Oct. 1991 rows; NEXT-RECORDS-REQUESTS item 2 ("October 18, 1991 … MOU"); PRESENTMENT-1993-FINDINGS machine-lineage row | P2 |
| 92 | **Three readings of the MOU, kept separate.** The archive should describe the MOU at three levels: (a) what the document says, (b) what the auditor summarized (12061 ¶57), and (c) what the jury concluded (presentment ¶49, "all performance requirements … waived"). For (a), state four things. The preamble keeps every unmodified provision in force. ¶1D retains a capacity test against the RFP caseload. ¶1F retains tuning through May 31, 1992. The benchmark release in ¶3A is conditional on installing the upgrade and delivering the code tapes, and it removes the benchmark as a deliverable for Tasks 12–15 only, with ¶3B barring liquidated damages for benchmark delays. The archive's sentence "released EDS from evidence of successful tests for implementation stages already completed" should be checked against ¶3A's actual wording † | Compl. Exh. B pp. 44–46 | main report § 5 and App. A acceptance-mechanism row; Webster Addendum; Making It Workable row 7; One Model Lessons 8–9 | P2 |
| 93 | **The quoted "purpose" sentence is 12061's wording, not the MOU's.** The main report § 5 quotes the purpose as "the timely completion of certain tasks relating to implementation of the FLORIDA System and to provide the amicable termination …". The MOU reads: "an amicable framework for the timely completion of certain Tasks under the Contract and, **at EDS's request**, the amicable termination of the contractual relationship between HRS and EDS." Attribute the existing quotation to 12061, or replace it with the MOU text, and keep "at EDS's request" | Compl. Exh. B p. 44 | main report § 5 | P2 |
| 94 | **Row 36c (Kastner's exit-sequence synthesis): one component becomes documentary.** That EDS sought to end the relationship by October 1991 is now documented. The MOU twice says "at EDS's request" (pp. 44, 48), and EDS pleads that "at EDS's strong urging, HRS agreed not to exercise its unilateral option to extend" (Compl. ¶22), an admission against interest. The **motive**, the March 1991 discovery, remains press-sourced inference. Revise the 36c text accordingly before it is applied | Compl. ¶22; Exh. B ¶10A, pp. 44, 48 | PENDING-CHANGES row 36c; then 36c's own targets | P2 |
| 95 | **The capacity benchmark was pinned to the 1988 caseload by agreement.** Benchmark workload = actual per-case transaction rates from cutover districts × "RFP 1993+20% caseload volumes" (Wewerka letter, Oct. 4, 1991, REF E1794). The RFP response-time categories were set aside and a "more appropriate methodology" was to be developed. EDS alleged that actual caseloads already exceeded the 1993+20% projection (Compl. ¶¶15, 20); 12061 ¶54 gives the figures, 318,655 design point and 547,159 actual. Present this as documentary for the agreement, and keep the interpretation that the test answered the contract's workload, not the State's, labeled as analysis | Compl. Exh. B pp. 50–51; ¶¶14–15, 20; 12061 ¶54 | main report § 8a; Processor Capacity paper (caseload design point); One Model workload lesson; Webster Addendum; concept page `capacity-planning-assumptions` | P2 |
| 96 | **Verbatim RFP performance standards.** RFP §§ 7.30–7.32 are now in hand. § 7.32.4 gives six categories (search 6 s; record retrieval 4 s; edit 3 s; screen-to-screen 1 s; case assessment 8 s; print initiation 3 s; each at 95 percent; measured every 15 minutes on a randomly selected day each month at randomly selected workstations; working hours 7:00 AM–6:30 PM ET). § 7.32.5 sets availability at 97 percent, and § 7.32.6 sets 97 percent per workstation. Replace or supplement the 12061 ¶51 paraphrase with RFP pinpoints. Retire the Sept. 6 flag "RFP text itself remains unrecovered" for these sections only; Volume I as a whole is still a target † | Compl. Exh. E pp. 70–79, esp. 75–76 † | main report "Sizing risk was unowned" paragraph and App. A (response-time rows); Webster Addendum; One Model Lesson 8 | P2 |
| 97 | **Contract ceiling from the document.** The standard contract reads "not to exceed $104,269,432.00, subject to the availability of funds." Cite it as the documentary basis for the press "$104.2 million," keep the press figure as corroboration, and recompute the App. B overrun line that uses "$104.2 million" (the change is immaterial at one decimal). Record EDS's "approximately $85.9 million" for the 36-month initial term (Compl. ¶10) separately. Do not combine the two; the gap is probably the O&M option years (inference) † | Compl. Exh. A p. 41 †; ¶10 | main report App. B (contract-value row, cost table row 1, overrun table) | P2 |
| 98 | **Cost of the 1991 upgrade.** The MOU ¶1B cap is **$11,615,000** for the M720 and used 600J. ¶1E adds ~$2,046,500 one-time, $140,000/month and $258,000/year, all split 65/35. EDS pleads "approximately $8.9 million, or 65 percent" (¶16), which reconciles with 65 percent of cap plus one-time items (agent arithmetic, label as such). Replace testimony-sourced "over 11 million dollars" with the document figure where cost is stated. Row 57 stands: $5.1M is still unexplained. Add a unit guard where the 65/35 split appears near the 65 percent CPU-utilization figure | Compl. Exh. B pp. 44–45; ¶¶16, 18 | Processor Capacity paper and brief, Oct. 1991 rows; Making It Workable row 7; One Model Lesson 9; main report § 5 | P2 |
| 99 | **The April 1992 benchmark: attribute both accounts.** EDS alleged it "completed a benchmark test demonstrating satisfactory response time in March 1992," with results sent April 3, 1992 (Compl. ¶79). The main report App. A, following 12061, says no test was conducted "except for data submitted in April 1992." Carry both, attributed; they agree on the transmittal | Compl. ¶79 p. 22 | main report App. A acceptance-mechanism row | P2 |
### New documentary facts to propagate

| # | Change | Source | Targets | Priority |
|---|---|---|---|---|
| 24 | **Eight freely published Auditor General reports mirrored** — 2011-141, 2013-005, 2014-196, 2017-009, 2019-022 (FLORIDA System IT audits), 2011-082 and 2013-182 (Northwood Shared Resource Center data centre), 2016-046. **None has been read.** 2013-005 is contemporaneous with ITN 03F12GC1 and the best remaining substitute for the lost as-built figures; the two data-centre audits are the best candidates for hardware and disaster-recovery detail. | Mirrored August 21 | SOURCES, COLLECTION-PLAN; read before next sweep | **P2** — **standing reading task; not an edit** |
| 36b | **Legal fees on the EDS lawsuit as of March 17, 1993: $189,347.** ¶58. Small dollar figure but the first attested legal-cost data point for the litigation the archive has. | 12061 ¶58 | Main report Appendix B, memoir | P3 |
| 36c | **Kastner synthesis, September 5, 2026 — the exit sequence, not merely late compliance.** Setting the ¶57 record beside what the archive already establishes about the capacity-assumption error EDS discovered internally in March 1991 (established in the Webster arbitration, unknown to the auditor in 1992–93), the pattern reads as a deliberate multi-quarter exit sequence rather than as a failing performance under strain: (a) **March 1991** — EDS internally discovers the transaction-volume error underpinning its own bid sizing; (b) **January 30, 1991 – May 12, 1992** — 16 months of Department requests for benchmark/capacity data that EDS did not satisfy; (c) **October 4, 1991** — MOU signed, released EDS from evidence of successful tests for implementation stages already completed, waived liquidated damages for benchmark-test delays, and stated its purpose as "the amicable termination of the contractual relationship" — meaning the exit was being planned in writing seven months after the internal discovery; (d) **April 1992** — one benchmark data submission, the only one before departure; (e) **May 31, 1992** — EDS ceases participation; (f) **August 21, 1992** — EDS files suit for $46.5M. Six weeks between departure and complaint suggests a substantial period of pre-drafting. The auditor could not see this pattern in 1992–93 because the March 1991 internal discovery did not surface until Webster. **Recorded as analyst synthesis linking documented items across multiple sources; label as such in any paper that quotes it.** Sequence is documented; the *intent* it suggests is inference. The distinction has to travel with the argument. | 12061 ¶57; Webster arbitration record (via 12581 § litigation and 13043); Kastner synthesis September 5, 2026 | Main report § 5, § 6, memoir, lessons study | **P2** |
| 100 | **The complaint as a primary source for the claim.** It confirms the archive's "roughly $46.5 million" against ¶¶3–4. Add the count structure: I $19,444,586.21; II $16,518,062 (I + II = $35,962,648.21); III $3,270,545; IV $1,193,051; V $246,356; VI $1,517,000; VII > $1M; VIII > $4.5M; IX and X declaratory. The prayers total ≥ ~$47.7M because Count VII is added. Add Compl. pinpoints beside 12061 ¶15 | Compl. ¶¶3–4, Counts I–X, pp. 1–36 | main report § 2 (Aug. 21, 1992 row) and § 8 ("EDS's claim and the settlement"), App. B settlement paragraph; SOURCES | P3 |
| 101 | **Contract particulars:** Contract **LU009**; RFP issued **May 20, 1988**; a parent **guarantee by Electronic Data Systems Corporation** (Part C) is incorporated; HRS contract manager Judy E. Mitchell; EDS representative Robert C. Thomason; EDS signatory Robert R. White, Regional Manager, signed and dated May 12, 1989 (handwritten); HRS signature, no printed name or title, dated May 15, 1989 (handwritten); form date 7/1/88. Signature page confirmed by Kastner's reading of the paper page, Nov. 21, 2026 (Exh. A p. 7 = PDF p. 43; no Bates number) † | Compl. ¶¶9–10; Exh. A pp. 41–43 †; Exh. B p. 49 | main report § 2; Unisys Protests timeline; README | P3 |
| 102 | **Hardware increment not in the timeline.** CPC equipment was installed in October 1989 and "upgraded pursuant to Contract Amendment 3 in December 1990" (EDS allegation, model unstated). Add it to the capacity timeline as a documented-by-pleading gap | Compl. ¶79 p. 22 | Processor Capacity paper and brief; Making It Workable; main report App. A | P3 |
| 103 | **Equipment financing (Exhibits C–D).** HRS and the Comptroller computed EDS's markup over its IBM subcontract at 10.20 percent, disputed $1,952,132.43, and financed $17,492,453.78 through IBM installment sale (HRS bid #92-6BC). Time sale price $19,844,915.94; finance charges $2,352,462.16 over 60 months † | Compl. ¶¶70–74; Exh. C pp. 53–55; Exh. D pp. 56–65 † | main report App. B cost reconciliation | P3 |
| 104 | **EDS's side of the 1992 IBM "snap-shot."** EDS alleged that HRS bought upgraded equipment directly from IBM without competitive bidding, after an IBM "snap-shot" benchmark (¶48), and that the 1991 upgrade came out of "secret discussions" between HRS, "including Ms. Viann Hardy," and IBM (¶19), both on information and belief. Pair them with presentment ¶¶49, 53–55 as a second interested account. Row 60's SNAP/SHOT guard applies | Compl. ¶¶17–19, 48 | main report § 5; PRESENTMENT-1993-FINDINGS § 2.2 | P3 |
| 105 | **CICS conversion dropped.** MOU ¶4C: "HRS agrees that there is no longer a requirement that EDS perform the CICS conversion process." This is a technical fact for the IMS/transaction-manager discussion; its meaning (from what, to what) is an open question | Compl. Exh. B p. 47 | README § 4; open questions | P3 |
| 106 | **Open question 2 ("When did the 3090 reach 600J, and who paid?") is partly answered.** A used 600J and an M720 were installed under the MOU as amended Oct. 18, 1991, due Nov. 4 and Nov. 20, 1991. EDS paid 65 percent and HRS 35 percent, under the $11,615,000 cap plus ¶1E items, with HRS owning the equipment. Whether the deadlines were met is still open | Compl. Exh. B pp. 44–45, 52 | PENDING-CHANGES § 3; README open questions | P3 |
| 111 | **DCF's 2012 replacement procurement reached an award decision.** The Vendor Bid System advertisement for ITN 03F12GC1 (no. 03F12GC1-eval/neg, version 022) carries an entry "Added 03/08/2013: AGENCY DECISION — Pursuant to Invitation to Negotiate Number 03F12GC1, the Department of Children and Families intends to award a contract to Deloitte Consulting LLP", with the standard s. 120.57(3) protest-waiver notice. Deloitte was one of three vendors shortlisted for negotiation on Sept. 18, 2012, with Accenture and Xerox (F13332). **Wording guard:** One Model says the 2012 procurement "produces no replacement" (2012 timeline row) and "did not produce a replacement" (§ on the visible increment). The notice does not contradict that, but the papers should say the procurement ended in a notice of intent to award to Deloitte, not that it lapsed. **Not documented by this set (do not print):** whether the contract was executed, its value and scope, whether any protest was filed, and any link to Deloitte's later MyACCESS contract (inference only). The executed contract is item D in DCS-ANALYSIS.md § 5 | VBS advertisement printout, 4 pp., printed 9/20/2019, p. 1 (born-digital text; technical pass, not citation-verified); F13332 shortlist; DCF P257878-072926 | One Model 2012 timeline row and § on the visible increment; post-2000 paper; Annals outline (2012 replacement attempt) | P2 |
| 112 | **ITN 03F12GC1 recovered: restore the citation.** SOURCES.md's "One source that could not be repaired" is now answered. The ITN confirms 88 OSAM and 206 VSAM databases and 1.17 TB (430 GB archive + 740 GB active; PDF p. 76, ITN p. 72), and FLORIDA plus twenty-two other subsystems (PDF p. 8, § 1.4; the ITN p. 43 repeat lists twenty-one, omitting the Quality Control System). Convert the topology paper's and Annals manuscript's availability notes to a citation of the produced document with a page pin. Decide at end of day whether to commit the PDFs at `PDFs/records-requests/DCF-P257878-072926/source/`; the folder is currently untracked and not git-ignored. That settles README future-work item 7 and answers open question 5 in § 3 (the substitute search is no longer needed for these figures). Other DCS-ANALYSIS.md § 5 proposals (A–F) remain for Kastner's decision | F4863 ITN v1.0, PDF pp. 8, 76 (born-digital text; technical pass) | topology paper; Annals manuscript; README item 7; AG-12581-13043-FINDINGS ("remain unsubstituted" line) | P2 |
| 114 | **FLORIDA was still the core of ACCESS Florida in 2012** (DCS-ANALYSIS item A). The ITN: "Implemented in 1992, the Florida Online Recipient Integrated Data Access system (FLORIDA) is the legacy mainframe that provides core functionality for the ACCESS Florida System." DCF's stated problem was architecture and change cost ("inherently rigid and difficult to maintain"; "an ever-increasing risk of infrastructure failure due to the age of the mainframe"), not throughput. **Inference, label as such:** by 2012 the 1991–92 capacity problem had become a change-cost problem | F4863 ITN pp. 2, 46–47 (born-digital text; quotes found in the run text Nov. 22; technical pass, page-image check pending) | post-2000 paper; One Model 2012 row; Annals outline | P2 |
| 115 | **2012 workload, Q1 2012 averages** (item B): 4,673,852 unduplicated individuals; 2,532,681 unduplicated households; 1,041,109 applications and reviews per month; 2,380,145 call-centre calls per month. **Units guard (row 89c applies):** individuals, households, applications and calls are different units and are not combined into one growth ratio against the 1988 design point (row 83) | F4863 ITN p. 2 (PDF p. 6), Q1 2012 table | CAPACITY-OVER-TIME brief (rows 79–89); main report § 8a | P2 |
| 116 | **FLORIDA's 2012 technical estate** (item C; the database and volume figures are row 112): mainframe "12 LPARS"; "on average 1 to 2 abends per day" (answer to Xerox, Q83); extracts in "custom COBOL and SyncSort … and SQL for loads", and "a comprehensive data quality analysis has not been performed" (answers to Unisys, Q45–46); the new system to be hosted at the Northwood Shared Resource Center | F26854 Response to Inquiries p. 12 (Q83), Q45–46; F4863 ITN p. 1 | topology paper; post-2000 paper | P2 |
| 117 | **Kastner's observations on the 2012 figures** (item F; **Kastner firsthand analysis, Nov. 22, 2026**). (a) 2,380,145 calls ÷ 2,532,681 unduplicated households = **0.94 calls per household per month** (0.51 per individual; 2.29 per application or review). That is arithmetic on DCF's figures; reading it as a symptom of "limited self-service capabilities" (ITN p. 47) is inference. (b) The 2012 O&M service level is an **"Average Response Time"** (penalty above 3 s, failure above 5 s, monthly) with no percentile, transaction scope, or measuring point stated (ITN p. 115, Attachment II Exh. A). The 1988 RFP § 7.32 set percentile standards ("six (6) seconds for 95 percent of searches"; Compl. p. 76). † The p. 76 lines agree in two OCR engines but still need Kastner's page-image check | F4863 ITN pp. 2, 47, 115; Compl. p. 76 (OCR, two-engine agreement) | CAPACITY-OVER-TIME brief; One Model lessons; main report § on performance standards | P2 |
| 118 | **Retrieve the 2013 Negotiation Team Recommendation from the Internet Archive** (item E): `20130305_ITN 03F12GC1_Historic Procurement Document v 3.pdf`, captured Feb. 14, 2019, from the DCF floridareplacement folder named in the award notice (row 111). The Accenture, Deloitte and Xerox reply tabs are also captured. Mirror it, hash it, and log what it says about the award basis | DCS-ANALYSIS.md § 4 (Wayback search Nov. 22, 2026) | SOURCES.md; row 111 | P2 |
| 120 | **Testimony date in the memoir layer contradicts the documentary record.** Study 5b4524 and memoir vol. 1 ch. 9 date Kastner's Tallahassee protest testimony to "c. 1990–1991" / "the early 1990s" and say his expert-witness career began in 1992. The Unisys protests ran from the June 1988 specification protest (88-2942BID) through the award protest decided by recommended order in March 1989 (89-0003BID); the testimony therefore fell between December 1988 and early 1989. Surfaced by `kw ask` on 2026-10-28 after the IMS refresh. On sweep: correct the dates in the 5b4524 abstract and source text, `_master_studies.csv` abstract, and memoir ch. 9; label the 1992 date as the start of the paid expert-witness practice, not the first testimony. Kastner to confirm from recollection before edit. (Logged on GitHub as row 79 in commit cd9bc10d, October 28, 2026; renumbered 120 on November 22, 2026, because row 79 had been assigned locally to the capacity brief.) | DOAH 88-2942BID; 89-0003BID (recommended order March 1989); FLORIDA main report § 2; kw ask output 2026-10-28 | 5b4524 package (abstract, source texts); `_master_studies.csv`; Kastner Memoir vol. 1 ch. 9; wiki pages (regenerate) | P2 |
<!-- irlm-correction-2026-10-27 -->

### Capacity over time (CAPACITY-OVER-TIME-BRIEF-2026-10-29.md; rows 79–89, appended November 21, 2026)

Rows 80–85 are the brief's own § 6 proposals, carried over with cross-references to the 1992 complaint rows. Rows 79 and 86–89 turn the brief's bottom line (§ 1) and open gaps (§ 5) into rows. The brief does not record whether its "bought after the fact" thesis is Kastner's own observation; confirm before attributing it.

| # | Change | Source | Targets | Priority |
|---|---|---|---|---|
| 79 | **New working brief: processor capacity over time, 1988–1998.** `CAPACITY-OVER-TIME-BRIEF-2026-10-29.md` lists every processor the record places under the FLORIDA System (3090-300E bid, 400E demonstration, 300J, ES/9021-720 + 3090-600J, 720 alone, 9021-900, 9021-982, 1998 Sysplex of 982 + 9672-R83 + R44), each tagged documentary / testimony / IBM reference / inference, with an IBM SRM-constant proxy. Its thesis, that capacity was bought after the workload had already overrun the machine in place at every step, is **inference** and enters a paper only as labeled analysis. List the brief in the README documents table and SOURCES. No SRM total or "× bid" multiple goes into a paper until row 88 is met. The older, shorter draft `FLORIDA System — Processor Capacity Over Time, 1988–1998.md` (no §§ 3a–3b) is superseded | Brief §§ 1–3 | README documents list; SOURCES; Annals manuscript outline (shelved) | P3 |
| 80 | **Row 78 is partly resolved.** IBM SRM constants (service units per CPU-second, per engine) are now cited as a **relative proxy, labeled "not MIPS"** ([IBM, Processor version codes and SRM constants](https://www.ibm.com/support/pages/processor-version-codes-and-srm-constants)). Keep row 78's prohibition on printing MIPS, and on printing any capacity ratio as a measurement | IBM SRM table (IBM reference); brief § 3 | README open questions (row 78 wording); COLLECTION-PLAN § 1.6 item 6 | P2 |
| 81 | **9021-720 engine count.** Six-way per the IBM SRM table, which also lists a separate "partitioned 5-way" entry. State "six-way (IBM SRM table)" only after confirming which form HRS installed; until then say the model, not the engine count | IBM SRM table; brief § 5 gap 2 | main report § 4a; README open questions | P2 |
| 82 | **A single-host alternative existed at the MOU (inference).** The 720 used the 3090-J engine; only the 820 and 900 were a new design; the 9021-900 was shipping from September 1991. The MOU (row 90) now documents that the coupled M720 + used 600J configuration was the one chosen on October 4, 1991; EDS alleged that HRS and IBM agreed the upgrade in "secret discussions" (Compl. ¶19, allegation only; row 104). Current IBM sources are secondary (Wikipedia; a reproduced IBM Archives text): confirm against the IBM announcement letter before print | Brief § 4 (secondary); Compl. Exh. B p. 44 (pilot-checked, pending signoff); Compl. ¶19 p. 6 | Annals manuscript § on the MOU; main report § 4a | P3 |
| 83 | **Caseload design point.** The RFP sized the system for 265,546 + 20 percent = **318,655** Food Stamp cases in FY 1992–93; actual cases reached **547,159** in FY 1991–92, 1.72× the design point (12061 ¶54). Add to the Annals outline and main report § 8a. **Write together with row 95:** the Wewerka letter shows the October 1991 benchmark kept this design point by agreement, so one passage should carry both | 12061 ¶54; Compl. Exh. B p. 50 (OCR, unverified) | main report § 8a; Annals outline | P2 |
| 84 | **User-base additions on the same application.** AHCA staff became end users from July 1, 1993 (Medicaid to AHCA); FDOR staff from July 1, 1994 (CSE to Revenue). The CSE financial management module was still incomplete on May 4, 1995, and the consultant named it as "anticipated increase in the workload" justifying the 982 | 12581 p. 27, ¶¶13, 48 | main report § 4a and § 8a; check One Model's AHCA passage for consistency | P2 |
| 85 | **Post-1993 application moves onto the FLORIDA hosts are undocumented.** No source shows WIC, Project Independence, any 9370-hosted application, or client-server work moving onto the FLORIDA hosts; the only documented transfer runs the other way (1992: memory taken from the WIC/PI machine for the 720, presentment ¶53). Record Kastner's recollection, if any, as **Kastner firsthand**, and add a records request for the HRS/DCF data-center workload inventory, 1993–1998 | Brief § 3b; presentment ¶¶53, 60–68 | NEXT-RECORDS-REQUESTS; COLLECTION-PLAN § 1.6 | P3 |
| 86 | **The 300E → 300J step: a candidate.** The date, cost and approval of the change from the bid 3090-300E to the 300J in production by October 1991 are undocumented (brief gap 1). EDS alleged the central-site equipment, installed October 1989, was "later upgraded pursuant to Contract Amendment 3 in December 1990" (Compl. ¶79; row 102). **Inference only:** Amendment 3 is a candidate for that step. Do not print the link; Contract Amendment 3 is already a records target (row 107) | Brief § 5(1); Compl. ¶79 p. 22 (OCR, unverified) | README open questions; brief § 3 timeline row "Before Oct. 1991" | P3 |
| 87 | **The 982's "six active" engines.** Quote AG 12581's exact wording. The nominal total for six active engines (about 14,668, read as the 962 constant) and any capacity-on-demand or microcode explanation are inference until the wording and IBM configuration are confirmed | 12581 pp. 29, 55, ¶¶9, 23; brief § 5(3) | README § 4; main report § 4a | P2 |
| 88 | **Precondition for any capacity ratio in print.** Obtain period IBM LSPR (ITR) tables for the 3090-E/J and 9021 lines to replace or corroborate the SRM proxy (the two already differ: SRM puts the 900 at 2.0× the 600J; IBM's marketing claim was 1.7–1.9×). Confirm the 9672-R83 and R44 generations (R83 per-engine constant 904.7 is below R44's 2,038.2) before quoting the 1998 combined total of 33,982. Until met, no "× bid" multiple appears in a paper | Brief §§ 4, 5(4)–(5); IBM SRM table | COLLECTION-PLAN § 1.6; SOURCES (LSPR entry) | P2 |
| 89 | **Demand-side wording guards.** (a) Access devices went from 8,158 (6,678 terminals + 1,480 PCs, 11 districts, Jan. 21, 1993) to about 16,000 (terminals, workstations, printers and controllers, 15 districts, Jan. 1995): "about double" is inference, not a measured ratio. (b) The documented scheduling wording is "off-peak hours (including nights and Saturdays)" (12581 ¶47); "six-day, round-the-clock" is unsourced and is not printed. (c) Case, device and user counts are different units and are never combined into one growth ratio | 12061 background; 12581 p. 27, ¶47 | ALL (wording guard) | P2 |

### Records-request state

| # | Change | Source | Targets | Priority |
|---|---|---|---|---|
| 107 | **New records targets:** the **amended complaint** (Nov. 9, 1992, docket entries 38–39); letters **E1115** (EDS, Mar. 28, 1991) and **H1246** (Aug. 23, 1991; the image reads "H1246", corrected Nov. 21, 2026 from the earlier "E1246"/OCR "51246"; the H prefix suggests an HRS letter, which is inference) defining the benchmark worker activities; **Contract Amendment 3** (Dec. 1990); the 1992 HRS–IBM acquisition (bid #92-6BC) | Docket 1992 CA 003618; Compl. Exh. B p. 50; ¶79; Exh. D | COLLECTION-PLAN § 1.6; NEXT-RECORDS-REQUESTS | P3 |
| 113 | **DCF P257878-072926 answered.** Close the request (sent July 28, acknowledged July 29, 2026; produced by November 21, 2026; 22 PDFs) in the request trackers. Record the production date from the DCF portal or Gmail when checked, and any fee | DCF production; DIGITAL-SUMMARY.md | FLORIDA-records-requests-drafts § 6 and status table; REQUESTS-AWAITING-RESPONSE-2026-09-23; NEXT-RECORDS-REQUESTS-2026-10-26 (Hold row); One Model sources-needed table (ITN row) | P2 |
| 119 | **New DCF records request** (item D): the ACCESS Florida Technical Architecture v1.0 (its § 7.0 Key Statistics, cited in the Q&A, is the most important missing item for capacity history); Feasibility Study v3.0 (Schedule IV-B); Requirements Definition Document v1.3; the FLORIDA IMS and FLODS data dictionaries; the response-time definition and monthly performance reports (row 117b); call-centre source data; the executed contract (row 111); and the s. 287.057(1)(c) determination. Addendum 2 lists the first five as posted only on DCF's now-dead website; the Internet Archive holds none. **Drafted Nov. 22, 2026 as a Gmail draft, not sent; send only on Kastner's instruction** | F31900 Addendum 2 p. 2; DCS-ANALYSIS.md §§ 4–5 | FLORIDA-records-requests-drafts (new § 7); NEXT-RECORDS-REQUESTS; COLLECTION-PLAN § 1.6 | P2 |
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

### 2026-11-21 — Complaint OCR transcript correction (Kastner direction; transcript only, no paper edited)

| Row | Applied to | Not reached / follow-up |
|---|---|---|
| 108 | **P. 44, "IBM 6007" → "IBM 600J" in two places** (MOU ¶1A: "a used IBM 600J processing unit"; "the IBM 600J unit is operational no later than November 20, 1991"). The production OCR misread both; the paragraph's middle occurrence was already correct. Evidence: blind Qwen vision transcription (qwen3.8:27b-mlx) read 600J at all three; independent Tesseract read (psm 4) read 600J at the second; image check of p. 44 confirms. Verification pilot `verify_20261122T005426Z_88e1b42d`, claims C05 (MODEL_ONLY) and C06 (MACHINE_CONFIRMED). Applied to `FLORIDA/sources/courts/eds-v-hrs-1992CA003618-complaint-1992-08-21-ocr.md` (layout text, now lines 2726 and 2733; header updated) and to the production run folder `~/Desktop/Memoirs/FLORIDA-documents/run_20261121t161910Z_prod/6_08211992_Complaint copy_88e1b42d/ocr/` (.md, .layout.md, .sidecar.txt; originals kept as `*.pre-correction-2026-11-21`; record in `CORRECTIONS-2026-11-21.md`) | Searchable PDFs not altered (hidden text layer still reads 6007). P. 52 (Amendment One) "used IBM 6007 is" awaits the full verification run. Rows 98 and 106 already use 600J; no paper change needed |
| 109 | **P. 43 (Exh. A contract p. 7 of 7, signature page), human reading.** Form date "11/88" → "7/1/88"; left (PROVIDER, E.D.S. Federal Corporation) signature → `[signature: Robert R. White]`, date "ny 12,1989" → `[handwritten] May 12, 1989`; right (HRS) signature → `[signature; no printed name or title]`, date "er LZ&F" → `[handwritten] May 15, 1989`. Evidence: Kastner's firsthand reading of the paper page (not OCR or model output); claims C34 and C35. Applied to the archive transcript (now lines 2659, 2670, 2678; header Corrections row updated) and to the run folder .md, .layout.md and .sidecar.txt (record in `CORRECTIONS-2026-11-21.md`, items 3–7). Row 101 text updated to match | Searchable PDFs not altered. Not checked: "PROVIOER", "SIGNED 8Y", "NAM E", federal ID/SAMAS/fiscal-year lines; the "711/88" form-date footer on another page (probably 7/1/88) |
| 110 | **Full-run OCR corrections, complaint transcript** (verification `verify_20261122T005901Z_88e1b42d`, 79 pages, 73 claims, 62 MACHINE_CONFIRMED). Eleven character misreads corrected where blind Qwen and the page image agree: p. 46 "4 deliverable … and iS" → "a deliverable … and 15"; p. 48 "Memeorandum" → "Memorandum"; p. 50 "51246" → **"H1246"**; p. 51 "RRS" → "HRS", "@ more" → "a more"; p. 52 "used IBM 6007 is" → **"600J is"**; p. 64 "5.682" → **"5.68%"**; p. 75 "norzal" → "normal", "6:39" → **"6:30"**, "Tine" → "Time". Applied to the archive transcript (lines 2868, 3009, 3109, 3153, 3159, 3189, 4644, 5473–5475; header Citation verification and Corrections rows rewritten) and to the run folder .md, .layout.md and .sidecar.txt (`CORRECTIONS-2026-11-21.md`, items 8–18). Row 107 changed from E1246 to H1246 | Searchable PDFs not altered. Layout line splits left as produced. Pp. 72–79 production text is word-scrambled; quote from the image. P. 41 "$104,269,432.00" (claim C30) confirmed by Kastner's image check, Nov. 21, 2026; p. 76 lines (C66, C69) still to check. Findings note `EDS-v-HRS-1992-COMPLAINT-FINDINGS.md` corrected Nov. 21, 2026 on Kastner direction (H1246, 5.68 percent, 6:30 PM confirmed, p. 41 and p. 43 confirmations; revision note at head) |

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
