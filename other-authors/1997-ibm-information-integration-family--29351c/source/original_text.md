# IBM Information Integration Family
## Original Source Text

**Source URL:** https://web.archive.org/web/19970604113322/http://www.aberdeen.com:80/secure/profiles/1997/ibmiif/ibmiif.htm  
**Publisher:** Aberdeen Group, Inc., Boston, Massachusetts  
**Copyright:** Copyright 1997 Aberdeen Group, Inc.  
**Archived:** Wayback Machine, June 4, 1997

---

The Wayback Machine - https://web.archive.org/web/19970604113322/http://www.aberdeen.com:80/secure/proﬁles/1997/ibmiif/ibmiif.htm
IBM Network Computing
IBM Information Integration Family
Executive Summary
Information integration is a great challenge – and a great opportunity – in
today‘s and tomorrow’s enterprise-scale network computing.
One of the major lessons of real-world data warehousing has been that full
integration of the enterprise’s data is difﬁcult if not impossible to achieve.
However, partial success can have a major positive impact on the corporate
bottom line. Attempts to represent all enterprise information in a data
dictionary’s metadata have led to "paralysis by analysis"; but focused efforts
and smaller-scale data marts that gather and mine data from a few sources have
achieved signiﬁcant competitive advantage in many cases. This, in turn, means
that coordinating common data across distributed network-computing databases
can be effective not only at the corporate level but in the division and the local
ofﬁce.
Moreover, an increasingly strategic challenge for IS -- at any level -- is to move
data. At the enterprise level, business competitive-advantage strategies focus
on amassing data, communicating it to key points in the organization, and
analyzing it, as effectively as possible. Each step leads to a different set of
databases, and linking them results in a distributed database architecture. These
architectures require ever-faster merging of ever-larger incoming data streams
and ever-greater integration of ever-proliferating data "archipelagoes".
Meanwhile, at the production level, IS is ﬁnding that per-project data migration
-- e.g., moving data from the mainframe to new servers, linking a data
warehouse to legacy OLTP, or feeding workgroup/desk-top/remote data into
corporate systems -- is occurring more and more frequently and leading to
recurring maintenance-type data reconﬁgurations.
In both of these cases, the key to getting more value for the organization’s
money is to reuse the middleware. Rather than creating or acquiring a new
information-integration tool for each new project, IS can extend highly ﬂexible
information-integration tools to cover each new situation.
IBM’s information integration product family offers infrastructure tools to
allow developers and end users to view and merge data from several databases
(Data-Joiner) and to move data from one database to another (MQSeries and
Data-Propagator). It also includes network-computing extensions that allow
information integration over the Internet and Intranets (Net.data and DB2
World Wide Web Connection). While these products are also available in
IBM’s Business Intelligence decision-support product family, in information
integration they take on a larger role of providing common operations and data
migration across a wide variety of data-management types (including
transaction-processing and "mixed" decision-support/TP architectures), and in
architectures ranging from departmental to enterprise-scale.
Because user information-integration needs cover such a wide range,
heterogeneity -- the ability of information integration products to operate across
an exceptionally broad range of suppliers, databases, platforms, and
communications methods -- is of special value to IS buyers. Information
integration tools can also leverage existing resources such as "legacy"
databases by combining them with each other and with new network-
computing-application data. Information integration tools speed deployment
and allow users to deploy network computing across a broader range of
situations, by allowing more-highly-automated data migration to the new
applications. For the same reasons, information integration products also can
reduce the costs of data migration and implementation of new data-intensive
network-computing applications.
For present IBM customers moving to network computing, information
integration tools provide a relatively risk-free migration path by leveraging
today’s key data. For both IBM and non-IBM customers, information
integration products deliver a way to combine a wide variety of existing
supplier databases and data types while extending them to remote and extra-
enterprise end users through the Web.

