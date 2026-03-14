# Object-Oriented Three-Tier-Plus Computing: Client-Server for Adults

> Archived from: https://web.archive.org/web/19970112011033/http://www.aberdeen.com:80/secure/whtpaper/3tier/3tier.htm
> Original publication date: 1996-02-01
> Author: Aberdeen Group

---

## Original Document Text

Object-Oriented Three-Tier-Plus Computing
Client-Server for Adults
An AberdeenGroup Whitepaper
February 1996
Table of Contents
I Executive Summary
II Three-Tier Computing: Meeting Real Customer Requirements
III Evolving Information Systems Architectures
IV Relevance of Object Technology
V Aberdeen Field Research
VI Aberdeen Conclusions
I Executive Summary
Recognizing Business Priorities
Senior management in both the public and private sectors has reached the conclusion that productivity improvements, increased customer satisfaction and revenue enhancement are the likely
outcomes of an effective information systems (IS) strategy. Furthermore, both line-of-business and technology executives are convinced that if they base new strategic enterprise applications
on a Three-Tier, client-server architecture, it will help them achieve several speciﬁc goals. These include:
Maximizing the return on information systems technology;
Reducing risks by using proven technology designs; and
Aligning information systems planning priorities with important business goals and objectives.
Despite signiﬁcant technological progress by industry suppliers in delivering robust, open, distributed systems, a variety of technological training and educational challenges remain. And
despite senior management buy-in to the concept of 3-Tier client-server computing, Aberdeen's ﬁeld research shows that many business and IS executives want additional insights and
analysis on how others have successfully implemented these projects before they are willing to launch projects of their own. Once executives are armed with proof points, insights, tips and
proven techniques -- staff training, system design and deployment is greatly facilitated.
This white paper has been prepared to provide an implementation trends update for management. In it, Aberdeen will present its ﬁndings on how and why customers are implementing 3-Tier
client-server systems. We will describe variations of the multi-tier architectural theme and discuss how these variations have evolved. Aberdeen will also address important software issues,
and demonstrate why object-oriented programming techniques, which enable developers to easily partition and deploy application components across a multiple-tier environment, are critical
to the implementation of 3-Tier systems. The report concludes with highlights of signiﬁcant research ﬁndings drawn from Aberdeen consulting assignments and ﬁeld interviews with senior
executives.
Why Three-Tier Computing?
When Aberdeen last addressed the issues of open systems and 3-Tier computing in a similar white paper in mid-1992, we were optimistic about the potential for these emerging technologies
and architectures. However, the deﬁnition of 3-Tier client-server has been a moving target -- constantly changing as the industry continues to shift from centralized, shared-logic-based
systems to networks of PCs, workstations and servers supplemented by powerful new software development toolsets.
With every new product launch, standards committee position paper or supplier product presentation; the transition seemed to have become more confusing and complicated, rather than
simpler and clearer. But despite this ever-changing technology landscape, we do have more facts and case studies than we did 3 years ago to demonstrate what it takes to successfully
implement a next-generation systems project. Some patterns have clearly emerged.
Today, the base hardware and RDBMS platforms that so confused the industry in 1992, are stable, reliable and much better understood. Many of the missing pieces from three years ago,
such as object-oriented programming tools, software testing capabilities, improved transaction processing performance, data replication and synchronization, systems and network
management software, and reliable networks, are now in production. Additionally, an industry infrastructure of related staff skill sets and distribution channels has matured to the point that
adequate software development, network design and other supporting services are becoming available. Given the initial work that ISVs have done to develop their own applications using the
3-Tier architecture, customers now have a wide variety of packaged applications to choose from to supplement those developed in-house.
The proven beneﬁts of a 3-Tier client-server architecture are easily understood. In bulleted form, they include:
freedom to select from a wide range of hardware, software and networking components;
interoperability among all the leading suppliers' products;
the ability to share information across the enterprise; and
the ﬂexibility to adapt computer systems to rapidly changing business conditions.
In short, we have sufﬁcient evidence for information systems executives to proceed with conﬁdence. The technology direction is clearer now. The products are more powerful and less
expensive than ever before.
Back to Table of Contents

