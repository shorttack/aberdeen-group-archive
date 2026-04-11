# Welcome to the RDBMS Jungle — Chapter 6

> Archived from: JUNGLE-6.pdf
> Original publication date: 1995
> Author: Peter S. Kastner / Aberdeen Group

---

## Original Document Text

FILE: JUNGLE-6.pdf
Study ID: jungle-6-7af8b7
Title: Welcome to the RDBMS Jungle — Chapter 6
Author: Peter S. Kastner / Aberdeen Group
Copyright: AberdeenGroup 1995
Slides: 58

[Slide 1]
Database Market Agenda
- Market Size
- Market Characteristics
- Suppliers
- Buyer Needs

[Slide 2]
Database Market Size (reprised)
- Overall WW market around $20 billion
- RDBMS market is largest segment at $5.5 billion
- Biggest market US, second Europe, fastest growing Japan (3rd largest) and Latin America
- Unix-server DBMS revenue now greater than mainframe revenues
- Major RDBMS suppliers are growing by 30-70% per year in revenue
- Pure decision support not yet over $2 billion. Bulk is OLTP and product query

[Slide 3]
Market Characteristics (reprised)
- An increasing number of sales for application server or database server to carry out one competitive-advantage application
- RDBMS submarket is exceptionally fast-growing (50+% per year)
- Aberdeen research sees 9 RDBMS licenses for every 10 commercial multiuser servers

[Slides 4-22]
[Supplier profiles -- Sybase, CA, Informix, Oracle, IBM, Microsoft -- same as JUNGLE-1-5 chapters 1-5]

Sybase 1994 revenue: $826M (+71%); Market cap $2.4B; 51.9% YTD growth; 41% stock drop April 1995
CA: $2.74B revenue; 22.2% net margin; 30% CS/70% mainframe; $30M Ingres marketing campaign
Informix 1994 revenue: $469M (+33%); trailing 12mo $568M; Market cap $4.3B (+from $1.5B); stock +207%
Oracle 1994 revenue: $2.4B (+40%); Market cap $18.7B (+100%); on track for $3.6B+ FY1996
IBM: largest DBMS supplier; DB2 focus; parallel SP2/PQS; proprietary replication
Microsoft SQL Server 6.0: derived from Sybase; diverged; 2,800 tpm_C on DEC Alpha; largest unit sales; 25% growth

[Slides 23-30]
[Hardware partnerships section -- same as JUNGLE-1-5]

[Slides 31-35]
[RDBMS common features; Top-10 humorous list; Aberdeen 1995 themes]

[Slide 36]
Aberdeen's 1995 RDBMS Rating Categories
- Scalability
- Distributed Data
- Open Data Access
- Development Tools
- Other Technology
- End-User Solutions

[Slide 37]
Scalability (same as JUNGLE-1-5 slide 37)

[Slide 38]
Scalability Notes
- CA Ingres: Modest scalability; no MPP
- IBM DB2 for AIX: Competitive but not leading on SMP; Only compatible SMP and MPP story except AT&T
- Informix: Good scalability to 8 processors on SMP. Many TPC-Cs. Soon on SP2 with version 8
- Microsoft: Modest scalability; no MPP; good on Alpha
- Oracle: Good scalability story from desktop to SP2 & ES/9000; No TPC-C until July 1995 -- Hot stuff
- Sybase: Poor scalability beyond 4 processors. Navigation Server: Poor high-end MPP on AT&T 3600

[Slide 39]
Distributed Technology (no separate Informix position slide in chapter 6)

[Slide 40]
Distributed Technology Notes
- CA Ingres: Best functionality
- IBM DB2 for AIX: Good async replication in Data Propagator, but no peer-peer replication
- Informix: Behind; better next year
- Microsoft: Limited replication in new SQL Server 6 for NT
- Oracle: Good replication including peer-peer
- Sybase: OK asynchronous replication; no peer-peer

[Slide 41]
Open Technology (categories)

[Slide 42]
Open Technology Notes
- CA Ingres: good mainframe gateways
- IBM DB2 for AIX: full 2-way DRDA, ODBC; limited non-IBM gateways
- Informix: DRDA client; limited gateways, but IBI ties. Improving APIs
- Microsoft: great for PC apps; OLE; ODBC inventor
- Oracle: DRDA client; broad gateways. Improving APIs.
- Sybase: Open Client & Open Server appeal to 3GL bigots. Best gateway breadth. Overall, most flexible.

[Slide 43]
Distributed Tool Technology (categories)

[Slide 44]
Development Tool Notes
- CA Ingres: OpenROAD is most mature OO CADE
- IBM DB2 for AIX: No comparable tools for OO CADE. More limited ISV selection
- Informix: New Era is maturing as OO CADE
- Microsoft: MFC as a 4GL is excellent for MS environment
- Oracle: clunky tools only work on Oracle. Oracle Objects is interesting but low-end, incompatible with Developer/2000
- Sybase: Powersoft & Watcom are among market leaders

