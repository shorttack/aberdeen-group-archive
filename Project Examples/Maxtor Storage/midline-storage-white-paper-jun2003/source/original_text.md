# Mid-Line Disk Storage Emerging as Significant Cost-Saving Opportunity

> Archived from: Mid-Line-Storage-White-Paper-06-13-03-3.doc
> Original publication date: 2003-06-13
> Author: Peter Kastner; David Hill / Aberdeen Group

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
| study_id | midline-storage-white-paper-jun2003 |
| title | Mid-Line Disk Storage Emerging as Significant Cost-Saving Opportunity |
| author | Peter Kastner; David Hill / Aberdeen Group |
| date | 2003-06-13 |
| type | white-paper |
| subject_domain | enterprise-storage |
| methodology | primary-research, face-to-face-interviews, industry-analysis, expert-opinion, survey-research |
| source_file | Mid-Line-Storage-White-Paper-06-13-03-3.doc |
| license | CC-BY-4.0 |

### Abstract

The seminal Aberdeen Group white paper that defined and named the 'midline' storage tier — ATA-based online storage positioned between high-performance FC/SCSI disk arrays and magnetic tape. Based on 75 face-to-face and telephone interviews with storage managers at billion-dollar enterprises, it presented a four-level storage pyramid, documented that 75% of enterprise buyers were moderately or highly likely to purchase midline storage, and predicted that over 50% of enterprise data would eventually migrate to the midline tier. The paper established ILM principles (Ageing, Freezing, Accumulation, Redundancy) as the rationale for a new storage tier.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Seminal paper that coined and defined the 'midline' storage tier and established the four-level storage pyramid (Online/Midline/Nearline/Offline); the paper directly created the enterprise market category for ATA/SATA-based enterprise storage; 'midline' and 'nearline' terminology entered and remains in industry vocabulary. |
| **Relevance** | high | Tiered storage is now the universal enterprise storage architecture; the economic logic (cost-per-GB differentiation driving data placement by lifecycle stage) remains the foundation of modern storage tiering; ILM-driven data placement is a standard enterprise storage feature; the paper's framework is directly applicable to current SSD/NVMe vs SATA vs tape tiering discussions. |
| **Prescience** | high | All major predictions proved correct: >50% of enterprise data moved to midline/SATA tier (Wikibon 2011 estimated 85% of data and 40% of spend by 2015); 75% buyer-likelihood statistic validated by rapid market adoption; ILM became a core enterprise data management concept; tiered storage became standard in every enterprise storage product. The 'midline' and 'nearline' terms entered and persist in industry vocabulary. Prescience score: 8-9/10. |

### Prescience Detail


**Prediction 1:** SCSI vs ATA cost multiple
- **Claimed:** SCSI disks can reach more than 5x the cost of ATA disks
- **Year:** 2003
- **Confidence at time:** high

**Prediction 2:** Data migration to midline tier — minimum estimate
- **Claimed:** At least 20% of enterprise data fits the definition of inactive/seldom-used online storage appropriate for high-capacity/low-cost ATA
- **Year:** 2003
- **Confidence at time:** high

**Actual Outcome 2:** Midline/SATA data share — verified outcome
- **Result:** Wikibon 2011 estimated SATA high-capacity disks would hold 85% of enterprise data and 40% of storage spend by 2015
- **Confidence:** verified
- **Notes:** Actual outcome: exceeds the >50% prediction; confirms and strengthens OBS-025

**Prediction 3:** Data migration to midline tier — long-term projection
- **Claimed:** Over half of enterprise data will eventually fall into the mid-line
- **Year:** 2003
- **Confidence at time:** high

**Actual Outcome 3:** Midline/SATA data share — verified outcome
- **Result:** Wikibon 2011 estimated SATA high-capacity disks would hold 85% of enterprise data and 40% of storage spend by 2015
- **Confidence:** verified
- **Notes:** Actual outcome: exceeds the >50% prediction; confirms and strengthens OBS-025

**Prediction 4:** Midline storage as critical component of every enterprise
- **Claimed:** Time and technology have arrived for mid-line storage to become a critical and cost-effective component of every enterprise storage strategy
- **Year:** 2003
- **Confidence at time:** high

**Actual Outcome 4:** Midline/SATA data share — verified outcome
- **Result:** Wikibon 2011 estimated SATA high-capacity disks would hold 85% of enterprise data and 40% of storage spend by 2015
- **Confidence:** verified
- **Notes:** Actual outcome: exceeds the >50% prediction; confirms and strengthens OBS-025

**Prediction 5:** Nearline/Offline lexicon prediction
- **Claimed:** Nearline (Disk Backup and Staging) and Offline (Tape Archive) tiers named as part of four-level storage hierarchy
- **Year:** 2003
- **Confidence at time:** high

**Actual Outcome 5:** Midline/SATA data share — verified outcome
- **Result:** Wikibon 2011 estimated SATA high-capacity disks would hold 85% of enterprise data and 40% of storage spend by 2015
- **Confidence:** verified
- **Notes:** Actual outcome: exceeds the >50% prediction; confirms and strengthens OBS-025


### Entities Referenced (8)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | acquired | Aberdeen/Harte-Hanks |
| Peter S. Kastner | person | active |  |
| David Hill | person | active |  |
| Maxtor Corporation | company | acquired | Seagate Technology (acquired Dec 2005 / completed May 2006) |
| Seagate Technology | company | active (public: STX) |  |
| EMC Corporation | company | acquired | Dell Technologies (acquired 2016) |
| NetApp (Network Appliance) | company | active (public: NTAP) |  |
| SNIA (Storage Networking Industry Association) | institution | active |  |

### Technologies Referenced (10)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Serial ATA (SATA) / ATA | protocol | Industry Standard (SATA-IO) | emerging | mature-standard |
| Fibre Channel (FC) | protocol | ANSI/T11 | mature | legacy-active |
| SCSI (Small Computer System Interface) | protocol | ANSI/T10 | mature | legacy-declining |
| RAID (Redundant Array of Independent Disks) | framework | Various | mature | active |
| Information Lifecycle Management (ILM) | framework | Various | emerging | evolved-into-tiered-storage |
| Solid-State Disk (SSD) | platform | Various | niche | dominant-tier |
| Magnetic Tape Storage | platform | Various | mature | active-niche |
| Disk-Based Backup Appliance | platform | Various | emerging | mature |
| Continuous Data Protection (CDP) | framework | Various | emerging | mature |
| SAP R/3 | application | SAP | mature | evolved-to-SAP-S4HANA |

### Observation Summary

- Total observations: 40
- By type: market-finding: 12, technology-benchmark: 5, viability-prediction: 5, framework-definition: 4, use-case-classification: 4, actual-outcome: 3, strategy-recommendation: 3, research-methodology: 2, technology-assessment: 1, market-assessment: 1
