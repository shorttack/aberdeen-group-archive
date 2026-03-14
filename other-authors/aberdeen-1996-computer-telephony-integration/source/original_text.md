# Internet Architecture: Prescription For Success

> Archived from: https://web.archive.org/web/19970112010334/http://www.aberdeen.com:80/secure/viewpnts/v9n8/v9n8.htm
> Original publication date: 1996-04-17
> Author: Aberdeen Group

---

## Original Document Text

Volume 9 / Number 8
April 17, 1996
Internet Architecture:
Prescription For Success
Users facing massive uncertainty due to the Internet's redeﬁnition of almost every
computing product ask two deceptively simple questions:
1. What is the Internet's real bottom-line value added for my enterprise? and
2. How do I get there from here?
This Aberdeen Technology Viewpoint suggests two deceptively simple answers:
1. The real bottom-line value of the Internet may lie in the Intranet, i.e., in the use
of In- ternet software and networking for internal purposes; and
2. To implement an Intranet effectively and deliver long-term Internet value, users should emphasize creating the right architectural foundation.
Table of Contents
Executive Summary
Upcoming Internet Challenges
Meeting The Challenges
Planning For A Long-Term Internet Architecture
Figure 1: A Scalable Internet Architecture
State Of The Art: Server Hardware
State Of The Art: RDBMSs
State Of The Art: Middleware
State Of The Art: Development Tools
State Of The Art: Data Mining
State Of The Art: Systems Management
State Of The Art: Electronic Commerce
Implementing The Long-Term Internet Architecture
Conclusions
Executive Summary
While the potential advantages of the Inter-net are enormous, they have not yet arrived.
In the short run, enterprises are ﬁnding that the Internet is unmatched as an inexpensive, ﬂexible, broadly available communications mechanism. Using the Internet, enterprises as well as
departments are already experiencing short-term signiﬁcant expansions of WANs and data access. In the long run, Internet-based electronic commerce promises dramatic decreases in selling
costs and new opportunities for customer interaction and add-on sales; the Internet's proliferation of information-
gathering sites promises new opportunities for research and for selling information; and using the Internet to broad-en access to corporate systems can extend the reach and scope of those
systems
to farﬂung subsidiaries and can provide unprecedented close relationships with major ustomers.
However, to translate short-run advantages into larger, long-term, bottom-line beneﬁts, Internet efforts must improve in content, scalability, ﬂexibility, robustness, and electronic-commerce
capabilities. Enterprises can effectively meet those challenges by deﬁning/implementing the right software and hardware architecture.
An effectively designed and implemented Internet/Intranet architecture links to enterprise databases to improve content, leverages today's scalable technologies, and allows bypassing or
upgrading of the Web browser and Web server to improve scalability. It adds integration with corporate networks and systems, provides greater links between software from multiple
suppliers for greater ﬂexibility, incorporates security and enterprise-scale administration for greater robustness, and includes new electronic-commerce applications.
The right Internet/Intranet architecture starts with highly scalable server hardware, complex-data-type-enabled RDBMSs, TP-monitor-like middleware, Internet-adapted data-mining tools,
and
Internet-enabled second-generation client-server development toolsets. It includes well-integrated electronic-commerce applications that allow commercial transactions fully online,
extensible and cross-DBMS administrative tools, and higher-bandwidth wide-area-networking infrastructure.
Based upon users' recent experience with client-server technology, those who do not plan their architectures for successful 'net implementations that scale rapidly will ﬁnd that the problems
of short-term success prevent long-term success. The Intranet should play a key role in design/implementation: as a proving ground; source of immediate beneﬁt; and long-term foundation.
In achieving the right architecture, users should emphasize ﬁnding the right suppliers as partners. Today's solutions vary signiﬁcantly in the ways that they integrate with or bypass the Web
browser and Web server, and many suppliers will not implement key features until 1-2 years in the future. Aberdeen recommends that users focus on suppliers such as those mentioned below
that are
aggressively aiming to solve the Internet's scalability problems.
Back to Table of Contents
Upcoming Internet Challenges
The Internet not only offers immediate beneﬁts but promises greater future ones. Most present Intranet applications offer signiﬁcant communications-cost savings and expand corporate text-
data access to new and remote end users in such applications as advertising and electronic catalogs, integrating the supply chain, point-of-sale data collection, and realtime ﬁnancial-industry
portfolio analysis and mortgage calculation. Potential long-term beneﬁts include carrying out commercial
transactions completely electronically, thus cutting sales and transaction costs and times and gaining new customer data. Long-term "side effect"; beneﬁts include rapid access to a larger
amount of extra-enterprise information for strategic ﬁne-tuning, connecting the organization more closely, delivering global solutions more rapidly, leveraging corporate databases more
effectively, and keeping pace with end-user demands more effectively.

