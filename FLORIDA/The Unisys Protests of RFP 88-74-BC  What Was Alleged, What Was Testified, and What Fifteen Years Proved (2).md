# The Unisys Protests of RFP 88-74-BC: What Was Alleged, What Was Testified, and What the Next Fifteen Years Proved

An evidence-based analysis prepared for the Kastner research archive
July 27, 2026

---

## Abstract

The FLORIDA procurement is one of the clearest documented cases in American public-sector computing of a failure that was visible in the record before it happened and could not be stopped by the machinery built to catch it. Between May 1988 and March 1989, an administrative tribunal found on the record that the winning transfer base had never issued a benefit check to a real client and was centrally rather than distributedly architected, that state evaluators had scored it as implemented and distributed anyway, that scoring data in four of eight areas was statistically indistinguishable from random numbers, that neither the evaluators nor anyone else fully understood the IBM capacity models on which the award turned — and it upheld the award, because *Groves-Watkins* deference does not permit a hearing officer to substitute a better technical judgment for an honest agency one. The tribunal's stated safeguard was the contract itself: a fixed price with substantial nonperformance penalties, which it treated as sufficient guarantee that optimistic capacity assumptions would be disciplined. Every subsequent event falsified that premise. EDS learned in March 1991 that the assumptions behind its model had overstated usable capacity by roughly half and did not disclose it; the state co-funded the remediation without knowing why; the machine ran at 95–100% CPU against the 60–65% headroom rule the same hearing officer had recited as a finding of fact nine months before award; response times reached minutes; $260 million in benefit errors accumulated; a grand jury found officials had broken laws and intimidated subordinates; and the special-master proceeding the contract's own dispute clause compelled ended with the state owing the contractor $42 million plus interest on top of $200 million already spent, on a holding that the system "complied with the terms of the contract." The historical importance lies in the conjunction: federal approval under FAMIS and 45 C.F.R. § 205.37 specified process deliverables and no performance numbers, exactly as GAO had warned in 1981 and repeated in 1992; state bid-protest law reviewed honesty rather than engineering; and the contract's performance terms proved enforceable by the vendor and not against it. Three independent control systems, each functioning as designed, together permitted a $107 million procurement to be awarded on capacity modeling nobody could verify, to a bidder $14 million more expensive in present value, over a competitor disqualified by 4.4 points out of 6,000 — and the one participant who testified that the response times would not be met was discounted for insufficient familiarity with the very models whose inputs turned out to be wrong.

---

## 0. Provenance of the evidence

This analysis rests on two primary documents recovered in full from the Florida Division of Administrative Hearings, both signed by Hearing Officer Robert E. Meale:

