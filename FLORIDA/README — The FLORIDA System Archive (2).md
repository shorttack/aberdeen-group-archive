# The FLORIDA System

### A Primary-Source Reconstruction of America's Least-Studied Major Government IT Failure

*Kastner Research Archive · Compiled July 2026*

---

## What this is

Between 1988 and 1997, the State of Florida procured, built, and then spent a decade repairing an integrated public-assistance eligibility system called FLORIDA — Florida On-Line Recipient Integrated Data Access. It cost at least **$245.3 million** against a **$107.7 million** winning bid, an overrun of roughly **128 percent**. It put the state dead last among 54 jurisdictions in AFDC payment accuracy three years running. It kept issuing food stamps to dead people for as long as seven months after their deaths, a defect flagged internally in 1989, 1991, and 1993 before anyone acted. And in 2026 it is **still running**, on the same COBOL and IMS foundation, with a state migration target of fiscal year 2028.

This directory is the working archive from a research effort that reconstructed that history from primary sources: two administrative-law recommended orders totaling roughly 200,000 characters of sworn findings, thirty-five years of Florida Auditor General reports, federal GAO and USDA OIG audits, legislative feasibility studies, procurement documents, and contemporaneous newspaper coverage.

It is also, deliberately, an invitation. FLORIDA is the largest well-documented state benefits-system failure of the 20th century that **no scholar has ever written about**. That absence is the reason this directory exists in public.

The archive's central finding is narrower and harder than "a big project failed." It is that a $100 million procurement turned on a single unverifiable assumption about how much work a welfare agency generates, that the assumption was supplied by the party that benefited from it, and that the process contained no mechanism capable of testing it — while actively disqualifying the one check that presented itself.

---

## Why you should care about this case

The abstract of the main analytical report states the historical claim, and it is worth reproducing here:

FLORIDA is the case in which every institution that was supposed to prevent a public-sector IT disaster instead helped cause one. Federal agencies, enforcing procurement-competition doctrine, ordered the state to weaken the one architectural requirement that would have disqualified the eventual winner. A competitive evaluation panel, in possession of written testimony that the winning bidder's transfer base had never been implemented and used the wrong architecture, scored it higher anyway. A losing bidder protested twice, lost twice, and was proved substantially correct within four years. A special master later found that the vendor had discovered its own capacity-assumption error in March 1991 and did not tell the state, which then paid to enlarge the machine without knowing why it was too small. And the state's remedy, when the system finally could not keep up, was to make caseworkers work nights and Saturdays.

A note on how that claim evolved. An earlier draft of this archive framed the case as a failure of computer modeling — a tribunal trusting a simulation over measured experience. Further research and the testifying witness's own correction established that the modeling tool was sound and widely used, that the transferred Ohio code was real and its path lengths measurable, and that the failure lay in a different place entirely: the workload assumptions fed into the tool, which no amount of code inspection could validate and which only a running welfare agency could supply. The archive now argues the harder and better-evidenced case.

Every element of the 2013 Healthcare.gov post-mortem, the 2018 automated-inequality literature, and the current federal debate over state benefit-system modernization is present in this 1988 record — with sworn testimony, paragraph-numbered findings, and a documented outcome spanning thirty-five years. It is the control experiment nobody ran, because nobody read the file.

---

## What we established

### 1. The architecture was specified as distributed and delivered as centralized — and the federal government is why

HRS's Advance Planning Document **required** distributed architecture. USDA's Food and Nutrition Service ordered it removed:

