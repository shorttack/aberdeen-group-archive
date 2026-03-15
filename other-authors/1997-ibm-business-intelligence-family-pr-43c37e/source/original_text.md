# Original Source Text: IBM Business Intelligence Family

**Source:** Aberdeen Group Product Profile, June 1997  
**Retrieved from:** https://web.archive.org/web/19970604113311/http://www.aberdeen.com:80/secure/profiles/1997/ibmbif/ibmbif.htm

---

The Wayback Machine - https://web.archive.org/web/19970604113311/http://www.aberdeen.com:80/secure/proﬁles/1997/ibmbif/ibmbif.htm
IBM Network Computing
Business Intelligence Family
Executive Summary
Potentially, data warehousing can be a major
bottom-line beneﬁt, not just at the corporate level
and in the realm of a few specialized "data
miners", but also – via network computing – in
lines of business and remote locations. Up to now,
however, the typical data-warehousing
implementation has links to operational online
transaction-processing systems, but little else.
The network-computing aim of IBM’s Business
Intelligence Family is to leverage IBM’s
information-processing strengths plus the global
reach of the rest of IBM’s network computing
solution to expand the availability of decision
support "to the masses". The IBM solution also
allows users the Business Intelligence Family and
of the rest of IBM’s network-computing products
to have access to greater func-tionality: data
warehousing users can employ the rest of IBM’s
network comput-ing architecture to access
Internet data, and users of the network-
computing architecture can do data mining. This
allows the Business Intelligence Family to
differentiate itself both as a standalone product –
because of the breadth of fea-tures and services,
and because of advanced functionality like
Intelligent Decision Server – and as an integrated
component of a wider network-computing
solution.
IBM’s Business Intelligence Family includes the
enterprise-scale Information Warehouse plus
Visual Warehouse for data marts, Intelligent
Decision Server for sophisticated Online
Analytical Processing (OLAP), and Intelligent
Miner for data mining. IBM’s DB2 is the
underlying database, with IBM systems-
management tools plus IBM and third-party
data-quality, data-transformation, and data-
access solutions. Business Intelligence Family is
integrated with the rest of IBM’s network
computing architecture particularly via the

Net.data Web-integration tool. It is also
integrated via the meshing of the DB2/data-
warehouse administrative tools with IBM’s
overall systems-management toolsets.
For IBM’s installed base migrating to network
computing, the integration of the Business
Intelligence Family with a broad network-
computing infrastructure gives the resulting
network-computing solutions increased decision-
support capabilities -- and from these capabilities
may come insights that have bottom-line,
competitive-advantage impact. For non-IBM
data-warehousing customers and prospects,
Business Intelligence Family plus network-
computing solutions means a more ﬂexible
solution that can be sliced multiple ways between
data warehouses and data marts and expanded to
new classes of remote and line-of-business end
users. To both sets of IS buyers, Business
Intelligence Family combined with network
computing and IBM services means a relatively
painless migration path to the new capabilities.
Overview: Business Intelligence Family Product
Suite
IBM’s Business Intelligence Family includes an overall enterprise-scale-data-
warehouse solution – Information Warehouse – plus three separate products for
different types of user decision-support needs: Visual Warehouse for 10-to-100-
gigabyte data marts; Intelligent Decision Server, the evolution of the Metaphor
DIS product, for sophisticated Online Analytical Processing (OLAP); and
Intelligent Miner for in-depth data mining. Underlying these solutions is IBM’s
DB2 RDBMS family. These solutions are Internet-enabled via IBM’s Net.data
product, which provides a Web-browser interface to DB2, and Business
Intelligence Family offers administrative-tool integration with IBM’s systems-
management tools such as TME. Table 1 lists the products in the Business
Intelligence Family and their functionality.
Table 1: Business Intelligence Family Product Suite
Product
Features
Information
Warehouse
includes DB2 Common Server or DB2/MVS for
underlying database server, DataPropagator
Relational for replication from OLTP systems,
DataGuide for the data-warehouse catalog, IBM or
third-party end-user decision-support tools, and
hooks to allow Visual Warehouse to act as an
integrated data mart or Intelligent Decision Server
to act as a front-end analysis tool
emphasizes scalability, ﬂexibility, sophisticated
needs
carries out the functions of importing data
(DataJoiner), transforming it (Data Propagator,
Data Refresher), distributing it (Data Propagator,
DataJoiner), storing it (DB2), supporting
administrators in ﬁnding and understanding it
(DataGuide), and allowing end users to discover,
display, and analyze it (Lotus Approach, Intelligent
Decision Server, Intelligent Miner, Application
System, Query Management Facility); also
manages the data warehouse (DataHub,
FlowMark) and provides IBM consulting services
Visual
Warehouse
supports 10-100 gigabyte data marts standalone,
linked, or subordinate to large-scale data
warehouse
emphasizes fast, inexpensive installation and
startup

