# Moving Effectively To Next-Generation Client-Server Development

> Archived from: https://web.archive.org/web/19970112011022/http://www.aberdeen.com:80/secure/whtpaper/gupta/gupta.htm
> Original publication date: 1996-01-12
> Author: Aberdeen Group

---

## Original Document Text

### Preface

Inevitably, users are finding that their first-generation client-server development tools are topping out.

Aberdeen research shows that the choice of client-server application development environment (CADE) is strategically important to IS buyers, and mounts in importance with each implemented application. Rapid development and deployment of competitive-advantage, business-reengineering, and data-mining client-server applications now can deliver bottom-line value to an enterprise—or to its competitors.

However, the new opportunities opening before the CADE user mean new challenges for the toolset, both for new-application development and first-generation-solution upgrade. The new applications—such as data warehousing and the SAP/PeopleSoft-type application servers—are larger-scale, and require CADE technologies aimed at larger-scale solutions, such as server-side development, application partitioning, business modeling, design/deployment/maintenance support, and team programming.

To put it bluntly, **today's most popular client-server development toolsets have so far failed to meet the challenge fully.** Users report increasing numbers of cases in which they seek new toolsets despite strong corporate commitment to Microsoft's Visual Basic and Powersoft's PowerBuilder. These toolsets have not yet delivered the complete range of new scalability technology needed in many user situations.

Therefore, Aberdeen recommends that users immediately begin a two-pronged **"insurance strategy"**:

1. **Prong 1 (most vital):** Catalog new and existing applications likeliest to "top out" and identify one or several "straddle" CADEs providing the scalability to meet most needs and flexibility to provide least-cost migration
2. **Prong 2 (long-term):** Forecast largest-scale new applications and search out a very-high-end CADE with innovative scalability technologies for "toolset-busters"

---

### Section I: The Increasing Need For Next-Generation Client-Server Toolsets

**Problems of first-generation CADEs:**

1. **Process and culture scalability** — Communication problems between developers increase as the square of the number of programmers involved; first-gen CADEs provide little software for scaling the development process
2. **Application scalability** — Applications that run well on a departmental LAN slow drastically as users/database size increase; first-gen CADEs provide little application partitioning, query optimization, or load balancing
3. **Implementation costs and delays** — Absence of automated deployment/maintenance software requires physical installation at each site; users must physically redeploy and retrain at each upgrade
4. **Inability to adapt to architectural changes** — First-gen CADEs lack repositories and application-repartitioning GUIs for 3-tier and Intranet architectures
5. **Programmer productivity ceiling** — Complex applications require reversion to 4GL or 3GL scripting, losing productivity gains

**Next-gen CADE requirements:**
- Team-programming tools (version control, project management)
- Application partitioning for performance scalability
- Load balancing (via TP monitor)
- Query optimization technology
- Full-lifecycle support (automated deployment/maintenance)
- Full-featured repository
- Business modeling and component support

**The Visual Basic and PowerBuilder repository problem:**
- TI-Microsoft initiative shows no signs of finishing; only fruit is administrator-intensive "Arranger" tool
- Sybase/Powersoft committed to repository from recently acquired company but delivery date unclear
- Use of repository for next-gen technology even further off

**User strategies:** Audit production client-server applications, divide into "one small step" (significant modification) and "one giant leap" (major surgery) categories, then choose appropriate new toolset.

---

### Section II: What To Look For In Next-Generation Technology

This section uses Gupta's Centura as the primary example of a next-generation CADE.

**Centura consists of four major products:**
1. Centura Team Developer — core component-based CADE
2. Centura Ranger — data-replication
3. Centura Application Server — application partitioning (beta 2Q96)
4. Centura Web Data Publisher — Internet/Intranet data publishing

**Ease of Migration:**
Centura offers: full repository with import facilities, OLE 2.0 support, Windows/Windows 95/Motif GUI support, QuickObjects facility for "codeless" data-linked GUI applications.

**Team Programming:**
Centura: Team Object Manager + Team Object Repository + integrated PVCS version control + project/configuration management features.

**Components:**
OOP delivers average ~35% development speed improvement (per fragmentary studies) after 1+ year learning curve. Centura: full OOP support, "Easy Introduction to OOP", Visual Toolchest class library, Fast Object Compiler.