> "The FNS letter also required that, in the interest of free and open competition, the APD requirement of distributed architecture... should be replaced in the RFP by a statement of preference for a distributed system." — ¶26, [DOAH Case 88-2942BID](https://www.doah.state.fl.us/ROS/1988/88002942.PDF)

The same federal agencies barred reuse of the state's installed Unisys A-15 and imposed a 60/40 technical-to-cost scoring split "even over Respondent's resistance" (¶62). Competition policy dissolved the requirement that would have excluded a centralized transfer base. A centralized transfer base then won.

### 2. The evaluators knew, in writing, and scored the winner higher anyway

> "The largest portion of the EDS system is derived from the Ohio CRIS-E System, which has never been implemented, does not serve any clients or cases, and features centralized architecture rather than the distributed architecture sought by HRS." — ¶134, [DOAH Case 89-0003BID](https://www.doah.state.fl.us/ROS/1989/89000003.PDF)

The losing bidder's base — New York State WMS plus New York City CSE — was implemented, federally certified, and distributed (¶135). EDS took 51 raw points to Unisys's 43 on that very question. One evaluator praised CRIS-E's "distributed processing procedure" while it was centralized (¶137); another explicitly noted it was centralized and unimplemented and still scored it higher (¶138); a third "stated incorrectly that CRIS-E had been implemented" and the hearing officer found "his scores were simply incorrect" (¶136). The award survived both protests on a 4.4-point margin out of 5,062.

### 3. The capacity case was decided on assumptions nobody in the room could test

This is the archive's core technical finding and it was substantially revised in July 2026.

The modeling behind the winning bid was **IBM's**, performed for EDS. The hearing officer says so three times: "the complex IBM modeling programs," "the informed use of modeling by IBM, in connection with capacity planning for the EDS system," and, at ¶146, "sophisticated computer simulation models." The tool was almost certainly IBM's SNAP/SHOT — Systems Network Analysis Program / Simulated Host Overview Technique, [documented in the *IBM Systems Journal* in 1979](http://bitsavers.informatik.uni-stuttgart.de/pdf/ibm/IBM_Systems_Journal/183/ibmsj1803C.pdf) — identified by the witness who read its output at the hearing.

**The tool was not the problem.** SNAP/SHOT ran across IBM's large-account base for over a decade; a systematic error of the magnitude later discovered would be in the public record and is not. Nor was the transferred Ohio code vapor: CRIS-E had been written even though it had never been switched on, which means instruction counts and disk I/O counts per transaction were measurable.

The problem was the class of input that no code inspection can produce. How often does a caseworker run a full multi-program eligibility determination rather than a status inquiry? How many transactions arrive at the peak of a Monday morning? Those parameters — `MSGINMIX` and `MSGRATE` in the model's terms — are not facts about software. They are facts about an operating welfare agency, and they set the load.

The hearing officer identified the problem precisely and then set it aside:

> "It is true that the data generated by the IBM modeling programs are no better than the assumptions that went into the models. It is also true that the HRS evaluators' understanding of the models, assumptions, and even the resulting data was incomplete." — Appendix, ruling on proposed finding 90, [DOAH 89-0003BID](https://www.doah.state.fl.us/ROS/1989/89000003.PDF)

He then credited the scores on grounds that were commercial rather than technical — fixed price, performance penalties, and IBM's institutional standing. He never found the model right. He found reliance on IBM reasonable.

And the losing bidder's disparaged method was the missing input. Extrapolation from existing caseloads **is** transaction mix and arrival rate, drawn in Unisys's case from New York systems the tribunal separately found "have been implemented and certified" (¶135). Paragraph 146 ranked "extrapolations from existing case loads" beneath simulation. It named the correct input, correctly identified the only available source for it, and called that source the inferior method.

The timing corroborates. Webster found EDS "discovered as early as March 1991" that capacity was half what was expected. A path-length error surfaces in testing; a configuration error in design review. A workload-mix error cannot surface until real caseworkers generate real work — and production began in roughly the first half of 1991. Among candidate errors, only a mix error has a detection date that could fall in March 1991.

**The structural finding:** EDS chose the mix, the mix set the machine, the machine set the price and the response-time promise, and IBM's tool faithfully printed what those assumptions implied across some 535 pages of variations. No independent party in that chain was capable of testing the first link. The evaluators could not, and the hearing officer wrote that down. The federal agencies imposed procedural requirements but reviewed no workload assumptions. IBM could not, because a modeler models what the client supplies. The tribunal declined to. The one check that existed was ruled out of order as methodology.

The error was not a risk the procurement was running. It was a certainty the procurement could not see.

### 4. The single-host topology is the causal spine of everything downstream

One IBM 3090-class mainframe, MVS, IMS DB and IMS/TM, COBOL, serving roughly 12,000 non-intelligent terminals across 11 service districts and 67 counties. No district-level processors at any point in thirty-five years. Response times ran in **minutes** in June 1992 and were only brought to four seconds by June 1994 by moving staff onto nights and Saturdays. CPU ran at 95–100 percent through the business day in fall 1994, against a commercial norm near 65 percent. Capital remediation across the entire decade totaled about $10.5 million, because in a centralized design a bigger box is the only thing there is to buy.

The negative evidence is decisive: when Florida piloted welfare reform in Escambia County, it could not change eligibility rules for one county, so it built a PC LAN alongside the mainframe that "is not directly linked to the FLORIDA system." Caseworkers ran three unconnected systems at once.

### 5. FLORIDA was never a DB2 design, and the misattribution trap is live

The platform was IMS — hierarchical, DL/I — from 1992 to the present. DB2 appears in the record only as a *future* migration target in Gartner's 2012 alternatives analysis. Researchers should be warned that the same Gartner-era Florida documents describe **FSFN** (Florida Safe Families Network, child welfare) as a DB2 system. Conflating the two is easy and has probably already happened somewhere.

### 6. The 21st-century record is asymmetric in a revealing way

Auditors never stopped writing about FLORIDA. USDA OIG documented a claims backlog stretching past thirteen years and attributed it to "lack of integrating a claims management system into the FLORIDA system when it was developed." Florida's Auditor General was still finding 650,131 overdue federal data exchanges in 2019 and still finding mass-change instructions "not updated since the mid-1990s."

Scholars, meanwhile, wrote nothing. FLORIDA is absent from Eubanks's *Automating Inequality*, from Citron's technological-due-process literature, from Montealegre and Keil's canonical IS escalation work, and from the standard IS-failure survey literature. A 2024 Florida TaxWatch report calling for procurement reform **does not mention FLORIDA once**. The state's own reform advocates have forgotten their largest case.

### 7. The federal policy arc bends around this case and then forgets it

The archive traces federal welfare-systems policy from the 1986 enhanced-funding regime through the 1996 devolution that dissolved the oversight apparatus, and forward to the present. The short version: the conditions that produced FLORIDA were not fixed, they were decentralized. The archive's standing question — whether another FLORIDA is one bad RFP away — is answered in the affirmative, with citations.

---

## Contents

### Analytical papers

| File | Subject |
|---|---|
| `FLORIDA-system-EDS-IBM-HRS-analysis.md` | Main report. Full narrative 1986–1997, with the remediation table and cost reconciliation as appendices A and B. |
| `FLORIDA-capacity-modeling-tools.md` | **The technical core.** IBM's 1988 capacity-planning toolkit, what SNAP/SHOT was told and what it printed, the assumptions-versus-tool finding, and what "distribution of certain processing functions" meant. |
| `FLORIDA-annals-manuscript.md` | Peer-review manuscript draft for *IEEE Annals of the History of Computing*. **Shelved as of July 28, 2026**, pending the outcome of a separate submission. Complete and internally consistent, but roughly 700 words over the journal's 8,000-word ceiling; the trim is unmade and the two sections most likely to give it up — the 21st-century afterlife and the academic-void discussion — exist in full elsewhere in this archive. |
| `FLORIDA-as-built-topology.md` | Physical, computing, and network topology; specified-versus-delivered comparison; the FNS architecture demotion. |
| `FLORIDA-operating-conditions.md` | What running the system was actually like, 1988–2001. Response times, client waiting, batch windows, and §4.1 on network-restart cost. |
| `FLORIDA-throughput-remediation-table.md` | Every documented performance-improvement measure of the 1990s, with costs where recoverable. |
| `FLORIDA-cost-reconciliation.md` | Original bid and performance promises against incremental contracts, to a bottom-line overrun. |
| `kastner-unisys-protest-analysis.md` | What Unisys protested, what was testified, and what fifteen subsequent years proved. |
| `FLORIDA-post2000-analysis.md` | 21st-century government and academic treatment, and the academic void. |
| `federal-policy-arc-1986-1999.md` | Federal welfare-systems law, funding, and oversight across the FLORIDA years. |
| `federal-arc-1996-to-present.md` | The post-devolution regime through 2026, and the recurrence question. |
| `FLORIDA-system-addendum-sources.md` | The Webster report and the 1988 RFP performance requirements. |
| `FLORIDA-lessons-and-prescience.md` | **Synthesis study.** Twelve lessons learned, and five scored prescience tables covering the 1988–89 procurement actors, the dissenters, federal policy architects 1986–2026, Kastner's own contemporaneous calls, and the archive's own forward claims to 2028. Self-scored; a subsequent independent pass is expected. |

### Primary documents

| File | Description |
|---|---|
| `unisys_88-2942BID_recommended_order.pdf` / `.txt` | DOAH recommended order, specifications protest, 1988. The FNS architecture-demotion finding lives here. |
| `unisys_89-0003BID_recommended_order.pdf` / `.txt` | DOAH recommended order, award protest, March 14, 1989. The evaluation-scoring findings live here. |
| `OTA-881203-electronic-delivery-federal-assistance-1988.pdf` / `.txt` | U.S. Office of Technology Assessment, *Electronic Delivery of Public Assistance Benefits: Technology Options and Policy Issues*, **OTA-BP-CIT-47, April 1988**. Contemporaneous federal thinking on benefits automation, published the month before RFP 88-74-BC. **Note on the filename:** "881203" is the Princeton OTA archive's filename for chapter 3, not a report number, and the report is April rather than December 1988; earlier working notes in this archive had both wrong. |
| `FL-general-records-schedule-GS1-SL-2023.pdf` / `.txt` | Florida General Records Schedule GS1-SL. Establishes retention periods, and therefore what may still legally exist; underlies the records-request drafts. |
| `SOURCES.md` | Every external source cited anywhere in the archive, with link-check status. |
| `CHRONOLOGY.md` | Master timeline, 1986–2028, with the source for each entry. |

### Records requests

| File | Description |
|---|---|
| `FLORIDA-records-requests-drafts.md` | Six requests: Auditor General 12581 and 13043, HHS/ACF and USDA/FNA Advance Planning Document files, the DCF procurement file, ITN 03F12GC1, and the 1993 grand jury presentment. **Five were sent July 28, 2026**; the Leon County Clerk request (§ 2) followed on August 20, 2026 (reference P022996-082026), so all six are now out. **First response received August 19, 2026:** DCF answered the § 5 procurement-file request (reference P257883-072926) with a finding of no responsive records — a null across the RFP, the Evaluation Manual, the EDS contract, the Webster report, and the settlement. Consistent with a five-fiscal-year bid-records retention that expired around 1994. A follow-up seeking the Rule 1B-24.003(9)(d) disposition documentation and any State Archives accession was **sent August 20, 2026** (§ 5b); the state-agency branch for RFP 88-74-BC is closed pending it, and the federal APD file is now the most likely surviving custodian. Every recipient was verified against the agency's own current page on that date — four of six were wrong, and the corrections are recorded in each section. |
| `DCF-ITN-03F12GC1-records-request.txt` | Verbatim copy of the § 6 request as sent, July 28, 2026. |
| `leon-clerk-grand-jury-records-request.txt` | Verbatim copy of the § 2 request as submitted through the Leon County Clerk's portal, August 20, 2026, reference P022996-082026. |
| `carlton-fields-records-request.md` | Request to protest counsel for the retained litigation file. |
| `AG-1998-SYSTEMS-REVIEW-FINDINGS.md` | What the Auditor General's August 11, 2026 delivery changes. Analysis of Report No. 13287, the 1997–98 systems review of the FLORIDA System — the first document in the archive describing the as-built machine from the inside. Records three corrections the archive must make, the documented 1998 configuration, and two previously unknown report numbers. |
| `AG-12581-13043-FINDINGS.md` | What Reports 12581 and 13043 change. Report 12581 is the primary source for the 95–100 percent CPU utilization claim the archive has been carrying on press coverage alone; it corrects the attribution, dates the response-time series, and shows the December 1994 three-second figure was achieved partly by rationing users. Report 13043 itemizes the $42.8 million settlement and fixes the litigation chronology. Also identifies Reports 11178, 11619, and 12061 — the pre-1995 audits the archive had been seeking by description. § 4a records Kastner's practitioner reading of the two-machine 1995 configuration, with the finding that every published utilization figure describes an application host that did not carry the 16,000-device network. § 4b answers why the bid was undersized: a fixed price that bundled the hardware, with no performance standard to size it against. |
| `sources/auditor-general/` | OCR transcriptions of Reports 12581, 12583, 12656, 12886, 13043, and 13287, supplied by the Auditor General's office August 11, 2026. Not available online. **The source PDFs for 12583, 12656, 12886, and 13287 must still be committed alongside these; 12581 and 13043 are held as PDFs in `PDFs/auditor-general/`.** |
| `COLLECTION-PLAN.md` | Acquisition plan for everything the open web cannot reach: non-digitized Tallahassee holdings, credentialed databases, and oral history. Includes a detailed two-day Tallahassee itinerary with verified addresses, hours, and pre-trip calls. Leads with a retention-rule analysis (Fla. R. Gen. Prac. & Jud. Admin. 2.430) concluding that the 1992 and 1995 circuit case files were probably destroyed while their progress dockets survive permanently — which reweights the trip away from the courthouse and toward the State Archives. |

### Research inputs

Files prefixed `research-` are the raw, heavily cited evidence-gathering passes underlying the analytical papers. They are retained because they contain material the finished papers did not use, and because they document what was searched and found empty. `research-florida-topology.md` in particular records dozens of dead ends that a future researcher need not repeat.

---

## The evidentiary standard used here

Every factual claim in the analytical papers carries an inline link to its source. Findings from the administrative record are cited to paragraph number. Where a conclusion is inferred rather than sourced, it is labeled as inference in the text — this is not a stylistic preference but a working requirement, because the most tempting gaps in this case are exactly the ones where generic mainframe-era assumptions would slot in unnoticed.

Every paper ends with an explicit statement of what could not be verified and where the answer would be held. Those sections are the most useful part of the archive for anyone continuing the work.

### A worked example of why the standard exists

In July 2026 the archive was audited end to end against Finding 3, and the same error turned up in five papers. Every instance was one substitution: **the model** standing in for **the assumptions**.

It entered from the press coverage, which is the source of the phrase and had no reason to be precise. The *St. Petersburg Times* reported that EDS "had made a mistake in modeling the FLORIDA computer," and the archive absorbed the compression without noticing it had changed the claim.

The compression mattered for three reasons, none of them cosmetic. It made the case **less damning**, because a tool that fails is a technical accident while an assumption nobody could check is a structural defect. It made the case **less generalizable**, since nobody runs SNAP/SHOT now but every procurement still accepts a vendor's estimate of its own future workload. And it made the case **refutable**, because SNAP/SHOT's public record is clean and a knowledgeable reviewer could have dismantled the tool-failure version in an afternoon.

The correction was not a reinterpretation. William Webster had the distinction in 1995 and wrote it down: good faith required EDS to disclose "the erroneous modeling assumption" — singular, locating the defect in an input rather than in the tool. The archive had quoted that sentence for months while paraphrasing around it.

Two general lessons are recorded here because they will recur for anyone working from this material. **Press paraphrase migrates into analysis and hardens there**, especially when the paraphrase is shorter and reads better than the accurate version. And **a claim that flatters the argument gets less scrutiny than one that complicates it** — "the model was wrong" was a more useful sentence than "the assumptions were unverifiable," which is exactly why it survived unexamined.

### A second worked example — log entries about work done are claims, not facts

In September 2026 the archive discovered that a log entry from July 28, 2026 recording a completed URL repair (casetext.com → CourtListener, sixteen occurrences across six papers) had never actually been applied to the published papers. The CourtListener URL was correctly added to `SOURCES.md`; the papers themselves were never edited. For six weeks the archive carried a blocker note describing "two divergent copies of the corpus, one repaired" — when in fact no repaired copy existed anywhere.

The repair was straightforward once discovered, but the shape of the error is worth naming. **A log entry recording completed work is a claim, not a fact.** The claim should be verifiable against the destination artifact by grep, checksum, or read — not accepted on the basis that a prior session said it was done. The archive should carry, and enforce, a periodic reconciliation check: given a log entry saying "X was removed from Y," verify that X is in fact absent from Y. That check would have caught the July 28 error in July 28.

The general form of this rule is: **the archive's own operational record is subject to the same standards as its evidentiary record.** Claims of the form "the archive was updated to reflect X" have to be provable in the same way that claims of the form "Auditor General Report 12061 documents Y" have to be provable. Both are claims. Both fail the same way when they are not.

---

## Future work: what is still out there

This is the section for you.

### Documents known to exist and confirmed not digitized

1. **Florida Auditor General Report 12581** — "Department of Health and Rehabilitative Services – Florida System," audit period 10/17/1994–02/28/1995, issued 09/12/1995. Confirmed present in the Auditor General's index; the link routes only to a copy-request page. This is almost certainly the report behind the September 1995 press coverage and is likely the single richest surviving source on the system's 1992–1995 hardware, capacity, and performance state. Request from `flaudgen@aud.state.fl.us` or (850) 412-2722.
2. **Florida Auditor General Report 13043** — "HRS Settlement of FLORIDA Contract with EDS," audit period 07/01/1995–12/31/1996. Same status, same request path. Should carry the definitive settlement accounting.
3. **The SNAP/SHOT sensitivity sweep** — approximately 535 pages of greenbar produced by IBM's model, delivered to the Unisys expert witness by courier on the Saturday before his Monday testimony and entered in the DOAH 89-0003BID record. **This is now the highest-value document outstanding in the project.** It would show which parameters were varied, what transaction mixes were explored, and whether any case in the disclosed range predicted the failure that occurred. Check the DOAH exhibit file and the Carlton Fields litigation file.
4. **EDS Proposal page VII-F-10** — an exhibit in the DOAH 89-0003BID record. The recommended order states that "a material difference in line speed" was disclosed here, without direction or magnitude. It bears directly on whether the winning bidder's system demonstration was representative of production.
5. **The 1993 grand jury presentment** and the underlying investigative file.
6. **The Webster special-master record** — the arbitration in which EDS's undisclosed March 1991 capacity-assumption error was established. Exhibits should be with the Leon County Clerk. Related: the § 2 request in `FLORIDA-records-requests-drafts.md`, seeking the 1993 grand jury presentment from the same custodian, was **sent August 20, 2026** through the Clerk's GovQA portal, reference P022996-082026. All six requests in that file are now out. Note that the Clerk's published presentment index begins at No. 137, dated November 15, 1995, so the threshold question is whether pre-1995 presentments remain in that office at all or were transferred to the State Archives.

### Archival hygiene

7. **Re-obtain ITN 03F12GC1 and commit it to this repository.** The 2012 replacement Invitation to Negotiate is the archive's most detailed description of the as-built system — 88 OSAM and 206 VSAM databases, 1.17 TB of production data, twenty-two satellite systems — and it went off the web during the research. The Vendor Bid System purged it and the Internet Archive never captured it. A Chapter 119 request was **sent to the DCF Custodian of Public Records on July 28, 2026**, alongside four others that day (Auditor General, HHS, USDA/FNA, and the DCF procurement file); the text and the verified recipient are recorded in `FLORIDA-records-requests-drafts.md` §6, and a verbatim copy of the message as sent is at `DCF-ITN-03F12GC1-records-request.txt`. Awaiting response.
8. **Mirror every load-bearing state-hosted PDF into the repository.** The ITN episode established the general rule: a link to a government document is not preservation. Roughly a dozen sources in `SOURCES.md` are single-copy state PDFs with no archive capture, and each is one retention-policy decision away from the same fate.

### Open technical questions

- **The network layer is still undocumented in public sources.** No published source names SNA, VTAM, NCP, a 3745 or 3725 communications controller, a 3174 or 3274 cluster controller, or a single leased-line speed in connection with FLORIDA. The witness attests that local terminal memory resided in the SNA branch controllers, which resolves what the hearing officer meant by "the distribution of certain processing functions" but does not give models, counts, or configurations. The "Design Telecommunications Network" contract deliverable is the place to look.
- **The transaction mix assumed in the winning proposal.** The single number this case turned on. EDS capacity volume; Webster arbitration exhibits.
- **Whether SNAP/SHOT's host model accounted for IMS lock contention.** If it did not, every page of the sweep understated the penalty of a heavy mix. IBM internal documentation and Computer Measurement Group proceedings of the period.
- **District-by-district rollout dates.** RFP Exhibit G-3 held the conversion schedule. Needed to tighten the March 1991 argument.
- **Where the mainframe physically sat between 1992 and 2008.** The predecessor A-15 was in HRS's Jacksonville Data Center. The system today is at the Northwood Shared Resource Center in Tallahassee. Three decades in between are blank.
- **The installed host model at each generation.** EDS proposed a 3090/300E and demonstrated a 3090/400E. What was actually installed, and what the mid-1990s upgrades bought, is not in any digitized record.
- **Whether any district-level equipment was ever installed.** Equipment schedules and acceptance records would settle it.
- **Disaster recovery.** No public source across thirty-five years of audits describes a standby site for a system that determines eligibility for millions of people. The absence may itself be the finding.

### Open scholarly questions

- **Why is this case absent from the literature?** The most likely answer is prosaic — the administrative record was never digitized in a searchable form, the press coverage is behind archive paywalls, and the system's name is a homonym for the state. But the absence has consequences, and mapping how a case this large fell out of the citation network is itself a paper.
- **The CRIS-E lineage.** Ohio's system is the transfer base, is still in use, and has its own history. A comparative study of the two implementations of the same codebase — one at home, one transferred to a state four times its caseload — is sitting there unwritten.
- **The competition-versus-architecture tension in federal procurement doctrine.** FNS's demotion of the distributed-architecture requirement was a defensible application of open-competition policy that produced a technically inferior outcome. This is a clean, documented instance of a structural conflict that recurs constantly and is rarely evidenced this well.
- **The evaluation-panel pathology.** Sixteen evaluators, paragraph-level findings on individual scores, and a hearing officer willing to write "his scores were simply incorrect." There are very few public-sector procurement evaluations this thoroughly exposed. It is a natural teaching case.

---

## A note on the compiler's role

Peter Kastner was a working technology-industry analyst throughout the period this archive covers, at Aberdeen Group and before that at Arthur D. Little, Prime, Stratus, and Digital. Where his own contemporaneous observations and testimony enter the record, they are attributed to him by name and, when they are period measurements on comparable equipment rather than measurements of FLORIDA itself, labeled as such. The §4.1 analysis of terminal-network restart cost in the operating-conditions paper is the clearest instance: the underlying observation is his, made at Cullinet Software in Westwood, Massachusetts in early 1988, and its application to FLORIDA is explicitly an inference.

He is also the witness whose testimony the 1989 tribunal discounted, which makes him an interested party in the account this archive gives of that ruling. The archive states this rather than leaving a reader to discover it. Three grades of evidence are distinguished throughout and should be read differently: **documentary** claims carry a source link; **attestations** are things the witness states from memory at thirty-seven years, including the identification of SNAP/SHOT, the approximate length of the sweep, and the location of terminal memory in the branch controllers; and **reconstructions** are inferences he forms now about what he most likely did then, of which the transaction-mix explanation is the principal example. He does not recall why he chose the page he chose, and the archive says so.

That grading is also why the archive corrected itself in July 2026. The original modeling argument was too broad, the witness said so, and the revision is visible in the papers rather than quietly absorbed.

---

## Using this archive

Cite the analytical papers by title and this repository. Cite the DOAH recommended orders directly to the [Florida Division of Administrative Hearings](https://www.doah.state.fl.us/) — they are public documents and both are reproduced here with their source URLs. Corrections are welcome and will be made visibly rather than silently; the archive's working assumption is that a flagged error is worth more than an unflagged smooth surface.

If you obtain any of the non-digitized documents listed above, the most useful thing you can do is put them somewhere permanent and public. Nobody has read Report 12581 in thirty years.