includes Visual Warehouse Manager (remote
administration on Windows NT workstation) using
Visual Warehouse Agents, and Visual Warehouse
Administrator Clients; a Visual Warehouse Control
Database (DB2) with importation from DB2-
family, Informix, Microsoft, Oracle, and Sybase
relational and VSAM and IMS non-relational
source databases; ODBC support for PC, Mac, and
Unix (AIX, Solaris, HP-UX) clients
integrates with third-party multidimensional
analysis and querying tools
Intelligent
Decision
Server
decision support tool that provides a broad array of
front-end multidimensional analysis operations
such as drill-down, roll-up, facts, and metrics
derived from DB2 or other major popular
RDBMSs
n supports a variety of clients, including Lotus
Notes, Web browsers, and ODBC-compliant
applications such as Lotus Approach
provides an application development environment
speciﬁcally geared to creating decision support
applications
Intelligent
Miner
supports data-mining operations such as clustering,
classiﬁcation, prediction, association discovery,
sequential pattern discovery, similar-time-sequence
discovery
provides data-preparation functions such as
Oracle/Sybase data extraction, data merge
Visual Warehouse
Visual Warehouse is presently focused particularly on IBM installed-base needs
for data marts, and especially those environments with OS/2 and AS/400
networks. The software in Visual Warehouse provides easy-to-use design and
installation, while providing a subset of the typical data warehouse’s features
that ensures Visual Warehouse will be most effective in the 10-100 gigabyte
data-mart database range. Recent extensions to Windows NT mean that Visual
Warehouse can also deliver data-mart functionality to implementations of
network computing based on widely-popular Windows NT LANs.
Visual Warehouse provides Business Views that allow users to transform the
raw decision-support data into business information. Sophisticated facilities use
Business Views as a base:
• DataGuide, an information catalog, allows end users to browse business-
view metadata and then "drill down" to analyze the underlying data;
• Editions and Versions – Editions containing past "histories" of how the
business view has changed over time, Versions allowing users to revert to
previous data for audit purposes – give users a historical record for such
uses as trend analysis;
• Schedules allow administrators to schedule the periodic update of
business-view data automatically; and
• Triggers allow notiﬁcation of users when a key business-view-update
"event" occurs.
Recognizing that the administrator is key to the success of any data mart,
Visual Warehouse also provides extensive administrative tools for functions
such as deﬁning target databases, managing security, scheduling, and
monitoring. These tools include Administrative Clients that provide the
administrative user interface; Agents that handle source-data access, ﬁltering,
transformation, subsetting, and delivery; and the Visual Warehouse Manager
that uses a Control Database (containing administrative information such as
metadata, logs, Business Views, and schedules) to execute the administrative
functions.
Visual Warehouse gives additional ﬂexibility to IS designers of IBM-based
overall data-warehouse solutions: it allows use of cost-effective, rapidly-
installable depart-mental data marts instead of or alongside an enterprise-scale
data warehouse. In network computing environments, Visual Warehouse’s
ability to integrate into an enterprise-scale Information Warehouse means that a
wider range of end users can access not only enterprise but also mission-critical
departmental data.
Intelligent Decision Server and Intelligent Miner

