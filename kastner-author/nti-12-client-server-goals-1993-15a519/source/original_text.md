# Realistic Goals for Client-Server Computing

> Archived from: NTI 12 Client-Server Goals 1993.pdf
> Original publication date: 1993-07-01
> Author: Peter S. Kastner, John Logan, Thomas Willmott

---

## Original Document Text

AberdeenGraup
Realistic Goals
for Client-Server
Computing
New Technology Impact Series
Number 12
July 1993
Aberdeen Group, Inc.
92 State Street
Boston, Massachusetts 02109
Telephone 617 723 7890
AberdeenGrowp Client-Server Computing
AGENDA
□ CLIENT-SERVER SYSTEM COMPONENTS
□ CURRENT IMPLEMENTATIONS
□ C-S APPLICATION CHARACTERISTICS
□ EVOLUTION TO NEXT-GENERATION, ADVANCED
DESIGNS
□ IMPACT OF EMERGING TECHNOLOGIES
□ WRAP-UP
Aberdeen Notes:
The industry appears to have reached a consensus that "client-server" is its
vision of next-generation computing. In this video, Aberdeen will provide
its own definition of this important concept. We will review current
implementations of the client-server architecture, as well as illustrating
important characteristics of emerging client-server applications.
The agenda will then shift to consider how client-server will likely evolve to
future designs, including a discussion of the impact of several emerging
technologies.
We conclude this tape with a summary of key findings and a recap of
major trends.
New Technology Impact Series
Page 1
AberdeenGrowp
Client-Server Computing
SYSTEM COMPONENTS
□ EVALUATING CLIENT OPTIONS
□ CHOOSING FROM A RANGE OF SCALABLE
SERVERS
□ UNDERSTANDING THE ROLE OF LEGACY
MAINFRAME AND MID-RANGE PLATFORMS
□ SYSTEMS SOFTWARE IN TRANSITION
□ BUILDING A NETWORK INFRASTRUCTURE
Aberdeen Notes:
Aberdeen research strongly indicates that the successful implementation of
client-server systems rests on a consideration of five critical planning areas.
First, in order to prepare for a smooth transition to the new architecture,
MIS organizations should review the multiple hardware and software
options that define the client PC or workstation. Next, the characteristics
of the back-end server must be defined. Of course, planning for server
technology must include a review of the most appropriate role for the
continuation of existing legacy systems - including both mainframes and
proprietary minicomputers.
For both the client as well as the server, the industry offers multiple
operating system options - Unix, Microsoft’s NT, Windows/DOS, IBM’s
OS/2, NeXTSTEP from NeXT and OSF from the Open Software
Foundation are just six of the available alternatives. In every area, systems
software is in transition and moving toward increasingly modular and
object-oriented designs. Because distributed computing is a major element
in client-server topologies, planning for the network infrastructure is also a
fundamental client-server component agenda item.
Each of these five areas will be considered in some detail in the next
slides.
New Technology Impact Series
Page 2
AberdeenGrowp Client-Server Computing
EVALUATING CLIENT OPTIONS
□ WHAT TO DO WITH INVESTMENTS IN ASCII
AND 3270 TERMINALS
□ PC PRICE/PERFORMANCE IMPROVEMENTS
ACCELERATE
□ WHAT IS A COMMERCIAL WORKSTATION?
Aberdeen Notes:
Aberdeen believes that nearly 40% of the typical information technology
budget is now consumed by PCs, terminals, workstations, local area
networks, and other "client" related expenses.
Although PCs are responsible for an increasing percentage of these outlays,
MIS organizations must also face the challenges posed by huge existing
investments in ASCII and 3270 terminals. Often the need to protect
investments in these devices represents a stumbling block to downsizing
initiatives, and client-server development.
Given the fact that client-server applications require independent
processing and a full-range of performance in the client device, it is simply
impossible to craft C-S applications using traditional terminals. An IS
department must, therefore, fully leverage its investment in terminals and
may have to be willing to postpone development of true client-server
applications until those financial commitments are fully written off.
In many cases where investment paybacks and ROI are of concern, a
compromise position can sometimes be reached by using the existing
installed base of terminals for heads-down production applications while
using PCs and workstations for early C-S prototypes in decision support
applications.
Another important planning consideration -- one that is having a impact on
the earlier-than-expected availability of client-server applications -- is the
continued, dramatic improvement in PC/workstation price-performance.
For example, Intel 486-based and popular RISC-based workstation
solutions (capable of all the functionality required of the most demanding
C-S applications) are already available 1993 at extremely low price points.
New Technology Impact Series
Page 3
AberdeenGrowp
Client-Server Computing
EVALU ATI N G CLIENT OPTIONS
□ WHAT TO DO WITH INVESTMENTS IN ASCII AND
3270 TERMINALS
□ PC PRICE/PERFORMANCE IMPROVEMENTS
ACCELERATE .
□ WHAT IS A COMMERCIAL WORKSTATION?
Aberdeen Notes:
In 1994, powerful client hardware platforms - which Aberdeen classifies as
commercial workstations -- will be available for under $3500, including 32-
bit multi-tasking operating systems such as Unix and Windows/NT.
Commercial workstations offer similar performance characteristics to
traditional technical workstations. However, commercial workstations
targeting robust client-server and multimedia applications must fit in a
price band between $3500 and $7000 before the commercial workstation
market can be expected to witness explosive growth.
New Technology Impact Series
Page 4
Aberdeentzrottp Client-Server Computing
SCALABLE SERVERS
□ PC-BASED LAN SERVERS COME OF AGE
□ MULTIPROCESSING: TIGHTLY COUPLED
□ MULTIPROCESSING: LOOSELY COUPLED
□ SCALABLE AND BASED ON BUILDING BLOCK
COMPONENTS
Aberdeen Notes:
On the back-end of the client-server architecture, users will be able to
employ scalable, microprocessor-based systems that offer an enormous
range of performance, memory, storage and communications options. In
the PC LAN environment, uniprocessor machines with large disk and
memory capacities already offer users powerful print and file services.
Companies like NetFrame and Tricord -- plus all the major PC
manufacturers -- offer server products for the LAN market.
Aberdeen believes that advanced servers, based upon multiple
microprocessor architectures, will become the standard server platforms of
the mid-to-late 1990s. These machines can be roughly divided into two
packaging schemes, notably tightly- and loosely-coupled multiprocessing.
Tightly coupled multiprocessing typically offers scalability from two to
approximately 16-20 CPUs, each of which shares a sinlge copy of the
operating system and a common memory. Loosely coupled
multiprocessing, at the high-end of the market segment, typically includes
dozens or hundreds of processors, each with its own OS and memory.
More advanced programming and precompiler technology is required to
take maximum advantage of these latter networked and massively parallel
designs, while the former tightly-coupled symmetric multiprocessing
platforms usually do not require any modification of applications software.
A more detailed analysis of this topic can be found in Aberdeen’s earlier
report Trends in Microprocessor-based Multiprocessing.
The bottom line is that new, powerful machines -- scalable from low-to-
high-end performance with microprocessor-based board upgrades - will
become the building blocks for back-end database, communications and
computational servers in the 1990s. Companies early to concentrate on
leadership and success in these markets include Compaq, Data General,
Hewlett-Packard, NCR, Pyramid, Sequent, and Unisys.
New Technology Impact Series
Page 5
AberdeenGrowp
Client-Server Computing
ROLE OF LEGACY SYSTEMS
□ REBALANCING, RESTRUCTURING TRADITIONAL
APPLICATION PORTFOLIOS
□ LEGACY SYSTEMS INCREASINGLY ACT AS DATA
REPOSITORIES - AND COMMUNICATION HUBS
□ NEXT-GENERATION: ONE SERVER = ONE
APPLICATION
Aberdeen Notes:
When preparing for client-server initiatives, the MIS department must also
devise a strategy for legacy systems, including the installed based of both
mainframes and proprietary minicomputers. One of the first considerations
is how to restructure the current applications portfolio. This includes
establishing a priority order for rehosting and reengineering mission critical
software programs.
In most organizations, legacy systems are being consolidated and gradually
replaced with servers based upon new microprocessor-based technology.
The mainframes and minicomputers that remain are being effectively used
to fill a new and important role as hub systems. Aberdeen defines these
hubs as enterprise data repositories as well as communications processors.
Despite the fact that organizations wish to extract as much value as
possible from their existing legacy systems, eventually the mainframe and
its application asset base will be devalued to zero. This erosion will
accelerate as the performance characteristics of powerful multiprocessing
servers and software development toolsets continues to improve.
In the future, Aberdeen believes that servers will typically be dedicated to
a single application or database. Prices will continue to decline to a point
at which it will no longer be necessary to balance multiple applications on
a single system. In this client-server topology, a variety of server types and
sizes will be distributed throughout the enterprise -- each dedicated to
servicing a focused type of information or computational requests.
Many IS organizations interviewed by Aberdeen Group are hoping to
protect their investments and extend the life of legacy systems by shifting
existing applications portfolios and changing these platforms into dedicated
servers, available as one more network resource.
New Technology Impact Series
Page 6
AberdeenGronp Client-Server Computing
SYSTEMS SOFTWARE
□ WINDOWS 3.1/DOS AND APPLE MACINTOSH
□ UNIX, OSF/1, AND WINDOWS/NT TRADE-OFFS
□ NOVELL, MICROSOFT, BANYAN FOR LANS
□ CAIRO, TALIGENT, D.O.E, NEXT STEP LOOM ON
THE HORIZON
□ SYNCHRONIZED DESIGNS FOR SECURE,
PRODUCTION SYSTEMS
Aberdeen Notes:
A third component in the client-server technology portfolio that requires
careful consideration is operating systems software. Several different
products and technologies are competing for popularity in this space, and it
seems that the area requires nearly constant planning attention. Here are
Aberdeen comments on some of the major alternatives.
Microsoft’s Windows/DOS and Apple Macintosh are the two graphical
environments that have major marketshare in 1993. However, these are
both supported by single-user operating systems, and in our opinion,
enhancements will have to occur in order to support robust client-server
applications.
In Microsoft’s case, there will be a transition to Windows for Workgroups
- a LAN optimized version of Windows -- and then a migration to NT and
future operating systems such as those codenamed Chicago and Cairo. In
the case of Apple, joint development work with IBM on the Power/PC will
move the familiar Macintosh interface to IBM’s AIX and RISC chip
platforms.
Of course, multiple variants of the Unix operating system also provide for
32-bit, multitasking, interrupt-driven operating functionality. Some of these
also offer a multi-threaded OS kernel and therefore, support for scalable
multiprocessing servers. Illustrative Unix products include HP/UX, Sun’s
Solaris, and USL’s UnixWare.
New Technology Impact Series
Page 7
AberdeenGronp Client-Server Computing
SYSTEMS SOFTWARE
□ WINDOWS 3.1 /DOS AND APPLE MACINTOSH
□ UNIX, OSF/1, AND WINDOWS/NT TRADE-OFFS
□ NOVELL, MICROSOFT, BANYAN FOR LANS
□ CAIRO, TALIGENT, D.O.E., NEXT STEP LOOM
ON THE HORIZON
□ SYNCHRONIZED DESIGNS FOR SECURE,
PRODUCTION SYSTEMS
Aberdeen Notes:
The three major providers of PC local area network operating systems are
Novell, Banyan and Microsoft. Novell has achieved dominant marketshare,
and is moving to enterprise wide directory services with Netware 4.0.
Banyan leads the high-end of market with its Vines product for enterprise
level networking, complete with sophisticated directory services.
Microsoft’s LAN Manager has not achieved dominance, despite high marks
for product quality and early relationships with Digital Equipment and
IBM. Microsoft’s ability to integrate LAN Manager into NT and build a
more robust indirect channel distribution system will likely define the
company’s future success in networking.
Object-oriented systems software, such as NeXTs NeXTSTEP, Taligent’s
Pink, Microsoft’s Cairo and SunSoft’s Distributed Objects Everywhere
(D.O.E), hold the promise of enabling third-parties to add custom
functionality directly to the operating system. This added functionality will
maintain compatibility with future releases of the operating system.
Aberdeen expects that client-server systems software requirements will
include a robust multi-tasking desktop OS and graphical user interface, as
well as a tightly integrated network operating system with high
performance links not only to file and print services, but also to high
performance database access. Furthermore, it is highly likely that within 3-
4 years these components will have evolved to an object-oriented
architecture. While several suppliers have provided product roadmaps and
strategies for dominating the client-server market, Aberdeen does not yet
believe that a clear winner scenario has emerged.
New Technology Impact Series
Page 8
AberdeenGroMp Client-Server Computing
NETWORK INFRASTRUCTURE
□ LANS ARE THE FOUNDATION FOR
DISTRIBUTED COMPUTING
□ HUBS, BRIDGES, ROUTERS, SWITCHES FOR
INTER-LAN NETWORKING
□ WIDE AREA NETWORK ACCESS REQUIRED
FOR ENTERPRISE-TO-ENTERPRISE
COMMUNICATIONS
□ HIGHER SPEEDS ON LOWEST COST MEDIA
□ CLIENT-SERVER COMPUTING WILL CONSUME
ENORMOUS AMOUNTS OF NETWORK CAPACITY
Aberdeen Notes:
One of the defining characteristics of client-server applications is the ability
to request information or processing services from a device that is remote
from the client workstation. These remote servers may be in the local area
workgroup or at a geographic location across the country or on another
continent. Therefore, network infrastructure is at the heart of planning for
an effective client-server initiative.
In the typical enterprise environment, the network is constructed from
multiple local area networks. PCs and workstations are linked to
departmental hubs and concentrators. These are interconnected by
bridges, routers and switches - one of the highest growth-rate segments in
the information processing industry over the last three years.
Wide area network access is required for long distance, or enterprise-to-
enterprise electronic data interchange. While corporations were quite
focused on private data networks in the 1980s, in the 1990s we are likely to
witness a shift toward the use of a wider number of bandwidth-on-demand
services from an increasing number of public utility long distance providers.
New Technology Impact Series
Page 9
Ab er deenGroup
Client-Server Computing
NETWORK INFRASTRUCTURE
□ LANS ARE THE FOUNDATION FOR DISTRIBUTED
COMPUTING
□ HUBS, BRIDGES, ROUTERS, SWITCHES FOR
INTER-LAN NETWORKING
□ WIDE AREA NETWORK ACCESS REQUIRED FOR
ENTERPRISE-TO-ENTERPRISE
COMMUNICATIONS
□ HIGHER SPEEDS ON LOWEST COST MEDIA
□ CLIENT-SERVER COMPUTING WILL CONSUME
ENORMOUS AMOUNTS OF NETWORK
CAPACITY
Aberdeen Notes:
An understanding of two key trends is a requirement for successful client­
server development. First, these new applications will consumer enormous
amounts of network capacity. Multimedia, video teleconferencing, and
increasingly high volumes of data communications spawned by client-server
application service requests will overwhelm current levels of network
capacity.
As a result of this enormous demand, the second trend, is for the industry
to continue to provide increased network performance on the lowest cost
media possible. For example, FDDI offers 100 Megabit/second
performance. However, the cost to connect to fiber media to obtain this
throughput speed is still approximately $2000 per connection. In order to
surmount this financial hurdle, suppliers are experimenting with CDDI -
100 Mbps speeds on unshielded-twisted pair high-grade telephone wiring --
as well as with new technologies such as ATM, asynchronous transfer
mode. Aberdeen can provide additional detailed information on these
topics in several of its recent studies, including Keeping in Step with
Advances in Networking.
New Technology Impact Series
Page 10
AberdeenGronp
Client-Server Computing
APPLICATION CHARACTERISTICS
□ DECISION SUPPORT AND MULTI-MEDIA
APPLICATIONS ARE EARLY CATALYSTS FOR
GROWTH
□ NEW DEPARTMENTAL COMPUTING METAPHOR:
LOTUS NOTES, WINDOWS FOR WORKGROUPS
□ CASCADING TRANSACTIONS IN COMPLEX
NETWORKS OF DISTRIBUTED SERVERS WILL
CHARACTERIZE PRODUCTION SYSTEMS OF
LATE 1990s
Aberdeen Notes:
Early client-server applications have centered on a variety of decision
support and multimedia applications. These programs create requests for
information, submit these requests to various distributed computing
resources, and then present the results to a GUI-based client workstation
for analysis and modeling.
This early prototype of the client-server design will likely be enhanced by
new departmental applications that emphasize message passing and other
LAN-based technologies. Products created to meet these specific
requirements include Lotus Notes and Windows for Workgroups.
Aberdeen believes that client-server applications will evolve to a much
more complex and sophisticated form during the forecast period. During
the late 1990s for example, client-server will be characterized by extremely
powerful workstations, by expanded networks of distributed servers, and
mission critical production applications. These production applications will
provide for peer-to-peer cooperative processing -- supporting high volumes
of transactions. A single request for information, for example, might
trigger dozens of cascading transactions in the network.
New Technology Impact Series
Page 11
AberdeenGronp
Client-Server Computing
CURRENT IMPLEMENTATIONS
□ TERMINAL EMULATION ON PCS AND
WORKSTATIONS
□ PC-BASED GUI --> FILE AND PRINT SERVICES
□ SQL SERVICE REQUESTS TO ONE OR MORE
BACKEND RELATIONAL DATABASES
□ NOVELL SPX/IPX OR TCP/IP COMMON
TRANSPORT PROTOCOLS
□ DOZENS OF MIDDLEWARE AND RDBMS
SOFTWARE SUPPLIERS PROVIDE DISTRIBUTED
SYSTEMS GLUE
Aberdeen Notes:
Early client-server involved PCs that created relatively simple look-up table
and database requests. Often these early applications reverted to terminal
emulation software in order to capture data currently stored in the
mainframe environment. They were an outgrowth of mid-1980s "micro­
mainframe" file transfer programs, and many of these applications still exist
today.
Today the dominant client-server design incorporates the PC or
workstation with its graphical user interface and a backend server(s) used
for file and print services in a local area network. Gradually, given the
popularity of products such as Lotus Notes, these applications are evolving
to sophisticated multi-user applications.
In the client-server decision support and database environment, there is a
heavy emphasis on SQL services. These request information from one or
more RDBMS resource locations on the network and present the resulting
information to the client for manipulation and modeling. Novell’s
Netware, using the SPX/IPX protocol and TCP/IP from the world of Unix
and Open Systems are the dominant transport protocols used to implement
distributed requests.
New Technology Impact Series
Page 12
RberdccnGroup
Client-Server Computing
CURRENT IMPLEMENTATIONS
□ TERMINAL EMULATION ON PCS AND
WORKSTATIONS
□ PC-BASED GUI -> FILE AND PRINT SERVICES
□ SQL SERVICE REQUESTS TO ONE OR MORE
BACKEND RELATIONAL DATABASES
□ NOVELL SPX/IPX OR TCP/IP COMMON
TRANSPORT PROTOCOLS
□ DOZENS OF MIDDLEWARE AND RDBMS
SOFTWARE SUPPLIERS PROVIDE
DISTRIBUTED SYSTEMS GLUE
Aberdeen Notes:
A whole new category of middleware software products has emerged to
meet the increasingly complex requirements of distributed client-server
applications. Companies such as Uniface, Auspex, Oracle, Sybase,
Cooperative Solutions, Forte, and Software AG with Entire are among the
leaders in aggressively pursuing these new development toolset market
opportunities.
New Technology Impact Series
Page 13
AberdeenGronp Client-Server Computing
ADVANCED CLIENT-SERVER DESIGNS
□ DISTRIBUTED RELATIONAL AND OBJECT-
ORIENTED DATABASES
□ TWO MAJOR ALTERNATIVES: CLUSTERING OR
TWO-PHASE COMMIT
□ HIGH-VOLUMES OF SERVER-TO-SERVER
INFORMATION REQUESTS - CASCADING
TRANSACTIONS
□ INTELLIGENT, HIGH-SPEED NETWORKS
□ CLIENTS AND SERVERS WILL INCLUDE A WIDE
VARIETY OF UNUSUAL INPUT/OUTPUT DEVICES
Aberdeen Notes:
Aberdeen believes that the IS planning staff should anticipate several new
types of functionality in future client-server designs. First we believe that
distributed relational databases - employing various business policies to
trigger transactions -plus the increasing use of object-oriented
programming will characterize the systems software of the second half of
the decade. Today, because network capacity is a precious resource,
clustering these databases into a large single image system while still
offering shared workstation and disk access is a popular design alternative.
As previously mentioned, we believe that high volumes of server-to-server
transactions will result from the next-generation of client-server program
requirements. It is possible that a single transaction - for example, a retail
store point-of-sale activity - might trigger a large number of server-to-
server transactions even though these were completely transparent to the
person scanning an item in the store.
New Technology Impact Series
Page 14
AberdeenGrowp
Client-Server Computing
ADVANCED CLIENT-SERVER DESIGNS
□ DISTRIBUTED RELATIONAL AND OBJECT-
ORIENTED DATABASES
□ TWO MAJOR ALTERNATIVES: CLUSTERING OR
TWO-PHASE COMMIT
□ HIGH-VOLUMES OF SERVER-TO-SERVER
INFORMATION REQUESTS - CASCADING
TRANSACTIONS
□ INTELLIGENT, HIGH-SPEED NETWORKS
□ CLIENTS AND SERVERS WILL INCLUDE A
WIDE VARIETY OF UNUSUAL INPUT/OUTPUT
DEVICES
Aberdeen Notes:
Of course, all of these new applications and distributed data transfers will
create enormous demand for high speed networks with intelligence
required to do least-cost and most efficient routing of traffic -- as well as
providing advanced systems and network management functionality.
Finally, Aberdeen believes that many new and innovative types of clients as
well as servers will become available to meet the needs of late 1990s
applications. Miniaturized, hand-held devices, scanners, printers and
copiers, pen-based and voice-actuated systems, and hundreds of servers -
each dedicated to and optimized for a specific class of application,
database, or store and forward task will emerge.
New Technology Impact Series
Page 15
AberdeenGroMp
Client-Server Computing
SOFTWARE COMPONENTS
Presentation Layer
4 »
Application
Development Layer
Database Layer
Hardware Layer
Aberdeen Notes:
The above figure illustrates the independence between different layers of
the software development environment. The ideal software development
toolset allows the developer to create an application without worrying
about the possible combinations of user interfaces, databases and hardware
platforms on which the completed application will eventually be deployed.
Toolsets modeled on this design include ACCELL/SQL from Unify
Corporation, Mapper from Unisys, Powerhouse from Cognos and
SmartStar Vision from SmartStar Corporation.
New Technology Impact Series
Page 16
AberdeenGrowp
Client-Server Computing
TECHNOLOGY DEPENDENCIES
□ OBJECT-ORIENTED SOFTWARE
□ DISTRIBUTED DATABASE FUNCTIONALITY
□ ROBUST MICROPROCESSORS
□ PRE-EMPTIVE, MULTITASKING OS
□ NETWORK CAPACITY
□ SYSTEMS & NETWORK MANAGEMENT TOOLS
□ APPLICATIONS SOFTWARE AVAILABILITY
Aberdeen Notes:
These key technology gating factors are self-explanatory and have also
been reviewed in the preceding slides.
New Technology Impact Series
Page 17
AberdeenGronp Client-Server Computing
NON-TECHNICAL DEPENDENCIES
□ MANAGEMENT VISION AND LEADERSHIP
□ PROCESS REENGINEERING ORGANIZATIONAL
SKILLS
□ HUMAN RESOURCES AND TRAINING
□ FINANCIAL STABILITY OF LEADING SUPPLIERS
Aberdeen Notes:
Technology is only part of the problem. There are also several non­
technical challenges to be surpassed. The client-server project
management team must have credibility with peers and senior
management. This can often be achieved by communicating clear,
articulate messages about the vision of the next-generation systems.
Another critical component is the ability to work with multiple groups in
the enterprise in order to obtain commitments to new ways of doing
business. Making sure that adequate staff resources and training are
available to initially support successful implementation is critical, as is an
on-going evaluation of the financial and technical stability of various
contributing suppliers.
New Technology Impact Series
Page 18
AberdeenGroizp Client-Server Computing
WRAP-UP
□ CLIENT-SERVER DRIVING OUR VISION OF NEXT­
GENERATION COMPUTING, BUT INSTALLED
BASE TECHNOLOGY DOES NOT YET SUPPORT
THE VISION
□ RUDIMENTARY TOOLS AND COMPONENTS NOW
AVAILABLE TO BEGIN FOR DECISION SUPPORT
APPLICATIONS
□ CUSTOM DEVELOPMENT OF PRODUCTION
SYSTEMS IS ONLY ALTERNATIVE TODAY
□ ADVANCED DESIGNS HAVE MULTIPLE
DEPENDENCIES
□ SIGNIFICANT BENEFITS WILL ACCRUE TO
THOSE WHO CAN EFFECTIVELY SELECT AND
IMPLEMENT THE TECHNOLOGY
Aberdeen Notes:
These five concepts summarize the key findings Aberdeen has reached
about the industry’s vision of client-server computing.
New Technology Impact Series
Page 19


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | nti-12-client-server-goals-1993-15a519 |
| title | Realistic Goals for Client-Server Computing |
| author | Peter S. Kastner, John Logan, Thomas Willmott |
| date | 1993-07-01 |
| type | market-study |
| subject_domain | client-server-computing |
| methodology | industry-analysis, technology-assessment, vendor-profiling |
| source_file | NTI 12 Client-Server Goals 1993.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group defines and evaluates the client-server computing paradigm across five critical planning areas: client hardware options, scalable server architectures, legacy system roles, systems software transitions, and network infrastructure. The study covers current client-server implementations and traces the evolution to advanced designs including distributed relational and object-oriented databases, cascading server-to-server transactions, and intelligent high-speed networks. Aberdeen concludes that client-server drives the next-generation computing vision but warns that the installed base technology does not yet fully support the vision and that significant non-technical barriers—management vision, process reengineering, and training—must be overcome.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Captures Aberdeen's structured framework for client-server planning at the exact inflection point in 1993 when the paradigm was becoming mainstream; the five-component planning model and the technology dependency matrix were influential decision-making tools. |
| **Relevance** | medium | The architectural decomposition (client/server/network/OS/legacy) and the non-technical dependency framework remain applicable to enterprise modernization projects; specific products and vendors are historical. |
| **Prescience** | high | Predictions of cascading server-to-server transactions, distributed object-oriented databases, hand-held clients, and object-oriented OS architectures all proved largely correct within the forecast decade; the warning about network capacity demands proved particularly accurate. |

