# The Pre-EDS Record

*Prepared September 5, 2026, on Auditor General Report No. 12061, "Systems Review of the Florida Department of Health and Rehabilitative Services, Florida On-Line Recipient Integrated Data Access (FLORIDA) System," for the period April 1, 1992 through October 14, 1992, and selected Department actions through February 12, 1993. Dated May 4, 1993. Audit supervised by Jonathan Ingram; audit made by Tina Greene; Auditor General Charles L. Lester. Supplied by the Auditor General's office September 5, 2026 as an image PDF, OCR by `ocr_pdf_v1.sh` at 300 dpi. Companion to `AG-12581-13043-FINDINGS.md` and `AG-1998-SYSTEMS-REVIEW-FINDINGS.md`. Full extraction is in `_working/AG-12061-extraction.md`.*

12061 is the report the archive has been building toward since July. Report 12581 describes itself as a follow-up to it. The August 1995 press coverage the archive has been leaning on takes its shape from findings first made here. This is the primary source for the pre-1995 record, and reading it changes the shape of the argument the archive can make. Two things worth flagging first, before the ordinary findings-note structure.

---

## 1. The RFP had a performance standard, and it had a number

**This overturns the archive's central structural claim.**

The archive has been arguing — carefully labeled as inference from silence in the appellate record — that RFP 88-74-BC specified no quantified throughput, response-time, availability, or utilization-headroom standard, and that the platform undersizing was structural because there was no numeric target against which to size. That inference is now wrong, and 12061 has the numbers:

> the contract required that **at least 95% of the time**, response fall within **1–8 seconds**, measured every 15 minutes at a random day/workstation on a monthly basis. Availability was required to be **at least 97%** over rolling 30-day periods. [¶¶49–59]

The contract carried a two-part quantified performance standard. Not silence. Not procedural boilerplate. A response-time SLA with a measurement protocol, and an availability SLA with a measurement window.

That changes several claims in the published papers, and this correction has priority over almost everything else in the pending log. See § 8 below for propagation.

**But it does not overturn the argument the archive is actually making.** The standard existed and was not held. Measured availability for the first three months the audit examined:

| Period | Availability | Required | Result |
|---|---|---|---|
| Feb 29 – Mar 29, 1992 | 94% | 97% | Shortfall |
| Mar 30 – Apr 28, 1992 | **80.5%** | 97% | Shortfall (largest) |
| Apr 29 – May 28, 1992 | 97.9% | 97% | Met, first month |

A manual response-time test on **May 13, 1992** produced an average response time of **2.8 minutes** [¶¶49–59] — not two-point-eight seconds, two-point-eight minutes, against a specification of 1–8 seconds. The archive's picture of a system running at minutes-per-transaction in mid-1992 is now grounded in an audit measurement, not press coverage.

The structural argument the archive has been making becomes stronger, not weaker, once phrased correctly. It is not "the contract had no performance standard." It is: **the contract had a performance standard, and the acceptance mechanism that would have enforced it did not run.**

## 2. The Department's own theory of the crisis, in its own words

Finding #5, Management's Response:

> "Correspondence shows that EDS postponed and rescheduled these deliverables, thereby delaying the tests, until they were useless, since the system had already experienced performance problems and system unavailability." [Exhibit E, response to Finding #5]

The Department blamed EDS for postponing the contractually required benchmark and capacity tests until they were meaningless. Combined with the auditor's own recommendation for the same finding — "periodic and timely capacity testing, clear contract specifications on capacity and response time, and documentation adequate to determine compliance, explicitly to reduce the risk of litigation and otherwise adversarial situations" [Recommendation #5] — this is the Department's contemporaneous legal theory of the capacity failure, on the record, in 1993, three years before the settlement.

The archive already has the auditor's finding. It now has the Department's account of who caused it, from before the arbitration. That is a much better position than either alone.

An **October 4, 1991 Memorandum of Understanding** modified the contract's benchmark obligations. The MOU is not reproduced in the report; it is the crux of both parties' legal theories in the ensuing litigation and it belongs on the collection-plan wish list.

The Department also concedes something the archive should quote alongside: "Management Systems staff then focused upon the identification and correction of production problems, rather than modeling capacity needs" [Response #5]. The remediation was reactive during the crisis rather than proactive. That admission comes from the audited party.

---

## 3. The as-built machine and its lineage, filled in

The archive now has three primary-source snapshots of the FLORIDA System hardware — 1992/93 (this report), 1995 (12581), and 1998 (13287) — and they trace a clean lineage that inference had gotten only partly right.

| Period | Production processor | Source |
|---|---|---|
| Pre-August 1992 | Two-mainframe configuration; interim single-mainframe **IBM ES9000/720** (OCR renders "9000/720" and "ES9000/720" inconsistently — see § 9) | 12061 ¶¶18, ¶¶49–59 |
| August 1992 – 1995 | **IBM ES9021/900**, installed "on a trial basis" August 1992, upgraded from the ES9000/720 which "had been deemed inadequate" | 12061 ¶18; 12581 ¶9 |
| April 1995 – 1998 | **IBM ES9021/982**, eight processors, installed April 22–23, 1995 at $5,438,079.75 | 12581 ¶¶9, ¶23 |
| 1998 | **Three-machine Sysplex**: ES9021-982, 9672-R83, 9672-R44; no 3090 | 13287 pp. 15–16 |

Two things the archive did not know until now.

**The two-mainframe configuration predates the archive's earliest snapshot.** An independent consultant, **Advanced Computer Services**, analyzed the system in July–August 1992 and traced the initial inadequate response times in part to the two-mainframe configuration and its communications overhead [¶¶49–59]. This is the earliest documented statement in the archive that the network host was a distinct concern. The August 1992 consolidation to a single mainframe was a *remedy* for that overhead, not the original design. The 3090 / ES9021 pairing seen in 1995 is thus a later re-splitting, not a persistence of the 1988 design.

**Advanced Computer Services was the July–August 1992 consultant.** The archive has been referring to "an independent consultant" — 12581 cited its report of October 11, 1994 without naming the firm. 12061 shows an earlier consulting engagement by the same or similar posture from a firm now named. Whether it is the same firm as the October 1994 consultant is unresolved by the two documents.

---

## 4. The IBM ES9021/900 acquisition and the State Attorney investigation

Full sequence at ¶¶18–21, already logged as PENDING-CHANGES row 27. Complete for the record:

| Date | Event |
|---|---|
| July 28 & 31, 1992 | Correspondence between Department and IBM; Department notified IBM that all aspects of the "potential purchase" were subject to review by the Information Resources Commission, DMS, and the State Comptroller |
| August 1992 | IBM installed the ES9021/900 "initially on a trial basis" |
| December 29, 1992 | ITRPAC met, recommended approval of the acquisition/upgrade; DMS Secretary approved the same day — four months after installation |
| January 14, 1993 | EDS, through counsel, petitioned ITRPAC to reconsider, "premised upon use of funds intended to be paid to EDS," and filed for a s. 120.57(1) administrative hearing in the alternative |
| January 26, 1993 | Department and IBM executed a written agreement "to clarify and resolve various issues arising from the [July] contract"; one term set payment at $9,150,000 |
| February 12, 1993 | State completed payment of $9,150,000 to IBM |

And the sentence that dates the criminal investigation:

> "The Department's acquisition of computer equipment from IBM is currently the subject of an investigation by the Office of the State Attorney of the Second Judicial Circuit." [¶21]

Predates the report's May 4, 1993 issue date. Predates the Los Angeles Times of May 2, 1993 which described a "$5.1 million" upgrade — this is the transaction the LA Times was chasing, at $9.15 million, and named by an auditor. The two dollar figures are not the same transaction and the archive should not conflate them.

---

## 5. The findings the archive did not have

Beyond the three already-logged pending rows (¶¶29–32 selection-committee, ¶¶18–21 IBM, ¶¶83–88 problem resolution), the report contains twenty-four other numbered findings in Exhibit E, most of them new to the archive. The five that matter most:

**Finding #20: ~$28 million Medicaid improper-payment exposure.** ¶¶128–132. Individuals no longer eligible for Medicaid were not timely removed from FMMIS eligible-client records. Discovered *after* audit fieldwork closed. This is the largest dollar figure in the report and the largest dollar exposure yet documented anywhere in the archive for a specific control failure. Roughly 200,000 ineligible individuals on FMMIS. Department response: monthly FMMIS/FLORIDA reconciliation implemented; one further monthly run in May 1993, then quarterly.

**Finding #6–#7: Food Stamp certification periods extended without federal authorization.** ¶¶60–68. Federal fund suspension or disallowance risk. The Department's Response #7 supplies the caseload-versus-staffing frame that reshapes the human account of the crisis: **"During this time of spiraling caseload growth of 162.5% from 1987–1992, staffing increases in the public assistance programs only grew 3.7%."** Note the direction of that argument — the Department is offering the caseload-versus-staffing gap as the frame for the QC error-rate spike, not for the capacity failure. The archive should quote it as the Department's framing, not as the auditor's.

**Finding #15: 2.6 million undeleted alerts, and undocumented mass purges.** ¶¶106–110 area. Full detail: more than **2.6 million** alerts accumulated undeleted as of July 1992; a mass purge of **1,477,090** alerts on July 19, 1992; a second of **879,974** on August 27, 1992. Purges generally applied to alerts 45 days or older, some at 14 days. The finding has a second, distinct deficiency: user-group review and approval of the purges themselves was not adequately documented, so the Department cannot confirm the correct deletions were made. Two months after the crisis the reference year 1998 report also records mass-accumulated alerts (12581's 1.4 million figure), demonstrating the alert-generation problem persisted for years.

**Finding #14: ~$900,000 in duplicate AFDC payments, August 1992 alone.** ¶¶100–104. Adequate controls were not established during conversion from the Transitional Issuance File to FLORIDA. 3,326 duplicate payment instances in the August 1992 sample. Cases referred to Benefit Recovery. This is what running conversion in production without a reconciliation step costs, in one month, in one program.

**Finding #17: segregation of duties failure — programmers were security-administrator backups.** ¶¶118–119. Application programmers doubled as backups to the application security administrators — a canonical audit failure of segregation between the people who write the code and the people who authorize access to it. Corrected effective November 3, 1992. Combined with Finding #24 (employees performing incompatible duties in eligibility determination, ¶¶150–153) which triggered an employee fraud-prevention task force with 22 Human Services Analyst positions dedicated to random case review in six targeted counties, and Finding #21 (undocumented nightly-processing programming changes via fix/override libraries — 814 override-library entries in December 1992, reduced to 290 by April 1993).

---

## 6. Costs the archive now has

Every dollar figure in EDS's August 1992 complaint, itemized [¶15]:

| Component | Amount |
|---|---|
| Equipment and software allegedly delivered | $35,962,648.21 plus interest |
| Extra work outside FLORIDA contract scope | in excess of $4,500,000 |
| Money withheld from implementation-task payments for federal certification | in excess of $3,200,000 |
| Computer usage charges related to change work | in excess of $1,100,000 |
| CSE acceptance-testing and implementation assistance | in excess of $246,000 |
| Penalties wrongfully withheld | in excess of $1,500,000 |
| Interest at 1 percent per month on unpaid amounts more than 40 days after invoice | — |

Total EDS claim as pleaded: on the order of **$46.5 million**, plus interest.

Compare to what EDS ultimately received in the April 30, 1996 settlement: $42,800,000 [13043 p. 2]. **The Department settled for roughly 92 percent of the pleaded claim.** That is a different characterization of the settlement than the archive has been carrying — it has been read as a loss on the merits, and it was, but the number attached to the loss is now visible as most-of-what-was-asked-for.

The Department withheld **$3,516,901** on the incomplete Task 7 (CSE acceptance) and Task 17 (federal certifications) deliverables; these withholdings were themselves among the disputed items in the lawsuit [¶37]. The $9,150,000 for the ES9021/900 was paid on February 12, 1993 [¶19].

---

## 7. What the report is missing

Stated plainly:

- **No specific quotation from the RFP or the contract** on the response-time and availability standards; the numbers are given as narrative in the findings text. The RFP itself remains the ultimate primary source, and it remains unrecovered.
- **No transcription of the October 4, 1991 MOU** that modified the benchmark/capacity-test obligations.
- **No prior Auditor General reports referenced beyond 11178 and 11619**, and those only in Finding #9 on BVS death-record matches. No sibling audits, no companion IT reviews. This is a self-contained systems review whose predecessors are the two death-records audits, no others.
- **A large block of Exhibit E's corrective-action-plan tables (pages ~130–166) OCR'd as mirror-flipped text and is functionally unusable.** Scattered dates and names surface where the reversal was partial. Nothing in this note or in `AG-12061-extraction.md` rests on the garbled region. If the tables matter later, they will need a re-OCR of that page range with orientation correction — or a hand-transcription of a small block.

---

## 8. What this does to the archive

This is a section for the eventual sweep, not action today. Recording it here so the pending log has the anchor.

**The performance-standard claim needs rewriting wherever it appears.** Currently the main report Section 5 argues the RFP specified no throughput or response-time standard. It did. The revised argument is that the RFP specified a two-part quantified standard (1–8 seconds at 95 percent, 97 percent availability over 30 days), that the acceptance mechanism which would have enforced it was postponed by EDS "until [it was] useless," and that the fixed-price hardware bundle nonetheless left the buyer paying for the equipment the vendor's undersizing required. The structural argument survives; the load-bearing sentence changes.

**The as-built lineage should be extended backward.** The topology paper's history should now start with the two-mainframe pre-August 1992 configuration and Advanced Computer Services' finding on its communications overhead, not with the 3090.

**The State Attorney investigation gets a firm date.** Before May 4, 1993, per ¶21 verbatim. The CHRONOLOGY entry for the 1993 investigation gets its documentary anchor here.

**The Department's own theory of the crisis becomes quotable.** Currently the archive has the auditor's finding of the capacity failure. It now has the Department's contemporaneous account, on the record, of who caused it. Both belong in the main report; neither replaces the other.

**The ~$28 million Medicaid finding is new to the archive and larger than anything in it.** ¶¶128–132. Belongs in the main report's cost-of-failure accounting.

Full pending row set added to `PENDING-CHANGES.md`.

---

## 9. Handling

1. **The 12061 PDF and reading-order Markdown are on the Mac** at `~/Desktop/Archive/FLORIDA/PDFs/auditor-general/AG-12061.pdf` (searchable) and `.md`. The sandbox holds a copy of the Markdown at `sources/auditor-general/12061.md`.
2. **Cite paragraph numbers, not OCR page markers**, in anything for publication. The report numbers its paragraphs and the numbers are stable; the Exhibit E marginalia gives paragraph ranges for each of the 27 findings.
3. **OCR caveats to watch**: the ES9000/720 processor model appears as both "9000/720" and "ES9000/720" (§ 9 of `AG-12061-extraction.md`). One dollar figure — the override-library reduction — was rendered "as of April 1992" in a passage that describes a reduction from a December 1992 figure; almost certainly a typo for **April 1993**, flagged rather than corrected. The mirror-flipped table region (pages ~130–166) is functionally unusable.
4. **The 12061 finding on the ~$28 million Medicaid exposure is the largest dollar figure in the archive tied to a specific control failure.** Sight-check the paragraph in the searchable PDF before it goes into any paper, and note that the finding text describes it as an *exposure* — ineligible individuals not timely removed from FMMIS records — not as a documented improper payment total for a fixed period. The dollar magnitude has to travel with that qualifier.

## Sources

- Florida Auditor General, Report No. 12061, *Systems Review of the FLORIDA System*, period April 1, 1992 through October 14, 1992 and selected Department actions through February 12, 1993, dated May 4, 1993. Supplied by the Auditor General's office; scanned image PDF, OCR by `ocr_pdf_v1.sh`. Not available online.
- Florida Auditor General, Report No. 12581. See `AG-12581-13043-FINDINGS.md`. Report 12061 is its predecessor.
- Florida Auditor General, Report No. 11178, dated March 1, 1989, and Report No. 11619, dated April 23, 1991. Both cited in 12061 Finding #9 (¶¶74–77) for the BVS death-record comparison finding, held over from those earlier reports. Held on the Mac; not yet read in full.
- Extraction: `_working/AG-12061-extraction.md`, produced September 5, 2026 by a Claude Sonnet subagent working from the full 168-page OCR.
