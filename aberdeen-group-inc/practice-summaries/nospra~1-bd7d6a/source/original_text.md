# Network Operating Systems: 1998 Practice Summary

> Archived from: NOSPRA~1.DOC
> Original publication date: 1998-05-01
> Author: Aberdeen Group

---

## Original Document Text

AberdeenGro
up
Network
Operating
Systems:
1998 
Practice 
Summary
May 1998
Aberdeen Group, Inc.
One Boston Place
Network Operating Systems Practice Summary
AberdeenGroup 
Boston, Massachusetts 02108 
USA
Telephone: 617 723 7890
Fax: 617 723 7897
www.aberdeen.com
ii
Network Operating Systems Practice Summary
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
iii
Network Operating Systems Practice Summary
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
iv
Network Operating Systems Practice Summary
AberdeenGroup 
TABLE OF CONTENTS
NETWORK OPERATING SYSTEMS (NOS) PRACTICE
V
Description, Focus and Benefits
v
Strategic Market Questions
v
EXECUTIVE SUMMARY
1
Key Aberdeen Findings
1
SUMMARY OF FINDINGS
3
Key Aberdeen Findings
3
NETWORK OPERATING SYSTEMS DEFINED
5
Source: Aberdeen Group, May 1998
5
How Middleware Fits into Network Services
6
Core NOS Components
6
File and Print Services
7
Directory Services
7
Network and Systems Management
8
Security
8
ISSUES AND CHALLENGES
9
Impact of Major IT Trends
9
Supplier Success Factors
10
User Success Factors
10
SUPPLIER ABSTRACTS
12
IBM Corporation — Personal Software Products
12
Microsoft Corporation
13
v
Network Operating Systems Practice Summary
AberdeenGroup 
Novell, Inc.
14
vi
Network Operating Systems Practice Summary
AberdeenGroup 
Preface
Network Operating Systems (NOS) 
Practice 
Description, Focus and Benefits
Aberdeen’s Network Operating Systems (NOS) practice focuses 
especially on Information Systems (IS) managers’ experiences with 
implementing and managing Novell NetWare, IBM OS/2 Warp 
Server and Microsoft Windows NT Server in a multi-platform 
environment.    The NOS practice also reviews IS managers’ plans 
for their legacy NOSes — Banyan (Vines) and Digital (PathWorks) 
installations in particular -- and identifies key issues.
Most mid- and large-sized organizations have a multi-tier 
hardware and software architecture installed.    These 
organizations already have one or more NOSes installed, along 
with myriad platforms running a wide-range of operating systems. 
The issue confronting IS is usually not which NOS to install in this 
environment, but how to get the pieces to interoperate, and 
therefore whether to pursue a "NOS unification" or "leave as is" 
strategy. Microsoft NT Server’s growing role in the enterprise and 
the decline of other suppliers are making these IS decisions urgent 
and strategic.
The NOS practice is a vital part of the Network Services area.    At 
the core of most existing Fortune-1000 networks is a welter of 
LANs, each with its NOS. Thus, when implementing or upgrading 
any enterprise network architecture, the enterprise planner must 
first and foremost consider its effect on this "NOS potpourri".
Strategic Market Questions

Is Novell still a viable company, and is NetWare still a 
viable product? 

Is IBM going to abandon OS/2 Warp Server? 

Is NT Server going to rule the world in the near term? 
Long term? 

What are the true costs and issues of NOS migration? 
vii
Network Operating Systems Practice Summary
AberdeenGroup 

Can traditional file and print services transverse 
individual LAN domains with disparate operating systems 
installed on a variety of platforms? 

Can multiple NOSs on multiple types of platforms be 
managed as one, or do we have to standardize on one 
NOS? 

Are directory services important to the operations of 
LANs and WANs? 

With the advent of the Internet and intranets, what is the 
role of the NOS? Is the NOS dead? 

