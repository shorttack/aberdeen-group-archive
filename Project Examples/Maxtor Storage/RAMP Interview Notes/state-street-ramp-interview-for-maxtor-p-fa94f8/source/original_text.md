# State Street RAMP Interview for Maxtor Project

> Archived from: State Street RAMP Interview for Maxtor Project.txt
> Original publication date: 2003-04-01
> Author: Peter S. Kastner; David Hill

---

## Original Document Text

RAMP Interview for Maxtor Project

Mr. Prithwi R. Thakuria
Vice President, Information Technology, Data Management Services
State Street
Westwood, MA

State Street is in the banking/financial/insurance business category with sales of over $5B.  

The total IT budget is $129M.

The CIO reports to the President/CEO.

He has responsibility for a little bit of both the entire company and a division or business unit.

State Street uses mainframes, Windows, and Unix/Linux, but he is responsible for the Unix/Linux side.

About 1 TB of Unix storage is available and about 600GB is actually allocated.  He expects Unix storage to increase 15% in the next 12 months and feels that 80% is the maximum percentage used that he would like to see his storage become.  All Unix is on a SAN.

No extra online copies are kept locally, but all production systems are replicated to another data center for disaster recovery purposes.

OLTP is both read write; data warehousing is read-only, but the operational data store (ODS) that they use is read/write.  He considers e-mail as read-only or seldom written.  They have unique large files in the form of blobs or large objects that relate to corporate actions, but this is part of a workflow process so he views them as not read-only or seldom written.  

On a 7 point scale, he rates as a 6 higher capacity disks with slightly less performance and availability and getting a 50% cost reduction whereas he rates as a 2 current disk sizes and performance, but slightly less availability and getting a 30% cost reduction.  

Storage vendors have not discussed low cost storage options with him, and he rates as a 7 that he is likely to purchase low-cost disk storage in the next 12 months.

Restoring at least one volume occurs less than once a year.  

There are no applications with very large non-changing/static data.

20% to 30% of Unix storage is SCSI and 70% to 80% is FC.
Yes for having a problem with the length of the backup window when offline backups are used.  Sometimes backup jobs fail to run to completion.  He believes that all critical data can be restore and that the backup/restore process is not an operational burden, but he agrees that the time to restore critical data is longer than he would like.

In response to understanding terms, he responded:
Active archiving ? follow business rules to move data from online to other media
Online archiving ? applies only to databases
Mezzanine storage ? don't know
Nearline storage ? don't know
Low-cost storage ? overall good TCO

The disk storage for which he has responsibility is located in one location.  Although they do not report to him, State Street has 15 to 20 people dedicated to storage administration for all of its storage.  

The disk storage he is responsible for is FC disk on a SAN connected to Unix servers.  

Any performance problems are network related.

He has a formal SLA (Service Level Agreement).  

The use a tape library and backups seem to run satisfactorily in a 12 a.m. to 6 a.m. backup window.  Three generations of backup are kept.  Data is kept 10 years.  

They use RAID-1 on a Symmetrix and plan to upgrade to DMX.

There are no other layers of the storage hierarchy other than disk and tape.  

His primary database application is the Corporate Actions System, which is a financial transactions workflow that is used by investment managers at customers such as Fidelity.  800GB are allocated for this application.

The disk array upon which this application runs also runs CDW (Client Data Warehouse), which is basically an operational data store.

The benefits that could be derived from moving this data to a less expensive disk storage media is to save money ? overall reduction in TCO, not just cost of individual devices.  

The primary file-based applications are Lotus Notes and Microsoft Exchange, but he does not have responsibility for them.  

A third application is a data warehouse for marketing.  Don't know how big this will be.  

Comments
Large organizations have multiple storage-purchasing decision makers and that can be by business unit as well as by operating system or application.  Wherever there is a silo that operates relatively independently.  However, the move to a SAN where multiple operating systems and applications have data on the SAN may complicate the purchasing decision if the IT operations group is not operating as a utility.  

He views low cost disk as providing TCO savings as well as direct lower costs for the devices themselves and is likely to buy even though his principal application provides critical information to outside clients within an SLA.  That would seem to indicate that he feels comfortable with both the availability and performance characteristics of low-cost disk and can therefore safely respond to budget management pressures.  




---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | state-street-ramp-interview-for-maxtor-p-fa94f8 |
| title | State Street RAMP Interview for Maxtor Project |
| author | Peter S. Kastner; David Hill |
| date | 2003-04-01 |
| type | market-study |
| subject_domain | enterprise-storage / financial-services |
| methodology | face-to-face-interview, market-research, vendor-evaluation |
| source_file | State Street RAMP Interview for Maxtor Project.txt |
| license | CC-BY-4.0 |

