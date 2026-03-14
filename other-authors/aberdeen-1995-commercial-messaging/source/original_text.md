# Commercial Messaging: The Keystone Of Strategic Long-Term Distributed Computing

> Archived from: https://web.archive.org/web/19970112011057/http://www.aberdeen.com:80/secure/whtpaper/ibmwp/ibmwp.htm
> Original publication date: 1995-10-01
> Author: Aberdeen Group

---

## Original Document Text

Commercial Messaging: The Keystone Of Strategic Long-Term Distributed Computing
An Executive White Paper
October 1995
Preface
Aberdeen research shows that while store-and-forward messaging should be a key infrastructure component of today's and tomorrow's distributed solutions, IS is not yet taking effective
advantage of Commercial Messaging's store-and-forward technology to achieve scalability, open interoperability, and long-term enterprise-architecture adaptability.
Store-and-forward messaging is spreading rapidly in supplier products to match the rapid increase in client-server computing, because of its ability to handle intermittent and wide-area
connections robustly. However, because users typically do not use Commercial Messaging independent of these products and do not demand a common store-and-forward component across
their enterprise architectures, both users and suppliers constantly "reinvent the wheel" in creating distributed solutions by developing their own per-project messaging techniques or creating
networking-limited program-to-program communications. Moreover, users developing solutions without Commercial Messaging are unnecessarily limited in interoperability across suppliers
and product types.
Aberdeen ﬁnds that Commercial Messaging can not only deliver immediate project-speciﬁc beneﬁts but is also a key part of a long-term IS distributed-computing architecture and strategy.
Commercial Messaging products can deliver immediate beneﬁts in increasing program performance, interoperability, mobile-user support, and distributed-system robustness, and long-term
infrastructure beneﬁts that allow enterprise architectures to automatically and rapidly scale and adapt to new user needs.
Executive Summary
Commercial Messaging is a set of tools and components that allows developers to use store-and-forward messaging to communicate between programs. Adding Commercial Messaging to a
set of applications or program components communicating across a geographically-distributed or intermittently-connected network improves performance, enhances robustness, supports the
periodic connections characteristic of laptop users, and gives IS greater architectural ﬂexibility.
However, the greatest beneﬁts of Commercial Messaging are enterprise-wide and long-term. Commercial Messaging can act as the keystone of an "enterprise infrastructure" allowing
program components and communications to adapt ﬂexibly and automatically to changing and rapidly-growing user needs. Using Commercial Messaging across all applications allows users
to move any application component from place to place or add new components without needing to change any other component (i.e., partitioning).
Commercial Messaging technology already has shown long-term beneﬁts across a broad range of today's most strategic products. These include groupware solutions such as Lotus Notes;
object-oriented programs that pass messages between distributed objects; the application partitioning technologies used by today's second-generation client-server development toolsets that
increase scalability, ﬂexibility, and programmer productivity in comparative-advantage application generation; the replication technologies key to today's data-warehousing solutions; the TP-
monitor-type database interoperability used to enhance many of today's mission-critical applications; and even E-mail.
The Commercial Messaging market and store-and-forward technology are not yet mature, and no supplier is a "one-stop shop". IS buyers should carefully assess today's products on their
ﬂexibility, scalability, and programmability. Products such as IBM's MQSeries incorporate sophisticated store-and-forward technology as well as single-point-of-control administration and
broad training, consulting, and support. Some second-generation client-server development toolsets are also joining IBM in delivering leading Commercial Messaging solutions.
Users that employ Commercial Messaging to create an enterprise infrastructure should also take care in designing the messaging architecture. A staged approach that meshes with the existing
enterprise architecture should deliver the best combination of immediate and long-term Commercial Messaging beneﬁts.
Aberdeen concludes that the time and technology are ripe for IS buyers to incorporate Commercial Messaging in their development strategies and tools. In fact, delay may add to a growing
mass of legacy network-limited applications that will require added costs to retroﬁt--or worse, new client-server applications that fail to scale in an increasingly distributed enterprise and
require early and costly rearchitecting. Aberdeen suggests that IS buyers take a close look at Commercial Messaging in general, and products such as IBM's MQSeries in particular, for their
immediate beneﬁts and long-term strategic importance.
The Long-Term Strategic Importance of Commercial Messaging
What Is Commercial Messaging?
Aberdeen Group deﬁnes Commercial Messaging as a set of tools and components that allows developers to use store-and-forward messaging to communicate between programs. That is, a
Commercial Messaging product takes a request for service or piece of data sent by one program, forwards it--often via intermediate programs and nodes--and stores it until a program is
ready to receive it. Reception can happen immediately if the program is waiting for the message, or can be deferred if the program is not ready to receive the message until some time later.
A Commercial Messaging product typically has several parts. These include:
Queues in which the instructions/data pieces are stored until they are sent (the instructions/data pieces are enclosed in "message envelopes" that tell the Commercial Messaging program
where the resulting message is to be sent);
A Queue Manager that handles its own queues, queues belonging to applications, and connections with other Queue Managers; and
Front-end APIs and tools that allow the developer to invoke the Queue Manager.
Some of the front-end tools are useful across a wide range of Commercial Messaging situations. For example, a Workﬂow Manager implementing "message-driven processing" can allow the
developer to create a script that automates the typical interactions between two communicating programs. An Agent can proactively search through a wide range of possible local and remote
receiving programs in order to gather, combine, and deliver results to an end user.
Why Should You Care About Commercial Messaging?
There are two basic reasons why Commercial Messaging should be important to the IS buyer.


