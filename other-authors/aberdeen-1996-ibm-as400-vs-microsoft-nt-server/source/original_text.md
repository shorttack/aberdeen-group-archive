# IBM's AS/400 Versus Microsoft's NT Server: The Challenge That Is Not

> Archived from: https://web.archive.org/web/19970112010618/http://www.aberdeen.com:80/secure/viewpnts/v9n3/v9n3.htm
> Original publication date: 1996-01-15
> Author: Aberdeen Group

---

## Original Document Text

Volume 9 / Number 3
January 15, 1996
IBM’s AS/400 Versus Microsoft’s NT Server: The Challenge That Is Not
Table of Contents
Executive Summary
The Importance of Winning in the SME Market
The Importance of Allies and Partners
AS/400: Advanced Series Transformation
Microsoft Windows NT: Client-Server Computing Only
NT and AS/400 FSIOP and IBM ProServers
The Bottom Line: Integrated Functionality versus Component Mixing-and-Matching
Conclusions and Observations
IBM has served the midrange commercial production computing needs of enterprises with its System/3X-AS/400 product line for 20 years. But as 1996 begins, many IS decision makers are
asking Aberdeen if Microsoft’s strategic vision of replacing AS/400s with PC servers running the Windows NT Server operating environment (BackOfﬁce) is a viable option for them. In this
Viewpoint, Aberdeen will examine the technologies and economics involved in the great AS/400 versus NT Server debate and let you decide which, or both, are right for your IS operations.
Executive Summary
IBM’s AS/400, with over 350,000 installations, is the leading choice in the midrange commercial computing marketplace for enterprise’s that want and require easy-to-acquire, -operate, and
-maintain information systems. Enterprises around the world have successfully used AS/400s to both automate their business processes and allow computer-naive end users straightforward
access to the data required to perform their jobs. IBM’s design center for the AS/400 is to provide sophisticated information systems capability in an integrated package that can be simply
used by both IS professionals and end users alike.
Microsoft believes that the AS/400 base’s buying criteria matches the proﬁle of the ideal customer for whom the Windows NT Server operating environment is designed. The NT Server
application environment — called
BackOfﬁce — consists of several bundled products, including SQL Server, SNA Server, Mail Server, Systems Management Server as well as NT Server itself, that provide the back-end
systems software services for front-end Microsoft clients.
The basis for Microsoft’s challenge to the AS/400 is three-fold. Microsoft believes that compared to the AS/400, Windows NT Server: 1) can be the basis for a lower cost hardware and
software server platform, 2) is more open, and 3) furnishes a direct path to client-server computing with its user-friendly PC-based interface. As a result, Microsoft is promoting Window NT
Server as the”AS/400 for the next-generation”— and many IS decision makers are now making their own comparative evaluations.
But Microsoft’s evaluation of the appeal of BackOfﬁce to the AS/400 customer base falls apart for the following four reasons.
1. The acquisition price of NT Server-based infrastructures will be more expensive than AS/400s when the price of fat-client PCs instead of 5250 terminals is taken into account. The NT
Server operating environment requires a Microsoft-based client (Windows 3.1, 95, or NT Workstation) to operate. For IS decision makers taking the Microsoft-directed two-plus year
view that NT Workstation is the appropriate client operating environment for business applications, the individual user PC — Pentium 133 MHz, 24 MB — price (including
maintenance) will be approximately $4,900 versus $1,940 for a comparable IBM 5250 dual session terminal with color monitor and local printer port. After taking into account the
difference in back-end server complex costs, this means that the total systems hardware cost may be up to $2,700 per installed user desktop more when implementing a NT Server-based
application compared to an AS/400.
When additional professional IS personnel support costs are accurately projected for supporting, maintaining, and upgrading a NT Server-based client-server infrastructure over a typical
ﬁve-year life-cycle, IS decision makers will probably ﬁnd that an AS/400-based solution will be less costly. For example, if a BackOfﬁce-based information system requires two more
full-time professional IS staff members than a comparable AS/400 system, the enterprise would need to spend hundreds of thousands of dollars more to support it over a typical ﬁve-year
life.
2. The majority of AS/400 customers have little experience or interest in the components approach required to assemble an NT Server operating environment — the downside of
Microsoft’s deﬁnition of”open". Rather than spend their efforts on such overhead tasks as determining which PC server is best for their needs, which systems management software
program they should use, and over time when and how to upgrade speciﬁc components, they would rather direct their attention to improving the automation of their enterprise’s business
processes. The AS/400 base’s acquisition strategy in general is to encourage their IS suppliers to add value by providing as much hardware-systems software component technical
integration as possible.
3. While Microsoft has provided numerous examples of the advantages of automating business processes with BackOfﬁce, it has not, and most likely cannot, show AS/400 users an
economic advantage for making the revolutionary 18-24 month, multi-million dollar change required to migrate their already working production systems to the NT Server environment.
4. The 1996 64-bit RISC-powered AS/400 Advanced Series operating environment which the AS/400 base can gracefully migrate to over the next several years has numerous technology-
based functional advantages over the 32-bit NT Server environment for running shared-logic production applications. In addition, it provides a pragmatic, evolutionary path for AS/400
users to move from their traditional green-screen applications to client-server computing.
From the AS/400 customer base’s perspective, NT Server most commonly represents a third option for adding a robust PC network operating system to its computing environment (Novell
NetWare and LAN Server/400 being the ﬁrst two choices) and/or a front-end workgroup compute engine to support applications that do not run on the AS/400.
As 1996 progresses and individual AS/400 customers do their own analysis of the advantages and disadvantages of using NT Server as their client-server production computing environment,
Aberdeen believes that almost all (95+%) will instead opt for adding additional functionality through an evolution to the AS/400 Advanced Series operating environment. And as Microsoft’s
marketing organization looks for easier opportunities requiring less direct, technical customer-support investments, its AS/400 attack program, like so many others in the past, will be
relegated to the back-burner and viewed by the industry as the 1995 challenge that was not.
Back to Table of Contents
The Importance of Winning in the SME Market