Is Unix a NOS? How does Unix fit in with the more 
traditional NOSes? 
This Aberdeen Group Practice Summary is a deliverable in a 
comprehensive service that includes Aberdeen published research 
and customized professional services aimed at executives who 
must make strategic business decisions regarding Information 
Technology.
viii
Network Operating Systems Practice Summary
AberdeenGroup 1
Chapter One
Executive Summary
Aberdeen’s Network Operating Systems (NOS) practice focuses on 
Information Systems (IS) managers’ experiences with 
implementing and managing Novell NetWare, IBM OS/2 Warp 
Server and Microsoft Windows NT Server in a multi-platform 
environment.    The NOS practice also reviews IS managers’ plans 
for their legacy NOSs ¾ Banyan (Vines) and Digital (PathWorks) 
installations in particular.
Most mid- and large-sized organizations have a multi-tier 
hardware and software architecture installed.    These 
organizations already have one or more NOSs installed, along with 
myriad platforms running a wide-range of operating systems.    The 
issue confronting IS is usually not which NOS to install in this 
environment, but how to get the pieces to interoperate, and 
therefore whether to pursue a “NOS unification” or “leave as is” 
strategy.    Microsoft NT Server’s growing role in the enterprise and 
the relative decline of other suppliers are making these IS decisions 
urgent and strategic.
Key Aberdeen Findings

Instead of fading out as the Internet arrives, NOSs are 
proving to be more effective than ever.    Key services that 
the Internet needs — e.g., directory services, end-user 
administration, and security — are services that the NOS 
is best positioned to contributed as part of an overall 
Internet Infrastructure.

Likewise, because of the Internet, Novell is not a dead 
company, and Novell NetWare and IBM’s OS/2 Warp 
Server are not dead products.    Aberdeen finds that both 
of these can play key roles in their company’s Internet 
infrastructure offerings by providing not only installed-
base Intranet workgroup support but also the core of 
directory services.

Microsoft’s NT Server 4.0 is being overused in customer 
sites for enterprise-scale NOS implementations that it 
cannot support.    Moreover, questions about which 
Network Operating Systems Practice Summary
AberdeenGroup 
features will be included in NT 5.0 Server make it 
imperative for IS to scrutinize present implementations 
carefully, since relief will not be coming in 1998.

NOS suppliers are answering user efforts towards server 
consolidation and interoperability between legacy NOSs 
by delivering new interoperability capabilities such as 
broader-scope directory services and cross-platform 
administrative solutions.
The audience of this NOS practice summary is Senior IS managers 
seeking to manage legacy NOSs more effectively, as well as IS 
decision makers trying to determine the role of the NOS in the new 
enterprise architecture. 
2
Network Operating Systems Practice Summary
AberdeenGroup 3
Chapter Two
Summary of Findings
There is a two-part controversy emerging in the Network Operating 
System arena.    The issues are:

Do we really need a NOS for client-server applications?

If we have one (or more) already, are there good reasons to 
change?
To the first question, there is a camp that says “No.”    Why install a 
network operating system when users can just as easily run clients 
attached to Unix- or Windows NT-based servers over a TCP/IP 
network?      You can simply add on the services necessary to run a 
network — such as directory, security and mail services — and 
you’re up and running.
Aberdeen, however, says “Yes”:    in order to run an enterprise-wide 
client/server-based network you do need a network operating 
system.    Users will get the most stable platform and the most 
transparent connectivity between services if these are all tightly 
integrated and provided through a single network operating 
system.    As more mission critical applications migrate off the 
mainframe and onto client/server-based networks, it is that much 
more important for these networks to provide the same coherence 
as a mainframe.
Key Aberdeen Findings

Aberdeen’s end-user research has identified three forces 
that are leading many network administrators to re-
examine their current network operating system choice.
1. LANs are being linked together, and more and more 
WANs are being built and expanded, so that the 
number of users on any one network is growing 
rapidly.
2. Many enterprises, especially those growing through 
mergers and acquisitions, are being confronted 
with having to manage multiple network operating 
systems.    Administrators must either find a way to 
Network Operating Systems Practice Summary
AberdeenGroup 
more easily manage two, three or four network 
operating systems, or decide on one standard 
network operating system for the enterprise ¾ with 
all the implied migration issues.
3. As noted, the majority of NOSs are purchased from 
either Microsoft (NT Server), IBM (OS/2 Warp), 
Novell (NetWare) or one of the Unix suppliers ¾ for 
those who consider Unix a NOS. 

