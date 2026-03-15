# IBM Extended Transaction Systems Family
## Original Source Text

**Source URL:** https://web.archive.org/web/19970604113249/http://www.aberdeen.com:80/secure/profiles/1997/ibmetsf/ibmetsf.htm  
**Publisher:** Aberdeen Group, Inc., Boston, Massachusetts  
**Copyright:** Copyright 1997 Aberdeen Group, Inc.  
**Archived:** Wayback Machine, June 4, 1997

---

The Wayback Machine - https://web.archive.org/web/19970604113249/http://www.aberdeen.com:80/secure/proﬁles/1997/ibmetsf/ibmetsf.htm
IBM Network Computing
IBM Extended Transaction Systems Family
Executive Summary
The advent of network computing has not decreased enterprises’ demands on
mission-critical transaction-processing solutions; and it has increased the
challenges to IS in implementing and scaling them.
Ever-ﬁercer competition and a stronger focus on the customer means that
systems processing customer transactions are a key ingredient in enterprise
bottom-line success. New network-computing architectures such as the Internet
and Intranets are "extending the application’s reach": cost-effectively adding
new TP-application end users – remote and global intra-enterprise personnel as
well as extra-enterprise electronic-commerce customers – and encouraging new
applications such as electronic commerce that require support for new
transaction patterns. These architectures also add Web browsers and Web server
software to the architecture, often creating scalability bottlenecks.
To meet these challenges, organizations need transaction-processing
infrastructure that is ﬂexible (i.e., it can handle the new architectures and
technologies without requiring massive code rewrites, and can change rapidly
in response to new customer needs and IS strategies); cost-effectively scalable
(i.e., it can apply and leverage the scalability technologies of the past in the
new environments); robust in the tradition of today’s mission-critical
applications; and programmer-productive for rapid solution customization and
adaptation.
IBM’s Extended Transaction Systems (ETS) product family offers
infrastructure solutions targeted at transaction-processing
performance/scalability, availability/reli-ability/manage-ability, platform
independence and interoperability, and rapid application development. ETS
includes IBM’s hot-technology MQSeries commercial-messaging product,
Lotus Notes for collaborative-computing support, Transaction Server with the
CICS and Encina transaction monitors for TP-monitor functionality, and
Database Server (based on IBM’s DB2 RDBMS), plus Internet Connection
Server access to IBM’s IMS mainframe data-management software.
These products are notable especially for their value-added technology – e.g.,
MQSeries’ ability to deliver high-performance, robust, platform-independent
communications between application components – and their broad popularity
– e.g., the omnipresence of CICS and IMS in the mainframe world, or Lotus
Notes on LANs. Transaction Server and MQSeries provide added value in
many situations through security, application-development support, and
systems management features.
For present IBM customers moving to network computing, ETS provides a
relatively risk-free and less costly migration path by leveraging tried-and-true
solutions. For both IBM and non-IBM customers, ETS delivers a way to add
important Web-enabled upcoming technologies such as a messaging
architecture, groupware and workﬂow, and the TP-monitor-based middleware
that is crucial to scaling Intranet data-intensive applications.
Technology Overview: Embedded Experience Plus New
Technologies
Aside from being widely popular in many cases, ETS products deliver features
that especially valuable for network-computing transaction processing. These
include MQSeries scalability as a messaging architecture for Internet/Intranet
distributed databases or 3-tier applications; users’ ability to implement
network-computing workﬂow via Lotus Notes; Transaction Server’s ability to
provide the load-balancing server-side scalability and security that today’s Web
servers typically lack; and DB2’s multimedia support that today’s Web-site
electronic-commerce applications typically demand.
Table 1: IBM Extended Transaction Systems Product Suite
Product
Features
MQSeries
store-and-forward messaging with queuing
supports location-/connection-independent
application coding

