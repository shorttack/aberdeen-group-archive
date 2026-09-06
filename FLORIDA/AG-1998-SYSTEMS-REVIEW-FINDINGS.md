# What the Auditor General Delivery Changes

*Prepared August 21, 2026, from four reports supplied by the Florida Auditor General's office on August 11, 2026 in partial response to the § 1 request of July 28, 2026. Source scans are Tesseract OCR of the office's PDFs; page citations are to the OCR page markers, which differ from the reports' printed pagination. Full extractions are in `_working/AG-13287-extraction.md` and `_working/AG-12583-12656-12886-extraction.md`.*

The delivery is Report Nos. 12583, 12656, 12886, and 13287. It does not include 12581 or 13043, which were the two the request actually led with. That gap is discussed in `FLORIDA-records-requests-drafts.md` § 1a.

One of the four is a substantial find. **Report No. 13287** is a systems review of the FLORIDA System itself, conducted September 1997 through January 1998 and issued July 27, 1998 — the first document in this archive that describes the as-built machine from the inside, by an auditor with access to it, rather than by inference from a bid protest. Two of the others are thin and one is empty; that is recorded below rather than glossed.

---

## 1. Corrections the archive must make

### 1.1 The cost figure is wrong by $65 million

The archive has carried **$245.3 million** as a documented cost floor, described as a 128 percent overrun on the $107,658,141 EDS bid. Report 13287 supersedes it:

> "Through the 1996-97 fiscal year, the Department estimates the total cost of the FLORIDA System, including nonrecurring as well as recurring costs, to be $310,621,339." [13287, p. 14]

That is the Department's own estimate, reported by the Auditor General, through a stated cutoff. Against the EDS bid it is a **188 percent overrun**, and it is a floor rather than a total — it stops at FY 1996-97, before the Unisys support agreement grew to roughly $58.7 million and before three decades of continued operation.

The $245.3 million figure should be retired wherever it appears, with the substitution noted rather than made silently. This is the second time in this project a number has been carried forward on weaker sourcing than was available; the first was the model-versus-assumptions substitution recorded in the README methodology note.

### 1.2 The settlement now has a date and an auditing authority

> "On April 30, 1996, the State of Florida entered into a settlement agreement with EDS, which required the Department to pay EDS $42,800,000." [13287, p. 16]

The archive has described this as the "1996–97 settlement" and the amount as "$42 million plus interest." The date is **April 30, 1996**, and the figure is **$42,800,000**. Report 13287 further states that Auditor General **Report No. 13043**, issued August 25, 1997, reviewed the settlement and contains a breakdown of the $42.8 million [13287, p. 16]. That confirms 13043 is exactly what the archive hoped it was, and makes its absence from this delivery the delivery's biggest gap.

### 1.3 EDS left in 1992, not at the settlement

> "EDS' participation in the development and implementation of the FLORIDA System ceased on May 31, 1992." [13287, p. 16]

A date the archive did not have. It places EDS's departure four years before the settlement and roughly fourteen months after the March 1991 internal discovery of the capacity-assumption error.

---

## 2. The as-built machine, documented at last

Every architectural statement in the archive to date has been inference from the 1988–89 protest record, with a single attested element in the branch-controller note. Report 13287 states the 1998 configuration directly.

| Element | As stated in Report 13287 | Page |
|---|---|---|
| Processors | "three International Business Machines (IBM) mainframe computers" — an **ES9021-982**, a **9672-R83**, and a **9672-R44** | 15 |
| Coupling | "linked together in a Sysplex environment" | 15 |
| Database | "The Information Management System (IMS) database management system" | 15–16 |
| Language | COBOL | 15–16 |
| Security | IBM RACF at the system level; application security inside FLORIDA itself | 16 |
| Operating system | "made Year 2000 compliant with the implementation of the OS/390 operating system in April 1998" | 26 |
| Batch scheduler | "job-scheduling software (CA-7)" | 35 |
| Configuration management | Endevor, with INFOMAN for tracking; the interface between them manual | 30–31 |
| Application scale | 1,774 programs in Production; 313 of them also in Acceptance (17.64%) | 37–38 |
| Modules | 33 PA and CSE modules as of March 13, 1998 | 13 |
| Design intent | "the creation of a single, centralized data processing system" | 13 |

