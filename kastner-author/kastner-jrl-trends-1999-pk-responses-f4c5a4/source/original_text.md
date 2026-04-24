# JRL 1999 Trends List with Peter Kastner Responses

> Archived from: TRENDS-1-14.DOC
> Original publication date: 1999-01-01
> Author: Peter S. Kastner (annotations on JRL trend list)

---

## Original Document Text

SOURCE: TRENDS-1-14.DOC

﻿

JRL list of trends for 1999.  (And he needs your collated list for the HP sales training project asap as well as Joe needs it for a speech in the Bahamas.)

    1. Application Integration.  The very real need exists.  Data repositories/dictionaries have never worked — felt to be constraining.  The Crossworlds, Oberon, etc approach seems to be going nowhere — too complex to build and maintain as well as too restrictive.  The Data Warehouse approach as defined by our EBA group seems to be the best path in 1999.  Still needs architectural details worked out, but note that it allows for LOB integration as well as supply chain, if done correctly.  Good for integrating existing applications as well as integrating new applications such as data knowledge and even e-commerce.

PK Response:  right topic, wrong answer.  The data warehouse aproach is only good for looking at past business – real-time warehousing is cutting edge (and another potential topic).  The key EAI points are buy vs. build.  Crossworlds offers a handful of application-to-application solutions such as R/3 invoicing from remedy Help Desk CIS.  Oberon et al offer tool kits for EAI.  Real alternative is rolling your own with an object broker-based tool kit.  Why roll your own?  Because of the intricate and proprietary details of every enterprise’s processes.   Dark horse to watch is the ERP vendors who are moving out towards CIS and warehousing and into more depth in vertical market.

    2. Year 2000 Testing and Correcting Absorbs over 50% of IS staff.  JRL is very pessimistic regarding preparedness for Year 2000.  It seems that users are finding a significant number of bugs in code that has been scanned and supposedly corrected.  And JRL is not hearing of a lot of success in the testing phases of remediation.  Furthermore, users were lax in 1998 in testing supposedly Y2K-compliant replacement applications they had acquired from ISVs — their assumption is that it is safe because they were promised it would be.  Finally, users must test their interfaces with their trading partners — and JRL just do not see that happening, even with Y2K-compliant EDI.  (Yes, many have tested at the transport level, but Y2K test data is not going into the applications.)

PK response:  Arguing that the world is unprepared for Y2K is whistling in the dark.  This topic needs scenarios, more depth: when will IS realize the problem; will the remediation be in 2000 or 1999; what pressure/event will result in an IS epiphany; how can an IS dept. test ISV applications; will testing and correcting make a tangible difference vs. fail & remediate in 2000?

    3. Y2K Contingency Planning At the Business-Unit Level Becomes THE 3Q99 Drill for Global Business.  See 2 above.  The impact of preparedness will spread to business unit managers who will suddenly be expected to be smart on both business resumption contingency planning as well as how to use PCs and NT servers for managing their own business processes.  (Note, IS will be too busy to assist, as described in 2.)

PK response:  VERY interesting scenario.  It suggests the line business units are cut off from support by IS (likely) and must do with their existing LANs, Microsoft desktop Office97 suite and NT and Unix servers.  So, forget about installing Office 2000 (now delayed to Q2) or Windows 2000.  The contingency plan’s technology should be based on the workgroup’s capabilities because I refuse to plan for business systems without electricity.  Suggests three contingency approaches: a) systems and processes should be built around Microsoft’s VBA scripting and Office97 applications including Access and Outlook for work flow; b) Lotus Notes shops should build around Notes and Office97; c) there is probably an Intranet toolset but I need more research.

    4. Intel Will Have A Banner Year.  JRL believes that small-to-medium sized enterprises are planning to replace their PCs and LAN servers in mid-1999 to both meet their Y2K issues as well as replace DOS, Windows 3.1, and Windows 95 desktops as well as whatever older, hard to maintain servers are cluttering up their offices.  (“New Millenium, new information infrastructure, have to do so anyway because of Y2K problems, yadee-dadee-do.)  And these buyers are all going to want new PCs and servers in  3Q99  (best price/performance the later you wait.)  Note that we already see this trend in 4Q98 for G2000 decision makers — but JRL does not believe SME decision makers see the macro implications yet that they could all be trying to squeeze each other out at the same time.

PK response:  agree and have formally told Intel that this is our scenario.

    5. The #1 Company In Each Well-Defined Product Category Will Gain Market Share.  IS decision makers do not really have the time to evaluate options, they are increasingly believing that all products are about the same in a mature market so they might as well buy from the leader where possible, and there is a desire to lower risk (with Y2K pressures) in any acquisition.  So we can expect to see, for example, SAP, Oracle, Cisco, Compaq (NT servers), Sun, IBM and Dell increase market shares in their specific areas of dominance in 1999.  Not the year for the new entrant.

