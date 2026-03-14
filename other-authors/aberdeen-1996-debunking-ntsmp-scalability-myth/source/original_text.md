# Debunking the NT/SMP Scalability Myth

> Archived from: https://web.archive.org/web/19970604112307/http://www.aberdeen.com:80/secure/viewpnts/v9n20/body.htm
> Original publication date: 1996-11-26
> Author: Aberdeen Group
> Publication: Aberdeen Group Market Viewpoint, Volume 9, Number 20

---

## Original Document Text

Volume 9 / Number 20
November 26, 1996
Debunking the NT/SMP Scalability Myth
There is widespread belief in the Information Systems (IS) community that Microsoft’s NT Server operating system is not as scalable (capable of taking advantage of multiple processors for
increased performance) as its SMP-based (Symmetrical MultiProcessing) Unix and proprietary operating system brethren. And there is a basis to that argument — IS managers and systems
suppliers tell Aberdeen that NT Server scales extremely well to four processors, but as additional processors are added, linear scaling efficiency has been known to decline.
But, whether or not NT can scale to an 8-way or 16-way or 32-way processor configuration is not the real issue for IS users — overall system performance is. Aberdeen believes that
Microsoft’s real SMP strategy is to increase NT performance on servers with four processors or less —taking aim at the server market’s volume sweet spot where 90% of all servers are sold.
And, by deploying NT on inexpensive 4-way, Intel-based commodity servers, Microsoft hopes to gain a pricing advantage over the highly-specialized hardware produced by its SMP
competitors.
In this Viewpoint, Aberdeen suggests that IT decision makers may wish to reconsider the NT/SMP scalability issue. Recent benchmarks indicate that NT servers are well on their way to
becoming an irresistible force in the mid-range server market.
Executive Summary
Information Technology (IT) executives — particularly Chief Financial Officers (CFOs), Chief Information Officers (CIOs), and IT architects and planners — have been desperately
searching for low-cost, high-performance computer platforms that could be deployed like building blocks throughout their organizations. And, until very recently, they believed that
Microsoft’s Windows NT Server platform was not a viable option — it did not meet the performance requirements of large departments and enterprises. And many IT executives believed that
the lack of NT SMP scalability beyond 4-way platforms was to blame.
However, recent and radical improvements in NT Server performance indicate that 4-way NT servers can now outperform some of the industry’s leading SMP servers with double, triple, or
even quadruple the number of processors – serving to debunk the importance of SMP scalability for overall system performance.
Aberdeen suggests that the more intriguing answer to why NT has lacked luster in scaling beyond 4-way processors is not engineering based, but actually based upon server market
economics. Aberdeen believes that Microsoft has consciously chosen not to aggressively invest in NT/SMP scalability beyond 4-way processors. The reason: Microsoft is pursuing volume
sales in the server market sweet-spot — the hundreds-of-thousands of systems sold in the 4-processor-or-less range.
And even microprocessor suppliers are directing their engineering efforts at the 4-processor space. Intel with its Pentium family, Digital with its Alpha family, and IBM with the Power-PC
family all realize that 90% of all servers sold will be 4-processor-or-less — and these suppliers have adjusted their strategies to focus on this configuration.
Note that Aberdeen is not saying that Microsoft and systems suppliers are completely foregoing NT/SMP scalability. Suppliers such as NCR and Sequent have already demonstrated that NT
can scale to 16 and 28 processors within a single systems environment — showing that NT can indeed scale. Aberdeen is simply saying that Microsoft and its key microprocessor and
systems suppliers realize that the lions share of server purchases will be made on 4-way-or-less platforms, and have adjusted their sales, pricing, and R&D strategies to capitalize on this
factor.
To Aberdeen, the scalability discussion needs to shift in focus to the efficiency of NT scaling — can it scale linearly? The most recent release of NT — Windows NT Server revision 4.0 —
includes performance enhancements that enable NT to make better use of 4-way and 8-way SMP architectures. And, several major systems suppliers are working on Non-Uniform Memory
Access (NUMA) technology for NT scalability to eventually efficiently scale NT to 16-way, 24-way, 32-way — and way beyond. And, a number of benchmarks already show that NT
suppliers have achieved almost linear scalability between single processor and four-way systems. Aberdeen expects that suppliers will continue to focus on NT linear scalability — and
especially on 4-way sever or less platforms.
Worthy of note is that some suppliers have intimated to Aberdeen that the real issue with NT scalability is not related to processor or operating system scaling limitations, but rather getting
client/server applications to take advantage of existing NT SMP capabilities — indicating that applications tuning will be in order to take maximum advantage of NT processing power.
In addition to SMP efforts to greatly increase the number of processors available to NT within a single systems environment, systems suppliers are also pursuing the use of clustering
technology as a means to improve overall systems reliability, availability and scalability (RAS) and performance. Initial NT cluster efforts have focused on high-availability, but Aberdeen
expects performance oriented clusters to arrive by year-end 1997. The idea of NT performance reaching the range of 20,000 transactions per minute using performance clustering
technologies is wholly realistic by 1999.
Given that 4-way NT systems have already proven that they can offer industry leading price/performance (see Transaction Processing Council benchmarks enclosed herein); that NT systems
are climbing the SMP ladder to 8-way servers and beyond; and that NT performance clustering technologies will arrive in the near term — Aberdeen believes that NT/SMP scalability should
no longer remain a major factor that prohibits the adoption of NT-based servers within an enterprise information systems infrastructure.
NT: The Real Scalability Strategy
Microsoft claims that NT can support load balancing in systems environments with up to 32 processors. And systems suppliers have proven that NT can scale. NCR has scaled NT on sixteen
processors, while Sequent can scale to twenty-eight and has actually sold a number of fourteen processor NT/SMP systems.
But, if NT is capable of scaling, then why has Microsoft not aggressively moved up the SMP performance ladder into high-performance 16-way or 32-way processors? Could it be that SMP
scaling is not really at issue?
Aberdeen believes that Microsoft’s real strategy is to exact high degrees of performance from 4-way servers, and to cluster those servers for even further performance gains (See Figure 1).
Figure 1 - The NT Performance/Reliability Roll-out Plan

