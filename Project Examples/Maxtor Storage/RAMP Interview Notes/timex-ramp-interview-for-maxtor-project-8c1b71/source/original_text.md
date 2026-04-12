# Timex RAMP Interview for Maxtor Project

> Archived from: Timex RAMP Interview for Maxtor Project.txt
> Original publication date: 2003-04-16
> Author: Peter S. Kastner; David Hill

---

## Original Document Text

RAMP Interview for Maxtor Project

Mr. Robert Lutz
Manager, Information Technology Operations
Timex
Middlebury, CT

Date: April 16, 2003

Timex is a privately held consumer manufacturing company (watches) with 5000 employees worldwide.

The total IT budget is between $10M and $24 M.

The CIO reports to the CFO.

Bob has responsibility for the entire company.  The company uses Window and Linux.  There are 6 TB in Middlebury and 10 TB WW.  80% of this storage is in use..  He expects that both Windows and Unix will increase 10% in the next 12 months.  The 80% is the maximum that he wants disk space to be used.

20% of Windows storage is internal direct attached storage whereas 80% is part of a SAN while with Unix 20% is internal direct-attached storage and 80% is external direct-attached storage.  

How many copies of tape storage depends upon the application.

80% of his data is inactive data (in response to the question do you have some data that is effectively read-only or seldom written).  Data warehousing and unique large files (images of watches for advertising) are the prime examples, but even OLTP is written-once and CAD/CAM is seldom written after a certain release point is reached.

Relatively to using higher capacity disks with slightly less performance and availability and getting a 50% cost reduction he is very unwilling (2) to use.  The same rating is for current disk sizes and performance, but slightly less availability and getting a 30% cost reduction.  The reason is that he likes to have flexibility and there is a question of having extra administrative work if there is another level of disks to manage.  The costs of disks has gone down so they are not a big factor in the equation as compared with administrative costs.  It would be a big job to manage a hierarchy so it doesn't make sense and he doesn't have the resources.  

HP and EMC have talked about a lower cost option, but he has not purchased and he is not likely to (2) in the next 12 months.  

His organization has to restore at least one volume less than once a year.  

He has several applications, as discussed earlier, that have very large non-changing data.

20% of storage is SCSI and 80% s FC.  

He uses hot backups and has no problem with backup jobs failing to run to completeion.  However, he cannot guarantee that all critical data can be restored, backup is an operational burden, and the time to restore critical data is longer than he would like.

For terms, active archiving is planned storage hierarching, online archiving is being able to archive from a more active to a more historical type of environment, he has never heard of mezzanine storage, nearline storage means archiving to a CD, and low low-cost storage means a CD or floppy disk.  

Timex has several data centers, but the main one is in Middlebury.  There are no full time people on storage.  The responsibility is spread over a number of system administrators.  There are no performance bottlenecks.  No formal SLAs are in place.

They use HP robotic tape drives with HP Omniback software.  Incrementals are taken daily with weekly full backups.  They use RAID5 with some mirroring.  

The primary data application is Oracle Financial for order entry, etc.  The production database is 1TB and is expected to stay the same for next year.  It is run on Unix.  The system is an HP FC60 on direct attached storage.  The array is dedicated to the application.  It is FC and there is no performance bottleneck.  No formal SLA.  A daily incremental tape is used for backup with a weekly full.  4 generations of tape are kept with 1 generation offsite.  Issue of manageability would prevent movement to less expensive disk media.

Oracle has test instances.  

The primary file-based application is Microsoft Exchange for e-mail and is about 1 TB.  It is run on Windows on a SAN.  There are other applications on the SAN, for example, the data warehouse is on the SAN as well as Active Project (images).  The SAN is FC-based using a Compaq SAN unit.  There are no performance bottlenecks and no formal SLAs.  Incrementals or a full backup are the backup methods. 4 generations are kept.  RAID5 is used on the array. E-mail is retained indefinitely on the array as he doesn't have the people to get rid of it.  There is a lot of data not used, but the problems of cleaning it up are more costly than new disk.

The third major application is Active Project.  This is a combination of imaging, project management, Web page, CAD/CAM with the information shared within the company as well as with vendors.  It is Windows-based on a SAN.  There are issues with backup.  

He is trying to keep budget flat or bring it down.  They lease equipment on a 3 year cycle using the operating budget.  They do not to a TCO/ROI analysis.  Since he has had to reduce headcount, he has to reduce complexity by trying to simplify things.  
Comments
Bob has a clear understanding that much of his data is inactive data, but his reasons for not wanting to consider low-cost disk alternatives are illustrative.  With tight budgets and decreasing headcount, he does not dare to introduce another level of disks to manage, as there is the danger of extra administrative work.  Disk costs are small as compared to administrative costs.  

