# New LIMD Technology: Speed Plus Real-World Experience

> Archived from: https://web.archive.org/web/19970112010820/http://www.aberdeen.com:80/secure/viewpnts/v8n15/v8n15.htm
> Original publication date: 1995-12-01
> Author: Aberdeen Group

---

## Original Document Text

Volume 8/Number 15
December 1, 1995
New LIMD Technology: Speed Plus Real-World Experience
Users implementing data-intensive competitive-advantage solutions such as data-mining data warehouses and application servers are ﬁnding that performance scalability is their key
constraint. In many cases, bandwidth requirements and database sizes are growing by up to an order of magnitude every 2-3 years. To meet the unprecedented demand increases, users
cannot simply add processors or disks: these yield decreasing returns to scale.
To fully scale today's powerful RDBMS/server-hardware solutions, systems need to support Large-Scale In-Memory Database (LIMD) technology. LIMD technology supports tens of
gigabytes of main memory, allowing users to scale their main memory to match the growth of the rest of the system or to provide super-high performance on medium-scale databases. As a
result, over the last year, proactive users have found that LIMD systems can provide impressive "scalability return on investment".
But while IS increasingly accepts the idea of LIMD as a useful technology, users are only beginning to understand its effect on real-world performance, how to apply it in particular
situations, and how to distinguish 64-bit solutions combined with parallel-scalable RDBMSs tuned for LIMD from non-LIMD solutions. This Technology Viewpoint reviews the business case
for LIMD and then probes more deeply, showing how enterprises can "read between the lines" of benchmark results and supplier marketing claims to ﬁnd the right LIMD technology and the
right suppliers for the job.
Table of Contents
Executive Summary
What Does LIMD Technology Buy You?
Where LIMD Technology Is Most Effective
Using The Right LIMD Technology For The Job
The Importance Of Benchmarks
The State Of The Art In LIMD Technology: Hardware
The State Of The Art In LIMD Technology: Software
Conclusions
Executive Summary
Over the last year and on into next year, Aberdeen is seeing a dramatic increase in the implementation and rate of growth of mission-critical and business-critical solutions, and especially of
application servers and data warehouses. New user demands and strategies for competitive advantage, such as data mining, customer-interface leveraging, and reengineering, require new
large-scale decision support and "mixed" OLTP/decision-support systems, while expanding the demands on legacy and host OLTP. The new solutions, in turn, are growing by leaps and
bounds, with few to no users reporting 100-gigabyte database sizes 18 months ago and more than 100 such databases reported today: an up to 7-fold increases in large-scale decision-support
database-size requirements within 18 months of initial implementation.
To meet these demands, enterprise IS architects are employing a range of innovative technologies, including parallel-scalable and distributed database RDBMSs with the ﬂexibility to adapt
to a range of OLTP/decision-support "mixes"; three-tier and ringed application servers; data warehouses and datamarts; SMP (Symmetric MultiProcessing) plus clustering system software
that is beginning to add MPP (Massively Parallel Processing) capabilities; and, increasingly, LIMD technology that breaks the 2-gigabyte main-memory "barrier" of past 32-bit hardware and
RDBMSs and allows scaling to the tens of gigabytes. In some cases, LIMD technology is allowing enterprises to improve performance in high-end data management, beyond the beneﬁts
provided by the other innovative technologies, by one or two orders of magnitude -- 10-100 times -- for the cost of simply adding main memory. LIMD is an extension of already popular and
well-supported products -- 64-bit architectures from major hardware suppliers and 64-bit-enabled RDBMSs from major RDBMS suppliers -- and can therefore simplify and encourage
enterprise adoption.
Enterprise IS architects are incorporating LIMD in their information infrastructures in many ways. LIMD systems can act as high-end platforms with dramatic performance speed-up. In the
case of large-scale decision support applications such as data warehouses and "mixed" OLTP/decision-support solutions such as application servers, LIMD allows end-users effective access
to larger databases -- even with complex queries. At the departmental level, the LIMD system can act as an ultra-high-performance tool for rapid-response applications. For example, the
LIMD system can deliver competitive advantage in such situations as stock-ticker processing, micromarketing, enterprise resource planning (ERP), and data warehousing.
Today's most effective LIMD-technology implementers carefully balance LIMD scaling against other parts of the system, and factor in the system's potential tasks, such as application server
or data-warehouse server. Typical tradeoffs include adding processors vs. increasing main-memory size and deciding how much main memory should be allocated to OLTP vs. decision
support in "mixed" situations. Today's TPC benchmark results indicate that an increase of 1 gigabyte in main-memory consumption is strongly correlated with an increase of 1,300 tpmC in
the TPC-C benchmark. This would suggest that in many cases, adding main memory extends a system's scalability limits.
At present, Aberdeen can unequivocally declare that Digital has assumed the leadership role with Oracle, Sybase, Informix, and Software AG in delivering real-world LIMD technology.
Digital's 64-bit Alpha servers and VLM64 architecture plus these powerful RDBMSs deliver exceptional scalability and ease of migration -- Digital Alpha/RDBMS customers with products
delivered after April 11, 1995 have LIMD built into their systems. Other hardware suppliers, notably Silicon Graphics (SGI), Sun, and IBM, while behind Digital, are also developing LIMD
technology.
Aberdeen concludes that LIMD technology is past the real-world acceptance hurdle. Now, the most effective users will probe deeper to determine the right LIMD architecture for the job, and
will partner with suppliers that deliver not only a "hot box" but also the experience to support high LIMD-based scalability. Aberdeen recommends that IS executives with high-end database
performance and capacity concerns not only prototype but implement and ﬁne-tune large-scale LIMD-based systems.
Back to Table of Contents
What Does LIMD Technology Buy You?
Aberdeen deﬁnes LIMD technology as:
(1) system technology allowing 5 or more gigabytes of in-system main memory, plus
(2) database technology that can take advantage of main-memory data storage to deliver high performance.

