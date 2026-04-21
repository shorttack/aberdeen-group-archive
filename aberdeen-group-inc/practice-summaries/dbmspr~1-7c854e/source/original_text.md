# Data Management: 1998 Practice Summary

> Archived from: DBMSPR~1.DOC
> Original publication date: 1998-05-01
> Author: Aberdeen Group

---

## Original Document Text

AberdeenGro
up
Data 
Management:
1998 
Practice 
Summary
May 1998
Aberdeen Group, Inc.
One Boston Place
Boston, Massachusetts 02108 
USA
Data Management Practice Summary
AberdeenGroup 2
Telephone: 617 723 7890
Fax: 617 723 7897
www.aberdeen.com
Data Management Practice Summary
AberdeenGroup 3
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
Data Management Practice Summary
AberdeenGroup 4
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
Data Management Practice Summary
AberdeenGroup 5
TABLE OF CONTENTS
STRATEGIC DATABASE MANAGEMENT SYSTEMS PRACTICE
VI
Description, Focus and Benefits
vi
Strategic Market Questions
vi
EXECUTIVE SUMMARY
1
SUMMARY OF FINDINGS
4
STRATEGIC DATA MANAGEMENT DEFINED
7
The Enterprise Role of Data Management
7
DBMSs as Infrastructure
8
DBMSs within Systems and Networks
8
Core DBMS Services/Capabilities
8
Manage Data
8
Accommodate Changing Levels of Business Usage
9
Accommodate New Data Types
9
Share Data With Other DBMSs
9
Provide Development Support and Access Options
10
Ensure Reliable and Available Data Storage
10
Support Different and Critical Application Types
11
Major Types of Database Management Systems
11
Mainframe File Management
11
Hierarchical DBMSs
12
Network DBMSs
13
Inverted List DBMSs
13
Relational DBMSs (RDBMSs)
14
Object DBMSs (ODBMSs)
15
Object-Relational DBMSs (ORDBMSs)
15
Desktop DBMSs
16
DBMS Deployment Models
16
ISSUES AND CHALLENGES
18
Data Management Practice Summary
AberdeenGroup 6
The DBMS Market: Dead or “Just Resting”?
18
Impact of Major IT Trends
19
Supplier Success Factors
23
User Success Factors
24
SUPPLIER ABSTRACTS
25
Relational and Object/Relational DBMS Suppliers
25
Oracle Corporation
25
Informix Software, Inc.
26
Sybase, Inc.
27
IBM Corporation
28
Microsoft Corporation
29
Computer Associates
30
Progress Software
31
Object DBMS Suppliers
32
Computer Associates
32
Object Design, Inc.
32
Versant Object Technology Corporation
33
InterSystems Corporation
33
Ardent Software, Inc.
33
POET Software
34
GemStone Systems, Inc.
34
Objectivity, Inc.
34
Embedded DBMS Suppliers
35
Pervasive Software, Inc.
35
Data Management Practice Summary
AberdeenGroup 7
Centura Software Corporation
35
InterBase Software Corporation
35
Extended Systems, Inc.
36
Small-Footprint, Highly-Distributed DBMS Suppliers  (for thin clients and portable 
devices)
36
Sybase, Inc.
36
Oracle Corporation
36
Cloudscape, Inc.
37
Object Design, Inc.
37
Centura Software Corporation
37
Computer Associates
37
Data Management Practice Summary
AberdeenGroup 8
Preface
Strategic Database Management Systems 
Practice 
Description, Focus and Benefits
Aberdeen’s Database Management Systems (DBMS) practice 
clarifies for users and suppliers the business benefits and technical 
and market trends of the products organizations use to manage 
their data.    Aberdeen focuses especially on the object-relational, 
object, and relational DBMSs that are key components of today’s 
distributed computing architectures.    As information hubs with 
which applications and other business software interact, DBMSs 
must store and process data effectively, and must easily 
interoperate with other crucial enterprise products, including 
middleware, development tools, servers, and clients. 
DBMSs enable organizations to build scaleable and frequently 
business-critical applications and to adopt the latest approaches to 
sharing information and streamlining business methods, including 
sophisticated decision support, robust on-line transaction 
processing (OLTP), and combinations of the two.    Using DBMSs, 
companies can develop applications that implement data 
warehousing and data mining, support mobile and occasionally 
connected users, and scale Internet sites and electronic commerce.
Effective DBMSs enable companies to distribute data access and 
management to a great range of users both within and outside a 
company, across heterogeneous platforms from different suppliers. 
They provide a secure and safe environment for storing and 
processing data of many different types, including objects, 
multimedia and legacy data, and communicate easily with other 
open software and hardware products. DBMSs can efficiently 
process complex operations as the number of users and the size of 
the database increase, and can support enterprise, workgroup and 
laptop environments.
Database Management Systems is a key practice within the 
Network Services and System Platforms & Architectures practice 
areas. Since most enterprise applications involve data 
manipulation, data display, or transactions, DBMSs are an 
important part of every application development and 
infrastructure initiative.
Data Management Practice Summary
AberdeenGroup 9
Strategic Market Questions

What are the tradeoffs of object and object-relational DBMS 
technology versus the mainstream relational databases? 

Are "mass" pricing and distribution models employed by 
Microsoft and others commoditizing enterprise DBMSs and 
previously high-end capabilities, such as object support, 
performance scalability and OLAP? 

Is the DBMS market slowdown a temporary result of 
overselling, a reflection of market maturity, or a prelude to a 
dramatic shift in the distribution and technical makeup of 
DBMSs? 

What is the impact of the trend towards distributed 
workgroup, mobile and desktop databases? 

How will the database needs of hot development areas, such 
as electronic commerce and Web content, drive the next 
round of DBMS products? 

Which DBMS should the IS buyer bet on for long-term 
Internet scalability? 

Are NT DBMSs ready for prime time? 
This Practice Summary is part of a comprehensive Aberdeen Group 
service aimed at executives who must make strategic database 
management technology decisions.
Data Management Practice Summary
AberdeenGroup 1
Chapter One
Executive Summary
The Critical Enterprise Role of DBMSs
Aberdeen’s Strategic Database Management Systems (DBMS) 
practice clarifies for users and suppliers the business benefits and 
technical and market trends of the products that organizations use 
to manage their data.    Aberdeen focuses especially on the object-
relational, object, and relational DBMSs that are key components of 
today’s distributed computing architectures and therefore strategic 
to today’s enterprise.
DBMSs enable organizations to build scalable and frequently 
business-critical applications and to adopt the latest approaches to 
sharing information and streamlining business methods, including 
sophisticated decision support, robust on-line transaction 
processing (OLTP), and combinations of the two.    Using DBMSs, 
companies can develop applications that implement data 
warehousing and data mining, support mobile and occasionally 
connected users, and scale Internet sites and electronic commerce.
Effective DBMSs enable companies to distribute data access and 
management to a great range of users both within and outside a 
company, across heterogeneous platforms from different suppliers. 
They provide a secure and safe environment for storing and 
processing data of many different types, including objects, 
multimedia, and legacy data, and communicate easily with other 
open software and hardware products.    DBMSs can efficiently 
process complex operations as the number of users and the size of 
the database increase, and can support enterprise, workgroup and 
laptop environments.
Since most enterprise applications involve data manipulation, data 
display, or transactions, DBMSs are an important part of every 
application development and infrastructure initiative.    As 
information hubs with which applications and other business 
software interact, DBMSs must store and process data effectively, 
and must easily interoperate with other crucial enterprise 
products, including packaged applications, middleware, 
development tools, servers, and clients.
Data Management Practice Summary
AberdeenGroup 2
The State of the DBMS Market
1997 and early 1998 have been an incredibly turbulent period 
within the DBMS marketplace.    The overall sales growth rates of 
several leading DBMS suppliers, including Oracle, Informix, and 
Sybase, stalled or even slumped, leading many to question the way 
in which DBMSs are produced and sold.
Aberdeen believes that the DBMS market is, indeed, in a 
transitional period and that certain DBMS market fundamentals 
will be permanently altered.    These changes are being driven not 
only by competition and new technology but also, and perhaps 
most importantly, by changes in the way organizations are buying 
and developing applications and building their information 
infrastructures.    Although current DBMS marketplace uncertainty 
can be worrisome for end-user organizations, the changes 
ultimately reflect their priorities and will result in more and better 
options.    Most vendors, on the other hand, will need to reposition 
their products and nimbly reinvent their entire strategies to 
achieve success or even remain viable.
Aberdeen has made the following findings about the current DBMS 
market and its expected evolution:

The DBMS market will continue to grow at a moderate pace.    
However, revenues in the major Unix-server-based market 
segment will grow slowly, and per-seat revenues in many 
segments will drop as DBMSs become commoditized. Overall 
DBMS market growth will be fueled by “hot” sub-segments such 
as business intelligence and mobile user databases and by 
packaged applications;

The DBMS market will experience greater segmentation, 
especially at the higher-growth low and high ends.    Important 
new segments include middle-tier databases supporting Web 
applications, small-to-mid-sized businesses, business 
intelligence applications, and mobile computer and computing 
device applications. 

Driven by packaged enterprise applications and the NT-based 
Microsoft volume sales model, important enterprise DBMS 
features and functions — but not the high-end segments 
themselves — will be commoditized;

The data management needs of new multi-tier application 
architectures will lead DBMS vendors to focus on the 
middleware and development tools markets even more than in 
the past; 
Data Management Practice Summary
AberdeenGroup 3

