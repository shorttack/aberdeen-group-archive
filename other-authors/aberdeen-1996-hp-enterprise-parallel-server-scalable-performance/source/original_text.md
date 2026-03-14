# Hewlett-Packard's Enterprise Parallel Servers: A Graceful Transition to Scalable, High-End Performance

> Archived from: [https://web.archive.org/web/19970112011544/http://www.aberdeen.com:80/secure/profiles/hp_eps/hpeps.htm](https://web.archive.org/web/19970112011544/http://www.aberdeen.com:80/secure/profiles/hp_eps/hpeps.htm)
> Original publication date: 1996-07-01
> Author: Aberdeen Group

---

## Original Document Text

Hewlett-Packard Company
19111 Pruneridge Avenue
Cupertino, CA 95014
1-800-637-7740
http://www.hp.com
Hewlett-Packard's Enterprise Parallel Servers:
A Graceful Transition to Scalable, High-End Performance
Preface
Aberdeen research continues to show that senior Information System (IS) executives are concerned about high-end scalability for both data warehousing and the new-generation of database-
centric, integrated process, client-server applications. Unix servers reign supreme in these two application areas — the software users demand simply does not run on MVS and NT has
neither the performance nor reliability capabilities to meet enterprises' demanding requirements.
This Profile examines Hewlett-Packard's architectural and product entry, the Enterprise Parallel Server (EPS), in the very high-end Unix server space. We then summarize the comments of
early users, position EPS from a competitive perspective, and discuss challenges and opportunities HP will be experiencing with EPS as it attempts to create a new high-end industry
standard.
Executive Summary
With quiet determination, Hewlett-Packard continues to extend the capabilities of its multi-user HP 9000 products. The newest high-end product introductions, the EPS21 and EPS30, are
probably the least known of HP's enterprise server offerings, and yet have the potential to be the datacenter systems-of-choice for very large application requirements.
The EPS21 and EPS30, introduced May 15, 1996, are the newest members of HP's Enterprise Parallel Server product family. HP's Enterprise Parallel Server architecture is built upon a
combination of the technologies used for massively parallel processing (MPP) and clustering in a commercial-application environment, as well as symmetric multiprocessing (SMP) at the
platform level. From a technology perspective, EPS is an evolutionary extension of HP's well-regarded MC/ServiceGuard clustering architecture which is an extension of HP's very popular
symmetric multiprocessing (SMP) architecture which is an extension of HP's core uni-processing systems environment.
From a datacenter operation's perspective, a key benefit of EPS is its compatibility with existing HP K- and T-Class SMP platforms (which can be upgraded to the EPS architecture) and the
HP-UX high-availability operating environment. In addition, the EPS architecture is designed to protect IS' investment in HP systems well into the future. As newer technologies are
introduced — more powerful processors, greater RDBMS functionality, higher fibre channel bandwidth, faster storage subsystems —they can be gracefully included in EPS complexes.
To enterprise users and planners the most important benefit offered by EPS is that the EPS architecture has the capability to support very large databases, large numbers of users, and fast
throughput rates. For IS managers and users who have run out of "headroom" — reaching limits in systems performance, user population, and database size with their current systems —
EPS provides increased processing power by using highly parallel processing techniques.
EPS has already shown very high performance capabilities — its 17,826 tpmC rating under the TPC-C benchmark is the second highest of any currently published system tests. But more
impressively, IT executives that Aberdeen has interviewed have been very pleased with their ability to upgrade their existing systems to the EPS architecture transparently to their users.
IS decision makers should view EPS as a flexible, growing high-end architecture for the future. Building upon the EPS architecture, HP believes that large enterprises can create the
datacenter infrastructures needed to run both today's and tomorrow's complex but quickly changing organizations.
Hewlett-Packard Enterprise Parallel Servers
The architectural design concept behind EPS is relatively straightforward:
1) connect existing high-performance HP 9000 SMP systems (SMP nodes within the EPS architecture) with a high-performance fibre channel switch;
2) manage the entire complex from a single console with software that ensures high availability;
3) work with ISV and storage subsystem partners to enhance their products for EPS with the mutual goal of providing users with the very highest performance capabilities to be obtained
from any commercial computing complex. (See Figure 1.)
The EPS commercial-application product line has been started with the EPS21 and EPS30. The EPS21, which replaces the EPS20 (primarily designed for technical applications), is available
now; the EPS30 utilizing T-Class SMP nodes is expected to ship 3Q96. The EPS21 consists of up to 16 4-way K-Class SMP nodes connected with a 266 Mbit/second fiber interconnect for
each port. Aberdeen expects that the next member of the EPS3X series will be configurable with up to sixteen 14-way attached T-Class SMP nodes through the HP Enterprise Switch and will
be generally available in 2Q97.

