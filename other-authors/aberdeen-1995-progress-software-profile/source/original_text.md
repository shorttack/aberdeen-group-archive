# Progress Version 8.0 Development Environment: The Importance Of Experience-Driven Scalability and Flexibility

> Archived from: https://web.archive.org/web/19970112012234/http://www.aberdeen.com:80/secure/profiles/progress/progress.htm
> Original publication date: 1995-12-01
> Author: Aberdeen Group

---

## Original Document Text

Progress Software Corp.
14 Oak Park
Bedford, MA 01730
(617) 280-4000
Progress Version 8.0 Development Environment
The Importance Of Experience-Driven Scalability and Flexibility
As more and more users perceive the limitations of ﬁrst-generation client-server application development environments (CADEs), IS buyers are turning to new, more highly scalable and
ﬂexible toolsets. Aberdeen ﬁnds that key considerations for IS buyers in assessing the new toolsets include not only their scalability in data-intensive applications and their ﬂexibility in
accessing multiple suppliers' databases and server platforms, but also their ability to leverage past experience and "sweat the details" of client-server programming. Thus, to be useful in the
long term, the CADE should provide comprehensive software-lifecycle support, include today's effective programmer-productivity techniques, give the developer constantly-improving
building-block libraries of components on which to construct ever more sophisticated applications, and provide value-added in such areas as foreign-language translation and migration from
ﬁrst-generation and legacy toolsets.
This Proﬁle describes the Progress Version 8.0 CADE, a client-server development toolset that drives effective development features deep into the details. Version 8.0 adds such features as a
development framework, powerful SMARTOBJECTÔ components, and integration with Microsoft's VBXs. Version 8.0 allows developers to use object-oriented technology effectively
without dealing with the complexities of object-oriented 3GL programming.
Executive Summary
The Progress CADE is a ﬁne example of a scalable, ﬂexible, database-independent development toolset with a relatively broad set of capabilities. Progress supports both the new
programmer-productive GUI-development Visual Programming Environments (VPEs) and older character-based applications, is concerned with deployment and maintenance as well as
coding and testing, provides broad international-ization capabilities, and is able to interoperate on a wide variety of platforms with major popular databases using industry-standard
communications protocols. These technical advantages translate into greater programmer productivity, a clearer migration path from legacy code, reduction of major software maintenance
and distribution costs, support for desktop and mission-critical transaction/batch processing and reengineered knowledge workers' access to data across departments, and overall support for
the trends towards client-server applications, rightsizing, and decentralizing.
Progress' client-server application development environment consists of two parts: the Progress Application Development Environment (ADE) and Progress DataServer Architecture. The
Progress ADE includes a powerful 4GL (Progress 4GL), an application-generation and screen-building facility (User Interface Builder), a repository (Progress Data Dictionary), coding and
testing facilities (Procedure Editor, Application Debugger, and Performance Proﬁlers), program deployment and maintenance tools (Progress On-Line Help, Progress Translation Manager for
foreign-language support, Progress Toolkit for program distribution, install, and upgrade, and Progress Database Administrator), querying/reporting facilities (Report Builder and Progress
RESULTS), and connections to third-party upper-CASE analysis and design tools. The Progress DataServer Architecture is a set of services that allows a Progress-ADE application to access
and update its own and other major suppliers' databases.
Progress version 8.0 adds an Application Component Environment (a framework that supports more rapid development at a higher level of abstraction by aiding the developer in creating and
assembling "template" components into ﬁnished applications), SMARTOBJECTs ("data-aware" reusable business objects that include database operations such as events), VBX (Visual
Basic Extension) integration, Microsoft OLE 2.0 support, a team-development tool (Enterprise ProVision) plus hooks for third-party team-development product integration, and Windows 95
support. Progress version 8.0 allows users to employ a new model of application development in which "fabricators" create new SMARTOBJECT templates and "assemblers" combine the
SMARTOBJECTs to create a ﬁnished application-in effect providing an "object workbench".
Progress version 8.0 with SMARTOBJECTs builds on Progress' past strengths: attractiveness to developers, links to other RDBMSs, availability on AS/400 and PC-LAN platforms, low
price, integration, and strength in VAR channels. Developers give its tools high marks for portability and internationalization.
The bottom line for the IS buyer is that Progress is delivering a client-server application development environment that expands the strengths of its past offerings in departmental, divisional,
and enterprise-scale client-server-application development, offering exceptional scalability, openness, portability, internationalization, and programmer productivity.
Market Position
Progress focuses mainly on enterprise application development, but provides solutions throughout the desktop, PC LAN, workstation, and midrange markets, including Unix, OpenVMS, a
Novell NetWare NLM, and IBM's OS/400. Progress' RDBMS is available on a wide range of low-end and midrange client and server operating systems and network operating systems,
including Unix, Windows NT,OS/2, DOS, Windows, LAN Manager/LAN Server, Digital's Pathworks, and Novell's NetWare. Communications protocols include DECnet, TCP/IP, SPX/IPX,
Netbios, and LU6.2.
Progress version 8.0 is ﬁrst available on the Microsoft-Windows and Windows NT GUI clients, and later available on other major platforms, including DOS, Windows 95, SCO Unix, HP-
UX, IBM AIX, Digital Unix, and Sun. Special high-performance DataServers access the Oracle, Sybase, Microsoft SQL Server, and DB2 RDBMSs. Using the DataServer Architecture,
developers can also access Oracle's Rdb and Digital's RMS, Informix C-ISAM, and all ODBC-client-supporting databases.
Within each market, Progress has positioned itself as a cost-effective provider. It achieves its price edge by distributing its products primarily through VARs. Progress' VARs are its software
partners. They supplement Progress' toolkit with a wide array of user-friendly tools and applications.
Progress distinguishes itself in client-server application development markets by user satisfaction, low price, large-scale DBMS-based application-development tools, providing turnkey
applications via Progress' Application Partners (VARs), and a wide array of platforms supported. Progress consistently receives high satisfaction ratings from users, e.g., in VARBusiness
Magazine, especially for its application-development tools. Progress' Progress/400 product is especially signiﬁcant, since it offers RDBMS-supplier tools for building client-server
applications for the native AS/400 database.