[Slide 45]
Other Technologies (categories)

[Slide 46]
Other Technology Notes
- CA Ingres: partnership with Fujitsu for 1st ORDBMS in '96
- IBM DB2 for AIX: fast moving into searchable audio, video, user-defined data types. Hot stuff.
- Informix: not much today. Practical BLOB support.
- Microsoft: OLE, futures
- Oracle: Most aggressive in multimedia marketing; objects by 1997; serious about video on demand
- Sybase: more multimedia/OO talk than action

[Slide 47]
Supplier Solutions (categories)

[Slide 48]
Supplier Added-Value Notes
- CA Ingres: almost no services; many ISVs plus CA apps
- IBM DB2 for AIX: world-class services; growing number of ISVs with many apps
- Informix: almost no services; many ISV apps; never own apps
- Microsoft: no services; most apps are for workgroups
- Oracle: lots of services; many ISVs; Oracle applications
- Sybase: fewer services; fewer ISVs; no applications

[Slide 49]
CA-Ingres Weaknesses
- No Ingres people remain -- but no customers have defected
- CA sales force does not understand the Unix world
- Product quality was poor, getting better
- RDBMS architecture is at On-Line 6.0 level -- no parallel
- OPENROAD left customers with character 4GL behind -- totally different, incompatible environment

[Slide 50]
IBM Weaknesses
- Essentially a new player with SMP RS/6000's and DB2/6000 v2 -- Old limits are still remembered
- Must shatter perceptions of limited scalability
- Limited cross-platform, cross-OS
- Still caution by "open" zealots

[Slide 51]
Informix Weaknesses
- Late with desktop & workgroup database/tools
- Behind in replication and will remain so
- NewEra 2.0 makes the product more useable
- Slow to build direct sales force, marketing ... missed growth opportunities over past two years
- No NetWare story
- No-consulting policy slowed large enterprise growth

[Slide 52]
Oracle Weaknesses
- RDBMS engine looks dated -- where are the TPC-C's?
- Informix can win on architecture and demonstrated performance
- Deal-driven, not partnership driven
- No 2nd generation client-server ala NewEra
- Unfocused: Hollywood multimedia, applications, TV set-tops
- Service/consulting drive makes ISV partnering tough
- Informix is the RDBMS specialist to Oracle the generalist

[Slide 53]
Sybase Weaknesses
- 1980s architecture runs out of steam -- need System 11 now
  - Poor scalability in SMP, database size = departmental RDBMS
- Poor GUI tools drove Powersoft acquisition
- Navigation Server platform-limited to NCR 3600, an OLTP dog (SP2 version imminent)
- Very few application solution partners & solutions
- A North American phenomenon, hardly seen elsewhere
- Over-reaching sales tactics turn off customers

[Slide 54]
Where is IBM Best Positioned Today?
- Worldwide support and service ... the SAP R/3 story
- Enterprises that commit to DB2 across IBM platforms
- With mainframe ISVs who have ported to client-Unix-server
- Departmental systems to 4-6 processors for OLTP -- SMP is new for RS/6000, old for competition
- Expandable workgroup-plus servers above/at OS/2 level -- SMP & SP2 improve ability to do bigger systems
- Modest data warehouses on SMP or SP2 -- Products now in place. Field experience will come over next year.

[Slide 55]
Wrap-up
- RDBMS on midrange server is the hot market
- Technology is incredibly fast-moving
  - Deemphasize today's product speeds and feeds
  - Emphasize long-term cost-of-ownership benefits
- Users are emphasizing scalability and flexibility
  - Parallel-scalable technologies for multi-size OLTP and definitely for data warehousing
  - Replication technologies for managing the process of moving data around the enterprise

[Slide 56]
ISV Support for Unix Platforms
- Application solutions pull through hardware/RDBMS
- IBM gained market share in 1994, usually at the expense of HP
Platform Choices by Hardware Supplier (Source: Aberdeen Group and ISVs)

[Slide 57]
Where RS/6000 with DB2 is Best Suited
Product Strengths:
- DB2 for AIX 2 engine -- functionally much improved but nobody knows about it
- Distributed technology using Data Propagator between mainframe and middle-server RS/6000s
- Good performance and price-performance
- Outstanding OLTP support with CICS, Ensina, & Tuxedo
- Promising scalability with HACMP and SP2

[Slide 58]
RS/6000 DB2 Elevator Story (for CIO & CEO)
[Content: Summary pitch for IBM RS/6000 + DB2 combination to executive decision makers]


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | jungle-6-7af8b7 |
| title | Welcome to the RDBMS Jungle — Chapter 6 |
| author | Peter S. Kastner / Aberdeen Group |
| date | 1995 |
| type | consulting-report |
| subject_domain | RDBMS vendor competitive analysis; technology ratings; IBM DB2 positioning |
| methodology | expert-analysis; competitive-intelligence; market-research |
| source_file | JUNGLE-6.pdf |
| license | CC-BY-4.0 |

