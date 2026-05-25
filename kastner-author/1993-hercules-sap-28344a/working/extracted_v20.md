June 16, 1993 

Mr. William Phile Hercules, Inc. CSD Building 8145 500 Hercules Road Wilmington DE 19808-1599 

Dear Bill, 

It was a pleasure to meet with you and other Hercules executives at your facility in Wilmington last Friday.  Based upon that discussion and the background 48-page report Aberdeen prepared for that meeting, Risc, Unix, and the Major Multiuser Commercial Suppliers, June 11, 1993, Aberdeen has prepared this summary report. 

## Executive Summary 

Hercules has decided to implement SAP's R3 application software modules to run its core, mission-critical applications.  SAP R3 will use Oracle 6 as the back-end RDBMS (relational database management system).  SAP will support the running of R3 on multiuser Risc/Unix systems from Digital Equipment Corporation (DEC), Hewlett-Packard (HP), and IBM. 

Aberdeen's assignment was to recommend which of the three hardware suppliers should be designated as the preferred supplier and why. 

Based upon Hercules' requirements and both the current status and future directions of the three suppliers under consideration for the implementation of commercial, multiuser Risc/Unix systems, Aberdeen recommends that Hercules implement SAP R3 on the HP 9000 Series 800. 

In addition, Aberdeen strongly recommends that before SAP R3 is distributed to the plant locations Hercules implement a third-tier of computing systems in Wilmington to provide the backup, recovery, network management, and corporate analytical services that are necessary for running a production-quality enterprise-wide information network. 

## Aberdeen Background 

Aberdeen Group, a market research and consulting firm, has considerable experience in helping enterprises implement new computing topologies to meet new and changing  business realities.  Aberdeen Group was a pioneer in helping Fortune 500 enterprises move applications off the mainframe before terms such as downsizing, mainframe alternatives, and client-server were made popular by suppliers and the trade press. 

Aberdeen Group has closely monitored the multiuser, commercial Risc/Unix market since 1990 and is considered to be the authority on worldwide size and market share statistics. 

As one of the top market research firms in the U.S., Aberdeen has had several research meetings with SAP over the last two years. 

## Aberdeen Summary of SAP R3 Status 

SAP has had tremendous success recently in the process manufacturing industry with large enterprises.  Aberdeen has met with several such organizations that are replacing their current accounting and management control applications with SAP's R3 product suite to increase operational effectiveness. 

SAP R2 was successful on the mainframe both because of the business logic incorporated in its application algorithms and the fast throughput capability of its custom database. 

However, the SAP installed customer base began demanding that SAP provide a set of products that provided the same R2 functionality but could run on much less expensive multiuser platforms.  SAP's response was to announce they would begin developing R3 to be the portable equivalent of R2 but running on midrange Unix platforms.  SAP's original product rollout schedule intended for all R3 modules to be completed by mid-1994. 

However, rewriting SAP's proprietary mainframe databases to run on midrange Unix systems was impractical. Therefore, SAP has chosen the Oracle RDBMS to be the back-end database engine.  (Note that Software AG's 

ADABAS is an alternative option for those that need higher performance.)  Aberdeen has not reviewed what modifications SAP has made to its Oracle interface and what procedures Hercules will need to follow to integrate non-SAP R3 applications into the tightly coupled SAP R3 Oracle target database, including those applications that also use other Oracle databases.  Oracle offers Oracle SQL*NET to provide this functionality and Hercules needs to be prepared to take advantage of this capability if it is possible. Page 

June 16, 1993 

Mr. William Phile -- Hercules, Inc. 

The original targeted hardware platform for SAP's rewrite (commonly described as a redevelopment) to meet users computer downsizing requirements was the HP 9000 Series 800.  And Aberdeen would note that Oracle uses the HP 9000 Series 800 as its Unix reference port. 

Aberdeen understands that SAP is in the process of developing R4 as its next generation of client-server software to take full advantage of the power available in single-user desktop computers such as PCs. 