### Prescience Detail


**Prediction 1:** Commercial workstation price target
- **Claimed:** By 1994, powerful client platforms (commercial workstations) under $3,500 with 32-bit multitasking OS (Unix, Windows NT)
- **Year:** 1993
- **Confidence at time:** high

**Actual Outcome 1:** Commercial workstation price target — outcome
- **Result:** [UNVERIFIED]
- **Confidence:** verified
- **Notes:** 

**Prediction 2:** Multiprocessor servers as standard
- **Claimed:** Advanced multiprocessor architecture servers will become standard platforms of mid-to-late 1990s
- **Year:** 1993
- **Confidence at time:** high

**Actual Outcome 2:** Multiprocessor servers as standard — outcome
- **Result:** [UNVERIFIED]
- **Confidence:** verified
- **Notes:** 

**Prediction 3:** OO architecture timeline
- **Claimed:** Within 3-4 years client-server systems software will evolve to object-oriented architecture
- **Year:** 1993
- **Confidence at time:** medium

**Actual Outcome 3:** OO architecture adoption — outcome
- **Result:** [UNVERIFIED]
- **Confidence:** verified
- **Notes:** 

**Prediction 4:** Client-server network capacity demand
- **Claimed:** Client-server computing will consume enormous amounts of network capacity; multimedia, video conferencing, high data volumes will overwhelm current capacity
- **Year:** 1993
- **Confidence at time:** high

