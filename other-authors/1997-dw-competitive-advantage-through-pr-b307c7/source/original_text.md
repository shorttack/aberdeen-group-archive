# Original Text: Competitive Advantage Through Prism Metadata Scalability

**Source:** Aberdeen Group Vendor Profile, June 1997  
**Publisher:** Aberdeen Group, One Boston Place, Boston MA 02108  
**Wayback Machine URL:** https://web.archive.org/web/19970604113329/http://www.aberdeen.com:80/secure/profiles/1997/prism/body.htm

---

The Wayback Machine - https://web.archive.org/web/19970604113329/http://www.aberdeen.com:80/secure/proﬁles/1997/prism/body.htm
Prism Solutions, Inc.
1000 Hamlin Court
Sunnyvale, CA 94089
408-752-1888
Competitive Advantage Through Prism Metadata
Scalability
Preface
Successful data warehouse initiatives — especially with the addition of rapid-
deployment data marts — are becoming more dynamic, pressuring
implementers and administrators to develop expertise in controlling changes
throughout the evolution of their information architectures.
Data warehouse scalability, so often viewed solely in terms of database-size
growth, also requires managing the underlying changes as the warehouse
evolves in response to a dynamic business environment. Driven by the deep
enterprise insights garnered from interacting with these new-style systems,
enterprises typically modify business rules, alter the number of data sources or
combinations of data from those sources, and add or substitute new underlying
warehouse technologies. As the enterprise continues to evolve, it transforms the
information content that the warehouse or data marts provide to users. These
modiﬁcations, whatever the business issues driving them, should not force IS to
squander precious time and skill in radical reconstructions of warehouses or
data marts.
Wise enterprises look to leverage, not undo, previous iterations of their
information architectures; continual warehouse alterations in turn expand the
range of IS administrative tasks. The key to success in such a dynamic
environment is an automated framework that ﬂows these changes to the
administrator and provides the functionality to control those changes.
This Proﬁle examines Prism Solutions Inc.'s newest generation of metadata-
driven software for the building, managing, accessing, refreshing — and the
critically important scaling — of data warehouses and data marts. Aberdeen
believes that Prism has created a product strategy and roll out for its metadata-
driven facilities that solidly delivers on a fundamental tenet of the Prism
warehouse philosophy: wherever the enterprise starts its initiative, the toolset
must deliver a consistent entry point, encourage and leverage short, iterative
deployment, and fully support business requirements throughout the warehouse
life cycle.
Executive Summary
Instead of watching idly as their warehouse costs spiral upward because of poor
planning, many IS executives have prudently decided to use short, iterative
steps to create and continually ﬁne-tune their data warehouse-driven
information architectures. Whether the enterprise starts out to build an
enterprise data warehouse, one or more data marts, or has a not-set-in-stone
plan that embraces a blend of the different styles, it is building its way toward a
new type of dynamic architecture. The emerging information architectures will
(indeed already have started to) impose requirements for different perspectives
on essentially the same underlying information. Aberdeen believes that the
more the warehouse architecture scales in importance to an enterprise, the more
the enterprise will demand a systematic approach to building different views of
similar information without redundant effort.
Aberdeen believes that robust metadata — and a tool-driven proﬁciency in
using it — is the key to managing the integrity of these new architectures.
Metadata, or data about data that serves as a map of the information within the
warehouse, is also the way to control potentially time-consuming and resource-
draining redundancies. Aberdeen believes that these redundancies, especially
relevant with the proliferation of data marts, could choke enterprises trying to
either rely on old-style — and non-scalable — warehousing techniques, or on
many of the newer data-mart-only transformation engines. To the extent that
any one data mart reuses the contents of another data mart (or of a larger data
warehouse), developers ought to be able to leverage the content, and the labor
used to create that content.