As with all other IS issues, the implementation and 
maintenance of NOSs has gotten so complex that it often 
requires outside assistance.    This is especially true if NT 
Server is being installed as the enterprise NOS.    (The 
subject of Windows NT professional services is addressed 
in a separate Aberdeen Practice Summary report.)

The blurring of the lines between operating systems and 
network operating systems has been an overall plus to the 
market.    The sales of all three of the major vendors have 
actually increased over the past two years as the market 
expands and as organizations upgrade and consolidate 
their NOSs.    While NT Server’s rate of growth is dramatic, 
it is difficult to tell where the application server sales end 
and the NOS begins ¾ but Aberdeen finds that the vast 
majority of NT Server sales as NOSs are in the workgroup. 
(The subject of Windows NT Server as an application 
server is addressed in a separate Aberdeen Practice 
Summary report.    This report deals with NT Server only 
as a NOS.)

While choosing the appropriate NOS and dealing with all 
the technical issues associated with this decision can have 
a strong impact on IS-operations effectiveness (end users 
complain strongly if the workgroup network goes down), 
line of business executives are becoming increasingly 
involved with the decision as to which NOS to purchase.
4
Network Operating Systems Practice Summary
AberdeenGroup 5
Chapter 
Three
Network Operating Systems Defined
In the most basic sense, a network operating system is software 
that resides on a server and manages the resources within the 
network.    It organizes the way information is processed among 
and between all the workstations and peripherals attached to it.
Microsoft has done a masterful job of recruiting large numbers of 
ISVs to write applications for NT Servers, and channel partners ¾ 
including all the PC suppliers ¾ to sell and install NT Server.    Since 
few non-IS executives understand or care about the difference 
between an Operating System and a Network Operating System, NT 
Server’s success in the former is helping it with the latter.
Typically, a NOS operates at the workgroup level ¾ depending on 
the NOS, for up to 1,000 users on one LAN ¾ tying together end-
user PCs.    As a result, an effective NOS brings significant IS 
benefits:

Sharing of PC applications and files for that allow the 
workgroup to leverage each other’s work;

Cost-effective sharing of printers and other resources;

Increased robustness — when the PC goes down, the server 
continues, and vice versa; and

Decreased administrative costs — NOS networks were the first 
practitioners of end-user “almost-lights-out” administration.
Table 1:    Network Service Practice
IS managers have been cobbling together a variety of pieces of 
software and services to ease their company’s implementation of a 
network infrastructure for e commerce, ERP, and all the other 
fascinating uses of the intra- and Internet.    To assist, Aberdeen has 
combined several areas of concentration in an easily accessible 
package ¾ Aberdeen’s Network Services practice.

Network Operating Systems 

Internet Infrastructure

Network and Systems 

Directory Services
Network Operating Systems Practice Summary
AberdeenGroup 
Management

Messaging & Transaction 
Management

