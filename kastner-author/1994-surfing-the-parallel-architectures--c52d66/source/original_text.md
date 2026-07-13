# Surfing the Parallel Architectures

> Archived from: TDMCOLOR.pptx
> Original publication date: 1994-09-27
> Author: Peter S. Kastner

---

## Original Document Text

# TDMCOLOR

*Source: TDMCOLOR.pptx — 41 slides*

## Slide 1: Surfing the Parallel Architectures

Surfing the Parallel Architectures
A Presentation to Tandem Computers’Board of Directors andIndustry Advisory PanelSeptember 27, 1994
Peter S. KastnerVice PresidentAberdeen Group, Inc.One Boston PlaceBoston, Mass. 02108(617) 723-7890

## Slide 2: Agenda

Agenda
Why Parallel?
Review of Parallel Architectures
Review of Parallel Software
Parallelism in Applications
Supplier Approaches to Parallelism
Aberdeen's Viewpoint on Tandem in a Parallel World

## Slide 3: Why Parallel Processing?

Why Parallel Processing?
Technology is an enabler
  - Parallel hardware is widely available, inexpensive
  - Parallel software (i.e., RDBMS)
  - $2M per terabyte disk storage
  - Scalability beyond traditional (mainframe) architectures ...
Demand is price elastic, business driven
  - Replace people with technology
  - Time really is money
  - “I can answer questions we never could before.”
  - "I'm running out of night!"
  - "I'm looking for a sustainable competitive advantage with IT."

## Slide 4: Very Quick Review of Parallel Architectures

Very Quick Review of Parallel Architectures
Uniprocessor
Symmetric Multiprocessor (SMP)
Cluster (Loosely-coupled)
Massively Parallel (MPP/SPP)

## Slide 5: Estimated Market Share by Architecture

Estimated Market Share by Architecture
Uniprocessor has the largest share but the lowest profits
Tandem’s architectures:Enterprise Computing

## Slide 6: Uniprocessor

Uniprocessor
Examples: Compaq PC servers, IBM RS/6000's to date, Integrity NR entry, each Himalaya node
No hardware parallelism
Useful as a software parallelism platform
Easy to design, manufacture, low selling price
Potential entry point for SMP
Benefits from 75% CAGR in processor/system performance
Problems: No scalability except to upgrade CPU.
Software
Hardware
OperatingSystemTask1
Task2Task3...

## Slide 7: Symmetric Multiprocessors

Symmetric Multiprocessors
Examples: Tandem Integrity NR, HP 9000, IBM ES/9000, many more
Multiple CPUs share common data highway (bus), memory and operating system
Well understood technology.  New chip set accelerators. Inexpensive engineering.
Scalability: Good to 4 processors; fair to 8; few do more than 10
Software
Hardware
OperatingSystemTask1
Task2Task3Task4Task n ...
Memory access isa big problemgetting worse
Memory & I/O
Processors

## Slide 8: Clusters

Clusters
Examples: Tandem Himalaya, Digital VAXcluster, IBM SP2 & ES/9000 Sysplex
Each node can be a uniprocessor or SMP
Multiple, independent computing nodes cooperate via messages
Most common use is for high availability; second is resource sharing
Issue: Message-passing resource expense
Message Bus
Node 1
Node 2
Node 4
OSTasks...

## Slide 9: Cluster Reality

Cluster Reality
Problems lie in software
  - Messaging between nodes is a very complex technology. Requires time to mature.  Example: Tandem's 20 years of experience.
  - Today's system software and customer applications are not cluster-enabled.  Require re-engineering to work in a cluster and may not scale well unless carefully architected
    - Example: Oracle Parallel Server, IBM ES/9000 Sysplex
Trend
  - Distributed operating systems will evolve from a cluster technology base

## Slide 10: Massively Parallel (MPP or SPP)

Massively Parallel (MPP or SPP)
Examples: nCube, Kendall Square, large Tandem Himalaya, large IBM SP2, Teradata, AT&T 3600
No industry-accepted definition.  Aberdeen says any system with more than 100 nodes is massive.
“Shared nothing” is required.
Differentiators
  - Merchant vs. custom micro-processor
  - Standard (e.g., Unix) vs. proprietary architecture
  - Interconnect technology

## Slide 11: MPP Markets

MPP Markets
Used today by bleeding-edge adopters in highly competitive markets
  - Dow Jones text retrieval (Thinking Machines)
  - Prudential Securities (derivatives)
  - American Express (mailing lists)
  - Retail industry (Teradata for data warehousing)
