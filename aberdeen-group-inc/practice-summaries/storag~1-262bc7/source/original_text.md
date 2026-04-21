# Storage & Storage Management: 1998 Practice Summary

> Archived from: STORAG~1.DOC
> Original publication date: 1998-05-01
> Author: Aberdeen Group

---

## Original Document Text

AberdeenGro
up
Storage & 
Storage 
Management:
1998 
Practice 
Summary
May 1998
Aberdeen Group, Inc.
One Boston Place
Storage & Storage Management Practice Summary
AberdeenGroup 
Boston, Massachusetts 02108 
USA
Telephone: 617 723 7890
Fax: 617 723 7897
www.aberdeen.com
2
Storage & Storage Management Practice Summary
AberdeenGroup 
Aberdeen Group, Inc.
Aberdeen Group is a Boston-based, computer and 
communications consulting and market-research 
organization.
Aberdeen Group performs specific projects for a select 
group of domestic and international clients.    Each requires 
a combination of strategic advice and pragmatic, 
experience-based action plans.    Assignments range from 
corporate and product positioning and organizational 
planning to in-depth market segment research.    Aberdeen 
consults on mergers and acquisitions, corporate positioning 
and investor relations, transaction-processing benchmarks, 
and has special expertise in software and midrange    
computer markets.
In carrying out assignments, Aberdeen uses a proprietary, 
comprehensive, analytical framework providing fresh 
insight into the complex future of computing and 
communications, both from a technological and a market- 
dynamics perspective.    Aberdeen also offers retainer-fee 
programs to a group of continuing clients.
Aberdeen principals and staff are recognized industry 
figures with hundreds of years of combined high-tech 
industry, research and financial community experience 
among them.    They are quoted extensively in industry trade 
and business publications.    Each is a frequent conference 
and seminar speaker.
In addition to client-related research and consulting, 
Aberdeen publishes several periodicals, Aberdeen 
Viewpoints and Profiles, which summarize its analysis and 
research findings.
Information contained in this publication has been obtained from 
sources we believe to be reliable, but is not warranted by us.    Opinions 
reflect judgment at the time and are subject to change without notice.
3
Storage & Storage Management Practice Summary
AberdeenGroup 
The trademarks and registered trademarks of the corporations 
mentioned in this publication are the property of their respective 
holders.
Warning:    This publication is protected by United States copyright law 
and international treaties.    Unless otherwise noted, the entire contents 
of this publication are copyrighted by Aberdeen Group, Inc., and may not 
be reproduced, stored in a retrieval system, or transmitted in any form 
or by any means without prior written consent.    Unauthorized 
reproduction or distribution of this publication, or any portion of it, may 
result in severe civil and criminal penalties, and will be prosecuted to the 
maximum extent necessary to protect the rights of the publisher. 
© 1998 Aberdeen Group, Inc., Boston, Massachusetts
4
Storage & Storage Management Practice Summary
AberdeenGroup 
TABLE OF CONTENTS
STORAGE MANAGEMENT PRACTICE 
V
Description, Focus and Benefits
v
Strategic Market Questions
v
EXECUTIVE SUMMARY
1
SUMMARY OF FINDINGS
3
Key Aberdeen Findings
3
STORAGE AND STORAGE MANAGEMENT DEFINED
6
How Storage & Storage Management Fits into System Platforms & Architectures
6
Market Dynamics
6
Core Storage & Storage Management Components
7
Network Storage Architecture
7
Storage Hardware
7
Storage Connectivity
7
Storage Management Software
8
Professional Services
9
Market Segmentation
9
How An Integrated Network Storage Architecture Works
10
Network Storage Architectures
10
The ‘Value of the Network Storage’ Perspective
12
ISSUES AND CHALLENGES
14
Impact of Major IT Trends
14
Supplier Success Factors
14
User Success Factors
15
5
Storage & Storage Management Practice Summary
AberdeenGroup 
SUPPLIER ABSTRACTS
17
Boole & Babbage, Inc.
17
Compaq Computer Corporation
18
Data General Corporation
19
Computer Associates International, Inc.
20
EMC Corporation
21
Hewlett-Packard Company
22
International Business Machines
23
Legato Systems, Inc.
24
Storage Technology Corporation
25
Sun Microsystems Computer Company
26
VERITAS Software Corporation
27
6
Storage & Storage Management Practice Summary
AberdeenGroup 
Preface
Storage & Storage Management Management 
Practice 
Description, Focus and Benefits
Aberdeen’s Storage & Storage Management practice follows the 
market trends and technical developments of the network storage 
and storage management markets — the distributed and 
centralized storage that a business user accesses over a network, 
and the software that monitors and maintains that storage.    
Today’s storage and storage management solutions give an 
enterprise a vantage point for planning and managing mission-
critical storage assets.    Aberdeen specializes in assessing suppliers’ 
positioning and the technical challenges faced by Information 
Technology (IT) executives as they deploy an effective network 
storage architecture in their enterprises.
The Storage & Storage Management practice includes hardware, 
management software, storage connectivity, and related services.    
Backup and recovery, capacity planning, hierarchical storage 
management, media management, and performance monitoring 
and control are key areas of storage management.    Capacity 
planning, backup and recovery services, and performance 
management are the heart of storage professional services.
Enterprises that successfully master the integration of network 
storage into the overall technology backbone — the enterprise 
network,    CPUs, applications portfolio, and database management 
systems — will reap a harvest of higher service levels, increased 
capability to meet new business demands, and more cost-effective 
use of the enterprise storage dollar.
Strategic Market Questions
1. How should enterprises go about the process of creating a 
network storage architecture? 
2. How will the Internet, intranets, and extranets modify the 
dynamics and location of storage technologies? 
3. How will storage hardware and software technology 
evolve over the next five years to provide new and 
enhanced functionality for both the old and new breed of 
mission-critical applications?    Which suppliers will place 
7
Storage & Storage Management Practice Summary
AberdeenGroup 
IT organizations in the best position to benefit from these 
changes? 
4. What are the advantages to true data sharing and what 
should forward-thinking enterprises do to reap 
immediate benefits? 
5. How can users implement new architectures to take 
advantage of terabyte/hour backup/restore in areas such 
as disaster recovery? 
6. What are the issues in implementing non-mainframe 
hierarchical storage management? 
 This Aberdeen Group Practice Summary is a deliverable in a 
