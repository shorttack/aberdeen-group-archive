# One Bad RFP Away: Federal Rules on State Benefit Systems, 1996–2026

*A short update to "The Empty Center: Federal Welfare-Systems Policy, 1986–1999"*

**Peter Kastner Research Archive** · July 27, 2026

---

## The short answer

No. It is not one bad RFP away. It already happened again, in Florida, to a system procured by the same state that procured FLORIDA, and the federal government still had no standard that would have caught it.

---

## What the federal rules added after 1996

The regulatory framework did not stand still. Four things were genuinely added, and it is worth being precise about each, because the gap that survived them is what matters.

**Independent Verification and Validation, October 28, 2010.** The APD rewrite at [75 FR 66340](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-95/subpart-F) created 45 CFR §95.626 — the first federal provision in the history of state welfare automation to use the words *capacity planning* as an obligation rather than a budget line. An IV&V contractor must "provide risk management assessment and capacity planning services" and "develop performance metrics which allow tracking project completion against milestones set by the State," and must report to the federal agency at the same time it reports to the state. But IV&V "may be required" only where a project already shows one of eight risk triggers — missed deadlines, cost overrun, at risk of failure. It is a distress signal, not a gate. And the verifier is retained by the state.

**Medicaid standards and conditions, 2011 and 2015.** [42 CFR §433.112(b)](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-433/subpart-C) now conditions the 90 percent match on a list that includes modularity, open interfaces, separation of business rules from core code, and — at (b)(17), the closest thing in the HHS framework to an engineering criterion — that a state "must have delivered acceptable MAGI-based system functionality, demonstrated by performance testing and results based on critical success factors, with limited mitigations and workarounds." Read closely, "performance" there means functional correctness, not throughput. The section still contains no number.