**IMS and COBOL are confirmed. The centralized topology is confirmed, and confirmed in the auditor's own words as a design intent rather than an outcome** — which is the finding the topology paper wanted and could not get. That sentence is worth quoting whole.

Two cautions before any of this is used.

**This is 1998, not 1989.** The three-machine Sysplex is not the machine EDS proposed or the machine the capacity model sized. The 1989 award was an IBM 3090; the ES9021 and the two 9672s are successors. What the report documents is where the upgrade path arrived, not where it started, and it says nothing about when or why each step was taken. The archive should present this as the as-built system at the ten-year mark and resist the temptation to read it backward into 1989.

**The report does not name IMS-TM.** It names IMS as the database management system and nothing more. The archive's IMS-TM claim remains inference and must not be upgraded on the strength of this document. The extraction flags this explicitly.

### What Report 13287 does not contain

Stated plainly, because the absences matter as much as the content. **No CPU-utilization figure. No design ceiling. No response-time measurement. No availability percentage. No capacity model or sizing method. No SNAP/SHOT reference. No IBM 3090 reference. No database count, no OSAM or VSAM count, no data volume. No terminal, workstation, office, or district count. No caseload figure. No disaster-recovery or backup-site arrangement. No RFP number, and no quotation from the RFP or the EDS contract.**

The report's own audit objective refers to "the system availability and capacity inefficiencies experienced in the FLORIDA System, as disclosed in audit report No. 12581" [13287, p. 10] — and then reports on the Department's corrective actions without restating the numbers. **Report 12581 therefore remains the sole documentary source for the 95–100 percent CPU utilization claim, and 12581 was not delivered.** The archive's most-cited performance figure still rests on press coverage of a report nobody in this project has read.

---

## 3. The procurement chronology, independently corroborated

Report 13287 restates the procurement from a source entirely outside the DOAH record:

> "FDHRS management issued a Request for Proposal (RFP) on May 20, 1988, to acquire a Statewide on-line integrated system through competitive solicitation and selected Electronic Data Systems Federal Corporation (EDS) as the prime contractor on November 28, 1988." [13287, p. 13]

> "This action arose out of disputes relating to a written contract, dated May 15, 1989, between EDS and the Department for the implementation of the FLORIDA System." [13287, p. 16]

The May 20, 1988 RFP date and the May 15, 1989 contract date now have a second, independent source. The **November 28, 1988 award date** is new to the archive and should go into `CHRONOLOGY.md`. Note what this date does to the protest timeline: DOAH 88-2942BID, the specifications protest, was decided before award; 89-0003BID, the award protest, followed it.

---

## 4. The finding nobody was looking for

**Unisys ended up running the FLORIDA programming shop.**

Report 13287 documents a September 22, 1995 three-year agreement with Unisys for application-programming staff, amended thirteen times by June 5, 1998 and extended through September 21, 1999, with the ceiling rising from no more than $41,513,980 to approximately **$58,663,980**; invoices through January 30, 1998 totaled $32,922,430.62. The start-up task alone staffed 36 senior programmer analysts, 49 programmer analysts, 20 programmers and a database analyst, and the support task was to furnish **154 support staff** [13287, pp. 38–39].

Unisys is the bidder that lost RFP 88-74-BC on 4.4 points out of 350, protested twice, warned about the schedule and the response times, and had its expert discounted for incomplete understanding of the IBM modeling programs. Seven years later the State was paying it upward of $58 million to maintain the system it lost.