---

The Major Technologies of Progress Version 8.0
The key "orthogonal" ideas and technologies behind Progress Version 8.0 are:
scalability,
software-lifecycle support,
integration,
openness (portability and interoperability),
support for legacy applications,
programmer productivity (RAD), and
internationalization.
These ideas are not unusual in the client-server application development environment market. It is Progress' way of driving these ideas down to the details of its client-server application
development environment that distinguishes Progress Version 8.0 from other client-server application development environments.
Source: AberdeenGroup, December 1995
Scalability
Aberdeen ﬁnds that users are typically concerned about two major aspects of scalability: performance scalability, or maintaining the performance of client-server applications as the number
of users or the size of the server database increases, and development-process scalability, or the ability to coordinate single- or double-digit numbers of programmers for complex
applications. In both of these areas, version 8.0 of Progress takes signiﬁcant steps forward that give Progress an edge for complex client-server applications.
Performance Scalability. Progress' DataServer Architecture provides both "native" drivers that produce high-performance database access compared to ODBC, and relatively long experience
in these drivers that gives it further performance enhancements. For example, Version 8.0 of Progress adds such proven techniques for data-access performance as prefetching and further
tuning of Progress' query optimization techniques. Since data-access performance is a key factor both in scaling data-intensive applications and in effectively leveraging the new
performance-scalability technologies of today's major RDBMSs, effective use of DataServers can allow users to scale complex data-intensive applications exceptionally well.
Development-Process Scalability. Version 8.0 of Progress adds a team-programming toolset-Progress's Enterprise ProVision plus Starbase's Roundtable TSMS-that builds on a central
development repository to deliver such features as checkin-checkout, version control (including tracking versions after production), project management, and incremental builds and
deployment. Progress integrates Roundtable closely with the rest of the Progress CADE, thus ensuring that such operations as component reuse can leverage the efforts of other programmers
quickly and safely. Overall, the new team-programming features give Progress strong development-process scalability features that can drive multideveloper projects for creating complex,
mission-critical, and data-intensive client-server solutions.
Lifecycle Technologies
Many client-server application development environment suppliers recognize the importance of supporting the entire software-lifecycle, and the increasing importance of software
deployment and maintenance to a corporation's costs and overall agility. Few have implemented client-server application development environment software that provides specialized support
for software deployment and maintenance, and most do not closely integrate such features as version control into their toolsets. Progress extends full-lifecycle support to reverse engineering,
internationalization, on-line help, and application-oriented database administration.
Typically, the major stages in software's "life" are:
design,
development,
deployment (distribution) of new applications and upgrades to end users, and
maintenance or evolution of applications in use.
Design. Progress' client-server application development environment offers connections that allow developers to pass third-party upper-CASE analysis and design information to its
development tools, and the reverse (i.e., it allows reverse engineering). The Open Access facilities allow information exchange with many upper-CASE suppliers, including Popkin,
LogicWorks, CSA, Evergreen, and S-Designor. The Progress data dictionary is also a repository for all default design information.
Develop. The Progress client-server application development environment's primary method for creating and generating programs is the User Interface Builder (UIB). The UIB offers a drag-
and-drop way of creating screens, and pick-from-a-list speciﬁcation of data linked to a screen. The UIB's main unique feature is "visualization", the ability to attach a graphical object such as
a button to a ﬁeld and store the combination as a template or default. This speeds up the creation of data-linked applications. The UIB includes form defaults.
At the core of the UIB are the Progress SMARTOBJECTs, which can be assembled together and linked to datasources in a visual drag-and-drop manner. These provide the building blocks
and outlines of GUI-based objects. Thus, SMARTOBJECTs can increase reusability, speed development, and improve look-and-feel consistency across applications. Moreover, the Progress