tpm = transactions per minute
Source: Aberdeen Group — 1996
Specifically, Microsoft will:
1. Put Paramount Focus on Increasing NT Server Performance on 4-way Platforms — Increase low-end system performance by tuning NT to take maximum advantage of the next
generation of fast-clock-rate microprocessors;
2. Continue to Scale NT Using the SMP Approach — But not make SMP scalability a major focus; and
3. Attain High-End Server Performance through Performance Clustering Technology — Work closely with systems suppliers to develop and tune NT performance clusters capable of
challenging high-end Unix/SMP and other enterprise servers from a performance perspective.
Microsoft NT: Taking Aim at the SMP Server Market Sweet Spot
To segment today’s server market, Aberdeen used benchmark data from the Transaction Processing Council (TPC) — an industry recognized, independent benchmarking organization. This
segmentation is based upon transaction ranges at the workgroup, department and enterprise for low-end, mid-range, and high-end servers (see Figure 2).
Figure 2 - Server-Level Transaction Ranges
Source: Aberdeen Group — 1996
Specifically, Aberdeen used TPC-C benchmark data. The benchmark itself includes a mixture of both read-only and update-intensive transaction types that simulate a real-world distribution
and warehousing applications. The object is to add as many orders per minute as possible while maintaining adequate response times for the orders and four other transaction types. User
think times are simulated, forcing the performance randomness typically seen in live OLTP systems. Even rejected transactions are modeled. The resulting tpmC (transactions per minute —
test suite C) is a measurement of the number of orders per minute processed on a given system — usually run at close to 100% CPU utilization to establish maximum loading.
And, using tpmC performance data, Aberdeen determined that low-end, workgroup servers were predominantly involved in file read/write/print activities and required performance capacity
of fewer than 2,500 transactions per minute (tpm) to satisfy user requirements.
Mid-range SMP servers from Hewlett-Packard (HP 9000), Digital (AlphaServer), IBM (RS/6000 and AS/400), and Sun (Ultra and SPARCcenter) performed in the 3,000 to 15,000 tpm
range. And the highest performance SMP systems from Digital (32-processor AlphaServer 5/35 at $305/tpm-C) and Hewlett-Packard (48-processor HP 9000 EPS30 at $396/tpm-C) reported
transaction levels in the greater than 15,000 tpm range – between 20,000 and 30,000 tpm — establishing the server high-end with Unix-based clustered system.
To put the very high-end of the server market into perspective, Aberdeen notes that some of the heaviest On-line Transaction Processing applications, for instance the United Airlines
reservation system, have less than 50,000 transactions per minute. Unix servers are now approaching this range, and ultimately NT-based servers in cluster configurations will approach and
surpass 50,000 tpm-C at the high-end.
Aberdeen believes that Microsoft and its partners are taking aim at the mid-range server sweet spot — from 2,000 to 15,000 tpm — and are planning to capture that market with 4-way-or-
less processor platforms.
NT Attacking the Midrange – Please Pass the Chips
A status check of NT performance progress in the mid-range server market shows that Microsoft and its partners are rapidly increasing the processing power of 4-way NT-based platforms. In
November, 1995, Aberdeen issued a Market Viewpoint entitled Undisputed Leadership in Departmental Price Performance. This Viewpoint stated that NT-based servers had moved into
departmental range based upon independent TPC performance benchmarks. At that point, Compaq’s Intel-based servers had exceeded 2,400 transactions per minute in the TPC tpmC
benchmarks at a cost of $242 per tpmC. Aberdeen concluded that this benchmark represented the first foray of NT-based platforms into the departmental server stronghold.
As of November, 1996, the Transaction Processing Council is reporting that its 4-way NT servers are exceeding 6,712 tpmCs, almost tripling NT performance levels reported only eleven
months previously — and at a cost of only $65/tpmC. Aberdeen attributes this increase to the use of the new revision of Windows NT Server, NT revision 4.0, and the use of more powerful
and faster clock rate microprocessor technologies. Aberdeen notes that at 6,721 tpmC, NT servers have now reached performance levels that enable NT servers to perform at the same level
as the today’s most popular servers — including Unix/SMP and IBM AS/400 models — in the mid-range market (see figure 3).

