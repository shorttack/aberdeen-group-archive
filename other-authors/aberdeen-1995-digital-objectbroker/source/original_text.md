# Digital's ObjectBroker -- Advanced Integration of Distributed Resources

> Archived from: https://web.archive.org/web/19970112012511/http://www.aberdeen.com:80/secure/profiles/objbrk/decobj.htm
> Original publication date: 1995-08-01
> Author: Aberdeen Group

---

## Original Document Text

Digital Equipment Corporation
Enterprise Software Group
110 Spit Brook Road
Nashua, NH 03062-2698
603-881-2317
Digital's ObjectBroker -- Advanced Integration of Distributed Resources
Digital's advanced ObjectBroker product family has been successfully used in numerous situations to coordinate and integrate distributed resources into new business solutions. Based on
object request broker (ORB) technology, ObjectBroker consists of a development toolset and runtime environment and provides a common interface through which various software
components can communicate -- uniting information resources. Digital is the only major systems supplier in this market that can combine an ORB-based product that works today with
extensive professional services capabilities and a proven track record.
As organizations rush to deploy new line-of-business, client-server applications that automate and improve business processes, a common theme is the desire to access data and services from
across the enterprise. Companies have found that individuals often need information from multiple departments to do their job. A salesperson, for example, may need to simultaneously
access inventory data, shipping schedules and customer credit ratings. The main obstacle is that the information system infrastructure is an ever-changing hodge-podge of individual systems
from multiple suppliers -- not originally intended to work with each other. Most Fortune 1000 companies have multiple systems deployed -- ranging from proprietary mainframes to Unix
servers to desktop PCs. As a result, one of the major assignments for developers is systems integration, in which heterogeneous systems are forged into a coherent enterprise-wide
infrastructure. Digital is able to solve this problem today with ObjectBroker.
Aberdeen believes that ObjectBroker is useful to information systems (IS) organizations, independent software vendors (ISVs) and systems integrators alike. The rest of the Proﬁle will detail
why ObjectBroker is an excellent systems integration solution and discuss how organizations can use it to their advantage.
Systems Integration through Distributed Object Computing
The advantages of integrating distributed resources are clear. Users have access to the information they need. When properly designed and implemented, these resources appear to be local,
even though they may actually reside on multiple, remote systems. In order to integrate distributed resources, two things must be done:
A common communications mechanism must be in place. Software on various heterogeneous platforms may execute differently and use different formats and protocols. There needs to
be a standard way for requests and returning services and data to be passed from one system to another.
Developers and users need to be able to ﬁnd the appropriate data and services they need, learn how to invoke those services, and register new services as they are created. A directory of
resources is critical.
To meet these needs, a growing number of leading organizations are ﬁnding that object request broker technology is the best solution. An ORB essentially acts as a trafﬁc cop, directing
requests from one system (the client) to one or more other systems (servers) which respond with the proper information. An ORB maintains a directory or repository to keep track of where
each software module or object is located, describes what it does, and speciﬁes how to call it. New services can be added to the repository on an ongoing basis. Additionally, should a
software component be modiﬁed or moved to a different system, only the repository needs to be updated. The rest of the system remains unaffected. The ORB is also responsible for
translating messages between different systems. Software complexity is hidden behind public interfaces that list what each object or software module does. As a result, object request brokers
are ideal for building and integrating distributed resources.
The advantages of an ORB-based architecture are three-fold. First, an ORB is an elegant means to integrate heterogeneous resources and provide a single view of the data. Companies have
used ORB technology to encapsulate existing data and services. A front-end graphical application can then be built with tools such as VisualBasic or PowerBuilder. The end-user is provided
with an environment that makes all these distributed resources appear to be located in one place -- making it much easier to ﬁnd the right information. The second advantage is that when one
software module is modiﬁed or moved, any other software components that depend on the code being changed are insulated and do not have to be updated. The third advantage is that object
request brokers enable companies to safely and securely add new technologies and functionality at their own pace.
The Object Management Group (OMG) is an industry consortium of information technology users and suppliers that establishes and promotes ORB standards. OMG's Common Object
Request Broker Architecture (CORBA) is supported by over 450 companies, including all the major hardware and software suppliers. The main focus of CORBA is to standardize the
interfaces between the components of a distributed computing environment. This is done by requiring all systems to use a common Interface Deﬁnition Language (IDL). Figure 1 shows how
Digital's ORB implementation, ObjectBroker, works in this scenario.
Aberdeen believes that ORBs will become increasingly critical as more companies look to pull together disparate systems. ObjectBroker is a market-leading object request broker
implementation that provides unique advantages to its customers.
Speciﬁc Business Advantages of ObjectBroker
In conducting its ﬁeld research, Aberdeen repeatedly ran into four major beneﬁts of ObjectBroker that put it beyond the competition. They are:
Encapsulation of Legacy Systems -- A core strength of ObjectBroker is its ability to wrap legacy systems with a CORBA-compliant, object-oriented interface. To the outside world, the
legacy system appears to be and acts as one or more independent objects. There is no discernable difference between this encapsulated procedural code and another software component
constructed using object-oriented techniques. This not only preserves existing software assets, it enhances their value by making them available for use in new applications.
Multiple Platform Support -- ObjectBroker supports 19 hardware/operating system combinations. No one else can claim the breadth of coverage that Digital can. This enables systems
integration across multiple, heterogeneous platforms -- a key user requirement. Developers do not have to custom build a system using ORBs from multiple suppliers and learn the
intricacies of each product. Additionally, having the same ORB implementation on all platforms makes systems management much easier and means that there is only one vendor
relationship for the user organization to administer.
Microsoft OLE-COM Integration -- While the CORBA standard prevails at the Unix server level, Microsoft's Object Linking and Embedding (OLE) standard and its underlying
Component Object Model (COM) dominate Windows-based desktops. Neither is going to displace the other. Any realistic solution for systems integration must accommodate both.
Digital has been a driving force in linking the two standards and is able to provide OLE-CORBA integration today.


