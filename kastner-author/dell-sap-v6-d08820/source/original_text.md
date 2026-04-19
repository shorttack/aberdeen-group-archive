# Dell, Oracle & Linux: Your Next SAP Platform? A Major EBA Replacement Cycle is Underway

> Archived from: Dell-SAP-v6.doc
> Original publication date: 2004-05-01
> Author: Peter S. Kastner (Executive Vice President, Technology Research, Aberdeen Group)

---

## Original Document Text

Dell, Oracle & Linux: Your Next SAP Platform?
A Major EBA Replacement Cycle is Underway
Ten years ago, Aberdeen was researching how a new generation of Intel-based servers running Microsoft Windows NT could support SAP’s R/3 ERP and financial EBA for small and medium (SMB) businesses.  That infrastructure platform worked fine to a point, but larger enterprises bought literally thousands of RISC-Unix platforms because these had a more mature hardware and operating system base, and had the performance metrics to support large-company workloads.  What Global 5000 companies did not like, but had to swallow and accept, was the high cost of those RISC-Unix platforms and the services needed to install, tune, and operate them.
Aberdeen estimates there are over 10,000 EBA RISC-Unix systems of the Y2K generation.  These worn-out systems have now reached a point of technology obsolescence and are up for replacement.  Basically, the entire IT system needs replacing because all the locked-down hardware, software, and application are increasingly out of step with 21st century architecture, standards and business processes.  They lack support for storage SANs, recent security improvements, XML, .Net, J2EE, WebSphere and the business process improvements in compliance, sourcing and supply chain developed over the past five years.  Software suppliers are increasingly making it clear they cannot support older versions forever.  These EBA platforms are beyond their useful technology life as the integrated mission-critical core of enterprise business processes, a key source of cost containment and business-value generation.  With the recession mentality a memory, Aberdeen research says 2004 will be a banner year for EBA replacement decisions.
Dell’s EBA Platform Infrastructure Approach Breaks Several Molds
The announcement by Dell and SAP on April 28th is significant.  We examine it from several angles: the facts, the architecture, the services delivery, and the IT value chain. 

What Dell and SAP Announced
Dell and SAP have a shared vision that future enterprise computing should be built on standards-based building blocks that scale as a business grows and flexes.  These building blocks will run composite applications, which deliver business value to customer- and supply-chain partners and which interface to custom applications and interfaces through standards such as XML and Java.  In product terms, the vision means Dell’s Intel-based servers, storage, Oracle’s database, a choice of Windows or Linux, and SAP’s mySAP or R/3 Enterprise applications built on SAP’s NetWeaver architecture.

Dell supplies pre-configured clustered servers, storage and backup, switches, Windows 2003 or Linux operating system, Oracle 9i RAC or 10g database, and a menu of planning, installation and tuning services, including database migration and a new application migration service. The customer has a single point of contact and cuts a single purchase-order to Dell for the IT infrastructure.  SAP licenses its latest mySAP or R/3 Enterprise applications running on the NetWeaver infrastructure.  Both partners will coordinate if a systems integrator is used in larger migrations, as well as post-installation support for any system or application issue.

Dell revealed it now has over 5,000 SAP customer installations in 60 countries.  There are three Dell-SAP competency centers in the U.S., Europe, and Japan.  The experience gained over several years working with customers, service partners, and SAP has, in the now famous Dell fashion, been honed to a cost-cutting, value-delivery proposition.  Dell’s Oracle-reseller business experience also plays an important role in giving the company confidence it can meet and exceed customer expectations.
The New Building-Block Architecture
The 1990’s saw the evolution and maturity of two significant computer architectures: symmetric multiprocessors (SMP); and high-availability clusters.  In SMP, lots of processors share a copy of the operating system.  Scalability typically declines as more processors are added due to parasitic resource contention, which can be somewhat reduced with expensive technology.  The current generation of EBA systems invariably has a large, expensive SMP server with attached storage handling the single instance of the EBA database.  In contrast, Dell’s cluster computing uses inexpensive but powerful servers with 2-4 processors per node, each of which efficiently handles a portion of the computing problem.  Typically, clusters add mission-critical application resiliency since a cluster can keep running even if a server fails, and can failback on recovery.

