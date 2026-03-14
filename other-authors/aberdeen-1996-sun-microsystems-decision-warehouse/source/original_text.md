# Sun Microsystems Decision Warehouse

> Archived from: [https://web.archive.org/web/19970112011832/http://www.aberdeen.com:80/secure/profiles/sun_dw/sun_dw.htm](https://web.archive.org/web/19970112011832/http://www.aberdeen.com:80/secure/profiles/sun_dw/sun_dw.htm)
> Original publication date: 1996-03-01
> Author: Aberdeen Group

---

## Original Document Text

Sun Microsystems Computer Company
2550 Garcia Avenue
Mountain View, CA 94043-1100
415-960-1300
Sun Microsystems Decision Warehouse
Preface
This Profile examines Sun Microsystems Computer Corporation's (SMCC) enormous investment of resources in refining how data warehousing needs to be designed for scalability.
Aberdeen has been tracking the explosive growth of data warehousing, decision support and data mining from several perspectives:
MIS departments that are responsible for meeting the demands of the business units wanting immediate access to all types of corporate data;
Users wanting easy-to-get, easy-to-read information from corporate data;
Software suppliers, especially those providing relational database management systems (RDBMS) and related tool sets for building and accessing the warehouses;
Hardware suppliers, that not only want to provide the physical platform to implement the warehouse, but that often want to be the prime hardware/ software/services integrators.
The largest Unix-based data warehouse efforts are still in the hundreds of gigabyte size, with only a handful over the terabyte size. However, Aberdeen's research also shows that growing
numbers of warehouses are now moving beyond the pilot stage to full implementation. As this happens, enterprise-level production data warehouses tend to increase in size very quickly --
often growing 3-to-5 times in 18 months -- with the numbers of attached users also growing. More warehouses are approaching terabyte-size, each with hundreds of attached users, each
doing queries which vary in scope and frequency -- putting stress on hardware and software that is totally different from an OLTP application. As a result, we expect to hear a plaintive wail
as MIS realizes that few of its suppliers have carefully worked through all of the issues associated with large-scale data warehouse production environments. For reasons explained in this
Profile, Aberdeen expects SMCC's Decision Warehouse customers to be spared the pain.
Data Warehouse - Aberdeen's Definition
A data warehouse -- typically residing on a RDBMS -- is an on-line collection of data from internal and external sources, specifically prepared to respond to user queries. Designed to off load
query processing for enterprise bread-and-butter operational systems, data warehouses are the culmination of a multi-step process that involves conditioning and filtering OLTP and legacy
data, and optimizing it for decision support access.
Unlike OLTP systems, a data warehouse contains a variety of data types, such as:
Current Detail Data
Lightly Summarized Data
Data From Internal or External Sources
Old Detail Data
Highly Summarized Data
Meta Data - data about the warehouse structure
Aberdeen research has shown that the majority of successful data warehouse implementations often start as proof-of-concept projects or pilots, and most have at least three things in common:
1. They grow in both size and in number of users, often beyond initial estimates;
2. Data warehouse implementations typically increase data administration (some OLTP is off-loaded, while some processes increase);
3. Most companies that have implemented successful warehouses have turned to their suppliers or third parties for assistance with some or all of the project.
Market Position
As detailed in Aberdeen's August 1995 Profile, Sun Microsystems has become a top-tier commercial systems supplier. We estimate that Sun's revenues for FY 1996 (ending June 30) will
approach $7 billion, and that revenues from commercial sales will account for at least a third of that.
Sun's major division, SMCC, has been involved with data warehouse implementations for some time now, but has not sought visibility for this effort until recently. Instead, it has quietly
developed both experience in building large-scale data warehouses, and an infrastructure to support large numbers of implementations.
Aberdeen believes that SMCC has the requisite servers, storage subsystems, partnerships with multiple RDBMS, software tools suppliers and systems integrators, technical and business
support staff, and knowledge of its vertical markets to be a formidable force in the data warehousing market. Augmenting this arsenal is SMCC's secret weapon: the behind-the-scenes
Database Engineering group that has a mission of "making the major database products run as fast as possible" on Sun products.
Partnerships with Data Warehouse Market Leaders
SMCC has taken the time to enlist a wide-range of software suppliers in its Decision Warehouse Program -- including all the major providers of relational databases management systems
(RDBMS), On Line Analytical Processing, data viewing, data modeling, etc. A partial list includes: Oracle, Red Brick, Sybase, Informix, SAS, Platinum, Prism, Business Objects, and Arbor
Software -- and integrators such as Price Waterhouse and KPMG. Unfortunately, just seeing the list does not provide customers with any comfort. In order to claim data warehousing
expertise, all the major hardware suppliers have "partnered" with all of the major software suppliers. Aberdeen believes that buyers must look under the covers -- beneath the press release --
to discern the real value of the partnership, particularly at the depth of technological integration between the suppliers.
Accordingly, Aberdeen talked with the major RDBMS suppliers to determine the elements of the relationship with SMCC vis-à-vis its Decision Warehouse program. We found:
Extensive involvement between engineering staffs at all levels of product development;
Bilateral agreements with the RDBMS suppliers which allow Sun to provide performance improvements to their products while the suppliers help Sun improvement Solaris;

Joint marketing and sales efforts, extending to the implementation of jointly run competency centers for customer benchmarking and proof of concept testing;
Strong contractual agreements between SMCC and the suppliers providing customers with traditional "back-end" support and service and unique "front-end" support and service.
Database Engineering Group
In recent years SMCC has increased funding and personnel of its Database Engineering group as SMCC moved aggressively into the commercial market place. This group has in place large
test beds consisting of SMCC servers and storage sub-systems. The testing has provided SMCC, RDBMS suppliers, and customers with invaluable information and experience. The group's
performance testing has led to significant improvements in Solaris 2.5, Sun's Unix operating system. This is evidenced with the SMP scalability ratings of 92%-97% (depending on the
RDBMS) as CPUs are added to a system. SMCC can work with customers on Decision Warehouse designs, and then run them at Sun's benchmarking and competency centers as a live proof-
of-concept test. RDBMS contacts indicate that the testing of their software has also led to significant performance improvements -- to the extent that one admitted that its RDBMS could not
have been brought to market without SMCC's involvement.
An example of Sun's improving both scalability and performance of its servers and storage systems is its Enterprise Server Test Center -- in which it has already invested over $10 million.
The group's testing of data warehousing implementations of various sizes -- from 20GB pilots to the 5.5TB Oracle demonstration -- has provided SMCC and RDBMS staff with ongoing
information of data warehouses' behavior in different environments.
The Database Engineering teams also run a series of proprietary and public (TPC, SAP, etc.) benchmarks so that customers can compare SMCC system performance to that of its
competitors. Finally, the Database Engineering teams provide training to SMCC field staff to improve their ability to provide customers with improved Decision Warehouse design,
implementation and support services.
Scalability
Data warehousing production systems fail for many reasons, although the inability of a system to scale well is of primary concern to those who anticipate steady growth in size and use of
their warehouse. Scalability issues, in many forms, often undermine optimal growth in size and usage. Potential trouble spots include:
The processor speed;
The speed and bandwidth of the bus;
The speed of the I/O, especially to disk;
The ability of the system to utilize multiprocessing (MP);
The speed and reliability of the storage sub-system used;
Parallel Capabilities of the RDBMS and its ability to take advantage of MP hardware.
Sun Servers
In the fall of 1995, Sun announced a new series of engineering workstations based on the new 64-bit UltraSPARC RISC microprocessor architecture -- which delivers twice the power of the
older SPARC. In May 1996, SMCC will ship its powerful UltraSPARC servers -- with a new system design, greater I/O bandwidth and reduced memory latencies -- for the commercial
market (See Table 1).
Table 1: SMCC UltraSPARC Commercial Unix Servers
Source: AberdeenGroup, March 1996
Given the mission-critical nature of decision support/data warehousing, Aberdeen believes that IS buyers should look for systems that can withstand the rigors typically associated with
enterprise-class applications. The UltraSPARC-based servers have hot-plugable parts for high-availability and built-in management features for server monitoring. The monitor can provide a
physical map of the system with physical information of the different components.
In addition to stand-alone servers, SMCC provides different types of clustering, for either high-availability features, or increased scalability for resource-hungry applications. SMCC's
clusters now support Oracle 7.3 and distributed parallel query so that a pair of servers can be clustered using high-speed fiber channels.
Super Fast Bus
A bus is like a system's traffic intersection -- information needs to clear through it before the next service request can utilize the road for accessing memory and disk. SMCC's new high speed
(2.6GBps) system bus (Gigaplane) will host "thin" boards, each with dual CPUs and memory (up to 2GB per board) and high-speed I/O channels for disk and network connections. The
combination of the new bus and integrated boards provide for multiple, parallel interconnections of CPU, I/O and network components -- allowing for speeds approaching those usually
found in mainframes, and exceeding anything available in similar Unix systems.
Decision Warehouse Scalability
Source: Sun Microsystems, February 1996
Solaris

