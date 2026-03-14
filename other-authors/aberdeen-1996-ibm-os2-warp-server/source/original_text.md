# IBM's OS/2 Warp Server: The Whole is Greater Than the Sum of the Parts

> Archived from: https://web.archive.org/web/19970112010601/http://www.aberdeen.com:80/secure/viewpnts/v9n4/v9n4.htm
> Original publication date: 1996-02-19
> Author: Aberdeen Group

---

## Original Document Text

Volume 9 / Number 4
February 19, 1996
IBM's OS/2 Warp Server: The Whole is Greater Than the Sum of the Parts
This Product Viewpoint describes two new and related products to be released by IBM in 1996: OS/2 Warp Server — a new product resulting from the marriage of OS/2 Warp and OS/2 LAN
Server; and a standards-based Directory and Security Server add-on which provides OS/2 Warp Server with the ability to scale from the department, to the division — to the enterprise.
By providing an integrated, modular, object-based 32-bit operating system packaged with many free utilities, as well as optional directory and security services — all of which run on Intel-
based servers — IBM's newly released OS/2 Warp Server is at least a year ahead of the competition.
Contrary to popular belief, the choice of a server network operating system (NOS) is not conﬁned to either Novell's NetWare or Microsoft's NT Server. Savvy business and IS executives will
look beyond the press and marketing hype to an integrated package from IBM which has the networking strengths of Novell's NetWare and the operating system strengths of Microsoft's NT
Server — plus a lot more.
Table of Contents
Executive Summary
1996 Product Announcements
OS/2 Warp Server — the Business Application Solution
Everything but the Kitchen Sink?
Application Server
Directory and Security Server
Aberdeen Conclusions
Executive Summary
OS/2 Warp Server has as its foundation the 32-bit, multitasking, multithreading, OS/2 Warp operating system for departmental application platforms — married to IBM's LAN Server 4.0
network operating system used for enhanced ﬁle and print services. The previous dual identity of OS/2 and LAN Server, exempliﬁed by the need for dual installation, is gone. The base
product is enhanced by the addition of several no-cost extras: systems management services, remote connectivity services, backup and recovery services and advanced printing capabilities.
Because of the confusion about the product, enhanced by the business press, it is necessary to state the obvious — OS/2 Warp Server is intended to run on Intel-based servers and does not
compete with desktop operating systems such as Windows 95, Windows NT Workstation or Windows 3.x. OS/2 Warp Server does compete with Novell NetWare 4.x, Microsoft NT Server
3.5x and various ﬂavors of Unix.
OS/2 Warp Server provides support for the major desktop operating systems: DOS, Windows 3.x, Windows NT, Windows 95, AIX, OS/2 and OS/2 Warp Connect, and Macintosh.
Network operating systems became popular ﬁrst as a means of sharing print services and ﬁles among workgroups, and NetWare is still the market share leader. NT Server is gaining
popularity in the exploding market for database and application servers. However, Aberdeen contends that neither NetWare nor NT Server has the level of stability to meet an IS department's
need for an operating system that has the capacity to be an integrated ﬁle, print, database and application server.
OS/2 Warp Server's highly-tuned 32-bit engine and integrated services offers departments and divisions of large organizations, as well as independent businesses, a powerful, easy to manage
operating environment. With the Directory and Security Server option, OS/2 Warp Server provides the means for sharing and securing data beyond the LAN across distributed applications
throughout the enterprise.
Back to Table of Contents
1996 Product Announcements
OS/2 Warp Server
OS/2 Warp Server is essentially a new product from IBM which integrates the OS/2 Warp operating system and the LAN Server 4.0 network operating system with a fully functional set of
administrative utilities, including:
Systems management services;
Remote access services;
Backup and Recovery services;
Advanced printing capabilities.
MIS is often forced to do its own integration patches when putting together various utilities with a network operating system. However, OS/2 Warp Server is integrated out-of-the-box so that
the components work smoothly together without the need for IS to patch and test it — then hope it all will really work together in a production environment. OS/2 Warp Server is also
modular in that administrators can choose to implement those services which best ﬁt the business plan — MIS is not forced into an all-or-nothing decision.
Directory and Security Server
For an enterprise-wide solution, IBM is providing — as a separate package — a standards-based Directory and Security Server (DSS). The directory provides administrators and users with a
"single view" of all resources and users across the corporate LANs and WANs. In addition, the directory provides the users access to all the network resources through a single logon.
Security services provide protection from unauthorized external and internal access.
Unlike proprietary network directory services, DSS is based on the Open Software Foundation's Distributed Computing Environment (OSF DCE). This means that other DCE-enabled
platforms and resources, including IBM mainframes, AS/400 midrange systems, and RS/6000 AIX servers — as well as Hewlett-Packard, Digital Equipment and Sun Microsystems clients
and servers — can be transparently accessed by OS/2 Warp Server and DSS administrators and users.


