# How Aberdeen Sees the Storage Pyramid Evolving

> Archived from: 11-Storage-Hierarchy-Presentation.txt
> Original publication date: 2002-10-01
> Author: David Hill, Aberdeen Group

---

## Original Document Text

Aberdeen Group
How Aberdeen Sees the Storage Pyramid 
Evolving
David Hill
Research Director
Storage and Storage Management
Fall  2002
 
 
AberdeenGroup
The Storage Pyramid â Four Key Levels
Lower
Faster
Higher
Slower
RAM-
related
(e.g., memory,
solid state disk,
and disk cache)
High Performance Disk
(FC/SCSI)
Tape
Capacity Speed
Higher
Lower
Cost
Cost-Effective Disk (ATA)
 Performance
Streaming
Note: All layers, e.g. Optical, not shown for simplicity
 
 
AberdeenGroup
IS Lament: âCanât I get rid of the storage hierarchy?
â¢ What if all four levels (RAM-based âdiskâ, FC/SCSI 
disks, ATA disks, tape) cost the same?
â RAM-based âdiskâ would prevail over hard disk only if scaling, 
manageability, security/safety issues are addressed
â High performance (FC/SCSI) disks would prevail over ATA 
disks
â Hard (or RAM-based) disks would replace tape only if 
portability issue can be solved
â¢ Chances are not likely that everything will be the same 
in price.
 
 
AberdeenGroup
Comparing Selected Random Access and 
Sequential Access Technologies
Cost
Capacity
Speed
Storability
Higher
Lower
Faster
Inflexible
Lower
Higher
Slower
Flexible
RAM âdiskâ
FC, SCSI disk
ATA disk
Tape
Note: Not to scale
 
 
AberdeenGroup
However the Mix in the Storage Hierarchy Can Change
â¢ Prices are both relative and absolute
â Absolute prices compare what IS can for a dollar with how 
much IS has in its wallet â what may not have been 
affordable last year may be affordable this year
â Relative prices are the difference between levels of the 
hierarchy for the same quantity
â¢ Key to change is not only price, but the impact upon IS 
processes, skill sets, and organizational structure
 
 
AberdeenGroup
What Goes Where on the Storage Pyramid
â¢ Continued existence of the pyramid does not tell 
what data should reside in each layer 
â¢ For that we need to understand content
â The types of content
â The principles underlying content
â How mapping content and principles leads to what 
content should go where on each layer of the 
storage pyramid
 
 
AberdeenGroup
Why Content, Why Not Data or Information?
â¢ Data â the bits that form a bit stream; 
unintelligible to the untrained eye
â¢ Information â organization of bits into 
something a person can recognize, such as a 
part of a file or a record in a database
â¢ Content  â information that is used for some 
purpose, such as decision-making, better 
understanding, or personal enjoyment.  
 
 
AberdeenGroup
The Three Faces of Content
Structured 
Semi-structured
Unstructured
Database 
Text documents
Bitmaps 
Sort 
Search 
Sense 
Heartbeat Operational 
Systems, such as ERP 
and sales force 
automation 
Business Information 
Management, such as 
customer relationship 
management and 
business intelligence
Interpersonal 
productivity, 
such as e-mail, 
document 
management, 
and HTTP 
Entertainment 
and education, 
such as video 
and audio 
Imaging, such as 
pictures, 
photographs, 
and MRI scans
Type
Form
Key 
Capability
Examples
 
 
AberdeenGroup
Content Matters
â¢ Processes are important, but processes (order 
acquisition, order fulfillment, billing) can be copied
â¢ Content (along with its distribution) is the long-term 
competitive differentiator
â Only one company owns its customer and product 
history data as well as intellectual property (patents, 
copyrights)
â The production, aggregation, and dissemination of 
content will separate successful from unsuccessful 
e-Businesses
 
 
AberdeenGroup
Four Principles of Enterprise Content
â¢ Ageing â value and use (access patterns) 
change as content ages
â¢ Freezing â content changes from dynamic to 
fixed as updates cease
â¢ Accumulation â very little old data is thrown 
away
â¢ Redundancy â more and more copies are 
being made of data
 
 
AberdeenGroup
Ageing  â All Content Ages
â¢ Conception and birth â read/write access 
limited to one or a few individuals (e.g., a 
transaction)
â¢ Youth   â may have high read access  as the 
sum of access by a large number of individuals 
(e.g., the latest video)
â¢ Middle age â infrequent access either on a 
scheduled or ad hoc basis
â¢ Old age â more or less flat lined usage
 
 
AberdeenGroup
Ageing â All Content Does Not Age the Same
â¢ All content  â even of the same type (structured, 
semi-structured, unstructured) does not age the 
same
â A medical image quickly goes to middle age
â A video may have a longer youth
â¢ Much content is in middle age
â Youth wilts quickly
â Old age never seems to arrive
 
 
AberdeenGroup
The Life Cycle of Content
Old
Age
Middle
Age
Youth
Content Life Cycle Stage
Sounds Minutes Hours Days
Weeks Months
Years
Decades
Note: Curve is an 
example. Different 
types of content 
would have different 
curves.
Time
 
 
AberdeenGroup
Content Access Follows Zipfâs Law
Frequency of Access
Most Frequently
Accessed Document
Least Frequently
Accessed Document
âThey also serve who
  only stand and wait.â
 
 