Today's 32-bit computer architectures typically address less than 2 gigabytes of main memory, and thus carry a heavy cost and perform-ance penalty for main memory application and data
applications that could effectively use more than 2 gigabytes. 64-bit architectures increase a system's ability to directly address main memory by several orders of magnitude. The size of an
in-memory database is now effectively limited by memory costs, which are continuously decreasing, not by the chipset. Thus, main-memory data storage in the tens of gigabytes is becoming
increasingly cost-effective and attractive for large-scale mission-critical data management.
LIMD technology has three major potential technical advantages over today's data management technologies:
more data, intermediate results, programs and memory-intensive tasks such as sorts and joins can be placed in main memory, drastically reducing time-robbing I/Os;
clustered system logs can be placed in shared main memory rather than on shared disks, improving data-access, system recovery, and checkpointing time;
since the data management system needs to deal less with the bottlenecks and complexities of disk access, the data management software is better able to optimize the system, improving
response times.
Therefore, LIMD:
can deliver ultra-high performance where other technologies cannot;
costs less than adding another system or solid-state disk;
gives a performance boost to topped-out SMP systems; and
can be employed in many situations where MPP is not a practical alternative due to implementation costs or lack of applications.
Back to Table of Contents
Where LIMD Technology Is Most Effective
LIMD technology delivers particular value-added where rapid response, ultra-high performance, or high-end scalability is key to an enterprise's strategy. These characteristics are found in
many industries and at many organization levels, but especially in competitive-advantage decision-support situations involving large-scale data-warehouse applications or close-to-the-
customer departmental solutions. These situations tend to involve the following platforms:
A computer system with a very-large-scale database (hundreds of gigabytes to a terabyte), e.g., a data warehouse or mission-critical OLTP system;
A front-end processor for a large-scale database server or as one of several clustered database servers;
or A standalone computer system with a medium-scale (5-20 gigabytes) database.
LIMD technology's beneﬁts are most likely where complex queries or large-scale decision support are involved, but extend as well to OLTP and rapid-customer-response applications. LIMD
technology in data warehousing allows users to process more complex queries, increase the size of the database, and improve query performance, often by an order of magnitude each. For
example, retail enterprises can provide near-realtime response to medium-scale local or regional point-of-sale data.
An example of a rapid-response situation involving a large database is the stock brokerage or other ﬁnancial institution driving actions from results fed in from a stock ticker. In this situation,
LIMD technology can support a greater volume of stock information ﬂow and allow analysts to perform more complex online queries and data analyses (especially for high-impact products
such as derivatives) more quickly. As a result ﬁnancial institutions can achieve an order of magnitude increase -- e.g., sub-half-second response time -- in stock information processed and
analyzed. For example, Merrill Lynch is now using a Digital/Oracle LIMD solution to provide high-performance stock, bond, and insurance portfolio management. Merrill Lynch sees LIMD
as having particular value for faster response times for stock analysts, the ability to handle larger and more portfolios, and as a means of delivering quick-response and deeper-data-mining
responsiveness to customer and prospect needs, thereby increasing Merrill Lynch's business substantially.
LIMD technology is also useful for rapid response in enterprises with key production facilities. For example, many enterprises drive production through ERP applications. The effectiveness
of these applications is constrained by their speed in processing line and supplier data and delivering instructions to pro-duction operations. By increasing response time for ERP-type
databases, LIMD technology allows near-just-in-time replanning in reaction to changes in supply, production-line conditions, or queues at any point in the process.
At the departmental and end-user level, LIMD technology allows users to engage in rapid-response "micromarketing". Retail enterprises can provide near-realtime response to medium-scale
local or regional point-of-sale data, and perform fast analyses of the data for driving ﬂexible, cost-saving actions to meet rapidly-changing micromarkets. Moreover, LIMD-based systems can
use this data to drive more ﬂexible distribution and supply to retail outlets.
Finally, LIMD technology can be effective in many other applications to improve the performance of existing systems. For example, a LIMD-based system can serve as a front-end processor
for back-ofﬁce systems, handling such key high-performance tasks as message and communications queuing. As telecommunications companies implement ATM networks with gigabyte-
per-second bandwidth, systems receiving and storing this data on disk simply cannot keep up. Only systems with multi-gigabyte main memories can buffer high-bandwidth communications
quickly enough to meet capacity requirements.
Back to Table of Contents
Using The Right LIMD Technology For The Job
Today's most effective LIMD-technology implementers carefully balance LIMD scaling against other parts of the system (see Figure 1), and factor in the system's potential tasks, such as
application server or data-warehouse server. Typical tradeoffs include adding processors vs. increasing main-memory size and deciding how much main memory should be allocated to OLTP
vs. decision support in "mixed" situations.
Figure 1: Some VLM64-System Architectural Choices