The audit's criticism is that the Department renewed at $17.5 million a year without ever comparing alternatives [13287, pp. 38–40]. The Department's reply is worth having: it said its own analyses showed state employees were cheaper than contractors, but that funding and salary competitiveness were the barriers [13287, pp. 66–67].

This is not evidence about the 1988–89 procurement and should not be presented as such. It belongs in the memoir and in the longitudinal narrative as what the market did next.

---

## 5. The 1998 audit's own verdict

The report is not a clean bill of health. It identifies two material weaknesses and closes on this:

> "The deficiencies described within this report continue to demonstrate significant inadequacies in the internal control of the FLORIDA System relative to the development, implementation, and operation of an information system intended to process billions of dollars of program benefits." [13287, p. 54]

Selected findings bearing on the archive's argument that the system's problems were structural rather than incidental:

- **Change requests aged 15.1 months on average.** Of 99 CSE Financial Management change requests outstanding in July 1997, 92 were still outstanding in January 1998 — 93 percent — and 60 of those were high priority [13287, p. 32]. The report expressly notes this as a repeat of findings in **Report No. 12581 ¶¶56–60 and Report No. 12061 ¶¶83–87** [13287, p. 31]. Three audits, same finding.
- **1.2 million transactions had gone unprocessed for years.** On August 29, 1997 the Department used emergency fix and override procedures to begin processing "approximately 1.2 million PA/CSE interface transactions that had not been processed over several years due to a program problem," and the run included erroneous updates [13287, p. 36]. Also a repeat finding, from 12581 ¶¶93–98 and 12061 ¶¶134–138.
- **The system could not be reconciled to the State's books.** FLORIDA recorded $462,035,883 in CSE collections for FY 1996-97 against $553,540,733 in FLAIR/SAMAS, a $91.5 million divergence, and "The FLORIDA System does not provide the capability to accomplish this reconciliation" [13287, pp. 43–45]. One of the two material weaknesses. Three CPA firms were engaged to reconcile July 1994 through June 1998.
- **The design could not answer the questions the Legislature asked of it.** FLORIDA could supply only five of twelve baseline CSE performance measures required by Chapter 97-170, and the 1998 Legislature reduced the requirement because the data did not exist. The auditor's own sentence: "The FLORIDA System, as then designed, could not provide FDOR management with the statistical data needed to develop the baseline measures" [13287, p. 46].
- **Medicaid paid for the dead.** $361,665 paid for dates after death for 634 deceased people in a single quarter, October–December 1997, with a further $163,545 found on a re-check of 80 records [13287, pp. 48–50]. This connects directly to the recurring pre-1995 findings, referenced in contemporaneous press coverage, that HRS was not matching welfare records against Bureau of Vital Statistics death records.

---

## 6. Two report numbers the archive did not know existed

Report 13287 cites both repeatedly.

**Report No. 12061** is the significant one. It is an earlier audit of the same system, cited at ¶¶83–87, ¶¶128–132, ¶¶134–138 and ¶¶139–143 on exactly the subjects 12581 and 13287 later revisited — delayed problem resolution, emergency change control, reference-table authorization, and approximately $28 million in improper Medicaid benefits. It does not appear on the Auditor General's online listings, whose archived coverage begins with FY 1995-96 ([Auditor General archived reports](https://flauditor.gov/pages/archived_reports.html)), so it predates September 1995. **A pre-1995 systems review of the FLORIDA System is precisely what the § 1 request asked for when it asked about the 1989, 1991, and 1993 audits, and it now has a number.** It should be requested by number immediately.

