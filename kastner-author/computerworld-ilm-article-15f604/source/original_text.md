# Waiting for ILM?

> Archived from: Archive-1/Computerworld ILM article.doc
> Original publication date: 2004-07-29
> Author: Peter S. Kastner

---

## Original Document Text



Waiting for ILM?
Advice by Peter S. Kastner

JULY 29, 2004 (COMPUTERWORLD) – Information life cycle management (ILM) is
the policy-driven management of information as it changes value throughout
its life cycle. Under ILM, data and data sets will migrate around a storage
hierarchy based on an enterprise’s storage policy. The principles of ILM
make enormously good sense, as ILM will generate better operational
practices, consistent compliance, and more economical use of storage —
demonstrable business value. But the cross-application management software
necessary to make integrated ILM a practical, enterprise-wide solution is
four or five years away.  Waiting for ILM maturity is a poor approach, as
the time can be used productively and economically to evolve into an ILM
environment.

ILM Recipe: Rich in Storage Pools

Here is a six-step recipe for how organizations can proceed in the adoption
of ILM over time. These steps should be taken in order, as each step
implies the existence of the prior one — not necessarily everywhere in the
enterprise, but rather within the experience of the IT organization.

1. Centralize each data center’s storage
ILM is most effective in a networked storage environment where storage
management economies on centrally managed pools of storage can have the
greatest benefits.  Storage Area Networks (SANs), supplemented with Network
Attached Storage (NAS), are affordable now for even small enterprises.

An increasing number of IT professionals are standardizing on a four-pool
storage model for data centers. Four pools cover the four types of data
storage most often found in the enterprise, including a new form of disk
storage called “midline”:
Online dynamic data — OLTP (online transaction processing) and high-
activity DSS (decision support systems) on FC/SCSI disks. Includes
structured data such as databases.
Midline data — Capacity-oriented disks for active fixed content and
compliance data. About 25% of the cost of FC/SCSI for moderate random
access on data that seldom or never changes. More than half of enterprise
data is semi-structured or unstructured and seldom changing. With industry
projections of storage growth at 45% a year, there is a coming huge swing
toward putting reference data on midline disks.
Nearline buffered data — Today’s disk-to-tape backup and restore pool adds
midline disk-to-disk backup and restore, compressing backup times by up to
50%. The disk library is the successor to today’s tape library.
Offline data — No change in offsite sequential tape for disaster recovery.
However, those tapes represent an enormous liability in litigation, so make
sure your data retention policy is adhered to.
2. Create pools of storage on three axes
A data classification process will identify and match application data
requirements to pools. The type of data is one axis. One way to think about
data is as structured, semi-structured, and unstructured.
Structured data is typically database data, which can be sorted.
Semi-structured data is text information, such as e-mail and word
processing documents that can be searched.
Unstructured data is bit-mapped data, such as medical images, video files,
and audio files, which can be sensed.
A second type of access is use, which can include frequency of access
(active or inactive) and frequency of updating (fixed, changeable). The
pools of storage themselves (online, midline, near-line, and offline) make
up the third axis.

Systematically analyzing which pool data belongs in is messy; no doubt
about it.  But the process will be enormously beneficial to designing a
hierarchy of data unique to your specific industry and enterprise.

[pic]3. Create life cycle policies
IT organizations have to start with existing storage management products
and policies, especially with backup/restore software.  Then add ILM-
oriented, hierarchy-based policies as appropriate. Improving storage asset
utilization and reducing storage administration costs are drivers for this
process; determining best practices for compliance, in general, and data
disposal policies in particular will follow.  Creating the policies will
not be trivial as many enterprise “interested parties” — starting with
legal — will be involved.

4. Populate new/rehosted applications on appropriate pools of storage
Key assumptions are that every application platform (hardware, application
revision, etc.) changes within five years, but no forced platform migration
before its time is possible. So develop standards that mandate the form of
pools of storage implementation for new/rehosted platforms. Then wait for
each application to reach its five-year “refresh point” where data can be
reallocated to the proper pool.