For flexibility reasons, it is most likely that R3 can be spread over multiple multiuser systems — a front-end application engine and a back-end dedicated RDBMS system.  While this is client-server by many definitions, especially software technologists, it is not client-server in terms that it takes full advantage of the users PC to run application code or sub-domains of the database. 

## Central IS Functions 

To determine the appropriate platform to meet Hercules' needs, Aberdeen asked which functions would be the responsibility of Hercules' central IS staff in the future. However, Aberdeen was told that Hercules is planning to move to a two-tier architecture by 1Q96 with minimal or no ongoing central IS coordination. 

It is Aberdeen's experience that a two-tier architecture is inappropriate for enterprises with a requirement for 

distributed computing — a point that was made very evident when IBM first endorsed two-tier in 1987 as a cornerstone of its now failed Systems Application Architecture (SAA). 

The two-tier topology has two fatal flaws.  First, it will not allow Hercules' corporate executives access to consolidated data that is maintained with integrity. Second, important operations services, such as backup, recovery, security, and data consistency are impossible to provide. 

Aberdeen suggests that Hercules consider implementing a tree-tier plus architecture as described in the report provided on June 11 in order to provide the necessary consolidation and analytical services as well as to be able to provide the data integrity services that become so necessary when a component (hardware, software, or communications) in the information network fails. 

Finally, Aberdeen's research shows that in enterprises similar to Hercules that distribute applications and data to remote locations, there is still a requirement for central IS to supply five essential coordination services — application/information architecture, network management, data management, operational services, and development methods and tools. 

Criteria for Selecting Hardware Platform 

Aberdeen interviewed Hercules IS executives regarding their requirements for both the supplier and platform on which SAP R3 would operate.  We believe the following criteria are listed in relative priority order.  Aberdeen believes that this criteria is not that much different from other enterprises comparable in size to Hercules that are also redeploying applications off the mainframe. 

Breadth of product line — Aberdeen understands that neither SAP nor Hercules are able to determine the size of the individual Risc/Unix platforms that will be used to run R3 at specific locations.  In addition, it has been Aberdeen's experience that when applications such as SAP R3 with Oracle are put in place that allow operational managers to much more easily obtain the specific 

information they require, throughput rates increase at 30%40% per year for the first three years after initial installation.  Therefore it is extremely important that any platform decision provide maximum growth path and that the suppliers' offering provide as much performance and expansion capability as possible. 

Supplier experience — Hercules does not know what it does not know about implementing mission-critical applications in a distributed topology.  Successful supplier experience and commitment, typically measured in market share and reported by references, will help facilitate the implementation process. 

Stable, robust, extensible Unix operating environment — Hercules will need a stable Unix operating systems that has functionality and middleware beyond the basic Unix standards to provide a production operating environment. This is especially important in the area of networking and communications support — including network management functionality. 

Upgradeable Risc processor technology — To ensure that Hercules captures the 50%+ performance advantages that Risc processors promise, Hercules will want to select a supplier whose Risc technology has proven itself in the past and has the basis for improvement in the future. 

ISV support — While SAP R3 may be the primary application to run on the new multiuser Risc/Unix systems, Hercules must also move other functions off the mainframe if it is to achieve its goal of removing the mainframe by 1Q96.  And to meet this goal in the most economical way, Hercules will both buy ISV (independent software vendor) application packages like SAP R3 and develop custom application programs with advanced application development tools — most likely tools that can take advantage of the Oracle RDBMS engine. 

Supplier Decision Will Be Winner-Take-All 

Before reviewing the individual supplier's relative positions — both current and future — against the above criteria, it is 

important that Hercules management understand that this will be a winner-take-all choice. 

While many in the industry have portrayed Unix-based systems as a commodity item that can be mixedandmatched on an enterprise network, the pragmatic reality is that this is a goal that is still two-to-four years away.  This has been proven by the history of enterprises that have acquired Risc/Unix workstations who have bitterly complained that they were promised commodity systems and that they could mix platforms from different vendors on a network.  But the reality has been that each individual network of workstations is composed of workstations from a single vendor and is managed with the vendor's own network management software. 

