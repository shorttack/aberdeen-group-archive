# PENDING-CHANGES — FLORIDA System Archive

**Purpose.** A cache of new evidence and the edits it requires, so that corrections are applied in scheduled sweeps rather than one at a time. Established August 23, 2026 at Kastner's direction, on the reasoning that per-item propagation across eight papers is expensive and error-prone, while batched propagation is cheap and auditable.

**Status: 0 blockers, 38 pending items (all P2/P3), 10 applied this sweep + 5 prior, 2 retired.**  
_Last updated: September 6, 2026 (second) — Plan B sweep executed: P1 rows 29, 1, 2, and 36a applied to the published papers by Claude Opus 5 subagents; rows 43, 44, 46, 47, 48 and part of 38 applied to COLLECTION-PLAN, the records-requests log, and the README. Casetext links re-pointed to CourtListener to match SOURCES.md. **P2 and P3 paper rows remain pending by design** — see § 2._

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
| 4 | **District count.** README says "11 service districts and 67 counties"; Report 12581 ¶9 says fifteen districts as of January 1995. HRS reorganized more than once. Establish which year each figure describes and say so. | 12581 ¶9 | README, main report, topology paper | **P2** |
| 5 | **Auditor General workpapers are not public records.** s. 11.45(4)(c), Fla. Stat. Any text treating them as obtainable by records request is wrong; release requires a majority vote of the Legislative Auditing Committee after a public hearing. | s. 11.45(4)(c) | Main report Appendix A (**fixed Aug 23**), COLLECTION-PLAN, records-requests file | **P2** |
| 6 | **"Offloaded to" vs "hosted on."** Report 12581 says the 3090 "is utilized for … data communications." It does not say the workload was moved off the ES9021. Use *hosted on* unless a document establishes a transfer. | 12581 ¶9 | Anywhere the two-host configuration is described | **P2** |

### New documentary facts to propagate