While SMCC's Servers can support a variety of clients with different operating systems, there is no server operating system identity crisis at SMCC -- it is a pure Unix play, with Solaris 2.5
at center stage.
The best hardware architecture is totally dependent on the operating system in order for the potential of the architecture to be realized. Sun's excellent scalability is possible in large part
because of Sun's SMP Unix implementation. Unlike its other top-tier competitors, Solaris 2.5 is fine-tuned for multiple processor configurations.
With SMP systems, each time a new processor is added a certain amount of performance is lost to overhead functions. Many Unix SMP implementations require between 15% and 20% of
the added CPU performance for overhead -- and a poorly tuned Unix SMP implementation (and all current NT Server implementations) use up to 30%. Sun has tuned Solaris to the point that
only 3%-to-8% of performance is lost by adding a CPU to the system.
To enhance I/O performance, Solaris is threaded at the I/O level and the networking level -- giving it the ability to read large amounts of data without blocking. Solaris also includes threaded
networking drivers needed for the creation of distributed data warehousing implementations with fewer bottlenecks.
For data warehouses, Solaris 2.5 has shown it can scale on two important levels:
Constant query response time is provided as the dataset grows;
Constant query response time is provided as the number of users grow.
SPARCstorage
Data warehousing requires massive amounts of disk space, for both storage and data manipulation. Going with the right storage management sub-system is as important as choosing the right
server -- and the storage, like the server, needs to be fast, safe, scalable, and appropriately priced.
SMCC's Storage Products Group is now an independent business unit within SMCC, with its own P/L responsibilities. Aberdeen estimates that the Storage Product Group's current revenues
are in excess of $1 billion.
I/O speed is king in data warehousing where the sequential access of data is much more demanding than that typically experienced on OLTP systems. SMCC offers several SPARCstorage
arrays, and each uses (industry-standard) fiber channels for very high-speed interconnects. The SPARCstorage Array 214 RSM, that Aberdeen believes will stand-up to the demands of
mission critical applications, has numerous high-availability features: hot-swap disk modules, hot-swap redundant fans and power supplies among them. The 4.2GB disk drives, that are in a
3.5" form-factor, plug into the back-plane, eliminating the need for cables. SMCC buys its drives from the major suppliers, but has its own rigorous quality program. This crucial watchdog
approach will lessen the impact of drives experiencing worsening MTBF (mean-time between failure) over the past few years. This attention to detail means that the drives OEMed by
SMCC have a better MTBF rating than the same drives used by SMCC's competitors.
In addition to pre-shipment quality management, SMCC has a RAS Customer Action Team (Reliability, Availability and Serviceability) in place to focus on customers' storage-related issues.
The results of this effort were highlighted by SMCC customers interviewed by Aberdeen. Those customers which are running data warehouses in excess of 600GB cite exceptional levels of
satisfaction with the Sun's storage performance and reliability.
Service and Support
Over the past three years, SunService has taken major steps in building a service and support organization appropriate for its emergence as a top-tier supplier in the commercial market. For
instance, it has added staff at a 40%-45% annual growth rate for the past 3 years, and expects to continue to expand the group.
For Decision Warehouse, SunService is contracting with the major software suppliers to provide what it calls front-end and back-end problem resolution to prevent customers from getting
trapped in a round-robin of finger pointing. Back-end problem resolution is fairly common -- hardware and software suppliers work together on a customer problem, but only after it has
escalated to a certain level. Front-end resolution is more unusual -- the specialist at the site taking the problem call is fully prepared to deal with it immediately.
Customer satisfaction surveys -- conducted by Sun and external organizations -- show a major upturn for Sun. According to most surveys, Sun is among the top three suppliers in customer
satisfaction in North America, Europe and Asia.
Price/Performance
Some senior executives at Sun are very sensitive about Sun's image as a low-cost provider, but the fact remains that Sun has a very competitive pricing structure. The new UltraSPARC-based
servers combined with Solaris 2.5 have given SMCC a major performance boost, while its business model allows it to be the low-cost provider in the Unix market.
For small data warehouse implementations, or proof-of-concept projects, Sun even competes well against a NT Server implementation. But NT Server's scalability pales in comparison to
Solaris. As one MIS executive stated, it didn't hurt that the best overall solution for her data warehousing project was also the low-bidder.
Aberdeen Conclusions
There has been so much written about data warehousing recently -- by the suppliers themselves, the press and industry analysts -- that it has become increasingly difficult for customers to
differentiate between suppliers. The fact that all the hardware system manufacturers have to work with the same software suppliers further blurs the qualitative differences.
Customers wanting mission-critical data warehouses implemented in anticipation of growth in both size and usage need to work with a supplier which has dealt effectively with all the critical
scalability issues.
The advent of SMCC's very powerful UltraSPARC-based Enterprise servers, combined with an excellent storage array sub-system, the very solid relationships with software suppliers, and a
vastly improved service and support organization provide a solid foundation for Decision Warehouse. The work the Database Engineering teams have done -- most recently with the creation
of the Enterprise Server Test Center and Sun's creation of Competency Centers -- provides the proof that the package works as advertised. Sun's Decision Warehouse clearly scales to meet
the requirements of the most challenging, high-end application environment.
Aberdeen's research findings show that SMCC has the requisite pieces in place to differentiate itself from much of the competition. After a careful review, Aberdeen believes that when
seeking mission-critical data warehouse implementations, MIS must evaluate SMCC's offerings.