Application Partitioning and Resource Identiﬁcation -- Digital has made some important extensions to IDL with its Implementation Mapping Language (IML) and Method Mapping
Language (MML). IML is used to describe the characteristics of each object implementation and MML tells how to select among multiple implementations of an object. This makes it
easy for developers to identify and work with distributed software components when building a new application or enhancing existing ones.
There are two other important reasons for selecting ObjectBroker. The ﬁrst is that Digital is a multi-billion dollar full-services ﬁrm that can provide the services and support users need. The
other is ObjectBroker's long history of success, having been ﬁrst introduced in 1991. IS decision makers want a proven solution.
ObjectBroker Product Speciﬁcs
ObjectBroker 2.5 is both a software development tool and a runtime environment. The product evolved from Digital's ACA Services offering. The core components of ObjectBroker include
the ORB Core itself, the Repositories for storing IDL, IML and MML deﬁnitions, Registries that contain conﬁguration information, and Context Objects which provide information about
each user and system. There is a command line interface for loading repositories as well as generating and compiling code. There are also application programming routines for
communicating with OLE- and DDE-aware servers. Finally, there are several graphical utilities, including a Systems Administrator, a Network Tester, a Context Object Editor, a Repository
Manager, an Implementation Viewer, an OLE Network Portal, and a DDE Listener.
The development toolset is used to build new applications and encapsulate legacy systems with CORBA-compliant ObjectBroker interfaces. Existing callable APIs are wrapped with the
Skeleton Server, while command line interfaces are encapsulated with the Script Server. Developers can edit IDL, IML and MML code and link and compile the components of an
application.
The runtime forms a layer between an application and the network and operating system environment. The ObjectBroker runtime is deployed on every hardware platform that is part of the
distributed computing environment. The runtime layer can be purchased on a per-machine basis. Prices start at $149 per seat for PCs and is structured based on the hardware/operating
system combination, with volume discounts available. The Unix version of the development tool is priced at $5,000 per seat and an NT development seat costs $980. The runtime is included
as part of Digital's NAS (Network Application Support) which is installed on over half of all Digital systems sold. As a result, an organization may have a signiﬁcant number of
ObjectBroker-ready systems already installed.
ObjectBroker currently conforms to version 1.2 of the CORBA speciﬁcation. Digital is working on making the product CORBA 2.0-compliant. CORBA 2.0 mainly speciﬁes how ORBs from
different vendors communicate with each other. ObjectBroker 2.5 supports IDL bindings to C and a Visual Basic DLL. ObjectBroker 2.6 will provide a CORBA 2.0 IDL-to-C++ binding. The
speciﬁc platforms supported by ObjectBroker are: Digital UNIX, ULTRIX, and Open VMS (Alpha and VAX) Windows 3.1, Windows NT (on Intel and Alpha), HP-UX, AIX, OS/2, SunOS,
Solaris, Macintosh System 7, and Tandem's Integrity and NonStop Kernel. The Tandem ports are the result of Logica North America, Inc. All other implementations have been done by
Digital.
OLE Integration -- Taking the Lead in Uniting Both Camps
Digital recognized the importance of OLE to most user organizations and has established a strong strategic partnership with Microsoft. The CORBA and OLE-COM worlds must work with
each other and Digital is a leader in this work. Digital and Microsoft are actively working with the OMG to develop standards for this integration. Aberdeen believes that OLE-COM will
dominate on Windows desktops and NT servers while CORBA will be focused on Unix servers. By including both OLE and CORBA in its strategy, Digital gives its customers the desktop
connectivity they need for building client-server applications.
Digital's OLE Integration is made possible by the OLE Network Portal contained in ObjectBroker 2.5 for Windows. The portal locates OLE-aware servers in the ObjectBroker registry and
presents an OLE 2.0 interface to Windows applications. As a result, client platforms can access and embed multiple remote OLE data objects. There is also a DDE Gateway that can accept
DDE messages.
ObjectBroker 2.6 will have OLE Automation Support. This will allow OLE applications to access not only remote data, but also the services and functionality of remote CORBA objects and
services. As an example, an OLE 2.0 client (such as Excel) will be able to remotely request that a CORBA object perform a calculation, in addition to transfering data.
Future versions of ObjectBroker will provide a bi-directional bridge between the CORBA and COM object models. Developers will no longer need to know the intricacies of both models in
order to build links. COM objects will look like CORBA objects to the CORBA developer and vice versa -- further hiding software complexity. This will allow programmers to use an OLE-
aware development tool, such as PowerBuilder, to access CORBA objects.
What's New in August 1995
The most recent new development from Digital is the formal announcement of ObjectBroker 2.6. With general availability expected in early 1996, version 2.6 will have several
enhancements useful for both encapsulating existing functionality as well as creating new, distributed object code. Speciﬁcally, the new release will include:
A Secure ORB -- ObjectBroker will make use of the GSS API for DCE, making Kerberos-level security possible.
OLE Automation -- As discussed above, users will now be able to access data and functionality from remote CORBA objects.
C++ Language Binding -- IDL will be directly mapped to C++ enabling developers to program in a native C++ environment.
APIs for Systems Management -- ObjectBroker has had some APIs added so that non-Digital systems management tools and customer applications can get access to systems
management functions.
"Quick Start" Capability -- This new capability will automatically generate the basic application framework by reading the IDL speciﬁcations created by the developer. As a result,
developers can have a running client-server skeleton in ten minutes.
Better Performance -- While adding all of these new features, Digital has also improved ObjectBroker's performance signiﬁcantly.
In addition, support will be forthcoming for the following platforms:
IBM MVS
OS/400
Windows 95
Silicon Graphics' IRIX (This port is being done by Logica.)
ObjectBroker will be the ﬁrst ORB to directly support an MVS mainframe environment, which will increase its appeal to IS organizations.
Developing with ObjectBroker
There are basically three development activities where ObjectBroker plays a role (see Figure 2). Digital's experience is that these steps typically follow a chronological order, although on
certain projects the order may change depending on each customer's unique requirements. The ﬁrst initiative is to encapsulate existing distributed data and software functionality and then
link these modules into a cohesive whole. The goal is to make all resources appear local to the user. This is done by ﬁrst identifying the software resources required for an application. The
existing local APIs and command line interfaces are then wrapped with an IDL interface. Each software module is then registered with the repository so that it can be located when needed.
Finally, the links are established, either statically or dynamically, between the various software components.