Transparency and significant cost savings would be the requirement to sell the "Bobs" of the world.


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | timex-ramp-interview-for-maxtor-project-8c1b71 |
| title | Timex RAMP Interview for Maxtor Project |
| author | Peter S. Kastner; David Hill |
| date | 2003-04-16 |
| type | market-study |
| subject_domain | enterprise-storage / consumer-manufacturing |
| methodology | face-to-face-interview, market-research, vendor-evaluation |
| source_file | Timex RAMP Interview for Maxtor Project.txt |
| license | CC-BY-4.0 |

### Abstract

Face-to-face RAMP interview with Robert (Bob) Lutz, Manager IT Operations at Timex (Middlebury CT), covering enterprise storage architecture, unwillingness to adopt additional storage tiers, and the critical insight that administrative costs dwarf hardware costs in storage decision-making. Timex had 6TB local / 10TB worldwide with 80% utilization and 80% inactive data, yet rated only 2/7 willingness to adopt low-cost disk. Lutz articulated that tight budgets and reduced headcount make adding a storage management tier more costly than the hardware savings — a foundational insight for the storage automation and hyperconverged infrastructure markets.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Captures the 'management complexity veto' — the counter-intuitive finding that budget-constrained IT shops with the most inactive data are least likely to adopt storage tiering due to administrative overhead. The Timex interview is the canonical expression of this paradox in the RAMP dataset and directly shaped Kastner/Hill's market sizing and positioning recommendations for MaXLine. |
| **Relevance** | high | The administrative cost > hardware cost insight remains the central tension in enterprise storage: it drove the entire storage automation software market (ILM, HSM), converged infrastructure, hyperconverged (HCI), and cloud storage adoption. 'Transparency and significant cost savings would be the requirement to sell the Bobs of the world' is still the sales challenge for every storage tier vendor. |
| **Prescience** | high | Lutz's 2003 insight that disk costs are small compared to administrative costs was visionary: it predicted exactly why enterprise storage tiering adoption was slow until automation tools matured (2008-2015), why hyperconverged infrastructure (Nutanix, vSAN) succeeded by eliminating tier management, and why cloud object storage (S3) eventually absorbed inactive data without adding admin overhead. |

### Prescience Detail


**Prediction 1:** Storage tiering adoption by SMB/cost-constrained shops without automation tools
- **Claimed:** Low without automation; management complexity will block adoption
- **Year:** 2003
- **Confidence at time:** high

**Actual Outcome 1:** Actual outcome: HCI/cloud as solution to tiering complexity
- **Result:** [DEFERRED]
- **Confidence:** high
- **Notes:** [DEFERRED] Hyperconverged infrastructure (Nutanix 2011, VMware vSAN 2014) and cloud object storage (S3) solved the 'Bob problem' by eliminating tier management entirely.


### Entities Referenced (12)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Timex Group USA | company | active | [none] |
| Robert Lutz (Bob Lutz) | person | active |  |
| Peter S. Kastner | person | active |  |
| David Hill | person | [DEFERRED] |  |
| Aberdeen Group | firm | acquired | Aberdeen/Harte-Hanks |
| Maxtor Corporation | company | acquired | Seagate (2006) |
| Hewlett-Packard (HP) | company | split | HP Inc./HPE (2015) |
| EMC Corporation | company | [DEFERRED] | [DEFERRED] |
| Compaq | company | dissolved | HP (2002) |
| Oracle | company | active |  |
| Microsoft | company | active |  |
| Western Digital | company | active |  |

### Technologies Referenced (13)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Fibre Channel (FC) | protocol | Various | mature | active |
| SCSI Disk | storage | Various | mature | legacy |
| Storage Area Network (SAN) | storage | Various | growing | active |
| Direct-Attached Storage (DAS) | storage | Various | mature | declining |
| HP FC60 Disk Array | storage | HP | current | legacy |
| RAID-5 | storage | Various | mature | active |
| Oracle Financials (ERP) | application | Oracle | mature | active |
| Microsoft Exchange | application | Microsoft | mature | active |
| HP Omniback Backup Software | application | HP | current | discontinued |
| HP Robotic Tape Library | storage | HP | current | declining |
| ATA (IDE) Disk / Low-Cost Disk | storage | Various | emerging | superseded-by-SATA |
| CAD/CAM Software / Imaging | application | Various | mature | active |
| Active Project (Imaging/Project Mgmt) | application | Various | current | [DEFERRED] |

### Observation Summary

- Total observations: 35
- By type: market-insight: 5, application-profile: 3, firmographic: 2, organizational-characteristic: 2, storage-capacity: 2, storage-growth-projection: 2, technology-mix: 2, willingness-to-adopt: 2, storage-utilization: 1, data-classification: 1, purchase-intent: 1, viability-prediction: 1, actual-outcome: 1, headcount-pressure: 1, budget-constraint: 1, storage-architecture: 1, backup-restore: 1, pain-point: 1, storage-staffing: 1, terminology-awareness: 1, technology-adoption: 1, procurement: 1, market-segment-archetype: 1
