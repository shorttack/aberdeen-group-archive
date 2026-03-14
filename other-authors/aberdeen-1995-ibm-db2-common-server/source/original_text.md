# DB2 Common Server Relational Database Management System

> Archived from: https://web.archive.org/web/19970112012303/http://www.aberdeen.com:80/secure/profiles/ibm_db2/ibm_db2.htm
> Original publication date: 1995-01-01
> Author: Aberdeen Group

---

## Original Document Text

IBM Corp.
DB2 Common Server Relational Database Management System
Having Your New RDBMS Technology And Leveraging It Too
IS buyers are ﬁnding that today's new relational database management system (RDBMS) technologies offer unprecedented opportunities for creating competitive-advantage applications, but
do not fully leverage corporate data. Parallel-scalable and replication technologies allow scaling of data-warehouse decision-support databases well into the terabyte range, increase the
scalability and ﬂexibility of OLTP and "mixed" OLTP/decision-support solutions such as application servers, and improve the robustness and power of the enterprise's overall database
architecture. However, these new technologies are applicable mainly to new applications, since it is difﬁcult to integrate them with corporate and legacy data-management systems now
typically residing on mainframes.
This Proﬁle describes IBM's DB2 common server RDBMS version 2 (also referred to as "DB2"), a data-management system whose message to IS buyers is: you can have your cake and eat
it too. DB2 offers competitive and leading-edge RDBMS technologies plus unmatched integration with today's corporate and mainframe databases. As a result, DB2 not only allows IS to
create highly scalable and ﬂexible new solutions for OLTP, decision support, and "mixed" environments, but also lets these solutions leverage today's corporate data-and present applications
access the new databases--more effectively.
Executive Summary
DB2 common server (also called "DB2") is a client-server version of IBM's DB2/MVS RDBMS that runs on IBM's RS/6000 workstations over IBM's AIX version of Unix and on PCs
running OS/2 Warp and Warp Connect. IBM has recently ported DB2 to the HP and Sun Unix platforms and is presently porting it to the Siemens Nixdorf, Windows NT, and PowerPC
platforms, making DB2 a distributed, open RDBMS (DORS). Because of IBM's large DB2 mainframe installed base and long experience in RDBMS technology, DB2 is a major player and
strong competitor in the DORS market, especially in the IBM-workstation-server market.
The core DB2 RDBMS includes basic RDBMS functionality such as stored procedures and two-phase commit plus advanced parallel-scalable and multimedia/abstract-data-type features and
a GUI-based administration toolkit. DB2 also enables tools that users or software suppliers may add to the core engine, e.g., by broad support of ODBC and X/Open CLI APIs and by
offering DataBasic, a visual procedure builder for client-side code, stored procedures, and user-deﬁned functions. The DB2 solution includes the core DB2 RDBMS plus related products that
add value for particular user needs, such as DataPropagator and DataRefresher for mass data loads and change-data replication, DataJoiner for distributed and heterogeneous data SQL joins,
reads, and "selects" (and single-site update), DataHub (an administration tool for distributed databases that can also serve as a foundation for other database administration tools), and
Visualizer, a query/report/chart tool for decision-support end users. DB2 Parallel Edition provides capabilities similar to those of DB2 version 1.2 for IBM RS/6000 loosely-coupled and SP
Massively Parallel Processing (MPP) hardware, and is interoperable with DB2.
IS buyers should consider DB2 especially for databases requiring connectivity to other IBM platforms, where IBM services are an important consideration in implementing or upgrading a
data-intensive application, and as the middle tier of a three-tier solution requiring a mainframe or AS/400 minicomputer as the top tier. Buyers should also consider DB2 where medium- to
large-scale data-warehousing is involved, or for particular applications such as mission-critical solutions requiring sophisticated DBMS tuning. In assessing DB2, IS buyers should factor in
its wide array of options and parameters that allow exceptional tuning to ﬁt user needs.
A substantial part of DB2's product revenues are in the IBM RS/6000 workstation and server installed base, where IBM competes with all of the major DORS suppliers. IBM's major
strengths in this competition are its replication technology, which supports IBM's data-warehousing efforts, and its ability to incorporate the mainframe and AS/400 in an enterprise-scale
RDBMS. The RS/6000's 1994 addition of SMP (Symmetric MultiProcessing) support plus the advent of DB2 Parallel Edition on IBM's RS/6000 SP MPP (Massively Parallel Processing)
hardware has allowed DB2 to add parallel-scalable DBMS technology comparable to these suppliers.
DB2 common server's Version 2 has added the functionality necessary for DB2 to compete on an equal technological basis with-and in some cases surpass-the other major distributed, open
RDBMS suppliers. As a result, DB2 users can now combine IBM's traditional strengths in service and corporate-data support, IBM's long experience in RDBMS technology, and the new
scalability and ﬂexibility technologies of a DORS to create new solutions better integrated with present ones. Thus, Aberdeen believes that it is time for IS buyers to take a new and closer
look at DB2 for distributed, open production systems.
Market Position
Presently, DB2 is positioned in the workstation and PC-LAN RDBMS markets. DB2 version 2 is available on OS/2, AIX, and Windows NT servers, and in beta on HP's HP-UX, Sun's
Solaris, and Siemens-Nixdorf's Sinix. Support for a DB2 Web server is upcoming. DB2 supports DOS/Windows, Windows NT, OS/2, and AIX clients, with Windows 95, HP-UX, Solaris,
Macintosh, and PowerPC-based clients in beta test. DB2 supports the TCP/IP, SPX/IPX, NetBIOS, and SNA LU6.2 (APPC/APPN) protocols, and allows interconnection to the MVS,
OS/400, VSE, and VM IBM platforms via DRDA (Distributed Relational Database Architecture). Eleven other suppliers have also implemented DRDA access to DB2 data.
IBM is presently in the process of rolling out DB2 version 2. This adds major features such as "SMP enablement" to DB2's functionality.
IBM sells DB2 primarily through a vast global direct-sales force, often bundled with IBM hardware and services. IBM's sales force is noted for its prowess and focus on customer
satisfaction. IBM is signiﬁcantly increasing its focus on other channels, and DB2 version 2 is "channel-enabled
Technology Overview: DB2's Long Experience
DB2 common server is an implementation of IBM's mainframe DB2/MVS RDBMS functionality for open Unix, Windows NT, and OS/2 platforms. DB2/MVS on the mainframe has over 10
years of datacenter and mission-critical-application experience, giving DB2 common server added robustness and OLTP scalability in many situations.