The Business Intelligence Family’s querying and analysis tools are key to
IBM’s efforts to extend data warehousing to a broader class of end users. At
present, these tools provide sophisticated operations such as drill-down and
clustering that are most useful to trained data analysts. Third-party tools such as
Cognos’ Impromptu are often used for more elementary querying and analysis.
Thus, as users implement network computing, there is a natural end-user
growth path from open, easy-to-learn querying to more sophisticated data
mining using IBM value-added tools.
Intelligent Decision Server (IDS) is an "analytical application server" – it
provides query, reporting, business graphics, and analytical functions on the
server that can be accessed by IBM and third-party client-side querying tools
via the Open Data Access Service (ODAS) and ODBC. Users can easily group
the server-side analytical objects into applications called Capsules,, using the
drag-and-drop GUI. Thus, an analyst can automate a series of data-access and
analysis tasks by creating a Capsule, or by building one on top of already-
existing IBM, third-party, or in-house Capsules. Typical Capsules include
market-penetration analyses, trend analysis and forecasting, fraud detection,
promotion-effectiveness analysis, credit-risk determination, and target
marketing.
IDS includes its own ROLAP administrative tool that allows users to set up
databases, connect database tables, create metadata, and other typical data-
warehousing tasks. IDS includes "transformer" business-analysis objects that
users can employ within Capsules to combine data from multiple databases.
IDS provides strong scalability support, with full multithreading of server-side
applications.
Information Warehouse
A particularly outstanding technology feature of Information Warehouse is its
ability to tie together multiple suppliers’ data sources effectively as a highly-
scalable distributed database. DB2, DataPropagator, DataHub, and DataJoiner
work especially effectively together. DataPropagator allows users to download
data copies from one database to another with high performance in such situa-
tions as data warehouses. DataHub provides management of multiple databases
and replicated data from a single control point. DataJoiner provides transparent
SQL-based data access, not only across DB2 (and non-DB2 RDBMS)
instances, but also across dissimilar data management systems such as IMS.
DB2's interoper-ability also allows end users to access transparently and
perform multisite updates on databases distributed across servers,
minicomputers, and mainframes.
Data Propagator and Data Refresher
A key differentiator for DataPropagator is its architecture. To replicate data,
Data-Propagator ﬁrst provides a "capture" stage to a staging area, then an
"apply" stage to the destination database. The RDBMS propagates changes to
the staging area, and DataPropagator then applies the changes to the target. The
capture stage monitors the RDBMS's log, and DataPropagator's implementation
allows replication to each RDBMS copy to occur asynchronously, in parallel
with normal RDBMS processing, with minimal overhead. As a result,
DataPropagator can operate in virtual isolation, minimizes performance
overhead, increases data integrity and the ability to recover from system
failures, and can operate against RDBMSs from multiple suppliers.
To connect to non-relational data such as IMS databases, users can hook Data-
Propagator NonRelational (for "capture") to DataPropagator Relational (for
"apply"). Also, DataRefresher provides support for "refresh" copying of IMS,
VSAM, and ﬂat ﬁles to DataPropagator Relational's staging area.
DataPropagator also shines in other replication details. Sophisticated operations
on data being replicated allow joins and subselects for data subsetting,
derivation, aggregation, conversion, consolidation, and application of SQL. For
laptops in mobile networks, replication can be "pushed" from the laptop or
"pulled" from the central server. DataPropagator can "reduce" the data to be
replicated before transfer for better communications performance. Before-
image data captures improve recovery and give the user useful historical data
about the distributed database.
Much of the attractiveness of DataPropagator for replication lies in its details.
Aside from those mentioned earlier, DataPropagator offers communications-
performance improvement via "hotspot reduction" (bundling several updates to
a piece of data into one), load balancing, sending of replications in sets of
messages rather than singly, data "fan-out" (sending replications to one server
which then sends them -- fans them out -- to the other servers), and update
batching.
DataJoiner
DataPropagator is complemented by DataJoiner, which supports distributed
joins across multiple databases -- relational, IMS, and VSAM -- from multiple
suppliers on multiple servers. DataJoiner's sophisticated cost-based global
optimizer considers not only the queries themselves but also the networks
involved and the I/O speed of the various systems. DataJoiner can simulate