II Three-Tier Computing: Meeting Real Customer Requirements
Executives have aggressive goals for improved proﬁtability, productivity and overall enterprise performance -- and computer technology is expected to play a pivotal role in achieving these
new business objectives.
In order to support the notion of pervasive computing, there are several ways in which customers have begun to measure the effectiveness of their information systems. It is no longer
sufﬁcient, for example, to invest large sums of money in mainframe systems that simply maintain records in support of manual processes. Instead, the effective organization wants to
integrate its new computer applications directly into the work process.
The question for any systems architecture is therefore, "How can we most effectively align our business objectives with accelerating investments in technology?" Aberdeen has identiﬁed four
major customer requirements that have become benchmarks for measuring success with the 3-Tier design. Each of these represents a critical objective for the second half of the 1990s.
1. Building New Computer Systems to Improve Enterprise Efﬁciency
Perhaps the most pressing industry agenda item is the creation of systems that automate business information ﬂows, improve productivity, add revenue opportunities and cut costs. For
several decades, data processing organizations have provided computer systems that were designed to support manual, paper forms-driven business routines. More often than not, these were
mainframe-based, batch applications -- complete with duplicated data entry routines. The applications created data ﬁles and printed reports that provide an historical record of the process -- a
snapshot of how things stood at a particular moment in time. The cost of the mainframe was viewed as excessive -- especially because the applications portfolio only provided a rudimentary
level of business process integration and management functionality.
Forward-looking organizations are now demanding that computer systems do more to automate and improve the process itself rather than simply keeping an accounting record of each
transaction. For example, with vastly increased hardware performance, declining prices and the emergence of more powerful software development toolsets, new applications can now be
built that actually create and ﬁll in electronic forms rather than requiring data elements like name, address, and social security number to be transferred from paper forms in a tedious, time-
consuming, manual procedure.
In another example, using a 3-Tier topology the computer system can instantaneously present insurance claims adjusters with relevant policy information and an electronic photograph of
damage to support the claim rather than making them wait for a mis-routed paper ﬁle.
Advanced computer systems can also balance departmental workloads by organizing and prioritizing existing job queues and staging the most appropriate assignment for the next available
worker. And these systems can provide real-time access to multiple sources of information in databases throughout a global network.
Powerful new applications such as these can be crafted today from a combination of workﬂow management software, automated business rules and policies, database triggers, threshold-
invoked subroutines, remote procedure calls, and other signiﬁcant new computing technologies. Rather than being forced to deploy these applications on a single type of computer hardware,
3-Tier computing permits the ﬂexibility to use the right size system with the most appropriate hardware architecture for the job. For this reason, a completed 3-Tier application results in an
empowered workforce -- in the warehouse, on the factory ﬂoor, at the airport airline reservation counter, or in the accounting department.
2. Providing Optimal Access to Multiple Sources of Information
With earlier systems and software architectures, it simply wasn't possible to access information -- except as this data was presented in the rigid format manually coded in the original
computer program. 3-Tier architectures provide for a wide range of more ﬂexible options. First and most important, PC software packages concentrate full attention on various methods of
creating and modeling information right at the user's desktop.
Second, the LAN and mid-tier server layer offer powerful relational databases whose core design characteristic is ﬂexible data access for decision support. A variety of data warehousing
products have been introduced to collect and consolidate data from all the major system components in the network so that the user may organize and manipulate the information as required
to meet a speciﬁc business challenge.
With a 3-Tier architecture, distributed computing becomes a reality, and the customer has access to multiple sources of information to support work in progress with real-time information
access. Given an emerging class of internet browsers and industry emphasis on Internet related research and development, Aberdeen expects the information access component of 3-Tier to
explode with additional functionality, ease of use and network throughput performance.
3. Scaleable Products that Easily Incorporate Emerging Technologies
Innovation and change are the only constants in the information processing industry. Over the coming years, even more new products and services will be introduced. Customers will want to
selectively add these to their existing platforms, software applications portfolio, and networking infrastructure. From handheld, mobile computing devices to massively parallel
supercomputers, to wireless LANs and high speed, bandwidth-on-demand networking services, to voice-actuated text processing, real-time server-to-server synchronization and widespread
use and reuse of software objects -- users will demand that new technologies be easily integrated into their existing infrastructure.
Of course, businesses accept that the rapid pace of change implies a measure of product obsolescence. However, executives charged with planning are less forgiving when products simply hit
a dead end or turn out to be incompatible with one another. The ability to make graceful, gradual transitions to next-generation products and solutions is seen as a fundamental industry
success factor. A single illustration of the point is the fact that scaleable servers and clustering -- offering board-level upgrades and high-speed server-to-server communications -- continue to
gain in popularity. This, in turn, signiﬁes that symmetric multiprocessing hardware has gained credibility and become the architectural workhorse of the server market.
Other examples of scalability and ease of transition include a modular development environment in which applications can be maintained and modiﬁed with the fewest possible staff
resources and in the shortest amount of time. The use of object technology and application partitioning to accomplish this is discussed in a following section.
The gradual and graceful evolution to new technologies provides investment protection for customers and permits information systems staff to stay current with a multitude of technologies
with the least expenditure of time and energy.
4. Achieving Superior Return on Investment
Given the ﬁerce nature of international competition, businesses will continue to focus on intermediate-term cost justiﬁcation of new information system projects. This means that executives
are willing to invest in technology in order to achieve a business objective -- without necessarily knowing the total impact of expense reduction on Day 1. They invest simply because their
management instincts tell them automation is the appropriate strategy. But this does not mean that the customer is price insensitive, that price/performance is insigniﬁcant, or that business
results are not a high priority.
Although customers are enthusiastic about acquiring new technology to improve productivity, reduce expenses, improve customer satisfaction, and add top-line revenue, they must also
continue to demonstrate these paybacks to management. While precise cost justiﬁcations, including items like head-count reductions or quarterly revenue increases, are not typically required
when launching a 3-Tier client-server initiative, Aberdeen's research does indicate that management wants information systems people to think like business people -- not just technologists.
Three-Tier architectures offer a superior return on investment for several reasons. First, new applications can be deployed on PCs, PC LANs, and mid-tier servers which come in a nearly
inﬁnite range of types and sizes -- each offering signiﬁcant price/performance improvements over previous generations. Service and support costs are also signiﬁcantly lower for these new
microprocessor-based systems. Most important, a new generation of software tools, relational databases, and packaged applications are now available to run on these powerful systems --
greatly adding to development ﬂexibility, rapid application prototyping and ease of maintenance to the 3-Tier solution.

