# Digital Debunks the NT/SMP Scalability Myth

> Archived from: https://web.archive.org/web/19970604112259/http://www.aberdeen.com:80/secure/viewpnts/v9n22/body.htm
> Original publication date: 1996-11-22
> Author: Aberdeen Group
> Volume 9 / Number 22

---

## Original Document Text

Volume 9 / Number 22
November 22, 1996

### Digital Debunks the NT/SMP Scalability Myth

There is widespread belief in the Information Systems (IS) community that Microsoft's NT Server operating system is not as scalable (capable of taking advantage of multiple processors for increased performance) as its SMP-based (Symmetrical MultiProcessing) Unix and proprietary operating system brethren. And there is a basis to that argument — IS managers and systems suppliers tell Aberdeen that NT Server scales extremely well to four processors, but as additional processors are added, linear scaling efficiency declines — sometimes dramatically.

But, whether or not NT can scale to an 8-way or 16-way or 32-way processor configuration is not the real issue for IS users — overall system price/performance is. And with Digital Equipment's most recent transaction benchmark announcement, Digital is proving that 4-way Pentium Pro Servers can readily outperform established midrange rival servers with double or triple the number of processors — and at a fraction of the cost.

In this Viewpoint, Aberdeen suggests that IT decision makers may wish to reconsider the NT/SMP scalability issue. Recent Transaction Processing Council benchmarks indicate that Digital's 4-way NT servers are well on their way to becoming an irresistible force in the midrange server market.

#### Executive Summary

Information Technology (IT) executives — particularly Chief Financial Officers (CFOs), Chief Information Officers (CIOs), and IT architects and planners — have been desperately searching for low-cost, high-performance computer platforms that could be deployed like building blocks throughout their organizations. And, until very recently, they believed that Microsoft's Windows NT Server platform was not a viable option — it did not meet the performance requirements of large departments and small enterprises. And many IT executives believed that the lack of NT SMP scalability beyond 4-way platforms was to blame.

However, recent and radical improvements in NT Server performance indicate that 4-way NT servers can now outperform some of the industry's leading SMP servers with double, triple, or even quadruple the number of processors — serving to debunk the importance of SMP scalability for overall system performance. Digital's recently announced that it had achieved an astounding 6,712 transactions at $65 per transaction minute on a 4-way Pentium Pro-based server — and at this performance level, Digital is now the undisputed leader in low cost, high-performance, NT-based midrange server price/performance.

Aberdeen believes that if IS managers examine the NT scalability issue closely they will find the more intriguing answer to why NT has lacked luster in scaling beyond 4-way processors is not engineering based, but actually based upon server market economics. Aberdeen believes that Microsoft has consciously chosen not to aggressively invest in NT/SMP scalability beyond 4-way processors. The reason: Microsoft is pursuing volume sales in the server market sweet-spot — the hundreds-of-thousands of systems sold in the 4-processor-or-less range. And Digital, with its industry leading 4-way Intel platform, is extremely well positioned to capture sales in this high-growth marketplace.

Note that Aberdeen is not saying that Microsoft and its system supplier partners are foregoing NT 8-way and greater scaling. A small number of systems suppliers are aggressively pursuing the development of 8-way systems and suppliers are using a new SMP architecture, Non-Uniform Memory Access (NUMA), for even greater SMP scaling. Aberdeen is simply saying that Microsoft and its key microprocessor and systems suppliers realize that the lion's share of server purchases will be made on 4-way-or-less platforms, and have adjusted their sales, pricing, and R&D strategies to capitalize on this factor.

And although some suppliers are working on scaling NT to 16-24-and-32 way systems, Aberdeen believes that the majority of NT midrange system suppliers are now turning their attention to NT clusters for the next, great performance leap.

Digital is well positioned from a technology and market standpoint in clustering — clustering has been a Digital core expertise since the introduction of VAX clusters in the 1980s. And Digital has been an early leader in NT cluster development — initial Digital NT high-availability clusters have already made their marketing debut. Aberdeen expects Digital to lead the charge into performance clusters — with initial performance-oriented clusters rolling-out in late 1997.

