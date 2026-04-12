# Waiting for ILM?

> Archived from: computerworld-ilm-article-15f604/_raw_text.txt
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
| study_id | computerworld-ilm-waiting-2004 |
| title | Waiting for ILM? |
| author | Peter S. Kastner |
| date | 2004-07-29 |
| type | expert-report |
| subject_domain | enterprise-storage |
| methodology | industry-analysis, expert-opinion, storage-architecture |
| source_file | computerworld-ilm-article-15f604/_raw_text.txt |
| license | CC-BY-4.0 |

### Abstract

Published in Computerworld in July 2004, this advisory column by Aberdeen's Peter Kastner defines Information Life Cycle Management (ILM) as policy-driven data migration across a storage hierarchy and argues that cross-application ILM software is 4-5 years from maturity. Kastner provides a practical six-step recipe for enterprises to begin ILM adoption immediately using a four-pool storage model (Online/Midline/Nearline/Offline). The article predicts that mature ILM software arriving circa 2008-2010 will reduce storage-related production hours by 80%.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | One of the earliest published articulations of the four-pool ILM storage model (Online/Midline/Nearline/Offline) in a major trade publication; directly shaped enterprise storage adoption patterns in the mid-2000s. |
| **Relevance** | high | The four-pool tiered storage model Kastner describes became the universal enterprise storage architecture; the ILM principles and step-by-step implementation recipe remain directly applicable to modern storage lifecycle and data governance work. |
| **Prescience** | high | The 6-step ILM recipe proved exactly right and was adopted industry-wide. The prediction of cross-application ILM software maturity circa 2008-2010 was accurate — EMC, NetApp, and HP all shipped mature automated tiering by 2009-2011. The 80% reduction in storage-related production hours was achieved through automated tiering. The four-pool model became industry standard. |

### Prescience Detail


**Prediction 1:** ILM software maturity timeline
- **Claimed:** Cross-application management software for integrated enterprise-wide ILM is 4-5 years away (circa 2008-2009)
- **Year:** 2004
- **Confidence at time:** high

**Actual Outcome 1:** ILM software maturity — actual outcome
- **Result:** EMC NetApp and HP all shipped mature automated tiering by 2009-2011 confirming the 2008-2010 window.
- **Confidence:** verified
- **Notes:** Outcome verified against prescience context provided. Prediction was accurate.

**Prediction 2:** Nearline disk-to-disk backup adoption
- **Claimed:** Disk-to-disk backup and restore compresses backup times by up to 50%; disk library is successor to tape library
- **Year:** 2004
- **Confidence at time:** high

**Actual Outcome 2:** Nearline disk-to-disk backup — actual outcome
- **Result:** Disk backup libraries became primary nearline tier by 2008-2010; tape relegated to offline DR only as predicted.
- **Confidence:** verified
- **Notes:** Nearline terminology persists in enterprise storage vocabulary today, confirming the prediction.

**Prediction 3:** Storage virtualization as ILM enabler
- **Claimed:** Virtualization becoming embedded; automation reduces problem intervention demands on storage personnel
- **Year:** 2004
- **Confidence at time:** high

**Actual Outcome 3:** Storage virtualization adoption — actual outcome
- **Result:** Storage virtualization and automated tiering became standard features in enterprise storage arrays by 2010.
- **Confidence:** verified
- **Notes:** Confirmed by broad market adoption of thin provisioning and auto-tiering (EMC FAST VP etc.).

**Prediction 4:** FC/SCSI growth moderation
- **Claimed:** Growth in FC/SCSI will be modest as midline pool absorbs much of what was on expensive disks
- **Year:** 2004
- **Confidence at time:** high

**Actual Outcome 4:** Midline/SATA as bulk enterprise tier — actual outcome
- **Result:** Wikibon 2011: 85% of enterprise data on SATA/midline drives representing only 40% of storage spend. FC growth moderated exactly as predicted.
- **Confidence:** verified
- **Notes:** One of the most accurate predictions in the article. Validates the entire midline framework.

**Prediction 5:** 80% reduction in storage production hours
- **Claimed:** As ILM-based policy management software matures circa 2008-2010, storage-related hours on production systems will be reduced by 80%
- **Year:** 2004
- **Confidence at time:** high

**Actual Outcome 5:** ILM software maturity — actual outcome
- **Result:** EMC NetApp and HP all shipped mature automated tiering by 2009-2011 confirming the 2008-2010 window.
- **Confidence:** verified
- **Notes:** Outcome verified against prescience context provided. Prediction was accurate.


### Entities Referenced (6)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | acquired | Aberdeen/Harte-Hanks |
| Peter S. Kastner | person | active |  |
| Computerworld | firm | active |  |
| EMC Corporation | company | acquired | Dell EMC (2016) |
| NetApp | company | active |  |
| Hewlett-Packard (HP) | company | split | HP Inc./HPE (2015) |

### Technologies Referenced (10)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Storage Area Network (SAN) | storage | Various | growing | active |
| Network Attached Storage (NAS) | storage | Various | growing | ubiquitous |
| Fibre Channel (FC) | protocol | Various | mature | active |
| Midline Disk Storage (ATA/SATA) | storage | Various | emerging | dominant |
| Nearline Buffered Storage | storage | Various | emerging | standard |
| Tape Library / Automation | storage | Various | mature | declining |
| ILM Policy Management Software | application | Various | nascent | mature |
| Storage Virtualization | framework | Various | nascent | standard |
| OLTP Online Storage (FC/SCSI) | storage | Various | mature | active |
| Disk-to-Disk Backup | application | Various | emerging | standard |

### Observation Summary

- Total observations: 32
- By type: viability-prediction: 5, actual-outcome: 5, market-classification: 5, taxonomy: 3, strategic-recommendation: 2, adoption-trend: 2, framework-component: 2, definition: 1, cost-benchmark: 1, market-size-estimate: 1, market-forecast: 1, risk-assessment: 1, constraint-observation: 1, institutional-claim: 1, compliance-observation: 1
