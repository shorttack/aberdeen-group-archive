# Mid-Line Disk Storage Emerging As Significant Cost-Saving Opportunity

> Archived from: 04-Mid-Line-Storage-V2-WhitePaper.txt
> Original publication date: 2003-08-01
> Author: Aberdeen Group

---

## Original Document Text

AberdeenGroup 
 
 
 
 
 
 
 
 
 
 
 
 
Mid-Line Disk Storage 
Emerging As Significant 
Cost-Saving 
Opportunity 
An Executive White Paper 
August 2003 
 
 
 
 
 
Aberdeen Group, Inc. 
260 Franklin Street 
Boston, Massachusetts 02110-3112 USA 
Telephone: 617 723 7890 
Fax: 617 723 7897 
www.aberdeen.com 
 
 
 
Mid-Line Disk Storage Emerging As Significant Cost-
Saving Opportunity 
Executive Summary 
After extensive field research conducted on the use of storage in the second quar-
ter of 2003, Aberdeen Group concludes that the old aphorism, “If all you have is a 
hammer, everything looks like a nail,” is widely true of enterprise storage. More 
than half of enterprises are completely run online using Fibre Channel (FC) and 
Small Computer System Interface (SCSI) disks. FC/SCSI disks are fast and reliable. 
They also are used a great deal of the time; that is, they have a high duty cycle. 
However, they are also much lower in capacity and much higher in cost relative to 
an emerging class of enterprise storage, Advanced Technology Attachment (ATA) 
disks. This Executive White Paper presents Aberdeen’s revised model for enter-
prise storage, carving out a middle tier — the mid-line — for ATA disks. It includes 
our most recent field research findings, conclusions, and recommendations to en-
terprise storage buyers.  
Mid-line storage is defined as high-capacity online ATA disks, which are in the 
middle tier between high-use FC/SCSI disk arrays and tape libraries. Today, the re-
quirements that can be met effectively using ATA disks are being serviced by rela-
tively expensive FC/SCSI disk arrays or by slow-to-restore tape.  
Mid-line storage is specifically aimed at data that not only needs to be online (i.e., 
provide reasonable response-time to read requests) but also has moderate access 
and rate-of-change requirements (as opposed to heavy-duty online transaction 
processing).  
ATA disks are not new. The technology has been used in PCs for years. The reliabil-
ity of ATA disk storage has risen enough so that it can safely accommodate low fre-
quency of access demands (i.e., a low duty cycle).  
Mid-line storage using enterprise ATA disks has the benefits of two to eight times 
the storage capacity of FC/SCSI — up to 300 GB per ATA disk compared with 
142/72/36 GB per FC/SCSI disk. ATA disks are about half the cost per gigabyte. 
The raison d'être for a new mid-line storage tier is fourfold: 
1. Move inactive and seldom-used online storage, which represents a mate-
rial factor in overall storage cost of ownership, to high-capacity/low-cost 
ATA disks. Examples include online archives, old e-mails, desktop backups, 
old versions of computer programs, log files, and images such as CAD/CAM 
designs. In a recent Aberdeen survey on the use of storage, respondents 
said that at least 20% of enterprise data fits this definition — and we believe 
more than half will eventually fall into the mid-line. 
2. Move applications with inactive and seldom-used data characteristics to 
mid-line storage. An example is a data warehouse with large detail tables. 
 
Mid-Line Disk Storage Emerging As Significant Cost-Saving Opportunity 
 2 
© 2003 Aberdeen Group, Inc. 
Telephone: 617 723 7890 
260 Franklin Street 
Fax: 617 723 7897 
Boston, Massachusetts 02110-3112 
www.aberdeen.com 
 
