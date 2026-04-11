# Middleware Technology: 1998 Practice Summary

> Archived from: MIDDLE~1.DOC
> Original publication date: 1998-05-01
> Author: Aberdeen Group

---

## Original Document Text

AberdeenGro
up
Middleware
Technology:
1998 
Practice 
Summary
May 1998
Aberdeen Group, Inc.
One Boston Place
Boston, Massachusetts 02108 
USA
Middleware Technology Practice Summary
AberdeenGroup 
Telephone: 617 723 7890
Fax: 617 723 7897
www.aberdeen.com
2
Middleware Technology Practice Summary
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
Middleware Technology Practice Summary
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
Middleware Technology Practice Summary
AberdeenGroup 
TABLE OF CONTENTS
Middleware Technology Practice ..................................................v
Description, Focus and Benefits.............................................................v
Strategic Market Questions.....................................................................v
Executive Summary.........................................................................1
Key Aberdeen Findings............................................................................1
Summary of Findings......................................................................3
Middleware Defined........................................................................5
How Middleware Fits into Network Services.......................................5
Core Middleware Components................................................................6
Gateways...............................................................................................................................6
Transaction Processing Monitors..................................................................................6
Remote Procedure Calls (RPC)........................................................................................7
Messaging.............................................................................................................................7
Request-Reply and Push Technology...........................................................................7
Object Request Brokers (ORB)........................................................................................8
Data Access...........................................................................................................................8
Application Integration....................................................................................................8
Application Servers...........................................................................................................9
How An Integrated Middleware Solution Works.................................9
Issues and Challenges...................................................................11
Impact of Major IT Trends.....................................................................11
Supplier Success Factors........................................................................12
User Success Factors...............................................................................12
Supplier Abstracts.........................................................................14
Active Software.......................................................................................14
BEA Systems, Inc.....................................................................................15
Borland International Inc., (soon to be Inprise)................................16
CrossWorlds Software............................................................................16
EXPERSOFT Corporation........................................................................17
IBM Corporation......................................................................................18
5
Middleware Technology Practice Summary
AberdeenGroup 
Insession, Inc...........................................................................................19
Microsoft Corporation...........................................................................20
New Era of Networks, Inc. (NEON).......................................................21
RELIANT Data Systems...........................................................................21
SmartDB Corporation.............................................................................22
TIBCO Software Inc.................................................................................23
Oracle Corporation.................................................................................24
Sybase, Inc................................................................................................24
6
Middleware Technology Practice Summary
AberdeenGroup 
Preface
Middleware Technology Practice 
Description, Focus and Benefits
Middleware is "mid-level" software — software above the 
operating system or communications protocol and below 
applications software — that allows other software to 
communicate and interoperate.  Today’s middleware product types 
include gateways, TP monitors, Remote Procedure Calls (RPCs) 
commercial messaging and Object Request Brokers (ORBs).
Middleware is hot: the outcome of middleware standards wars 
such as CORBA versus DCOM are crucial to ISV strategies.  
Suppliers and IS increasingly view middleware as a key component 
of an overall enterprise architecture because of its ability to "glue 
together" enterprise applications and extend their scope to new 
platforms and multi-tier architectures.
Middleware can deliver major scalability benefits by optimizing 
client-server and server-server communications as well as 
reducing server overhead.  These scalability benefits are often vital 
to the long-term success of Internet architectures.  Middleware 
provides greater robustness by spreading applications across 
clients and servers and allowing failover when parts of the 
network fail.  Middleware improves programmer productivity and 
simplifies administration by allowing location, RDBMS, application, 
hardware, and communications-protocol independence.  Open 
middleware’s ability to incorporate new technologies such as 
distributed objects and the Internet gives users far greater 
flexibility, reducing the costs of change.
Middleware is an integral component of the Network Services 
Practice — effective middleware is now vital to supporting today’s 
myriad of applications, systems software, and hardware from 
many suppliers across a complex enterprise network.  Middleware 
is also key to scaling an enterprise network and adapting it to new 
technologies.
Strategic Market Questions
7
Middleware Technology Practice Summary
AberdeenGroup 

Which suppliers will put together a fully scalable Internet 
middleware solution first— BEA Systems, Microsoft, 
Visigenic/Borland, or IBM? 

Who will win the ORB wars? DCOM or CORBA? How can 
suppliers and IS buyers hedge their bets? 

How should the IS buyer fit together point middleware 
products such as push technology, messaging, ORBs, and 
gateways for an effective long-term middleware strategy? 

Will Microsoft and IBM’s messaging solutions be compatible? 

Who has the best Web application and transaction servers? 
 This Aberdeen Group Practice Summary is a deliverable in a 
comprehensive service that includes Aberdeen published research 
and customize professional services aimed at executives who must 
make strategic business decisions regarding Information 
Technology.
8
Middleware Technology Practice Summary
AberdeenGroup 
Chapter One
Executive Summary
Middleware is “mid-level” software — software above the 
operating system or communications protocol and below 
applications software — that allows other software to 
communicate and interoperate.    Today’s middleware product 
types include gateways, Transaction Processing monitors, Remote 
Procedure Calls (RPCs), commercial messaging, request/reply and 
push technology, Object Request Brokers (ORBs), data access tools, 
Enterprise Application Integration solutions (EAI) and Application 
Servers.
While middleware has traditionally been difficult to establish as a 
major market, suppliers and Information Systems (IS) managers 
are increasingly viewing middleware as a key component of an 
overall enterprise architecture because of its ability to “glue 
together” enterprise applications and extend their scope to new 
platforms and multi-tier architectures.    There are tangible 
economic benefits when IS “buys” middleware rather than building 
it.
Trends taking place in networking, Internet and object 
technologies are forcing IS to reconsider the way in which they 
build, buy and deploy information systems.    Today’s middleware 
has become increasingly broad with respect to the various 
platforms that must be supported and the functionality required; it 
has become increasingly integrated and increasingly important.    
Middleware used to be viewed as the “plumbing” infrastructure 
decision that no one wanted to be bothered with.    Now 
middleware is a strategic business decision in many organizations.
Key Aberdeen Findings