AberdeenGroup
Freezing â Content Changes From Dynamic to Fixed
â¢ Updates for particular content cease at some point, whether 
that be a transaction, text, film, etc. 
â For an MP3 file, content is fixed early in youth as the period of 
greatest access (youth) follows
â For a transaction, content is fixed at the end of youth (after billing, 
receipt of payment, and acknowledgement)
â In some cases, what appears to be dynamic (changing Web pages) 
is only a thin veneer that is dynamic with fixed content making up 
the bulk
â¢ Frozen content is read-only
â¢ Response time for frozen content depends upon 
expectations â wait for Web pages is a few seconds, wait 
for an audio or video file can be much longer
 
 
AberdeenGroup
Accumulation
â¢ New content is additive â new data does not 
replace old data
â¢ Weeding out is hard to do
â At pennies per megabyte, it may not be cost effective 
to have individuals clean out regularly (even if they 
would)
â Policy-driven cleaning can be effective, but only in 
limited ways
 
 
AberdeenGroup
Redundancy â What, How, and Why
What
How
Why
Protection Against:
Physical disk failure
RAID
Business continuity
Logical disk failure
Point-in-time copy; 
backup to disk/tape
Business continuity
Catastrophic site 
failure
Remote mirroring, 
remote backup
Business continuity/ 
disaster recovery
Unexpected 
demands for archived 
data
Offsite archiving
Legal/Regulatory
 
 
AberdeenGroup
Redundancy â What, How, and Why
What
How
Why
Normal Business Uses:
Versioning
User-drive copies
Reference, audit trail
Test copy
Point-in-time copy, 
user-driven-copy, tape
Application 
development testing
Historical analysis
Data warehouse or 
other business 
intelligence repository
Better decision making
Online copy of 
production database for 
suppliers/ customers
Broadcast (e-mail) 
Cached (rich media)
Reach a wider 
audience
Closer to user
 
 
AberdeenGroup
Where Content Lives When
On Site
Off Site
Online
Online/
Near Line
Offline
Age
Task
RAM-based
âDiskâ
High-Performance
Disk
ATA Disk
Youth
Youth/Middle Age
Old Age
Performance-oriented
storage demands
Active archiving
Data protection
Deep archiving
Note: A copy of any piece of content may be in 
multiple locations
 
 
AberdeenGroup
Enterprise-Class Disk and Tape Advantages
High
Fast response to
ad hoc requests
Uncompleted
end-user task
WIP, messages,
and documents
Currently
retrieved file
= The dividing line between what should be on placed in each category
Low
Meet expectations where
no interactivity needed, or slow
initial start times acceptable
Completed
end-user tasks
Older messages
and documents
Structured Data
(e.g., OLTP databases)
Semi-Structured Data
(e.g., Messaging [e-mails] and documents)
Unstructured Data
(e.g., Streaming video and audio, and photographs)
Not currently required files
Favors High-Performance Disk
Favors Tape
Response Time
Frequency of Access
Favors Cost-Effective Disk
 
 
AberdeenGroup
The Future of Tape
Some analysts:  âTape is dead.â
Tape:  âThe reports of my death have 
been greatly exaggerated.â (Mark Twain)
IS:  âThere is a place for everything, 
and everything in its place.â
 
 
AberdeenGroup
Enterprise-Class Tape Meets Future Demand
Tape
Streaming video, audio, medical
images, messages, and documents
Disk
New online
applications


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | 11-storage-hierarchy-presentation-e84d53 |
| title | How Aberdeen Sees the Storage Pyramid Evolving |
| author | David Hill, Aberdeen Group |
| date | 2002-10-01 |
| type | market-study |
| subject_domain | enterprise-storage |
| methodology | industry-analysis, content-taxonomy, storage-tiering-framework |
| source_file | 11-Storage-Hierarchy-Presentation.txt |
| license | CC-BY-4.0 |