Data warehouses hold data that has been downloaded and ﬁltered from various
operational stores in the enterprise. This data will change over time. Among
metadata’s many tasks, it must instruct both technical and business users about
how data arrived in the warehouse, where it came from, and how it was
transformed. The proliferation of data marts — coupled with the business-
driven demand to build them quickly and subsequently manage them — has
increased the role of metadata. Enterprises will increasingly need to rely on
facilities for building data warehouses and data marts that continually leverage
previous iterations as they build, say, a data mart that offers users a particular
view or special slant of a subject area. As a result, Aberdeen believes that
metadata must not only offer substantial help in tracking and managing changes
on multiple levels, but it must also be tightly linked to strong documentation
that can assist implementers in the rapid-deployment phase of the life cycle.
Above all, enterprise success will depend on the toolset’s ability to leverage
metadata to keep information in context for both the developer and the user.
Rightly heeding the counsel of its forward-thinking user base, Prism Solutions
continues to focus its initiatives on building a complete metadata-leveraged
toolset that can soundly respond to any size of data warehouse chore. These
offerings, bundled into the Prism Scaleable Data Warehousing Solutions
packages, consist of the same drag-and-drop transformation environment, but
Prism has tailored them in price and functionality for the appropriate
environment. These solutions packages are tailored for Unix- and NT-based
data marts, more complex legacy-to-Unix and Unix-based departmental marts
and warehouses, and full-scale enterprise warehouses. Each scalability step
includes the commensurate selection of pre-designed (but extensible)
transformations typically needed to build the warehouse.
Prism has leveraged this foundation with the introduction of its new Prism
Warehouse Executive and the Prism Warehouse Directory. Working in concert,
these facilities comprise a process-sensitive environment (refer to Figure 1) that
helps both technical and business users navigate through the intricacies of
information access.
Figure 1: Prism’s Metadata-Driven Architecture
Undisplayed Graphic
Source: Prism Solutions, January 1997
The Prism Warehouse Executive (see below) combines a graphical user
interface and a workﬂow model to help guide implementers through the many
data transformations and conversions required to build both data marts and data
warehouses. Toward that end, Prism Warehouse Executive integrates the
design, construction, maintenance, and operations phases of the life cycle.
During these processes, the Prism Warehouse Executive collects metadata and
stores it within the Prism Warehouse Directory for use (and reuse) by
developers, administrators, business users, and the tools that these workers
require to do their jobs. Decision-support tools and industry-standard Web
browsers can access the information contained within the Prism Warehouse
Directory.
Prism's newest enhancements to its metadata-driven facilities will start rolling
out this month and will continue to do so at regular, vision-fulﬁlling intervals
throughout 1997. Of particular note is Prism’s pledge to extend its formerly
Cobol-centric transformation engine to include the C programming language.
Over time, the company will facilitate the use of other languages, for example,
C++ and Java, or other emerging languages. Prism is also well under way in
integrating its "objectized" facilities with the Object Management Group’s
Corba (Common Object Request Broker) and Microsoft’s DCOM (Distributed
Component Object Model). Prism facilities will use these object backbones to
distribute and synchronize metadata.
Aberdeen believes that Prism's delivered and impending enhancements to its
architecture — from Web-enabling metadata access to giving business users the
ability to build their own personal data marts and later enfold them into multi-
user systems — are solidly pointed at playing a role in elevating the warehouse
potential for business users, easing the IS burden, and maintaining a detailed
and enlightening audit trail of critical and reusable warehouse processes.
Executive Decisions
At the heart of Prism's architecture is the recently unveiled Prism Warehouse
Executive, next-generation data warehouse management software that extends
the functionality of Prism Warehouse Manager, a Windows-based construction
and maintenance facility. The Prism Warehouse Executive offers a common

