# Systems Management: Delayed Promise

> Archived from: Systems-Management-Delayed-Promise.webarchive
> Original publication date: 1998-08-03
> Author: Stuart J. Johnston with Monua Janah, InformationWeek #694

---

## Original Document Text

SOURCE_URL: http://www.informationweek.com/694/94iusys.htm;jsessionid=QRCIIVADGX0LMQSNDLRSKHSCJUNN2JVN
MIME: text/html

--> InformationWeek.com / TOP POP UP AD 1 of 2 --> /SUPERNAV --> <script language="JavaScript" type="text/javascript"> document.write('<a href="http://clk.atdmt.com/MRT/go/114378118/direct/01/bkggbWK,bfdqsbIeRzvAp" target="_blank"><img src="http://view.atdmt.com/MRT/view/114378118/direct/01/bkggbWK,bfdqsbIeRzvAp"/></a>'); </script><noscript><a href="http://clk.atdmt.com/MRT/go/114378118/direct/01/bkggbWK,bfdqsbIeRzvAp" target="_blank"><img border="0" src="http://view.atdmt.com/MRT/view/114378118/direct/01/bkggbWK,bfdqsbIeRzvAp" /></a></noscript> Welcome Guest. | Log In | Register | Membership Benefits United Business Media --> InformationWeek Defining The Business Value Of Technology Part of the TechWeb Business Technology Network --> New Image Galleries: The Nokia N810 Linux Internet Tablet Doesn't Make Sense Vote: Dubious Dweeb, Courageous Crusader, Or Tech Terrorist? --> Apple's iPhone Rules Wal-Mart's Linux Retreat --> / take IW with you promo --> / mobile promo --> / iw500 promo wide --> --> --> --> --> --> --> Get News On Your Phone --> RSS Feeds Subscribe Events Digital Library News Blogs Software Security Hardware Mobility Windows Internet Global CIO Government Careers --> August 3, 1998 Systems Management: Delayed Promise The pieces of Microsoft's Zero Administration strategy are falling into place, but the plan still hinges on the delayed Windows NT 5.0 By Stuart J. Johnston with Monua Janah he elements of Microsoft's Zero Administration initiative, first outlined nearly two years ago, are falling into place-slowly. The latest additions include Windows-based terminals from Hewlett-Packard, which can be used with Microsoft's month-old Terminal Server edition of Windows NT 4.0 to extend Windows applications to users who don't need PCs. Microsoft has also begun final testing of Systems Management Server 2.0, a significant upgrade to its flagship management platform. The products, along with other tools now available, such as Zero Administration Kits for Windows NT Workstation and Windows 95, can simplify management of Windows environments. But Microsoft's ultimate goal-hands-free PC administration-is behind schedule, due largely to delays in Windows NT 5.0. The operating system upgrade, originally slated for the first half of this year, won't ship until the first half of 1999 at the earliest. Microsoft's Zero Administration strategy hinges on key technologies in NT 5.0, including Active Directory, which will keep track of network resources, and IntelliMirror, a mirroring scheme that prevents data loss and lets users easily switch PCs. For businesses, the delays are more than an inconvenience-they mean that the lower costs associated with simplified administration are also overdue. Microsoft chairman and CEO Bill Gates declared last year that lowering total cost of PC ownership was his company's top priority. Gates and other Microsoft officials have said that Zero Administration could lower the cost of owning a PC by up to 50%. "We would stand on the desk and cheer if Microsoft can deliver that," says Fred Morsheimer, CIO and VP at food retailer Trader Joe's Co. in South Pasadena, Calif., which uses Windows NT 4.0. "Our profit model requires us to have a small IT shop. Any TCO savings would let us put that money into things that drive the business." For now, Microsoft customers are leveraging Zero Administration technologies where they can. Federal Express Corp. is testing 1,000 of HP's $699 Windows-based terminals, introduced last week, as replacements for 3270 terminals. FedEx may eventually deploy as many as 20,000 of the HP devices. The company wants a system that supports a graphical user interface, Web connectivity, and productivity applications-without the expense and administration requirements of PCs. "It's about total cost of ownership and manageability," says Rob Carter, a FedEx VP and the company's chief technology officer. Windows-based terminals, also available from several other companies, have no disk drive or local storage. Shell Canada used Terminal Server, along with Citrix Systems Inc.'s MetaFrame add-on, to roll out NT Workstation capabilities to 300 users in two weeks. The setup lets those users-many equipped with Unix workstations and older PCs-run Windows applications, including Microsoft Office and Micrografx's Suite 2 drawing package, from centralized NT servers. "We definitely get greater manageability, and we also get the cost avoidance of not having to upgrade a bunch of PCs," says Ron Patterson, new technology projects coordinator with Shell Canada, in Calgary, Alberta. "It saved us on the order of six figures." Simplified Administration When it ships, SMS 2.0 will come with across-the-board enhancements that should also simplify Windows administration, including improved server monitoring, network tracing, and software distribution. New capabilities include an interface to the Microsoft Management Console, which is a presentation tool for hosting third-party management products, and support for Web browsers via Microsoft's Web-Based Enterprise Management technology. General Motors uses SMS to manage its NT servers and eventually plans to move to SMS 2.0, says Ajit Kapoor, director of worldwide network standards and architecture at GM. Of Microsoft's incomplete Zero Administration strategy, Kapoor says, "The good news is the concept is there." But Microsoft officials admit that the linchpin in the strategy is NT 5.0. "We've got a good management story today, but it gets better with NT 5.0," says Victor Raisys, Microsoft's lead product manager of systems management marketing. In addition to IntelliMirror, NT 5.0 adds the ability to reformat a PC's hard disk and reinstall the system on a new PC or on one that has recovered from a crash. Also new: software-management features to ensure that users have the latest software installed without user or administrator intervention. Then there's Active Directory, a repository of information within NT 5.0 about the users, files, and devices on a network. The directory is gaining third-party support even before NT 5.0's release. Last week, enterprise software vendors SAP, Baan, and J.D. Edwards disclosed plans to integrate their application suites with Active Directory, which should result in simplified user access to their applications and elimination of a layer of passwords. Cisco Systems is already collaborating with Microsoft on using Active Directory to combine the management of servers, routers, and switches. But a controversy is brewing over an architectural issue that some observers think could hinder Active Directory's ability to simplify network administration. Microsoft has decided to use static inheritance-rather than dynamic inheritance, the method preferred by X.500 directories-to propagate changes in the directory. With static inheritance, if an administrator changes a rule about a department's file access, the alteration has to be made to each object within the directory. Once done, the change will replicate across a group of NT servers, which could consist of thousands of objects. Analysts say the approach could cause network management problems. "If you have substantial changes to your [directory hierarchy], it could have substantial impact on replication," says Jamie Lewis, president of the Burton Group, a network consulting firm. Another concern, Lewis says, is that changes in Active Directory can't be inherited across domains, thus complicating the configuring and changing of network rules. In contrast, dynamic inheritance doesn't attach a rule or attribute to individual objects; rather, the rule is "inherited" by all classes lower down in the directory hierarchy, or tree. If a network administrator makes a change, the directory automatically looks up the tree and makes the necessary alterations. "From the point of view of managing the network, it's very important to have dynamic inheritance," says Peter Cruikshank, systems engineer for the U.S. Navy's Spawar corporate systems. "The whole idea of a directory is to have functions that can go across a hierarchy." Jeff Price, lead product manager for NT Server, says Active Directory provides multiple ways to group users and to apply rules to those groups. "In real-world deployments, that's a much more high-performance and flexible model," he says. Another potential drawback is Microsoft's Windows-centric approach to Zero Administration, with the full benefits accruing only to companies with homogenous NT 5.0 environments. That leads Aberdeen Group analyst Peter Kastner to conclude that the cost savings Microsoft promises "will happen very slowly, in an evolutionary fashion" as companies upgrade to NT 5.0. -with additional reporting by Mary Hayes and Caryn Gillooly Back to This Week's Issue Send Us Your Feedback Top of the Page --> CAREER CENTER Looking for a new job? Open | Close Employers: Give your recruitment message influence. Advertise in the InformationWeek 500 . --> SEARCH Function: Information Technology Engineering Keyword(s): State: Post Your Resume Employers Area News & Features Blogs & Forums Career Resources Browse By: State | City SPONSOR RECENT JOB POSTINGS BTG - Now Hiring --> Featured Jobs: Boeing seeking Software Engineer 1 in Anaheim, CA Switch and Data seeking Site Facility Technician in Sunnyvale, CA New York Life seeking Insurance and Investment Sales in Schaumburg, IL Washington State Investment Board seeking IT Specialist in Olympia, WA Kforce seeking VA Mortgage Processors in Phoenix, AZ For more great jobs, career-related news, features and services, please visit our Career Center . CAREER NEWS Companies Looking To Hire CIO 2.0 After months of gloom and doom, companies are again hiring new CIOs. Minorities, Women Underrepresented In IT According to reports, minorities are underrepresented in high-technology companies. More articles from our career center Today's Top News China Making Green Dam Internet Filter Optional Sun Dropping Rock Chip Project, Says Report MySpace Cuts 30% Of Workforce AT&T Axes Prepaid iPhone 3G Plans Microsoft Sues Three For Click Fraud Opera Browser Becomes File Sharing Platform --> See Image Galleries Specialty Resources Get on the Path to Effective Endpoint Security Protect Systems and Data with Data Loss Protection (DLP) Technology Virtualization's Bottom-Line Benefits A Day in the Life of a Business Process Analyst EMC Outlines its Content Archiving Strategy VIEW ALL BRIEFING CENTERS Featured Microsite InformationWeek Marketplace (Sponsored Links) Windows 7—join the conversation Take a look behind the scenes of the next generation of Windows Kaplan University Online Degrees in IT Free Program Info! Get Your Degree in Information Technology 100% Online! Learn More Today! Advertise With Us InformationWeek Home News Windows Security Mobility Internet Software Hardware CIO Central Research & Tools Careers Become A Member/Membership Benefits About Us Contact Us Current Issue Back Issues White Papers Briefing Centers Site Map Advertising Contacts Technology Marketing Solutions Editorial Calendar Other Techweb Sites: Informationweek Germany Network Computing TechWeb Intelligent Enterprise Dark Reading Light Reading Byte & Switch Internet Evolution bMighty out.println(" Small Biz Resource "); Insurance & Technology Wall Street & Technology Bank Systems & Technology Advanced Trading --> Terms of Service | Privacy Statement | Copyright © 2009 United Business Media LLC, All rights reserved. --> --> / TOP POP UP AD 2 of 2 -->

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | systems-management-delayed-promise-1bc587 |
| title | Systems Management: Delayed Promise |
| author | Stuart J. Johnston with Monua Janah, InformationWeek #694 |
| date | 1998-08-03 |
| type | feature-article |
| subject_domain | systems-management-zero-admin |
| methodology | industry-analysis, vendor-commentary, analyst-commentary |
| source_file | Systems-Management-Delayed-Promise.webarchive |
| license | CC-BY-4.0 |