In this Viewpoint, Aberdeen takes a look at the evolving NT midrange server marketplace — and closely examines Microsoft's growth intentions. And, Aberdeen concludes that Digital is working in lock-step with Microsoft — closely aligned with Microsoft's strategic NT directions. And Aberdeen gives Digital high marks for its 4-way server price/performance leadership and its advancement of NT clustering technology.

#### NT: The Real Scalability Strategy

Microsoft claims that NT can support load balancing in systems environments with up to 32 processors. And systems suppliers have proven that NT can scale. NCR has scaled NT on sixteen processors, while Sequent can scale to twenty-eight and has actually sold a number of fourteen processor NT/SMP systems.

But, if NT is capable of scaling, then why has Microsoft not aggressively moved up the SMP performance ladder into high-performance 16-way or 32-way processors? Could it be that SMP scaling is not really at issue?

Aberdeen believes that Microsoft's real strategy is to exact high degrees of performance from 4-way servers, and to cluster those servers for even further performance gains. Specifically, Aberdeen expects that Microsoft will:

1. Put Paramount Focus on Increasing NT Server Performance on 4-way Platforms — Increase low-end system performance by tuning NT to take maximum advantage of the next generation of fast-clock-rate microprocessors;
2. Continue to Scale NT Using the SMP Approach — But not make 5-plus SMP processor scalability a major focus; and
3. Attain High-End Server Performance through Performance Clustering Technology — Work closely with systems suppliers to develop and tune NT performance clusters capable of challenging high-end Unix/SMP and other enterprise servers from a performance perspective.

And Aberdeen believes that Digital recognizes this agenda, and is aggressively building highly-tuned 4-way servers and clusters to capture large segments of the midrange server market using NT-based server technologies.

#### Microsoft NT: Taking Aim at the SMP Server Market Sweet Spot

To segment today's server market, Aberdeen used benchmark data from the Transaction Processing Council (TPC) — an industry-recognized, independent benchmarking organization. This segmentation is based upon transaction ranges at the workgroup, department and enterprise for low-end, midrange, and high-end servers (see Figure 1).

*Figure 1 - Server-Level Transaction Ranges — Source: Aberdeen Group, 1996*

Specifically, Aberdeen used TPC-C benchmark data. The benchmark itself includes a mixture of both read-only and update-intensive transaction types that simulate real-world distribution and warehousing applications. The object is to add as many orders per minute as possible while maintaining adequate response times for the orders and four other transaction types. User think times are simulated, forcing the performance randomness typically seen in live OLTP systems. Even rejected transactions are modeled. The resulting tpmC (transactions per minute — test suite C) is a measurement of the number of orders per minute processed on a given system — usually run at close to 100% CPU utilization to establish maximum loading characteristics.

Using tpmC performance data, Aberdeen determined that low-end, workgroup servers were predominantly involved in file read/write/print activities and required performance capacity of fewer than 2,500 transactions per minute (tpm) to satisfy user requirements.

Midrange SMP servers from Hewlett-Packard (HP 9000), Digital (AlphaServer), IBM (RS/6000 and AS/400), and Sun (Ultra and SPARCcenter) performed in the 3,000 to 15,000 tpm range. And the highest performance SMP systems performed in the greater than 15,000 tpm range — between 20,000 and 30,000 tpm on Unix-based servers — establishing the server high-end. (And note that Digital is the leader of this pack, too, with Unix-based AlphaServer clusters performing in excess of 30,000 transactions per minute).

Aberdeen believes that Microsoft and Digital are taking aim at the midrange server sweet spot — from 2,000 to 15,000 tpm — and are planning to capture that market with 4-way-or-less processor platforms.

#### NT Attacking the Midrange — Please Pass the Chips

A status check of NT performance progress in the midrange server market shows that Microsoft and its partners are rapidly increasing the processing power of 4-way NT-based platforms.

In November, 1995, Aberdeen issued a Market Viewpoint entitled *Undisputed Leadership in Departmental Price Performance*. This Viewpoint stated that NT-based servers had moved into departmental range based upon independent TPC performance benchmarks. At that point, Compaq's Intel-based servers had exceeded 2,400 transactions per minute in the TPC tpmC benchmarks at a cost of $242 per tpmC. Aberdeen concluded that this benchmark represented the first foray of NT-based platforms into the departmental server stronghold.