### Abstract

Chapter 6 continuation of the RDBMS Jungle training deck. Reprises market size and supplier data from Chapters 1-5, then provides expanded competitive detail: vendor-by-vendor weakness analyses, RDBMS technology rating breakdowns (scalability, distributed data, open technology, development tools, other technologies, supplier solutions), ISV platform support data (IBM gaining Unix share at HP's expense in 1994), IBM RS/6000 + DB2 best-fit scenarios, and wrap-up on RDBMS market dynamics. 58-slide deck.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | HIGH | Deep competitive-intelligence supplement to JUNGLE-1-5; particularly valuable for IBM DB2 positioning and vendor weakness analysis from Informix sales perspective. |
| **Relevance** | medium | Historical primary-source competitive intelligence; IBM's 1994 Unix market share gain at HP's expense is a specific data point of archival significance. |
| **Prescience** | very-high | Correctly identified all major vendor weaknesses that materialized: Oracle's multimedia distraction; Sybase's architectural stagnation; IBM's perception problem; CA-Ingres's market decline. IBM gaining Unix share at HP's expense in 1994 proved a real trend. Microsoft's upward trajectory was underestimated. |

### Prescience Detail


**Prediction 1:** oracle_oo_multimedia
- **Claimed:** Most aggressive in multimedia marketing; objects by 1997; serious about video on demand
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 1:** oracle_oo_multimedia
- **Result:** unknown
- **Confidence:** medium
- **Notes:** Placeholder: Oracle multimedia/OO actual outcome

**Prediction 2:** ca_ingres_ordbms
- **Claimed:** CA-Ingres partnership with Fujitsu for first ORDBMS in 1996
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 2:** oracle_oo_multimedia
- **Result:** unknown
- **Confidence:** medium
- **Notes:** Placeholder: Oracle multimedia/OO actual outcome


### Entities Referenced (12)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | acquired | Harte-Hanks (2010) |
| Peter S. Kastner | person | active |  |
| Oracle Corporation | company | active |  |
| Sybase | company | acquired | SAP (2010) |
| Computer Associates (CA) | company | renamed | CA Technologies/Broadcom |
| International Business Machines Corporation | company | active |  |
| Microsoft Corporation | company | active |  |
| Sun Microsystems | company | acquired | Oracle (2010) |
| Hewlett-Packard (HP) | company | split | HP Inc. & HPE (2015) |
| Ingres | company | acquired | Computer Associates |
| Sequent Computer Systems | company | acquired | IBM (1999) |
| Tandem Computers | company | acquired | Compaq (1997) |

### Technologies Referenced (25)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Relational Database (RDBMS) | application | various | dominant | dominant |
| Online Transaction Processing | application | various | dominant | current |
| Decision Support / Business Intelligence | application | various | growing | dominant |
| Oracle 7.x | application | Oracle | dominant | legacy |
| Oracle 8 | application | Oracle | pre-release | legacy |
| Sybase SQL Server / System 11 | application | Sybase | major | legacy |
| Sybase Navigation Server | application | Sybase | niche | legacy |
| Sybase IQ Accelerator | application | Sybase | niche | legacy |
| Sybase PowerBuilder | application | Sybase | dominant | legacy |
| IBM DB2 | application | IBM | major | dominant |
| IBM SP2 | platform | IBM | growing | legacy |
| IBM RS/6000 SMP | platform | IBM | growing | legacy |
| Microsoft SQL Server | application | Microsoft | growing | dominant |
| CA-Ingres (OpenIngres) | application | Computer Associates | declining | end-of-life |
| TPC-C Benchmark | standard | TPC | dominant | legacy |
| UNIX (various) | platform | various | dominant | current |
| IBM AIX | platform | IBM | mature | current |
| HP 9000 | platform | HP | mature | legacy |
| Sun Solaris | operating-system | Sun | dominant | legacy |
| Object-Relational DBMS (ORDBMS) | application | various | emerging | current |
| Oracle Parallel Server | application | Oracle | growing | legacy-superseded |
| IBM CICS TP Monitor | platform | IBM | mature | current |
| IBM SP2 | platform | IBM | growing | legacy |
| IBM RS/6000 | platform | IBM | growing | legacy |
| IBM DB2 for AIX | application | IBM | growing | legacy |

### Observation Summary

- Total observations: 42
- By type: competitive-position: 31, market-share: 3, market-size: 2, viability-prediction: 2, market-growth: 1, actual-outcome: 1, recommendation: 1, benchmark-result: 1