3. Improve the data restoration process. More than 60% of survey 
respondents report that data restorations are performed more than once a 
year — 20% report a data restore monthly or more frequently. The labor 
costs of file restorations are well known to be very high, and restoration 
typically has a business-interruption cost as well. Mid-line storage can pro-
vide an economical online backup of one or more data versions.  
4. Improve backup windows. Data backup windows are too short for a large 
majority of the survey respondents. The inability to get critical files offline 
to tape is often a gating item to the next day’s mission-critical system start-
up. Disk-based backup can compress the backup window by writing to an 
array of mid-line disks that are dedi-
cated to this purpose. 
The storage ecosystem is complex, and stor-
age buyer inertia is well known. Mid-line stor-
age is emerging in spite of those barriers be-
cause it has the support of the major disk 
drive manufacturers, the storage systems sup-
pliers, and early adopters. The fact that mid-
line storage can be added to today’s direct-
attached storage area network (SAN) and 
network-attached storage (NAS) products eliminates concerns about radical 
change in a very conservative IT environment — data management.  
Aberdeen Group research, 
backed by our industry 
experience, indicates that the 
time and technology have 
arrived for mid-line storage to 
become a critical and cost-
effective component in every 
enterprise storage strategy. 
Aberdeen research indicates that 75% of storage buyers are moderately or highly 
likely to buy mid-line storage in the coming year. This finding bodes well for early 
market acceptance.  
Aberdeen Group makes the following recommendations:  
• Storage planners need a better understanding of the applications and 
files that could benefit from mid-line technology.  
• Buyers should examine how much new capacity should be devoted to 
mid-line technology while planning new and replacement applications 
with an eye toward splitting storage requirements between mid-line and 
traditional FC/SCSI online storage. This strategy requires a revised stor-
age planning process. 
• Backup, restore, and copy-retention labor-cost issues are key. The great-
est savings will come with management tools that enable the effective 
use of the mid-line tier for these data protection purposes.  
With the emergence of the mid-line tier, planners need to rethink their long-term 
strategy to manage storage and the tools to implement it. 
Mid-Line Disk Storage Emerging As Significant Cost-Saving Opportunity 
 3 
© 2003 Aberdeen Group, Inc. 
Telephone: 617 723 7890 
260 Franklin Street 
Fax: 617 723 7897 
Boston, Massachusetts 02110-3112 
www.aberdeen.com 
 
Aberdeen Group research, backed by our industry experience, indicates that the 
time and technology have arrived for mid-line storage to become a critical and 
cost-effective component of every enterprise storage strategy.  
Make Room, Make Room — The Arrival of Mid-Line Disk Storage 
Enterprises are familiar with layers of the storage pyramid (aka storage hierarchy) 
— high-speed but volatile random access memory (RAM)-based devices, Winches-
ter disks, and sequential-access tape (Figure 1). (Optical storage also plays a role, 
but will be left out of this discussion.) From a pure storage perspective, enterprises 
typically have thought in terms of disk and tape. Moreover, enterprise disk storage 
has typically been thought of as FC and SCSI disks, which Aberdeen calls high-
performance disks. 
However, a new level of disk that is based on ATA technology is rapidly emerging. 
Aberdeen terms this level of the pyramid mid-line storage. Mid-line storage is  
Figure 1: The Storage Pyramid — Four Key Levels 
 
Source: Aberdeen Group, August 2003 
Mid-Line Disk Storage Emerging As Significant Cost-Saving Opportunity 
 4 
© 2003 Aberdeen Group, Inc. 
Telephone: 617 723 7890 
260 Franklin Street 
Fax: 617 723 7897 
Boston, Massachusetts 02110-3112 
www.aberdeen.com 
 
