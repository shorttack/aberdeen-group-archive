# PyramidOLTP Overview

> Archived from: PYRAMI-1.pptx
> Original publication date: 1995
> Author: Wayne T. Kernochan; Robert J. Sakakeeney

---

## Original Document Text

# PYRAMI-1

*Source: PYRAMI-1.pptx — 30 slides*

## Slide 1

PyramidOLTP Overview
Wayne T. KernochanRobert J. SakakeeneyAberdeen Group, Inc.One Boston PlaceBoston, Mass. 02108(617) 723-7890

## Slide 2

Agenda
Impact of Information Technology on Business
Midrange Platform Technology & Leading Suppliers

## Slide 3

Summary
Business is continuously in a state of change
Information technologies grow only when they solve real world business problems
Many business executives have learned how to use IT for the benefit of their enterprises.  Many have not and tend to blame their IS staffs
The IS function within an enterprise is charged with evaluating new information technologies and implementing them as appropriate for the benefit of the entire enterprise
  - The technologies are changing too rapidly to keep abreast of all
  - Business goals and requirements are unclear and changing

## Slide 4

Top Mgt Issues For IT Executives

## Slide 5

Aberdeen Three Tier Plus Model
Mainframe
(Massively) Parallel
Division,  Department
Replicated Branch
PC, Workstation
PC LAN
PC LAN Server
ProductionSystem
DecisionSupportSystem
OLTP at POS
User Desktops and Workgroups

## Slide 6

Increase Line Access to Data
Workgroup Server
and/or Router
Fat Clients
Enterprise Databases
Departmental/
Other Workgroup
Servers

## Slide 7

Adopting Technology
RDBMS
Unix
NT
ORDBMS
Downsizing
Warehousing
Multi-tier OLTP

## Slide 8

Examining the Midrange Leaders
IBM
Hewlett-Packard
Digital Equipment
Sun Microsystems
AT&T Global Information Systems

## Slide 9

1995 Worldwide Commercial Multiuser Risc/Unix Market $14B
Source: Aberdeen Group, February, 1995
Market Share

## Slide 10

IBM Hardware Line-up
RS/6000 Servers
  - Second largest supplier of multiuser RISC/UNIX systems -- 19% market share
  - 52% revenue increase ‘93/94
  - 1994 revenues = $2 billion
  - Product line is transitioning from uniprocessor, Power2 (RIOS) systems to SMP, PowerPC 601 servers
  - Following an IBM-first strategy, will frequently offer DB2/6000 RDBMS at considerable cost savings with platform
  - Value Proposition: IBM’s professional services organizations will help our customers implement RISC/UNIX-based open, client-server computing with the RS/6000

## Slide 11

IBM Hardware Line-up
SP2
  - Up to 512 Power2 processors each running AIX 4.x for commercial and technical applications
  - 1995 revenues = $400 million
  - Positioned as high-end of RS/6000 line and DB/2 offload for ES/9000
  - Major commercial applications: Complex Decision Support, LAN server consolidation, OLTP
  - Has generated 380 ISV promises to port RDBMSs and applications
  - Futures: SMP Nodes and RIOS2 upgrades
  - Value Proposition: IBM’s entry into very large scale, open systems computing.  Hot new technology from IBM.

## Slide 12

IBM Strengths
Size
  - Global support
  - Range of products
  - Talent pool to draw upon
Customer base and sales reps’ knowledge of customers
  - Shared history,  Customer Trust
  - Former IBM employees working now as customers
Services
  - Planning, Implementation, Operations, Outsourcing, Financing
Third-party support and competition
  - ISVs by the 1,000’s
  - PCM and peripheral suppliers
  - Professional service organizations (e.g., Andersen Consulting)

## Slide 13

IBM Challenges
Processor technology -- PowerPC 600 will not be leading the industry for many years
Re-energizing and focusing the field organization
Gaining the trust of leading-edge, business line manager, and X-generation buyers
Learning how to work with ISVs as allies -- not enemies
Recognizing that its chief competition for IS executive allegiance is not other hardware suppliers such as HP but software solution suppliers such as Oracle, SAP, and Microsoft

## Slide 14

Points-You-Should Know: IBM RS/6000
Customers buy RS/6000 for support and historical relationship reasons and have replaced it until lately because of lack of high-end growth path.
Platform-of-choice for VARs whose customers cannot afford AS/400 but want IBM platform
RDBMS ISVs fear that if they recommend RS/6000 IBM will still switch customer to low priced DB2/6000
Expect growth to continue in 1996 as datacenter managers experiment with RS/6000 Tier-2 surround strategies
RS/6000 with DB2 is neither the fastest nor least expensive option
Whole story includes NetView, Data Propagator, DataHub

