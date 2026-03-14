# Bull's Sagister: Datacenter-Disciplined UNIX for Business-Critical Applications

> Archived from: https://web.archive.org/web/19970112011753/http://www.aberdeen.com:80/secure/profiles/bull_sag/bull_sag.htm
> Original publication date: 1996
> Author: Aberdeen Group

Bull Enterprise Information Systems
Rue Jean-Jaurès
78340 Les Clayes-sous-Bois, France
33 (1) 30 80 37 73

---

## Original Document Text

Bull Enterprise Information Systems division knows both datacenter operations and UNIX. With over 15 years of experience in implementing UNIX systems in its customers' operations, Bull has learned the strengths and weaknesses of UNIX-based applications running in conjunction with mainframe applications and the best practices required for prudently and effectively operating and managing a state-of-the-science datacenter. Bull has now packaged its hard-earned knowledge in a new product — Sagister. Aberdeen believes that after evaluating the benefits and functionality of Sagister, both senior information systems (IS) executives and their non-technical executive managers will agree that this is a "must-have" product for running production, bet-the-business, UNIX-based applications in the datacenter.

### Executive Summary

Datacenter managers are continuously being asked to meet two conflicting requirements by their enterprise managers and users. The first demand is that the datacenter must provide the enterprise with a new-generation of client-server, process-integrated applications to make the entire organization — whether it be a government agency, bank, manufacturing operation, service provider, university, or whatever — both more effective and efficient. The second is an insistence that the datacenter continue to follow mainframe-developed operational disciplines such as 7X24X365 availability, back-up of all data, security (only authorized individuals having access to designated data and programs), reliability (applications work as described and data does not become lost or corrupted), and low-operational costs. In the real world however, developers (both in-house and independent software vendors) of client-server applications typically do not have the time, resources, tools, and/or culture required to build mainframe-discipline functionality into their systems.

Bull has identified the need to bridge the gap between UNIX-based client-server applications and mainframe-discipline practices. More importantly, with its history of servicing datacenter needs for both mainframe and UNIX systems, and its leading-edge UNIX-technology competency, Bull believes that it is uniquely qualified to provide the products and support that can allow UNIX operations to have the same robustness that enterprise users have come to expect from mainframe-operating environments.

Bull is packaging the RISC/UNIX hardware, systems software, and support services that it has developed for mainframe-class datacenter UNIX operations under the product name Sagister. Sagister is packaged in 3 base configurations consisting of single or multi-node SMP (symmetric multiprocessing) systems based upon PowerPC technology and PowerScale architecture, and the Sagister Operations Base software.

Bull is investing in and positioning Sagister to significantly differentiate itself from IBM, Hewlett-Packard, Sun Microsystems, Digital Equipment Corporation, ICL/Fujitsu, Siemens, and NCR (formerly AT&T GIS) in the UNIX marketplace. Bull's commitment level to Sagister is high — it has assigned approximately 200 individuals to the project effort.

### Sagister: Packaging Best Practices For Enterprise Datacenters

The name Sagister is a combination of Sage, for wise, and Magister, the Latin word for teacher. Bull frequently describes Sagister as "the UNIX Multiframe."

Bull has designed Sagister to offer a completely open software system that customers and professional service organizations can customize to meet specific datacenter application and best-practice requirements. The architectural philosophy has been to take industry-standard, open systems components and add value to them from a systems basis while avoiding the invention of new, proprietary technology.

### Sagister Architecture

Sagister is built on a base of the following four major technology components:

1. **Escala** — Bull's industry-leading SMP, redundant and scalable clustered systems, incorporating the PowerPC RISC processor. Sagister hardware nodes consist of 6-8 processor systems;
2. **AIX 4.1** — the commercial UNIX operating system jointly developed by Bull and IBM that allows 10,000+ packaged applications to run on Sagister now;
3. **HACMP** — UNIX clustering technology developed by CLAM Associates, Cambridge, MA, for high availability and load balancing with AIX-based systems. Sagister incorporates the High Availability Subsystem (HAS) and Common Resource Manager (CRM) components of HACMP;
4. **ISM/OpenMaster** — Bull's standard network and system management framework tailored specifically to meet the demanding requirements of commercial datacenter managers.

### Sagister — The Base-level Product

The three standard Sagister configurations are:

1. **M1** — single 6-8 node system and the Sagister Operations Base software; supports up to 2,000 PC-based client users; suited for prototyping and development;
2. **M2** — two-node system with HAS; 12-16 processors supporting up to 3,000 PC-based client users; Aberdeen's recommended resilient production system;
3. **M3** — four-node system with high-speed FDDI interconnect; up to 32 PowerPC processors; supports up to 5,000 users; designed for very large databases.