5. Drive economies of scale.
ILM policies will be become more sophisticated as virtualization becomes
embedded and automation reduces the problem intervention and resolution
demands on storage personnel. The key metric will be a rising number of
terabytes that a storage administrator and a database administrator can
effectively manage. At this point, growth in FC/SCSI should be modest as
the midline pool will have absorbed much of what was on expensive disks.

6. Implement intelligent ILM-based storage
As cross-application ILM-based policy management software comes to maturity
circa 2008-2010, expect storage-related hours on production systems to be
reduced by 80% — but there will be more storage than today due to growth.
Although attempts will be made to accelerate the process, full legal and
audit compliance sign-off on automated ILM policy management won’t occur
before this time.

Peter S. Kastner is co-founder and a member of the board of directors of
Aberdeen Group Inc., an industry market research firm.



---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | computerworld-ilm-article-15f604 |
| title | Waiting for ILM? |
| author | Peter S. Kastner |
| date | 2004-07-29 |
| type | expert-report |
| subject_domain | Enterprise Storage / Information Lifecycle Management |
| methodology | Practitioner advisory; prescriptive six-step framework based on industry observation |
| source_file | Archive-1/Computerworld ILM article.doc |
| license | CC-BY-4.0 |

### Abstract

Published in Computerworld on 29 July 2004, this advisory article argues that integrated cross-application ILM software is 4-5 years away from maturity but that enterprises should begin evolving toward ILM now using a six-step recipe: (1) centralize storage into SANs/NAS, (2) classify data across three axes (type/access/pool), (3) create lifecycle policies, (4) populate new applications on appropriate pools, (5) drive economies of scale via virtualization, (6) implement intelligent ILM circa 2008-2010. The article introduces the four-pool storage model (online FC/SCSI, midline, nearline, offline tape) and projects 45% annual storage growth driving a swing toward midline disk for reference data.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | ILM was a defining storage strategy concept of the mid-2000s; Kastner's framework was widely read and shaped enterprise storage planning. |
| **Relevance** | high | Directly authored by Peter S. Kastner, published as Computerworld column; core Kastner collection piece on enterprise IT strategy. |
| **Prescience** | high | Predicted cross-application ILM maturity by 2008-2010 and 45% annual storage growth; the midline disk tier (now 'nearline SAS') became the dominant enterprise tier, and ILM capabilities did mature in that timeframe. |

### Prescience Detail


**Prediction 1:** ILM Cross-Application Software Maturity Timeline
- **Claimed:** Integrated cross-application ILM software is 4-5 years from practical enterprise-wide maturity (circa 2008-2009)
- **Year:** 2004
- **Confidence at time:** high

**Actual Outcome 1:** ILM Software Maturity Actual Outcome
- **Result:** [UNVERIFIED]
- **Confidence:** partially-verified
- **Notes:** 

**Prediction 2:** Storage Administrator Productivity via Virtualization
- **Claimed:** Rising terabytes-per-admin ratio as virtualization becomes embedded and automation reduces intervention
- **Year:** 2004
- **Confidence at time:** medium

**Prediction 3:** ILM Production System Hours Reduction
- **Claimed:** Storage-related hours on production systems reduced by 80% when ILM matures circa 2008-2010
- **Year:** 2004
- **Confidence at time:** medium

**Actual Outcome 3:** ILM Software Maturity Actual Outcome
- **Result:** [UNVERIFIED]
- **Confidence:** partially-verified
- **Notes:** 


### Entities Referenced (3)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group Inc. | firm | acquired | Harte-Hanks Communications (2006); later spun off as Aberdeen Strategy & Research |
| Peter S. Kastner | person | active |  |
| Computerworld | institution | renamed | Part of IDG/Foundry (IDG acquired by Blackstone 2017; digital brand continues under Foundry/IDG Communications) |