PK response:  a) let’s pick ten areas where new technology is driving new entrants and where the big guys aren’t yet playing; b) let’s name some likely (and unlikely) merger/acquisitions for 1999.  And don’t forget that stock price (e.g., Internet stock price mania) is not the measure of market success.

    6. G2000 Companies Will Switch Or Threaten To Switch Voice And Data Telecommunications Suppliers As Price Incentives and Service Promises Increase.  My sources tell me that AT&T, Worldcom/MCI, Sprint, British Telecom, and Cable and Wireless are cutting each other’s throats for overarching enterprise contracts.  But users are worried more about quality of service and support, especially for non-US communications, than price.

PK response: Tie this no-brainer to the mainframe market.  Amdahl, Hitachi, and IBM are equivalent, so IT gets very good very fast at negotiating best terms for an 18 month to 4 year period.  The hidden issue here is whether IS is prepared to managed shared (currently separate) telecomm facilities and deal with the shared bandwidth and QoS issues.  I say not ready.  So what are all the issues, Virginia?

    7. Sun Will Continue To Gain Market Share In the Enterprise Data Center.  For data center managers that must implement web-based applications Sun seems to be one of the only large beacons of intellectual ideas content emanating from the supplier community.  While HP may have higher-end servers and IBM better services, Sun’s enterprise application architectures and championing of JAVA puts it in the forefront of providing new technologies that data center managers must know about.

PK response:  Sun’s ascendancy is inevitable.  We should focus our analysis on where Sun is really good and where buyers should look elsewhere/where Sun can improve.  Secondary analysis (by Sloane and Fournier) is about the evolution of Sun’s software strategy, especially the server-side Internet-to-database stuff.

    8. Windows 2000 Will Not Be Quickly Adopted By Large Enterprises In 1999.  Between Y2K issues that must be addressed, inability of Microsoft to deliver Windows 2000 functionality as promised, and the need to have Windows 2000 on both the server and desktop to operate properly, it is highly likely that this will be regarded as one of Microsoft’s flops at the end of 1999.

PK response:  We have a new research report on this subject.  Note also that Office 2000 will arrive later than the expected Q1 and Office represents 40% of Microsoft’s profits.  The key feature of Office 2000 is the ability to move into and out of HTML – great for posting on an Intranet.

    9. After Enterprises Fix Y2K, They Will Use Their New and Improved Methodologies to Develop Web-based Applications.  It is obvious at this point that serious e-commerce applications require a roll-your-own approach — we are probably several years away from having production-quality ISV e-commerce applications that could handle an Amazon.com, Barnes and Noble, Egghead, Sharper Image, Dell, Cisco, Intel, IBM, General Motors, American Airlines, etc.  For those companies that followed best practices in Y2K remediation, they now have in place a structure for more effectively developing e-commerce applications than they did in the past plus, from contingency planning, a current, holistic view of their enterprise’s operations.  Putting it together, they will be in a better position than ever before to develop effective e-commerce applications.

PK response:  And Mr. Sakakeeny’s group will tell us all about next-generation, Intranet-based applications development while Mr. Alschuler will ponder building ever-more-powerful web commerce sites.
 

Peter extends John’s trends with a few of his own below
    10. Who owns security?
Security used to be one program on the mainframe.  Now, security issues are rampant as distributed systems create enormous complexity.  Further, TCP/IP, for all its benefits, opens enormous holes in any LAN or WAN environment.  Is this a problem solved by Line Of Business Managers or by the CIO?  Can it be solved?

    11. Is 1999 the Year of the Object?
After ten years in the marketplace, object-oriented development is most commonly found in supplier’s software products, not in IT applications.  In 1999, leading ERP suppliers and IBM’s San Francisco project will open a new era of objects for practical business use.

    12. Computing as just another utility service:  the ISPs take off
What are the dimensions, strategies, scenarios and segments of the development of the ISP business.  Are they just toll-takers on the Internet highway, or is there a long-term, sustainable business here?  Consolidation, hot niches, key products and services aimed at ISPs.  And, of course, will 1999 be the year of IP telephony?


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | kastner-jrl-trends-1999-pk-responses-f4c5a4 |
| title | JRL 1999 Trends List with Peter Kastner Responses |
| author | Peter S. Kastner (annotations on JRL trend list) |
| date | 1999-01-01 |
| type | annotated-trends-memo |
| subject_domain | 1999-it-trends-y2k-w2k-sun-intel-mainframe-internet |
| methodology | industry-analysis, contrarian-commentary, scenario-planning |
| source_file | TRENDS-1-14.DOC |
| license | CC-BY-4.0 |

### Abstract