Market is most likely to evolve with existing large-computer suppliers rather than MPP new-starts
  - Scale up from clusters: Tandem, IBM SP2, AT&T 3600
  - Possible exception: MPP as pure database platform (not a  general purpose computer) -- for example, Teradata

## Slide 12: MPP Reality

MPP Reality
Problems
  - Scalability in the real world
  - Systems management software is lacking
  - Writing parallel commercial applications without tools
  - Lack of support by small MPP companies
Aberdeen conclusion is that MPP will remain a side show to the SMP and cluster markets, but that MPP buyers will come from the attractive World-1000 base

## Slide 13: Hardware Supplier Approaches to Parallelism

Hardware Supplier Approaches to Parallelism
IBM ES/9000, PTS, SP2
Hewlett-Packard
Digital Equipment
Unisys
Compaq
AT&T Global Information Solutions
Others

## Slide 14: IBM

IBM
Mainframe markets are driven by largest customers.  Sysplex clusters will only appeal to existing customers, lack overall price-performance value.
Parallel Query and Transaction mainframe products are a premature product reaction to market share losses to non-mainframe competition (i.e., Tandem, HP).  IBM microprocessors are too slow, software too limited, prices too high to be effective before 1997.
SP2 cluster/SPP is all talk, no commercial product.  Awaits parallel database software, tools, applications.  Shows great promise in markets Tandem seeks.
DB2 has four different variations under common product name.  Technology is not competitive but is getting better.
Strategically, IBM cannot concede the parallel market.  Will they be the Russian army or the mouse that roared?  Mostly hot air for next two years.

## Slide 15: Hewlett-Packard

Hewlett-Packard
Mediocre in SMP due to focus on ultra-fast RISC microprocessors.  "Fewer is better" approach.
Has next-century microprocessor deal in place with Intel
Surprisingly weak in clusters, even for high availability
Appreciates distributed systems management
Expect better clusters and marketing heat by mid-1995
HP MPP vague, driven by customers, expected in 1997 or later.  Ignore Convex.

## Slide 16: Digital Equipment

Digital Equipment
Good job on low-end SMP.  Fair scalability on high end.
VAXclusters the original shared-resource facility.  Slowly migrates to Alpha.
Encore reflected memory technology under-appreciated
New focus on alternate distribution/box volume mentality will likely hurt high end R&D efforts
Aberdeen is negative on Digital’s long term prospects

## Slide 17: Unisys

Unisys
Focus is on maintaining Burroughs and Sperry installed bases
Adequate clustered OLTP today
Recent MPP plans lack credibility, investment
Unix is not strategic to Unisys, so Intel/SMP will progress with market
Conclusion:  Unisys will be a minor competitor, and a potential roll-over sale target for Tandem

## Slide 18: Compaq

Compaq
Climbing up the enterprise food-chain from desktop/workgroup base
Next year's Intel P6-based 4/8-way SMP will beat IBM mainframe ES/9000s in OLTP with RDBMS
"Good enough" for many OLTP & moderate DSS applications
The horse that Microsoft’s NT operating system will ride

## Slide 19: AT&T Global Information Solutions

AT&T Global Information Solutions
#2 Unix server player with Intel-based line
Owns the Teradata base of 400 large sites
SMPs and 3600 cluster that grows to MPP
Best company-wide at understanding complex DSS issues and experience
Retail and banking powerhouse.  Weak elsewhere.
Often the bridesmaid.  Will they ever get on track?

## Slide 20: Other Hardware Suppliers

Other Hardware Suppliers
SMP specialists Sequent and Pyramid
ICL Goldrush query parallelization OS features
nCube's fate rests with Oracle push
Cray Research invades Wall Street with ex-Tandem sales rep
Kendall Square Research is dead

## Slide 21: Review of Parallel Software

Review of Parallel Software
SAP says "I need 300 SQL statements/second today, 3,000 per second in two years."
Relational databases are the most important commercial technology
Operating systems become more parallel to evolve to distributed computing/object world of 1998
Applications evolve towards distributed computing with partitioning and objects

## Slide 22: Relational Databases (RDBMS)

Relational Databases (RDBMS)
New software versions unleash the power of parallel hardware
Complex decision support is the killer application
Major  suppliers are participating
  - Oracle
  - Sybase
  - Informix
  - IBM DB2

## Slide 23: Independent Software Supplier Parallel Strategies