The second process consists of upgrading these legacy components by either adding new functionality or rearchitecting them to follow an object-oriented model. As these modiﬁcations take
place, the interfaces remain the same. ObjectBroker plays the critical role of insulating the outside world from internal changes to an object or software component.
The third and ﬁnal procedure is to develop completely new objects and applications and link these into the ObjectBroker infrastructure. New components are developed by ﬁrst specifying
them in IDL. Using a standard C++ compile, edit debug tool, the actual source code is generated and links are established. The objects are then deployed and registered with the repository.
To help in this process, Digital provides its ObjectPlus development environment. This special version of Protosoft's Paradigm Plus analysis and design tool has been modiﬁed to
automatically generate IDL code.
Digital's Professional Services
A systems integration project cannot live by software alone. There must also be training and implementation services as well as the overall expertise that turns a product into a solution. To
meet this need, Digital provides services and support through a variety of channels.
Digital has a force of specialized software support engineers that are focused on making sure ObjectBroker customers succeed with the product. ObjectBroker customers also have access to
Digital's worldwide ﬁeld service organization. Aberdeen views Digital's size and corresponding professional services resources as a major advantage of selecting ObjectBroker. In addition,
Digital has several third-party partners that also provide expert advice and implementation services. Some of the more notable of this group are The Cushing Group and NetLinks Technology
-- both from Nashua, NH. Logica North America provides support for Tandem and SGI machines, and Linkvest is a key service provider in Europe. Digital is also actively recruiting large
systems integrators and value-added resellers. Digital recognizes that training and industry infrastructure is a major factor in how fast it can grow its ObjectBroker business. The company
expects demand to increase quickly over the next 12 to 24 months and is deploying resources accordingly.
ObjectBroker Sales and Marketing
To date, most ObjectBroker customers are user organizations in need of systems integration assistance. These companies often turn to Digital when they realize that they can no longer easily
add new components and functionality to existing systems. It has become too difﬁcult for them to extend their existing applications and deploy new ones. The reason customers choose
ObjectBroker is not necessarily because it is object-oriented or conforms to CORBA, but because it solves their problems. Digital's initial installations have been concentrated in the banking,
ﬁnancial services, and discrete and process manufacturing sectors.
Digital is also beginning to see interest from independent software vendors. These companies feel that they can distinguish themselves in the market by providing access to complementary,
3rd-party applications. For example, a provider of a human resources application may gain a market advantage by building a seamless interface to a ﬁnancial system. These ISVs are
naturally attracted to ObjectBroker's support for multiple, heterogeneous platforms and its ability to serve as the basic systems infrastructure for a distributed computing environment.
ObjectBroker releases ISVs -- as well as systems integrators -- from having to build this infrastructure themselves. To capitalize on this market, Digital is establishing more formal programs
for ISVs.
Figure 3: Why Pick ObjectBroker?
Currently, ObjectBroker is primarily sold by software specialists in Digital's direct sales force. This group actively promotes ObjectBroker to existing Digital clients as well as outside the
installed base of Alpha and VAX systems. In addition to this dedicated sales force, general account representatives have also uncovered several opportunities through their ongoing client
interaction.
Logica is the principal sales channel for the Tandem and SGI implementations. Digital also plans to recruit a partner to help it penetrate MVS accounts. Finally, major professional services
ﬁrms and systems integrators will resell Object Broker as they use it in their own customer assignments. EDS is one such ﬁrm that is using ObjectBroker.
Aberdeen Conclusions
ObjectBroker is highly strategic for Digital and has the support of senior management. It is one of the few areas in Digital that has consistently had increases in investment during the recent
years of cost cutting. Aberdeen believes the stature of ObjectBroker will continue to grow both at Digital and with its customers.
ObjectBroker is an excellent implementation of ORB technology and from day one has been designed to solve real customer problems. Rather than make esoteric claims about reusing source
code, ObjectBroker gets to the heart of the matter reusing services and information. By taking this high level approach, Digital helps its customer leverage existing systems and increase the
value of their software portfolio. Organizations can build ﬂexible systems that adapt to changing business needs.
Digital is the only major systems supplier today that can offer a working implementation with a proven long history of success. The company's size and resources mean it has the services and
support needed to implement a solution. ObjectBroker's multiplatform support and OLE integration lets IS organizations and ISVs choose a single ORB vendor without limiting their options.
The popularity of ObjectBroker will continue to increase as companies build next generation client server applications that take advantage of existing software resources.
Aberdeen Group
One Boston Place
Boston, Massachusetts
02108
Telephone: 617-723-7890
FAX: 617-723-7897

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1995-digital-objectbroker |
| title | Digital's ObjectBroker -- Advanced Integration of Distributed Resources |
| author | Aberdeen Group |
| date | 1995-08-01 |
| type | product-profile |
| subject_domain | distributed-object-computing |
| methodology | industry-analysis,competitive-profiling,field-research |
| source_file | 1995-oo-dev-Digital_s-Object-Broker-pr-9.pdf |
| license | CC-BY-4.0 |