support for Unix, OS/2, Windows NT, Digital
VAX, and IBM MVS servers, and Unix, DOS,
OS/2, and Windows/95/NT clients
Lotus Notes
popular LAN groupware solution
new Web integration capabilities (e.g., Notes
access from Web browsers, Web access from
Notes clients)
integrated with other IBM network-computing
solutions (e.g., OfﬁceVision, MQSeries,
FlowMark) and E-mail/ofﬁce solutions
includes support for replication, security, mobile
computing
Transaction
Server
supports CICS and Encina TP monitors
can access via gateways from the Internet, Notes
supports IBM object-oriented development
environments
supports a broad range of platforms
Web, Java, and Lotus Notes integration
mainframe-access and security features
Database
Server
based on DB2 database server that includes strong
distributed-database support, multimedia-object
Extenders
also includes Web and multiuser gateways, OS/2
querying tool
IMS
includes application integration with other MVS
tools (e.g., TSO, batch) via MQSeries
MQSeries Internet Gateway (Internet Connection
Server) allows Web browser to connect to IMS (or
DB2) database
MQSeries
A commercial messaging product takes a request for service or piece of data
sent by one program, forwards it – often via intermediate programs and nodes –
and stores it until a program is ready to receive it. Store-and forward messaging
is a key technology for large-scale distributed computing, since it handles
interrupted and delayed communications, minimizes none-to-node routing
times and costs, and makes the location of the receiving program transparent to
the developer and end user. Commercial messaging can add architectural
ﬂexibility, improve performance, enhance enterprise-wide robustness, and
improve programmers’ productivity and program quality. Commercial
messaging can aid application location independence, application partitioning,
and data-warehouse data replication.
Aberdeen ﬁnds that IBM’s MQSeries commercial-messaging product is a
sophisticated solution with performance, robustness, and ﬂexibility features
especially suited to network-computing environments. MQSeries includes
multithreading, traces for testing and monitoring, assured delivery of a message
once and only once, and, on some platforms, single-point-of-control systems-
management enablement. MQSeries also integrates with Powersoft's popular
PowerBuilder CADE as well as IBM's own VisualAge development toolsets
and 3GLs (part of the IBM Application Development network-computing
product family).
MQSeries' robustness includes "connection independence" (the ability to send a
message whether or not the connection to the target is available, with assured
delivery). MQSeries also can provide the messaging "infrastructure" for
transactions, allowing unit-of-work commitment or backout of groups of
messages, and also supporting integration with major popular TP monitors such
as CICS, Tuxedo, and Encina. Thus, developers can ensure that all (or none) of
a set of database updates or series of program-to-program communications is
completed as a single "unit of work". MQSeries supports a broad range of
Unix, Windows NT, and proprietary environments (e.g., Tandem, AS/400, and
MVS/ESA) plus Windows, Windows95, and DOS at the client level. MQSeries
allows simultaneous operation of multiple popular communications protocols,
including TCP/IP, SNA, Netbios, and DECnet protocols.
Lotus Notes
Like IMS in the mainframe-database arena and CICS in the TP-monitor space,
Lotus Notes is today’s most popular product in the LAN groupware market.
Particularly useful are Lotus’ ability to store not just data but documents and
other information in a shared database; its ability to support mobile computing
by resynchronizing laptop and central-server versions when the remote client
logs in; and its highly-popular LAN E-mail integrated with its groupware
capabilities. Lotus Notes Release 4 also includes support for a wide variety of
platforms, security and management features, Note-application development
tools such as LotusScript 4GL or Microsoft’s Visual Basic, integration with
other IBM products via MQSeries and CICS Links, and new Internet-
integration capabilities – e.g., the Internet InterNotes Web Publisher, Web-