The Sagister Operations Base software has four major components:

1. **Operational Graphic Interface (OGI)** — icon representation of all applications on one Dashboard screen;
2. **Command Wrapper & Execution (CWE)** — creates icons for systems and application commands without requiring UNIX command-line knowledge;
3. **Event Manager** — monitors messages and launches corrective actions/alarms when predefined conditions occur;
4. **Mainframe-class operational Tools** — including: Accounting, Alarm, Distributed Printing, EpochBackup, Extended Remote Service, IP Discovery, MIB Inventory, Monitor, OS Manager, Pager, Pilot, QueryBuilder, Remote Operation, Scheduler, Script, Software Distribution, System Performance, Trouble/ARS, User Management.

Bull believes, and Aberdeen agrees, that the use of the Operations Base will lower a datacenter's required support costs significantly while increasing systems overhead by less than 7%. On this basis alone Sagister can be cost justified with a greater than 50% return on investment (ROI) compared to alternative systems with their third-party add-on requirements.

### Function Sets

The optional Function Sets fall into four major categories:

**1. Production Facilities**
- **RDBMS Function Set** — enhances Oracle 7.2 with DB*Monitor, DBA Expert administrative tools, and Oracle Troubleshooting;
- **TP Function Set** — includes Tuxedo Manager, MicroFocus COBOL, high-availability scripts for transaction processing.

**2. Operations Facilities**
- **Security Function Set** — ISM/AccessMaster for centralized security; IP Firewall; Application Firewall (from Trusted Information Systems);
- **Multi-Server Function Set** — identifies, analyzes, and controls network activity;
- **LAN Management Function Set** — Transcend Enterprise Manager and Transcend NetBuilder for hub management;
- **Automation Function Set** — EpochMigration for automatic data archiving and hierarchical storage management;
- **Clustering Function Set** — concurrent resource management for M2.

**3. Integrated Applications**
- **SAP R/3 Function Set** — adds security, automated ops, high-availability, backup, event management to SAP R/3; planned general availability Q3 1996.

**4. Mainframe Support**
- **GCOS and MVS Link Function Sets** — based on Stella fast connection; application-to-application cooperative processing; FlowBus information brokerage.

### Sagister's Future

Version 2 scheduled for Q3 1996; two versions per year planned afterward. Future enhancements include:

- Support for 8-node clusters (currently 4); expanding to 16 and 32 by end of 1997;
- Up to 16 CPUs per system by end of 1997 (from current 8 CPUs max);
- Motorola PowerPC 620 64-bit processor in fall 1996;
- RDBMS Function Sets for Informix and Sybase;
- Additional Function Sets for BAAN, PeopleSoft, SAS, Oracle Applications;
- Potential Sagister software support on IBM RS/6000 and HP 9000 through partnerships.

### Bull Enterprise Information Systems Organization

Bull had 1995 revenues of FF 26,656M and a net profit of FF 306M — the first profit since 1988. This is evidence of Bull's continued seriousness about meeting its objective to become a financially stable IT supplier.

### Competitive Positioning

- **CA-Unicenter**: Similar operations functionality but lacks event management, HA, graphical command icons, and Function Sets;
- **IBM RS/6000 SP**: Lacks reliability, manageability, load balancing, availability, backup/restore, ease-of-administration of Sagister; designed for HPC not commercial datacenter;
- **HP MC/ServiceGuard + OpenView**: May have better clustering; but has not created Sagister's mainframe-class operational functionality; relies on partners;
- **DEC TruCluster + Oracle 7.3**: May provide highest throughput of any UNIX platform; but Digital has not developed datacenter operational capabilities.

### Aberdeen Conclusions and Observations

Bull's design philosophy and objectives for Sagister are on target for meeting enterprises' datacenter and production requirements for UNIX systems. The current functionality is correct and the future enhancements — especially MVS interoperability — promise to make Sagister a very viable UNIX platform for enterprises that are not currently Bull customers.

IS professionals consistently and accurately state that the UNIX operating environment is a step down from GCOS, MVS, VMS, VM, OS/400, MPE/iX and other proprietary operating environments in terms of manageability, reliability, availability and security. What Sagister does is provide IS professionals with the mainframe-discipline tools they need to maintain and operate UNIX-based applications to meet end-users' production-quality expectations.

For sophisticated, forward-thinking senior-level line and IS managers seeking to prudently manage and grow their enterprise's information infrastructure through the use of best practices, mainframe disciplines, and datacenter operations integration, Bull's Sagister is an important product introduction that deserves very serious consideration.