operations such as multiple open cursors that the data-management system may
lack, allowing relational and nonrelational systems to join in performing
sophisticated operations.
DataJoiner provides location and network transparency, so that applications do
not have to change when the underlying architecture changes. End users can
invoke DataJoiner from Lotus Approach, and Microsoft Access, and
programmers from IBM's VisualAge and Sybase/Powersoft's PowerBuilder and
other ODBC-supporting data-access and development tools.
DataHub and FlowMark
DataHub provides database administration services for DB2, and connects its
administrative tools to other IBM data-management and systems-management
solutions. DataHub includes SNMP support that should allow users to create
mechanisms to pass information between DataHub and other DORS suppliers'
administrative tools. DB2 version 2 provides a database Management
Information Base (MIB) and SNMP subagent.
DataHub provides management of data from a single control point. Database
management tools arriving with DB2 version 2 -- especially DB2 Performance
Monitor, Visual Explain, and the SNMP subagent -- provide extensive database
statistics, monitoring, and tuning capabilities. Visual Explain shows the
optimizer's SQL plan, allowing users to monitor and ﬁne-tune application
performance. Performance Monitor performs analyses and enables
administrators to view the system and generate reports. The SNMP subagent
allows today's major systems management solutions to monitor DB2 and work
with DataHub.
DataHub provides exceptional administrative ﬂexibility and automation for
single-site and distributed databases. Administrators may use DataHub's
command scheduler or IBM's FlowMark workﬂow management product to
automate operations.
DataHub provides sophisticated, relatively automated distributed-database
administration. DataHub allows management of multiple databases and systems
from a single control point, including task-oriented database-administration
functions and automated system and database monitoring and alerting.
DataPropagator users may register and subscribe to data copies via a GUI-
based tool integrated into DataHub.
DB2
DB2 offers competitive and leading-edge RDBMS technologies plus
unmatched integration with today's corporate and mainframe databases. As a
result, DB2 not only allows IS to create highly scalable and ﬂexible new
solutions for OLTP, decision support, and "mixed" network-computing
environments, but also lets these solutions leverage today's corporate data --
and present applications access the new databases -- more effectively.
Interoperable DB2 variants include DB2 common server, DB2/MVS, and DB2
Parallel Edition, which provides capabilities similar to those of DB2 version
1.2 for IBM RS/6000 loosely-coupled and SP Massively Parallel Processing
(MPP) hardware.
DB2 provides especial support for data-warehousing via its integration with
DataPropagator, DataRefresher, DataJoiner, and DataHub; via its "query
rewrite" that provides high performance for complex queries; and via its
Relational Online Analytical Processing (ROLAP) features such as the CUBE
operation and bitmapped indexing.
DB2 provides effective hooks to support Internet-type network computing.
IBM has announced extensive Internet support, including CICS-based
middleware providing access to DB2 and other suppliers' RDBMSs, and a
World-Wide-Web connection allowing creation of Web applications accessing
DB2 database using HTML and dynamic SQL.
DB2's multimedia support is especially effective for multimedia Web servers.
DB2 provides signiﬁcant support for complex data types, such as "character"
and "double-byte character" data types (for internationalization), and large (up
to 2 gigabytes) data types. DB2 also provides functions to access parts of a data
type, and the ability to insert a data type too large for main memory into the
database from a client ﬁle or CD-ROM. DB2 now offers Universal-Server
bundles of triggers, user-deﬁned data types, and user-deﬁned functions for
particular data types called Relational Database Extenders.
DB2 is useful not only for the decision-support side of network computing but
in many other data-management areas as well: for databases requiring
connectivity to other IBM platforms, where IBM services are an important
consideration in implementing or upgrading a data-intensive application, and
for particular applications such as mission-critical solutions requiring
sophisticated DBMS tuning and proven reliability. In assessing DB2, IS buyers
should factor in its wide array of options and parameters that allow exceptional
tuning to ﬁt user needs.