**Report No. 13256** is "State of Florida — Federal Awards Programs," FYE 06/30/1997, issued May 29, 1998 ([FY 1997-98 report listing](https://flauditor.gov/pages/list9798page.htm)) — the statewide federal single audit, cited here for CSE control deficiencies including the absent SAMAS-to-FLORIDA reconciliation. Lower value, but identifiable and probably online.

The same listing independently confirms **Report No. 13043**, "HRS Settlement of FLORIDA Contract with EDS," audit period 07/01/1995–12/31/1996, issued 08/25/1997 — the report the § 1 request named first and the delivery omitted.

---

## 7. The other three reports

Honest accounting, since two of these produced almost nothing.

**Report No. 12656** (Operational Compliance Audit of HRS, April 1993 – March 1995, issued February 20, 1996) has one item worth having:

> "The FLORIDA System mainframe equipment that was received by the Department prior to July 1, 1994, but added to the property records during the 1994-95 fiscal year, totaled approximately $30.3 million, which included approximately $10.3 million in CEFP purchases."

Mainframe equipment received during FY 1991-92 through FY 1993-94 was not entered into the State's property subsystem until FY 1994-95. Two uses: it is a hardware-spend figure for the upgrade era, and the delayed recording is itself a control finding on a project already under investigation. It bears on — without resolving — the reported 1993 grand jury interest in a $5.1 million hardware upgrade.

**Report No. 12886** (Operational Audit of HRS, April 1995 – March 1996, issued January 14, 1997) contains nothing on FLORIDA, EDS, IBM, eligibility error rates, or federal sanctions. Its one adjacent item is an audit of fifteen Information Technology Resources contracts totaling $46,007,427.78 with deficient approval, recording, and payment controls.

**Report No. 12583** (Review of the HRS Inspector General/Internal Audit Function, April 1994 – March 1995, issued September 18, 1995) contains nothing on the topic at all. It does record that 30 percent of Inspector General effort went to quality control reviews and audits of public assistance determinations. Documented negative; no further action.

---

## 8. Handling and caveats

These are OCR transcriptions, not the source PDFs. Before any figure from this document is published:

1. **Verify against the PDF image.** The extraction files list specific OCR hazards. The most important: on 13287 p. 15 the three processor models read cleanly as ES9021-982, 9672-R83 and 9672-R44 and the OCR shows no "3090" anywhere — do not let familiarity substitute the wrong model. The Exhibit C department responses at pp. 62–70 are heavily corrupted and their dates should not be quoted.
2. **Commit the PDFs, not only the markdown.** The whole lesson of the ITN 03F12GC1 404 is that a document you can currently reach is not a document you have preserved. These four came from an office that does not publish them online.
3. **Cite the printed report pagination, not the OCR marker,** in anything for publication. The two differ by roughly eight pages in 13287.
4. **Nothing here has been reconciled against `CHRONOLOGY.md`, `SOURCES.md`, or the five published papers.** The corrections in § 1 above are identified, not yet propagated. That is the next task and it should be done as one pass, the way the model-versus-assumptions substitution was.

## Sources

- Florida Auditor General, Report No. 13287, *Systems Review of the Florida Department of Children and Family Services, Florida On-Line Recipient Integrated Data Access (FLORIDA) System, Selected General and Application Controls*, period September 2, 1997 – January 30, 1998, dated July 27, 1998. Supplied by the Auditor General's office August 11, 2026; not available online.
- Florida Auditor General, Report No. 12656, *Operational Compliance Audit of the Florida Department of Health and Rehabilitative Services*, period April 1, 1993 – March 31, 1995, dated February 20, 1996. Same provenance.
- Florida Auditor General, Report No. 12886, *Operational Audit of the Florida Department of Health and Rehabilitative Services*, period April 1, 1995 – March 31, 1996, dated January 14, 1997. Same provenance.
- Florida Auditor General, Report No. 12583, *Review of the Office of Inspector General/Internal Audit Function of the Florida Department of Health and Rehabilitative Services*, period April 1, 1994 – March 31, 1995, dated September 18, 1995. Same provenance.
- [Florida Auditor General, archived report listings](https://flauditor.gov/pages/archived_reports.html) — establishes that online coverage begins with FY 1995-96.
- [Florida Auditor General, FY 1997-98 report listing](https://flauditor.gov/pages/list9798page.htm) — Report 13043 and Report 13256 entries.