comprehensive service that includes Aberdeen published research 
and customized professional services aimed at executives who 
must make strategic business decisions regarding Information 
Technology. 
8
Storage & Storage Management Practice Summary
AberdeenGroup 
Chapter One
Executive Summary
The burgeoning storage market encompasses much more than disk 
drives and tape drives, their respective media, and the parts that 
make them up:
·
Storage is about architecture, such as network-attached storage 
and storage area networks, so enterprises have to plunge into 
storage connectivity issues related to Fibre Channel, SCSI, and 
SSA;
·
Storage is about the physical or logical pooling of storage into 
disk arrays and tape libraries;
·
Storage is about storage management software that ensures the 
responsive access to, the availability of, and the protection of 
the information upon which the enterprise depends for its 
livelihood; and
·
Storage is about storage-related professional services that an 
organization engages to secure the maximum benefits from its 
storage investments.
With a mushrooming number of servers scattered throughout an 
organization, an enterprise can no longer sensibly make one-off ad 
hoc storage purchases to satisfy a business application 
requirement “just in time”.    The cumulative effect of ad hoc 
storage decisions taken over the course of years — that 
individually seem to make sense — may result in network storage 
that is “cost leaching”, unresponsive to business-demanded service-
level obligations, and difficult to manage.    These problems do not 
manifest themselves at low levels of IT infrastructure complexity, 
but soon become prominent as the complexity inevitably rises.    
The higher complexity level requires a higher degree of data 
protection (including faster backup and restore), more stringent 
service-level targets, and a more powerful data-sharing solution.
The incessantly rapid growth in the number of megabits that can 
be stored on each square inch of storage media continues to drive 
down per-megabyte prices.    At the same time, storage-devouring 
applications, including Enterprise Resource Management and the 
Intra/Internet, have dramatically increased the demand for 
storage.    But this increased storage requires network storage (any 
1
Storage & Storage Management Practice Summary
AberdeenGroup 
storage accessed over a network) composed of much more than 
very large agglomerations of raw megabytes of storage.    This 
network storage environment will interweave storage servers with 
enhanced storage connectivity solutions and expanded storage 
management software.    But the enterprise storage infrastructure 
will require a change in how IS organizations think about, acquire, 
and manage storage. 
Aberdeen finds that storage is an integral part of the IS hardware 
substratum, on a par with servers and architecture — the Big 2 is 
now the Big 3.    Architectural planning for the IS infrastructure has 
to include not only storage and its hardware components, but also 
the applications portfolio and database management systems.    
Enterprises will have to decide how best to acquire and deploy new 
storage connectivity solutions (e.g., Fibre Channel), storage 
intelligence (e.g., data sharing), and storage management software 
(e.g., improved data availability and data protection).    This will 
require organizations to think in terms of storage as part of an 
overall system. 
At the same time, the importance and benefits of today’s storage 
are rapidly increasing, and storage ensures the circulation, 
availability, and safety of this data.    Without an efficient and 
effective global network storage infrastructure in place, 
enterprises risk less than acceptable availability and responsive 
access to data, less than necessary data protection, loss of storage 
asset investment protection, and loss of labor productivity.    And 
knowing which suppliers can meet enterprise needs and when will 
require careful planning by the IS organization. 
Anyone who has responsibility for the network of storage in an IS 
organization — CIO, data center manager, IS planner, and system or 
storage administrator among them — should be aware of the 
dynamic changes in the storage market that will affect their lives 
over the next three to five years. 
2
Storage & Storage Management Practice Summary
AberdeenGroup 
Chapter Two
Summary of Findings
At some level of complexity in an enterprise — say, beyond 20 
servers, 100 gigabytes (GBs) of data to be stored and backed up, and 
a number of files and databases to be managed — storage reaches a 
level of organizational consciousness that requires an enterprise to 
treat storage planning, acquisition, and management as a key to 
building an effective IT infrastructure.    Failure to recognize this 
change can lead an IS organization to have difficulty achieving 
application response time and availability goals, storage 
investment protection, and storage management labor 
productivity.
In order to provide the building blocks for the storage component 
of the IT infrastructure, the storage market is rapidly evolving, as 
expressed in the key Aberdeen findings below.    Individually the 
findings simply represent different aspects of the storage market, 
but the cumulative effect of all the changes taken together is that 
the IS perspective of storage is in for a sea change.    Aberdeen 
believes that this sea change means that enterprises will have to 
view storage as network storage, which is any storage that a 
business user accesses over a network.
Key Aberdeen Findings
7. Enterprises will continue to see lower prices for storage 
media and storage drives as data are packed tighter and 
tighter on physical media.    For example, Quinta 
Corporation (a Seagate Technology company) has 
announced an optically-assisted Winchester storage 
technology with a theoretical maximum areal density of 
250 Gbits/in2 that far exceeds the expected limits of 20-40 
Gbits/in2 given current technologies.    Since drive prices 
remain relatively constant in price, the cost per megabyte 
falls as the data packing density increases on the physical 
media. 
8. But storage has to be viewed as a system, since 
commodity megabytes do not represent the full cost.    
Storage is also more than the controller, the enclosure, 
and an array of drives.    Storage is now about intelligent 
3
Storage & Storage Management Practice Summary
AberdeenGroup 
software for data protection, data movement, and data 
sharing. 
9. Even though most disk storage sold in the Unix and NT 
market is still captive as part of a server sale, IS is starting 
to view storage decisions as server-independent. 
10.But IS is finding that increased complexity in managing 
storage scattered across a large number of servers may 
lead to chaos.    Although each storage system might be 
manageable in isolation, IS organizations cannot afford to 
hire additional people to manage the increased storage.    
This trend is driving storage consolidation and the need 
for better storage management.
11.IS organizations care especially about storage 
performance/scala-bility, architectural flexibility to adapt 
the system to changing needs, high availability, and 
cutting administrative complexity to save costs.    The 
problem is that IS finds it hard to determine what part of 
the performance/scalability and availability comes from 
storage.
12.Easing the burden of system and storage administrators is 
becoming more important in complex IS environments.    
Under- managing storage can lead to inefficiently used or 
poorly performing storage assets, but finding sufficient 
storage management staff may be too difficult (and too 
expensive).
13.Although tape is perceived as secondary storage, tape 
technology remains an essential component of the storage 
infrastructure.    Rapidly changing tape technologies will 
cause IS organizations to rethink their tape strategy.    
Quantum has announced its next generation Super 
DLTtape technology and Hewlett-Packard, IBM, and 
Seagate Technology have announced the Linear Tape-
Open (LTO) tape technology.    Given a goal of terabyte-per-
hour backups at a reasonable price, IS organizations will 
need to understand how these technologies and other 
competing technologies will best help them move toward 
this goal over the next few years.
14.Which type of vendor has responsibility for storage 
management functions is still unclear to IS.    For example, 
backup and restore can be done through an operating 
system utility (a system vendor responsibility in the case 
of Unix), a database management system utility (RDBMS 
4
Storage & Storage Management Practice Summary
AberdeenGroup 
vendor responsibility), or a specific data protection 
software package — from a third-party or from the 
storage vendor.
15.Storage Area Networks (SANs) promise to give IS 
management greater flexibility and functionality for 
managing storage, but SANs will require robust Fibre 
Channel connectivity solutions.    And these robust 
solutions are not quite here, so 1998 is not the year of 
Fibre Channel or SANs.    Although IS organizations should 
plan and perhaps start pilots now, adoption of Fibre 
Channel solutions will not start to become common until 
sometime in 1999.    Fibre Channel hubs and switches 
need greater product maturity and the software to 
effectively manage large heterogeneous SANs is not 
available. 
16.Much-lower disk prices over the past two years are now 
causing a rapid expansion of high-availability storage 
even at the workgroup level.    RAID on LAN servers has 
quickly become commonplace.    RAID only emphases — 
not replaces — the need for tape backup and for storage 
resource management, such as space management.    RAID 
can protect loss of data availability from hardware 
failure, but tape backup is necessary for archiving, 
disaster recovery, and restoration from non-hardware-
related losses of data. 
5
Storage & Storage Management Practice Summary
AberdeenGroup 
Chapter Three
Storage and Storage Management Defined
How Storage & Storage Management Fits into System 
Platforms & Architectures
Storage is a fundamental component of a system.    Traditionally, 
storage couples closely to a specific server through channel 
connectivity, such as SCSI between a Unix server and a disk array.    
Severing this “horse and carriage” mentality is server-independent 
storage, where storage is no longer slave to any particular server. 
Both types of server-independent storage — network-attached 
storage (NAS) and storage area networks (SANs) — lead to greater 
configuration flexibility, higher storage performance, and more 
effective utilization of storage assets.    As such, both play a key role 
in network storage, which Aberdeen defines as any storage a 
business user accesses over a network. 
Aberdeen research indicates that enterprises are beginning to view 
storage as network storage.    As a result, they will need to consider 
its interdependencies with the other components in the IT 
technology backbone — applications, CPUs, database management 
systems, and network.    Storage is no longer just a buy-it-off-the-
shelf ingredient with speeds, feeds, and price as the only variables. 
Moreover, network storage is not only hardware.    Enterprises 
must weave storage management software for managing service 
levels and data protection into their storage plans. 
Planning, acquiring, deploying, and managing the storage and 
storage management assets is and will continue to be a major IT 
management focus for the systems platforms and architectures 
environment. 
Market Dynamics
On the supply side, the year-by-year significant increase in areal 
density (megabits per square inch) for both disk and tape has 
resulted in dramatically reduced storage prices as well as the 
volume required to store a specified amount of storage.    Storing 
textual information electronically is now much less expensive than 
6
Storage & Storage Management Practice Summary
AberdeenGroup 
storing the same amount of information on paper in a filing 
cabinet.
But demand is increasing ever faster.    New applications are 
storage-thirsty — data warehousing, data mining, Enterprise 
Resource Management, and the Inta/Internet among them.    
Moreover, ease of replication results in multiple copies of the same 
information.
Core Storage & Storage Management Components
The storage market is much broader than disk and tape drives that 
form the heart of the physical storage devices (see Figure 1).    The 
storage & storage management market consists of several major 
components:
17.Architectures that mold storage into useful 
configurations;
18.Physical hardware and connectivity products used to 
actualize the architectural concepts,
19.Storage management software that drives the data 
protection, service-level management, and planning 
activities “in the background”; and,
20.Professional services that maintain complex storage as 
part of overall enterprise administration. 
Network Storage Architecture
If IS organizations are to reduce the complexity of acquiring, 
deploying, and managing their enterprise-wide storage assets, a good 
network storage architecture will play a critical role.    Planning for 
network storage means planning to use not only server-independent 
storage using an NAS or SAN but also server-dependent storage. 
Storage Hardware
Choosing storage hardware is not merely choosing a device — disk 
drive or tape drive — or aggregating disk drives into a disk array or 
tape drives into a tape library.    Enterprises must also evaluate storage 
“intelligence” and performance.    The degree of intelligence indicates 
the level of functionality storage can deliver, such as high availability 
through RAID and time-saving through “snapshot” copying facilities.    
Performance is not only the response time for online queries, but also 
relates to the tradeoff among online, near-online, and offline response 
time requirements.
Storage Connectivity
7
Storage & Storage Management Practice Summary
AberdeenGroup 
With the arrival of network storage, the storage channel sinews that 
connect storage to either a network or a server have an increased 
prominence.    Channel connectivity is important not only between 
hardware components, such as a server and a storage unit, but also 
within a storage unit itself.    The choice of channels — along with the 
appropriate bridges, hubs, routers, and switches — is key to 
determining the type of network storage.    Although Fibre Channel 
can play a key role, the other channel options will continue to play an 
important role.    For example, SCSI provides internal storage 
connectivity within many legacy disk array and tape library storage 
units. 
Storage Management Software
Components of 
Storage & Storage 
Management
Primary Divisions Within Each 
Component
Network Storage 
Architecture
·
Network Attached Storage (NAS)
·
Storage Area Network (SAN)
Storage Hardware
·
Disk Drives and Disk Arrays
·
Tape Drives and Tape Libraries
·
Other Storage Devices including 
Magneto Optical
Storage Connectivity
·
ESCON
·
Fibre Channel
·
SCSI
·
Serial Storage Architecture
Storage Management 
Software
·
Backup/Restore 
·
Capacity Planning
·
Duplication and Sharing
·
Hierarchical Storage Management
·
Media Management
·
Supervision and Control
Professional Services
·
Storage Architecture Planning
·
Backup/Recovery Consulting
Figure 1: Components 
of the Storage Market
8
Storage & Storage Management Practice Summary
AberdeenGroup 
·
Capacity Planning Consulting
·
Disaster Recovery
·
Performance Management 
Consulting
Good storage management software should remain unseen and 
unheard by business users.    IT professionals use storage management 
software to ensure that storage fulfills its duties in protecting data and 
in meeting service level objectives for data availability and 
responsiveness to user requests.    Storage management software — 
more so than storage hardware — will be the key to the successful 
management of network storage.    Storage management needs to be 
more scalable, have greater availability, provide more functionality, 
and provide stronger integration.    Moreover, storage management 
needs to be more proactive and predictive.    Policy management tools 
using software agents will help storage management in detecting and 
resolving problems.    New predictive systems management 
techniques will enable storage management to practice preventative 
maintenance.    Individual storage management tools need to integrate 
with other categories of storage management software and with 
systems management frameworks — HP OpenView, Tivoli, and 
Unicenter TNG — in the sense of passing actionable data and in 
displaying a common user interface.    Storage management tools will 
need the functionality to operate effectively in a network storage 
world, including SANs. 
Professional Services
Storage professional services run the gamut from training, on-site 
implementation assistance consulting and systems integration, to 
outsourcing.    Each type of service requires a different level of 
involvement from a professional services organization.    Training is a 
transfer of knowledge from the services organization to the IS group, 
but outsourcing transfers to the professional services organization the 
full-time responsibility for a function.    Most storage professional 
services today are bread-and-butter support with little long-term 
investment of time by the professional services organization, such as 
backup/recovery or performance management consulting.    However, 
Aberdeen research shows that many enterprises need help in 
understanding how to put together a network storage architecture 
and then to help IS organizations implement the architecture.    
        Source:    Aberdeen Group, May 