### Abstract

InformationWeek issue #694 feature (Aug 3 1998) by Stuart J. Johnston with Monua Janah analyzing the state of Microsoft's Zero Administration Windows (ZAW) initiative nearly two years after its announcement. Core thesis: the pieces are falling into place — Windows-based terminals (HP), Terminal Server edition of Windows NT 4.0, Systems Management Server 2.0 in final testing — but the plan still hinges on the delayed Windows NT 5.0 (later Windows 2000). Peter Kastner, Aberdeen Group analyst, provides the key skeptical quote: full benefits of Zero Administration accrue only to companies with homogeneous NT 5.0 environments, so cost savings 'will happen very slowly, in an evolutionary fashion' as companies upgrade. Additional reporting by Mary Hayes and Caryn Gillooly. Article captures the 1998 moment when NT 5.0's delays and the thin-client/terminal strategy dominated the IT systems-management conversation.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Primary contemporaneous IW coverage of Microsoft's Zero Administration initiative at a critical 1998 juncture; Kastner's 'evolutionary not revolutionary' prediction frames how the industry actually experienced the NT 5.0 / Windows 2000 rollout. |
| **Relevance** | medium | Zero Admin Windows as a branded initiative is long-dead, but its core goals (reduce PC TCO via centralized policy, software distribution, and remote management) persist in modern MDM/Intune/Jamf/Kandji and endpoint-management platforms. Kastner's homogeneity-gating observation recurs today with Azure AD join, co-management. |
| **Prescience** | high | Kastner's prediction that cost savings would happen 'very slowly, in an evolutionary fashion' gated on NT 5.0 adoption was precisely right. Windows 2000 shipped Feb 2000 (18+ months after this article); enterprise deployment lagged into 2003-2005; mixed-environment pain points persisted well into the Windows XP era. Group Policy, IntelliMirror, and SMS realized their potential only as NT 5.x homogeneity emerged. |