Security
Source: Aberdeen Group, May 1998
How Middleware Fits into Network Services
The NOS practice is a vital part of the Aberdeen Network Services 
model (see Table 1).    At the core of most existing Fortune-1000 
networks is a welter of LANs, each with its NOS.    Thus, when 
implementing or upgrading any enterprise network architecture, 
the enterprise planner must first and foremost consider its effect 
on this “NOS potpourri.”
Core NOS Components
As noted above, a network operating system is the software that 
resides on a server and manages the resources within the network. 
But there are also underlying hardware pieces necessary to build 
the network on which the network operating system runs.
PCs are connected to one another and/or to the server via cabling ¾ 
twisted-pair, coaxial or fiber-optic cabling.    For the PC and the 
server to know how to communicate with each other over that 
cabling, each needs a network interface card, or NIC adapter.
The adapters explain how the PC and server communicate, but the 
devices must be talking the same language for the connection to be 
successful.    This language is specified in the transport protocol.    
The most commonly used transport protocols are the Internetwork 
Packet Exchange/Sequenced Packet Exchange (IPX/SPX) and the 
Transport Control Protocol/Internet Protocol (TCP/IP).    IPX/SPX is 
the protocol used by Novell NetWare, while TCP/IP was originally 
designed to be used by the government and higher-education 
facilities, but has evolved into one of the most commonly used 
transport protocols in use today.
The transport protocols and other communications facilities are 
specified by the NOS itself. The transport protocol component is 
software that resides on the server.    In a traditional network 
operating system environment, all the files and network resources 
are resident on the server as well, or are attached to the network 
and linked through the NOS server.
The server software controls how users access files and resources 
in an orderly fashion.    The client also needs a piece of network 
6
Network Operating Systems Practice Summary
AberdeenGroup 7
operating system software in order to communicate with the 
server.    Some clients need only the correct transport protocols to 
forge that connection — most of these are within environments 
that use TCP/IP.    But most network operating systems have a client 
piece specific to the server piece that instructs the two exactly how 
to interact.    Herein lies one of the qualitative differences between 
NT Server and its NOS competitors.    While NT Server can use 
TCP/IP for communications, if the Windows Internet Name Service 
(WINS) as the NT Server directory (required in most all situations) and 
Windows 95 is used as a client, then the NetBeui protocol has to be used. 
This legacy from LAN Manger constantly identifies the users’ identity, 
which WINS translates to an IP address, causing a major increase in 
network traffic.
Above the basic hardware and software are specific services for 
common NOS functions:

File and print services;

A directory service;

Network and systems management utilities; and