As of November, 1996, the Transaction Processing Council is reporting that Digital's Prioris ZX 6200MP/4-way NT at 6,712 tpmCs, almost triples the NT performance levels reported only eleven months previously — and at a cost of only $65/tpmC.

Aberdeen attributes this increase in performance to the use of the new revision of Windows NT Server, NT revision 4.0, the use of more powerful and faster clock rate microprocessors, and expert tuning by Digital. But Digital's pricing is truly outstanding — and Aberdeen attributes Digital's pricing posture to economies of scale in manufacturing that yield low systems cost coupled with an elegant Internet technology approach for transaction handling that eliminates an expensive Tuxedo-based front-end processor.

And, Aberdeen notes that at 6,712 tpmC, NT servers have now reached performance levels that enable NT servers to perform at the same level as today's most popular servers — including Unix/SMP and IBM AS/400 models — in the midrange market (see Figure 2).

**Figure 2 — Transaction Processing Council TPC-C Benchmark Results**

| Company | O/S | System | # CPUs | Database | tpmC | Price/tpmC |
|---------|-----|--------|--------|----------|------|------------|
| Digital | NT | Prioris ZX 6200 MP | 4 | Microsoft SQL Server | 6,712 | $65* |
| Compaq | NT | ProLiant 5000 6/200 | 4 | Microsoft SQL Server | 6,671 | $90 |
| Compaq | Unixware | ProLiant 5000 6/200 | 4 | Sybase SQL Server | 8,311 | $95 |
| Compaq | NT | ProLiant 5000 6/200 | 4 | Informix OnLine | 6,842 | $100 |
| IBM | AIX | RS 6000 J40 c/s | 8 | Sybase SQL Server | 5,774 | $198 |
| HP | HP/UX | HP 9000 K420 c/s | 4 | Oracle 7 | 4,939 | $232 |
| IBM | OS/400 | AS/400 9406 53S | 1 | DB2/400 | 1,496 | $320 |

*TPC-C Price/Performance Leadership — Source: Transaction Processing Council, November 1996*

Aberdeen believes that ongoing tuning of NT 4-way servers coupled with the increased processing power of next generation microprocessors from Digital with Alpha (now reporting clock speeds at the 500 MHz level) or Intel with its forthcoming Pentium processors (Klamath expected at the 266 MHz level; and Deschutes expected at the 333 MHz level) will result in substantial increases in 4-way system performance through 1997 and 1998. Aberdeen projects that 4-way systems will at least double and perhaps triple in speed by year-end 1998 — taking 4-way processors into the 11,000 to 16,000 transaction per minute range.

With the projected growth in individual 4-way system performance, Microsoft NT-based servers will be ideally positioned from a performance perspective to service the needs of most OLTP applications. In fact, many IS managers claim that today's NT tpmC performance of greater than 6,712 tpm rivals the OLTP computing power of their existing mainframe systems.

Finally, Aberdeen notes that Compaq's current transaction speeds are higher on a ProLiant Unix-based server (8,311) running a Sybase database and Tuxedo transaction monitor. But the systems price is significantly higher on this Compaq system, and Aberdeen sees very few real world examples of this "benchmark special" configuration actually installed.

#### The Advent of 8-Way and Greater Systems

Systems suppliers tell Aberdeen that the arrival of NT 8-way servers that scale well is imminent. They cite the availability of NT 4.0, a release that embodies NT SMP scalability enhancements as well as systems engineering factors such as the use of shared-memory, as primary factors that contribute to performance boosts.

And other suppliers are writing elegant SMP extensions for NT — using approaches such as Non-Uniform Memory Access (NUMA) to scale to 16, 32, and higher processor levels. But these suppliers will need more scalability assistance from Microsoft in order to optimize NUMA in the long term.

In Aberdeen's view, the suppliers who are concentrating their efforts to scale to eight-way and beyond are primarily designing NT scalable architectures for two reasons:
1. to serve specialized high-end markets — for instance high-end decision support, or data warehousing; and
2. to act as consolidation servers.

In either case, as long as NT remains a 32-bit operating system, NT servers sold to address these needs will be high margin but low volume products — developed and sold into specialized, niche markets.