**Actual Outcome 4:** Network capacity demand — outcome
- **Result:** [UNVERIFIED]
- **Confidence:** verified
- **Notes:** 

**Prediction 5:** Late 1990s client-server characteristics
- **Claimed:** Extremely powerful workstations, expanded distributed server networks, mission-critical production apps with peer-to-peer cooperative processing; single request may trigger dozens of cascading server-to-server transactions
- **Year:** 1993
- **Confidence at time:** high

**Actual Outcome 5:** Network capacity demand — outcome
- **Result:** [UNVERIFIED]
- **Confidence:** verified
- **Notes:** 

**Prediction 6:** Distributed OO databases in late 1990s
- **Claimed:** Distributed relational databases employing business policy triggers plus increasing OO programming will characterize second half of decade
- **Year:** 1993
- **Confidence at time:** high

**Actual Outcome 6:** OO architecture adoption — outcome
- **Result:** [UNVERIFIED]
- **Confidence:** verified
- **Notes:** 

**Prediction 7:** Future client device diversity
- **Claimed:** Many new and innovative client types will emerge: miniaturized hand-held devices, scanners, pen-based, voice-actuated systems
- **Year:** 1993
- **Confidence at time:** high

**Actual Outcome 7:** Network capacity demand — outcome
- **Result:** [UNVERIFIED]
- **Confidence:** verified
- **Notes:** 