Where Business Intelligence Family Is Most
Effective
For enterprises moving to a network computing architecture, Business Intelli-
gence Family is especially effective where large-scale data warehousing is an
important part of IS’ strategy and such factors as breadth and scalability of
data-warehousing functionality, design/implementation service and support, or
analysis-tool sophistication are important criteria. Where the organization is
migrating from IBM systems, Business Intelligence Family’s integration with
other IBM products such as DB2 and IBM’s extensive services mean a
relatively low-risk migration strategy. Moreover, network computing can
leverage IBM’s data ware-housing and vice versa: network computing can
bring wider end-user access to key data, and data warehousing can deliver
competitive-advantage insights to this wider class. This is especially true where
mainframes hold much of the organiza-tion’s key data; IBM’s strength on the
mainframe means that VSAM, IMS, and DB2/MVS data can now be seen
outside of the data center, ﬁrst by translation to the data warehouse and then by
distribution to end users via network computing.
For organizations moving to network computing and having software and
hardware from multiple suppliers, Business Intelligence Family’s ability to
incorporate third-party querying and administrative tools and carry out high-
performance replication to and from multiple suppliers’ RDBMSs can also be
particularly effective in many cases. IBM’s broad services mean one-stop-shop
support for the complex tasks of not only of designing and administering a data
warehouse or data mart, but also of migrating data warehousing to a network
computing environment.
Aberdeen Conclusions
IBM’s Business Intelligence Family of data warehousing products is an
exceptionally strong and useful component of IBM’s network computing
solution suite. Enterprise-scale data warehousing and distributed computing
play to the distributed-database strengths of products such as DB2 and
DataPropagator, and IBM’s strong presence in data warehousing and extensive
service arm that is well-experienced in implementing data warehouses and data
marts give IBM a clear differentiation in delivering large-scale network-
computing decision support. IBM’s Universal-Server multimedia strengths via
DB2’s Extenders can aid in downloading Web-page multimedia data. Tools
such as Intelligent Decision Server and Intelligent Miner hold the promise of
allowing greater end-user data-mining sophistication across a wider range of
Intranet and Internet end users.
The Business Intelligence Family will need to continue to evolve rapidly as
network computing solutions advance and proliferate. For example, IBM will
need to add data-mining and administrative functionality to its Visual
Warehouse and continue to move it to more platforms; provide closer
integration between Intelligent Decision Server and Intelligent Miner and basic
third-party or IBM querying tools; further Web-enable the key components of
the Information Warehouse to allow such functionality as cursors and
governors on Web-browser clients; and add Extender functionality for Internet-
speciﬁc querying.
The Business Intelligence Family can therefore deliver immediate bottom-line
competitive-advantage data-mining beneﬁts on its own, and IS buyers can use
IBM’s data warehousing to leverage their network computing strategies – or
IBM’s network computing with Business Intelligence Family included to
leverage their data warehousing. Aberdeen recommends that IS buyers
considering a network computing strategy rank the Business Intelligence
Family high in importance among IBM’s network-computing products, and
high in potential effectiveness among their overall network-computing
purchases.
AberdeenGroup,
Inc.
One Boston Place
Boston,
Massachusetts
Contact Information:
Susan Rinehart, Client Services Manager(direct #:
617.854.5212)
David Borde, Marketing Manager (direct #:
617.854.5226)