“Pure” object DBMSs will begin to lead in several niche market 
segments, including component-based application development, 
but will remain a minor player in the mainstream market.
Aberdeen believes that users increasingly demand and vendors 
need to provide a range of DBMSs offering extreme deployment 
versatility while still providing the stability required by mission-
critical applications running in all parts of the enterprise.    DBMS 
vendors can meet these complex and conflicting demands, but will 
need to change their fundamental strategies to do so.
Data Management Practice Summary
AberdeenGroup 4
Chapter Two
Summary of Findings
The DBMS market is being altered fundamentally by dramatic 
shifts in IS buying behavior.    First, enterprises increasingly are 
buying products within the context of applications — as solutions 
— rather than as pieces of the enterprise architecture.    Second, the 
DBMS market is becoming increasingly segmented, with most 
buying within sectors driven by distinct and different technical 
and business priorities.    Third, to gain competitive advantage 
while making themselves more flexible and efficient, organizations 
are accruing and processing ever-greater amounts of data while 
distributing information and dispersing decision-making to every 
corner of the enterprise.    Finally, the three-headed technical hydra 
of Windows NT, objects, and Internet technologies are 
transforming the way databases are deployed, just as they are 
changing every other part of most companies’ information 
infrastructures.
As a result, DBMS vendors’ previously successful business and 
technical strategies no longer map to the new IS landscape.    
Vendors will require new perspectives, new atlases, and new paths.
Key Findings

The DBMS Market Is Subdividing.    New market segments are 
being added to the old at a rapid pace, each segment with its 
own combination of technical and business values, distribution 
channels, users, and purchasers.    These segments include 
traditional sectors, such as enterprise production, 
department/branch office, and single-user desktop, and newer 
sectors such as enterprise decision support, application 
repository, mobile user, and portable computing device.

LOB Is Hot, Enterprise is Not.    The enterprise production 
segment, based largely on Unix platforms, has slowed, while NT-
driven line-of-business and small-to-mid-sized business 
segments, enterprise decision support, and mobile user sectors 
are exploding.

Embedded Rules.    Facing a shortage of skilled developers, 
increasing complexity, and shrinking deployment schedules, 
organizations more and more are buying enterprise packaged 
Data Management Practice Summary
AberdeenGroup 5
applications instead of custom-developing them.    Databases 
thus are seen as embedded engines.    This fundamentally 
changes the revenue and channel models that DBMS suppliers 
have been using. It also means that supplier VAR and ISV 
indirect-channel networks are more critical than ever.

Aberdeen Criteria Remain the Same, But The Weighting Varies.    
Aberdeen’s key buyer criteria for DBMSs — scalability, 
openness, extensibility, distributed-technology support, 
programmer productivity, and new technology support — 
remain the same.    However, the relative importance of each 
criterion now varies from market segment to market segment.    
For example, in the packaged-application-driven small-to-mid-
sized business (SMB) market, easy administration and Windows 
NT support are much more important than extensibility and 
distributed technologies.

The Market Opens Up.    Market leadership is accelerating in 
certain market segments.    For example, both Oracle8 in the 
enterprise Unix production segment and Microsoft SQL Server 
in departments and branch offices are magnifying their market 
shares.    However, the marketplace changes are creating new 
opportunities even in the established segments, while the newer 
segments represent opportunities for both established vendors 
and start-ups. Although Aberdeen doesn’t expect near-term 
consolidation among the major vendors, we do believe the 
major vendors will buy small start-ups to more quickly enter 
and occupy newer market segments. 

Great Opportunities for Value-Added Resellers (VARs) and 
Independent Software Vendors (ISVs).    Many of the same factors 
driving enterprises to buy packaged applications also are 
creating large opportunities for VARs and ISVs.    Companies are 
outsourcing system integration work to match their packaged or 
prefabricated applications.    It’s no coincidence that the largest 
DBMS vendor, Oracle, has service revenues as large as its 
software licensing revenues, and that Informix and Sybase both 
are greatly expanding their service operations. 

The Two Tracks of Object DBMS Technology.    Three of the six 
largest DBMS vendors (Informix, IBM and Oracle) have adopted 
in differing ways the object-relational data storage model.    The 
remaining companies, Microsoft, Computer Associates, and 
Sybase, are largely committed to a relational model, specifically 
deferring object capabilities to separate object databases.    
Aberdeen believes that object capabilities are increasingly 
Data Management Practice Summary
AberdeenGroup 6
important, if not yet critical, capabilities, and that many 
applications will need to integrate both object and relational 
data management. Thus, the three vendors advocating separate 
relational and object databases need to not only provide specific 
object database solutions, either home-grown or through third 
parties (as CA’s Jasmine does today), but also must offer a stable 
means by which applications can integrate access to both (as 
CA’s Harmony aims to do). 

Internet Technologies Transform the DBMS.    Internet 
technologies tremendously expand access to enterprise data, 
meaning that DBMSs must scale more than ever before, provide 
Internet middleware to complement the DBMS engine, and 
accommodate sometimes “spiky” usage patterns.    Moreover, 
Java support has become a required DBMS capability in order to 
leverage DBMSs’ scalability for new Internet applications.

Costs Go Down, Expenditures Go Up. Aberdeen believes that 
DBMS price/performance and overall per-unit costs will 
continue to drop, in some segments precipitously, thanks to 
Microsoft-driven commoditization and the packaged application 
purchasing model.    However, given greater data usage and new, 
compelling DBMS uses, overall DBMS expenditures for most 
companies will increase. 
Further into the future, Aberdeen anticipates that NT Clustering 
will fundamentally alter the enterprise production market 
segment.    Within 2-3 years, Windows NT should scale sufficiently 
to accommodate many enterprise production applications.    
Microsoft’s own SQL Server will be enterprise-ready, further 
extending the reach of the Microsoft volume product model and 
providing real competition on the high end for Oracle in particular.
Data Management Practice Summary
AberdeenGroup 7
Chapter Three
Strategic Data Management Defined
The Enterprise Role of Data Management
Data management software consists of products and technologies 
that companies, departments and individuals use to store, manage, 
process and broadly distribute data of all types.    Although Data 
Management includes several important types of software, the 
category is dominated by Database Management Systems (DBMSs), 
integrated sets of programs that enable companies to record, 
modify and retrieve information stored within a database 
according to a specific model. 
DBMSs are “information hubs” with which applications and other 
business software interact, and thus DBMSs must store and process 
data effectively and easily interoperate with other crucial 
enterprise products — especially middleware and development 
tools.    Because of these capabilities, DBMSs underlie most business 
applications, whether they are networked or reside within a single 
computer.
DBMSs currently are in the middle of a major evolutionary step 
forward.    The emerging generation of object and object-relational 
DBMSs are providing greater performance, scalability, and 
flexibility and can support intensive analysis and order-of-
magnitude transaction-rate increases, accommodate complex data, 
and facilitate multi-tier access to business information using 
Internet technologies. 
Ultimately, DBMSs provide the foundation for new business-critical 
applications.    IS increasingly assesses DBMSs based on how well 
they support and interact with applications such as those for:

Enterprise Resource Planning (ERP), especially packaged 
applications;

Electronic commerce;

Decision support, including data warehouses, data marts 
and On-line Analytical Processing (OLAP) programs;

Web-based dynamic publishing and content management;

Mission-critical On-Line Transaction Processing (OLTP);
Data Management Practice Summary
AberdeenGroup 8

Mobile and disconnected users, including applications for 
Portable Computing Devices (PCDs); and