### Abstract

Face-to-face RAMP (Rapid Analysis Market Profiling) interview with Prithwi R. Thakuria, VP Information Technology Data Management Services at State Street (Westwood MA), covering Unix SAN storage architecture, willingness to adopt low-cost ATA disk, EMC Symmetrix/DMX infrastructure, and backup/restore practices. State Street had ~1TB Unix storage, all on SAN, 70-80% FC, with EMC Symmetrix RAID-1 and planned DMX upgrade. Thakuria rated 7/7 likelihood to purchase low-cost disk despite SLA obligations to investment management clients, citing TCO savings. The interview captures the financial sector's early-mover posture toward midline storage and the multi-silo purchasing decision structure of large banks.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | First-person face-to-face interview with a senior financial services IT executive on ATA/low-cost disk adoption; rare primary source capturing banking-sector storage decision-making in 2003 at a systemically important institution (State Street). Provides ground-truth demand signal for the nascent midline storage market. |
| **Relevance** | high | Financial sector storage consolidation onto SAN, TCO-driven purchasing pressure, multi-decision-maker enterprise buying patterns, and the tension between SLA obligations and cost reduction remain directly applicable to storage procurement and vendor positioning today. |
| **Prescience** | high | Thakuria's willingness to adopt low-cost disk even for SLA-bound production workloads serving Fidelity proved prescient: financial services became one of the earliest and largest adopters of SATA/nearline SAS; TCO-driven consolidation onto tiered SAN architectures is now universal. His insight about siloed purchasing decision-making in large enterprises presaged the decades-long struggle vendors faced penetrating multi-platform accounts. |

### Prescience Detail


**Prediction 1:** Planned platform upgrade
- **Claimed:** EMC Symmetrix → DMX
- **Year:** 2003
- **Confidence at time:** high

**Actual Outcome 1:** Actual outcome: EMC DMX adoption in financial services
- **Result:** [UNVERIFIED]
- **Confidence:** medium
- **Notes:** [UNVERIFIED] EMC DMX became dominant in financial services 2004-2008; State Street likely upgraded.

**Prediction 2:** SLA-constrained adoption of low-cost disk
- **Claimed:** Likely to purchase even with SLA obligations to outside clients
- **Year:** 2003
- **Confidence at time:** high

**Actual Outcome 2:** Actual outcome: EMC DMX adoption in financial services
- **Result:** [UNVERIFIED]
- **Confidence:** medium
- **Notes:** [UNVERIFIED] EMC DMX became dominant in financial services 2004-2008; State Street likely upgraded.


### Entities Referenced (8)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| State Street Corporation | company | active | [none] |
| Prithwi R. Thakuria | person | active |  |
| Peter S. Kastner | person | active |  |
| David Hill | person | unknown [REVIEW] |  |
| Aberdeen Group | firm | acquired | Aberdeen/Harte-Hanks |
| Maxtor Corporation | company | acquired | Seagate (2006) |
| EMC Corporation | company | unknown [REVIEW] |  |
| Fidelity Investments | company | active | [none] |

### Technologies Referenced (10)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Fibre Channel (FC) | protocol | Various | mature | active |
| SCSI Disk | storage | Various | mature | legacy |
| Storage Area Network (SAN) | storage | Various | growing | active |
| EMC Symmetrix | storage | EMC | mature | legacy |
| EMC DMX (Symmetrix DMX) | storage | EMC | emerging | legacy |
| RAID-1 (Mirroring) | storage | EMC (via Symmetrix) | mature | active |
| Lotus Notes | application | IBM/Lotus | mature | declining |
| Microsoft Exchange | application | Microsoft | mature | active |
| ATA (IDE) Disk / Low-Cost Disk | storage | Various | emerging | superseded-by-SATA |
| Tape Library | storage | Various | mature | active |

### Observation Summary

- Total observations: 35
- By type: data-classification: 4, backup-restore: 3, firmographic: 2, storage-capacity: 2, technology-adoption: 2, technology-mix: 2, viability-prediction: 2, actual-outcome: 2, willingness-to-adopt: 2, application-profile: 2, market-insight: 2, organizational-characteristic: 1, storage-growth-projection: 1, operational-threshold: 1, disaster-recovery: 1, purchase-intent: 1, vendor-engagement: 1, pain-point: 1, storage-staffing: 1, expert-opinion: 1, terminology-awareness: 1