---

CADE allows developers to design and register their own SMARTOBJECTs in the system for all developers to share.
The UIB also includes a Section Editor. This allows a developer to stitch together window code into a complex application, by deﬁning the interfaces between each window/module and the
others. Furthermore, the UIB includes a Trigger Editor to list and deﬁne all the events and triggers for a window. Thus, the UIB (and Progress 4GL) can support event-driven programming.
The UIB generates Progress 4GL code. For developing Progress-4GL programs, the Progress client-server application development environment includes a Procedure Editor that allows
developers to interrupt editing to debug or compile, and can cut-and-paste directly from the Progress-Data-Dictionary repository into the program. The Progress 4GL itself has been enhanced
to support event-driven programming.
The Application Debugger supports breakpoints and single-step source-code debugging. Notably, it also supports event tracing, and can be customized by developers via macros and custom
toolbars. An Application Performance Proﬁler and Database Performance Proﬁler collect statistics to help developers to tune Progress-4GL applications and Progress databases.
Deploy. Progress On-Line Help allows programmers to incorporate on-line help into a program from a word processor. Progress On-Line Help supports hypertext, text annotation, and help-
text portability.
The Progress Toolkit supports packaging and deploying applications. It includes the ability to freeze a database schema, to deliver minor upgrades of data and application components, and to
customize applications for users with startup and batch facilities. Enterprise ProVision adds such features as integrated version control.
Maintain. The Progress Database Administrator is included in the Progress ADE. It allows administrators to load data and metadata, exchange metadata with non-Progress servers, implement
security, and import and export from spreadsheets and text and graphics databases. Progress' development tools can also use the Performance Proﬁler for performance monitoring, and the
Progress RDBMS' facilities for backup and restore, recovery, audit trails, and accounting.
Change-impact analysis in Roundtable allows Enterprise ProVision users to assess the impact of any source or schema change before it is made. Thus, users can predict the engineering,
quality-assurance, and documentation costs of a maintenance effort.
Integration Within The Development Environment
Progress's client-server application development environment provides integration of the development environment through its use of Progress 4GL as underlying code, through its
repository, and through the ability to pass easily from UIB to Procedure Editor to Application Debugger. To the programmer, the Progress ADE appears to be a single integrated product,
hiding the details of switching from task to task by its consistent GUI, or GUI-like character-mode, interface and its ability to preserve the state of development in one module while the
programmer detours to another module. As noted above, Progress SMARTOBJECTs provide further look-and-feel consistency and reusability, increasing the environment's overall
integration.
Many client-server application development environments are conglomerations of tools that originally were separate and intended for different uses. By using the Progress 4GL and the
RDBMS's data dictionary as the core of every module, Progress gives all components of its client-server application development environment a common core that saves developer training
and learning costs and allows immediate leverage of one module's added features throughout the whole client-server application development environment. Pro*Tools and the ADE API
allow users to integrate their own and third-party tools into the ADE easily.
Open Technologies
The Progress 4GL and RDBMS have both been known for their ability to operate on multiple platforms and operating systems, access multiple suppliers' data-management systems and
databases, and use multiple communications protocols. Progress Version 8.0 provides these capabilities throughout its client-server application development environment.
Interoperability. Progress offers access via high-performance DataServer components to Oracle, Sybase, Microsoft, and IBM DB2 RDBMSs. The DataServer Architecture also includes other
DataServers allowing connections to Oracle Rdb, Digital RMS, and Informix C-ISAM. The DataServer for ODBC allows connections to a wide range of other ODBC-compliant data
managers.
The DataServer Architecture resides on the client desktop, increasing overall client-server performance by removing gateways' data-translation and communications loads from the server.
Progress allows transparent application-client access to multiple protocols, including APIs for access to TCP/IP, Netbios, DECnet, and SPX/IPX. The DataServer Architecture adds support
for LU6.2. Progress version 8.0 adds openness to third-party suppliers via Pro*Tools and and new published APIs.
Portability. Progress's client-server application development environment allows development of applications porting exceptionally easily across multiple servers and across PCs and Unix
workstations. Progress 4GL source code is portable, as is the P-code runtime code produced by the Progress compiler.
The Progress client-server application development environment supports full translation between Windows and Motif applications, as well as portability of on-line help and foreign-
language translations. The Progress client-server application development environment also supports translation between GUI and character-mode user interfaces without code change.
Programmer-Productivity Technologies
The major development-environment technologies that have proven their worth in increasing programmer productivity in many situations are:
4GLs,
Upper-CASE tools,
Visual Programming Environments (VPEs), and
Object-Oriented Programming (OOP) techniques.
Progress has long experience and a well-regarded product in Progress 4GL. Progress' UIB is a full-ﬂedged VPE with its own unique features.
4GLs. Progress 4GL supports event-driven programming. Progress 4GL constructs allow record- or set-level data manipulation, record locking, text retrieval, ANSI SQL, user-deﬁned
functions, reusable procedures and templates, and default forms, including "report" forms.
A particularly noteworthy feature of Progress 4GL and the Progress CADE is the ability to program batch processing as well as transaction processing. This is particularly effective for
automating administration of complex applications and load balancing in high-throughput situations.
Upper CASE Tools. Progress's Open Access program provides links to upper-CASE tools from LBMS, ERwin, Popkin, Chen, CSA, and many others.
VPEs. The UIB offers a drag-and-drop way of creating Windows and Motif screens, including speciﬁcation of data-screen links. The UIB's main unique feature is "visualization", the ability
to attach a graphical object such as a button to a ﬁeld and store the combination as a template or default. This speeds up the creation of data-based applications. The UIB includes form
defaults.
The UIB also includes a Section Editor and SMARTOBJECTs. This allows a developer to stitch together windowing components into a complex application, by deﬁning the interfaces
between each window/module and the others. Furthermore, the UIB includes a Trigger Editor to list and deﬁne all the events and triggers for a window. Thus, the UIB (and Progress 4GL)
can support event-driven programming.

