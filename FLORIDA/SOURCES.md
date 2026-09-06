# SOURCES — The FLORIDA System Archive

Every external source cited in the analytical papers of this archive, grouped by kind, with the state of each link as of **July 28, 2026**.

This file exists because the archive's central claim about itself is that it is traceable. A reader who wants to check any statement in any paper should be able to find the underlying document without reading fifteen files. It also exists because link rot is the standing threat to work of this kind: the events described here are thirty-eight years old, several of the newspapers that covered them have changed platforms twice, and one primary procurement document went off the web during the research.

## Mirroring pass, August 19, 2026

Of the 140 sources listed below, 105 were classified as load-bearing (directly supporting a specific quote, figure, or claim reproduced in an archive paper, as opposed to general background). Of those 105, **99 now have a full-text local mirror** saved under `sources/` and linked inline ("— mirrored: ...") next to the original URL. Coverage:

- **95** mirrored via automated fetch during this pass (5 batches of ~20 URLs each).
- **3** LA Times articles mirrored directly (see "press articles starting with LA," below).
- **1** additional recovery: the CourtListener opinion in *State, DHRS v. EDS Federal Corp.* returned an empty HTTP 202 body to every automated retrieval attempt (a bot-challenge holding page, not link rot — the citation itself is correct and the case is real); the full opinion text was instead recovered from a CaseMine mirror and saved.
- **2 already-mirrored primary documents** (the two DOAH recommended orders) predate this pass.
- **1 genuine gap remains**: the IBM CICS TS documentation glossary page (LSPR terminology) blocked automated retrieval across 4 URL variants and was not force-mirrored, since it is a generic glossary definition already corroborated by other mirrored IBM LSPR documents in this table.
- **3** Wayback Machine capture URLs (already-archived-equivalent by definition) were left as-is, not separately re-mirrored.
- The 35 sources classified as "context" (not load-bearing — CFR index pages, docket/portal homepages, FOIA portals, and similar) were left unmirrored per the scope agreed for this pass; they can be added later if the archive's traceability standard is extended to cover them too.
- One citation discrepancy was discovered and documented in both this file and the citing paper: a govregs.com URL slug for "§ 205.38" actually reads "section205.50" in its address, though the underlying prose citation in `FLORIDA-system-addendum-sources.md` was already correct.

All mirror files follow a standard header (source, URL, title, retrieval date, citing files, and the specific load-bearing quote/figure) followed by the full retrieved text.

## How to read the status column

| Status | Meaning |
|---|---|
| OK | Returned HTTP 200 or 202 to an automated request on July 28, 2026 |
| Live; blocks automated checks | Returned 403 or timed out to an automated request, but the page loads in a browser. Common for newspaper sites with bot protection — the *Tampa Bay Times*, *Los Angeles Times*, *Washington Post*, and *Miami Herald* archives all behave this way |
| Archived | The original address is dead; the citation points to an Internet Archive capture, with the capture timestamp in the URL |

## Repairs made in this pass

Six links in the published papers were dead and have been repaired:

| Was | Now | Notes |
|---|---|---|
| `casetext.com/case/state-dhrs-v-eds-federal-corp` (HTTP 410) | [CourtListener opinion 1895493](https://www.courtlistener.com/opinion/1895493/state-dhrs-v-eds-federal-corp/) | *State, DHRS v. EDS Federal Corp.*, 631 So. 2d 353 (Fla. 1st DCA 1994). This was the most-cited link in the archive — it appeared in nine papers — and Casetext retired it. CourtListener is a non-profit with a durability commitment, which Casetext, now owned by Thomson Reuters, does not have |
| USDA OIG report `27004-3-AT.pdf` (404) | [`27004-3-At.pdf`](https://usdaoig.oversight.gov/sites/default/files/reports/2023-07/27004-3-At.pdf) | Case-sensitive filename. The file never moved |
| `vm.ibm.com/events/2006-L79.PDF` (404) | [Internet Archive capture, Oct. 19, 2022](https://web.archive.org/web/20221019025134/http://www.vm.ibm.com/events/2006-L79.PDF) | The Miami-Dade SNA topology document, load-bearing for the era-plausibility argument in the topology paper |
| Industry Insider Florida, DCF budget request (404) | [Internet Archive capture, Oct. 10, 2025](https://web.archive.org/web/20251010101725/https://insider.govtech.com/florida/news/department-of-children-and-families-asks-for-74m-for-it) | |
| DCF MyACCESS modernization press release (404) | [Internet Archive capture, Oct. 30, 2025](https://web.archive.org/web/20251030231755/https://www.myflfamilies.com/news-events/newsroom/press-release/department-children-and-families-announces-modernized-myaccess) | |
| UK CPR Heflin & Mueser discussion paper (404) | [Internet Archive capture, Aug. 9, 2025](https://web.archive.org/web/20250809092014/https://cpr.uky.edu/sites/ukcpr/files/research-pdfs/DP2010-01_heflin_mueser.pdf) | |

## One source that could not be repaired

**Florida Department of Children and Families, *ACCESS Florida System Replacement*, Invitation to Negotiate 03F12GC1, June 22, 2012.**

This document is the source of the IMS database inventory — 88 OSAM and 206 VSAM databases, 1.17 TB of production data — the imaging-store volumes, and the list of twenty-two satellite systems, all of which appear in the topology paper and one of which appears in the Annals manuscript. It was retrieved during research from the Florida Vendor Bid System at `myflorida.com/apps/vbs/adoc/F4863_20120622DCF10ACCESSFloridaReplacementITNv1.0.pdf`.

That address now returns HTTP 404. The Vendor Bid System purges advertisements after a retention interval, and the Internet Archive has no capture — the CDX index returns nothing for the path prefix, and a save request cannot capture a page that is already gone. The citation has therefore been converted in both papers from a hyperlink to a full bibliographic reference with an availability note, which is the correct scholarly treatment of a document that exists but is not online.

It remains a public record under Chapter 119, Florida Statutes. A request for it has been added to the records-request set. **When a copy is obtained it should be committed to this repository**, so that the archive's most detailed description of the as-built system stops depending on a state webserver's retention policy.

The general lesson is worth stating because it applies to roughly a dozen other state-hosted PDFs in the tables below: a link to a government document is not preservation. Anything genuinely load-bearing should be mirrored into the repository, and that is now a standing item in the README's future-work list.

## Counts

| Category | Sources |
|---|---|
| Administrative, judicial, and statutory record | 31 |
| Federal oversight, policy, and program documents | 22 |
| Florida state records and official publications | 14 |
| Technical and scholarly literature | 13 |
| Contemporaneous and later press | 10 |
| Other press, trade, and secondary sources | 50 |
| **Total** | **140** |

The `research-*.md` files carry a further 180-odd URLs. Those are raw retrieval notes rather than published analysis, and they are not link-checked here.

## Short names used in the "Cited in" column

`main` = FLORIDA-system-EDS-IBM-HRS-analysis · `protest` = kastner-unisys-protest-analysis · `topology` = FLORIDA-as-built-topology · `capacity` = FLORIDA-capacity-modeling-tools · `cost` = FLORIDA-cost-reconciliation · `operating` = FLORIDA-operating-conditions · `remediation` = FLORIDA-throughput-remediation-table · `post-2000` = FLORIDA-post2000-analysis · `federal-86` = federal-policy-arc-1986-1999 · `federal-96` = federal-arc-1996-to-present · `annals` = FLORIDA-annals-manuscript · `addendum` = FLORIDA-system-addendum-sources · `requests` = FLORIDA-records-requests-drafts · `carlton` = carlton-fields-records-request

---

## Administrative, judicial, and statutory record

| Source | Cited in | Link status |
|---|---|---|
| [40 U.S.C. 11312](https://www.govinfo.gov/content/pkg/USCODE-2010-title40/pdf/USCODE-2010-title40-subtitleIII-chap113-subchapII-sec11312.pdf) — mirrored: [`sources/40-usc-11312-capital-planning.txt`](sources/40-usc-11312-capital-planning.txt) | federal-86 | OK |
| [42 CFR §433.112(b)](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-433/subpart-C) — mirrored: [`sources/42-cfr-433-112-medicaid-mmis-ffp.txt`](sources/42-cfr-433-112-medicaid-mmis-ffp.txt) | federal-96 | OK |
| [45 CFR 1355.52, CCWIS](https://www.ecfr.gov/current/title-45/subtitle-B/chapter-XIII/subchapter-G/part-1355/section-1355.52) — mirrored: [`sources/45-cfr-1355-52-ccwis-requirements.txt`](sources/45-cfr-1355-52-ccwis-requirements.txt) | federal-96 | OK |
| [45 CFR 205.37](https://www.govinfo.gov/content/pkg/CFR-2012-title45-vol2/pdf/CFR-2012-title45-vol2-sec205-37.pdf) — mirrored: [`sources/45-cfr-205-37-acf-responsibilities-govinfo.txt`](sources/45-cfr-205-37-acf-responsibilities-govinfo.txt) | federal-86 | OK |
| [45 CFR 205.37 (LII)](https://www.law.cornell.edu/cfr/text/45/205.37) — mirrored: [`sources/45-cfr-205-37-acf-responsibilities-cornell-lii.txt`](sources/45-cfr-205-37-acf-responsibilities-cornell-lii.txt) | addendum, federal-86, main, protest, remediation, requests | OK |
| [45 CFR 307.10](https://www.law.cornell.edu/cfr/text/45/307.10) — mirrored: [`sources/45-cfr-307-10-functional-requirements-child-support.txt`](sources/45-cfr-307-10-functional-requirements-child-support.txt) | federal-86 | OK |
| [45 CFR Part 95 Subpart F](https://www.law.cornell.edu/cfr/text/45/part-95/subpart-F) | federal-86 | OK |
| [45 CFR Part 95 Subpart F, current](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-95/subpart-F) — mirrored: [`sources/45-cfr-95-subpart-f-adp-conditions-ffp.txt`](sources/45-cfr-95-subpart-f-adp-conditions-ffp.txt) | federal-96 | OK |
| [59 FR 94-14326 (June 15, 1994)](https://www.govinfo.gov/content/pkg/FR-1994-06-15/html/94-14326.htm) — mirrored: [`sources/fr-1994-famis-enhanced-funding-elimination.txt`](sources/fr-1994-famis-enhanced-funding-elimination.txt) | federal-86 | OK |
| [63 FR 98-7714 (Mar. 25, 1998)](https://www.govinfo.gov/content/pkg/FR-1998-03-25/html/98-7714.htm) | federal-86 | OK |
| [7 CFR 277.18, 1999 annual edition](https://www.govinfo.gov/content/pkg/CFR-1999-title7-vol4/pdf/CFR-1999-title7-vol4-sec277-18.pdf) — mirrored: [`sources/7-cfr-277-18-1999-annual-edition-adp.txt`](sources/7-cfr-277-18-1999-annual-edition-adp.txt) | federal-86, federal-96 | OK |
| [7 CFR 277.18, current](https://www.ecfr.gov/current/title-7/subtitle-B/chapter-II/subchapter-C/part-277/section-277.18) — mirrored: [`sources/7-cfr-277-18-current-ecfr-full.txt`](sources/7-cfr-277-18-current-ecfr-full.txt) | federal-96 | OK |
| [7 CFR 277.18, current](https://www.law.cornell.edu/cfr/text/7/277.18) — mirrored: [`sources/7-cfr-277-18-current-snap-is-apd.txt`](sources/7-cfr-277-18-current-snap-is-apd.txt) | federal-86 | OK |
| [Child Support Enforcement Amendments of 1984, P.L. 98-378](https://www.congress.gov/98/statute/STATUTE-98/STATUTE-98-Pg1305.pdf) — mirrored: [`sources/pl-98-378-child-support-enforcement-amendments-1984.txt`](sources/pl-98-378-child-support-enforcement-amendments-1984.txt) | federal-86 | OK |
| [CSPIA 1998, P.L. 105-200](https://www.govinfo.gov/content/pkg/PLAW-105publ200/html/PLAW-105publ200.htm) — mirrored: [`sources/pl-105-200-cspia-1998.txt`](sources/pl-105-200-cspia-1998.txt) | federal-86 | OK |
| [DOAH Case 88-2942BID, Recommended Order](https://www.doah.state.fl.us/ROS/1988/88002942.PDF) — mirrored: [`unisys_88-2942BID_recommended_order.pdf`](unisys_88-2942BID_recommended_order.pdf) | README, annals, capacity, cost, federal-86, federal-96, main, operating, post-2000, protest, remediation, requests, topology | OK |
| [DOAH Case 89-0003BID Recommended Order](https://www.doah.state.fl.us/ROS/1989/89000003.PDF) — mirrored: [`unisys_89-0003BID_recommended_order.pdf`](unisys_89-0003BID_recommended_order.pdf) | README, annals, capacity, cost, federal-86, main, operating, post-2000, protest, requests, topology | OK |
| [Doe v. Chiles](https://law.justia.com/cases/federal/appellate-courts/F3/136/709/553690/) | operating | Live; blocks automated checks |
| [Family Support Act of 1988, P.L. 100-485](https://www.congress.gov/100/statute/STATUTE-102/STATUTE-102-Pg2343.pdf) — mirrored: [`sources/pl-100-485-family-support-act-1988.txt`](sources/pl-100-485-family-support-act-1988.txt) | federal-86 | OK |
| [Federal Acquisition Streamlining Act of 1994](https://www.congress.gov/bill/103rd-congress/senate-bill/1587) — mirrored: [`sources/federal-acquisition-streamlining-act-1994-s1587.txt`](sources/federal-acquisition-streamlining-act-1994-s1587.txt) | federal-86 | Live; blocks automated checks |
| [Florida Division of Administrative Hearings](https://www.doah.state.fl.us/) | README | OK |
| [Florida Supreme Court statewide grand jury page](https://supremecourt.flcourts.gov/News-Media/Statewide-Grand-Jury) — mirrored: [`sources/florida-supreme-court-statewide-grand-jury.txt`](sources/florida-supreme-court-statewide-grand-jury.txt) | requests | OK |
| [GAO/AIMD-94-115](https://www.govinfo.gov/content/pkg/GAOREPORTS-AIMD-94-115/html/GAOREPORTS-AIMD-94-115.htm) | federal-86 | OK |
| [GAO/AIMD-94-52FS](https://www.govinfo.gov/content/pkg/GAOREPORTS-AIMD-94-52FS/html/GAOREPORTS-AIMD-94-52FS.htm) — mirrored: [`sources/gao-aimd-94-52fs-automated-welfare-systems.txt`](sources/gao-aimd-94-52fs-automated-welfare-systems.txt) | addendum, annals, cost, federal-86, main, operating, remediation, topology | OK |
| [GAO/HEHS-00-48](https://www.govinfo.gov/content/pkg/GAOREPORTS-HEHS-00-48/pdf/GAOREPORTS-HEHS-00-48.pdf) | post-2000 | OK |
| [Gonzalez v. Pingree](https://law.justia.com/cases/federal/appellate-courts/F2/821/1526/255811/) | operating | Live; blocks automated checks |
| [Government Performance and Results Act of 1993](https://www.congress.gov/103/bills/s20/BILLS-103s20enr.pdf) — mirrored: [`sources/gpra-1993-pl-103-62-s20.txt`](sources/gpra-1993-pl-103-62-s20.txt) | federal-86 | OK |
| [H. Rept. 104-250 (P.L. 104-35)](https://www.congress.gov/committee-report/104th-congress/house-report/250/1) — mirrored: [`sources/h-rept-104-250-automation-deadline-extension.txt`](sources/h-rept-104-250-automation-deadline-extension.txt) | federal-86 | Live; blocks automated checks |
| [Michigan MiDAS](https://law.justia.com/cases/federal/appellate-courts/ca6/18-1296/18-1296-2019-01-03.html) — mirrored: [`sources/cahoo-v-sas-analytics-michigan-midas-6th-circuit-2019.txt`](sources/cahoo-v-sas-analytics-michigan-midas-6th-circuit-2019.txt) | federal-96 | Live; blocks automated checks |
| [PRWORA, P.L. 104-193](https://www.congress.gov/104/plaws/publ193/PLAW-104publ193.pdf) — mirrored: [`sources/prwora-pl-104-193.txt`](sources/prwora-pl-104-193.txt) | federal-86 | OK |
| [State, Dep't of HRS v. E.D.S. Federal Corp., 631 So. 2d 353](https://www.courtlistener.com/opinion/1895493/state-dhrs-v-eds-federal-corp/) — mirrored: [`sources/state-dhrs-v-eds-federal-corp-631so2d353.txt`](sources/state-dhrs-v-eds-federal-corp-631so2d353.txt) | addendum, annals, cost, federal-86, federal-96, main, post-2000, protest, remediation | OK |

## Florida state records and official publications

| Source | Cited in | Link status |
|---|---|---|
| [AG Report 2010-066](https://www.flauditor.gov/pages/pdf_files/2010-066.pdf) — mirrored: [`sources/florida-auditor-general-2010-066.txt`](sources/florida-auditor-general-2010-066.txt) | topology | OK |
| [Auditor General Report 2013-005](https://flauditor.gov/pages/pdf_files/2013-005.pdf) — mirrored: [`sources/florida-auditor-general-2013-005.txt`](sources/florida-auditor-general-2013-005.txt) | post-2000, topology | OK |
| [Auditor General Report 2019-022](https://flauditor.gov/pages/pdf_files/2019-022.pdf) — mirrored: [`sources/florida-auditor-general-2019-022.txt`](sources/florida-auditor-general-2019-022.txt) | annals, post-2000, topology | OK |
| [Auditor General Report 2025-162](https://flauditor.gov/pages/pdf_files/2025-162%20sspaf.pdf) — mirrored: [`sources/florida-auditor-general-2025-162.txt`](sources/florida-auditor-general-2025-162.txt) | annals, post-2000, topology | OK |
| [Florida Auditor General FY1995-96 listing](https://flauditor.gov/pages/list9596page.htm) — mirrored: [`sources/florida-auditor-general-fy1995-96-listing.txt`](sources/florida-auditor-general-fy1995-96-listing.txt) | addendum, annals, main, protest, remediation, requests, topology | OK |
| [Florida Auditor General FY1997-98 listing](https://flauditor.gov/pages/list9798page.htm) — mirrored: [`sources/florida-auditor-general-fy1997-98-listing.txt`](sources/florida-auditor-general-fy1997-98-listing.txt) | addendum, annals, cost, main, protest, remediation, requests, topology | OK |
| [Florida Auditor General Report 2019-183](https://flauditor.gov/pages/pdf_files/2019-183.pdf) | federal-96 | OK |
| [Florida Auditor General report request page](https://flauditor.gov/pages/report_request.html) | requests | OK |
| [Florida DCF](https://web.archive.org/web/20251030231755/https://www.myflfamilies.com/news-events/newsroom/press-release/department-children-and-families-announces-modernized-myaccess) | post-2000 | OK |
| [FY 1996-97](https://flauditor.gov/pages/list9697page.htm) | addendum | OK |
| [FY 1998-99](https://flauditor.gov/pages/list9899page.htm) | addendum | OK |
| [Gartner AHCA study](https://www.leg.state.fl.us/Data/Committees/Joint/JLBC/Meetings/Packets/AHCA%20-%20Integrated%20Eligibility%20System%20Modernization%20Feasibility%20Study.pdf) — mirrored: [`sources/gartner-ahca-feasibility-study.txt`](sources/gartner-ahca-feasibility-study.txt) | topology | OK |
| [Gartner, AHCA Integrated Eligibility System Modernization Feasibility Study](http://www.leg.state.fl.us/Data/Committees/Joint/JLBC/Meetings/Packets/AHCA%20-%20Integrated%20Eligibility%20System%20Modernization%20Feasibility%20Study.pdf) — mirrored: [`sources/gartner-ahca-feasibility-study-annals.txt`](sources/gartner-ahca-feasibility-study-annals.txt) | annals, post-2000 | OK |
| [Gartner, Report to the Joint Legislative Budget Commission](http://www.leg.state.fl.us/Data/Committees/Joint/JLBC/Meetings/Packets/Gartner%20Study.pdf) — mirrored: [`sources/gartner-report-jlbc-2012.txt`](sources/gartner-report-jlbc-2012.txt) | annals, post-2000, topology | OK |

## Federal oversight, policy, and program documents

| Source | Cited in | Link status |
|---|---|---|
| [GAO-23-105478](https://www.gao.gov/assets/gao-23-105478.pdf) — mirrored: [`sources/gao-23-105478.txt`](sources/gao-23-105478.txt) | federal-96 | Live; blocks automated checks |
| [GAO/AIMD-10.1.13](https://www.gao.gov/assets/aimd-10.1.13.pdf) | federal-86 | Live; blocks automated checks |
| [GAO/AIMD-97-72](https://www.gao.gov/products/aimd-97-72) — mirrored: [`sources/gao-aimd-97-72.txt`](sources/gao-aimd-97-72.txt) | federal-86 | Live; blocks automated checks |
| [GAO/AIMD-98-134](https://www.gao.gov/assets/aimd-98-134.pdf) — mirrored: [`sources/gao-aimd-98-134.txt`](sources/gao-aimd-98-134.txt) | federal-86 | Live; blocks automated checks |
| [GAO/HR-95-1](https://www.gao.gov/assets/hr-95-1.pdf) — mirrored: [`sources/gao-hr-95-1.txt`](sources/gao-hr-95-1.txt) | federal-86 | Live; blocks automated checks |
| [GAO/HR-97-9](https://www.gao.gov/assets/hr-97-9.pdf) — mirrored: [`sources/gao-hr-97-9.txt`](sources/gao-hr-97-9.txt) | federal-86 | Live; blocks automated checks |
| [GAO/HRD-81-119](https://www.gao.gov/products/hrd-81-119) — mirrored: [`sources/gao-hrd-81-119.txt`](sources/gao-hrd-81-119.txt) | addendum, federal-86, protest, requests | Live; blocks automated checks |
| [GAO/IMTEC-92-29](https://www.gao.gov/products/imtec-92-29) — mirrored: [`sources/gao-imtec-92-29.txt`](sources/gao-imtec-92-29.txt) | addendum, federal-86, federal-96, protest, requests | Live; blocks automated checks |
| [GAO/IMTEC-92-46](https://www.gao.gov/assets/imtec-92-46.pdf) — mirrored: [`sources/gao-imtec-92-46.txt`](sources/gao-imtec-92-46.txt) | federal-86 | Live; blocks automated checks |
| [HHS DAB No. 1520 (1995)](https://www.hhs.gov/sites/default/files/static/dab/decisions/board-decisions/1995/dab1520.html) — mirrored: [`sources/hhs-dab-1520-1995.txt`](sources/hhs-dab-1520-1995.txt) | operating | Live; blocks automated checks |
| [HHS OIG OEI-04-96-00010](https://oig.hhs.gov/oei/reports/oei-04-96-00010.pdf) — mirrored: [`sources/hhs-oig-child-support-certified-data-systems-1997.txt`](sources/hhs-oig-child-support-certified-data-systems-1997.txt) | federal-86 | OK |
| [HHS OIG, AFDC/SSI coordination (Oct. 1995)](https://oig.hhs.gov/reports/all/1995/florida-department-of-health-and-rehabilitative-services-procedures-for-coordinating-afdc-and-ssi-benefits/) — mirrored: [`sources/hhs-oig-florida-afdc-ssi-coordination-1995.txt`](sources/hhs-oig-florida-afdc-ssi-coordination-1995.txt) | operating | OK |
| [HHS/ASPE historical AFDC quality-control data](https://aspe.hhs.gov/sites/default/files/migrated_legacy_files//155481/08tanf.txt) — mirrored: [`sources/aspe-hhs-afdc-quality-control-historical-data.txt`](sources/aspe-hhs-afdc-quality-control-historical-data.txt) | annals, operating | OK |
| [Memorandum M-97-02, the "Raines Rules," issued October 25, 1996](https://trumpwhitehouse.archives.gov/wp-content/uploads/2017/11/1997-M-97-02-Funding-Information-Systems-Investments.pdf) — mirrored: [`sources/omb-memorandum-m-97-02-raines-rules-1996.txt`](sources/omb-memorandum-m-97-02-raines-rules-1996.txt) | federal-86 | OK |
| [National Archives](https://www.archives.gov) — mirrored: [`sources/national-archives-nara-homepage.txt`](sources/national-archives-nara-homepage.txt) | requests | OK |
| [National Performance Review's information-technology report](https://clintonwhitehouse6.archives.gov/1993/09/1993-09-01-npr-on-reengineering-through-information-technology-part.html) | federal-86 | OK |
| [OTA, *Informing the Nation*](https://ota.fas.org/reports/8812.pdf) | federal-86 | OK |
| [OTA, *Making Government Work*](https://ota.fas.org/reports/9333.pdf) | federal-86 | OK |
| [USDA FNS, "Modernization of the Food Stamp Program in Florida," Feb. 2008](https://fns-prod.azureedge.us/sites/default/files/FloridaModern.pdf) — mirrored: [`sources/usda-fns-modernization-food-stamp-program-florida-2008.txt`](sources/usda-fns-modernization-food-stamp-program-florida-2008.txt) | capacity, post-2000, topology | OK |
| [USDA FOIA Division listing](https://www.usda.gov/about-usda/general-information/staff-offices/office-general-counsel/office-information-affairs/freedom-information-act-division) | requests | Live; blocks automated checks |
| [USDA OIG Audit 27004-3-AT (Nov. 2001)](https://usdaoig.oversight.gov/sites/default/files/reports/2023-07/27004-3-At.pdf) — mirrored: [`sources/usda-oig-audit-27004-3-at-florida-food-stamp-2001.txt`](sources/usda-oig-audit-27004-3-at-florida-food-stamp-2001.txt) | annals, federal-86, operating, post-2000 | OK |
| [USDA Public Access Link](https://efoia-pal.usda.gov) | requests | OK |

## Contemporaneous and later press

| Source | Cited in | Link status |
|---|---|---|
| [*Los Angeles Times*, May 2, 1993](https://www.latimes.com/archives/la-xpm-1993-05-02-mn-30237-story.html) — mirrored: [`sources/latimes-1993-05-02-florida-computer-hurricane.txt`](sources/latimes-1993-05-02-florida-computer-hurricane.txt) | addendum, annals, capacity, cost, federal-86, main, operating, protest, remediation, requests, topology | OK |
| [LA Times, Apr. 19, 1995](https://www.latimes.com/archives/la-xpm-1995-04-19-mn-56404-story.html) — mirrored: [`sources/latimes-1995-04-19-california-saws-audit.txt`](sources/latimes-1995-04-19-california-saws-audit.txt) | federal-96 | OK |
| [LA Times, Nov. 21, 1997](https://www.latimes.com/archives/la-xpm-1997-nov-21-mn-56038-story.html) — mirrored: [`sources/latimes-1997-11-21-california-child-support-computer-dies.txt`](sources/latimes-1997-11-21-california-child-support-computer-dies.txt) | federal-86 | OK |
| [Maryland](https://www.washingtonpost.com/local/md-politics/noridian-to-pay-45m-to-state-us-government-for-flawed-md-exchange/2015/07/21/cb9b7028-2fd5-11e5-8353-1215475949f4_story.html) — mirrored: [`sources/washington-post-maryland-noridian-settlement-2015.txt`](sources/washington-post-maryland-noridian-settlement-2015.txt) | federal-96 | Live; blocks automated checks |
| [Miami Herald](https://www.miamiherald.com/news/politics-government/state-politics/article249702448.html) | federal-96 | Live; blocks automated checks |
| [St. Petersburg Times account of September 15, 1995](https://www.tampabay.com/archive/1995/09/15/hrs-supercomputer-can-t-hack-it-report-says/) — mirrored: [`sources/tampa-bay-times-1995-09-15-hrs-supercomputer-cant-hack-it.txt`](sources/tampa-bay-times-1995-09-15-hrs-supercomputer-cant-hack-it.txt) | addendum, annals, capacity, cost, federal-86, main, operating, protest, remediation, topology | OK |
| [St. Petersburg Times, Aug. 3, 1992](https://www.tampabay.com/archive/1992/08/03/state-faces-fine-of-5-million-for-food-stamp-errors/) — mirrored: [`sources/tampa-bay-times-1992-08-03-food-stamp-fine.txt`](sources/tampa-bay-times-1992-08-03-food-stamp-fine.txt) | annals, cost, main, operating, protest, remediation, requests | OK |
| [Tampa Bay Times, Apr. 28, 1993](https://www.tampabay.com/archive/1993/04/28/eds-wins-another-computer-contract/) — mirrored: [`sources/tampa-bay-times-1993-04-28-eds-five-year-contract.txt`](sources/tampa-bay-times-1993-04-28-eds-five-year-contract.txt) | cost, main, protest, remediation | OK |
| [Tampa Bay Times, Aug. 16, 1995 account](https://www.tampabay.com/archive/1995/08/16/faulty-computer-could-cost-state-more/) — mirrored: [`sources/tampa-bay-times-1995-08-16-faulty-computer-could-cost-more.txt`](sources/tampa-bay-times-1995-08-16-faulty-computer-could-cost-more.txt) | addendum, annals, capacity, cost, federal-86, main, operating, protest, remediation, requests | OK |
| [Tampa Bay Times, Mar. 9, 2021](https://www.tampabay.com/news/florida-politics/2021/03/09/dont-blame-us-for-unemployment-failures-deloitte-tells-florida-senators/) — mirrored: [`sources/tampa-bay-times-2021-03-09-deloitte-unemployment.txt`](sources/tampa-bay-times-2021-03-09-deloitte-unemployment.txt) | federal-96 | OK |

## Technical and scholarly literature

| Source | Cited in | Link status |
|---|---|---|
| [*ACM Computing Surveys*](https://dl.acm.org/doi/pdf/10.1145/356733.356738) — mirrored: [`sources/acm-computing-surveys-best1-queueing-model.txt`](sources/acm-computing-surveys-best1-queueing-model.txt) | capacity | Live; blocks automated checks |
| [bitsavers.org](https://bitsavers.org/pdf/ibm/IBM_Systems_Journal/183/ibmsj1803C.pdf) — mirrored: [`sources/bitsavers-ibm-systems-journal-1979-stewart.txt`](sources/bitsavers-ibm-systems-journal-1979-stewart.txt) | annals | OK |
| [IBM Communication Controller Migration Guide](https://www.redbooks.ibm.com/redbooks/pdfs/sg246298.pdf) — mirrored: [`sources/ibm-redbook-communication-controller-migration.txt`](sources/ibm-redbook-communication-controller-migration.txt) | capacity | OK |
| [IBM GDDM documentation](https://www.ibm.com/docs/en/gddm?topic=gddm-distributed-function-terminals-3179-3192-3472-3472) — mirrored: [`sources/ibm-gddm-distributed-function-terminals.txt`](sources/ibm-gddm-distributed-function-terminals.txt) | capacity | OK |
| [IBM IMS documentation](https://www.ibm.com/docs/en/ims/15.4.0?topic=eto-overview-extended-terminal-option) — mirrored: [`sources/ibm-ims-extended-terminal-option.txt`](sources/ibm-ims-extended-terminal-option.txt) | annals, operating | OK |
| [IBM program directory](https://publibfp.dhe.ibm.com/epubs/pdf/i1085472.pdf) — mirrored: [`sources/ibm-program-directory-eto.txt`](sources/ibm-program-directory-eto.txt) | operating | OK |
| [IBM zEXPO 2006, "CCL Customer Experiences"](https://web.archive.org/web/20221019025134/http://www.vm.ibm.com/events/2006-L79.PDF) | topology | OK |
| [IBM, CICS TS documentation, LSPR terminology](https://www.ibm.com/docs/en/cics-ts/6.x?topic=terminology-large-systems-performance-reference) — **NOT mirrored**: blocked automated retrieval on Aug. 19, 2026 across 4 attempted URL variants (`missing_corpus` / client-error responses from ibm.com's docs platform to both `fetch_url` and direct `curl`). Page content is a standard glossary definition of "LSPR" corroborated by IBM's own LSPR reference documents already mirrored elsewhere in this table (see `ibm-lspr-large-systems-performance-reference.txt`); not re-attempted further as low marginal value. | capacity | Live; blocks automated checks |
| [IMS migration guide](https://publibfp.dhe.ibm.com/epubs/pdf/dfsmigg5.pdf) — mirrored: [`sources/ims-migration-guide-glossary.txt`](sources/ims-migration-guide-glossary.txt) | annals, operating | OK |
| [IMS System Definition manual](https://publibfp.dhe.ibm.com/epubs/pdf/dfssdgi5.pdf) — mirrored: [`sources/ims-system-definition-manual.txt`](sources/ims-system-definition-manual.txt) | annals, operating | OK |
| [Montealegre & Keil, MIS Quarterly 24(3), 2000](https://dl.acm.org/doi/10.2307/3250968) | post-2000 | Live; blocks automated checks |
| [own description](https://www.ibm.com/support/pages/system/files/inline-files/SC28118726.pdf) — mirrored: [`sources/ibm-lspr-large-systems-performance-reference.txt`](sources/ibm-lspr-large-systems-performance-reference.txt) | capacity | OK |
| [System z Mean Time to Recovery Best Practices](https://www.redbooks.ibm.com/redbooks/pdfs/sg247816.pdf) | operating | OK |

## Other press, trade, and secondary sources

| Source | Cited in | Link status |
|---|---|---|
| ["Large Project Software Scare"](https://www.govtech.com/magazines/gt/large-project-software-scare.html) — mirrored: [`sources/govtech-large-project-software-scare.txt`](sources/govtech-large-project-software-scare.txt) | post-2000 | OK |
| [*Chianne D.* proposed findings, M.D. Fla. 3:23-cv-00985](https://affordablecareactlitigation.com/wp-content/uploads/2024/10/chianne-d-def-proposed-ffcl-9-18-24.pdf) — mirrored: [`sources/chianne-d-defendants-proposed-findings.txt`](sources/chianne-d-defendants-proposed-findings.txt) | annals, topology | OK |
| [*IBM Systems Journal*, vol. 18, no. 3 (1979), pp. 356–373](http://bitsavers.informatik.uni-stuttgart.de/pdf/ibm/IBM_Systems_Journal/183/ibmsj1803C.pdf) — mirrored: [`sources/ibm-systems-journal-1979-stewart-snapshot.txt`](sources/ibm-systems-journal-1979-stewart-snapshot.txt) | README, capacity | OK |
| [1,600 percent surge in claims](https://www.nj.com/coronavirus/2020/04/nj-unemployment-claims-are-processed-by-a-40-year-old-computer-system-as-demand-soars.html) — mirrored: [`sources/nj-com-unemployment-40-year-old-computer.txt`](sources/nj-com-unemployment-40-year-old-computer.txt) | federal-96 | Live; blocks automated checks |
| [3.1 million busy signals out of 3.5 million calls on April 7, 2020](https://www.texastribune.org/2020/05/19/texas-unemployment-benefits-coronavirus/) — mirrored: [`sources/texas-tribune-unemployment-mainframe-coronavirus.txt`](sources/texas-tribune-unemployment-mainframe-coronavirus.txt) | federal-96 | OK |
| [acf.gov/foia](https://acf.gov/foia) | requests | OK |
| [Advanced Systems Design, Inc. v. Strawn, Fla. 1st DCA 1997](https://caselaw.findlaw.com/court/fl-district-court-of-appeal/1203645.html) — mirrored: [`sources/advanced-systems-design-v-strawn-1997.txt`](sources/advanced-systems-design-v-strawn-1997.txt) | cost, main, protest, remediation | Live; blocks automated checks |
| [announced February 15, 1988 for 3090 E models](https://en.wikipedia.org/wiki/IBM_3090) — mirrored: [`sources/wikipedia-ibm-3090.txt`](sources/wikipedia-ibm-3090.txt) | capacity | OK |
| [CA State Auditor 97116](https://information.auditor.ca.gov/pdfs/reports/97116.pdf) — mirrored: [`sources/ca-state-auditor-97116-sacss-lockheed.txt`](sources/ca-state-auditor-97116-sacss-lockheed.txt) | federal-86 | OK |
| [California CWS-CARES](https://lao.ca.gov/Publications/Report/5006) — mirrored: [`sources/lao-2025-26-budget-cws-cares.txt`](sources/lao-2025-26-budget-cws-cares.txt) | federal-96 | OK |
| [Carlton Fields Tallahassee attorney guide](https://www.carltonfields.com/files/upload/AttyMediaGuideTallahassee.pdf) | carlton | OK |
| [CaseMine full text](https://www.casemine.com/judgement/us/591485a5add7b049344c93d0/amp) — mirrored: [`sources/casemine-eds-v-hrs-florida-dispute-resolution.txt`](sources/casemine-eds-v-hrs-florida-dispute-resolution.txt) | main | OK |
| [Citron, Technological Due Process (2008)](https://scholarship.law.bu.edu/faculty_scholarship/615/) | post-2000 | OK |
| [Clinger-Cohen Act of 1996](https://home.treasury.gov/system/files/236/Clinger-Cohen_Act_of_1996.pdf) — mirrored: [`sources/clinger-cohen-act-1996.txt`](sources/clinger-cohen-act-1996.txt) | federal-86 | OK |
| [Cover Oregon](https://www.doj.state.or.us/wp-content/uploads/2017/06/FINAL_Complaint_8_22_14.pdf) — mirrored: [`sources/cover-oregon-doj-complaint-oracle.txt`](sources/cover-oregon-doj-complaint-oracle.txt) | federal-96 | OK |
| [Daytona Beach News-Journal](https://www.news-journalonline.com/story/news/2021/03/09/consulting-firm-deloitte-defends-firms-work-floridas-much-maligned-unemployment-system/6922197002/) — mirrored: [`sources/daytona-beach-news-journal-deloitte-connect.txt`](sources/daytona-beach-news-journal-deloitte-connect.txt) | federal-96 | Live; blocks automated checks |
| [DOAH Case 05-003144BID](http://flrules.elaws.us/doahcase/05-003144bid) | main, protest | OK |
| [DOL OIG press release, Apr. 27, 2026](https://oig.dol.gov/public/Press%20Releases/OIG-Press-Release-042726.htm) — mirrored: [`sources/dol-oig-press-release-042726.txt`](sources/dol-oig-press-release-042726.txt) | federal-96 | OK |
| [DOL OIG Report 19-23-008-03-315](https://www.oig.dol.gov/public/reports/oa/2023/19-23-008-03-315.pdf) — mirrored: [`sources/dol-oig-report-19-23-008-03-315.txt`](sources/dol-oig-report-19-23-008-03-315.txt) | federal-96 | OK |
| [Dwivedi et al., "IS/IT Project Failures: A Review of the Extant Literature for Deriving a Taxonomy of Failure Factors" (2013)](https://inria.hal.science/hal-01467815v1/document) | post-2000 | OK |
| [ERIC ED407606](https://files.eric.ed.gov/fulltext/ED407606.pdf) — mirrored: [`sources/eric-ed407606-family-transition-program.txt`](sources/eric-ed407606-family-transition-program.txt) | annals, topology | OK |
| [Florida Fiscal Portal](https://floridafiscalportal.state.fl.us/Document.aspx?ID=6166&DocType=PDF) — mirrored: [`sources/florida-fiscal-portal-nsrc-long-range-plan.txt`](sources/florida-fiscal-portal-nsrc-long-range-plan.txt) | topology | OK |
| [Florida Legislature, 1992 Summary of General Legislation](http://library.law.fsu.edu/Digital-Collections/FLSumGenLeg/FlSumGenLeg1992.pdf) — mirrored: [`sources/florida-legislature-1992-summary-general-legislation.txt`](sources/florida-legislature-1992-summary-general-legislation.txt) | topology | OK |
| [Florida Politics on the CIG findings](https://floridapolitics.com/archives/409408-connect-investigation-first-findings-deloitte-ran-insufficient-stress-testing/) | federal-96 | Live; blocks automated checks |
| [Florida TaxWatch, "It's Time to Reform Florida's Information Technology Procurement and Oversight" (January 2024)](https://thecapitolist.com/wp-content/uploads/2024/01/Its-Time-to-Reform-Floridas-Information-Technology-Procurement-and-Oversight.pdf) | annals, post-2000 | OK |
| [FOIA.gov](https://www.foia.gov) | requests | OK |
| [Guide for States](https://acf.gov/css/training-technical-assistance/automated-systems-child-support-enforcement-guide-states) | federal-86 | OK |
| [Heflin & Mueser (2010)](https://web.archive.org/web/20250809092014/https://cpr.uky.edu/sites/ukcpr/files/research-pdfs/DP2010-01_heflin_mueser.pdf) | post-2000 | OK |
| [House Ways & Means hearing, 1997](https://commdocs.house.gov/committees/ways/hwmw105-21.000/hwmw105-21_0.HTM) — mirrored: [`sources/house-ways-means-child-support-1997.txt`](sources/house-ways-means-child-support-1997.txt) | federal-86 | OK |
| [IBM Network Control Program](https://en.wikipedia.org/wiki/IBM_Network_Control_Program) — mirrored: [`sources/ibm-network-control-program-wikipedia.txt`](sources/ibm-network-control-program-wikipedia.txt) | capacity | OK |
| [IMS release history](https://www.edm2.com/index.php/IBM_Information_Management_System) | operating | OK |
| [In the Public Interest](https://www.inthepublicinterest.org/wp-content/uploads/flchild.pdf) — mirrored: [`sources/in-the-public-interest-florida-child-welfare-privatization.txt`](sources/in-the-public-interest-florida-child-welfare-privatization.txt) | post-2000 | OK |
| [Indiana v. IBM](https://caseclips.courts.in.gov/2016/03/24/state-v-ibm/) — mirrored: [`sources/indiana-v-ibm-supreme-court-2016.txt`](sources/indiana-v-ibm-supreme-court-2016.txt) | federal-96 | OK |
| [Industry Insider Florida on DCF's FY2025-26 LBR](https://web.archive.org/web/20251010101725/https://insider.govtech.com/florida/news/department-of-children-and-families-asks-for-74m-for-it) | annals, post-2000, topology | OK |
| [Leon County Clerk records page](https://leonclerk.com/helpful-resources/records/court-records/) | requests | OK |
| [Massachusetts](https://www.masslive.com/politics/2014/06/massachusetts_health_connector_3.html) — mirrored: [`sources/masslive-2014-massachusetts-health-connector-cgi.txt`](sources/masslive-2014-massachusetts-health-connector-cgi.txt) | federal-96 | Live; blocks automated checks |
| [Massachusetts State Auditor](https://www.mass.gov/doc/department-of-transitional-assistance-0/download) — mirrored: [`sources/massachusetts-state-auditor-2005-beacon-dta.txt`](sources/massachusetts-state-auditor-2005-beacon-dta.txt) | federal-86 | Live; blocks automated checks |
| [Michigan OAG 4359505](https://audgen.michigan.gov/finalpdfs/05_06/r4359505.pdf) — mirrored: [`sources/michigan-oag-micses-performance-audit-2006.txt`](sources/michigan-oag-micses-performance-audit-2006.txt) | federal-86 | OK |
| [Michigan Senate Fiscal Agency, 2003](https://sfa.senate.michigan.gov/Publications/Notes/2003Notes/NotesNovDec03cc.pdf) — mirrored: [`sources/michigan-senate-fiscal-agency-micses-2003.txt`](sources/michigan-senate-fiscal-agency-micses-2003.txt) | federal-86 | OK |
| [office page](https://www.carltonfields.com/offices/tallahassee) | carlton | OK |
| [Ohio AOS Clermont County, 2001](https://ohioauditor.gov/auditsearch/Reports/2001/clermont_child_support_enforcement_agency_performance_01-clermont.pdf) | federal-86 | OK |
| [Ohio AOS SETS, 1999](https://ohioauditor.gov/auditsearch/Reports/1999/statewide_setsimplementation_finalrpt.pdf) — mirrored: [`sources/ohio-aos-sets-implementation-1999.txt`](sources/ohio-aos-sets-implementation-1999.txt) | federal-86 | OK |
| [OPPAGA 08-13 (2008)](https://oppaga.fl.gov/Documents/Reports/08-13.pdf) — mirrored: [`sources/oppaga-08-13-access-2008.txt`](sources/oppaga-08-13-access-2008.txt) | post-2000 | OK |
| [records request page](https://leonclerk.com/helpful-resources/records/records-request/) | addendum | OK |
| [Rhode Island's UHIP](http://www.transparency.ri.gov/uhip/documents/assessments/UHIP%2030-day%20assessment.pdf) — mirrored: [`sources/rhode-island-uhip-30-day-assessment-2017.txt`](sources/rhode-island-uhip-30-day-assessment-2017.txt) | federal-96 | OK |
| [Tennessee TEDS](https://healthlaw.org/wp-content/uploads/2024/09/AMC-Case-Explainer.pdf) — mirrored: [`sources/tennessee-teds-amc-v-smith-case-explainer-2024.txt`](sources/tennessee-teds-amc-v-smith-case-explainer-2024.txt) | federal-96 | OK |
| [WFSU](https://news.wfsu.org/state-news/2021-03-08/inspector-general-report-injected-into-lawsuit-over-floridas-unemployment-system) — mirrored: [`sources/wfsu-2021-florida-unemployment-system-inspector-general.txt`](sources/wfsu-2021-florida-unemployment-system-inspector-general.txt) | federal-96 | OK |
| [WFTV 9 Investigates (2025)](https://www.wftv.com/news/9investigates/records-show-florida-knew-about-defects-application-portal-dcf-benefits/KYWKBCEGLBCXZOUIAN4F3U4SGM/) — mirrored: [`sources/wftv-2025-myaccess-portal-defects.txt`](sources/wftv-2025-myaccess-portal-defects.txt) | post-2000 | OK |
| [WUSF, June 26, 2026](https://www.wusf.org/politics-issues/2026-06-26/usda-releases-florida-snap-error-rate-comes-with-penalty) — mirrored: [`sources/wusf-2026-florida-snap-error-rate-penalty.txt`](sources/wusf-2026-florida-snap-error-rate-penalty.txt) | main | OK |
| [§ 205.38](https://www.govregs.com/regulations/expand/title45_chapterII_part205_section205.50) — mirrored: [`sources/45-cfr-205-govregs-adp-planning.txt`](sources/45-cfr-205-govregs-adp-planning.txt). **Citation note (found during mirroring, Aug. 19, 2026):** the URL slug reads "section205.50," but § 205.50 covers information safeguarding and is unrelated to the quoted implementation-plan language. That text is verbatim from **45 CFR § 205.37(a)(7)**, and the FFP match-rate structure this row is actually citing is set out in **§ 205.38** — both captured in full in the mirrored file. `FLORIDA-system-addendum-sources.md` should cite § 205.37(a)(7)/§ 205.38 directly rather than this govregs.com slug. | addendum | OK |

---

## Method

URLs were extracted from the fifteen published markdown files by pattern match, deduplicated, and checked with an automated HEAD request falling back to GET, using a desktop browser user-agent and a thirty-second timeout. Codes 403 and connection timeouts were treated as inconclusive rather than dead, because every such host in this set is a newspaper with bot protection and every one of them was confirmed reachable interactively during research. Only 404, 410, and 5xx responses were treated as failures, and each was investigated individually rather than swept into an archive link by default — two of the six turned out not to need an archive at all, one being a case-sensitivity error and one a publisher migration.

Link checking establishes that an address responds. It does not establish that the content at that address is the content that was cited. For the six repairs above the substituted documents were opened and confirmed to be the intended ones.