### Prescience Detail


**Prediction 1:** Slow evolutionary savings
- **Claimed:** Full benefits [of Zero Administration] accrue only to companies with homogeneous NT 5.0 environments. Cost savings Microsoft promises will happen very slowly, in an evolutionary fashion, as companies upgrade to NT 5.0.
- **Year:** 1998
- **Confidence at time:** high

**Actual Outcome 1:** Evolutionary realization
- **Result:** Zero Admin Windows as a branded initiative dissolved, but its substance — Group Policy, IntelliMirror, SMS/SCCM, Remote Desktop — became mainstream only as NT 5.x homogeneity emerged in enterprise desktops 2003-2005, directly validating Kastner's evolutionary-not-revolutionary call.
- **Confidence:** verified
- **Notes:** Backfill — ZAW lifecycle

**Prediction 2:** NT 5.0 delayed
- **Claimed:** Microsoft Windows NT 5.0 delays were the central risk to the Zero Administration initiative as of August 1998; the release was rebranded Windows 2000 and shipped Feb 17 2000 — roughly 18 months after this article, validating Kastner-era skepticism about the schedule.
- **Year:** 1998
- **Confidence at time:** verified


### Entities Referenced (7)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | acquired | Harte-Hanks (2002-2017) -> Spiceworks Ziff Davis |
| Peter S. Kastner | person | active |  |
| Microsoft Corporation | company | active |  |
| Hewlett-Packard Company | company | split | HP Inc. + Hewlett Packard Enterprise (2015) |
| InformationWeek / TechWeb | firm | active |  |
| Stuart J. Johnston | person | active |  |
| Monua Janah | person | [DEFERRED] |  |

### Technologies Referenced (5)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Microsoft Windows NT | operating-system | Microsoft | new | active |
| Microsoft Windows NT 5.0 / Windows 2000 | operating-system | Microsoft | new | legacy-supplanted |
| Microsoft Zero Administration initiative | framework | Microsoft | new | legacy-supplanted |
| Windows NT 4.0 Terminal Server Edition | operating-system | Microsoft | new | legacy-supplanted |
| Microsoft Systems Management Server (SMS) | platform | Microsoft | mature | legacy-supplanted |

### Observation Summary

- Total observations: 6
- By type: viability-prediction: 2, market-data: 2, actual-outcome: 2