browser access to Notes and Notes-client access to the Web, and the Domino
product.
While ETS products such as Transaction Server and Database server stress
support for data-intensive network-computing applications, Lotus Notes adds
two new dimensions to ETS’ network-computing story: collaborative/business-
process computing, and combined-text/data databases. Notes allows IBM’s
network-computing customers to provide end-user collaboration by placing
documents, other ﬁles, and data in shared databases viewed by all, as well as
supporting business processes by ﬂowing data from person to person via E-
mail.
Lotus Notes is particularly effective in enhancing both IBM-customer and non-
IBM-site network computing with these collaborative and text/data-database
capabilities. With its E-mail strengths, it can also serve as a powerful bridge
between present internal E-mail systems and the wider E-mail of the Internet.
Transaction Server
IBM’s Transaction Server is an open TP monitor that includes CICS Internet
and Notes Gateways, CICS Clients, CICS Monitor (the CICS TP-monitor
server), Encina Clients and the DCE Encina Lightweight Client (DE-Light),
Encina Monitor (the Encina TP-monitor server), and underlying Transaction
Management Services supporting both CICS and Encina. Transaction Server
supports traditional TP-monitor functions, including data-management-
transaction load balancing across multiple servers, access to multiple suppliers’
databases, and communications multiplexing.
Aberdeen’s Viewpoint, "Internet Architecture: Prescription For Success" ﬁnds
that of all Internet architectural components, TP-monitor-type middleware is
the most critical to scalability. Scaling Intranet and Internet architectures
requires that the 'net architecture support typical TP monitor functions: server-
side load balancing and transaction multiplexing across multiple database-
server copies, often from multiple suppliers, plus client-side and server-side
query optimization. The middleware needed to carry out this task should
support store-and-forward commercial messaging (for load balancing, routing,
and delayed response), should connect to multiple suppliers' backend databases,
and should integrate with present Web browsers and servers.
A TP monitor such as Transaction Server is therefore a logical predecessor to a
3+-tier and/or Internet network-computing solution: it has long had load
balancing, transaction and communications multiplexing and optimization,
messaging, and connectivity to multiple suppliers' RDBMSs, as well as server-
side application-development capabilities. Above all, it has proven its worth in
scaling RDBMSs in the past. It also includes support for IBM’s object-oriented
development environments, and operates on a broad range of platforms.
Transaction Server includes Web, Java, and Lotus Notes integration features
(e.g., the CICS Gateway for Java), and is DCE-compliant, giving users (and
Transaction Server itself) ﬂexibility to evolve architectures relatively easily.
Since CICS is by far the most popular TP monitor, the Transaction Server’s
CICS implementation should be especially attractive for legacy-application
transaction-processing users moving to network computing. Encina is designed
to support new applications in workstation environments and is therefore
particularly appropriate for new mission-critical solutions. DE-Light extends
DCE/Encina-based applications’ reach by allowing central-server business-
critical-system access from smaller client machines such as hand-held
portables, often in remote local ofﬁces.
Database Server
Database Server is based on IBM’s DB2 RDBMS. DB2 offers competitive and
leading-edge RDBMS technologies plus unmatched integration with today's
corporate and mainframe databases. As a result, DB2 not only allows IS to
create highly scalable and ﬂexible new solutions for OLTP, decision support,
and "mixed" network-computing environments, but also lets these solutions
leverage today's corporate data -- and present applications access the new
databases -- more effectively. DB2 is especially effective in supporting
mission-critical solutions requiring sophisticated DBMS tuning and proven
reliability. In assessing DB2, IS buyers should factor in its wide array of
options and parameters that allow exceptional tuning to ﬁt user needs.
Interoperable DB2 variants include DB2 common server, DB2/MVS, and DB2
Parallel Edition, which provides capabilities similar to those of DB2 version
1.2 for IBM RS/6000 loosely-coupled and SP Massively Parallel Processing
(MPP) hardware.
DB2 provides effective hooks to support Internet-type network computing.
IBM has announced extensive Internet support, including Transaction-Server-
based middleware providing access to DB2 and other suppliers' RDBMSs, and
a World-Wide-Web connection allowing creation of Web applications accessing
DB2 database using HTML and dynamic SQL.
DB2's multimedia support is especially effective for multimedia Web servers.
DB2 provides signiﬁcant support for complex data types, such as "character"
and "double-byte character" data types (for internationalization), and large (up

to 2 gigabytes) data types. DB2 also provides functions to access parts of a data
type, and the ability to insert a data type too large for main memory into the
database from a client ﬁle or CD-ROM. DB2 now offers Universal-Server
bundles of triggers, user-deﬁned data types, and user-deﬁned functions for
particular data types called Relational Database Extenders.
IMS
The IMS portion of the ETS product family provides integration (via MQSeries
for MVS/ESA) of IMS – an IBM-mainframe data-management solution that is
perhaps today’s most-used DBMS – with other MVS utilities – TSO, MVS
Batch, and CICS. The IMS offering also includes the ability to use a Web
browser as the end-user interface for an IMS application, employing Internet
Connection Server as the link between the Web server and the backend
database-server mainframe.
Because of IMS’s mainframe popularity, extending it to network computing via
ETS means that enterprises can make a much larger percentage of mainframe
data processing available to a larger range of end users across network-
computing Intranets. Thus, ETS allows organizations to "extend the reach" of
IMS and allow legacy IMS-based applications to play a part in network
computing.
Meeting Key User Criteria
Flexibility. The key ETS products here are MQSeries and Transaction Server.
These middleware products effectively glue the ETS architecture together.
Moreover, MQSeries’ low cost, availability on most platforms, ease of
installation, and support for location- and connection-independent messaging
communication between applications makes it easy for enterprises to use in a
wide variety of situations, with a wide variety of applications. Transaction
Server extends ETS’ data-management support to mainframes with its
mainframe connectivity, and adds multiple-supplier-database connectivity.
Scalability. Database Server’s DB2 Parallel Edition has proven itself in very-
large-database data-warehousing situations, and TP monitors such as CICS and
Encina are well known for their ability to scale performance, e.g., in TPC
benchmarking. Aberdeen also ﬁnds that MQSeries can deliver performance
approaching that of remote procedure calls (RPCs).
Robustness. MQSeries’ store-and-forward method of communications provides
high availability through failures of source and target systems as well as the
communications paths between them. Likewise, Transaction Server’s TP-
monitor capabilities allow failover from transaction-processing one server to
the next. Database Server provides extensive RDBMS failure-handling utilities
such as backup/recovery and transaction logging. Lotus Notes’
resynchronization features allow end users to recover from local failures by
downloading from the server.
Manageability. MQSeries and Transaction Server, in particular, include support
for systems administration functions that can aid the user in reducing network
computing’s administrative costs.
Where ETS Products Are Most Effective In Network
Computing
ETS products are particularly effective in allowing IBM users to move key
mission-critical transaction-processing applications towards network
computing. Typically, these users have such IBM products as CICS and IMS
already; MQSeries and Internet-integration tools aid IBM customers in moving
easily, at low cost, and with minimal risk to application Web-enablement and
implementation of transaction processing on Intranets.
ETS products also support IS development of new network-computing
transaction-processing solutions, whether by present IBM customers or non-
IBM sites. IBM users can leverage present CICS-, DB2-, or IMS-based
applications in developing new ones; new users can use Transaction Server and
MQSeries to link the new applications not only to the other ETS products but
also other suppliers’ applications and databases. Both types of customer can
add new network-computing capabilities to the new application, such as
business-process workﬂows and collaboration mechanisms (Notes) or
multimedia extensions (DB2 Extenders). IBM’s extensive services should be
especially effective in aiding design and implementation of complex new
network-computing applications.
Aberdeen Conclusions
ETS products combine effective technologies, popularity, and transaction-
processing experience to deliver signiﬁcant advantages in ﬂexibility, scalability,
and robustness that are key to users’ network-computing transaction-processing
success. Technologies such as MQSeries’ store-and-forward commercial
messaging, Database Server’s distributed-database and multimedia support, and
Lotus Notes’ collaborative and business-process groupware complement proven
and widespread solutions such as Transaction Server with CICS and Encina.
Via integration with each other and with new Internet-type architectures, these