DB2 common server version 2 adds not only multithreading support for SMP scalability and two-phase commit, but also a wealth of other features that make DB2 broadly comparable in
distributed and open technology to the other major RDBMS suppliers. Related products such as DataPropagator and DataJoiner give DB2 new strength in large-scale multisupplier and
decision-support situations, and DataHub adds distributed-database and multisupplier database-administration support.
Much of the power of DB2 lies in its details. For example, DataPropagator Relational's effective way of carrying out log-based data replication in parallel with the usual data-management
tasks decreases replication overhead and hence provides added performance in OLTP, data warehouse, and "mixed" OLTP/decision-support architectures. In version 2, IBM is extending this
focus on details to include large and complex data types, with extensive support for video, audio, text, and imaging.
Aberdeen's Distributed, Open RDBMS (DORS) Buying Guide ﬁnds that the following capabilities are key to IS' effective use of DORSs to create distributed, open production systems:
scalability,
distributed-database support,
ﬂexibility, and
administrative support and robustness.
Below, we describe the DB2 features that deliver competitive and leading-edge technology in each of these areas.
Scalability
Performance Scalability. DB2 provides a broad array of features for improving performance. DB2 includes multithreading, stored procedures, "compound SQL" that allows it to process a
group of SQL statements together, caching of SQL-runtime plans, tracing and monitoring tools, and statistics on RDBMS speeds and loads that allow the user to ﬁne-tune system
performance. DB2 also includes features for unusually ﬂexible placement of data on disk to avoid I/O-to-memory transfer bottlenecks.
DB2's multithreading allows high-performance OLTP on parallel systems hardware, and version 2 is now "SMP-enabled", matching other major DORS suppliers in OLTP-type parallel
performance features. A major performance enhancer in version 2 is a reworking of IBM's cost-based optimizer to perform more in-depth analysis of queries, including "query rewrite" of
complex queries to allow better optimization, consideration of more alternatives, more sophisticated query modeling, better detection of non-uniform data distributions, pre-fetching of data
from disk, parallel I/O operations and devices, big-block reads, and asynchronous writing from buffers to disk.
A separate IBM product, DB2 Parallel Edition for AIX, provides parallelism across joins, inserts, updates, deletes, index creation and scan, backup and restore, selects, and other common
querying functions. DB2 Parallel Edition is available on loosely-coupled RS/6000s with HACMP or connected via a LAN, and on IBM's high-end RS/6000 SP Massively-Parallel Processing
(MPP) systems.
DB2's ability to drive performance into the details shows up in benchmarks. For example, a recent TPC-C result on an 8-way RS/6000 model J30 shows DB2 delivering 3119.16 tpmC at 349
$/tpmC.
Large Databases. DB2 has many features that show IBM's long experience with large-database management. For example, integration with the Adstar Distributed Storage Manager (ADSM)
allows backup/recovery with IBM S/390 mainframes and AS/400 minicomputers. DB2 version 2 supports parallel backup and restore on a tablespace basis. This allows high performance in
a key operation that has proven a major gating factor in scaling DORS databases to the terabyte range.
Distributed-Database Support
DB2 provides excellent distributed-database support via products that work effectively with DB2: DataPropagator, DataHub, and DataJoiner. DataPropagator allows users to download data
copies from one database to another with high performance in such situations as data warehouses. DataHub provides management of multiple databases and replicated data from a single
control point. DataJoiner provides transparent SQL-based data access, not only across DB2 instances, but also across dissimilar data management systems such as IMS. DB2's
interoperability also allows end users to access transparently and perform multisite updates on databases distributed across servers, minicomputers, and mainframes.
Asynchronous Replication. DB2 supports asynchronous replication via DataPropagator. DataPropagator allows time-interval-based replication (e.g., it can propagate changes every hour or
send a mass "refresh" change once a day) across DBMSs supporting IBM's DRDA protocol. The DBMSs involved must provide a "change capture" capability supporting change
propagation. DataPropagator works with Data-Joiner to allow replication to and from non-IBM and non-DRDA data sources.
A key differentiator for DataPropagator is its architecture. To replicate data, Data-Propagator ﬁrst provides a "capture" stage to a staging area, then an "apply" stage to the destination
database. The RDBMS can use triggers to propagate changes to the staging area, and DataPropagator then applies the changes to the target. The capture stage uses the RDBMS's log, and
DataPropagator's implementation allows replication to each RDBMS copy to occur in parallel with normal RDBMS processing, with minimal overhead. As a result, DataPropagator can
operate in virtual isolation, minimizes performance overhead, increases data integrity and the ability to recover from system failures, and can operate against RDBMSs from multiple
suppliers.
To connect to non-relational data such as IMS databases, users can hook DataPropagator NonRelational (for "capture") to DataPropagator Relational (for "apply"). Also, DataRefresher
provides support for "refresh" copying of IMS, VSAM, and ﬂat ﬁles to DataPropagator Relational's staging area.
DataPropagator also shines in other replication details. Sophisticated operations on data being replicated allow joins and subselects for data subsetting, derivation, aggregation, conversion,
consolidation, and application of SQL. For laptops and mobile networks, replication can be "pushed" from the laptop or "pulled" from the central server. DataPropagator can "reduce" the
data to be replicated before transfer for better communications performance. Before-image data captures improve recovery and give the user useful historical data about the distributed
database.
Much of the attractiveness of DataPropagator for asynchronous replication lies in its details. Aside from those mentioned earlier, DataPropagator also offers communications-performance
improvement via "hotspot reduction" (bundling several updates to a piece of data into one), load balancing, sending of replications in sets of messages rather than singly, data "fan-out"
(sending replications to one server which then sends them-fans them out-to the other servers), and update batching.
Update Anywhere. DB2's replication facilities are being enhanced to support update anywhere. An upcoming version of DataPropagator will deliver added update-anywhere robustness by
providing features that take unusual care to ensure global data consistency when multiple updates are being performed simultaneously.
Synchronous Replication. Using DB2's two-phase commit (2PC) and multisite update capabilities, users can implement replicated data kept synchronized at all times across a network. DB2
provides full 2PC support across LAN internetworks and across IBM hardware in the enterprise, including replication between RS/6000s, PCs, AS/400 minicomputers running the OS/400
operating system, and mainframes running the MVS operating system, using a TP monitor such as IBM's CICS, Transarc's Encina, or Novell's Tuxedo.
Transparent Data Access. DataPropagator is complemented by DataJoiner, which supports distributed joins across multiple databases-relational, IMS, and VSAM-from multiple suppliers on
multiple servers. DataJoiner's sophisticated cost-based global optimizer considers not only the queries themselves but also the networks involved and the I/O speed of the various systems.
DataJoiner can simulate operations such as multiple open cursors that the data-management system may lack, allowing relational and nonrelational systems to join in performing
sophisticated operations. DataJoiner provides location and network transparency, so that applications do not have to change when the underlying architecture changes. End users can invoke
DataJoiner from Visualizer, Lotus Approach, and Microsoft Access, and programmers from IBM's VisualAge and Sybase/Powersoft's PowerBuilder.
DB2's Client Application Enabler provides transparent access to DRDA-connected and LAN-based database servers from embedded SQL and ODBC/CLI programs.

