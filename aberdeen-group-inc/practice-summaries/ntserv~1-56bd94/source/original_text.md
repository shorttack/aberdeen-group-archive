# Windows NT Server: 1998 Practice Summary

> Archived from: NTSERV~1.DOC
> Original publication date: 1998-05-01
> Author: Aberdeen Group

---

## Original Document Text

AberdeenGro
up
Windows 
NT Server:
1998 
Practice 
Summary
May 1998
Aberdeen Group, Inc.
One Boston Place
Boston, Massachusetts 02108 
USA
Windows NT Server Practice Summary
AberdeenGroup 
Telephone: 617 723 7890
Fax: 617 723 7897
www.aberdeen.com
2
Windows NT Server Practice Summary
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
Windows NT Server Practice Summary
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
Windows NT Server Practice Summary
AberdeenGroup 
TABLE OF CONTENTS
NT SERVERS PRACTICE 
V
Description, Focus and Benefits
v
Strategic Market Questions
v
EXECUTIVE SUMMARY
1
Defining Windows NT Servers
1
The Bigger Picture — Growth of NT/Intel Servers
1
Key Findings
2
The Focus of the Report
3
SUMMARY OF FINDINGS
4
Key Aberdeen Findings
4
Technology Findings
4
Market Dynamics
5
WINDOWS NT SERVERS DEFINED
7
How Windows NT Servers Fit Into System Platforms &  Architectures
7
Market Dynamics
8
Core Windows NT Server Components
10
Hardware — Processors, I/O and SMP Architectures
10
The Packaging — Making NT Servers Stand Out Among A Crowd
11
Professional Services — The Key Differentiator For NT/Intel Servers
12
SMP Architectures — Scaling System Power To Target The Enterprise
12
Systems Management
14
ISSUES AND CHALLENGES FACING THE WINDOWS NT/INTEL 
SERVER MARKET
16
Impact of Major IT Trends
16
5
Windows NT Server Practice Summary
AberdeenGroup 
The Internet
16
The transition to client-server and network-centric applications
17
Year 2000
17
NT and Unix Interoperability
17
Will Intel be the only choice for server architectures?
18
Single Application Limits for Windows NT platforms
19
Use of NT/Intel servers in mission-critical production environments
19
NT Supplier Success — Price, Performance, Packaging Professional Services and 
Punch
19
User Success Factors — Understanding the Realities of Windows NT
20
SUPPLIER PROFILES
21
Intel Corp.
21
Microsoft Corp.
22
Compaq Computer Corp.
23
Hewlett-Packard Co.
24
IBM Corp.
25
Dell Computer Corp.
25
Digital Equipment Corp.
26
6
Windows NT Server Practice Summary
AberdeenGroup 
Preface
NT Servers Practice 
Description, Focus and Benefits
Aberdeen’s NT Servers practice follows the market trends and 
technology developments in the Intel-based and Microsoft 
Windows NT-driven server market — including advances in Intel 
microprocessor development, NT clustering software, systems 
management as it pertains to the server, and the Windows NT 
Server operating environment.    Aberdeen emphasizes assessment 
of the market positioning of key suppliers and tactical challenges 
faced by Information Systems (IS) executives as these executives 
look to deploy and maintain NT-based server environments in their 
enterprises.
NT servers are rapidly becoming a strategic IS solution and a 
market comparable in size to Unix servers.    As IS undertakes NT 
implementation, servers originally aimed at workgroups have to 
take on additional responsibilities as application, Internet and even 
database servers.    Thus, NT servers are rapidly acquiring the key 
hardware technologies such as SMP, and software technologies 
such as clustering, to achieve robust scalability.    New systems and 
performance management tools that deliver greater reliability and 
control are arriving.    Individual server suppliers are turning to 
new areas to make their products stand out to IS buyers — 
packaging, service and support and systems management.    
Moreover, Intel’s rapid product turnover rate is constantly driving 
the high end of NT’s software scalability upward into the 
enterprise-class.    Nevertheless, down in the trenches, IS continues 
to report difficulties in handling NT software outages and scaling 
NT to the enterprise.    In this environment, picking the right tool is 
vital to IS success.
Because of their wide acceptance, NT Servers are a key part of any 
enterprise’s System Platforms & Architectures infrastructure.
Strategic Market Questions
1. What are the strategic directions of Intel microprocessor- 
and system-level designs — including roadmaps and 
7
Windows NT Server Practice Summary
AberdeenGroup 
implementation of new microprocessor features and 
performance? 
2. What are the leading suppliers of NT servers and what 
makes their systems different from the rest of the market? 
3. How will the introduction of new Intel microprocessor 
architectures — stretching up to 8-way-and-beyond SMP 
servers affect IS infrastructures? 
4. What new technologies will alter the placement and 
capabilities of NT Servers in enterprise sites, including 
I2O, clustering and SMP architectures? 
5. How will Microsoft’s enhancements in its Windows NT 5.0 
operating environment affect supplier directions, 
technology advancements and IS executives? What is the 
NT 5.0 roadmap? 
6. When will NT Servers be enterprise ready? What will get 
them to that point? 
7.
This Aberdeen Group Practice Summary is a deliverable in a 
comprehensive service that includes Aberdeen published research 
and customized professional services aimed at executives who 
must make strategic business decisions regarding Information 
Technology.
8
Windows NT Server Practice Summary
AberdeenGroup 
Chapter One
Executive Summary
Windows NT servers are now a key component of the strategic 
plans of most Information Systems (IS) executives.    However, in 
many cases a particular NT server may not adequately meet IS 
departments’ strategic needs.    To understand what NT servers can 
— and cannot — do, IS buyers need to dig beneath the vendor 
hype.
Defining Windows NT Servers
The Windows NT server market encompasses the Intel hardware 
systems, Digital’s Alpha-based platform, and Microsoft Windows 
NT Server operating environment — and this market centers on the 
NT Server environment running on Intel hardware. 
This market is predominantly based on commodity building blocks 
found in each system— the Intel Architecture or Digital 
Equipment’s Alpha systems and the Windows NT Server operating 
system.    How each system supplier differentiates itself comes 
down to features that are built on top of these systems or packaged 
with the server.    These include:
1. Professional services and support;
2. SMP architectures; 
3. Clustering technologies and implementations; and,
4. Systems management tools.
The NT/Intel market can also be divided along hardware lines — 
focusing on the hardware features and specifically on the number 
of Intel microprocessors used in the system.    There are three 
hardware classes: 
8. Entry-level (using up to two processors);
9. Midrange (using either dual or quad processors); and,
10.Enterprise-level (using more than four processors).
The Bigger Picture — Growth of NT/Intel Servers
NT/Intel-based servers are rapidly becoming a strategic IS 
alternative to Unix servers, with a market comparable in size to 
Unix servers.    The year 1998 is a strategic inflection point for the 
1
Windows NT Server Practice Summary
AberdeenGroup 
NT/Intel server market.    Intel is in the midst of rolling out new 
microprocessors which provide more power than ever before, 
reaching frequency speeds of up to 450 MHz.    Other technologies 
coming to fruition on the Intel Architecture include new systems 
management capabilities and enhanced, balanced system 
performance through new I/O technologies.    Microsoft’s much 
anticipated Windows NT Server 5.0 will be released by sometime in 
1999, offering new directory services, manageability, and 
scalability.
Aberdeen has found through numerous customer interviews that 
Windows NT servers are part of strategic plans for more than 90 
percent of Information Systems (IS) executives in Fortune 1000 
companies.    By the end of the century, NT will be a factor in most 
IS and Line of Business (LOB) departments’ acquisition plans.    For 
this reason, NT servers are growing at an explosive rate.    
Aberdeen suggests that the NT server hardware market, estimated 
to be about $6 billion in 1997, will grow by 50 percent each year in 
the coming four years, year over year.    At another level, Aberdeen 
estimates NT application revenues to be roughly $2 billion in 1997, 
an amount that will grow to roughly $13 billion by 2001.
Because of a combination of factors, including IS departments’ 
focus on Year 2000 problems and mismanagement of inventories 
by both IBM and Compaq, the total market will experience a 
slowdown to 50 percent growth during 1998 and onward into 1999. 
Hardware component prices are dropping at a daily rate, forcing 
server suppliers to be price sensitive and reducing the revenues 
each can earn from the hardware.    Pricing will be an increased 
factor for a number of IS decision-makers, because of the increased 
competition between suppliers.
Key Findings
1. Windows NT Server as an operating environment still 
needs a number of improvements in the areas of 
interoperability, manageability, scalability, overall 
robustness, and Year 2000 readiness;
2. Intel Architecture servers are taking on a number of 
dimensions over time, targeting specific market segments 
(low-price, midrange and enterprise), and featuring new 
technologies such as Intelligent I/O, the Virtual Interface 
Architecture, and systems management capabilities; 
3. Between now and the release of Intel’s IA-64 architecture, 
Digital Equipment Corp.’s Alpha microprocessor will 
2
Windows NT Server Practice Summary
AberdeenGroup 
continue to provide a higher-performance alternative to 
Intel using NT Server;
4. NT/Intel server suppliers are boosting the capabilities of 
servers to support evolving trends in the industry — 
consolidation of application servers, the emergence of NT 
databases, and new server-centric network configurations 
supporting network and thin-client computing; and,
5. While NT/Intel servers continue to be focused primarily 
as workgroup and departmental servers, during 1998 and 
onward into 2000 these servers will quickly migrate 
upwards into larger Internet, application and eventually 
database servers.
The Focus of the Report
This report is meant to assist IS decision-makers as they seek to 
understand the Windows NT server market, including hardware, 
operating system, and supporting components of these products. 
3
Windows NT Server Practice Summary
AberdeenGroup 
Chapter Two
Summary of Findings
The NT/Intel market is at a turning point as new technologies 
arrive, ranging from new Intel hardware to Microsoft’s coming 
enhancements in Windows NT 5.0.    A key turning point for the 
NT/Intel server market will occur during 2000 — culminating with 
the volume release of the predicted powerful Merced 
microprocessor, the first of a family of microprocessors to utilize 64 
bits (the IA-64 architecture family).
Aberdeen expects the conversion to IA-64 will likely take up to five 
years or more, allowing greater segmentation of the Intel server 
market between enterprise servers and cost-effective servers that 
will continue to plummet in price/performance as measured by 
price per transaction to less than $15 from today’s values of about 
$27 for a four-way Pentium Pro server.    A number of technology 
initiatives spearheaded by Intel will also increase system 
performance, add industry-standard clustering interfaces, and 
provide system management capabilities.
Further advances from ISVs and Microsoft are likely to increase 
server capabilities yet more — especially Microsoft’s work to add 
scalability to the NT Server operating system through its 
introduction of Active Directory and more advanced greater-than-
two-server clusters.    Both efforts are expected to be introduced to 
products sometime before the year 2000.    Microsoft has a 
significant number of issues to address in future versions of NT 
Server to make them viable alternatives to all levels of Unix 
operating environments, including interoperability, scalability, 
number of end users supported, stability, storage management, and 
security.
Key Aberdeen Findings
Technology Findings
Today’s Windows NT 4.0 operating environment has significant 
limitations, including:
1. Interoperability — not only with servers using Unix but 
many times within the various versions of NT Server;
4
Windows NT Server Practice Summary
AberdeenGroup 
2. Stability — that is, the number of users supported by one 
copy of the operating system and the availability of that 
server;
3. Systems Management — the NT-based tools used to 
manage the server are still in their infancies;
4. Storage Management; and,
5. Security.
Although IS managers expect that many of these issues will be 
addressed in Windows NT 5.0, a number of features currently 
planned for this release of the operating system may not actually 
be in the final product. 
Market Dynamics
11.NT/Intel servers are deployed by a combination of the 
following — depending on the complexity of the servers:
1. By IS administrators who are experienced with NT 
servers and understand the limitations — especially as 
file/print, workgroup, and departmental servers;
2. By server-supplier professional service organizations 
that specialize in NT professional services and 
deployment; and,
3. By independent systems integrators and resellers that 
have a background in NT deployment and can handle 
more complex implementations.
12.Professional services are increasingly used by IS 
executives to plan, architect and deploy NT/Intel server 
architectures into infrastructures.
13.The NT/Intel server market is growing at a rate of 50 
percent year over year, with the NT operating system and 
support applications market growing at closer to 100 
percent annually.    In 1997, there was roughly $2 billion 
on OS revenue for NT servers and about $6.3 billion for 
hardware and operating system components collectively. 
Because a combination of factors, including IS 
departments’ focus on Year 2000 problems and 
mismanagement of inventories by both IBM and Compaq, 
the total market will experience a slowdown during 1998 
and into 1999.
14.The number of large NT/Intel server suppliers is 
decreasing as a number of mergers occur — and as 
5
Windows NT Server Practice Summary
AberdeenGroup 
second-tier server suppliers attempt to carve out a 
customer base with limited market exposure.
15.Although top Line of Business executives have been 
crucial to pushing the enterprise’s strategic directions 
towards NT/Intel servers because of their lower 
acquisition and operational costs, increasingly IS 
administrators are taking an active interest in 
standardizing their infrastructures on NT.
16.Major buying criteria in the NT/Intel server market are 
cost, performance, lifecycle support, investment 
protection, manageability, and reliability.    In addition, 
there is a strong correlation between desktop market 
share and server market share; it is hard to grow a robust 
customer relationship in servers when a supplier lacks 
desktop credibility.    Buyers want to limit the number of 
supplier relationships.
6
Windows NT Server Practice Summary
AberdeenGroup 
Chapter Three
Windows NT Servers Defined
How Windows NT Servers Fit Into System Platforms & 
Architectures
Windows NT and Intel-based servers are one of the most 
prominent hardware architectures now present in the Information 
Technology (IT) industry. 
To a great extent, many of the NT/Intel-based server suppliers have 
their roots in desktop architectures.    Industry leaders Intel, 
Microsoft and Compaq all began as desktop suppliers, and have 
continued to lead the push of technology into more powerful, 
scalable, and manageable servers that make up much of the mid-
range of IT hardware architectures. 
Figure 1: How NT Servers Fit Into Platforms and Architectures
Source:    AberdeenGroup, April 1998
The Windows NT server environment is one of the hardware 
platforms on which enterprise sites are currently building their IT 
7
Windows NT Server Practice Summary
AberdeenGroup 
infrastructures, and it has a wide acceptance in workgroup 
settings.    But the Windows NT server market remains less robust, 
scalable and enterprise-ready than the more mature Unix 
platforms available — and NT has not gained the critical support it 
needs from IS executives to be considered ready for the enterprise. 
Because of this, NT still remains a second choice for larger 
enterprise sites that support mission-critical applications.
That will change over the next 2 years, as Microsoft and Intel 
introduce new, more robust products that are scalable and more 
highly available.    Furthermore, NT/Intel servers are beginning to 
take on additional responsibilities as application, Internet and even 
database servers. 
Figure 2: NT/Intel Servers’ Role in Hardware Platforms
Source:    AberdeenGroup, April 1998
Market Dynamics
Technology built upon Intel Architecture (IA)-based servers and the 
drive of the Windows NT operating environment to offer more 
capabilities are the key market forces that are pushing the NT/Intel 
server market forward.    All of this appears to have a simple but 
ambitious goal:    NT server deployment beyond its traditional 
8
Windows NT Server Practice Summary
AberdeenGroup 
bastion of file and print servers and workgroup settings to the 
more reliable mission-critical production environments.
To get there, the leaders of the NT/Intel server market (Microsoft, 
Compaq, and Intel, among others) along with alliance partners are 
scaling the hardware environment by offering servers that utilize 
more than four processors.    They also are working with 
Independent Software Vendors on a number of technology 
initiatives meant to increase the capabilities of the Windows NT 
Server operating environment and boost performance of 
applications that run in the environment.    There are therefore 
four major trends in the Windows NT/Intel server market in early 
1998:

Boosting the capabilities of the Intel Architecture servers 
through a number of technology initiatives conducted by 
Intel and server OEMs — from offering more advanced 
systems-management-type hardware monitoring to boosting 
I/O subsystem bandwidth to offering larger Symmetrical 
Multiprocessing (SMP) architectures;

Consolidation of servers and of the suppliers themselves — 
e.g., the use of larger, more powerful SMP servers, and the 
Compaq acquisition of Digital;

Advancing the reliability of the Windows NT operating 
environment and fine-tuning applications to provide 
improved performance on the platform; and

Speeding the scalability, availability and eventually 
performance of these servers through the use of clustering — 
still very much a work in progress in the NT environment.
9
Windows NT Server Practice Summary
AberdeenGroup 
Key suppliers include the big four:    Compaq, Hewlett-Packard, IBM 
and Dell.    There are a number of smaller suppliers — sometimes 
referred to as “second tier” suppliers — including Digital 
Equipment (soon to be part of Compaq), NCR Corp., NEC Corp., 
Netframe (a division of Micron), Axil Computer Inc., Data General, 
Gateway, and Unisys.    These suppliers often are niche suppliers — 
meaning that they offer products that are to a great extent targeted 
at specific vertical or application markets — unlike the big four 
suppliers that provide varying levels of IA-based servers.
The growing demand for NT/Intel servers is amplified by Intel’s 
development of the IA-64 platform with Hewlett-Packard, 
scheduled to be available in late 1999.    This will offer IS executives 
a new standard hardware platform on which to operate 64-bit 
applications in either Unix or NT operating environments.    With 
this merging of microprocessor architecture behind Intel, as well 
as the escalating demand for Windows NT, more Independent 
Software Vendors (ISVs) are choosing the NT/Intel platform as their 
primary development platform.    And as the number of NT/Intel 
servers deployed in IS departments increases, so does the 
availability of effective storage and database management tools. 
Windows NT as an operating environment is also showing rapid 
growth — faster than the underlying hardware because of the 
release of new versions of Microsoft’s operating system.    Aberdeen 
projects that NT Server operating system shipments will increase 
Figure 2:    Worldwide UNIX and NT Application Server Revenue
1996
1997
1998
1999
2000
0
5
10
15
20
25
30
35
40
1996
1997
1998
1999
2000
NT
UNIX
$ Billions
Source:    Aberdeen Group, August 1997
10
Windows NT Server Practice Summary
AberdeenGroup 
88% in 1998, and over 100 % in 1999.    It needs to be stressed that 
overall market growth that includes hardware will be 50 percent 
annually — as IS departments spend less money on hardware in 
order to allocate revenues to Year 2000 problems.    So, while 
customers may upgrade operating systems, they may hang onto 
servers for longer periods of time.
Aberdeen predicts that NT Server operating system and application 
revenues will still remain much smaller than Unix revenues for 
sometime to come.    Thus, the global market for UNIX application 
servers is projected to grow from $19.6 billion in 1996 to $40 billion 
in 2000 — and still be 4.5 times larger than the NT application 
server market.    But note that in 1996, all suppliers of NT 
application servers only shipped $750 million in hardware.    
Aberdeen believes that the projected growth to $9 billion in 2000 
will be phenomenal and tax the resources of the professional IS 
community to implement NT application servers. 
Core Windows NT Server Components
Hardware — Processors, I/O and SMP Architectures
NT/Intel-based servers are classified at the hardware level by the 
number of processors that can be included in the Central Electronic 
Complex (CEC) — i.e., the server “horsepower”.    This simple view 
is complicated by the advent of today’s new generations of 
microprocessors as well as the Merced generation due to arrive in 
1999.    So IS buyers must also consider the availability of new 
processors — including the Pentium II Xeon for up to four-way and 
beyond SMP architectures and the Pentium II processor for dual-
processor architectures.    Using the hardware as way to segment 
the market, there are three levels of servers:
17. Entry-level
 
  :    utilizing two processors (Pentium II) and 