Aberdeen has observed that often the most radical information systems (IS) changes start within the millions of small-to-medium-sized enterprises (SMEs) located throughout the world.
Because of their lack of large IS staffs to automate business processes, but facing the same efﬁciency challenges as larger organizations — though on a smaller, less complex scale — SMEs
are more likely than their larger brethren to experiment with new technologies for production applications.
When IBM’s System/3X (the AS/400’s ancient predecessor) was introduced in the mid-1970s, it was radically different from mainframe computer technology. But because it was much less
expensive to acquire and operate from the perspective of needing minimal dedicated technical staff, it was wildly successful in the SME market.
Following this pattern, new products such as Lotus 1-2-3 and Unix-based relational database management systems (RDBMSs) gained their ﬁrst acceptance in the IS marketplace with SMEs.
Fortune 1000-sized enterprises, with more complex planning, budgeting, and stafﬁng issues as well as concerns about greater organizational disruptions, tend to be 18-24 months behind
SMEs in adopting more revolutionary technology products.
In addition, SMEs are very loyal over time to their IS suppliers. They are tolerant — not happy or forgiving — if their primary supplier misses one or two product cycles compared to the
competition. They simply do not want to change for the sake of changing and they recognize the economic penalty of completing a major IS infrastructure makeover just when their
incumbent supplier catches up to or leapfrogs the competition. For example, Aberdeen’s research shows that over 90% of IBM’s SME-derived AS/400 revenues come from its installed base
and the IS decision makers involved do not seriously consider another supplier.
A critical challenge facing Microsoft today is how to penetrate the large enterprise data center with its NT Server client-server operating environment. One crucial step in achieving this
objective is to ﬁrst gain the acceptance and loyalty of SME decision makers. Microsoft has come to what seems to it to be the obvious conclusion that it must take on the AS/400 in head-to-
head competition in the SME marketplace if it is to eventually be successful in the large data center. And thus the challenge has been laid down.
Back to Table of Contents
The Importance of Allies and Partners
To be a successful supplier in the IS industry today, a company must be able to work in conjunction with allies and partners that provide complementary products and services. Despite all the
media pronouncements that Microsoft and IBM are at each others throats over OS/2 versus Windows, IBM’s PC server organization, a key Microsoft NT Server ally, has been working with
independent software vendors (ISVs), including those whose products are primarily designed for the AS/400 or Unix, to optimize their applications on Intel- and PowerPC-based IBM servers
running NT Server. As a result, many AS/400-oriented ISVs are now offering the client-server versions of their software running under BackOfﬁce as well as on the AS/400. And in their
commitment to openness, these ISVs’ products are also available for many popular Unix operating environments.
In addition, Microsoft is recruiting the tens-of-thousands of independent software consultants that are desktop and LAN competent and encouraging them to acquire the skills necessary to
support all the
BackOfﬁce products for business critical applications within an enterprise. This is similar to the efforts IBM has put into its AS/400 Business Partner program to ensure customers that local,
independent support as well as IBM direct support will be available for their AS/400 installations. But while Microsoft’s professional service providers may have the technical-skill
competencies similar to what is required to support the Windows desktop environment, the majority are still lacking the business process skills that the AS/400 business partners have
obtained over numerous years of working to automate their customers’ operations to achieve higher ﬁnancial returns.
The allies and partners of both IBM and Microsoft in this challenge want to be neutral and encourage their customers to make their own decisions as to which operating environment to use
for production applications. However, it was Aberdeen’s observation in 1995 that for OLTP (online transaction processing) projects NT Server was being used primarily in prototype and test
planning phases in the hopes of discovering if it really is a lower cost, more effective client-server production operating environment (especially in comparison to Unix alternatives) while
AS/400s were being acquired to be placed into immediate use as production systems for business-critical applications. As a result, the allies and partners of both IBM and Microsoft are
continuing to increase their commitment to the AS/400 until the market decides NT Servers’ long-term role within users’ information infrastructures.
Back to Table of Contents
AS/400: Advanced Series Transformation
IBM is in the midst of a major, but often little noticed, product transformation of the AS/400. (See Aberdeen Product Viewpoint, IBM’s New AS/400 Advanced Series: Achieving
Sophistication Through Simplicity, June 21, 1995.) Highlights of this transformation include:
New systems packaging and lower pricing. Advanced Systems are designed for online transaction and batch processing while Advanced Servers are intended for PC support and
decision support applications.
64-Bit RISC processors. The AS/400 has now made the transition from 48-bit CISC (complex instruction set computing) processors to 64-bit RISC. The result is signiﬁcant increases
(50+%) in performance that will be improved as the systems software is better tuned to take advantage of the hardware capability.
DB2/400 functionality. Integrated into the AS/400’s current operating system (OS/400 Version 3) is its relational database, DB2/400. DB2/400 has been signiﬁcantly upgraded to
provide the functionality required to meet the needs of the distributed, production OLTP applications necessary today to run highly effective enterprise operations.
With these technology advances, the AS/400 has gone from being a premium-priced, monolithic system to one that allows users to build a comprehensive, ﬂexible, distributed, easy-to-
operate information infrastructure. The former major weaknesses, such as poor client-server and PC network operating system support, in the AS/400 operating environment based on the
previous version of OS/400, Version 2, that Microsoft was shooting at with NT Server have been eliminated with the introduction of the AS/400 Advanced Series and OS/400 Version 3. For
example, the AS/400 has shown excellent client-server performance and price/performance under the Client/Server Labs (an independent testing organization, 404-552-3645) tests compared
to Unix/Risc and NT/Intel operating environments. (See Aberdeen Viewpoint, Client/Server Benchmarks: IBM Sets the Standard, April 11, 1995)
Back to Table of Contents
Microsoft Windows NT: Client-Server Computing Only
Microsoft developed NT to have the equivalent, or superior, functionality and capability of both Novell’s NetWare (the leading PC network operating system) and Unix-based client-server
online transaction processing (OLTP). However, unlike AS/400 or Unix, NT Server supports only intelligent client-based applications — it does not support low-cost, shared-logic, terminal
enabled applications.
The product deliverables (which are estimated to account for approximately $500 million of Microsoft’s 1995 revenues) of the
1. NT Workstation: This is the desktop version of NT that was originally shunned by almost all commercial IS decision makers because of the cost of the PC hardware requirements
(especially the cost of a recommended 24 MB of RAM) for running applications on it. However, since Microsoft has recently stated that NT Workstation is the preferred operating
environment for NT Server clients within enterprises and eventual successor to both Windows 3.1 and Windows 95 (and will be upgraded by April 1996 to include the Windows 95
interface), many organizations are now adopting it to be the fat-client operating environment for their OLTP client-server and workgroup productivity applications. In addition,
Microsoft has positioned NT Workstation head-to-head against Unix-based technical workstation operating environments from suppliers such as Sun Microsystems, Hewlett-Packard,
and IBM.