1998
9
Storage & Storage Management Practice Summary
AberdeenGroup 
Systems integrators can play an important role in helping IS design a 
network storage architecture. 
Market Segmentation
The storage market can be divided into integrated components, 
subsystems, storage management software, and services (see 
Figure 2).    Integrated components are, for example, disk drives, 
tape drives, controllers, hubs, and switches.    Parts, such as 
read/write heads, are subsumed with integrated components and 
are not considered separately by this practice.    Integrated 
components connect to or are incorporated with subsystems — 
disk arrays or tape libraries. 
Software designed to augment a capability of a storage system may 
add considerable value to the storage system, but, if specific to a 
storage system, will be considered as part of the storage system.    
Software independent of a particular storage system architecture 
and designed to help manage the storage system will be referred to 
as storage management software.    Services — for the purposes of 
this analysis — are specialized professional services above and 
beyond normal field engineering and systems engineering.    Both 
field service and systems engineering are critical for the service 
and support of hardware and software, including installation, 
repair, and problem resolution, but can be considered bundled 
with the purchase of a selected product. 
How An Integrated Network Storage Architecture Works
Today’s enterprises should look to integrate the components of a 
storage solution together using a network storage topology that 
integrates with the enterprise’s backbone network (see Figure 3).    
Enterprises that successfully master the integration of network 
storage into the overall technology backbone — the enterprise 
network, CPUs, applications portfolio, and database management 
systems — will reap a harvest of higher service levels, increased 
capability to meet new business demands, and more cost-effective use 
of the enterprise storage dollar. 
Failure to integrate network storage may leave an IS organization 
unable to cost effectively provide desired service levels — 
availability and response time — for key applications.    
Functionality required to perform key tasks — backups, extraction, 
and replication — may be lacking.    Moreover, the scalability 
required for a business application — data warehouse, ERP, or 
10
Storage & Storage Management Practice Summary
AberdeenGroup 
mixed media — and the flexibility to respond quickly to 
unexpected business demands (by adding the right storage, 
bandwidth, and servers) may be missing.    Many suppliers 
advocate throwing more technology at any application 
consumption problem, justifying their arguments on the supposed 
dramatic reductions in the cost of storage per megabyte.    
Aberdeen believes that this cheap-storage myth disguises a harsh 
reality.    Storage that cannot perform a required function (such as 
backup) quickly enough is expensive.    Moreover, replacing 
existing storage with new storage because of a server upgrade 
changes what was perceived as inexpensive storage into expensive 
storage.    Eventually, the enterprise may find it too expensive to 
correct storage infrastructure deficiencies. 
Network Storage Architectures
The main options IS organizations have for capitalizing on network 
storage (see Figure 3) revolve around the use of server-dependent 
or server-independent storage.    Server-independent storage 
architectures — NAS and SAN — have greater overall flexibility 
than a server-dependent architecture and thus open up a wide 
range of opportunities. 
Integrated 
Component
s
Storage 
Systems
Management 
Software
Professional 
Services
Vendors
System
Compaq
X
Data General
X
Hewlett-Packard
X
X
X
IBM
X
X
X
X
Sun Microsystems
X
X
X
Storage
EMC Corporation
X
X
X
Exabyte
X
StorageTek
X
Figure 2: 
Representative 
Vendors for 
Each Storage 
Market 
Segment
11
Storage & Storage Management Practice Summary
AberdeenGroup 
Component
Brocade
X
Gadzoox
X
Quantum
X
X
Vixel
X
Software
Boole & Babbage
X
Computer 
Associates
X
Intelliguard 
Software
X
Legato
X
VERITAS
X
Services
Comdisco
X
SunGard
X
The storage resource sharing, very fast speeds, and easy 
configurability of a SAN improves service levels and manageability. 
Because storage channels rather than the network channels move 
the data, a SAN also reduces traffic on the backbone network and 
thereby improves service for many applications, not to mention 
allowing the network to perform its other functions faster. 
Enterprises can use the flexibility of a SAN to leverage their 
investment in ESCON and SCSI.    These older storage channel 
technologies can now be part of a specialized storage network and 
can share resources with the newer, higher speed (100MB per 
second) Fibre Channel transmission technology.    But Fibre 
Channel, although helpful, is not the solution to the I/O speed 
imbalance between CPU internal instruction speeds and drive — 
either disk or tape — speeds. 
          
            Source:    Aberdeen Group, May 