**CCWIS, June 2, 2016.** [45 CFR §§1355.52–.57](https://www.ecfr.gov/current/title-45/subtitle-B/chapter-XIII/subchapter-G/part-1355/section-1355.52) replaced SACWIS with data-quality and modularity requirements for child welfare systems. Again functional, again unquantified.

**The real exception: SNAP, January 2, 2014.** The one place where the federal government finally wrote down what the 1988 FLORIDA record shows was missing is FNS's rewrite of [7 CFR §277.18](https://www.ecfr.gov/current/title-7/subtitle-B/chapter-II/subchapter-C/part-277/section-277.18) at **79 FR 12**. It now requires a complete test plan before testing begins; documented User Acceptance Testing results delivered to FNS, with FNS concurrence to move from test to pilot "a condition for continued FFP"; acceptance testing that must include "error condition handling and destructive testing, security testing, recovery testing, controls testing, **stress and throughput performance testing**, and regression testing"; verification that the system complies with "performance standards including responsiveness, usability, capacity and security"; and a live-production pilot, usually at least three months, before statewide rollout, with FNS approval again a condition of continued funding.

That is, substantively, the rule whose absence defined the FLORIDA disaster. It arrived on **January 2, 2014** — twenty-five and a half years after Florida issued RFP 88-74-BC, and it applies to SNAP.

## What was still missing when the test came

Six years after that SNAP rule, the largest simultaneous load test in the history of American public administration arrived. It did not fall on SNAP eligibility systems. It fell on unemployment insurance, which sits under the Department of Labor and outside every regulation described above.

The result is documented by the federal government's own auditors in terms that could be lifted from the 1989 DOAH record. [GAO-23-105478](https://www.gao.gov/assets/gao-23-105478.pdf), published July 2023, found that as of June 2023 DOL had **not defined standards to measure states' UI IT performance**, had **not measured state IT performance at all**, and did not even know how many states had moved to cloud infrastructure. Its existing oversight — State Quality Service Plans tracking first-payment promptness and appeal timeliness, plus a pre-implementation planning checklist — is process-based and contains no load, concurrency, or capacity benchmark. GAO recommended that DOL "define UI IT modernization standards for states" and "measure states' UI IT performance against established standards." DOL only partially concurred with the first.

[DOL OIG Report 19-23-008-03-315](https://www.oig.dol.gov/public/reports/oa/2023/19-23-008-03-315.pdf) went further: the Employment and Training Administration "did not evaluate the capability of state UI IT systems to successfully administer benefits" and lacked the information to identify which states were most at risk of failure. The service center that can advise states "has no authority to enforce the recommendations." The modernization office created in August 2021 "will not assume any of ETA's responsibilities or oversight." On [April 27, 2026](https://oig.dol.gov/public/Press%20Releases/OIG-Press-Release-042726.htm) DOL OIG opened a further audit of how states spent post-pandemic modernization money.

Read that against [GAO/IMTEC-92-29](https://www.gao.gov/products/imtec-92-29), which in 1992 recommended a federal office with on-site inspection authority over state welfare systems and was refused by HHS and USDA. Thirty-one years later GAO made functionally the same recommendation to a different department and got a partial concurrence. The institutional answer has not changed.

## Florida did it again, and the parallel is nearly exact

Florida's CONNECT unemployment system was contracted to Deloitte in 2010–11 and went live October 15, 2013. Chief Inspector General Melinda Miguel's 95-page report, released March 4, 2021, found:

> "The contract mandated system capacity for a minimum of 200,000 concurrent external users... We could not find evidence where DEO enforced this contract requirement. Deloitte's stress testing documentation shows testing was for approximately 4,200 concurrent users (internal and external)."

— quoted in [WFSU](https://news.wfsu.org/state-news/2021-03-08/inspector-general-report-injected-into-lawsuit-over-floridas-unemployment-system) and the [Daytona Beach News-Journal](https://www.news-journalonline.com/story/news/2021/03/09/consulting-firm-deloitte-defends-firms-work-floridas-much-maligned-unemployment-system/6922197002/). The IG also found the independent verifications "were neither fully independent nor adequately rigorous," that 14 of 31 findings from the 2015 state audit remained open in 2021, and — per the [Tampa Bay Times](https://www.tampabay.com/news/florida-politics/2021/03/09/dont-blame-us-for-unemployment-failures-deloitte-tells-florida-senators/) — that the system carried 14 "fatal" defects the day before go-live under a contract that allowed none. After emergency addition of 72 servers during the pandemic, capacity reached roughly 100,000 users, half the contractual figure. Deloitte's defense before the Florida Senate was that 200,000 "concurrent" users never meant 200,000 simultaneous users, and that the 4,200 figure "was based on a complicated formula."

Set the two side by side:

| | FLORIDA, 1988–1995 | CONNECT, 2010–2021 |
|---|---|---|
| Quantified capacity requirement | 60–65% CPU utilization design rule in the RFP ([DOAH 88-2942BID](https://www.doah.state.fl.us/ROS/1988/88002942.PDF) ¶56) | 200,000 concurrent external users in the ITN/contract |
| Source of the requirement | State document, not federal rule | State document, not federal rule |
| Verified before award or go-live? | No; volume model conceded "no better than the assumptions" (89-0003BID App. ¶90) | No; tested to 4,200 |
| Independent check | None existed | IV&V existed and was "neither fully independent nor adequately rigorous" |
| Discovery | Vendor knew of the volume error March 1991; concealed | State never enforced the term; exposed by demand shock |
| Delivered performance | 95–100% CPU, response time degrading from a 3-second target | Site crashes, phone lines saturated, benefits unpaid |
| Federal standard that would have caught it | None | None |
| Vendor liability | Litigated to [631 So.2d 353](https://www.courtlistener.com/opinion/1895493/state-dhrs-v-eds-federal-corp/) | Class actions dismissed on sovereign-immunity grounds; state fine of $8M+; Deloitte awarded a $135M Florida Medicaid contract in August 2020 |

The 2020 collapse was not confined to Florida. Texas's Workforce Commission was running a mainframe from the early-to-mid 1990s and generated [3.1 million busy signals out of 3.5 million calls on April 7, 2020](https://www.texastribune.org/2020/05/19/texas-unemployment-benefits-coronavirus/). New Jersey's governor publicly solicited volunteer COBOL programmers against a [1,600 percent surge in claims](https://www.nj.com/coronavirus/2020/04/nj-unemployment-claims-are-processed-by-a-40-year-old-computer-system-as-demand-soars.html). Michigan's site crashed while its fraud algorithm flagged one-third of 1.7 million claims.

## The honest qualification

Capacity failure is no longer the dominant failure mode in state benefit systems, and the archive should say so. The 2013–2016 generation of failures — [Cover Oregon](https://www.doj.state.or.us/wp-content/uploads/2017/06/FINAL_Complaint_8_22_14.pdf) ($240M, settled with Oracle for a package valued at $100M), [Massachusetts](https://www.masslive.com/politics/2014/06/massachusetts_health_connector_3.html) (CGI fired, $35M clawback), [Maryland](https://www.washingtonpost.com/local/md-politics/noridian-to-pay-45m-to-state-us-government-for-flawed-md-exchange/2015/07/21/cb9b7028-2fd5-11e5-8353-1215475949f4_story.html) (Noridian repaid $45M), [Rhode Island's UHIP](http://www.transparency.ri.gov/uhip/documents/assessments/UHIP%2030-day%20assessment.pdf) ($135M projected to roughly $794M), [Indiana v. IBM](https://caseclips.courts.in.gov/2016/03/24/state-v-ibm/) ($1.3B contract, $78M net judgment for the state), [Michigan MiDAS](https://law.justia.com/cases/federal/appellate-courts/ca6/18-1296/18-1296-2019-01-03.html) (a 93 percent error rate on fraud determinations, $20M and $55M settlements), [Tennessee TEDS](https://healthlaw.org/wp-content/uploads/2024/09/AMC-Case-Explainer.pdf) (held unconstitutional in 2024), and [California CWS-CARES](https://lao.ca.gov/Publications/Report/5006) (over $2 billion, launch now slated for October 2026) — were overwhelmingly failures of requirements definition, testing rigor, governance, and program logic rather than of transaction-volume modeling.

That is a real change, and part of it is attributable to the post-1996 rules: modularity, IV&V, and the SNAP testing regime have made a certain class of monolithic-transfer disaster harder to execute. But the change is also partly an artifact of load. Systems that are never stressed do not fail from capacity. **The rule the record supports is narrower and less comforting: whenever an unanticipated demand shock has actually hit a state benefit system since 2000, the 1988 failure mode has reappeared.** California's own auditor warned in [1995](https://www.latimes.com/archives/la-xpm-1995-04-19-mn-56404-story.html) that SAWS "may never be able to accommodate the high volume of transactions and records" it would face — and that the state had "failed to set specific performance goals." Twenty-five years later that sentence still described the national unemployment estate.

## Conclusion

The specific hole identified in the 1986–1999 analysis has been closed in exactly one program — SNAP, in 2014 — and left open everywhere the money is largest. Where a quantified capacity number did exist, in Florida's own CONNECT contract, it lived in a state procurement document, went untested by a factor of nearly fifty, was not enforced by the buying agency, was missed by a paid independent verifier, and after failure was defended on the ground that the word "concurrent" had never meant what it appeared to mean. That is not a gap one bad RFP away from producing a disaster. It is the same gap, thirty-two years later, having already produced one.

---

### Sources

[45 CFR Part 95 Subpart F, current](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-95/subpart-F) (§95.626 IV&V added at 75 FR 66340, Oct. 28, 2010; §95.613 amended 81 FR 3020, Jan. 20, 2016 and 89 FR 80071, Oct. 2, 2024) · [42 CFR 433.112](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-433/subpart-C) (76 FR 21975, Apr. 19, 2011) · [45 CFR 1355.52, CCWIS](https://www.ecfr.gov/current/title-45/subtitle-B/chapter-XIII/subchapter-G/part-1355/section-1355.52) (81 FR 35479, June 2, 2016) · [7 CFR 277.18, current](https://www.ecfr.gov/current/title-7/subtitle-B/chapter-II/subchapter-C/part-277/section-277.18) (testing and pilot requirements added at 79 FR 12, Jan. 2, 2014) · [7 CFR 277.18 as of Jan. 1, 1999](https://www.govinfo.gov/content/pkg/CFR-1999-title7-vol4/pdf/CFR-1999-title7-vol4-sec277-18.pdf) (for contrast) · [GAO-23-105478](https://www.gao.gov/assets/gao-23-105478.pdf) · [DOL OIG 19-23-008-03-315](https://www.oig.dol.gov/public/reports/oa/2023/19-23-008-03-315.pdf) · [DOL OIG press release, Apr. 27, 2026](https://oig.dol.gov/public/Press%20Releases/OIG-Press-Release-042726.htm) · [GAO/IMTEC-92-29](https://www.gao.gov/products/imtec-92-29) · [Florida Auditor General Report 2019-183](https://flauditor.gov/pages/pdf_files/2019-183.pdf) · [Florida Politics on the CIG findings](https://floridapolitics.com/archives/409408-connect-investigation-first-findings-deloitte-ran-insufficient-stress-testing/) · [WFSU](https://news.wfsu.org/state-news/2021-03-08/inspector-general-report-injected-into-lawsuit-over-floridas-unemployment-system) · [Daytona Beach News-Journal](https://www.news-journalonline.com/story/news/2021/03/09/consulting-firm-deloitte-defends-firms-work-floridas-much-maligned-unemployment-system/6922197002/) · [Tampa Bay Times, Mar. 9, 2021](https://www.tampabay.com/news/florida-politics/2021/03/09/dont-blame-us-for-unemployment-failures-deloitte-tells-florida-senators/) · [Miami Herald](https://www.miamiherald.com/news/politics-government/state-politics/article249702448.html)

**Note on sourcing:** the CIG report's key findings are quoted here from four independent contemporaneous accounts that reproduce the same passage verbatim. The 95-page report itself was released as a draft by the Executive Office of the Governor on March 4, 2021; a direct PDF was not located and would be worth a public-records request to the Office of the Chief Inspector General, The Capitol Suite 1902, Tallahassee — a natural companion to the FLORIDA requests already out the door.
