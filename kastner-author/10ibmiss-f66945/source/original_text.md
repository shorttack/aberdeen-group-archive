# Ten Issues for IBM Mainframe MIS Executives

> Archived from: 10IBMiss.docx
> Original publication date: 1991-01-01
> Author: Peter S. Kastner

---

## Original Document Text

Ten Issues for IBM Mainframe MIS Executives
Preface
MIS executives responsible for IBM mainframe systems are under considerable pressure today. Their corporate management superiors are demanding lower MIS costs to be accompanied by higher returns on MIS assets, and faster reactions by MIS to meet changing business needs.
However, MIS management at IBM mainframe sites has numerous technical constraints built into the System/390 architecture itself that are major obstacles to meeting corporate management's objectives for MIS. The foremost of these problems is coping with IBM's existing mainframe technology that is built around the major data processing requirement of the mid-1960s - batch processing.
An equally difficult management area for MIS managers is making the right choices among planning options from IBM's many different, often conflicting technologies. While IBM has announced its intentions to change its core technologies over the next several years, it has not published technology white papers, as it had done in the past, to define the direction of these changes. This does not help MIS executives who are accustomed to working under a 5-7 year planning horizon with IBM. As a result, MIS executives with IBM mainframe responsibility are severely handicapped in their ability to manage and plan the future of their data centers to corporate management's satisfaction.
This section examines a prioritized list of ten technology-related issues which IBM mainframe-site MIS executives will be facing over the next two years. These ten issues have an enormous financial impact on the typical mainframe MIS organization, and are creating significant interest in non-IBM alternative solutions such as those offered by Hewlett-Packard.
As the following discussion will detail, IBM's mainframe customers are becoming increasingly restless due to the continuing high labor costs needed to support mainframes, and disappointed at IBM's repeated inability to effectively deliver production-quality products from widely publicized architectural initiatives such as SAA (Systems Application Architecture), OfficeVision for enterprise office automation, DB2 for SQL-based relational database applications, and AD/Cycle software development methodology and tools.
The ten technology-related issues examined in detail are:
1) IBM's multilayer systems software architecture;
2) Annual upgrade/conversion cycles;
3) DB2 and production databases;
4) SNA and standards-based networking;
5) OfficeVision and IBM office automation in the 1990s;
6) AD/Cycle and applications development;
7) SNA network and systems complex management;
8) Client/server production systems;
9) SAA-based planning;
10) Changing jobs and organizational structures.
A Multilayer Architecture
The System/390 carries many layers of software baggage accumulated since it was introduced as the System/360 in 1964. Based on a 1960s design as a general-purpose batch processor, today's System/390 has gradually had multiple layers of systems software added which allowed it to evolve to cope with a 1990s-style workload that also includes online transaction processing, development timesharing, ad hoc query, and office automation.
A ratio of one systems programmer (at an average of $80,000-$90,000 per year fully burdened cost) per two mainframe MIPS is typical - meaning large sites with multiple mainframes can have over 100 highly trained (and compensated) systems programmers on staff. This translates to a systems programmer labor cost alone approaching $10 million at large sites, ranging down to a floor of about $250K at the smallest MVS sites.
Entry costs are formidable. Users report that their internal costs of migrating systems software and applications up to the MVS/Enterprise System Architecture (ESA) from IBM's smaller mainframe operating systems such as DOS/VSE to be at least $1.5 million - plus up to an equal amount for the IBM software licenses.
IBM mainframe sites often require multiple operating systems. Costs from running VM/SPF alongside MVS can easily exceed $250,000 per year.
Each new IBM system software product must be customized for each mainframe through a sysgen process. Many mainframe sites reserve up to 600 hours per year of mainframe downtime for the purposes of sysgen, installation, and reconfiguration.
For production crash-recovery reasons, multiple versions of IBM systems software products are stored on disk. The result is incremental costs that can range from $100,000 to $200,000 per year per mainframe.
IBM mainframe systems management and operations costs are at least twice those of even the highest priced mainframe alternative systems.
The annual cost of leased IBM system software on a typical mainframe often exceeds $1 million.
The September 1990 introduction of the ES/9000 models of the System/390 introduced the Sysplex cluster, ESCON storage architecture, and new releases of the MVS mainframe operating system and DB2 database.
IBM mainframe application programmers require two years of on-the-job training (costing the employer approximately $100,000) for a computer science college graduate to begin to be a productive programmer.
Most IBM MIS shops report that programmer labor costs just to maintain existing systems - not to develop new applications - consume 65%-80% of their annual data processing expense budgets.
Annual Upgrade/Conversion Cycles
IBM's mainframe product line has very fine granularity (different mainframe models may vary in CPU performance by only 15%) in order to allow IBM and its customers to plan an alternating CPU and DASD annual upgrade.
IBM upgrades are packaged and priced to continuously encourage upgrades and to charge a relatively high penalty for customers that skip an upgrade cycle.
The mainframe is upgraded at a million-dollar-plus cost in some fashion every year, and every four or five years there is a major replacement of the mainframe.
IBM software license fees are based on CPU power, and they can exceed $250,000 - per product.
DB2 and Production Database for the 1990s
DB2's performance with real-world production applications is inadequate compared with applications previously written for IBM's VSAM or IMS.
The MIS rule-of-thumb is 1-2 MIPS per RDBMS user as a planning guideline. At $100,000 per IBM mainframe MIPS, DB2 is obviously not for small budgets.
MIS has three choices: Pay IBM the costs in upgrades ($100,000-$200,000 per active online user), Delay an application migration to DB2, or Choose an alternative from Computer Associates or Software AG ($250,000-$500,000) or Teradata ($1 million per typical system).
IBM canceled a project which would have provided a migration path for IMS hierarchical database applications to its DB2 relational database. Costs for migration are estimated at $200,000 to several million dollars.
SNA and Standards-based Networking
IBM provides LU6.2 (SNA Logical Unit 6.2) tools for peer-to-peer communications. The SNA communications coding of complex applications can easily consume over 30% of all coding costs - and be the source of 50% of all coding errors.
OfficeVision: IBM Office Automation in the 1990s
OfficeVision is still not production quality some two-plus years after introduction in May 1989. The initial capital cost per OfficeVision user is approximately $8,000 for an appropriately configured PS/2 and an additional $4,000 for incremental mainframe resource upgrades, totaling $12,000 per user.
AD/Cycle: Applications Development
AD/Cycle, announced in June 1990, describes a framework for moving application development software from the IBM mainframe onto fully-loaded, LAN-connected PS/2s running OS/2 (typically $15,000 each without development software). The PS/2s must still be connected to a System/390 mainframe with MVS and DB2 (typically a $5 million-and-up investment).
For a $10 million System/390 installation, 10%-25% of prime-shift machine cycles on programmer development translates to $1 million-$2.5 million devoted to application development and maintenance.
The hard-dollar cost to displace an IBM-mainframe programmer is at least $40,000.
SAA-Based Planning
SAA was announced in 1987 as an umbrella vision for allowing interoperability across IBM's many incompatible hardware and software platforms. Even with 30,000 IBM programmers working on SAA, the definitions and products for most of IBM's SAA vision still do not exist some four years after IBM's announcement.
Client/Server Production Systems
IBM is not expected to deliver the ability to read and update multiple remote databases until the end of 1993.
The worldwide data processing costs for programming and testing alone to migrate legacy applications from the mainframe to client-server is estimated to be at least $200 billion.
Changing Jobs and Organizational Structures
The hard-dollar cost to displace an IBM-mainframe programmer is at least $40,000, more when the function goes away but the position is not eliminated.


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | 10ibmiss-f66945 |
| title | Ten Issues for IBM Mainframe MIS Executives |
| author | Peter S. Kastner |
| date | 1991-01-01 |
| type | white-paper |
| subject_domain | mainframe-computing, enterprise-IT-management |
| methodology | industry-analysis, expert-opinion, competitive-analysis |
| source_file | 10IBMiss.docx |
| license | CC-BY-4.0 |

