# U.S. Insurance Industry Overview

> Archived from: SAGNAI-1.pptx
> Original publication date: 1998
> Author: Peter S. Kastner (Chief Research Officer, Aberdeen Group)

---

## Original Document Text

# SAGNAI-1

*Source: SAGNAI-1.pptx — 18 slides*

## Slide 1: U.S. Insurance Industry Overview

U.S. Insurance Industry Overview
Peter S. KastnerChief Research OfficerAberdeen Group, Inc.Boston, Massachusetts(617) 723-7890

## Slide 2: Agenda

Agenda
Market Segmentation
Business Drivers
Industry Trends
Technology in Insurance
Attractiveness to SAGA
2
(c) Aberdeen Group, Inc.

## Slide 3: Market Segmentation

Market Segmentation
Property & Casualty
  - Home, business, liability, interruption
  - $260B in premiums
  - All consumers and businesses are customers
Life & Health
  - Life and health insurance
  - $330B in premiums
  - Personal and group are major sub-segments
  - 80%+ of businesses and consumers are customers
3
(c) Aberdeen Group, Inc.

## Slide 4: Business Drivers

Business Drivers
Erosion of profitability due to competition and poor actuarial planning
  - Breakdown in traditional business relationships, driving many to seek “lowest price” — commodity products
  - Lack of product and service differentiation
  - Relative disadvantage in consumer face-time
  - Bad bets placed on coastal real estate, longevity, HMO savings
High expense ratios, slowing growth, market-share challenges, M&A
4
(c) Aberdeen Group, Inc.

## Slide 5: Business Drivers

Business Drivers
Customer Service
  - A huge cost-center opportunity for $$$ savings
  - A means of differentiation (e.g., 24x7, drive-in, etc.)
Government regulation
  - 50 states plus federal = high cost to enter market
Complicated, multi-tier selling and service delivery schemes are traditional
  - Agencies
  - Group plan administration
5
(c) Aberdeen Group, Inc.

## Slide 6: Industry Trends

Industry Trends
Financial Disintermediation
  - “Why not buy insurance from … a bank”
  - Or over the Internet from the lowest-cost bidder
  - The Citibank/Travellers merger was not an aberration
Year 2000 Creates Supply-Chain Opportunities
  - Safe HQ but failing agencies?
6
(c) Aberdeen Group, Inc.

## Slide 7: Industry Trends

Industry Trends
Health Care Remains a Wild Card
  - Managed care will become more regulated by politicians
  - Nationalized system unlikely
  - Result:  be prepared for rapid systems change
Electronic Commerce Proliferates
  - supplier-to-consumer
  - business-to-business
  - supplier-to-intermediary
7
(c) Aberdeen Group, Inc.

## Slide 8: Technology in Insurance

Technology in Insurance
Architecture
  - Mainframe tradition for OLTP and batch
  - Agency systems are moving towards NT
  - Multi-tier, geographically distributed systems are the norm
Interface: almost all human-to-computer [unlike POS and ATM special terminals in retail and banking]
8
(c) Aberdeen Group, Inc.

## Slide 9: Technology in Insurance

Technology in Insurance
Vast Data Requirements
  - Underwriting
  - Actuarial
  - Claims
  - Regulatory
Data Warehousing is a natural, growing fast
9
(c) Aberdeen Group, Inc.

## Slide 10: Technology in Insurance

Technology in Insurance
Computing Styles
  - Large volumes dictate mature software
  - Complicated transactions (volumes vary by segment)
  - Client-server in local offices for speed.  Perhaps a local database
Complex data (e.g., ORDBMS) slow to take off
  - Imaging also slow uptake due to costs.  Is changing due to cheap digital cameras and printers.
10
(c) Aberdeen Group, Inc.

## Slide 11: Technology Problem Example

Technology Problem Example
Large, for-profit insurance company with huge investment in mainframe systems
Slow information turnaround due to batch orientation and lack of a data warehouse
Under market pressure to make casualty claims decisions faster in 500 local offices.  Walk-up claim resolution is the business goal.
But fraud checking and cost-comparison data must be kept at headquarters
11
(c) Aberdeen Group, Inc.

## Slide 12: 3-Tier Application Example:Insurance Claims