### Technologies Referenced (9)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Storage Area Network (SAN) | platform | Multiple | mature | {'lifecycle_current': 'active', 'notes': 'Storage Area Networks remain a core enterprise storage infrastructure technology. FC SANs and iSCSI SANs widely deployed. Market active and growing.', 'source': 'General knowledge'} |
| Network Attached Storage (NAS) | platform | Multiple | mature | {'lifecycle_current': 'active', 'notes': 'Network Attached Storage is actively growing. Enterprise NAS (NetApp, Dell PowerScale/Isilon, Pure Storage FlashBlade) and consumer NAS (Synology, QNAP, WD) are all actively developed.', 'source': 'General knowledge'} |
| Fibre Channel / SCSI Disk (Online Tier) | storage | Multiple | mature | {'lifecycle_current': 'mature', 'notes': 'Fibre Channel/SCSI disk (15K RPM online tier storage) remains in use in legacy enterprise environments. The technology is mature; new installs favor all-flash arrays (NVMe). FC-NVMe is the current evolution for high-performance FC storage.', 'source': 'https://fibrechannel.org/wp-content/uploads/2024/11/Fibre-Channel-Solutions-Guide-2024.pdf'} |
| Midline Disk Storage | storage | Multiple | emerging | {'lifecycle_current': 'mature', 'notes': 'Midline (NL-SAS/SATA) disk drives for capacity storage tiers remain in active production and use. Still widely deployed in high-capacity storage arrays and cloud storage infrastructure. Competing with higher-capacity HDDs and object storage.', 'source': 'General knowledge'} |
| Disk-to-Disk Backup (D2D) | storage | Multiple | emerging | {'lifecycle_current': 'active', 'notes': 'Disk-to-disk (D2D) backup is an active and mainstream backup approach. Modern implementations include VTL (virtual tape libraries), backup appliances (Data Domain/Dell, Veeam), and cloud backup. Widely adopted.', 'source': 'https://www.lenovo.com/us/en/glossary/what-is-disk-to-disk/'} |
| Sequential Tape (Offline / Disaster Recovery) | storage | Multiple | mature | {'lifecycle_current': 'active', 'notes': 'Sequential tape backup for offline/disaster recovery remains active. LTO tape shipments hit a record 176.5 Exabytes in 2024 (15.4% growth). Tape is widely used for long-term archiving, ransomware protection (air gap), and disaster recovery.', 'source': 'https://www.theregister.com/2025/07/23/lto_2024_tape_shipment_data/'} |
| Cross-Application ILM Policy Management Software | application | Multiple (emerging) | pre-market | {'lifecycle_current': 'evolved', 'notes': 'Cross-application ILM (Information Lifecycle Management) Policy Software as a standalone category evolved into broader data governance, cloud archiving, and compliance platforms. The ILM market is active and growing (projected CAGR of 14%), but the specific standalone ILM software category has been absorbed into broader data management platforms.', 'source': 'https://concentric.ai/2025-guide-to-modern-information-lifecycle-management/'} |
| Storage Virtualization | platform | Multiple | emerging | {'lifecycle_current': 'active', 'notes': 'Storage virtualization is an active and growing technology. Market projected at $14.99B by 2030 (CAGR 10.7%). SDS (Software-Defined Storage), HCI (Hyper-Converged Infrastructure), and cloud storage virtualization are mainstream enterprise technologies.', 'source': 'https://www.openpr.com/news/4433215/leading-companies-reinforce-their-presence-in-the-storage'} |
| Online Transaction Processing (OLTP) | application | Multiple | mature | {'lifecycle_current': 'active', 'notes': 'Online Transaction Processing (OLTP) systems are the backbone of transactional business applications. Modern OLTP runs on relational databases (Oracle, SQL Server, PostgreSQL) and cloud-native databases. Actively used and developed.', 'source': 'General knowledge'} |

### Observation Summary

- Total observations: 16
- By type: viability-prediction: 3, trend-analysis: 3, actual-outcome: 2, technology-adoption: 1, market-sizing: 1, growth-rate: 1, benchmark-result: 1, risk-assessment: 1, recommendation: 1, topic-insight: 1, expert-opinion: 1