Customer Interaction Software (CIS).
At the same time, DBMSs increasingly are being used by less 
technical line-of-business (rather than centralized IS) users, who 
demand that the new DBMSs be relatively easy and inexpensive to 
use and develop for.
DBMSs as Infrastructure
DBMSs play several major structural roles.    First, DBMSs serve as 
sub-application-level infrastructure, establishing a framework for 
storing information too voluminous or complex to store as files.
Second, DBMSs also provide application-level infrastructure by 
consistently identifying and structuring data according to 
published proprietary and public standards so that a broad range 
of applications can efficiently and reliably insert, extract and 
modify this data.    Finally, DBMSs themselves process application 
logic, through stored procedures and processed queries.    DBMSs 
thus are one of several architectural components that mediate 
between operating systems and the applications, enabling the 
latter to process and present information to end users according to 
established business processes.
DBMSs within Systems and Networks
A new generation of Internet-based data-connectivity and 
middleware technologies, many of which are integrated into the 
DBMS, enable “universal” access to distributed databases.    Thus, 
DBMSs increasingly are critical components of an enterprise 
“framework” or “software architecture,” typically integrated with 
development tools and middleware.
Core DBMS Services/Capabilities
Strategic DBMSs typically provide the following key capabilities:
Manage Data 
Store.    Adhering to one or more database models (relational, 
object, etc.), using the underlying computer operating system(s), 
and following published standards, a DBMS maps information into 
a structured memory space on a computer’s physical hard drive so 
that it is consistently identified and easily accessed.
Process.    DBMSs handle specific types of “tiny applications” called 
transactions that are specialized for data processing.    By 
Data Management Practice Summary
AberdeenGroup 9
multiplexing and optimizing transactions, DBMSs can achieve high 
performance and scalability for data-rich applications.
Support Manipulation.    DBMSs enable applications to enter, modify 
and output stored data.    Standard DBMS methods of supporting 
data access include Structured Query Language (SQL) for relational 
databases and Object SQL (OSQL) for object databases.
Accommodate Changing Levels of Business Usage 
Horizontal Scalability.    DBMSs must efficiently accommodate more 
and more data and requests without incurring performance 
degradation.    IS must be able to increase the capacity of the system 
by adding processing power.    Parallel/scalable technologies such as 
symmetric multiprocessing (SMP) provide a way to achieve such 
gains in performance and size. Horizontal scalability enables IS to 
get maximum usage out of hardware and database software 
investments and to handle sudden, system-threatening traffic 
increases.
Vertical Scalability. Different versions of the DBMS should target or 
at least accommodate distinct enterprise segments, allowing users 
to deploy a system that specifically addresses their needs.    Key 
enterprise segments include extended enterprise (heavy 
concurrent usage    by 100+ active end users), limited enterprise 
(moderate concurrent usage by 50 end users), workgroup 
(departmental usage by 25 end users) desktop (single end user with 
PC/workstation), and mobile/thin client (single user with mobile 
device or Network Computer).
Accommodate New Data Types
Certain types of business-critical applications, such as OLAP and 
Web multimedia publishing, require the ability to store complex 
data, objects, and other new data types.    This capability also 
provides a measure of    investment protection by ensuring that the 
DBMS will support unknown future data types and accompanying 
applications.
Share Data With Other DBMSs
Today’s DBMSs must be distributed, i.e., they are capable of 
exchanging and synchronizing data with other DBMSs of the same 
or different models, from the same or different vendors, and 
running on different platforms.    This capability is crucial given 
today’s increasingly dispersed organizations and the broadly-
accessible applications they require. To possess distributed 
capabilities, a DBMS system must have sophisticated replication 
Data Management Practice Summary
AberdeenGroup 10
tools and data integration middleware, enabling it to accurately 
synchronize its data with a wide variety of other databases.
A data warehouse is a common example of a distributed database, 
in which a DBMS hosting the warehouse and the warehouse 
application will retrieve and synchronize relevant information 
from a number of heterogeneous data sources, including 
client/server and mainframe DBMSs.    Another common 
distributed database scenario consists of applications for mobile 
and occasionally disconnected users that synchronize local 
databases with a centralized enterprise database.
Provide Development Support and Access Options
To support development and provide a wide variety of data-access 
options, today’s DBMSs offer standards-based utilities, such as 
ODBC and JDBC, and proprietary technologies, such as native 
drivers and optimized connectivity APIs.    These enable 
applications to efficiently submit queries and requests to the 
DBMS.    Internet and object technologies, in particular, are 
expanding the spectrum of access options.    Some key technologies 
include:

Web access.    Middleware or a dedicated application component
—integrated with or separate from the DBMS—handles Web 
access.    Typically, Web-access components translate HTML form 
input into SQL queries and repackage the results in HTML.

Java support.    Current DBMSs support JBDC or comparable 
technologies, so that Java applications can directly query, 
modify, and input relational data.    Furthermore, the latest 
DBMSs store Java objects and stored procedures and triggers 
written in Java or other languages.    Some DBMSs feature 
proprietary, optimized JBDC or other Java connectivity 
technologies, bypassing JBDC’s “least common denominator” 
performance limitations.