---

The UIB stresses conformance to Windows standards, including such details as OLE2, VBX, Browser and Combo-box, Print dialog, and 3-D look-and-feel support. Moreover, developers
can customize the UIB Toolbox for particular applications or development styles.
The Progress Report Builder is a VPE that can be used by developers or power users to create reports, report programs, or report templates. Thus, Report Builder extends the Progress client-
server application development environment's scope beyond professional programmers to the backlog of end users needing quick "one-off" reports. Progress Version 8.0 also offers
RESULTS, either standalone or integrated with Progress, allowing forms generation, querying, and master-detail reporting for application users.
OOP. Progress Version 8.0 delivers the core ideas of OOP: object classes, encapsulation, and inheritance. Progress Version 8.0 allows developers to create Application Objects, UIB
templates, classes of GUI-component objects that can be applied in multiple screens across many applications and can be assembled together into complex applications rapidly. Progress
Version 8.0 allows developers to convert legacy code into objects by "wrapping" (encapsulating) them as persistent procedures. A UIB multi-layout capability enables developers to use
(inherit) the same code in multiple user interface source code modules. The overall effect of this object-oriented technology is to increase code reusability and GUI-application development
speed, and therefore programmer productivity, substantially.
Version 8.0 increases Progress's capabilities substantially with the addition of SMARTOBJECTs. These are customized and customizable components-e.g., SmartFolder, SmartBrowse,
SmartViewer, SmartPanel, SmartQuery, SmartWindow, and SmartDialog-that include features well beyond the average object: business events, user-interface features, "data-aware" features
that incorporate common data-management operations, and "active templates" that lead the user through the steps of customization via wizards and "cue cards".
SMARTOBJECTs operate within a "framework"-the Application Component Environment, or A.C.E.-that allows the developer to invoke the Progress 4GL and Visual Tools to combine and
reuse components, other Progress objects, and third-party objects. The A.C.E. also provides such value added as procedure objects and polymorphism, as well as deﬁning how components
and objects can be combined through "application links" (SmartLinks). Together with SMARTOBJECTs, the A.C.E. makes it easier to reuse code and objects, improves programmer
productivity and program quality by allowing programmers to operate at a higher level (with Progress taking care of the details), and incorporates high-performance data-access code that can
improve performance scalability in data-intensive applications.
Support For Legacy Applications
Progress Version 8.0 provides support for legacy applications in two ways: its integration of its traditional character-based-application support with its Windows and Motif GUI support, and
its deﬁnition of a clear migration path from legacy to client-server.
The Progress client-server application development environment's interfaces can be either GUI or terminal-both provide the same functions and features. An application can be coded once
for both types of interface, can be ported easily from one type to the other, and can support both GUI-desktop and terminal clients simultaneously. Based on this dual support, Progress allows
straightforward migration from legacy applications or earlier Progress versions. For example, migration from earlier versions of the Progress CADE to version 8.0 involves a straightforward
application recompilation.
Internationalization
Translation Manager 2.0 and the new Visual Translator provide an exceptional degree of internationalization support that allows a nonprogrammer to customize an application for various
foreign languages. Progress takes foreign-language versioning a step further, by providing extensive built-in character sets and collating sequences, and by allowing translation -switching at
runtime, thus allowing American visitors to a German site to view the same application in English. Version 8.0 adds to the Translation Manager "visual in-context translation" incorporating
Microsoft's language dictionaries and translation-project management features, as well as delivering localized versions of its report builders. As a result, Version 8.0 gives users the ability to
create internationalized applications via a "project coordinator" who uses Translation Manager to deﬁne the internationalization basics (e.g., source code, ﬁlters, and glossaries) and deploys
the ﬁnal product, and a "translator" who uses Visual Translator and the project coordinator's work to perform the translation and update the glossary.
Progress Version 8.0 provides double-byte character enablement (DBE), enabling support of Japanese, Korean, simpliﬁed and traditional Chinese languages, and other Asian languages.
Moreover, Version 8.0 drives DBE "down into the details", providing features such as support for four different Windows versions, GUI-based data input, and protections against data
corruption and incorrect data-table search results. Aberdeen believes that as a result of these improvements, Progress Version 8.0 is taking a leadership role in extending the breadth and depth
of CADEs' internationalization support.
Vision Statement/Marketing Strategies
Progress aims to provide application development and deployment software to support professional IS organizations building "enterprise client/server" solutions worldwide. In particular, the
Progress CADE focuses on enabling development and deployment of "complex, enterprise applications that are scalable, portable, and reconﬁgurable across heterogeneous client/server and
host environments". Progress version 8.0 emphasizes "capabilities that further enable corporate IS and ISV developers to effectively buy, build, and customize component-based
applications", looking toward future application-delivery models in which IS organizations "purchase best-of-breed components, customize as required, develop company-speciﬁc
components, assemble those components, and distribute them in a multi-tiered computing environment".
Progress has a strong presence in the PC LAN, Unix-workstation, proprietary-operating-system, and Unix-midrange-server markets. It has a stronger focus than most other RDBMS suppliers
on the desktop and the PC LAN. Progress' VARs provide a wide array of business-solution applications, as well as greater functionality.
Financials
Progress had ﬁscal-1994 revenues of $139 million, a 25 % rise over 1993. Revenues over the ﬁrst 9 months of ﬁscal 1995 increased by 28 % over the ﬁrst 9 months of 1994. Net income in
3Q95 was $4.3 million, a 38 % increase over 3Q94.
Conclusions
Progress Version 8.0 delivers a complete client-server application development environment that drives the core ideas of scalability, integration, openness, programmer-productivity
enhancement, software-lifecycle support, and support for legacy applications deep into the details of programming. IS buyers should expect to reap beneﬁts from this approach in migrating
to client-server computing, rightsizing, and decentralizing IS.
The new Progress client-server application development environment builds on Progress' past portability, internationalizability, availability on Digital, Unix, AS/400 and PC-LAN platforms,
low price, strong client-server RDBMS, and strength in VAR channels.
The details of Progress' approach include taking advantage of the new programmer-productive GUI-development Visual Programming Environments (VPEs) while supporting older
character-based applications, supporting deployment and maintenance as well as coding and testing, integrating the client-server application development environment with Progress'
powerful client-server RDBMS, providing reusability via powerful object-oriented technology, and delivering portability and interoperability across a wide range of suppliers, platforms,
databases, and communications protocols. Version 8.0 of the Progress CADE adds strong performance and development-process scalability features such as the Enterprise ProVision team
programming toolset, programmer-productivity enhancements via the A.C.E. framework and SMARTOBJECTs, and further enhancements to past strengths such as internationalization and
the DataServers. These technical details should deliver greater scalability and programmer productivity, reduction of major software maintenance and distribution costs, support for desktop
mission-critical transaction processing, and increased knowledge-worker access to farﬂung data. Moreover, Progress can deﬁne a clear, step-by-step migration path from its legacy
host/terminal applications to client-server ones.
The bottom line for IS buyers is that it is deﬁnitely worth taking a look at Progress' application-development capabilities. The beneﬁts of Progress' approach, in the details and overall
integration as much as in each module's functions, are likely to increase as the new IS strategies drive deeper into the corporation.