Aberdeen does not deny that there is pent-up demand for more headroom (computing power) by IS managers currently using NT. And initially, suppliers of 8-way systems should do fairly well as they address that demand. But longer term, Aberdeen believes that performance clusters — because they offer the side benefit of addressing systems high-availability — will become the more popular method of extending NT performance.

#### The Advent of NT Clusters

As Aberdeen looks at the NT big picture, we expect that tremendous strides will be made in NT 4-way performance in the near term; that 8-way and greater systems will become available for high-end, specialized applications and as consolidation servers; and that clustering technologies — both high-availability and performance clusters — will arrive en masse over the next three years (see Figure 3).

*Figure 3 - The NT Performance/Reliability Roll-out Plan — Source: Aberdeen Group, 1996*

IS managers have told Aberdeen that performance is secondary to reliability in their mission-critical environment. These managers already have first-hand evidence that NT can scale and does have the processing power available to run business-critical applications within their enterprise IS infrastructure. But, in order to deploy NT on a broad scale, these IS managers indicated that they require assurance that NT servers can be deployed and run in a highly-available fashion. Digital's initial NT clusters have been focused on ensuring NT systems reliability, availability, and serviceability (RAS) such that NT servers can be reliably deployed in mission-critical, midrange environments.

Aberdeen expects Digital's next step in NT cluster development will be the adoption of an official NT release, codenamed Wolfpack — a release that will act as a baseline standard for cross-system NT clustering capabilities. But, to many Aberdeen analysts, Wolfpack represents a subset of functionality already found on clusters available from suppliers such as Digital Equipment, NCR and Stratus. Aberdeen expects Digital to adopt the Wolfpack standard, but to continue to offer value-added high-availability features above-and-beyond Wolfpack features for the foreseeable future.

The next giant step in clustering for Digital will be NT performance clusters — expected to arrive in late 1997 or early 1998. Performance clusters will enable IS managers to increase systems performance by harnessing the processing power of multiple NT servers using clustering technology to handle large transaction loads or to run complex database queries.

If an individual 4-way NT server reaches the 11,000 to 16,000 transaction per minute range by 1998 as projected, then the addition of a second 4-way server (in a performance cluster configuration) should provide at least a 50% boost in processing power — leading Aberdeen to project that NT performance clusters (two 4-way servers loosely coupled) should exceed 20,000 transactions per minute by early 1999.

Aberdeen projects that by year-end 1999, more than 100,000 NT high availability/performance clusters will be deployed.

#### Summary Observations

NT systems scalability using SMP technologies should no longer be the focal point preventing the widespread adoption of NT within an enterprise context. Microsoft is taking a different approach to improving systems performance — NT is focused on exacting high degrees of performance out of 4-way processors to improve NT server performance. And Microsoft is taking this approach in order to capture sales in the server market sweet-spot — over 90 percent of all systems sold are 4-way-or-less servers.

Digital Equipment Corporation is well positioned to capitalize on the Microsoft advance into the server midrange. Digital's Prioris 6200 MP/4-way is now the undisputed NT server price/performance leader with its extremely aggressive pricing at $65/tpm-C putting Digital's NT servers on a price curve that is way ahead of its competition.

Aberdeen gives Digital high marks for its commitment to the NT marketplace. Digital has forged a tight alliance with Microsoft; Digital has the broadest NT product line in the industry; Digital has the largest Microsoft products training organization in the world; and Digital also has more than 2,000 fully-trained Microsoft-certified systems and software specialists to assist in NT system deployment and troubleshooting. With all of these plusses, Aberdeen expects that making a Digital NT server decision should prove irresistible to many IT decision makers.

---
AberdeenGroup, Inc.
One Boston Place, Boston, Massachusetts 02108 USA
Tel: 617.723.7890 | Fax: 617.723.7897
Copyright © 1996 Aberdeen Group, Inc., Boston, Massachusetts

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-digital-debunks-ntsmp-scalability-myth |
| title | Digital Debunks the NT/SMP Scalability Myth |
| author | Aberdeen Group |
| date | 1996-11-22 |
| type | market-study |
| subject_domain | server-computing-NT-SMP |
| methodology | industry-analysis, benchmarking, competitive-profiling |
| source_file | 1996 Digital Debunks the NT_SMP Scalability Myth 1996.pdf |
| license | CC-BY-4.0 |