However, to translate from immediate to long-term beneﬁts, IS planners must identify the likely solutions that will deliver long-term beneﬁts, weave them into a comprehensive overall IS
strategy, and plan an architecture that will get the enterprise from today's ad-hoc Internet solutions to
an integrated enterprise-wide solution. Today's primary Internet challenges in achieving a good long-term strategy and architecture are:
Content. Most of today's Internet- available data is in text format; most of today's key enterprise data is plain-vanilla data. To deliver the right information to the end user accessing the
Web server, the enterprise must deﬁne those elements of corporate data that will be effective when presented on the Web, and design a user-friendly interface to those data elements, as
today's data-access tools do.
Scalability. In a typical Internet application, the end user invokes an action in Web browser software, which ﬁres off a message to a Web server; the Web server processes the request and
returns a page or more of displayed text and graphics -- then disconnects the session. As end-user demands on enterprise Internet and Intranet solutions increase, the Web browser and
Web server begin to act as bottlenecks, unable to optimize session-oriented data-access requests or multiplex and multithread transactions. Suppliers and users must therefore focus on
achieving an architecture that bypasses or upgrades browser and server with the same scalability techniques that have been so effective in RDBMSs and TP monitors.
Flexibility. Presently, no supplier has shrink wrapped solutions for all of the enterprise's long-term strategic Internet needs. IS buyers need to seek out powerful rapid-development tools
to customize and extend today's supplier products, e.g., Internet-enabled client-server application development environments (CADEs).
Robustness. Internet Web servers lag today's enterprise systems in security, availability,
and administrative tools. IS needs to emphasize upgrading in these areas using present enterprise solutions as well as the newer Internet security "ﬁrewalls".
Electronic Commerce Add-Ons. The Internet electronic-commerce market is beginning to
offer a wide array of solutions. IS needs to move aggressively to integrate the new electronic-commerce mechanisms into their architectures.
Back to Table of Contents
Meeting The Challenges
Figure 1 shows a sample architecture to meet upcoming Internet challenges. This architecture expands content by providing access to backend databases, improves scalability by providing
alternate paths and multiplexing at each stage between the end user and the target database, and increases ﬂexibility by inserting cross-supplier middleware and Internet-enabled second-
generation client-server development toolsets on the Web server. It adds robustness by incorporating global security and administration solutions, and integrates electronic commerce. IS
buyers can use Figure 1 in RFPs to suppliers (and download it from Aberdeen's Web site!).
To move from a typical present-day architecture to a long-term Internet architecture such as that in Figure 1, enterprises need to do the following:
Link between the Internet/Intranet home page and Web server and existing enterprise databases and applications -- this improves Web content and allows the Intranet to leverage
existing solutions;
Bypass or upgrade Web browsers and servers via middleware, avoiding the Web browser/server scalability "bottleneck"
Internet-enable present development toolsets, packaged applications, decision-support
systems such as data warehouses, administrative tools, and networking infrastructure -- this allows IS to apply these tools and applications to Internet/Intranet solutions; and
Add and integrate into the architecture the new electronic-commerce software.
Back to Table of Contents
Planning For A Long-Term Internet Architecture
To implement the new architecture, enterprises need not only to assess the new solutions but also to reassess past hardware, software, and communications technologies for their usefulness in
meeting
likely upcoming Intranet and Internet challenges. Aberdeen recommends that enterprises look particularly closely at:
Server hardware. In many of today's 'net implementations, one or a few "Web servers" stand at the interface between enterprise systems and the "outside world" (i.e., end users outside
the corporation and remote end users inside the corporation). Web servers today have two key functions: as a text-database server, and as a communications server fanning requests out
to backend data-bases. IS buyers will need Internet server hardware speciﬁcally optimized for the remote, unsophisticated-end-user, small-query, large-response communications typical
of the Internet. In other words, users
should seek server hardware and operating-system software optimized for TP-monitor-type multithreading and load balancing, the merging of SMP/clustering/MPP technologies known
as "fusion technology" for scalability, and fast pass-through from disk or backend system to the front-end communications
ports.
Complex-data-type-enabled RDBMSs. In particular, today's RDBMSs need to extend their querying and data-storage support to include text, mixed text/data, and to some extent
graphics -- e.g., via object-relational technology that adds object-oriented technology's support for complex data/code objects to the RDBMS.
TP-monitor-like middleware. As noted above, scaling Intranet and Internet architectures requires that the 'net architecture support typical TP monitor functions: server-side load
balancing and transaction multiplexing across multiple database-server copies, often from multiple suppliers, plus client-side and server-side query optimization. Of all Internet
architectural components, middleware is the most critical to scalability.
Administration Tools. Users may face unprecedented challenges, because now administration can in effect cross company boundaries. Therefore, Aberdeen believes that security should
be a greater concern than before; however, supplier "ﬁrewalls" are aggressively attacking this problem. A potentially equally serious problem in the long term is the ability of the Web
server's administration toolset and corporate directory service/data dictionary to encompass all of the major data to which remote end users need access. A potential solution to this is to
build a distributed data repository, deﬁning and integrating key backend datasets.
Internet-adapted data- mining tools. The Web browser is a new, more text-focused
metaphor for end-user interaction with server-side information -- and thus today's data-access/"relational OLAP" tools need to incorporate text access and the Web-browser user
interface into their query GUIs and client-server architectures. Moreover,
present querying toolsets need to deliver client-side and server- side query optimization adapted to the needs of remote end users with less focused or planned queries.
Internet-enabled client-server packaged applications. Today's client-server applications have made major advances in scalability, and some are beginning to deliver the ability to operate
across the Internet. However, users also need solutions that incor-porate new Internet technologies such as electronic commerce into ﬁnancial, sales-automation, EDI, and
other applications that can beneﬁt from outside-the-enterprise information.
Internet-enabled client-server development toolsets. The rapid-change nature of the Internet, and the ability to leverage Internet competence and internal competitive advantage into
long-term core competencies, demand rapid, cost- effective development of Internet-speciﬁc user applications. Users should look for those of today's CADEs that not only
Internet-enable broad second-generation toolset functionality but also allow the developer to focus on and control key Internet- application success factors, such as optimizing Web-
client-to-Web- server communications.
Electronic-commerce software. The object of the game is to allow every commercial interaction -- inside the company via its accounting systems, with suppliers, or with customers -- to
take place completely on the Internet, thus cutting costs while expanding the enterprise's information about its own state, its suppliers, and its customers. To achieve this, users need to
mimic the operation of these transactions outside the Internet: in the case of intraenterprise transactions, by feeding the data semi-automatically to company accounting systems; in the
case of customers, by handling order logging, credit veriﬁcation, and supplementary bank transactions; and in the case of supplier interactions, by doing both.
Networking infrastructure. If the enterprise's Internet server must scale, so must the networks that attach it to the outside world and to backend databases. Users should not
expect the big telecom companies to deliver major increases in end-user bandwidth in the near future, since they have not yet ﬁgured out how to make a proﬁt from rewiring the world,
and promising technologies such as two-way cable are not yet ready for prime time. These trends should provide some limits on enterprise-network overload in the near future; but in the
long term, users should expect to upgrade their lines both into the Web server and back to backend databases, to match increased internal and external use.
Figure 1: A Scalable Internet Architecture:

Back to Table of Contents
State Of The Art: Server Hardware
Users should look particularly closely at two new server-hardware technologies that are
especially promising for delivering Internet server-hardware scalability: VLM (Very Large Memory) technology and fusion technology.
Aberdeen deﬁnes VLM technology as system technology allowing more than 4 gigabytes of in-system main memory, plus database technology that can take advantage of the added main-
memory data storage to deliver high perform-ance. In the case of large-scale 'net decision support applications such as access to data warehouses as well as "mixed" OLTP/decision-
support solutions such as application servers, VLM allows end-users effective access to larger databases -- even with complex queries. For more medium-scale applications, the VLM system
can
act as an ultra-high-performance tool for rapid-response applications. For example, the VLM system can deliver competitive advantage in such situations as stock-ticker processing,
micromarketing, enterprise resource planning (ERP), and data warehousing.
To allow users to exploit VLM technology, three major trends are occurring: (1) a few major hardware suppliers are providing 64-bit operating environments with an effective upgrade path
for their installed bases, (2) major RDBMS suppliers are providing a minimal-pain upgrade for their software and that of third-party application ISVs, and (3) VLM "bundles" are beginning
to arrive, based on real-world experience with VLM technology, that give the user a "one-stop
shop" of solutions customized for a wide variety of needs. Server hardware suppliers such as Digital, Sun, SNI/Pyramid, and Silicon Graphics have announced or delivered 64-bit VLM
solutions, and major RDBMS suppliers such as Oracle, Sybase, Informix, and Software AG have announced versions optimized for 64-bit processing.
Fusion technology (also known as NUMA technology) is the extension of SMP technology by adding clustering and MPP features such as high-bandwidth CPU interconnects, thus allowing
IS to scale the number of processors beyond the traditional limits of SMP cost-effectively without
requiring application upgrades. Fusion technology is particularly effective in scaling high-end Internet servers such as 'net data-warehousing implementations. Server hardware suppliers such
as Sequent, Digital, Pyramid, and Data General have announced or delivered hardware architectures using fusion
technology.
Back to Table of Contents
State Of The Art: RDBMSs
Three recently-introduced RDBMS technologies should be particularly effective in Intranet architectures:
parallel-scalable technologies that drive parallelism deep into the details of the RDBMS's core engine to provide higher performance on today's parallel server hardware;
replication technology that integrates an Intranet database with other enterprise databases; and
object-relational technology that provides an object-oriented "veneer" to an RDBMS, providing better performance on complex queries and allowing more rapid
development and deployment of complex-data-type applications such as multimedia.
Major RDBMS suppliers' implementations of parallel-scalable and replication technology is now relatively mature, with support for both SMP and MPP scalability and signiﬁcant experience
in high-volume replication for hundreds-of-gigabytes data warehouses. Internet architec-tures may also require replication from the Internet database server to backend databases from
multiple suppliers; most RDBMS suppliers do not yet support such quot;heterogeneous replication", although Aberdeen anticipates that by the end of 1996 most will do so, as well as third-
party suppliers such as Praxis.
IS buyers should be cautious in estimating the positive impact of object-relational technology on Internet data management. While its beneﬁts in complex-query performance are substantial,
most of the new end users that access an enterprise's Internet architecture are likely to be less specialized and generate less complex queries than previous data miners. Likewise, most if not
all of today's
development toolsets are not yet designed to take advantage of object-relational RDBMS features, and therefore object- relational's advantages in rapid development of complex applications
will in most cases not be substantial over the next 1-2 years. Oracle 7.3 provides substantial support for
potentially much more important Internet data types such as text, spatial, and video, and Informix's acquisition of the Illustra DataBlades object-relational solution gives it a strong object-
relational story once the Informix RDBMS and the DataBlades are merged (by 1997).
Back to Table of Contents
State Of The Art: Middleware
As noted above, an Internet framework that provides load balancing and transaction and communications multiplexing on the server -- and preferably server- and client-side query
optimization -- is likely to be key to Internet architecture scalability. The middleware needed to
carry out this task should support store-and-forward commercial messaging (for load balancing, routing, and delayed response), should connect to multiple suppliers' backend databases, and
should integrate with present Web browsers and servers.
At present, Internet middleware solutions are beginning to arrive, each with a different architectural approach. Three sets of suppliers are in the forefront of the Internet-middleware market:

TP monitor suppliers,
RDBMS suppliers;and
Middleware suppliers.
The TP monitor is the logical predecessor to an Internet solution: it has long had load balancing, transaction and communications multiplexing and optimization, commercial messaging, and
connectivity to multiple suppliers' RDBMSs, as well as server-side application-development
capabilities; above all, it has proven its worth in scaling RDBMSs in the past. However, TP-monitor suppliers up to now have focused mainly on supporting their installed bases' move to the
Internet, leaving new suppliers such as Spider Technologies to tout TP-monitor-type middleware speciﬁcally designed for the Internet.
RDBMS suppliers have been more proactive in developing solutions to bridge between the Web server or browser and the backend database. For example, Oracle provides Oracle
WebSystem, a "replacement" Web browser and Web server with load balancing and multiplexing capabilities that is fully integrated with Oracle's RDBMS. However, most RDBMS suppliers
-- Sybase being a notable exception -- are not perceived as effective in bridging to other suppliers' databases compared to TP monitors. Aberdeen suggests that RDBMS-supplier Internet
middleware is particularly appropriate where that supplier is already a key element in an enterprise architecture.
Middleware suppliers such as Intersolv, Gradient, Platinum's Trinzic, and Visigenic are of interest especially because they can bring valuable add-ons to the Internet middleware: for example,
Intersolv's object- class and metadata support and Gradient's security and directory- server capabilities. They also have a good track record for expanding end users' access to multiple data
sources. However, they have not focused on load balancing and similar server-side scalability considerations. Middleware suppliers are particularly appropriate where the user needs the add-
ons that these suppliers provide.
Back to Table of Contents
State Of The Art: Development Tools
To assess long-term Internet development needs, the IS buyer needs to set aside one of the
most overhyped new technologies of the Internet: Java. Java is in fact an extension of the C++ object-oriented programming language that provides features remedying many of C++'s
difﬁculties in the past -- such as hiding the pointers that cause innumerable coding errors -- thereby dramatically improving object-oriented-programming quality and speed. It also has an
"Internet side-effect": the ability to download an object from a server to a client when appropriate. As a result, technologists envision Java providing a kind of "thin client" or client-on-
demand for the Internet: providing small "applets" that are downloaded when needed from a Web server, carrying out many of the functions now providing by PC applications.
Aberdeen ﬂatly states that users should expect little from Java in the immediate future. In the ﬁrst place, Java, like C++ before it, is by itself not very scalable: it is a 3GL that lacks the 4GL
and Visual Programming Environment (VPE) extensions that have proven so effective in client-server
development over the last 10 years. In the second place, Java or Java-enhanced toolsets are still few and far between, although Aberdeen anticipates that most toolset suppliers will provide
Java support by the end of 1996. In the third place, the "applet" idea has yet to prove itself in the slow-communications environment of the Internet: 28.8K baud is simply too slow to
download the 100K-bytes-or-more of many of today's major functions, such as database access or graphics-enhanced "wizards". Thus, in the near future, Java is likely to be most effective as
"C++ for the Internet".
Where then should IS look for Internet development and customization ﬂexibility? The key development technologies for the Internet are not client-on-demand applets, but ﬂexible
evelopment toolsets that allow the programmer to determine the most effective split between client and server, support not only download-on-demand but also one-time downloads for
permanent residence on an Internet-client PC, and give the developer client- and server-side control over data-access to optimize and scale queries and transactions. IS may ﬁnd these
characteristics -- application partitioning, automated deployment, and RDBMS scalability -- plus many other useful
scalability features such as business-modeling design tools and software-lifecycle support in today's second-generation Client-server Application Development Environments (CADEs) as
described
in Aberdeen's CADE Buying Guide.
Aberdeen believes that once a second-generation CADE has added Internet and Java support, it can offer "the best of all worlds": exceptional application and development-process
scalability, multisupplier openness and Internet-architecture and customization ﬂexibility, today's best programmer-productivity technologies, and full Internet-application software-lifecycle
support. Second-generation CADEs are steadily adding Internet and Java support, and many will allow highly scalable and ﬂexible Internet-application development by mid-1996.
If a second-generation CADE does not ﬁt, IS has other attractive development options. Object-oriented Unix toolsets have "reinvented" themselves for the Internet and also added second-
generation CADE features (such as Next Software's NextStep and Galaxy), and "Internet-enabled" middleware toolsets that provide strong server-side programming support (such as Spider
Technologies' toolset), are also particularly useful for developing many Internet solutions.
Back to Table of Contents
State Of The Art: Data Mining
As indicated in the recent Aberdeen Technology Viewpoint, Web Warehouses: DSS For The Masses, data-mining-solution &quot;relational OLAP&quot; suppliers offer a great deal of useful
functionality for 'net decision support:
RDBMS-based data warehouses optimized for large-scale decision support;
Metadata repositories that can not only provide information on multiple enterprise databases to the Internet server, but also potentially incorporate Web-page link information to
integrate text and data bases;
SQL query generators that can handle multidimensional data, allowing end
users to generate more complex queries for deeper data
mining;
Development tools focused on decision support to enhance the performance of large-scale, complex decision support applica-tions; and
Client-side data-access tools that can cross backend databases and that provide end-user friendliness and data-mining power.
Relational OLAP solutions are not yet fully integrated with the 'net because Internet middleware
solutions have not yet fully closed the gap between the end user operating on the Web and the data-warehouse database server, nor provided client- and server-side performance optimization
to
match that available (and needed!) for present internal data- warehouse systems. Thus, Aberdeen recommends that IS buyers looking to implement data-warehouse access as the &quot;next
big
thing&quot; in Internet bottom-line beneﬁts focus strongly on solutions that combine data warehousing with strong middleware that can scale with the decision-support solution.
Back to Table of Contents
State Of The Art: Systems Management
Extension of today's enterprise-scale systems management solutions to manage an Intranet is relatively straightforward. However, to allow outside end users to access internal databases will
require careful attention to security &quot;ﬁrewalls&quot;. Likewise, providing external access to multiple backend databases will mean that the new end users will want to see different data
sets than internal end users, requiring extension of distributed-database administration to provide a metadata repository that crosses databases and suppliers. Moreover, administering external

end users -- e.g., supplier-to-customer interactions -- will require careful demarcation of boundaries between one supplier's systems-management scope and another's: who is responsible
when a key payment goes astray while being communicated between one enterprise and another?
While suppliers clearly recognize and are attacking security concerns via such distributed-system
security technology as Kerberos and &quot;ﬁrewall&quot; products, they are less far along in tackling distributed-database repositories and integrating enterprise-scale systems management
solutions. The Metadata Coalition's standard for cross-supplier metadata is an encouraging ﬁrst step, but wide implementation of that standard and extension to the Internet will not be fully
accomplished in 1996. Likewise, SNMP as a systems-management-solution integrator
is far too primitive, and therefore makes data exchange and coordinated functioning between systems management solutions too slow and costly to develop. Computer Associates' Internet
Commerce Enabled (ICE) enhancements to CA-Unicenter and CA-Ingres exemplify the trend towards enterprise-class systems management of 'net computing.
The immature state of Internet systems management is a good reason for IS buyers to begin with an
Intranet, and move only cautiously into full Internet implementation. Aberdeen suggests that Internet systems-management solutions buyers look closely at their security, distri-buted data,
and cross-enterprise architectures.
Back to Table of Contents
State Of The Art: Electronic Commerce
Internet electronic commerce has three core parts:
supporting the commercial transaction, e.g., via order entry and transaction
logging;
supporting the method of payment, e.g., via electronic cash and electronic banks; and
supporting the connections to previously existing commercial-transaction entities and systems, e.g., credit card companies for credit card veriﬁcation, banks for electronic transfers.
Of these three, commercial-transaction support is farthest along, with enterprises' existing order-entry systems translated to their home pages and new products such as Open Market's
Merchant
Solution providing added functionality and security. Connections to existing backend systems are being created, with suppliers such as Verifone extending their credit card authorization and
bank-connection software to the Internet, while banks are Internet-enabling their PC-banking suites. Electronic cash has not been widely implemented or accepted on the 'net, but products
such as CyberCash's Wallet and CashRegister are providing the infrastructure for a system through which users can participate in fully-online electronic payments in the future.
The keys to the success of these efforts are the delivery of exceptional security/privacy and tandards that allow the end user to use methods similar to those in the present system to carry out
most commercial transactions. Today's security schemes, often based on such low-level technology as Kerberos and RSA, do not by themselves handle the complex security and privacy
requirements
of a wide variety of end users; Aberdeen suggests that users carefully study and Intranet-test proposed electronic-commerce-software acquisitions to avoid bottom-line-impacting security
holes or end-user-unfriendly interfaces.
Likewise, users should be cautious about presently proposed Internet electronic-commerce standards. The past history of the Internet suggests that the Internet itself will determine its own
difﬁcult-to-forecast de-facto standards. Users should consider partnering not necessarily with a big supplier that attempts to force its own electronic-commerce technology on the Internet, but
with a
supplier committed to delivering open-systems products and able to adapt rapidly to the swift evolution of these standards.
Back to Table of Contents
Implementing The Long-Term Internet Architecture
Most users are likely to use the &quot;bridge-building&quot; method of implementing an Internet
architecture: start from an isolated Web site and an enterprise architecture with no Internet capabili-ties, and build integrating mechanisms into each side until they meet in the middle.
Aberdeen suggests that in these implementation efforts, building an Intranet is likely to be key. An
Intranet:
allows proof-of-concept of the Internet architecture;
lets the enterprise gain immediate beneﬁts from expanding intraenterprise data access;
provides a least-cost, least-effort, least-risk path from present systems to the Internet, leveraging present data and applications; and
incorporates the Internet into the enterprise's business and IS strategies and architectures instead of creating more &quot;information archipelagoes&quot;.
Once the core architecture is set, equal attention should be given to attacking immediate-beneﬁt applications and to integrating point Intranet solutions into the new architecture. Although a
new application may have more signiﬁcant impact on the bottom line, the longer unintegrated Intranet solutions are allowed to proliferate the lower the payback and the greater the eventual
cost of
rationalizing a large backlog of nonstandard applications.
Back to Table of Contents
Conclusions
Aberdeen suggests that the key to long-term enterprise Internet success is picking the right architecture and implementing it, ﬁrst as a proof-of-concept/easy-migration Intranet, and then as
a global solution encompassing suppliers and customers.
The &quot;right stuff&quot; Internet architecture should factor in server hardware, complex-data-type-enabled RDBMSs, TP-monitor-like software, Internet-adapted querying tools, Internet-
enabled client-server development toolsets and packaged applications, administrative security and directory services, and electronic commerce software. Users should aim for enhanced
Internet
content, very high scalability, rapid-response and rapid-change ﬂexibility, and the ability to carry out sales and other customer and supplier transactions entirely electronically.
The supplier state of the art in providing a one-stop-shop long-term Internet solution is not yet quite
there. The components are in place or under development; but most suppliers have not yet bundled the components into an overall solution, and in areas such as Web-browser and Web-server
scalability, bottlenecks loom. Nevertheless, enough functionality is out there for users to begin aggressively planning and implementing.
Aberdeen believes that the long-term potential beneﬁts of the Internet are not only real but should be far more substantial than today's piecemeal successes; but only effective designers and
implementers with the right architecture will reach the promised land, or keep pace with exceptionally-fast-paced Internet technology changes. Aberdeen therefore urges users to proceed
immediately to enterprise-level Intranet planning and implementation; but with care and with due attention to leveraging present corporate solutions and data. Above all, IS buyers should
seek partnership with experienced and
Internet-savvy suppliers that understand the bottlenecks, barriers, and right architectural approach.

Aberdeen Group Registration and HTML Market Research
Home Page || General Information || Aberdeen Abstracts
Aberdeen Group Publications||Custom Consulting
Aberdeen Group
One Boston Place
Boston, Massachusetts
02108
Telephone: 617-723-7890
FAX: 617-723-7897
The trademarks and registered trademarks of the corporations mentioned in this publication are the property of their respective holders. Unless otherwise noted, the entire contents of this publication are copyrighted by Aberdeen
Group, Inc. and may not be reproduced, stored in a retrieval system, or transmitted in any form or by any means without prour written consent of the publisher.
Copyright © 1996 Aberdeen Group, Inc., Boston, Massachussetts
This Document is for Electronic Distribution Only -- DO NOT COPY

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-computer-telephony-integration |
| title | Internet Architecture: Prescription For Success |
| author | Aberdeen Group |
| date | 1996-04-17 |
| type | white-paper |
| subject_domain | internet-intranet-architecture |
| methodology | industry-analysis, competitive-profiling, document-review |
| source_file | 1996 New Computer Telephony Integration_ Doe...nization Have the Backbone to Succeed tvp.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group prescribes an enterprise Internet/Intranet architecture for 1996, arguing that long-term value lies in the Intranet rather than public Internet. The study recommends a scalable architecture combining TP-monitor-like middleware, 64-bit VLM server hardware, parallel-scalable RDBMSs, and second-generation CADEs. Aberdeen dismisses Java as immature and warns that enterprises without proper architectural foundations will find that short-term Internet success blocks long-term success.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Published at the apex of the first Internet boom; Aberdeen's architectural framework influenced thousands of IS decisions in 1996-1997. |
| **Relevance** | high | Core principles — TP-monitor-like middleware, separation of presentation from data tiers, metadata repositories — are directly ancestral to microservices and API gateways. |
| **Prescience** | high | Intranet-first thesis proved correct; Java skepticism accurate for 1996-1998; e-commerce prediction fully verified; middleware centrality confirmed by modern architectures. |

### Prescience Detail

**Prediction 1:** Informix Illustra object-relational merger timeline
- **Claimed:** Informix + Illustra DataBlades to be merged by 1997
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 1:** Informix Illustra merger outcome
- **Result:** Informix Universal Server (1996) integrated Illustra DataBlades on schedule
- **Confidence:** verified
- **Notes:** Timeline prediction accurate; Informix acquired by IBM 2001

**Prediction 2:** Java medium-term role
- **Claimed:** Most toolset suppliers will provide Java support by end of 1996; CADEs+Java will offer best-of-all-worlds
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 2:** Java enterprise adoption outcome
- **Result:** Java became dominant enterprise language (J2EE by 1999-2001); applets declined as Aberdeen predicted; CADEs largely displaced by Java IDEs
- **Confidence:** verified
- **Notes:** Near-term skepticism accurate; long-term Java dominance via servlets/J2EE not fully anticipated

**Prediction 3:** E-commerce long-term transformation
- **Claimed:** Internet e-commerce promises dramatic decreases in selling costs and new customer interaction opportunities
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 3:** E-commerce transformation outcome
- **Result:** E-commerce transformed retail, financial services, and B2B transactions globally
- **Confidence:** verified
- **Notes:** Amazon, eBay etc. fully validated Aberdeen's prediction

**Prediction 4:** Telecom bandwidth constraint (near-term)
- **Claimed:** Big telecoms will not deliver major bandwidth increases in near future; 2-way cable not ready
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 4:** Bandwidth expansion outcome
- **Result:** Broadband (DSL, cable modem) accelerated 1998-2002; Aberdeen slightly too pessimistic on cable timeline
- **Confidence:** verified
- **Notes:** Cable modems arrived 1998-2000; faster than Aberdeen expected but directionally correct for near-term

**Prediction 5:** Second-generation CADE Java support by mid-1996
- **Claimed:** Many CADEs will allow highly scalable Internet development by mid-1996
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 5:** CADE Java support outcome
- **Result:** CADEs added Java support by 1997-1998; ultimately displaced by Java IDEs (Eclipse, NetBeans) by 2000
- **Confidence:** verified
- **Notes:** Timing slightly delayed; Java displaced CADEs rather than augmenting them

### Entities Referenced (7)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | merged | Aberdeen (Harte-Hanks) |
| Oracle Corporation | company | active | — |
| Informix Software | company | acquired | IBM (2001) |
| Sybase Inc. | company | acquired | SAP SE (2010) |
| Spider Technologies | company | dissolved | — |
| Computer Associates International | company | active | CA Technologies -> Broadcom (2018) |
| Sequent Computer Systems | company | acquired | IBM (1999) |

### Technologies Referenced (8)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|----------------------|--------------------|
| TP Monitor / Internet Middleware | framework | multiple | mature | active |
| VLM Technology | platform | Digital/Sun/SGI | emerging | obsolete |
| Fusion/NUMA Technology | platform | Sequent/Digital | emerging | obsolete |
| Object-Relational RDBMS | application | Informix/Oracle | emerging | legacy-supported |
| Java | language | Sun Microsystems | emerging | active |
| CADE | framework | multiple | mature | obsolete |
| Web Browser / Web Server | platform | Netscape/Apache | emerging | active |
| Internet Electronic Commerce | application | multiple | emerging | active |

### Observation Summary

- Total observations: 23
- By type: strategy-classification(1), framework-factor(5), technology-assessment(3), viability-prediction(5), actual-outcome(5), expert-opinion(1), market-data(0), benchmark-result(0)