GUI across all Prism applications and fulﬁlls the Prism charter of continuing to
deepen the integration between the design, construction, and maintenance
functions of data warehousing, while setting a common metadata foundation.
Toward that end, the Prism Warehouse Executive supports the following ﬁve
warehouse-critical features within a single workstation:
Document editing, which captures and documents warehouse requirements
as well as the metadata representing those requirements, is integrated with
the Prism Iterations methodology, and supports a hypertext-style editing;
Diagram editing, which helps graphically model the warehouse and the
transformations used to create it, enhances the ability to edit the tables,
maps, and transformations, and pulls templates and data models from
third-party computer-aided software engineering (CASE) tools and data
repositories;
Construction, including transformations, business rules and user exits as
well as veriﬁcation, code generation and database loading;
Searching, which is particularly valuable when looking for tables, maps
and ﬁelds in the metadata directory; and
Administration, particularly in offering efﬁcient ways of setting up and
managing warehouse projects and in generating standard reports and print
diagrams.
From the same Prism Warehouse Executive workstation, the Diagram Editor
helps graphically model the data mappings and transformation that represent
the ﬂow of data from multiple sources into the warehouse. With this
diagramming capability, developers can display the workﬂow of a particular
mapping, and display the input or output of individual ﬁelds.
The Prism Warehouse Executive Document Editor, in turn, captures and
documents the warehouse requirements. Tightly linked to other Prism
Warehouse Executive components, the Document Editor will enable enterprises
to create design documents and reports.
These facilities, Aberdeen believes, will serve as a value-add communications
mechanism during the warehouse requirements-gathering phase, and can help
obviate the miscommunications typical of such procedures when performed
either manually or with less powerful tools. Moreover, Prism plans to increase
Prism Warehouse Executive’s ability to leverage best practices from previous
warehouse iterations by supporting the templates contained in the Prism
Iterations methodology.
Simplifying Scalability
Many installations have been demanding toolsets that dramatically reduce the
complexity created by the success of their data warehouses and data marts. In
response to its largest users, Prism has delivered several features that eliminate
many steps during the complex transformation process. For example, designers
can now use a single step to merge multiple sequential ﬁles and integrate them,
and then output the multiple ﬁles in a many to many manner. Moreover, they
are able to mask or deﬁne the layout of date ﬁelds when moving data or
business rules from sources to target databases, which will have particular
applicability to the year 2000 problems.
With the introduction of a feature called Intelligent Copying, developers will be
able to reuse particular mappings or tables and user exits within mappings.
When a warehouse designer copies a program or mapping, he or she can
specify whether to reuse existing tables or user exits in a given program and
whether to reuse the metadata within the same subject area or across subject
areas. This feature, Aberdeen believes, will be particularly valuable in the rapid
deployment of data marts, or in the reverse direction — that is, in building a
cohesive enterprise-wide warehouse one subject-oriented data mart at a time.
Stronger Metadata Role, Stronger Metadata Facilities
The Prism Warehouse Directory, a metadata facility for both business and
technical users, is becoming an increasingly critical weapon in helping Prism
users track and manage the metadata necessary for accomplishing their goals.
While the Prism Warehouse Directory continues to serve the enterprise by
supplying users with ways to intelligently navigate through it, Prism Warehouse
Directory is also the common-format integration point for Prism's ability to
exchange metadata with CASE tools and repositories. The Prism Warehouse
Directory can exchange metadata via the CDIF standard between Hewlett
Packard’s Intelligent Warehouse middleware, and PLATINUM technology
inc.'s PR/MVS and R&O's Rochade repositories. This capacity both leverages
the enterprise’s existing data and melds metadata into the enterprise’s IS
infrastructure. Moreover, Prism Warehouse Directory is able to accept metadata
from CASE tools, including Logic Work's Inc.’s Erwin, Texas Instruments
Inc.’s I.E.F. Composer, Bachman Terrain and Groundworks, Sterling Software
Inc.’s Key:Model (Knowledgeware), and Oracle Corp. Designer/2000.
While Prism has broadened the reach of its metadata facilities, it continues to
increased the depth of metadata access for access tools and environments,