Back to Table of Contents
OS/2 Warp Server — the Business Application Solution
Since the announcements of LAN Server 4.0, NT Server 3.51 and NetWare 4.1 in the Fall of 1994, there have been a number of reviews and benchmarks of NOSs reported in the industry
press, most of which end by recommending Microsoft's NT Server 3.5x in spite of its numerous reported ﬂaws. However, given the positive reactions to OS/2 Warp Server by its Beta users,
and from what Aberdeen has seen of the product, IBM must have taken LAN Server's reported short comings to heart and used them as a product development feature/function list.
Once perceived as ungainly, the installation process is now dramatically reﬁned — to the extent that most administrators will be able to use the Easy Installation process which includes
device autodetection. The installation process is modular — users are not forced to install all the features, functions and utilities.
As with LAN Server 4.0, OS/2 Warp Server uses the Multi-Protocol Transport Services (MPTS) — a framework for the protocol independence administrators have been demanding. The
MPTS framework provides concurrent support for the popular protocols such as NetBIOS, IPX, TCP/IP and 802.2.
OS/2 Warp Server has preemptive multitasking and multithreading. Preemptive multitasking allows administrators to manage the processing of concurrent tasks and assignment of priorities
based on business rules rather than forcing administrators to follow the operating system's sequence. It also removes the pain of the "three-ﬁnger salute" of control-alt-delete — having to
reboot the entire system if one application crashes. Multithreading allows applications to run multiple functions concurrently across several processors rather than sequentially on one, giving
the system a no-cost performance boost.
Many of OS/2 Warp Server's strengths are based on its use of objects. Objects combine data and algorithms into a single, self-contained software module. Objects are essentially software
building blocks that are linked together to form a working client-server application. With OS/2 Warp Server, objects are used to perform drag-and-drop administrative tasks, such as adding
new resources and users. The use of objects also plays a major role in the implementation of DSS's administrative services, and OS/2 Warp Server's ability to link resources throughout the
enterprise.
The High Performance File System (HPFS) provides OS/2 Warp Server with excellent uniprocessor performance. One OS/2 Warp Server draw-back, the lack of symmetric multiprocessing
(SMP) capability for low-cost
scalability, will be ﬁxed with a SMP upgrade which was entering beta testing as this report was being written. When released, this free upgrade will allow administrators to add relatively
inexpensive CPUs to a system rather than add an additional server in order to improve performance.
Back to Table of Contents
Everything but the Kitchen Sink?
OS/2 Warp Server beta users interviewed were pleased with the basic product — and very enthusiastic about the utilities and services now included. While other network operating systems
have add-on utilities which provide similar functionality to what is in the OS/2 Warp Server package, to our knowledge no other supplier provides them in the same shrink-wrapped package
with the NOS as no-cost extras. Figure 1 lists the services provided with OS/2 Warp Server. Descriptions of the major services follow.
Figure 1- OS/2 Warp Server Product Package
Source: IBM, February 1996
Systems Management
OS/2 Warp Server includes an integrated systems management package based on IBM's SystemView for OS/2 and NetFinity manage-ment products. In addition to managing any OS/2 Warp
Servers on a LAN, OS/2 and Windows clients can also be managed. Windows 95 and Windows NT Workstation clients are in development and will be available soon.
Over the past year, Aberdeen has interviewed scores of network and LAN managers, to determine which features they desire most in a server's operating system. Management tools in general
topped the list, and the management tools provided by OS/2 Warp Server map very well against those administrators want.
The systems management utilities include a software inventory discovery function for keeping track of both shrink-wrapped applications as well as those developed in-house. The predeﬁned
list of applications include those from Microsoft, Lotus, IBM and Novell. For tracking applications developed in-house, and others not on the predeﬁned list, administrators have access to a
dictionary for adding new software deﬁnitions.
Hardware and software asset management that provides full inventory details on IBM and non-IBM PCs is included. The asset manager keeps track of memory, disk, adapter, etc.
Performance monitoring and help desk tools are also included.
Software distribution is turning out to be one of the more expensive network management functions given the human resources needed to manually update each desktop every time a new
version of an application is released. IBM has ported major components of its NetView DM/6000 software distribution utility to the OS/2 Warp Server — allowing for remote updates of
applications from the server to clients without the need for on-site intervention. While this utility requires up-front training, the payback in personnel savings can be signiﬁcant.
A systems alert manager is also part of the package, and it can be tailored to generate different levels of alerts for different problems. For instance, remote server and client systems can be
monitored and managed from a central server. For the enterprise, alerts from the OS/2 Warp Server can be fed to a central SystemView console. Aberdeen feels that all enterprise
management platforms — whether from IBM, Hewlett-Packard, Sun, et al — are far from fully developed, and it still takes considerable staff intervention to manage an enterprise-wide
network. OS/2 Warp Server's system management utilities can at least make a difﬁcult situation easier, and lay the ground-work for that time when the management platforms are more fully
developed.


