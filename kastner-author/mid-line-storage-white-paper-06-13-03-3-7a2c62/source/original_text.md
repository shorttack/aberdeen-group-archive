# Mid-Line Disk Storage: Emerging as Significant Cost-Saving Opportunity

> Archived from: Mid-Line-Storage-White-Paper-06-13-03-3.doc
> Original publication date: 2003-06-13
> Author: Peter S. Kastner / Aberdeen Group

---

## Original Document Text

SOURCE FILE: Mid-Line-Storage-White-Paper-06-13-03-3.doc
STUDY ID: mid-line-storage-white-paper-06-13-03-3-7a2c62
TITLE: Mid-Line Disk Storage Emerging as Significant Cost-Saving Opportunity
AUTHORS: Peter Kastner and David Hill, Aberdeen Group
DATE: 2003-06-13

[Page 1]
AberdeenGroup
Mid-Line Disk Storage Emerging as Significant Cost-Saving Opportunity
An Executive White Paper
June 2003
Aberdeen Group, Inc.

[Page 2]
Aberdeen Group, Inc.
260 Franklin Street
Boston, Massachusetts 02110
Telephone: 617 723 7890
Fax: 617 723 7897
www.aberdeen.com
(C) 2003 Aberdeen Group, Inc.

[Page 3-4]
Executive Summary

After extensive field research conducted on the use of storage in the second quarter of 2003, Aberdeen Group concludes that the old aphorism, "If all you have is a hammer, everything looks like a nail," is widely true of enterprise storage. More than half of enterprises are completely run online using Fibre Channel (FC) and Small Computer System Interface (SCSI) disks. FC/SCSI disks are fast, reliable, and are used a great deal of the time, i.e., they have a high duty cycle. However, they are also much lower in capacity and much higher in cost relative to an emerging class of enterprise storage, Advanced Technology Attachment (ATA) disks. This Executive White Paper presents Aberdeen's revised model for enterprise storage, carving out a middle tier — the mid-line — for ATA disks. It includes our most recent field research findings, conclusions, and recommendations to enterprise storage buyers.

Mid-line storage is defined as high-capacity online ATA disks, which are in the middle tier between high-use FC/SCSI disk arrays and magnetic tape off-line storage. Today, the requirements that can be met effectively using ATA disks are being serviced by relatively expensive FC/SCSI disk arrays, or by slow-to-restore tape.

Mid-line storage is specifically aimed at data that needs to be online (as opposed to tape) and has moderate access and rate-of-change requirements (as opposed to heavy-duty online transaction processing).

ATA disks are not new. The technology has been used in PCs for years. The reliability of ATA disks has improved to the point that, when ATA is coupled with RAID technology, enterprises can now safely trust the use of ATA disks in enterprise-class applications.

Mid-line storage using enterprise ATA disks has the benefits of two to eight times the storage capacity of FC/SCSI — up to 300 GB per ATA disk compared to 142/72/36 GB per FC/SCSI disk. ATA disks are about half the cost per gigabyte.

The raison d'etre for a new mid-line storage tier is four-fold:
1. Move inactive and seldom-used online storage to high-capacity/low cost ATA disks. At least 20% of enterprise data fits this definition — over half will eventually fall into the mid-line.
2. Move applications with inactive and seldom-used data characteristics to mid-line storage (e.g., data warehouse with large detail tables).
3. Improve the data restoration process. Over 60% of survey respondents report data restorations more than once a year — 20% report a data restore monthly or more frequently.
4. Improve backup windows. Over 80% of survey respondents could have a problem with backup window length.

Our research indicates 75% of storage buyers are moderately or highly likely to buy mid-line storage in the coming year.

Aberdeen Group recommendations:
- Storage planners need a better understanding of applications/files that could benefit from mid-line technology.
- Buyers should examine how much new capacity should be devoted to mid-line technology.
- Backup, restore, and copy-retention labor-cost issues demand storage management software.

Aberdeen Group research, backed by our industry experience, indicates that the time and technology have arrived for mid-line storage to become a critical and cost-effective component of every enterprise storage strategy.

[Pages 3-6]
Make Room, Make Room — The Arrival of Mid-Line Disk Storage

Enterprises are familiar with layers of the storage pyramid: high-speed volatile RAM-based devices; random access-based disks; and sequential-access tape.

A new level of disk based on ATA technology is rapidly emerging. Aberdeen terms this level of the pyramid mid-line storage. Mid-line storage is online storage that sits between high-performance disk and tape. It will replace neither high-performance disk nor tape, but will dramatically change how each is used.

Figure 1: The Storage Pyramid — Four Key Levels
Source: Aberdeen Group, June 2003

Mid-line storage has a cost and capacity advantage with respect to high-performance disk. Applications that are not write-performance-bound, such as read-only, fixed content (a.k.a. reference or recallable) data, will gravitate towards mid-line storage.