Technology Overview: A Highly Open And
Flexible Toolset
IBM’s information integration products are especially notable for their support
for heterogeneous data. That is, DataPropagator, DataJoiner, and Net.data
handle an unusually wide variety of source and target databases – relational and
non-relational; desktop, client-server, and mainframe. DataPropagator and
DataJoiner also "drive value-added into the details" – they provide features
within the overall product that enhance scalability, ﬂexibility, and ease of use,
such as log-based data replication that has proven a key to high replication
performance.
Table 1: IBM Information Integration Product Suite
Product
Features
Net.data
macros created via cut-and-paste from web-
authoring and SQL reporting tools) support HTML,
SQL to allow dynamic interaction between browser
and backend databases
can access local, LAN-attached, and remote DB2 as
well as heterogeneous data via DataJoiner
overall solution provides ﬁrewall, encryption,
authentication security
native access to DB2, Oracle, Sybase; native ﬂat-ﬁle
support; ODBC, DRDA support
DB2 Extender (image, video, audio, text) and DB2
stored procedure support
supports ICAPI, ISAPI, NSAPI
supports applets, libraries, REXX, Perl, Java,
C/C++, COBOL backends
allows placement of logic at client, Web server,
database server
allows "variable substitution" for changing Web-
page content automatically (handles "state" for
backend RDBMSs)
overall solution provides ﬁrewall, encryption,
authentication security
DataJoiner
supports "open server" operations (including joins)
on Informix, IMS, ISAM, and additional legacy
sources (via 3rd-party data drivers) and non-
relational (VSAM, IMS) databases; multiple sources
and targets (multiple supplier databases)
data location, SQL dialect, datatype transparency
global catalog (across multiple suppliers’ data)
sophisticated join performance optimizer
Data-
Propagator
log-based replication
supports multiple targets, subset distribution, data
enhancement
administrative features include trend analysis with
history tables, control tables that permit GUI-based,
batch, or program interaction
heterogeneous replication when used with
DataJoiner
MQSeries
store-and-forward messaging with queuing
supports location-independent application coding
support for Unix, OS/2, Windows NT, Digital VAX,
and IBM MVS servers, and Unix, DOS, OS/2, and
Windows/95/NT clients
Net.data

Net.data allows businesses to deploy interactive Web-based applications that
leverage existing application logic and data. Net.data DB2 WWW Connection
enables developers to write HTML/SQL-based macros that handle Web-server
data access. Thus, both Web pages and end users issuing queries can access or
update information in backend databases "dynamically", i.e., immediately,
without bringing down or bypassing the Web server. DB2 WWW Connection
can act as a client to DataJoiner, allowing data-management operations on
multiple suppliers’ databases simultaneously over the Internet. Developers can
not only create macros from scratch, but also by cut-and-paste from web-
authoring tools.
Net.data delivers higher performance by allowing native access to DB2, Oracle,
and Sybase databases, and native APIs rather than CGI. Net.data also includes
ODBC-gateway and native ﬂat-ﬁle support (thus allowing access to a wide
range of supplier databases) and supports DB2 Extenders for Internet-
multimedia-data access). Net.data allows developers to place application logic
on the client, Web server, or database server as appropriate. It supports client
logic via Java and JavaScript applets. Net.data supports today’s most popular
server-side programming by providing APIs and development tools for Java,
C/C++, COBOL, and other server-side "backend" applications (a full-ﬂedged
Visual Programming Environment is due next year) – thus, users can quickly
redeploy existing logic into new Web-based applications. Net.data supports
DB2 stored procedures, allowing higher performance for commonly-used data
management operations.
In three notable ways, Net.data steps beyond much of today’s Internet
middleware. First, Net.data supports invocation of DB2 stored procedures,
allowing higher performance for commonly-used data-management operations.
Second, Net.data provides extensive client-side support key to Internet
scalability, by providing applet support and extensive built-in libraries. Third,
Net.data allows Web-site developers to use "variable substitution": creation of
variables that can be initialized by end users or backend programs (e.g., from a
database) and changed by the administrator or backend programs while the
Web server is running, allowing constant update of Web displays. Developers
can also use these to keep track of an end user’s Internet connections associated
with accesses to a backend database – i.e., the "state" of a DB2 transaction
between connections. Thus, a Web site can ensure that OLTP and decision-
support transactions are carried out correctly.
DataPropagator Relational and NonRelational
A key differentiator for DataPropagator is its architecture. To replicate data,
Data-Propagator ﬁrst provides a "capture" stage to a relational-table staging
area, then an "apply" stage to the destination database. DataPropagator provides
log-based capture for DB2 and IMS DBMSs, which minimizes the impact on
users’ production databases. The DataPropagator architecture also supports
trigger-based capture from additional RDBMSs such as Oracle, Informix, and
Sybase. DataPropagator then reads the changes from the staging area and
applies them to the target.
Replication to each RDBMS copy can occur in parallel with normal RDBMS
processing. As a result, DataPropagator can operate in virtual isolation,
minimizes performance overhead, increases data integrity and the ability to
recover from system failures, and can operate against RDBMSs from multiple
suppliers.
To connect to non-relational data such as IMS databases, users can hook Data-
Propagator NonRelational (for "capture") to DataPropagator Relational (for
"apply"). Also, DataRefresher provides support for "refresh" copying of IMS,
VSAM, and ﬂat ﬁles to DataPropagator Relational's staging area.
Working together with DataJoiner, DataPropagator provides heterogeneous
replication between DB2, Oracle, Informix, Sybase, and other data sources.
Customers have used DataPropagator and DataJoiner to replicate data from
DB2 to Sybase SQL Server, DB2 to Oracle, Oracle to DB2, and Oracle to
Oracle.
DataPropagator also shines in other replication details. Sophisticated operations
(stored in "control tables") on data being replicated allow joins and subselects
for data subsetting, derivation, aggregation, conversion, consolidation, and
application of SQL. For laptops in mobile networks, replication can be
"pushed" from the laptop or "pulled" from the central server. DataPropagator
can "reduce" the data to be replicated before transfer for better communications
performance. Before-image data captures improve recovery and give the user
useful historical data about the distributed database, e.g., for audit purposes.
Much of the attractiveness of DataPropagator for replication lies in its details.
Aside from those mentioned earlier, DataPropagator offers communications-
performance improvement via "hotspot reduction" (bundling several updates to
a piece of data into one), load balancing, sending of replications in sets of
messages rather than singly, data "fan-out" (sending replications to one server
which then sends them -- fans them out -- to the other servers), and update
batching. DataPropagator also offers added ﬂexibility by allowing distribution
of subsets of the data to multiple targets. Administrators can perform trend
analysis on replication to determine better architecture designs, and can change
the control tables for new data transformations.

