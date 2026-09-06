# The Empty Center: Federal Welfare-Systems Policy, 1986–1999, and Why Nothing in It Would Have Caught the FLORIDA System's Defect

*A companion analysis to "The Unisys Protests of RFP 88-74-BC: What Was Alleged, What Was Testified, and What Fifteen Years Proved"*

**Peter Kastner Research Archive** · July 2026

---

## Abstract

Between 1986 and 1999 the federal government built an elaborate apparatus to govern the automation of state welfare systems: an advance-planning-document regime with prior-approval authority, enhanced federal match rates used as both carrot and stick, statutory certification deadlines, escalating financial penalties reaching thirty percent of a state's administrative funding, two decades of Government Accountability Office and Inspector General reporting, a landmark rewrite of federal information-technology acquisition law, and a White House capital-planning discipline that required quantified return on investment before a dollar could be obligated. Not one element of that apparatus imposed a quantified engineering performance standard — response time, transaction throughput, capacity headroom, or availability — on a federally funded state welfare or child-support system. The single numeric performance requirement Congress enacted in the entire period was a two-business-day transmission rule for income-withholding notices. This report traces the arc of that legislation and oversight, establishes the absence at its center from primary sources, and shows that the FLORIDA system's central failure — transaction-volume assumptions that proved wrong by roughly a factor of two, discovered internally in March 1991 and concealed — sat precisely in the gap the federal framework never closed. Florida was not an outlier that escaped a federal bar. There was no bar, for any state, and the recurrence of capacity and performance failures across Ohio, California, Michigan, and Massachusetts in the same years is the predictable consequence.

---

## 1. The Argument in Brief