3-Tier Application Example:Insurance Claims
Unix or NT cluster
Highly Parallel, Scaleable
8,000 users at 500 offices and headquarters
Local transaction processing against a replicated database
Data Warehouse
PC desktops and Intel/Risc Office Server
Economical, Scaleable15-500 Users
5,000 Users
OLTP ProductionSystem &Admin.

> **Notes:** A real-world insurance company and Aberdeen client is planning a next generation claims processing system.  Any customer can stop in any office for complete support.  Claims can be updated from any local office.
A server at HQ will manage 3,500 HQ users, systems management, and batch.
.

## Slide 13: 3-Tier Application Example:Information Flow

3-Tier Application Example:Information Flow
Data Warehouse Transformation & Replication
Transaction Pull
Replication to every office
Transaction Push
Database of RecordEnterprise Superserver
Java & HTML to Suppliers
Classic 2-Tier Client-Server

> **Notes:** Local servers in 50 offices are desired for fast, local response time.  Each office will have a complete copy of the active claims database.  Replication or transaction queuing will be used to pull every transaction from the local office to an “enterprise superserver” at headquarters which will serve as the database of record.  This superserver will service 3,500 HQ users, replicate (“push”) all transactions out to all offices, and drive data transformation onto a data warehouse server.
Supporting transactions from 5,000 remote users and 3,500 local users as well as push replication, batch, and data warehouse transformation duties demands considerable computing capacity -- beyond traditional SMP architectures and even many clusters.
What computing platform can handle this workload and still be able to grow with the projected 15%-20% annual business volume?

## Slide 14: Attractiveness to SAG NA: Positive

Attractiveness to SAG NA: Positive
Insurance is one of the “biggie” markets
  - Industry focus by IBM, HP, Sun, SAP, and Microsoft
  - Large, readily identifiable list of prospects.  Geographic distribution across the country.
Business drivers and trends are compelling rapid changes in it to support new business initiatives
Application issues are U.S-centric:  globalization does not matter much
14
(c) Aberdeen Group, Inc.

## Slide 15: Attractiveness to SAG NA: Positive

Attractiveness to SAG NA: Positive
Emergence of an electronic insurance supply chain is inevitable but will not happen over night
  - Yes, software solutions connecting insurers, agencies, reinsurers, etc. are high value
Major, long-standing appreciation of RAS, scalability, interoperability, security issues
Large volumes of complex data and business processes: difficult data management problems
Still a tendency to make rather than buy
15
(c) Aberdeen Group, Inc.

## Slide 16: Attractiveness to SAG NA: Negative

Attractiveness to SAG NA: Negative
Where does SAG fit among legacy and new-breed data management and middleware choices?
  - No new mainframe database managers
  - Fighting SQL Server/DCOM head on
New application projects typically involve $10 million to $200 million in costs (IT only part).  Take years to complete.  Outside integrators.
Middleware standard-based products are immature
Need for ISV support
16
(c) Aberdeen Group, Inc.

## Slide 17: Questions Insurers Will Ask

Questions Insurers Will Ask
Where has SOM been in operation for a year at an insurance company?
How could SOM possibly be plug-and-play into my legacy applications?  That’s ridiculous.
I cannot afford the [network bandwidth/security/ response time penalty/etc.] of SOM.
I only deal with six [five, ten] strategic suppliers and SAGA is not on the list.
What makes you think that SAGA can out middleware IBM and Microsoft?
17
(c) Aberdeen Group, Inc.

## Slide 18: Partner Possibilities

Partner Possibilities
Property & Casualty
  - Agena			PRC
  - AMS			Allenbrook
  - Applied			PMSC
Life
  - Continuum			Cybertek
  - FDP			EZ Data
  - Sterling Wentworth		ECTA
Integrators
  - Andersen			EDS
  - Deloitte & Touche		MCI SHL
18
(c) Aberdeen Group, Inc.


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | 199x-us-insurance-industry-overview-saga-6ce857 |
| title | U.S. Insurance Industry Overview |
| author | Peter S. Kastner (Chief Research Officer, Aberdeen Group) |
| date | 1998 |
| type | market-study |
| subject_domain | insurance-IT |
| methodology | industry-analysis, market-segmentation, expert-opinion |
| source_file | SAGNAI-1.pptx |
| license | CC-BY-4.0 |