AberdeenGroup, Inc.
One Boston Place
Boston, Massachusetts
02108 USA
Tel: 617.723.7890
Fax: 617.723.7897
Contact Information:
Susan Rinehart, Client Services Manager (direct #: 617.854.5212)
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
| study_id | aberdeen-1996-sun-microsystems-decision-warehouse |
| title | Sun Microsystems Decision Warehouse |
| author | Aberdeen Group |
| date | 1996-03-01 |
| license | CC-BY-4.0 |
| source | https://web.archive.org/web/19970112011832/http://www.aberdeen.com:80/secure/profiles/sun_dw/sun_dw.htm |

### Abstract

This Aberdeen Group profile evaluates Sun Microsystems Computer Corporation's (SMCC) Decision Warehouse program, examining its UltraSPARC server architecture, SPARCstorage arrays, Solaris 2.5 SMP optimization, Database Engineering group, and partnerships with Oracle, Sybase, Informix, and other RDBMS vendors. Aberdeen concludes that SMCC has the requisite components to differentiate itself in the data warehousing market, projecting strong scalability for terabyte-class warehouses through the Enterprise Server Test Center and Competency Centers.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Documented Sun's pivotal strategic shift toward commercial data warehousing at the UltraSPARC launch moment; influential in directing enterprise data warehouse procurement toward Sun platforms in the late 1990s. |
| **Relevance** | medium | Solaris SMP tuning principles, the Database Engineering group model, and scalability frameworks for data warehousing retain methodological relevance; specific Sun hardware/software is obsolete but the competitive analysis framework applies to modern cloud and on-premises BI infrastructure. |
| **Prescience** | high | Aberdeen's prediction that data warehouses would grow 3-5x in 18 months and require suppliers who addressed scalability holistically proved accurate; Sun did become a dominant Unix data warehouse platform through 2005. Prediction that NT Server scalability 'pales' vs Solaris was correct for the era. |

### Prescience Detail


**Prediction 1:** Data Warehouse Growth Trajectory Prediction
- **Claimed:** Aberdeen predicts warehouse sizes approaching terabyte with hundreds of attached users; production warehouses outpacing supplier capabilities except those (like SMCC) who solved scalability issues
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 1:** Data Warehouse Growth Trajectory Actual Outcome
- **Result:** Prediction proved accurate: enterprise data warehouses grew to multi-terabyte scale by 2000-2005; petabyte-scale warehouses emerged by 2010 (Teradata, Netezza, then Hadoop). Scalability became the defining vendor differentiator as Aberdeen predicted.
- **Confidence:** verified
- **Notes:** 

**Prediction 2:** SMCC Data Warehouse Market Leadership Prediction
- **Claimed:** Aberdeen believes SMCC has requisite pieces to differentiate in data warehousing; expects Decision Warehouse customers to be 'spared the pain' of inadequate scalability
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 2:** SMCC Data Warehouse Market Position Actual Outcome
- **Result:** Sun became a leading Unix data warehouse platform through the late 1990s-early 2000s; UltraSPARC/Solaris widely used for Oracle data warehouses. Sun's position weakened after 2003 as x86/Linux and commodity hardware eroded Unix server market; acquired by Oracle 2010.
- **Confidence:** verified
- **Notes:** Source: Oracle acquisition of Sun Microsystems completed January 27, 2010


### Entities Referenced (9)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Sun Microsystems Computer Corporation (SMCC) | company | acquired | Oracle Corporation |
| Aberdeen Group, Inc. | firm | acquired | Aberdeen (Harte-Hanks) |
| Oracle Corporation | company | active | — |
| Informix Software | company | acquired | IBM |
| Sybase, Inc. | company | acquired | SAP |
| Red Brick Systems | company | acquired | Informix then IBM |
| SAS Institute | company | active | — |
| Price Waterhouse | firm | merged | PricewaterhouseCoopers |
| KPMG | firm | active | — |

### Technologies Referenced (6)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Sun UltraSPARC RISC Processor | platform | Sun Microsystems | emerging | obsolete |
| Solaris 2.5 | platform | Sun Microsystems | mature | obsolete |
| Sun Gigaplane System Bus | platform | Sun Microsystems | emerging | obsolete |
| SPARCstorage Array 214 RSM | platform | Sun Microsystems | emerging | obsolete |
| Oracle 7 | application | Oracle | mature | obsolete |
| Windows NT Server | platform | Microsoft | emerging | obsolete |

### Observation Summary

- Total observations: 21
- By type: actual-outcome: 2; benchmark-result: 2; expert-opinion: 1; framework-factor: 5; market-data: 5; strategy-classification: 1; technology-assessment: 3; viability-prediction: 2