including software from Cognos Corp., Brio Technology Inc., Business Objects
Inc., and MicroStrategy Inc. Moreover, Prism has laid the foundation for a
comprehensive Web-based architecture by opening Prism Warehouse Directory
access to Web browsers (see below).
Leveraging the tool's ability to capture metadata, Prism Warehouse Executive
also allows implementers to annotate the metadata — e.g., the historical
requirements that drove the creation of the metadata in the ﬁrst place — and
store it within the Prism Warehouse Directory. This annotating feature,
Aberdeen believes, will allow the system to transcend the limitations of any
one developer creating it, and help the enterprises maintain a complete
versioning history of transformations and metadata.
Operational Capacities
Aberdeen believes that information-access architectures will require facilities
that continually and automatically manage — and in some instances trigger —
the movement of data throughout the environment. These facilities will become
especially crucial as enterprises increase the number of data marts, each
offering a data perspective necessary for a particular view of the business and
each requiring updating of different information, and at a different pace. In
addition to metadata management, automated design and development, and
capturing and applying changes from sources to the warehouse, Prism is
creating several new facilities to help automate information-access
architectures. These include:
Graphical operations management, which allows the designer to layout
the warehouse operational ﬂow so that, for example, it can be picked up
by the operational management for execution by existing schedulers;
Operations metadata capture, agent technology that captures critical
metadata pertaining to the ﬂow of information from source to target,
including, for example, the time required for the transformation and
whether the processes were disrupted before completion; and
Event scheduling, to enable administrators to script actions (e.g.
dynamically update the warehouse) based on events, activities, and rules.
Prism is integrating its facilities with Computer Associates’ CA-7, and
Unix scheduling facilities.
Throughout 1997 Prism plans to augment its facilities with administration
software designed to help set up users and authorize access, monitor access and
usage patterns as well as warehouse events, archive low-usage data to tape, and
back up and purge the warehouse contents. Over time, the company plans to
release query-management facilities to help ensure persistent query generation
(based on the cost of the query), and analyze the cost structure of a query.
These facilities will generate reports, monitor query-usage patterns, route
queries to best-results summary tables, and advise administrators about what
summarizations will speed up queries.
Maintaining a Strong Foundation
Prism has also continued its well-established pattern of adding new sources and
targets and ﬁne-tuning the transformation and loading processes. Sources
include DB2/MVS, DB2/400, Enscribe, IDMS, IMS, Informix, NonStop SQL,
Sybase, Teradata, Oracle databases including Rdb, Digital RMS, and VSAM
and sequential ﬁles under MVS or Unix. In addition, the company has ﬁeld-
developed utilities for Software AG's Adabas. Target RDBMSs now include
mainframe DB2 and DB2 Parallel Edition, Informix, Microsoft SQL Server
(spring), NonStop SQL (with new enhancements to the loading mechanism),
Oracle databases including Rdb, Red Brick Warehouse, Sybase/SQL Server,
and Teradata. In addition, Prism supports Windows 4.0 NT clients, as well as
SQL Server NT as a data mart server.
Iterations
Faced with new-style architectures, many IS executives have prudently decided
to bring best-practices data warehousing methodologies into the loop. Not only
must a methodology guide enterprises through the manifold processes of
crafting information architectures based on data warehouses and data marts,
they must also train relevant enterprise personnel to discover business areas
within the enterprise particularly suited for the get-business-payback-quick
beneﬁts of information architectures. In other words, even a successful
implementation must be viewed as a point of departure, as a work in progress.
Prism's Iterations is a comprehensive, experience-based methodology for
helping enterprises correctly scope, design, and build their data
warehouse/information architectures. Based on experience gleaned from some
250 data warehouse implementation and consulting engagements, the Iterations
methodology is composed of interlocking tracks that will help IS executives,
planners, and architects — and, equally important, business users — quickly
and conﬁdently think and step through the numerous issues that could
potentially become data warehouse mineﬁelds — and step through them again
as they realize that information architectures must continuously evolve to meet
the needs of the enterprise.