Distributed Administrative Tools. DataHub provides sophisticated, relatively automated distributed-database administration. DataHub allows management of multiple databases and systems
from a single control point, including task-oriented database-administration functions and automated system and database monitoring and alerting. DataPropagator users may register and
subscribe to data copies via a GUI-based tool integrated into DataHub.
Flexibility Features
Standards adherence and security. DB2's SQL presently follows almost all of the the 1992 ANSI standard (Entry), plus some functions in the Intermediate and Full standard and in the
proposed SQL3 standard. DB2 supports IBM's DRDA interoperability mechanism, which includes the X/Open CLI API standard.
DB2 supports IBM's widely-used RACF login-security product in connected hosts.
Gateways, Open Clients, Open Servers. DB2 presently connects to other DORSs via DRDA. At present, Informix, Oracle, and Sybase among DORS suppliers support client-side remote
access via DRDA (Application Requester, Remote Unit of Work). DB2 provides server support-and has announced stored procedure and 2PC support-across DRDA. DB2 also provides
ODBC version 2 support.
Open TP Monitors. DB2 provides outstanding TP-monitor support. This includes long-standing support for IBM's widely-popular CICS TP monitor, plus support for Transarc's Encina and
Novell's Tuxedo and implementation of the X/Open XA API.
Database Administration and Robustness
High-Availability Features. DB2 supports the IBM RS/6000's HACMP clustering solution, which includes extensive failover features. DB2's other high-availability features, such as its
backup and recovery, have been ﬁeld-proven over a decade. DB2 version 2 includes the parallel backup and recovery key to scaling today's client-server RDBMSs.
Administrative Support. DataHub provides database administration services for DB2, and connects its administrative tools to other IBM data-management and systems-management
solutions. DataHub includes SNMP support that should allow users to create mechanisms to pass information between DataHub and other DORS suppliers' administrative tools. DB2 version
2 provides a database Management Information Base (MIB) and SNMP subagent.
DataHub provides management of data from a single control point. Database management tools arriving with DB2 version 2-especially DB2 Performance Monitor, Visual Explain, and the
SNMP subagent-provide extensive database statistics, monitoring, and tuning capabilities. Visual Explain shows the optimizer's SQL plan, allowing users to monitor and ﬁne-tune application
performance. Performance Monitor performs analyses and enables administrators to view the system and generate reports. The SNMP subagent allows today's major systems management
solutions to monitor DB2 and work with DataHub.
DataHub provides exceptional administrative ﬂexibility and automation for single-site and distributed databases. Administrators may use DataHub's command scheduler or IBM's FlowMark
workﬂow management product to automate operations.
Other Technologies
Business-rules processing. DB2 provides extensive business-rules support, such as stored procedures, triggers (including triggers before and after inserts, deletes, and updates), column and
table constraints, and user-deﬁned functions and data types. User-deﬁned functions allow the user to customize DB2.
Complex Data Types. DB2 provides signiﬁcant support for complex data types, such as "character" and "double-byte character" data types (for internationalization), and large (up to 2
gigabytes) data types. DB2 also provides functions to access parts of a data type, and the ability to insert a data type too large for main memory into the database from a client ﬁle or CD-
ROM.
Upcoming are bundles of triggers, user-deﬁned data types, and user-deﬁned functions for particular data types called Relational Database Extenders (e.g., a text server, imaging server, audio
server, and video server). These allow developers to create sophisticated solutions in these areas at a higher, more programmer-productive level. For example, Extenders will support
ﬁngerprint analysis and querying by SQL of image content-color, shape, or pattern.
The text Extender may be particularly valuable to users in the long term, because it includes information-retrieval technology. Aberdeen believes that the ability to detect and adjust to
patterns of user queries can improve the efﬁciency and effectiveness of data mining on large text databases signiﬁcantly.
Client-Server Development Toolsets. IBM offers for use with DB2 the VisualAge object-oriented toolset based on the Smalltalk or C++ object-oriented programming languages, as well as
macro-language tools such as REXX and compilers for popular client programming languages such as C and C++. A server-side Stored Procedure Builder (DataBasic) gives DB2 strong
capabilities for building client-server applications with complex server components. Seer Technologies, a third-party supplier with close historical ties to IBM, provides a client-server
application development environment (CADE) with broad ﬁrst- and second-generation technology.
End-User Solutions. IBM's OS/2 Warp, on which a version of DB2 runs, provides a strong end-user-desktop graphical interface. IBM estimates over 10 million users of OS/2. The Visualizer
query/report/charting tool provides end-user access to DB2 database servers on OS/2 and AIX platforms. IBM has announced plans to extend Lotus Approach to support access to DB2 from
OS/2 and Windows NT platforms.
Workgroup Server. DB2 runs full-featured on OS/2, and is therefore a relatively powerful engine for workgroup and departmental environments. DB2's "push-pull" replication facilities are
particularly useful for mobile connections to a workgroup server, as noted above. The upcoming incorporation of Lotus Notes into IBM's product set should give DB2 especially close
integration with today's leading groupware solution. Lotus' newly announced NotesPump provides replication support between Notes and DB2 via an ODBC interface.
Where DB2 Is Most Effective
DB2 is especially effective where users with mainframe or midrange-AS/400 platforms wish to connect them to new open-server-hardware-based solutions, in large-scale decision-support
situations as data marts interoperating with data warehouses on high-end and MPP platforms such as IBM's RS/6000 SP hardware, and as an effective way to translate IBM's OLTP and
"mixed" solutions to open systems, e.g., as application servers.
DB2's DRDA support allows users connecting mainframes, AS/400s, and RDBMSs in an overall enterprise architecture to replicate data in bulk via DataPropagator. DB2 also enables users
to replicate data not only between DB2 database servers and mainframe data-management systems such as IMS, but also between DB2 and other popular RDBMSs. Thus, DB2 empowers
users to extend their new solutions to access mainframe and AS/400 data, and to integrate their corporate and legacy data with open-server hardware.
In large-scale decision support, DB2 can combine with DB2 Parallel Edition on IBM's RS/6000 SP to deliver a combined data-mart/data-warehouse architecture. Such combinations are
increasingly attractive to end users seeking to avoid the massive review of the enterprise's data involved in implementation of a single, central data warehouse. DB2's strong replication
features and effective interoperability with legacy OLTP can provide an effective foundation for long-term scalability and ﬂexibility of the data-mart/data-warehouse architecture. DB2 is part
of an exceptionally comprehensive IBM data-warehouse solution that also includes a wide array of IBM and third-party data-warehouse components, plus IBM's usual extensive service and
support.
DB2 can also add beneﬁts as the data-management system for an application server. Its value-added server-side development tools, packages for complex data types, and wealth of tuning
features can aid users in rapidly developing highly customized and relatively complex client-server applications.
Vision Statement/Marketing Strategies