The same lesson has been learned by buyers of multiuser Unix systems.  But for multiuser systems, the problem is aggravated even more because of the reliance on the functionality that is built in above the basic Unix standard calls.  At the workstation level, application software can hide many of the variations among different 

Unixderivatives.  But while applications may be portable among multiuser Risc/Unix systems, each supplier's Unix is different in terms of ability to provide failure recovery, data integrity, performance monitoring, security, etc.  And the middleware written above Unix and compiler technology is very different from each supplier.  Therefore, enterprises do not simply look at DEC's OSF1, IBM's AIX 3.2, and HPUX as commodities that can be mixed-andmatched for the same application. 

As a result, large buyers spend considerable time testing and evaluating the various suppliers' offerings and then commit to acquiring only one.  Not only does this make remote network management practical, it also lowers staff training expenses (fewer systems to learn and possibilities to be confused about the subtle but important differences), and lowers on-going operational costs. 

Therefore, Aberdeen believes that Hercules should not take the criteria selection lightly for running SAP R3 in the belief that if one vendor does not live up to its expectations it can easily buy "commodity" Unix systems from another. 

Aberdeen believes that Hercules will be committed to but one of the hardware suppliers under consideration for the next 3-5 years if it makes its selection in June 1993. 

## Summary Review of DEC 

DEC has now re-entered the multiuser Unix market for the fifth time in the last five years with its Alpha/OSF1 offering. While the Alpha/OSF1 product line was supposedly shipped in March of this year, Aberdeen has found that ISVs and earlier adopters still consider it to be a beta version — not yet ready for production implementation.  As a proof point, Aberdeen would note that DEC normally releases TPC-A benchmark results with new multiuser systems — Alpha/OSF1 TPC-A results have not yet been announced although they are promised to be made available at the end of June. 

In addition, at the corporate level DEC has consistently over the last two years told Aberdeen Group that its primary operating system for multiuser production computing will be OpenVMS — not OSF1. 

Reviewing DEC's Alpha/OSF1 product line by what we believe to be the five primary criteria Hercules should consider: 

Breadth of product line — While Alpha/OSF1 has been implemented on the DECstation 300 workstations and servers up through the DEC 4000 AXP, 7000 AXP, and 10000 AXP multiuser systems, it has done so only in a uniprocessor operational mode.  As a result, it realistically only runs on three multiuser systems and without SMP (symmetric multiprocessing) capability has limited growth capability for large Hercules installations.  Simply put, if any Hercules SAP R3 installation requires more processing capability than the single processor DEC 10000 AXP could provide, the entire implementation could be in jeopardy. 

Supplier experience — DEC's support organization has either no or very limited experience in implementing OSF1 on Alpha.  And due to Digital's withdrawal of major Unix initiatives in the past for VAX/Ultrix, MIPS/Ultrix, VAX/Unix 

SVR4, and Intel/SCO, Aberdeen doubts that there is strong Digital expertise available for multiuser Unix. 

Stable Unix operating environment — Of all the members of the Open Software Foundation, only Digital has chosen to productize OSF1.  The other members have deemed OSF1 deficient in functionality — an action that has caused a conciliation between OSF and its one-time rival, Unix International.  And since OSF1 from Digital has only been generally available on multiuser systems since March and workstations since May, there are very few add-on middleware products available to make it production ready. As a result, OSF1 fails Aberdeen's test for stability when looking at a bet-your company production decision. 

Upgradeable Risc processor Technology — Alpha was originally to be available in a 200 MHz version.  However, production yields have been mostly for 133 MHz and 150 MHz —  Digital still has not been able to produce production quantities of the 200 MHz Alpha processor. And because today's Alpha processor is the first implementation of this technology, Digital has not yet shown if it can implement a next-generation Alpha with advanced silicon techniques.  Because of the relatively high clock rates designed in Alpha and the lack of a major second source, next-generation Alpha processors will be a major engineering challenge for DEC. 