Independent Software Supplier Parallel Strategies
Trend: Aberdeen sees a 3x-5x increase in information demand by the late 1990s.  Complex DSS is the next major hurdle for commercial computing.
Oracle: “Beat IBM mainframes.  Protect Ellison's nCube investment.”  Technology is behind.
Sybase: talks enterprise, does departmental.  Navigation Server an embarrassment.
Informix: Bets the ranch on parallel RDBMS.  Technology good but company lacks board-room visibility.

## Slide 24: Aberdeen's Viewpoint on Tandem in a Parallel World

Aberdeen's Viewpoint on Tandem in a Parallel World
Architecture
Technology
Markets

## Slide 25: Architecture

Architecture
Tandem ought to be a leader in distributed, object-based computing
Tandem understands parallel issues in depth, with experience
Market is recognizing that clustering (loose-coupling) is required for high-end applications
Objects communicate via messages.  Tandem does this better than others.  The late 1990s will be dominated by object-oriented software issues.

## Slide 26: Technology

Technology
Himalaya is at the enterprise-server market sweet-spot
Integrity NR/FT cover mass-markets for commercial servers.  High availability story great.
“Open” Tandem will require by 1996 a better DCE and distributed-object technology roadmap.
SGI/MIPS microprocessor faces enormous competition from Intel.  Be prepared to switch.

## Slide 27: Markets

Markets
Parallel computing profits are being made now in competitive-advantage markets (i.e., retail, telecomm, transportation, finance) where Tandem is already focused
Tandem momentum has changed for the positive.  Company has a wonderful opportunity to re-establish itself in existing markets for new applications
Best near-term, cross-market opportunity is data warehousing (complex decision support).  Tandem has the right-stuff technology, but needs partners in teaching buyers how to maximize their warehouse investments.
Dual product strategy (Integrity & Himalaya) makes sense, recognizes that one-size-fits-all approach is unrealistic.

## Slide 28: Backup Information

Backup Information
The following material supplements the main presentation
See also Aberdeen Group Viewpoints on Tandem, Digital Equipment, Parallel-Scalable Databases

## Slide 29: SMP (cont'd)