Source: AberdeenGroup, December 1995
Aberdeen ﬁnds that in typical high-end conﬁgurations, adding main memory and adding processors can both have a strong, cost-effective positive impact on performance. Effective
implementers adding processors focus on the transaction load on the system, while effective implementers adding memory focus on the ratio between main memory and disk storage. Thus,
for example, medium-sized but high-throughput OLTP sites may add more processors and less main memory, while terabyte data warehouses focusing on breadth of data rather than
complexity of analysis may add more memory and fewer processors.
Implementers of "mixed" systems such as high-performance application servers often stress adding main memory particularly highly, since large main memories give the system
administrator more ﬂexibility in allocating resources -- and especially caches -- between OLTP and decision support. Thus, solutions such as Digital-Alpha/Sybase-System-11, with
sophisticated caching facilities, ﬁnd that tens of gigabytes allow a large increase in supported end users per system, up to 10,000 end users according to preliminary tests.
Back to Table of Contents
The Importance Of Benchmarks
Benchmarks can give IS an effective proof point for a particular LIMD solution. Since LIMD advantages are likely to be more striking in decision support and mixed situations, TPC-C
OLTP benchmarks offer a reasonable lower bound on the effects of adding main memory. In fact, recent TPC-C benchmark results indicate that an increase of 1 gigabyte of main memory is
strongly correlated with an increase of approximately 1,300 tpmC in the TPC-C benchmark, resulting in difﬁculties in scaling non-LIMD systems beyond 5,000 tpmC.
Initial TPC-C benchmarks indicate dramatic performance and price-performance improvements with LIMD technology. Digital-Alpha results for Unix are in the 10,000-12,000 tpmC range,
more than double almost all previous results, and price-performance is clearly better than other results in both Unix and Windows NT.
User experience with LIMD shows a 20-40 times overall performance increase in many situations, depending upon the applications. More dramatically, for complex queries with 5-way
joins, a tester has reported a 105 times speed up. Other tests show an ability to handle 10,000 connected users on a single server and backup speeds approaching if not surpassing 100
gigabytes per hour. The bottom line is that users may reasonably expect LIMD technology to deliver one or even two orders of magnitude performance increases in many cases, at the cost
only of adding main memory.
Back to Table of Contents
The State Of The Art In LIMD Technology: Hardware
Most of today's hardware instructions are 32-bit, effectively limiting main-memory databases to 2 gigabytes at most. To allow users to exploit LIMD technology, three major trends are
occurring: (1) most major hardware suppliers are providing 64-bit architectures with an effective upgrade path for their installed bases, (2) major RDBMS suppliers are providing a minimal-
pain upgrade for their software and that of third-party application ISVs, and (3) LIMD "bundles" are beginning to arrive, based on real-world experience with LIMD technology, that give the
user a "one-stop shop" of solutions customized for a wide variety of needs. Aberdeen ﬁnds that the new solutions are a major step forward in delivering the beneﬁts of LIMD technology to
users.
At this time, two major hardware suppliers have been shipping 64-bit chipsets with Unix for 1/2 year or more: Digital with its Alpha chip and VLM64 architecture and Silicon Graphics, Inc.
(SGI) with its MIPS-Technology 64-bit chip technology (although SGI does not support more than 2 gigabytes per process). Other suppliers -- notably Sun Microsystems, HP, and
IBM/Motorola -- have previewed and begun to ship new 64-bit architectures over the last few months. However, these are so new on the market that in most cases users do not yet have
signiﬁcant real-world experience with them.
Digital's Alpha 8200 and 8400 servers support up to 6 and 14 gigabytes, respectively, of main memory, and up to 8.5 terabytes of total storage. The 8200 server can be conﬁgured with up to 6
CPUs and the 8400 servers with up to 12 CPUs. Further scalability can be provided using Digital's industry-leading clustering product. Digital enhances clustering scalability and reliability
by including a massive information pipeline, the 100 megabyte-per-second Memory Channel bus. Memory Channel allows nodes in a cluster to pass data rapidly through the bus rather than
at the slower pace of download and upload from a shared disk. Other features aimed at reliability include hot swapping of components, RAID, redundant power supplies, self-test and error
correction, and failover typically in the tens of seconds (a speed comparable to that of today's much smaller systems).
The Digital LIMD solution combines Digital's Alpha 8200 and 8400 servers with Oracle 7.x, Sybase System 11, or Informix-OnLine 7.x (and soon 8.0) parallel-scalable RDBMSs enhanced
to take full advantage of Digital's VLM64 architecture -- Software AG has announced plans to follow soon. The Digital/Oracle combination reports record-shattering TPC-C benchmarking
numbers of 11,456 tpmC, at $286/tpmC.
Digital has announced speciﬁc "bundles" combining Alpha servers, RDBMSs, and third-party applications for data warehousing, business and ﬁnancial solutions, and OLTP (in particular,
telecommunications-industry OLTP). These "bundles" include support via Digital and systems-integrator services, training and seminars, and "expertise centers". Thus, Digital is leveraging
previous user experience with LIMD technology both in product customization and enhanced support. At present, Aberdeen can unequivocally declare that Digital has assumed the leadership
role with Oracle, Sybase, and Informix in delivering real-world LIMD technology.
SGI is a major player in technical rather than data-management markets (although it has recently announced a new focus in the commercial area) and does not support high-end database and
systems administration tools. Since SGI's operating system does not support more than 2 gigabytes per process, Aberdeen believes that SGI cannot yet fully take advantage of LIMD
technology.
Sun's new UltraSPARC 64-bit architecture and SunOS operating system (presently in the process of being adapted to support 64-bit applications) are in the initial stages of shipping. Sun's
new Java technology may allow it to deliver attractive Internet-based data management services, but users have little or no experience with Sun's new LIMD architecture to determine its
effectiveness.
HP's new HP 9000 Enterprise Parallel Servers use the PA-RISC 32-bit CPU and allow a maximum of 3.5 gigabytes per node. HP has announced plans for a PA-8000 64-bit chip to upgrade
these servers in the next product generation. Likewise, IBM has announced plans for a 64-bit PowerPC chipset to upgrade its present PowerPC architectures.
Tandem has extensive experience in greater-than-32-bit architectures and high-end data management. With its Himalaya line, Tandem is taking a leadership position in delivering distributed,
open high-end hardware for today's OLTP and decision support. Tandem provides its own RDBMS, NonStop Guardian, rather than supporting the major RDBMS suppliers. Tandem will
need to add LIMD technology to its Non-Stop Guardian database to catch up to Oracle, Sybase, and Informix.
Back to Table of Contents
The State Of The Art In LIMD Technology: Software
Major RDBMS suppliers Oracle, Sybase, and Informix have upgraded their products to take advantage of 64-bit architectures, while CA-Ingres, Software AG, and IBM have announced
plans to do likewise. The RDBMS suppliers indicate that their servers allow transparent migration to 64-bit hardware for current users, and third-party ISV applications that use one of these
RDBMSs as a back-end database will also be able to take advantage of LIMD.
To take advantage of LIMD technology, Oracle has rearchitected its RDBMS kernel. These changes allow the Oracle 7.1, 7.2, and upcoming 7.3 RDBMS (as well as Oracle Rdb, the
RDBMS that Oracle acquired from Digital) and any applications or utilities written to run on Oracle's RDBMS to run unchanged in a 64-bit environment. Oracle loudly and clearly asserts

that a change from a 32-bit to a 64-bit environment will be transparent to administrators, end users, and developers alike.
The Oracle 7.x RDBMS provides features that allow full exploitation of LIMD technology. In particular, Oracle's parallel- scalable technology allows high-end database-server scalability,
especially in complex decision-support applications using SMP or MPP technology. Oracle 7.1's Symmetric Data Replication and Update Anywhere features support effective use of LIMD
systems as part of a distributed database. This can be especially beneﬁcial for high-end data warehousing applications. Oracle reports performance improvements of 20 to 40 times across a
broad range of today's most common applications and transaction patterns. Moreover, Oracle reports over-200-times performance increases versus non-LIMD Oracle-on-Alpha
conﬁgurations in 3-, 4-, and 5-way joins.
Sybase's System 11 is a major improvement over System 10 in performance and performance scalability. It includes such additions as IQ Accelerator, providing order-of-magnitude speedup
in many cases for complex queries, and extended SMP support for today's highly scalable SMP hardware.
In addition, in System 11 Sybase has added several features that can take particular advantage of LIMD suppliers' large main memory. These include:
large database "device" support;
Named caches, with support for up to 2 gigabytes per cache;
Variable and large block I/O sizes;
fully symmetric network engines, allowing parallel management of thousands of end user connections without a TP monitor; and
Parallel BCP (bulk copy) for import/export of data to/from a database.
Sybase preliminary tests suggest that a combined solution can handle 10,000 connected end users on a single server and deliver backup speeds approaching if not surpassing 100 gigabytes
per hour. Preliminary results also tend to show 3-5 times performance improvement vs. System 10 running on the same hardware, and 80-90% CPU scalability¾that is, performance
improvement by adding one more processor, compared with performance on a one-processor system¾scalability that extends upward to greater numbers of processors than before. These
improvements are particularly visible for decision support and when major client-server applications are running over SQL Server 11.
Informix has likewise announced 64-bit support in the most recent version of Informix-OnLine. Preliminary indications from beta testers are that the upcoming Informix-OnLine 8.0 provides
exceptional performance scalability on LIMD hardware, and will be a strong competitor, especially in high-end data-warehousing situations. Aberdeen believes that Sybase and Informix
LIMD-system TPC benchmark results, when announced, will be extremely competitive.
Back to Table of Contents
Conclusions
LIMD technology has now proven itself: LIMD solutions are showing 10 to 100 times performance increases in benchmarks and in many real-world situations simply for the price of adding
main memory. Users have initially found these performance and scalability beneﬁts to yield the most immediate payback in complex-query and large-database decision support applications,
but are now extending them to medium-scale OLTP and "mixed" application-server situations as well. For a substantial number of applications, upgrade and administration appears almost
painless.
Aberdeen believes that a new wave of performance improvements, in some cases up to an order of magnitude, will arrive over the next 2 years as key ISV applications such as ﬁnancial
Client-Server Solutions are rewritten to take full advantage of LIMD technology.
Aberdeen ﬁnds that Digital with its VLM64 architecture and the major RDBMS suppliers have taken a strong leadership position in delivering on the promises of LIMD technology. At the
same time, as other suppliers such as Sun enter the fray, competition is heating up. Aberdeen recommends that IS buyers focus increasingly not just on ﬁnding a "hot box", but also a supplier
that can deliver a "bundle" of products and services customized for a user's needs, and can demonstrate the real-world LIMD experience and service depth to support fast-increasing and
rapidly-changing enterprise needs.
The bottom line for enterprise-level IS decision makers is that LIMD technology is here, and is proving itself effective at delivering major performance and scalability beneﬁts at relatively
small cost and effort. Aberdeen recommends that users begin to take advantage of an increasing body of real-world experience to prototype and design new applications for, or upgrade,
LIMD solutions immediately.
Back to Table of Contents
The trademarks and registered trademarks of the corporations mentioned in this publication are the property of their respective holders. Unless otherwise noted, the entire contents of this publication are copyrighted by Aberdeen
Group, Inc. and may not be reproduced, stored in a retrieval system, or transmitted in any form or by any means without prour written consent of the publisher.
Copyright © 1995 Aberdeen Group, Inc., Boston, Massachussetts
Aberdeen Group Registration
Home Page || General Information
HTML Market Research|| Aberdeen Abstracts
Aberdeen Group Publications||Custom Consulting
©Aberdeen Group, Inc.
One Boston Place
Boston, Massachusetts
02108
Contact: Chris Stevenson
Voice: (617)723-7890
Fax: (617)723-7897
E-mail: chriss@aberdeen.com

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1995-limd-technology |
| title | New LIMD Technology: Speed Plus Real-World Experience |
| author | Aberdeen Group |
| date | 1995-12-01 |
| type | market-study |
| subject_domain | database-performance-technology |
| methodology | industry-analysis,benchmarking,field-research |
| source_file | 1995-New-LIMD-Technology_-Speed-Plus-Real-World-Experience-1995-8.pdf |
| license | CC-BY-4.0 |

### Abstract

Technology Viewpoint analyzing Large-Scale In-Memory Database (LIMD) technology, examining how 64-bit architectures and large main memories deliver 10-100x performance improvements for data warehousing, OLTP, and decision support.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Pioneering analysis of large-scale in-memory database technology at 64-bit RISC adoption inflection; Aberdeen quantified 10-100x performance improvements and documented the TPC-C benchmark correlation between RAM and throughput that became foundational to modern in-memory computing. |
| **Relevance** | high | LIMD's core insight—that main memory databases offer order-of-magnitude performance gains—remains highly relevant; SAP HANA (2011) is the direct commercial realization; modern in-memory databases (Redis, VoltDB, MemSQL/SingleStore) confirm Aberdeen's 1995 architectural thesis. |
| **Prescience** | high | Aberdeen correctly identified that 64-bit LIMD would deliver 10-100x performance improvements and that ISV apps would be rewritten for LIMD over 2 years; the prediction of database size growth and in-memory as standard proved fully correct; SAP HANA's 2011 launch validated the prescience at scale. |

### Prescience Detail

**Prediction 1:** next-wave-performance-improvement
- **Claimed:** 10 x-times
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 1:** *(No matching outcome recorded)*
- **Result:** N/A
- **Confidence:** N/A
- **Notes:** N/A

**Prediction 2:** New wave of LIMD performance improvements up to 10x over next 2 years as ISV apps rewritten
- **Claimed:** Aberdeen forecast up to order-of-magnitude performance improvements arriving over next 2 years as ISV applications were rewritten for LIMD architectures
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 2:** LIMD performance wave outcome 1997-1998
- **Result:** Sybase System 11 and Oracle 7.x/8.x updates delivered significant memory-optimized improvements in 1996-1998. 64-bit Alpha/Oracle combination held TPC-C records. Performance improvements were confirmed but LIMD as distinct category was absorbed into mainstream RDBMS architecture by late 1990s.
- **Confidence:** verified
- **Notes:** Source: ACM Queue 64-bit history (2006); in-memory database Wikipedia. Performance gains confirmed; LIMD as category evolved into mainstream. Prediction substantially confirmed.

**Prediction 3:** 64-bit transition enabling large main memory as standard enterprise database platform
- **Claimed:** Study implied that as 64-bit platforms became available, LIMD would transition from specialty to mainstream for database workloads exceeding 32-bit memory ceiling
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 3:** *(No matching outcome recorded)*
- **Result:** N/A
- **Confidence:** N/A
- **Notes:** N/A


### Entities Referenced (14 entities)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | analyst-firm | acquired | Acquired by Harte-Hanks 2001; brand dissolved into Aberdeen Group Holdings under SFG Capital |
| Digital Equipment Corporation | hardware-vendor | acquired | Acquired by Compaq 1998; Compaq then acquired by HP 2002 |
| Oracle Corporation | software-vendor | active | Still active as Oracle Corporation; major database and cloud vendor |
| Sybase | software-vendor | acquired | Acquired by SAP 2010; product line continued as SAP Sybase |
| Informix | software-vendor | acquired | Acquired by IBM 2001; continued as IBM Informix |
| Silicon Graphics Inc. (SGI) | hardware-vendor | defunct | Filed bankruptcy 2009; assets acquired by Rackable Systems (renamed SGI); that SGI acquired by HP... |
| Sun Microsystems | hardware-vendor | acquired | Acquired by Oracle Corporation 2010 |
| IBM | hardware-vendor | active | Still active as IBM Corporation |
| Hewlett-Packard (HP) | hardware-vendor | active | HP Inc. and Hewlett Packard Enterprise split 2015; both active |
| Tandem Computers | hardware-vendor | acquired | Acquired by Compaq 1997; then HP 2002 |
| Software AG | software-vendor | active | Still active as Software AG; acquired by Silver Lake 2023 |
| CA-Ingres | software-vendor | rebranded | Became Actian Corporation 2011 |
| Merrill Lynch | financial-services | acquired | Acquired by Bank of America 2009 |
| Aberdeen Group (publisher) | analyst-firm | acquired | Publisher of the study; same as ENT001 |

### Technologies Referenced (20 technologies)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| LIMD (Large-Scale In-Memory Database) | database-architecture | N/A | evolved | Evolved into modern in-memory databases (SAP HANA |
| 64-bit computing architecture | hardware-architecture | N/A | ubiquitous | 64-bit is now universal in server and desktop computing; 32-bit largely obsol... |
| VLM64 architecture | hardware-architecture | N/A | obsolete | Proprietary to DEC/Compaq; became obsolete after HP absorbed DEC; replaced by... |
| Alpha chip (DEC Alpha) | processor | N/A | obsolete | Discontinued after HP acquisition of Compaq; last Alpha CPUs shipped ~2007 |
| MIPS 64-bit (SGI R8000/R10000) | processor | N/A | obsolete | MIPS processors for commercial servers largely obsolete; MIPS IP discontinued... |
| UltraSPARC 64-bit (Sun) | processor | N/A | obsolete | SPARC architecture discontinued by Oracle post-2010 Sun acquisition; last SPA... |
| PA-RISC (HP PA-8000) | processor | N/A | obsolete | HP PA-RISC discontinued; replaced by Itanium then x86-64 |
| PowerPC 64-bit (IBM/Motorola) | processor | N/A | evolved | IBM POWER architecture continues as POWER9/POWER10; used in IBM mainframes an... |
| Oracle RDBMS 7.x | database-software | N/A | evolved | Oracle 7.x superseded; Oracle database continues as 19c/21c/23c |
| Sybase System 11 | database-software | N/A | evolved | System 11 superseded by later Sybase/SAP versions; SAP ASE (Adaptive Server E... |
| Informix-OnLine 7.x / 8.0 | database-software | N/A | evolved | Acquired by IBM 2001; continues as IBM Informix 14.x |
| SMP (Symmetric MultiProcessing) | hardware-architecture | N/A | active | SMP is still the dominant architecture for multi-core server CPUs; continues ... |
| MPP (Massively Parallel Processing) | hardware-architecture | N/A | active | MPP concepts continue in modern big data platforms (Teradata; AWS Redshift; S... |
| TPC-C benchmark | benchmark | N/A | active | TPC-C still actively used as of 2024; benchmark standard for OLTP database pe... |
| Oracle Rdb | database-software | N/A | evolved | Oracle Rdb continues in niche use on OpenVMS; current version Oracle Rdb 7.4 |
| Sybase IQ Accelerator | database-software | N/A | evolved | Evolved into SAP IQ (formerly Sybase IQ); still active as SAP IQ for analytics |
| Memory Channel bus | hardware-interconnect | N/A | obsolete | Proprietary DEC interconnect; replaced by InfiniBand and high-speed Ethernet ... |
| ATM (Asynchronous Transfer Mode) networking | networking | N/A | evolved | ATM largely replaced by Ethernet (10GbE; 100GbE) and MPLS in carrier networks |
| 32-bit computing architecture | hardware-architecture | N/A | obsolete | 32-bit server computing largely obsolete by mid-2000s; 32-bit client computin... |
| NonStop Guardian (Tandem) | database-software | N/A | evolved | Continues as HPE NonStop SQL / NonStop Advanced Server; still used in financi... |

### Observation Summary

- Total observations: 52
- By type:
  - actual-outcome: 2
  - benchmark-result: 23
  - expert-opinion: 4
  - market-data: 8
  - technology-assessment: 12
  - viability-prediction: 3