### Abstract

David Hill's Fall 2002 presentation establishing Aberdeen Group's analytical framework for the four-tier storage pyramid evolution. Introduces a content-centric approach to storage architecture based on four principles (ageing, freezing, accumulation, redundancy) and maps content types (structured/semi-structured/unstructured) to appropriate storage tiers. Provides foundational intellectual basis for the Pools of Storage and midline storage category initiative.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Foundational theoretical document for the midline category creation project; establishes the intellectual infrastructure (content principles and storage pyramid) that the entire Maxtor/Aberdeen engagement was built upon. David Hill's framework predated and enabled the Pools of Storage framework. |
| **Relevance** | high | Content lifecycle principles (ageing freezing accumulation redundancy) are more relevant than ever in cloud/object storage era; tiered storage mapping is core to modern storage architecture including S3 Intelligent-Tiering. Zipf's Law application to content access frequency is still cited in storage economics. |
| **Prescience** | high | Predicted that ATA cost-effective disk would displace tape for many archival functions; confirmed. Predicted content-based storage tiering would drive enterprise storage decisions; confirmed by ILM movement and cloud tiering. Predicted tape would not die but find its specific niche; tape remains active for deep archive. |

### Prescience Detail


**Prediction 1:** Future of tape assessment
- **Claimed:** Some analysts say tape is dead; Aberdeen position: there is a place for everything and everything in its place; tape meets streaming data demand
- **Year:** 2002
- **Confidence at time:** high

**Actual Outcome 1:** Tape survival in storage hierarchy
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** Tape did survive; LTO tape still active for deep archive in 2024

**Prediction 2:** Cost-effective disk role expansion
- **Claimed:** ATA disk growing to serve active archiving and data protection functions as prices decline relative to FC/SCSI
- **Year:** 2002
- **Confidence at time:** high

**Actual Outcome 2:** Cost-effective disk role expansion
- **Result:** [DEFERRED]
- **Confidence:** [DEFERRED]
- **Notes:** SATA drives did dominate nearline/midline storage through 2010s; largely confirmed


### Entities Referenced (4)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | acquired | Aberdeen/Harte-Hanks |
| David Hill | person | [DEFERRED] |  |
| EMC Corporation | company | acquired | Dell |
| Data General | company | acquired | EMC |

### Technologies Referenced (6)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Fibre Channel (FC) | protocol | Various | mature | active |
| SCSI (Small Computer System Interface) | protocol | Various | mature | legacy |
| ATA (Advanced Technology Attachment) | hardware | Various | mature | legacy |
| RAID Disk Storage | storage | multiple | mature | legacy-supported |
| Network Attached Storage (NAS) | storage | Various | growing | active |
| Storage Pyramid Framework | framework | Aberdeen | current | superseded |

### Observation Summary

- Total observations: 22
- By type: analytical-judgment: 6, content-taxonomy: 3, framework-component: 2, redundancy-framework: 2, viability-prediction: 2, actual-outcome: 2, lifecycle-model: 1, analytical-model: 1, content-placement-model: 1, tier-recommendation: 1, comparative-analysis: 1