online storage that sits between high-performance disk and tape. It will not re-
place high-performance disk or tape, but it will dramatically change how each is 
used, and it will play both a complementary and supplemental role. Mid-line stor-
age will have its own ecological niche in the storage hierarchy. 
Mid-line storage has a cost and capacity advantage with respect to high-
performance disk. Applications that are not write-performance bound, such as 
read-only, fixed content (aka reference or recallable) data, will gravitate toward 
mid-line storage. Mid-line storage that has a long working life (e.g., 10 years) at a 
very low duty cycle would be attractive for long shelf-life data, such as MRI files. 
Mid-line storage has a speed and random access advantage with respect to tape 
storage. That speed is especially important when the time to restore data is critical 
enough to justify a cost difference between mid-line storage and tape. Disk-based 
data restoration is one way to achieve this goal. Another method is an emerging 
concept called continuous data protection that quickly restores data to any point 
in time.  
Mid-Line Storage Is Already Moving into the Enterprise 
To examine the need for and the progress in implementing mid-line storage, Aber-
deen conducted primary market research that included 75 face-to-face and tele-
phone interviews with storage managers at 
companies with $1 billion or larger in revenue, 
including several Fortune 50-size businesses in 
the U.S. with financial services industries over-
represented and government and nonprofits 
underrepresented.  
The research covered storage that is accessed 
by servers using the three basic types of operating systems: mainframe, Windows, 
and Unix/Linux.  
Applications that are not 
write-performance bound, 
such as read-only, fixed 
content (aka reference or 
recallable) data, will gravitate
toward mid-line storage. 
Enterprises show a strong willingness to consider higher capacity disks with 
slightly less performance, but with at least a significant cost reduction from current 
capacity disks — characteristics that distinguish mid-line disks from high-perfor-
mance disks. More than one quarter of respondents showed a high willingness to 
purchase such disks, and nearly half showed a moderate willingness to purchase 
such disks. Only about one-quarter showed little or no willingness to purchase 
such disks.  
Respondents were asked whether their current storage supplier(s) had discussed 
their low-cost storage options with them, and 60% responded yes. Respondents 
were then asked how likely they were to purchase low-cost storage. The response 
to purchase low-cost disk storage was remarkably high — two-fifths said highly 
likely, one-third said moderately likely, and only one-quarter said unlikely. The  
Mid-Line Disk Storage Emerging As Significant Cost-Saving Opportunity 
 5 
© 2003 Aberdeen Group, Inc. 
Telephone: 617 723 7890 
260 Franklin Street 
Fax: 617 723 7897 
Boston, Massachusetts 02110-3112 
www.aberdeen.com 
 
implication of these results is that IT organizations are generally willing to con-
sider disk storage options other than what they already use. However, Aberdeen 
must add the cautionary note that respondents may not have a clear understand-
ing of what low-cost disk storage really is. 
Respondents were asked whether they had any single applications with very large 
non-changing/static data, such as video data, images, data warehouse detailed data, 
and old e-mails, and 60% responded yes. This data is typically read-only and does 
not have the same performance demands of an online transaction processing 
(OLTP) application. This finding indicates that higher capacity and lower cost disks 
could play a significant role in satisfying these demands.  
Another potential role for mid-line storage is in the area of improving the 
backup/restore process, which has also been noted as an area of significant con-
cern in previous Aberdeen research. For example, based on Aberdeen’s current 
research: 
• Nearly two-thirds of the respondents said that restoring critical data 
takes longer than they would like.  
• About half said that the operational management required to manage 
the backup process is a burden and a management concern.  
• Close to half would not guarantee that all critical data can be restored 
on a given day.  
• More than four-fifths said that when offline backups are used, they could 
have a problem with the length of the backup window. 
These results indicate that there is an opportunity for mid-line storage to help in 
alleviating these problems. High-performance disks could also conceivably be used 
for this purpose, but even though the price of FC and SCSI drives has fallen dra-
matically over the years, price elasticity curve economics still apply. Mid-line stor-
age is less costly and can do the job just as well as FC/SCSI disks. Mid-line storage 
is the superior choice to alleviate problems in the backup/restore process. 
The Information Life Cycle — Managing Content on the Storage Pyramid 
It is generally recognized that data goes through a life cycle. As data ages, the value 
of the data tends to diminish along with the need to access the data. However, dif-
ferent applications and different collections of data can vary greatly. Mid-line stor-
age falls between high-performance disk and tape (i.e., tape libraries) in this life 
cycle (Figure 2). 
The term “information life cycle management” (ILM) is typically used for how data 
will move around the storage pyramid over time. The continued existence of the 
pyramid does not tell us what data (and, by implication, what kind of applications 
Mid-Line Disk Storage Emerging As Significant Cost-Saving Opportunity 
 6 
© 2003 Aberdeen Group, Inc. 
Telephone: 617 723 7890 
260 Franklin Street 
Fax: 617 723 7897 
Boston, Massachusetts 02110-3112 
www.aberdeen.com 
 
that use that data) should reside in each layer. Once the types and principles un-
derlying the life cycle of data (aka information or content) are understood, the 
mapping of what data to what level on the storage pyramid can take place. 
Four basic principles for ILM are: 
• Aging — Value and use of content (access patterns) change as content 
ages (birth, youth, middle age, and old age); as information passes 
through the various stages of life, the need to access that data tends to 
drop dramatically. 
• Freezing — Content changes from dynamic to fixed as updates cease; 
thus, the content becomes — for all practical purposes — read-only and, 
therefore, fixed content. 
Figure 2: Where Mid-Line Storage Fits 
 