---

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
Copyright © 1995 Aberdeen Group, Inc., Boston, Massachussetts

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|---|---|
| study_id | aberdeen-1995-progress-software-profile |
| title | Progress Version 8.0 Development Environment: The Importance Of Experience-Driven Scalability and Flexibility |
| author | Aberdeen Group |
| date | 1995-12-01 |
| type | product-profile |
| subject_domain | client-server application development environments |
| methodology | vendor-briefing,product-evaluation,user-interviews |
| source_file | 1995 Progress Software Profile pr.pdf |
| abstract | Aberdeen evaluates Progress Software's Version 8.0 client-server application development environment (CADE), finding it  |
| license | CC-BY-4.0 |
| importance | medium |
| importance_rationale | Progress 8.0 represented a substantive client-server toolset in a competitive 1995 market. Its DataServer architecture a |
| relevance | medium |
| relevance_rationale | The study documents a specific product generation in the CADE market segment, offering concrete evidence of 1995 client- |
| prescience | medium |
| prescience_rationale | Aberdeen's emphasis on database independence and scalability proved directionally correct, though Progress's market shar |

### Abstract

Aberdeen evaluates Progress Software's Version 8.0 client-server application development environment (CADE), finding it a scalable, flexible, database-independent toolset. The study examines Progress's SMARTOBJECT components, VPE tools, 4GL language, DataServer architecture, and object-oriented capabilities, concluding Progress 8.0 addresses key IS requirements for complex data-intensive applications through experience-driven engineering.