Another reason for the attractiveness of 3-Tier designs is that the customer is not forced to abandon current computer systems or release trained staff in order to begin the transition to new
architectures. Existing applications that are running effectively on installed third-tier servers need not be changed or will require only minor modiﬁcations in the new environment. These
production applications can gradually be retired when the new systems duplicate the functionality of the old ones.
Meanwhile, connections between new 3-Tier software and existing dataﬁles can be built with application programming interfaces (APIs). Thus, if an existing batch- or host-based multiuser
application is performance-tuned and meeting its business objectives, it need not be immediately rewritten in order to implement a 3-Tier distributing computing architecture. This offers the
customer maximum convenience and signiﬁcant expense relief.
Back to Table of Contents
III Evolving Information Systems Architectures
Three-Tier Plus
The information systems architecture of the mid-1990s is typically organized into three processing layers, or tiers of computing. Figure 1 illustrates a typical 3-Tier Plus hardware
implementation found in many large enterprises. It is important for customers to understand that a 3-Tier software architecture must also be created. A modular software application may or
may not require all three hardware layers. The hardware and software architectures are related, but different.
Figure 1 - Three Tier Hardware Architecture
Source: AberdeenGroup, February 1995
Enterprise Systems
Enterprise systems deﬁne the top (or third-tier) in the architecture and include all the organization's mainframes and other multi-user computers now deployed for both batch and online
production systems. Consolidation has occurred in this market, but the segment is now stable with single-digit growth both for suppliers of mainframes as well as traditional high-end
minicomputer replacement models and technology upgrades. Aberdeen believes that enterprise systems will continue to play a major role in the corporate information-processing
infrastructure because they will be used as servers for high-volume transaction processing, especially where robust performance, security, and reliability are key IS objectives.
Of course, the application mix on enterprise systems will change over the next several years as major new applications are developed and as older, ﬁrst-generation software programs are
gradually moved from the multi-user host to distributed-processing nodes in a development process called application partitioning. Despite this trend, Aberdeen has observed that leading
systems suppliers are continuing to incorporate powerful CMOS semiconductor fabrication technologies into their product lines and to reduce prices. This means that customers will not be
forced to abandon their core data center applications at too frantic a pace.
The multi-user host still offers critical performance functionality, including data capture, batch reporting, central information repository services, and can act as a communications store-and-
forward device. Aberdeen believes these capabilities will continue to be critical to enterprise computing for the next ﬁve years.
Departmental and Replicated Branch Systems
The middle tier in a 3-Tier architecture is represented by a micro-processor-based (often SMP-enabled) hardware platform and plays several important roles. In the mid-1980s, these
machines were introduced as departmental servers in order to up-size a new class of decision-support applications that were developed in a prototype form on personal computers. In other
words, early LAN servers and network operating systems focused on simple ﬁle and print services -- leaving relational database (RDBMS) and multiuser application implementations to the
more powerful middle tier.
From a timeline perspective, replicated applications were introduced next. These distributed systems, including branch banking, insurance agency management, and retail point-of-sale
systems were the ﬁrst of a new class of mission-critical, MIS department-developed applications to be deployed on the middle tier.
Recently, middle-tier servers (typically outﬁtted with an RDBMS) have been pressed into service as store-and-forward devices as well as the platforms on which a wide range of new
applications are executed in the 3-Tier architecture.
In this example, the mid-range machine is used to download ﬁles from the enterprise multiuser host. These ﬁles are then prepared for processing by an employee using a client device in the
PC LAN environment. The reverse is also true. As new data is captured by the PC, it may be uploaded to the mid-range server and held for later consolidation with other departmental ﬁles at
the enterprise system tier in the architecture. Additionally, data gathered by the PC LAN or information downloaded from the mainframe can also be manipulated and analyzed by
applications written for the mid-range tier.
PC and Workstation Clients
The ﬁrst tier is represented by personal computers and workstations clustered together in a local area network. Clearly, this conﬁguration is enormously popular and well understood. Some
25 million business client workstations were shipped worldwide in 1995 and while industry growth rates have pulled back from the torrid pace of several years ago, the PC and workstation
are still the dominant industry market segment. Perhaps most important, the workstation or PC client -- with its inherent processing capabilities -- is redeﬁning the applications software
portfolio of every enterprise information systems organization. Aberdeen addresses this in the client-server section below.
Three-Tier Enhancements