DataPropagator Relational and Non-Relational, together with DataJoiner, allow
replication across an exceptionally broad range of supplier databases and
platforms, and provide performance scalability by "driving performance into
the details". In network computing, DataPropagator’s advantages are especially
useful where IBM customers are using replication to connect data warehouses
or distributed databases to the Internet or Intranets, where enterprises wish to
link multiple suppliers’ backend databases together in an Intranet by replicating
to share common data, or where users want to set up one-time or repeated data
movement to or from Internet databases.
DataJoiner
DataJoiner simpliﬁes heterogeneous data access, complementing
DataPropagator. DataJoiner supports distributed joins and queries across
multiple databases – DB2, Oracle, Informix, Sybase, Microsoft, IMS, and
VSAM -- from multiple suppliers on multiple servers, plus update operations
on multiple relational databases. DataJoiner's sophisticated cost-based global
optimizer considers not only the queries themselves but also the networks
involved and the I/O speed of the various systems. DataJoiner can simulate
operations such as multiple open cursors that the data-management system may
lack, allowing relational and nonrelational systems to join in performing
sophisticated operations. In 1997, IBM plans DataJoiner support for many of
the features of the advanced SQL-3 SQL standard, and mimicking of SQL-3’s
advanced operations on DBMSs that do not support them. Thus, developers
will be able to invoke more operations than the typical RDBMS provides.
DataJoiner’s open-server API features provide location and network
transparency, so that applications do not have to change when the underlying
architecture changes. End users can invoke DataJoiner from Lotus Approach
and Microsoft Access, and developers can invoke DataJoiner from IBM's
VisualAge, Sybase/Power-soft's PowerBuilder, and other ODBC-supporting
data-access and developer tools.
In network computing, DataJoiner, together with Net.data, can play a key role
in allowing Web-server developers to "write once" applications that access
multiple suppliers’ legacy backend databases as well as new Web-site ﬂat-ﬁle
and relational data. DataJoiner also aids users in migrating to network
computing by allowing new Intranet data-intensive applications to access
legacy databases without the need for extensive changes to, or migration from,
the legacy data.
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
MQSeries' robustness includes transactional support that allows unit-of-work
commitment or backout of groups of messages, and also supports integration
with major popular TP monitors such as CICS, Tuxedo, and Encina. Thus,
developers can ensure that all (or none) of a set of database updates or series of
program-to-program communications is completed as a single "unit of work".
MQSeries supports a broad range of Unix, Windows NT, and proprietary
environments (e.g., Tandem, AS/400, and MVS/ESA) plus Windows,
Windows95, and DOS at the client level. MQSeries allows simultaneous
operation of multiple popular communications protocols, including TCP/IP,
SNA, Netbios, and DECnet protocols.
Where Information Integration Is Most Effective
In Network Computing
Information integration products are especially useful for network-computing-
implementing enterprises with key databases from multiple suppliers, of
multiple types, or on multiple platforms. For these, DataJoiner’s and
DataPropagator’s exceptional heterogeneity, their performance scalability and
ﬂexibility driven into the details, and their administrative support can deliver