Mid-line storage has a speed and random access advantage with respect to tape storage. Disk-based data restoration is one way to achieve this goal. Another method is continuous data protection (CDP) that quickly restores data to any point in time.

[Pages 6-7]
Mid-Line Storage Is Already Moving Into the Enterprise

Aberdeen conducted primary market research: 75 face-to-face and telephone interviews with storage managers at companies with  billion or larger in revenue, including several Fortune 50-size businesses in the U.S. with financial services industries over-represented and government/non-profits under-represented.

The research covered storage accessed by servers using three basic types of operating systems: mainframe, Windows, and Unix/Linux.

Survey findings:
- Over 25% showed high willingness to purchase higher-capacity/lower-cost disks
- Nearly 50% showed moderate willingness
- Only ~25% showed little or no willingness
- 60% said their current storage supplier had discussed low-cost storage options
- ~40% said highly likely to purchase low-cost disk storage
- ~33% said moderately likely
- ~25% said unlikely

60% of respondents have single applications with very large non-changing/static data (video, images, data warehouse detailed data, old e-mails).

Backup/restore findings:
- Nearly 2/3 (67%) said restoring critical data takes longer than desired
- ~50% said backup management is a burden
- ~50% would not guarantee all critical data can be restored on a given day
- >80% said backup windows could be a problem with off-line backups

[Pages 8-9]
The Information Life Cycle — Managing Content on the Storage Pyramid

It is generally recognized that data goes through a life cycle. As data ages, the value of the data tends to diminish along with the need to access it.

Figure 2: Where Mid-Line Storage Fits
Source: Aberdeen Group, June 2003

Four basic principles for ILM:
1. Ageing — value and use of content change as content ages (birth, youth, middle-age, old age); need to access data drops dramatically
2. Freezing — content changes from dynamic to fixed as updates cease; becomes read-only/fixed content
3. Accumulation — as data increases, frequency of access per piece drops; very little old content thrown away; compliance reinforces this
4. Redundancy — more copies being made for faster access and better data protection

Most data is in middle age, where value is less, and where mid-line disk is most appropriate.

[Pages 10-12]
Where Content Resides

Figure 3: Storage Pyramid — What Can Each Level Do Best
Source: Aberdeen Group, July 2003

- Solid-state disks: ultra-performance-intensive database applications
- High-performance FC/SCSI: mission-critical OLTP
- Mid-line ATA: fixed content, aged data, sequential-read applications
- Tape: backup/restore and off-site archiving

Guidelines for Matching Each Level to Application Data Requirements:

Database-based Applications:
1. Traditional OLTP (order entry): update-intensive; keep on high-perf disk; closed transactions (shipped orders) may move to mid-line
2. Contemporary "mixed" applications (e.g., SAP/R3): mix of writes and reads; if data can be segregated, mid-line may work
3. Business Intelligence / Data Warehousing: query intensive (sequential reads); mid-line storage can play a significant role; compelling cost-per-GB

File/Database Hybrid Applications:
- Web applications: hybrid; primarily random reads with some transaction processing; hybrid of mid-line + some high-perf may be suitable

File-based Applications:
- Personal productivity (word processing, e-mail): write-once then read many times
- Interactive design (CAD/CAM, post-production): mix of reads/writes on large data; identify inactive portions for mid-line
- Unique large files (X-rays, MRIs): fixed after creation; low access frequency; mid-line sufficient
- Large files for distribution (MP3, video): read-only copies; mid-line or high-perf depending on performance requirements

[Pages 12-13]
The Need for No Overall Increased Workload

Disk-based backup appliance example: includes array + specialized software; simplifies configuration; eliminates tape drive/media errors via RAID reliability.

ATA disks evolved from PC market; administrators may be concerned about availability. They should not be:
- ATA disk reliability has evolved to high level
- Individual disks protected as part of RAID group
- Higher capacity drives means fewer drives that can fail

Anticipate a period of "tuning" for proper balance of performance and capacity.

[Pages 13-14]
Mid-line Storage Adoption Strategies

Two approaches:
1. Embedded in array or storage appliance (incremental; case-by-case)
2. Proactive architectural planning (strategic; storage pyramid review)

Cost savings can be significant:
- SCSI disks can reach more than 5x the cost of ATA disks
- Mid-line solutions can be as much as half the price of high-performance disk-based systems
- 2 TB disk-based backup appliance: ,000-0,000 (ATA) vs 5,000-0,000 (SCSI)
- In 30TB+ FC environments: savings >00,000 off deals formerly 00,000+

Rethink the Storage Infrastructure:
- IT must adopt QoS perspective; not all applications require same service levels
- Create formal or informal service level agreements (SLAs)
- Long-term plan: storage utility as part of information utility
- Mid-line storage should be impetus to rethink entire storage infrastructure

[Pages 14-15]
Aberdeen Conclusions

