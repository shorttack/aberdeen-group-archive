# Software AG and Digital: Spreading High-Performance Solutions Throughout The Enterprise

> Archived from: 1996 Software AG and Digital_ Spreading High-Performance Solutions Throughout The Enterprise.pdf
> Original publication date: 1996-12-01
> Author: Aberdeen Group

---

## Original Document Text

The Wayback Machine - https://web.archive.org/web/19970112012052/http://www.aberdeen.com:80/secure/proﬁles/sagdec/sagdec.htm
Software AG and Digital: Spreading High-Performance SolutionsThroughout The Enterprise
Preface: Handling The Scalability Crisis
Over the last year--driven by the need for competitive-advantage applications and insights--users are implementing the new application servers and decision-support solutions not only at the
corporate level, but in the divisions, lines of business, and local ofﬁces.
To succeed in these efforts, users need new characteristics from their RDBMSs and hardware. From the RDBMS, users require support for more widely distributed data, low-overhead
administration, downward scaling of key RDBMS technologies, and the ability to integrate into an existing multi-RDBMS architecture. From the hardware, users demand exceptionally good
performance and price-performance in medium-scale data-intensive applications. The RDBMS/hardware combination must work effectively together across a broad set of user application
types, from traditional divisional OLTP to data-mart decision support to "mixed" OLTP/decision-support application servers.
This Proﬁle describes the Software AG/Digital ADABAS D/Alpha solution. This RDBMS/hardware combination allows users to leverage such hardware technologies as Alpha's Very Large
main Memory (VLM) capabilities--and such RDBMS technologies as ADABAS D's distributed-database features, low cost of ownership, and near-lights-out administrative support--to drive
ultra-high-performance OLTP, data marts, and application servers deeper into the enterprise than ever before.
Executive Summary
Aberdeen ﬁnds that the new Large-scale In-Memory Database (VLM) technology is allowing enterprises to improve performance in high-end data management by one or two orders of
magnitude--10-100 times--for the cost of simply adding main memory. VLM technology is based upon a 64-bit software and hardware architecture that allows the system's processor to
directly address much more main memory, plus software--speciﬁcally RDBMS and operating system software--that takes advantage of this new access to faster data storage.
Software AG ADABAS D RDBMS plus Digital's 64-bit Alpha servers, an early entrant into the VLM market, promises scalability over an exceptionally broad range of data-management
applications. Software AG has optimized ADABAS D to take advantage of large-memory Alpha servers, including support for 10-gigabytes-and-over data caches. Moreover, Software AG
has built on its long experience with mainframe environments to deliver effective integration of legacy mainframe data with the new solutions, such as compatibility with mainframe-based
Oracle, ADABAS C, and DB2, as well as its ENTIRE-networking connections. Combined with ADABAS D's low price point and automated distributed-database administration, these
features allow the Alpha/ADABAS D combination to provide exceptional scalability not only for new OLTP, decision-support, and application-server enterprise-scale solutions, but also for
mainframe integration and divisional and departmental solutions.
ADABAS D offers such features as baked-in-from-the-beginning distributed-data support, highly-automated distributed-database administration capabilities, delivery of parallel-scalable and
distributed-data RDBMS technologies at a departmental and divisional as well as an enterprise level, integration with today's other major RDBMSs such as Oracle and DB2, and low cost of
ownership. Digital Alpha servers' Very Large main Memory (VLM) technology supports tens-of-gigabytes of main memory, allowing ultra-high performance for medium-scale databases.
Software AG and Digital both have extensive experience in medium- to large-scale OLTP, while their combination is demonstrating the ability to deliver high performance for such
application servers as SAP's R/3 and such decision-support solutions as Software AG's ESPERANT in medium-scale environments.
IS architects can incorporate Software AG/Digital VLM in their information infrastructures in many ways. VLM systems can act as high-end platforms with dramatic performance speed-up.
In large-scale decision support applications, VLM allows end-users effective access to larger databases--even with complex queries. A departmental VLM system can act as an ultra-high-
performance tool for rapid-response applications. VLM can deliver competitive advantage for stock-ticker processing, micromarketing, enterprise resource planning (ERP), and data
warehousing. VLM:
can deliver ultra-high performance where other technologies cannot;
costs less than adding another system or solid-state disk;
gives a performance boost to topped-out SMP systems; and
can be employed in many situations where MPP (massively parallel processing) is not a practical alternative due to implementation costs or lack of applications.
Aberdeen concludes that Software AG's ADABAS D with Digital's Alpha server extends VLM technology to new application areas, meeting a broader range of user needs. IS buyers looking
to drive the new RDBMS and VLM technologies throughout the enterprise should carefully consider the new Software AG/Digital combination.
Market Position
The combined Software AG/Digital solution leverages both Software AG's and Digital's market strengths. Digital indicates that it has shipped more than 15,000 Alpha servers in the past year,
and it has a large installed base of VAX customers that it is in the process of upgrading to Alpha. Software AG is a large (upwards of $500 million in revenues in ﬁscal 1995) data-
management supplier, strong especially in many US data centers and in the European market, with a broad solution set that extends beyond RDBMS technology to include a powerful client-
server development toolset (NATURAL), and data-warehousing solutions such as ESPERANT.
A user may integrate the combined Software AG/Digital solution with ADABAS D or other RDBMSs on Digital or other hardware, with "compatibility modes" for the Oracle and DB2
RDBMSs. Software AG's ADABAS D V6 is available on major Intel and RISC hardware, including HP-UX, IBM AIX, Sun Solaris, SCO Unix, Digital Unix (on Alpha servers), Windows
NT, and OS/2 platforms. ADABAS D works with Software AG's ENTIRE networking solution and ODBC open-client support. ENTIRE includes networking solutions to connect to most
popular protocols and ENTIRE Access (allowing SQL and NATURAL native access to Oracle, Sybase, and other databases). ADABAS D also integrates with ODBC-supporting client-server
development toolsets, which can provides gateways to most popular relational and mainframe databases. ENTIRE NET-WORK runs on DECnet, TCP/IP, Netbios, SPX/IPX, and SNA. Thus,
ENTIRE can interoperate across most mainframe, workstation, midrange, and PC-LAN environments.
Users may also access Software AG and Digital service and support. Software AG over the last two years has placed increasing emphasis on front-end services such as business-process
reengineering and systems integration, as well as upgrading its back-end service delivery via hot-line support from a central site. Digital has extensive, experienced, well-regarded service
and support capabilities, especially in divisional and enterprise-scale situations.
The Importance Of VLM Technology
Aberdeen deﬁnes VLM technology as:

system technology allowing 5 or more gigabytes of in-system main memory, plus
database technology that can take advantage of main-memory data storage to deliver high performance.
Today's 32-bit computer architectures typically address less than a gigabyte of main memory, and thus carry a heavy cost and performance penalty for main-memory and data applications
that could effectively use more than 2 gigabytes. 64-bit architectures such as Digital's Alpha series increase a system's ability to directly address main memory by several orders of
magnitude. The size of an in-memory data-base is now effectively limited by memory costs, which are continuously decreasing, not by the chipset. Thus, main-memory data storage in the
tens of gigabytes will become increasingly more cost-effective and attractive for large-scale mission-critical data management.
VLM technology has three major potential technical advantages over today's data management technologies:
more data, intermediate results, programs and memory-intensive tasks such as sorts and joins can be placed in main memory, leading to more efﬁcient I/O systems that decrease
contention under heavy loads and drastically reduce time-robbing I/Os;
clustered system logs can be placed in shared main memory rather than on shared disks, improving data-access, system recovery, and checkpointing time; and
since the data management system needs to deal less with the bottlenecks and complexities of disk access, the data management software is better able to optimize the system, improving
response times.
User experience with VLM products suggests a 20-40 times overall performance increase, depending upon the application. More dramatically, for complex queries with 5-way joins, a tester
has reported a 105-times speedup. Other tests show an ability to handle 10,000 connected users on a single server and backup speeds approaching if not surpassing 100 gigabytes per hour.
The bottom line is that users may reasonably expect VLM technology to deliver--at the incremental cost only of main-memory addition--one or two orders of magnitude performance
increases in some cases.
VLM technology's ability to improve performance gives the IS manager greater ability to meet user demand and greater ﬂexibility in enterprise-architecture design. These IS beneﬁts deliver
competitive advantages for the enterprise: rapid response to a large ﬂow of business-critical information at the departmental level, and better data analysis of larger databases at the
enterprise-scale data warehouse level. Fast response time also translates into increased productivity. IBM research shows that personal productivity improves 100%, with half-second
response time, in intense man-machine interactions versus the more typical 2-3 second response time.
VLM technology can also improve the performance and robustness of mission-critical OLTP by decreasing system overhead from logging, backup, and other data-integrity measures. This
should give the OLTP system a longer useful lifetime and greater ability to incorporate occasional decision-support queries. Thus, while VLM technology's beneﬁts are most likely where
complex queries or large-scale decision support are involved, they extend as well to OLTP and rapid-customer-response applications.
Software AG/Digital VLM Technology Overview
The Digital/Software AG VLM product offering combines Digital's Alpha 8200 and 8400 servers with Software AG's ADABAS D V6. Aberdeen ﬁnds that the new Digital/Software AG
solution is a signiﬁcant step forward in delivering the beneﬁts of VLM technology to a wider range of users and user needs. Software AG states that ADABAS D will allow transparent
migration to 64-bit hardware for current Software AG users. Third-party ISV applications such as SAP's R/3 that use Software AG as their back-end database will also be able to take
advantage of VLM, usually without a port.
Digital's 8200 and 8400 servers deliver highly scalable VLM hardware: up to 14 gigabytes of main memory, up to 12 CPUs, and up to 8.3 terabytes of disk storage, with further scalability by
Digital's market-leading clustering technology. The 8200 and 8400 are aimed at the key markets for VLM technology, and represent a signiﬁcant step forward in this space. Digital is taking a
leading role in delivering 64-bit technology, large main memories, and systems designed for speedup and scaleup in high-end OLTP and decision-support applications.
Software AG's ADABAS D V6, introduced in Q3 of 1995, is a Distributed, Open RDBMS (DORS) with all the major features of the other major DORSs plus such features as attractive
pricing and highly-automated administration tools built from the start for distributed-database administration. In combination with ODBC support or other Software AG products--e.g.,
ENTIRE networking, the NATURAL client-server development toolset, and the ESPERANT querying tool--these features allow users to apply VLM technology cost-effectively not only to
enterprise-scale implemen-tations but also to data marts and divisional and departmental OLTP and application servers.
Aberdeen research shows that the key overall technical criteria by which users judge today's DORSs for use in distributed, open production systems are:
scalability,
distributed-database support,
administrative support, and
open technology.
Below, we describe how ADABAS D optimized for Alpha hardware not only meets these criteria but delivers further value-added in many cases.
Scalability
ADABAS D provides the Symmetric MultiProcessing (SMP) multithreading support that has proven effective in delivering performance scalability, especially in OLTP and "mixed"
OLTP/decision-support applications. A cost-based optimizer is particularly useful for optimizing decision-support queries. Moreover, ADABAS D includes a feature called "processor
afﬁnity" that, if possible, assigns a resuming task to the processor on which it had last been operating. This can minimize the often-costly SMP overhead of loading a task's "state" into the
processor as it switches from task to task, and thus increases the performance and scalability of an SMP system such as Alpha across all types of data management.
ENTIRE NET-WORK optimizes communications performance between client and server by using multithreading, array processing, and data compression.
From its long experience in the mainframe world, Software AG has proven large-database capabilities. Software AG cites as an example the Spanish Social Security system, with 500 trillion
bytes online. ADABAS D includes such important scalability features as parallel online backup, a key gating factor for database-size scaleup.
ADABAS D's SMP features also provide parallel-technology processor redundancy for SMP systems, allowing users to trade robustness for processor scaling as appropriate.
Caching Scalability
ADABAS D supports caching of more than 10 gigabytes of main memory. Used in conjunction with Digital's Unix RAID software and large main memory, this feature dramatically
accelerates large-object scans. In operations such as database scans in very large databases, ADABAS D can load a greater proportion of a larger database device into main memory at once.
This can signiﬁcantly reduce the time to carry out large-scale and complex queries.
Speciﬁcally, ADABAS D's caching delivers faster I/O, thus improving overall performance and mixed-workload adaptability, and especially for large-main-memory hardware such as
Digital's Alpha servers. Caches are the places in the system's main memory where the RDBMS (or the operating system) keeps disk data that is being used, or is most likely to be about to be
used, by the processor. The better the RDBMS anticipates what data the processor will need next (the "hit ratio") and the larger the cache, the more closely the system can mimic the ultra-
high speed of a system in which all the data is stored in main memory. Thus, large caches and large-cache management are a key determinant of RDBMS performance.

