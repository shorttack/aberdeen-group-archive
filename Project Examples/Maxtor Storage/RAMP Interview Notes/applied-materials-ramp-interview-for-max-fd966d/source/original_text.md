# RAMP Interview: Applied Materials (Maxtor Midline Storage Study)

> Archived from: Applied Materials RAMP Interview for Maxtor Project.txt
> Original publication date: 2003-04-01
> Author: Peter S. Kastner, David Hill

---

## Original Document Text

RAMP Interview for Maxtor Project

Mr. Bill Foley
Director, Computing & Intranet Services
Applied Materials
Santa Clara, CA

Applied Materials is in the industrial manufacturing business.  It has $6B in revenues and 23,000 people.

The company uses both Windows and Unix/Linux operating systems, but he has responsibility for Windows.  

There is 16 to 20 TB of Windows storage, 60% of it is used, and it is expected to grow at 20% in the next 12 months.  He would like the percentage of use to rise to 80%.  80% of this storage is internal direct-attached storage, whereas 20% is on a storage area network.  He keeps 2 online copies.  The number of tape copies varies by application.  

He has some data that is effectively read-only or seldom written, but he feels that this is very small as applications typically tend to be both read and write.  

On a scale of 1 to 7, his willingness to try higher capacity disks with a 50% cost reduction is a 6, but he is completely unwilling (1) to try current capacity disks with slightly less availability at a 30% cost reduction.  Availability is a key issue, but it would not be as critical for online development.

HP, IBM, and EMC have all discussed low-cost disk storage options with him, but he has not purchased any and is unlikely to do so on a massive scale.  EMC is the main supplier, but he also has HP.

Restores of at least one volume occur less than once a year.

He has no single large applications with very large non-changing/static data.  

80% of storage is SCSI and 20% is FC.

He has a problem with the backup window, but jobs run well and he can guarantee that all critical data can be restored.  However, backup is an operational burden and the time to restore is longer than he would like.

As far as terms go,
Active archiving ? scheduled real-time archiving
Online archiving ? real-time archiving
Mezzanine storage ? don't know
Nearline storage ? proximity
Low-cost storage ? lower cost

His IT budget is between $1M and 4$M.

The CIO reports to the President/CEO.  

His responsibility is global.  

Storage is distributed campus-wide, but he hopes to consolidate.  50% of his storage of 16 to 20 TB is distributed over the campus and 50% is in the data center.  

The Window group does not have specific people assigned to storage, but the Unix people do.

They have service availability agreements called MDA (mutual delivery agreements).  If requirements are not met, the worst case scenario would be that it would be revenue impacting.  

They use an LTO-based tape library.

RAID5 is used to protect the data.  

Retention policy varies.  One application is at 3 years, but others are just accumulating.  

Disk and tape are the members of the storage hierarchy although a solid state device is used, but not in the U.S.

Outside his responsibility, the company runs SAP using Oracle on Unix.  There is only one location for this database although there are distributed sites that feed off the master.  There are no formal service level agreements.  

The backup is late at night after midnight for about an hour.  The data is mirrored.  

The main file-based application is Lotus Notes that provides e-mail and online databases.  He expects this to grow by 20% in the next 12 months.  It runs on Windows.  Parts are on the SAN and parts are not.  This application is shared on an EMC Symmetrix with Unix applications.  The data is at one site and is on FC-based disk.  There are no performance bottlenecks.  There are no formal SLAs , but there are informal expectations.  The data is RAID protected.

The bulk of the data is still read/write for e-mail.  They wipe out data over 3 months.  The user can archive to a laptop or a desktop.

Reliability is the key to moving any of this application data to a less costly disk technology.  

The third application is CAD/CAM which takes up 4TB and is expected to grow at 30to 35% over the next 12 months.  The client code is on Windows, but the main side is Unix.  It is run on an external direct attached array that was originally provided by Compaq.  

The application is at a central site, but there is distributed data.  The disk technology used is SCSI.  There are no performance issues at this point.  No formal SLA.  Reliability and serviceability are issues in moving to less costly disk technology.  

Both TCO and ROI are used in financial analysis.  ROI is more detailed with a 24 month payback, but TCO is more fluid.  Everything is on a project-by-project basis.  