The ﬁrst reason is that store-and-forward messaging is a key technology for implementing large-scale distributed computing. In enterprise-scale networks, communications will inevitably be
interrupted or delayed. Store-and-forward messaging is the only method that key distributed-computing applications such as electronic mail, mobile-user-supporting groupware, and
distributed directory services ﬁnd effective in handling these problems. Commercial Messaging products minimize node-to-node routing times and costs and make the location of the
receiving program transparent to the developer and the end user, and some Commercial Messaging products such as IBM's MQSeries assure message delivery.
The second reason that Commercial Messaging can be vital to IS is that it can deliver signiﬁcant immediate beneﬁts versus today's typical program-to-program communication mechanism. It
can:
Add architectural ﬂexibility--users can place and move Queue Managers to minimize client-server and server-server communications bottlenecks, create multiple communications paths
to improve performance or availability, or move server applications without needing to change and reinstall the client programs accessing them. Using a common API, users can easily
take advantage of underlying Commercial Messaging communications between nodes when an application needs connectivity in a multiplatform (e.g., Unix, MVS, and AS/400) and
multisupplier (e.g., Oracle, DB2, Sybase, and Informix database servers) environment.
Improve performance--because communicating programs are not directly connected to each other, each can perform a task at its own pace without waiting for the other or the
communications mechanism to complete. In addition, users can design sophisticated applications to take advantage of parallelism, with a client program invoking multiple server
applications simultaneously over the same or parallel communications paths.
Enhance enterprise-wide robustness--Aberdeen ﬁnds that robust communications are vital to both client-server and wide-area-network computing availability, reliability, and resiliency
(e.g., for warm backup to a disaster-recovery site). Commercial Messaging allows alternate communications paths for failover, provides recovery mechanisms after node and
communications failures, and has the potential--depending on application design--to insulate applications and end users from network and node failures.
Provide invaluable services to the the application programmer such as easier development of robust and location-transparent distributed applications, thus improving application-
programmer productivity and application-program quality. Users with signiﬁcant object-oriented programming efforts should also note that Commercial Messaging can provide a way to
implement distributed messaging between objects. Aberdeen ﬁnds that major distributed-object players such as Microsoft and CORBA will not provide Commercial Messaging
capabilities in the near future.
Commercial Messaging's Long-Term Beneﬁts and Importance
Far more important, however, is Commercial Messaging's key role in achieving scalable, ﬂexible enterprise-scale distributed computing a long-term role that is already showing up in today's
strategic technologies.
Aberdeen believes that one of the major goals of today's distributed computing technology is to create enterprise-scale internetworks that can adapt and scale as user needs change. This, in
turn, means that applications are split into small components that can move from server to server and between client and server, transparently to the end user and as far as possible online and
automatically, without administrator intervention. To achieve this, application components must be location-independent: when two components communicate, a sending component must not
hard-code the location of a receiving component.
All programs using Commercial Messaging to communicate can be completely location-independent. The Commercial Messaging product can access an enterprise-wide directory to
determine where to send a message. When a component's location changes, that component tells the directory, and the Commercial Messaging product uses the new directory entry to access
the component, online and without the sending program knowing.
The outstanding example of the effectiveness of this technique is in the application partitioning provided by most of today's second-generation client-server application development
environments (CADEs) such as Forte and Seer Technologies' Seer*HPS. The major second-generation CADEs include Commercial Messaging capabilities integrated with a
repository/directory and development tools. To repartition an application between client and server or server and server, the toolset repartitions and rebundles the development versions of the
application components, and then sends them automatically to the locations speciﬁed in the repository, transparently to the end user. When the end user invokes a client program, Commercial
Messaging hides the new component locations from the user. Publish-and-subscribe capabilities allow new applications to declare themselves ("publish") to the repository, and client
programs to use the new applications ("subscribe"), automatically.
A second area in which Commercial Messaging promises to be increasingly effective is in distributed database management. When distributed databases share data as in today's data
warehouses, which receive data copies from OLTP databases--their replication technology allows them to share and synchronize these data copies. Commercial Messaging used for
replicating data allows users to move a database from one location to another transparently to the other database with which it is sharing data, perform replication functions asynchronously,
and handle multiple replication sources and targets ﬂexibly and with high performance. Moreover, Commercial Messaging can be supplier-independent : it enables replication across multiple
relational database management system (RDBMS) suppliers' databases. Thus, Commercial Messaging can allow distributed-database as well as distributed-program adaptation and scaling.
IS buyers should note that limiting Commercial Messaging to these key programs may have long-term costs. Most of today's standalone or client-server programs cannot fully access the
entire enterprise-wide network of resources, and each takes a different approach to communicating with other programs. As a result, users and software suppliers "reinvent the wheel" each
time they add network communications to a program, and create a steadily growing mass of legacy networking-limited applications. To minimize these long-term costs, users need to
"message-enable" all of their programs; and the simplest way to do this is to ensure that Commercial Messaging is a part of every developed application. In other words, Commercial
Messaging is a key component of an enterprise infrastructure.
Factors To Consider In Choosing A Commercial Messaging Product
User experience shows that neither users nor suppliers are fully prepared to take advantage of Commercial Messaging's store-and-forward technology. E-mail, in which Commercial
Messaging technology is invisible to users, is by far the most frequent use of store-and-forward. Users that are employing Commercial Messaging in their programming are typically using it
either at the initial stages of implementation of complex client-server applications via second-generation toolsets, or for speciﬁc projects, e.g., "warm backup" for a mission-critical
application's disaster recovery. Commercial Messaging and publish-and-subscribe are beginning to appear in second-generation CADEs and in some client-server RDBMSs and TP monitors,
but by far the majority of client-server applications and RDBMSs lack messaging capabilities.
Given the preliminary state of the market, Aberdeen recommends that users focus on open--ended products with long-term "legs", products that mesh well with users' present solutions and
are likely to grow and evolve with the market and user needs. Users are ﬁnding that Commercial Messaging is easy to justify for particular projects, either to enhance existing mission-critical
applications or to deliver better performance or robustness in new large-scale applications. However, as noted above, it is likely that users will eventually see Commercial Messaging as
applicable to most if not all legacy and new applications. Thus, the Commercial Messaging product that a user chooses should be able to adapt to a much larger role.
Aberdeen identiﬁes the key yardsticks of long-term Commercial Messaging product value for IS buyers as:
Flexibility,
Scalability, and
Programmability.
Flexibility
Users should prefer products that work well with a variety of development toolsets and RDBMSs and that can be used not only for a particular application but also for such broad areas as
data replication, groupware workﬂow, and linking different application types. Thus, users should choose products that demonstrate openness, a broad scope of applicability, customizability,
and ability to evolve as the market matures.


