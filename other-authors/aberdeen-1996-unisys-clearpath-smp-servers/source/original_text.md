# Unisys Corporation - ClearPath SMP Servers

> Archived from: https://web.archive.org/web/19970112011850/http://www.aberdeen.com:80/secure/profiles/unisys_2/unisys2.htm
> Original publication date: 1996-04-01
> Author: Aberdeen Group

---

## Original Document Text

**Unisys Corporation - ClearPath SMP Servers**
2700 North First Street
San Jose, CA 95134
(408) 434-2848

### Preface

To understand Unisys role in today's computing environment, it is necessary to understand how far the pendulum has swung back to the days when full service suppliers were in vogue. When it comes to open systems, MIS Executives are faced with a good-news, bad-news conundrum. On the one hand, the move to openness over the past decade has increasingly given MIS the opportunity to choose best-of-breed components from which to build the best hardware, software and network systems.

However, confronted with having to know all about hundreds of components — including which are integrated with the others — MIS has been overwhelmed with the effort of keeping up. In effect, the move away from proprietary systems to open systems has shifted the onus for making sure every component in a system works well and works together from the suppliers to the users.

For an enterprise, there are myriad component groupings which impact the operation of all the computing tiers:

- System hardware: desktop, mid-tier servers and back-end systems
- Operating systems: desktop, mid-tier servers and back-end systems
- Networks: protocols, devices, network operating systems — internal and external links to/from customers and mobile users
- Relational Databases
- Application development tools
- System and Network management platforms and tools

Layered on top of all of this, especially as applications move from the category of "nice to have" to "must have," is the old data center standard — RAS, or Reliability, Availability and Security.

This Profile describes how Unisys has managed to find the balance between meeting the users' need for openness and while still providing "one-stop" services.

### Market Position

In late 1995, Unisys reorganized itself into three separate business groups: the Global Customer Service Group; the Information Service Group; and the Computer Systems Group. The latter includes the Enterprise Server Division, which in turn is responsible for the ClearPath SMP Servers and ClearPath Enterprise Servers — follow-ons to Unisys A Series and 2200 mainframes. This unit has responsibility for taking technology and turning it into product — operational applications, workgroup computing and decision support on SMP servers — for sale to Unisys customers using direct sales, VARs and distributors.

Since Aberdeen's initial Profile of this group in October 1994, the mission has grown and matured — moving from being systems-centric to solution-centric over that time. Unisys is able to deliver these solutions because of its tight working relationships with other suppliers — such as Intel, as shown in Figure 1 below — and with Unisys in-house systems integrator, Information Services Group.

**Figure 1: Unisys/Intel Cooperation**
*(Source: Unisys, April 1996)*

### Server Products

#### Entry-Level Servers

Early in 1996, Unisys will be rolling out a complete update of its Intel-based servers, driving down price and increasing performance at all levels. In April, Unisys will ship the SMP5200 workgroup-platform with one or two 100MHz or 133MHz processors, and the SMP5400 departmental-platform with up to four 100, 133 or 166 MHz processors. In the second-half of the year, the optionally rackmounted SMP6400 — with 166 or 200MHz Pentium Pro processors — will join the product line-up.

In addition to the new server lineup, Unisys will begin the change from its current SVR4MP-based Unix operating system to the UnixWare 2.1 being provided by the SCO led consortium.

Even though the SMP5200 is targeted at the workgroup, it can be configured with large amounts of memory (256MB) and disk (24GB in-cabinet) necessary for today's resource-hungry applications.

The SMP5400 and SMP6400 have a dual PCI bus architecture which provides for very high-speed I/O, have large memory and internal RAID (0, 1, 5) support and excellent high-availability features — all attributes of good application servers in both stand-alone and networked environments. Both will be able to use the latest Pentium (P5) and Pentium Pro (P6) processors.

**Table 1 - SMP System Features**
*(Source: Aberdeen Group, April 1996)*

#### Mid-to-Large Range Servers

The new SMP product line are replacements for the entry level U6000/ family, and can all use U6000 peripherals and are U6000 software compatible. The new SMP product line can either replace an existing U6000, or be added onto an existing network of U6000s without extra effort.

The SMP61000 being released will replace the current U6000/550 and /580, but again, it is not just a simple refresh of the series but a significant technology upgrade for the product.

The SMP61000 introduces PCI technology to the mid-range of the Unisys server family with seven PCI slots (along with five EISA). It has also been designed for multiple operating system support — while most of the SMP61000 sales will include Unisys SVR4/MP enhanced Unix operating system, the unit can also run UnixWare and NT Server.

The SMP61000 uses Unisys proprietary Synchronous Coherent Memory (SCM) passive backplane architecture — a 64-bit, 533MBps backplane bus. This architecture provides flexibility, allowing for relatively easy system upgrades via board swaps.

The unit will support up to ten 150MHz Pentium and will have 200MHz Pentium Pro processors when delivered in the third-quarter. SCM allows for processor boards of the same technology, but operating at different speeds, to be mixed in the same base cabinet. Aberdeen expects Unisys to enhance the SCM bus by the end of the year, allowing for up to 24 processors in the unit.