### Document Assessment

| Dimension | Rating | Rationale |
|---|---|---|
| Importance | medium | Progress 8.0 represented a substantive client-server toolset in a competitive 1995 market. Its DataServer architecture and SMARTOBJECT approach addressed real scalability problems documented by IS buyers. |
| Relevance | medium | The study documents a specific product generation in the CADE market segment, offering concrete evidence of 1995 client-server tooling capabilities and buyer criteria. Progress Software remains active today as OpenEdge. |
| Prescience | medium | Aberdeen's emphasis on database independence and scalability proved directionally correct, though Progress's market share in app-dev tools eroded as Java and later web frameworks dominated. Progress survived by pivoting to infrastructure software. |

### Prescience Detail

**Prediction (aberdeen-1995-progress-software-profile-OBS-007):** scalable toolsets will displace first-generation CADEs
- Year predicted: 1995
- Confidence: high
- Notes: Aberdeen predicts IS buyers will adopt new scalable toolsets over first-gen CADEs

**Prediction (aberdeen-1995-progress-software-profile-OBS-008):** component-based development will improve productivity for complex applications
- Year predicted: 1995
- Confidence: medium
- Notes: Aberdeen implies SMARTOBJECT-style component reuse will be key competitive differentiator

**Prediction (aberdeen-1995-progress-software-profile-OBS-009):** full software lifecycle support is required for long-term CADE viability
- Year predicted: 1995
- Confidence: high
- Notes: Aberdeen recommends CADE must provide comprehensive software-lifecycle support to remain useful long-term