The FLORIDA procurement record established three facts that this companion report takes as given, each pinpointed in the Division of Administrative Hearings record for [DOAH Case 89-0003BID](https://www.doah.state.fl.us/ROS/1989/89000003.PDF):

1. The Department of Health and Rehabilitative Services selected a transfer base — Ohio's CRIS-E — that was not operational and had not completed user acceptance testing at the time of award (¶57), and whose architecture was centralized (¶134).
2. The specifications protest record contains a state-authored planning convention: a 60–65 percent CPU utilization design rule ([DOAH 88-2942BID](https://www.doah.state.fl.us/ROS/1988/88002942.PDF), ¶56). It was a planning rule inside an RFP, not a contractual acceptance criterion and not a federal requirement.

3. The capacity and volume modeling underlying the winning proposal was conceded to be "no better than the assumptions" behind it (Appendix ¶90), and the hearing officer accepted that risk on the theory that fixed pricing and contractual penalties would discipline it.

**Correction, September 2026.** This report earlier described that utilization rule as the only quantified engineering constraint anywhere in the procurement, and inferred from the appellate record's silence that RFP 88-74-BC set no numeric response-time, throughput, or availability standard. That reading was wrong, and the document that corrects it is the Auditor General's. Florida Auditor General Report No. 12061, issued May 4, 1993 — audit supervised by Jonathan Ingram, audit made by Tina Greene, Auditor General Charles L. Lester — found that the contract required response times of 1 to 8 seconds at least 95 percent of the time, measured every 15 minutes at a random day and workstation on a monthly basis, and availability of at least 97 percent over rolling 30-day periods (Report No. 12061 ¶¶49–59). That is a two-part quantified performance standard with a measurement protocol attached. The procurement was not silent. What went missing was the mechanism that would have enforced the standard: the Department's own response to Finding #5 states that EDS "postponed and rescheduled these deliverables, thereby delaying the tests, until they were useless," and an October 4, 1991 Memorandum of Understanding waived the liquidated damages that attached to benchmark delays (Report No. 12061 ¶57 and Exhibit E, response to Finding #5). The standard Florida wrote was measured and missed — the Auditor General recorded availability of 94 percent, then 80.5 percent, then 97.9 percent for the three 30-day periods ending March 29, April 28, and May 28, 1992, and a manual test on May 13, 1992 produced an average response time of 2.8 minutes against a specification of 1 to 8 seconds (¶¶49–59).

The federal argument of this report is unaffected, because the standard was Florida's and not Washington's. The sentence that no numeric performance target existed anywhere in the procurement does not survive Report 12061, and it is replaced here rather than quietly dropped.

By late 1994 the production CPU was running at approximately 95 percent capacity during most of the regular work day and at 100 percent during some peak times. Those figures were not the Auditor General's measurements. They come from a report dated October 11, 1994 by an independent consultant the Department hired, which Auditor General Report No. 12581 quotes at ¶44; the roughly 65 percent commercial-data-center figure used for comparison is industry data the Department itself obtained. The press account of degrading response times is the [St. Petersburg Times of September 15, 1995](https://www.tampabay.com/archive/1995/09/15/hrs-supercomputer-can-t-hack-it-report-says/); the special master found EDS had known of the volume-model error since March 1991 without disclosing it, per the [August 16, 1995 account](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/).

The question this report answers is the one a reader of that record inevitably asks: where was the federal government? Florida drew $184.87 million in federal financial participation for welfare automation between FY1984 and FY1992 ([GAO/AIMD-94-52FS](https://www.govinfo.gov/content/pkg/GAOREPORTS-AIMD-94-52FS/html/GAOREPORTS-AIMD-94-52FS.htm)). Federal money paid for most of the system. Federal approval was required before the state could spend it. What did the federal government require in exchange?

The answer, documented below from statutes, regulations as they read at the time, and the oversight literature, is: functional scope, procedural paperwork, and deadlines — and nothing that would have detected, prevented, or penalized a wrong set of capacity assumptions.

---

## 2. The Legislative Arc, 1984–1998

### 2.1 The bargain: money for scope and speed

The framework Florida procured under was set by the [Child Support Enforcement Amendments of 1984, P.L. 98-378](https://www.congress.gov/98/statute/STATUTE-98/STATUTE-98-Pg1305.pdf), which established a 90 percent federal match for approved automated systems, and by the eligibility-side FAMIS regulations that offered the same enhanced rate. Congress's instrument was price. It bought automation by making it nearly free at the margin, and it specified what the automation had to *do*, never how well it had to *perform*.

The [Family Support Act of 1988, P.L. 100-485](https://www.congress.gov/100/statute/STATUTE-102/STATUTE-102-Pg2343.pdf) — enacted five months after Florida issued RFP 88-74-BC on May 20, 1988 — tightened the bargain at Section 123: every state was to have a statewide, federally certified child-support system operating by **October 1, 1995**, and the 90 percent enhanced match was repealed effective September 30, 1995. Deadline plus expiring subsidy. This is the structural core of the era's policy design, and it is worth naming plainly: Congress created a nationwide, simultaneous, hard-dated procurement stampede, funded at ninety cents on the dollar, with no technical acceptance standard attached and a subsidy that vanished on the deadline date. Every incentive ran toward signing a contract quickly and toward optimistic assumptions about what could be delivered by the date. None ran toward conservative capacity engineering.

Florida's own procurement exhibits the pattern in miniature. The 88-2942BID hearing officer recommended a 29-month schedule rather than the 26 months in the RFP (¶ recommendation). Schedule compression was already visible at the specifications stage, before a vendor was selected.

### 2.2 The subsidy is withdrawn, the deadline is not met, the penalties escalate

The bargain then unwound in sequence:

| Date | Instrument | Effect |
|---|---|---|
| Aug. 1993 | OBRA 1993, Sec. 13741 | Eligibility-side (FAMIS) enhanced match cut from 90% to 50%, effective April 1, 1994 ([59 FR 94-14326](https://www.govinfo.gov/content/pkg/FR-1994-06-15/html/94-14326.htm)) |
| Oct. 1, 1995 | FSA 1988 deadline arrives | **One state** in the nation is certified ([HHS OIG OEI-04-96-00010](https://oig.hhs.gov/oei/reports/oei-04-96-00010.pdf)) |
| Oct. 12, 1995 | P.L. 104-35 | Deadline extended two years to Oct. 1, 1997; [H. Rept. 104-250](https://www.congress.gov/committee-report/104th-congress/house-report/250/1) records HHS projecting only 18 states compliant six months *after* the original date |
| Aug. 22, 1996 | [PRWORA, P.L. 104-193](https://www.congress.gov/104/plaws/publ193/PLAW-104publ193.pdf), Secs. 344–345 | New system requirements layered on top; the sole quantified performance mandate of the era appears at SSA §454A(g)(1)(A)(i) — income-withholding notices transmitted within **two business days** |
| Sept. 1997 | Extended deadline approaches | **Seven states** fully certified (Colorado, Connecticut, Montana, New Hampshire, Virginia, Washington, Wyoming), eight conditionally — under 20% of national caseload ([House Ways & Means hearing, 1997](https://commdocs.house.gov/committees/ways/hwmw105-21.000/hwmw105-21_0.HTM)) |
| July 1998 | [CSPIA 1998, P.L. 105-200](https://www.govinfo.gov/content/pkg/PLAW-105publ200/html/PLAW-105publ200.htm) | Escalating penalties of 4/8/16/25/30 percent of federal IV-D administrative funding |

By March 31, 1998, only 25 of 54 state and territorial systems were certified or conditionally certified, covering about 38 percent of the FY1995 caseload ([GAO/AIMD-98-134](https://www.gao.gov/assets/aimd-98-134.pdf)).

The instructive point for the FLORIDA analysis is the *content* of the escalation. When compliance failed on a national scale, Congress's response was to raise the financial penalty for missing a functional-certification checklist. It never added a performance standard to the checklist. A state could be certified with a system that met all fifteen functional requirements of 45 CFR §307.10 and ran at 100 percent CPU utilization with unusable response times. Certification and usability were orthogonal.

### 2.3 The acquisition-reform track, and why it did not reach Tallahassee

Running alongside was the most consequential rewrite of federal IT acquisition law in forty years. The [Government Performance and Results Act of 1993](https://www.congress.gov/103/bills/s20/BILLS-103s20enr.pdf) required outcome measurement; the [Federal Acquisition Streamlining Act of 1994](https://www.congress.gov/bill/103rd-congress/senate-bill/1587) overhauled procurement procedure; and the [Clinger-Cohen Act of 1996](https://home.treasury.gov/system/files/236/Clinger-Cohen_Act_of_1996.pdf) did two things directly relevant here. Section 5101 repealed the Brooks Act and 40 U.S.C. 759 effective August 8, 1996, eliminating the General Services Board of Contract Appeals' bid-protest jurisdiction over ADP procurements. Sections 5122–5123, codified at [40 U.S.C. 11312](https://www.govinfo.gov/content/pkg/USCODE-2010-title40/pdf/USCODE-2010-title40-subtitleIII-chap113-subchapII-sec11312.pdf), required that IT investments be justified with a "quantitatively expressed" projected return on investment.

OMB then operationalized this in the eight criteria of [Memorandum M-97-02, the "Raines Rules," issued October 25, 1996](https://trumpwhitehouse.archives.gov/wp-content/uploads/2017/11/1997-M-97-02-Funding-Information-Systems-Investments.pdf): quantifiable return on investment, phased milestones with usable increments, pilots before full deployment, and explicit allocation of risk to the contractor.

Read against the FLORIDA record, the Raines Rules are almost a point-by-point indictment. Phased milestones with usable deliverables, mandatory piloting before statewide deployment, and contractor risk allocation address exactly the failure modes the 1988–89 record exposed: a monolithic transfer of an untested centralized system, a compressed statewide schedule, and a capacity model whose risk the hearing officer allocated to the vendor by assumption rather than by verified mechanism.

**These rules bound federal agencies. They did not bind states spending federal money.** And they arrived eight years after Florida's award and one year after the system's capacity failure became public. The reform that would have caught FLORIDA was written, in substance, after FLORIDA — and addressed to the wrong party.

---

## 3. The Regulatory Framework, as It Actually Read

This is the analytical core, and it rests on primary text rather than secondary characterization.

### 3.1 The eligibility side: FAMIS, 45 CFR §§205.35–205.38

FAMIS governed the AFDC, food-stamp, and Medicaid eligibility automation that FLORIDA was. Section 205.37 conditioned ACF approval on an advance planning document containing a requirements analysis, a system description, security and interface requirements, resource projections, a cost-benefit analysis "in terms of qualitative and quantitative measures," an implementation plan with **"proposed acceptance criteria,"** and backup and fallback procedures ([45 CFR 205.37](https://www.govinfo.gov/content/pkg/CFR-2012-title45-vol2/pdf/CFR-2012-title45-vol2-sec205-37.pdf)).

The two operative words are *proposed* and *cost-benefit*. Acceptance criteria were authored by the state and submitted for approval; the federal rule specified no floor. The quantification the rule demanded was financial justification for spending, not engineering performance of the thing bought.

The government said so itself, contemporaneously. [GAO/HRD-81-119](https://www.gao.gov/products/hrd-81-119), reviewing FAMIS at the outset, found the requirements had not been pilot tested and that they:

> "(1) have not been shown to be cost beneficial for all State systems, **(2) do not contain sufficiently specific performance standards for evaluating the quality of State developed systems**, (3) do not adequately address the internal controls needed to ensure that State systems function as mandated by legislation, and (4) do not facilitate compatibility of State AFDC systems with systems used to administer other welfare programs."

That finding was published in 1981. Florida issued RFP 88-74-BC in 1988. The defect GAO identified was seven years old at award and was never remedied.

### 3.2 The child-support side: 45 CFR Part 307

Section 307.10 enumerates fifteen functional requirements at subsection (b)(1)–(15) — identifying information, data verification, federal reporting, delinquency tracking, collection and distribution, incentive computation, accounts receivable, cost tracking, IV-A referrals, TANF interfacing, security, management information, Medicaid data exchange, locate/EFT/interstate integration, and audit capability ([45 CFR 307.10](https://www.law.cornell.edu/cfr/text/45/307.10)). No numeric threshold of any kind appears in the section. The OCSE [Guide for States](https://acf.gov/css/training-technical-assistance/automated-systems-child-support-enforcement-guide-states) is interpretive and procedural, directed at documenting compliance with the checklist.

### 3.3 The food-stamp side: 7 CFR 277.18 — a resolved question

This deserves particular attention, because the *current* text of the FNS advance-planning rule is the one place in the modern federal framework where quantified performance language appears. Today 7 CFR 277.18 requires a formal test plan covering "stress and throughput performance testing," documented user acceptance testing before piloting, a live-production pilot of usually at least three months, and verification of "performance standards including responsiveness, usability, capacity and security" ([7 CFR 277.18, current](https://www.law.cornell.edu/cfr/text/7/277.18)).

If that language had existed in 1988, the analysis would change materially. FLORIDA carried food-stamp functionality; it would have been subject to a federal requirement for stress and throughput testing and for verified capacity — precisely the standard whose absence this report identifies, and precisely the defect the system exhibited.

**It did not exist.** I retrieved the annual codification of the rule as it read on January 1, 1999 — the last year of the study window and the version most favorable to the contrary hypothesis — from the Government Publishing Office. The section's own amendment history at that date reads: *Amdt. 319, 55 FR 4355, Feb. 7, 1990, as amended by Amdt. 345, 57 FR 11259, Apr. 1, 1992; Amdt. 342, 59 FR 2733, Jan. 19, 1994; Amdt. 368, 61 FR 33643, June 28, 1996* ([CFR-1999-title7-vol4, §277.18](https://www.govinfo.gov/content/pkg/CFR-1999-title7-vol4/pdf/CFR-1999-title7-vol4-sec277-18.pdf)). The full text contains no acceptance-testing plan requirement, no stress testing, no throughput testing, no responsiveness criterion, and no capacity verification. The words "capacity" and "pilot testing" appear only twice and only in funding contexts: "computer capacity planning" is listed as an allowable Implementation APD *budget line item*, and "pilot testing and an initial period of parallel processing for test purposes may be considered developmental costs" eligible for the 63 percent enhanced match. Capacity planning was a reimbursable expense category. It was not a standard to be met.

The modern testing language is a later addition. During 1986–1999, on the food-stamp side as on the HHS side, no quantified federal performance standard applied.

### 3.4 The framework in one table

| Instrument | Governs | What it required | Quantified performance standard? |
|---|---|---|---|
| 45 CFR §§205.35–205.38 (FAMIS) | AFDC/Medicaid/food-stamp eligibility — i.e., FLORIDA | Requirements analysis, cost-benefit analysis, **state-proposed** acceptance criteria, fallback plan | **No** — GAO/HRD-81-119 found it lacked "sufficiently specific performance standards" |
| 45 CFR Part 95, Subpart F | APD prior approval for all HHS-funded ADP | Prior approval, procurement standards, IV&V (§95.626), milestone-based funding | **No** — process required; pass/fail content left to the state's own APD |
| 45 CFR §307.10 | CSE certification | Fifteen enumerated functional requirements | **No** — functional checklist only |
| 7 CFR 277.18 (as of 1-1-99) | FNS/SNAP automation APD | Dollar-threshold prior approval; capacity planning as a **budget line**; 63% match | **No** — verified against the [1999 annual CFR volume](https://www.govinfo.gov/content/pkg/CFR-1999-title7-vol4/pdf/CFR-1999-title7-vol4-sec277-18.pdf) |
| SSA §454A(g)(1)(A)(i) (PRWORA 1996) | CSE income withholding | Transmission within **two business days** | **Yes** — the only one, and it is a business-process rule, not a systems-engineering standard |

---

## 4. The Oversight Literature: A Twenty-Year Warning Nobody Was Empowered to Act On

The remarkable feature of the GAO and Inspector General record is not that it missed the problem. It is that it identified the problem repeatedly, precisely, and early — and that the one structural remedy it proposed was refused.

- **1981** — [GAO/HRD-81-119](https://www.gao.gov/products/hrd-81-119) finds FAMIS lacks specific performance standards. Seven years before Florida's RFP.
- **1988** — [OTA, *Informing the Nation*](https://ota.fas.org/reports/8812.pdf) surveys federal information-systems management in the year of the FLORIDA award.
- **1992** — [GAO/IMTEC-92-46](https://www.gao.gov/assets/imtec-92-46.pdf) examines three "severely flawed" state child-support systems, with problems persisting three to eight years and over $32 million in federal funds spent on systems ultimately abandoned. One is California, stopped after seven years and $17 million despite OCSE concerns raised as early as 1987.
- **1992** — [GAO/IMTEC-92-29](https://www.gao.gov/products/imtec-92-29) recommends a joint HHS/USDA program office with **on-site inspection authority** over state welfare-automation projects. **Both agencies rejected the recommendation.** This is the pivotal non-event of the period: the one proposal that would have put a federal technical reviewer inside a project like FLORIDA, with authority to look at the actual system, was declined the year after EDS internally discovered the volume-model error and did not disclose it.
- **1993** — [OTA, *Making Government Work*](https://ota.fas.org/reports/9333.pdf) and the [National Performance Review's information-technology report](https://clintonwhitehouse6.archives.gov/1993/09/1993-09-01-npr-on-reengineering-through-information-technology-part.html).
- **1994** — [GAO/AIMD-94-52FS](https://www.govinfo.gov/content/pkg/GAOREPORTS-AIMD-94-52FS/html/GAOREPORTS-AIMD-94-52FS.htm) compiles historical costs: Florida drew $184.87 million FY1984–92, with FAMIS needing $13.5 million more plus a $5.6 million mainframe upgrade — a contemporaneous federal document recording, in budget language, the capacity shortfall the state was then litigating. [GAO/AIMD-94-115](https://www.govinfo.gov/content/pkg/GAOREPORTS-AIMD-94-115/html/GAOREPORTS-AIMD-94-115.htm) addresses IT investment practice.
- **1995** — [GAO/HR-95-1](https://www.gao.gov/assets/hr-95-1.pdf) places information management on the high-risk list.
- **1997** — [GAO/AIMD-10.1.13](https://www.gao.gov/assets/aimd-10.1.13.pdf) publishes an assessment framework; [GAO/HR-97-9](https://www.gao.gov/assets/hr-97-9.pdf) records $145 billion in federal IT spending with poor returns; [GAO/AIMD-97-72](https://www.gao.gov/products/aimd-97-72) puts cumulative child-support automation spending above $2.6 billion since 1980, with individual state systems ranging from $1.5 million to $344 million, and notes OCSE moving to require "critical milestones" and "other measures to quantify progress" — against **state-proposed** criteria.
- **1998** — [HHS OIG OEI-04-96-00010](https://oig.hhs.gov/oei/reports/oei-04-96-00010.pdf) documents the single-state compliance figure.
- **2001** — the most Florida-specific federal document located: [USDA OIG Audit 27004-3-AT](https://usdaoig.oversight.gov/sites/default/files/reports/2023-07/27004-3-At.pdf), which cites a January 1994 OIG audit finding 460,600 backlogged referrals and $57.1 million in unestablished claims, a backlog that took more than seven years to clear.

The pattern is consistent. Federal oversight of state welfare automation was **financial and procedural** — did the state file an APD, was the cost allocation correct, did it hit a certification checklist by a date. It was never **technical**. No federal body had the authority, the staff, or the mandate to examine a capacity model and ask whether the assumptions behind it were sound. When GAO proposed creating exactly that authority in 1992, HHS and USDA said no.

---

## 5. Florida in the National Frame

Set against peer states, the FLORIDA record loses its appearance of aberration.

| State | System | Outcome |
|---|---|---|
| **Florida** | FLORIDA (EDS/IBM/Touche Ross) | ~$104M at award; ~$260M in downstream error costs by 1993; up to $144M federal penalty exposure ([LA Times, May 2, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html)); litigation to [631 So.2d 353](https://www.courtlistener.com/opinion/1895493/state-dhrs-v-eds-federal-corp/); grand jury |
| **California** | SACSS (Lockheed Martin IMS) | $75.5M contract → $260M estimate; terminated Nov. 20, 1997 operating in 17 of 58 counties ([LA Times](https://www.latimes.com/archives/la-xpm-1997-nov-21-mn-56038-story.html)); auditor found a "flawed computer system that failed testing," $27M in improper payments, QA warnings ignored ([CA State Auditor 97116](https://information.auditor.ca.gov/pdfs/reports/97116.pdf)); vendor won $46.4M judgment, state paid $157M total |
| **Michigan** | CSES → MiCSES | Built 1983–1995, missed certification; $68.7M in penalties gross / $33.9M net; MiCSES certified Nov. 25, 2003, eight years late; $710.3M cumulative ([Michigan OAG 4359505](https://audgen.michigan.gov/finalpdfs/05_06/r4359505.pdf); [Senate Fiscal Agency](https://sfa.senate.michigan.gov/Publications/Notes/2003Notes/NotesNovDec03cc.pdf)) |
| **Ohio** | CRIS-E (FLORIDA's transfer base); SETS | SETS restarted after two failed 1991 federal reviews; ≥$252M projected; $43M in penalties paid, $56M at risk; auditor: designed "to meet federal guidelines with little concern for the needs of the end users" ([Ohio AOS](https://ohioauditor.gov/auditsearch/Reports/1999/statewide_setsimplementation_finalrpt.pdf)) |
| **Massachusetts** | BEACON | ~$63.56M ([MA State Auditor](https://www.mass.gov/doc/department-of-transitional-assistance-0/download)) |
| **Washington** | ACES | Delivered; one of seven states fully certified before the 1997 deadline — the counter-example |

Three observations follow.

**First, the failure mode was shared, not idiosyncratic.** Michigan's system "was not developed with the advantage of user testing and input." California's "failed testing." Ohio's was built to the federal checklist "with little concern for the needs of end users." Florida's workload assumptions were wrong by roughly half and the error was concealed for four years. These are four descriptions of one thing: systems certified against functional scope and delivered against a deadline, with performance verification treated as a residual.

**Second, Ohio's role is the sharpest single indictment of the transfer-system doctrine.** Federal policy actively encouraged states to transfer existing systems to save money. Florida transferred CRIS-E, a system that was not operational and had not completed acceptance testing (¶57). Nothing in 45 CFR Part 95 Subpart F, in FAMIS, or in the APD approval process required the donor system to be proven in production before the recipient state could obligate federal funds against it. The economy the transfer doctrine was meant to produce was purchased with unverified risk.

**Third, on dollars, Florida sits in the middle of the distribution, not at its tail.** California paid more, Michigan spent more, Ohio's penalties were comparable. What distinguishes Florida is the quality of the surviving record — an eleven-day evidentiary hearing with a written recommended order, a special master's findings, a grand jury presentment, and legislative auditor reports. Florida is better documented, not worse governed.

---

## 6. Where the FLORIDA Failure Fell Through

Mapping the specific defects to the framework produces the report's central finding.

| FLORIDA failure mode | Federal requirement that addressed it, 1986–1999 |
|---|---|
| Transfer base not operational, UAT incomplete at award (¶57) | **None.** Transfer was encouraged; donor-system maturity was not a condition of APD approval |
| Centralized architecture chosen for a statewide caseload (¶134) | **None.** No architectural review authority existed |
| Transaction-volume model wrong by roughly a factor of two | **None.** No throughput or capacity standard; capacity planning was a reimbursable budget line, not a test |
| Production CPU at ~95% on a regular work day and 100% at some peaks, measured by a Department-hired consultant on October 11, 1994, against a 60–65% design rule | **None federally.** The 60–65% rule was a state RFP convention (88-2942BID ¶56) |
| Response time of 2.8 minutes on the Department's May 13, 1992 manual test, against a contractual 1–8 seconds at 95% of measurements | **None federally.** No response-time standard in FAMIS, Part 307, or 7 CFR 277.18 as it then read. The numeric standard was Florida's own (Report No. 12061 ¶¶49–59), and its acceptance mechanism was postponed and then modified away |
| Defect known to the vendor from March 1991, undisclosed | **None.** GAO proposed on-site federal inspection authority in 1992; HHS and USDA refused it |
| 26-month statewide schedule; no piloting requirement | **None** until the Raines Rules of October 1996 — federal agencies only, eight years after award |
| Evaluation scoring shown to be statistically unreliable (¶163) | **None.** Federal approval covered cost allocation and scope, not source-selection methodology |

Every row reads the same. The federal government financed the system, approved the plan, set the deadline, and penalized the outcome — and at no point required, or possessed the authority to verify, that the machine would work.

---

## 7. Why This Matters to the Procurement Record

Three implications bear directly on how the Unisys protests and the fifteen years that followed should be read.

**The hearing officer's risk allocation was the only one available.** Appendix ¶90 concedes that capacity data is "no better than the assumptions" and rests on fixed pricing plus contractual penalties to contain the risk. That reasoning is often read as credulous. Read against the federal framework, it was the only mechanism in existence. There was no federal capacity standard to invoke, no federal technical reviewer to defer to, no certification test to await. Florida's administrative law judge in 1989 was working inside a policy vacuum that the Government Accountability Office had identified in 1981 and that Congress and two federal agencies declined to fill for another seven years. The commercial-risk theory failed — the state paid, EDS litigated, and the record at [631 So.2d 353](https://www.courtlistener.com/opinion/1895493/state-dhrs-v-eds-federal-corp/) shows how — but it failed because it was the only instrument on the table. Two things follow from Report 12061 that this report earlier had wrong. The penalties the hearing officer relied on were attached to a real numeric standard — 1 to 8 seconds at 95 percent of measurements, 97 percent availability over rolling 30 days (¶¶49–59). And the instrument was never fired: acceptance testing was postponed by EDS until, in the Department's words, the tests "were useless," and the liquidated damages for benchmark delay were waived by the October 4, 1991 Memorandum of Understanding (¶57).

**Bid protests carried a load they were never designed to bear.** With no federal technical gate, the administrative protest became the only forum in which a state's engineering assumptions were examined by an adversary before award. That is what the eleven days of hearings in 89-0003BID actually were: the sole substantive technical review the FLORIDA system received from any external party before contract signature. Under [*Groves-Watkins*](https://www.doah.state.fl.us/ROS/1989/89000003.PDF), 530 So.2d 912 (Fla. 1988) (¶179), the standard of review was fraud, illegality, arbitrariness, or dishonesty — a standard that cannot reach capacity assumptions that are merely wrong. The forum with the evidence lacked the standard; the framework with the money lacked the forum. Both statements are true simultaneously, and together they explain the outcome. Clinger-Cohen's abolition of GSBCA protest jurisdiction in 1996 removed the analogous federal forum entirely.

**The reform arrived, correctly diagnosed, and addressed to the wrong party.** The Raines Rules of 1996 — quantified return on investment, phased usable increments, mandatory piloting, explicit contractor risk allocation — read as a specification for what FLORIDA should have been. They bound federal agencies. States spending federal welfare money remained under the FAMIS and Part 307 regimes, whose acceptance criteria they wrote themselves. The federal government reformed its own house in 1996 and left the state welfare-automation estate, then consuming billions in federal match, governed by rules GAO had criticized in 1981.

---

## 8. Conclusion

The FLORIDA system did not fail because Florida evaded a federal standard. It failed in a policy environment engineered — through enhanced match rates, hard statutory deadlines, an encouraged transfer doctrine, and escalating penalties tied to functional certification — to maximize the speed and scope of state welfare automation while requiring nothing verifiable about whether the resulting systems would perform. The Government Accountability Office named the missing element in 1981 and again in 1992, and the two agencies with the authority to supply it declined. Congress's answer to nationwide failure was larger fines against the same unquantified checklist. When quantified investment discipline finally arrived in 1996, it applied to federal agencies and came eight years too late for a system awarded in 1989 and known to be broken by 1991.

The record of RFP 88-74-BC is therefore not primarily a record of a bad vendor selection or a flawed evaluation, though it is both. It is the most fully documented instance available of what happens when the numeric proof that a large transaction-processing system can carry its load is written into a state contract, required by no one above the state, and then postponed, waived, and left unmeasured until the system was in production and failing.

---

## Sources

Primary legislation: [P.L. 98-378 (1984)](https://www.congress.gov/98/statute/STATUTE-98/STATUTE-98-Pg1305.pdf) · [P.L. 100-485, Family Support Act of 1988](https://www.congress.gov/100/statute/STATUTE-102/STATUTE-102-Pg2343.pdf) · [GPRA 1993](https://www.congress.gov/103/bills/s20/BILLS-103s20enr.pdf) · [FASA 1994](https://www.congress.gov/bill/103rd-congress/senate-bill/1587) · [H. Rept. 104-250 (P.L. 104-35)](https://www.congress.gov/committee-report/104th-congress/house-report/250/1) · [Clinger-Cohen Act of 1996](https://home.treasury.gov/system/files/236/Clinger-Cohen_Act_of_1996.pdf) · [40 U.S.C. 11312](https://www.govinfo.gov/content/pkg/USCODE-2010-title40/pdf/USCODE-2010-title40-subtitleIII-chap113-subchapII-sec11312.pdf) · [PRWORA, P.L. 104-193](https://www.congress.gov/104/plaws/publ193/PLAW-104publ193.pdf) · [CSPIA 1998, P.L. 105-200](https://www.govinfo.gov/content/pkg/PLAW-105publ200/html/PLAW-105publ200.htm)

Regulations: [45 CFR 205.37](https://www.govinfo.gov/content/pkg/CFR-2012-title45-vol2/pdf/CFR-2012-title45-vol2-sec205-37.pdf) · [45 CFR 205.37 (LII)](https://www.law.cornell.edu/cfr/text/45/205.37) · [45 CFR Part 95 Subpart F](https://www.law.cornell.edu/cfr/text/45/part-95/subpart-F) · [45 CFR 307.10](https://www.law.cornell.edu/cfr/text/45/307.10) · [7 CFR 277.18, 1999 annual edition](https://www.govinfo.gov/content/pkg/CFR-1999-title7-vol4/pdf/CFR-1999-title7-vol4-sec277-18.pdf) · [7 CFR 277.18, current](https://www.law.cornell.edu/cfr/text/7/277.18) · [59 FR 94-14326 (June 15, 1994)](https://www.govinfo.gov/content/pkg/FR-1994-06-15/html/94-14326.htm) · [63 FR 98-7714 (Mar. 25, 1998)](https://www.govinfo.gov/content/pkg/FR-1998-03-25/html/98-7714.htm)

Oversight: [GAO/HRD-81-119](https://www.gao.gov/products/hrd-81-119) · [OTA 1988](https://ota.fas.org/reports/8812.pdf) · [GAO/IMTEC-92-29](https://www.gao.gov/products/imtec-92-29) · [GAO/IMTEC-92-46](https://www.gao.gov/assets/imtec-92-46.pdf) · [OTA 1993](https://ota.fas.org/reports/9333.pdf) · [NPR 1993](https://clintonwhitehouse6.archives.gov/1993/09/1993-09-01-npr-on-reengineering-through-information-technology-part.html) · [GAO/AIMD-94-52FS](https://www.govinfo.gov/content/pkg/GAOREPORTS-AIMD-94-52FS/html/GAOREPORTS-AIMD-94-52FS.htm) · [GAO/AIMD-94-115](https://www.govinfo.gov/content/pkg/GAOREPORTS-AIMD-94-115/html/GAOREPORTS-AIMD-94-115.htm) · [GAO/HR-95-1](https://www.gao.gov/assets/hr-95-1.pdf) · [OMB M-97-02, Raines Rules](https://trumpwhitehouse.archives.gov/wp-content/uploads/2017/11/1997-M-97-02-Funding-Information-Systems-Investments.pdf) · [GAO/AIMD-10.1.13](https://www.gao.gov/assets/aimd-10.1.13.pdf) · [GAO/HR-97-9](https://www.gao.gov/assets/hr-97-9.pdf) · [GAO/AIMD-97-72](https://www.gao.gov/products/aimd-97-72) · [GAO/AIMD-98-134](https://www.gao.gov/assets/aimd-98-134.pdf) · [HHS OIG OEI-04-96-00010](https://oig.hhs.gov/oei/reports/oei-04-96-00010.pdf) · [USDA OIG 27004-3-AT](https://usdaoig.oversight.gov/sites/default/files/reports/2023-07/27004-3-At.pdf) · [House Ways & Means hearing, 1997](https://commdocs.house.gov/committees/ways/hwmw105-21.000/hwmw105-21_0.HTM)

Florida Auditor General: Report No. 12061, *Systems Review of the FLORIDA System*, dated May 4, 1993, audit supervised by Jonathan Ingram, audit made by Tina Greene, Auditor General Charles L. Lester — supplied by the Auditor General's office; not available online. Report No. 12581, *HRS — Florida System*, dated September 12, 1995 — supplied by the Auditor General's office; not available online.

Florida record: [DOAH 89-0003BID](https://www.doah.state.fl.us/ROS/1989/89000003.PDF) · [DOAH 88-2942BID](https://www.doah.state.fl.us/ROS/1988/88002942.PDF) · [State DHRS v. EDS Federal Corp., 631 So.2d 353](https://www.courtlistener.com/opinion/1895493/state-dhrs-v-eds-federal-corp/) · [LA Times, May 2, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html) · [Tampa Bay Times, Aug. 16, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/) · [Tampa Bay Times, Sept. 15, 1995](https://www.tampabay.com/archive/1995/09/15/hrs-supercomputer-can-t-hack-it-report-says/)

Peer states: [CA State Auditor 97116](https://information.auditor.ca.gov/pdfs/reports/97116.pdf) · [LA Times, Nov. 21, 1997](https://www.latimes.com/archives/la-xpm-1997-nov-21-mn-56038-story.html) · [Michigan OAG 4359505](https://audgen.michigan.gov/finalpdfs/05_06/r4359505.pdf) · [Michigan Senate Fiscal Agency, 2003](https://sfa.senate.michigan.gov/Publications/Notes/2003Notes/NotesNovDec03cc.pdf) · [Ohio AOS SETS, 1999](https://ohioauditor.gov/auditsearch/Reports/1999/statewide_setsimplementation_finalrpt.pdf) · [Ohio AOS Clermont County, 2001](https://ohioauditor.gov/auditsearch/Reports/2001/clermont_child_support_enforcement_agency_performance_01-clermont.pdf) · [Massachusetts State Auditor](https://www.mass.gov/doc/department-of-transitional-assistance-0/download)

---

## Open Items

1. **CRIS-E's user-acceptance-testing status in 1988–89** rests on DOAH 89-0003BID ¶57. No independent contemporaneous Ohio source corroborating it was located; Ohio ODHS or legislative records circa 1987–1989 would settle it.
2. **45 CFR Part 95 Subpart F amendment history for 1986–1999.** Current eCFR text returns inconsistent amendment chains, indicating renumbering. Only 51 FR 45326 (Dec. 18, 1986) as the subpart's origin and 59 FR 94-14326 (June 15, 1994) for the FFP reduction are firmly established. Historical annual CFR volumes would resolve the rest.
3. **The 1990s-vintage OCSE Guide for States.** Only 2009 and later editions are available online; an archived 1990s edition would strengthen the finding on the CSE side.
4. **7 CFR 277.18 before 1996.** The 1999 annual edition is verified above and its amendment history runs back to 55 FR 4355 (Feb. 7, 1990), which is dispositive for the study window. Pre-1990 text has not been retrieved and would close the question back to the 1988 award date.