four to five I/O slots;
18. Midrange:
 
  containing dual or quad processors (Pentium 
Pro, and by mid-1998 Pentium II Xeon) and seven to 10 I/O 
slots; and
19. Enterprise-level
 
 :    using four to eight 32-bit Pentium Pro 
(until the arrival of Pentium II Xeon in the second half of 
1998), or 64-bit Merced processors (64-bit architecture 
arriving in late 1999), and four server I/O slots.
11
Windows NT Server Practice Summary
AberdeenGroup 
Source: AberdeenGroup, May 1998
Furthermore, each supplier differentiates itself by how it uses Intel 
architectures.    For example, the past year has seen the emergence 
of greater-than-four-way architectures that utilize SMP 
implementations to boost processor power for IS executives 
needing additional system “headroom” to tackle demanding Online 
Transaction Processing (OLTP) or decision-support applications.
The Packaging — Making NT Servers Stand Out Among A Crowd
Because all NT/Intel server suppliers use the same underlying 
microprocessors with a few augmentations, suppliers use 
packaging to differentiate themselves more clearly.    This 
packaging includes:

Professional Services — like systems integration, NT 
systems/application project management, and lifecycle 
management;

SMP architectures — including technologies such as I2O and 
greater than four-way architectures (now mostly proprietary 
but more industry standard by late 1998 with the 
introduction of an Intel-backed 8-way architecture);