| # | Change | Source | Targets | Priority |
|---|---|---|---|---|
| 7 | **Award date November 28, 1988.** EDS selected as prime contractor. New to the archive; independently stated in two reports. | 12581 ¶8, 13287 p. 13 | CHRONOLOGY, main report, Unisys Protests | P3 |
| 8 | **Webster Report and Recommendations issued August 14, 1995** — two days before the press coverage the archive cites. Arbitration ran January 9 to April 1995; proposed recommended orders May 8, 1995; exceptions filed by both parties. | 12581 ¶17 | CHRONOLOGY, main report § 6, Addendum | P3 |
| 9 | **Final Judgment for EDS March 22, 1996**, Circuit Court of the Second Judicial Circuit, Leon County, on the Special Master Final Report. Settlement April 30, 1996. | 13043 p. 2 | CHRONOLOGY, main report | P3 |
| 10 | **Litigation dates.** EDS filed suit August 21, 1992 against HRS *and Comptroller Gerald A. Lewis*; HRS moved to dismiss September 14, 1992; Department counter-sued September 21, 1993; suit held in abeyance December 1993; parties agreed to arbitrate July 1994. | 12581 ¶¶16–17, 13043 p. 2 | CHRONOLOGY | P3 |
| 11 | **Settlement itemization.** $42,800,000 = District Equipment $19,446,676 + Central Processing Equipment $13,188,325 + Federal Certification $3,270,545 + Computer Usage Charges $1,078,602 + CSE Programming $(229,413) + **Liquidation Damages $1,517,000** + Negotiated Costs $4,528,265. Federal allocation $38,271,735. | 13043 p. 2 | Main report Appendix B, lessons study | P3 |
| 12 | **Three companies bid, not two.** Third bidder unidentified. Add to open research items. | 12581 ¶8 | Main report § 8, Unisys Protests, COLLECTION-PLAN | P3 |
| 13 | **EDS subcontractors named:** IBM, Deloitte and Touche (formerly Touche Ross), IV-D Systems Inc., MIS Software Development Inc. (MSD), Florida State University. The archive has treated this as an EDS/IBM pairing. | 12581 ¶8 | Main report, Unisys Protests | P3 |
| 14 | **Contract type: "a fixed price, single vendor contract"** covering development, hardware, telecommunications network, training, conversion, implementation, and facilities management. Load-bearing for the undersizing argument. | 12581 ¶8 | Main report § 7 (**applied Aug 23**), lessons study, Addendum | P3 |
| 15 | **Cost series.** $81.1 million projected March 1989; ~$118 million spent through September 1993; $196 million projected through September 1995 (Sept. 1994 APDU); $310,621,339 through FY 1996-97. **The $81.1M does not reconcile with the $107.66M bid — carry the discrepancy, do not resolve it.** | 12581 ¶12, 13287 p. 14 | Main report Appendix B, CHRONOLOGY | P3 |
| 16 | **Response-time series with dates and mechanism.** Minutes June 1992 → 8 sec January 1994 → 4 sec June 1994 → 3 sec December 1994, with the June 1994 concurrent-user cap and night/Saturday scheduling bracketing the 8→4 improvement. The gains were partly demand suppression. | 12581 ¶47 | Main report, Making It Workable, lessons study, README | **P2** |
| 17 | **1995 two-host configuration.** ES3090/600J for training, development, and data communications; ES9021/982 for production, installed April 22–23, 1995 at $5,438,079.75, replacing an ES9021/900 "deemed inadequate." New CPU at 90–97.5 percent on six of eight processors as of May 1, 1995. ~16,000 network devices January 1995. 37 PA and CSE modules May 1995. | 12581 ¶¶9, 23, 49 | Main report § 4a (**applied Aug 23**), topology paper, README | P3 |
| 18 | **1998 configuration.** Three IBM mainframes — ES9021-982, 9672-R83, 9672-R44 — in a Sysplex; IMS; COBOL; RACF; OS/390 April 1998; CA-7 scheduling; Endevor/INFOMAN; 1,774 production programs; 33 modules. No 3090. Note that a 3090 cannot host a coupling facility, so the Sysplex postdates the 3090's retirement. | 13287 pp. 15–16, 26, 37 | Topology paper, README, main report | P3 |
| 19 | **Unisys ran the FLORIDA programming shop.** September 22, 1995 agreement, amended 13 times, ceiling raised from $41,513,980 to ~$58,663,980, extended to September 21, 1999; 154 support staff. The bidder that lost by 4.4 points maintained the winner's system. | 13287 pp. 38–39 | Main report § 7, memoir, Unisys Protests | P3 |
| 20 | **The 1995 protest repeats the 1989 pattern.** Deloitte and Touche protested the HRS award to Unisys; DOAH hearing officer found for the protester May 12, 1995; a Substitute Secretary from the Governor's office reversed August 10, 1995 because the HRS Secretary was a material witness. Emergency purchase approved February 22, 1995 before resolution. **Structural resemblance only — different procurement, different posture. Do not overstate.** | 12581 ¶¶18–21 | Unisys Protests, memoir | P3 |
| 21 | **Prior Auditor General reports identified.** 11178 (March 1, 1989), 11619 (April 23, 1991), 12061 (May 4, 1993), 12363 (FYE 6/30/1993), 12565 (FYE 6/30/1994), 13256 (FYE 6/30/1997, issued 5/29/1998). **12061 is the key one** — 12581 is its follow-up and cites its ¶¶49–59 on capacity and response times, placing the failure in the auditor's hands in May 1993. | 12581 pp. 27, 45; 13287 | Main report § 8 (**applied Aug 23**), SOURCES, COLLECTION-PLAN, CHRONOLOGY | **P2** |
| 22 | **Operational scale figures.** 1.4 million outstanding alerts January 14, 1995 (net +1.1 million since August 1992); 561 PA and 107 CSE top-priority problems outstanding January 20, 1995; 11,398 open-case members matched to death records, 35 percent of a 199-record sample still active. Federal conditional certification April 28, 1993 with 11 areas needing improvement. | 12581 ¶¶30–35, 56–60, 67–72, ¶14 | Main report § 4, lessons study | P3 |
| 23 | **Property records gap.** No SAMAS property entries for EDS-contract equipment between April 1992 and May 1995 — three years in which the State did not record what it owned. ~$30.3 million of FLORIDA mainframe equipment received FY 1991-92 to FY 1993-94 and not recorded until FY 1994-95. | 13043 p. 6, 12656 | Main report, lessons study | P3 |
| 24 | **Eight freely published Auditor General reports mirrored** — 2011-141, 2013-005, 2014-196, 2017-009, 2019-022 (FLORIDA System IT audits), 2011-082 and 2013-182 (Northwood Shared Resource Center data centre), 2016-046. **None has been read.** 2013-005 is contemporaneous with ITN 03F12GC1 and the best remaining substitute for the lost as-built figures; the two data-centre audits are the best candidates for hardware and disaster-recovery detail. | Mirrored August 21 | SOURCES, COLLECTION-PLAN; read before next sweep | **P2** |
| 26 | **Selection-committee documentation was defective.** ¶29–32: the Department did not provide completed conflict-of-interest questionnaires for the seven selection-committee members, and the final evaluation report "was not prepared or signed by any members of the evaluation committee. Rather, the report was prepared by the Department's management staff based on the records and documentation prepared/maintained by the evaluation committee." Auditor's finding, in 1993 — a documentary basis for revisiting the press's "improper favoritism" language. | 12061 ¶¶29–32 | Main report § 3 (procurement), Unisys Protests, memoir; consider a note in the archive's account of the 1993 press coverage | **P2** |
| 27 | **The $9.15M IBM ES9021/900 acquisition, sequenced.** ¶18–21: installed August 1992 "on a trial basis" under July 28 and 31, 1992 correspondence *before* ITRPAC review and DMS approval; ITRPAC recommended approval December 29, 1992; written agreement January 26, 1993; State paid $9,150,000 February 12, 1993. EDS petitioned January 14, 1993 to reconsider, "premised upon use of funds intended to be paid to EDS." ¶21 in terms: **"The Department's acquisition of computer equipment from IBM is currently the subject of an investigation by the Office of the State Attorney of the Second Judicial Circuit."** Dates the State Attorney investigation to before May 4, 1993 — the piece the LA Times of May 2 was chasing. Note: this is $9.15M, not the $5.1M figure the press used; those are different transactions. | 12061 ¶¶18–21 | Main report § 4 / § 6, CHRONOLOGY, memoir | P3 |
| 28 | **The ¶49–59 problem-resolution finding, in the auditor's hands in September 1992.** ¶¶83–88: of 180 potential problems sampled, 74 of 126 PA-component issues (59%) and 29 of 54 CSE-component issues (54%) unresolved for 3–15 months; 27 of 74 with no action for approximately three months as of the review. This is what Report 12581 later cites as evidence that the failure was documented years before the press found it. Ties directly to lessons study on delayed remediation. | 12061 ¶¶83–88 (Report 12581 cites as ¶¶49–59) | Lessons study, main report § 4, README | **P2** |
| 30 | **Measured availability shortfalls, 1992, and the 2.8-minute response test.** Availability 94% (Feb 29–Mar 29, 1992), **80.5%** (Mar 30–Apr 28, 1992), 97.9% (Apr 29–May 28, 1992) against a 97% requirement. A manual response-time test on **May 13, 1992** averaged **2.8 minutes** against a 1–8 second specification. First audit-measured performance data in the archive; supersedes press characterisation. | 12061 ¶¶49–59 | Main report § 4 and § 4a, lessons study, CHRONOLOGY | **P2** |
| 31 | **The Department's contemporaneous theory of the capacity failure.** Finding #5 response: EDS "postponed and rescheduled these deliverables, thereby delaying the tests, until they were useless, since the system had already experienced performance problems and system unavailability." Plus the concession that "Management Systems staff then focused upon the identification and correction of production problems, rather than modeling capacity needs." The Department's account of causation, on the record in 1993, three years before the settlement. An **October 4, 1991 MOU** modified the benchmark obligations and is not reproduced in the report — add to collection plan. | 12061 Exhibit E Finding #5 | Main report § 5 and § 6, lessons study, memoir, COLLECTION-PLAN | **P2** |
| 32 | **The two-mainframe configuration predates the archive's earliest snapshot.** Independent contractor **Advanced Computer Services** analysed the system July–August 1992 and traced initial inadequate response times in part to the **two-mainframe configuration and its communications overhead**. Consolidation to a single ES9000/720 in July/August 1992 was a *remedy*; the 1995 3090/ES9021 split seen in 12581 is a later re-splitting, not persistence of the 1988 design. Extends the topology paper's lineage backward. **Kastner reading, September 5, 2026:** the interconnect was not free — the two machines consumed a meaningful share of their own capacity talking to each other, so the July/August 1992 consolidation recovered capacity that had been going to inter-machine communication rather than user work. Consistent with ACS's communications-overhead finding. | 12061 ¶¶18, ¶¶49–59; Kastner reading 9/5/2026 | Topology paper, main report § 4a, README | **P2** |
| 33 | **~$28 million Medicaid improper-payment exposure — the largest dollar figure in the archive tied to a control failure.** ¶¶128–132: individuals no longer eligible for Medicaid not timely removed from FMMIS eligible-client records; roughly 200,000 ineligible individuals. Discovered *after* audit fieldwork closed. **Carry the qualifier**: the finding describes an exposure, not a documented improper-payment total for a fixed period. | 12061 ¶¶128–132 | Main report cost-of-failure accounting, lessons study | P3 |
| 34 | **EDS's pleaded claim was ~$46.5M; the settlement paid $42.8M — roughly 92 percent.** ¶15 itemises the August 1992 complaint: $35,962,648.21 equipment/software plus interest; >$4.5M extra work; >$3.2M certification withholdings; >$1.1M computer usage; >$246K CSE assistance; >$1.5M penalties; interest at 1%/month after 40 days. Recharacterises the settlement — the archive reads it as a loss on the merits, which it was, but the number attached is now visible as most-of-what-was-asked. Also ¶37: the Department withheld **$3,516,901** on incomplete Tasks 7 and 17. | 12061 ¶15, ¶37; 13043 p. 2 | Main report Appendix B and § 6, lessons study | **P2** |
| 35 | **Operational control failures new to the archive.** Finding #15: **2.6 million** undeleted alerts by July 1992; purges of **1,477,090** (July 19, 1992) and **879,974** (August 27, 1992); purge approval itself undocumented. Finding #14: **~$900,000** in duplicate AFDC payments in August 1992 alone, 3,326 instances, from the Transitional Issuance File conversion gap. Finding #17: application programmers doubling as security-administrator backups, corrected November 3, 1992. Finding #24: incompatible duties in eligibility determination, triggering an employee fraud-prevention task force. Finding #6–7: Food Stamp certifications extended without federal authorization; Department cites **162.5% caseload growth 1987–92 against 3.7% staffing growth** — quote as the Department's framing of the QC error spike, not the auditor's, and not as a frame for the capacity failure. | 12061 Findings #6, #7, #14, #15, #17, #24 | Main report § 4, lessons study, memoir | P3 |
| 36 | **DOCUMENTED, PROMOTED — the benchmark data delivery was a box-check.** ¶57 verbatim: *"We noted that except for benchmark/capacity data submitted by EDS to the Department in April 1992, no benchmark/capacity tests were conducted by EDS or the Department prior to May 31, 1992, the date EDS ceased its participation in implementation of the FLORIDA System."* One data submission from EDS in April 1992, then EDS departed on May 31, 1992. No tests were conducted before departure. The Auditor General also documents (¶57) that Department–EDS correspondence from **January 30, 1991 through May 12, 1992** shows the Department repeatedly requesting benchmark/capacity data and being "not satisfied that the appropriate data had been provided." So the pattern is 16 months of unsatisfied data requests, one submission in April 1992, and departure six weeks later. Kastner's original reading (analyst, September 5, 2026): a box-checking move creating a paper trail for the exit. The record supports it. | 12061 ¶57 | Main report § 5, lessons study, memoir | **P2** |
| 36b | **Legal fees on the EDS lawsuit as of March 17, 1993: $189,347.** ¶58. Small dollar figure but the first attested legal-cost data point for the litigation the archive has. | 12061 ¶58 | Main report Appendix B, memoir | P3 |
| 36c | **Kastner synthesis, September 5, 2026 — the exit sequence, not merely late compliance.** Setting the ¶57 record beside what the archive already establishes about the capacity-assumption error EDS discovered internally in March 1991 (established in the Webster arbitration, unknown to the auditor in 1992–93), the pattern reads as a deliberate multi-quarter exit sequence rather than as a failing performance under strain: (a) **March 1991** — EDS internally discovers the transaction-volume error underpinning its own bid sizing; (b) **January 30, 1991 – May 12, 1992** — 16 months of Department requests for benchmark/capacity data that EDS did not satisfy; (c) **October 4, 1991** — MOU signed, released EDS from evidence of successful tests for implementation stages already completed, waived liquidated damages for benchmark-test delays, and stated its purpose as "the amicable termination of the contractual relationship" — meaning the exit was being planned in writing seven months after the internal discovery; (d) **April 1992** — one benchmark data submission, the only one before departure; (e) **May 31, 1992** — EDS ceases participation; (f) **August 21, 1992** — EDS files suit for $46.5M. Six weeks between departure and complaint suggests a substantial period of pre-drafting. The auditor could not see this pattern in 1992–93 because the March 1991 internal discovery did not surface until Webster. **Recorded as analyst synthesis linking documented items across multiple sources; label as such in any paper that quotes it.** Sequence is documented; the *intent* it suggests is inference. The distinction has to travel with the argument. | 12061 ¶57; Webster arbitration record (via 12581 § litigation and 13043); Kastner synthesis September 5, 2026 | Main report § 5, § 6, memoir, lessons study | **P2** |
| 38 | **PARTIALLY APPLIED 2026-09-06 (COLLECTION-PLAN done; paper-side pending).** **11178 and 11619 are NOT systems audits — correct the archive's expectation.** 11178 (3/1/1989) is a management-controls audit; ¶3 lists ten control areas and data processing is not among them. 11619 (4/23/1991) is scoped to institutional fees, client trust funds, and an OSS follow-up. Full-text search of 11619 finds **zero** occurrences of FLORIDA System, EDS, IBM, RFP, APD, DHHS/FNS/ACF, Food Stamp QC error rate, or AFDC caseload — despite an audit period straddling the RFP release, the EDS award, and contract signing. **The pre-FLORIDA operational baseline the archive wanted is not in either report.** Anywhere the collection plan or main report describes these as pre-FLORIDA operational baselines, correct it. | 11178 ¶3; 11619 ¶3 | COLLECTION-PLAN, main report § 8, README | **P2** |
| 39 | **The pre-FLORIDA architecture, documented in three patterns.** (a) **MORS**: paper HRS Form 2012 → centralized keypunching at the Jacksonville Data Center → monthly computer tape → Comptroller prints warrants → payroll-by-exception; *"the MORS does not generate a turnaround document"* [11178 ¶49]. (b) **Income Verification (IVS)**: requests *"prepared manually… batched and forwarded to the HRS Technology Center for keypunching. Responses are returned… in the form of computer printouts which are separated and mailed"* [11619 Ex. E ¶¶54–57]. (c) **The software's age**: *"The software package was purchased in 1976 and has been extensively modified periodically to maintain the current service level"* and *"We believe the only accurate record keeping that can be done is outside the system"* [11619 Ex. E ¶¶74–77]. Batch-oriented, paper at both ends, 14-year-old package the Department said required record-keeping outside it. This is what FLORIDA replaced. | 11178 ¶49; 11619 Ex. E ¶¶54–57, ¶¶74–77 | Main report § 3, topology paper, lessons study, memoir | **P2** |
| 40 | **The 3.7% staffing-growth claim is now testable.** 12061 Finding #7 Management Response cites "162.5% caseload growth from 1987–1992" against "3.7%" staffing growth. 11178 ¶18 supplies the 1987 denominator: **Economic Services 6,487.69 filled of 6,828.85 authorized FTE at June 30, 1987**. 11619 ¶22 gives HRS-wide at 6/30/89: 42,460.53 authorized / 39,132.30 filled, Economic Services 7,467.05 / 7,024.50, Management Systems 310.00 / 276.00. **Check the 3.7% against these before quoting it in any paper.** Note the Economic Services number rose from 6,487.69 (1987) to 7,024.50 (1989) — about 8% in two years, which does not obviously square with 3.7% over five. | 11178 ¶18; 11619 ¶22; 12061 Finding #7 | Main report § 4 and § 7, lessons study | **P2** |
| 41 | **The BVS commitment-and-failure sequence across four audit cycles.** 11619 ¶128: *"Department personnel stated on July 20, 1990, that a quarterly computer match… would be instituted."* First recommended 1989 (11178, per 12061's citation — but see row 42). Promised July 1990. Still open in 12061 (1993, Finding #9). Still open in 12581 (1995). Also 11619 ¶124: MORS paid **771 cases, 4,957 warrants, ~$129,000 after death; 79 still generating warrants November 1989.** Establishes the Department's baseline behavior on audit commitments — context every reader of the FLORIDA settlement should have, independent of FLORIDA itself. | 11619 ¶124, ¶128 | Main report § 4, lessons study, memoir | **P2** |

### Records-request state

| # | Change | Source | Targets | Priority |
|---|---|---|---|---|
| 25 | **DCF holds no responsive records** for RFP 88-74-BC, the Evaluation Manual, the EDS contract, the Webster report, or the settlement (reference P257883-072926, August 2026). Consistent with a five-fiscal-year bid-records retention that expired around 1994. Follow-up sent August 20 seeking the Rule 1B-24.003(9)(d) disposition documentation and any State Archives accession. **The state-agency branch for the RFP is closed pending that answer; the federal APD file is now the most likely surviving custodian.** | DCF response | COLLECTION-PLAN (applied), main report § 8, Addendum | **P2** |

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