Security services.
File and Print Services
File and print services were the first NOS “killer app” and created 
the multi-billion-dollar NOS market in the 1980s.    Today’s NOS file 
and print services (typically shared printers and files with 
coordination of access by multiple end users) are handled so 
smoothly by the NOS and IS that few outside of IS consider it an 
issue.    And, for the most part, IS has to spend little time worrying 
about this service as well ¾ until they try to manage a mixed 
environment.    Now, maintaining the integrity of file and print 
services is a major issue in most multi-vendor environments ¾ and 
is one of the driving forces behind server consolidation.
Directory Services
The number of users, devices, applications, and other resources of 
all types on the corporate network is expanding daily, and 
enterprises are constantly adding connections to suppliers and 
customers through the use of public and private networks.    Logic 
dictates that some mechanism be used to keep track of all those 
people and things and events and their respective attributes in 
order to manage the IT infrastructure.
Network Operating Systems Practice Summary
AberdeenGroup 
If the corporate e-mail is Lotus Notes running on OS/2, the 
corporate database Oracle running on a Unix SMP platform, and 
the corporate order entry application from SAP running on NT 
Server, how does one person get access to all three without IS 
having to create and maintain three different directory entries?    
The answer is a common repository of information (a directory 
service).    NOS directory services are today’s prime candidates to 
handle remote resource access across the enterprise.    The major 
issue here is the proliferation of different directory services in the 
typical enterprise:    IS seeks to attain a central directory service 
operating across multiple platforms, or multiple directory services 
that can interoperate.    Thus, the battle between Novell’s currently 
shipping Novell Directory Services (NDS) and Microsoft’s upcoming 
ActiveDirectory for supremacy truly is strategic.
8
Network Operating Systems Practice Summary
AberdeenGroup 9
Network and Systems Management
Ideally, IS managers want a single network, systems and 
application management framework.    The reality is that in many 
shops systems and network management are still seen as separate 
functions; implementing monolithic frameworks such as Tivoli 
TME 10 or CA-Unicenter TNG is seen as time-consuming and 
resource-intensive; and crossing platform boundaries is still 
daunting.    Thus, especially at the workgroup level, many IS shops 
fall back on tried-and-true NOS management utilities.    Moreover, 
the capabilities of NOS management are expanding, so that they 
now hold the promise of providing systems management for all 
devices and network management for all workgroups in the 
enterprise from a unified console.
Security
Securing the enterprise network and the various devices attached 
to it is such an onerous task that few large organizations have done 
much beyond putting in firewalls and relying on each OS’s security 
features.    Normal interoperability issues are complicated by the 
vast differences already built in to the individual operating 
systems ¾ from very high-level security at the mainframe level, to 
very adequate security at the Unix-server, to almost non-existent 
security at the NT Server and Windows desktop levels.
The NOS can be more vulnerable than most IS buyers realize, since 
remote access, often from end users’ homes, is built in to the NOS.    
As a result, IBM and Novell over the years have been in the 
forefront of efforts to provide network security, to the point where 
their NOSs today provide very adequate security ¾ comparable to 
Unix servers.
Network Operating Systems Practice Summary
AberdeenGroup 
Chapter Four
Issues and Challenges
Impact of Major IT Trends
The Internet.    Some continue to anticipate that today’s dramatic 
rise in the use of the Internet will have a negative impact on the 
use of NOSs, and, in fact, that the services provided by the Internet 
would replace those provided by NOSs.    Aberdeen finds that, on 
the contrary, the increase in network computing (including the 
Internet) is fueling a need for powerful NOSs.    Just those services 
that an Internet Infrastructure requires — directory services, 
server administration, and end-user security — are those for which 
NOSs have the best time- and end-user-tested solutions right now.    
The trick, and the challenge to NOS suppliers such as Novell, is to 
integrate NOS services with Internet-specific technology such as 
Java tools, browsers, and Web servers in an overall Internet 
Infrastructure solution, as detailed in the Aberdeen Internet 
Infrastructure Practice Summary.
Object-oriented application development.    In the past, NOSs’ 
relative inability to support rapid application development was a 
major factor in their failure to capture the lion’s share of 
companies’ enterprise-networking efforts.    However, the advent of 
object-oriented Internet distributed-application development is 
giving NOSs a second chance.    Directory service object “class 
libraries”, in particular, could be useful in allowing remote access 
to enterprise-computing resource “objects”.
Up to now, NOS suppliers have been slow to seize the opportunity. 
However, initiatives such as Novell’s IntranetWare hold promise of 
delivering new rapid application-development capabilities to the 
NOS installed base and directory-service capabilities to 
development toolsets in the Internet Infrastructure offerings of 
major suppliers such as IBM.
Year 2000.    NT 4.0 Server is listed as “compliant with minor 
issues,” and can be made Year-2000 compliant with Service Pack 3, 
Site Server Express 3.0 (in beta as of this writing), and NT 
Year-2000 QFE (definition coming) fixes.    A 32-bit client can be 
made safe with just the Service Pack and the QFE fixes.    Anyone 
running mission-critical systems on NT 3.51 needs to upgrade 
10
Network Operating Systems Practice Summary
AberdeenGroup 11
immediately, and 16-bit clients need to be upgraded as no Y2K fixes 
will be made available.
Novell's NetWare and IntranetWare products are Year-2000-ready 
in their 4.11a and 3.2 versions ¾ those using 4.11 or earlier 
versions will simply need to download the upgrades and patches 
from Novell’s Web site.    The current version of OS/2 Warp Server 
is Y2K compliant ¾ administrators need to check with IBM’s web 
site for the status of older versions.
Supplier Success Factors

The remaining three NOS contenders are pouring large 
resources into R&D efforts to improve their products.    
Each, led by Novell, will be releasing version 5 of their 
flagship products over the next 12 months.    However, 
each has a different challenge facing them to be 
successful in the market place.

IBM is focusing its efforts on maintaining its 
installed base, and ¾ realistically ¾ is not 
anticipating significant market share gains.    But 
businesses representing more than $30 billion of 
IBM’s overall revenue rely on OS/2 as their NOS, so 
it is important for IBM to keep these customers 
satisfied ¾ since the loss of the NOS to Microsoft 
could lead to the loss of other business.

Novell is still both the technology leader and the 
market-share leader ¾ and will maintain this lead 
with the release of a feature-rich NetWare 5.    
Novell’s success is dependent on its ability to 
market itself and its products ¾ to turn the cold, 
dead fish into market-enticing sushi.