2. NT Server: By itself, NT Server is merely a network operating system (NOS) — although a very sophisticated multiprocessing system — for providing print and ﬁle services to PCs.
3. BackOfﬁce: BackOfﬁce is the server suite of systems software packages — NT Server, SQL Server, SNA Server, Systems Management Server, and Mail Server — that support
Microsoft-based clients. Microsoft has packaged, priced and closely interfaced these BackOfﬁce products together to provide the basis for its OLTP, decision support, and workﬂow
application engine. BackOfﬁce is one-half of the NT product option (the other half is the required PC-based Windows client operating environments) that Microsoft is employing to
challenge IBM and the AS/400. Aberdeen anticipates that Microsoft will add additional packages to BackOfﬁce, such as Exchange and Internet Services, during 1996.
NT Server with SQL Server has been gaining industry attention from its success in running Transaction Processing Council TPC-C Version 3 benchmarks. In the three NT Server operating
environment TPC-C tests published through December 15, 1995, two on Digital Equipment Corporation AlphaServers and one on a Compaq ProLiant 4500, the systems tested showed both
very good midrange OLTP performance and excellent price/performance. However, TPC-C Version 3 does not include the price of end-user devices — terminals or PCs — as TPC-C Version
2 did. If Version 3 did, and because NT Server does not support terminals, only PCs and X-Stations, the price/performance would not look nearly as good as it does for a total system (one
that includes NT Workstation clients) in comparison to the AS/400 which does support lower-cost 5250 terminals.
As shown in Figure 1, Aberdeen estimated the impact on total 5-year systems acquisition costs for the TPC-C prices for both the AS/400 and Compaq ProLiant systems including end-user
devices. We priced both a NT Workstation (the recommended OLTP client solution) and smaller Windows 95 Server clients (good-enough clients) for the NT Server system. Note that the
cost of the server complex, including front-end processors, is relatively small compared to the cost of end-user devices. More to the point, the Compaq ProLiant 4500 systems tested would
have over $10 million in additional cost — making the $593,216 cost of the NT Server complex seem almost to be a discounting or rounding error. Even taking into account the lower NT
Server’s cost, Aberdeen’s conclusion is that an NT Server-based OLTP information infrastructure will cost $1,700-$2,700 more per deployed, end-user input device in computer hardware
alone than an AS/400 solution.
In addition, Aberdeen needs to point out that all three NT Server TPC-C tests, both from Compaq and Digital, used front-end Unix systems to multiplex the data entry PCs and share the
transaction workload with the back-end NT Server server processor. This implies that for an enterprise to obtain the same performance and price/performance that the suppliers did in their
tests, an organization would need to support both NT Server and Unix — an additional on-going operating cost.
At this time, Aberdeen estimates that there are fewer than 10,000 BackOfﬁce installations running business-critical OLTP applications — and even fewer get-the-bills-out or close-the-books
batch applications. BackOfﬁce has just not been matured long enough — note that the production version of SQL Server was only released in June 1995 — for IS executives to stake their job
on its robustness for running highly visible and vital applications.
Finally, Aberdeen notes that according to Microsoft, NT Server is to be replaced eventually with Cairo — its object-oriented networked operating system environment. Aberdeen does not
believe that the migration path from NT Server to Cairo will be an easy, transparent upgrade path for the early adopters of pre-Cairo operating environments but rather another disruptive
change requiring new hardware and applications — similar to the problems too many users experienced in 1995 when trying to upgrade their existing PCs from Windows 3.1 to Windows 95.
Aberdeen’s analysis of the current status of NT Server is that it is a well-performing network operating system for basic ﬁle and print services with Microsoft applications and its best
application function is as a local, departmental workﬂow engine. Its two chief longer-term appeals for IS decision makers today seem to be: 1) its low cost of platform acquisition, allowing
enterprises to automate
tasks that could not have been cost justiﬁed in the past, especially for smaller workgroups that already have deployed individual PCs for users, and 2) its integration with the Windows 95
desktop operating environments. However, it has not yet proven to the market that it is a superior OLTP operating environment or NOS compared to the alternative products that are designed
for these speciﬁc functions.
Back to Table of Contents
NT and AS/400 FSIOP and IBM ProServers
IBM’s reaction to NT Server is not uniform across the company. In one division, the group responsible for IBM’s PC servers, the ProServer line, there is tremendous support for NT Server
and BackOfﬁce — their potential success could fuel this division’s success. In IBM’s database division, which has released a version of DB2 for NT, the same revenue growth objectives are
at work. This is in direct contradiction to the objectives of the software organization responsible for gaining market share for both OS/2 and IBM/Lotus Notes.
Even within the AS/400 product marketing group, similar contradictions are obvious. On one hand, IBM is annoyed by Microsoft’s direct marketing attack on the AS/400 and the technology
it represents. At the same time, the AS/400 has as an option an Intel processor on a board, the FSIOP (ﬁle server input/output processor), that can run IBM’s LAN Manager PC network
operating system and will support both Novell NetWare and IBM/Lotus Notes shortly. Adding NT Server support to provide comprehensive NOS choices for its customer should be a small
technical issue — but it is emotionally difﬁcult to support one component of a supplier’s product that is challenging the whole product line.
Aberdeen anticipates that NT Server will be supported on the AS/400’s FSIOP in the future. In the meantime, users can run BackOfﬁce on a separate system and connect to their AS/400
using the SNA Services module. AS/400 users who want NT Server functionality can easily have the best of all worlds — the AS/400 for production, run-the-company applications and NT
Server for a NOS to support connected PCs. AS/400 users can then make an even more intelligent decision, with fewer technical limitations, as to how to increase their information
infrastructure’s functionality — by adding either additional BackOfﬁce components or AS/400 options.
Back to Table of Contents