IS needs middleware tools that support a wide variety of 
applications, platforms and hardware requirements out 
of the box.

A middleware architecture/solution does better in real-
world situations than today’s point products.
1
Middleware Technology Practice Summary
AberdeenGroup 

Over the next 1-1 ½ years, EAI middleware will be crucial 
to the effective use of enterprise critical packaged 
applications such as SAP R/3.
Middleware can deliver major scalability benefits by optimizing 
client-server and server-server communications as well as by 
reducing server overhead.    These scalability benefits are often 
vital to the long-term success of Internet architectures.    
Middleware provides greater robustness by spreading applications 
across clients and servers and allowing failover when parts of the 
network fail.    Middleware improves programmer productivity and 
simplifies administration by allowing location, RDBMS, application, 
hardware, and communications-protocol independence.    Open 
middleware’s ability to incorporate new technologies such as 
distributed objects and the Internet gives users far greater 
flexibility, reducing the costs of change.
This practice summary is intended for an audience of corporate 
managers responsible for planning and managing initiatives for 
integrating applications, and extending applications to new 
platforms and multi-tier architectures.
2
Middleware Technology Practice Summary
AberdeenGroup 
Chapter Two
Summary of Findings
Today’s competitive pressures are driving enterprises to build and 
develop their applications in a well-timed manner.    These 
applications must closely match business strategies and processes 
— requiring that development of new systems and applications, 
and especially for the Internet, be designed in sync with evolving 
business processes.    Aberdeen research shows that middleware 
such as application-to-application communications can play a 
critical role in delivering enterprise architecture scalability, 
flexibility and cost-effectiveness — but today is increasingly a 
technological bottleneck.    It is especially a problem in the key 
areas of Internet development and complex-data support.
The need for “universal middleware” has also become a critical 
business challenge.    For example, information needed by 
customers may be housed in incompatible formats on multiple 
hosts; users increasingly need to connect customers with the 
information they require; and integrating heterogeneous 
computing and networking environments is becoming vital to an 
organization’s IS infrastructure (see Figure 1).
Figure 1:    Market Drivers for Middleware
3
Middleware Technology Practice Summary
AberdeenGroup 
Source:    AberdeenGroup, April 1998
Other Aberdeen Findings

Middleware becomes vital to IS especially when the 
integration of existing systems and applications is 
required; new applications/systems must be developed; 
information must be delivered reliably; or flexibility is 
key to long term success.

The middleware market is growing fast, especially 
because of enterprises strategically using the Internet.    
The market should continue to grow and reach about $6 
billion by the year 2000.

Enterprise middleware initiatives that involve integrating 
many sources and targets, while maintaining 
independently coded modules for each integration 
process, is extremely resource intensive.    Using a single, 
flexible and consistent middleware framework for each 
process will greatly reduce the amount of personnel 
resources needed to maintain and develop the system.

Throughout 1997 the middleware market underwent 
some consolidation (e.g., BEA/Digital, Visigenic/Borland).    
Aberdeen believes that consolidation will continue to 
occur, since the ideal middleware solution is a 
combination of middleware technologies (e.g., messaging, 
ORBs, TP monitors).

No one supplier has developed/marketed a completely 
integrated middleware solution.
4
Middleware Technology Practice Summary
AberdeenGroup 

Mid-level IS managers typically make the middleware 
buying decision today.    The buying criteria used by many 
user organizations include reliability, flexibility, 
guaranteed delivery, transactional performance, and the 
ability to connect disparate applications.