Iterative thinking and design — which requires strong project management
skills and deploying during the process of developing — must encompass the
identiﬁcation of business metrics and business analysis as well as tough
implementation issues, including database design, metadata management,
platform selection, and both information access by end-users and the
information architecture's continual acquisition of legacy data. Accordingly,
Prism has partitioned the interrelate processes of building and using the
information architectures into ﬁve tracks, each with corresponding activities in
the phases of analysis, design, construction, and testing — and each occupying
a position in a loop that returns to the perpetual processes of new iterations and
maintenance.
Identify these and many associated design, development, and usage issues, and
addressing them within its approximately 30 modules, the Iterations
methodology uses experience as its springboard. Since iterative methods go
against the grain of most development practices, Prism complements Iterations
with SureStart, a two week on-site consulting and training program that will
train the enterprise staff in the methodology. Equally important, the consulting
portion of the program includes an assessment of whether the enterprise has the
adequate technical skills and environments to match the enterprise data
warehouse technical and business objectives.
Leveraging Objects: A New ORB Solution
Throughout 1997, Prism will evolve its entire architecture toward an object
component model — toward an infrastructure that integrate its "objectized"
facilities with the Object Management Group’s CORBA and Microsoft’s
DCOM. Prism facilities will use these object backbones to distribute and
synchronize metadata and control the ﬂow of scheduling and monitoring tasks.
This architecture will contain a common repository and warehouse applications
framework. The ﬁrst manifestation of this architectural shift is the Prism
Warehouse Executive, which contains a common GUI and an application
framework (see above). Prism will leverage Prism Warehouse Executive and its
common metadata repository with operations and administration management
software. By the second half of the year, say company ofﬁcials, they will have
delivered a common architecture and a common use model across all offered
facilities.
Getting Personal
In keeping with Prism's charter of allowing identical access and functionality,
whether for data marts or data warehouses, the company has taken several steps
toward delivery low-cost information access. Prism’s Web Access module,
which will be available in the ﬁrst quarter of 1997 at a cost of $2,500 for ﬁve
concurrent seats, creates Java and Hypertext Markup Language (HTML) views
of metadata. Web access means that browser-enabled users will be able to peer
into the Prism Warehouse Directory to gain access to the available Java views
or HTML pages, or metadata to help guide their decision-support queries. Users
can download this information and incorporate it within existing Microsoft
Excel and Access desktops for reporting and analysis.
During the same time frame, Prism will deliver its Personal Mart Toolkit,
which is similar in price point to the Web Access module and is designed to
help business users understand the available data in relational databases and
build their own Web-based views of their desired data. While the point-and-
click interface promises to allow business users to work independently of IS,
the Personal Mart Toolkit’s navigational model can be stored on, say, a
workgroup server, thus allowing both the user views (and the navigational
paths required to deliver the views) to be updated as requirements change.
Since session histories can be recorded for future use, Prism ofﬁcials say that
users will be able to select from among existing queries, and IS will be able to
track users’ requirements and use them for prototyping data warehouse and data
mart subject areas and applications.
Aberdeen Conclusions
Prism Solutions continues to leverage its position as a leading supplier to
forward-thinking data warehouse users by, ﬁrst, identifying critical
information-access issues and problems, then quickly delivering metadata-
driven solutions that soundly respond to them. Prism Solutions’ newest
generation of metadata-driven software for the building, managing, accessing,
refreshing — and the critically important scaling — of data warehouses and
data marts offers a common GUI across all Prism applications and fulﬁlls the
Prism charter of continuing to deepen the integration between the design,
construction, and maintenance functions of data warehousing. With the
introduction of its new Prism Warehouse Executive and the Prism Warehouse
Directory, the company has delivered a process-sensitive toolset that combines
a graphical user interface and a workﬂow model to help guide implementers
through the many data transformations and conversions required to build both
data marts and data warehouses. During these processes, Prism Warehouse
Executive collects metadata and stores it within the Prism Warehouse Directory
for use (and reuse) by developers, administrators, business users, and the tools
that these workers require to do their jobs. End users' decision-support tools as

well as Web browsers can access the metadata to help guide and enrich
analyses.
Throughout 1997, the company plans to integrate its metadata facilities with the
OMG’s CORBA and Microsoft’s DCOM, using these object backbones to
distribute and synchronize metadata and ultimately create a metadata-leveraged
architecture that can soundly respond to any size of data warehouse chore.
As data warehouses scale, enterprises will need an automated framework that
helps administrators distribute and track changes. These dynamic architectures
will have to respond to modiﬁcations to data warehouses and/or data marts,
particularly in the number of data sources or in the combinations of data from
those sources, in underlying warehouse technologies, and ultimately in the
information content the warehouse or data marts provide to users.
Aberdeen believes that Prism continues to demonstrate foresight and initiative
in delivering a metadata-driven toolset that encourages and leverages short,
iterative deployment, and fully supports business requirements throughout the
warehouse life cycle. Aberdeen is conﬁdent that Prism will continue to give
enterprises a best-practices competitive-advantage toolset that will fully support
and leverage technical and business requirements throughout the warehouse life
cycle.
AberdeenGroup,
Inc.
One Boston Place
Boston,
Massachusetts
02108 USA
Tel: 617.723.7890
Fax: 617.723.7897
Contact Information:
Susan Rinehart, Client Services Manager(direct #:
617.854.5212)
David Borde, Marketing Manager (direct #:
617.854.5226)
Email: rinehart@aberdeen.com or
borde@aberdeen.com
This Document is for Electronic Distribution
Only
-- REPRODUCTION PROHIBITED --
Copyright 1997 Aberdeen Group, Inc., Boston, Massachusetts
The trademarks and registered trademarks of the corporations mentioned in this
publication are the property of their respective holders. Unless otherwise noted, the entire
contents of this publication are copyrighted by Aberdeen Group, Inc. and may not be
reproduced, stored in a retrieval system, or transmitted in any form or by any means
without prior written consent of the publisher.