### Abstract

This white paper identifies ten prioritized technology-related issues facing IBM mainframe MIS executives in the early 1990s, arguing that System/390 architecture constraints—rooted in 1960s batch-processing design—severely hamper cost reduction and agility demanded by corporate management. Kastner contends that IBM's failure to publish clear technology roadmaps leaves MIS planners in the dark, and that rising support costs and architectural limitations are driving mainframe customers to consider non-IBM alternatives such as Hewlett-Packard.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | An influential analyst opinion piece that crystallized the mainstream IT industry's growing disenchantment with IBM mainframes at a pivotal moment in computing history, helping accelerate the shift to open, distributed systems. |
| **Relevance** | medium | The specific IBM System/390 issues are largely historical, but the framework for evaluating legacy-platform lock-in and architectural debt remains instructive for enterprise IT decision-makers today. |
| **Prescience** | high | Kastner's prediction that IBM mainframe dominance would erode under cost and architectural pressures proved accurate; the 1990s saw a massive migration to distributed and open systems, and IBM was eventually forced to dramatically reinvent its mainframe value proposition. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (8)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| IBM | company | active |  |
| Hewlett-Packard | company | split |  |
| Aberdeen Group | firm | acquired |  |
| Peter S. Kastner | person | active |  |
| Computer Associates (CA) | company | renamed |  |
| Amdahl Corporation | company | unknown | Fujitsu (wholly owned subsidiary 1997 for $878M); exited mainframes 2000 |
| Hitachi Data Systems | company | unknown | Hitachi Vantara (2017) |
| Lotus Development Corp. | company | unknown | IBM (acquired 1995 for $3.5B) |

### Technologies Referenced (17)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| IBM MVS | operating-system |  |  | evolved |
| IBM CICS TP Monitor | platform |  |  | active |
| IBM DB2 | application |  |  | active |
| IBM VSAM | application |  |  | legacy-supported |
| IBM IMS | application |  |  | active |
| IBM OS/390 | platform |  |  | discontinued |
| IBM z/OS (Mainframe OS) | platform |  |  | active |
| IBM zSeries Mainframe | hardware |  |  | active |
| IBM Mainframe Assembler Code | language |  |  | legacy-supported |
| Client-Server Architecture | framework |  |  | legacy |
| IBM AS/400 | platform |  |  | legacy-supported |
| IBM 4300 Series | platform |  |  | legacy |
| Relational Database (RDBMS) | application |  |  | current |
| Online Transaction Processing | application |  |  | current |
| IBM SNA (Systems Network Architecture) | protocol |  |  | legacy-supported |
| IBM SAA (Systems Application Architecture) | framework |  |  | discontinued |
| IBM ESCON (Enterprise System Connection) | hardware |  |  | discontinued |

### Observation Summary

- Total observations: 30
- By type: : 30