ISV support — As a major supplier with a large installed customer base, many ISVs have proclaimed that they will support Alpha/OSF1 for both workstation and multiuser applications.  As of March, DEC counted 550 applications that ISVs such as SAP and Oracle have stated will be ported.  However, Aberdeen's interviews with ISVs indicates that multiuser Alpha/OSF1 support will not be a major priority unless there is widespread user demand — and they have not uncovered such tremendous demand to date. 

Conclusion — Aberdeen strongly recommends that Hercules not select DEC as the supplier of choice for multiuser Risc/Unix systems on which to operate SAP R3. 

Summary Review of IBM 

With a 1992 market share of 15%, IBM is the second largest supplier of multiuser Risc/Unix systems.  However, according to IBM, the majority of its 1992 multiuser Risc/ Unix systems sales were to small-to-medium sized enterprises and supported by value-added resellers. 

However, in 1993 IBM has been increasing its emphasis on direct sales of its RS/6000 product line to large enterprises such as Hercules. 

Breadth of product line — IBM has a relatively broad range of uniprocessor RS/6000s but no high-end SMP capability. The RS/6000 is sold in two different packages, the 200/300/500 which can be attached to a LAN and have limited expansion capability (the same package is intended to be either a workstation or multiuser system) and the model 900 which is rack-mounted and has greater expansion capability.  The most popular RS/6000s for multiuser computing have been the model 500s. 

Supplier experience — IBM's own experience with commercial, multiuser Risc/Unix is dependent upon local direction.  In general, IBM itself has sold the RS/6000 in a workstation and server topology for applications such as compute intensive trading room operations.  Aberdeen does not believe IBM has as much experience in implementing RS/6000s with timesharing applications such as SAP R3 — such timesharing applications have traditionally been implemented by IBM either on mainframes or AS/400s.  However, numerous ISVs, valueadded resellers and systems integrators may have the experience Hercules will require. 

Stable Unix operating environment — IBM's 

implementation of Unix, AIX 3.2, has not shown itself to be highly stable according to user reports.  Aberdeen believes that this is a major reason why so few large enterprises have deployed large numbers of RS/6000s and why originally IBM-dedicated value-added resellers such as FileNet and Wang have chosen to add competitive product lines.  To address the issue of stability and robustness, IBM has created a new development center for AIX in Toronto to replace the original efforts out of Austin. Aberdeen expects to see a more stable and robust version 

of AIX, AIX/6000, emerge from this effort before the end of 1993. 

Upgradeable Risc processor technology — IBM's current RS/6000 processor is called RIOS.  However, due to technical issues involved in implementing RIOS in large SMP systems and powerful low-priced systems, IBM has publicized its intentions to migrate its entire product line — PCs, RS/6000, AS/400, and even mainframes — to the PowerPC 600 (sometimes referred to as RIOS 2) processor family that it is developing in conjunction with Apple and Motorola.  From a technology perspective, this also implies a major change in the operating environment, including operating system (hence AIX/6000) and new compilers being developed in Toronto.  The bottom line is that Aberdeen believes that the end of the current RIOS processor is in sight and the new PowerPC 600 family of processors for multiuser systems is not yet released and in production for evaluation purposes. 

ISV support — IBM's RS/6000 is the platform that ISVs support for multiuser, commercial applications after they are released on the HP 9000 Series 800.  Hercules will find no deficiency in ISV support for the RS/6000 today. 

Conclusion — The RS/6000 is a viable platform on which Hercules could run SAP R3 but there are several deficiencies that make it a relatively poor choice in comparison to the HP 9000 Series 800. 

## Summary Review of HP 

HP is the market leader in multiuser, commercial Risc/Unix systems with a 1992 market share of 45+%.  With continuing new account wins for multiple system sales in large enterprises, HP claims a 1993 growth rate for its HP 9000 of over 40%. 

Breadth of product line — HP has the broadest product line and is the only supplier with both high-end and midrange SMP.  In addition, its midrange product line has been designed to provide buyer granularity by processor speed versus expansion slots.  TPC-A benchmarks indicate that the HP 890-400 has more throughput capability than Hercules' current 3090-200. (IBM will not run TPC-A tests 