### Abstract

Profile evaluating Digital Equipment Corporation's ObjectBroker, a CORBA-compliant object request broker for integrating distributed heterogeneous resources. Examines ORB technology, legacy system encapsulation, OLE-COM integration, and 19-platform support.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | CORBA and ORB technology were the central distributed computing standard battle of the mid-1990s with 450+ industry supporters; Aberdeen's analysis of ObjectBroker informed Fortune 1000 integration architecture decisions worth billions. |
| **Relevance** | medium | CORBA itself is largely obsolete but the architectural patterns (distributed object invocation, IDL contracts, platform-neutral integration) directly prefigure gRPC, Protobuf, and microservices. The ORB as middleware concept transferred to ESB, API gateways, and service mesh. |
| **Prescience** | low | Core predictions failed: OLE-CORBA interop was abandoned by Microsoft, DEC/ObjectBroker was discontinued after Compaq acquisition in 1998, and CORBA was supplanted by SOAP/REST/microservices. Only short-term 2.6 feature roadmap was confirmed. |

### Prescience Detail

**Prediction 1:** ObjectBroker 2.6 announcement
- **Claimed:** GA expected early 1996
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 1.1:** ObjectBroker 2.6 release and CORBA 2.0 compliance — actual outcome
- **Result:** ObjectBroker 2.6 released 1996 with CORBA 2.0 features as predicted; however DEC acquired by Compaq 1998, ObjectBroker product line discontinued; renamed Compaq ObjectBroker briefly then terminated
- **Confidence:** verified
- **Notes:** Short-term prediction (OBS-025, OBS-028) confirmed: 2.6 shipped in 1996. Long-term: product killed by acquisition. DEC/Compaq ObjectBroker history documented.

**Actual Outcome 1.2:** ObjectBroker IBM MVS mainframe support — actual outcome
- **Result:** ObjectBroker 2.6 did add MVS support as planned; however IBM's own CICS CORBA gateway and SOM/DSOM became primary IBM mainframe CORBA solutions by 1997
- **Confidence:** medium
- **Notes:** Prediction (OBS-032) confirmed in product: MVS support shipped. But IBM offered competing mainframe CORBA solutions; DEC/Compaq acquisition in 1998 ended ObjectBroker MVS track.