Suppliers are differentiating themselves from their rivals 
by providing solutions that incorporate a particular 
combination of middleware technologies (e.g., messaging 
and ORBs); delivering an open approach; or working with 
other middleware suppliers and interconnecting with 
their technologies.
5
Middleware Technology Practice Summary
AberdeenGroup 
Chapter Three
Middleware Defined
How Middleware Fits into Network Services
Middleware is the “mid-level” software, sitting above the operating 
system or communications protocol and below applications 
software, that allows other software to communicate and 
interoperate.
Today, middleware is increasingly gaining in importance and 
represents about one half of the overall application and data 
integration market, which is projected to grow from $1.3 billion in 
1997 to $8 billion in 2001 (IDC & Cowen).
While middleware has traditionally been difficult to establish as a 
major market, suppliers and IS managers are increasingly viewing 
middleware as a key component of an overall enterprise 
architecture because of its ability to “glue together” enterprise 
applications and extend their scope to new platforms and multi-
tier architectures.    In addition, middleware is viewed as strategic 
software that integrates and moves information between legacy 
applications, databases, client/server systems and the Internet.
Thus, middleware is an integral component of Network Services, 
that integration of distributed infrastructure technologies that 
allows enterprises to operate and leverage today’s complex, 
distributed business critical applications.    This is because 
middleware has the capability to support the myriad of 
applications, platforms and hardware requirements found in many 
of today’s distributed, heterogeneous computing environments (see 
Figure 2).
6
Middleware Technology Practice Summary
AberdeenGroup 
Core Middleware Components
Gateways
Gateways interconnect, and perform the appropriate conversions 
necessary between, two different networks or data management 
systems. Gateways are a mature market and when many people 
think of middleware they may think of gateways.
However, gateways may be low performance and do not always 
keep in sync with other supplier’s products.
Transaction Processing Monitors
TP Monitors handle communications multiplexing, do transaction 
routing to back-end databases and applications, and support 
distributed applications, thus helping to transfer data between 
multiple local and remote terminals or workstations and 
databases. 
Figure 2:    How Middleware Fits in Network Services
Middleware
Middleware
Security
System and
Application
Management
NOS
NETWORKING
System
Services
Network
Services
DBMS
Source:    AberdeenGroup, April 1998
Usually a TP monitor sits primarily on an application server (the 
2nd tier) or a database server (the 3rd tier) in a 3-tier architecture 
(see Figure 3 for an example of an N tier architecture).
7
Middleware Technology Practice Summary
AberdeenGroup 
TP monitors route transactions across diversified systems, provide 
load balancing and thread control to ensure performance, and 
restart systems and transactions when a failure occurs.    Because 
of this functionality, TP monitors are reliable, fast, and can 
typically handle a large number of concurrent users (hundreds to 
thousands).
Remote Procedure Calls (RPC)
The RPC product category is small and diminishing, primarily 
because this functionality is now built into most operating systems. 
RPCs are typically used in a client-server environment.    They 
provide specialized access to data or applications on a remote 
server, in a way very similar to that of a function call used to access 
a local database.    In addition, RPCs can access relational and non-
relational data within a single application, and are ideal for an 
enterprise using a two-tiered architecture.
Often RPC technology is referred to as a “point-to-point” solution.    
Many enterprises dealing in highly distributed environments or 
that have the need to access multiple data sources find RPCs less 
robust than messaging.    A drawback to RPCs is the proprietary 
nature of the programming interface — a long-term vendor lockin.
Messaging
Messaging technology supports communications between objects 
and applications by storing messages in queues until the recipient 
program is ready for them and then forwarding the messages.    
Messaging technology ensures flexible routing and guaranteed 
delivery of applications, data, or objects to multiple recipients on 
multiple platforms, regardless of system or network failures.    
Messaging technology is also a solid foundation for three-tiered 
architectures and can provide greater performance than standard 
file transfers.    Moreover, messaging technology is appropriate for 
communicating between objects because it supports an object’s 
way of intercommunicating and hides the complexity and location 
of destination objects.
However, messaging technology usually needs to be supplemented 
by software that allows developers and administrators to use it at a 
higher level, without all the interface details.
Request-Reply and Push Technology
Request-Reply technology is a typical Web mechanism — when a 
remote client requests a page, the Web server replies by sending it 
(i.e., replying).
8
Middleware Technology Practice Summary
AberdeenGroup 
Push technology by contrast “pushes” material to clients that have 
not specifically requested it, but have “subscribed” to services that 
the server has announced are available or “published” (called 
“publish-and-subscribe”).
Both technologies are particularly scalable because they can 
reduce network traffic:    clients do not need to send request 
messages and servers can bundle and target responses.    However, 
they are not widely accepted today in mainstream corporate 
enterprises as a communications solution.
Object Request Brokers (ORB)
Object request brokers (ORBs) act as a central “clearinghouse” that 
supports the interaction between objects in an application across a 
network.    Object requests are the same no matter where the 
request is from.
One of the key challenges of ORB technology has been the 
scalability issue.    Aberdeen research indicates that today’s major 
ORBs (e.g., IONA, Visigenic, ICL) by-and-large do not communicate 
with each other:    for instance, there are few ways for CORBA and 
DCOM to interoperate.    Thus, the adoption of ORB technology is 
not a priority of today’s broad IS development efforts, but rather 
for specific applications.    Broader acceptance can be found among 
independent software vendors.
Data Access
Data access technology provides the ability to translate and migrate 
data between disparate systems.    Aberdeen research indicates that 
as programming, administration and knowledge worker functions 
become increasingly distributed, IS requires cost-effective, 
reusable data-access tools.
Data access technology can be particularly effective in enterprises 
with multiple or on-going data migration needs as well as for data 
migration efforts requiring low cost or rapid implementation.    
Data access tools that provide productivity, flexibility, reusability 
and cost-effectiveness will make the IS short list for data-migration 
projects.
However, one of the major drawbacks of present data access tools 
is the lack of automation.    Many of these tools still require some 
degree of manual manipulation or customization in order for the 
solution to be fully implemented.    Most of the suppliers that 
Aberdeen covers are working toward automating more and more 
of the functionality they provide.
9
Middleware Technology Practice Summary
AberdeenGroup 
Application Integration
Today, many enterprises are implementing multiple, cross-
enterprise applications to support the full range of businesses 
processes, from sales order management to vendor-managed 
inventory.    However, business processes and best practices 
continue to rapidly evolve in ways previously not even imagined.    
Because these new processes require new or enhanced 
applications and application types, the demand to integrate all 
enterprise applications into a coherent, process-oriented whole is 
increasing.
Moreover, the pressures of a competitive marketplace are driving 
IT to implement and evolve applications in an environment of 
compressed time frames and tight budgets.    Rather than “reinvent 
the wheel”, IT is being forced to reuse previous applications more 
effectively by integrating them with each other and with new 
applications more effectively.
As a result of these two trends, Aberdeen research indicates that 
application integration projects are becoming more crucial and 
strategic ¾ involving mission critical business processes, data 
warehousing, and Year 2000 conversions.    To meet the application 
integration need, IT is looking for application integration solutions 
based on a flexible and reusable architecture rather than a one-
time, per-application “integration fix”.    Moreover, enterprises are 
looking for solutions that have been designed to operate on the 
same conceptual basis as the leading packaged-applications 
systems ¾ that is, speaking the language of business processes and 
cross-functional best practices.    Aberdeen calls this higher-level 
middleware Enterprise Application Services (EAS).
Application Servers
Application servers carry out much of the same tasks for objects 
that TP monitors carry out for transactions:    they multiplex and 
load balance incoming requests for objects.    Like TP monitors for a 
data architecture, application servers provide an architecture with 
greater scalability and flexibility by allowing IS to extend the 
overall architecture across multiple servers.
Many of today’s application servers have successfully applied TP 
monitor technology to handle application and object access across 
the environment.
Aberdeen research indicates that IS buyers should look for 
application servers that bridge application and data approaches, by 
supporting load balancing not only across multiple server 
platforms but also across multiple backend databases.
10
Middleware Technology Practice Summary
AberdeenGroup 
 How An Integrated Middleware Solution Works