**Application Partitioning:**
Centura Application Server (beta 2Q96): drag-and-drop partitioning across 2-tier and 3-tier architectures; supports DCE, TCP/IP, Network OLE.

**Load Balancing:**
Centura supports Novell's Tuxedo TP monitor with Tuxedo Deployment Suite; middleware access to IBM CICS and Encina; 3-Tier Wizard simplifies TP programming.

**Query Optimization:**
Centura SAL: extensive database/gateway operations; Centura Ranger for heterogeneous replication across multiple vendors' databases; SQLBase (full RDBMS) and Quest data-access tool available.

**Full-Lifecycle Support:**
Design (Rational Rose, LogicWorks ERWin, Oracle/Sybase data-dictionary links), Programming/Testing (debugger, incremental compiler, third-party testing tool integration), Deployment (repository-based semi-automatic deployment), Maintenance (SQLConsole integration).

**Repository:**
Team Object Repository on standard RDBMSs (Sybase/Microsoft SQL Server); open to Oracle and Sybase metadata; Team Object Manager for search/access/administration.

**Business Modeling:**
Data Model Viewer; reverse engineering of business-model schemas from modeler, CASE tools, or RDBMS metadata.

**3+-Tier and Intranet:**
Internet QuickObjects for Web-enabled SQL data access; 3-Tier Wizard; Centura Web Data Server with firewall security; Java compilation planned for subsequent release.

---

### Section III: Business Benefits Of Moving To Next-Generation Technology

Next-generation CADE technology is a key tool in creating a short-term competitive-advantage and then turning it into a long-term core competency. User experiences show competitive advantages especially in:

- **Data-mining applications** — yields competitive insights increasing gross margin
- **Business-process reengineering applications** — decreases SG&A expenses
- **Customer-interface applications** — generates increased sales, closer customer relationships

Data warehouse growth rate: **6-7 times growth in database size over 18 months** in many cases.

---

### Section IV: Key Considerations In Making The Move

Aberdeen finds that effective CADE migration strategies include:

- Long-term technology plan anticipating enterprise-architecture stresses 2-3 years out
- Allocation of resources for migration with attention to ease-of-use, wizard training features, import facilities
- Built-in plan flexibility accounting for rapid pace of technology change

CADE technology is **not yet mature**: testing and maintenance not as well adapted to large-scale distributed development; Intranet requires new technology. Users should include in assessments of CADE suppliers consideration of underlying long-term technologies such as a full-featured repository.

---

### Section V: Available Solutions

CADE market taxonomy:

| Category | Vendors | Best For |
|----------|---------|----------|
| First-generation/departmental | Visual Basic, PowerBuilder, Delphi, SQLWindows | Departmental, simple, client-centric apps |
| Next-gen scaling first-gen | **Gupta Centura**, Symantec, Unify, Compuware Uniface | Scaling existing apps; new moderate-scale development |
| High-end from RDBMS suppliers | Oracle, Sybase, Informix, CA-Ingres, Progress | RDBMS-installed-base upgrading, data-intensive apps |
| Ultra-high-end CADE specialists | Forte, Dynasty, Seer Technologies | Very complex/data-intensive new apps, multi-DB |

---

### Section VI: Aberdeen Conclusions

The effective IS buyer will choose the right tool for the job. For large new projects and installed-base needs, a very-high-end CADE may be most effective; for scaling existing applications and developing new ones that do not require a large leap, **a next-generation CADE with long experience in the first-generation market and a solid repository foundation, such as Gupta's Centura, should be especially appropriate.**

Much of the next two years in CADE technology should be a matter of extending the basic foundation to cover object-relational RDBMSs, 3-tier architectures, and the Intranet. **Aberdeen recommends that IS buyers place next-generation CADE solutions such as Gupta's Centura on their short lists.**

---