SMP (cont'd)
Most system software (e.g., RDBMS) today can harness SMP automatically
Excellent for distributed OLTP nodes, departmental decision support
Problems: Bus bottlenecks, cache coherency, memory bandwidth sap performance & growth
Implementations
  - Poor: IBM AS/400
  - Medium (80% scalability): Hewlett-Packard, IBM ES/9000
  - Good (90%+ scalability): Sequent to 20 processors, SGI/Tandem

## Slide 30: Clusters (cont'd)

Clusters (cont'd)
Excellent for high availability failover, shared-nothing growth, resource sharing
System software must be messaging-enabled to participate
  - Very uncommon today to find cluster-ready software
  - But distributed computing trend benefits cluster suppliers
  - Next 3 years will see explosion of messaging-aware systems software:
    - Informix Dynamic Scalable Architecture 8.0 RDBMS
    - Sybase Navigation Server
    - Common Object Request Broker Architecture (CORBA)
    - Distributed Computing Environment (DCE)

## Slide 31: Informix

Informix
Sub-process (threads) specialized tasks
Both function and data parallelism
Cluster and MPP versions in late 1995
Closest architecture to Tandem with NonStop SQL
Architecturally superior to competition

## Slide 32: Oracle

Oracle
Parallel Server has VAXcluster roots, severe limitations in OLTP
Parallel Query Option uses Unix process pool vs. Informix threads
160 processor nCube MPP is slower than 20 processor Sequent SMP
No data partitioning.  Poor use of indexes (Mervyn's).

## Slide 33: Sybase Navigation Server

Sybase Navigation Server
Announced September 1994 for NCR/AT&T 3600 (cluster).  Available 12/94.
How it works
  - TP-monitor-like Control server manages execution plan
  - Parallel optimizer generates plan or invokes compiled procedure
  - Multiple SQL Server instances execute independently on their own data partition
  - Data is partitioned by Range, Hash Key, or schema
Problems
  - First version for DSS, not OLTP
  - NCR 3600 lock-in?
  - Not integrated with System 10 servers (i.e., Replication, Backup)

## Slide 34: IBM

IBM
ES/9000 Sysplex: a slowly unfolding cluster strategy aimed at IBM's largest mainframe customers
Transactions (PTS): IMS clustered on 13 MIPS CMOS-based cluster.  DB2 in 1996.  Too pricey?
Query (PQS): Query-only DB2 on CMOS-based cluster.  Low availability.  ES/9000 required.
Massive (SP2): viable commercial cluster/MPP lacks RDBMS, tools.  IBM locks up the market now in evaluations.  Decent products & partners in late 1995 and 1996.

## Slide 35: IBM DB2

IBM DB2
Parallel query I/O in MVS, HQS, and DB2 6000 for SP2
Version 3 adds basics like stored procedures, triggers.  Still functionally weak, but getting better slowly.
SP2 cluster version of DB2/6000
  - Still in early alpha according to customers
  - Realistically, a 1996 mainstream product
DB2/6000
  - Common code base with OS/2
  - Presently works on uniprocessor hardware, moving to SMP
  - Considered not competitive with independent RDBMSs
  - IBM bids DB2/6000 against RDBMS partners, spoiling relationships

## Slide 36: Other  Database Software

Other  Database Software
Red Brick Software: RDBMS for decision support.  Adding parallelism for SMPs.
IRI Software:  Express multidimensional database provides Rubic Cube approach to aggregating data, instead of brute (parallel) force of merchant RDBMSs.
Prism, et al:  Large DSS systems will need loading/preparation utility products

## Slide 37: Parallel Operating System Issues

Parallel Operating System Issues
SMP: How many processes can an OS juggle efficiently?
Distributed OS near-future technology will change product requirements dramatically
  - Distributed computing via DCE
  - Distributed objects will turn the network into a big cluster
Implication: Tandem already has the loosely coupled/distributed/parallel experience required to lead in this technology migration

## Slide 38: Data Warehouse Specialists

Data Warehouse Specialists
Red Brick: an RDBMS optimized for complex DSS
IRI Software: multidimensional front-end to RDBMS and legacy data
Prism, etc. -- specialists in getting data in and out of the warehouse

## Slide 39: Parallelism in Applications

Parallelism in Applications
High availability: requires a cluster
Online Transaction Processing (OLTP): spread many short tasks over many CPUs
Messaging applications: electronic mail, workflow, store-forward = Comm + transactional I/O
Simple decision support systems (DSS): does not benefit appreciably from parallelism

## Slide 40: Parallelism in Applications

Parallelism in Applications
Online Analytic Processing (OLAP)/complex DSS
  - Ad hoc decision support by knowledge workers
  - Management by exception approach to work
  - Unknown number of queries -- the "quest"
  - Fast response time a plus.  Parallelism can help.
Market Basket DSS
  - Large database scans benefit from many kinds of parallelism
  - Find product, customer affinities.  Huge ROI for customers.
  - Example: large greeting card company
  - An obvious market target for Tandem

## Slide 41: Parallelism in Applications

Parallelism in Applications
Transaction managers have long parallelized available resources (i.e., IBM CICS, Tandem Pathway and TMF)
Next client-server phase requires application process partitioning (a form of parallelism)
Big Caveat: Programmers should NOT have to worry about parallelizing their code.  Scientific parallel market languished due to lack of  automatic parallelization.


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | 1994-surfing-the-parallel-architectures--c52d66 |
| title | Surfing the Parallel Architectures |
| author | Peter S. Kastner |
| date | 1994-09-27 |
| type | market-study |
| subject_domain | parallel-computing |
| methodology | industry-analysis, competitive-profiling, expert-opinion |
| source_file | TDMCOLOR.pptx |
| license | CC-BY-4.0 |

### Abstract

This board-level presentation surveys the 1994 commercial parallel-computing market across uniprocessors, SMP systems, clusters, and massively parallel machines, then compares the leading hardware and database suppliers against Tandem's position. Kastner argues that software-enabled clustering and parallel databases will matter more than pure MPP experimentation, and he frames data warehousing plus distributed object computing as Tandem's best near-term strategic opening. The deck combines architecture taxonomy, vendor-by-vendor competitive critique, and explicit forward-looking judgments about how the market would evolve.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | This is a candid board-level competitive assessment delivered directly to Tandem's directors and advisory panel at a major architectural inflection point. It captures how a top industry analyst framed the full SMP-cluster-MPP transition, vendor threats, and Tandem's strategic choices in real time. |
| **Relevance** | high | The presentation remains a valuable primary source on mid-1990s enterprise computing because it links architecture, database software, and go-to-market strategy in one compact narrative. It is especially useful for understanding how practitioners evaluated clusters, MPP, data warehousing, and commodity Intel systems before those markets fully sorted out. |
| **Prescience** | high | Many of the deck's core directional calls were strong: it favored clusters and software maturity over general-purpose MPP hype, highlighted the coming importance of distributed-object and messaging software, and anticipated the rise of commodity Intel-based scale-up systems. Not every timing call was exact, but the overall strategic read of the market proved notably prescient. |

### Prescience Detail


**Prediction 1:** distributed-os-evolves-from-clusters
- **Claimed:** Distributed operating systems will evolve from a cluster technology base.
- **Year:** 1998
- **Confidence at time:** high

**Actual Outcome 1:** distributed-os-evolves-from-clusters
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Placeholder for later verification of the prediction.

**Prediction 2:** mpp-remains-sideshow
- **Claimed:** MPP will remain a side show to the SMP and cluster markets.
- **Year:** 1997
- **Confidence at time:** high

**Actual Outcome 2:** mpp-remains-sideshow
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Placeholder for later verification of the prediction.

**Prediction 3:** ibm-parallel-push-not-effective-before-1997
- **Claimed:** IBM's microprocessors, software, and pricing will leave its parallel push ineffective before 1997.
- **Year:** 1997
- **Confidence at time:** high

**Actual Outcome 3:** ibm-parallel-push-not-effective-before-1997
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Placeholder for later verification of the prediction.

**Prediction 4:** hp-better-clusters-by-mid-1995
- **Claimed:** HP should show better clusters and stronger market messaging by mid-1995.
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 4:** distributed-os-evolves-from-clusters
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Placeholder for later verification of the prediction.

**Prediction 5:** digital-long-term-prospects-negative
- **Claimed:** Digital's shift toward alternate distribution and box-volume economics will likely damage high-end R&D and hurt long-term prospects.
- **Year:** 1997
- **Confidence at time:** medium

**Actual Outcome 5:** digital-long-term-prospects-negative
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Placeholder for later verification of the prediction.

**Prediction 6:** unisys-minor-competitor
- **Claimed:** Unisys will remain a minor competitor and a possible roll-over sale target for Tandem.
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 6:** unisys-minor-competitor
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Placeholder for later verification of the prediction.

**Prediction 7:** compaq-p6-smp-beats-es9000-oltp
- **Claimed:** Intel P6-based 4/8-way Compaq SMP systems will beat IBM ES/9000 mainframes in OLTP with RDBMS workloads.
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 7:** compaq-p6-smp-beats-es9000-oltp
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Placeholder for later verification of the prediction.

**Prediction 8:** information-demand-3x-to-5x
- **Claimed:** Aberdeen expects information demand to rise threefold to fivefold by the late 1990s, making complex DSS the next major commercial hurdle.
- **Year:** 1998
- **Confidence at time:** medium

**Actual Outcome 8:** information-demand-3x-to-5x
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Placeholder for later verification of the prediction.

**Prediction 9:** object-oriented-software-dominates-late-1990s
- **Claimed:** The late 1990s will be dominated by object-oriented software issues.
- **Year:** 1998
- **Confidence at time:** medium

**Actual Outcome 9:** object-oriented-software-dominates-late-1990s
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Placeholder for later verification of the prediction.

**Prediction 10:** tandem-needs-better-dce-roadmap-by-1996
- **Claimed:** Open Tandem will need a stronger DCE and distributed-object technology roadmap by 1996.
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 10:** tandem-needs-better-dce-roadmap-by-1996
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Placeholder for later verification of the prediction.

**Prediction 11:** messaging-aware-software-explodes-by-1997
- **Claimed:** The next three years will bring an explosion of messaging-aware systems software, including Informix DSA, Sybase Navigation Server, CORBA, and DCE.
- **Year:** 1997
- **Confidence at time:** medium

**Actual Outcome 11:** tandem-needs-better-dce-roadmap-by-1996
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Placeholder for later verification of the prediction.

**Prediction 12:** db2-6000-mainstream-1996
- **Claimed:** The cluster version of DB2/6000 is realistically a mainstream 1996 product, not a 1994-ready one.
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 12:** ibm-parallel-push-not-effective-before-1997
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Placeholder for later verification of the prediction.


### Entities Referenced (27)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | [DEFERRED] | [DEFERRED] |
| Tandem Computers Incorporated | company | [DEFERRED] | [DEFERRED] |
| IBM Corporation | company | [DEFERRED] | [DEFERRED] |
| Hewlett-Packard Company | company | [DEFERRED] | [DEFERRED] |
| Digital Equipment Corporation | company | [DEFERRED] | [DEFERRED] |
| Unisys Corporation | company | [DEFERRED] | [DEFERRED] |
| Compaq Computer Corporation | company | [DEFERRED] | [DEFERRED] |
| AT&T Global Information Solutions | company | [DEFERRED] | [DEFERRED] |
| Sequent Computer Systems Inc. | company | [DEFERRED] | [DEFERRED] |
| Pyramid Technology Corporation | company | [DEFERRED] | [DEFERRED] |
| Oracle Corporation | company | [DEFERRED] | [DEFERRED] |
| Sybase Inc. | company | [DEFERRED] | [DEFERRED] |
| Informix Software Inc. | company | [DEFERRED] | [DEFERRED] |
| Microsoft Corporation | company | [DEFERRED] | [DEFERRED] |
| Intel Corporation | company | [DEFERRED] | [DEFERRED] |
| nCUBE Corporation | company | [DEFERRED] | [DEFERRED] |
| Teradata Corporation | company | [DEFERRED] | [DEFERRED] |
| Kendall Square Research | company | defunct | [DEFERRED] |
| Red Brick Systems | company | [DEFERRED] | [DEFERRED] |
| IRI Software | company | [DEFERRED] | [DEFERRED] |
| Prism Solutions | company | [DEFERRED] | [DEFERRED] |
| SAP AG | company | [DEFERRED] | [DEFERRED] |
| Silicon Graphics | company | [DEFERRED] | [DEFERRED] |
| Thinking Machines Corporation | company | [DEFERRED] | [DEFERRED] |
| Cray Research, Inc. | company | [DEFERRED] | [DEFERRED] |
| ICL | company | [DEFERRED] | [DEFERRED] |
| Convex Computer | company | [DEFERRED] | [DEFERRED] |

### Technologies Referenced (25)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Symmetric Multiprocessing (SMP) | platform | (multi) | mature | [DEFERRED] |
| Cluster architecture (loosely-coupled) | platform | (multi) | mature | [DEFERRED] |
| Massively Parallel Processing (MPP) | platform | (multi) | emerging | [DEFERRED] |
| IBM ES/9000 | platform | ibm-corporation | mature | [DEFERRED] |
| HP 9000 | platform | hewlett-packard | mature | [DEFERRED] |
| Online Transaction Processing | application | (multi) | mature | [DEFERRED] |
| Intel Pentium Pro (P6) | platform | intel-corporation | prelaunch | [DEFERRED] |
| Teradata (data warehouse) | application | teradata | mature | [DEFERRED] |
| Relational Database Management System | application | (multi) | mature | [DEFERRED] |
| Oracle RDBMS (Oracle7) | application | oracle-corporation | mature | [DEFERRED] |
| Sybase Navigation Server | application | sybase | announced | [DEFERRED] |
| Informix Dynamic Scalable Architecture (DSA) | application | informix-software | emerging | [DEFERRED] |
| Tandem Himalaya | platform | tandem-computers | growing | [DEFERRED] |
| Tandem Integrity NR/FT | platform | tandem-computers | mature | [DEFERRED] |
| Distributed Computing Environment (DCE) | framework | (standard) | emerging | [DEFERRED] |
| Common Object Request Broker Architecture (CORBA) | protocol | (standard) | emerging | [DEFERRED] |
| Oracle Parallel Server | application | oracle-corporation | emerging | [DEFERRED] |
| IBM DB2/6000 | application | ibm-corporation | emerging | [DEFERRED] |
| IBM DB2 | application | ibm-corporation | mature | [DEFERRED] |
| Online Analytical Processing (OLAP) | application | (multi) | emerging | [DEFERRED] |
| Data warehousing | application | (multi) | emerging | [DEFERRED] |
| AT&T 3600 cluster platform | platform | att-gis | emerging | [DEFERRED] |
| Red Brick RDBMS (DSS-optimized) | application | red-brick-systems | emerging | [DEFERRED] |
| IRI Express multidimensional database | application | iri-software | emerging | [DEFERRED] |
| Tandem NonStop SQL | application | tandem-computers | mature | [DEFERRED] |

### Observation Summary

- Total observations: 49
- By type: viability-prediction: 12, actual-outcome: 12, competitive-assessment: 10, technology-assessment: 8, market-data: 3, expert-opinion: 3, strategy-classification: 1
