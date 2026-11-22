# DCS set P257878-072926: intake review and analysis

Run: `run_20261122t020853Z_dcs` (overnight, 2026-11-21 22:00 EST, runner exit 0)
Source: `/private/tmp/FLORIDA/DCS P257878-072926` (22 PDFs, 207 pages; source folder unchanged)
Prepared: 2026-11-22. Status: for your acceptance. Nothing moved out of /tmp; no archive files edited.

Labels: **[doc]** = stated in the document (file and page given). **[inference]** = my reading, not stated in the record.

## 1. What the set is

DCF's procurement file for **ITN 03F12GC1, ACCESS Florida System Replacement** (June 2012 to March 2013): the ITN itself (147 pp.), the Response to Inquiries (23 pp.), Addenda 1-15, the reply-opening notice, the shortlist, and a 2019 printout of the Vendor Bid System advertisement history. [doc]

Timeline [doc]:
- 2012-06-22 ITN v1.0 issued (F4863, p. 1)
- 2012-07-20 Response to Inquiries (F26854); Addendum 2 lists the supporting documents (F31900, p. 2)
- 2012-08-20 reply opening (F14148, F31660)
- 2012-09-18 shortlist: Accenture, Deloitte, Xerox (F13332)
- 2013-03-08 notice of intent to award to **Deloitte Consulting LLP** (VBS printout, p. 1)

## 2. Intake checks (the "needs a human look" list)

| Item | Result |
|---|---|
| Text layer | All 207 pages kept their born-digital text; differences are whitespace only. No OCR was needed. |
| 9 files with unembedded fonts | Extracted text checked: no replacement characters or garbled glyphs; text reads correctly in all nine. **Pass.** |
| F4863 p. 1 (image) | Cover page: DCF logo only. All words on the page are in the text layer. **No loss.** |
| F4863 p. 89 (image) | "Exhibit A: Project Organization" org chart (ITN p. 85). **The box labels are an image and are not in the text layer.** Transcription below (§ 2a). |
| VBS printout p. 1 (image) | Page is a browser printout; its text (including "intends to award a contract to Deloitte Consulting LLP") is in the text layer. **No loss.** |
| Apparent duplicates | Not duplicates. The two Addendum 7 files (F11370, F1467; created 15:42 and 16:48 on 2012-11-13) differ in one heading ("Team to Develop Recommendation for" vs. "Team to Discuss Moving Forward"). The two Addendum 8 files (F30667 11:33Z, F12906 12:19Z on 2012-12-17) differ in the year of three dates: the earlier copy says "February 6, 2012", the later corrects it to 2013. Keep both of each as issued versions. |
| 205 vs. 207 pages | The run counted 207 pages, which matches the per-file totals. The 205 figure from yesterday's test can't be reconciled from the run record; I'm treating 207 as correct. |

### 2a. Transcription of F4863 p. 89 org chart (from the page image)

DCF Secretary → Executive Steering Committee (DOH Representative; FHKC Representative; DCF 3 Representatives; AHCA 3 Representatives) → DCF Executive Sponsor (with IV&V Team (Provider)) → DCF Project Sponsor (with DCF Contract Manager) → Project Leadership Team: Project Director (Provider); Project Management Office (Provider); DDI Project Manager (Provider), Functional Lead, Technical Lead → DDI Project Team Organization (Provider), Business Process Owners, Database Administrator, Architect, Application Development Lead. Project Support: Legal Counsel, Human Resources, Financial Management.

## 3. What it tells us about FLORIDA

1. **FLORIDA was still the core of the system twenty years on.** "Implemented in 1992, the Florida Online Recipient Integrated Data Access system (FLORIDA) is the legacy mainframe that provides core functionality for the ACCESS Florida System." [doc: F4863, ITN p. 46 and p. 2] The web portal, workflow, imaging and call-center tools were layered around it, not in place of it.

2. **DCF's own diagnosis was architectural, not capacity.** The stated problem is "the underlying architecture of the FLORIDA mainframe which is inherently rigid and difficult to maintain," with updates "time-consuming and expensive" and "an ever-increasing risk of infrastructure failure due to the age of the mainframe." [doc: F4863, ITN pp. 46-47] Nowhere in the set does DCF say the mainframe lacked throughput. [inference] By 2012 the complaint's 1991-92 capacity crisis had turned into a change-cost problem: the machine could carry the load, but the design could not be changed cheaply.