Some organizations are adding a new dimension to the traditional 3-Tier hardware architecture. The "Plus" in Aberdeen's "Three-Tier Plus" description stands for the introduction of
massively parallel or clustered SMP machines as an incremental data-processing resource. These computers, based upon tens -- and sometimes hundreds -- of microprocessor components
combined in a single machine, offer on-line access to large numbers of users for complex query and data warehousing projects as well as support for scientiﬁc or numerically-intensive
compute server applications.
The historical challenge with this type of massively parallel architecture is that each software application needs to be custom developed in order to run on the many, loosely-coupled
processors. This parallelization of software involves signiﬁcant programming energy, time and expense. Nevertheless, as popular relational databases such as Oracle and Informix are ported
and tuned, as other software development toolsets mature, and as prices for these systems continue to decline, Aberdeen believes that massively parallel machines will achieve broader
market acceptance as enterprise-class servers. In the meantime, other innovative architectures, including 64-bit architectures that permit an entire database to run in memory offer the
customer a unique performance advantage for several classes of complex query applications.
The Middle-Tier Operating System
At those sites where 3-Tier applications were being implemented on a 3-Tier hardware architecture, Aberdeen found a number operating systems vying for dominance on the mid-tier
platform, including all the ﬂavors of Unix, NT Server, OS/2 Warp Server and OpenVMS.
From a systems software perspective, in early 1996 the performance distinction between a middle-tier departmental server and a LAN server is beginning to blur. Because the traditional
systems have been ﬁeld tested over the last decade in customer production environments on the middle tier, and because a wide range of software utilities are now available to enhance these
systems, applications on these systems tend to be superior for higher-volume transaction processing, especially on 4-to-8-way SMP conﬁgurations, when compared to Microsoft's NT Server.
But Aberdeen believes that for application servers, NT-based systems will begin to close the sales gap over the next 24 months, and will at least begin to equal unit sales of other operating
systems in the workgroup environment.
Already, for example, NT Server (witinterconnect services to Novell NetWare) is beginning to dominate new LAN server shipments. And, the NT Server as well as IBM's OS/2 Warp Server
operating environments offer application services superior to previous network operating systems.
The Role of Client-Server
Client-server is perhaps best understood as a new method for designing and delivering software applications. While this popular approach is often implemented on a 3-Tier hardware
topology, the notion of client-server computing actually has more to do with software architectures than hardware platforms.
For example, in a traditional, shared-logic computing model, a single, centralized host machine is responsible for processing almost 95% of the program logic. Attached dumb terminals in
this conﬁguration simply pass keystrokes to control central -- the host central-processing unit. Make no mistake, this traditional approach is powerful and still a dominant force in a majority
of commercial, enterprise-wide, production information system applications. However, the industry is increasingly moving to interactive applications, especially those with an emphasis on
large data transfers supporting graphical user interfaces. In this environment, the shared-logic system is rather quick to suffer signiﬁcant performance degradation and encounter bottlenecks
in network bandwidth. As trafﬁc to and from the CPU increases, response times deteriorate rapidly.
As more PCs are installed in end-user departments and as more processing responsibility is transferred from the host to intelligent workstations and distributed midrange servers dedicated to
speciﬁc applications, the residual value of the mainframe software portfolio will continue to decline during the second half of the 1990s. Information systems executives are looking for more
ﬂexible and higher-performance architectures for deploying next-generation business systems. This is a major catalyst in the growing popularity of 3-Tier topologies with client-server
software designs.
Despite growing market momentum, the reality is that an evolution to client-server application development is only occurring gradually. Aberdeen has observed that there are several natural
stages in the transition to true client-server production applications. Of course, the most popular use of a client device is when the PC simply manipulates information with its own
application software. This PC activity is completely self-contained -- the intelligent workstation processes data independently of any other servers or traditional shared-logic mainframe
resources -- despite the fact it may be connected to them on the network.
The ﬁrst real sign of client-server is when the PC -- with its full complement of application software packages -- is more tightly integrated with ﬁle and print servers via the local area
network. Much early client-server prototyping occurs at this workgroup level in order to create a variety of innovative, departmental applications. The LAN environment is likely to consist
of one or more of the popular network operating systems, plus Unix, Microsoft NT and/or various other vendor-speciﬁc operating software. In particular, several of the traditional
minicomputer suppliers have successfully integrated the PC LAN environment with their existing proprietary systems. This strategy permits the customer to choose when to migrate from
stable, installed applications, rather than forcing a premature migration made even more complicated because the enterprise also lacks internal staff resources with expertise in emerging
technologies.
In succeeding stages, client-server applications combine the data entry, modeling, and queries produced on the PC with data stored on a LAN, departmental, or third-tier enterprise server.
Typically, this integration has been based upon relational database and structured query language (SQL) technology components, where the request for services is made by the client and the
server responds with rapid processing of the transaction.
In addition to having a PC make a simple request to a single server, there are many other powerful forms of the basic client-server design. In a customer-service application, for example, a
one-to-many relationship might be required where the client requests information from multiple servers across the corporate network and assembles the results into a sophisticated decision-
support system. And in the future, Aberdeen notes that progressive customers with 3-Tier architectures are already developing sophisticated server-to-server software systems.
In these environments, based upon triggers and stored procedures, requests for certain services may well create database conditions that cause a cascade of additional transactions throughout
the network. This means that a single client-server process such as a retail point-of-sale event may create database conditions that produce automated requests for additional services such as
inventory replacement -- even though these incremental transactions are likely to be completely transparent to the original client-server user. In the next section, Aberdeen will describe some
of the software technologies that make these powerful and exciting applications possible today.
Back to Table of Contents
IV Relevance of Object Technology
Over the last few years, the use of objects has found its way out of the laboratory and into real-world applications. Nowhere is this more apparent than in the development and
implementation of 3-Tier systems. On a regular basis Aberdeen conducts in-depth ﬁeld research interviews with senior IS executives and their staff. A consistent theme is the use of object
technology for building ﬂexible 3-Tier client-server applications that can be easily modiﬁed to reﬂect changing business conditions. To fully understand why objects are the most appropriate
software development approach for 3-Tier systems, the basics of object technology must be understood.
The most fundamental difference between object technology and the more traditional, procedural programming approach is that objects combine data and algorithms into a single, self-
contained software module. Objects are essentially software building blocks that are linked together to form a working client-server application.
Figure 2: Three-Tier Application Architecture