The initial ship of the SMP61000 with Pentium Pro processors will support up to 4GB of memory, but will be increased to 8GB by the end of the year. The unit has some excellent high-availability features, including six hot-swappable internal disks (allowing for internal RAID 0, 1, or 5 configuration) and redundant power supplies. Multiple modular cabinets can be added to house up to seven additional hot-swappable disk drives.

#### High-End Servers

For those needing more power than the SMP61000 can offer, there are several options. One means available for the past several years was via the high-end servers OEMed from Sequent. The second is through the use of a massively parallel processing (MPP) offering called OPUS (Open Parallel Unisys Server) which was developed in cooperation with Intel. OPUS is offered with 8 to 128 Pentium processors, and uses SVR4 Unix with a Chorus microkernel for distributed processing.

The third, and increasingly popular method of increasing both performance and availability is through the use of clustering — increasing potential up time to between 99.9% and 99.999%. Unisys can cluster two, three or four of its SMP systems through the use of Veritas' Vx Reliant — which is based on Pyramid Technology Corp.'s Reliant software. Unisys has added cluster management capabilities enabling failure handling between the four nodes, and an optional distributed lock manager will allow for parallel processing of Oracle's Parallel Server (OPS) applications.

**Figure 2: Unisys High Availability Through Clustering**
*(Source: Unisys, April 1996)*

### Application Development

Unisys has a vast array of applications which can run on these SMP-based servers, has very good working relationships with the RDBMS suppliers (Unisys is the largest reseller of Oracle), and a long history in both On-Line Transaction Processing environments and client/server application development. The Unisys subsidiary, USoft, Inc. markets a set of client-server software tools which can be used for application development on both Unisys and non-Unisys server platforms.

Besides its database and decision support solutions from Oracle and Informix, Unisys is working with Red Brick to offer its customers support in developing decision support warehousing solutions.

[Remaining sections cover Unisys services, SAP R/3 partnership, and Aberdeen's conclusion that Unisys's solution-centric strategy provides a compelling value proposition for enterprises seeking to reduce open systems complexity while maintaining enterprise-grade RAS.]

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-unisys-clearpath-smp-servers |
| title | Unisys Corporation - ClearPath SMP Servers |
| author | Aberdeen Group |
| date | 1996-04-01 |
| type | market-study |
| subject_domain | enterprise-servers |
| methodology | competitive-profiling, industry-analysis, expert-opinion, benchmarking |
| source_file | 1996 Unisys Corporation - ClearPath SMP Servers pr.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group profiles Unisys Corporation's ClearPath SMP Server product line following Unisys's 1995 reorganization. The study examines Unisys's full-service strategy, covers entry-level to high-end SMP servers, and analyzes clustering, OS transition, and application development ecosystem.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Captures Unisys at a key strategic pivot—from proprietary mainframe to Intel-based SMP—at a time when enterprise server markets were consolidating. |
| **Relevance** | medium | ClearPath Forward remains active through 2026 with roadmap to 2050; specific 1996 server specs are primarily historical. |
| **Prescience** | medium | Solution-centric evolution prediction proved partially correct—ClearPath survived but Unisys exited commodity Intel server markets. |

### Prescience Detail

**Prediction 1:** Unisys ClearPath solution-centric evolution
- **Claimed:** Unisys mission to continue moving from systems-centric to solution-centric; ClearPath SMP to mature as enterprise platform
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 1:** Unisys ClearPath evolution outcome
- **Result:** Unisys ClearPath Forward platform survived with roadmap to 2050; however Unisys exited commodity Intel server market and refocused on services and legacy ClearPath platforms
- **Confidence:** verified
- **Notes:** Partial confirmation; services-led transformation succeeded, broader server market share eroded

### Entities Referenced (10)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Unisys Corporation | company | active | — |
| Intel Corporation | company | active | — |
| Sequent Computer Systems | company | acquired | IBM (1999) |
| Oracle Corporation | company | active | — |
| Informix Software | company | acquired | IBM (2001) |
| Veritas Software | company | acquired | Symantec (2005) |
| Pyramid Technology Corporation | company | acquired | Siemens Nixdorf → Fujitsu |
| USoft Inc. | company | dissolved | Unisys absorbed |
| Red Brick Systems | company | acquired | Informix → IBM |
| Aberdeen Group | firm | acquired | Aberdeen Strategy & Research |

### Technologies Referenced (8)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|----------------------|---------------------|
| Unisys ClearPath SMP Servers | platform | Unisys | emerging | legacy-supported |
| Intel Pentium Pro (P6) | platform | Intel | emerging | obsolete |
| Unix SVR4/MP (Unisys Enhanced) | platform | Unisys | mature | obsolete |
| UnixWare 2.1 | platform | SCO/Novell | emerging | obsolete |
| OPUS MPP | platform | Unisys/Intel | mature | obsolete |
| Veritas Vx Reliant Clustering | framework | Veritas | emerging | obsolete |
| Unisys SCM Backplane | platform | Unisys | emerging | obsolete |
| Windows NT Server | platform | Microsoft | emerging | obsolete |

### Observation Summary

- Total observations: 22
- By type: market-data (5), strategy-classification (3), technology-assessment (4), expert-opinion (3), framework-factor (4), viability-prediction (1), actual-outcome (1), benchmark-result (1)