*© Aberdeen Group, Inc. One Boston Place, Boston, Massachusetts 02108. Telephone: 617-723-7890. Copyright © 1996.*

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-moving-effectively-next-gen-client-server |
| title | Moving Effectively To Next-Generation Client-Server Development |
| author | Aberdeen Group |
| date | 1996-01-12 |
| type | white-paper |
| subject_domain | client-server-development-tools-CADE |
| methodology | industry-analysis, competitive-profiling, field-research, expert-opinion |
| source_file | 1996 Moving Effectively To Next-Generation Client-Server Development wp.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group white paper, sponsored by Gupta Technologies, argues that first-generation client-server application development environments (CADEs) such as Visual Basic and PowerBuilder are "topping out" and recommends immediate adoption of next-generation CADEs. The study provides a 7-factor evaluation framework for next-generation CADE selection and positions Gupta's Centura product as the leading choice.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Captured the mid-1990s transition from departmental to enterprise-scale client-server development, identifying limitations of Visual Basic and PowerBuilder. The CADE evaluation framework was substantive, though the vendor-sponsored nature limits independence. |
| **Relevance** | low | Specific products largely obsolete, but scalability challenges described (application partitioning, deployment automation, 3-tier architecture) directly anticipate modern cloud-native and microservices concerns. |
| **Prescience** | medium | Correctly predicted VB/PowerBuilder scalability constraints would drive toolset replacement. However, the winning solution was Java EE and .NET (not Centura/Gupta, acquired through multiple hands to OpenText by 2015). |

### Prescience Detail

**Prediction 1:** Prediction: Visual Basic and PowerBuilder users face serious scalability constraints
- **Claimed:** In short to medium term, users may have serious concerns about VB/PowerBuilder shops' ability to solve first-gen problems without new toolset
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 1:** Outcome: Visual Basic/PowerBuilder scalability constraints realized
- **Result:** PowerBuilder never achieved full-featured repository; VB evolved to VB.NET (2002) with significant breaking changes; both lost significant market share to Java and C# as Aberdeen predicted
- **Confidence:** verified
- **Notes:** Source: PowerBuilder Wikipedia (https://en.wikipedia.org/wiki/PowerBuilder). Aberdeen correctly identified the scalability problem but misjudged the solution.

**Prediction 2:** Prediction: Gupta Centura as leading next-gen CADE for migration
- **Claimed:** Aberdeen recommends Gupta Centura on short lists; builds on full-featured repository; especially appropriate for scaling existing apps
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 2:** Outcome: Gupta Technologies / Centura fate
- **Result:** Gupta renamed to Centura Software (1995); passed through investors (Warp Technology 2005, Unify 2006); acquired by OpenText 2015; Centura did not become dominant next-gen CADE
- **Confidence:** verified
- **Notes:** Source: Wikipedia/Gupta Technologies (https://en.wikipedia.org/wiki/Gupta_Technologies). Java EE and .NET emerged as dominant platforms instead.

### Entities Referenced (10)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Gupta Technologies | company | acquired | OpenText (2015) via Centura/Unify chain |
| Sybase/Powersoft (PowerBuilder) | company | acquired | SAP SE (2010, $5.8B) |
| Microsoft Corporation | company | active | — |
| Aberdeen Group, Inc. | firm | acquired | Aberdeen (Harte-Hanks / independent) |
| Texas Instruments (IEF) | company | active | IEF sold to Sterling Software 1997 |
| Rational Software | company | acquired | IBM (2003, $2.1B) |
| Borland International | company | active | Embarcadero (2008) → Idera (2016) |
| Oracle Corporation | company | active | — |
| Forte Software | company | acquired | Sun Microsystems (1999) |
| Symantec | company | active | Gen Digital (2022) |

### Technologies Referenced (8)

| Technology | Category | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|---------------------|---------------------|
| Gupta Centura | framework | emerging | obsolete |
| Gupta SQLWindows | framework | mature | obsolete |
| Microsoft Visual Basic | language | mature | active |
| Powersoft/Sybase PowerBuilder | framework | mature | active |
| 3-Tier Architecture | framework | emerging | active |
| TP Monitor (Tuxedo/Encina/CICS) | framework | mature | active |
| Java / Intranet | language | emerging | active |
| Data Warehousing | application | emerging | active |

### Observation Summary

- Total observations: 30
- By type: actual-outcome (4), benchmark-result (1), expert-opinion (0), framework-factor (7), market-data (2), strategy-classification (4), technology-assessment (5), viability-prediction (2), expert-opinion (5)