Source: Digital Equipment Corporation, February 1995
Each object is accessed through a well-deﬁned interface, which contains a description of the functions and services provided by the object and how those services can be accessed. This
interface acts as a buffer between each object's unique data and algorithms (also called the object implementation) and the rest of an application. As long as the interface remains unaltered,
modiﬁcations can be made to the implementation of an object without requiring any changes to the other objects that comprise an application. This compartmentalization is impossible in the
procedural world, where "spaghetti code" requires developers to spend tedious hours tracking down all the possible ramiﬁcations that a change to a single line of code may entail.
Aberdeen believes the inherent modularity of object-oriented software provides the following advantages when applied to a 3-Tier client-server architecture:
Application Partitioning -- 3-Tier applications are distributed across multiple, heterogeneous hardware platforms. As systems evolve, certain components of an application may be re-
hosted to take advantage of new hardware or network topologies, or to provide services to additional groups within the enterprise. Users interviewed by Aberdeen state that object-
oriented code is much easier to partition and distribute across the network -- a major advantage when building applications that need to constantly adapt to new market conditions.
Sharing of Data and Services -- An object's interface, through which its data and services are accessed, provides a standardized communications mechanism. As a result, it is much
easier for developers to take advantage of existing software resources because the same syntax is used to communicate with multiple objects. For example, an organization's
procurement and ﬁnancial systems can access the same object-oriented services that consolidate the inventory in a warehouse.
Easier Maintenance -- Because object-oriented code is modular, it is much easier to pinpoint the source of a problem or where an application needs to be enhanced. Additionally, as
stated above, the change to one object is transparent to the other objects in an application. Thus, modiﬁcations to an object can be done in an isolated fashion.
Better Representation of Business Processes -- The combination of data and algorithms is a much better way to model real-world entities. Programmers and end-users have a common
framework for discussing the various functions and components of an application under development -- resulting in software that more accurately meets user needs.
Extended Life of Existing Software Resources -- Object-oriented applications can be integrated with legacy software by building an object interface (or "wrapper") around existing data
and services. This preserves previous software investments and lets organizations continue to take advantage of applications hosted on the wrapped legacy systems.
Over the last few years, object-oriented software development tools have matured to the point that user organizations can now select from a broad range of market-tested offerings. Robust
browsers, editors, compilers and tools for analysis, design and testing are now available, and new conﬁguration management tools that support team development have been introduced.
Objects are being used today by leading organizations intent on building enterprise-wide systems and the adoption rate of object technology is accelerating.
Figure 3: Using Objects to Partition Applications
Source: Digital Equipment Corporation, February 1995
Now that object-oriented development tools are ready for prime time, user organizations are shifting their attention to how to best implement the technology. Aberdeen's research clearly
shows that the user organizations which succeed in implementing an object-oriented 3-Tier application have one thing in common -- a strong emphasis on developer training. In fact, one
company interviewed by Aberdeen stated that the main reason it selected a solution put forward by Digital Equipment and Forté over competitive proposals was the ability of those two
suppliers to quickly educate developers in the IS organization.
Developers must not only learn the intricacies of the new tool and different language syntax, they must also adopt new methodologies that stress iterative development and sharing of
software modules. As a result, Aberdeen believes the training of new object-adept developers will be the biggest issue facing user organizations as they look to build next-generation client-
server applications using object technology.
The good news is that it is now much easier for user organizations to ﬁnd knowledgeable third-parties to assist in the transition to object technology. Over the last few years an infrastructure
of educational programs, systems integrators and object-savvy developers has been established, making a development strategy based on object technology a mainstream option.
Additionally, powerful new software development tools have been introduced, simplifying the process of developing and deploying object-oriented applications. These tools have been
designed with the needs of the novice object developer in mind and include products from: Dynasty, Forté , Open Environment Corporation and Magic Software at the high end; Seer, Four
Seasons, Unify and Sapiens at the next level; and many others which are reformulating their tools to be able to play in this environment.