IBM states that it "is dedicated to being an open, client-server vendor capable of providing industry-leading client/server solutions to customers". IBM stresses its belief that data-
management technology is key to its customers' competitive advantage. IBM aims to incorporate into DB2 the best optimization technology in the market, plus "industrial-strength" RDBMS
functions and object extensions to leverage object-oriented and multimedia technologies. IBM is also focusing DB2 on the SOHO (small ofﬁce, home ofﬁce) market as a single-user or
unconnected-LAN RDBMS.
DB2 service is worldwide, and includes a warranty as well as regional or country-wide installation,design, support, education, and training services. IBM also offers extensive systems-
integration and outsourcing services. IBM has an unmatched reputation for comprehensive service. DB2 is fully enabled for worldwide indirect-channel sales (e.g., VARs and systems
integrators).
Financials
IBM does not break out its DB2 results. IBM's overall 1994 revenues were $64.0 billion, a 2 % increase from 1993, with $3 billion in net proﬁt. IBM estimates that its software revenues
were $11.3 billion in 1994, which would make IBM's software revenues more than twice as large as those of the largest software company.
Aberdeen Conclusions
With the advent of DB2 common server version 2, IBM demonstrates that it has made enormous strides that have allowed it to match or surpass its competitors' technology advances and
begin to spread beyond IBM platforms. DB2 is a strong competitor in the DORS market, with a robust solution and the ability to add other IBM products to achieve high scalability,
distributed-database and data-warehouse support, open replication and administrative tools for multisupplier RDBMS environments, and database management integrated from desktops to
mainframes. DB2's strengths in medium-scale OLTP and in decision support are especially attractive on departmental and divisional systems with predominantly IBM-hardware
architectures, or requiring connectivity to AS/400 or mainframe databases.
The keys to DB2's success in the long term are its ability to continue to fold its ancillary products into an overall DB2 "bundle", upgrade its client-server development toolset capabilities,
continue to move ahead rapidly in scalability technology to match the rapid pace of RDBMS technology, and position itself effectively and sell aggressively against DORS competitors on
non-IBM platforms. IBM must also continue to gain experience in marketing to VARs as well as its traditional IS customers.
Nevertheless, DB2 now provides IS with an attractive option for creating new distributed, open production systems, with an exceptional ability to integrate with and leverage today's
corporate and legacy databases. IS buyers seeking to have their RDBMS-technology cake, and leverage it too, should take a close look at the new DB2.
Aberdeen Group Registration
Home Page || General Information
HTML Market Research|| Aberdeen Abstracts
Aberdeen Group Publications||Custom Consulting
Aberdeen Group
One Boston Place
Boston, Massachusetts
02108
Telephone: 617-723-7890
FAX: 617-723-7897
The trademarks and registered trademarks of the corporations mentioned in this publication are the property of their respective holders. Unless otherwise noted, the entire contents of this publication are copyrighted by Aberdeen
Group, Inc. and may not be reproduced, stored in a retrieval system, or transmitted in any form or by any means without prour written consent of the publisher.
Copyright © November 1995 Aberdeen Group, Inc., Boston, Massachussetts

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1995-ibm-db2-common-server |
| title | DB2 Common Server Relational Database Management System |
| author | Aberdeen Group |
| date | 1995-01-01 |
| type | product-profile |
| subject_domain | relational-database-management |
| methodology | industry-analysis, competitive-profiling, benchmarking |
| source_file | https://web.archive.org/web/19970112012303/http://www.aberdeen.com:80/secure/profiles/ibm_db2/ibm_db2.htm |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group profile evaluating IBM's DB2 Common Server, a distributed relational database management system designed to provide a common SQL interface across multiple platforms. Examines competitive positioning against Oracle, Sybase, and Informix.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Evaluated DB2 v2 at the critical juncture when it achieved functional parity with Oracle/Sybase/Informix; Aberdeen's DORS framework and recommendation drove enterprise purchasing at IBM's $64B revenue scale; the study's assessment accurately captured DB2's competitive positioning in the $11B IBM software business. |
| **Relevance** | medium | IBM Db2 remains an active enterprise database platform in 2026, and DataPropagator/replication technology concepts survive in IBM's replication suite; however specific products (OS/2, RS/6000) are obsolete and the competitive landscape has transformed with cloud databases. |
| **Prescience** | high | DB2 delivered on roadmap promises (Relational Extenders, DataPropagator update-anywhere, Lotus integration); DB2 revenue grew 73% in 2000 vs industry 3x faster (IBM Annual Report 2000); approximately 1,000 Oracle customers switched to DB2 by 2000—validating Aberdeen's recommendation. |