Backup and Recovery
OS/2 Warp Server now includes Personally Safe and Sound, an integrated backup and recovery service. In small organizations and depart-ments, the OS/2 Warp Server can also act as a
standalone backup server for the LAN.
In larger organizations, with multiple OS/2 Warp Servers, a centralized and dedicated server can be used to back-up other servers on the LAN, including those using Novell's Net-Ware or
Microsoft's NT Server. This feature allows for backing up the LAN without reducing server performance or requiring system downtime by taking advantage of the multi-threaded design of
the operating system.
An OS/2 Warp Server backup server can become an AdStar Distributed Storage Manager (ADSM) client as part of an enterprise-wide hierarchical storage management (HSM) design which
may include other IBM servers (mainframe, RS/6000 AIX and AS/400) and/or servers from HP or Sun which have the appropriate ADSM product installed.
No matter how it is implemented, the application uses a graphical user interface which is both useful and attractive, and makes backup administratively easy. The GUI walks the administrator
through the development of a backup strategy for automatic implementation at pre-set times.
Remote Access
OS/2 Warp Server provides three types of remote access: Remote Client, Remote Con-trol and Remote Node. Remote Client pro-vides users with the familiar dial-in to access an application
(i.e., e-mail) or services on a server.
Remote Control allows a remote user to "take over" his or her ofﬁce PC which is on the ofﬁce network, for access to ﬁles and local services.
Remote Node allows a mobile user to log-on to the LAN (or WAN if using DSS) and be treated the same as any locally attached desktop.
Remote Client and Remote Control in essence treat the guest device as a terminal, with little processing taking place on the remote device. Remote Node, on the other hand, is critical for
users needing to access applications and services which are on systems other than the local host, and especially to run those applications which are truly client/server based. Here again,
administrators would have to buy one or more add-on applications to gain the same functionality when using other NOSs.
Back to Table of Contents
Internet Access
Warp Server includes protocols necessary for it to be an Internet server platform. Many of the OS/2 Warp Server components can be used to provide Internet connectivity options, including
LAN and dial-up support (SLIP, PPP, and remote LAN access) with its native TCP/ IP protocol support — both directly to a corporate network or through an Internet service provider. Figure
2 is a picture of an administrator's screen, depicting the range of services available through OS/2 Warp Server.
Figure 2 - OS/2 Warp Server Administrator's Screen
Source: IBM, February 1996
Application Server
There are already many applications which run on OS/2 Warp Server, and IBM is moving quickly to position OS/2 Warp Server as a client/server application platform by recruiting many key
independent software vendors (ISVs).
Btrieve Technologies, Inc., has agreed to make hundreds of its applications available on OS/2 Warp Server by mid-1996. Sybase has ported its SQL Server for the platform, and Vinca has
ported its fault-tolerant package for OS/2 Warp Server. Oracle and other ISVs are also porting their databases and applications to OS/2 Warp Server for early 1996 shipment.
Back to Table of Contents
Directory and Security Server
As Aberdeen's Proﬁle of LAN Server 4.0 pub-lished in 1994 highlighted, IBM has been a consistently strong supporter of the Open Software Foundation's development of its standards-based
Distributed Computing Environment (DCE).
After a considerable development and testing effort, IBM will shortly ship DCE-based Directory and Security Server (DSS) software for OS/2 Warp Server.
Digital Equipment, Hewlett-Packard, Sun Microsystems, Sequent, Oracle and many other major hardware and software suppliers have signed on to develop DCE-compliant systems and
applications. Therefore, OS/2 Warp Server will have the ability to interact with a wide range of IBM and non-IBM systems and applications.