products provide an attractively straightforward and low-risk migration path for
mission-critical enterprise-scale transaction processing.
Aberdeen predicts that ETS products should continue to move ahead rapidly
and keep pace with fast-moving network-computing markets and technologies.
For example, Aberdeen anticipates that Database Server will extend its
multimedia capabilities to meet Web-site and Internet needs; that MQSeries
will add third-party and IBM tools supporting particular commercial-messaging
applications such as backup and distributed Object Request Brokers; and that
Lotus Notes will continue to integrate its products and development tools with
the Internet.
ETS is a highly-attractive part of IBM’s network-computing family that
delivers value-added in areas vital to the enterprise’s functioning and bottom
line: mission- and business-critical transaction-processing applications. If there
is one IBM network-computing product family that deserves IS buyers’ closest
attention, this is the one.
AberdeenGroup,
Inc.
One Boston Place
Boston,
Massachusetts
02108 USA
Tel: 617.723.7890
Fax: 617.723.7897
Contact Information:
Susan Rinehart, Client Services Manager(direct #:
617.854.5212)
David Borde, Marketing Manager (direct #:
617.854.5226)
Email: rinehart@aberdeen.com or
borde@aberdeen.com
This Document is for Electronic Distribution
Only
-- REPRODUCTION PROHIBITED --
Copyright 1997 Aberdeen Group, Inc., Boston, Massachusetts
The trademarks and registered trademarks of the corporations mentioned in this
publication are the property of their respective holders. Unless otherwise noted, the entire
contents of this publication are copyrighted by Aberdeen Group, Inc. and may not be
reproduced, stored in a retrieval system, or transmitted in any form or by any means
without prior written consent of the publisher.