Back to Table of Contents
V Aberdeen Field Research
For this White Paper, Aberdeen conducted a series of in-depth interviews with MIS executives from Fortune 100 companies, ISVs and government agencies who were implementing 3-Tier
architectures. There were expected differences between the groups' motivations for moving to 3-Tier, methods of implementing 3-Tier and types of post-production experiences. But there
were more similarities than differences, and those common experiences can be valuable lessons for others.
Signiﬁcant Findings
A number of major ﬁndings were garnered from the interviews, other primary research, and Aberdeen's long involvement with 3-Tier computing:
High-level application-development tools are the cornerstone of developing, partitioning, and deploying large departmental and enterprise-wide applications. Tools with the widest name
recognition -- for instance, Powersoft's PowerBulider and Microsoft's Visual Basic -- do not scale up to the top tier, and are only moderately functional for use in the middle tier. Given
the importance of these new tools, MIS should spend several months reviewing the candidates -- a relatively short list -- before making a commitment.
Given the mission-critical nature of the applications being developed, high-availability and stability are obviously important. To this end, enterprises developing 3-Tier applications tend
to maintain their legacy applications -- often running on MVS mainframes or OpenVMS clusters -- as the 'always available and stable' data repository. For many, the stability of the
platform housing the data is the critical factor driving the choice of an operating system at this level.
Most of the mid-tier platforms already installed were either Unix-based or OpenVMS-based. However, many of the individuals interviewed were seriously looking at Microsoft's NT
Server as the mid-tier operating system of choice for the future, often because of its perceived ease of use and management. Regardless of platform, all those interviewed were willing to
spend the extra money adding high-availability features to the mid-tier servers, including system clustering and component redundancy. (There were three reasons for ﬁnding so many
OpenVMS platforms in shops moving to 3-Tier Plus: Digital's tight relationship with several high-level tools vendors; OpenVMS' well-known high-availability options; and OpenVMS'
current and growing sharing of common features with Windows NT.)
Those interviewed have as little as possible running or stored on the desktop so that users can easily be moved if their desktop system is down. While this would allow for a "thin" client,
given users' need to access personal productivity tools and given the emotional attachment users have to "their" PCs, most desktop systems remain "fat."
All see the ability to use myriad "open" components is a good-news/bad-news story -- while it provides MIS with the opportunity to use best-of-breed modules, it also often forces MIS
to integrate these components itself. This is no less true with selecting the low-level tools to work with the chosen high-level application development tool. To deal with the negatives,
companies are adopting the following internal policies:
» Select only one high-level development tool for use within the enterprise, to cut down on training time and costs and to increase the transferability of development staff between
divisions.
» Require all external developers and consultants to use the same tool(s).
» Use only those low-level tools (PC-based, low scalability) integrated with the high-level tool (multi-platform based, highly scaleable) by the supplier of that high-level tool, even
if this means passing up the "best of breed," or
» Do the tools integration internally and give the results back to the tool supplier(s).
Given the increasing role of the network, more attention has to be paid to network availability, reliability and security. This means spending increasing resources on installing and using
advanced systems and network management applications. (See Aberdeen's 1996 report on Network and Systems Management.)
Companies treated return-on-investment (ROI) criteria for moving to 3-Tier in two ways. One group vaguely set a cap on spending by saying that the new implementation should cost no
more than the old, but agreed that actually determining ROI was difﬁcult. The other group admitted that ROI was not a major consideration, but that "opportunity cost" was a critical
factor. Given the competitive advantages 3-Tier provided, these companies could not afford to not forge ahead with development of the new applications.
Four Case Studies
As examples of how 3-Tier is emerging in the enterprise, the experiences of four organizations may be helpful.
Company "A" is an international provider of materials for the telecommunications industry with an MIS group which has received much press over the years for its innovative uses of
technology. The demand for one of the company's primary products is so great that its manufacturing plants are running 24 hours a day, 360 days a year (the plant is shut-down for ﬁve days
at the end of the year). System availability and reliability is critical, so it was decided that the back-end servers managing all aspects of the manufacturing process will continue to be
controlled by clusters of Digital OpenVMS systems running Oracle's Rdb relational database.
Mid-tier SMP servers being installed are mostly Intel-based running Microsoft's NT Server. Installed Macintosh desktops will eventually be replaced by Intel-based PCs running NT
Workstation (since stability, reliability and availability are key, the company will not be installing any Windows '95).
After an intensive search and testing process, MIS decided to use Forté 's Forté tool-set for developing the applications to be partitioned for deployment on all tiers. (The company insists,
with justiﬁcation, that it has an "n-Tier" architecture -- multiple tiers which are both clients and servers, depending on the application's need at any one time.) Forté was chosen because of its
focus on objects, its ability to scale sufﬁciently for enterprise-wide applications, its ability to develop and deploy across multi-platforms, and especially for its short learning curve.
Company "B" is a multi-billion dollar international consumer goods conglomerate, with approximately 1,000 developers -- most of whom will eventually be involved in the development and
deployment of 3-Tier applications. In its manufacturing group, it runs Fortran applications on Digital OpenVMS clusters, with Macintoshes and Unix workstations on the desktop. As it
moves to 3-Tier in manufacturing, it will add NT Server-based systems in the middle tier.
In its marketing groups, the legacy applications are MVS-based using DB/2 relational databases, and the mid-tier consists of Sun Microsystems 1000E and 2000E servers using Sybase's
RDBMS.
Macintoshes rule the marketing desktops, but MIS is making every attempt to replace the Macintoshes in both manufacturing and marketing with Intel-based PCs. To ease the transition, the
company will ﬁrst use Windows '95 on the PCs, but MIS intends to move to NT Workstation as soon as possible.
This company chose Forté as the tools provider after a very intense and expensive search and testing process for many of the same reasons as company "A."
Company "C" is a large national retailer using 3-Tier as a means of moving applications off its mainframe platforms over a period of time. This company has NT Workstation on the desktop,
NT Server in the mid-tier, and NCR Unix-based multiprocessing systems for the 3rd tier. While using PowerBuilder and Visual Basic for front-end development, the company chose Seer
Technologies High Productivity Systems (HPS) as the high-end tool for application development and partitioning.
Organization "D" is a European navy with an MVS-based IT system running ﬁnancial, personnel and materials-processing applications. This IT architecture did not meet the organization's
new business requirements as identiﬁed by its leadership. Initially ﬁnding that either developing a totally new set of mainframe applications, or moving to PC-based applications was not
functional, the head of computer operations decided to move to an open 3-Tier approach. The navy chose Open Environment Corporation's Entera product set, which is based on the Open
Software Foundation's Distributed Computing Environment (OSF DCE). This allowed the navy to keep its older applications on the mainframe while accessing the data via new applications
developed on mid-tier servers. Because of the need for 24-hour, 365-day access, the new back-end housing the data, as well as the new mid-tier application platforms, run on OpenVMS. The

clients are NT Workstation-based PCs, and several 4GL's were used to developed the graphical user interfaces. Using Entera allowed for parallel development across the three tiers -- linking
the presentation, business logic and database server platforms using DCE's remote procedure call (RPC) mechanism.
Back to Table of Contents
VI Aberdeen Conclusions
3-Tier represents the best practices for the implementation of productivity-enhancing, revenue-producing, client-server applications. 3-Tier provides rapid access to a wide range of
information sources for users needing to make critical decisions. 3-Tier uses hardware that takes full advantage of the customer's recent investments in PCs and LANs, and also protects
investments in existing production systems. 3-Tier application development and maintenance is made easier and faster by using objects to build business-process software components. 3-Tier
client-server is able to use the exact platform type required by each module of a partitioned application, and it permits these platforms to be scaled up or down as the number of users and
transaction volumes increase or decrease over time.
Moving to 3-Tier is not without its challenges, costs and tribulations. The tools required for application development, partitioning and deployment are fairly expensive. There is also a rather
steep, in-house staff learning curve -- in some cases amounting to 20% of the information systems payroll. This money simply must be spent in order to assimilate new technologies into an
established, centralized data processing infrastructure. Furthermore, implementation of distributed systems requires out-of-pocket expense for new microprocessor-based hardware as well as
upgrades to corporate networks with inadequate bandwidth.
Despite these investment requirements, Aberdeen's ﬁeld research has conclusively demonstrated that over the last three years, 3-Tier technology components have matured dramatically, the
professional services to assist with design and development have emerged in nearly every geographical region, and leading suppliers have come to grips with most of their pressing sales and
distribution channel issues.
All of the companies interviewed by Aberdeen achieved best results by creating tight, two-way communication with their lead platform suppliers. Perhaps there is no more critical lesson
learned by IS organizations that have successfully deployed 3-Tier client-server applications. Customers should select a company that has internal experience with distributed 3-Tier
architectures, as well as with object-oriented software, one that can demonstrate solid partnerships with leading RDBMS and toolset suppliers, and one that has the resources and the
inclination to partner with their customer -- from project concept to production deployment.
3-Tier hardware and application architectures are no longer reserved for the slightly masochistic, "bleeding edge" enterprise. For companies of all sorts and sizes that want to create and
maintain next-generation business systems with cost-effective new technologies -- systems with ﬂexibility, scalability and performance -- 3-Tier Plus is the best design strategy.
Back to Table of Contents
Aberdeen Group Registration
Home Page || General Information
HTML Market Research|| Aberdeen Abstracts
Aberdeen Group Publications||Custom Consulting
Aberdeen Group
One Boston Place
Boston, Massachusetts
02108
Telephone: 617-723-7890
FAX: 617-723-7897
The trademarks and registered trademarks of the corporations mentioned in this publication are the property of their respective holders. Unless otherwise noted, the entire contents of this publication are copyrighted by Aberdeen
Group, Inc. and may not be reproduced, stored in a retrieval system, or transmitted in any form or by any means without prour written consent of the publisher.
Copyright © 1996 Aberdeen Group, Inc., Boston, Massachussetts

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-object-oriented-three-tier-plus-computing |
| title | Object-Oriented Three-Tier-Plus Computing: Client-Server for Adults |
| author | Aberdeen Group |
| date | 1996-02-01 |
| type | white-paper |
| subject_domain | client-server-architecture |
| methodology | field-research, industry-analysis, competitive-profiling |
| source_file | 1996 Object-Oriented Three-Tier-Plus Computing wp.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group's whitepaper examines the maturation of three-tier client-server computing in 1996, presenting the "Three-Tier Plus" model that adds MPP/clustered SMP as a fourth tier for data warehousing. The study synthesizes field research showing organizations achieve four key business outcomes: improved enterprise efficiency, multi-source information access, scalability for emerging technologies, and superior ROI. Aberdeen argues OOP is critical for application partitioning across tiers and predicts NT Server will close the gap with Unix within 24 months.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | One of the most comprehensive 1996 frameworks for enterprise client-server architecture; Aberdeen's Three-Tier Plus model captured the evolution to n-tier computing foundational to all modern enterprise architectures. |
| **Relevance** | high | Three-tier (presentation/logic/data) remains the foundational pattern for web applications, microservices, and cloud-native architectures. |
| **Prescience** | high | NT Server gap closure within 24 months verified; MPP mainstream adoption verified; OOP dominance prediction fully confirmed. |

### Prescience Detail

**Prediction 1:** NT Server mid-tier competitiveness timeline
- **Claimed:** NT systems will close sales gap with Unix for mid-tier within 24 months; will at least equal unit sales in workgroup
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 1:** NT Server mid-tier actual outcome
- **Result:** Windows NT Server 4.0 (1996) and NT 4.0 EE (1997) closed gap with Unix; NT dominated enterprise by 1998-2000
- **Confidence:** verified
- **Notes:** 24-month prediction accurate; NT/Windows 2000 became the dominant enterprise OS

**Prediction 2:** MPP broader market acceptance
- **Claimed:** As Oracle/Informix port to MPP and prices decline, MPP will achieve broader enterprise acceptance
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 2:** MPP market acceptance actual
- **Result:** MPP data warehouse systems (Teradata, Netezza, later Amazon Redshift) became mainstream for enterprise analytics by 2000-2005
- **Confidence:** verified
- **Notes:** Aberdeen's prediction fully confirmed; cloud MPP (Redshift, BigQuery) extended the trend

**Prediction 3:** Mainframe residual value decline
- **Claimed:** Residual value of mainframe software portfolio will continue declining in second half of 1990s
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 3:** Mainframe decline actual
- **Result:** Mainframe installed base shrank but did not disappear; IBM z-series maintained banking/insurance role; 3-tier dominated new development
- **Confidence:** verified
- **Notes:** Aberdeen's nuanced prediction accurate; mainframes maintained critical niche while 3-tier dominated new work

**Prediction 4:** NT vs Novell LAN market
- **Claimed:** NT Server with NetWare interconnect beginning to dominate new LAN server shipments
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 4:** NT vs Novell LAN actual
- **Result:** Windows 2000 Server completely displaced Novell NetWare as dominant LAN OS by 2000; Novell collapsed from >70% to <10% share
- **Confidence:** verified
- **Notes:** Aberdeen's directional prediction understated the speed and completeness of Novell's displacement

**Prediction 5:** OOP dominance in enterprise development
- **Claimed:** Object technology will be the method for modular enterprise application development
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 5:** OOP dominance actual
- **Result:** OOP became universally dominant paradigm for enterprise application development by 2000 (Java/.NET/C++)
- **Confidence:** verified
- **Notes:** Aberdeen's prediction fully confirmed

### Entities Referenced (6)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | merged | Aberdeen (Harte-Hanks) |
| Microsoft Corporation | company | active | — |
| Oracle Corporation | company | active | — |
| IBM | company | active | — |
| Novell Inc. | company | acquired | Attachmate (2011) -> OpenText |
| Informix Software | company | acquired | IBM (2001) |

### Technologies Referenced (8)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|----------------------|--------------------|
| Three-Tier Architecture | framework | industry-standard | mature | active |
| Object-Oriented Programming | framework | multiple | mature | active |
| RDBMS | application | Oracle/Informix | mature | active |
| SMP Servers | platform | multiple | mature | active |
| MPP Systems | platform | Teradata/Tandem | emerging | active |
| Windows NT Server | platform | Microsoft | emerging | obsolete |
| Application Partitioning | framework | industry-concept | mature | active |
| Data Warehousing | application | multiple | emerging | active |

### Observation Summary

- Total observations: 24
- By type: strategy-classification(2), framework-factor(4), technology-assessment(4), market-data(1), viability-prediction(5), actual-outcome(5), benchmark-result(1), expert-opinion(1)
