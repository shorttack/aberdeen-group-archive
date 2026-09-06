# The FLORIDA System: EDS, IBM, and the Collapse of a Landmark State Integrated-Eligibility Procurement (1988–1996)

An analytical case study of the Florida Department of Health and Rehabilitative Services (HRS) *Florida On-Line Recipient Integrated Data Access* (FLORIDA) system — one of the largest non-military transaction-processing applications attempted by a U.S. state government in the late 1980s.

---

## 1. Executive summary

FLORIDA was procured as a fixed-scope, prime-contractor build of a statewide integrated public-assistance eligibility system: AFDC, food stamps, and Medicaid on a single on-line case record. HRS issued a two-volume RFP in May 1988 and executed a contract with EDS Federal Corporation on May 15, 1989 ([State, Dep't of HRS v. E.D.S. Federal Corp., 631 So. 2d 353](https://www.courtlistener.com/opinion/1895493/state-dhrs-v-eds-federal-corp/)); press accounts value the build-and-manage award at roughly $104 million ([Tampa Bay Times, Aug. 16, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/); $104.2 million in [Tampa Bay Times, Aug. 3, 1992](https://www.tampabay.com/archive/1992/08/03/state-faces-fine-of-5-million-for-food-stamp-errors/)).

By May 1993 the program had produced $260 million in benefit-payment errors, exposure to as much as $144 million in federal penalties, a statewide grand jury inquiry into whether HRS improperly steered a $5.1 million upgrade to IBM, and a $46 million contractor lawsuit ([Los Angeles Times, May 2, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html)).

The analytically important finding is not the litigation outcome but its cause. A special master — former federal judge and FBI/CIA director William Webster — found that EDS had discovered by **March 1991** that the capacity assumptions behind its bid had overstated usable throughput by roughly a factor of two, and did not disclose it; HRS then agreed to help fund an enlargement of the system without knowing why the enlargement was needed ([Tampa Bay Times, Aug. 16, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/)).

Earlier versions of this paper read that record as a procurement containing no mechanism for testing a vendor's estimate of its own future workload, and inferred from the silence of the appellate and protest records that the RFP set no numeric performance standard. **That inference was wrong, and the correction is documentary.** The specifications incorporated into the initial contract required that for at least 95 percent of the time response times not exceed a period ranging between one and eight seconds depending on the type of processing requested, measured every 15 minutes during a randomly selected day each month at randomly selected work stations, and required the system to be available to users at least 97 percent of the time during normal working hours within any consecutive 30-day period (Auditor General Report No. 12061, ¶51). EDS was also required to perform, or to provide the data allowing the Department to perform, periodic benchmark and capacity tests (¶56). FLORIDA is therefore best read not as a software-quality failure, and not as a failure of the modeling tool, but as a failure of **assumption validation and of the enforcement of standards the contract already contained** — the standard existed, and the acceptance mechanism that would have enforced it never ran. It is compounded by a governance structure in which the buyer adjudicated its own disputes and the hardware vendor was paid more when the sizing was wrong.

Two appendices carry the quantitative record. **Appendix A** catalogues the fifteen remediation measures taken between 1991 and 1997 with their costs and measured effects, and shows that the most effective intervention — moving caseworker use to nights and Saturdays, which halved response time — carried no identified capital cost, while the $5.4 million CPU upgrade bought 20 percent. **Appendix B** reconciles the $107,658,141 bid to a cost floor of **$310,621,339** through fiscal year 1996-97 — the Department's own estimate of total FLORIDA System cost, nonrecurring and recurring, as reported by the Auditor General (Report No. 13287, p. 14) — an overrun of roughly $203.0 million, or **188 percent**. Earlier versions of this paper carried a floor of $245.3 million and an overrun of 128 percent, built up from press-reported cumulative spend; that construction is superseded by the Department's own figure and is retired here rather than quietly adjusted.

---

## 2. Chronology of record

| Date | Event | Source |
|---|---|---|
| May 1988 | HRS issues two-volume RFP for a fully integrated on-line eligibility system; disputes clause at § 7.11 | [631 So. 2d 353](https://www.courtlistener.com/opinion/1895493/state-dhrs-v-eds-federal-corp/) |
| May 15, 1989 | HRS and EDS execute contract incorporating specified RFP sections, including § 7.11 | [631 So. 2d 353](https://www.courtlistener.com/opinion/1895493/state-dhrs-v-eds-federal-corp/) |
| March 1991 | EDS internally discovers its transaction-volume model was wrong; usable capacity ≈ half of what EDS and HRS expected. Not disclosed to HRS | [Tampa Bay Times, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/) |
| 1991 | System begins handling live welfare cases | [LA Times, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html) |
| 1992 | HRS engages Maximus to review FLORIDA acceptance testing; Maximus finds the system meets standards; HRS conditions payment on changing the conclusion | [Tampa Bay Times, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/) |
| June 1992 | Average response time measured in **minutes** | [Tampa Bay Times, Sept. 15, 1995](https://www.tampabay.com/archive/1995/09/15/hrs-supercomputer-can-t-hack-it-report-says/) |
| Aug. 3, 1992 | USDA assesses ~$5 million food-stamp error penalty; FY1990–91 Florida payment error rate 10.89% vs. 10.31% national | [Tampa Bay Times, 1992](https://www.tampabay.com/archive/1992/08/03/state-faces-fine-of-5-million-for-food-stamp-errors/) |
| May 31, 1992 | EDS ends its computer contract with HRS | [Tampa Bay Times, Apr. 28, 1993](https://www.tampabay.com/archive/1993/04/28/eds-wins-another-computer-contract/) |
| Aug. 21, 1992 | EDS files ten-count circuit-court complaint against HRS and Comptroller Gerald Lewis, alleging >$45 million unpaid | [631 So. 2d 353](https://www.courtlistener.com/opinion/1895493/state-dhrs-v-eds-federal-corp/) |
| Mar. 22, 1993 | HRS Secretary Bob Williams resigns; Lt. Gov. Buddy MacKay becomes acting head | [LA Times, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html) |
| Apr. 27, 1993 | Governor and Cabinet approve a separate five-year, $24.2 million EDS student-loan processing contract, 5–2 | [Tampa Bay Times, 1993](https://www.tampabay.com/archive/1993/04/28/eds-wins-another-computer-contract/) |
| May 2, 1993 | Statewide grand jury in Tallahassee weighing evidence that HRS improperly favored IBM on a $5.1 million upgrade; two staff already out | [LA Times, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html) |
| 1993 | Grand jury presentment accuses HRS officials of violating laws, acting unethically, intimidating subordinates; two administrators indicted (one dropped; one misdemeanor conviction later thrown out) | [Tampa Bay Times, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/) |
| Feb. 7, 1994 | First DCA grants HRS certiorari, quashes the circuit court order, and directs dismissal of counts I–IX: EDS must first use the § 7.11 procedure | [631 So. 2d 353](https://www.courtlistener.com/opinion/1895493/state-dhrs-v-eds-federal-corp/) |
| Jan.–Dec. 1994 | Response time 8 seconds (Jan.), 4 seconds (June, after shifting work to nights/Saturdays), 3 seconds (Dec.) | [Tampa Bay Times, 1995](https://www.tampabay.com/archive/1995/09/15/hrs-supercomputer-can-t-hack-it-report-says/) |
| Aug. 16, 1995 | Special master Webster recommends the state pay EDS $42 million plus multi-year interest; HRS due only $4.7 million; ~$200 million already spent | [Tampa Bay Times, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/) |
| Sept. 14, 1995 | Auditor General reports the findings of an independent consultant hired by the Department, whose report of October 11, 1994 put the CPU at approximately 95% capacity through most of the regular work day and 100% at some peak times; the ~65% commercial comparison is industry data the Department obtained, not an Auditor General measurement; $5.4 million CPU upgrade five months earlier yielded ~20% improvement | [Tampa Bay Times, 1995](https://www.tampabay.com/archive/1995/09/15/hrs-supercomputer-can-t-hack-it-report-says/) |
| Mar. 1995 | HRS terminates the Deloitte & Touche programming-staff contract on FLORIDA and awards an emergency contract to Unisys | [Advanced Systems Design v. Strawn (Fla. 1st DCA 1997)](https://caselaw.findlaw.com/court/fl-district-court-of-appeal/1203645.html) |

---

## 3. The IBM question: what the grand jury was actually examining

The LA Times account is precise and narrow, and it is worth quoting exactly: "A state grand jury in Tallahassee is considering evidence that HRS improperly favored International Business Machines Corp. when it upgraded the system at a cost of $5.1 million. Two people involved have already lost their jobs" ([LA Times, May 2, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html)).

Three analytical points follow.

**The alleged favoritism attached to the upgrade, not the original award.** The 1988–89 competitive procurement produced a prime contract with EDS; IBM's exposure in the scandal is as the hardware beneficiary of a *subsequent* capacity remediation. Characterizing FLORIDA as "won by EDS and IBM" is defensible in the commercial sense — the platform was an IBM mainframe estate and IBM captured the growth — but the contractual counterparty of record, and the defendant/plaintiff in all the litigation, is EDS Federal Corporation.

**The upgrade was structurally inevitable once the capacity assumptions failed.** Webster's finding that usable capacity was roughly half of plan ([Tampa Bay Times, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/)) means the state faced a forced, urgency-driven hardware purchase from the installed-base vendor. That is precisely the condition under which competitive procurement discipline collapses: an incumbent-locked, time-critical, sole-realistic-source buy. Whether or not individual officials acted improperly, the *procurement economics* guaranteed an IBM-favorable outcome.

**The remediation did not end.** A further $5.4 million CPU upgrade around April 1995 delivered only about a 20% performance improvement, and the system still ran near the ceiling: an October 11, 1994 report by an independent consultant hired by the Department found regular-day CPU utilization at 95 percent and peak-period utilization at 100 percent, against a 65 percent figure for the average commercial data center that was industry data the Department obtained rather than an Auditor General measurement (Auditor General Report No. 12581, p. 53; [Tampa Bay Times, Sept. 15, 1995](https://www.tampabay.com/archive/1995/09/15/hrs-supercomputer-can-t-hack-it-report-says/)). Two rounds of hardware spend did not restore headroom, which is the signature of a workload that was mis-modeled at the transaction level rather than merely under-provisioned.

---

## 4. The cost of error: why the numbers got so large so fast

By May 1993, cumulative errors reached $260 million: $28 million in taxpayer cost associated with removing 235,000 ineligible people — some deceased — from Medicaid rolls, plus $232 million in AFDC and food-stamp errors over two years. Federal exposure ran as high as $144 million; Lt. Gov. MacKay argued only about $70 million of the total exceeded what would have occurred without the computer ([LA Times, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html)).

MacKay's defense deserves to be taken seriously rather than dismissed. Florida's food-stamp payment error rate was 10.89% against a 10.31% national rate in FY1990–91 — bad, but sixth-worst rather than anomalous, and the USDA penalty regime charges states only for the excess above the national average ([Tampa Bay Times, 1992](https://www.tampabay.com/archive/1992/08/03/state-faces-fine-of-5-million-for-food-stamp-errors/)). Automation made a pre-existing error problem **measurable and attributable** at scale. The system did not invent the errors; it industrialized their detection while simultaneously adding new machine-generated ones. Analysts of the period consistently underweighted this asymmetry: an integrated on-line system converts diffuse, unquantified caseworker error into a single auditable number with a federal price tag attached.

The counterweight is that error correction depended on functions the system never reliably performed. The Auditor General flagged HRS's failure to match welfare records against its own Bureau of Vital Statistics death file in 1989, 1991, 1993, and again in 1995, when roughly 12,000 recipients matched death records and 35% of a sampled subset remained active two months later ([Tampa Bay Times, Sept. 15, 1995](https://www.tampabay.com/archive/1995/09/15/hrs-supercomputer-can-t-hack-it-report-says/)). Integration was sold as the cure for exactly this class of defect and did not deliver it.

---

## 4a. What the machine actually grew into

The cost of error is one measure of the sizing failure. The machine itself is another, and it is now documented rather than inferred.

The design targets most widely reported in 1993 were 5 million transactions per day, 2.3 million welfare cases, and **12,000 terminals** ([LA Times, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html)). Those figures are press-reported and their derivation from the RFP has not been verified; the RFP itself remains unrecovered. They are nonetheless the only public statement of what the system was built to carry.

By January 1995 the Auditor General found the Department operating **"approximately 16,000 network devices consisting of terminals, workstations, printers, and controllers"** across the Central Office and fifteen districts (Auditor General Report No. 12581, September 12, 1995, ¶9). The two figures are not the same unit — terminals alone are some unstated fraction of the 16,000 — so the archive does not assert a percentage. What the record supports is plainer and sufficient: the reported design target was twelve thousand terminals, and within two years of full statewide conversion the installed estate was half again as large in devices of all classes.

**The configuration those devices attached to is the finding.** Report 12581 describes not one production machine but two:

> "The FLORIDA System's hardware configuration consists of an IBM ES3090/600J central processing unit (CPU) which is utilized for training, development, and data communications, and an IBM ES9021/982 CPU on which the production data is processed." (¶9)

The division of labor in that sentence rewards attention. A six-way 3090-600J is not a training machine. Training and development workloads in a shop of this size do not occupy top-of-line hardware; sixteen thousand attached devices do. The function in that list that justifies the machine is the third one, data communications — and the practical reading is that the network had become a workload requiring a host of its own.

Two consequences follow, and both make the capacity failure larger than the archive has previously stated.

**First, the processor bid bears almost no relation to the processor needed.** EDS proposed a 3090/300E, a three-way machine, and the winning demonstration was run on a larger 3090/400E ([DOAH 89-0003BID](https://www.doah.state.fl.us/ROS/1989/89000003.PDF) ¶¶71–72). By 1995 the 3090 in service was a **600J** — six engines and a generation beyond the E series. IBM restricted that conversion path so that only 600S or 600E machines could be upgraded to a 600J, which means the state's 3090 had first to be doubled in engine count and then converted. And the 600J was by then the *secondary* machine. Production had moved to an **eight-processor ES9021/982**, which IBM had announced in 1993 as the most powerful single-image commercial processor it offered.

**Second — and this is the part that reframes every published utilization figure — those figures describe only the application host.** The 95 percent regular-day and 100 percent peak measurements taken by the Department's consultant in October 1994, the roughly 95 percent recorded for the predecessor ES9021/900, and the 90 to 97.5 percent measured on the new ES9021/982 on May 1, 1995 are all figures for the machine that was *not* carrying the terminal network. The full production estate was that machine plus a six-way 3090 alongside it.

So the honest statement of the outcome is this. The State bid a three-way processor. Seven years later it was running an eight-way flagship for the application workload alone, with a six-way machine beside it absorbing the communications overhead, having capped the number of concurrent users and moved caseworkers onto nights and Saturdays — and the application host was still at ninety percent and above with six of its eight engines active.

That is not a forecast that was somewhat optimistic. It is a forecast wrong by a multiple large enough that two processor generations, a second host, and administrative rationing of the user population together failed to close the gap.

---

## 5. Contract architecture: § 7.11 and the buyer as judge

The single most consequential clause in the entire procurement was a paragraph most bidders would have skimmed. RFP § 7.11 provided that any dispute concerning contract performance "shall be decided by the HRS Contracting Officer," whose decision became final absent a petition to the Secretary of HRS within 30 days, with the Secretary's decision then "final, subject to the contractor's right to administrative and judicial review pursuant to Chapter 120" ([631 So. 2d 353](https://www.courtlistener.com/opinion/1895493/state-dhrs-v-eds-federal-corp/)).

EDS did not protest the RFP terms; it submitted a proposal with a letter accepting the RFP's provisions. When EDS later sued in circuit court, the First DCA granted HRS certiorari, quashed the trial court's order, and directed dismissal of nine of ten counts, holding that the statutory power to contract includes the power to agree to an alternative dispute-resolution procedure, and that EDS had waived direct judicial recourse. The court rejected EDS's arguments that HRS could not be impartial, that the clause had no time limits, and that money damages were unavailable administratively ([CaseMine full text](https://www.casemine.com/judgement/us/591485a5add7b049344c93d0/amp)).

**The second consequential modification was not litigated but negotiated.** On October 4, 1991, the Department and EDS signed a memorandum of understanding that modified the contract provisions requiring EDS to provide data for and to perform benchmark and capacity testing. Its documented terms are four. It established a basis for a benchmark/capacity test to be conducted after additional hardware upgrades were made by EDS's subcontractor, IBM. It released EDS from the contractual requirements to provide evidence of successful completion of benchmark/capacity tests relating to the initial stages of system implementation, which had already occurred. It provided that the Department would not assess liquidated damages against EDS for any delays associated with the completion of a benchmark test. And it provided that the Department and EDS would work together to develop revised response-time requirements — which were not developed and agreed upon before EDS terminated its participation on May 31, 1992 (Auditor General Report No. 12061, ¶57).

EDS alleged that the memorandum also released it from having to establish a system meeting the response times in the initial contract. The stated purpose of the memorandum was to establish a basis for "the timely completion of certain tasks relating to implementation of the FLORIDA System and to provide the amicable termination of the contractual relationship" between the Department and EDS. The Auditor General declined to characterize it further: "the legal effect of this modification is unknown and is currently the subject of litigation" (Report No. 12061, ¶57). The Auditor General separately found that this modification and the response-time modification lacked documented prior review and approval by fiscal, contract administration, and legal staff (¶48). The memorandum document itself is not reproduced in the report; its terms are, and this paper's earlier treatment of the modification's content as unknown was wrong.

The lesson for procurement practice is exact and still current: **a disputes clause is a pricing term.** By declining to protest § 7.11 in 1988 — and by affirmatively accepting it in writing — EDS surrendered forum selection on a nine-figure claim and lost roughly eighteen months to jurisdictional litigation before the merits were reached through a special master. Vendors routinely price schedule risk, liquidated damages, and acceptance criteria; far fewer price the cost of the remedy path.

---

## 6. What Webster actually found — a two-sided verdict

Webster's August 1995 recommendation is the closest thing to a neutral adjudication of the merits, and it went against both parties in different ways.

**For EDS:** "EDS did not warrant that it would provide a perfect or maintenance-free computer system," and while "FLORIDA system performance was not what HRS had hoped it would be when the system was turned over to HRS[,] [n]evertheless, it functioned properly, albeit imperfectly, and complied with the terms of the contract." Recommended award: $42 million plus interest accrued in some cases over three years; HRS recovered only $4.7 million ([Tampa Bay Times, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/)).

**Against EDS:** the March 1991 nondisclosure of the modeling error, which Webster held good faith and fair dealing required EDS to reveal — HRS general counsel Kim Tucker read this as a finding that EDS "actively defrauded the state of Florida by concealing unknown deficiencies," and the state signaled a follow-on fraud case ([Tampa Bay Times, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/)).

**Against HRS:** the Maximus episode. HRS's own independent reviewer concluded the system met standards; HRS told Maximus it would have to change that conclusion to be paid, gave Maximus a negative reference to Missouri, and then — the day after Maximus revised its conclusions — wrote Missouri a letter of recommendation ([Tampa Bay Times, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/)).

That sequence is the analytical center of gravity. The buyer that had contractually reserved to itself the role of first-instance judge under § 7.11 was found to have manipulated the evidentiary record produced by its own independent assessor. The 1993 grand jury presentment describing HRS officials violating laws, acting unethically, and intimidating subordinates ([Tampa Bay Times, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/)) fits the same pattern of institutional behavior.

---

## 7. Assessment

**Contract type was mismatched to requirement volatility.** A fixed-price-flavored build for a system whose scope is defined by federal AFDC, food-stamp, and Medicaid eligibility rules — rules that change on legislative and regulatory cycles the contractor cannot control — pushes both parties toward adversarial change management from day one. The $46 million unpaid-bill claim is the arithmetic residue of that mismatch.

**Sizing risk was unowned, and the standard that would have owned it was never enforced.** Nothing in the public record suggests either party independently validated the transaction-volume model before award. What the record now shows is that the contract did not need a new standard invented for it: response times were required to fall within one to eight seconds at least 95 percent of the time, sampled every 15 minutes on a randomly selected day each month at randomly selected work stations, and availability was required to be at least 97 percent during normal working hours over any consecutive 30-day period (Auditor General Report No. 12061, ¶51). This paper previously argued that no numeric standard existed. It did exist, and the correction matters because it relocates the defect from drafting to enforcement. Availability came in at 94 percent, then 80.5 percent, then 97.9 percent across the last three monthly periods of EDS's participation, and a manual response-time test the Department ran on May 13, 1992 produced an average of 2.8 minutes against a specification of one to eight seconds (¶¶52–53). Except for benchmark/capacity data EDS submitted in April 1992, no benchmark or capacity test was conducted by either party before EDS ceased participation on May 31, 1992 (¶56). The October 4, 1991 memorandum of understanding analyzed in Section 5 waived liquidated damages for benchmark-test delay and released EDS from evidence of successful tests for the implementation stages already completed (¶57). The Department's own account of why the tests did not run is in its written response to the finding: "Correspondence shows that EDS postponed and rescheduled these deliverables, thereby delaying the tests, until they were useless, since the system had already experienced performance problems and system unavailability" (Report No. 12061, Exhibit E, response to Finding #5). A standard with no test behind it prices like no standard at all. For a claimed 5-million-transaction-per-day, 12,000-terminal, 2.3-million-case workload ([LA Times, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html)), the root defect is the absence of a timely, independent acceptance test tied to that standard, together with the absence of any sustained utilization-headroom covenant — the contract quantified response time and availability, not processor headroom. The tool used to produce the winning capacity case was sound and is identified, with its documented input requirements, in the companion paper `FLORIDA-capacity-modeling-tools.md`; the inputs it was given are what no party to the procurement was in a position to check. The industry had the methodology by 1988 — audited benchmark disciplines and utilization-headroom rules were standard practice in commercial OLTP procurement. State-government procurement did not import them.

**And the contract structure rewarded undersizing.** Report 12581 records that the award was "a fixed price, single vendor contract that provided for system development, **hardware**, a telecommunications network, training and conversion activities, system implementation, and facilities management" (¶8). Bundling the iron into a fixed price makes every additional processor a charge against the bidder's own margin and confers no scoring advantage, and the quantified standards the contract did carry — response time and availability — constrained the delivered service rather than the size of the platform underneath it. The rational bid under those terms is the smallest platform that can be defended through evaluation — and the bid that won was $16.9 million cheaper than the one that lost by 4.4 points out of 350.

The structure then failed to hold the vendor to the consequence. When the platform proved inadequate, the additional equipment became the substance of the litigation EDS brought and won: the 1996 settlement paid EDS **$19,446,676 for district equipment and $13,188,325 for central processing equipment**, on top of $3,713,085 the Department had already paid for district equipment (Auditor General Report No. 13043, August 25, 1997). Roughly $30.3 million of FLORIDA mainframe equipment was received between fiscal years 1991-92 and 1993-94 (Report No. 12656), and the 1995 processor upgrade cost a further $5,438,079.75 (Report No. 12581, ¶23). A fixed price that excludes the machine the system actually needs is not a fixed price. Whether that outcome was foreseen by the bidder is not established by any document in this archive and is not asserted here; that the structure permitted it is.

One concession belongs alongside this. The Auditor General attributes the shortfall in part to "an unanticipated increase in the public assistance caseload" as well as to "inadequacies and inefficiencies in the System's initial hardware, software, and application programming design" (Report No. 12581, ¶45). Some of the volume growth was exogenous; welfare caseloads rose nationally in the early 1990s. That concession sharpens rather than weakens the finding. Every forecast of a decade-long workload is wrong. A contract whose response-time and availability standards are never tested on schedule, whose benchmark obligations are modified away in a 1991 memorandum, and which sets no utilization ceiling or headroom covenant, is one in which being wrong is automatically the buyer's problem — which is why the correction arrived as a $32.6 million settlement rather than a warranty claim.

**The incentive gradient favored escalation.** Undersizing produced upgrade revenue for the platform vendor, change-order revenue for the integrator, and, for the agency, a narrative in which the contractor was to blame. No participant's interest was served by an early, honest capacity disclosure — which is precisely what did not occur in March 1991.

**Institutional consequences outlasted the contract.** The Deloitte & Touche staffing contract terminated in March 1995 with an emergency award to Unisys ([Advanced Systems Design v. Strawn](https://caselaw.findlaw.com/court/fl-district-court-of-appeal/1203645.html)); a decade later the successor agency was still procuring programming support for the same FLORIDA system, with Unisys again protesting an award to Deloitte under RFP06U05DP4 ([DOAH Case 05-003144BID](http://flrules.elaws.us/doahcase/05-003144bid)). Florida's SNAP error-rate exposure remains a live fiscal issue — a 12.97% FY2025 rate carrying a projected penalty near $984 million ([WUSF, June 26, 2026](https://www.wusf.org/politics-issues/2026-06-26/usda-releases-florida-snap-error-rate-comes-with-penalty)). The structural problem FLORIDA was built to solve was not solved by FLORIDA, and arguably has not been solved since.

**Reputationally, the market absorbed the failure with remarkable indifference.** Within a year of terminating EDS and while suing and being sued by it, the Governor and Cabinet approved a new five-year, $24.2 million EDS contract with the Department of Education ([Tampa Bay Times, Apr. 28, 1993](https://www.tampabay.com/archive/1993/04/28/eds-wins-another-computer-contract/)). In the concentrated large-scale-integration market of the early 1990s, the pool of credible bidders was small enough that debarment-by-reputation was not economically available to the buyer.

---

## 8. Open research items

- **Resolved since first drafting:** the procurement is **RFP 88-74-BC**, identified from the DOAH protest record. The RFP document itself is still not digitized; likely locations are DCF procurement/records management, the Florida State Archives HRS record series, the Leon County circuit court case file exhibits, or HHS/FNS Advance Planning Document approval files. The numeric service levels are no longer unrecovered: Report No. 12061, ¶51, states them as one to eight seconds for at least 95 percent of measurements and 97 percent availability over any consecutive 30-day period. What is still missing is the RFP's own wording of them — see Appendix B, Part A.
- The 1993 statewide grand jury presentment text (Leon County / Office of Statewide Prosecution) — names of the two indicted HRS administrators and the specific IBM upgrade findings.
- The final circuit-court disposition of Webster's recommendation and any subsequent state fraud action against EDS; the record located here stops at the August 1995 recommendation with both sides filing objections.
- Florida Auditor General reports on FLORIDA. **Resolved, August 2026.** Reports No. **12581** (FLORIDA System, audit period Oct. 17, 1994–Feb. 28, 1995, issued Sept. 12, 1995) and No. **13043** ("HRS Settlement of FLORIDA Contract with EDS," period July 1, 1995–Dec. 31, 1996, issued Aug. 25, 1997) were obtained from the Auditor General's office on a Chapter 119 request, together with Nos. 12583, 12656, 12886, and **13287** (Systems Review of the FLORIDA System, Sept. 1997–Jan. 1998, issued July 27, 1998). None is available online. Report 12581 is the primary source for the capacity findings used above; note that the 95-percent figure originates with an independent consultant retained by the Department, in a report dated October 11, 1994, and the 65-percent commercial comparison is industry data the Department itself supplied — the Auditor General reported both rather than measuring them.
- **The earlier reports now have numbers.** Report 12581 identifies its predecessors as No. **11178** (March 1, 1989), No. **11619** (April 23, 1991), and No. **12061** (May 4, 1993), and describes itself as a follow-up to 12061, citing that report's paragraphs 49 through 59 on system capacity and response times. **Report 12061 was obtained on September 5, 2026** and establishes that the capacity and response-time failures were documented by the State's own auditor in May 1993, two years before the press reported them and three years before the settlement. It also supplies the quantified performance standard used in Sections 1, 5, and 7 above, and the terms of the October 4, 1991 memorandum of understanding at ¶57. Reports 11178 and 11619 have been requested.
- Contract values for the Deloitte & Touche engagement (June 1992) and the Unisys emergency award (March 1995), and any dollar accounting for the extended-hours and Saturday-shift program — see Appendix A.

---

# Appendix A — Remediation Measures, 1991–1997: Cost and Measured Effect

## A.0 Note on the evidence

The FLORIDA system's remediation record was, until recently, preserved in fragments. The two Auditor General reports that documented it in detail — **12581** and **13043**, identified in Section 8 above — were available only by mail request, and Report 12581's substance was known almost entirely through the [St. Petersburg Times account of September 15, 1995](https://www.tampabay.com/archive/1995/09/15/hrs-supercomputer-can-t-hack-it-report-says/), published three days after issuance. **Both reports were obtained in August 2026 and the tables below have not yet been revised against them.** Where a cell below cites the press account for a figure that Report 12581 states directly, the report supersedes it. The tables continue to separate what is documented from what is known to exist but not yet recovered, and that separation should be redrawn in the next revision.

## A.1 Remediation measures, cost, and measured effect

| # | Date | Measure | Type | Documented cost | Measured effect | Source |
|---|---|---|---|---|---|---|
| 1 | Mar. 1991 | EDS internally discovers the transaction-volume model was wrong; usable capacity is **half** of what both parties expected. Not disclosed to HRS; EDS instead attributes strain to rising caseloads | Concealed defect — the trigger for everything below | — | None; the four-year delay in disclosure is the proximate cause of the remediation sequence | [Tampa Bay Times, Aug. 16, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/) |
| 2 | 1991–92 | Caseworkers pulled onto manual conversion of food-stamp cases onto the new system; recertifications not performed, benefits auto-extended | Manual workaround | Not quantified | **Created** a USDA-mandated review of **399,320 cases** — a backlog itself delayed by computer shutdowns | [Tampa Bay Times, Aug. 3, 1992](https://www.tampabay.com/archive/1992/08/03/state-faces-fine-of-5-million-for-food-stamp-errors/) |
| 3 | FY 1992 | **444 additional HRS public-assistance workers** added, paired with automation, to attack the food-stamp error rate | Staffing | Not disclosed in the source | Error-rate reduction claimed by HRS; not independently measured in the record | [Tampa Bay Times, Aug. 3, 1992](https://www.tampabay.com/archive/1992/08/03/state-faces-fine-of-5-million-for-food-stamp-errors/) |
| 4 | May 31, 1992 | HRS terminates EDS as prime contractor | Contractual | — | Leads to items 5 and 8 | [Advanced Systems Design v. Strawn](https://caselaw.findlaw.com/court/fl-district-court-of-appeal/1203645.html) |
| 5 | June 1992 | **Deloitte & Touche** engaged to supply programmers and analysts; D&T subcontracts to Advanced Systems Design for at least three programmers | Application maintenance staffing | **Not located** | Sustained the codebase for three years | [Advanced Systems Design v. Strawn](https://caselaw.findlaw.com/court/fl-district-court-of-appeal/1203645.html) |
| 6 | 1992 | HRS commissions **Maximus** to review FLORIDA performance tests. Maximus finds the system performing to standards; HRS tells Maximus it must change its conclusion to be paid — and it does | Test review (compromised) | Not disclosed | Cited by special master Webster in his findings | [Tampa Bay Times, Aug. 16, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/) |
| 7 | c. 1992–93 | **First CPU upgrade** — HRS "decided to enlarge the computer and agreed to pay part of the cost," without knowing of the March 1991 modeling error | Hardware | **$5.1 million** | Not quantified. Became the subject of the statewide grand jury inquiry into favoritism toward IBM discussed in Section 3; **two staff lost their jobs** | [LA Times, May 2, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html); [Tampa Bay Times, Aug. 16, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/) |
| 8 | Apr. 1993 | **New five-year EDS contract** approved by the Governor and Cabinet while EDS's $46M suit against the state was pending | Contractual | **$24.2 million** | Retained the original builder's knowledge base | [Tampa Bay Times, Apr. 28, 1993](https://www.tampabay.com/archive/1993/04/28/eds-wins-another-computer-contract/) |
| 9 | 1993–94 | **Extended staff hours** — offices operating outside normal business hours because response time and capacity would not support the workload inside them | Operational (demand-side) | Not disclosed | Spread the workload across more clock hours | [Tampa Bay Times, Sept. 15, 1995](https://www.tampabay.com/archive/1995/09/15/hrs-supercomputer-can-t-hack-it-report-says/) |
| 10 | 1993–94 | **Rationing concurrent users** — HRS "limit[ed] the number of people using the system at the same time" | Operational (demand-side) | Not disclosed; borne as caseworker idle time and client wait | Held peak concurrency below the level at which response time collapsed | [Tampa Bay Times, Sept. 15, 1995](https://www.tampabay.com/archive/1995/09/15/hrs-supercomputer-can-t-hack-it-report-says/) |
| 11 | Jan.–June 1994 | **Schedule shifting** — some staff use moved to **nights and Saturdays** | Operational (demand-side) | Not disclosed | **Response time 8 s → 4 s.** The single largest measured improvement in the record | [Tampa Bay Times, Sept. 15, 1995](https://www.tampabay.com/archive/1995/09/15/hrs-supercomputer-can-t-hack-it-report-says/) |
| 12 | June–Dec. 1994 | Continued schedule and load management | Operational | Not disclosed | **Response time 4 s → 3 s** | [Tampa Bay Times, Sept. 15, 1995](https://www.tampabay.com/archive/1995/09/15/hrs-supercomputer-can-t-hack-it-report-says/) |
| 13 | Mar. 1995 | HRS **terminates Deloitte & Touche** and awards an **emergency contract to Unisys** — the losing 1988 protester. About **60 percent** of D&T programmers and support staff leave on or about Mar. 31, 1995, "creating a severe shortfall in the number of experienced computer programmers needed to maintain and upgrade the FLORIDA system" | Application maintenance | **Not located** | Net loss of maintenance capacity at the moment of greatest need | [Advanced Systems Design v. Strawn](https://caselaw.findlaw.com/court/fl-district-court-of-appeal/1203645.html) |
| 14 | c. Apr. 1995 | **Second CPU upgrade** | Hardware | **$5.4 million** | HRS told auditors the upgrade **"didn't match the need"** but improved performance **20 percent** | [Tampa Bay Times, Sept. 15, 1995](https://www.tampabay.com/archive/1995/09/15/hrs-supercomputer-can-t-hack-it-report-says/) |
| 15 | Aug. 1995 | Webster award: state to pay EDS **$42 million** plus interest accruing in some cases over three years; HRS recovers only **$4.7 million**; total exposure **more than $50 million** on top of **$200 million already spent** | Settlement of the remediation dispute | **$42M + interest** | Holding analyzed in Section 6 | [Tampa Bay Times, Aug. 16, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/) |

## A.2 What the interventions actually bought

| Period | Average response time | Intervening measure | Cost of that measure |
|---|---|---|---|
| June 1992 | **Minutes** | — | — |
| Jan. 1994 | **8 seconds** | First CPU upgrade (A.1 item 7) plus early operational changes | $5.1M |
| June 1994 | **4 seconds** | Shifting staff use to nights and Saturdays (item 11) | No capital cost identified |
| Oct. 11, 1994 | CPU at **95%** of capacity through most of the regular work day and **100%** at some peak times, as found by an independent consultant hired by the Department; the ~65% commercial-data-center comparison is industry data the Department obtained, not an Auditor General measurement | — | — |
| Dec. 1994 | **3 seconds** | Continued load management (item 12) | No capital cost identified |
| c. Sept. 1995 | Still "slow and overburdened"; upgrade "didn't match the need" | Second CPU upgrade (item 14), +20% | $5.4M |

## A.3 What the appendix shows

**Total identified capital remediation: $10.5 million.** Two CPU upgrades against a program that had consumed roughly $200 million by 1995 and generated a further $42 million judgment. GAO's [AIMD-94-52FS](https://www.govinfo.gov/content/pkg/GAOREPORTS-AIMD-94-52FS/html/GAOREPORTS-AIMD-94-52FS.htm) projected a $5.6 million Florida mainframe upgrade for FY1993–94, almost certainly the $5.4 million purchase that materialized. The hardware bill was small because hardware was never the binding constraint.

**The cheapest intervention was the most effective.** Moving staff to nights and Saturdays cut response time in half, from eight seconds to four. The $5.4 million CPU upgrade delivered 20 percent. Rescheduling human beings outperformed silicon by a wide margin — the signature of a workload whose peak concurrency, not whose aggregate throughput, had been mis-modeled. Spreading the same transactions across more hours works when the problem is a peak; buying more processor works when the problem is volume. That the former worked better is direct evidence about the shape of the defect, and it corroborates the utilization-headroom analysis in Section 7.

**The measures were overwhelmingly demand-side.** Of the fifteen entries, only two are capacity purchases. The rest ration, defer, or redistribute the load: limiting concurrent users, extending office hours, moving work to nights and weekends, deferring recertifications, and — in the 1991–92 conversion — simply not performing eligibility reviews and letting benefits auto-extend. That last workaround produced the 399,320 cases USDA required Florida to re-examine, and fed the error costs analyzed in Section 4.

**The costs were shifted onto people who could not refuse them.** Extended staff hours, Saturday shifts, and concurrent-user rationing appear in the record with no dollar figure attached because they were not paid for in appropriations. They were paid in caseworker overtime and displaced schedules, and in client waiting. The true remediation cost is therefore substantially larger than any figure in A.1, and structurally invisible in the accounting.

**A system running at 95 percent CPU on a regular work day was contractually compliant on headroom, and the standards it did carry went untested.** Earlier versions of this appendix said the contract set no performance standard at all. That was wrong: the contract required response within one to eight seconds at least 95 percent of the time and 97 percent availability over any consecutive 30-day period (Auditor General Report No. 12061, ¶51). What it did not require was headroom. The 60–65 percent utilization rule the same hearing officer had recited as a finding of fact in [88-2942BID ¶56](https://www.doah.state.fl.us/ROS/1988/88002942.PDF) nine months before award was a design convention, not a term, and nothing in the contract, in FAMIS, or in [45 CFR §205.37](https://www.law.cornell.edu/cfr/text/45/205.37) obliged the system to have any. The response-time and availability standards were breached during EDS's last months — 80.5 percent availability in the period ending April 28, 1992, and a 2.8-minute average on May 13, 1992 (¶¶52–53) — but the benchmark and capacity tests that would have established compliance were postponed, and the October 4, 1991 memorandum of understanding removed the liquidated-damages exposure for that delay (¶57). Every measure in this appendix exists because the standard that was written was never made to bite.

**The remediation destroyed its own maintenance capacity.** In March 1995, at maximum stress, HRS terminated Deloitte & Touche and lost roughly 60 percent of the programming staff overnight. The emergency award went to Unisys — the vendor that had protested the original procurement in 1988 and testified that the response times would not be met.

## A.4 Gaps, and how to close them

| Missing item | Where it likely exists |
|---|---|
| Dollar value of the extended-hours and Saturday-shift program (overtime, differentials) | HRS budget amendments. **Not Report 12581's workpapers:** under s. 11.45(4)(c), Fla. Stat., Auditor General workpapers are not public records and may be released only by majority vote of the Legislative Auditing Committee after a public hearing. Report 12581 itself describes the June 1994 user-limiting and off-peak scheduling plan (¶47) but states no cost for it |
| Contract values for Deloitte & Touche (1992) and the Unisys emergency award (Mar. 1995) | DCF contract files; Auditor General **13043** |
| Whether the concurrent-user limit was a technical cap or an administrative instruction, and at what number | Report 12581 workpapers; HRS operations memoranda |
| Any DASD, memory, or telecommunications upgrades 1991–1997 | APD Updates filed with HHS/ACF and USDA/FNS |
| Names of the two dismissed staff and the two indicted administrators; specific IBM-upgrade findings | 1993 statewide grand jury presentment, Leon County Clerk |
| Settlement accounting: what the $42M plus interest was actually paid for | Auditor General **Report 13043** |
| The October 4, 1991 memorandum of understanding itself. **Its terms are documented** — Report 12061 ¶57 reproduces all four, and Section 5 above sets them out; the signed document is not reproduced in the report and remains unrecovered | Leon County circuit court case file exhibits; DCF contract files |

All seven fall within the scope of records requests already drafted in this archive.

---

# Appendix B — Cost Reconciliation: From Bid to Bottom Line, 1988–1997

## B.1 Part A — What was bid and what was promised

| Element | As bid / as specified | Source |
|---|---|---|
| Winning bidder | **EDS Federal Corporation**, with IBM (hardware, software, telecommunications) and Touche Ross (public assistance software) | [DOAH 89-0003BID](https://www.doah.state.fl.us/ROS/1989/89000003.PDF) ¶65, ¶141 |
| Business proposal opened | November 22, 1988 | 89-0003BID ¶11 |
| **Total price bid** | **$107,658,141** | 89-0003BID ¶12 |
| **Present-value price bid** | **$88,914,316** | 89-0003BID ¶12 |
| Contract executed | May 15, 1989 | [631 So. 2d 353](https://www.courtlistener.com/opinion/1895493/state-dhrs-v-eds-federal-corp/) |
| Contract value as reported in the press | $104 million / **$104.2 million** — slightly below the bid, reflecting terms settled between award and execution | [LA Times, May 2, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html) |
| Losing bid not taken | Unisys: **$90,792,930** total / **$74,894,776** present value — $16.9M lower nominal, $14.0M lower in present value | 89-0003BID ¶13 |
| Margin of the decision | Unisys disqualified by **4.4 points out of 350** in one evaluation area, on a 6,000-point scale (EDS 5062.1, Unisys 4415.3) | 89-0003BID ¶11 |

### The performance promises

| Promise | What the record establishes | Source |
|---|---|---|
| Response time | **Quantified, and now documented.** For at least 95 percent of the time, response times were not to exceed a period ranging between one and eight seconds depending on the type of processing requested, measured every 15 minutes during a randomly selected day each month at randomly selected work stations. The numeric values do not appear in the surviving recommended order, which found only that "there is no credible evidence that the system proposed by EDS fails to satisfy any response times in the RFP or possesses insufficient capacity to handle the projected caseloads." Earlier versions of this table recorded the values as unrecovered; they were recovered from the 1993 systems review | Auditor General Report No. 12061, ¶51; 89-0003BID ¶73 |
| Availability | Within any consecutive 30-day period, the system was required to be available to users at least 97 percent of the time during normal working hours | Auditor General Report No. 12061, ¶51 |
| Acceptance mechanism | EDS was required to perform, or to provide the periodic data allowing the Department to perform, benchmark/capacity tests. Except for data submitted in April 1992, no such test was conducted by either party before EDS ceased participation on May 31, 1992. The October 4, 1991 memorandum of understanding released EDS from evidence of successful tests for implementation stages already completed and barred liquidated damages for benchmark-test delay | Auditor General Report No. 12061, ¶¶56–57 |
| Capacity headroom | **60–65 percent** CPU utilization, spikes to 80–85 percent, and "a processor should not be operated for more than a few minutes with utilization over 80 percent" — recited as a finding of fact nine months before award. A design convention, **not a contract term** | [DOAH 88-2942BID](https://www.doah.state.fl.us/ROS/1988/88002942.PDF) ¶56 |
| Scale | 2.3 million welfare cases, 5 million transactions per day, 12,000 terminals | [LA Times, May 2, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html) |
| Schedule | 26 months, extended to **29 months** after Unisys won the specifications protest | 88-2942BID Recommendation; 89-0003BID ¶5 |
| Risk allocation | **Fixed price with substantial monetary penalties for nonperformance** — the tribunal's stated reason for accepting unverified capacity assumptions | 89-0003BID ¶145 |
| Basis of the capacity case | "Elaborate computer modeling conducted by EDS and IBM"; the assumptions "were reasonable" | 89-0003BID ¶145 |

## B.2 Part B — What was actually contracted and spent

| # | Date | Item | Amount | Source |
|---|---|---|---|---|
| 1 | May 1989 | Original EDS contract | **$104.2 million** (bid $107.66M) | [Tampa Bay Times, Aug. 3, 1992](https://www.tampabay.com/archive/1992/08/03/state-faces-fine-of-5-million-for-food-stamp-errors/) |
| 2 | June 1992 | Deloitte & Touche programming/analyst contract | **Value not located** | [Advanced Systems Design v. Strawn](https://caselaw.findlaw.com/court/fl-district-court-of-appeal/1203645.html) |
| 3 | c. 1992–93 | First CPU upgrade | **$5.1 million** | [LA Times, May 2, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html) |
| 4 | Apr. 1993 | New five-year EDS contract | **$24.2 million** | [Tampa Bay Times, Apr. 28, 1993](https://www.tampabay.com/archive/1993/04/28/eds-wins-another-computer-contract/) |
| 5 | Mar. 1995 | Unisys emergency contract | **Value not located** | [Advanced Systems Design v. Strawn](https://caselaw.findlaw.com/court/fl-district-court-of-appeal/1203645.html) |
| 6 | c. Apr. 1995 | Second CPU upgrade | **$5.4 million** | [Tampa Bay Times, Sept. 15, 1995](https://www.tampabay.com/archive/1995/09/15/hrs-supercomputer-can-t-hack-it-report-says/) |
| 7 | 1989–95 | **Total actually spent as of August 1995** — the state's own reported figure, inclusive of items 1–6 | **$200 million** | [Tampa Bay Times, Aug. 16, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/) |
| 8 | Aug. 1995 | Webster award to EDS | **$42 million**, plus interest accruing in some cases over three years | [Tampa Bay Times, Aug. 16, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/) |
| 9 | Aug. 1995 | Reported total taxpayer exposure of the award package | **"More than $50 million"** | [Tampa Bay Times, Aug. 16, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/) |
| 10 | Aug. 1995 | Amount HRS recovered from EDS | **($4.7 million)** | [Tampa Bay Times, Aug. 16, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/) |

Items 3, 4 and 6 are components of the $200 million in item 7, not additions to it. The $200 million is the state's own cumulative reported spend as of August 1995. It is no longer the base for the reconciliation below; the Department's estimate of $310,621,339 through fiscal year 1996-97 is.

## B.3 Part C — Bottom line and overrun

### Procurement cost

**This part has been rebuilt.** Earlier versions of Appendix B assembled a cost floor of approximately $245,300,000 by adding the reported Webster exposure of more than $50 million to the $200 million cumulative spend the state reported to the press in August 1995 and subtracting the $4.7 million HRS recovered. That construction was an analyst's summation of press figures. It is superseded by the Department's own estimate, reported by the Auditor General, and the $245.3 million figure is retired — the error was one of sourcing, not of arithmetic.

| Line | Amount | Source |
|---|---|---|
| Department's initial projection of purchase and implementation, March 1989 | $81,100,000 | Report No. 12581, ¶12 |
| Cost through September 1993, per the Department's September 1994 Advance Planning Document Update | ~$118,000,000 | Report No. 12581, ¶12 |
| Cumulative spend reported by the state as of August 1995 | ~$200,000,000 | [Tampa Bay Times, Aug. 16, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/) |
| **Total cost of the FLORIDA System through fiscal year 1996-97, nonrecurring and recurring — the Department's own estimate** | **$310,621,339** | Auditor General Report No. 13287, p. 14 |

The Department's March 1989 projection of $81.1 million and the $107,658,141 EDS bid of November 1988 are not obviously reconcilable and may cover different scopes. This paper states both and does not choose between them.

| Comparison | Overrun | Multiple |
|---|---|---|
| Against the EDS bid of **$107,658,141** | **≈ $203.0 million (188 percent)** | **2.89×** |
| Against the executed contract of **$104.2 million** | **≈ $206.4 million (198 percent)** | **2.98×** |
| Against the **Unisys** bid of $90,792,930 rejected by 4.4 points | ≈ $219.8 million (242 percent) | 3.42× |

This is a floor, not a total. The Department's estimate stops at fiscal year 1996-97; it excludes three decades of subsequent operation, the unrecovered values of the Deloitte & Touche and Unisys contracts, and the uncosted operational remediation catalogued in Appendix A. Items 1 through 10 in Part B are components of it rather than additions to it.

### Consequential cost, outside the procurement ledger

| Item | Amount | Source |
|---|---|---|
| USDA food-stamp error penalty, FY ended Sept. 30, 1991 | **$5 million** | [Tampa Bay Times, Aug. 3, 1992](https://www.tampabay.com/archive/1992/08/03/state-faces-fine-of-5-million-for-food-stamp-errors/) |
| Cumulative benefit-payment errors by May 1993 — $232M AFDC and food stamps over two years, $28M Medicaid | **$260 million** | [LA Times, May 2, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html) |
| Federal penalty exposure under negotiation, 1993 | **up to $144 million** | [LA Times, May 2, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html) |
| Acting Secretary MacKay's estimate of errors attributable to the system itself | ~$70 million | [LA Times, May 2, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html) |

### Who paid

Florida drew **$184.87 million** in federal automated-welfare-system funds between FY1984 and FY1992 — $71.59 million enhanced, $113.28 million regular — with FAMIS development continuing through FY1994 at an estimated $13.5 million remaining plus a projected $5.6 million mainframe upgrade ([GAO/AIMD-94-52FS](https://www.govinfo.gov/content/pkg/GAOREPORTS-AIMD-94-52FS/html/GAOREPORTS-AIMD-94-52FS.htm)).

## B.4 The reconciliation in one line

Florida rejected a bid $16.9 million cheaper in nominal terms and $14.0 million cheaper in present value, on a 4.4-point margin out of 6,000, in favor of a capacity case whose assumptions the tribunal declined to examine because the contract was fixed-price with penalties. The fixed price held for approximately three years. The state then paid for two CPU upgrades on a defect it did not know existed, signed a $24.2 million follow-on with the contractor then suing it for $46 million, and ended by paying that contractor a further $42 million plus interest under a holding that the system "functioned properly, albeit imperfectly, and complied with the terms of the contract."

**The bid was $107,658,141. The Department's own estimate of total cost through fiscal year 1996-97 is $310,621,339. The overrun is approximately $203.0 million, or 188 percent — and the fixed-price contract that was the stated basis for accepting the risk is the instrument through which the overrun was collected.** The floor this paper previously published, $245.3 million and 128 percent, was built from press-reported spend and understated the cost by roughly $65 million.

---

*Prepared July 26, 2026; Appendices A and B added July 28, 2026. All figures and quotations are drawn from the linked contemporaneous sources; where accounts differ (e.g., $104 million vs. $104.2 million contract value), both are noted. Dollar figures are nominal unless expressly identified as present value.*