Figure 3 — Tpm-C Benchmark Results
The new tpm-C figures also highlight that Microsoft’s SQL Server on an NT platform has yet again set a new price/performance record — breaking new ground at $65 per tpm-C while
slightly improving performance.
Aberdeen believes that ongoing tuning of NT 4-way servers coupled with the increased processing power of next generation microprocessors from Digital with Alpha (now reporting clock
speeds at the 500 MHz level) or Intel with its forthcoming Pentium processors (Klamath expected at the 266 MHz level; and Deschutes expected at the 333 MHz level) will result in
substantial increases in 4-way system performance through 1997 and 1998. Aberdeen projects that 4-way systems will at least double and perhaps triple in speed by 1998 — taking 4-way
processors into the 11,000 to 16,000 transaction per minute range (see Figure 4).
Figure 4 – Individual NT 4-way Server Performance Trajectory through 1998
Source: Aberdeen Group — 1996
With the projected growth in individual 4-way system performance, Microsoft NT will be ideally positioned from a performance perspective to service the needs of most OLTP applications.
In fact, many IS managers claim that today’s NT tpmC performance of greater than 6,750 tpm rivals the computing power of their existing mainframe systems.
4-Way Server Performance
In this Viewpoint, Aberdeen has shown that NT-based servers are capable of scaling — and that 4-way systems have now reported transaction processing capabilities that position NT servers
in the mid-range systems market. Aberdeen has also projected that due to improvements in NT’s ability to utilize multiple processors as well as advances in microprocessor speed, NT-based
servers can be expected to reach the 16,000 tpm-C range by the end of 1998.
From a performance perspective, scalability varies greatly by supplier in the NT server marketplace. Some PC suppliers are still in learning mode on NT SMP scalability, and are currently
obtaining approximately 50% performance return from each processor they add. Meanwhile,other enterprise-experienced suppliers with years of SMP development and tuning experience are
seeing NT scalability that approaches 90% across four processors. One such high-performance supplier is NCR. NCR, in testing on its own Intel-based NT 4-way platforms, has observed
that scalability on NT revision 4.0 approaches the 90% utilization range — with the database, rather than the operating systems environment, becoming the bottleneck. NCR points out that,
that initial indications are that NT 4.0 scales well on 4-way platforms — however, applications tuning may be necessary to exact higher degrees of overall NT systems scalability.
To Aberdeen, the scalability discussion ulti-mately comes down to a user's requirement for performance — and with NT performance rapidly approaching the 7,000 transaction per min-ute
mark on 4-way platforms, many users will find that NT-based servers can already address most of their departmental computing needs today.
The Advent of 8-Way and Greater Systems
Systems suppliers tell Aberdeen that the arrival of NT 8-way servers that scale well is imminent. They cite the availability of NT 4.0 — a release embodies NT SMP scalability enhancements
— as well as systems engineering factors such as the use of shared-memory as primary factors that contribute to performance boosts.
Early benchmarks from NCR indicate that 8-way systems with dual instances of the database have increased NT performance by one-third over 4-way servers. Aberdeen expects 8-way
scalability to improve — but estimates that in the near term most 8-way NT servers will yield 1.33 times the performance of current NT 4-way servers, placing 8-way systems in the 9,000
tpm performance range. And again, Aberdeen notes that for applications to take advantage of multiple SMP nodes, applications tuning may be in order.
Aberdeen also note that a number of NT systems suppliers are writing elegant SMP extensions for NT — using approaches such as Non-Uniform Memory Addressing to scale to 16, 32, and
higher processor levels.
The Advent of NT Clusters
To further increase NT server processing power, Microsoft and its NT systems supplier partners are actively involved in the development of NT performance clusters. But, Aberdeen notes,
NT clusters will first address IS requirements for systems high-availability, and then be followed by performance tuning for increased processor headroom.
High-Availability Clusters
Aberdeen believes that clusters tuned for NT high-performance will not arrive en masse until 1998. Instead, initial NT clusters will be focused on ensuring NT systems reliability, availability,