**Actual Outcome 1.3:** DEC ObjectBroker multi-platform ORB leadership — actual outcome
- **Result:** Failed: DEC acquired by Compaq 1998; ObjectBroker discontinued; IONA Technologies Orbix, Borland VisiBroker, and then IBM WebSphere MQ became enterprise middleware leaders
- **Confidence:** verified
- **Notes:** Prediction (OBS-036) wrong for long-term: DEC/ObjectBroker never established market leadership. IONA, Borland, and IBM dominated the ORB/middleware market that emerged.

**Prediction 2:** v2.6 feature: Secure ORB
- **Claimed:** GSS API / DCE / Kerberos security
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 2.1:** ObjectBroker 2.6 release and CORBA 2.0 compliance — actual outcome
- **Result:** ObjectBroker 2.6 released 1996 with CORBA 2.0 features as predicted; however DEC acquired by Compaq 1998, ObjectBroker product line discontinued; renamed Compaq ObjectBroker briefly then terminated
- **Confidence:** verified
- **Notes:** Short-term prediction (OBS-025, OBS-028) confirmed: 2.6 shipped in 1996. Long-term: product killed by acquisition. DEC/Compaq ObjectBroker history documented.

**Actual Outcome 2.2:** ObjectBroker IBM MVS mainframe support — actual outcome
- **Result:** ObjectBroker 2.6 did add MVS support as planned; however IBM's own CICS CORBA gateway and SOM/DSOM became primary IBM mainframe CORBA solutions by 1997
- **Confidence:** medium
- **Notes:** Prediction (OBS-032) confirmed in product: MVS support shipped. But IBM offered competing mainframe CORBA solutions; DEC/Compaq acquisition in 1998 ended ObjectBroker MVS track.

**Actual Outcome 2.3:** DEC ObjectBroker multi-platform ORB leadership — actual outcome
- **Result:** Failed: DEC acquired by Compaq 1998; ObjectBroker discontinued; IONA Technologies Orbix, Borland VisiBroker, and then IBM WebSphere MQ became enterprise middleware leaders
- **Confidence:** verified
- **Notes:** Prediction (OBS-036) wrong for long-term: DEC/ObjectBroker never established market leadership. IONA, Borland, and IBM dominated the ORB/middleware market that emerged.

**Prediction 3:** v2.6 feature: OLE Automation
- **Claimed:** Remote CORBA object access from OLE clients (e.g. Excel)
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 3.1:** ObjectBroker 2.6 release and CORBA 2.0 compliance — actual outcome
- **Result:** ObjectBroker 2.6 released 1996 with CORBA 2.0 features as predicted; however DEC acquired by Compaq 1998, ObjectBroker product line discontinued; renamed Compaq ObjectBroker briefly then terminated
- **Confidence:** verified
- **Notes:** Short-term prediction (OBS-025, OBS-028) confirmed: 2.6 shipped in 1996. Long-term: product killed by acquisition. DEC/Compaq ObjectBroker history documented.

**Actual Outcome 3.2:** ObjectBroker IBM MVS mainframe support — actual outcome
- **Result:** ObjectBroker 2.6 did add MVS support as planned; however IBM's own CICS CORBA gateway and SOM/DSOM became primary IBM mainframe CORBA solutions by 1997
- **Confidence:** medium
- **Notes:** Prediction (OBS-032) confirmed in product: MVS support shipped. But IBM offered competing mainframe CORBA solutions; DEC/Compaq acquisition in 1998 ended ObjectBroker MVS track.

**Actual Outcome 3.3:** DEC ObjectBroker multi-platform ORB leadership — actual outcome
- **Result:** Failed: DEC acquired by Compaq 1998; ObjectBroker discontinued; IONA Technologies Orbix, Borland VisiBroker, and then IBM WebSphere MQ became enterprise middleware leaders
- **Confidence:** verified
- **Notes:** Prediction (OBS-036) wrong for long-term: DEC/ObjectBroker never established market leadership. IONA, Borland, and IBM dominated the ORB/middleware market that emerged.

**Prediction 4:** v2.6 feature: C++ binding
- **Claimed:** CORBA 2.0 IDL-to-C++ binding
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 4.1:** ObjectBroker 2.6 release and CORBA 2.0 compliance — actual outcome
- **Result:** ObjectBroker 2.6 released 1996 with CORBA 2.0 features as predicted; however DEC acquired by Compaq 1998, ObjectBroker product line discontinued; renamed Compaq ObjectBroker briefly then terminated
- **Confidence:** verified
- **Notes:** Short-term prediction (OBS-025, OBS-028) confirmed: 2.6 shipped in 1996. Long-term: product killed by acquisition. DEC/Compaq ObjectBroker history documented.