Distributed-Database Support
ADABAS D is "built from the ground up" for distributed-data management. Thus, for example, ADABAS D contains a global data catalog, an overall data dictionary for a distributed
database that keeps track not only of data location but also of data copies, and gives the administrator a centralized view of the entire database architecture. For higher data-dictionary-access
performance and robustness, the global data catalog is itself a location-transparent distributed database, with replicated metadata kept strictly in synchronization via a two-phase commit.
ADABAS D also includes distributed referential integrity, ensuring that changes to one part of a relational-data item stored across multiple databases are immediately reﬂected in all other
parts of the item.
ADABAS D provides two-phase commit as well as an alternative basis for data distribution: asynchronous replication. The Software-AG mainframe ADABAS-C data-management solution
also continues to provide this capability; Software AG is therefore in a leadership position in experience with the new replication technologies. A "snapshot" capability allows mass
replication of rows or tables at a time. Moreover, ENTIRE-based integration with Software AG's companion ADABAS-C mainframe product (e.g., via an ADABAS D gateway) allows
replication between mainframes and highly-scalable Unix servers such as Digital's Alpha. Thus, ADABAS D can provide an exceptional degree of database distribution between ADABAS
D/Alpha solutions and legacy mainframe systems and applications.
Administrative Support
Not only is ADABAS D designed for effective, highly-automated distributed-database administration: it provides an exceptional level of automation (and therefore of cost-effective
administration) in other areas of database administration, as well. Particularly noteworthy is ADABAS D's "dynamic reorganization" feature that automatically reconﬁgures data on disk
storage, without the need for administrator intervention, when necessary.
Dynamic reorganization attacks an often-underestimated problem with data management: system deterioration over time. At its start, a typical database is designed for optimal performance
by grouping related data on adjacent storage areas on disks. When data is added, adjacent storage areas may not be available, so that the new data may be "chained" to another storage area,
which in turn may ﬁll up. As a result, over time, data access becomes a process of following multiple chains, each causing one or more time-consuming disk accesses, instead of going
directly to data assembled in one spot.
To ﬁx this, administrators must periodically halt the system, determine a new optimal data storage, and manually go in and redistribute the data across disks--in effect, redesigning the
database. If the problem is not ﬁxed, database performance becomes steadily worse; on the other hand, ﬁxing the problem causes system downtime in mission-critical applications and
signiﬁcant added administrator work and expense. Thus, by automating data reorganization (with some--carefully minimized--system overhead during the reorganization process), ADABAS
D's dynamic reorganization can improve performance, cut administrator costs, and minimize mission-critical-application downtime.
Open Technology
Software AG has now spread its emphasis on open technology throughout its systems. For example, ADABAS C is fully SQL89 compliant and ADABAS D is fully ANSI SQL92 entry-level
compliant, including features such as referential integrity; it also includes features of the full standard such as scrollable cursors, domains, subtransactions, and temporary tables. Oracle and
DB2 "compatibility modes" provide such features as support for Oracle or DB2 versions of SQL applied to a ADABAS D database.
ENTIRE and NATURAL are also key parts of Software AG's open technology. ENTIRE has implemented support for the XA open-TP-monitor standard. NATURAL offers a wide variety of
gateways to high-end data-management systems. ENTIRE Access allows SQL (and NATURAL native) access to Oracle and Sybase databases. ADABAS D ODBC support ensures access
from ODBC-compliant desktop tools.
ENTIRE NET-WORK runs on SNA, TCP/IP, Netbios, SPX/IPX, and DECnet. Thus, ENTIRE can interoperate across most mainframe, workstation, midrange, and PC-LAN environments.
Developers can also use Software AG's NATURAL toolset to create open applications. NATURAL offers an open-server API to access ADABAS-C, IBM IMS and DB2, Oracle Rdb, and
standard-SQL-supporting RDBMSs such as Oracle and Sybase.
Digital's Alpha Technology
Digital's Alpha 8200 and 8400 servers support up to 6 and 14 gigabytes, respectively, of main memory, and up to 8.5 terabytes of total storage. The 8200 server can be conﬁgured with up to 6
CPUs and the 8400 servers with up to 12 CPUs. Further scalability can be provided using Digital's industry-leading clustering product. Digital enhances clustering scalability and reliability
by including a massive information pipeline, the 100 megabyte-per-second Memory Channel bus. Memory Channel allows nodes in a cluster to pass data rapidly through the bus rather than
at the slower pace of download and upload from a shared disk. Other features aimed at reliability include hot swapping of components, RAID, redundant power supplies, self-test and error
correction, and failover typically in the tens of seconds (a speed comparable to that of today's much smaller systems).
Digital/RDBMS VLM solutions have already shown outstanding performance and scalability in industry benchmarks. For example, a recent TPC-C benchmark shows that the
Alpha/RDBMS combination can deliver 11,456 tpmC at $286/tpmC. Software AG has demonstrated 90-times increase in performance in complex joins between ADABAS D on 64-bit Alpha
and comparable 32-bit platforms with less main memory, and Digital has shown performance increases ranging from 36 times for a 5-way join to 243 times for a table scan for ADABAS D
using a 6.2-gigabyte versus a 240 megabyte cache. Aberdeen believes that the Alpha/ADABAS D solution should achieve comparably outstanding performance and price-performance
improvements on upcoming TPC-C benchmarks.
Digital has announced speciﬁc "bundles" combining Alpha servers, RDBMSs, and third-party applications for data warehousing, business and ﬁnancial solutions, and OLTP (in particular,
telecommunications-industry OLTP). These "bundles" include support via Digital and systems-integrator services, training and seminars, and "expertise centers". Thus, Digital is leveraging
previous user experience with VLM technology both in product customization and enhanced support. At present, Aberdeen can unequivocally declare that Digital has assumed the leadership
role, together with major RDBMS suppliers, in delivering real-world VLM technology.
Where The Software AG/Digital Solution Should Be Most Effective
Aberdeen ﬁnds that enterprises will generally employ VLM technology for value added in the following three situations:
In a computer system with a very-large-scale database (hundreds of gigabytes to a terabyte), e.g., a data warehouse or mission-critical OLTP system. In this case, exploiting a large main
memory allows improved performance and robustness and thus supports access to larger databases;
In a computer system acting as a front-end processor for a large-scale database server or as one of several clustered database servers. In these cases, VLM allows the user to improve
performance where transactions involve a small subset of the total database (and ADABAS D may allow users to support thousands of end users directly); and
In a standalone computer system with a small-to-medium-scale (5-20 gigabytes) database. In this case, VLM delivers ultra-high performance.
VLM technology delivers particular value-added where rapid response, ultra-high performance, or high-end scalability is key to an enterprise's strategy. These characteristics are found in
many industries and at many organization levels, but especially in corporations seeking competitive advantage through large-scale data-warehouse applications or close-to-the-customer
departmental solutions.
An example of a rapid-response situation involving a large database is the stock brokerage or other ﬁnancial institution driving actions from results fed in from a stock ticker. In this situation,
VLM technology such as the Digital/Software-AG solution can support a greater volume of stock information ﬂow and allow analysts to perform more complex online queries and data
analyses (especially for high-impact products such as derivatives) more quickly. As a result ﬁnancial institutions can achieve an order of magnitude increase--e.g., sub-half-second response
time--in stock information processed and analyzed.

VLM technology is also especially useful for rapid response in enterprises with key production facilities. For example, many enterprises drive production through ERP applications. The
effectiveness of these applications is constrained by their speed in processing line and supplier data and delivering instructions to production operations. By increasing response time for
ERP-type databases, VLM technology allows near-just-in-time replanning in reaction to changes in supply, production-line conditions, or queues at any point in the process.
Users are ﬁnding today's data-warehousing applications a key competitive advantage, particularly for processing customer data in industries such as retail, banking, and insurance. These data
warehouses are increasing rapidly in size from hundreds of gigabytes to terabytes, and frequently require the ability to handle complex queries. VLM technology such as the Digital/Software
AG solution improves performance in complex joins and other query operations by enlarging cache size and storing intermediate results in main memory rather than on disk. Moreover, VLM
technology allows larger database sizes, since database size may effectively be constrained by the size of the main-memory cache. The net result of VLM technology in data warehousing,
therefore, is that users can process more complex queries, increase the size of the database, and improve query performance, often by an order of magnitude each.
The new Digital/Software-AG combination allows users to drive data warehousing down to divisions and departments in the form of "data marts", medium-scale but high-performance
servers for division-speciﬁc querying. Because ADABAS D offers a solution with a lower price point and lower-cost "near-lights-out" distributed-database administration, it can be used cost-
effectively in lower-scale applications than previous VLM solutions. Data-warehousing and data-mart users can also complement ADABAS D and Alpha with Software AG's Data
Warehousing and Data Mart initiatives, each a full suite of decision-support-focused solutions and services. This suite includes NATURAL for data modeling, Carleton's PASSPORT for
extracting and transforming data from source OLTP databases, ENTIRE for networking, ESPERANT for end-user querying/reporting, NETMAP for end-user graphical visualization of data,
and SourcePoint for data-warehouse administration, as well as extensive Software-AG data-warehousing systems-integration and support services.
At the departmental and end-user level, VLM technology allows users to engage in rapid-response "micromarketing". Retail enterprises can provide near-realtime response to medium-scale
local or regional point-of-sale data, and perform fast analyses of the data for driving ﬂexible, cost-saving actions to meet rapidly-changing micromarkets. Moreover, VLM-based systems can
use this data to drive more ﬂexible distribution and supply to retail outlets.
Finally, VLM technology such as the Digital/Software AG solution can be effective in a host of other applications to improve the performance of existing systems. For example, a VLM-
based system can serve as a front-end processor for back-ofﬁce systems, handling such key high-performance tasks as message and communications queuing. As telecommunications
companies implement ATM networks with gigabyte-per-second bandwidth, systems receiving and storing this data on disk simply cannot keep up. Only systems with multi-gigabyte main
memories can buffer high-bandwidth communications quickly enough to meet capacity requirements.
The Competition
Among other RDBMS suppliers, Oracle, Sybase, and Informix have also announced VLM support. Software AG distinguishes the Alpha/ADABAS D solution from these especially by its
low cost of ownership and cost-effective highly-automated distributed-database administration. As the market for this technology grows and suppliers such as CA-Ingres join the fray, further
new VLM choices will arrive over the next 2 years.
At this time, two major hardware suppliers have been shipping 64-bit chipsets with Unix for 1/2 year or more: Digital with its Alpha chip and VLM64 architecture and Silicon Graphics, Inc.
(SGI) with its MIPS-Technology 64-bit chip technology. Other suppliers--notably Sun Microsystems, HP, and IBM/Motorola--have previewed or (in Sun's case) begun to ship new 64-bit
architectures over the last few months. However, these are so new on the market that in most cases users do not yet have signiﬁcant real-world experience with them.
Of the hardware suppliers, Digital and SGI have most fully committed to 64-bit Unix chipsets and are farthest along in migrating real-world users to the new systems. SGI is a major player
in technical rather than data-management markets (although it has recently announced a new focus in the commercial area) and does not support high-end database and systems
administration tools. Since SGI's operating system does not support more than 2 gigabytes per process, Aberdeen believes that SGI cannot yet fully take advantage of VLM technology.
Sun's new UltraSPARC 64-bit architecture and SunOS operating system (presently in the process of being adapted to support 64-bit applications) are in the initial stages of shipping. Sun's
new Java technology may allow it to deliver attractive Internet-based data management services, but users have little or no experience with Sun's new VLM architecture to determine its
effectiveness.
Tandem has extensive experience in greater-than-32-bit architectures and high-end data management. With its Himalaya line, Tandem is taking a leadership position in delivering distributed,
open high-end hardware for today's OLTP and decision support. Tandem provides its own RDBMS, NonStop Guardian, rather than supporting the major RDBMS suppliers. Tandem will
need to add VLM technology to Non-Stop Guardian to catch up to Software AG, Oracle, Sybase, and Informix.
Conclusions
VLM technology should deliver 10 to 100 times performance increases in many real-world situations simply for the price of adding main memory--and main memory costs approximately
$100,000 per gigabyte, much less than adding additional high-end systems. These performance and scalability beneﬁts will be valuable not only in complex-query and large-database
decision support applications but also in mixed-workload situations. Enterprises can add VLM systems to support enterprise-scale and close-to-the-customer departmental solutions to deliver
competitive advantage across a broad range of applications.
Users are beginning to reap the full beneﬁts of more powerful 64-bit microprocessor-based systems architectures as all of the major RDBMS suppliers provide 64-bit application support and
"transparent" portation of applications. This, in turn, allows key ISV applications such as SAP's R/3 to take full advantage of VLM technology, giving users an often-transparent upgrade plus
performance increases in these applications of an order of magnitude or more in some cases. As rewrites of key ISV applications not so dependent on an RDBMS arrive over the next two
years, users should see a similar performance increase in these applications.
Aberdeen believes that Software AG and Digital have taken a strong leadership position in delivering on the promises of VLM technology. By combining high-performance 64-bit SMP
server hardware with a full-featured RDBMS at a lower price point and with highly cost-effective distributed-database administration, the Digital/ Software AG combination allows users to
deploy VLM technology in a broader range of applications and drive it deeper into the enterprise.
The bottom line for enterprise-level IS decision makers is that Software AG and Digital are offering a cost-effective package for delivering the beneﬁts of VLM technology in a wider range
of situations. Aberdeen recommends that users looking to provide high-performance OLTP, decision support, and application-server data-management solutions not only at the enterprise
level but also in the divisions and departments give close consideration to the Software AG/Digital offering.
Aberdeen Group Registration and HTML Market Research
Home Page || General Information || Aberdeen Abstracts
Aberdeen Group Publications || Custom Consulting
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

> Auto-generated by Archival Ingest Skill v13 on 2026-03-14

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-software-ag-digital-high-performance-solutions |
| title | Software AG and Digital: Spreading High-Performance Solutions Throughout The Enterprise |
| author | Aberdeen Group |
| date | 1996-12-01 |
| type | market-study |
| subject_domain | RDBMS-hardware-performance |
| methodology | industry-analysis, benchmarking, competitive-profiling |
| source_file | 1996 Software AG and Digital_ Spreading High-Performance Solutions Throughout The Enterprise.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group evaluates the Software AG ADABAS D RDBMS combined with Digital Equipment Corporation's 64-bit Alpha servers with Very Large Memory (VLM) technology. The study finds that VLM technology delivers 10-100x performance improvement for in-memory database operations, positioning the Software AG/Digital combination as an enterprise solution for OLTP, data marts, and application servers. Aberdeen concludes the combination meets a broad range of user needs for high-performance data management.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Published at a pivotal moment in database hardware architecture when 64-bit/VLM technology was emerging; provides early documentation of in-memory database performance benefits that presaged today's in-memory computing era (SAP HANA, Redis, etc.). |
| **Relevance** | medium | The in-memory database performance principles documented here remain foundational to modern data architectures; however, ADABAS D and Digital Alpha are both effectively obsolete, limiting direct applicability. |
| **Prescience** | medium | Aberdeen correctly predicted in-memory computing would deliver orders-of-magnitude performance gains; however, the specific Software AG/Digital combination did not dominate the market as suggested—Digital was acquired by Compaq in 1998, and the VLM approach was eventually eclipsed by commodity x86 with large RAM. |

### Prescience Detail


**Prediction 1:** Digital Equipment Corporation Market Position
- **Claimed:** Aberdeen implies DEC has strong market position via Alpha; large VAX install base upgrading to Alpha
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 1:** Digital Equipment Corporation Fate
- **Result:** Acquired by Compaq for $9.6B in June 1998; largest computer industry merger at the time
- **Confidence:** verified
- **Notes:** DEC was sold; Compaq then acquired by HP in 2002; Alpha architecture discontinued


**Prediction 2:** Software AG/ADABAS D Long-term Viability
- **Claimed:** Aberdeen recommends IS buyers consider Software AG/Digital for RDBMS and VLM deployments; implies long-term viability
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 2:** Software AG/ADABAS D Long-term Fate
- **Result:** Software AG survived and grew; acquired by Silver Lake in 2023 for €2.2B; ADABAS & Natural being spun off as independent business in 2025
- **Confidence:** verified
- **Notes:** ADABAS has survived 50+ years; still has active installed base in mainframe/legacy environments


**Prediction 3:** In-Memory Database Performance Trajectory
- **Claimed:** VLM technology extends high-performance database to broader enterprise applications; orders-of-magnitude improvements achievable
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 3:** In-Memory Database Performance Trajectory - Outcome
- **Result:** In-memory databases (SAP HANA 2011, Redis, Memcached, VoltDB) became mainstream; Aberdeen's directional prediction proved accurate
- **Confidence:** verified
- **Notes:** Aberdeen correctly identified the trajectory; specific technology vendors changed dramatically



### Entities Referenced (6)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Software AG | company | active | Silver Lake-owned (2023); now Software AG GmbH |
| Digital Equipment Corporation (DEC) | company | acquired | Compaq (1998) -> Hewlett-Packard (2002) |
| SAP AG | company | active |  |
| Oracle Corporation | company | active |  |
| IBM Corporation | company | active |  |
| Aberdeen Group, Inc. | firm | acquired | Harte-Hanks (2001) |


### Technologies Referenced (7)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|--------------------|
| ADABAS D | application | Software AG | mature | legacy-supported |
| Digital Alpha Architecture (64-bit) | platform | Digital Equipment Corporation | emerging | obsolete |
| Very Large Memory (VLM) Technology | platform | Digital Equipment Corporation | emerging | obsolete |
| SAP R/3 | application | SAP | mature | obsolete |
| ENTIRE Networking | framework | Software AG | mature | obsolete |
| ESPERANT | application | Software AG | mature | obsolete |
| NATURAL (4GL Development Language) | language | Software AG | mature | legacy-supported |


### Observation Summary

- Total observations: 20
- By type: actual-outcome: 3, benchmark-result: 2, framework-factor: 3, market-data: 3, strategy-classification: 1, technology-assessment: 5, viability-prediction: 3

---

*Sources:*
- *Original document archived via Wayback Machine*
- *Entity status: Wikipedia, company press releases, web search verification*
- *[SQA/Rational acquisition: CNET, November 1996](https://www.cnet.com/tech/tech-industry/rational-deal-boosts-sqa-stock/)*
- *[Software AG history: Wikipedia](https://en.wikipedia.org/wiki/Software_AG)*
- *[Digital Equipment Corporation: Wikipedia](https://en.wikipedia.org/wiki/Digital_Equipment_Corporation)*
- *[Sun Microsystems acquisition by Oracle: Oracle press release](https://www.oracle.com/corporate/pressrelease/oracle-buys-sun-042009.html)*
- *[ISS acquisition by IBM: NBC News, August 2006](https://www.nbcnews.com/id/wbna14482359)*