1998
12
Storage & Storage Management Practice Summary
AberdeenGroup 
With the configuration flexibility these three methods furnish, an 
IS organization can construct a cost efficient SAN that can share 
and allocate data easily, move data faster and protect the storage 
investment from dependency upon a single server.
The ‘Value of the Network Storage’ Perspective
Viewing storage purchase decisions in the context of network 
storage is radically different from purchasing storage as extra 
space into which more data will fit.    With ad hoc storage 
purchases, price, speed, and basic availability are the principal 
variables in a runoff competition among various suppliers.    Ad 
hoc purchasing can be used to determine immediate needs, but the 
cumulative effect of a series of ad hoc decisions over time may lead 
to a suboptimal storage architecture.    With network storage, an 
enterprise can consider the impact of storage on service-level 
obligations, the other elements of the IT technology backbone, and 
overall business requirements. 
Storage needs vary widely in an enterprise.    At the lowest level is 
PC storage, including both grounded desktops and mobile laptops. 
This storage is already significant in most enterprises.    IBM’s 
announcement of a 16.8 GB desktop drive is a continuation of a 
trend toward even more storage in the hands of business users.    
But even though prices for desktop storage is only in the hundreds 
of dollars for each drive, user-managed storage is slow and is a 
Figure 3: Generalized Network Storage Topology
Source:    Aberdeen Group, May 1998
13
Storage & Storage Management Practice Summary
AberdeenGroup 
backup challenge for the IS organization.    IS can provide backup 
services over a LAN or the Web, but an alternative is to offer PC 
users shared storage on centralized servers as an alternative.    IS 
can then apply storage administrative disciplines on availability 
and backup protection, but this strategy places demands upon the 
network and server CPU cycles. 
At the middle level is distributed storage.    Storage needs for 
distributed systems may vary widely.    An individual point of sale 
system may not collect much data in a day, but the system may 
require hardware and storage component redundancy for business 
continuance during the day.    At night, a central site needs to 
upload the data.    In contrast, a department may have a large data 
mart, which requires a central site to refresh once a week.    In 
either situation, logically-centralized storage management is 
necessary to mange the redundancy of physically centralized and 
decentralized storage assets for distributed applications.    For 
example, centralized storage management software can backup 
distributed servers to a tape library at a central site.
At the highest level within an organization, an IS-managed 
operations center can contain server-dependent storage in addition 
to server-independent storage.    This storage can serve as a 
platform for consolidating storage from a number of previously 
distributed servers and for housing large new large databases, 
including scaling up to a very large data warehouse.    An 
operations center can include a heterogeneous mix of mainframes, 
Unix servers, and Windows NT servers, plus, perhaps, a wildcard, 
such as AS/400 systems.    Although some storage will remain server 
dependent, the operations center will be the primary beneficiary of 
SANs to improve performance, availability, cost, and labor 
productivity for the use of storage.    But even though storage in the 
operations center may have the greatest focus of IS attention, the 
distributed and PC layers of the storage-distribution hierarchy 
must receive their due in obtaining value from the network storage 
architecture.
14
Storage & Storage Management Practice Summary
AberdeenGroup 
Chapter Four
Issues and Challenges
Impact of Major IT Trends
Computerization is a key driver for storage.    Text documents are 
much larger than sheer text would dictate, because of formatting 
and embedding of objects from other applications, such as a 
PowerPoint slide.    Embedding of multimedia — video and voice — 
is further increasing the need for storage.    Moreover, a new breed 
of mission-critical applications, including data warehousing and 
enterprise resource planning systems, push computerization.    And 
storage that has fallen an order of magnitude in price over the last 
five years provides an accelerant that keeps the flames of 
computerization burning. 
The mainframe is no longer dominant; in storage markets the 
combination of Unix and NT is.    Storage sales for Unix and NT 
reflect this trend — billions and billions more sold in both 
megabytes and dollars than on the mainframe.    But Unix and NT 
environments do not have the software and management 
disciplines commonplace on the mainframe.    The mission-critical 
new applications require these disciplines, and over the next two 
years, Unix/NT storage software and hardware products will 
increasingly provide them.
With the new connectivity facilities available via the Internet, 
systems or storage administrators can now manage physically 
distributed or centralized storage logically from anywhere, as if 
they were at a centralized console.    This single point of control 
provides flexibility and power, but requires that tight security is in 
place, as networks are subject to possible intrusion from 
malefactors. 
Supplier Success Factors
Aberdeen research shows that users demand four things above all 
for storage suppliers:    ease of use, flexibility, 
performance/scalability, and robustness. 
Suppliers should think in terms of a network storage architecture. 
This storage architecture is not the architecture of a particular 
15
Storage & Storage Management Practice Summary
AberdeenGroup 
product or service, but rather the overarching framework that ties 
the IT infrastructure together.    Selling the least expensive product 
with the greatest functionality and the best service and support to 
boot will not be enough to ensure ongoing sales if the product 
cannot be easily integrated now and in the future with all the other 
pieces of the network storage architectural puzzle.
Enterprises build network storage architectures over time and so 
need to know a supplier’s vision.    Moreover, no one supplier can 
do it all.    Partnering will be a key supplier skill in the next 1-2 
years. 
Suppliers need to sell solutions as part of the architecture, not 
point products.    In these solutions, service and support will be 
critical.    Enterprises must have confidence in their suppliers’ 
ability to deliver service and support — even if they seldom need it. 
User Success Factors
Speeds and feeds, whether for software or hardware, used to be all 
that an IS organization needed to compare storage-related 
products.    But what use is a 10% performance and 10% cost 
advantage if an enterprise cannot find the time to build a business-
driven data warehouse, back up mission-critical databases in an 
acceptable time, or pass the IS auditor’s requirements for disaster 
recovery?    An enterprise needs to understand how storage can 
help ensure response time and availability service levels, squeeze 
more business value out of a tight batch window, move data from a 
mainframe to an open system quickly enough to build a data 
warehouse, and protect the enterprise’s data assets in case of a 
disaster.
But to use storage most effectively, individual storage acquisition 
decisions must fit into an overall framework — a network storage 
architecture.    Otherwise, seemingly-sound individual decisions 
can lead over time to an overall storage architecture that suffers 
from storage arteriosclerosis.    For example, without careful 
planning, the backbone enterprise network may not support the 
movement of data from an MVS mainframe to a Unix server fast 
enough to build a data warehouse. 
Storage is not an issue reserved for systems administrators and 
technical support staff any longer.    CIOs have to set storage 
architecture direction, articulate that storage strategy and the 
budgetary requirements for it to senior management and business 
unit managers, and oversee the planning, acquisition, 
implementation, ongoing management, and continual upgrading of 
16
Storage & Storage Management Practice Summary
AberdeenGroup 
a network storage architecture.    The CIO must involve his/her 
architectural planning staff as well as all IS line managers.    This 
includes both the hardware infrastructure components — the 
operations center and network services groups — and the software 
infrastructure components — applications development and 
database management groups. 
Finally, enterprises must carefully examine if a product will 
provide investment protection for the next three years (such as 
through planned upgrades or integration with complementary 
products) or if a product can be considered a stopgap to be thrown 
away when a version that fits better into the architecture appears. 
17
Storage & Storage Management Practice Summary
AberdeenGroup 
Chapter Five
Supplier Abstracts
Boole & Babbage, Inc.
3131 Zanker Road
San Jose, CA 95134
(408) 526-3000
www.boole.com
Market Position
Boole & Babbage offers SpaceView Explorer, storage management 
software that enables an IS organization to manage storage from a 
service-level perspective.    For example, an IS organization can 
improve service levels — availability or response time from storage 
— with alerts for faster response to backup or power failures and 
the ability to take action to avoid out-of-space conditions.    
SpaceView Explorer delivers enterprise storage management 
supporting not only mainframe, but also Unix and Windows NT 
server environments. 
Boole & Babbage blends both old and new software concepts to 
weld together strong storage resource management software.    The 
old is the requirement that IS organizations have for robust 
software that it learned from its mainframe heritage.    The new is 
event-driven management using intelligent agents that ease the 
management burden and the drain upon network resources.    
Boole & Babbage’s partnership with EMC enables it to get detailed 
information so that an IS organization can better manage its EMC 
disk systems.    SpaceView distinguishes itself from its competition 
with heterogeneous connectivity, policy-driven management, and 
depth of data scooping facilities. 
Aberdeen Conclusions
SpaceView Explorer is an illustration of a critical type of storage 
management software that will be needed in the world of the 
network storage architecture.    Boole & Babbage will have to work 
with other partners, such as IBM, to provide supplier-specific data 
storage information, and with backup/restore software suppliers 
18
Storage & Storage Management Practice Summary
AberdeenGroup 
for two-way exchange of actionable information, as well as to 
provide a Web-enabled console. 
19
Storage & Storage Management Practice Summary
AberdeenGroup 
Compaq Computer Corporation
Enterprise Storage and Options Division
P.O. Box 692000
Houston, TX    77269-2000
(281) 370-0670
www.compaq.com
Market Position
Compaq is putting the pieces together to become a major player in 
the storage market.    In addition to Tandem, Compaq will be able to 
add Digital’s StorageWorks to its portfolio.    Compaq will thus be 
able to effectively cover both the Unix and Windows NT storage 
environments.    The only piece that is missing is the mainframe, 
but Digital has an agreement with Hitachi Data Systems that may 
fill this gap.    Compaq is acquiring Fibre Channel and storage 
software management technology from StorageTek.
Compaq has three ace cards that will stand it in good stead.    The 
first is capable distribution channels to deliver storage products.    
The second are products that offer good price for reasonable 
performance and availability.    The third is a large installed base 
can serve as the foundation for future business.
Aberdeen Conclusions
Compaq has many of the necessary hardware pieces, but it has to 
integrate disparate functional organizations and come up with an 
overall strategy and vision.    While Digital can contribute 
StorageWorks’ vision, Compaq needs to develop a comprehensive 
storage management strategy.    Although some internal 
development of software will help, Compaq will have to look 
primarily to partnering (with perhaps a leavening of acquisition). 
20
Storage & Storage Management Practice Summary
AberdeenGroup 
 Data General Corporation