### Prescience Detail

**Prediction 1:** upcoming
- **Claimed:** upcoming version will deliver update-anywhere robustness to ensure global data consistency
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 1:** *(No matching outcome recorded)*
- **Result:** N/A
- **Confidence:** N/A
- **Notes:** N/A

**Prediction 2:** upcoming
- **Claimed:** text, imaging, audio, video server extenders; fingerprint analysis; SQL querying of image content by color, shape, pattern
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 2:** *(No matching outcome recorded)*
- **Result:** N/A
- **Confidence:** N/A
- **Notes:** N/A

**Prediction 3:** integration with DB2
- **Claimed:** upcoming incorporation of Lotus Notes into IBM product set will give DB2 close integration with leading groupware solution
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 3:** IBM Lotus Notes DB2 integration outcome
- **Result:** IBM acquired Lotus in June 1995 for $3.5B; Notes and DB2 integration deepened through late 1990s. Lotus Domino 5.0 (1999) provided tighter database integration. However Notes market share was eventually eroded by Microsoft Exchange. Product continues as HCL Notes after IBM sold to HCLSoftware in 2019.
- **Confidence:** verified
- **Notes:** IBM Lotus acquisition confirmed; integration delivered but competitive outcome mixed. Prediction partially confirmed.

**Prediction 4:** Upcoming DataPropagator update-anywhere global consistency
- **Claimed:** IBM planned upcoming DataPropagator version with update-anywhere robustness ensuring global data consistency during simultaneous updates
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 4:** DataPropagator update-anywhere outcome
- **Result:** IBM delivered advanced DataPropagator functionality through DB2 Replication; technology evolved into InfoSphere Data Replication. IBM DB2 revenue on UNIX/NT grew 73% in 2000 per IBM Annual Report, validating the replication investment.
- **Confidence:** verified
- **Notes:** Source: IBM Annual Report 2000 (ibm.com). Prediction substantially confirmed.