Clustering — such as the use of Microsoft Cluster Server (a 
Microsoft-based cluster software that provides simple 
failover) and value-added capabilities such as a service pack 
12
Windows NT Server Practice Summary
AberdeenGroup 
that provides additional clustering capabilities plus storage 
packages supporting storage subsystems and use of multi-
node interconnect technologies; and,

Systems Management — including software suites available 
on suppliers’ platforms that are distinctive and can be used 
as point products or as part of a larger enterprise 
management framework.
Professional Services — The Key Differentiator For NT/Intel 
Servers
In general, NT service offerings include the following:
1. NT Systems Design/Integration Services — consisting of an 
initial assessment, followed by architecture design, systems 
and network design, and related systems/applications 
deployment services;
2. NT Systems/Applications Project Management — these 
services include scheduling, tracking, and trouble-shooting 
activities related to the implementation and deployment of 
NT systems and applications;
3. NT Lifecycle Management — services designed to 
accommodate the ongoing maintenance and management of 
an installed NT environment; and
4. Training — services related to the use and understanding of 
NT-based systems applications and their administration.
SMP Architectures — Scaling System Power To Target The 
Enterprise
Intel suppliers have taken two approaches to scaling system 
performance on the hardware.    Some suppliers have chosen to 
offer customers proprietary greater-than-four-way servers 
supporting the existing Intel Pentium Pro microprocessor.    Others 
have taken a more conservative approach, waiting to offer more 
than four-way servers until Intel does it through its own 
forthcoming chipset for use with the Pentium II Xeon.    And, 
although greater-than-four-way architectures offer additional 
processing power, few NT applications have yet been written to 
take advantage of multi-threading and the additional processors in 
the SMP architecture.
From an IS executive’s perspective, escalating enterprise 
infrastructures are requiring either more processing power or 
more disparate servers to handle additional tasks.    So, these same 
13
Windows NT Server Practice Summary
AberdeenGroup 
IS executives must decide how to increase their NT/Intel servers’ 
“headroom” immediately.    Many also want to reduce the 
complexity of managing multiple small NT servers by consolidating 
these servers into one larger, more easily managed NT Server 
platform.    Acquiring larger NT/Intel SMP servers is an effective 
way to accomplish this consolidation.
Figure 4: Intel Server Units by CPUs per Server
Clustering — Following the Microsoft Standard and Adding 
Capabilities
Microsoft Cluster Server (MSCS, a.k.a. Wolfpack), introduced in fall 
1997, marks the start of a standardization of clustering on NT.    
Microsoft Cluster Server is a commodity-based product intended to 
bring basic failover clustering between two servers to IS managers 
who do not require more advanced clustering functionality.    It is 
important to mention that there are presently two kinds of 
clustering — high availability (keeping server downtime to a very 
small percentage) and performance clusters (providing load 
balancing to boost overall production performance).    MSCS is only 
providing some increased availability — not complete high-
availability — to clustered servers, and does not yet provide 
automatic load balancing.
14
Windows NT Server Practice Summary
AberdeenGroup 
Microsoft Cluster Server remains very much a “work in progress.” 
Microsoft and partners like NCR, Digital, Compaq (Tandem), IBM 
and HP are already providing new features and capabilities that go 
well with MCSC today.    A number of these suppliers are working to 
offer a standardized clustering interconnect technology called the 
Virtual Interconnect (VI) Architecture.    Spearheaded by Intel, VI 
allows a common API for I/O drivers and intelligent network 
interface cards (NICs).
Most server suppliers have turned to Microsoft to provide 
clustering for their hardware.    Additionally, some of the early 
adopters of Microsoft’s clustering initiative have chosen to pursue 
a dual strategy:    support and work closely with Microsoft to fine-
tune industry-standard commodity clustering.    At the same time, 
suppliers are continuing to offer IS buyers a choice of Microsoft 
Cluster Server or their own more robust clustering software by:
1. Providing service packs or systems management tools that 
run on top of MSCS;
2. Offering packages that use different configurations of storage 
subsystems, i.e. shared SCSI, RAID, and Fibre Channel; and,
3. Giving IS executives the option of seeking additional 
capabilities from a number of software clustering products 
instead of utilizing the Microsoft-based product.
For the highest levels of availability, Marathon’s Endurance is the 
leader in providing fault-tolerant NT systems, with Stratus’ Radio 
Clusters also providing fault tolerance.
Systems Management
A relatively new trend in the NT/Intel server market is the arrival 
of more sophisticated systems management tools for servers.    
Currently, Intel and Microsoft as well as major system suppliers are 
trying to standardize how system management occurs on these 
servers with limited success.    There are several major initiatives 
underway, including the Desktop Management Interface (allowing 
monitoring of Windows desktops from an NT Server or in an 
enterprise systems management framework), Web-based 
enterprise management (WBEM), and the Intelligent Platform 
Management Interface (IPMI). 
Because systems management is not yet standardized, NT/Intel 
server suppliers are able to offer IS executives a mix of 
management tools as a way of making themselves stand out — 
especially at the enterprise level.    Entry-level and midrange 
15
Windows NT Server Practice Summary
AberdeenGroup 
servers are less likely to be packaged with systems management 
tools, because they are not yet viewed as the backbones of Local 
Area Networks (LANs) or as supporting mission-critical production 
environments.    Products offered in this area are usually divided 
into the following categories:

Enterprise Systems Management:    including the 
development of frameworks like CA Unicenter TNG and 
Tivoli TME-10 that manage across mainframes, Unix and NT 
networks and provide both hardware and software 
monitoring tools and agents;

Domain Management tools:    managing from the server 
down to the desktop — including LAN management tools 
such as HP OpenView, Compaq Insight Manager and IBM 
NetFinity; and

Point products:    specific administrative tools for specific 
hardware components such as network interface cards, 
desktops, and the server components themselves.
16
Windows NT Server Practice Summary
AberdeenGroup 
 Chapter Four