Source: Aberdeen Group, August 2003 
Mid-Line Disk Storage Emerging As Significant Cost-Saving Opportunity 
 7 
© 2003 Aberdeen Group, Inc. 
Telephone: 617 723 7890 
260 Franklin Street 
Fax: 617 723 7897 
Boston, Massachusetts 02110-3112 
www.aberdeen.com 
 
• Accumulation — As the amount of data increases, the frequency with 
which a particular piece of data is accessed drops. Very little old content 
is thrown away. Compliance with new regulations will further reinforce 
this tendency. 
• Redundancy — More copies are being made of content to ensure faster 
access and better data protection. 
Together, these principles explain a lot of the growth in storage.  
Storage growth puts pressure on IT organizations to move content down the stor-
age hierarchy stack as quickly as possible to reduce costs and simplify storage 
management (Figure 3). Most data is in middle age, where the value is less, and 
where mid-line disk is most appropriate. Data in middle age is typically frozen, so 
the lower access requirements play to the strength of mid-line disk. And where ac-
cumulated older information or extra copies must reside on disk, mid-line storage 
is an appropriate choice — for example, old versions of content, such as CAD 
drawings and Web sites, that need to be online-recallable, but have only intermit-
tent, ad hoc access requirements. Last year’s Christmas Web site for a retailer may 
prove useful as a starting point for this year’s Christmas Web site. 
Figure 3: Storage Pyramid — What Each Level Does Best 
 
Source: Aberdeen Group, August 2003 
Mid-Line Disk Storage Emerging As Significant Cost-Saving Opportunity 
 8 
© 2003 Aberdeen Group, Inc. 
Telephone: 617 723 7890 
260 Franklin Street 
Fax: 617 723 7897 
Boston, Massachusetts 02110-3112 
www.aberdeen.com 
 
Where Content Resides 
The net result is that a lot of content is in middle age and frozen. That means that 
it is read-only and has a lower pattern of access, meaning performance require-
ments are not as important. Lower cost, higher capacity disk storage can meet 
these needs. Therefore, mid-line disk can handle a large proportion of the typical 
enterprise’s content. 
Where content resides depends on performance requirements (Figure 3). Ultra-
performance-intensive database applications can benefit from solid-state disks. 
Mission-critical OLTP applications will continue to benefit from high-performance 
disks. But a lot of content is fixed and can effectively function at the mid-line level 
of the storage pyramid. Tape will also continue to perform an essential role for 
backup/restore and off-site archiving. 
Guidelines for Matching Each Level to Application Data Requirements 
Aberdeen’s research indicates that enterprises are not clear on what data is read-
only or seldom read. The reason for this uncertainty seems to be that it is difficult 
to logically separate the application that processes the data from the data that is 
used in conjunction with the application. Take, for example, e-mail: a user can cre-
ate e-mail, reply to it, or forward an e-mail that has been received. This write activ-
ity uses more disk space (either at the sender’s or respondent’s end or both). 
However, unless e-mail is deleted right after it is read, the bulk of e-mail is effec-
tively “near-read-only.”  
Applications can essentially be categorized into database-based applications and 
file-based applications. There are several key types of applications in each category, 
and each may or may not be able to use mid-line disk storage. The key is to deter-
mine when a database record or file ages enough so that it frozen into effectively 
read-only status and when it makes sense (managerially and cost-wise) to separate 
those records and files from high-performance disk to mid-line disk.  
Database-Based Applications 
Traditional Online Transaction Processing 
OLTP applications, such as order entry, are typically update-intensive (both reads 
and writes, but the focus is on writes). Performance requirements typically mean 
that high-performance disk is best for these applications. However, closed transac-
tions, such as shipped orders, may make good candidates to be transferred to mid-
line storage. Clearing out the hardened data arteries could restore much-needed 
performance to the OLTP application. As an additional benefit, a two-tier database 
would be easier to back up and restore as necessary.  
 