**Prediction 5:** DB2 Relational Extenders for text/imaging/audio/video
- **Claimed:** IBM planned Relational Database Extenders for text, imaging, audio, video; SQL querying of image content by color/shape/pattern; fingerprint analysis
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 5:** DB2 Relational Extenders outcome
- **Result:** IBM shipped DB2 Extenders (text, image, audio, video, XML) through late 1990s-2000s, evolving into DB2 Content Manager and IBM Information Integrator. The multimedia extension concept validated; specific extender products eventually superseded by broader content management.
- **Confidence:** verified
- **Notes:** Prediction confirmed. DB2 Extenders shipped and evolved. Source: IBM DB2 product history.

**Prediction 6:** Upcoming Lotus Notes incorporation into IBM product set with DB2 integration
- **Claimed:** IBM planned close integration of Lotus Notes (then being incorporated into IBM) with DB2, building on NotesPump ODBC replication announced at study time
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 6:** *(No matching outcome recorded)*
- **Result:** N/A
- **Confidence:** N/A
- **Notes:** N/A

**Prediction 7:** DB2 will compete on equal basis with Oracle/Sybase/Informix for open systems
- **Claimed:** Aberdeen predicted DB2 v2 had achieved functional parity and IS buyers should look at DB2 for distributed open production systems as serious Oracle/Sybase/Informix alternative
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 7:** DB2 competitive standing vs Oracle outcome
- **Result:** DB2 revenue on UNIX/NT platforms grew 73% in 2000 (IBM Annual Report 2000), growing 3x faster than industry. ~1,000 companies replaced Oracle with DB2 in 18 months to 2000. SAP, Siebel, PeopleSoft selected DB2 as preferred database. However Oracle retained market leadership overall.
- **Confidence:** verified
- **Notes:** Source: IBM Annual Report 2000. Prediction substantially confirmed for enterprise segment.