Issues and Challenges Facing the Windows 
NT/Intel Server Market
Impact of Major IT Trends
As has been stated a number of times, NT/Intel servers are taking 
on new roles in enterprise sites as more IS executives deploy and 
migrate applications to the NT environment.    And with this new 
strategic direction come a number of issues that IS executives must 
examine — as well as issues that affect the entire industry.    This 
chapter examines technology-specific and industry-wide trends, as 
well as factors that contribute to the success of suppliers offering 
NT/Intel servers and users of these systems. 
Major IT Trends
A number of overall industry trends are affecting the NT/Intel 
server market, and a number of industry-specific challenges, 
including:
20.The Internet;
21.The transition to client-server and network-centric 
applications;
22.Year 2000;
23.NT and Unix interoperability;
24.Will Intel be the only choice for server hardware;
25.Single application limit for NT servers;
26.Use of NT/Intel servers in mission-critical production 
environments; and
27.Deployment of “NetPC” and thin client-based 
infrastructures in place of classic desktop clients.
The Internet
For many of the suppliers in the NT/Intel market — and 
particularly IBM, HP, and Compaq — the Internet signifies an 
emerging market that allows suppliers to target customers, such as 
Internet Service Providers (ISPs).    These hardware suppliers, along 
with a number of smaller vendors, are either developing their own 
software suites (e.g., IBM’s Domino Suite) or creating specific 
17
Windows NT Server Practice Summary
AberdeenGroup 
packages of third-party software suites on top of the hardware to 
deliver solutions specifically for use as Internet servers.    Even 
Microsoft has gotten involved, offering such software as Internet 
Information Server, Site Server, and Communications Server.    
Networking devices are also being packaged with servers to 
increase these suppliers’ leverage against competitors, and the 
Intel server hardware systems themselves are increasingly being 
packaged in “rack-mount” systems to allow the stacking of multiple 
systems. 
The transition to client-server and network-centric 
applications
As the importance of client-server environments increases — with 
the emergence a standard that split the environment into three 
tiers (enterprise, middle and client tiers) — in which NT servers 
are now seen as the front end to a lot of production environments. 
Because of the recent focus on client-server architectures, NT 
servers often carry out network-centric applications and monitor 
the network itself.    These same servers are also being used as the 
front-end servers to more complex databases — handling the 
administrative tasks of queries.    In addition, the emergence of the 
sub-$1,000 PC, the NetPC, and Network Computers is also 
increasing the move to client-server environments and placing 
more responsibility on the shoulders of NT servers.
Year 2000
The perception concerning the Year 2000 problem and NT/Intel 
servers has been that these servers will be a safe harbor — in other 
words, that they are in compliance with Year 2000 guidelines.    The 
truth is that they are not — and IS executives need to double check 
to make sure their NT infrastructures have been made safe by 
carrying out a number of software updates at the application, 
operating system, and hardware levels. 
Each supplier is tackling the problem in different ways, with no 
standard means for IS executives to determine whether or not 
their hardware is safe for the rollover to the Year 2000.    Intel has 
issued a statement on Year 2000, pointedly saying that as long as 
the operating system and applications supported on its 
architectures are compliant, the architecture itself is also Year 2000 
safe.    It is important to note that systems that use the older 386 
and 486 microprocessors will need to be manually rolled over, due 
to legacy BIOS — firmware that handles the computer systems’ 
18
Windows NT Server Practice Summary
AberdeenGroup 
low-level input and output functions and provides interfaces with 
the operating system and server hardware.
Desktop applications, many of which also run on NT Server, are not 
immune from the infamous Year 2000 issue.    Key Microsoft 
products such as Windows 95 and versions of Windows 3.1 have 
bugs that will improperly write file dates for files created after the 
turn of the century.    Furthermore, problems with spreadsheet 
programs include a number of Microsoft and other popular NT 
products, such as Excel, Access, and Lotus 1-2-3. 
NT and Unix Interoperability
With the increasing presence of NT/Intel servers, the need to 
interoperate with Unix servers is also escalating.    More and more 
enterprise sites are turning towards multi-tiered client-server 
networks with Unix and mainframe systems at the high end and 
NT servers in the mid-range and lower end, supporting direct 
Windows clients.    A vast majority of new NT server deployments 
are occurring when IS executives are expanding LANs and 
developing new production environments.    New deployments 
moving existing applications from Unix to NT are relatively rare.    
Thus, the need for interoperability between Unix and NT will likely 
continue well into the next decade.
Microsoft is planning to offer over the next year a Windows NT 
Services for Unix Add-On Pack that includes a number of 
interoperability features for NT Server and Unix operating 
environments.    This includes    resource sharing, remote 
administration, password synchronization, and common scripting 
across platforms.
Microsoft’s solution in the short term is to support third-party 
vendors that provide interoperability software, including Data 
Focus’ NuTCRACKER.    In the longer term, Microsoft has also 
developed program interfaces for software developers, called 
Distributed Component Object Model (DCOM).    This allows the 
integration of platform-neutral development frameworks and Java 
Virtual Machine environments.    DCOM also delivers some cross-
platform abstraction for object oriented distributed computing that 
includes connection to and creation of components, locating 
components, invoking methods on components, and a security 
framework.
Will Intel be the only choice for server architectures?
19
Windows NT Server Practice Summary
AberdeenGroup 
Intel now holds a significant portion of the hardware used in this 
evolving market, with Digital Equipment Corp.’s more powerful 
Alpha microprocessor holding a much smaller percentage (roughly 
2 percent) of the market that utilizes the Windows NT operating 
environment.    Aberdeen suggests that the Alpha architecture will 
continue to be a force for the next three years and into the next 
decade — reaching microprocessor speeds of 660MHz by the 
second half of this year and upwards of 1GHz by 2000.    Going 
forward, IS executives will need to determine the pros and cons of 
acquiring Alpha versus Intel systems.
Digital’s AlphaServer platform generally provides better 
performance than Intel-based systems, especially when running 
transaction-based applications on clustered systems running 64-bit 
Digital Unix.    As for the NT operating environment on Alpha, there 
are a limited choice of native NT applications.    That issue has been 
addressed by Digital in the last year through the FX32 technology, a 
dynamic translator and binary recompiler slated to be included in 
NT 5.0.
Other companies could “dabble” in the NT server market in the 
coming years, especially by providing processors for entry-level 
servers    These companies include Cyrix and AMD. 
Single Application Limits for Windows NT platforms
Windows NT environments have a number of limitations — 
discussed earlier — that limit NT server deployments in larger 
enterprise infrastructures.    A key hurdle, not shared by the Unix 
world, is the current support for essentially one application per 
copy of the operating system.    This limit has kept NT servers 
deployed on the periphery of larger database environments.    So, 
for example, in a typical three-tier environment, enterprise servers 
where the primary database resides are Unix systems.    Middle tier 
servers responsible for handling individual queries might be NT 
servers, and “fan servers” (handling client query requests) will also 
be NT servers.    Aberdeen suggests that future versions of NT will 
provide support for running multiple applications simultaneously.
Use of NT/Intel servers in mission-critical production 
environments
The number of end users supported on each server still remains 
less than in comparable Unix-based operating environments.    
Furthermore, the Windows NT operating environment is not as 
manageable as Unix because of a dearth of significant OS 
management tools, as well as a lack of awareness on the part of IT 
20
Windows NT Server Practice Summary
AberdeenGroup 
departments of existing management tools available to assist in the 
performance tuning of these servers. 
NT 5.0 as well as a number of evolving systems management 
standards targeting the NT platform (DMI, WBEM, and IPMI) offer 
hope of solving robustness and scalability issues.    However, 
Aberdeen advises IS executives to hold off on deployment of new 
production systems using NT 5.0 until it is determined that NT 5.0 
is stable.    Bugs plagued the first versions of previous NT releases.
NT Supplier Success — Price, Performance, Packaging Professional 
Services and Punch
Each supplier in the NT/Intel server market essentially starts at the 
same starting point — using Intel Architecture-based server 
systems and the Microsoft Windows NT operating system.    From 
there, each supplier aims to achieve market success by focusing on 
one or several of a number of factors, including:
28.Price — offering IS executives a competitive server that is 
the most inexpensive when compared to other suppliers 
by keeping margins low and using both direct model and 
build-to-order product strategies;
29.Performance — using the Intel Architecture-based server 
to its fullest through a combination of additional 
technology innovation, such as additional RAM and 
storage capacity, larger SMP architectures, and clustering 
middleware;
30.Packaging — offering IS executives additional “perks” for 
going with a specific server line — e.g., lifecycle financing, 
high availability packages such as Data General’s “Cluster-
in-a-Box,” and investment protection through processor 
upgrade programs (like the one offered by Compaq);
31.Professional Services — targeting the high end of the NT-
in-the-Enterprise market (and increasingly the midrange 
market) where a considerable amount of expertise is 
required to integrate NT-based application and database 
environments with other non-NT-based application and 
database environments; and
32.Punch — that is, using any of the above factors to their 
advantage as a supplier to create a specific market edge in 
a particular area (e.g. Dell’s sales model and just-in-time 
manufacturing that allows it to profit from low margins 
through volume).
21
Windows NT Server Practice Summary
AberdeenGroup 
User Success Factors — Understanding the Realities of Windows NT
User success factors include working with experienced system 
integrators, and strategic consensus-building between IS 
administrators and the business executives in the enterprise.    
When deploying NT/Intel servers, IS buyers should consider:
1. The migration of Windows NT Server 4.0 to Windows NT 
5.0 — especially changing the ways domains can be 
configured;
2. The ways to achieve scalability — through either larger 
SMP architecture-based servers or by clusters — and the 
relative advantages and disadvantages of each;
3. The coming transition to Intel’s IA-64 architecture — 
when to take the plunge — and how to implement the 
hardware platform, the operating environment and the 
applications that will take advantage of the new, larger 
memory address space and parallelism in applications; 
and,
4. The balance between price and performance in acquiring 
Intel/NT servers — looking for lowest cost of acquisition 
while focusing on the best hardware features of the 
hardware to meet IS strategic needs, i.e., the processor 
power, the available storage capacity, redundancy and 
management features.
22
Windows NT Server Practice Summary
AberdeenGroup 
Chapter Five
Supplier Profiles
Intel Corp.
Enterprise Server Group
15400 N.W. Greenbrier Pkwy.
Beaverton, OR 97006-5783
www.intel.com
Market Position
Intel is the gorilla in the NT Server space — and the key supplier 
for server hardware.    Intel’s microprocessors are the main 
ingredient of more than 95 percent of today’s NT servers.    Intel 
gives the image of a non-competitor, providing its microprocessors 
to all of the main suppliers in the NT Server market without 
prejudice. 
Going forward over the next several years, Intel will have two 
main product lines:    IA-32 and IA-64.    IA-32 is made up of a 
number of current microprocessors — including the Pentium Pro, 
more recently the Pentium II, and the future Pentium II Xeon 
microprocessor.    IA-64 will offer IS executives new levels of 
performance for applications that can take advantage of 
parallelism — especially in database, Internet, and decision-
support applications.
Aberdeen Conclusions
Aberdeen views Intel as having a rosy forecast, based on its 
price/performance ratios that continue to offer IS executives 
increasing power for less price, and the volume of microprocessor 
products that Intel will offer the server market 1998.    Intel has 
demonstrated that it has the ability to drive industry standards 
through alliance partners — ideally giving IS executives better 
technology at a lower price.    Over time, Intel will need to execute 
and work with its partners to deliver technologies such as 
23
Windows NT Server Practice Summary
AberdeenGroup 
Intelligent I/O, Virtual Interface Architecture, and systems 
management standards like DMI, WBEM and IPMI.
Intel is facing both a time of opportunity and challenge through its 
pending introduction of its IA-64 family of microprocessors, slated 
to arrive by end of 1999.    It will be an opportunity for Intel in that 
with few exceptions (Sun Microsystems), NT and Unix suppliers 
will be providing IS executives with servers utilizing these more 
powerful and more advanced processors.    At the same time, Intel 
is facing increasing fragmentation of its OEM partners, as each 
server supplier strives to market themselves as the most optimized 
for the IA-64 architecture.
Microsoft Corp.
One Microsoft Way
Redmond, WA    98052-6399
www.microsoft.com
Market Position
Microsoft’s current success stems from its efforts to provide both a 
desktop operating environment and a network operating system 
(NOS) — driving its products to be industry standard as well as 
providing a large pool of supporting ISV applications.    Microsoft’s 
Windows NT Server operating system’s a clear leader in the PC LAN 
and workgroup. And, more and more frequently, Windows NT is 
being tapped as an operating environment for departmental 
settings — as one of the fastest growing operating environments, 
outnumbering new deployments of Unix at this level.
Microsoft continues to add new features to successive generations 
of Windows NT, and is marketing the operating system as a 
possible corporate desktop operating environment.    Additionally, 
IS executives are seeing more applications available on the 
Windows NT operating environment, making it an appealing 
strategic direction.    However, IS buyers continue to evaluate NT 
based on its robustness — especially in business critical 
environments — and a number still turn to Unix to provide 
enterprise-quality operating environments.
Aberdeen Conclusions
To succeed in fully leveraging the NT market, Microsoft needs to 
deliver technologies to boost its reliability and manageability.    
Additionally, Microsoft needs to enhance interoperability with 
24
Windows NT Server Practice Summary
AberdeenGroup 
other operating environments, and add scalability by better 
clustering support in Microsoft Cluster Server.    Microsoft will 
likely have a tremendous impact on market directions through the 
assimilation of new technologies.
25
Windows NT Server Practice Summary
AberdeenGroup 
Compaq Computer Corp.
20555 State Highway 249
Houston, TX 77269-2000
www.compaq.com
Compaq is the largest NT/Intel server supplier as well as the 
number one desktop maker, and also is changing the fastest in this 
industry as it aims to complete the second major acquisition in the 
last year — Tandem and Digital Equipment Corp.
Compaq has an enormously successful NT server business.    In fact, 
Compaq listened to customers early and often, focusing on IS-
quality NT servers, not just desktops on steroids    Compaq’s line of 
NT servers, called ProLiant, range from entry-level uni-processor to 
four-way and (later this year) eight-way Intel servers.    Over the 
last year, it has developed and enhanced a number of industry 
alliances to make it a technology leader in the NT/Intel server 
market, including its work with database suppliers SAP, Siebel, and 
Baan.    All of these alliances will make Compaq more attractive to 
IS executives looking for server suppliers capable of handling 
complex deployments of NT in the enterprise and datacenter 
environments.
Aberdeen Conclusions 
A key to future Compaq success is following through on its new 
sales model.    Compaq has attempted to redefine its indirect model 
of selling products —    and the process of streamlining its 
distribution model remains a work in progress. 
Aberdeen suggests that Compaq will continue to get great marks 
from customers as Compaq gradually assimilates Digital’s 
technology and product offerings into Compaq’s line of servers and 
supporting technologies.    Compaq will be able to leverage these 
new products and technologies as it competes against HP, IBM and 
Dell.    Compaq has already started to demonstrate its continued 
industry leadership through its recently published benchmarks of 
a six-node cluster that features Oracle Parallel Server and 
Tandem’s ServerNet interconnect. 
Compaq has earned the bragging rights for an industry “first” 
greater than two-way NT cluster with documented performance.    
For IS executives, the question remains on how long before this 
will be both viable and necessary for enterprise sites.    
Nonetheless, Compaq is off to an impressive launch into the 
26
Windows NT Server Practice Summary
AberdeenGroup 
enterprise environment, and will likely to continue to leverage its 
newly acquired technology from Digital and Tandem as well as 
alliances.
Hewlett-Packard Co.
3000 Hanover St.
Palo Alto, CA 94304
www.hp.com
Hewlett-Packard and IBM fall into the same category.    Both are 
large, powerful computer companies that support multiple lines of 
computers from the desktop to larger supercomputers — including 
growing NT/Intel server businesses that had the two neck-and-neck 
in NT revenues in 1997.    Today, HP appears to be in a stronger 
long-term position than IBM, due primarily to its work with Intel 
on the next big thing in enterprise computing — IA-64, based on 
their combined efforts to create Explicitly Parallel Instruction 
Computing, the underlying computing architecture. 
HP’s strength lies in its technical knowledge of systems 
management, Unix and enterprise datacenter environments.    But 
its NetServer line, made up of Intel-based servers, hasn’t 
traditionally provided industry-standard computing with much 
finesse.    That is changing. HP continues to focus its work on 
creating larger, more powerful and flexible systems — as well as 
larger SMP architectures that extends to 8-way and possibly 16-way 
Intel-based servers. 
While HP has demonstrated that it has an extensive professional 
services organization, it hasn’t yet shown that it has a clear focus 
on providing IS executives with the best, most advanced NT 
environment.    HP has a working relationship with Microsoft 
through its work with the Simplified Enterprise Computing (SEC) 
alliance and that alliance is expected to deliver new initiatives 
during 1998.
Aberdeen Conclusions
Unless HP interjects innovation into its NT/Intel server line, it could 
conceivably lose market share and it could also lose the attention 
of IS executives looking for technology-leading NT/Intel platforms 
that could ultimately be deployed across enterprises.    HP seems to 
realize this, and is introducing a number of new innovations to its 
servers, including better management tools, more competitive 
pricing, and more features.    HP has also boosted its customer 
27
Windows NT Server Practice Summary
AberdeenGroup 
service programs for both customers and resellers, and is spending 
significantly more time streamlining its supply chain assembly 
programs to offer IS buyers less expensive systems.
28
Windows NT Server Practice Summary
AberdeenGroup 
IBM Corp.
Route 100
Somers, NY 10589
www.ibm.com
IBM’s Netfnity line, the re-branded PC Server product family, is 
beginning to show gradual progress to being more competitive, 
leveraging packaging with many of IBM’s key software applications 
and professional services.    IBM’s current advantage in the 
marketplace is its ability to leverage its technology, especially 
through its Lotus division and Global Services, and offer packaged 
servers that can be sold both as free-standing and directly into the 
company’s extensive installed base.    Unlike any of the other 
suppliers in the top four, IBM appears to be less concerned about 
introducing leading-edge technology to its servers — and has not 
shown technology leadership.    This could significantly hurt IBM as 
it moves forward in competition against Compaq and HP.    IBM 
appears also to be in a downward spiral in the NT market, with 
early estimates suggesting that its Intel server line’s revenues are 
down for 1998 so far.
Potentially, IBM can offer NT servers that are advantageous to 
enterprises where NT is being deployed in production 
environments for which professional services are vital.    Aberdeen 
sees IBM covering the basics in the Microsoft-solutions 
professional-services market, while offering a richer professional 
services portfolio for users deploying IBM products on NT/Intel 
servers.
Aberdeen Conclusions
IBM will need to broaden its line of NT/Intel servers, add new 
technologies at a more rapid pace, and do more to leverage its 
extensive NT-based application suite to catch the eyes of IS 
executives looking for complete systems suppliers.
Dell Computer Corp.
One Dell Way
Round Rock, Texas 78682
www.dell.com
Dell is the company to watch in 1998 — offering IS executives a 
combination of “first to market” technologies from Intel and good 
29
Windows NT Server Practice Summary
AberdeenGroup 
comparative pricing against other NT/Intel server suppliers.    Dell, 
as the leading computer manufacturer using the direct model of 
distribution, has been focused on selling more to entry-level 
businesses, with a number of IS executives from small and medium 
businesses turning to Dell’s performance desktops to fulfill file, 
print and departmental server needs.    But it has not concentrated 
on the larger and more competitive NT-in-the-enterprise market 
that seeks to deploy larger enterprise servers as application and 
production servers.    That is about to change.
Dell is expected during 1998 to completely revise its PowerEdge 
server line, and will roll out rack-mounted eight-way servers by the 
end of the year.    Additionally, Dell will add new innovations to its 
servers — including unique rack systems — that will move beyond 
its traditional position as providing only Intel technology with little 
of its own technical expertise.    Dell is also the first supplier to 
disavow its line of uni-processor servers — suggesting that NT 
servers have reached a point in the market where customers are 
no longer buying server with only one processor (using desktops as 
less expensive file and print servers). 
Dell this year will form a number of partnerships and alliances, 
both to build a professional services network using systems 
integrators like EDS and Wang for fulfillment and to cement its 
alliances with database suppliers Microsoft and Intel in order to 
advance technology development.    Dell also has taken other 
actions in preparation for focusing on the enterprise, including 
OEMing Data General’s fibre channel storage and establishing its 
own storage division. 
Aberdeen Conclusions
Dell’s hurdle will be to convince IS executives that it can utilize 
partners to offer the same level of service and support needed to 
deploy and manage enterprise-level NT/Intel servers, and offer the 
bleeding edge innovations that IS executives look for in production 
environment caliber servers.    Aberdeen suggests that Dell will be 
able to transition to the enterprise successfully, and continue to 
attract IS executives’ attention.    Dell will continue to foster and 
improve its automated way of getting components and complete 
systems to customers without a middleman, and companies such as 
Compaq, IBM and HP will continue to try and emulate what Dell 
has done through its distribution model. 
Digital Equipment Corp.
30
Windows NT Server Practice Summary
AberdeenGroup 
111 Powder Mill Rd.
Maynard, MA 01754-1482
www.digital.com
Digital Equipment has attracted the eyes of Compaq’s strategists 
because of key assets that make Digital Equipment a standout in 
the NT/Intel server market:    its NT professional services and its 
enterprise NT strategy, technology and product offerings.    Digital 
Equipment may have the market’s largest installed base of its own 
NT-based (as well as Microsoft Cluster Server) clustered systems, as 
well as over 1,600 trained certified professionals focusing solely on 
NT.    Digital Equipment also has a number of technology initiatives, 
including its Alpha microprocessor (with its fabrication recently 
sold to Intel), clustered systems and software tools on both Unix 
and NT, and systems management and Internet application 
resources.
Moreover, Digital Equipment has:
33.A large investment in research and development on NT, 
including 64-bit expertise;
34.Extensive experience in deployment of NT-based 
infrastructures that includes solving NT-based network, 
scalability, availability, security, and systems management 
issues;
35.Specific NT expertise in the deployment of Microsoft 
Exchange, Internet, data warehouse, and Electronic 
Commerce servers, as well as NT/Unix integration; and
36.The cachet of being the first Microsoft-backed “Prime 
Integrator” — positioning Digital Equipment as one of the 
top NT professional services forces.
However, up to now, Digital Equipment has not gained enough 
market share with its systems, and its overall execution has not 
been effective in gaining the interest of enough IS executives.    
Until just before Compaq and Digital Equipment announced their 
tentative plans to merge, Digital Equipment provided two lines of 
servers that used NT:    its enterprise-level high-powered Alpha 
microprocessor-based systems and a line of Intel-based servers.    
Digital Equipment has now merged the two lines into one, better 
positioning them to offer a full-line approach to IS executives.    
This includes “ready to go” NT-based clusters that feature Digital 
Equipment’s new systems management tools to better monitor and 
administer clusters.
31
Windows NT Server Practice Summary
AberdeenGroup 
Aberdeen Conclusions
For Digital, the challenge going forward will be to retain its lead 
both from a technology and professional services standpoint in the 
NT/Intel server market.    IS executives may also want to pay close 
attention to where Digital’s product lines end up within Compaq’s 
umbrella of offerings, if the acquisition goes through.
32


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | ntserv~1-56bd94 |
| title | Windows NT Server: 1998 Practice Summary |
| author | Aberdeen Group |
| date | 1998-05-01 |
| type | other-research |
| subject_domain | windows-nt-server |
| methodology | industry-analysis |
| source_file | NTSERV~1.DOC |
| license |  clustering (Microsoft Cluster Server/Wolfpack) |