---

## Frictionless Data Package Metadata Appendix

**Package ID:** 1997-ibm-extended-transaction-systems-fa-0369fa  
**Archival Date:** 2026-03-14  
**License:** CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)  
**Source File:** 1997 IBM Extended Transaction Systems Family pr.pdf

### Key Entities
- IBM Corporation (ent-ets-001) — Active
- Aberdeen Group (ent-ets-002) — Acquired/continued
- Lotus Development Corporation (ent-ets-003) — Acquired by IBM 1995; sold to HCL 2019
- Transarc Corporation (ent-ets-004) — Acquired by IBM; Encina discontinued 2006
- Powersoft Corporation (ent-ets-005) — Merged with Sybase 1994

### Key Technologies
- MQSeries → WebSphere MQ (2002) → IBM MQ (2014); active through 2026
- CICS Transaction Server for z/OS: active through 2025+ (v6.3)
- Encina TP Monitor: discontinued (removed from TXSeries V6.1 in 2006)
- Lotus Notes/Domino: sold to HCL Technologies 2019; active as HCL Notes/Domino
- IBM DB2 → IBM Db2 (rebranded 2017): active
- IBM IMS: active on z/OS

### Prescience Detail

**Prediction: MQSeries will add ORB and third-party tool support**  
Outcome: CONFIRMED. MQSeries was renamed WebSphere MQ in 2002, then IBM MQ in 2014. IBM MQ added extensive third-party integrations and CORBA/ORB support. Now at version 9.4 (2024).  
Source: https://en.wikipedia.org/wiki/IBM_MQ

**Prediction: Lotus Notes will continue integrating with the Internet**  
Outcome: PARTIALLY CONFIRMED. Notes/Domino did add extensive web integration (Domino product line). However, Notes fundamentally lost the collaboration market to Microsoft Exchange and later Microsoft 365. IBM sold Notes/Domino to HCL Technologies for $1.8B in 2019.  
Source: https://techcrunch.com/2018/12/07/ibm-selling-lotus-notes-domino-business-to-hcl-for-1-8b/

**Prediction: DB2 will extend multimedia capabilities for Web/Internet**  
Outcome: CONFIRMED. DB2 Universal Database introduced expanded Extenders; later added XML, JSON, spatial data support. Db2 12.1 active as of 2024.  
Source: https://en.wikipedia.org/wiki/IBM_Db2

**Prediction: TP-monitor middleware is most critical Internet scalability layer**  
Outcome: STRONGLY CONFIRMED. IBM WebSphere Application Server (1998), BEA WebLogic, JBoss all implemented the TP-monitor pattern for Internet scale. The entire Java EE/Jakarta EE ecosystem validated this architecture. Modern microservices event buses (Kafka, RabbitMQ) are the current evolution.  
Source: https://en.wikipedia.org/wiki/IBM_WebSphere