Mid-Line Disk Storage Emerging As Significant Cost-Saving Opportunity 
 9 
© 2003 Aberdeen Group, Inc. 
Telephone: 617 723 7890 
260 Franklin Street 
Fax: 617 723 7897 
Boston, Massachusetts 02110-3112 
www.aberdeen.com 
 
Contemporary “Mixed” Applications (Such As SAP/R3) 
These applications have a mix of writes and reads — updating for transactions, but 
also random reads of reference data. If the data can be clearly segregated as to 
what is what, then mid-line storage might be able to serve in a complementary 
role. This is most easily accomplished when the application is planned or newly 
implemented.  
Business Intelligence 
Demands for business intelligence applications, such as data warehousing, are in-
creasing in order to take advantage of the data created by OLTP systems. These ap-
plications are query intensive (e.g., primarily sequential reads). Depending on per-
formance and capacity requirements, mid-line storage can play a significant role. 
Mid-line storage may actually expand the market by making it more cost-effective 
to build a data warehouse/data mart or to do data mining. The cost per gigabyte of 
mid-line storage is compelling for business intelligence applications. 
File/Database Hybrid Applications 
Web applications are frequently a hybrid of files and databases — for example, 
providing text for product information and using a database for credit verification, 
order entry, and order management. These types of applications involve primarily 
random reads with a little transaction processing. A hybrid of mid-line storage, 
along with some high-performance disks, may be a suitable combination.  
File-Based Applications 
Many file-based applications are appropriate targets for mid-line storage, as fol-
lows: 
• Personal productivity — Word processing, e-mail, and other office ap-
plications are productivity tools for an enterprise. They are primarily 
write-once (albeit perhaps spanning a period of time and involving some 
collaboration), but then read many times.  
• Interactive design  CAD/CAM and post-production editing are exam-
ples of interactive design applications. These are likely to include a mix 
of reads and writes on large pieces of data. IT managers have to figure 
out what part of the information is more or less inactive and can, there-
fore, be appropriately moved to mid-line storage.  
• Unique large files — These are files of unstructured data, such as X rays 
and MRIs. After creation, the content of the file is fixed (in fact, inalter-
able should be an attribute of the file) and is, therefore, read-only. Low 
frequency of access means that a high-performance disk is not needed 
for this type of content. Mid-line disk is sufficient.  
Mid-Line Disk Storage Emerging As Significant Cost-Saving Opportunity  10 
© 2003 Aberdeen Group, Inc. 
Telephone: 617 723 7890 
260 Franklin Street 
Fax: 617 723 7897 
Boston, Massachusetts 02110-3112 
www.aberdeen.com 
 