Figure 3 shows an example of integrated middleware as part of an 
overall Internet solution that many enterprises will move toward over 
the next 1-2 years, incorporating electronic commerce and business 
critical applications.    Aberdeen expects that middleware suppliers 
will need to offer users a complete integrated middleware solution or 
establish alliances with complementary vendors to have long-term 
market viability.
By implementing integrated middleware, enterprises are able to 
isolate their applications from the extensive differences in “back end” 
software such as network protocols, databases, operating systems, 
etc., as well as understand the potential of open, heterogeneous, multi-
supplier computing infrastructure.
Figure 3:    Integrating Middleware Technologies
Repository
Object-
Relational
Database
Object Partitioning
Software 
(administrative)
Web
Server
Web
Application
Servers
ORB
Request/Reply
Push Technology
Messaging
Object-
Data Access
Other
Servers
1)  End
user
sends
request
 to  Web
Server
 2)  Web
Server
detects
object
access,
passes to
Web
application
server
3)  Web
application
server uses
messaging
to multiplex to
multiple servers
and deliver to
ORB or backend
database
4) ORB
accesses
repository or
backend
database for
the object and
returns to Web
application
server
5) Web
application
server
sends reply
to end user
6) Periodically
applications
“publish” to the
Web application
server, which
“pushes” messages
to all subscribing
clients
7) Partioning software
periodically deploys
upgrades and new
objects to all 
repositories
2nd Tier
3rd Tier
Source:    AberdeenGroup, April 1998
11
Middleware Technology Practice Summary
AberdeenGroup 
12
Middleware Technology Practice Summary
AberdeenGroup 
Chapter Four
Issues and Challenges
Impact of Major IT Trends
Aberdeen research shows that middleware such as application-to-
application communications can play a critical role in delivering 
enterprise-architecture scalability, flexibility, and cost-effectiveness 
¾ but today it is increasingly a technological bottleneck.    It is 
especially a problem in the key areas of Internet development and 
complex-data support.

The Internet.    To handle the need for rapid development 
and complex-data support, enterprise architectures need 
to achieve greater distributed-object support, object-
handling scalability, and object-based flexibility and 
adaptability, user connects and sessions, and do this in a 
cost-effective manner.    IS’ development efforts need to 
build on open middleware that can support the new 
Internet and complex-data objects.    Administrators need 
a way to monitor and load-balance the new objects that 
are flooding their systems.    IS management wants an 
extensible infrastructure for the long-term successful 
rollout of distributed systems.    And middleware can also 
play a role in scaling Internet servers’ ability to handle 
end-user connects and sessions.

The application-connecting middleware in many 
enterprises today is beginning to be a bottleneck to 
answering these needs.    Web middleware like CGI is 
slowing server performance and complicating 
development efforts.    Many user implementations of 
messaging solutions like IBM’s MQSeries do not have 
adequate administrative or development tools, slowing 
deployment and maintenance.    Without the ability to 
repartition applications flexibly, much of today’s 
middleware locks users into outdated application 
partitions even as the enterprise architecture evolves 
rapidly.    If carelessly applied, today’s middleware not 
only does not meet the new user needs but has the 
potential to create a major new legacy-software problem.
13
Middleware Technology Practice Summary
AberdeenGroup 

The transition to client-server and network-centric 
applications is dramatically increasing the need for 
middleware.    Simultaneously, the complexity and 
abundance of data to be managed by business 
applications has increased.    The popularity of the 
Internet has made it possible to distribute content 
involving text, images and audio, and new applications 
are beginning to incorporate RDBMS suppliers’ object-
relational technology.    Thus, systems must be able to 
handle various complex data types (e.g., time-series, 
graphics) within a highly distributed and complex 
environment¾often using objects.

Object-oriented application development.    Today’s 
competitive pressures are driving enterprises to build 
new applications in a rapid, well-timed, and cost-effective 
manner.    These applications typically must deliver 
continually-upgraded competitive advantage, closely 
match evolving business strategies, processes, and 
architectures, and compete for IS dollars with Year 2000 
and other IT imperatives.    Internet and distributed-object 
support give today’s development tools the flexibility to 
achieve “write once, deploy many” productivity gains; 
and the tool suppliers are achieving this by incorporating 
middleware in their toolsets.
Supplier Success Factors

To meet long-term user flexibility needs, suppliers should 
continue integrating various middleware pieces 
(technologies) into a smoothly working whole.    The aim is 
to enable IS to create a distributed environment in which 
applications and data move instantly, cost-effectively, and 
flexibly to where an end user needs them.

A supplier’s middleware solution should be extensible 
and reusable for the project at hand as well as future 
projects.    The tools should be designed in such a manner 
that users are able to extend the tool from a per-project 
basis to an ongoing enterprise-wide usage.

In the long term, the middleware supplier’s tools/solutions 
should be able to contribute to an organization’s bottom 
line by reducing the cost of application design, 
development, deployment and maintenance.    Suppliers 
should also satisfy user overall criteria such as scalability 
and robustness.
14
Middleware Technology Practice Summary
AberdeenGroup 
User Success Factors

Enterprise middleware initiatives may involve integrating 
many sources and targets while maintaining 
independently coded modules for each integration 
process.    This is extremely resource intensive.    Using a 
single, flexible and consistent middleware framework for 
each process will greatly reduce the amount of personnel 
resources needed to maintain and develop the system.

A middleware solution should be built on an architecture 
that has the ability to scale, support and introduce new 
technologies within a globally distributed environment.    
In addition, the solution should provide the flexibility to 
add multiple servers as a system grows as well as the 
ability to use pre-configured components that “hook” into 
legacy applications.