**Actual Outcome 4.2:** ObjectBroker IBM MVS mainframe support — actual outcome
- **Result:** ObjectBroker 2.6 did add MVS support as planned; however IBM's own CICS CORBA gateway and SOM/DSOM became primary IBM mainframe CORBA solutions by 1997
- **Confidence:** medium
- **Notes:** Prediction (OBS-032) confirmed in product: MVS support shipped. But IBM offered competing mainframe CORBA solutions; DEC/Compaq acquisition in 1998 ended ObjectBroker MVS track.

**Actual Outcome 4.3:** DEC ObjectBroker multi-platform ORB leadership — actual outcome
- **Result:** Failed: DEC acquired by Compaq 1998; ObjectBroker discontinued; IONA Technologies Orbix, Borland VisiBroker, and then IBM WebSphere MQ became enterprise middleware leaders
- **Confidence:** verified
- **Notes:** Prediction (OBS-036) wrong for long-term: DEC/ObjectBroker never established market leadership. IONA, Borland, and IBM dominated the ORB/middleware market that emerged.

**Prediction 5:** v2.6 feature: Systems Management APIs
- **Claimed:** Non-Digital sysmanagement API access
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 5.1:** ObjectBroker 2.6 release and CORBA 2.0 compliance — actual outcome
- **Result:** ObjectBroker 2.6 released 1996 with CORBA 2.0 features as predicted; however DEC acquired by Compaq 1998, ObjectBroker product line discontinued; renamed Compaq ObjectBroker briefly then terminated
- **Confidence:** verified
- **Notes:** Short-term prediction (OBS-025, OBS-028) confirmed: 2.6 shipped in 1996. Long-term: product killed by acquisition. DEC/Compaq ObjectBroker history documented.

**Actual Outcome 5.2:** ObjectBroker IBM MVS mainframe support — actual outcome
- **Result:** ObjectBroker 2.6 did add MVS support as planned; however IBM's own CICS CORBA gateway and SOM/DSOM became primary IBM mainframe CORBA solutions by 1997
- **Confidence:** medium
- **Notes:** Prediction (OBS-032) confirmed in product: MVS support shipped. But IBM offered competing mainframe CORBA solutions; DEC/Compaq acquisition in 1998 ended ObjectBroker MVS track.

**Actual Outcome 5.3:** DEC ObjectBroker multi-platform ORB leadership — actual outcome
- **Result:** Failed: DEC acquired by Compaq 1998; ObjectBroker discontinued; IONA Technologies Orbix, Borland VisiBroker, and then IBM WebSphere MQ became enterprise middleware leaders
- **Confidence:** verified
- **Notes:** Prediction (OBS-036) wrong for long-term: DEC/ObjectBroker never established market leadership. IONA, Borland, and IBM dominated the ORB/middleware market that emerged.

**Prediction 6:** v2.6 feature: Quick Start
- **Claimed:** 10-minute skeleton generation
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 6.1:** ObjectBroker 2.6 release and CORBA 2.0 compliance — actual outcome
- **Result:** ObjectBroker 2.6 released 1996 with CORBA 2.0 features as predicted; however DEC acquired by Compaq 1998, ObjectBroker product line discontinued; renamed Compaq ObjectBroker briefly then terminated
- **Confidence:** verified
- **Notes:** Short-term prediction (OBS-025, OBS-028) confirmed: 2.6 shipped in 1996. Long-term: product killed by acquisition. DEC/Compaq ObjectBroker history documented.

**Actual Outcome 6.2:** ObjectBroker IBM MVS mainframe support — actual outcome
- **Result:** ObjectBroker 2.6 did add MVS support as planned; however IBM's own CICS CORBA gateway and SOM/DSOM became primary IBM mainframe CORBA solutions by 1997
- **Confidence:** medium
- **Notes:** Prediction (OBS-032) confirmed in product: MVS support shipped. But IBM offered competing mainframe CORBA solutions; DEC/Compaq acquisition in 1998 ended ObjectBroker MVS track.

**Actual Outcome 6.3:** DEC ObjectBroker multi-platform ORB leadership — actual outcome
- **Result:** Failed: DEC acquired by Compaq 1998; ObjectBroker discontinued; IONA Technologies Orbix, Borland VisiBroker, and then IBM WebSphere MQ became enterprise middleware leaders
- **Confidence:** verified
- **Notes:** Prediction (OBS-036) wrong for long-term: DEC/ObjectBroker never established market leadership. IONA, Borland, and IBM dominated the ORB/middleware market that emerged.

**Prediction 7:** v2.6 feature: Better Performance
- **Claimed:** Performance improvement
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 7.1:** ObjectBroker 2.6 release and CORBA 2.0 compliance — actual outcome
- **Result:** ObjectBroker 2.6 released 1996 with CORBA 2.0 features as predicted; however DEC acquired by Compaq 1998, ObjectBroker product line discontinued; renamed Compaq ObjectBroker briefly then terminated
- **Confidence:** verified
- **Notes:** Short-term prediction (OBS-025, OBS-028) confirmed: 2.6 shipped in 1996. Long-term: product killed by acquisition. DEC/Compaq ObjectBroker history documented.