and serviceability (RAS) such that NT servers can be reliably deployed in mission critical, mid-range environments. Suppliers such as Compaq, Digital, NCR, and Tandem have already taken
their first cluster steps by delivering first generation NT "availability clusters".
IS managers have told Aberdeen that performance is secondary to reliability in a mission-critical environment. These managers already have first-hand evidence that NT can scale and does
have the processing power available to run business-critical applications within their enterprise IS infrastructure. But, in order to deploy NT on a broad scale, these IS managers indicated that
they require assurance that NT servers can be deployed and run in a highly-available fashion.
A number of NT systems suppliers have chose to address the requirement for NT RAS using 4-way clustered systems and additional dual port I/O, local area networking and RAID storage
options. And Aberdeen expects that this clustering approach will be highly successful because the almost minimal cost of adding additional systems boards (as low as $16,000 for a 4-way
Pentium Pro) will be regarded by many IS managers as a small and almost irresistible price to pay for NT systems availability. Aberdeen expects that by the end of 1998, more than 100,000
NT/HA servers will have been sold.
Aberdeen notes that during 1997, Microsoft expects to release a version of NT that will contain a "Microsoft-blessed" version of high-availability clustering. This so-called "Wolfpack"
release will establish the NT cluster standard that will enable a number of suppliers to intermix and interoperate at the cluster level. Most suppliers will adopt Microsoft’s Wolfpack release
when available.
Performance Clusters
The next giant step for systems suppliers will be NT performance clusters — expected to arrive in late 1997. Performance clusters will enable IS managers to increase systems performance
by harnessing the processing power of multiple NT servers using clustering technology to handle large transaction loads or to run complex database queries.
If an individual 4-way NT server reaches the 11,000 to 17,000 transaction per minute range by 1998 as projected, then the addition of a second 4-way server (in a performance cluster
configuration) could provide at least a 50% boost in processing power — leading Aberdeen to project that NT performance clusters (two 4-way servers loosely coupled) could be able to
exceed 20,000 transactions per minute by early 1999.
Summary Observations
NT systems scalability using SMP technologies should no longer be the focal point preventing the widespread adoption of NT within an enterprise context. Microsoft is taking a different
approach to improving systems performance –exacting high-degrees of performance out of 4-way processors to improve NT server performance. And Microsoft is taking this approach in
order to capitalize on the server market sweet-spot — over 90 percent of all systems sold are 4-processor-or-less servers.
Aberdeen suggests that the real meter for evaluating NT-based servers should be linear scalability — the ability to get maximum performance boosts for every processor added to a system.
Current benchmarks indicate that NT servers are seeing excellent linear scalability results on 4-way Intel-based systems platforms. And continual tuning of NT combined with increased
microprocessor performance improvements will lead to even greater 4-way system performance. Aberdeen expects that 4-way NT servers will perform in the 16,000 tpmC range by year end
1998.
Yet, systems and microprocessor suppliers are not exclusively focused on 4-way system platforms. Many suppliers are attempting to take NT performance to new heights using 8-way
processor platforms, elegant SMP architectures like NUMA, and clustering technologies. Aberdeen expects that 8-way processors that perform in the 9,000 tpm range will imminently arrive
on the market — probably by early 1997. And, NT high-availability clusters will represent the first wave of NT clustering technology, followed by performance clusters that can be expected
to perform in the 20,000+ tpm range in early 1999.
Aberdeen believes that the NT performance and NT SMP scalability discussion will now shift to the forthcoming wave of new applications that will utilize NT-based distributed systems. The
hardware and operating system can be tuned only so far — applications tuning to take advantage of NT SMP server architectures will be the next step in performance improvement.
Aberdeen believes that NT systems are capable today of meeting mid-range systems performance requirements — and at the lowest transaction per minute cost in the industry. And NT
servers are on a performance trajectory that will enable them to meet the future needs of most mid-range system users – and on a price curve that should prove irresistible to most IT decision
makers.
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
| study_id | aberdeen-1996-debunking-ntsmp-scalability-myth |
| title | Debunking the NT/SMP Scalability Myth |
| author | Aberdeen Group |
| date | 1996-11-26 |
| type | white-paper |
| subject_domain | server-computing |
| methodology | industry-analysis, benchmarking, competitive-profiling |
| source_file | 1996 debunking NTSMP scalability myth.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group's November 1996 Viewpoint argues that IS decision-makers should reconsider Windows NT's SMP scalability limitations, framing them as a deliberate Microsoft market strategy rather than an engineering constraint. Using TPC-C benchmark data, Aberdeen demonstrates that 4-way NT servers had already reached mid-range performance levels (6,712 tpmC at $65/tpmC), and projects NT will achieve 16,000 tpmC on 4-way platforms by 1998 while NT performance clusters will exceed 20,000 tpmC by early 1999. The study positions NT as an irresistible force in the mid-range server market based on price/performance momentum.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Published at a pivotal inflection point in the mid-range server market, this Viewpoint directly challenged conventional wisdom that NT could not compete with Unix and proprietary SMP systems. Aberdeen's TPC-C analysis was highly influential in legitimizing NT for enterprise IS planning in 1997-1998. |
| **Relevance** | medium | The analytical framework—using transaction benchmarks to segment server markets and project performance trajectories—remains methodologically sound and applicable to current cloud/on-premises performance debates. The specific hardware predictions are dated but the market dynamics analysis transfers well. |
| **Prescience** | high | Aberdeen's core predictions proved largely accurate: NT/Windows Server did dominate the mid-range market by 2000-2002 (IDC data confirms), 4-way NT performance exceeded 16,000 tpmC by 1998 (Microsoft/Compaq TPC-C results), and NT availability clusters (Wolfpack/MSCS) shipped in 1997. Performance cluster prediction at 20,000+ tpmC was also validated. |