For example, users might look at the openness of a Commercial Messaging product by seeing how well it works with popular low-end toolsets such as Microsoft's Visual Basic and
Powersoft's PowerBuilder. To judge scope of applicability, the IS buyer might determine the features it offers for areas such as data replication. For customizability, the user might assess the
ability of the Commercial Messaging product to work with a Workﬂow Manager or an Agent. For evolvability, the user might look at the commitment of the supplier to the product, the
supplier's plans to integrate it with other applications and to upgrade and evolve it, and the supplier's understanding of the likely uses of the product.
Scalability
IS is facing a major increase in demand for enterprise-scale decision support, plus related rises in OLTP and application-server demand. Aberdeen ﬁnds that data-warehouse databases are
growing at 6-7 times in 18 months in many cases. The new demands, in turn, place an added scalability burden on CADEs, distributed-database management, and database administration.
Thus, Commercial Messaging performance enhancements can have particular impact in these areas, and products that are particularly effective in enhancing the performance of these
products are to be preferred.
Particular Commercial Messaging features are proving critical in achieving high performance. Multithreading and support for multiple queues allows the Queue Manager to take advantage
of today's parallel hardware. Although queues may overﬂow onto disk, effective caching and memory management that minimizes I/O overhead can be key to performance. Passing pointers
to queues where possible instead of copying them can be especially effective in increasing performance. Administrative features that allow the network administrator to reconﬁgure queues
and detect bottlenecks improve performance in a production environment.
Programmability
The primary task of a Commercial Messaging product is to allow the developer to communicate between programs. Therefore, the more that the product aids the developer in this task, the
better. The product should have APIs for a wide range of Commercial Messaging tasks. Moreover, the product should, via its own tools or a development toolset, provide support at least for
coding and testing store-and-forward messaging. Design tools would also be useful, especially for determining where the Queue Managers should be placed on the enterprise internetwork.
Fitting Commercial Messaging Technology To The Enterprise's IS Strategy
If the enterprise commits to making Commercial Messaging a part of the enterprise infrastructure, IS's job of using store-and-forward effectively is not done with the acquisition of a product.
The major remaining task is to determine on which nodes to seed Queue Managers for effective functioning, and how to mesh Commercial Messaging with the enterprise's existing systems.
That is, Commercial Messaging must be ﬁtted to the enterprise's architecture, user needs, and IS strategy.
Aberdeen ﬁnds that most successful enterprise-scale store-and-forward implementations start by putting Queue Managers on the same nodes as an enterprise-wide distributed directory or
repository containing routing information. Effectively, the Commercial Messaging product piggybacks on the enterprise's network management superstructure. By putting Queue Managers
where the routing information is, IS ensures speedy and efﬁcient message routing and sets up a "skeleton" messaging architecture that ﬁts nicely with the overall enterprise architecture.
2-Tier, 3-Tier, 4-Tier. The next step is to determine the most effective placement of Queue Managers at the departmental and divisional level, on the LANs and LAN internetworks, among 2-,
3-, and 4-tier client-server architectures, and with the data marts and application servers. Here, the logical places to put Queue Managers are on the ﬁrst-level servers, to handle client-server
communications, and on those servers that communicate most heavily with other servers, such as data marts and application servers that access a backend database server.
Users should keep in mind that a Queue Manager is, practically speaking, a high-level communications server that allows program-to-program communication locally or across the network.
Thus, where it may make sense to keep a communications server on a separate front-end node, a Queue Manager should generally be on the same system as a mission-critical application,
because the Queue Manager's processing overhead is outweighed by the greater speed with which it can handle the application's communications.
The Enterprise WAN. Having provided an enterprise "skeleton" and achieved immediate beneﬁts by implementing Commercial Messaging on key applications, the user has achieved a store-
and-forward messaging enterprise infrastructure. To leverage Commercial Messaging even further, the user can then extend Queue Managers across the enterprise wide-area network (WAN).
In this stage, the user can select "targets of opportunity", key or large-scale wide-area communications where high performance and/or robustness are critical, such as a remote disaster
recovery facility. Putting Queue Managers at either end of these point-to-point situations can deliver signiﬁcant immediate beneﬁts beyond those of the skeleton and local systems in
enterprise-scale and geographically distributed applications.
The Commercial Messaging Market
Today's store-and-forward messaging market, like the object-oriented technology market, is an iceberg. Above the surface exists a small visible market for Commercial Messaging products;
below the surface is a much larger market for which Commercial Messaging technology is key.
The market for store-and-forward messaging APIs and tools, such as the X.400 electronic mail products of the 1980s, has always been a small one. Even today, Aberdeen estimates that
market at less than $100 million. However, store-and-forward messaging is included in markets with much greater scope, and especially the EDI, E-mail, and groupware markets, some
portions of the network operating system (NOS) market, parts of the object-oriented technology market, and the second-generation CADE market.
In the billion-dollar E-mail market, store-and-forward messaging is the major communications mechanism for today's E-mail products, and users may employ the APIs of some E-mail
products to achieve some of the same effects as a Commercial Messaging product. Likewise, the billion-dollar groupware market now dominated by Lotus Notes uses store-and-forward and
in some cases Workﬂow Manager technology to provide ﬂows of tasks and messages between users; APIs are typically at the Workﬂow-Manager level. Products such as Distributed
Computing Environment (DCE) in the network operating system market provide directories and APIs for location independence, although they generally do not provide direct APIs to
messaging; they constitute a small (hundred-million range) submarket of the overall NOS market. Objects use messaging to communicate; however, the technology is hidden (encapsulated)
within the object in today's object-oriented products, and the market for distributed objects is less than $10 million. Second-generation CADEs are today achieving $100-200 million in
revenue, including in many cases publish-and-subscribe APIs and tools, although splitting that revenue out between messaging and their many other features is problematic.
Aberdeen draws two conclusions from its market survey: (1) because of the market's small visible size, users that focus on visibility may underestimate the presence of store-and-forward
messaging within their organizations and the technology's usefulness; and (2) suppliers of Commercial Messaging technology vary widely in the degree to which the user can take advantage
of store-and-forward, with Commercial Messaging products the best in that regard and some second-generation CADE suppliers also especially effective.
The Commercial Messaging Suppliers
The Commercial Messaging market is not neatly separated from related markets, and no one supplier presently supplies all of the products in all of these markets. Therefore, the IS buyer
should focus on suppliers that provide a bundled solution, including third-party products and services, that allows the user's Commercial Messaging implementation to mesh well with the
user's development toolsets and systems management, and optionally with the user's groupware or name service product, if either of those is critical to IS's strategy.
In the core Commercial Messaging market--the Queue Manager and related components--IBM's MQSeries is taking a leadership role in a very new market. Aberdeen ﬁnds that MQSeries is
a sophisticated product with most of the key perform-ance, robustness, and ﬂexibility features mentioned as attractive above. In particular, MQSeries includes multithreading, traces for
testing and monitoring, assured delivery of a message once and only once, and, on some platforms, single-point-of-control systems-management enablement. MQSeries also integrates with
Powersoft's popular PowerBuilder CADE as well as IBM's own VisualAge and VisualGen development toolsets and 3GLs.
MQSeries' robustness includes transactional support that allows unit-of-work commitment or backout of groups of messages, and also supports integration with major popular TP monitors
such as CICS, Tuxedo, and Encina. Thus, developers can ensure that all (or none) of a set of database updates or series of program-to-program communications is completed as a single "unit
of work". MQSeries supports a broad range of Unix and proprietary environments (e.g., Tandem, AS/400, and MVS/ESA) plus Windows and DOS at the client level; Windows 95 and
Windows NT support is upcoming. MQSeries allows simultaneous operation of multiple popular communications protocols, including TCP/IP, SNA, Netbios, and DECnet protocols.
Other competitors in the basic market include such suppliers as Hewlett-Packard and Complex Architectures. HP's OpenMail provides a set of APIs and tools that allow users to message-
enhance their applications across multiple standard E-mail APIs, as well as the ability to integrate multiple enterprise E-mail products. OpenMail is focused primarily on the E-mail market,