**Prediction (aberdeen-1995-progress-software-profile-OBS-024):** multi-vendor RDBMS support via DataServer is long-term competitive advantage
- Year predicted: 1995
- Confidence: medium
- Notes: Aberdeen implies database independence is differentiating for large enterprises with mixed DB environments

**Actual Outcomes:**

- **aberdeen-1995-progress-software-profile-OBS-010** (Year 2010): survived as OpenEdge; pivoted to infrastructure software
- **aberdeen-1995-progress-software-profile-OBS-011** (Year 2000): category collapsed; displaced by Java, .NET, and later web frameworks
- **aberdeen-1995-progress-software-profile-OBS-012** (Year 1997): obsolete; replaced by OCX/ActiveX/COM in 1996
- **aberdeen-1995-progress-software-profile-OBS-013** (Year 2010): acquired by SAP for $5.8B in 2010
- **aberdeen-1995-progress-software-profile-OBS-025** (Year 2024): $753 million USD

### Entities Referenced (5)

| entity_id | entity_name | status | successor |
|---|---|---|---|
| ENT-PROGRESS | Progress Software Corporation | active | — |
| ENT-MICROSOFT | Microsoft Corporation | active | — |
| ENT-ORACLE-DB | Oracle Corporation | active | — |
| ENT-SYBASE | Sybase Inc. | acquired | SAP SE (acquired 2010) |
| ENT-INFMX | Informix Corporation | acquired | IBM (database assets acquired 2001) |

### Technologies Referenced (6)

| tech_id | tech_name | lifecycle_at_study | lifecycle_current |
|---|---|---|---|
| TECH-PROGRESS-4GL | Progress 4GL | growth | legacy |
| TECH-SMARTOBJECT | SMARTOBJECT Components | emerging | obsolete |
| TECH-VBX | Microsoft VBX (Visual Basic Extensions) | mainstream | obsolete |
| TECH-ODBC | ODBC (Open Database Connectivity) | mainstream | legacy-active |
| TECH-CADE | Client-Server Application Development Environment (CADE) | mainstream | obsolete |
| TECH-RAD | Rapid Application Development (RAD) | mainstream | evolved |

### Observation Summary

| Observation Type | Count |
|---|---|
| actual-outcome | 5 |
| expert-opinion | 2 |
| market-data | 2 |
| strategy-classification | 2 |
| technology-assessment | 10 |
| viability-prediction | 4 |
| **Total** | **25** |
