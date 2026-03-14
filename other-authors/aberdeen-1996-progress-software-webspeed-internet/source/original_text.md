# Progress Software's WebSpeed: Business Transaction Processing On The Internet

> **Archived from:** [https://web.archive.org/web/19970604103320/http://www.aberdeen.com:80/secure/profiles/proweb/body.htm](https://web.archive.org/web/19970604103320/http://www.aberdeen.com:80/secure/profiles/proweb/body.htm)
> **Original publication date:** 1996-10-01
> **Author:** Aberdeen Group

---

## Original Document Text

Progress Software
14 Oak Park
Bedford, Mass. 01730
Tel: (617) 280-4000
Internet: webspeed.progress.com
Progress Software’s WebSpeed: Business Transaction Processing On The Internet
Preface
To fully exploit the potential of the Internet, corporations must move beyond text-based marketing-oriented Web sites to deliver full-ﬂedged transaction-processing applications.
To execute distributed client-server applications across an Internet or Intranet, IS needs to build in an ability for the application to scale rapidly. This is particularly true for data-intensive
applications, where past scalability techniques must adapt to the new architectures. Moreover, today’s Web-browser/Web server combination lacks the robust transaction processing features
necessary to scale without help -- or the means to integrate well enough with tried-and-true scalable legacy applications.
To meet the scalability challenge, Internet-application developers must have:
• TP-monitor-like Internet middleware, and development tools that can take advantage of the middleware’s features; and
• Application and database servers that, combined, deliver effective support for data operations – e.g., a relational, SQL-based database server that can provide data/transaction integrity,
ensuring data accuracy and more robust processing.
This Proﬁle describes Progress Software’s WebSpeed, a product directly aimed at meeting the Internet’s scalability challenge, from a technology supplier exper-ienced in both business-TP
data management and advanced development tools.
Executive Summary
Progress Software’s WebSpeed is an Internet development tool aimed at aiding developers to deliver data-intensive Web applications that scale effectively as end users are added, deliver high
Internet performance, and can change Web pages dynamically, allowing customer and end-user interaction to databases via a Web browser. WebSpeed is comprised of two main components;
WebSpeed Workshop, a set of development tools that include the Progress 4GL scripting language, and Transaction Server, a scalable Web-based deployment engine.
WebSpeed’s technology was developed speciﬁcally for the Internet and leverages Progress Software’s powerful client-server application development environment (CADE). Thus,
developers can create robust, data-intensive programs rapidly with a point-and-click Visual Programming Environment rather than having to slog through low level 3GL programming.
WebSpeed directly targets the Internet’s Web-server scalability problems by incorporating multiplexing/load-balancing middleware that can manage multiple client requests at one time and
pass them along to server-based Web objects that service the requests. In fact, WebSpeed allows developers to "rewrap" existing services such as stored procedures as Web objects. Thus,
developers can reuse ﬁeld-proven legacy data-intensive applications, cutting development costs and speeding up Internet development.
In what is fast becoming an Internet/Intranet "tradition", self-styled "Webmasters" creating Web sites work outside of IS, without IS’ supervision and without its typical processes.
WebSpeed’s transaction-processing capabilities, integration with authoring tools and object-based development strategy give users the "best of both worlds": entrepreneurial, fast-paced Web
authorship plus automated IS-process-based development.
WebSpeed Workshop
The Workshop further breaks down into three development tools for creating data-driven, transaction-based Web objects:
• WebSpeed WorkBench,
• WebSpeed 4GL, and
• TagExtract.
WebSpeed WorkBench, the core development tool and visual programming environment (VPE), automates the process of creating Web objects. Developers can also use WebSpeed
WorkBench to link database schemas, forms, and Web objects. Thus, the developer can rapidly generate a data-access form (and form-type Web-object) for display on a Web site based on an
enterprise’s backend corporate data, or ensure that Web-site data is consistent (and integrated) with key enterprise databases. WebSpeed allows users to incorporate their HTML authoring
tool of choice, such as HotMetal Pro or Front Page, to build the end-user front-end HTML pages for a Web-transactional application.
The WebSpeed 4GL provides native and SQL-based access to Oracle7, IBM AS/400, and the Progress RDBMS. WebSpeed’s open architecture allows developers to use their choice of Web-
server software such as Microsoft’s Internet Information Server and Netscape’s servers. Thus, developers can use a sophisticated, experienced 4GL rather than immature Java coding to
handle detailed data-intensive-application programming.
The third component is TagExtract, a tool that assists in mapping WebSpeed data to HTML. TagExtract generates the information needed for runtime merge processing. TagExtract allows
developers to create "dynamic applications" that can change Web-page displays on the ﬂy, as the underlying data changes.
The advantages to using WebSpeed Workshop for building Web applications are numerous, but two stand out as especially notable:
• The WorkBench VPE delivers increased Web-programming productivity because of its CADE visual-programming drag-and-drop ease-of-development, allowing rapid development of
Web-enabled applications;
• WebSpeed Workshop offers effective data-intensive-application Internet-development support by allowing rapid creation of, and changes to, data-based Web forms.
Transaction Server
The Transaction Server, a scalable Web engine that executes the Web objects created in WorkBench, also breaks down into four major elements:


• Transaction Agents that execute Web objects, perform database transactions, and merge data into HTML format;
• The Transaction Messenger that transfers data between the Web server and a Transaction Agent during a single Web transaction; and
• The Transaction Broker that manages a pool of Transaction Agents (making them available when Web applications request them) and maintains status information used to dispatch
Transaction Agents efﬁciently or shut down the underlying Web objects.
A key advantage of this approach is that Agents provide a means of maintaining "state". In a typical interaction, the Web server breaks the connection with the end user’s Web browser, even
though the end user may be in the middle of a transaction. The Agent keeps track of end users and where they are within transactions, ensuring that Internet applications can deliver the same
transaction support and robustness as today’s client-server applications built on RDBMSs – and that those same client-server applications translate readily to the Internet.
WebSpeed Transaction Server’s most useful beneﬁts include not only its support for "state" but also its ability to provide communications multiplexing and load balancing across multiple
servers. These transaction servers have proven exceptionally effective in scaling data-intensive applications to hundreds of end users or large-scale databases. For example, via load balancing
users can spread the transaction load across multiple servers and the Transaction Server can steer client requests to underutilized servers, helping to avoid unnecessary peak-time overload.
Market Position
A new market is springing up based on delivering Internet/Intranet applications rapidly and efﬁciently. The current crop of 3GL tools and Web-site authoring toolsets, such as Java and Active
X, are valuable advances in Internet technology, but in many cases mean that complex, database-using applications are difﬁcult to implement.
As noted above, Progress Software’s WebSpeed offering is designed to meet several key requirements of the well-thought-out Internet development tool:
• It can maintain the "state" of a connection during an Internet session;
• It remains open for integration with any Web-site authoring tool, Java applet, Web server, and security software; and
• Its modular approach to development and partitioned services structure lend naturally to the integration of existing Progress applications into the mix.
Progress Software is aiming the tool at organizations that wish to combine current business transaction-processing-application development efforts with IS Internet/Intranet efforts and newly
developed Internet/Intranet applications. In these cases, WebSpeed can be combined with DataServers for high-performance database access and to merge existing transaction services with
Internet-enabled features. In addition, WebSpeed can act as a complement to traditional Progress development tools.
WebSpeed Workshop is available on Microsoft Windows 95 and Windows NT. The WebSpeed Transaction Server is available on Windows NT, Sun Solaris, Digital Unix and IBM AIX
server platforms. It supports application development for DB2/400, Oracle, and PROGRESS databases.
WebSpeed’s Flexible Architecture
The WebSpeed architecture is designed as a multi-tier conﬁguration that makes it easier to distribute pieces of a Web-enabled application and to upgrade or change those software
components when needed. The ﬁrst two tiers are the client, which is a Web browser that accesses a Web site, and the standard Web server that serves up static information in HTML pages.
The WebSpeed Messenger resides on the Web Server.
The third tier is the WebSpeed Transaction Server itself, which stands between the Web server and the corporate data. WebSpeed Transaction Broker and WebSpeed Transaction Agent reside
on this server. The fourth and ﬁnal tier is the user’s database server, the backend RDBMSs in which corporate data is stored.
This ability to share processing between multiple tiers gives the developer added ﬂexibility in placing application components on any of the tiers. It also gives the application administrator
greater ability to scale the application by shifting the components from tier to tier as needs change.
Key Advantages Of WebSpeed
As security is always an important issue when transactions occur over the Web, WebSpeed Transaction Server supports multiple levels of password protection and secure identiﬁcations
generated by the Web browser or by a Web server. It can also integrate with other security products, as evidenced by Progress’ partnership with Security Dynamics Technologies Inc. The two
companies have set up a strategic partnership in which they will work together to integrate Security Dynamics’ user authentication technology, ACE/Server and SecurID solutions, into
WebSpeed. ACE/Server provides a positive user authentication and SecurID that combines a user password ID with a randomly generated access code that continually changes for the
duration of a secure transaction.
Internet application performance is a key consideration for developers deploying applications over the Web. As noted above, the WebSpeed Transaction Server can help to alleviate
slowdowns and time outs by its ability to multiplex and load balance transactions.
No transactions are possible, over the WWW or otherwise without robust and reliable connections to multiple back end databases. The Transaction Server can manage multidatabase as well
as single database transactions and provides two-phase commit for data integrity. If a transaction is terminated at any time during the process WebSpeed Transaction Server will roll back the
database to its original unaltered state.
New-Application Development Using WebSpeed Workshop
Application development is changing signiﬁcantly as Web-enabled development tools proliferate and developers start to look seriously at the difﬁculties and advantages of building Web
applications. Unlike Web authoring environments or browser companies that sell development components separately, WebSpeed includes both the full development and deployment
environment. It is compatible with any browser, CGI-compliant server, HTML authoring tool or Java development environment that a developer might want to use. This compatibility with
third-party tools combined with the rich visual-development capabilities of WebSpeed Workshop make this tool extremely usable.
WebSpeed applications are, in effect, a "collection of Web objects that are managed by a single Transaction Broker and that require the services of the same set of databases." The Web page
designer uses a Web authoring tool to create the graphical user interface while developers use WebSpeed Workshop to build Web objects that contain the business logic that drives the
application. WebSpeed Workshop can also be used to deﬁne ﬁeld-level mapping to the requisite database, making necessary RDBMS connections. Developers may also build Web objects
that contain embedded HTML statements, allowing the Web page to be generated dynamically based on the returned data. In any of these cases, WebSpeed can enhance developer
productivity -- by making use of already existing knowledge and skill using a third-party tool, or by automating time-consuming parts of the development process that do not necessarily
require a skilled programmer.
Combining WebSpeed with third-party Web authoring tools is also an effective way for IS to incorporate business end-users and Web site designers into the development of Web transaction-
processing applications. Users report that outside business and design expertise is often a good way to troubleshoot potential problems with Internet-application behavior or to target new
feature requirements.


Leveraging Today’s Data-Intensive Applications
To be truly successful, Internet/Intranet applications should be more than static Web pages and should take full advantage of the database services already provided by many existing client-
server applications. WebSpeed allows the developer to tie Web pages together with business logic through the link with the database schema and through the design of applications as a series
of Web objects.
WebSpeed’s support for transaction processing and its strong database integration via TagExtract data mapping can be a great boost in incorporating existing databases into the Internet
application. New applications simply have to use the same ﬁeld naming conventions as the database in order to support robust transaction processing, a signiﬁcant boost to development.
Existing PROGRESS users will beneﬁt even more, as they can use WebSpeed to Web-enable legacy Progress toolset- and database-based applications.
Competition
Progress faces competition from two fronts, current CADE suppliers and new Internet-toolset suppliers.
Major CADEs such as Microsoft's Visual Basic, Powersoft's PowerBuilder, Forte, Unify's Vision, and Oracle's Developer/2000 deliver much of the scalability, ﬂexibility, programmer-
productivity features, software-lifecycle support, and application partitioning and business modeling needed to deliver major business-development bottom-line value-added over previous
toolsets. However, many of these CADEs lag in supporting crucial Internet application technology, such as Web-site authoring tools, transaction processing support over TCP/IP, new user
interface features, and distributed object technology, above and beyond class libraries. Most do support Java and legacy integration, especially those that provide application partitioning.
Versus these, Progress distinguishes itself especially by its ability to wed high-end Internet-data-intensive-application support (e.g., via its "state" support) with Web-site tool integration, and
its proactive implementation of Java support.
While Internet development toolsets are often leaders in providing Web-site authoring support, incorporating Web-site authoring tools, supporting Java-code generation, and providing
distributed-object support, they may be signiﬁcantly lacking in traditional database technology and legacy integration. Progress therefore strongly differentiates itself from these by its proven
data-intensive-application scalability and broad support for CADE technologies such as high-performance native multiple-database access and the WebSpeed 4GL.
Financials
Progress Software maintains a solid growth record as well as a $200 million revenue run rate for 1995, which will most likely continue through ﬁscal 1996. An astute citizen of the database
and tools market, Progress has been experiencing continued revenue growth of approximately 20% year-to-year.
Conclusion
Most Internet and Intranet applications provide an immediate beneﬁt through signiﬁcant communications-cost savings and the ability to expand corporate text-data access to new and remote
end users. Expanding that data access to new customers and features, such as electronic commerce, can additionally shave costs, increase sales and open the door to new data collection
opportunities. Thus, many enterprises are looking to Web-enable current client-server database-centric applications, giving new classes of end users access to them, as well as developing
Internet-speciﬁc database-using applications. However, these application efforts will only be as effective as the Internet software development tools used to build them. As stated above, the
better the tool, the quicker the solutions arrive, the better integrated with legacy applications, and the more features are available to end-users.
Aberdeen ﬁnds that Progress Software’s WebSpeed provides proven technology that can enhance these enterprises’ ability to deliver the new solutions rapidly. WebSpeed adds down-in-the-
details data-intensive-application scalability via "state" and TP-monitor middleware support, plus tried-and-true CADE technology such as a powerful drag-and-drop VPE that mean
increased productivity for Web-site authors and Web-application programmers.
As the new Internet development toolsets appear, now is the time for IS buyers to start eliminating those that cannot make the grade over the long term. Aberdeen recommends that users
focus on suppliers that are tackling a broad range of
Internet challenges and are using technologies proven effective in the recent past. These suppliers, like Progress, understand that Internet development success lies in successfully merging
old and new technology.
AberdeenGroup, Inc.
One Boston Place
Boston, Massachusetts
02108 USA
Tel: 617.723.7890
Fax: 617.723.7897
Contact Information:
Susan Rinehart, Client Services Manager(direct #: 617.854.5212)
David Borde, Marketing Manager (direct #: 617.854.5226)
Email: rinehart@aberdeen.com or borde@aberdeen.com
The trademarks and registered trademarks of the corporationsmentioned in this publication are the property of their respective holders. Unless otherwise noted, the entire contents of this publication are copyrightedby Aberdeen
Group, Inc. and may not be reproduced, stored in a retrieval system,or transmitted in any form or by any means without prior written consent of thepublisher.
Copyright © 1996 Aberdeen Group, Inc., Boston, Massachussetts
This Document is for Electronic Distribution Only
-- REPRODUCTION PROHIBITED --


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-progress-software-webspeed-internet |
| title | Progress Software's WebSpeed: Business Transaction Processing On The Internet |
| author | Aberdeen Group |
| date | 1996-10-01 |
| type | market-study |
| subject_domain | internet-development-tools, transaction-processing, web-application-development |
| methodology | industry-analysis, competitive-profiling, expert-opinion, document-review |
| source_file | 1996 Progress Software's WebSpeed_ Business Transaction Processing On The Internet pr.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group profiles Progress Software's WebSpeed, an Internet development platform aimed at building data-intensive, scalable web applications that integrate with legacy transaction-processing systems. WebSpeed combines the Progress 4GL development environment with a multi-tier Transaction Server providing TP-monitor-like middleware, state management, and load balancing. Aberdeen recommends WebSpeed to enterprises seeking to merge proven client-server data-management with Internet architecture, and positions Progress as superior to both traditional CADE suppliers and new web-only toolset vendors for data-intensive Internet applications.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Progress Software held a meaningful but niche position in the mid-1990s application development market; WebSpeed addressed a real architectural gap but was less influential than Oracle, Microsoft, or Netscape in shaping internet application development at the industry level. |
| **Relevance** | low | WebSpeed's specific 4GL-based architecture was superseded by Java EE, .NET, and later frameworks; Progress Software survived as a company but WebSpeed is a legacy product primarily of historical interest to researchers studying 1990s internet development tooling. |
| **Prescience** | medium | Aberdeen correctly identified that state management and TP-monitor middleware would be essential for scalable web apps (validated by J2EE/EJB, later microservices), but WebSpeed itself lost to Java and .NET; Progress Software survived via pivot to OpenEdge and data integration. |

### Prescience Detail

**Prediction 1:** Progress Software long-term viability
- **Claimed:** Aberdeen recommends enterprises focus on suppliers tackling broad Internet challenges like Progress
- **Year:** 1996
- **Confidence at time:** high
- **Source:** Conclusion

**Actual Outcome 1:** Progress Software survival and pivot
- **Result:** Progress Software survived; WebSpeed became legacy; company pivoted to OpenEdge, Telerik, Corticon
- **Confidence:** verified
- **Notes:** Active public company PRGS; WebSpeed still supported but not strategic product

**Prediction 2:** WebSpeed market success
- **Claimed:** Products using proven technology will succeed; WebSpeed adds proven scalability to internet
- **Year:** 1996
- **Confidence at time:** medium
- **Source:** Conclusion

**Actual Outcome 2:** Progress Software survival and pivot
- **Result:** Progress Software survived; WebSpeed became legacy; company pivoted to OpenEdge, Telerik, Corticon
- **Confidence:** verified
- **Notes:** Active public company PRGS; WebSpeed still supported but not strategic product


### Entities Referenced (8)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Progress Software Corporation | company | active | — |
| Aberdeen Group, Inc. | firm | acquired | Harte-Hanks -> Aberdeen Strategy & Research |
| Microsoft Corporation | company | active | — |
| Oracle Corporation | company | active | — |
| Powersoft Corporation | company | acquired | Sybase (acquired 1994); SAP (via Sybase 2010) |
| Security Dynamics Technologies, Inc. | company | acquired | RSA Security (merged 1999) |
| IBM | company | active | — |
| Forte Technologies (now Forte for Java) | company | acquired | Sun Microsystems (acquired 1999) |

### Technologies Referenced (9)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Progress Software WebSpeed | framework | Progress Software | emerging | legacy-supported |
| Progress 4GL (OpenEdge ABL) | language | Progress Software | mature | legacy-supported |
| WebSpeed Transaction Server | application | Progress Software | emerging | obsolete |
| WebSpeed WorkBench / Workshop | application | Progress Software | emerging | obsolete |
| Java / Java Applets | language | Sun Microsystems | emerging | active |
| ActiveX | framework | Microsoft | emerging | obsolete |
| IBM DB2/400 (AS/400) | platform | IBM | mature | legacy-supported |
| RSA ACE/Server and SecurID | application | Security Dynamics (now RSA Security) | mature | active |
| CGI (Common Gateway Interface) | protocol | NCSA/IETF standard | mature | obsolete |

### Observation Summary

- **Total observations:** 24
- **By type:**
  - actual-outcome: 2
  - benchmark-result: 1
  - expert-opinion: 1
  - framework-factor: 2
  - market-data: 3
  - strategy-classification: 3
  - technology-assessment: 10
  - viability-prediction: 2

---

*Copyright © 1996 Aberdeen Group, Inc., Boston, Massachusetts. Archived for research purposes under CC-BY-4.0.*
*Source: [https://web.archive.org/web/19970604103320/http://www.aberdeen.com:80/secure/profiles/proweb/body.htm](https://web.archive.org/web/19970604103320/http://www.aberdeen.com:80/secure/profiles/proweb/body.htm)*