Access through workflow and e-mail programs.    DBMSs 
increasingly include middleware or other connectivity 
technologies that enable them to easily exchange data with e-
mail or workflow software (which the DBMS supplier often 
offers as well). DBMSs empower workflow and e-mail solutions 
with greater data management capabilities and give their end 
users additional means of data access.
Ensure Reliable and Available Data Storage 
Strategic DBMSs commonly support “mission-critical” applications 
that represent the backbone of a business.    DBMSs thus must offer 
Data Management Practice Summary
AberdeenGroup 11
very high performance, must be able to continuously accommodate 
a high volume of traffic, and must provide “information 
investment protection” by ensuring that the entire database and 
user interactions with the database are relatively fail-safe.    DBMSs 
achieve high performance especially by employing Symmetric 
Multiprocessing (SMP)-supporting technologies such as 
multithreading and parallelization support within the query 
optimizer.    These technologies also help processes to “fail over” to 
increase system availability.    To supply a high degree of data and 
transaction protection, DBMSs also should include backup, 
transaction logging, recovery, and replication capabilities.    
Performance and protection features are especially important in 
today’s distributed database schemas, where more complex 
topologies and applications mean greater risk.
Support Different and Critical Application Types 
Aberdeen notes the increasingly central importance of packaged 
applications and other “prefabricated” solutions as a criterion for 
selecting a database.    Thus, a key DBMS capability is a supplier’s 
network of Value Added Resellers (VARs) and system integrators, 
and the supplier’s relationships with other suppliers creating 
packaged and prefabricated applications.    All of these types of 
companies play vital roles in building, installing and customizing 
solutions using a supplier’s DBMS. 
Additionally, the very nature of applications is changing, blurring 
previous categories, such as OLTP and decision-support.    Next-
generation Strategic DBMSs must frequently host synergistic 
applications rather than being too specifically optimized for one 
type.
Enable Efficient Administration and Optimization
DBMSs or associated tools must maintain, monitor and tune for 
optimum efficiency the processes by which the DBMS manages 
data and interacts with applications, as well as the DBMS itself.    
Such capabilities become ever more important as enterprises seek 
to ensure maximum application ROI and as DBMSs tackle more 
complex applications such as data warehouses and e-commerce. 
Major Types of Database Management Systems
There are eight basic types of database management systems being 
used today by organizations (see Figures 1-3, “Revenues by DBMS 
Type,” for market trends of these types).    Most of the database 
management types have supplemented, rather than supplanted, 
Data Management Practice Summary
AberdeenGroup 12
earlier types.    Figures 1 through 3 reflect this pattern, illustrating 
that, although DBMS type adoption patterns are changing, none of 
the older types are disappearing. 
Thus, most large companies use at least several of the DBMS types 
together, requiring that the DBMSs themselves, middleware, and 
applications all ensure these systems can interoperate.    Note that 
in some cases DBMS types are tied to specific computer platforms 
or operating systems, while others, such as Relational and Object-
Relational database management systems, run on a wide range of 
platforms. 
The eight basic categories of data management systems include: 
Mainframe File Management
Most mainframe data, and thus a large portion of all corporate data 
worldwide, is stored as records and files directly on the hard drives 
of mainframe systems.    File management database software, 
usually integrated with a mainframe operating system, enables 
users to record, modify, and retrieve these records and files.    IBM 
produces - and sells as part of its mainframe systems - all of the 
leading file management database systems - ISAM (Indexed 
Sequential Access Method), VSAM (Virtual Sequential Access 
Method), and CICS/Fastpath.    All use indexes of keys to directly 
access individual records.    File management database systems are 
very fast for on-line transaction processing (OLTP) for small 
datasets, but are hard to administer and upgrade, and process 
queries slowly. 
Mainframe file management systems continue to be used primarily 
for older, “legacy” mainframe applications that required many 
small transactions.    Newer or upgraded mainframe systems 
increasingly employ IBM’s DB2 object-relational DBMS. 
Hierarchical DBMSs
Structuring records and files in an inverted “tree” schema, 
hierarchical DBMSs are relatively easy to create and manage but 
do not flexibly capture more complex “parent-child” relationships 
between data elements.    Hierarchical DBMSs are moderately fast 
at OLTP and batch processing, and can support fast querying only 
if a database’s hierarchical structure matches that required by a 
particular query.    IBM’s IMS, which is the second most heavily-
used data management software on mainframes, typifies the 
hierarchical type of data management software.    Hierarchical 
DBMSs predominantly are used for large-scale OLTP in datacenters 
and 
Data Management Practice Summary
AberdeenGroup 13
Figure 1:    1996 Revenue Shares by DBMS “Type”
Source: 
Aberdeen Group, April 1998
Data Management Practice Summary
AberdeenGroup 14
medium-sized businesses or divisions.    As is the case with file 
management data systems, most hierarchical DBMSs are found 
within IBM mainframe systems and are gradually being replaced 
by IBM’s DB2.
Network DBMSs
These DBMSs use pointers to establish relationships between 
records and files.    Network DBMSs thus are relatively easy to 
design, given the flexibility in establishing inter-data relationships, 
but also are difficult to program.    Network DBMSs are most often 
used within mainframes and high-end minicomputers and 
represent a relatively small part of the market.    They sometimes 
are found in medium-scale data environments.    Network DBMSs 
process OLTP and batch requests relatively quickly, but do not 
execute queries as well. 
Inverted List DBMSs
These DBMSs use pointers and tables to enable users to more 
directly and efficiently access values within records from indexes. 
Inverted list DBMSs are often not easily designed, programmed, or 
managed, but for DBMSs with a modest sets of values they offer 
excellent data processing performance and scale quite well. 
Inverted list DBMSs are housed on mainframes and are most 
commonly used for medium-to-large scale OLTP in datacenters and 
medium-sized divisions and businesses.    The 
Figure 2: 1997 Revenue Shares by DBMS “Type”
Data Management Practice Summary
AberdeenGroup 15
Source: Aberdeen Group, 1998
Data Management Practice Summary
AberdeenGroup 16
leading inverted list DBMSs are Computer Associates’ CA-Datacom 
and Software AG’s Adabas.    A significant sub-segment of the 
mainframe DBMS market, inverted list data systems are gradually 
being replaced by relational and object DBMSs that better support 
queries.
Relational DBMSs (RDBMSs)
For the past decade the dominant database model in terms of new 
installations, RDBMSs structure data in tabular sets of rows and 
columns.    Designers and programmers can establish varied and 
reasonably complex relationships between these tables and use 
“relational algebra” (in the form of a query language) to define the 
scope and required results of a request.    RDBMSs offer reasonable 
performance for OLTP and excellent support for queries and 
analysis.    As a result, RDBMS success has directly reflected 
organizations’ growing need to better analyze their information 
and exploit it for business gain.    The RDBMSs’ flexible architecture 
has enabled this type of DBMS to work well in distributed 
environments and continuously gain improvements in 
performance, design, manageability and programmer productivity. 
Figure 3: 1998 Revenue Shares by DBMS “Type” 
Source: Aberdeen Group, 1998
Data Management Practice Summary
AberdeenGroup 17
RDBMSs and their technical offspring the object-relational DBMSs 
(ORDBMSs) dominate the minicomputer, PC LAN, and mid-range 
server markets and are gradually gaining prominence in the 
mainframe and PC sectors.    RDBMSs and ORDBMSs account for 
over 80% of all new DBMS revenues.    Figures 1-3 illustrate the 
broad impact of object technology on DBMS systems and the 
resulting, evolutionary shift of majority market share from 
relational to object-relational DBMSs.    In an era of sophisticated 
data types and processing and distributed object computing, 
companies need at least some object data capabilities, and the 
RDBMS segment has begun to suffer as a result.    The RDBMS 
segment would appear quite weakened if it weren’t for the surging 
growth of Microsoft’s SQL Server RDBMS.
Object DBMSs (ODBMSs)
Heralded a decade ago as the next defining database technology, 
object database management systems are today a relatively small 
(less than $200 million in 1997 revenues) but still important market 
segment.    Rather than storing simple text and numerical data like 
RDBMSs, ODBMSs store a wide range of data types in the form of 
integrated packages (objects) of data and, sometimes, code 
operating upon this data.    ODBMSs possess distinctive strengths, 
including the ability to store multimedia, complex data types, and 
business logic and the ability to better interoperate with 
increasingly object-oriented application development tools. 
Although ODBMSs are used significantly within certain vertical 
market segments demanding complex data processing, such as 
telecommunications and finance, object database technologies 
have moved into the mainstream primarily by being assimilated 
into “traditional” RDBMSs (see “Object-Relational DBMSs below).    
However, as Figures 1-3 illustrate, use of “pure” ODBMSs continues 
to grow, and the segment is vibrant if small. 
Object-Relational DBMSs (ORDBMSs)
Sometimes referred to as “Universal Servers,” ORDBMSs are a 
variant of RDBMSs that add a base level of support for objects and 
complex data types to a relational database system. This support 
can be implemented in several different, primary ways: the 
ORDBMS may provide a common interface to both relational and 
object data but store them separately, or the ORDBMS may actually 
store the object data within the core relational engine, usually by 
“wrapping” the object data in a relational veneer. 
Data Management Practice Summary
AberdeenGroup 18
The ORDBMS model has been embraced by several leading DBMS 
vendors, including Oracle, Informix and IBM.    However, other 
market leaders, including Microsoft, Computer Associates, and 
Sybase, believe that such a hybrid structure compromises object 
and even relational performance.    These suppliers assert the 
superiority of separate object and relational databases.    Thanks to 
the launch of the Oracle8 ORDBMS in 1997, ORDBMSs now generate 
over 50% of new DBMS revenue.    As Figure 3 shows, 1998 will be 
the first year that ORDBMS revenues outpace those of RDBMSs.    
Although most companies deploying ORDBMS systems do not yet 
fully leverage their object capabilities, these systems nonetheless 
now govern much of the marketplace.    ORDBMSs anticipate an 
emerging enterprise landscape dominated by distributed object 
computing and huge, sophisticated decision support systems 
integrating heterogeneous data
Desktop DBMSs
These DBMSs are defined by the platforms on which they are based 
and the single-user (versus multi-user) applications they generally 
support rather than by a distinguishing technology, although they 
generally employ a flat-file or simple object data structure.    The 
clear leader in desktop DBMSs is Microsoft’s Access, although 
others compete in this segment.    Figures 1-3 show that the desktop 
DBMS market, dominated by Microsoft, continues to grow as fast as 
the general market.
DBMS Deployment Models
Enterprises typically deploy strategic DBMSs following a “2-tier” or 
“3+-tier” model.
Figure 4:    Application Architectures
Data Management Practice Summary
AberdeenGroup 19
Source: Aberdeen Group, May, 1998
As shown in Figure 4, a 3+ tier model currently is the favorite in 
enterprise computing and stems from the growth of Internet client 
and middleware technologies.    The new middle layers, including 
Web, application, and, increasingly, transaction servers, provide 
session and state management and other qualities that Internet 
technologies lack, and imbue Internet-based schemas with 
scalability and robustness.    In this schema, the middle layers tend 
to host most of the processing, taking some of the load off the 
backend database server.    Programmers can leverage reusable 
components and objects at any level to work more productively.
The two-tier development model is less scalable but will not go 
away in the next several years.    For example, users implementing 
corporate workgroup and departmental Intranets may find that a 
direct client-to-database connection provides adequate scalability, 
flexibility, and administrative support in the near term.
Data Management Practice Summary
AberdeenGroup 20
Chapter Four
Issues and Challenges
1997 witnessed the high-profile revenue struggles of leading DBMS 
vendors, including Oracle, Sybase, and Informix.    Does this mean 
the DBMS has indefinitely or permanently stagnated? 
Aberdeen believes that the overall DBMS market will continue to 
grow at a healthy rate — the demands of today’s information-
driven businesses are simply too great.    However, we do think that 
1998 is a year of transformation for the DBMS market.
Over the next 1-2 years, changing enterprise needs will produce a 
more highly segmented market.    Each segment will require a 
unique combination of channel, pricing and technical 
requirements.    DBMS vendors are scrambling to meet new user 
needs and define new channel strategies.    The result should be 
lower IS data-management costs and wider deployment options. 
The DBMS Market: Dead or “Just Resting”? 
The DBMS marketplace now is being strained by several competing 
forces.    On the one hand, the aggregate market for DBMS systems - 
the units themselves - continues to grow quite well, albeit not at 
the 30% annual rate of five years ago.    On the other hand, per-unit 
and per-seat revenues and thus vendor profits in key market 
segments are dropping as DBMSs become commoditized.    The 
market is being beset by increasing segmentation, changing 
channel business models, and temporary slowdowns in some 
market segments.    This combination has quite understandably 
produced several quarters of poor revenue growth and profits 
among major DBMS vendors as they try to adapt to a new market 
landscape. 
In spite of these factors, Aberdeen believes that the DBMS market 
overall will continue to grow at a moderate pace for the next two 
years, because:

A second generation of Web servers is beginning to turn 
to scalable databases for rapid deployment;

Low-priced PCs plus new mobile and wireless support in 
low-end products will drive more sophisticated DBMSs 
onto a wider range of desktops; and
Data Management Practice Summary
AberdeenGroup 21