### Abstract

Aberdeen Group's 1998 practice summary on the Windows NT Server market covering Intel-based server hardware and the NT operating environment. The report sizes the NT server hardware market at $6 billion in 1997 and projects 50% annual growth; it also covers SMP architectures

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** |  systems management deficiencies |  and supplier profiles for Intel |
| **Relevance** |  Microsoft |  Compaq |
| **Prescience** |  HP |  IBM |

### Prescience Detail


**Prediction 1:** NT server hardware market growth forecast
- **Claimed:** 50% annual growth for next 4 years; hardware market to grow to $9 billion by 2000
- **Year:** 1998
- **Confidence at time:** high

**Prediction 2:** NT application server revenue forecast (2001)
- **Claimed:** NT application revenues ~$2B in 1997; will grow to ~$13 billion by 2001
- **Year:** 1998
- **Confidence at time:** medium

**Prediction 3:** NT 5.0 release timeline and features
- **Claimed:** Windows NT 5.0 to be released sometime in 1999; will add Active Directory
- **Year:** 1998
- **Confidence at time:**  better clustering

**Actual Outcome 3:** NT 5.0 (Windows 2000) release timing
- **Result:** [DEFERRED]
- **Confidence:** high
- **Notes:** Windows 2000 shipped February 17 2000 — verify and update.