• Large files for distribution — These files  (e.g., video training, corporate 
images, and rich media) are copies of originals and may be distributed 
many times in many locations. These files previously created large bit-
mapped files and have read-only access. Performance requirements may 
cause a move to high-performance or mid-line disks.  
The Need for No Overall Increased Workload 
IT managers already have to deal with very complex infrastructures, so they do not 
want to introduce a new tier of storage if it means increasing complexity or creat-
ing additional administrative burdens. Inserting mid-line disk in an environment 
means introducing change through acquiring a storage appliance, purchasing a 
new disk array, or adding mid-line disks to an existing array. Change for the better 
improves overall storage administration. 
Consider disk-based backup, for example. One way to do disk-based backup is to 
put in an appliance that includes both a storage array and new specialized soft-
ware to manage the array. Simplification of the configuration and management of 
the backup means that an administrator no longer has to worry about how to fit a 
new backup requirement onto already overused scarce tape drives. Learning a new 
software tool to manage the appliance is well worth the time, not to mention the 
higher completion rate of backup jobs through eliminating tape drive and tape 
media errors by substituting RAID-based disk reliability. 
A similar situation would occur for a storage appliance that stores fixed content 
and for a storage array that embeds high-performance and mid-line disks. Separat-
ing high-performance disks from mid-line disks should make the management of 
each easier, such as eliminating the time taken to figure out how to get more per-
formance out of and reduce the backup window for high-performance disk. 
Mid-line Storage Adoption Strategies 
Enterprises can use two approaches to adopting mid-line storage. The first ap-
proach adopts mid-line storage that is embedded in an array or a storage appli-
ance. The second takes a proactive stance and plans how each layer of the storage 
pyramid can be best used. Then case-by-case decisions can be made in the context 
of the overall strategy. 
Making a decision to use mid-line disk storage is not a decision to buy mid-line 
disks by themselves, but rather a decision to acquire an array or a storage appli-
ance that helps a business application perform more cost-effectively. Deciding the 
use of mid-line storage on a case-by case basis, such as for a fixed content appli-
ance or a data protection appliance, has advantages — buyers can focus on a single 
decision from a cost/benefit perspective and the minimization of impact on IT or-
ganizations by making only incremental storage infrastructure changes.  
Mid-Line Disk Storage Emerging As Significant Cost-Saving Opportunity  11 
© 2003 Aberdeen Group, Inc. 
Telephone: 617 723 7890 
260 Franklin Street 
Fax: 617 723 7897 
Boston, Massachusetts 02110-3112 
www.aberdeen.com 
 
This advantage may be important for networking storage, such as adding disk-
based backup into a storage area network (SAN) or adding a fixed content appli-
ance to the corporate network. In these cases, the management software necessary 
to run the appliance is included with the appliance hardware. 
Cost savings can be significant. Although the cost of SCSI disks can easily reach 
more than five times the cost of ATA disks, IT organizations typically buy complete 
solutions, and some mid-line storage-based solutions can be as much as half the 
price of high-performance disk-based systems. For example, a 2-TB disk-based 
backup appliance can run between $15,000 and $20,000 for SCSI solutions, but 
only $7,000 to $10,000 for configuration-equivalent ATA solutions. In a much lar-
ger environment (north of 30 TB) for an FC-based disk array, the savings are not as 
dramatic, percentagewise, but saving more than $100,000 off a deal that would 
have gone for half a million dollars is still very significant. 
Rethink the Storage Infrastructure 
Moving to add mid-line storage to the storage pyramid in an enterprise has a pro-
found effect on how IT organizations build and manage their storage infrastruc-
ture. An IT organization has to think about storage from a quality of service (QoS) 
perspective, in which all applications do not require the same service levels, 
whether in terms of response time or in the availability of the application — the 
hammer looking for the nail. QoS is another reason for those IT organizations to 
discipline themselves with the creation of either formal or informal service level 
agreements (SLAs).  
A long-term plan involves a thorough architectural review as part of a plan for a 
storage utility in an information utility. The sum of individually optimal decisions 
does not necessarily yield an overall optimal storage infrastructure. Mid-line  stor-
age should be the impetus for IT organizations to rethink through their storage 
infrastructure. Decisions can then still be made individually and incrementally to 
change the infrastructure. However, the goals behind the changes that are being 
made will have been taken into account. The infrastructure will be more scalable 
and flexible; hence, it will be easier to manage. 
Mid-Line Disk Storage Emerging as Significant Cost-Saving Opportunity 
 12 
To provide us with your feedback on this research, please go to www.aberdeen.com/feedback . 
Aberdeen Group, Inc. 
260 Franklin Street 
Boston, Massachusetts 
02110-3112 
USA 
 
Telephone: 617 723 7890 
Fax: 617 723 7897 
www.aberdeen.com 
 