Mid-line storage is a "quiet" storage revolution. Enterprises are still learning how to best use the new tier.

The mid-line storage tier gives the most cost-effective answer to:
1. Storing data that has aged and frozen into effectively read-only data that is too expensive on high-performance disk yet may have usage requirements unsuited for tape
2. Solving long-standing backup/restore process issues that tape alone could not handle

Enterprises that manage ILM effectively will:
- Cut costs for disk storage
- Balance performance to need more effectively
- Focus IT administrator resources more effectively
- Achieve greater overall scalability and flexibility

[Page 16]
Abstract:
White Paper: Mid-Line Disk Storage Emerging as Significant Cost-Saving Opportunity
Authors: Peter Kastner and David Hill
Keywords: mid-line, mid-line disk, mid-line disk storage, ATA, FC, Fibre Channel, SCSI, RAID, backup, backup/restore, storage, disk, storage pyramid, storage hierarchy, information life cycle, ILM
Coverage Area: Storage and Storage Management Practice

(C) 2003 Aberdeen Group, Inc. All rights reserved. June 2003
Aberdeen Group, Inc., 260 Franklin Street, Suite 1700, Boston, Massachusetts 02110-3112 USA
Telephone: 617 723 7890 | Fax: 617 723 7897 | www.aberdeen.com
This document is the result of sponsored research performed by Aberdeen Group.


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | mid-line-storage-white-paper-06-13-03-3-7a2c62 |
| title | Mid-Line Disk Storage: Emerging as Significant Cost-Saving Opportunity |
| author | Peter S. Kastner / Aberdeen Group |
| date | 2003-06-13 |
| type | white-paper |
| subject_domain | Enterprise Storage / Information Lifecycle Management |
| methodology | Primary market research; 75 face-to-face and telephone interviews with storage managers at companies $1B+ revenue; survey research; analyst field research |
| source_file | Mid-Line-Storage-White-Paper-06-13-03-3.doc |
| license | CC-BY-4.0 |

### Abstract

Seminal Aberdeen Group white paper defining "mid-line storage" as a new enterprise storage tier between high-performance Fibre Channel/SCSI disks and tape. Based on primary research with 75 storage managers at $1B+ enterprises. Defines four-level storage pyramid with mid-line ATA disks as a distinct tier. Key findings: ATA disks offer 2-8x capacity of FC/SCSI at ~half the cost per GB; 75% of storage buyers moderately or highly likely to purchase mid-line storage; over 60% report data restorations more than once a year; over 80% face backup window problems. Introduces Information Lifecycle Management (ILM) framework. Authored by Peter Kastner and David Hill of Aberdeen Group; sponsored by Maxtor Corporation.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | HIGH | Seminal white paper that defined and marketed the "midline storage" concept; co-invented by Kastner and Maxtor CMO Stephen DiFranco; shaped enterprise storage strategy for years to come |
| **Relevance** | HIGH | Serial ATA in enterprise storage became a massive market; this paper was ahead of the curve and accurately forecast SATA adoption |
| **Prescience** | HIGH | The midline storage concept proved enormously successful; SATA drives became the standard enterprise storage tier; ILM terminology became industry standard |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (4)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | acquired | Aberdeen (Harte-Hanks) |
| Maxtor Corporation | company | unknown | unknown |
| Peter S. Kastner | person | active |  |
| David Hill | person | unknown | unknown |

### Technologies Referenced (15)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Serial ATA (SATA) / ATA Disks | storage | Multiple (incl. Maxtor) | emerging | dominant |
| Fibre Channel (FC) Disk | storage | Multiple | dominant | unknown |
| SCSI Disk | storage | Multiple | dominant | unknown |
| Magnetic Tape (off-line storage) | storage | Multiple | current | unknown |
| RAID (Redundant Array of Independent Disks) | storage | Multiple | current | dominant |
| Storage Area Network (SAN) | network | Multiple | current | active |
| Network Attached Storage (NAS) | storage | Multiple | current | active |
| Continuous Data Protection (CDP) | storage | Multiple | emerging | unknown |
| Solid State Disk (SSD) | storage | Multiple | emerging | dominant |
| Storage Management / HSM Software | application | Multiple | current | unknown |
| Disk-Based Backup Appliance (ATA) | hardware | Multiple | emerging | unknown |
| Online Transaction Processing (OLTP) | application | Multiple | current | current |
| Data Warehouse / Business Intelligence | application | Multiple | current | active-evolved |
| SAP R/3 (mixed applications) | application | SAP | current | legacy-superseded |
| RAM-based Storage (volatile) | storage | Multiple | current | current |

### Observation Summary

- Total observations: 40
- By type: market-finding: 14, use-case: 5, framework-definition: 4, technology-comparison: 3, pricing-data: 3, technology-assessment: 3, recommendation: 3, market-assessment: 2, market-sizing: 1, research-methodology: 1, forecast: 1
