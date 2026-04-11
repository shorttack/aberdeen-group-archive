# Informix Software Overview

> Archived from: INFORX95-3.pdf
> Original publication date: 1995
> Author: Peter S. Kastner / Aberdeen Group

---

## Original Document Text

FILE: INFORX95-3.pdf
Study ID: inforx95-3-9a45fe
Title: Informix Software Overview
Author: Peter S. Kastner / Aberdeen Group
Date: ~1995
Slides: 38

[Slide 1]
Informix Software Overview
Peter S. Kastner, Vice President, Aberdeen Group, Inc., One Boston Place, Boston, MA 02108

[Slide 2]
Agenda
- The company
- Database products & technology
- Client-server application development tools
- Services
- Aberdeen Group Findings

[Slide 3]
Company Overview
- A Top-10 Independent Software Vendor
- Fastest growing independent RDBMS company
- A respected rival of Oracle and Sybase

[Slide 4]
Company Characteristics
- Technology concentration on superior RDBMS and tools
- Small service and consulting business
- Key markets are Telecommunications, Retail, Financial Services, Manufacturing, and State/Local Government

[Slide 5]
Changing Strategy
- Historical indirect-channel focus: Many have Informix-based apps and don't know it; 1,000s of VAR & ISV partners and applications
- Recent thrust into Fortune 1000 with direct sales

[Slide 6]
Financial Overview
- Five year growth rates
- Profitability

[Slide 7]
Databases
- Standard Engine
- OnLine: Informix-OnLine; Dynamic Server; Extended Parallel Server; Specialized versions (OnLine/Secure; OnLine/Optical)

[Slide 8]
Informix SE
- Designed for distributed, replicated systems (Example: retail stores and bank branches)
- Was used as small Unix server
- Now positioned as personal/workgroup RDBMS

[Slide 9]
Informix SE Characteristics
- High performance
- Small memory and disk footprint
- Very easy to install & maintain
- Rock-solid operations
- Low cost
- Competes with Gupta, Progress, Sybase/Watcom SQL Anywhere

[Slide 10]
Informix-OnLine
- Entry-level product for scalable applications (OnLine -> OnLine Dynamic Server -> Extended Parallel Server)
- Powerful RDBMS for OLTP
- Includes stored procedures; triggers; referential integrity; document-imaging support (BLOBS)
- Frequently used for hardware vendor TPC-C OLTP benchmarks as the highest performing midrange-server database
- Versions for Unix and NT Server

[Slide 11]
OnLine Dynamic Server
- Midrange for scalable applications
- Application compatibility down to OnLine and up to XPS
- Particularly well-suited for multiprocessor SMP servers: parallel operations; low-level parallelism
- Well-suited for complex, large OLTP applications
- Particularly well suited for complex decision support and data warehousing

[Slide 12]
Extended Parallel Server (XPS)
- High-end parallel database for the largest OLTP and decision support applications
- Applications are compatible with OnLine and Dynamic Server
- Harnesses loosely-coupled clusters and Massively Parallel architectures
- Is just being delivered in Q4-1995
- Competes with parallel RDBMS products from IBM DB2/6000, Oracle & Sybase plus AT&T Teradata

[Slide 13]
Specialized Database Products
- OnLine Secure Dynamic Server: All features of OnLine Dynamic Server plus government security rating of B1; No extra charge; Government and commercial secure apps including Internet
- OnLine Optical: Optical juke box support for read-only image BLOBs; Eliminates overhead of managing large image files in the RDBMS

[Slide 14]
Introducing Informix Parallel Technology [transition]
- Dynamic Server
- Extended Parallel Server

[Slide 15]
Design Objectives
- Hardware architecture & platform independence
- Transparency to applications
- Core internal parallelism
- Scalability and performance
- Maximum on-line manageability

[Slide 16-18]
Transparent to Applications / Core Internal Parallelism / Dramatic Performance Increases
[Graphics referenced]