The IBM value-add includes the addition of a graphical user interface (GUI) to the DCE services. Thus, as an example, the powerful cross platform directory can be created and updated
through an easy to use, object-based, drag and drop GUI.
OS/2 Warp Server, out of the box, uses the same concept of "domain" as does LAN Server, LAN Manager and — given the common parentage — NT Server. The development of a domain
allows users a single logon to the LAN, with access to the resources on that LAN.
Compared to the global directory services provided by NetWare's Network Directory Services (NDS) and Banyan's StreetTalk, domains lack the power to cross LAN boundaries effectively.
This has been a major factor inhibiting both IBM's LAN Server and Microsoft's NT Server from becoming a true enterprise-wide NOS.
DCE-compliant directory services and security for OS/2 Warp Server has many implications for users since it provides the capability for disparate servers and clients to operate as a uniﬁed
network of systems.
Ultimately, DSS may turn OS/2 Warp Server into the industry's ﬁrst true enterprise-wide NOS, connecting not only all its own servers — as Novell's NDS does — but also, unlike NDS,
bringing in all other platforms a customer has within the enterprise network.
DSS gives users single logon capabilities — the ability to logon once to the entire enterprise network and access services on various hosts without having to logon to those hosts individually.
The DSS directory services also give OS/2 Warp Server administrators a way to manage the entire enterprise network, including remote sites. The DSS directory can manage thousands of
users, devices, objects and other resources on a global basis — from either a central location or distributed locations.
Banyan's StreetTalk and Novell's NDS are the two leading network operating system directory services available today.
But, Novell is still living in a NetWare-centric world — NDS only brings together NetWare servers, and only those based on NetWare 4.x.
Among Aberdeen's clients, Banyan is fast losing market acceptance as a viable NOS supplier and has lost much of its competitive edge over the past year.
OS/2 Warp Server will continue to support the domain naming structure. Unlike Novell's NDS, this will allow customers to install the optional directory services only when they want to, and
at their own pace.
With both single logon and central management OS/2 Warp Server users also have the advanced security promised through DCE. The DCE security model uses a series of encryption
methods to ensure not only that unauthorized users be denied access to ﬁles, it also ensures that messages and transmissions cannot be forged by one user claiming to be another.
DSS' DCE security features are based on Kerberos, a sophisticated but non-proprietary security model. It provides user authentication and authorization with encryption allowing for a safe
single logon — without the need for passwords ﬂowing across the network.
The services included in DSS will be an extra-cost add-on to OS/2 Warp Server and can be implemented within the enterprise over time. DSS does not force administrators to implement it all
at once.
Finally, IBM has also taken the time to build an excellent set of tools to assist the administrator in installing and implementing DSS across the network.
Back to Table of Contents
Aberdeen Conclusions
For any size business, OS/2 Warp Server is an excellent product for traditional ﬁle and print services, and compares very well against the traditional network operating systems such as
NetWare and Banyan Vines.
Further, OS/2 Warp Server, with all its added utilities, is equally an excellent application operating environment, exceeding the functionality of Microsoft's NT Server even when the needed
extra-cost utilities are included.
Having Oracle7, the long list of Btrieve applications, as well as SQL Server available goes a long way to settling the question of application and database availability. And, even with its
short-term deﬁciency — waiting for SMP support — management at IBM shops still need to think long and hard before moving to something else beside OS/2 Warp Server.
Executives in non-IBM shops who are looking for a NOS for work groups, departments and small divisions are well advised to include OS/2 Warp Server on their short list for 1996.
While possible, it is incredibly difﬁcult to build enterprise-wide computing networks without three major ingredients: the use of conforming objects, the use of distributed directory services
and the skillful implementation of network security.
To the best of our knowledge, OS/2 Warp Server with DSS is at least a year ahead of both NetWare 4.x's and NT Server's ability to provide all three in an integrated package.
Those executives who wish to go beyond just serving the department or division , those with the enterprise in mind, and those interested in developing true multi-tier, distributed client/server
applications must look to OS/2 Warp Server to identify the application server operating system of choice.
Aberdeen believes that IBM's plans for OS/2 Warp Server will be successful in 1996. We project that the following four activities will ensure that its market position improves from an
already strong start.
First, IBM will continue to add more features and functions — such as SMP — to OS/2 Warp Server. Second, more third-party software, such as Oracle with DCE compliant Oracle7, will
become available. Third, as more multi-tier applications are deployed, MIS will be confronted with the need for a robust mid-tier operating system to enable true distribution of applications
and their data across the enterprise.
Fourth, and very important in Aberdeen's view, IBM will put some considerable marketing muscle behind these deserving products so that the customers have a fair chance to evaluate them.
As these events unfold, it will be much easier for MIS to make OS/2 Warp Server the short list choice — since its strengths uniquely matches so many enterprise needs.
Back to Table of Contents
Aberdeen Group Registration
Home Page || General Information
HTML Market Research|| Aberdeen Abstracts
Aberdeen Group Publications||Custom Consulting
©Aberdeen Group, Inc.
One Boston Place
Boston, Massachusetts
02108
Contact: Chris Stevenson
Voice: (617)723-7890