### Abstract

This presentation profiles the late-1990s U.S. insurance industry for Software AG's North American middleware business, combining market sizing, business drivers, industry trends, and an insurance claims architecture example. It argues that insurance offers a large but demanding opportunity for SAGA SOM because insurers face disintermediation, e-commerce, Y2K, and data-management pressures while remaining skeptical of immature middleware and new suppliers. Prepared circa 1998, the deck also proposes partner categories spanning insurance ISVs and integrators.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | The deck is a concise primary-source snapshot of how a major IT analyst framed insurance market structure, modernization pressures, and middleware go-to-market issues at the moment banks, the web, and enterprise integration were beginning to reshape the sector. |
| **Relevance** | high | It remains useful for understanding insurance IT architecture, distribution-channel change, and the practical objections enterprise buyers raise when evaluating new middleware platforms and ecosystem strategies. |
| **Prescience** | high | The presentation accurately anticipated bank-insurance convergence, internet distribution, e-commerce expansion, and the central role of data warehousing and scalable distributed architectures in insurance operations. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (26)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Software AG | company | [DEFERRED] | [DEFERRED] |
| Aberdeen Group | firm | [DEFERRED] | [DEFERRED] |
| Peter S. Kastner | person | [DEFERRED] | [DEFERRED] |
| IBM Corporation | company | [DEFERRED] | [DEFERRED] |
| Hewlett-Packard Company | company | [DEFERRED] | [DEFERRED] |
| Sun Microsystems Inc. | company | [DEFERRED] | [DEFERRED] |
| SAP AG | company | [DEFERRED] | [DEFERRED] |
| Microsoft Corporation | company | [DEFERRED] | [DEFERRED] |
| Citibank | company | [DEFERRED] | [DEFERRED] |
| Travelers | company | [DEFERRED] | [DEFERRED] |
| Agena | company | [DEFERRED] | [DEFERRED] |
| AMS | company | [DEFERRED] | [DEFERRED] |
| Applied Systems | company | [DEFERRED] | [DEFERRED] |
| PRC | company | [DEFERRED] | [DEFERRED] |
| Allenbrook | company | [DEFERRED] | [DEFERRED] |
| PMSC | company | [DEFERRED] | [DEFERRED] |
| Continuum | company | [DEFERRED] | [DEFERRED] |
| Cybertek | company | [DEFERRED] | [DEFERRED] |
| FDP | company | [DEFERRED] | [DEFERRED] |
| EZ Data | company | [DEFERRED] | [DEFERRED] |
| Sterling Wentworth | company | [DEFERRED] | [DEFERRED] |
| ECTA | company | [DEFERRED] | [DEFERRED] |
| Andersen Consulting LLP | firm | [DEFERRED] | [DEFERRED] |
| Deloitte & Touche | firm | [DEFERRED] | [DEFERRED] |
| Electronic Data Systems (EDS) | company | [DEFERRED] | [DEFERRED] |
| MCI SHL | company | [DEFERRED] | [DEFERRED] |

### Technologies Referenced (11)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| SAGA SOM (middleware) | framework | software-ag | emerging | legacy |
| Microsoft Windows NT | platform | microsoft-corporation | growing | legacy |
| Microsoft SQL Server | application | microsoft-corporation | growing | active |
| Microsoft DCOM | protocol | microsoft-corporation | emerging | legacy |
| Data warehousing | application | (multi) | growing | mainstream |
| Online Transaction Processing | application | (multi) | mature | mainstream |
| Object-Relational DBMS | application | (multi) | emerging | niche |
| Cluster architecture | platform | (multi) | growing | mainstream |
| SAP R/3 | application | sap-ag | growing | legacy-supported |
| Internet / World Wide Web | protocol | (standard) | emerging | mainstream |
| Imaging technology | application | (multi) | early-adoption | mainstream |

### Observation Summary

- Total observations: 40
- By type: architecture-analysis: 12, competitive-strategy: 10, topic-insight: 7, risk: 5, expert-opinion: 4, market-data: 2