**Actual Outcome 7.2:** ObjectBroker IBM MVS mainframe support — actual outcome
- **Result:** ObjectBroker 2.6 did add MVS support as planned; however IBM's own CICS CORBA gateway and SOM/DSOM became primary IBM mainframe CORBA solutions by 1997
- **Confidence:** medium
- **Notes:** Prediction (OBS-032) confirmed in product: MVS support shipped. But IBM offered competing mainframe CORBA solutions; DEC/Compaq acquisition in 1998 ended ObjectBroker MVS track.

**Actual Outcome 7.3:** DEC ObjectBroker multi-platform ORB leadership — actual outcome
- **Result:** Failed: DEC acquired by Compaq 1998; ObjectBroker discontinued; IONA Technologies Orbix, Borland VisiBroker, and then IBM WebSphere MQ became enterprise middleware leaders
- **Confidence:** verified
- **Notes:** Prediction (OBS-036) wrong for long-term: DEC/ObjectBroker never established market leadership. IONA, Borland, and IBM dominated the ORB/middleware market that emerged.

**Prediction 8:** v2.6 new platform: IBM MVS
- **Claimed:** IBM MVS mainframe ORB support (first)
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 8.1:** ObjectBroker 2.6 release and CORBA 2.0 compliance — actual outcome
- **Result:** ObjectBroker 2.6 released 1996 with CORBA 2.0 features as predicted; however DEC acquired by Compaq 1998, ObjectBroker product line discontinued; renamed Compaq ObjectBroker briefly then terminated
- **Confidence:** verified
- **Notes:** Short-term prediction (OBS-025, OBS-028) confirmed: 2.6 shipped in 1996. Long-term: product killed by acquisition. DEC/Compaq ObjectBroker history documented.

**Actual Outcome 8.2:** ObjectBroker IBM MVS mainframe support — actual outcome
- **Result:** ObjectBroker 2.6 did add MVS support as planned; however IBM's own CICS CORBA gateway and SOM/DSOM became primary IBM mainframe CORBA solutions by 1997
- **Confidence:** medium
- **Notes:** Prediction (OBS-032) confirmed in product: MVS support shipped. But IBM offered competing mainframe CORBA solutions; DEC/Compaq acquisition in 1998 ended ObjectBroker MVS track.

**Actual Outcome 8.3:** DEC ObjectBroker multi-platform ORB leadership — actual outcome
- **Result:** Failed: DEC acquired by Compaq 1998; ObjectBroker discontinued; IONA Technologies Orbix, Borland VisiBroker, and then IBM WebSphere MQ became enterprise middleware leaders
- **Confidence:** verified
- **Notes:** Prediction (OBS-036) wrong for long-term: DEC/ObjectBroker never established market leadership. IONA, Borland, and IBM dominated the ORB/middleware market that emerged.

**Prediction 9:** v2.6 new platform: OS/400
- **Claimed:** IBM AS/400 OS/400
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 9.1:** ObjectBroker 2.6 release and CORBA 2.0 compliance — actual outcome
- **Result:** ObjectBroker 2.6 released 1996 with CORBA 2.0 features as predicted; however DEC acquired by Compaq 1998, ObjectBroker product line discontinued; renamed Compaq ObjectBroker briefly then terminated
- **Confidence:** verified
- **Notes:** Short-term prediction (OBS-025, OBS-028) confirmed: 2.6 shipped in 1996. Long-term: product killed by acquisition. DEC/Compaq ObjectBroker history documented.

**Actual Outcome 9.2:** ObjectBroker IBM MVS mainframe support — actual outcome
- **Result:** ObjectBroker 2.6 did add MVS support as planned; however IBM's own CICS CORBA gateway and SOM/DSOM became primary IBM mainframe CORBA solutions by 1997
- **Confidence:** medium
- **Notes:** Prediction (OBS-032) confirmed in product: MVS support shipped. But IBM offered competing mainframe CORBA solutions; DEC/Compaq acquisition in 1998 ended ObjectBroker MVS track.

**Actual Outcome 9.3:** DEC ObjectBroker multi-platform ORB leadership — actual outcome
- **Result:** Failed: DEC acquired by Compaq 1998; ObjectBroker discontinued; IONA Technologies Orbix, Borland VisiBroker, and then IBM WebSphere MQ became enterprise middleware leaders
- **Confidence:** verified
- **Notes:** Prediction (OBS-036) wrong for long-term: DEC/ObjectBroker never established market leadership. IONA, Borland, and IBM dominated the ORB/middleware market that emerged.

**Prediction 10:** v2.6 new platform: Windows 95
- **Claimed:** Microsoft Windows 95
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 10.1:** ObjectBroker 2.6 release and CORBA 2.0 compliance — actual outcome
- **Result:** ObjectBroker 2.6 released 1996 with CORBA 2.0 features as predicted; however DEC acquired by Compaq 1998, ObjectBroker product line discontinued; renamed Compaq ObjectBroker briefly then terminated
- **Confidence:** verified
- **Notes:** Short-term prediction (OBS-025, OBS-028) confirmed: 2.6 shipped in 1996. Long-term: product killed by acquisition. DEC/Compaq ObjectBroker history documented.