The Bottom Line: Integrated Functionality versus Component Mixing-and-Matching
IBM and Microsoft have many functional upgrades (such as clustering) for their respective operating environments planned throughout 1996. In today’s competitive world, neither supplier
can rest on its pre-1996 successes.
However, the core design philosophy of the two operating environments will not change. The AS/400 is designed to be an integrated operating environment where evolutionary upgrades will
be developed as part of IBM’s most important, holistic computing platform offering. NT Server, BackOfﬁce, and Microsoft’s allies and partners (such as hardware suppliers) products will be
designed from a component-based philosophy where each new product release may represent technical challenges for upgrading entire systems. Both approaches have numerous advantages
and disadvantages that are the exact opposite of the other. For example, paying scant attention to designing in upgradeability features assures a supplier faster time to market, more advanced
functionality, and lower development costs for a new release of a product — it also ensures the customer base frustration for (and often failure at) implementing new features and
functionality it had often been counting on for quite some time.
Many AS/400 users are now facing the challenge of how to effectively implement client-server computing throughout their enterprise. They have resisted client-server computing because of
the component approach required. Recognizing this, IBM has engineered an integrated client-server solution for the AS/400 with the combinations of
AS/400 Advanced Servers, FSIOP, CA/400, and industry-standard ODBC (open database connectivity) interoperability between DB2/400 and all major PC applications. The result is that
AS/400 users now can migrate to client-server computing with an integrated solution that shows both excellent performance and price/performance compared to component-based
alternatives.
Numerous years of research with the AS/400 base show it is highly resistant to adopting the component acquisition approach to implementing information infrastructures. It recognizes the
economic advantages of having a supplier-of-choice provide that value. As a result, Aberdeen does not believe that Microsoft will convince more than a very few AS/400 customers to
migrate to NT Server for product-technology advantage reasons.
The very few IS decision makers with the luxury of being able to start building a new information infrastructure in 1996 will have the option of choosing whether to follow the components-
based approach of Microsoft’s NT Server or the integrated-and-ready-to-run philosophy of IBM’s AS/400.
Back to Table of Contents
Conclusions and Observations
The reasons both AS/400 and BackOfﬁce are expected to grow and ﬂourish in 1996 is that they are viewed by IS decision makers as the two low-total-cost, easy-to-use approaches for
multiuser computing applications.
Quite frankly, based on the early 1995 assessments by many leading-edge IS organizations and ISVs’ marketing departments, Aberdeen thought that BackOfﬁce might emerge as a very
signiﬁcant OLTP operating environment by now. However, Aberdeen was disappointed, but not surprised, by the number of shops that thought they were going to go live with production NT
in 1995 and did not. Technical integration issues (especially those surrounding Microsoft’s OLE standard), immaturity of the client-server operating environment (including ISV client-server
applications) and total cost to implement and maintain over a ﬁve-year life-cycle seemed to play a major role in the cooling of enthusiasm for BackOfﬁce by IS professionals. As with any
new technology, the devil is in the implementation details.
As we enter 1996 and the industry has had several months — Aberdeen started the clock with the release of SQL Server 6.0 in mid-1995 — to better understand BackOfﬁce’s capabilities and
limitations, it is increasingly clear that NT Server is best suited for enterprises that have strong Unix- and client-server-expert IS organizations — not AS/400-dedicated organizations.
Microsoft’s buyer-be-willing-to-invest-in-experimenting component-based product design philosophy is the same as that found in the Unix world — an IS approach that continues to be
rejected by AS/400 decision makers.
After all is said and done, much of the appeal of NT and BackOfﬁce lies in their marketing glamour and future promise. For example, Microsoft and Digital Equipment Corporation are
showing excellent AlphaServer-NT Server price/performance
using the TPC-C benchmarks compared to Unix systems. Jumping early on the NT Server bandwagon is a means for many to make up for missing the Unix or PC revolutions. But for
AS/400-trained IS executives, jumping before looking could be a serious CLD — career limiting decision. The costs of NT Server look much less attractive when decision makers add on the
cost of a PC on every desk, on-going staff or independent professional service support costs (especially for upgrading the server and PCs with new product version releases), and the very real
possibility of higher-downtime due to the relative immaturity of the NT Server software/hardware platform components that must all work together.
Aberdeen notes that one of the ultimate ironies of the Microsoft challenge is that Microsoft itself uses AS/400s to run its own business operations. How it progresses in migrating to SAP’s
R/3 integrated suite of client-server applications running on BackOfﬁce will be closely watched by the industry throughout 1996.
With the dramatic functionality enhancements IBM has made to the AS/400 with the introduction of the AS/400 Advanced Series and OS/400 Version 3, Aberdeen cannot see where AS/400
users would gain a cost-based or production-application technology advantage by changing to BackOfﬁce. A better, more productive return-on-investment-based IS strategy would be to put
possible migration resources (people and budgets) to work to automate more internal enterprise-wide business processes by leveraging existing AS/400-based applications.
As Microsoft concerns itself more with the direct threat to its core PC software business in the form of the Internet (see Bill Gates’ 1995 book, The Road Ahead), its enthusiasm for investing
in the resources required to migrate AS/400 users to BackOfﬁce — even with the help of allies’ and partners’ monies and time — will most likely wane.
And as AS/400 users better understand the comparative technical strengths of the new AS/400 Advanced Series, their enthusiasm for their installed information infrastructure will grow. As
result, in 1997 the industry will surely view the great AS/400-NT Server debate as the challenge-that-was-not.
Back to Table of Contents
AberdeenGroup, Inc.
One Boston Place
Boston, Massachusetts
Contact Information:
Susan Rinehart, Client Services Manager (direct #: 617.854.5212)


02108 USA
Tel: 617.723.7890
Fax: 617.723.7897
David Borde, Marketing Manager (direct #: 617.854.5226)
Email: rinehart@aberdeen.com or borde@aberdeen.com
The trademarks and registered trademarks of the corporations mentioned in this publication are the property of their respective holders. Unless otherwise noted, the entire contents of this publication are copyrighted by Aberdeen
Group, Inc. and may not be reproduced, stored in a retrieval system, or transmitted in any form or by any means without prior written consent of the publisher.
Copyright © 1996 Aberdeen Group, Inc., Boston, Massachussetts
This Document is for Electronic Distribution Only
-- DO NOT COPY --


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-ibm-as400-vs-microsoft-nt-server |
| title | IBM's AS/400 Versus Microsoft's NT Server: The Challenge That Is Not |
| author | Aberdeen Group |
| date | 1996-01-15 |
| type | product-viewpoint |
| subject_domain | midrange-computing-platform-competition |
| methodology | industry-analysis, competitive-profiling, benchmarking, field-research |
| source_file | 1996 IBM's AS_400 Versus Microsoft's NT Server_ The Challenge That Is Not pvp.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group analyzes Microsoft's challenge to IBM's AS/400 installed base, arguing that the AS/400 with over 350,000 installations will retain its dominance in midrange commercial computing against Microsoft's NT Server (BackOffice). Aberdeen presents four economic and technical reasons why the challenge will fail: higher total cost for NT due to fat-client PCs, lack of match with AS/400 customer culture, absence of proven migration economics, and AS/400 Advanced Series' superior 64-bit RISC capabilities — predicting the debate will be viewed as 'the challenge that was not' by 1997.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Addressed the defining platform battle of mid-1990s commercial computing with quantitative TCO analysis that influenced IS executive decision-making. |
| **Relevance** | medium | TCO framework and integrated vs. component platform analysis remain applicable; AS/400 platform survived as IBM i and is still active in 2026, validating Aberdeen's assessment. |
| **Prescience** | high | Aberdeen's core predictions proved accurate: virtually no AS/400 customers migrated to NT Server, and the platform survived 30 years to become IBM i. |

### Prescience Detail

**Prediction 1:** AS/400 customer retention against NT
- **Claimed:** Almost all (95%+) AS/400 customers will opt for evolution to AS/400 Advanced Series rather than migrate to NT Server
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 1:** AS/400 customer retention
- **Result:** AS/400 installed base remained loyal; platform survived and evolved into iSeries (2000), System i (2006), IBM i (2008); still actively supported in 2026
- **Confidence:** verified
- **Notes:** IBM i release lifecycle data shows continuous platform evolution; no mass migration to NT occurred

**Prediction 2:** Microsoft AS/400 attack program prognosis
- **Claimed:** Microsoft's AS/400 attack program will be relegated to back-burner and viewed as the 1995 challenge that was not
- **Year:** 1996-1997
- **Confidence at time:** high

**Actual Outcome 2:** Microsoft AS/400 attack program outcome
- **Result:** Microsoft shifted focus to Internet strategy; BackOffice as AS/400 replacement faded from priority by 1997-1998; AS/400 retained its base
- **Confidence:** verified
- **Notes:** Consistent with Microsoft's documented Internet pivot per Bill Gates' "The Road Ahead" (1995)

**Prediction 3:** NT Server support on AS/400 FSIOP
- **Claimed:** Aberdeen anticipates NT Server will be supported on AS/400 FSIOP in the future
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 3:** NT Server support on AS/400 FSIOP
- **Result:** IBM did add NT Server support options for AS/400 users; AS/400 users used NT as complementary not replacement, consistent with Aberdeen's coexistence model prediction
- **Confidence:** medium
- **Notes:** FSIOP line eventually discontinued; coexistence model proved accurate

**Prediction 4:** AS/400 vs NT debate perception by 1997
- **Claimed:** In 1997 the industry will view the great AS/400-NT Server debate as the challenge-that-was-not
- **Year:** 1997
- **Confidence at time:** high

**Actual Outcome 4:** AS/400 vs NT debate public perception
- **Result:** By 1997-1998, Microsoft's focus had shifted to Internet/Exchange; direct AS/400 attack program did wind down as Aberdeen predicted; the debate faded from industry discourse
- **Confidence:** verified
- **Notes:** Microsoft's major 1997-1998 announcements focused on Windows 98, Exchange, and Internet strategy

### Entities Referenced (9)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| IBM Corporation | company | active | — |
| Aberdeen Group | firm | acquired | Aberdeen (Harte-Hanks -> Spiceworks-Ziff Davis) |
| Microsoft Corporation | company | active | — |
| Compaq Computer Corporation | company | acquired | HP (2002) |
| Digital Equipment Corporation (DEC) | company | acquired | Compaq (1998) -> HP (2002) |
| Novell, Inc. | company | acquired | Attachmate (2011) -> Micro Focus (2014) -> OpenText (2023) |
| Lotus Development Corporation | company | acquired | IBM (1995) |
| Client/Server Labs | firm | unknown | — |
| SAP AG | company | active | — |

### Technologies Referenced (10)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| IBM AS/400 Advanced Series | platform | IBM | emerging | legacy-supported |
| Microsoft BackOffice | platform | Microsoft | emerging | obsolete |
| Microsoft NT Server | platform | Microsoft | emerging | obsolete |
| Microsoft NT Workstation | platform | Microsoft | emerging | obsolete |
| OS/400 Version 3 | platform | IBM | mature | obsolete |
| DB2/400 | application | IBM | mature | legacy-supported |
| Microsoft SQL Server 6.0 | application | Microsoft | emerging | obsolete |
| Microsoft Cairo | platform | Microsoft | emerging | obsolete |
| AS/400 FSIOP | platform | IBM | emerging | obsolete |
| IBM 5250 Terminal | platform | IBM | mature | obsolete |

### Observation Summary

- Total observations: 31
- By type: benchmark-result: 5; technology-assessment: 5; market-data: 4; strategy-classification: 4; viability-prediction: 4; actual-outcome: 4; framework-factor: 4; expert-opinion: 1