on the 3090 line.)   Therefore, no matter what size system is required, no matter how large, HP should be able to meet Hercules' needs.  Aberdeen believes this is of critical importance when SAP is not able to accurately size the systems Hercules will require. 

Supplier experience — HP is fully committed to Risc and Unix and has the longest history of any of the suppliers being considered.  HP's Professional Services Organization (PSO) claims that it is the world's largest supplier of Unix-related and open systems services. Aberdeen would not disagree with this statement although it believes that the quality of services provided could be greater and the breadth broader. 

Stable Unix operating environment — While no Unix operating environment can yet match the stability of proprietary operating systems, HP-UX is reported to be in the top tier for stability.  More importantly, HP has led the industry in providing desirable extensions to Unix such as OpenView that is has then made available to other suppliers such as IBM to accelerate the rate of acceptance of a stable Unix environment. 

Upgradeable Risc processor Technology — HP has gone through seven generations of PA-Risc implementations to date.  While HP is concentrating on midrange implementations, Hitachi is developing next-generation high-end PA-Risc processors and Samsung low-end processors.  If there is any drawback to HP's Risc processor technology, it is that more emphasis has been placed on floating point performance to meet the needs of compute intensive workstation users than on integer performance for database processing requirements.  Yet even with this drawback, the high-end 800 series systems TPC-A results are the highest in the industry. 

ISV support — HP is the Risc/Unix reference port for both SAP and Oracle as well as the majority of ISVs who sell into the multiuser Unix marketplace.  And it is Oracle's most important multiuser platform in terms of revenue generated. 

Conclusion —  At this time, Aberdeen would have to strongly recommend that Hercules acquire its Risc/Unix systems to run SAP R3 from HP.  And due to the network management, training, and operational issues discussed earlier, Hercules should be prepared to acquire all the multiuser systems its anticipates implementing SAP R3 on in 1993 and 1994 from HP. 

## Conclusion 

Aberdeen Group believes that Hercules is making an excellent decision in migrating from its mainframe to distributed multiuser Risc/Unix systems running SAP R3. 

Based upon the Risc/Unix suppliers current product offerings, marketplace acceptance, and experience and what we believe to be Hercules' need to come up the learning curve on how to implement, manage, and expand the use of its next-generation enterprise-wide information systems, Aberdeen recommends that Hercules designate Hewlett-Packard as its sole supplier for the SAP R3 program. 

If you have any questions regarding our analysis or conclusions as stated above, please do not hesitate to contact Peter Kastner or me. 

With warm regards, 

John R. Logan Vice President 

## **2024 Metadata** 

### 1. Concise Summary of the Findings in the Document 

The document is a summary report prepared by Aberdeen Group for Hercules, Inc., recommending the implementation of SAP R3 application software modules 

on HP 9000 Series 800 multiuser RISC/Unix systems. The report evaluates three hardware suppliers—Digital Equipment Corporation (DEC), IBM, and Hewlett-Packard (HP)—and concludes that HP is the best choice based on criteria such as product line breadth, supplier experience, Unix operating environment stability, RISC processor technology, and ISV support. The report also advises Hercules to implement a third-tier computing system for backup, recovery, network management, and corporate analytical services. 

### 2. Summary of How Computer Technology Buyers Should React to the Document 

Computer technology buyers should consider the following actions based on the document's recommendations: 

- Prioritize selecting a hardware supplier with a broad and scalable product line to accommodate future growth. 

- Choose a supplier with proven experience and commitment to RISC/Unix systems to ensure smooth implementation and support. 

- Ensure the selected Unix operating environment is stable and robust, with necessary middleware for production readiness. 

- Opt for a supplier with a track record of upgradable RISC processor technology to leverage performance improvements. 

- Evaluate ISV support to ensure compatibility with essential applications like SAP R3 and other missioncritical software. 

### 3. Analysis of the Technology Discussed in the Document and Its Relation to Mainstream Computing in 2024 