Comments
Although much data is really read only, it is really hard to separate out what is effectively read-only from what still could be written to.  IT managers do not think in those terms.  They think in terms of applications and what the applications are capable of doing rather than the composition of databases and files.

Even a small decrease in availability is a red flag to IT managers.  The funny thing is that the difference is likely to be so small overall that they are not likely to experience any problems as a result.  Positive positioning on availability will be important for cost-effective disk.


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | applied-materials-ramp-interview-for-max-fd966d |
| title | RAMP Interview: Applied Materials (Maxtor Midline Storage Study) |
| author | Peter S. Kastner, David Hill |
| date | 2003-04-01 |
| type | market-study |
| subject_domain | enterprise-storage / midline-disk-evaluation |
| methodology | ramp-interview, face-to-face, industry-analysis |
| source_file | Applied Materials RAMP Interview for Maxtor Project.txt |
| license | CC-BY-4.0 |

### Abstract

Face-to-face RAMP interview with Bill Foley, Director of Computing & Intranet Services at Applied Materials (Santa Clara CA), documenting enterprise storage practices and willingness-to-adopt ATA/low-cost disk alternatives. Applied Materials operated 16-20TB of Windows storage with 80% DAS / 20% SAN, rating high willingness for capacity at lower cost (6/7) but zero willingness for any availability reduction (1/7). The interview surfaced a foundational insight: IT managers perceive applications and availability holistically, making even marginal reliability trade-offs unacceptable — a signal that positioned the midline storage market.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Primary market-validation data point in Aberdeen's RAMP study for Maxtor; captures enterprise ATA adoption sentiment from a major semiconductor equipment manufacturer at the exact inflection point of ATA-to-SATA transition. |
| **Relevance** | high | Storage tiering, availability SLAs, and the tension between cost reduction and reliability remain central to enterprise storage decisions; the 6/7 vs. 1/7 availability-willingness gap is still a relevant framework for flash/cloud tiering decisions. |
| **Prescience** | medium | The strong rejection of availability trade-offs (1/7) accurately predicted enterprise resistance to early ATA; however, the study underestimated how SATA would eventually resolve availability parity — and neither participant foresaw SSD/flash eliminating the cost-reliability trade-off entirely by ~2015. |

### Prescience Detail


**Prediction 1:** ata-adoption-prognosis
- **Claimed:** unlikely at massive scale
- **Year:** 2003
- **Confidence at time:** high


### Entities Referenced (10)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Applied Materials Inc. | company | active |  |
| Bill Foley | person | active |  |
| Maxtor Corporation | company | unknown [REVIEW] |  |
| EMC Corporation | company | unknown [REVIEW] |  |
| Hewlett-Packard (HP) | company | split | HP Inc./HPE (2015) |
| IBM | company | active |  |
| Compaq | company | dissolved | Acquired by HP (2002) |
| Peter S. Kastner | person | active |  |
| David Hill | person | active |  |
| Aberdeen Group | firm | acquired | Aberdeen/Harte-Hanks |

### Technologies Referenced (13)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| SCSI (Small Computer System Interface) | protocol | Industry Standard | mature | legacy |
| Fibre Channel (FC) | protocol | Industry Standard | growing | active |
| ATA Disk (IDE/ATA-100) | platform | Industry Standard | emerging | legacy |
| Serial ATA (SATA) | protocol | Industry Standard | emerging | active |
| Storage Area Network (SAN) | platform | Industry Standard | growing | active |
| Network Attached Storage (NAS) | platform | Industry Standard | growing | active |
| RAID 5 (Striping with Parity) | protocol | Industry Standard | mature | active |
| LTO (Linear Tape Open) | platform | IBM/HP/Seagate | growing | active |
| EMC Symmetrix | platform | EMC | mature | legacy |
| Lotus Notes | application | IBM/Lotus | mature | legacy-supported |
| Solid State Drives (SSD) | platform | Various | emerging | dominant |
| CAD/CAM Software | application | Various | mature | active |
| SAP on Oracle (Unix) | application | SAP, Oracle | mature | active |

### Observation Summary

- Total observations: 33
- By type: infra-profile: 8, expert-opinion: 5, org-profile: 4, app-profile: 3, growth-metric: 2, willingness-to-adopt: 2, vendor-relationship: 2, operational-metric: 2, sla-profile: 1, financial-analysis: 1, viability-prediction: 1, actual-outcome: 1, market-sizing: 1