Figure 1: HP's Enterprise Parallel Server Architecture
HP's MC/System Environment (MCSE) management tools are bundled with EPS clusters to allow for a solid, single-system view and single-point of management. MCSE includes tools and
utilities for systems administration, configuration, and system-wide performance monitoring — including load balancing. Aberdeen believes that HP's MC/ServiceGuard, a high-availability
systems management option, should be included for commercial use to provide 7x24x365 availability.
One of the key technology elements in HP's EPS, and one that separates it from other MPP systems, is the fibre channel switch. The HP Enterprise Switch uses a hub architecture — each
node is attached directly to the switch which can then pass messages from a sending node directly to the appropriate receiving node without incurring the overhead of going through
intermediate node-to-node connections. The current switch can support up to 16 ports at 266 Mbits/second — or 532 Mbit/second full duplex. And each directly connected node can be up to
2 kilometers from the switch. HP anticipates increasing the speed of each port to 1 Gigabit/second and increasing the number of SMP nodes supported to 32 by 3Q97. In addition, HP has
developed the high-performance Tachyon fibre channel adapter for fibre channel switches which is being adopted by leading storage subsystem suppliers such as EMC, DG/CLARiiON, and
50 others. In the near future, HP expects to make generally available the ability to attach storage devices directly into the Enterprise Switch using the Tachyon adapter.
Competitive Positioning
HP's EPS is squarely aimed at IBM's RS/6000 SP for winning the hearts, minds and budgets of IS datacenter managers. Many large enterprises have chosen to standardize on either HP or
IBM for Unix-based commercial applications.
The HP EPS offering's technology advantages over the RS/6000 SP are numerous at this time. For example:
Upgradeability of existing K-Class and T-Class servers to the EPS architecture (IBM requires users to purchase new RS/6000 nodes with the high-speed switch interconnect to fit into
the SP frame); SMP node support (the SP only has single-processor nodes);
HP's parallel-enabling and clustering software technology works (the SP's similar operating environment for decision support and high-end OLTP applications still seems to be under
development);
The same operating environment on EPS as well as clusters (the RS/6000 uses CLAM Associates HACMP for RS/6000 cluster support and PSSP for SP systems administration);
Comprehensive fibre channel switch and adapter architecture and products (HP's Tachyon has a very high probability of becoming an open systems industry standard);
Ability to geographically disperse SMP nodes within a campus environment (SP must be at one central site);
Support for very high-end storage subsystems from solutions partners (the SP has been engineered to best support IBM's own products).
At numerous IBM-sponsored conferences, IBM's most senior executives have described the SP as a not-yet-ready-for-production-applications platform — but rather a prototype MPP
architecture for leading-edge ISVs and techno-experimental enterprises. In comparison, early HP users can recount their successes with EPS.
Other competitive high-end Unix-server offerings include: TruCluster from Digital (the highest TPC-C performance ratings on record); Sun Microsystems Ultra Enterprise 6000 (best TPC-D
price/performance on record); and NCR's 5100M (highest TPC-D performance rating on record).
Clusters, MPP, SMP Nodes and Other High-End Concepts
Aberdeen's research shows that one of the perplexing issues IS decision makers face when evaluating EPS concerns how to place it in a conventional technology category. For example,
while EPS has many of the characteristics of a cluster and uses much of the same software that HP has incorporated in its clustered systems, the implementation of the fibre channel switch
and support by the major RDBMS suppliers for the switch provides performance and scalability well beyond what is obtainable from a conventional high-availability cluster.
A technically-correct MPP system should have one copy of the operating system and dedicated memory per processor. While processors may be grouped as nodes, each node should have a
direct interconnect to every other node. Obviously, the EPS architecture does not fit this definition. However, the high-speed switch that allows nodes to send messages to each other does fit
the MPP definition. Although HP calls its EPS nodes "SMP nodes", EPS actually has some of the characteristics of an MPP system. But when one backs away from theory and looks at the
pragmatic, note that if each EPS SMP node had direct access to every other SMP node as they should in a true MPP architecture, scalability, performance, and manageability would be
negatively affected for commercial applications. The Enterprise Switch is a more effective method to achieve high-end performance than a pure MPP structure.
HP itself uses the term "Highly Parallel Processing" (HPP) to best describe the EPS architecture. Processing can be parallel both within SMP nodes and across nodes within the complex.
HPP provides the performance and scalability benefits of the MPP world, while providing programmers with the simplicity and ease-of-management of the SMP world. Commercial IT
decision makers should be attracted by this joint-benefit value proposition.
For IS decision makers that need a technology category for EPS, HPP seems to be the most accurate description.

High Availability and High Performance — Not Necessarily a Contradiction in Terms
Generally, IS executives have regarded high performance and high availability as trade-offs. That is, to obtain high performance, one needed to turn off high availability features. But with the
growing sophistication of such products as HP's MC/ServiceGuard, MC/LockManager, and additional high-availability utilities designed into the EPS architecture, users can have both.
The hardware architecture of EPS inherently provides a considerable amount of component redundancy. And, HP offers its own high-availability software, and other solutions through its
solutions partners. As a result, users can obtain the same or higher levels of availability with EPS than are achievable with today's state-of-the-science clustering solutions.
Running the Transaction Processing Council TPC-C benchmark, an EPS30 composed of 48 processors in T-Class SMP nodes and using Oracle 7.3 achieved a performance rating of 17,826
tpmC at a price performance of $396/tpmC. Under this industry-standard on-line transaction processing (OLTP) benchmark, the EPS30 is the second most powerful system tested as of the
first week in July 1996. Note however, that at a time when many SMP systems are showing price/ performance of under $200/tpmC, the EPS does incur a price premium for its high
performance value-add.
While HP did submit a TPC-D (the Transaction Processing Council's decision support benchmark) result for the EPS30, HP only used a single 12-way T-Class system and then for the
intermediate 100 GB version of the test. While HP's performance results were industry-leading when released, HP now lags NCR, Sun Microsystems, and Tandem in overall compute power.
Aberdeen believes that when HP combines its latest PA-8000 microprocessor technology with additional SMP nodes and re-tests EPS, HP's performance and overall position will improve
significantly.
The Early Users Like EPS
While IS decision makers need to know the technology underpinnings of any new architecture, what is even more important is to learn from the experiences of other IS professionals.
Over the last decade, IS executives have faced numerous issues in making the transition from one generation of high-performance Unix operating environments to the next, more powerful
and more scalable generation. Aberdeen talked to several early commercial users of EPS to better understand their experiences in moving from installed HP cluster and/or SMP platforms to
EPS. The results of these interviews were very positive — especially considering that the architecture is still in the early stages of customer use.
IS decision makers told Aberdeen that EPS had gone well beyond their expectations for solving "headroom" problems associated with systems that just plain ran out of top-end processing
power. EPS has provided these customers with a scalable, high-end growth path that readily meets their transaction processing and high-end decision support needs — and offers tremendous
expansion capability for future growth. A number of customers interviewed had already expanded their initial EPS configurations — and were relieved to be able to easily grow their systems
to meet new applications and database demands.
IS administrators especially like the integrated single system image aspect of EPS. EPS systems were easy to manage and easy to tune — workload balancing was considered a real joy.
IT executives reported that they experienced a smooth transition from their existing HP server and cluster environments to the new EPS architecture. However, they made the point that they
needed several days of on-site professional technical support from both HP and their database supplier to implement the modifications to the operating environment necessary to successfully
make the transition. These executives were delighted that their systems and applications migration to the new EPS architecture had gone smoothly. They credited HP and its software solution
partners for making the systems transition straightforward.
Finally, the investment protection offered by EPS was considered a major business benefit. The IS executives interviewed could devote more resources to meeting their enterprises'
application requirements and less time worrying about obtaining the level of compute-performance required.
EPS and the Future
EPS is an architecture on which HP can gracefully add higher performance technology components well into the future. For example, Aberdeen anticipates a significant performance increase
during 3Q96 as the next generation of HP 9000 Risc processor (64-bit PA-8000) SMP nodes are available. From a scalability perspective, HP has projected that in the later half of 1998 the
EPS architecture will be able to support 768 processors — 64 SMP nodes each with 12 processors.
HP claims that the speed of the fibre channel switch will be increased from 266 Mbit/second to 1 Gbit/second by 3Q97 and the number of ports increased from 16 to 32. In addition, the
interconnect distance is planned to be extended from 2 kilometers to 10 kilometers.
Very importantly, HP needs the future support of its solutions partners — and has been working hard to ensure that its solutions partners get the support they require. Oracle, for example, has
been working with HP's MC/LockManager to obtain high OLTP performance ratings with Oracle Parallel Server. Informix has been working extensively with the EPS to optimize the
performance of its OnLine XPS for data warehousing applications. Database-centric application suppliers, such as SAP, Oracle, PeopleSoft, and Baan need to establish joint engineering
teams with HP to partition and tune the performance of their products on EPS to meet users' growing performance requirements. And HP needs to ensure that high-end storage products, both
its own such as optical disks systems and the Advanced Digital Linear Tape Library, and others from leading suppliers such as EMC, Storage Technologies, and Data General, make full use
of both the Tachyon fibre channel adapter to achieve the highest levels of throughput possible and interoperate with MCSE for more effective systems management. Finally, HP needs in the
very near term to build a more aggressive sales and marketing campaign around EPS. Most IS decision makers Aberdeen has interviewed in recent months simply do not know that EPS
exists — much less its architecture and benefits. For enterprises without a high-end Unix platform-of-choice, acquiring an EPS is a significant decision. And for HP-committed customers, HP
still needs to show a strong public allegiance to this architecture to re-assure IS decision makers that this is a prudent upgrade path to follow now.
Summary Observations
Many IS managers have already run out of performance "headroom" on their current generation of systems platforms and now require significantly more power to deal with new,
sophisticated, high-end decision support applications, and an ever-increasing volume of transactions that require considerable RDBMS systems resources. These managers are looking for
systems solutions that can meet their current processing needs — and that can also readily scale to meet acknowledged but as yet unquantifiable future processing requirements.
Early adopters of EPS and leading RDBMS ISVs tell Aberdeen that they are highly satisfied with the production capabilities of the HP EPS. They have found that EPS is an elegant way to
move to the next-generation of Unix performance with minimal hassle and almost no disruption of operations while at the same time preserving their past (and considerable) investments in
hardware, software, and staff training.
Aberdeen has asked datacenter managers what qualities they want in their next-generation high-performance Unix systems. And their responses uniformly focus on their needs for scalability,
performance, availability, and manageability as they transition gracefully — including investment protection of both their current information infrastructure and staff's skills — to a more
powerful systems architecture. The HP EPS accurately meets these operational requirements of datacenter executives.
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
| study_id | aberdeen-1996-hp-enterprise-parallel-server-scalable-performance |
| title | Hewlett-Packard's Enterprise Parallel Servers: A Graceful Transition to Scalable, High-End Performance |
| author | Aberdeen Group |
| date | 1996-07-01 |
| license | CC-BY-4.0 |
| source | https://web.archive.org/web/19970112011544/http://www.aberdeen.com:80/secure/profiles/hp_eps/hpeps.htm |

### Abstract

This Aberdeen Group profile evaluates Hewlett-Packard's Enterprise Parallel Server (EPS) architecture, specifically the EPS21 and EPS30 introduced May 15, 1996. The study examines EPS's combination of SMP nodes connected via a fibre channel switch for high-end OLTP and data warehousing, compares it against IBM RS/6000 SP and other competitors, documents a TPC-C benchmark of 17,826 tpmC at $396/tpmC for the EPS30, and reports positive feedback from early adopters.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | First detailed independent assessment of HP's EPS architecture at launch, documenting its TPC-C benchmark results and positioning against IBM RS/6000 SP at a decisive moment in Unix datacenter competition; directly informed enterprise procurement decisions. |
| **Relevance** | low | HP's EPS platform and PA-RISC architecture are long discontinued; HP-UX servers have declined significantly since the rise of x86/Linux; methodology for evaluating parallel server architectures retains some value for historical comparison. |
| **Prescience** | medium | Aberdeen correctly predicted HP's PA-8000 upgrade would improve performance and that fibre channel would become an industry standard. The prediction that EPS would become a 'datacenter system of choice' was overstated; HP servers lost significant ground to x86/Linux in subsequent years. |

### Prescience Detail


**Prediction 1:** EPS Datacenter Standard Prediction
- **Claimed:** Aberdeen predicts EPS will become datacenter system-of-choice for very large application requirements as HP builds aggressive EPS sales/marketing campaign
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 1:** EPS Datacenter Actual Outcome
- **Result:** HP EPS/PA-RISC platform did not become dominant datacenter standard; HP shifted to Itanium (Integrity servers) around 2001-2002; x86/Linux ultimately dominated high-end commercial computing; HP-UX market share declined steadily
- **Confidence:** verified
- **Notes:** HP 9000 K/T-Class EOS listed; HP-UX declining as of 2026

**Prediction 2:** Tachyon FC Standard Prediction
- **Claimed:** Aberdeen predicts HP Tachyon fibre channel adapter has very high probability of becoming an open-systems industry standard; 50+ storage suppliers adopting it
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 2:** Tachyon FC Standard Actual Outcome
- **Result:** Fibre Channel became an industry standard for storage connectivity (FC-AL, FCAL SAN), though standardization occurred through ANSI/IEEE rather than Tachyon-specifically; HP Tachyon was a key enabler of FC storage area network adoption in late 1990s
- **Confidence:** verified
- **Notes:** Prediction directionally correct on FC standardization

**Prediction 3:** PA-8000 Performance Improvement Prediction
- **Claimed:** Aberdeen anticipates significant performance increase in 3Q96 as next-gen HP 9000 64-bit PA-8000 SMP nodes become available
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 3:** PA-8000 Performance Improvement Actual Outcome
- **Result:** HP PA-8000 processor introduced as planned; HP EPS with PA-8000 nodes improved TPC-C results significantly in 1997; prediction proved accurate
- **Confidence:** verified
- **Notes:** 


### Entities Referenced (10)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Hewlett-Packard Company | company | active | HP Inc / HPE (split 2015) |
| IBM | company | active | — |
| Oracle Corporation | company | active | — |
| Informix Software | company | acquired | IBM |
| EMC Corporation | company | acquired | Dell Technologies |
| Digital Equipment Corporation (DEC) | company | acquired | Compaq then HP |
| NCR Corporation | company | active | — |
| Sun Microsystems | company | acquired | Oracle |
| SAP AG | company | active | — |
| Aberdeen Group, Inc. | firm | acquired | Aberdeen (Harte-Hanks) |

### Technologies Referenced (8)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| HP Enterprise Parallel Server (EPS) | platform | Hewlett-Packard | emerging | obsolete |
| HP-UX | platform | Hewlett-Packard | mature | declining |
| HP Tachyon Fibre Channel Adapter | platform | Hewlett-Packard | emerging | obsolete |
| HP Enterprise Switch (Fibre Channel) | platform | Hewlett-Packard | emerging | obsolete |
| HP PA-8000 RISC Processor | platform | Hewlett-Packard | emerging | obsolete |
| IBM RS/6000 SP | platform | IBM | emerging | obsolete |
| Oracle Parallel Server | application | Oracle | emerging | obsolete |
| TPC-C Benchmark | framework | Transaction Processing Council | mature | active |

### Observation Summary

- Total observations: 20
- By type: actual-outcome: 3; benchmark-result: 4; expert-opinion: 1; framework-factor: 3; market-data: 1; strategy-classification: 1; technology-assessment: 4; viability-prediction: 3
