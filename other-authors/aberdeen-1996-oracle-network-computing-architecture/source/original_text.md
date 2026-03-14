# Oracle's Network Computing Architecture

> **Archived from:** [https://web.archive.org/web/19970604113530/http://www.aberdeen.com:80/secure/profiles/oraclnca/orclnca.htm](https://web.archive.org/web/19970604113530/http://www.aberdeen.com:80/secure/profiles/oraclnca/orclnca.htm)
> **Original publication date:** 1996-10-01
> **Author:** Aberdeen Group

---

## Original Document Text

Oracle Corporation
500 Oracle Parkway
Redwood Shores, CA 94065
(415) 506-7000
Oracle’s Network Computing Architecture
Preface
Today’s advent of new system architectures such as the Internet is an ISV and IS opportunity wrapped as a technological challenge.
The new architectures promise competitive-advantage communications-cost savings, closer customer and supply-chain interfaces, cost-cutting automated elec-tronic commerce, and broader
scope across the enterprise for corporate applica-tions. Internet applications expand corporate text-data access to new and remote end users in such applications as advertising and electronic
catalogs or point-of-sale data collection. Long-term "side effect" beneﬁts include rapid access to a larger amount of extra-enterprise information for strategic ﬁne-tuning, connecting the
organization more closely, delivering global solutions more rapidly, leveraging corporate databases more effectively, and keeping pace with end-user demands.
However, these new architectures carry with them two new sets of technologies to be digested: those associated with the Internet itself – e.g., Web browsers, Web servers, and applets – and
object-oriented technologies, especially those assoc-iated with distributed objects – e.g., CORBA, ActiveX, and Java. The challenge that ISVs and IS must meet is to take full advantage of
the new architectures, both by using the new technologies effectively and by leveraging older technologies such as client-server architectures, "legacy" applications, and existing databases.
As Aberdeen has noted in its recent Viewpoint, "Internet Architecture: Prescrip-tion For Success", the key to success in meeting the challenge is deﬁning an effec-tive overall "network
computing architecture" – one that allows users to scale new Intranets by using tried-and-true client-server technology plus the new complex-data-type capabilities associated with object-
relational Universal Servers, and to integrate them with legacy applications and databases easily, using the ﬂexibility of distributed-object middleware.
Executive Summary
Oracle’s new Network Computing Architecture is an exceptionally comprehensive and real-world approach directly aimed at the challenge of the new architectures and technologies. The
Network Computing Architecture includes existing Oracle products that support today’s three major technologies/environments – client-server, the Internet, and distributed objects – plus
new features – especially "cartridge" services/components and an Inter Cartridge Exchange (ICX) mechanism – that integrate these and allow developers to create enterprise-scale
applications that span all three. Thus, Oracle seeks to give enterprises a least-cost growth path towards mission-critical transaction processing for the 21st century.
The Network Computing Architecture includes client, application server, and database server cartridges, letting developers partition their applications between these for highly scalable
performance, rapid and low-cost software installation, and ﬂexibility in including new application components and new software technology. The cartridges and services include an extensive
set of Oracle product functionality that improves programmer productivity by embedding much of the down-and-dirty details of programming for multi-tier client-server, Internet, and
distributed-object environments in infrastructure code. The Network Computing Architecture’s open approach encourages third-party and IS developers to create their own "shrink-wrapped
component" cartridges for reuse or sale in a "cartridge market".
The ﬁrst step that Oracle provides for customers seeking to create a Network Computing Architecture is NetSolutions, including Oracle’s Web-enabled development toolsets, a Cartridge
Development Kit, and the Oracle Web Server, Oracle Workgroup Server, and Interofﬁce software. NetSolutions allows users to begin to create cartridges on top of the core "Cartridge
Services" of the Network Computing Architecture (e.g., transaction and data-access support, messaging, and queuing). As new cartridges from Oracle and third-party suppliers arrive, users
can incorporate these into the overall architecture and use them as the basis for creating further cartridges, as needed. Other enhancements to Oracle’s products arriving over the next few
months include the above-mentioned ICX, bridges between CORBA and Microsoft’s COM, IDL (Interface Deﬁnition Language) encapsulation of present interfaces to turn them into
cartridges, Java integration into CORBA, and creation of a Universal Application Server providing Object Request Broker and Connectivity services for applications.
Aberdeen ﬁnds that the Network Computing Architecture is not a "marketecture" but a straightforward extension of already-proven Oracle products that can deliver signiﬁcant beneﬁts right
off the bat. Present users of Oracle databases, development tools, and administrative toolsets can use the new cartridges to Web-enable, distribute, and extend the scope of their Oracle-based
applications and data. Developers of new applications can use a common set of cartridge component technologies at the client, application server, and database server levels to span client-
server or Internet environments, or incorporate Internet and distributed-object technologies such as messaging with relatively little effort. IS buyers seeking to integrate the new technologies
with legacy applications can "wrap" these as cartridges and provide not only access to host solutions but also common interfaces across applications and databases.
The implicit business beneﬁts of the approach are subtler but more profound. The Network Computing Architecture should deliver all the short-term and long-term beneﬁts of client-server,
Internet, and distributed-object technologies, and also allow users to more fully leverage legacy client-server and host applications in the new environments. In turn, the proven scalability
and reliability of past technologies can be transferred more easily to the Internet. The modularity and high level of cartridges should allow greater reusability and programmer productivity. A
thriving market in vertical-industry or functional cartridges should let companies improve on and increase competitive advantage by customizing "best practices" for the enterprise’s
particular needs. In summary, the Oracle Network Computing Architecture deserves to be closely studied, planned for, and implemented in ISVs’ and major-enterprise IS’ strategies.
Overview: Oracle’s Network Computing Architecture
Oracle’s Network Computing Architecture combines three architectural approaches: multi-tier client-server, Web, and distributed-object. This multi-tier architecture includes client,
application server, and database server software, often on separate platforms (although application server and database server are also often placed on the same system). While in the past
Oracle has often supplied a client and database server to its customers, the Network Computing Architecture adds a full-ﬂedged application server that gives developers and IS much greater
ﬂexibility in designing their solutions. For example, the multi-tier approach allows them to improve application performance and scalability by ofﬂoading the application’s server side to a
different system.
A typical Internet Web architecture includes a Web-browser "client" and Web ser-ver. End users can download application-client software "applets" from the Web server as needed. Thus, the
Web architecture places much of its functionality on the server platform. The advantages for developers and users are that their appli-cation clients can be fully portable across client
platforms and easily installable, while "fat-client" applications can be ofﬂoaded to the Web-server platform.


A typical distributed-object architecture includes multiple servers plus a common repository such as an Object Request Broker that allows developers and end users to access objects in a
location-independent way. Thus, the distributed-object architecture allows objects to be placed on any server or client, dynamically, as needed. Developers gain the productivity of object-
oriented programming and the ﬂexible location independence of distributed objects, while users ﬁnd that ﬂexibility in placing objects on the network leads to greater performance and
performance scalability.
Oracle’s Network Computing Architecture seeks to give users the advantages of multi-tier client-server, distributed-object, and Web architectures – and reduce any disadvantages – by
combining them effectively. It does this by allowing developers to "beef up" the client with tried-and-true multi-tier-client objects and compon-ents; by providing application-server
components and class libraries on which to build enterprise-scale Web-enabled applications; and by offering components to allow developers to Web-enable the database server. To simplify
the developer’s and system designer’s task, it provides a common infrastructure on the client, application server, and database server.
Oracle's Network Computing Architecture infrastructure can be grouped into ﬁve distinct areas (see Figure 1). These are:
• a set of Cartridges -- grouped into Client, Application Server, and Data Cartridges -- that can be deployed on multi-tier client/application-server/database-server architectures, and that
perform distinct functions across client-server, Internet, and distributed (object) architectures;
• an Inter-Cartridge Exchange (ICX) mechanism that lets cartridges communicate not only with other cartridges but also with underlying services;
Figure 1: Oracle’s Network Computing Architecture
Source: Oracle Corp. and AberdeenGroup, October 1996
• the underlying Services themselves -- also grouped into Universal Client, Universal Application Server, and Universal Server services that can be deployed on multi-tier architectures,
and corresponding to Oracle's client, middleware, and RDBMS;
• a Development Environment (NetSolutions) that gives developers common tools and functions to access underlying services; and
• a common Management Environment, provided by the Oracle Enterprise Manager systems-management product.
Cartridges
Cartridges are a signiﬁcant advance over previous Oracle development aids as well as other RDBMS suppliers’ data-oriented Universal-Server "DataBlades". Cartridges allow the developer
to write, in a common way, components that run on all Web or non-Internet client, application server, or database server platforms. Since cartridges are high-level "component" objects, the
developer can gain productivity both from programming at a higher level and from object-oriented technology’s advantages. Cartridges make the application highly extensible; developers
can easily add more high-level capabilities, either by developing a new cartridge based on old ones, or by acquiring customizable cartridges available in upcoming "component" markets.
Moreover, the developer gains added ﬂexibility: the developer can choose how to partition the application in new ways, e.g., by placing more functionality on the application server or the
backend database server. For example, in a medical-imaging application, the developer can place image translation in the client, application server, or database server cartridge, and easily
move it to another tier to handle system bottlenecks.
Cartridges are components (high-level object classes) that include an IDL (standard) interface and access "infrastructure" services across client-server, Internet, or distributed-object (e.g.,
peer-to-peer) architectures. To aid in making objects more manageable and packageable, Universal Cartridge Services provide component registration, installation on various platforms,
security, administration, and monitoring. In addition, Scaleable Cartridge Services carry out transaction, data-access, messaging, and queuing functions across client, application server, and
database server platforms. Finally, specialized Cartridge Services provide platform-speciﬁc services such as user-interface functions on the client; middleware functions such as
communications multiplexing, load balancing, and recovery on the application server; and "data manipulation" functions on the database server.
For presently existing "infrastructure" and application software, creating a cartridge is primarily a matter of wrapping it in an IDL interface. Thus, any existing software based on the client,
application server or database server can be "IDL-wrapped" to allow developers to access these services as cartridges. Likewise, users can invoke a wide variety of third-party software (e.g.,
Netscape ONE or a SQL client) as a cartridge. Enterprises can wrap legacy client-server and host applications to create cartridges in a relatively straightforward way. The result of creating a
cartridge in this manner is more open, reusable, and ﬂexible software.
Aberdeen anticipates that there will be a highly-useful cartridge market: a pool of Oracle, third-party, and home-grown cartridges for which ISVs can develop, and into which an ISV or
enterprise can dip for particular development needs. Oracle plans to encourage third-party supplier creation of cartridges, and to make such a "pool" available to its customers. As a result,
over the next year users should expect the arrival of a wide variety of cartridges from which to choose.
The Core Of The Architecture: Inter-Cartridge Exchange
Oracle’s ICX can be thought of as an "object bus": a set of tools and a database of component addresses on the same or different platforms that allows a cartridge to invoke another cartridge
or component in a location-independent way. ICX is based on the Object Management Group’s CORBA standard for Object Request Brokers (ORBs, the database of component addresses
and associated tools), and uses Oracle’s Web Request Broker ORB. ICX also provides bridges to Microsoft’s COM ORB, thus providing support for both of today’s major ORB approaches.
When a component invokes another component across platforms, ICX supports today’s open Internet protocols (HTTP and Netscape’s IIOP).
ICX is particularly useful in allowing enterprise developers to access cartridges, components, or services on other platforms or written for other architectures without having to specify a
location or architecture-dependent information. Moreover, since ICX provides a connection between Oracle’s Network Computing Architecture cartridges, the developer can invoke a client
cartridge and know that backend application-server and database-server functions will be carried out automatically, across architectures. For "mixed" architectures in which some instances of
an application are operating across the Internet while others are running client-server on local LANs, ICX coordinates the application instances, and allows the developer to write one
program for all cases.
The Core of the Architecture: Software Platforms and Services
Oracle maps its infrastructure services into three platforms: a Universal Client, a Universal Application Server, and a Universal Server. The Client aims to allow users to choose any of
today’s popular desktop environments that span Windows and Internet functionality: Netscape’s ONE, Microsoft’s ActiveX Desktop, Oracle’s network computer machines, or SQL client
software. Cartridges based on these core Services will be programmable using today’s popular client-side 3GLs and 4GLs – Java/JavaScript, C/C++, Microsoft’s Visual Basic, and ANSI SQL
Level 3 (including PL/SQL).


The Universal Application Server includes an integrated set of middleware, one for each type of environment (multi-tier client-server, Internet, and distributed-object). For the Internet,
Oracle’s Web Request Broker carries out HTTP connections and provides an ORB to Web-cartridge developers. For performance scalability, this allows developers to bypass low-
performance CGI and low-level APIs. For distributed-object environments, Oracle provides transaction, data-access, and messaging functions based on an ORB, and manages IIOP
connections. For client-server environments, an Oracle Connectivity Broker based on Oracle’s gateway products handles all other connections (e.g., client-server via Oracle’s SQL*Net
protocol or mobile-user connections).
The Universal Server is Oracle’s Universal Server RDBMS, enhanced to provide cartridge access. Thus, cartridges can access the Universal Server’s PL/SQL-based stored procedures, or can
access the Universal Server via SQL/multimedia Extensions/3GL calls, or can use Database Extensibility Services that access the Universal Server via IIOP. The Database Extensibility
Services include the ability to invoke Oracle’s query optimizer, access methods, and administration functions, giving the developer exceptional open, hands-on control over database tuning.
Enterprises may ﬁnd Oracle’s Services especially attractive because of the breadth of the functionality that they expose to the developer. Oracle’s client-side and middleware products are
especially attractive where the Internet is involved, because they provide proven client-server technologies such as cursors, governors, and load balancing to deliver scalability of Intranet and
Web-enabled data-intensive applications. Oracle’s Universal Server offers a breadth of RDBMS server technology unbeaten in the industry, including parallel-scalable technology for today’s
parallel hardware, replication technology for such distributed-database solutions as data warehouses and data marts, and Universal Server technology for multimedia and complex-data-type
applications.
Development Environment
The Development Environment gives the developer access to Network Computing Architecture services. At present, it includes Oracle's powerful Designer/2000 (for Web program design)
and Developer/2000 (for Web programming) Web-enabled client-server development toolsets, plus a new Cartridge Development Kit that has sample code and a Developer's Guide.
Developers can also use their own 3GLs and 4GL scripting languages, such as Java/JavaScript, C/C++, Visual Basic, or PL/SQL.
The Development Environment's added value for the enterprise lies in both the existing Oracle toolsets and the addition of cartridge development tools. As noted in the Aberdeen Client-
Server Application Development Environment Buying Guide, the combination of Designer/2000 and Developer/2000 offers exceptionally broad development capabilities that implement key
technologies delivering scalability, open ﬂexibility, programmer productivity, and software-lifecycle support. Moreover, Designer/2000 and Developer/2000 offer technologies that are
exceptionally useful in the new architectures, e.g., application partitioning that allows automatic software deployment across the Internet. Designer/2000 and Developer/2000 have recently
been Web-enabled, so that not only new applica-tions but also legacy client-server applications written using Developer/2000 can be translated to Internet architectures with relatively little
effort.
Management Environment
Oracle’s Management Environment is the Oracle Enterprise Manager, extended to allow cartridge access. Oracle Enterprise Manager is a GUI-based systems-management suite that provides
map and tree views and easy, drag-and-drop reconﬁguration operations. Oracle Enterprise Manager includes a long list of general and database administration utilities, such as job scheduling
and logging, event management, monitoring and diagnostics, replication management, network management, database administration utilities, and software distribution. Oracle Enterprise
Manager also provides SNMP MIB (management information base) support that allows it to integrate its solutions with other global systems-administration products such as HP's OpenView.
As with the other Network Computing Architecture products, Oracle is extending Oracle Enterprise Manager with cartridge support to allow developers to invoke Oracle Enterprise
Manager’s administrative utilities.
Network Computing Architecture’s Management Environment gives users added value particularly in two areas: the ability of programmers to invoke database and systems management
functions via the cartridge interface, and Oracle’s extensive administration functionality. For example, developers can access Oracle’s data-dictionary metadata to allow programming of data-
intensive applications at a higher level, and users can apply the same Oracle Enterprise Manager administration across Intranet, client-server, and host environments – a one-stop, expandable
administration toolset.
Where Oracle’s Network Computing Architecture Is Most Effective
Oracle’s Network Computing Architecture offers a golden opportunity for third-party ISVs to differentiate themselves with relatively little effort. By using high-level cartridges, ISVs can
create new portable, customizable, and extensible appli-cations that are easy to install, run on all major platforms and enterprise architec-tures, and can adapt readily to changing network and
system loads. Moreover, ISVs can sell components as well as solutions in the upcoming cartridge market, and use functional or vertical-industry components available from Oracle or the
market to build their applications or components more rapidly, starting from a higher level.
Oracle’s Network Computing Architecture can be particularly effective where IS buyers are trying to scale Intranet architectures to handle data-intensive applications or integrate them with
"legacy" client-server and host applications. Where users are trying to scale Intranets, Oracle’s underlying Internet services bypass often-bottlenecked Web browsers and servers provide
proven client and server technology for minimizing client-to-server communications, and offer communications multiplexing and load balancing to minimize the load on the server. Oracle’s
services allow developers to Web-enable legacy applications by "wrapping" them as cartridges, to improve their Internet performance (for Developer/2000-created applications) by altering
the split between client and server via application partitioning, and to access backend applications and databases via gateways.
The Network Computing Architecture can also help where enterprises are trying to minimize the cost and time of moving to Internet and/or distributed-object technologies, or improve
programmer productivity in creating mission-critical data-intensive applications. As noted above, cartridges allow developers to write one piece of code that can handle all three architectures
– client-server, Internet, and distributed-object – thus improving programmer productivity and avoiding the need to train developers in the complex and arcane details of the new
technologies. Since cartridges are high-level components, developers can increase productivity both by component reuse and by operating at a higher level. And since legacy applications can
be wrapped as cartridges, moving these applications to the Internet rather than creating new ones becomes relatively easier and faster.
Aberdeen Conclusions
Aberdeen ﬁnds that Oracle’s Network Computing Architecture is that rare combination, a large goal that can be reached with relatively low risk. The Network Computing Architecture’s goal
– allowing ISVs and IS to use the new Internet and distributed-object architectures and technologies effectively while protecting investments in client-server and host applications and
environments – offers ISVs the ability to write portable, customizable, and extensible applications at a higher level for greater productivity; and it requires IS only to build new applications
on cartridges and wrap old ones as cartridges, in a relatively easy procedure. Since most cartridges on which the developer builds are based on broad and proven Oracle functionality, creating
new applications is relatively low-risk; and the Network Computing Architecture’s straightforward way of wrapping old applications as cartridges allows users to leverage more low-risk
legacy applications rather than scrapping them for new ones.
Given the rapid pace of Internet technology, the Network Computing Architecture is necessarily a work in progress. Over the next 1-2 years, Aberdeen anticipates that Oracle will integrate
Microsoft’s COM more tightly with the Network Computing Architecture, will provide more advanced tools within Developer/2000 for creating and distributing cartridges, will release a
spate of new cartridges customized for typical business functions such as ﬁnance and typical vertical industries, will add extensive Web-based consulting and service, and will continue to
improve the underlying technologies’ scalability and ﬂexibility.
Overall, Oracle’s Network Computing Architecture is a leadership technology suite for ISVs and IS buyers seeking to move effectively into today’s new Internet and distributed-object
technologies. Aberdeen recommends that most ISVs and users not only prototype and test its capabilities but also factor it into their strategies as a clear and comprehensive migration path for
the next 1-2 years.


AberdeenGroup, Inc.
One Boston Place
Boston, Massachusetts
02108 USA
Tel: 617.723.7890
Fax: 617.723.7897
Contact Information:
Susan Rinehart, Client Services Manager(direct #: 617.854.5212)
David Borde, Marketing Manager (direct #: 617.854.5226)
Email: rinehart@aberdeen.com or borde@aberdeen.com
The trademarks and registered trademarks of the corporationsmentioned in this publication are the property of their respective holders. Unless otherwise noted, the entire contents of this publication are copyrightedby Aberdeen
Group, Inc. and may not be reproduced, stored in a retrieval system,or transmitted in any form or by any means without prior written consent of thepublisher.
Copyright © 1996 Aberdeen Group, Inc., Boston, Massachussetts
This Document is for Electronic Distribution Only
-- REPRODUCTION PROHIBITED --


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-oracle-network-computing-architecture |
| title | Oracle's Network Computing Architecture |
| author | Aberdeen Group |
| date | 1996-10-01 |
| type | market-study |
| subject_domain | enterprise-software, distributed-computing, internet-architecture, RDBMS |
| methodology | industry-analysis, competitive-profiling, expert-opinion, document-review |
| source_file | 1996 Oracle's Network Computing Architecture pr.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group evaluates Oracle's Network Computing Architecture (NCA), a comprehensive framework integrating multi-tier client-server, Internet, and distributed-object technologies through a 'cartridge' component model and Inter-Cartridge Exchange (ICX) middleware based on CORBA. The study concludes that NCA is not a 'marketecture' but a substantive extension of proven Oracle products providing a least-cost migration path to mission-critical 21st-century transaction processing, and recommends ISVs and enterprise IS factor it into their 1-2 year technology strategies.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Oracle's NCA represented a defining moment in enterprise middleware strategy as the industry transitioned from client-server to Internet architectures; Aberdeen's endorsement of NCA over competing approaches from Microsoft and others carried significant weight with enterprise IT buyers. |
| **Relevance** | medium | The cartridge/component model anticipated modern microservices and API-based architectures; Oracle's Universal Server became the foundation for Oracle Database which remains active, though NCA-specific cartridge mechanisms are long obsolete. |
| **Prescience** | high | Aberdeen correctly predicted Oracle would dominate enterprise internet database strategy and that component-based architecture would become the standard; Oracle remains a dominant enterprise database and application platform 30 years later. |

### Prescience Detail

**Prediction 1:** NCA adoption recommendation
- **Claimed:** Aberdeen recommends ISVs and IS not only prototype but factor NCA into strategies for next 1-2 years
- **Year:** 1996
- **Confidence at time:** high
- **Source:** Aberdeen Conclusions

**Actual Outcome 1:** NCA commercial outcome
- **Result:** NCA succeeded in establishing Oracle as enterprise internet platform; Oracle grew to dominant position
- **Confidence:** verified
- **Notes:** Oracle remained #1 enterprise RDBMS; NCA evolved to Oracle9iAS then Oracle Fusion

**Prediction 2:** NCA cartridge market prediction
- **Claimed:** Thriving market in vertical/functional cartridges expected within next year
- **Year:** 1996
- **Confidence at time:** medium
- **Source:** Cartridges

**Actual Outcome 2:** NCA commercial outcome
- **Result:** NCA succeeded in establishing Oracle as enterprise internet platform; Oracle grew to dominant position
- **Confidence:** verified
- **Notes:** Oracle remained #1 enterprise RDBMS; NCA evolved to Oracle9iAS then Oracle Fusion

**Prediction 3:** Oracle roadmap: COM tighter integration
- **Claimed:** Aberdeen anticipates Oracle will integrate Microsoft COM more tightly over 1-2 years
- **Year:** 1996
- **Confidence at time:** medium
- **Source:** Aberdeen Conclusions

**Actual Outcome 3:** NCA commercial outcome
- **Result:** NCA succeeded in establishing Oracle as enterprise internet platform; Oracle grew to dominant position
- **Confidence:** verified
- **Notes:** Oracle remained #1 enterprise RDBMS; NCA evolved to Oracle9iAS then Oracle Fusion

**Prediction 4:** Oracle roadmap: Developer/2000 cartridge tools
- **Claimed:** More advanced tools within Developer/2000 for creating and distributing cartridges expected
- **Year:** 1996
- **Confidence at time:** medium
- **Source:** Aberdeen Conclusions

**Actual Outcome 4:** NCA commercial outcome
- **Result:** NCA succeeded in establishing Oracle as enterprise internet platform; Oracle grew to dominant position
- **Confidence:** verified
- **Notes:** Oracle remained #1 enterprise RDBMS; NCA evolved to Oracle9iAS then Oracle Fusion

**Prediction 5:** Oracle roadmap: vertical cartridges
- **Claimed:** Release of cartridges customized for business functions (finance) and vertical industries expected
- **Year:** 1996
- **Confidence at time:** medium
- **Source:** Aberdeen Conclusions

**Actual Outcome 5:** NCA commercial outcome
- **Result:** NCA succeeded in establishing Oracle as enterprise internet platform; Oracle grew to dominant position
- **Confidence:** verified
- **Notes:** Oracle remained #1 enterprise RDBMS; NCA evolved to Oracle9iAS then Oracle Fusion


### Entities Referenced (6)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Oracle Corporation | company | active | — |
| Aberdeen Group, Inc. | firm | acquired | Harte-Hanks -> Aberdeen Strategy & Research |
| Microsoft Corporation | company | active | — |
| Netscape Communications | company | dissolved | AOL 1999; browser discontinued 2008 |
| Object Management Group (OMG) | institution | active | — |
| Hewlett-Packard (HP) | company | active | HP Inc + HPE (split 2015) |

### Technologies Referenced (10)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Oracle Network Computing Architecture (NCA) | framework | Oracle Corporation | emerging | obsolete |
| Oracle Universal Server (RDBMS) | platform | Oracle Corporation | mature | active |
| CORBA (Common Object Request Broker Architecture) | protocol | OMG standard | emerging | obsolete |
| ActiveX / COM (Microsoft) | framework | Microsoft | emerging | obsolete |
| Java / JavaScript | language | Sun Microsystems | emerging | active |
| Oracle Developer/2000 | application | Oracle Corporation | mature | obsolete |
| Oracle Designer/2000 | application | Oracle Corporation | mature | obsolete |
| Oracle Enterprise Manager | application | Oracle Corporation | emerging | active |
| Oracle Web Server / Web Request Broker | application | Oracle Corporation | emerging | obsolete |
| Oracle NetSolutions | framework | Oracle Corporation | emerging | obsolete |

### Observation Summary

- **Total observations:** 30
- **By type:**
  - actual-outcome: 5
  - benchmark-result: 2
  - expert-opinion: 1
  - framework-factor: 3
  - market-data: 2
  - strategy-classification: 2
  - technology-assessment: 10
  - viability-prediction: 5

---

*Copyright © 1996 Aberdeen Group, Inc., Boston, Massachusetts. Archived for research purposes under CC-BY-4.0.*
*Source: [https://web.archive.org/web/19970604113530/http://www.aberdeen.com:80/secure/profiles/oraclnca/orclnca.htm](https://web.archive.org/web/19970604113530/http://www.aberdeen.com:80/secure/profiles/oraclnca/orclnca.htm)*