3. **The 2012 workload, in DCF's figures (Q1 2012 averages)** [doc: F4863, ITN p. 2]:
   - 4,673,852 unduplicated individuals; 2,532,681 unduplicated households
   - 1,041,109 applications and reviews per month
   - 2,380,145 call-center calls per month
   - **Ratios (Pete's observation, 2026-11-22):** 2,380,145 calls ÷ 2,532,681 unduplicated households = **0.94 calls per household per month**, almost exactly one. Other bases: 0.51 per unduplicated individual, 0.58 per duplicated (program) household, 2.29 per application or review. That is a very high call level. [inference] It fits DCF's own complaint that "limited self-service capabilities drive operational costs higher" (ITN p. 47): when the eligibility system can't tell the client where a case stands, the client phones. The ITN doesn't say whether "calls" means agent-handled calls or includes automated (IVR) calls, which changes the reading a lot; this is in the new records request.
   - [inference] Against the 1988 RFP design point in the complaint (318,655 cases) this is roughly an eightfold rise in households, but the units differ (RFP "cases" vs. DCF "households"), so I would not print a ratio without the RFP's case definition. This fits the capacity-planning theme: the 1988 workload assumption was outgrown many times over, and the 1992 design still survived.

4. **Technology inventory** [doc]:
   - FLORIDA data: IMS database, "88 osam databases and 206 vsam databases"; 740 GB active + 430 GB archive = 1.17 TB production (F4863, ITN pp. 71-72).
   - Surrounding systems on Oracle and SQL Server (AMS, web application, My ACCESS Account, FLODS operational data store).
   - Mainframe estate: "12 LPARS", "on average 1 to 2 abends per day" (F26854, p. 12, Q83, answer to Xerox).
   - Data tooling: "custom COBOL and SyncSort for extracts and SQL for loads"; no comprehensive data-quality analysis had been done (F26854, Q45-46, answers to Unisys).
   - Hosting: new system to run from the Northwood Shared Resource Center, Tallahassee (F4863, ITN p. 1).

5. **Response-time standard then and now.** The O&M service level for the legacy system is "Average Response Time", measured monthly: under 3 seconds to avoid a penalty, under 5 seconds before failure (F4863, Attachment II, Exhibit A: Performance Measures, ITN p. 115). The "10%" in that row is the penalty percentage, not a percentile. **Pete's point (2026-11-22): the measure has no percentile attached.** Nothing in the ITN, addenda or Q&A says which transactions count (all, or online inquiry only), whether it is a plain mean or a 90th/95th-percentile figure, or where it is measured (host or user's screen). [inference] A plain monthly mean lets a long tail of slow transactions hide behind fast ones. The 1988 RFP § 7.32, as quoted in the complaint (p. 76), was stricter in form: it set seconds against a share of transactions, e.g. "six (6) seconds for 95 percent of searches" and "one (1) second for 95 percent of the time." (Qwen and Tesseract agree on these two p. 76 lines; your page-image check of them is still open.) So the 1988 buyer wrote a percentile standard and the 2012 buyer, on the same core system, wrote an average. The definition, if one exists, would be in the resulting contract or the monthly performance reports; both are in the new records request.

6. **Who was in the room.** Questions came from Xerox State & Local (61 mentions), Deloitte (46), Accenture (33), HP Enterprise Services (13), Northrop Grumman (8), Unisys (6) and IBM (1) (F26854). [inference] Northrop Grumman's questions about the transition from the "incumbent" O&M provider are consistent with it being the incumbent, but the set does not name the incumbent; that needs a source.

7. **The award was driven by the ACA deadline.** Medicaid/CHIP functionality was required "by October 2013 in preparation for a January 2014 implementation," which DCF called "a very tight timeframe" (F4863, ITN p. 3). The ITN also allowed for the AHCA feasibility study to choose remediation instead of replacement (ITN p. 1).

## 4. Gaps: documents referenced but not in this set

Addendum 2 (F31900, p. 2) lists supporting documents posted only on DCF's website, which is no longer live:
- **ACCESS Florida Technical Architecture.v.1.0.pdf** (its "Section 7.0 Key Statistics" and hardware/software specifications are cited in the Q&A). This is the most important missing item for the capacity history.
- DCF Feasibility Study v3.0 (Schedule IV-B)
- Requirements Definition Document v1.3
- FLORIDA IMS Data Dictionary; FLODS Data Dictionary

The Internet Archive holds none of these. It does hold one later item from the same DCF folder: `20130305_ITN 03F12GC1_Historic Procurement Document v 3.pdf` (Negotiation Team Recommendation, captured 2019-02-14), plus some vendor reply tabs (Accenture, Deloitte, Xerox).

## 5. Proposed log entries (not written; for your decision)

Following your rule of logging new evidence for the sweep, these are candidate PENDING-CHANGES rows. I have not written them.

- A. Cite ITN 03F12GC1 p. 46 for "FLORIDA, implemented 1992, still the legacy mainframe core in 2012."
- B. Q1 2012 workload figures (§ 3.3), with the units caveat, for the capacity-over-time brief (rows 79-89).
- C. FLORIDA IMS footprint 1.17 TB and the 12-LPAR, COBOL/SyncSort estate (§ 3.4).
- D. Records request to DCF for the Technical Architecture Document v1.0, the Feasibility Study v3.0 and the IMS data dictionary, plus the response-time definition, call-center source data, executed contract and the s. 287.057(1)(c) determination. Drafted 2026-11-22 as a Gmail draft (not sent).
- E. Fetch the Wayback copy of the 2013 Negotiation Team Recommendation.
- F. Calls per household (0.94/month) and the average-vs-percentile response-time contrast with the 1988 RFP, as observations for the capacity brief.

## 6. Acceptance still open

- Flagged items: reviewed above (all pass; p. 89 transcribed).
- Permanent location for the run outputs: **not yet chosen**. They are in /tmp, which is not backed up.
