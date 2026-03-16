# Waiting for ILM?

> Archived from: Computerworld ILM article.txt
> Original publication date: 2004-07-29
> Author: Peter S. Kastner

---

## Original Document Text

Waiting for ILM?
Advice by Peter S. Kastner

JULY 29, 2004 (COMPUTERWORLD) -- Information life cycle management (ILM) is the policy-driven management of information as it changes value throughout its life cycle. Under ILM, data and data sets will migrate around a storage hierarchy based on an enterprise's storage policy. The principles of ILM make enormously good sense, as ILM will generate better operational practices, consistent compliance, and more economical use of storage -- demonstrable business value. But the cross-application management software necessary to make integrated ILM a practical, enterprise-wide solution is four or five years away.  Waiting for ILM maturity is a poor approach, as the time can be used productively and economically to evolve into an ILM environment.

### ILM Recipe: Rich in Storage Pools

Here is a six-step recipe for how organizations can proceed in the adoption of ILM over time. These steps should be taken in order, as each step implies the existence of the prior one -- not necessarily everywhere in the enterprise, but rather within the experience of the IT organization.

**1. Centralize each data center's storage**

ILM is most effective in a networked storage environment where storage management economies on centrally managed pools of storage can have the greatest benefits.  Storage Area Networks (SANs), supplemented with Network Attached Storage (NAS), are affordable now for even small enterprises.

An increasing number of IT professionals are standardizing on a four-pool storage model for data centers. Four pools cover the four types of data storage most often found in the enterprise, including a new form of disk storage called "midline":

* Online dynamic data -- OLTP (online transaction processing) and high-activity DSS (decision support systems) on FC/SCSI disks. Includes structured data such as databases.
* Midline data -- Capacity-oriented disks for active fixed content and compliance data. About 25% of the cost of FC/SCSI for moderate random access on data that seldom or never changes. More than half of enterprise data is semi-structured or unstructured and seldom changing. With industry projections of storage growth at 45% a year, there is a coming huge swing toward putting reference data on midline disks.
* Nearline buffered data -- Today's disk-to-tape backup and restore pool adds midline disk-to-disk backup and restore, compressing backup times by up to 50%. The disk library is the successor to today's tape library.
* Offline data -- No change in offsite sequential tape for disaster recovery.  However, those tapes represent an enormous liability in litigation, so make sure your data retention policy is adhered to.

**2. Create pools of storage on three axes**

A data classification process will identify and match application data requirements to pools. The type of data is one axis. One way to think about data is as structured, semi-structured, and unstructured.

* Structured data is typically database data, which can be sorted.
* Semi-structured data is text information, such as e-mail and word processing documents that can be searched.
* Unstructured data is bit-mapped data, such as medical images, video files, and audio files, which can be sensed.

A second type of access is use, which can include frequency of access (active or inactive) and frequency of updating (fixed, changeable). The pools of storage themselves (online, midline, near-line, and offline) make up the third axis.

Systematically analyzing which pool data belongs in is messy; no doubt about it.  But the process will be enormously beneficial to designing a hierarchy of data unique to your specific industry and enterprise.

**3. Create life cycle policies**

IT organizations have to start with existing storage management products and policies, especially with backup/restore software.  Then add ILM-oriented, hierarchy-based policies as appropriate. Improving storage asset utilization and reducing storage administration costs are drivers for this process; determining best practices for compliance, in general, and data disposal policies in particular will follow.  Creating the policies will not be trivial as many enterprise "interested parties" -- starting with legal -- will be involved.

**4. Populate new/rehosted applications on appropriate pools of storage**

Key assumptions are that every application platform (hardware, application revision, etc.) changes within five years, but no forced platform migration before its time is possible. So develop standards that mandate the form of pools of storage implementation for new/rehosted platforms. Then wait for each application to reach its five-year "refresh point" where data can be reallocated to the proper pool.

**5. Drive economies of scale.**

ILM policies will be become more sophisticated as virtualization becomes embedded and automation reduces the problem intervention and resolution demands on storage personnel. The key metric will be a rising number of terabytes that a storage administrator and a database administrator can effectively manage. At this point, growth in FC/SCSI should be modest as the midline pool will have absorbed much of what was on expensive disks.

**6. Implement intelligent ILM-based storage**

As cross-application ILM-based policy management software comes to maturity circa 2008-2010, expect storage-related hours on production systems to be reduced by 80% -- but there will be more storage than today due to growth.  Although attempts will be made to accelerate the process, full legal and audit compliance sign-off on automated ILM policy management won't occur before this time.

Peter S. Kastner is co-founder and a member of the board of directors of Aberdeen Group Inc., an industry market research firm.

---

## Frictionless Data Package Metadata