## Slide 15

HP Hardware Line-up
Midrange:
HP 9000:
  - Multi-user RISC/UNIX industry leader -- 50% share
  - 57% revenue growth in 1995
  - 1995 revenues = $5 billion
  - Value Proposition: Leading platform for Unix applications in terms of technology and ISV application support
HP 3000:
  - Legacy MPE/IX system updated with HP’s PA-RISC technology. Same hardware as HP 9000 but with MPE/iX operating system

## Slide 16

HP Strengths
Trusted-supplier by IS decision makers for making the transition to high-performance UNIX systems
Supports and is supported by ISVs and professional service organizations -- usually as a first among equals
One of a handful of hardware suppliers that can support enterprises on a global basis
Technology leadership perception
  - RISC processors
  - Complete Unix operating environment
  - OpenView systems management framework
HP Professional Service Organization knows Unix operating environment capabilities thoroughly

## Slide 17

HP Challenges
Running as a lean and mean organization means business opportunities often slip by
Making the transformation from selling hot boxes on price and price/ performance to being seen as an incumbent supplier that can add value in additional ways
Current generation of PA-RISC, PA-7200, is not the fastest chip in the market
Does not have a very high-end RISC/UNIX product offering (i.e. clusters & MPP) and is being squeezed by Intel/NT at the low end
After 3 years as Top Gun, HP is getting arrogant, sloppy

## Slide 18

Points-You-Should Know: HP
Is considered the mainframe alternative leader
In new sales deals, HP’s most common hardware competitors will be IBM and Sun
HP’s Computer Systems Organization (HP 3000/9000, Workstations, PSO) has a separate sales force from its Computer Products Organization (Vectras, LaserJets, NetManagers) resulting in sales confusion and annoyance for customers and prospects
Is consistently ranked as one of the computer industry’s most respected companies
Should be respected but not feared.  HP is not invincible.

## Slide 19

Digital Hardware Line-up
Midrange:
Digital ALPHAserver XX00:
  - Multi-user RISC/UNIX 64 bit -- 3% market share
  - 75% revenue growth rate 1995
  - Value Proposition: Faster processors capable of managing vast amounts of memory and disk -- VLM64
Digital VAX:
  - Legacy VMS system updated to OpenVMS
  - VAX revenues declining 50% per annum
  - 1995 revenues = less than 10% of company revenues - with all add-ons
  - Value Proposition: Hold base while selling evolution and migration (if possible) to OpenVMS and ALPHA AXP

## Slide 20

Digital Strengths
Alpha performance combined with aggressive pricing has created the best price/performance in the industry.
Digital's UNIX (OSF/1) meets the specifications of more standards setting groups than any other Unix operating system.
Digital will deliver enterprise-class open platforms with Microsoft NT on Alpha.  Note recent TPC-C benchmarks.
Digital is creating software frameworks for enterprise-wide open computing to meet customer needs for applications interoperability from the desktop to datacenter.

## Slide 21

Digital Challenges
Digital is finally emerging from the restructuring woods.  As a result, customers and prospects remain concerned about:
  - who will sell to them
  - where support will come from
  - which support people will continue to be there
  - which promised products may be eliminated
With the current neutral attitude of prospects to Digital's limited number of Alpha UNIX systems, Digital has yet to establish a critical mass for long-term viability.
Alpha/NT looks like a rosy future, but lacks 1996 revenues to sustain the company alone

## Slide 22

Points-You-Should Know: Digital
The company's diligence and resolve is regaining it respect from the industry and Wall Street.  Prospects becoming more willing to entertain a Digital solution.
Digital remains an excellent engineering company.  Development of Large In-Memory Databases (LIMD) could revolutionize enterprise OLTP and complex DSS.
Digital and Oracle have been increasing their strategic commitments
  - Oracle acquires RDB and installed base
  - Oracle is the LIMD database

## Slide 23

Sun Hardware Line-up
Midrange:
SPARCcenter 2000 and SPARCserver 1000 :
  - Multi-user RISC/UNIX - 9% market share
  - Revenues = ~ 20%  of Sun / $1.3 Billion
  - SPARCcenter -  2 to 20 processors
  - SPARCserver -  2 to 8 processors
  - Challenging IBM for number 2 position with ISVs for application support
  - Value Proposition:  The open systems, price leader for enterprises that want alternative high-risk, high-reward solutions