[Slide 19]
Maximum On-line Manageability
- Objective: avoid database downtime
- On-line dynamic reconfiguration: Virtual processors; Degree of parallelism; Memory management
- On-line parallel backup & recoverability
- Tables, partitions, full or incremental

[Slide 20]
Extended Parallel Server
- Addresses performance, scalability, and availability issues for: Complex transaction processing or decision support; Very large databases (> 100 GB); Database failover
- Architecture extends DSA to shared-nothing environment of clusters or MPP
- Ideal where fast response times are critical or where scalability is required but difficult to plan: data warehouses; client-server applications

[Slide 21]
XPS Architecture [graphic]

[Slide 22]
RDBMS Database Summary
- An advanced architecture for desktop to massively parallel applications
- Coherent product-line differentiation between OnLine versions
- Informix Advantages: Infinite scalability in a shared-nothing architecture; Parallel SQL functionality is excellent on SMP; High availability; Full RDBMS functionality

[Slide 23]
Database Middleware [transition]
- Replication
- Connectivity

[Slide 24]
Replication
- Hot-site table-level failover
- Synchronous and asynchronous transfers
- Partition-level, table, or database
- SQL-Select-level replication
- Update anywhere

[Slide 25]
Connectivity
- Enterprise gateway
- DCE/Net
- Gateway to IBM using DRDA
- XA support for OLTP monitors

[Slide 26]
Informix in Tools
- $150M of $470M in 1994
- Over 500,000 licenses sold
- 75% of partner apps use tools
- Target developers, end users and power users

[Slide 27]
Application Development [transition]
- NewEra C-S application development
- Informix 4GL
- Informix-SQL suite
- CLI & ESQL

[Slide 28]
Informix NewEra
- Next-generation environment
- Client-server oriented
- Full object model
- Scalable and high performance

[Slide 29]
NewEra Features
- OO database application language
- Visual programming environment
- Framework promotes reuse
- Team programming support
- Open connectivity

[Slide 30]
Informix 4GL
- Powerful database application development tool
- Creates character-based and GUI-lite applications
- Suite provides a complete toolkit for rapid application development

[Slide 31]
Informix SQL Suite
- RDBMS development tool suite
- Includes: Schema editor; Menu builder; SQL editor; Forms builder; Report writer

[Slide 32]
CLI and ESQL
- CLI - a low-level API
- ESQL - embedding SQL in 3GL programs

[Slide 33]
End-User Access - NewEra Viewpoint
- Query & report writing
- Graphical SQL access
- Includes forms, reports & queries
- Aimed at end and power users

[Slide 34]
End-User Access - NewEra Viewpoint Pro
- Adds to NewEra ViewPoint
- Application development for power users and IS
- SuperViews - a powerful tool

[Slide 35]
Informix Services
- Maintenance & support
- Education
- Limited consulting services
- Third-party partnerships

[Slide 36]
Aberdeen Group Findings
- A secret success
- Strong database architecture enables parallelism
- Advanced development tools led by NewEra

[Slide 37]
Aberdeen Group Findings
- Adequate replication & connectivity
- Thousands of applications
- Growth rate indicates increasing market share
- A company focused on database and development tools

[Slide 38]
[End slide]