**Prediction 4:** IA-64 (Merced) timeline
- **Claimed:** Intel IA-64 (Merced) arriving late 1999; IA-32 to IA-64 conversion likely takes 5+ years
- **Year:** 1998
- **Confidence at time:** medium

**Actual Outcome 4:** IA-64 (Itanium) commercial availability
- **Result:** [DEFERRED]
- **Confidence:** medium
- **Notes:** Itanium shipped June 2001; verify market adoption pace.


### Entities Referenced (17)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | acquired | Aberdeen/Harte-Hanks |
| Microsoft Corporation | company | active |  |
| Intel Corporation | company | active |  |
| Compaq Computer Corporation | company | acquired | HP (2002) |
| Hewlett-Packard (HP) | company | split | HP Inc./HPE (2015) |
| International Business Machines Corporation | company | active |  |
| Dell Computer Corporation | company | active |  |
| Digital Equipment Corporation | company | acquired | Compaq (1998) |
| NCR Corporation | company | active |  |
| Data General Corporation | company | acquired | EMC (1999) |
| Netframe (a division of Micron) | company | [DEFERRED] | [DEFERRED] |
| NEC Corporation | company | active |  |
| Unisys Corporation | company | active |  |
| Gateway, Inc. | company | acquired | Acer (2007) |
| Electronic Data Systems (EDS) | company | acquired | HP (2008) |
| Wang Laboratories | company | acquired | Getronics (1999) |
| Tandem Computer Corporation | company | acquired | Compaq (1997) |