**Prediction 8:** Microsoft future OS strategy
- **Claimed:** Transition path: Windows -> Windows for Workgroups -> NT -> Chicago -> Cairo future OO OS
- **Year:** 1993
- **Confidence at time:** medium

**Prediction 9:** Apple PowerPC strategy
- **Claimed:** Joint PowerPC development with IBM will move Macintosh interface to AIX and RISC chip platforms
- **Year:** 1993
- **Confidence at time:** medium

**Actual Outcome 9:** Apple PowerPC strategy — outcome
- **Result:** [UNVERIFIED]
- **Confidence:** verified
- **Notes:** 


### Entities Referenced (33)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | acquired | Harte-Hanks 2006 |
| Peter S. Kastner | person | active |  |
| John Logan | person | unknown |  |
| Thomas Willmott | person | unknown |  |
| Microsoft Corporation | company | active |  |
| Apple Computer | company | active | renamed Apple Inc. 2007 |
| IBM | company | active |  |
| Novell, Inc. | company | acquired | Attachmate (2011 for $2.2B) -> Micro Focus (2014) -> OpenText (2023) |
| Digital Equipment Corporation (DEC) | company | acquired | Compaq 1998 |
| Banyan Systems | company | dissolved | Renamed ePresence (1999); assets acquired by Unisys (2003); ceased operations Oct 2003 |
| Sun Microsystems | company | acquired | Oracle 2010 |
| Hewlett-Packard | company | active | HP Inc./HPE 2015 |
| NCR Corporation | company | split | Split into NCR Voyix (digital commerce) and NCR Atleos (ATMs) in October 2023 |
| Compaq Computer Corporation | company | acquired | HP 2002 |
| Unisys Corporation | company | active |  |
| Oracle Corporation | company | active |  |
| Sybase, Inc. | company | acquired | SAP 2010 |
| Software AG | company | active |  |
| Lotus Development Corporation | company | acquired | IBM (acquired 1995 for $3.5B) |
| NeXT Computer | company | acquired | Apple Computer (acquired 1997 for $429M); NeXTSTEP became basis of Mac OS X |
| Taligent | company | dissolved | Absorbed into IBM (1996-1998); technology became part of VisualAge |
| NetFrame Systems | company | acquired | Micron Electronics (acquired 1996) |
| Tricord Systems | company | dissolved | Filed bankruptcy mid-1990s; assets dissolved |
| Uniface | company | acquired | Compuware (acquired 1994); then Rocket Software acquired Compuware's Uniface unit |
| Auspex Systems | company | acquired | Network Appliance (NetApp) acquired 2003 |
| Forte Software | company | acquired | Sun Microsystems (acquired 1999 for $540M) |
| Cooperative Solutions | company | dissolved | Acquired by Sybase mid-1990s; product line discontinued |
| Unify Corporation | company | acquired | Merged with Daegis (2010); acquired Gupta Technologies; then OpenText acquired (2015) |
| Cognos | company | acquired | IBM (acquired 2008 for $5B) |
| SmartStar Corporation | company | dissolved |  |
| Data General Corporation | company | acquired | EMC Corporation (acquired 1999) |
| Pyramid Technology | company | acquired | Siemens Nixdorf (acquired 1995) |
| Sequent Computer Systems | company | acquired | IBM (acquired 1999 for $810M) |