## Slide 24

Sun Strengths
Originator and still a leader in the open systems client-server computing marketplace.  Customers and Prospects still may have Sun religion.
Large number of software applications available - a pound-for-pound leader.
Sun is regarded as an innovator in providing networked client/server solutions to the industry.
Sun’s positive working relationships with value-added resellers and third party distributors can mean  lower acquisition and maintenance costs.
Strong ISV relationships.  Most ISVs use Sun workstations to develop their client/server products and applications.

## Slide 25

Sun Challenges
Sun direct field support is limited and is often contracted out to other firms.
There are very few  references for running SPARCcenter 2000s and SPARCserver 1000s for business critical production OLTP applications.
Transitions between operating system releases has historically been problematic, compounded by minimal technical support from its corporate offices.  Problems with Solaris in 1994.
Real world scalability of applications appears to be very poor on all of Sun’s workstations and servers.
Loss of influence.  Sun does not appear to be a major player in the new generation of standards setting groups.  Many Sun products, such as its critical OpenLook GUI, may be excluded from future standards.

## Slide 26

Points-You-Should Know: Sun
Large number of applications.
Champion of the “common” customer.
Strong alternate channel presence - will sell through any distributor.
1996 is an important product year with UltraSPARC 64-bit rollout
Sun’s commercial client/server strategy is making inroads via Networking and application development.
Sun maintains both the lowest entry price and best price/performance point for commercial servers.

## Slide 27

AT&T Global Information Solutions (i.e. NCR)
1995 total revenues of approx. $7.0 Billion
Revenues have been flat for several years -- with financial results running in the red
Spin-out of AT&T has immediate implications to customers and prospects
  - Is the company viable?
  - Will the company play in my market?

## Slide 28

AT&T Global Information Solutions (i.e. NCR)
Product strategy is to offer open systems based on midrange to massively parallel product lines -- Worldmark models from  departmental to Teradata for decision support
All servers based on Unix and Intel Pentium microprocessor -- no RISC servers
Unix System V.4 MP OS with Reliability, Availability, Serviceability enhancements
Low-end servers also run OS/2, SCO Unix, NetWare, and Windows NT (an NT champion)
Full line of peripherals, including RAID storage
High availability clustering with LifeKeeper
Open OLTP with TopEnd

## Slide 29

NCR Strengths
Breadth of compatible server products is excellent
Good, often leading, TPC price/performance
The backing of AT&T (for a few more months)
Bullet-proof version of UNIX.  Known for stability.
The Intel multiprocessor market champion (vs. RISC) and leader --  ~$2.0 Billion in 199
Market strength and broad solutions strength in retail and banking
  - Will mostly consolidate into above markets
  - Also Telecomm, Government, Transportation markets

## Slide 30

NCR Challenges
While the leader in Intel/Unix servers, losing ground to leading RISC providers, not to mention Compaq
Never the leader in OLTP high-end performance
Intel is depending on NCR to be premier supplier of P6-based servers for enterprise computing
Organization seems to lack the fire required to gain market share
Customer base may erode due to financial uncertainties and pull-out from general market distribution
Failure to properly manage Teradata for big customers has resulted in unexpected backlash and opened up new opportunities for data warehousing/complex DSS.


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | 1995-midrange-oltp-platform-overview-pyr-44c8e4 |
| title | PyramidOLTP Overview |
| author | Wayne T. Kernochan; Robert J. Sakakeeney |
| date | 1995 |
| type | market-study |
| subject_domain | midrange-platforms |
| methodology | industry-analysis, competitive-profiling, market-sizing |
| source_file | PYRAMI-1.pptx |
| license | CC-BY-4.0 |

### Abstract

This Aberdeen Group presentation frames mid-1990s enterprise computing with its Three Tier Plus model and then profiles the leading commercial midrange RISC/UNIX suppliers. It combines market-share and revenue sizing with vendor-by-vendor strengths, challenges, and buying guidance for IBM, Hewlett-Packard, Digital Equipment, Sun Microsystems, and AT&T GIS/NCR. The deck is also notable for explicit forward-looking claims about RS/6000 momentum, UltraSPARC, Digital large in-memory databases, and NCR's Intel server role.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | The deck captures a concise 1995 snapshot of the commercial multiuser RISC/UNIX market, pairing Aberdeen's framework with vendor shares, revenue figures, and strategic assessments during a pivotal client-server transition. |
| **Relevance** | medium | The product details are period-specific, but the presentation remains useful for understanding how analysts framed midrange platform competition, open systems adoption, and enterprise buying criteria in the mid-1990s. |
| **Prescience** | medium | Several directional calls look sound from general knowledge, including continued RS/6000 momentum, the importance of UltraSPARC, and intensifying Intel-based server competition, but not every vendor-specific expectation appears equally durable. |