CLARiiON Division
Coslin Drive
Southboro, MA    01772
(800) 672-7729
www.clariion.com
Market Position
The good news for CLARiiON is that — in contrast to some of its 
systems supplier brethren’s storage divisions — it understands 
what it means to be a server-independent storage supplier.    The 
bad news is that CLARiiON depends upon OEM sales to other 
suppliers, such as Hewlett-Packard and Storage Technology 
Corporation, and these suppliers could conceivably develop 
alternatives that would squeeze CLARiiON out of their storage 
picture.    Consequently, the decision of Dell to team with CLARiiON 
for its server storage affirms both CLARiiON’s technology — strong 
technology always having been a strong suit of Data General — and 
its viability. 
And CLARiiON has a strong technology.    The division is a leader in 
the use of Fibre Channel technology with its FC5000 Series disk 
array family.    Its Multidimensional Storage Architecture 
emphasizes flexibility — online transaction processing systems, file 
servers, data warehouses, and multimedia each require a targeted 
configuration with different drive-to-controller ratios, I/O rates, 
and transfer rates. 
Aberdeen Conclusions
Getting its products to market in a timely manner and keeping 
costs down are CLARiiON’s keys to keeping its current OEM 
customers happy and to developing more OEM business.    Although 
it has software to manage its own disk arrays (Navisphere), 
CLARiiON will have to team with partners to develop a broader 
storage management message.
21
Storage & Storage Management Practice Summary
AberdeenGroup 
Computer Associates International, Inc.
One Computer Associates Plaza
Islandia, NY 11788-7000
(516) 342-5224
www.cai.com
Market Position
Computer Associates designed ARCserve backup/restore software 
to protect mission-critical application information in a distributed 
world.    Computer Associates understands the robustness 
requirements that software needs to succeed at the enterprise 
level.    CA Cheyenne understands ease of use from its Novell 
NetWare days.    Computer Associates’ emphasis on innovation in 
software has led to extensive functional additions to ARCserve that 
greatly extend its reach in both Windows NT and Unix 
environments. 
ARCserve is particularly effective in online backup of key 
applications, including SAP R/3, databases, and groupware systems. 
Beyond backup and restore alone, ARCserve provides mainframe-
class media management capabilities, hierarchical storage 
management, and a very-high-availability data protection strategy.
Aberdeen Conclusions
ARCserve should appeal to enterprises because of its breadth of 
platform coverage, application coverage, integration with systems 
management, and attention to performance.    In addition, 
ARCserve’s remote management facility from one central point 
lessens the burden upon an IS organization for the deployment of 
backup and restore.    Moreover, CA’s storage management products 
can be integrated with its industry-leading enterprise management 
software, Unicenter TNG.    Computer Associates needs to continue 
to offer more of what it has already done — more applications and 
even greater performance. 
22
Storage & Storage Management Practice Summary
AberdeenGroup 
EMC Corporation
171 South Street
Hopkinton, MA    01748-9103
(508) 435-1000
www.emc.com
Market Position
With its Symmetrix line of disk storage systems as a foundation, 
EMC now has an annual revenue run rate of over $3 billion — an 
order of magnitude increase in the space of only six years.    One of 
EMC’s strengths is its modular hardware and storage architecture 
— Intelligent Storage Architecture (ISA). 
MOSIAC:2000 is the hardware foundation of ISA.    With 
MOSIAC:2000, EMC pioneered the use of small-form-factor disk 
array subsystems using large quantities of cache in disk controllers 
to significantly enhance storage performance.    EMC continues to 
build upon this base, such as offering 47GB disk drives.    But EMC’s 
real focus is to continue to add value-enhancing software to 
distinguish its disk systems from those of the competition. 
With ISA software, EMC provides potent facilities for the 
movement, sharing, and protection of data.    This common 
architectural platform enables EMC to extend functionality that 
typically is available only to mainframe-accessed storage to Unix 
and Windows NT platforms as well.    None of EMC’s competitors 
can offer on a single disk system the breadth and depth of features 
and functionality that EMC offers on a Symmetrix system.
Aberdeen Conclusions
EMC is the only supplier that can back up in depth its claim to 
provide enterprise storage — simultaneous access from 
mainframe, Unix, and Windows NT servers.    With strong storage 
software and service and support, EMC has a good message to 
convey at the high end of the disk storage market.    In the 
upcoming world of a network storage architecture, EMC will have 
to offer (through partnerships, acquisitions, and internal 
development) a broader range of storage products, including a 
broader selection of secondary-storage integration solutions and 
storage management software. 
23
Storage & Storage Management Practice Summary
AberdeenGroup 
Hewlett-Packard Company
Enterprise Storage Solutions Division
11413 Chinden Boulevard
Boise, ID    83714-0021
(208) 396-2786
www.hp.com
Market Position
Hewlett-Packard’s Enterprise Storage Solutions Division (ESSD) 
markets three lines of disk storage products, each addressing a 
distinct market requirement.    HP’s own AutoRAID delivers ease of 
installation and RAID management for the midrange storage 
market.    HP partners with CLARiiON to provide disk array systems 
for midrange customers that require high availability Fibre 
Channel.    At the high end of the HP-UX and Windows NT market, 
HP partners with EMC to deliver open Symmetrix disk storage 
systems. 
ESSD is also well positioned in secondary storage.    ESSD sells 
products from HP’s Information Storage Group (ISG), including 
midrange tape libraries, and has an agreement with StorageTek 
whereby customers can purchase high end tape libraries.    
Moreover, HP joins with IBM and Seagate to sponsor the new 
Linear Tape Open technology. 
HP has a good foundation in storage management software with 
HP OpenView OmniBack II for backup and restore. 
HP’s well-deserved research and development reputation gives it a 
strength in the development of Fibre Channel products, which will 
stand it in good stead in helping IS organizations implement 
storage area networks.
Aberdeen Conclusions
HP can continue to build upon its Fibre Channel technology 
strengths, its strong partnership base, its storage management 
products, and the ease of use designed into AutoRAID.    For 
example, HP can create tighter links between HP OpenView 
OmniBack II and systems management frameworks, including HP 
OpenView.    However, HP needs to move rapidly toward SAN 
technology to fend off challenges from IBM, Sun, and Compaq. 
24
Storage & Storage Management Practice Summary
AberdeenGroup 
International Business Machines 
Storage Systems Division
5600 Cottle Road
San Jose, CA 95193
Telephone
www.ibm.com
Market Position
As a full systems supplier, IBM has always provided a complete 
range of storage products starting from the ground up with a 
leadership role in base technology, such as magneto-resistive head 
technology.    IBM’s Storage Systems Division (SSD), which was 
formerly known as ADSTAR, provides a wide range of storage 
products for the enterprise.
IBM offers RAMAC disk arrays for the mainframe, including one 
product line developed within IBM and two product lines that it 
resells from StorageTek.    For the open systems market, IBM 
emphasizes the IBM 7133 disk system, which utilizes the Serial 
Storage Architecture (SSA) that IBM pioneered.    For tape storage, 
IBM offers the Magstar family of high-performance tape products. 
The ADSTAR Distributed Storage Manager (ADSM) is IBM’s lead 
storage management software for backup and restore and for 
hierarchical storage management. 
IBM is building upon this base with Seascape, a storage enterprise 
architecture that IBM is designing for the connected world of 
storage.    Seascape rests upon three principles: snap-in building 
blocks, universal data access (and especially connectivity among 
heterogeneous server platforms and IBM storage), and storage 
servers.    One of the planned building blocks is the Enterprise 
Storage Resource Manager (ESRM), which will build on ADSM to 
offer comprehensive storage management — not just backup and 
recovery, but performance management, capacity planning, and 
configuration management as well — and will connect to the Tivoli 
Plus systems management framework.    ESRM integration with 
ADSM should be available in the first quarter of 1999. 
Aberdeen Conclusions
IBM already has a few fruits from its Seascape architecture, such as 
the Network Storage Manager that bundles hardware and ADSM to 
provide network backup and recovery.    IBM has a clear vision of 
what other products that it wants to deliver, but needs to deliver 
these products, including a storage server, on schedule.    Although 
25
Storage & Storage Management Practice Summary
AberdeenGroup 
it naturally favors home-grown SSA over Fibre Channel, IBM 
should move to embrace, rather than merely endure the presence 
of, of Fibre Channel.
26
Storage & Storage Management Practice Summary
AberdeenGroup 
Legato Systems, Inc.
3210 Porter Drive
Palo Alto, CA    94304
(415) 812-6000
www.legato.com
Market Position
Legato is the fortunate position of being in the right market at the 
right time.    Several years ago storage management software for 
the Unix and Windows NT market was not a high priority for the IS 
organization.    With the rapid adoption of mission-critical 
applications on these platforms, storage management software has 
assumed a more prominent role and Legato is one of the leaders in 
the parade to deliver storage management software
Legato NetWorker, available on both Unix and Windows NT 
platforms, is backup/restore and media management software for 
network storage management.    Legato has layered its enterprise 
storage management software, Global Enterprise Management of 
Storage (G.E.M.S.) above NetWorker.    A systems administrator can 
run G.E.M.S. from a central console to manage a series of 
NetWorker servers distributed across the enterprise.
Legato has arrangements with 22 of the largest systems and 
applications vendors for the use of NetWorker.    NetWorker now 
provides service to over 2 million systems containing perhaps a 
hundred petabytes of storage.
Aberdeen Conclusions
Legato has one of the key bases of storage management software 
covered, but the service-level supervision and control component 
of storage management software is also essential.    Enterprises are 
going to want one common storage management interface 
accompanied by the ability to share data needed by more than one 
storage management component (such as the service management 
component knowing about the failure of backup due to a power 
loss).    Legato will have to decide whether integration with another 
supplier’s product is preferable to development or acquisition of 
the technology.
27
Storage & Storage Management Practice Summary
AberdeenGroup 
Storage Technology Corporation
2270 South 88th Street
Louisville, CO    80028
(888) 202-8829
www.storagetek.com
Market Position
Storage Technology Corporation (StorageTek) is the original 
storage-only company.    StorageTek is the market leader in 
automated tape libraries after having pioneered the robotics used 
in large tape silos.    But StorageTek has always been a major player 
in disk storage as well; for example, as part of its agreement with 
StorageTek, IBM sells the RAMAC Virtual Array Storage, which 
originally was code-named Iceberg by StorageTek. 
StorageTek has continued to sell midrange storage directly and 
plans to expand upon this role.    The company now sells its 
OPENstorage brand, which is a bundled hardware package 
consisting of a RAID disk array and a tape library for Windows NT 
applications. 
StorageTek also understands the importance of network storage 
and is developing storage network connectivity solutions as 
evidenced by Compaq’s agreement to buy technology from 
StorageTek.
Moreover, the company understands the enterprise-level storage 
market, is well-received at the enterprise level, and has always had 
a well-articulated vision of the storage market.
Aberdeen Conclusions
If StorageTek wants to be a full service storage supplier, it needs to 
put together a complete story on how it can help an IS organization 
deliver a network storage architecture.    The company will have to 
build a disk array story from the low end to the high end and add 
in a storage management strategy.    Although StorageTek can use 
its research and development skills in some cases (and buy the 
technology in other cases), partnering is StorageTek’s best means 
for filling in the other pieces of the network storage architecture 
portfolio that it needs.
28
Storage & Storage Management Practice Summary
AberdeenGroup 
Sun Microsystems Computer Company 
Networked Storage Division
901 San Antonio Road
Palo Alto, CA    94303
(650) 960-1300
www.sun.com
Market Position
Along with its system supplier counterparts, Sun has recognized 
the growing importance of storage and has created a specific 
storage division.    Sun is building marketing and management 
facilities for the storage division in Newark, CA across the 
Dumbarton Bridge from Silicon Valley — in addition to its 
investment in Encore in Florida. 
Sun has three families of disk storage products under its StorEdge 
branding.    The A7000 Intelligent Storage Server, the legacy of Sun’s 
acquisition of Encore, supports mainframe, Unix, and Windows NT 
environments.    Sun positions the A7000 — and the DataShare 
software for information sharing included with the A7000 — 
against EMC.    The home-grown A5000 uses Fibre Channel for 
scalability and for reliability, serviceability, and availability.    
Rounding out its offering are the Symbios-controller-based A3000 
and A1000 arrays for the midrange market.    The result of these 
moves is a full suite of products that span medium-range and high-
end user needs — plus Sun strengths in Fibre Channel, server, and 
network technology.
Sun’s vision is its Intelligent Storage Network architecture, 
consisting of five principal technologies and capabilities:    
intelligent storage server system, true information sharing, Fibre 
Channel networking, Java technology storage network 
management software, and building block components. 
Aberdeen Conclusions
Sun’s challenge is to ensure that each of its product lines can match 
the principles listed in its Intelligent Storage Network architecture. 
Sun also needs to work on building up distribution channels, 
including a direct sales force, that is proficient in selling at the 
enterprise level — including to mainframe customers.    Moreover, 
Sun has to develop a comprehensive storage management story, 
probably by expanding upon current storage management 
software relationships and developing new ones. 
29
Storage & Storage Management Practice Summary
AberdeenGroup 
VERITAS Software Corporation
1600 Plymouth Street
Mountain View, CA    94043
(650) 335-8000
www.veritas.com
Market Position
As a storage management software leader, VERITAS has a series of 
software products for storage management, including NetBackup 
for backup and restore (from its acquisition of OpenVision), a 
Volume Manager for managing storage distributed across multiple 
storage devices, and a Media Librarian for control of secondary 
storage media. 
Moreover, VERITAS has one of today’s clearest visions of end-to-end 
storage management.    The centerpiece will be the VERITAS storage 
management engine that will be an intelligent management layer 
for VERITAS’ product suite.    The VERITAS Storage Manager will 
enable a systems administrator to set storage policies and use these 
policies with intelligent agents, which automatically respond to 
non-judgment-requiring problems or which send alerts for 
problems requiring human judgment.    The VERITAS Storage 
Advisor would forecast historical rules-based performance analysis 
and assist in identifying tuning optimizations.    The VERITA Storage 
Planner would forecast storage needs and configurations.    If 
VERITAS can deliver on all of its promises, it will have solidified an 
already strong position in the storage management market.
Aberdeen Conclusions
VERITAS’ main challenge is to execute on its architecture.    
Although VERITAS has chosen a hard road, success could give 
VERITAS a long window of opportunity over its competitors in the 
battle to provide storage management for the network storage 
architecture. 
30


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | storag~1-262bc7 |
| title | Storage & Storage Management: 1998 Practice Summary |
| author | Aberdeen Group |
| date | 1998-05-01 |
| type | other-research |
| subject_domain | enterprise-storage |
| methodology | industry-analysis |
| source_file | STORAG~1.DOC |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group's 1998 analysis of the enterprise storage market, arguing that storage must be treated as a system-level architectural decision — not a commodity — and introducing the concept of 'network storage' (any storage accessed over a network). The report covers SANs, NAS, Fibre Channel, RAID, tape technologies, and storage management software, forecasting that SANs would not become common until 1999 and that storage management software would be the critical differentiator. Supplier profiles cover 11 vendors including EMC, IBM, HP, VERITAS, Legato, and StorageTek.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Institutional practice summary capturing the inflection point when enterprise storage transitioned from captive server-attached to networked architectures; valuable historical context for SAN/NAS adoption. |
| **Relevance** | high | Network storage architectures (SAN/NAS), storage management software, and the principle that storage must integrate with overall IT architecture remain foundational enterprise IT topics. |
| **Prescience** | high | Aberdeen correctly predicted that Fibre Channel SANs would not mainstream until 1999-2000 and that storage management software would become the key differentiator over raw hardware. |