Aberdeen advises IS buyers: to demand that their 
middleware suppliers define a path towards an integrated 
overall architecture; to choose the supplier with the best 
combination of a strong current solution, a good vision, 
and a solid, open position within the industry; to plan to 
prototype within the next 6 months; and to spread a 
middleware architecture across the enterprise in the year 
after that.
15
Middleware Technology Practice Summary
AberdeenGroup 
Chapter Five
Supplier Abstracts
Active Software
3255-1 Scott Blvd
Santa Clara, CA 95054
Phone:    (408) 988-0414
www.activesw.com
Market Position
Active Software, founded in 1995, distinguishes itself in the market 
by providing an Integration System which is designed to 
specifically integrate applications.    Essentially, Active seeks to 
commoditize the heterogeneous technologies involved in the 
integration of applications by providing an architected system.    
The architected system (ActiveWeb) allows the integration of 
packaged applications with custom applications (Packaged 
Application Integration), the integration of functional 
organizations together with IS (Enterprise Integration), and the 
integration of an enterprise with its partners and customers (E-
Business Integration).
Aberdeen Conclusions
Active offers a targeted solution to the application integration 
challenge that is robust and extensible.    As prospective customers 
with complex integration requirements seek solutions that are 
capable of integrating diverse applications and their 
heterogeneous technologies, Active will increasingly be considered. 
When early customers go public with complex Active 
implementations, Active should garner favorable public 
acknowledgment as a complex-EAI-solution provider.
16
Middleware Technology Practice Summary
AberdeenGroup 
BEA Systems, Inc.
835 Moffett Park Drive
Sunnyvale, California 94089
Phone:    (800) 817-4BEA
www.beasys.com
Market Position
Since its inception, BEA has pursued a very aggressive business 
strategy — taking a market dominant position in products and 
services related to the TUXEDO Transaction Processing (TP) 
monitor.      In January 1996, BEA formed a partnership with Novell, 
where BEA became the developer and master distributor of 
TUXEDO.    Prior to the 1996 partnership with Novell, BEA acquired 
Information Management Company (IMC) and Independence 
Technologies, Inc. (ITI), the two largest suppliers of enterprise-level 
TUXEDO systems, providing professional services and management 
and connectivity software supporting OLTP environments.    In 
addition, BEA acquired Paris-based Unix Systems Laboratories S.A., 
the largest TUXEDO distributor outside the U.S. and Client-Server 
Technologies Oy Ltd. in Finland.    Hence, the root of BEA’s 
Enterprise Middleware Solution is TUXEDO, TP monitor software 
that manages high volume transactions, application messaging and 
run-time services in enterprise-wide applications.
The recent acquisition of Digital Equipment’s DECMessageQ (now 
called BEA MessageQ) and Digital ObjectBroker (now BEA 
ObjectBroker) will expand the Enterprise Middleware Solution by 
integrating transaction capabilities, messaging and new object-
oriented initiatives.
Aberdeen Conclusions
An especially notable feature of the BEA solution suite is that it 
includes strong technology in three of the key areas of tomorrow’s 
enterprise middleware—TP monitors, messaging and an Object 
Request Broker (ORB).    These are particularly of importance to IS 
because of the need to rapidly build flexible, distributed (especially 
Internet) competitive-advantage applications.    As a result, BEA is 
in a strong position to succeed if it follows through effectively on 
its Iceberg integrated-architecture initiative.
17
Middleware Technology Practice Summary
AberdeenGroup 
Borland International Inc., (soon to be Inprise)
100 Borland Way
Scotts Valley, CA 95066
Phone:    (408) 431-1000
www.borland.com
Market Position
In the past 2 years, Borland has diverged from its traditional 
development/database/application focus and moved steadily 
towards positioning itself as a supplier of middleware.    Its most 
notable move has been to acquire Visigenic, purveyor of 
Visigenic/DAP.    The Visigenic/DAP (distributed application 
platform) solution is based on Visigenic’s ORB technology 
(VisiBroker) and Visigenic’s extension of its cross-database data-
access technology to support object-data access.
Aberdeen Conclusions
Borland has an interesting solution that should prove to be 
effective for desktop centric Internet implementations.    However, 
Borland’s immediate challenge will be to integrate their products 
into an overall middleware solution and gain mind and market 
aside from the traditional developer community where they are 
known best.
CrossWorlds Software
577 Airport Blvd
Suite 800
Burlingame, CA 94010
Phone:    (650) 685-9000
www.crossworlds.com
Market Position
CrossWorlds, founded in 1996, has set out to build a packaged 
integration solution in partnership with the industry-leading EBA 
suppliers.    The company is now providing out-of-the-box, pre-
built, partner-certified application-integration capabilities.    These 
capabilities  referred to as Processware  are delivered as 
Collaborations and Connectors.    Of note, CrossWorlds' approach 
focuses on the business methods and processes that require multi-
18
Middleware Technology Practice Summary
AberdeenGroup 
system integration  not solely on the data-level or messaging-
based middleware approach.
In many respects, and with the begrudging acknowledgment of the 
competition, CrossWorlds has led the charge in creating industry 
awareness of what has become the market for Enterprise 
Application Integration.    With a world renowned list of investors 
and the largest war chest on the block, CrossWorlds is the company 
with which all EAI competitors must reckon.
Aberdeen Conclusions
CrossWorlds is capitalizing on its high-end market and PR visibility 
as well as the production release of its Customer Interaction 
Solutions product line.    As one of the hottest application markets, 
CIS represents a great first target.    With the prerequisite 
Connectors to the leading ERP solutions and a list of twenty 
process-based Collaborations, prospective customers seeking an 
elegant and cost-effective solution to the CIS-to-ERP integration 
issue are CrossWorlds' for the taking.    Follow-on into the Human 
Resource space (mid-1998 and primarily a SAP-to-PeopleSoft 
opportunity) will likely yield a sizable "low hanging fruit" 
opportunity.
EXPERSOFT Corporation
5825 Oberlin Drive
San Diego, CA 92121
Phone:    (619) 824-4100
www.expersoft.com
Market Position
The PowerBroker product suite foundation is a distributed 
software infrastructure that provides transparent object 
distribution, multiple object models, language support, event-
driven asynchronous operation, and platform autonomy.    The core 
of the architecture is an advanced, standards-based object request 
broker, the PowerBroker ORB.
Expersoft provides a one-stop-shopping solution for the distributed 
object developer.    CORBAplus supports the use of Java, C++, 
Smalltalk, Visual Basic and OLE enabled applications running in 
Microsoft Windows 95, Windows NT, Solaris, HP/UX and AIX Unix 
environments.    PowerBroker Extended C++ supports 
19
Middleware Technology Practice Summary
AberdeenGroup 
PowerBroker’s original XShell® programming model that is a 
superset of the OMG CORBA functionality.    In addition, it combines 
a set of C++ class libraries that have been integrated into the 
PowerBroker programming model and architecture.
Expersoft distinguishes its offering from similar tools by its focus 
on supporting mission critical applications in a distributed 
environment.    Expersoft’s ability to bridge to DCOM is especially 
important for users with mixed Windows NT/Unix environments.
Aberdeen Conclusions
Aberdeen believes that Expersoft is positioned to provide value-
added by supporting enterprises that deploy new object-based 
applications/systems more rapidly, ensure the reliable delivery of 
object-type information, and add architectural flexibility.    
However, Expersoft must diligently work toward differentiating 
their message and solution in a crowded and confused ORB market 
as well as increasing their current “slice” of market and mind 
share.
IBM Corporation
Route 100
Somers, NY 10589
Phone:    (914) 766-1800
www.ibm.com
Market Position
IBM’s middleware offerings include the widely-popular MQSeries, 
the CICS and Encina TP monitors, and Component Broker (CB), a 
notable new technology, placing IBM in a strong position to take a 
leadership role in the integrated middleware market.    CB offers a 
distributed object-based middleware solution that consists of a 
development environment, a run-time environment and a server 
management environment.    CB includes Component Broker 
Connector (CBConnector), an application runtime environment, 
and Component Broker Toolkit (CBToolkit), a set of development 
tools enabling developers to enhance basic business processing 
logic.    Portions of the CB technology will be incorporated in 
current IBM middleware offerings (DB2, CICS, Encina, IMS and 
MQSeries).    IBM’s middleware offerings form the keystone of IBM’s 
Network Computing Framework (NCF).
20
Middleware Technology Practice Summary
AberdeenGroup 
Aberdeen Conclusions
With the popularity of MQSeries and the introduction of NCF, IBM 
is in a relatively strong position in the middleware market.    
However, to succeed in the long term, it will need to demonstrate 
that NCF integration is more than skin-deep and that IBM is open to 
third-party middleware (e.g., for MQSeries administration).
21
Middleware Technology Practice Summary
AberdeenGroup 
Insession, Inc.
100 Arapahoe Avenue
Boulder, Colorado 80302
Phone:    (303)440 3300
www.insession.com
Market Position
The philosophy of Insession is to provide organizations with 
technology solutions that integrate distributed systems with host-
based environments.    In 1990, Insession introduced ICE, a data 
communications software solution that integrates Tandem systems 
into enterprise SNA, APPN, and TCP/IP networking environments.
Insession has further continued its focus on the interoperability of 
distributed systems with host-based environments with the 
introduction of the TransFuse software solution.    TransFuse allows 
the content of existing server transaction processing systems to be 
accessible to any client platform, whether it be a desktop 
application or a Web browser.
TransFuse has a clear differentiation from most if not all other 
middleware suppliers in its ability to enable Web, client/server and 
object-oriented applications to interact with TP monitors by using 
APIs that are based on a standard object model.    Furthermore, 
TransFuse can be deployed in a two, three or n-tier client/server 
architecture.    Client applications are able to access the TP monitor 
services directly or through gateway servers that run on a middle-
tier system.
Aberdeen Conclusions
Insession’s experience and broad knowledge base in transaction 
processing, data communications and network management and 
services solidly position them to take a leadership role in the 
ability to link Internet and client/server applications to host 
transaction systems.    Insession’s TranFuse is a strong solution for 
these user needs, and especially because of its flexible integration 
with both client-server/Internet and host solutions as well as its 
down-in-the-details support for these solutions’ scalability, 
robustness, and programmer-productivity features.    However, 
Insession must achieve greater mindshare for both “accessware” 
and its own products to succeed in the long term.
22
Middleware Technology Practice Summary
AberdeenGroup 
Microsoft Corporation
One Microsoft Way
Redmond, WA 98052-6399
Phone: (425) 882-8080
www.microsoft.com
Market Position
Microsoft is presently well positioned to move into enterprise 
environments with their middleware suite and interoperability 
story that includes Microsoft Transaction Server (MTS), Microsoft 
Message Q (MSMQ) and Web services.
At the heart of each of these product offerings is the Microsoft 
Component Object Model (COM) — a component software model 
that provides integrated services, tools, and applications that 
promote reusable, off-the-shelf, client and server components.
Microsoft Transaction Server (MTS) provides broad component 
functionality such as automatic transaction support, role-based 
security, access to databases, message queuing functionality and 
mainframe-based applications, and performance-enhancing 
features such as database connection pooling.
MSMQ offers message queuing functionality such as reliable 
message delivery, cost-based message routing and support for 
transactions.    In addition, MSMQ can be used to enable Windows 
applications to communicate with each other asynchronously or to 
integrate with applications running on other platforms.
Internet Information Server 4.0 (IIS) is a web server that supports 
Active Server Pages (ASPs).    ASPs enable developers to combine 
HTML with VBScript or JavaScript to build presentation interfaces, 
implement business logic, and call components based on 
Microsoft's COM.
Aberdeen Conclusions
With the popularity of Microsoft in the desktop environment and 
the introduction of their middleware solution, Microsoft is in a 
strong position to become a dominant player in the integrated 
middleware market.    However, to succeed in the long term, 
Microsoft will need to demonstrate that MTS, MSMQ and its Web 
services are integrated, can scale, and are more than just another 
Microsoft solution that has been introduced to the market without 
23
Middleware Technology Practice Summary
AberdeenGroup 
the “proof of implementation” that is critical to the IS buyers of 
enterprise-wide middleware solutions.
24
Middleware Technology Practice Summary
AberdeenGroup 
New Era of Networks, Inc. (NEON)
7400 East Orchard Road, Suite 230
Englewood, Colorado 80111
Phone:    (303) 694-3933
www.neonsoft.com
Market Position
NEON, founded in 1993, aims to establish NEONet, its EAI solution 
already popular in (and customized for) financial institutions, as 
the leading standard for application integration across the 
enterprise.    Key elements of its strategy are a direct sales model, 
expansion into vertical markets, and expansion of a global sales 
force.
Aberdeen Conclusions
The proof of NEON's success will be its ability to expand beyond 
the financial vertical market  where highly-specialized, custom-
developed applications are the rule  to markets with other 
commercial orientations and interest in using messaging 
technology to achieve integration of their application portfolios.
RELIANT Data Systems
13915 Burnet Road Suite 200
Austin, Texas 78728
Phone:    (800) 713-7070
www.reliantdata.com
Market Position
Reliant Data Systems has been able in many cases to prove that the 
Data Conversion, Loading and Extraction Engine (DCLE) reduces 
the project time and cost of converting data from legacy systems to 
new applications.    In addition, the ability to reuse DCLE Engine in 
multiple projects conserves the investment in the tools as well as 
saves time in training.
The Data Conversion, Loading and Extraction Engine (DCLE 
Engine) is an embeddable, reusable three-tier architecture.    This 
architecture enables users to specify a migration once, and embed 
the execution module within an application for future migration 
25
Middleware Technology Practice Summary
AberdeenGroup 
projects.    Additional features enable the solution to be powerful 
and flexible, easy to use and offer functional depth enterprise 
application migration projects require.    These features are:

DCLE Connect, a graphical user interface;

The Command Processor, a central metadata store and 
factory used to create and distribute execution processes 
network wide;

The Execution Module, a separate module, which 
functions as the Engine and can be invoked from the 
DCLE Command Processor or as an independent 
execution; and

Object Oriented Design, the ability to define data as 
objects for inclusion in object or object-relational 
databases.
Reliant Data Systems has a strong technical and management team, 
as well as partnerships with other leading industry providers. In 
addition, Reliant Data Systems offers a comprehensive range of 
consulting and customer support services.
Aberdeen Conclusions
Aberdeen finds that Reliant Data Systems delivers an embeddable, 
reusable architecture that is scalable and reliable in enhancing 
business critical information.    The DCLE Engine provides 
sophisticated data transformation capabilities effective in large 
organizations that need to migrate legacy based applications with 
new relational systems, synchronize disparate software 
applications, introduce data warehouses, and improve Year 2000 
initiatives.    To continue to succeed, in the long-term, Reliant will 
need to increase IS’ perception of the DCLE Engine as strategic and 
continue to integrate it with other supplier’s toolsets such as Year 
2000 tools.
SmartDB Corporation
1121 San Antonio Road
Palo Alto, CA 94303
Phone: (415) 988-8996
www.smartdb.com
26
Middleware Technology Practice Summary
AberdeenGroup 
Market Position
SMART Corporation’s products, SMART Templates, are well 
positioned in the data-integration middleware market, and can be 
particularly effective for enterprises with multiple or on-going data 
migration needs or the need to rapidly implement Oracle 
applications.    Because the templates have been designed to be 
reused, saved and modified they become a cost effective tool for 
present and future data migration projects.
The SmartDB Workbench product suite focuses on integrating data 
between disparate applications by providing an easy way to map, 
transform, and move data between them.    The product can be 
used for one-time data conversions from mainframe applications 
to client-server, or to provide bi-directional data movement 
between operational applications.
SmartDB Corporation’s product suite is comprised of SmartDB 
Workbench Development product, the SmartDB Workbench 
Templates for Oracle Applications (“SMART Templates”), and the 
SmartDB Workbench Run-time product (“Run-time product”).    The 
SmartDB Workbench development product is the development 
environment that allows the user to create data extraction, 
transformation, and loading scenarios with a GUI front end.    The 
Smart Templates products provide pre-built data transformation 
modules specifically for Oracle applications.    The Run-time 
product allows the developed conversion objects to be deployed in 
a distributed environment.    SmartDB Corporation offers a total 
solution that includes training and consulting services.
Aberdeen Conclusions
SmartDB Corporation’s continued growth, combined with its 
increasing customer base, indicate that SmartDB Corporation is a 
safe bet for IS and business managers looking for cost-effective, 
easy-to-use data migration technology that will address immediate 
data migration needs as well as becoming a strategic component of 
an organization’s long-term data movement-strategy.    If Smart 
manages to transition from Oracle-centric to database-eclectic 
successfully, its immediate future is bright.
TIBCO Software Inc.
3165 Porter Drive
Palo Alto, CA 94304
27
Middleware Technology Practice Summary
AberdeenGroup 
Phone:    (650) 846-5000
www.tibco.com
Market Position
Founded in 1985 as Teknekron Software Systems Inc., TIBCO (a 
subsidiary of Reuters Holdings PLC) pioneered the early 
development of commercial publish-and-subscribe technology.    
The publish-and-subscribe philosophy is at the core of the 
company’s patented middleware solution known as The 
Information Bus (TIB) integration platform.    The TIBCO solution 
was first adopted by Wall Street for use in trading systems, where it 
quickly became a de facto standard for integrating disparate 
information from various data sources and distributing it across a 
variety of networks and platforms.
In early 1998, TIBCO introduced a new EAI-capable solution ¾    
TIB/ActiveEnterprise.    TIB/ActiveEnterprise links systems and 
applications, to solve a particular tactical problem, such as 
integrating legacy data on mainframe computers with modern 
desktop applications, or as part of a strategic initiative to deploy an 
information infrastructure that integrates business processes 
worldwide.    With TIB/ActiveEnterprise, the major business 
functions of an enterprise can share the same data, at the same 
time, in real-time.
For financial institutions, TIB/ActiveEnterprise offers a platform 
for building Straight-Through-Processing (STP) systems, which 
automate front-office, middle-office and back-office operations. 
Likewise, manufacturing firms will be able to more quickly meet 
customer demands by implementing real-time, integrated, web-
based, global supply chain management systems.
Aberdeen Conclusion
TIBCO’s TIB/ActiveEnterprise is designed to deliver a technology-
rich solution that can reliably deliver cross-enterprise, application 
integration that is event-based and scalable.    TIBCO uses 
sophisticated push, multicasting, and object-oriented technologies 
to achieve these ends.    As a result, TIBCO is middleware-
technology-rich.    To succeed in the long term, it will need to 
increase IS perception that it is more than a niche player.
Oracle Corporation.
500 Oracle Parkway
28
Middleware Technology Practice Summary
AberdeenGroup 
Redwood Shores, CA    94065
Phone:    (415) 506-7000
www.oracle.com
Sybase, Inc.
6475 Christie Avenue
Emeryville, CA 94608
(800) 879-2273
www.sybase.com
29


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | middle~1-a64fa0 |
| title | Middleware Technology: 1998 Practice Summary |
| author | Aberdeen Group |
| date | 1998-05-01 |
| type | other-research |
| subject_domain | middleware |
| methodology | industry-analysis, market-overview |
| source_file | MIDDLE~1.DOC |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group's 1998 practice summary covering the middleware technology market, analyzing gateways, TP monitors, RPCs, messaging, ORBs, data access tools, EAI solutions, and application servers as distinct middleware categories. The report sizes the middleware market at approximately $6 billion by 2000, identifies the CORBA vs. DCOM standards battle as a critical industry question, and provides supplier abstracts for thirteen vendors including BEA Systems, IBM, Microsoft, TIBCO, and CrossWorlds. Key findings include that no vendor had yet delivered a fully integrated middleware solution and that market consolidation was underway.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Captures the middleware landscape at a pivotal moment when the market was transitioning from point products to integrated EAI solutions and Internet-centric architectures; profiles vendors who would become major players (BEA acquired by Oracle; TIBCO IPO). |
| **Relevance** | high | Middleware categories like messaging, application servers, and EAI are foundational to modern enterprise architecture; the CORBA vs. DCOM debate resolved in favor of neither (REST/HTTP won), but the underlying integration challenges remain highly relevant. |
| **Prescience** | high | Aberdeen correctly predicted market consolidation, the rise of EAI as a strategic priority, the importance of integrated middleware over point products, and BEA/TIBCO viability — most of these proved accurate over the following five years. |