### Prescience Detail


**Prediction 1:** rs6000 growth outlook
- **Claimed:** Expect RS/6000 growth to continue in 1996 as datacenter managers experiment with Tier-2 surround strategies.
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 1:** rs6000 growth outlook
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Placeholder for later verification of the 1996 RS/6000 growth outcome.

**Prediction 2:** large in-memory databases impact
- **Claimed:** Development of large in-memory databases could revolutionize enterprise OLTP and complex DSS.
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 2:** large in-memory databases impact
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Placeholder for later verification of the LIMD prediction.

**Prediction 3:** ultrasparc product-year importance
- **Claimed:** 1996 will be an important product year for Sun because of the UltraSPARC 64-bit rollout.
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 3:** ultrasparc product-year importance
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Placeholder for later verification of the UltraSPARC outcome.

**Prediction 4:** ncr p6 server leadership outcome
- **Claimed:** Intel is depending on NCR to be the premier supplier of P6-based servers for enterprise computing.
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 4:** ncr p6 server leadership outcome
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Placeholder for later verification of NCR's P6 server leadership outcome.


### Entities Referenced (15)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | [DEFERRED] |  |
| Wayne T. Kernochan | person | [DEFERRED] |  |
| Robert J. Sakakeeney | person | [DEFERRED] |  |
| IBM Corporation | company | [DEFERRED] |  |
| Hewlett-Packard Company | company | [DEFERRED] |  |
| Digital Equipment Corporation (DEC) | company | [DEFERRED] |  |
| Sun Microsystems Inc. | company | [DEFERRED] |  |
| AT&T Global Information Solutions | company | [DEFERRED] | ncr-corporation |
| NCR Corporation (formerly AT&T GIS) | company | [DEFERRED] |  |
| Oracle Corporation | company | [DEFERRED] |  |
| Microsoft Corporation | company | [DEFERRED] |  |
| SAP AG (later SAP SE) | company | [DEFERRED] |  |
| Andersen Consulting LLP (Accenture) | firm | [DEFERRED] |  |
| Intel Corporation | company | [DEFERRED] |  |
| Teradata Corporation | company | [DEFERRED] |  |

### Technologies Referenced (18)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| IBM RS/6000 | platform | ibm-corporation | growth | [DEFERRED] |
| IBM SP2 | platform | ibm-corporation | growth | [DEFERRED] |
| IBM DB2/6000 | application | ibm-corporation | growth | [DEFERRED] |
| HP 9000 | platform | hewlett-packard | mature | [DEFERRED] |
| HP 3000 (MPE/iX) | platform | hewlett-packard | legacy-supported | [DEFERRED] |
| HP PA-RISC | platform | hewlett-packard | mature | [DEFERRED] |
| Digital AlphaServer / Alpha AXP | platform | digital-equipment-corporation | growth | [DEFERRED] |
| Digital VAX | platform | digital-equipment-corporation | legacy | [DEFERRED] |
| Sun SPARCcenter 2000 / SPARCserver 1000 | platform | sun-microsystems | growth | [DEFERRED] |
| Sun UltraSPARC | platform | sun-microsystems | emerging | [DEFERRED] |
| NCR WorldMark | platform | ncr-corporation | mature | [DEFERRED] |
| NCR TopEnd (Open OLTP) | application | ncr-corporation | growth | [DEFERRED] |
| Teradata (data warehouse) | application | teradata | mature | [DEFERRED] |
| Microsoft Windows NT | platform | microsoft-corporation | growth | [DEFERRED] |
| UNIX (System V.4) | platform | (multi) | mature | [DEFERRED] |
| Relational Database Management System | application | (multi) | mature | [DEFERRED] |
| Online Transaction Processing | application | (multi) | mature | [DEFERRED] |
| Intel Pentium Pro (P6) | platform | intel-corporation | emerging | [DEFERRED] |

### Observation Summary

- Total observations: 41
- By type: market-data: 17, competitive-assessment: 14, viability-prediction: 4, actual-outcome: 4, framework-component: 1, strategy-assessment: 1