Internal Aberdeen-era memo: a list of 9 trends for 1999 compiled by 'JRL' (John R. Logan, Aberdeen Group co-founder, partner, and board chairman) followed by detailed 'PK Response' annotations from Peter Kastner. Trends covered: application integration, Y2K remediation, Y2K contingency planning at the business-unit level, Intel banner year, #1-vendor market-share gains, telecom switching, Sun's enterprise data center ascendancy, Windows 2000 slow adoption, post-Y2K e-commerce. Kastner adds three extension trends: who owns security, the year of the object, and computing as a utility / ISP business. Primary-source artifact of Kastner thinking in 1999.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Primary-source Kastner thinking artifact in long-form annotation style — direct evidence of how Kastner reasoned about IT trends as Aberdeen Research Director in 1999, including extensions he added to colleagues' trend lists. |
| **Relevance** | medium | Specific 1999 forecasts are dated, but Kastner's 'Computing as utility / ISPs' extension trend foreshadowed cloud/SaaS by 5-10 years. Methodology of scenario-extension on top of trend lists remains useful. |
| **Prescience** | high | Multiple Kastner predictions validated: Sun's ascendancy was real (peaked ~2000); Office 2000/Win2K Q1 delays validated; security cross-cutting concern proved correct; 'Computing as utility service' foreshadowed AWS by ~7 years; Y2K remediation patterns proved largely correct (most fixed in 1999, not 2000). Bookkeeping: his agreement with the 'Intel banner year' SME-PC-replacement scenario was substantially validated by 2H1999 PC sales. |

### Prescience Detail


**Prediction 1:** PK Extension 12: computing as utility service via ISPs
- **Claimed:** What are the dimensions, strategies, scenarios and segments of the development of the ISP business? Are they just toll-takers on the Internet highway, or is there a long-term, sustainable business here? Consolidation, hot niches, key products and services aimed at ISPs. And, will 1999 be the year of IP telephony?
- **Year:** 1999
- **Confidence at time:** high


### Entities Referenced (25)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Peter S. Kastner | person | active |  |
| Aberdeen Group | firm | acquired | Harte-Hanks (2007); Spectrum Equity (2017) |
| John R. Logan (JRL) | person | active | Automated Compliance Solutions LLC (later venture) |
| Intel Corporation | company | active |  |
| Microsoft Corporation | company | active |  |
| Sun Microsystems | company | acquired | Oracle (2010) |
| Hewlett-Packard | company | split | HP Inc + HPE (2015) |
| IBM Corporation | company | active |  |
| Compaq Computer Corporation | company | acquired | Hewlett-Packard (2002, $25B) |
| Oracle Corporation | company | active |  |
| Cisco Systems | company | active |  |
| SAP AG | company | active |  |
| Dell Computer Corporation | company | active | now Dell Technologies |
| Amdahl Corporation | company | acquired | Fujitsu (1997) |
| Hitachi (computer division) | company | active |  |
| AT&T | company | active |  |
| WorldCom / MCI | company | dissolved | Bankruptcy 2002; Verizon (2006) |
| Sprint Corporation | company | acquired | T-Mobile US (2020) |
| British Telecom | company | active |  |
| Cable and Wireless | company | split | Vodafone (2012); Liberty Global (2016) |
| Lotus Development Corporation | company | acquired | IBM (1995) |
| Amazon.com | company | active |  |
| Crossworlds Software | company | acquired | IBM (2001) |
| Oberon Software | company | acquired | OnDisplay (Jan 2000, $181M stock swap); subsequently Vignette (2000), Open Text (2009) |
| Remedy Corporation | company | acquired | Peregrine (2001); BMC (2002) |

### Technologies Referenced (20)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Application Integration / EAI | discipline | industry | growth | evolved-to-ipaas |
| Data Warehouse | category | industry | mature | evolved-to-data-lakehouse |
| Real-Time Warehousing | discipline | industry | early | evolved-to-stream-processing |
| Y2K (Year 2000) Remediation | category | industry | peak | completed |
| Y2K Contingency Planning | discipline | industry | peak | completed |
| Windows 2000 | platform | Microsoft | pre-launch | obsolete |
| Microsoft Office 97 | application | Microsoft | mature | obsolete |
| Microsoft Office 2000 | application | Microsoft | pre-launch | obsolete |
| Microsoft VBA (Visual Basic for Applications) | language | Microsoft | mature | active |
| Microsoft Access | application | Microsoft | mature | active |
| Lotus Notes | platform | Lotus/IBM | mature | rebranded-HCL-Notes |
| Intranet | category | industry | growth-1999 | active |
| E-Commerce | category | industry | growth-1999 | ubiquitous |
| ISP / Internet Service Provider business | category | industry | growth-1999 | evolved-to-cloud |
| IP Telephony / VoIP | protocol | industry | early-1999 | ubiquitous |
| Object-Oriented Development | discipline | industry | mature-1999 | ubiquitous |
| IBM San Francisco Project | framework | IBM | growth-1999 | discontinued |
| ERP Systems (SAP/Oracle/PeopleSoft) | category | industry | mature | active |
| Enterprise IT Security | category | industry | growth-1999 | active |
| TCP/IP | protocol | industry | ubiquitous | ubiquitous |

### Observation Summary

- Total observations: 15
- By type: expert-opinion: 11, market-data: 2, viability-prediction: 1, biographical: 1