© 2003 Aberdeen Group, Inc. 
All rights reserved 
August 2003 
Aberdeen Group is a computer and communications  
research and consulting organization closely monitoring 
enterprise-user needs, technological changes, and mar-
ket developments. 
Based on a comprehensive analytical framework,  
Aberdeen provides fresh insights into the future of  
computing and networking and the implications for  
users and the industry. 
Aberdeen Group performs projects for a select group  
of domestic and international clients requiring strategic 
and tactical advice and hard answers on how to manage 
computer and communications technology. This docu-
ment is the result of research performed by Aberdeen 
Group, which was underwritten. Aberdeen Group be-
lieves its findings are objective and represent the best 
analysis available at the time of publication. 
 
 
 
Aberdeen Conclusions 
So far, mid-line storage is a “quiet” storage revolution. Although the trend toward 
the use of ATA disks in enterprise-class applications has been well recognized, en-
terprises are still learning how they can best make use of the new tier on the stor-
age pyramid.  
The mid-line storage tier exists because it gives the most cost-effective answer to 
two classes of storage problems. It is an answer to storing data that has aged and 
frozen into effectively read-only data that is really too expensive to store on high-
performance disk, yet may have usage requirements that make it unsuited for tape. 
Mid-line is also an answer to solving long-standing data protection issues (i.e., 
backup/restore process issues that tape, by itself, could not handle). 
The emergence of the mid-line storage tier will cause IT organizations to change 
their thinking about storage infrastructure. IT organizations have to get away from 
thinking that all data is on high-performance disk except when it is purged for 
deep archiving and that tape is the only mechanism for backup/restore protection. 
Instead, IT organizations need to focus on the information life cycle and how con-
tent progressively moves through the tiers of the storage hierarchy as a function of 
that content’s value and access requirements.  
Enterprises that manage the ILM effectively will cut costs for disk storage. Effec-
tively managing ILM should also enable enterprises to balance performance to 
need more effectively, focus IT administrator resources more effectively, and 
achieve greater overall scalability and flexibility. And the key to all this goodness is 
the mid-line storage tier. 


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | 04-mid-line-storage-v2-whitepaper-7db9bc |
| title | Mid-Line Disk Storage Emerging As Significant Cost-Saving Opportunity |
| author | Aberdeen Group |
| date | 2003-08-01 |
| type | white-paper |
| subject_domain | midline-storage / enterprise-storage / ILM |
| methodology | primary-research,industry-analysis |
| source_file | 04-Mid-Line-Storage-V2-WhitePaper.txt |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group's Executive White Paper presenting the case for a new 'mid-line' disk storage tier using ATA technology positioned between high-performance FC/SCSI disk arrays and tape. Based on 75 face-to-face and telephone interviews with Fortune-class storage managers. The paper defines four tiers of the storage pyramid (high-performance disk / mid-line / near-line / tape) and argues that mid-line ATA disk can serve at least 20% of enterprise data — and potentially over half — at 50% lower cost per gigabyte. It also introduces information lifecycle management (ILM) as the strategic framework for multi-tier storage.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | The published deliverable of the Aberdeen-Maxtor SOW engagement — the formal launch artifact of the midline storage category. Aberdeen's first major published articulation of the mid-line tier concept backed by 75 enterprise interviews. This white paper is the intellectual foundation of the broader Pools of Storage program. |
| **Relevance** | high | ILM tiered storage and the concept of aligning data to cost-appropriate storage based on access patterns remain current enterprise architecture principles. The white paper's four ILM principles (Aging/Freezing/Accumulation/Redundancy) are still analytically valid. ATA-based midline storage is now the standard (SATA SSDs and HDDs dominate secondary tiers). |
| **Prescience** | high |  |

### Prescience Detail


**Prediction 1:** Mid-line tier adoption outlook
- **Claimed:** Mid-line storage emerging in spite of storage buyer inertia with support of major disk drive manufacturers storage systems suppliers and early adopters
- **Year:** 2003
- **Confidence at time:** high

**Actual Outcome 1:** Mid-line storage adoption by 2007
- **Result:** [UNVERIFIED]
- **Confidence:** high
- **Notes:** SATA-based storage became dominant in secondary storage by 2006-2008 — Phase 3 verification of timing