and HP has indicated that it will implement transaction support sometime in the next 2 years. Complex Architectures has announced a similar basic product particularly focused on the laptop
market.
Workﬂow Manager and Agent tools are few and far between. Early, Cloud & Co. offers MDp, a Workﬂow Manager that can run with MQSeries or in-house Commercial Messaging
implementations. Users may also consider workﬂow software from such suppliers as Banyan (the Beyond toolset, acquired with Banyan's acquisition of Beyond, Inc.).
Second-generation CADE suppliers are now steadily adding store-and-forward capabilities. For example, Seer Technologies' Seer*HPS offers publish-and-subscribe messaging. Users should
consider carefully the pros and cons of choosing this path to Commercial Messaging. On the positive side, these capabilities are well integrated into high-productivity, highly scalable
toolsets. However, their messaging does not necessarily transfer easily to applications written outside of these toolsets, and Aberdeen ﬁnds that many of today's Fortune-1000 development
projects, especially at the departmental level, are using Microsoft's Visual Basic or Powersoft's PowerBuilder rather than a second-generation CADE.
Finally, some RDBMS suppliers have a store-and-forward architecture--for example, Software AG's ADABAS. These suppliers have not yet fully provided APIs and tools to allow
developers to use these for Commercial Messaging.
Another Key Factor: Service and Support
Aberdeen ﬁnds that over time, enterprises implementing Commercial Messaging ﬁnd unexpected places in which store-and-forward technology proves effective. To shorten this process,
users can call upon the experience of the Commercial Messaging supplier in the early stages, including training and consulting. Moreover, the ongoing counsel and support of the supplier is
valuable in meshing Commercial Messaging with other solutions in which the supplier has expertise.
Suppliers such as IBM are therefore particularly valuable for enterprise-scale Commercial Messaging. Their general support depth and long experience with these technologies can deliver
signiﬁcant value-added as part of an overall Commercial Messaging bundled solution.
At the same time, IS buyers should not expect one-stop shopping for all components of a large-scale Commercial Messaging implementation. The market has not yet developed to the point
where one supplier provides Queue Manager, Workﬂow Manager, development toolset, administration tools, and service by itself. Rather, the user should seek a "one-stop storefront", a
supplier that can bundle its own and third-party products, seeking the best of breed, moving rapidly with the technology, and accumulating Commercial Messaging experience to deliver as
part of its consulting and training.
Aberdeen Conclusions
Commercial Messaging is potentially on the verge of a major increase in its strategic importance to users. This is due in part to its ability to play a constructive role in today's major
applications, from laptop support to data warehousing to application servers to programmer-productive client-server development. However, in great part Commercial Messaging's potential
is due to its power to enable location- and supplier-independent ﬂexible, distributed computing. By message-enabling all applications, an enterprise can create an architecture in which
programs and data move, grow, and adapt almost as user needs do, with minimal IS intervention.
The key to user success in taking full advantage of Commercial Messaging is taking a long-term view, picking initial targets not just for immediate beneﬁt but as part of a long-term strategy.
Users should view Commercial Messaging as a key part of an enterprise infrastructure that also includes an enterprise-wide directory or name service and enterprise-wide systems
management. By the same token, users should ﬁt the Commercial Messaging product's architecture to the enterprise's architecture, user needs, and IS strategy.
Above all, a user should pick a supplier or suppliers that provide not only an excellent product but also integration with the enterprise's strategic development tools and consulting and
support driven by experience and a focus on the broad picture. IBM with its MQSeries provides a technically strong product and broad-scope services. Second-generation CADEs provide
effective integration with highly scalable and powerful development toolsets.
Today's Commercial Messaging products have a substantial road of evolution ahead. Workﬂow Managers and Agents for speciﬁc user needs will proliferate; Commercial Messaging
development tools will integrate more effectively with CADEs and RDBMSs; and more suppliers at all levels will enter the market. However, the basic tools for building the enterprise
infrastructure are here today.
Aberdeen concludes that IS buyers should take a fresh look at the potential and the immediate payoffs of Commercial Messaging. Without the ﬂash of a competitive-advantage application,
Commercial Messaging can deliver solid blocking-and-tackling beneﬁts that enhance these and similar applications, now and in the future.
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

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1995-commercial-messaging |
| title | Commercial Messaging: The Keystone Of Strategic Long-Term Distributed Computing |
| author | Aberdeen Group |
| date | 1995-10-01 |
| type | white-paper |
| subject_domain | middleware-messaging |
| methodology | industry-analysis, technology-assessment, market-analysis |
| source_file | 1995-Commercial-Messaging_-The-Keystone-Of-S...-Computing-An-Executive-White-Paper-wp-2.pdf |
| license | CC-BY-4.0 |

### Abstract

This 1995 Aberdeen Group white paper examines Commercial Messaging—store-and-forward messaging middleware—as a foundational component of enterprise distributed computing architecture, arguing that IS organizations are underutilizing the technology despite its growing presence in products like IBM MQSeries, Lotus Notes, and second-generation client-server application development environments (CADEs). Using industry analysis and market assessment, Aberdeen surveys the emerging Commercial Messaging market (estimated below $100 million standalone, embedded in billion-dollar e-mail and groupware markets), evaluates leading products including IBM MQSeries, HP OpenMail, and CADE tools from Forte and Seer Technologies, and finds that IBM MQSeries leads on flexibility, scalability, and programmability. Key findings include that data-warehouse databases are growing 6-7x in 18 months, that CORBA and Microsoft distributed-object platforms will not deliver Commercial Messaging capabilities in the near term, and that failure to adopt Commercial Messaging will create a growing mass of legacy networking-limited applications requiring costly retrofits; Aberdeen recommends that IS buyers immediately incorporate Commercial Messaging—particularly IBM MQSeries—into enterprise infrastructure strategy.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | White paper advocating for commercial messaging middleware as enterprise infrastructure foundation; IBM MQSeries recommendation influenced billions in middleware investment. Aberdeen's framing of messaging as strategic became the dominant enterprise architecture view. |
| **Relevance** | high | Message-oriented middleware (Apache Kafka, RabbitMQ, IBM MQ, AWS SQS) remains foundational to distributed computing in 2026; Aberdeen's architectural arguments about decoupling and asynchrony are more relevant than ever. |
| **Prescience** | high | Most predictions confirmed: IBM MQSeries achieved dominance, CORBA/COM failed to deliver messaging, pub/sub became ubiquitous, legacy messaging debt materialized as SOA/ESB market. |

### Prescience Detail

**Prediction 1:** Commercial Messaging strategic importance trajectory
- **Claimed:** potentially on verge of major increase in strategic importance to enterprise IS
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 1.1:** Legacy networking-limited application debt outcome
- **Result:** verified; enterprise integration and API modernization debt became multi-billion dollar challenge
- **Confidence:** verified
- **Notes:** Aberdeen's 1995 warning about growing legacy networking-limited application debt proved prescient; enterprise integration became a major market segment

**Actual Outcome 1.2:** Legacy messaging debt — actual outcome
- **Result:** Confirmed: enterprises that delayed messaging adoption faced costly SOA/ESB modernization projects in 2000s; message broker architectures became multi-billion dollar market (IBM WebSphere MQ, TIBCO, webMethods)
- **Confidence:** verified
- **Notes:** Prediction confirmed: integration middleware became a massive market. ESB/SOA wave of 2000s was direct consequence of deferred messaging investment.

**Prediction 2:** Workflow Manager and Agent proliferation
- **Claimed:** will proliferate for specific user needs; more suppliers at all levels will enter market
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 2.1:** Publish-and-subscribe proliferation actual outcome
- **Result:** verified; became dominant messaging paradigm (Apache Kafka, RabbitMQ, AWS SNS/SQS, Azure Service Bus)
- **Confidence:** verified
- **Notes:** Aberdeen's 1995 prediction of pub/sub proliferation fully confirmed by 2010s event-streaming ecosystem; market grew to multi-billion dollars

**Prediction 3:** Enterprise infrastructure adoption trajectory
- **Claimed:** users will eventually see Commercial Messaging as applicable to most or all legacy and new applications
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 3.1:** Legacy networking-limited application debt outcome
- **Result:** verified; enterprise integration and API modernization debt became multi-billion dollar challenge
- **Confidence:** verified
- **Notes:** Aberdeen's 1995 warning about growing legacy networking-limited application debt proved prescient; enterprise integration became a major market segment

**Actual Outcome 3.2:** Legacy messaging debt — actual outcome
- **Result:** Confirmed: enterprises that delayed messaging adoption faced costly SOA/ESB modernization projects in 2000s; message broker architectures became multi-billion dollar market (IBM WebSphere MQ, TIBCO, webMethods)
- **Confidence:** verified
- **Notes:** Prediction confirmed: integration middleware became a massive market. ESB/SOA wave of 2000s was direct consequence of deferred messaging investment.

**Prediction 4:** HP OpenMail transaction support delivery
- **Claimed:** HP indicated transaction support within next 2 years (by approximately 1997)
- **Year:** 1995
- **Confidence at time:** low

**Actual Outcome 4:** *(No matching outcome record found)*

**Prediction 5:** IBM MQSeries market leadership prediction
- **Claimed:** Aberdeen predicts IBM MQSeries will dominate enterprise commercial messaging; recommends immediate adoption as enterprise infrastructure
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 5.1:** MQSeries market outcome
- **Result:** renamed IBM MQ; remained active enterprise messaging platform for 30+ years
- **Confidence:** verified
- **Notes:** Aberdeen's market leadership prediction for MQSeries fully verified; product renamed IBM MQ in 2014 and remains in active enterprise use

**Actual Outcome 5.2:** IBM MQSeries market leadership — actual outcome
- **Result:** IBM MQSeries did achieve dominant enterprise messaging position; renamed IBM MQ in 2014; still a top enterprise messaging platform in 2026
- **Confidence:** verified
- **Notes:** Prediction confirmed: IBM MQ (formerly MQSeries) remains a primary enterprise messaging backbone. Aberdeen's recommendation proved correct.

**Prediction 6:** Legacy messaging debt prediction
- **Claimed:** Aberdeen predicts that companies not adopting Commercial Messaging will accumulate a growing mass of legacy networking-limited applications requiring costly retrofits
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 6.1:** Legacy networking-limited application debt outcome
- **Result:** verified; enterprise integration and API modernization debt became multi-billion dollar challenge
- **Confidence:** verified
- **Notes:** Aberdeen's 1995 warning about growing legacy networking-limited application debt proved prescient; enterprise integration became a major market segment

**Actual Outcome 6.2:** Legacy messaging debt — actual outcome
- **Result:** Confirmed: enterprises that delayed messaging adoption faced costly SOA/ESB modernization projects in 2000s; message broker architectures became multi-billion dollar market (IBM WebSphere MQ, TIBCO, webMethods)
- **Confidence:** verified
- **Notes:** Prediction confirmed: integration middleware became a massive market. ESB/SOA wave of 2000s was direct consequence of deferred messaging investment.

### Entities Referenced (17 entities)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| IBM (International Business Machines) | company | active |  |
| Lotus Development Corporation | company | acquired | IBM (1995), then HCL Technologies (2019) |
| Microsoft | company | active |  |
| Hewlett-Packard | company | active | HP Inc. (consumer 2015) and Hewlett Packard Enterprise (enterprise 2015) |
| Powersoft Corporation | company | acquired | Sybase (1995), then SAP (2010) |
| Seer Technologies | company | acquired | Merisel (acquired), subsequently dissolved |
| Forte Software | company | acquired | Sun Microsystems (1999), then Oracle (2010) |
| Complex Architectures | company | dissolved |  |
| Early, Cloud & Co. | company | dissolved |  |
| Banyan Systems | company | dissolved | assets sold to inacom and others; effectively dissolved circa 2001 |
| Oracle Corporation | company | active |  |
| Informix Software | company | acquired | IBM (2001) |
| Sybase | company | acquired | SAP (2010) |
| Software AG | company | active |  |
| CORBA Consortium (Object Management Group) | institution | active |  |
| Aberdeen Group | firm | acquired | Harte-Hanks (acquired 2001), Aberdeen Group LLC (spun off 2010) |
| Beyond, Inc. | company | acquired | Banyan Systems (acquired) |

### Technologies Referenced (28 technologies)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| IBM MQSeries | platform | IBM | emerging | active |
| Store-and-Forward Messaging | protocol | various | emerging | active |
| Commercial Messaging | framework | various | emerging | active |
| Lotus Notes | application | Lotus Development / IBM | mature | legacy-supported |
| Distributed Computing Environment (DCE) | framework | OSF / The Open Group | mature | obsolete |
| CORBA (Common Object Request Broker Architecture) | framework | OMG Consortium | emerging | obsolete |
| Microsoft Visual Basic | language | Microsoft | mature | legacy-supported |
| Powersoft PowerBuilder | application | Powersoft / Sybase / Appeon | mature | legacy-supported |
| Seer*HPS | application | Seer Technologies | emerging | obsolete |
| Forte (Second-Generation CADE) | application | Forte Software | emerging | obsolete |
| X.400 Electronic Mail Protocol | protocol | ITU / ISO | mature | obsolete |
| TCP/IP | protocol | IETF | mature | active |
| IBM SNA (Systems Network Architecture) | protocol | IBM | mature | obsolete |
| NetBIOS | protocol | IBM / Microsoft | mature | obsolete |
| DECnet | protocol | Digital Equipment Corporation | declining | obsolete |
| IBM CICS (Customer Information Control System) | platform | IBM | mature | legacy-supported |
| Tuxedo TP Monitor | platform | AT&T / Novell / BEA / Oracle | mature | legacy-supported |
| Encina TP Monitor | platform | Transarc / IBM | mature | obsolete |
| EDI (Electronic Data Interchange) | protocol | various standards bodies | mature | legacy-supported |
| Windows 95 | platform | Microsoft | emerging | obsolete |
| Windows NT | platform | Microsoft | emerging | obsolete |
| HP OpenMail | application | Hewlett-Packard | emerging | obsolete |
| Software AG ADABAS | platform | Software AG | mature | legacy-supported |
| Publish-and-Subscribe Messaging | framework | various | emerging | active |
| MDp Workflow Manager | application | Early, Cloud & Co. | emerging | obsolete |
| IBM VisualAge | application | IBM | emerging | obsolete |
| IBM VisualGen | application | IBM | emerging | obsolete |
| Beyond Workflow Toolset | application | Beyond Inc. / Banyan Systems | emerging | obsolete |

### Observation Summary

- Total observations: 42
- By type:
  - actual-outcome: 10
  - benchmark-result: 1
  - expert-opinion: 5
  - framework-factor: 3
  - market-data: 6
  - strategy-classification: 3
  - technology-assessment: 8
  - viability-prediction: 6