### Technologies Referenced (14)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Windows NT Server 4.0 | platform | Microsoft | current | obsolete |
| Windows NT Server 5.0 | platform | Microsoft | pre-release | obsolete |
| Intel IA-32 Architecture (Pentium Pro/II/Xeon) | platform | Intel | current | obsolete |
| Intel IA-64 Architecture (Merced/Itanium) | platform | Intel/HP | pre-release | legacy |
| Digital Alpha Microprocessor | platform | Digital Equipment | current | obsolete |
| Microsoft Cluster Server (MSCS/Wolfpack) | framework | Microsoft | emerging | obsolete |
| Symmetric Multiprocessing (SMP) Architecture | platform | Various | current | active |
| Microsoft Active Directory | application | Microsoft | pre-release | dominant |
| Intelligent I/O (I2O) | framework | Intel | emerging | obsolete |
| Virtual Interface Architecture (VIA) | framework | Intel | emerging | obsolete |
| Unix Server Platform | platform | Various | mature | active |
| Microsoft Exchange | application | Microsoft | current | active |
| Fibre Channel | protocol | ANSI | emerging | active |
| DMI/WBEM/IPMI Management Standards | framework | DMTF/Intel | emerging | legacy |

### Observation Summary

- Total observations: 23
- By type: market-assessment: 11, competitive-assessment: 6, viability-prediction: 4, actual-outcome: 2