**Prediction 2:** ILM adoption requirement
- **Claimed:** IT organizations need to focus on information life cycle and how content progressively moves through storage tiers as a function of value and access requirements
- **Year:** 2003
- **Confidence at time:** high

**Actual Outcome 2:** ILM adoption as standard enterprise planning
- **Result:** [UNVERIFIED]
- **Confidence:** high
- **Notes:** ILM became a dominant storage concept 2004-2008 — Phase 3 verification of depth and timeline

**Prediction 3:** Mid-line market size prediction
- **Claimed:** Aberdeen believes more than half of enterprise data will eventually fall into mid-line tier
- **Year:** 2003
- **Confidence at time:** medium

**Actual Outcome 3:** Mid-line storage adoption by 2007
- **Result:** [UNVERIFIED]
- **Confidence:** high
- **Notes:** SATA-based storage became dominant in secondary storage by 2006-2008 — Phase 3 verification of timing

**Prediction 4:** Mid-line adding to SAN/NAS without radical change
- **Claimed:** Mid-line can be added to existing DAS SAN and NAS products eliminating concerns about radical change in conservative IT environment
- **Year:** 2003
- **Confidence at time:** high

**Actual Outcome 4:** Mid-line storage adoption by 2007
- **Result:** [UNVERIFIED]
- **Confidence:** high
- **Notes:** SATA-based storage became dominant in secondary storage by 2006-2008 — Phase 3 verification of timing

**Prediction 5:** Data warehouse mid-line opportunity
- **Claimed:** Mid-line storage may actually expand the market by making it more cost-effective to build a data warehouse/data mart or do data mining
- **Year:** 2003
- **Confidence at time:** medium

**Actual Outcome 5:** Mid-line storage adoption by 2007
- **Result:** [UNVERIFIED]
- **Confidence:** high
- **Notes:** SATA-based storage became dominant in secondary storage by 2006-2008 — Phase 3 verification of timing

**Prediction 6:** CDP as emerging mid-line use case
- **Claimed:** Continuous data protection (CDP) that quickly restores data to any point in time is an emerging concept enabled by mid-line disk
- **Year:** 2003
- **Confidence at time:** medium

**Actual Outcome 6:** CDP adoption outcome
- **Result:** [UNVERIFIED]
- **Confidence:** high
- **Notes:** Phase 3 verification — CDP adopted by NetApp EMC and others as mainstream feature by 2006-2008

**Prediction 7:** Mid-line as quiet storage revolution
- **Claimed:** Mid-line storage is a 'quiet' revolution — enterprises still learning best use of the new tier but widespread adoption predicted
- **Year:** 2003
- **Confidence at time:** high

**Actual Outcome 7:** Mid-line storage adoption by 2007
- **Result:** [UNVERIFIED]
- **Confidence:** high
- **Notes:** SATA-based storage became dominant in secondary storage by 2006-2008 — Phase 3 verification of timing


### Entities Referenced (2)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | acquired | Aberdeen/Harte-Hanks |
| Maxtor Corporation | company | unknown [REVIEW] |  |

### Technologies Referenced (10)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| ATA / PATA Disk Interface | protocol | Industry Standard | mature | legacy |
| MaXLine ATA Disk Drives | platform | Maxtor | emerging | discontinued |
| Fibre Channel (FC) | protocol | Industry Standard | mature | active |
| SCSI Disk Interface | protocol | Industry Standard | mature | legacy |
| Storage Area Network (SAN) | platform | Industry Standard | mature | active |
| Network-Attached Storage (NAS) | platform | Industry Standard | mature | active |
| Information Lifecycle Management (ILM) | framework | Industry Standard | emerging | unknown [REVIEW] |
| RAID (Redundant Array of Independent Disks) | protocol | Industry Standard | mature | legacy-supported |
| Continuous Data Protection (CDP) | framework | Industry Standard | emerging | unknown [REVIEW] |
| Solid-State Disk (SSD) | platform | Industry Standard | niche | active |

### Observation Summary

- Total observations: 34
- By type: survey-finding: 11, viability-prediction: 7, benchmark: 4, actual-outcome: 4, framework-component: 4, market-insight: 3, strategic-decision: 1