Fax: (617)723-7897
E-mail: chriss@aberdeen.com
The trademarks and registered trademarks of the corporations mentioned in this publication are the property of their respective holders. Unless otherwise noted, the entire contents of this publication are copyrighted by Aberdeen
Group, Inc. and may not be reproduced, stored in a retrieval system, or transmitted in any form or by any means without prour written consent of the publisher.
Copyright © 1996 Aberdeen Group, Inc., Boston, Massachussetts
This Document is for Electronic Distribution Only -- DO NOT COPY


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-ibm-os2-warp-server |
| title | IBM's OS/2 Warp Server: The Whole is Greater Than the Sum of the Parts |
| author | Aberdeen Group |
| date | 1996-02-19 |
| type | product-viewpoint |
| subject_domain | server-network-operating-systems |
| methodology | industry-analysis, competitive-profiling, field-research |
| source_file | 1996 IBM_s OS_2 Warp Server_ The Whole is Greater Than the Sum of the Parts pvp.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group evaluates IBM's newly released OS/2 Warp Server, arguing it combines the networking strengths of Novell NetWare with the application strengths of Microsoft NT Server plus integrated directory and security services via a DCE-based Directory and Security Server (DSS) add-on. The study contends that OS/2 Warp Server is at least a year ahead of competitors in delivering an integrated, enterprise-wide NOS with objects, distributed directory services, and network security.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Published during peak NOS competition; offered credible third-option assessment but OS/2 held niche position and did not reshape industry decisions. |
| **Relevance** | low | OS/2 Warp Server was discontinued by IBM in 2006 and never achieved mainstream adoption; primarily of historical interest. |
| **Prescience** | low | Aberdeen predicted OS/2 Warp Server market success in 1996; instead the product lost market share to Windows NT and was sunset by 2006. |