The document discusses the transition from mainframe to distributed multiuser RISC/Unix systems, highlighting the importance of scalability, stability, and supplier experience. In 2024, mainstream computing has evolved significantly, with cloud computing and virtualization playing central roles. However, the principles of selecting scalable, stable, and well-supported platforms remain relevant. Modern enterprises still prioritize robust infrastructure capable of handling mission-critical applications, though the focus has shifted towards cloud-native solutions and hybrid cloud environments. The emphasis on supplier experience and support continues to be crucial in ensuring successful technology deployments. 

### 4. Analysis of How the Contents of the Document Played a Role in Impacting the History of the Companies Mentioned 

The document's recommendation for Hercules to adopt HP's RISC/Unix systems likely contributed to HP's dominance in the multiuser Unix market during the 1990s. By securing large enterprise clients like Hercules, HP solidified its market leadership and expanded its influence in the enterprise computing sector. For SAP, the successful implementation of SAP R3 on HP systems reinforced its reputation as a leading enterprise software provider, paving the way for future growth and innovation. The document also highlights the challenges faced by DEC and IBM, influencing their strategic decisions and market positioning in subsequent years. 

### 5. Market Acceleration Catalysts 

- Adoption of scalable and stable RISC/Unix systems for enterprise applications. 

- Increased demand for robust backup, recovery, and network management solutions. 

- Growth in ISV support for multiuser Unix platforms, enhancing software compatibility. 

- Advancements in RISC processor technology, driving performance improvements. 

- Expansion of enterprise software solutions like SAP R3, boosting market adoption. 

### 6. Keywords 

SAP R3, RISC/Unix systems, HP 9000 Series 800, multiuser computing, enterprise software, hardware suppliers, Digital Equipment Corporation, IBM, Aberdeen Group, Hercules Inc. 

Citations: 