### Entities Referenced (11 entities)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| IBM | company | active | IBM remains an active global technology company as of 2026 |
| Oracle | company | active | Oracle remains an active global database and cloud technology company as of 2026 |
| Sybase | company | acquired | Sybase was acquired by SAP in July 2010 for approximately $5.8 billion; operates as SAP Sybase |
| Informix | company | acquired | Informix acquired by IBM in 2001 for $1 billion; continued as IBM Informix; active development de... |
| Computer Associates | company | rebranded | Computer Associates rebranded as CA Technologies; subsequently acquired by Broadcom in 2018 |
| Transarc | company | acquired | Transarc (maker of Encina TP monitor) acquired by IBM in 1994 |
| Novell | company | active | Novell (Tuxedo TP monitor) still operates; acquired by Attachmate in 2011, then Micro Focus in 2014 |
| Seer Technologies | company | unknown | Third-party client-server application development environment (CADE) provider with close IBM ties... |
| Lotus Development | company | acquired | Lotus acquired by IBM in 1995; Lotus Notes eventually folded into IBM Collaboration Solutions |
| Powersoft | company | acquired | Powersoft acquired by Sybase in 1995; PowerBuilder product line continues under SAP |
| Aberdeen Group | company | active | Aberdeen Group is an active technology research and analysis firm |