### Prescience Detail

**Prediction 1:** OS/2 Warp Server market success in 1996
- **Claimed:** IBM's plans for OS/2 Warp Server will be successful in 1996; market position will improve from already strong start
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 1:** OS/2 Warp Server market fate
- **Result:** IBM discontinued OS/2 support December 31, 2006; never achieved mainstream enterprise NOS adoption; lost decisively to Windows NT Server
- **Confidence:** verified
- **Notes:** Wikipedia: IBM ended OS/2 Warp 4 support 2006; internal IBM budget cuts decimated OS/2 marketing by 1997

**Prediction 2:** DSS as enterprise-wide NOS catalyst
- **Claimed:** DSS may turn OS/2 Warp Server into industry's first true enterprise-wide NOS connecting all platforms
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 2:** DSS enterprise NOS adoption
- **Result:** Microsoft Active Directory (shipped 1999) dominated enterprise directory market; DSS/DCE never achieved predicted enterprise-wide NOS role
- **Confidence:** verified
- **Notes:** Microsoft Active Directory became the standard; Kerberos (used by DSS) survived as an authentication protocol but within Microsoft's ecosystem

**Prediction 3:** IBM marketing investment in OS/2 Warp Server
- **Claimed:** IBM will put considerable marketing muscle behind OS/2 Warp Server products (fourth of four success factors)
- **Year:** 1996
- **Confidence at time:** low

**Actual Outcome 3:** IBM marketing investment in OS/2 Warp Server
- **Result:** IBM investment in OS/2 marketing was inadequate; internal IBM politics and budget cuts decimated OS/2; product withdrawn from mass market by 2001
- **Confidence:** verified
- **Notes:** Documented extensively in OS/2 Wikipedia article; IBM conceded OS/2 was not viable for PC business

### Entities Referenced (12)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| IBM | company | active | — |
| Aberdeen Group | firm | acquired | Aberdeen (Harte-Hanks -> Spiceworks-Ziff Davis) |
| Novell, Inc. | company | acquired | Attachmate (2011) -> Micro Focus (2014) -> OpenText (2023) |
| Microsoft Corporation | company | active | — |
| Banyan Systems | company | dissolved | ePresence (1999); services div sold to Unisys (2003) |
| Oracle Corporation | company | active | — |
| Sybase, Inc. | company | acquired | SAP (2010) |
| Btrieve Technologies, Inc. | company | acquired | Pervasive Software (renamed 1994) |
| Digital Equipment Corporation | company | acquired | Compaq (1998) -> HP (2002) |
| Hewlett-Packard | company | active | HP Inc / HPE (split 2015) |
| Sun Microsystems | company | acquired | Oracle (2010) |
| Vinca Corporation | company | acquired | Novell (1999) |

### Technologies Referenced (10)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| IBM OS/2 Warp Server | platform | IBM | emerging | obsolete |
| IBM LAN Server 4.0 | platform | IBM | mature | obsolete |
| Novell NetWare 4.x | platform | Novell | mature | obsolete |
| Microsoft NT Server 3.5x | platform | Microsoft | emerging | obsolete |
| OSF DCE | framework | Open Software Foundation | emerging | legacy-supported |
| Directory and Security Server (DSS) | application | IBM | emerging | obsolete |
| HPFS | protocol | IBM/Microsoft | mature | obsolete |
| TCP/IP | protocol | IETF | emerging | active |
| ADSM | application | IBM | mature | obsolete |
| IBM NetFinity | application | IBM | emerging | obsolete |

### Observation Summary

- Total observations: 25
- By type: technology-assessment: 13; viability-prediction: 3; actual-outcome: 3; strategy-classification: 2; expert-opinion: 2; market-data: 1; benchmark-result: 1