The underlying business demand for greater amounts of 
business-critical data continues to be insatiable.
Not surprisingly, the segments that will experience the greatest 
growth during the next few years are smaller, newer markets.    In 
other words, the emerging market opportunities during the next 
few years will be quite different than those of the past decade, and 
not all of the recent market leaders will continue their success into 
the next century. 
Impact of Major IT Trends
Because DBMSs provide a foundational layer between operating 
systems and hardware and applications, they are affected by — 
and often must accommodate — trends in all major parts of an 
enterprise information structure. The following business, technical 
and application developments will alter the way DBMS systems are 
designed, used and sold during the next several years.
Market Segmentation.    Over the next year, as enterprises look for 
more specific and more pre-packaged solutions to their exploding 
data management needs, IS buyers will seek DBMSs specifically 
configured for specific types of tasks and specific levels within the 
enterprise.    The primary market segments, applications typically 
developed within each, and the segments’ near-term growth 
prospects are outlined in Figure 5.
Figure 5:    Primary DBMS Market Segments
User Segment
Typical Applications 
Near-Term 
Growth
Enterprise 
Production
Enterprise Resource 
Planning (ERP)
OLTP (including e-
commerce)
High-end: strong 
unit sales and 
revenues
Low-end: modest 
unit sales, 
decreasing per-seat 
revenues
Enterprise Decision 
Support
OLAP
Business Intelligence
Very strong unit 
sales and revenues
Branch Office
ERP
Modest unit sales 
but decreasing per-
Data Management Practice Summary
AberdeenGroup 22
OLTP
OLAP
Competitive Advantage
seat revenues
Small-to-Mid-Sized 
Business (SMB)
ERP
OLTP
Mixed workload 
(OLTP/OLAP)
Web/Content Management
Very strong unit 
sales but decreasing 
per-seat revenues
Department/
Workgroup/Line of 
Business
Competitive Advantage
Web/Content Management
Strong unit sales but 
slow per-seat 
revenue increases
Single PC User
Business Productivity
OLTP & ERP client
Modest unit and 
revenue growth
Thin Client - 
continuously 
connected
Business Productivity
OLTP & ERP client
Competitive Advantage 
client
Strong unit sales 
(but not a large 
market)
Mobile user - 
occasionally 
connected
Business Productivity
Competitive Advantage 
client
Field service & sales apps
Very strong unit 
sales (but not a large 
market)
Portable Computing 
Device
Business Productivity
Competitive Advantage 
client
Field service & sales apps
Very strong unit 
sales (but currently 
a small market)
Source: Aberdeen Group, May 1998
The Rise of Packaged Applications.    Packaged applications, 
rather than architectural considerations, are increasingly driving 
database purchasing decisions.    Facing a shortage of skilled 
developers for key new competitive-advantage applications, 
enterprises are increasingly purchasing packaged or pre-fabricated 
enterprise applications from vendors such as Baan, SAP, Peoplesoft, 
and Oracle instead of custom-developing them.    This does not 
necessary mean that fewer DBMSs will be sold — packaged 
application deployment may ultimately increase the number of 
units sold.    However, the increase in importance to IS of packaged 
applications contributes to the commoditization of enterprise 
production DBMSs and will help decrease DBMS suppliers’ revenue 
per DBMS unit. 
Data Management Practice Summary
AberdeenGroup 23
Commoditization.    Several converging factors, most notably the 
growth of Windows NT servers, are changing the traditional 
business model within some DBMS market segments (usually low-
end) from modest-volume sales and architectural purchases 
towards high-volume (“mass-deployment”) sales and business-
productivity use.    This means exploding unit volume sales in low-
end segments but much less revenue — and profit — per unit sold. 
Consulting & Services.    Because of the shortage of capable 
programmers, limited IS budgets, and the tremendous complexity 
of information technology, the consulting and services business 
within the DBMS market continues to boom, outpacing software 
licensing revenues.    The major DBMS vendors all either are 
expanding their networks of system integrators and VARs or 
building their own in-house services businesses, or both.    The 
latter avenue is especially attractive, given the need to diversify 
revenue sources in the face of revenue slowdowns in some DBMS 
market segments. 
Microsoft will continue to broaden its reach.    Windows NT will 
continue to become more scalable, and Microsoft will further 
capitalize on these opportunities with the launch of SQL Server 7 
later in 1998.    Although we don’t believe that Microsoft will 
dominate the very high and very low ends of the DBMS market 
segment, the company will possess significant market share in all 
other segments and should    lead in the NT market, with Oracle 
retaining a significant revenue share.    Where Microsoft is 
competitive, the segment becomes at least somewhat 
commoditized.    The Business Intelligence DBMS segment will be 
the next area to experience this effect.
Windows NT.    The explosive growth of the NT and NT-database 
markets should continue for the foreseeable future.    Aberdeen 
finds that branch offices, departments, and small-to-mid-sized 
businesses will increasingly use and try to scale Windows NT.    
These buyers are particularly looking for “turnkey” and “almost-
lights-out” solutions with little administration or outside support 
required after the design phase.    Thus, these markets look 
especially for aggressively-priced, “commoditized” DBMSs. 
Scalable High-End Databases.    Enterprise DBMSs (for OLTP and 
decision support) continue to require ever-greater horizontal 
scalability to support increasing transaction rates and numbers of 
users, and vertical scalability so that applications can be shared 
across different levels of an organization.    The need for horizontal 
scalability has been accentuated by expanded, browser-based 
Data Management Practice Summary
AberdeenGroup 24
client data access that also can generate unpredictable loads on 
DBMS systems.    However, advances in parallel-processing support 
within major RDBMSs and ODBMSs will continue to provide much 
of the availability and performance enterprises will require.    This 
combination of new needs and DBMS capabilities will continue to 
expand high-ticket sales of high-end DBMSs over the next two 
years, although at a lower rate than NT sales.
Internet technologies.    Web client technologies are having a 
profound impact on the DBMS market, because they provide a low-
maintenance, platform-neutral vehicle for mass data 
dissemination.    Web sites demand rapid DBMS scalability and 
DBMS multimedia-object support.    In addition, Java is emerging as 
the server-side programming language of choice within many 
enterprises.    Support for Java, and even the ability to store Java 
components and procedures, is driving the arrival of a new and 
rapidly growing market segment of “second-tier” Web databases. 
Object and object-relational DBMSs.    Object database 
capabilities continue to grow in importance, but still have not 
redefined the DBMS market to the degree many anticipated.    As 
Aberdeen predicted, object technologies are now in use primarily 
within object-relational databases, not object ones.    Aberdeen also 
finds that the “best purposes” of pure object and object/relational 
models are increasingly clear.    Object-relational DBMSs are 
gaining ever-stronger object capabilities, and will dominate in 
providing general-purpose data management and for bridging 
legacy and new data needs.    Pure object DBMSs will represent a 
growing niche and will continue to address the demanding needs 
of complex-data management and Internet and multimedia 
computing.
Distributed DBMS Technologies.    Distributed database 
technologies are key to enabling organizations to effectively 
manage their information, given the increasingly decentralized 
nature of today’s global enterprises and their broad-based need for 
timely and integrated data.    These trends are compounded by 
Internet technologies that enable even broader client access and 
foster multi-tier computing schemas.    Increasingly sophisticated 
and capable database administration tools enable IS professionals 
to view and interact with multiple, displaced systems as though 
they were one, making operations and locations easier to distribute 
and manage. Also, DBMS suppliers continue to dramatically 
improve replication technology, critical for several major new 
types of applications, including advanced decision 
Data Management Practice Summary
AberdeenGroup 25
support/business intelligence and mobile/occasionally-connected 
users. 
E-Commerce/Web Content Management.    The Web has proven to 
be an tremendously effective medium for broadly distributing 
many types of information.    Unfortunately, it also is a difficult 
medium for managing information:    the file-system storage model 
of most companies’ Web servers drains resources and limits the 
true information management potential of Web technology.    The 
market recognizes that DBMSs should be the foundation for 
content management applications, but, with a few high-end 
exceptions, such solutions have not been available.    Fortunately, 
developers and DBMS suppliers themselves have begun to address 
this need.    Within the next several years, Aberdeen believes that 
packaged and custom content-management solutions will be a 
significant new driver for DBMS systems. 
Business Intelligence.    One of the bright spots for high-end DBMS 
vendors in 1997, this market segment demands not simply high-
performance DBMSs featuring powerful query optimizers and 
parallel-scalable capabilities, but also effective partnerships with 
third-party vendors offering data warehousing, data mining, and 
other advanced decision-support applications.    Aberdeen notes 
that all of the major DBMS vendors are directly targeting this high-
growth and high-profit segment, but also observes that they will 
have to perform a balancing act between building — or buying — 
their own business intelligence applications and actively 
supporting the development efforts of their decision-support 
partners. 
Mobile/Occasionally-connected Workers.    This promising — and 
highly hyped — market segment has been fueled by the trend 
within enterprises to decentralize decision-making and by the 
continuing success of laptop computers and Portable Computing 
Devices (PCDs) such as the Palm Computer.    The improving 
price/performance of these devices and the sophisticated nature of 
the new applications that companies are seeking to run on them 
(most notably sales force automation and field service programs) 
are creating a new market for small-footprint, highly distributed, 
embedded databases.    Several major and a number of smaller 
DBMS suppliers are currently developing or shipping DBMSs 
specifically for this market.    The mobile PC market already is 
established and should continue to grow rapidly, as should the 
market for mobile DBMSs.    The viability of the PCD hardware and 
database markets will depend entirely on the success of the 
Data Management Practice Summary
AberdeenGroup 26
applications.    Aberdeen believes that this is a significant new 
niche market.
Supplier Success Factors
Repositioning.    During 1998 all major DBMS suppliers will need to 
reevaluate their product strategies and positioning in light of the 
new user segments, applications, and business imperatives.    
Aberdeen anticipates that most suppliers will:

Launch new products and new business initiatives for 
business-intelligence, mobile user, and Small-to-Mid-sized 
Business (SMB) market segments;

Beef up their services business offerings — note that 
Oracle’s service revenue about equals its software 
licensing revenue; 

Launch second-generation Web development tools and 
middleware.
However, all of the major suppliers and many small ones are 
targeting the same hot new markets, whether they suffered during 
1997 or not, and these hot segments also are relatively small.    The 
good news for some suppliers is that in many of the new segments, 
such as mobile user, Small-to-Mid-Size Businesses, and multi-tier 
deployments, the “corporate tilt” towards a particular supplier 
does not carry the same weight as at the enterprise level.
VARs Rule.    The technology and features offered by different 
vendors always drive DBMS deployment strategies and product 
selection.    However, Aberdeen believes that a defining success 
factor in 1998 will be a vendor’s ability to support packaged and 
pre-fabricated application development and deployment, via Value-
Added Reseller (VAR) and Independent Software Vendor (ISV) 
relationships in all segments and effective service offerings.    
Although such packaged applications do not yet represent the bulk 
of all enterprise applications, they are determining new enterprise 
DBMS deployments and are the primary means by which new 
DBMS licenses will be sold in many high-growth market segments. 
To be sure, companies will continue to make “architectural” 
database purchases, but in light of a host of factors, including the 
lack of significant new database technologies, the growth of such 
approaches will be slow.      The most successful DBMS vendors will 
make their products more customizable for packaged application 
vendors, such as Enterprise Resource Planning (ERP) and Customer 
Data Management Practice Summary
AberdeenGroup 27
Interaction Software (CIS) vendors, and let the needs of such 
companies more fully influence new feature development. 
User Success Factors
Certain “standard” factors, including scalability, replication and 
interoperability, will be even more important during 1998 for IS 
organizations selecting and deploying DBMSs.    However, these 
professionals should view database decisions more from a task-
specific perspective then they have in the past.
For example, if IS is evaluating a new enterprise packaged 
application, it will rate potential DBMSs to a significant degree 
based on how well such products support a specific application, 
including performance, programmability, and required 
maintenance.    Companies are buying packaged applications 
especially because they save time (both personnel time and project 
lifecycle) and money, and they are increasingly searching for 
DBMSs that reflect these same priorities.    DBMS vendors 
increasingly are providing benchmarks demonstrating application-
specific performance.    Aberdeen notes that the growth of 
packaged application vendors, VARs and ISVs means that even 
more than in the past they are helping companies select DBMS 
systems or are selecting them entirely. 
Many new DBMS deployments will accompany multi-tier Web 
application development projects.    Users in such situations will 
look for DBMSs with object — especially Java — capabilities, 
excellent open communication features, and robust scalability to 
handle “bursty” traffic loads typical of universally accessible 
applications. 
Data Management Practice Summary
AberdeenGroup 28
Chapter Five
Supplier Abstracts
This chapter lists names, addresses, and in some cases short 
assessments of suppliers in four major strategic-DBMS categories:

Relational and Object/Relational DBMS suppliers;

Object DBMS suppliers;

Embedded DBMS suppliers; and

Suppliers of small-footprint, highly-distributed DBMSs for Thin 
Clients and Portable Devices.
Relational and Object/Relational DBMS Suppliers
Oracle Corporation
500 Oracle Parkway
Redwood Shores, CA    94065
(650) 506-7000
www.oracle.com
Products:    Oracle8.    Enterprise object/relational DBMS
Market Position
One of the original RDBMS vendors targeting mid-range servers, 
Oracle achieves its market leadership by riding the growth of the 
client/server application model and also by offering excellent 
features across an exceptionally wide range of platforms, backed 
by a substantial in-house services operation.    Oracle’s strategy 
directly targets large enterprises that have a greatly varied mix of 
platforms and application needs, such that they would benefit from 
adhering to one “standard” DBMS that runs on all their platforms. 
The company’s flagship DBMS, Oracle8, leads the DBMS market 
with projected 1998 license revenues of approximately $2 billion, 
and is becoming the de facto standard DBMS on Unix servers.    
Oracle8 is an extremely comprehensive package that addresses at 
least competently all major enterprise DBMS criteria — scalability 
(especially via new parallel processing technologies), flexibility 
Data Management Practice Summary
AberdeenGroup 29
(including new object and complex data type support), distributed 
technology, new-technology support, and programmer productivity. 
Aberdeen Conclusions
Oracle will continue to dominate the profitable, but less quickly 
growing and increasingly commoditized enterprise Unix DBMS 
market segment. Oracle is having to alter its traditional and 
aggressive direct sales strategy to support the VARs, ISVs, and 
package application vendors critical to the new DBMS marketplace. 
Consistent with its traditional “run everywhere” philosophy, Oracle 
is active in almost every new significant market segment, and 
needs to do so to sustain traditionally high growth rates.    As a core 
part of Oracle’s Network Computing Architecture, Oracle8 
specifically supports the development of Web-based multi-tier 
applications and is positioned quite well as a back end to data-
driven Web sites and programs.    Oracle8 has sold reasonably well 
on the Windows NT platform and should retain a significant share 
of the NT-dominated workgroup and small-to-mid-sized business 
markets.    Given its size, success and deep pockets, Oracle has the 
ability to be a major player in the new DBMS segments, and will be 
extremely competitive in 1998. 
Informix Software, Inc.
4100 Bohannon Drive
Menlo Park, CA 94025 USA
(650) 926-6300
www.informix.com
Products:    Informix Dynamic Server 7.3.    Very scalable and high-
performance object-relational DBMS.
Market Position
Informix has a well-deserved reputation as a technology leader, a 
double-edged sword that in the past has produced both success and 
failure for the company.    Informix Dynamic Server 7.3 is the 
company’s core DBMS and is built upon a very scalable 
architecture in which every major function and task exploits 
parallel processing.    Under the revamped product line launched in 
the fall of 1997, the core Informix Dynamic Server actually is a 
relational DBMS that provides a good range of basic features and 
excellent performance for OLTP, decision support, and general data 
management applications.    Users can buy optional configuration 
Data Management Practice Summary
AberdeenGroup 30
packages that provide additional features and support specifically 
for data-driven Internet content and application development, 
advanced decision support/OLAP, high-end OLTP, and user-defined 
data types. Informix consistently posts impressive performance 
numbers for both OLTP and decision support applications.
After restating and lowering revenues in 1997, Informix has 
refocused its business strategy and is targeting four key market 
segments:    high-performance OLTP, data warehousing/business 
intelligence, Web/content management, and distributed enterprise 
computing.    Traditionally a company that partners well with ISVs 
and developers, Informix is pushing hard to develop successful 
relationships with major enterprise packaged applications vendors 
including Baan, SAP and Peoplesoft.    Informix’s excellent user-
defined data type architecture and corresponding customizability 
appeal to packaged application developers seeking advanced 
ORDBMS functionality.
Aberdeen Conclusions
Informix has made great strides during the past six months 
towards addressing its financial and product problems, and is 
positioned to at least compete in its targeted market segments.    
The Web content/develop-ment segment poses some obstacles for 
Informix, given that this segment is being driven by middleware 
and tools, rather than DBMS technologies.    Additionally, Informix 
will struggle where the market becomes commoditized — for 
example, in much of the Windows NT DBMS marketplace.    
However, the company’s innovative DataBlade object-relational 
and other technologies and excellent performance will enable it to 
capture and keep a healthy chunk of the high-end OLTP, business 
intelligence, and even ERP markets, and to compete effectively 
within the Web content/development segment. 
Sybase, Inc.
6475 Christie Avenue
Emeryville, CA    94608
(800) 879-2273
www.sybase.com
Data Management Practice Summary
AberdeenGroup 31
Products:    Sybase Adaptive Server family, which includes 
Adaptive Server Enterprise 11.5, Adaptive Server IQ 11.5 for data 
warehousing, and Adaptive Server Anywhere for mobile and 
occasionally-connected deployments.
Market Position
Adaptive Server is a powerful RDBMS distinguished most by its 
integration with other Sybase DBMS products (middleware and 
development tools).    It is especially well suited for multi-tier, 
distributed Web application development, decision-support, and 
application integration.    Adaptive Server Enterprise offers good 
uniprocessor performance and increasingly solid multi-processor 
performance, but still is trying to shake a market perception that it 
doesn’t scale horizontally as well as some competitors.    However, 
the combination of Adaptive Server Enterprise and Adaptive 
Server IQ provides an excellent foundation for data warehousing 
applications.
The Adaptive Server family offers perhaps the best vertical 
scalability of the leading DBMS vendors, by enabling developers to 
write one application that can run virtually unchanged on DBMSs 
at the enterprise, workgroup, desktop and mobile computer level.    
The combination of Adaptive Server with Powersoft development 
tools and application servers (i.e., Jaguar CTS, PowerDynamo) and 
with successful Sybase connectivity and data distribution 
middleware serves as an effective platform for creating 
component-based, distributed applications.    Adaptive Server does 
not currently support objects or user-defined data types; it defers 
such capabilities to other specific servers.    Aberdeen does expect 
Adaptive Server to support Java in the near future, however. 
Aberdeen Conclusions
Adaptive Server is a good product that nonetheless is suffering 
because of marketplace dynamics.    Sybase’s strategy of 
distinguishing its DBMS by leveraging its more successful tools, 
middleware and mobile/embedded products is a smart, customer-
oriented move that may keep the DBMS competitive.    Aberdeen 
believes that Sybase will continue to have a tough time building its 
market share in the enterprise DBMS market segment, and that the 
company’s fortunes during the year will largely be driven by its 
mobile-user database and development products. 
IBM Corporation
Data Management Practice Summary
AberdeenGroup 32
Armonk, NY
(800) 426-2968
www.ibm.com
Products:    DB2 Universal Database Version 5.0, a feature-rich 
and very scalable Object-Relational DBMS.
Market Position
In Version 5.0 of DB2, IBM has combined previously separate 
parallel-scalable and replication products with its core ORDBMS to 
create an extremely competitive product that, indeed, tries to be 
“universal.”    Although the vast majority of IBM DBMS sales, 
including DB2, VSAM and IMS, are for mainframe systems, the DB2 
Universal Database has given IBM a foothold on Unix and even 
Windows NT.    DB2 now offers very strong capabilities in almost all 
functional areas: it scales and performs quite well, is very reliable, 
and, through its “Extender” technology, effectively accommodates 
complex and user-defined data types.    In Version 5.0, IBM 
addressed a previous weakness by rebuilding its management 
utilities and making them easier to use.    DB2’s distributed data 
technologies, which now include the Data Joiner and Data 
Propagator technologies, are a strength.    DB2 also is benefiting 
from IBM’s commitment to Internet technologies and Java; the 
product integrates support for these technologies. 
IBM is implementing high-profile initiatives in the business 
intelligence, electronic commerce and content management areas, 
with DB2 as a key component. IBM is also is leveraging its 
traditional strengths in bundling and selling enterprise hardware 
and software and its strong relationships with VARs in selling DB2. 
Aberdeen Conclusions
IBM’s enterprise market penetration and successful general 
product strategies should help DB2 expand its overall market 
share, particularly on IBM servers.    Aberdeen believes that IBM 
will emerge as a market leader in the business intelligence and 
electronic commerce segments, but will struggle to beat Oracle and 
Microsoft in the mainstream, increasingly packaged-application-
driven Unix and NT markets.
Microsoft Corporation
One Microsoft Way
Redmond, WA    98052-6399
(425) 882-8080
Data Management Practice Summary
AberdeenGroup 33
www.microsoft.com
Products:    SQL Server 6.5, a good, all-around relational DBMS 
offering tremendous price/performance for lower scale 
operations.
Market Position
Microsoft originally licensed the SQL Server code from Sybase, but 
during the past few years has reworked most of the system’s core, 
gradually added new features and capabilities, and developed and 
marketed it into a DBMS powerhouse. SQL Server has been 
achieving annual revenue growth rates of over 50% and is among 
the largest DBMSs in unit sales, thanks partly to being bundled 
with the Microsoft Back Office server software suite. These 
numbers reflect the highly aggressive pricing and ubiquitous 
distribution that are Microsoft marketing trademarks. 
Although it is facing Windows NT competition from Oracle, 
Microsoft continues to build its majority share of the Windows NT 
DBMS market and, correspondingly, of the workgroup, 
departmental, and portions of the Small-to-Mid-Size Business 
markets. Although SQL Server has lacked certain critical enterprise 
DBMS features, such as row-level locking and object/complex data 
support, this simply reflects the fact that such capabilities are not 
as important at the lower-end market segments as 
price/performance.    And price/performance on Windows NT is 
where Microsoft dominates, leveraging its tight integration with 
the operating system.    Although Microsoft wants SQL Server to 
accompany Windows NT server as it continues to penetrate into 
the enterprise, at the moment it remains, like Windows NT itself, a 
DBMS for departments and workgroups.    On four-processor 
servers, SQL Server delivers tremendous relative performance, but 
it remains limited by the four-to-eight processor limitations of 
Windows NT itself. 
SQL Server 7.0, due in the second half of 1998, will offer new 
scalability and replication capabilities, performance optimization, 
and support for data warehousing and advanced decision support 
applications.    Release 7.0 also will bolster SQL Server’s robustness, 
add row-level locking, and greatly simplify and automate data 
management functions.
Aberdeen Conclusions
SQL Server Release 7.0 may be the biggest DBMS story of 1998.    It 
could cement Microsoft’s lead in the Windows NT DBMS market 
Data Management Practice Summary
AberdeenGroup 34
and extend the reach of its volume product strategy further into 
the enterprise and into the business intelligence market segment.    
Microsoft’s challenges primarily involve the scalability of Windows 
NT platform itself and the company’s ability to sell at the enterprise 
level, in the past a more service-oriented effort than Microsoft’s 
traditional product volume strategy. 
Computer Associates
One Computer Associates Plaza
Islandia, New York    11788-7000
(800) CALL-CAI
www.cai.com
Products:    Ingres/DBMS, a competitive relational DBMS with 
particularly good distributed database technology.
Market Position
Ingres/DBMS, previously called, “OpenIngres 2.0,” is the relational 
half of Computer Associates’ DBMS strategy; its counterpart is the 
new “pure object” DBMS Jasmine (see “Object DBMS Suppliers”).    
Ingres/DBMS is a solid, if not high-profile RDBMS that 
predominantly sells on mid-range Unix servers. Ingres/DBMS 
provides excellent replication and distributed administration tools 
and includes a good query optimizer.    The last major release of the 
product, in mid-1997, bolstered Ingres/DBMS’s parallel-scalable and 
reliability features.    Ingres/DBMS thus effectively supports 
distributed OLTP, decision support, and mobile applications. 
Ingres/DBMS is now a cornerstone of Computer Associates’ Ingres 
II product family, an open set of development, database, and 
connectivity tools that seeks to offer companies both specific 
products and a roadmap for integrating enterprise applications.    
Computer Associates thus is appealing to companies that view 
database decisions from a broader strategic, versus specific 
product, perspective.    Ingres/DBMS benefits from Computer 
Associates’ OpenRoad development toolset (also part of the Ingres 
II family) and Unicenter systems management software.    
Ingres/DBMS (and the Ingres II family), Jasmine and other 
Computer Associates products will be integrated within the 
forthcoming Harmony initiative, which broadly addresses 
enterprise information management needs. 
Data Management Practice Summary
AberdeenGroup 35
Aberdeen Conclusions
1998 is a critical year for Ingres/DBMS, given tremendously 
increased competition in this DBMS’s traditional OLTP and 
decision-support markets.    Synergy with Jasmine and the Ingres II 
and Harmony initiatives will help, but Computer Associates will 
need to aggressively push new features and positioning to 
maintain Ingres/DBMS’s market share.    While Jasmine is off to a 
good start, Computer Associates is ahead of the mass information 
technology marketplace, and thus the company can’t yet bank on 
the ODBMS as a major revenue source. 
Progress Software
14 Oak Park
Bedford, MA    01730
(617) 280-4000
www.progress.com
Products:    Progress Enterprise Server and Progress Workgroup 
Server. 
Market Position
Although not a market leader, Progress has succeeded by selling a 
reliable and reasonably robust and well-performing DBMS that 
minimizes the resources needed for installation and 
administration.    At the same time, Progress leverages its fine 
Apptivity and other development tools to sell the DBMS.    The 
result is a cost-effective package for Small-to-Mid-sized Businesses 
(SMBs), which Progress generally reaches indirectly, through a 
strong network of VARs and ISVs. 
Aberdeen Conclusions
The smallest of the major RDBMS vendors, Progress has more in 
common with vendors emphasizing indirect sales channels and 
targeting the embedded DBMS market.    In many instances, the 
DBMS will be a follow-up sell to customers of the Progress 
development tools. 
Object DBMS Suppliers
Computer Associates
Data Management Practice Summary
AberdeenGroup 36
One Computer Associates Plaza
Islandia, New York    11788-7000
(800) CALL-CAI
www.cai.com
Product:    CA-Jasmine.    A pure object DBMS that includes a 
sophisticated visual development environment (Jasmine Studio).
The first enterprise ODBMS from a major database vendor, Jasmine 
is a powerful package that Computer Associates has aggressively 
launched and priced. It has excellent general-purpose ODBMS 
capabilities and scales exceptionally well for an ODBMS. Jasmine 
thus is effective for a range of complex data applications, although 
Computer Associates has been stressing its role as a DBMS in 
object-rich multimedia and Internet/Intranet applications.    With 
Jasmine, Computer Associates shrewdly appeals to major 
enterprises with RDBMSs that haven’t or won’t bank on hybrid 
Object-Relational DBMSs. 
Object Design, Inc.
25 Mall Road
Burlington, MA    01803
(781) 674-5000
www.odi.com
Product:    Enterprise Edition.
ObjectStore is a pure object DBMS designed to support workgroup 
and enterprise applications.    A revenue leader in the ODBMS 
market, ObjectStore is demonstrating that object databases can 
scale quite well and has established a good niche in information-
intensive industries like telecommunications, finance and 
healthcare that need to accommodate complex data and processes. 
ObjectStore’s extensive support for distributed object standards 
enables it to fit nicely in multi-tier application environments. 
Versant Object Technology Corporation
6539 Dumbarton Circle
Fremont, CA    94555
(510) 789-1500
www.versant.com
Data Management Practice Summary
AberdeenGroup 37
Product: Versant ODBM Release 5.
Versant ODBM Release 5 targets enterprise-level applications, 
especially in information-intensive vertical markets.    Versant has 
been especially successful in the telecommunications market, 
where it frequently is used to support network switching 
applications.    Like other enterprise ODBMSs, Versant is leveraging 
natural support for Java and distributed objects to penetrate the 
market for component-based, multi-tier application development. 
InterSystems Corporation
One Memorial Drive
Cambridge, MA    02142
(617) 621-0600
www.intersys.com
Product: Cache
InterSystems’ Cache is a very robust, object DBMS that integrates at 
the table/class level object and SQL data management technologies. 
Cache thus seeks to provide the strengths of both methods while 
minimizing their weaknesses, specifically offering optimized 
performance for complex transaction processing.
Ardent Software, Inc.
50 Washington Street
Westboro, Mass. 01581-1021
(508) 366-3888
www.ardentsoftware.com
Product:    O2 ODBMS.
O2 ODBMS is a leading enterprise object database that has 
demonstrated performance on databases above 100 gigabytes.    
Note that O2 ODBMS was originally created by O2 Technology; after 
a series of quick mergers and acquisitions, the product now is 
owned and sold by Ardent Software. 
POET Software
999 Baker Way, Suite 100
San Mateo, CA    94404
(415) 286-4640
Data Management Practice Summary
AberdeenGroup 38
www.poet.com
Product:    Poet 5.0 Object Server Suite.
The company has aggressively positioned itself on Windows NT 
and adopted Microsoft technologies.    Further, it has specifically 
targeted the content management (via XML support) and object-
oriented application development markets, where object database 
capabilities can be especially appealing. 
GemStone Systems, Inc.
20575 N.W. von Neumann Drive
Beaverton, OR    97006
(503) 533-3000
www.gemstone.com
Product:    GemStone 5.0.
GemStone 5.0 object application server is a hybrid between an 
object database and a Java application server.    Part of GemStone’s 
GemStone for Java family, the server specifically supports the 
development and deployment of distributed, scalable, and multi-
tier Java applications. 
Objectivity, Inc.
301B East Evelyn Avenue
Mountain View, CA    94041-1530
(415) 254-7100
www.objectivity.com
Product:    Objectivity 5.0.
Objectivity Version 5.0 is a robust and multi-threaded object 
database that stresses support for Java, C++, and other object and 
Web technologies. 
Data Management Practice Summary
AberdeenGroup 39
Embedded DBMS Suppliers
Pervasive Software, Inc.
8834 Capital of Texas Highway
Austin, TX    78759
(512) 794-1719
www.pervasive-sw.com
Product: Pervasive.SQL.
Pervasive.SQL is a hybrid DBMS that integrates two established and 
successful products, the Btrieve transactional database engine and 
the Scalable.SQL Relational DBMS.    The result is a DBMS ideal for 
small-to-mid-size business applications that enables developers to 
optimally mix transactional and query activities within one 
application.
Centura Software Corporation
975 Island Drive
Redwood Shores, CA    94065
(800) 444-8782
www.centurasoft.com
Product: SQLBase 7.0.
Centura is a once-hot client/server development tools company that 
made some costly, failed business decisions in recent years.    The 
company has begun to turn itself and is refocusing its business on 
its relational DBMS and the embedded database market.    Centura 
has technology and tools well suited for the embedded DBMS 
market and is pushing hard to expand its offerings for the mobile 
and occasionally-connected user market segments.
InterBase Software Corporation
1800 Green Hills Road, Suite 150
Scotts Valley, CA    95066-4928
(408) 430-1500
www.interbase.com
Product: InterBase 5.0.
Data Management Practice Summary
AberdeenGroup 40
InterBase 5.0 is a relational DBMS offering scalability and several 
high-end features unusual for an embedded database targeting 
small-to-mid-sized businesses and departments.    A spin-off of 
Borland International, InterBase retains access to its parent’s 
developer installed base. 
Extended Systems, Inc.
5777 N. Meeker Avenue
Boise, ID    83713
(208) 322-7575
www.advantagedatabase.com
Product: Advantage Database Server 5.0.
Advantage Database Server 5.0 is a flat file database specifically 
designed for high performance and for the Small to Mid-sized 
Business (SMB) embedded database market.    It has a strong 
installed base among developers using Borland’s Delphi 
development environment — who want the performance and like 
the access programming options Advantage’s database provides.
Small-Footprint, Highly-Distributed DBMS Suppliers 
(for thin clients and portable devices)
Sybase, Inc.
6475 Christie Avenue
Emeryville, CA    94608
(800) 879-2273
www.sybase.com
Product:    Sybase Adaptive Server Anywhere; Adaptive Server for 
Windows CE; Ultralight.
Oracle Corporation
500 Oracle Parkway
Redwood Shores, CA    94065
(650) 506-7000
www.oracle.com
Product:    Oracle Lite 3.0, Oracle Lite for Windows CE. 
Data Management Practice Summary
AberdeenGroup 41
Cloudscape, Inc.
180 Grand Avenue
Suite 300
Oakland, CA    94612
(510) 873-0900
www.cloudscape.com
Product:    JBMS 1.0.
Object Design, Inc.
25 Mall Road
Burlington, MA    01803
(781) 674-5000
www.odi.com
Product:    ObjectStore PSE Pro 2.0.
Centura Software Corporation
975 Island Drive
Redwood Shores, CA    94065
(800) 444-8782
www.centurasoft.com
Product:    SQLBase 7.0 Light.
Computer Associates
One Computer Associates Plaza
Islandia, New York    11788-7000
(800) CALL-CAI
www.cai.com
Product:    CA Ingres/DBMS Desktop.


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | dbmspr~1-7c854e |
| title | Data Management: 1998 Practice Summary |
| author | Aberdeen Group |
| date | 1998-05-01 |
| type | other-research |
| subject_domain | data-management |
| methodology | industry-analysis, market-overview |
| source_file | DBMSPR~1.DOC |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group's 1998 practice summary on the Database Management Systems (DBMS) market, covering relational, object-relational, object, embedded, and mobile DBMS categories. The report surveys major vendors including Oracle, IBM, Informix, Sybase, Microsoft, and Computer Associates, assesses turbulent 1997 market dynamics including revenue stagnation among major vendors, and forecasts the impact of Windows NT, packaged applications, commoditization, and Internet technologies on DBMS market segmentation. Aberdeen predicts continued Oracle dominance on Unix, Microsoft SQL Server growth on NT, and emerging opportunities in business intelligence, mobile user, and Web content management segments.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Comprehensive 1998 snapshot of the DBMS market at a pivotal inflection point when Oracle, Informix, and Sybase faced revenue pressure and Microsoft SQL Server began its ascent; catalogs 25+ vendors across RDBMS, ORDBMS, ODBMS, embedded, and mobile categories. |
| **Relevance** | high | DBMS market structure and vendor dynamics documented here directly predict the Oracle-Microsoft duopoly that emerged; ORDBMS adoption trajectory, commoditization forces, and mobile database emergence all remain directly relevant to understanding modern cloud database market structure. |
| **Prescience** | high | Aberdeen's Oracle/Unix dominance prediction proved accurate; SQL Server 7.0 enterprise push prediction proved accurate; commoditization forecast proved correct; ORDBMS dominance over pure ODBMS proved correct; mobile/embedded DBMS growth as niche proved accurate. |