### Prescience Detail


**Prediction 1:** SAN mainstream adoption timeline
- **Claimed:** 1998 is not the year of Fibre Channel or SANs; adoption common by 1999
- **Year:** 1998
- **Confidence at time:** high

**Actual Outcome 1:** SAN/Fibre Channel mainstream — actual outcome
- **Result:** Prediction proved accurate; Fibre Channel SAN began mainstream adoption 1999-2001.
- **Confidence:** high
- **Notes:** Prediction proved accurate; Fibre Channel SAN began mainstream adoption 1999-2001.

**Prediction 2:** Storage management software vs hardware importance
- **Claimed:** software will be key differentiator over hardware
- **Year:** 1998
- **Confidence at time:** high

**Prediction 3:** Storage management software integration requirement
- **Claimed:** must integrate with HP OpenView / Tivoli / Unicenter TNG
- **Year:** 1998
- **Confidence at time:** high

**Prediction 4:** Storage policy management evolution
- **Claimed:** software agents and predictive systems will enable preventative maintenance
- **Year:** 1998
- **Confidence at time:** medium


### Entities Referenced (22)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | acquired | Aberdeen/Harte-Hanks |
| Boole & Babbage Inc. | company | unknown | unknown |
| Compaq | company | dissolved | HP (2002) |
| Data General Corporation | company | unknown | unknown |
| Computer Associates (CA) | company | renamed | CA Technologies (2006) -> Broadcom (2018) |
| EMC Corporation | company | unknown | unknown |
| Hewlett-Packard (HP) | company | split | HP Inc./HPE (2015) |
| IBM | company | active |  |
| Legato Systems | company | unknown | unknown |
| Storage Technology Corporation (StorageTek) | company | unknown | unknown |
| Sun Microsystems | company | acquired | Oracle (2010) |
| VERITAS Software | company | unknown | unknown |
| Seagate Technology | company | active |  |
| Quinta Corporation | company | unknown | unknown |
| Quantum Corporation | company | unknown | unknown |
| Exabyte | company | unknown | unknown |
| Brocade Communications | company | unknown | unknown |
| Gadzoox Networks | company | unknown | unknown |
| Vixel Corporation | company | unknown | unknown |
| Intelliguard Software | company | unknown | unknown |
| Comdisco | company | unknown | unknown |
| SunGard Data Systems | company | unknown | unknown |

### Technologies Referenced (13)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Storage Area Network (SAN) | storage | Various | emerging | active |
| Network Attached Storage (NAS) | storage | Various | growing | active |
| Fibre Channel (FC) | protocol | Various | emerging | mature |
| SCSI (Small Computer System Interface) | protocol | Various | mature | legacy |
| RAID (Redundant Array of Independent Disks) | storage | Various | mature | active |
| Tape Backup and Libraries | storage | Quantum; HP; IBM; Seagate; StorageTek | mature | active |
| Linear Tape-Open (LTO) | storage | HP; IBM; Seagate | emerging | active |
| Super DLTtape | storage | Quantum | emerging | active |
| Hierarchical Storage Management (HSM) | application | Various | growing | active |
| Storage Management Software | application | VERITAS; Legato; CA; Boole & Babbage | growing | active |
| Network Storage Architecture | platform | Various | emerging | dominant |
| Serial Storage Architecture (SSA) | protocol | IBM | emerging | legacy |
| ESCON (Enterprise Systems Connection) | protocol | IBM | mature | legacy |

### Observation Summary

- Total observations: 22
- By type: market-assessment: 11, viability-prediction: 4, competitive-assessment: 4, expert-opinion: 2, actual-outcome: 1