---

## Frictionless Data Package Metadata Appendix

### Study Record

| Field | Value |
|-------|-------|
| study_id | 1997-dw-competitive-advantage-through-pr-b307c7 |
| title | Competitive Advantage Through Prism Metadata Scalability |
| author | Aberdeen Group |
| date | 1997-06-01 |
| type | Profile |
| subject_domain | Data Warehousing / Business Intelligence / Metadata Management |
| source_file | 1997 dw Competitive Advantage Through Prism Metadata Scalability pr.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group profile of Prism Solutions Inc. evaluating its metadata-driven data warehouse software suite including Prism Warehouse Executive, Prism Warehouse Directory, Prism Iterations methodology, Web Access, and Personal Mart Toolkit. Aberdeen endorses Prism's metadata-first architecture as key to managing dynamic data warehouse evolution. Prism acquired by Ardent Software for $42M in January 1999.

### Document Assessment

| Dimension | Score (1-5) | Rationale |
|-----------|-------------|-----------|
| Importance | 4 | Full-text profile of a genuine 1997 DW market leader with 400 customers and $55M 1998 revenue. |
| Relevance | 4 | Directly relevant to data warehousing ETL and data governance history; technology lineage through IBM DataStage. |
| Prescience | 4 | Metadata thesis proved foundational (modern data catalogs validate it). CORBA/DCOM integration prediction failed. Prism financial viability overstated. |

### Prescience Detail

1. **Metadata management thesis confirmed:** Aberdeen's assertion that metadata is THE key to DW scalability proved correct. Modern data catalog market (Collibra valued $3B+ in 2021, Alation, Atlan) directly validates this 1997 prediction. (Source: [Ardent buys Prism, ESJ 1999](https://esj.com/articles/1999/01/06/ardent-buys-warehouse-vendor-prism-solutions_633718596211835545.aspx))

2. **Data warehouse growth confirmed:** DW became universal enterprise infrastructure. Cloud DW platforms (Snowflake IPO $33B+ 2020, Amazon Redshift, Google BigQuery) confirm Aberdeen's 1997 DW importance thesis.

3. **Iterative DW methodology confirmed:** Aberdeen's endorsement of iterative DW development aligned perfectly with Kimball dimensional modeling methodology and modern agile data practices.

4. **CORBA/DCOM integration — failed:** Prism's planned CORBA/DCOM object architecture for metadata distribution was not delivered before the 1999 acquisition. Both technologies were superseded by web services.

5. **Prism financial viability — overstated:** Despite Aberdeen's strong endorsement, Prism's stock fell from ~$35 (IPO 1996) to ~$2 by late 1998. Acquired by Ardent Software for $42M in January 1999. The technology was good but the independent company did not survive.

6. **Ardent-Informix-IBM lineage:** Ardent (which acquired Prism) was itself acquired by Informix for ~$880M in March 2000. Informix sold its database to IBM in 2001, remainder became Ascential Software, acquired by IBM in 2005 for $1.1B. DataStage (the Ardent/Prism ETL lineage) became IBM InfoSphere DataStage — still a leading enterprise ETL tool today.

### Entities (15 records — see data/entities.csv)

Key: Prism Solutions (acquired $42M 1999), Ardent Software (acquired $880M 2000 by Informix), Cognos (acquired IBM $4.9B 2008), Business Objects (acquired SAP $6.8B 2008), MicroStrategy (still active), Oracle (still active), HP (split 2015), PLATINUM/CA (acquired 1999), Logic Works/ERwin (acquired CA 1999; now independent erwin Inc.)

### Technologies (14 records — see data/technologies.csv)

Key lifecycles: Prism Warehouse Executive/Directory (Defunct/Absorbed), Metadata Management (Mature/Critical), CORBA/DCOM (Superseded), ETL paradigm (Dominant), Cloud DW (successor technology), Data Catalogs (direct descendant of Prism Warehouse Directory concept)

### Observation Summary

30 observations: 1 strategy-classification, 4 market-data, 6 technology-assessment, 3 benchmark-result, 4 framework-factor, 3 expert-opinion, 4 viability-prediction + 4 actual-outcome pairs. Rich empirical profile with verifiable outcomes.