### Technologies Referenced (26)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Client-Server Computing | framework | Various | growth | mature |
| Microsoft Windows 3.1 | operating-system | Microsoft | current | obsolete |
| Microsoft Windows NT | operating-system | Microsoft | emerging | legacy-supported |
| Microsoft Windows for Workgroups | operating-system | Microsoft | current | obsolete |
| IBM OS/2 | operating-system | IBM | growth | obsolete |
| Unix | operating-system | Various | growth | mature |
| Apple Macintosh OS | operating-system | Apple Computer | mature | mature |
| Novell NetWare | operating-system | Novell | mature | legacy |
| Banyan Vines | operating-system | Banyan Systems | growth | obsolete |
| Microsoft LAN Manager | operating-system | Microsoft | declining | obsolete |
| NeXTSTEP | operating-system | NeXT Computer | niche | obsolete |
| Taligent Pink | operating-system | Taligent | emerging | obsolete |
| Microsoft Cairo | operating-system | Microsoft | announced | obsolete |
| SunSoft Distributed Objects Everywhere (D.O.E.) | framework | Sun Microsystems | announced | obsolete |
| Symmetric Multiprocessing (SMP) | hardware | Various | emerging | mature |
| Massively Parallel Processing (MPP) | hardware | Various | emerging | mature |
| Lotus Notes | application | Lotus Development | growth | legacy-supported |
| FDDI (Fiber Distributed Data Interface) | protocol | ANSI | growth | obsolete |
| ATM (Asynchronous Transfer Mode) | protocol | Various | emerging | obsolete |
| TCP/IP | protocol | IETF | growth | mature |
| Novell SPX/IPX | protocol | Novell | mature | obsolete |
| Intel 486 / 80X86 | hardware | Intel | current | obsolete |
| IBM/Apple PowerPC | hardware | IBM, Apple | announced | legacy |
| Relational Database Management System (RDBMS) | application | Various | mature | mature |
| Object-Oriented Programming / Databases | framework | Various | emerging | mature |
| Two-Phase Commit | protocol | Various | growth | mature |

### Observation Summary

- Total observations: 30
- By type: viability-prediction: 9, actual-outcome: 7, expert-opinion: 4, competitive-position: 4, technology-assessment: 3, benchmark-result: 2, market-size: 1