**Actual Outcome 10.2:** ObjectBroker IBM MVS mainframe support — actual outcome
- **Result:** ObjectBroker 2.6 did add MVS support as planned; however IBM's own CICS CORBA gateway and SOM/DSOM became primary IBM mainframe CORBA solutions by 1997
- **Confidence:** medium
- **Notes:** Prediction (OBS-032) confirmed in product: MVS support shipped. But IBM offered competing mainframe CORBA solutions; DEC/Compaq acquisition in 1998 ended ObjectBroker MVS track.

**Actual Outcome 10.3:** DEC ObjectBroker multi-platform ORB leadership — actual outcome
- **Result:** Failed: DEC acquired by Compaq 1998; ObjectBroker discontinued; IONA Technologies Orbix, Borland VisiBroker, and then IBM WebSphere MQ became enterprise middleware leaders
- **Confidence:** verified
- **Notes:** Prediction (OBS-036) wrong for long-term: DEC/ObjectBroker never established market leadership. IONA, Borland, and IBM dominated the ORB/middleware market that emerged.

**Prediction 11:** v2.6 new platform: Silicon Graphics IRIX
- **Claimed:** SGI IRIX via Logica
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 11.1:** ObjectBroker 2.6 release and CORBA 2.0 compliance — actual outcome
- **Result:** ObjectBroker 2.6 released 1996 with CORBA 2.0 features as predicted; however DEC acquired by Compaq 1998, ObjectBroker product line discontinued; renamed Compaq ObjectBroker briefly then terminated
- **Confidence:** verified
- **Notes:** Short-term prediction (OBS-025, OBS-028) confirmed: 2.6 shipped in 1996. Long-term: product killed by acquisition. DEC/Compaq ObjectBroker history documented.

**Actual Outcome 11.2:** ObjectBroker IBM MVS mainframe support — actual outcome
- **Result:** ObjectBroker 2.6 did add MVS support as planned; however IBM's own CICS CORBA gateway and SOM/DSOM became primary IBM mainframe CORBA solutions by 1997
- **Confidence:** medium
- **Notes:** Prediction (OBS-032) confirmed in product: MVS support shipped. But IBM offered competing mainframe CORBA solutions; DEC/Compaq acquisition in 1998 ended ObjectBroker MVS track.

**Actual Outcome 11.3:** DEC ObjectBroker multi-platform ORB leadership — actual outcome
- **Result:** Failed: DEC acquired by Compaq 1998; ObjectBroker discontinued; IONA Technologies Orbix, Borland VisiBroker, and then IBM WebSphere MQ became enterprise middleware leaders
- **Confidence:** verified
- **Notes:** Prediction (OBS-036) wrong for long-term: DEC/ObjectBroker never established market leadership. IONA, Borland, and IBM dominated the ORB/middleware market that emerged.

### Entities Referenced (11 entities)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Digital Equipment Corporation | vendor |  |  |
| Object Management Group | standards-body |  |  |
| Microsoft Corporation | vendor |  |  |
| Logica North America Inc | si-partner |  |  |
| Electronic Data Systems | si-partner |  |  |
| Protosoft Inc | vendor |  |  |
| Tandem Computers | vendor |  |  |
| Aberdeen Group | research-firm |  |  |
| The Cushing Group | si-partner |  |  |
| NetLinks Technology | si-partner |  |  |
| Linkvest | si-partner |  |  |

### Technologies Referenced (19 technologies)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Object Request Broker (ORB) |  |  |  |  |
| Digital ObjectBroker |  |  |  |  |
| CORBA (Common Object Request Broker Architecture) |  |  |  |  |
| Interface Definition Language (IDL) |  |  |  |  |
| Implementation Mapping Language (IML) |  |  |  |  |
| Method Mapping Language (MML) |  |  |  |  |
| OLE (Object Linking and Embedding) |  |  |  |  |
| COM (Component Object Model) |  |  |  |  |
| DDE (Dynamic Data Exchange) |  |  |  |  |
| DCE (Distributed Computing Environment) |  |  |  |  |
| Visual Basic |  |  |  |  |
| PowerBuilder |  |  |  |  |
| OpenVMS |  |  |  |  |
| C++ Language Binding |  |  |  |  |
| GSS-API (Generic Security Services API) |  |  |  |  |
| ACA Services |  |  |  |  |
| ObjectPlus |  |  |  |  |
| Paradigm Plus |  |  |  |  |
| NAS (Network Application Support) |  |  |  |  |

### Observation Summary

- Total observations: 55
- By type:
  - actual-outcome: 5
  - expert-opinion: 11
  - market-data: 8
  - technology-assessment: 20
  - viability-prediction: 11