### Prescience Detail


**Prediction 1:** app_data_integration_market_forecast
- **Claimed:** $8 billion by 2001
- **Year:** 2001
- **Confidence at time:** medium

**Prediction 2:** middleware_market_forecast
- **Claimed:** ~$6 billion by year 2000
- **Year:** 2000
- **Confidence at time:** medium

**Prediction 3:** eai_sap_integration_criticality
- **Claimed:** EAI middleware will be crucial to effective use of SAP R/3 within 1-1.5 years
- **Year:** 1999
- **Confidence at time:** high

**Prediction 4:** integrated_middleware_requirement
- **Claimed:** Middleware suppliers must offer complete integrated solution or alliances for long-term viability
- **Year:** 2000
- **Confidence at time:** high


### Entities Referenced (17)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | company | dissolved | Harte-Hanks -> Aberdeen (rebranded) |
| Active Software | company | [DEFERRED] | [DEFERRED] |
| BEA Systems Inc. | company | [DEFERRED] | [DEFERRED] |
| Borland International Inc. (soon to be Inprise) | company | [DEFERRED] | [DEFERRED] |
| CrossWorlds Software | company | [DEFERRED] | [DEFERRED] |
| EXPERSOFT Corporation | company | [DEFERRED] | [DEFERRED] |
| IBM Corporation | company | active | [DEFERRED] |
| Insession Inc. | company | [DEFERRED] | [DEFERRED] |
| Microsoft Corporation | company | active | [DEFERRED] |
| New Era of Networks Inc. (NEON) | company | [DEFERRED] | [DEFERRED] |
| RELIANT Data Systems | company | [DEFERRED] | [DEFERRED] |
| SmartDB Corporation | company | [DEFERRED] | [DEFERRED] |
| TIBCO Software Inc. | company | [DEFERRED] | [DEFERRED] |
| Oracle Corporation | company | active | [DEFERRED] |
| Sybase Inc. | company | [DEFERRED] | [DEFERRED] |
| Visigenic Software | company | [DEFERRED] | [DEFERRED] |
| IONA Technologies | company | [DEFERRED] | [DEFERRED] |