better leveraging of existing databases, faster deployment across a wider range
of network-computing architectures through easier, more ﬂexible data
movement, and lower implementation costs and risks.
Information integration products also offer an exceptionally extensive
middleware component for network-computing new-application developers,
and particularly those using IBM’s DB2 RDBMS as the back end. Net.data’s
upcoming support for DB2 Extenders for Internet multimedia and DB2 "state"
and stored procedures for robustness and scalability offer new capabilities to
Web-site developers looking to scale via enterprise-scale-RDBMS technology,
as does Net.data’s broad support for dynamic Web-page update and "variable
substitution". Combining Net.data with DataJoiner and DataPropagator gives
these developers the ability to leverage legacy databases and "write once"
applications that access multiple supplier databases and platforms.
Aberdeen Conclusions
Information integration products provide an effective solution for enterprises’
new network-computing needs for coordinating common data across distributed
databases and moving data – i.e., rearchitecting the enterprise’s database
architecture – as the competitive environment rapidly changes. DataPropagator
and DataJoiner provide signiﬁcant advantages in open ﬂexibility, performance
and performance scalability, and distributed-database support; Net.data adds
extensive Internet data-access and application-logic support. Combined, they
provide heterogeneity, ability to leverage legacy databases, speed of
deployment, and lowered network-computing-migration risks and costs. Thus,
enterprises should be able to reuse these products in a wider variety of cases for
more rapid and cost-effective network-computing implementations.
Because of the rapid pace of Internet technology, the information integration
product family’s major upcoming technological challenges lie primarily in
providing further Internet capabilities and greater Internet scalability. Aberdeen
anticipates that information integration products will provide further support
for traditional RDBMS scalability technologies such as cursors and governors;
will add a VPE (Visual Programming Environment) for rapid development and
further Java capabilities, possibly in combination with the IBM Application
Development family; and will upgrade administrative tools to provide further
administration automation and near-lights-out ease of use.
The information integration product family is an outstanding example of IBM’s
ability to "win by the details" in an increasing strategic area of user needs –
linking and moving data between today’s proliferating "data archipelagoes". IS
buyers faced not only with network-computing implementation but also with
multiple suppliers’ databases and the need to leverage legacy data more
effectively – by far the majority of today’s enterprises -- should take a very
close look at the information integration products.
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
Copyright © 1997 Aberdeen Group, Inc., Boston, Massachusetts
The trademarks and registered trademarks of the corporations mentioned in this publication are
the property of their respective holders. Unless otherwise noted, the entire contents of this
publication are copyrighted by Aberdeen Group, Inc. and may not be reproduced, stored in a
retrieval system, or transmitted in any form or by any means without prior written consent of
the publisher.


---

## Frictionless Data Package Metadata Appendix

**Package ID:** 1997-ibm-information-integration-family--29351c  
**Archival Date:** 2026-03-14  
**License:** CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)  
**Source File:** 1997 IBM Information Integration Family pr.pdf

### Key Entities
- IBM Corporation (ent-iif-001) — Active
- Aberdeen Group (ent-iif-002) — Acquired/continued
- Oracle Corporation (ent-iif-003) — Active
- Informix Corporation (ent-iif-004) — Acquired by IBM 2001
- Sybase Inc. (ent-iif-005) — Acquired by SAP 2010
- Microsoft Corporation (ent-iif-006) — Active

### Key Technologies
- DataJoiner: Discontinued; superseded by IBM DB2 Information Integrator (~2002) then InfoSphere Federation Server
- DataPropagator: Absorbed into IBM DB2 replication services; log-based CDC pattern validated industry-wide
- Net.data: Discontinued; superseded by WebSphere Application Server / JSP-servlet model
- MQSeries → IBM MQ: Active through 2026 (v9.4)
- Log-based CDC: Now dominant enterprise data replication pattern (Debezium, AWS DMS, Fivetran)

### Prescience Detail

**Prediction: DataPropagator will add further RDBMS scalability technologies**  
Outcome: CONFIRMED. DataPropagator absorbed into IBM DB2 replication with extended scalability features. Log-based CDC became the dominant industry pattern.  
Source: https://public.dhe.ibm.com/ps/products/db2/info/vr6/htm/db2dm/db2dm82.htm

**Prediction: Visual Programming Environment for rapid development**  
Outcome: PARTIALLY CONFIRMED. IBM Rational tooling and later Eclipse-based tools provided visual development, though not a direct continuation of the Net.data VPE vision.  
Source: https://en.wikipedia.org/wiki/IBM_WebSphere

**Prediction: Information integration products will be reused across wider variety of cases**  
Outcome: STRONGLY CONFIRMED. The entire modern data integration platform market (Informatica, Talend, IBM InfoSphere, MuleSoft, Fivetran) is built on this reuse model.  
Source: https://en.wikipedia.org/wiki/IBM_Db2

**Prediction: DataJoiner + Net.data enables write-once apps across multiple legacy databases**  
Outcome: PARTIALLY CONFIRMED. DataJoiner itself discontinued, but the vision materialized via JDBC/ODBC abstraction, ORM layers, and federated query engines like Presto/Trino.  
Source: https://en.wikipedia.org/wiki/Presto_(SQL_query_engine)

**'Data archipelago' framing of enterprise data fragmentation**  
Outcome: STRONGLY CONFIRMED. The 'data archipelago' concept directly anticipates the modern data lakehouse and data mesh architectures designed to federate distributed domain data stores.  
Source: https://martinfowler.com/articles/data-mesh-principles.html