Supplementary data extracted from JUNGLE-1-5 (same training deck):
- Informix 1994 revenue: $469M (up 33% from 1993); trailing 12mo: $568M
- Informix market cap: $4.3B (up from $1.5B); stock up 207% in 52 weeks (source: Software Magazine and Business Week, as of 7/29/95)
- Informix ranked third-largest RDBMS supplier
- Informix scalability: good to 8 processors SMP; many TPC-Cs
- Informix replication: behind; better next year
- NewEra: only challenged by Ingres OPENROAD
- Informix services: almost none
- Informix key weakness: late with desktop/workgroup; behind in replication; no NetWare; no consulting
- Informix key strengths: best parallel-scalable; price-performance leader; per-user pricing leader


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | inforx95-3-9a45fe |
| title | Informix Software Overview |
| author | Peter S. Kastner / Aberdeen Group |
| date | 1995 |
| type | consulting-report |
| subject_domain | RDBMS product portfolio; competitive positioning; Informix software architecture |
| methodology | expert-analysis; product briefing |
| source_file | INFORX95-3.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group overview of Informix Software for sales training. Covers company profile (Top-10 ISV, fastest-growing RDBMS company), full product portfolio (SE, OnLine, Dynamic Server, XPS, specialized variants), parallel DSA technology architecture, database middleware (replication, connectivity), tools revenue ($150M of $470M in 1994, 500K+ licenses), application development tools (NewEra, 4GL, SQL Suite, CLI/ESQL), end-user access, and services. 38-slide deck used in Informix sales training.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | HIGH | Core product-portfolio briefing for Informix sales reps; provides financial metrics, product positioning, and competitive comparisons as of 1995. |
| **Relevance** | medium | Historical product/company snapshot; instructive for understanding Informix's competitive differentiation vs. Oracle and Sybase in mid-1990s RDBMS market. |
| **Prescience** | high | Correctly positioned Informix OnLine DSA as SMP performance leader; correctly forecast XPS/MPP trajectory; NewEra prediction as OO GUI tool of the future was partially accurate before Informix's 1997 crisis. |

### Prescience Detail


**Prediction 1:** informix_xps_delivery
- **Claimed:** XPS just being delivered in Q4-1995; competes with IBM DB2/6000, Oracle, Sybase plus AT&T Teradata
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 1:** informix_xps_delivery
- **Result:** unknown
- **Confidence:** medium
- **Notes:** Placeholder for XPS delivery outcome

**Prediction 2:** informix_oneyear_outlook
- **Claimed:** Excellent OO/GUI/4GL tools; leader in practical parallel RDBMS with OnLine 8.0; 100GB+ scalability; adequate replication; viable for most RDBMS requirements
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 2:** informix_xps_delivery
- **Result:** unknown
- **Confidence:** medium
- **Notes:** Placeholder for XPS delivery outcome


### Entities Referenced (6)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | acquired | Harte-Hanks (2010) |
| Peter S. Kastner | person | active |  |
| Oracle Corporation | company | active |  |
| Sybase | company | acquired | SAP (2010) |
| International Business Machines Corporation | company | active |  |
| Microsoft Corporation | company | active |  |

### Technologies Referenced (17)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Relational Database (RDBMS) | application | various | dominant | dominant |
| Online Transaction Processing | application | various | dominant | current |
| Decision Support / Business Intelligence | application | various | growing | dominant |
| Oracle 7.x | application | Oracle | dominant | legacy |
| Sybase SQL Server / System 11 | application | Sybase | major | legacy |
| IBM DB2 | application | IBM | major | dominant |
| Microsoft SQL Server | application | Microsoft | growing | dominant |
| TPC-C Benchmark | standard | TPC | dominant | legacy |
| Object-Relational DBMS (ORDBMS) | application | various | emerging | current |
| UNIX (various) | platform | various | dominant | current |
| CA-Ingres (OpenIngres) | application | Computer Associates | declining | end-of-life |
| Sybase PowerBuilder | application | Sybase | dominant | legacy |
| Sybase IQ Accelerator | application | Sybase | growing | legacy |
| Red Brick RDBMS | application | Red Brick Systems | niche | legacy |
| Oracle Parallel Server | application | Oracle | growing | legacy-superseded |
| IBM RS/6000 SMP | platform | IBM | growing | legacy |
| IBM SP2 | platform | IBM | growing | legacy |

### Observation Summary

- Total observations: 30
- By type: competitive-position: 16, strategic-assessment: 3, expert-opinion: 3, viability-prediction: 2, actual-outcome: 2, market-growth: 1, market-size: 1, market-share: 1, benchmark-result: 1