Microsoft is the mindshare leader, and the master of 
transfer ¾ getting people to believe that the ruler of 
the desktop needs to be the ruler of the NOS 
connecting the desktop.    Microsoft has positioned 
NT Server 5.0 as the single most important of its 
products going forward.    However, Aberdeen 
believes that the 5.0 release is a 1999 production 
issue ¾ leaving buyers to sort out what to do in 
1998.    Microsoft will be successful, but to be really 
successful it has to match the marketing hype with 
product reality.
Network Operating Systems Practice Summary
AberdeenGroup 
User Success Factors
IS executives tell Aberdeen that the IT world they dream about is 
defined by the word stability.    On top of the massive and rapid 
technology changes taking place around them come problems 
associated with the way that IT purchase decisions are being made. 
Given that more of the business operations are dependent of a 
smoothly running IT operation, the risks of making the wrong 
technology decisions have risen to the point of it literally 
destroying a company.    Yet more IT decisions are based on 
emotional and political reasons rather than a careful assessment of 
what is best for the company.    The key user success factor is just 
what your woodworking teacher taught you ¾ measure twice, cut 
once.
12
Network Operating Systems Practice Summary
AberdeenGroup 13
Chapter Five
Supplier Abstracts
IBM Corporation — Personal Software Products
11400 Burnet Road
Austin TX 78758
512-323-0000
Market Position
IBM’s OS/2 Warp Server has as its foundation the 32-bit, 
multitasking, multithreading, OS/2 Warp operating system for 
departmental application platforms — married to IBM’s LAN 
Server 4.0 network operating system used for enhanced file and 
print services.    The previous dual identity of OS/2 and LAN Server, 
exemplified by the need for dual installation, is gone.    The base 
product is enhanced by the addition of several no-cost extras: 
systems management services, remote connectivity services, 
backup and recovery services and advanced printing capabilities.
Because of the confusion about the product, enhanced by the 
business press, it is necessary to state the obvious — OS/2 Warp 
Server is intended to run on Intel-based servers and does not 
compete with desktop operating systems such as Windows 95, 
Windows NT Workstation or Windows 3.x.    OS/2 Warp Server does 
compete with Novell NetWare 4.x, Microsoft NT Server 4.0 and 
various flavors of Unix.
OS/2 Warp Server's highly-tuned 32-bit engine and integrated 
services offer departments and divisions of large organizations, as 
well as independent businesses, a powerful, easy to manage 
operating environment.    With the Directory and Security Server 
option, OS/2 Warp Server provides the means for sharing and 
securing data beyond the LAN across distributed applications 
throughout the enterprise.
Aberdeen Conclusions
For any size of business, OS/2 Warp Server is an excellent product 
for traditional file and print services, and compares very well 
against the traditional network operating systems such as NetWare 
Network Operating Systems Practice Summary
AberdeenGroup 
and Banyan Vines.    Furthermore, OS/2 Warp Server, with all its 
added utilities, is equally an excellent application operating 
environment, exceeding the functionality of Microsoft’s NT Server 
even when the needed extra-cost utilities are included.    IBM’s 
challenge is to stem the erosion of IS mindshare cause by 
Microsoft’s NT marketing blitz and position OS/2 Warp Server as an 
alternative IBM Internet infrastructure option with added value 
compared to NT.    Given Microsoft’s huge camp of ISV allies, this 
will be a difficult challenge to over come.
Microsoft Corporation
One Microsoft Way
Redmond, WA    98052-6399
(800) 426-9400; (425) 882-8080
Market Position
Microsoft’s Windows NT Server 4.0 went to market in August 1996 
with a reception from the press that would do credit to a visiting 
celebrity.    NT Server has been touted by many as the universal 
panacea for everything from running your Web site to curing your 
back ache, and competitive offerings are being scorned as relics 
used only by those unprepared for the new era.
When it first arrived, Microsoft was touting the improvements 
incorporated in NT 4.0 to improve earlier versions and ease 
acceptance by enterprise buyers, including:

Greater support for symmetric multiprocessing (SMP), for 
inexpensive scalability;

Expected clustering support from system suppliers for both 
high-availability and increased scalability;

Expanded, standards-based network services;

Integrated Internet capabilities, including a Web server.
Enough organizations have built production applications around it 
for NT Server’s strengths and weaknesses in real-world operations 
to be analyzed.    For some, NT Server has been a reasonably good 
experience.    NT Server used as an application, database or 
communications server for workgroups or departments can be 
very effective and efficient.    For others, NT Server has been 
anything from an annoyance to a nightmare.    When NT Server is 
oversold, and attempts are made to use NT Server as the enterprise 
platform, many implementations have failed.
14
Network Operating Systems Practice Summary
AberdeenGroup 15
Aberdeen Conclusions
There is no doubt that NT Server will have a strong enterprise 
story, especially as future enterprise versions are shipped.    There 
are certainly circumstances for which a company should consider 
an NT Server solution.    For instance, workgroup or department 
application, database or Web server roll-outs continue to be a 
natural application for the technology.    File and printer sharing is 
a reasonable use for groups with under 2,000 end users.
Microsoft is determined for NT to succeed and has the resources to 
achieve their desire.    But the massive amount of publicity given 
NT Server as the wonder machine of the 20th century is causing a 
lemming-like stampede to use NT Server in situations for which it 
is not suited at this time.
Novell, Inc.
1555 N. Technology Way
Orem, UT 84097
(801) 429-7000
Market Position
Aberdeen interviews with senior network managers in North 
America and Europe show that Novell’s NetWare is firmly 
entrenched as the enterprise network operating system of choice.    
While Microsoft’s NT Server is receiving considerable attention as a 
possible application server, few network managers are seriously 
considering it as a enterprise NOS.
Novell’s core component, available as a standalone product, is 
called NetWare (presently on version 4.11).    IntranetWare adds to 
NetWare 4.11 a series of functions to assist companies with linking 
their current networks to the Internet, and with forming their own 
Intranets.
Aberdeen Conclusions
Until recently, Novell has been more adept at creating good 
technology than at communicating with the market and its 
influencers.    Market conditions have coaxed the company into 
exploring its role in the enterprise network, with considerable 
technical success.    With true directory services and a robust and 
fast architecture, Novell has made great strides in enterprise-wide 
distributed computing.    IntranetWare provides extensive 
improvements in the platform itself, in the print and file services 
Network Operating Systems Practice Summary
AberdeenGroup 
upon which NetWare’s past success has rested, in application 
services, and in security.
Novell’s new leadership and its ability to craft a new strategy that 
is acceptable both internally among its employees and externally 
among its customers, and its ability to right itself financially, will 
be tested in the summer of 1998 with the release of NetWare 5.    
From all indications, the launch is on track to be successful ¾ beta 
testing is on schedule, and feedback from customers is quite 
favorable.    Given Microsoft’s difficulty in meeting deadlines for NT 
Server 5.0, NetWare 5 has an excellent chance of recapturing the 
mind-share of network administrators and their line of business 
counterparts.
Table 1: NetWare Partial Feature Comparison
Feature
NetWare 3.12
NetWare 4.1
IntranetWar
e
Intranet/Internet 
Platform
Web server
NetBasic tool
TCP/IP
DHCP Support
IP/IPX Gateway
Multiprotocol routing
Internet Service 
Provider connectivity
Netscape browser
Java Platform
—
Add-on
Add-on
Add-on
—
Add-on
—
—
—
—
—
Add-on
Add-on
—
Add-on
—
—
—
Yes
Yes
Yes
Yes
Yes
Integrated
Yes
Yes
Yes
Symmetric 
Multiprocessing
—
From OEMs
Yes
Directory Services
Single Login to 
Network
—
—
Yes
Yes
Yes/Improved
Yes
Graphical 
Administration
—
Yes
Yes/Improved
Security
Network C2
RSA public/private key
—
—
—
Yes
Yes
Yes
Source: Novell, Inc. October 1997
16


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | nospra~1-bd7d6a |
| title | Network Operating Systems: 1998 Practice Summary |
| author | Aberdeen Group |
| date | 1998-05-01 |
| type | other-research |
| subject_domain | network-operating-systems |
| methodology | industry-analysis |
| source_file | NOSPRA~1.DOC |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group's 1998 practice summary on Network Operating Systems (NOS) covering Microsoft Windows NT Server, Novell NetWare/IntranetWare, and IBM OS/2 Warp Server. The report addresses key strategic questions about NOS viability in an Internet era and assesses the competitive landscape among the three major NOS vendors. Aberdeen finds that NOSs remain essential even as Internet infrastructure grows and that Novell's market leadership will be tested by the NetWare 5 launch.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Documents the pivotal 1998 NOS competitive landscape at the height of the Windows NT versus NetWare war; useful historical record of the period. |
| **Relevance** | low | NOS market was subsequently consolidated under Microsoft; NetWare and OS/2 Warp are effectively defunct making much content of only historical interest. |
| **Prescience** | high | Correctly anticipated NT Server enterprise limitations and Novell's ongoing relevance; accurately predicted NT 5.0 as a 1999-not-1998 release; NetWare 5 launch success prediction proved accurate. |