### Technologies Referenced (35 technologies)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| DB2 Common Server | RDBMS | N/A | active | Continues as IBM Db2; current versions available for cloud and on-premises |
| DB2/MVS | RDBMS | N/A | active | Continues as IBM Db2 for z/OS (mainframe) |
| DB2 Parallel Edition | RDBMS extension | N/A | active | Capabilities absorbed into mainstream IBM Db2 |
| SQL | query-language | N/A | active | SQL remains the dominant relational database query language; ANSI/ISO standar... |
| DRDA (Distributed Relational Database Architecture) | protocol | N/A | legacy | DRDA largely superseded by modern REST APIs and JDBC/ODBC connectivity; still... |
| ODBC | API | N/A | active | ODBC remains a widely used database connectivity standard |
| X/Open CLI | API | N/A | legacy | X/Open CLI largely superseded by JDBC and modern ORMs; ODBC descended from it |
| DataPropagator | replication-tool | N/A | legacy | DataPropagator functionality absorbed into IBM InfoSphere Data Replication an... |
| DataJoiner | federated-data | N/A | legacy | DataJoiner functionality absorbed into IBM InfoSphere Federation Server |
| DataHub | administration-tool | N/A | legacy | DataHub replaced by IBM Data Management Console and other tools |
| DataRefresher | data-loading | N/A | legacy | Superseded by modern ETL tools |
| DB2 Visualizer | reporting-tool | N/A | legacy | Superseded by modern BI tools |
| DataBasic (Stored Procedure Builder) | development-tool | N/A | legacy | Superseded by modern DB2 development tools |
| VisualAge | development-environment | N/A | legacy | VisualAge superseded by IBM Rational and Eclipse-based tools |
| OS/2 Warp | operating-system | N/A | obsolete | OS/2 discontinued; IBM ended OS/2 support in December 2006 |
| AIX | operating-system | N/A | active | AIX remains IBM's enterprise Unix OS for Power Systems |
| Windows NT | operating-system | N/A | legacy | Windows NT superseded by Windows 2000 and later Windows Server versions |
| IBM RS/6000 | hardware-platform | N/A | legacy | RS/6000 line evolved into IBM Power Systems |
| IBM RS/6000 SP | mpp-hardware | N/A | legacy | RS/6000 SP evolved into IBM Blue Gene and later HPC platforms |
| TCP/IP | networking-protocol | N/A | active | TCP/IP remains the dominant networking protocol |
| SNA LU6.2 (APPC/APPN) | networking-protocol | N/A | legacy | SNA largely replaced by TCP/IP in enterprise networks |
| CICS | tp-monitor | N/A | active | CICS remains active as IBM CICS Transaction Server |
| Encina | tp-monitor | N/A | legacy | Encina TP monitor discontinued after IBM acquired Transarc |
| Tuxedo | tp-monitor | N/A | active | Tuxedo still active; transferred through BEA Systems to Oracle |
| ADSM (Adstar Distributed Storage Manager) | storage-management | N/A | legacy | ADSM rebranded as IBM Tivoli Storage Manager, later IBM Spectrum Protect |
| REXX | scripting-language | N/A | active | REXX remains supported on IBM platforms and continues in use |
| RACF | security | N/A | active | RACF remains IBM's mainframe security manager |
| SNMP | management-protocol | N/A | active | SNMP remains widely used for network management |
| PowerBuilder | development-tool | N/A | active | PowerBuilder continues under SAP (via Sybase acquisition); current versions a... |
| Lotus Approach | end-user-tool | N/A | legacy | Lotus Approach discontinued; Lotus suite absorbed into IBM products |
| Lotus Notes | groupware | N/A | active | Lotus Notes/Domino continues as HCL Notes/Domino after HCL acquired IBM Colla... |
| NotesPump | replication-tool | N/A | legacy | NotesPump functionality absorbed into later IBM/HCL replication tools |
| IBM FlowMark | workflow-management | N/A | legacy | FlowMark evolved into IBM MQSeries Workflow and later IBM Business Process Ma... |
| HACMP | high-availability | N/A | active | HACMP continues as IBM PowerHA SystemMirror |
| TPC-C | benchmark | N/A | active | TPC-C benchmark still used for OLTP performance measurement |

### Observation Summary

- Total observations: 58
- By type:
  - actual-outcome: 4
  - expert-opinion: 7
  - market-data: 7
  - strategy-classification: 5
  - technology-assessment: 28
  - viability-prediction: 7