### Prescience Detail


**Prediction 1:** Oracle Unix enterprise market outlook
- **Claimed:** Will continue to dominate Unix enterprise but face commoditization pressure
- **Year:** 1998
- **Confidence at time:** high

**Prediction 2:** SQL Server 7.0 significance
- **Claimed:** May be the biggest DBMS story of 1998
- **Year:** 1998
- **Confidence at time:** high

**Prediction 3:** Informix competitive outlook
- **Claimed:** Can capture high-end OLTP/BI/ERP but will struggle in commoditized NT segments
- **Year:** 1998
- **Confidence at time:** high

**Prediction 4:** Windows NT enterprise scalability forecast
- **Claimed:** NT should scale sufficiently for many enterprise production apps within 2-3 years
- **Year:** 1998
- **Confidence at time:** high

**Prediction 5:** Java DBMS support status
- **Claimed:** Java support has become a required DBMS capability
- **Year:** 1998
- **Confidence at time:** high

**Prediction 6:** Future DBMS market consolidation
- **Claimed:** Aberdeen does NOT expect near-term consolidation among major vendors; expects major vendors to buy small start-ups
- **Year:** 1998
- **Confidence at time:** high

**Prediction 7:** Pure ODBMS market outlook
- **Claimed:** Will lead in niche segments including component-based app development; remain minor player in mainstream
- **Year:** 1998
- **Confidence at time:** high