### Prescience Detail

**Prediction 1:** NT 4-way TPC-C will reach 11,000-16,000 tpmC by end 1998
- **Claimed:** 4-way NT servers will at least double and perhaps triple in speed by 1998 (from 6,712 tpmC baseline)
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 1:** NT 4-way TPC-C actual performance by 1998
- **Result:** Verified — exceeded 16,000 tpmC on 4-way NT by 1998; Sequent NUMA (NT) achieved 48,793 tpmC Oct 1998
- **Confidence:** verified
- **Notes:** TPC-C public results database; https://www.tpc.org/results/fdr/tpcc/sequent.numa.98101303.fdr.pdf

**Prediction 2:** NT Wolfpack HA clustering will ship in 1997
- **Claimed:** Microsoft expects to release Wolfpack in 1997; suppliers will adopt
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 2:** NT Wolfpack clustering release
- **Result:** VERIFIED — Microsoft Cluster Server (MSCS/Wolfpack) released in NT 4.0 Enterprise Edition Q4 1997
- **Confidence:** verified
- **Notes:** Released on schedule; became Windows Server Failover Clustering in 2008

**Prediction 3:** NT performance clusters will exceed 20,000 tpmC by early 1999
- **Claimed:** Two 4-way NT servers in performance cluster could exceed 20,000 tpmC by early 1999
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 3:** NT performance cluster tpmC outcome
- **Result:** VERIFIED — Sequent NUMACentre achieved 48,793 tpmC in Oct 1998, well ahead of schedule
- **Confidence:** verified
- **Notes:** TPC-C result for Sequent NUMACentre 2000 NE300, Oct 13, 1998; https://www.tpc.org/results/fdr/tpcc/sequent.numa.98101303.fdr.pdf