---

Aberdeen Group, Inc.
One Boston Place, Boston, Massachusetts 02108
Copyright © 1996 Aberdeen Group, Inc.

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-bulls-sagister-datacenterdisciplined-unix-businesscritical-applications |
| title | Bull's Sagister: Datacenter-Disciplined UNIX for Business-Critical Applications |
| author | Aberdeen Group |
| date | 1996-01-01 |
| type | market-study |
| subject_domain | UNIX-datacenter-management |
| methodology | industry-analysis, competitive-profiling, document-review, expert-opinion |
| source_file | 1996 Bull_s Sagister_ Datacenter-Disciplined UNIX for Business-Critical Applications pr.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group evaluates Groupe Bull's Sagister product, combining PowerPC-based RISC/UNIX systems with mainframe-discipline operational tooling. The study covers four architecture tiers, three hardware configurations (M1/M2/M3), optional Function Sets, and competitive analysis versus IBM RS/6000 SP, HP MC/ServiceGuard, DEC TruCluster, and CA-Unicenter.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Sagister addressed a real 1996 enterprise challenge — UNIX lacking mainframe-class operational discipline — that was widely debated; Bull was a smaller market player than IBM, HP, and Sun, limiting the study's reach. |
| **Relevance** | medium | The mainframe-discipline-applied-to-open-systems framework directly anticipates modern DevOps/SRE practices; specific hardware specs and vendors are dated. |
| **Prescience** | medium | Aberdeen correctly predicted the UNIX operational rigor market need; the broader thesis proved correct (met by ITIL, HP OpenView, IBM Tivoli). Bull's acquisition by Atos in 2014 limited Sagister's standalone market impact. |

### Prescience Detail

**Prediction 1:** Sagister future market viability
- **Claimed:** Sagister's design philosophy is on target; future MVS interoperability will make it viable for non-Bull enterprises
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 1:** Groupe Bull company fate
- **Result:** Bull acquired by Atos SE in October 2014 for €620M; Sagister discontinued well before acquisition as UNIX midrange market consolidated
- **Confidence:** verified
- **Notes:** Source: Bloomberg/Atos 2014; Bull never expanded Sagister to non-Bull customer base as predicted

---

**Prediction 2:** UNIX operational rigor market need
- **Claimed:** IS professionals consistently state UNIX is a step down from GCOS/MVS in manageability; Sagister fills this critical gap
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 2:** UNIX operational rigor market evolution
- **Result:** The broader need proved correct; met by ITIL frameworks, HP OpenView, IBM Tivoli, and eventually cloud-native ops (Kubernetes, Prometheus)
- **Confidence:** verified
- **Notes:** The thesis was correct; Sagister specifically did not win the market

### Entities Referenced (12)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Groupe Bull | company | acquired | Atos SE (2014) |
| Aberdeen Group, Inc. | firm | acquired | Harte-Hanks (2001) -> Informa (2019) |
| IBM Corporation | company | active | — |
| Hewlett-Packard | company | active | HP Inc + HPE (split 2015) |
| Digital Equipment Corporation | company | acquired | Compaq (1998) -> HP (2002) |
| Sun Microsystems | company | acquired | Oracle (2010) |
| Computer Associates | company | active | CA Technologies -> Broadcom (2018) |
| Oracle Corporation | company | active | — |
| CLAM Associates | company | unknown | — |
| NCR Corporation | company | active | — |
| ICL/Fujitsu | company | acquired | Fujitsu Technology Solutions |
| Siemens AG | company | active | — |

### Technologies Referenced (9)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|----------------------|---------------------|
| Sagister | platform | Bull | emerging | obsolete |
| Bull Escala | platform | Groupe Bull | mature | obsolete |
| AIX 4.1 | platform | IBM/Bull | mature | legacy-supported |
| HACMP | platform | CLAM Associates/IBM | mature | legacy-supported |
| ISM/OpenMaster | framework | Groupe Bull | mature | obsolete |
| SAP R/3 | application | SAP AG | emerging | legacy-supported |
| Oracle 7.2 | application | Oracle | mature | obsolete |
| IBM RS/6000 SP | platform | IBM | mature | obsolete |
| PowerPC 604 | platform | Motorola/IBM | mature | obsolete |

### Observation Summary

- Total observations: 25
- By type: strategy-classification (1), viability-prediction (2), actual-outcome (2), technology-assessment (7), benchmark-result (4), framework-factor (2), market-data (3), expert-opinion (4)