02108 USA
Tel: 617.723.7890
Fax: 617.723.7897
Email: rinehart@aberdeen.com or
borde@aberdeen.com
This Document is for Electronic Distribution
Only
-- REPRODUCTION PROHIBITED --
Copyright © 1997 Aberdeen Group, Inc., Boston, Massachusetts
The trademarks and registered trademarks of the corporations mentioned in this publication are
the property of their respective holders. Unless otherwise noted, the entire contents of this
publication are copyrighted by Aberdeen Group, Inc. and may not be reproduced, stored in a
retrieval system, or transmitted in any form or by any means without prior written consent of
the publisher.




---

## Appended Frictionless Metadata

**Study ID:** 1997-ibm-business-intelligence-family-pr-43c37e  
**Archive Date:** 2026-03-14  
**Pipeline Version:** Archive-13 v1.0  
**License:** CC-BY-4.0  
**Source URL:** https://web.archive.org/web/19970604113311/http://www.aberdeen.com:80/secure/profiles/1997/ibmbif/ibmbif.htm

---

## Prescience Detail

### Prediction Assessment: 4/5

Aberdeen's 1997 IBM BI Family profile demonstrated exceptional prescience about the direction of business intelligence.

#### Correct Predictions
1. **BI democratization to the masses (CONFIRMED):** Aberdeen's core thesis — that network computing would expand BI from corporate data analysts to line-of-business users — precisely describes the BI market trajectory from 1997 to 2020. Tableau (2003), Power BI (2015), and self-service analytics validated this vision.

2. **Data mining as growth path from querying (CONFIRMED):** Aberdeen described data mining as the natural end of a user sophistication continuum starting with querying. The rise of machine learning/AI analytics after 2010 confirms this trajectory.

3. **Data warehouse + data mart hybrid architecture (CONFIRMED):** Aberdeen's description of flexible warehouse/data-mart architectures presaged the modern logical data warehouse and later the "data lakehouse" concept.

4. **Metadata/business views semantic layer (CONFIRMED):** Visual Warehouse Business Views as semantic layer between raw data and users describes the exact architecture of modern BI tools (LookML in Looker, semantic layers in Power BI, etc.).

5. **DataPropagator async CDC (CONFIRMED):** Change Data Capture for data warehouse population, as described for DataPropagator, became a standard component of modern data pipelines (Debezium, Fivetran, etc.).

#### Less Accurate / Missed
- **IBM-branded BI longevity (MISSED):** Aberdeen could not predict IBM would eventually acquire its cited third-party Cognos tool and replace its native BI products. The irony: Cognos Impromptu (described as supplementary) became IBM's primary BI platform.
- **DB2-centric architecture durability (PARTIALLY WRONG):** Aberdeen assumed DB2 as the permanent foundation. Cloud columnar databases (Amazon Redshift 2012, Snowflake 2014) disrupted this architecture.
- **SaaS delivery model (MISSED):** Aberdeen's network-computing model did not anticipate SaaS-delivered BI.

#### Technology Evolution Summary
| Product | 1997 Status | Outcome |
|---------|-------------|---------|
| Information Warehouse | Mature | Replaced by Cognos analytics post-2008 |
| Visual Warehouse | Growth | Discontinued; DB2 DWE successor |
| Intelligent Decision Server | Mature | Replaced by Cognos TM1/PowerPlay |
| Intelligent Miner | Growth | Discontinued ~2010; SPSS Modeler took over |
| DataPropagator | Mature | Evolved to IBM Data Replication |
| DataJoiner | Mature | Evolved to IBM Federation Server |
| Net.data | Introduction | Discontinued ~2005 |
| IBM DB2 | Mature | Still active in 2026 |