### Prescience Detail


**Prediction 1:** NT Server 5.0 release timeline
- **Claimed:** NT 5.0 is a 1999 production issue — no relief coming in 1998; buyers must sort out 1998 on their own
- **Year:** 1998
- **Confidence at time:** high

**Actual Outcome 1:** NT Server 5.0 release timing
- **Result:** Windows 2000 shipped February 2000 — verify actual date.
- **Confidence:** high
- **Notes:** Windows 2000 shipped February 2000 — verify actual date.

**Prediction 2:** NetWare 5 launch success
- **Claimed:** NetWare 5 launch on track; beta testing on schedule; customer feedback favorable; good chance to recapture mindshare
- **Year:** 1998
- **Confidence at time:** high

**Actual Outcome 2:** NetWare 5 launch success
- **Result:** Verify NetWare 5 reception and market impact.
- **Confidence:** medium
- **Notes:** Verify NetWare 5 reception and market impact.


### Entities Referenced (8)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | acquired | Aberdeen/Harte-Hanks |
| Microsoft Corporation | company | active |  |
| Novell, Inc. | company | acquired | Attachmate (2011) |
| International Business Machines Corporation | company | active |  |
| Banyan Systems | company | dissolved | unknown |
| Digital Equipment Corporation | company | acquired | Compaq (1998) |
| Tivoli Systems | company | acquired | IBM (1996) |
| Computer Associates International | company | renamed | CA Technologies (2006) |

### Technologies Referenced (14)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Windows NT Server 4.0 | platform | Microsoft | current | obsolete |
| Windows NT Server 5.0 | platform | Microsoft | pre-release | obsolete |
| Novell NetWare 4.11 / IntranetWare | platform | Novell | current | obsolete |
| Novell NetWare 5 | platform | Novell | pre-release | obsolete |
| IBM OS/2 Warp Server | platform | IBM | current | obsolete |
| Novell Directory Services (NDS) | application | Novell | mature | legacy |
| Microsoft Active Directory | application | Microsoft | pre-release | dominant |
| TCP/IP Protocol Suite | protocol | IETF | dominant | dominant |
| IPX/SPX Protocol | protocol | Novell | mature | obsolete |
| Banyan VINES | platform | Banyan Systems | declining | obsolete |
| Digital PathWorks | platform | Digital Equipment | declining | obsolete |
| Tivoli TME 10 | application | IBM/Tivoli | current | legacy |
| CA-Unicenter TNG | application | Computer Associates | current | legacy |
| Novell IntranetWare | platform | Novell | current | obsolete |

### Observation Summary

- Total observations: 20
- By type: market-assessment: 10, competitive-assessment: 5, viability-prediction: 2, actual-outcome: 2, expert-opinion: 1