### Entities Referenced (23)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | acquired | Aberdeen/Harte-Hanks |
| Oracle Corporation | company | active |  |
| IBM Corporation | company | active |  |
| Informix Software Inc. | company | dissolved | unknown |
| Sybase Inc. | company | dissolved | unknown |
| Microsoft Corporation | company | active |  |
| Computer Associates | company | dissolved | unknown |
| Progress Software | company | active |  |
| Object Design Inc. | company | dissolved | unknown |
| Versant Object Technology Corporation | company | dissolved | unknown |
| InterSystems Corporation | company | active |  |
| Ardent Software Inc. | company | dissolved | unknown |
| POET Software | company | dissolved | unknown |
| GemStone Systems Inc. | company | dissolved | unknown |
| Objectivity Inc. | company | unknown | unknown |
| Pervasive Software Inc. | company | dissolved | unknown |
| Centura Software Corporation | company | dissolved | unknown |
| InterBase Software Corporation | company | dissolved | unknown |
| Extended Systems Inc. | company | dissolved | unknown |
| Cloudscape Inc. | company | dissolved | unknown |
| Baan | company | dissolved | unknown |
| SAP | company | active |  |
| PeopleSoft | company | dissolved | unknown |

### Technologies Referenced (22)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Relational DBMS (RDBMS) | application | Various | mature | dominant |
| Object-Relational DBMS (ORDBMS) | application | Oracle, IBM, Informix | growing | dominant |
| Object DBMS (ODBMS) | application | Various (CA, ODI, Versant) | niche | niche |
| Oracle8 | application | Oracle | growing | legacy |
| Informix Dynamic Server 7.3 | application | Informix | growing | legacy |
| Sybase Adaptive Server Enterprise 11.5 | application | Sybase | growing | legacy |
| Sybase Adaptive Server IQ 11.5 | application | Sybase | growing | legacy |
| Sybase Adaptive Server Anywhere | application | Sybase | growing | legacy |
| Microsoft SQL Server 6.5 | application | Microsoft | growing | dominant |
| Microsoft SQL Server 7.0 | application | Microsoft | pre-release | legacy |
| IBM DB2 Universal Database Version 5.0 | application | IBM | growing | legacy |
| CA Ingres/DBMS (formerly OpenIngres) | application | Computer Associates | mature | legacy |
| CA-Jasmine | application | Computer Associates | emerging | legacy |
| Pervasive.SQL | application | Pervasive Software | growing | legacy |
| Oracle Lite | application | Oracle | growing | legacy |
| Windows NT | platform | Microsoft | growing | legacy |
| Java DBMS Support / JDBC | framework | Various | emerging | dominant |
| Online Transaction Processing (OLTP) | application | Various | mature | mature |
| Data Warehousing / Business Intelligence | application | Various | growing | dominant |
| IBM IMS (Hierarchical DBMS) | application | IBM | mature | legacy |
| IBM Mainframe File Management (VSAM/ISAM/CICS-Fastpath) | application | IBM | mature | legacy |
| Palm Computing Device (PDA) | platform | 3Com | growing | legacy |

### Observation Summary

- Total observations: 30
- By type: market-assessment: 14, competitive-assessment: 8, viability-prediction: 7, expert-opinion: 1