### Technologies Referenced (14)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Transaction Processing (TP) Monitors | framework |  | mature | legacy |
| IBM MQSeries | application | IBM | growth | active |
| CORBA (Common Object Request Broker Architecture) | framework | OMG | emerging | legacy |
| DCOM (Distributed Component Object Model) | framework | Microsoft | emerging | legacy |
| TUXEDO TP Monitor | application | BEA Systems (originally Novell) | mature | active |
| CGI (Common Gateway Interface) | framework |  | growth | legacy |
| Microsoft Transaction Server (MTS) | application | Microsoft | emerging | legacy |
| Microsoft Message Queue (MSMQ) | application | Microsoft | emerging | active |
| IIS/Active Server Pages (ASP) | application | Microsoft | growth | legacy |
| VisiBroker ORB | application | Visigenic/Borland | emerging | legacy |
| IBM Component Broker (CB) | application | IBM | emerging | legacy |
| TIB/ActiveEnterprise | application | TIBCO | emerging | legacy |
| Remote Procedure Calls (RPC) | protocol |  | declining | legacy |
| SAP R/3 | application | SAP | growth | legacy |

### Observation Summary

- Total observations: 23
- By type: market-assessment: 8, competitive-assessment: 7, viability-prediction: 4, expert-opinion: 4