Dell has focused on the technology to successfully bring economical industry-standard clusters to market.  The key ingredients:
2-way to 4-way server building block with Intel Xeon microprocessors
Clustering technology in Oracle’s 9i RAC and 10g database that spreads the work over multiple servers — 4 x 4-way SAP solutions are Dell tested and validated to date.  The shared-nothing architecture is resource efficient and scales well 
High-availability — a minimum of 2 server nodes is necessary to achieve server backup with failover should a node crash
2-way front-end servers for client dialog and application processing
Linux gains needed robustness with Oracle managing the data.  Windows Server 2003 is a competent option.
A Dell|EMC storage area network (SAN) that supports high availability, remote mirroring, and storage consolidation, along with the requisite switches, tape backup/recovery hardware and software.
With Oracle Real Application Clusters, Dell’s 2- or 4-way Linux servers are scaleable building blocks for next-generation EBA systems at Global 5000 enterprises.  This architectural option was just not feasible until now, and it works.  In SAP’s widely used Sales and Distribution (SD) performance test, a two-node cluster of Dell 6650 4-way servers had about 9% to 16% better performance than 8-way RISC, Xeon, and Itanium SMP competitors for as little as one-third the cost.
SAP’s architecture is called NetWeaver, a web services-based application platform that integrates applications while providing extensibility with industry de facto standards such as Microsoft’s .Net, Sun’s J2EE, and IBM’s WebSphere.  In short, SAP applications are much easier to integrate with other enterprise applications and processes, eliminating much of the enterprise application integration (EAI) cost that accompanied the predecessor architecture.  NetWeaver is a software layer below the SAP solutions —mySAP, and R/3 Enterprise.   
Services Make an Attractive Difference
Dell’s competitors often deride the company as lacking an understanding of what services customers want.  That is a myth, Aberdeen research shows.  Dell is growing faster than the industry, customers tell us, because the company packages the services most needed and wanted.  Professional and managed services tripled at Dell in FY2003.
The Dell-SAP offering, following on to the Dell-Oracle bundle of hardware, database software, and services, brings the comfort and risk avoidance of a managed installation.
Dell and SAP configurations are certified, with predictable performance.  Typical Dell services for existing SAP customers include:
Pre-sales sizing and technical consulting
SAP on Dell migration assessment
SAP on Dell migration
Performance tuning
While SAP-on-Intel has largely been on the Microsoft Windows OS, Unix-to-Linux is the typical path chosen by RISC hardware users. Dell offers Unix migration services to move customers off RISC-Unix servers.  
For a small customer, Dell has “prime contractor” project management and deployment services for the infrastructure installation.  For larger customers, the Dell-SAP partnership will work with systems integrators on a total migration plan.  Dell will sign multi-year support contracts on the infrastructure it sells.
In a technical support partnership, Dell and SAP coordinate issues and escalation related to a Dell-SAP installation with improved processes.  This approach should eliminate the likelihood of vendor finger-pointing that drives IT operations executives’ crazy.
Strengthening the IT Value Chain
The Dell-SAP announcement deserves consideration by IT and business executives for a number of sound reasons:
RISC-Unix customers now have a viable, low-risk migration path for both the IT platform and services to do it.  The result is a modern, lower cost, industry-standard infrastructure without sacrificing performance or growth headroom.
Displacing the hardware and software maintenance costs of existing large SMP servers may even pay for the new infrastructure: today’s faster Intel processors can mean fewer per-processor software license charges, for instance.
Dell’s architecture is a cluster of SMP building blocks, which allows Oracle’s database to handle hardware and OS failover.  This is necessary in business-critical systems but a cost-doubler in other architectures.  
The architecture for the first time makes Linux robust enough to run enterprise mission-critical applications with low disruption risk.
The architecture scales efficiently.  It is running Dell Inc.and Oracle Corp., to name two large enterprises.  
Intel-based 2-way or 4-way Xeon servers have zero technology risk, excellent performance and price-performance — and a credible path upwards with Itanium and, shortly, 64-bit Xeon.
SAP NetWeaver is open to standards-based integration, lowering EAI development and maintenance costs, while not impeding the development of business process customization that leads to competitive advantage and differentiation.
The new Dell-SAP technology base will reduce operations costs, provide growth flexibility and scalability, and use shared resources efficiently.
Aberdeen Conclusions
While Unix is not dead, this announcement puts another nail in the coffin.  Linux clusters have arrived for mission-critical EBA applications. That’s not hype:  Dell and SAP are using their collective resources to make their customers successful.
RISC-based servers are not dead either, but 5+-year old large SAP systems are definitely due for a technology refresh.  Dell will earn a fair share of that replacement business, with some going to Linux and some to Windows.
The performance numbers are typical for Dell: 9%-16% better performance for as little as one-third the cost.  This fact alone continues to drive value-oriented large and small enterprise customers to Dell’s increasing market share. 
The migration process is honed and repeatable based on experience at over 5,000 Dell/SAP installations — lowering business risks and hastening ROI.
The pre-planned installation of the Dell-SAP offering reduces time, risk, complexity, paperwork, and vendors to manage.  Mid-size businesses, which have fewer on-staff resources than their larger-enterprise cousins, should be particularly interested in this announcement for the obvious potential benefits.  The one-phone-call post-installation support program is also attractive.
SAP has to date been a server Switzerland, neutral to all comers.  After 5,000 installations, SAP is giving a nod to Dell.  If the two partners working together can deliver a new world-class service and support model, then customers will benefit from a more efficient, cost-reduced delivery of support and upgrades, with lower integration risks.
Should Dell, Oracle, and Linux be you next SAP platform?  The proof points behind this announcement make it a question worth serious evaluation.
 

 Perspective Abstract:

Keywords: Dell, SAP, R/3, NetWeaver, mySAP, ERP, enterprise resource planning, Linux, Oracle, Microsoft, EBA, RISC, Unix, servers, platforms, IT services, architecture, obsolescence, SMB, enterprise business applications, Enterprise Business Application, infrastructure

Dell, Oracle & Linux: Your Next SAP Platform?
	
Dell and SAP have quietly built expertise and a close working relationship at over 5,000 sites.  Now, bolstered by its Oracle database integration experience, Dell is offering customers a managed infrastructure installation and migration to go with SAP’s latest ERP infrastructure, NetWeaver, and enterprise business applications including financials and enterprise resource planning applications.  Dell's offer has two key attributes: a scale-out clustered system with high availability and failover, and services that make it easy for customers to migrate their SAP environment, including database, thus removing barriers to achieving the cost and performance benefits of industry-standard servers. 

- Peter Kastner, Executive Vice President, Technology Research

Issue@Hand | 
Thousands of older enterprise business application (EBA) systems are reaching obsolescence.  How should the business value of a next-generation platform be evaluated? | Thousands of older enterprise business application (EBA) systems are reaching obsolescence.  How should the business value of a next-generation platform be evaluated?
Aberdeen Perspective | 
Synopsis | 
Dell has quietly built expertise at over 5,000 SAP sites.  Now, bolstered by its Oracle database integration experience, Dell is offering customers worldwide a hardware, software, and services bundle to go with SAP’s latest EBA infrastructure and applications. Dell's offer has two key attributes: a scale-out clustered system with high availability and failover, and services that make it easy for customers to migrate their SAP environment, including database, thus removing barriers to achieving the cost and performance benefits of industry-standard servers. And while Windows is offered, Linux will gain acceptance. | Dell has quietly built expertise at over 5,000 SAP sites.  Now, bolstered by its Oracle database integration experience, Dell is offering customers worldwide a hardware, software, and services bundle to go with SAP’s latest EBA infrastructure and applications. Dell's offer has two key attributes: a scale-out clustered system with high availability and failover, and services that make it easy for customers to migrate their SAP environment, including database, thus removing barriers to achieving the cost and performance benefits of industry-standard servers. And while Windows is offered, Linux will gain acceptance.

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | dell-sap-v6-d08820 |
| title | Dell, Oracle & Linux: Your Next SAP Platform? A Major EBA Replacement Cycle is Underway |
| author | Peter S. Kastner (Executive Vice President, Technology Research, Aberdeen Group) |
| date | 2004-05-01 |
| type | market-study |
| subject_domain | enterprise-business-applications |
| methodology | industry-analysis, competitive-profiling, expert-opinion, architecture-assessment |
| source_file | Dell-SAP-v6.doc |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Perspective on the April 28, 2004 Dell-SAP announcement. Argues that over 10,000 Y2K-generation RISC-Unix EBA systems are obsolete and ready for replacement, and positions the Dell/SAP/Oracle/Linux clustered-Intel stack (NetWeaver + mySAP/R3 + Oracle 9i RAC/10g + Dell|EMC SAN) as a lower-cost, standards-based successor. Notes a two-node Dell 6650 cluster delivered 9-16% better SD performance than 8-way RISC/Xeon/Itanium SMP at one-third the cost.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | One of the clearest early-2004 articulations of the 'Linux cluster + Oracle RAC + x86' alternative to RISC-Unix SMP for Tier-1 ERP; shaped buyer conversations during the 2004-2008 ERP refresh wave. |
| **Relevance** | high | Framework of industry-standard clusters displacing proprietary SMP is the template for today's cloud-native ERP (SAP HANA on cloud x86, S/4HANA on Linux); historical lens is directly applicable. |
| **Prescience** | high | Key predictions — Linux clusters ready for mission-critical EBA, RISC-Unix refresh to x86, NetWeaver as open integration layer — all materialized between 2004 and 2015. |