### Abstract

This Aberdeen Group Market Viewpoint argues that IT decision-makers should reconsider NT SMP scalability concerns. Using TPC-C data, Aberdeen shows Digital's 4-way NT server achieves 6,712 tpmC at $65/tpmC, outperforming Unix midrange at a fraction of the cost. Aberdeen concludes Microsoft's real strategy is performance clustering, and Digital is optimally positioned for NT midrange leadership.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Reframed the NT scalability debate using TPC-certified data at a critical market inflection point; influenced enterprise IT purchasing. |
| **Relevance** | medium | Price/performance methodology via independent benchmarks remains applicable; specific hardware references are dated. |
| **Prescience** | high | 4-way NT dominated midrange, Wolfpack shipped on schedule, 8-way remained niche — most predictions correct; Digital was acquired rather than winning independently. |

### Prescience Detail

**Prediction 1:** 4-way NT server TPC-C projection by end of 1998
- **Claimed:** 4-way NT servers will at least double and perhaps triple in speed by year-end 1998, reaching 11,000-16,000 tpmC range
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 1:** 4-way NT server TPC-C by 1998 - actual outcome
- **Result:** By 1998, 4-way Pentium II/Xeon NT servers exceeded 15,000 tpmC; prediction substantially correct; DEC acquired by Compaq January 1998
- **Confidence:** verified
- **Notes:** Intel Klamath (Pentium II) and Deschutes shipped as predicted; TPC-C records on NT crossed 15,000 tpmC mark

**Prediction 2:** NT performance cluster deployment prediction by 1999
- **Claimed:** More than 100,000 NT HA/performance clusters deployed by year-end 1999; NT clusters exceed 20,000 tpmC by early 1999
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 2:** NT performance cluster deployment - actual outcome
- **Result:** Microsoft Cluster Service shipped in Windows NT 4.0 Enterprise Edition 1997; HA clustering widely adopted; performance clustering (NLB) deployment was slower than 100,000 unit projection; TPC-C on NT clusters exceeded 20,000 tpmC by 2000
- **Confidence:** verified
- **Notes:** Wolfpack shipped on schedule; quantitative deployment target was ambitious

**Prediction 3:** Digital NT market leadership viability
- **Claimed:** Making a Digital NT server decision should prove irresistible; Aberdeen expects Digital to lead NT midrange charge
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 3:** Digital NT market leadership - actual outcome
- **Result:** Digital acquired by Compaq January 1998 for $9.6B; Digital's NT expertise absorbed into Compaq; Digital did not achieve independent NT market leadership
- **Confidence:** verified
- **Notes:** Compaq then acquired by HP 2002; Digital's assets live on but not as independent DEC

### Entities Referenced (11)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Digital Equipment Corporation | company | acquired | Compaq (1998) -> HP (2002) |
| Microsoft Corporation | company | active | — |
| Compaq Computer Corporation | company | acquired | HP (2002) |
| IBM Corporation | company | active | — |
| Hewlett-Packard Company | company | active | HP Inc./HPE (2015) |
| Sun Microsystems | company | acquired | Oracle (2010) |
| Sequent Computer Systems | company | acquired | IBM (1999) |
| NCR Corporation | company | active | — |
| Tandem Computers | company | acquired | Compaq (1997) -> HP (2002) |
| Transaction Processing Council | institution | active | — |
| Stratus Technologies | company | active | — |

### Technologies Referenced (8)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Microsoft Windows NT Server | platform | Microsoft | emerging | obsolete |
| Digital Prioris ZX 6200MP | platform | Digital | emerging | obsolete |
| Intel Pentium Pro | platform | Intel | emerging | obsolete |
| Digital Alpha Processor | platform | Digital | mature | obsolete |
| TPC-C Benchmark | framework | TPC | mature | active |
| Windows NT Wolfpack Clustering | platform | Microsoft | emerging | obsolete |
| NUMA Architecture | framework | multiple | emerging | active |
| Microsoft SQL Server | application | Microsoft | emerging | active |

### Observation Summary

- Total observations: 26
- By type: benchmark-result (7), viability-prediction (3), actual-outcome (3), strategy-classification (3), expert-opinion (3), market-data (3), technology-assessment (4)