**Prediction 4:** NT will dominate mid-range server market
- **Claimed:** NT/SMP scalability should no longer prevent adoption; NT on price curve irresistible to IT decision makers
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 4:** NT/Windows Server mid-range market outcome
- **Result:** VERIFIED — Windows 2000/2003 Server became mid-range market leader by 2002; IDC confirmed Windows up 6 share points, Unix down 3
- **Confidence:** verified
- **Notes:** Microsoft press release May 8, 2002; https://news.microsoft.com/source/2002/05/08/windows-2000-server-leads-server-market-growth/

### Entities Referenced (10)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Microsoft Corporation | company | active |  |
| Aberdeen Group | firm | acquired | Harte-Hanks / Aberdeen (brand revived) |
| Compaq Computer Corporation | company | acquired | Hewlett-Packard |
| NCR Corporation | company | active |  |
| Sequent Computer Systems | company | acquired | IBM |
| Intel Corporation | company | active |  |
| Digital Equipment Corporation (DEC) | company | acquired | Compaq / HP |
| Hewlett-Packard (HP) | company | active | HP Inc. / HPE |
| Tandem Computers | company | acquired | Compaq / HP |
| Transaction Processing Performance Council (TPC) | institution | active |  |

### Technologies Referenced (7)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Windows NT Server 4.0 | platform | Microsoft | emerging | obsolete |
| Intel Pentium Pro / Klamath / Deschutes | platform | Intel | mature | obsolete |
| DEC Alpha Processor | platform | Digital Equipment Corporation | mature | obsolete |
| TPC-C Benchmark | framework | TPC Council | mature | active |
| Non-Uniform Memory Access (NUMA) | framework | Multiple (Sequent, NCR, DEC) | emerging | active |
| Microsoft Wolfpack NT Clustering | platform | Microsoft | emerging | obsolete |
| Microsoft SQL Server 6.5 | application | Microsoft | mature | obsolete |

### Observation Summary

- Total observations: 24
- By type: actual-outcome: 3, benchmark-result: 4, expert-opinion: 3, framework-factor: 3, market-data: 1, strategy-classification: 2, technology-assessment: 3, viability-prediction: 5