### Prescience Detail


**Prediction 1:** 2004-ebavreplacement-banner-year
- **Claimed:** 2004 will be a banner year for EBA replacement decisions.
- **Year:** 2004
- **Confidence at time:** high

**Prediction 2:** unix-nail-in-coffin
- **Claimed:** While Unix is not dead, this announcement puts another nail in the coffin. Linux clusters have arrived for mission-critical EBA applications.
- **Year:** 2004
- **Confidence at time:** high

**Actual Outcome 2:** unix-decline-outcome
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Placeholder.

**Prediction 3:** linux-mission-critical-readiness
- **Claimed:** The architecture for the first time makes Linux robust enough to run enterprise mission-critical applications with low disruption risk.
- **Year:** 2004
- **Confidence at time:** high

**Actual Outcome 3:** linux-mission-critical-outcome
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Placeholder.

**Prediction 4:** dell-market-share-gain
- **Claimed:** Dell will earn a fair share of RISC-Unix replacement business, some to Linux and some to Windows.
- **Year:** 2004
- **Confidence at time:** medium

**Actual Outcome 4:** dell-market-share-outcome
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Placeholder.


### Entities Referenced (10)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Dell Inc. | company | active |  |
| SAP AG | company | active |  |
| Oracle Corporation | company | active |  |
| Microsoft Corporation | company | active |  |
| IBM | company | active |  |
| Intel Corporation | company | active |  |
| EMC Corporation | company | acquired | Dell |
| Sun Microsystems | company | acquired | Oracle (2010) |
| Aberdeen Group | firm | acquired | Aberdeen/Harte-Hanks |
| Peter S. Kastner | person | active |  |

### Technologies Referenced (17)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| SAP R/3 Enterprise | application | SAP | mature | legacy |
| mySAP | application | SAP | mature | legacy |
| SAP NetWeaver | platform | SAP | emerging | legacy |
| Oracle 9i Real Application Clusters (RAC) | platform | Oracle | mature | legacy |
| Oracle Database 10g | platform | Oracle | emerging | legacy |
| Linux | platform | Open Source / Red Hat / SUSE | growing | active |
| Windows Server 2003 | platform | Microsoft | emerging | legacy |
| Intel Xeon | platform | Intel | mature | active |
| Intel Itanium | platform | Intel/HP | emerging | obsolete |
| RISC-Unix servers (generic) | platform | IBM / HP / Sun | mature | legacy |
| IBM WebSphere | platform | IBM | growing | active |
| J2EE (Java 2 Enterprise Edition) | framework | Sun Microsystems | mature | legacy |
| Microsoft .NET | framework | Microsoft | mature | active |
| XML | protocol | W3C | mature | active |
| Storage Area Network (SAN) | platform | Industry Standard | mature | active |
| Symmetric Multiprocessor (SMP) | platform | Multi-vendor | mature | legacy |
| Dell PowerEdge 6650 | platform | Dell | mature | obsolete |

### Observation Summary

- Total observations: 27
- By type: framework-factor: 6, expert-opinion: 5, market-data: 4, viability-prediction: 4, actual-outcome: 4, strategy-classification: 2, benchmark-result: 1, technology-assessment: 1