[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/directfiles/18598228/61d551ad-1a18-4c7f-a1242179f9aa92c0/1993 Hercules SAP.pdf 

[2] https://www.imdb.com/title/tt0119282/plotsummary/ 

[3] 

https://my.unlv.nevada.edu/psp/lvporprd_10/EMPLOYEE/S A/e/?url=https%3A%2F%2Fxn--b1afzj3b4c.xn-p1ai%2F1973524fe4fe43y 

[4] https://www.sap.com/about/company/history/19912000.html 

[5] https://www.hercules- 

tc.com/uncategorized/transforming-organizations-througha-shared-vision-of-success/ 

## [6] https://meromgalil.my- 

free.website/s/cdn/?https%3A%2F%2Funicom.mx%2Fmicr ositios.aspx%3Fi=https%3A%2F%2Fxn-- 

b1amecrkpgh0d.xn--p1ai%2F3861729wwwjutounetrfe43a 

## [7] 

https://www.esd.whs.mil/Portals/54/Documents/FOID/Read ing%20Room/Selected_Acquisition_Reports/FY_2017_SA RS/18-F-1016_DOC_06_AF_C-130J_SAR_Dec_2017.pdf 

## [8] 

https://www.accessdata.fda.gov/drugsatfda_docs/nda/2019 /761112Orig1s000MultiR.pdf 

[9] https://patents.google.com/patent/US8117078 

## [10] 

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7186903/ 

[11] 

https://en.wikipedia.org/wiki/Hercules_%281997_film%29 

[12] https://patents.google.com/patent/US8027886B2 

[13] https://en.wikipedia.org/wiki/Hercules_beetle 

[14] https://www.helpingwritersbecomeauthors.com/moviestorystructure/hercules-1997/ 

[15] https://canadabuys.canada.ca/en/tender- 

opportunities?items_per_page=50&order=award_ifnot_am ended&page=%2C14%2C17%2C14&sort=asc&words=Cis tel+Technology+Inc. 

[16] https://www.epa.gov/sites/default/files/2014- 

03/documents/revised_phase_II_work_plan_final_complet e.pdf 

[17] 

https://www.lsu.edu/hss/news_and_publication/NewsandE vents/2015/item75930.php 

[18] 

https://my.unlv.nevada.edu/psp/lvporprd_10/EMPLOYEE/S 

A/e/?url=https%3A%2F%2Fxn----btbgfrrpf9bg6b.xn-p1ai%2F2894536fe4fe43y 

[19] https://www.change.org/p/the-walt-disney-companywe-want-tamar-slay-that-vocal-braxton-to-play-calliope-inthe-live-action-hercules 

- [20] https://chatheart.my free.website/s/cdn/?https%3A%2F%2Funicom.mx%2Fmicr ositios.aspx%3Fi=https%3A%2F%2Fxn--18-9kcqtmtt.xn-p1ai%2F7263148btlawcnrfe43a 

### Key Factors Leading Aberdeen to Recommend HP 9000 Series 800 for SAP R3 

## **Aberdeen Group's recommendation for Hercules, Inc. to implement SAP R3 on the HP 9000 Series 800 was based on several critical factors:** 

1. **Breadth of Product Line**: 

- HP offered the broadest product line among the suppliers considered, with both high-end and midrange symmetric multiprocessing (SMP) capabilities. This breadth ensured that HP could meet Hercules' needs regardless of the size of the system required, providing a significant growth path and performance expansion capability[1]. 

2. **Supplier Experience**: 

- HP had a long history and strong commitment to RISC and Unix systems. Their Professional Services Organization (PSO) was claimed to be the world's largest supplier of Unix-related and open systems services, which was crucial for facilitating the implementation process for Hercules[1]. 

3. **Stable Unix Operating Environment**: 

- HP-UX, HP's Unix operating system, was reported to be among the top tier for stability. HP also led the industry in providing desirable extensions to Unix, such as OpenView, which accelerated the acceptance of a stable Unix environment[1]. 

4. **Upgradeable RISC Processor Technology**: 

- HP had demonstrated a strong track record with seven generations of PA-RISC implementations. This history indicated a reliable path for future performance improvements, which was essential for capturing the performance advantages promised by RISC processors[1]. 

5. **ISV Support**: 

- HP was the reference port for both SAP and Oracle, as well as the majority of independent software vendors (ISVs) in the multiuser Unix marketplace. This extensive ISV support ensured compatibility with essential applications and facilitated the transition from mainframe to Unix systems[1]. 

## 6. **Market Leadership and Growth**: 

- HP was the market leader in multiuser, commercial RISC/Unix systems with a significant market share and a high growth rate. This leadership position provided confidence in HP's ability to support large-scale enterprise implementations like that of Hercules[1]. 

7. **Benchmark Performance**: 

- HP's high-end 800 series systems had the highest TPC-A benchmark results in the industry, indicating 

superior throughput capability compared to competitors. This performance was critical for running mission-critical applications like SAP R3[1]. 

These factors collectively made HP 9000 Series 800 the most suitable choice for Hercules' SAP R3 implementation, ensuring scalability, stability, and robust support for their enterprise-wide information network. 

Citations: 

[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/directfiles/18598228/61d551ad-1a18-4c7f-a1242179f9aa92c0/1993 Hercules SAP.pdf 

## [2] 

https://www.iaop.org/Download/Download.aspx?AID=1005 &ID=80&RP=%2FContent%2F35%2F194%2F1005&SID= 35&SSID=194 

[3] https://community.hpe.com/t5/hpe-9000-and-hpee3000-servers/relocation-of-hp-9000-800-orreplacement/td-p/4920166 

[4] http://hparchive.com/HP-Professional/HP-ProfessionalVol-12-Num-10-Oct-1998.pdf 

[5] http://www.3kranger.com/HP3000/HPP/1999/HPP199907.p df 

[6] https://www.hpcwire.com/1997/12/12/hp-posts-recordbenchmark-sap-r3-app-suite/ 

[7] https://www.asafm.army.mil/Portals/72/Documents/Budget Material/2007/awcf/awcf.pdf 

[8] https://link.springer.com/book/10.1007/978-3-64256502-1 

[9] https://aamontillo.net/videos/?link=https%3A%2F%2Fxn-b1axgca3b.xn-p1ai%2F19243683fe43y&title=Predicting+Response+to+th e+Antidepressant+Bupropion+using+Pretreatment+fMRI 