### Study Record

| Field | Value |
|-------|-------|
| **study_id** | computerworld-ilm-article-ce11c2 |
| **title** | Waiting for ILM? |
| **author** | Peter S. Kastner |
| **date** | 2004-07-29 |
| **type** | article |
| **subject_domain** | enterprise-storage |
| **methodology** | industry-analysis, document-review |
| **source_file** | Computerworld ILM article.txt |
| **license** | CC-BY-4.0 |

### Abstract

Computerworld published column by Aberdeen Group co-founder Peter S. Kastner presenting a six-step recipe for enterprise adoption of Information Lifecycle Management (ILM). Argues that while cross-application ILM management software is four to five years away (circa 2008-2009), organizations should not wait but should proactively evolve toward ILM. Prescribes centralizing storage on SANs and NAS, creating pools on three axes, establishing lifecycle policies, populating applications on appropriate pools during five-year refresh cycles, driving economies of scale through virtualization and automation, and finally implementing intelligent ILM-based storage by 2008-2010. Introduces a four-pool storage model and projects 45% annual storage growth.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Practical ILM adoption guide published in a major trade publication; useful six-step framework but not groundbreaking research |
| **Relevance** | high | Tiered storage and data lifecycle management are more relevant than ever with cloud storage tiers, compliance requirements, and enterprise data governance frameworks |
| **Prescience** | high | Correctly predicted ILM software maturity timeline of 2008-2010; correctly predicted midline/capacity tier dominance; correctly predicted automation reducing storage admin effort; four-pool model maps well to modern cloud storage tiers |

### Prescience Detail

**Prediction 1: ILM software matures circa 2008-2010**
- *Viability-prediction (OBS-020):* Cross-application ILM software predicted to reach maturity 4-5 years from 2004.
- *Actual-outcome (OBS-024):* ILM concepts became standard in enterprise storage management by 2008-2010; EMC, IBM, and others delivered tiered storage management platforms on the predicted timeline.

**Prediction 2: Midline pool absorbs expensive FC/SCSI workloads**
- *Viability-prediction (OBS-021):* Growth in FC/SCSI should be modest as midline absorbs capacity workloads.
- *Actual-outcome (OBS-028):* SATA, NL-SAS, and object storage became dominant enterprise storage media by volume; flash/SSD replaced FC/SCSI for performance tier.

**Prediction 3: Disk-to-disk backup replaces tape libraries**
- *Viability-prediction (OBS-022):* Disk library positioned as successor to tape library.
- *Actual-outcome (OBS-026):* Tape persists for cold/compliance storage but disk-to-disk backup became the dominant backup method; cloud backup further extended the model.

**Prediction 4: Virtualization and automation drive rising TB-per-admin ratios**
- *Viability-prediction (OBS-023):* Embedded virtualization and automation reduce intervention demands on storage personnel.
- *Actual-outcome (OBS-027):* Software-defined storage and cloud managed services validated the prediction; TB-per-admin ratios increased by orders of magnitude.

### Entities Referenced (7)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | analyst | acquired | spiceworks-ziff-davis |
| Computerworld | publisher | active | -- |
| EMC Corporation | vendor | acquired | dell-technologies |
| Hitachi Data Systems | vendor | acquired | hitachi-vantara |
| StorageTek | vendor | acquired | oracle |
| IBM | vendor | active | -- |
| Veritas Software | vendor | active | -- |

### Technologies Referenced (8)

| Technology | Category | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|---------------------|---------------------|
| Storage Area Networks | storage-infrastructure | growth | mature |
| Network Attached Storage | storage-infrastructure | growth | mature |
| Fibre Channel/SCSI Disks | storage-media | mature | legacy |
| Midline Capacity Disks | storage-media | emerging | evolved |
| Disk-to-Disk Backup | storage-technology | emerging | mature |
| ILM Policy Management Software | storage-software | pre-market | evolved |
| Tape Storage | storage-media | mature | niche |
| Storage Virtualization | storage-technology | emerging | mature |

### Observation Summary

- **Total observations:** 31
- **By type:**
  - framework-factor: 6 (six-step ILM adoption recipe)
  - technology-assessment: 7 (SAN, NAS, FC/SCSI, midline, D2D backup, tape, ILM software)
  - market-data: 4 (45% storage growth, midline cost, 80% admin reduction, data composition)
  - viability-prediction: 4 (ILM maturity, midline absorption, D2D replacing tape, automation impact)
  - actual-outcome: 5 (ILM maturity validated, cloud tiers validated, tape persists, automation validated, midline dominance)
  - strategy-classification: 3 (four-pool model, three-axis classification, ILM definition)
  - expert-opinion: 2 (compliance warning, adoption urgency)