- **Recommended Order, *Unisys Corporation v. Department of Health and Rehabilitative Services*, DOAH Case No. 88-2942BID**, entered August 4, 1988 — the specifications protest ([DOAH](https://www.doah.state.fl.us/ROS/1988/88002942.PDF))
- **Recommended Order, *Unisys Corporation v. Department of Health and Rehabilitative Services, and E.D.S. Federal Corporation, Intervenor*, DOAH Case No. 89-0003BID**, entered March 14, 1989 — the award protest ([DOAH](https://www.doah.state.fl.us/ROS/1989/89000003.PDF))

Both identify the solicitation as **Request for Proposal 88-74-BC, issued May 20, 1988** (89-0003BID ¶1; 88-2942BID ¶1) — the number that appears in no court opinion, news account, or archival catalog located in this research.

Secondary evidence is drawn from the First District Court of Appeal's 1994 opinion, contemporaneous press coverage, Florida Auditor General report listings, and federal audit literature, each cited at point of use. The **hearing transcripts of both proceedings do not survive**; Florida's general records schedule assigns permanent retention to final orders but only five years to the supporting evidentiary record.

---

## 1. What Unisys protested — two distinct actions

### 1.1 The specifications protest (May–August 1988)

Unisys filed a notice of intent to protest on **May 25, 1988 — five days after the RFP issued** — and a corrected formal protest on June 14. Three provisions were litigated: the prohibition against proposals incorporating the Unisys A-15 mainframe already installed in the HRS Jacksonville Data Center; the sufficiency of the 26 months allowed for statewide implementation; and the sufficiency of time allotted to each task (88-2942BID, Background).

Unisys lost the A-15 issue and won on schedule. Meale recommended amending RFP 88-74-BC "to allow 29 months between the date that the contract is signed and the completion of implementation and conversion," plus a clarification of conversion responsibilities under Task 15 (88-2942BID, Recommendation). The 89-0003BID order confirms the outcome: "As a result of a protest by Unisys Corporation (Unisys) of certain provisions in the RFP, HRS later extended by three months the time within which the vendor would be required to implement the system" (¶5).

**The finding that matters most in hindsight is not the outcome but a fact recited in passing.** In establishing why the A-15 could not absorb FLORIDA, the 1988 order states the governing engineering rule:

> "No more than 60 percent-65 percent of the processing capacity of a mainframe such as the A-15 should be utilized because on-line user demands will occasionally spike to 80 percent-85 percent. At such high rates of utilization, the response time of the computer is slowed considerably, and generally a processor should not be operated for more than a few minutes with utilization over 80 percent." (88-2942BID ¶56)

The order records the A-15 at 51% utilization during working hours as of June 1988, up from 28% in February 1987, with May 1988 peaks near 75%, and concludes HRS "reasonably anticipates that the A-15 will have to be upgraded, due to insufficient processor capacity" (¶55–56).

The 60–65% headroom standard was therefore **in the administrative record of this procurement, as a finding of fact, nine months before award** — applied to the incumbent's machine as grounds for excluding it.

### 1.2 The award protest (December 1988–March 1989)

Proposals from Unisys, EDS, and CSX Technology were submitted September 30, 1988 (¶6). HRS declared the Unisys and CSX technical proposals nonresponsive and, at 4:30 p.m. on November 28, 1988, noticed intent to award to EDS. Unisys filed notice of protest on December 1 and its formal protest on December 12 (¶14–15). CSX protested and later dismissed (¶16).

**The scoring.** Eight weighted areas totaling 6,000 points, with dual thresholds: 70% in each area and 4,500 points (75%) overall (¶7–9). Final weighted scores: **EDS 5,062.1; Unisys 4,415.3; CSX 4,296.9** (¶10). EDS alone cleared both thresholds. Unisys cleared 70% in seven of eight areas, "missing the threshold by 4.4 of a possible 350 points in the area of Operations Management Approach" (¶11).

**The prices, which were never allowed to matter.** EDS: total $107,658,141, present value $88,914,316 (¶12). Unisys: total $90,792,930, present value $74,894,776 (¶13). The HRS Secretary opened the Unisys business proposal — an extraordinary step under RFP ¶2.2.6 — precisely "based upon the narrow margins by which the Unisys Proposal failed to satisfy the above-described thresholds" (¶19). **Unisys was disqualified by 4.4 points out of 6,000 from a bid roughly $17 million cheaper in nominal terms and $14 million cheaper in present value.**

**The grounds.** Unisys spent over $2 million preparing an 18-volume technical proposal (¶17, ¶19) and alleged, in substance:

1. **Transfer-base responsiveness.** The RFP required offerors to identify "existing, operational" systems for transfer, or systems that "will have completed testing" before the demonstration (¶26). EDS proposed Ohio's CRIS-E as the public-assistance and client-registration base. Meale found flatly: "CRIS-E is not operational. At the time of its selection by EDS, CRIS-E was due to have completed acceptance testing in September or October, 1988. As of November 4, 1988, which was the date of the EDS system demonstration, CRIS-E had not completed user acceptance testing" (¶57). He nonetheless held the operational and completed-testing sentences were not mandatory requirements (¶46) and that CRIS-E had completed "what amounted to system testing" (¶58).
2. **Key personnel residency** — rejected (¶60–69).
3. **Demonstration hardware substitution.** EDS demonstrated on a 3090/400E but proposed a 3090/300E, one processor fewer (¶71). Held permissible because the RFP required only "hardware compatible with that proposed" (¶71–72).
4. **Capacity and response times** — the subject of §2 below.
5. **Evaluation integrity**, including statistical unreliability of scoring.

**The evaluation findings are damning on their own terms and were then set aside as immaterial.** On question 8, evaluator Kuecks "stated incorrectly that CRIS-E had been implemented, served a number of cases or clients, and utilized distributed system architecture," and "offered no rational explanation... his scores were simply incorrect" (¶136). Evaluator Gettis scored EDS a perfect 10 "even though the CRIS-E System's stage of development clearly precluded a perfect score," citing an "excellent" distributed processing procedure while ignoring "that CRIS-E is an example of centralized architecture" (¶137). On questions 19 and 24, Kuecks wrote that "all proven components will be used" when "the CRIS-E System was still in acceptance testing and had never been proven by actual use in the field" (¶143). Meale summarized the underlying reality: CRIS-E "has never been implemented, does not serve any clients or cases, and features centralized architecture rather than the distributed architecture sought by HRS" (¶134), while the Unisys New York bases "have been implemented and certified" and "feature distributed architecture" (¶135).

Unisys's statistical experts showed that for four scoring areas the evaluators' data "cannot be differentiated from randomly generated data" under the Intraclass Correlation Coefficient (¶163). Meale accepted that "the absence in reliability among the evaluation data was statistically significant" but held it "of no practical significance," reasoning that the tests or standards "are unsuitable" for a procurement of this subjectivity and scale (¶159, ¶161, ¶164, ¶167).

He concluded the irregularities "are immaterial in light of the complexity and magnitude of the FLORIDA System, RFP, and evaluation process" (¶151) and recommended dismissal (Recommendation, Mar. 14, 1989). HRS adopted the order in toto on March 24, 1989. There was no appeal — a search of Florida's appellate case index returns no Unisys v. HRS proceeding from this era.

---

## 2. What Kastner testified

The testimony survives only as it was characterized in the appendix rulings on Unisys's proposed findings of fact. Three passages are dispositive.

**On response times** — proposed finding 85, second sentence, was "rejected as against the greater weight of the evidence, which does not support the testimony of Mr. Kastner that the EDS system would not satisfy the specified response times" (89-0003BID, Appendix ¶85).

**On weight** — proposed finding 89 was rejected because "the weight accorded to Mr. Kastner's testimony was limited by his incomplete understanding of the complex IBM modeling programs and the distribution of certain processing functions in the system proposed by EDS" (Appendix ¶89).

**On the modeling itself** — the ruling on proposed finding 90 is the most revealing document in the entire record, because it concedes the premise and rejects the conclusion:

> "It is true that the data generated by the IBM modeling programs are no better than the assumptions that went into the models. It is also true that the HRS evaluators' understanding of the models, assumptions, and even the resulting data was incomplete. However, as noted in the recommended order, the capacity-planning assumptions are reasonable. The contract in this case is for a fixed price and contains substantial monetary penalties for nonperformance. Under these circumstances, the incompleteness of the evaluators' understanding of the model, assumptions, and data did not render their scoring arbitrary or capricious. This is a highly technical area whose complexities confused even Unisys' expert witness. The scoring was rational." (Appendix ¶90)

The corresponding findings of fact read: "The relatively high scores given EDS and low scores given Unisys in response to questions concerning capacity planning and rationale were justified in view of the elaborate computer modeling conducted by EDS and IBM in simulating the performance of the system proposed by EDS. Moreover, the assumptions that went into the modeling, which are critical to the success of the simulation, were reasonable. Also, the motivation to develop accurate assumptions is strong due to the severe provisions for damages in the fixed-price contract" (¶145). And: "The capacity planning of EDS is superior to that of Unisys because of the latter's reliance upon extrapolations from existing case loads versus the former's use of sophisticated computer simulation models. Also, there is no credible evidence that the EDS system would fail to satisfy any applicable response times set forth in the RFP" (¶146). Elsewhere the tribunal attributed the entire capacity allegation to "a misinterpretation of data produced by certain modeling programs designed to assess system capacity and response times" (¶73).

**The structure of the ruling.** Kastner's proposition was that the EDS configuration would not meet the RFP's response times. The tribunal did not find the modeling correct on the merits; it found the assumptions "reasonable," inferred their reliability from the contract's fixed price and damages provisions, and discounted the contrary witness for lack of familiarity with IBM's modeling tools. Three of the four supports for that holding are non-technical: the sophistication of the method, the incentive structure of the contract, and the credentials gap. Only "the assumptions... were reasonable" is a substantive engineering finding, and it is stated without analysis.

Note also that HRS's own evaluators were found not to understand the models, the assumptions, or the output (Appendix ¶90) — yet their scores on precisely those questions were upheld as rational.

---

## 3. What the next fifteen years established

| Date | Event | Source |
|---|---|---|
| May 15, 1989 | HRS and EDS execute the contract, incorporating RFP sections including the § 7.11 disputes clause | [631 So. 2d 353](https://www.courtlistener.com/opinion/1895493/state-dhrs-v-eds-federal-corp/) |
| **March 1991** | EDS internally discovers its transaction-volume model was wrong; usable capacity is roughly **half** what both parties expected. EDS does not disclose. HRS later agrees to help fund an enlargement without knowing why | [Tampa Bay Times, Aug. 16, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/) |
| 1991 | System begins handling live welfare cases | [LA Times, May 2, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html) |
| June 1992 | Average response time measured in **minutes** | [Tampa Bay Times, Sept. 15, 1995](https://www.tampabay.com/archive/1995/09/15/hrs-supercomputer-can-t-hack-it-report-says/) |
| 1992 | HRS conditions payment to independent reviewer Maximus on reversing its finding that the system met standards | [Tampa Bay Times, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/) |
| May 31, 1992 | EDS terminates the contract | [Tampa Bay Times, Apr. 28, 1993](https://www.tampabay.com/archive/1993/04/28/eds-wins-another-computer-contract/) |
| Aug. 1992 | USDA assesses ~$5M food-stamp error penalty; Florida error rate 10.89% vs. 10.31% national | [Tampa Bay Times, Aug. 3, 1992](https://www.tampabay.com/archive/1992/08/03/state-faces-fine-of-5-million-for-food-stamp-errors/) |
| Aug. 21, 1992 | EDS files a ten-count complaint, Leon County Case 1992 CA 003618, seeking >$45M | [631 So. 2d 353](https://www.courtlistener.com/opinion/1895493/state-dhrs-v-eds-federal-corp/) |
| May 1993 | $260M cumulative errors; up to $144M federal exposure; statewide grand jury examining whether HRS improperly favored **IBM** on a $5.1M upgrade; two staff out | [LA Times, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html) |
| 1993 | Grand jury presentment: HRS officials violated laws, acted unethically, intimidated subordinates; two administrators indicted | [Tampa Bay Times, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/) |
| Feb. 7, 1994 | First DCA quashes the circuit order, forcing EDS into the § 7.11 procedure | [631 So. 2d 353](https://www.courtlistener.com/opinion/1895493/state-dhrs-v-eds-federal-corp/) |
| Mar. 1995 | HRS terminates the Deloitte & Touche programming contract; emergency award to **Unisys** | [Advanced Systems Design v. Strawn](https://caselaw.findlaw.com/court/fl-district-court-of-appeal/1203645.html) |
| Aug. 16, 1995 | Special master William Webster recommends the state pay EDS $42M plus interest; HRS recovers $4.7M; ~$200M spent | [Tampa Bay Times, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/) |
| Sept. 12, 1995 | Auditor General Report 12581: CPU at **95–100% utilization** through most of the business day against a ~65% commercial norm; a $5.4M CPU upgrade five months earlier yielded ~20% improvement; response times 8s (Jan. 1994) → 4s (June, after moving work to nights and Saturdays) → 3s (Dec.) | [report listing](https://flauditor.gov/pages/list9596page.htm); [Tampa Bay Times, Sept. 15, 1995](https://www.tampabay.com/archive/1995/09/15/hrs-supercomputer-can-t-hack-it-report-says/) |
| Oct. 25, 1995 | State counter-suits filed: HRS v. EDS (1995 CA 005279) and Attorney General Butterworth v. EDS (1995 CA 005280) | Leon County Clerk case index |
| Aug. 25, 1997 | Auditor General Report 13043, "HRS Settlement of FLORIDA Contract with EDS" | [FY97-98 listing](https://flauditor.gov/pages/list9798page.htm) |
| Aug. 6, 1998 | Auditor General Report 13287, DCF (Florida System) — follow-up audit | Florida Auditor General report index |
| 2005 | Unisys protests award of FLORIDA-system programming support (RFP06U05DP4) to Deloitte, DOAH Case 05-003144BID | [flrules.elaws.us](http://flrules.elaws.us/doahcase/05-003144bid) |

### 3.1 The vindication, stated precisely

Two findings of the 1989 order were tested by events and failed.

**"The assumptions that went into the modeling... were reasonable" (¶145).** Webster found that by March 1991 EDS knew the assumptions behind its capacity model had overstated usable capacity by roughly a factor of two, and that "good faith and fair dealing required EDS to disclose the erroneous modeling assumption to HRS" ([Tampa Bay Times, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/)). The assumptions were not reasonable. The specific failure mode Kastner was discounted for not understanding — the inputs to the IBM models — is the failure mode that occurred.

Webster's own phrase repays attention. He did not write that EDS had an erroneous model. He wrote **"the erroneous modeling assumption,"** singular, locating the defect in an input rather than in the tool. The distinction runs through the archive and is developed in `FLORIDA-capacity-modeling-tools.md`: IBM's simulator was sound and widely used, the transferred Ohio code was real enough to yield instruction and I/O counts, and the parameter that governed the answer — the mix of transactions a caseworker actually generates — was a fact about an operating welfare agency that no bidder could derive from software and that only the losing bidder had measured.

**"There is no credible evidence that the EDS system would fail to satisfy any applicable response times set forth in the RFP" (¶146).** By June 1992 response times were measured in minutes; in January 1994 they were 8 seconds; and the machine ran at 95–100% CPU against the 60–65% standard the same tribunal had recited in the companion case ([Tampa Bay Times, Sept. 15, 1995](https://www.tampabay.com/archive/1995/09/15/hrs-supercomputer-can-t-hack-it-report-says/); 88-2942BID ¶56).

The 1989 tribunal was thus wrong on the technical merits and right on the law it applied. Under *Department of Transportation v. Groves-Watkins Constructors*, 530 So. 2d 912 (Fla. 1988), quoted at 89-0003BID ¶179, the inquiry is "limited to whether the purpose of competitive bidding has been subverted," and an agency's honest exercise of discretion stands "even if it may appear erroneous and even if reasonable persons may disagree" (¶180, quoting *Liberty County v. Baxter's Asphalt & Concrete*, 421 So. 2d 505, 507 (Fla. 1982)). Meale found the scoring irregularities real but not subversive (¶172, ¶181). **The protest was not lost because the engineering was wrong; it was lost because Florida procurement law does not permit a tribunal to second-guess technically incorrect but honestly reached agency judgments.**

### 3.2 The load-bearing assumption that collapsed

The single sentence carrying the most weight in Appendix ¶90 is: "The contract in this case is for a fixed price and contains substantial monetary penalties for nonperformance."

That reasoning is a bet that contractual incentives will discipline technical optimism. Every subsequent event falsified it. EDS discovered the error and stayed silent while HRS co-funded the remediation ([Tampa Bay Times, 1995](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/)). The nonperformance penalties produced $4.7 million for the state against $42 million plus interest for the contractor. And Webster's operative holding — the system "functioned properly, albeit imperfectly, and complied with the terms of the contract" — establishes that the performance obligations the 1989 tribunal relied on as a guarantee were not, in the event, enforceable against the delivered configuration.

This is consistent with the federal requirements framework the RFP inherited. To draw 90% federal match, HRS had to satisfy FAMIS and secure Advance Planning Document approval (89-0003BID ¶3–5), and [45 C.F.R. § 205.37](https://www.law.cornell.edu/cfr/text/45/205.37) enumerates required APD contents — requirements analysis, information flows, security, cost-benefit analysis, implementation plan with "proposed acceptance criteria" — while specifying no throughput, response-time, availability, or utilization standard. GAO had warned at FAMIS's inception that the requirements "do not contain sufficiently specific performance standards for evaluating the quality of State developed systems" ([GAO/HRD-81-119](https://www.gao.gov/products/hrd-81-119)) and repeated the systemic finding in [GAO/IMTEC-92-29](https://www.gao.gov/products/imtec-92-29).

### 3.3 The subcontractor thread

The EDS team was disclosed as: "IBM for hardware, system software, and telecommunications; Touche Ross for the public assistance application system software; IV-D Systems for the CSE application system software; Florida State University for training; and MIS Software Development for conversion and system services" (¶65). Touche Ross was also "responsible for the development of" Ohio CRIS-E (¶141), and its Development Manager for CRIS-E, Tim Wiest, was named EDS's Technical Manager for the public assistance and client registration modules (¶67).

Two consequences follow across the fifteen years. **IBM**, whose modeling supplied the capacity case that defeated the protest, became the vendor of the remediation hardware — the $5.1 million upgrade that drew a grand jury in 1993 and the $5.4 million upgrade that produced a 20% improvement in 1995. **Touche Ross**, successor Deloitte & Touche, held the programming contract that HRS terminated in March 1995, whereupon the emergency award went to Unisys — the protester. By 2005 the pattern had inverted again, with Unisys protesting an award of FLORIDA-system support to Deloitte ([DOAH 05-003144BID](http://flrules.elaws.us/doahcase/05-003144bid)).

---

## 4. Analytical conclusions

**The dispositive margin was 4.4 points on a 350-point subscore.** Unisys was ruled nonresponsive by 0.07% of the total scoring scale, on the one area — Operations Management Approach — where Meale separately found an evaluator's scoring "inconsistent" (¶155) and unsupported ("no basis to differentiate between the respective proposals," ¶148). He then showed the threshold would still have been missed by 0.8 points with that evaluator's scores removed entirely (¶155). A procurement design in which a $14 million present-value price advantage is extinguished by a sub-one-point subjective scoring margin is not a robust design, whatever the merits of the winner.

**The tribunal identified the correct technical standard and did not apply it to the winning bid.** The 60–65% utilization rule appears as a finding of fact in the companion case (88-2942BID ¶56), used to justify excluding the incumbent's machine. Nothing in the award order applies that standard to the proposed EDS configuration; the capacity findings rest on the sophistication of the modeling method rather than the headroom of the result. The system that won was later found running at 95–100%.

**Methodological sophistication was treated as evidence of accuracy.** EDS's simulation modeling was rated superior to Unisys's caseload extrapolation (¶146), and this comparative judgment substituted for validation of either result. The record explicitly concedes that model output "are no better than the assumptions" (Appendix ¶90) and then declines to test the assumptions. In 1991 the assumptions proved wrong by roughly half.

**The expert-credibility finding inverted over time.** Kastner's testimony was discounted for "incomplete understanding of the complex IBM modeling programs" (Appendix ¶89); the evaluators whose understanding was equally "incomplete" (Appendix ¶90) were upheld. Six years later the modeling was found erroneous and concealed. The asymmetry is instructive for expert practice in administrative fora: a challenger's technical dissent is measured against the sophistication of the incumbent method, not against the eventual behavior of the system.

**The administrative record was more accurate than the adjudication.** Every fact needed to predict the outcome is in the 1988–89 orders: CRIS-E never implemented and centrally architected (¶57, ¶134), evaluators recording it as implemented and distributed (¶136–137, ¶143), scoring data indistinguishable from random in four areas (¶163), and the utilization rule that would later be breached (88-2942BID ¶56). What was missing was not evidence but a legal standard permitting a tribunal to act on it. *Groves-Watkins* deference, applied to a technically incorrect but honest agency judgment, converted an accurate record into an adverse result.

---

## 5. Evidence inventory and remaining gaps

**Held in full:** both recommended orders (PDF and extracted text). **Confirmed non-surviving or unlocated:** the hearing transcripts of both proceedings; RFP 88-74-BC itself; the Evaluation Manual; the Unisys 18-volume technical proposal; Webster's August 1995 report.

**Highest-value outstanding targets**, in order: Auditor General Report 13043 (the settlement audit) and 12581 (the 1995 performance audit); the Carlton Fields closed-file archive for the 1988–89 transcripts and exhibits; the HHS/ACF and USDA/FNS Advance Planning Document files, which would establish whether any quantified performance standard existed in the federally approved requirements; and the 1993 grand jury presentment.

A note on citation practice for the archive: paragraph numbers above refer to the numbered findings of fact in each recommended order, and "Appendix ¶N" refers to the rulings on Unisys's proposed findings, which are numbered separately at the end of the 89-0003BID order.
