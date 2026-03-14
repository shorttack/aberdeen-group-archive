# Exploring Intersolv's Virtual Data Warehouse

> Archived from: https://web.archive.org/web/19970108191541/http://www.aberdeen.com:80/secure/profiles/intsolv/interslv.htm
> Original publication date: 1995-10-01
> Author: Aberdeen Group

---

## Original Document Text

Intersolv Inc.
9420 Key West Ave
Rockville, Maryland 20850
800-547-4000
Exploring Intersolv's Virtual Data Warehouse
Preface
As enterprises face the challenge of turning data warehouse theory into implementations, they must inevitably ask themselves some tough questions about the size and scope of their
endeavors and to what degree databases optimized for decision support can help guide the enterprise into a competitively-advantageous position.
Aberdeen believes that by the end of the decade most enterprises will be using some form of complex decision support to help develop a better understanding of customers as well as the
operations that will attract new customers -- and, more importantly, keep current customers within the fold. Information-access seekers will be able to select among a variety or blend of
approaches -- from large data warehouses with detailed data to data marts using summarized data, from so-called canned or prepackaged queries to systems that use metadata, or data about
data, to perform the intricate calculations that are needed to answer business-user queries.
This Proﬁle examines Intersolv's Virtual Data Warehouse: a decision-support environment that combines metadata, powerful Intersolv client-side and server-based data-access technology,
and query, analysis and reporting tools. This metadata- driven approach, Aberdeen believes, can help some organizations eliminate the need for a physical departmental data warehouse,
transform third-party -- for example, ﬁnancial -- applications into a data warehouse, and prepare enterprises for a step-by-step, cost-conscious progression into the complex decision-support
environment of their choice.
Executive Summary
Although many leading-edge enterprises continue to attest to the beneﬁts of data warehousing, it does not follow that all decision-support applications will require -- or even beneﬁt from --
building on-line collections of data speciﬁcally geared toward supporting these applications and users' quests for business-driven information. Data warehouses, which are generally built on
relational database management systems (RDBMSs) and sometimes on proprietary multidimensional databases, are the result of a multi-step process that includes designing the warehouse,
exploring the array of hardware, software, middleware, and training choices, as well as moving, enriching, and reformatting the data that will reside in it.
Until now, the best that enterprises looking to measure the value of data warehousing could hope for were the least-cost-of-entry and proof-of-concept alternatives devised by individual
suppliers or various data warehouse initiatives. While removing some of the development and ﬁnancial burden from the enterprise, these incentives still demand at least a minimum
component investment; and for all practical purposes, the buy-in constitutes a commitment.
But with the October 2, 1995 introduction of the Virtual Data Warehouse, Intersolv Inc. has removed most of the obligatory investment for the initial stages. Using an intelligent metadata
layer, called SmartData, which leverages the Intersolv DataDirect Explorer desktop query and reporting tool, the Virtual Data Warehouse enables business users to easily build sophisticated
database queries without having to know cryptic database commands or the Structured Query Language (SQL). This intelligent layer of metadata relates the physical tables and joins and
performs the aggregations that permit users to query and analyze the real-time data. For example, the Virtual Data Warehouse will automatically compute different aggregates depending on
what other columns have been selected for a query. Moreover, users can continue to drill down within a query in search of additional information. The Virtual Data Warehouse uses a blend of
source security as well as the security setup by the systems administrator. And as an architecture based on open database connectivity (ODBC), Intersolv's drivers are able to access more than
35 data sources and most client-server operating systems, including all versions of Windows, IBM's OS/2 and AIX, the Apple Macintosh, HP-UX, and Sun Solaris, as well as any relational
database.
The Virtual Data Warehouse architecture (refer to Figure 1) consists of the following four components:
DataDirect SmartData, which shields business users from the complexities of SQL and is implemented as an ODBC driver, uses intelligent metadata to create (and serve as a common
interface for) each data source in the Virtual Data Warehouse;
DataDirect Explorer, a set of business-user tools (see below) for ad hoc query, analysis, and reporting, includes a job scheduler for performing speciﬁc queries at predetermined times;
DataDirect ODBC Pack, a set of Intersolv ODBC drivers that provide support for more than 35 databases on eight operating systems and can connect any ODBC-compliant application
to any personal, relational, or legacy database; and
DataDirect SequeLink, a server-based, performance-enhancing, data-access technology, which will enable the Virtual Data Warehouse to support large user populations without reducing
performance.
Indeed, it is the power of DataDirect SequeLink, which was recently acquired from TechGnosis International (see below), that will enable enterprises to scale their Virtual Data Warehouses
from client- to server-based systems. While maintaining a single interface into a system of whatever size, enterprises will be able to move pieces of the client to the server, intelligently
dividing processing chores. Furthermore, DataDirect SequeLink will serve as the foundation to supply Virtual Data Warehouse users with enterprise-scale technologies, such as the ability to
perform heterogeneous joins.
Aberdeen believes that Intersolv's Virtual Data Warehouse will be sufﬁciently robust as a solution for many departmental warehouse chores, as well as for those applications the enterprise
considers vital but not necessarily mission critical. Moreover, the Virtual Data Warehouse can serve as a strong interim tool for those enterprises embarking on the multi-month process of
building a physical data warehouse. While the Virtual Data Warehouse will supply users with almost immediate information access, it can easily be enfolded within a physical warehouse,
thus leveraging the enterprise investment. Moreover, Aberdeen believes that the Virtual Data Warehouse will likely help reﬁne and reduce the footprint of the physical data warehouse.
Prices range from $499 for a single-user system running against a single data base to approximately $40,000 for a 20-user server-based Virtual Data Warehouse.
Given these factors and the ability to use the metadata-driven Virtual Data Warehouse with or without a physical warehouse, and with any ODBC-compliant desktop tool, Aberdeen believes
that it deserves close scrutiny by both IS and line-of-business executives.
Building A Virtual Warehouse
While protecting users from database complexities, SmartData metadata can give the information-access hungry organization a single view of its information and rapidly retrieve data. IS
administrators can build a Virtual Data Warehouse -- its columns, constructs, and SmartSets -- by using a point-and-click tool called the SmartData Warehouse Manager. In addition, this tool
also generates semantically correct SQL, a feature that can spare administrators from writing incorrect SQL and that can be exposed or hidden depending on the taste of the administrator.

The Virtual Data Warehouse, in turn, functions like a RDBMS catalog. But rather than the actual data, it contains metadata about the physical structures and the relationships between those
structures. This SmartData semantic layer, which is wrapped around each data source, creates a virtual database, or SmartSet, for each system within the Virtual Data Warehouse.
As a result an enterprise may, for example, create a SmartSet that relates all the tables concerning inventory and orders, and it may contain numerous different tables and views from different
sources; these can be presented in a language and form that business users readily understand. Moreover, each virtual database can contain tables as well as joins; and system builders can
combine more than one table or more than one view. These SmartSets are dynamic; they generate the SQL necessary for a speciﬁc request.
Aberdeen believes that enterprises will be able to transform many virtually dormant data sources into vital information-delivery vehicles. Using SmartData technology, an enterprise can
transform a third-party application, say, human resources or manufacturing software, into a full-feature data warehouse.
Viewing and Sharing Information
With SmartSets established, business users can select from among any ODBC-compliant desktop tools. Intersolv's own Explorer is a multifaceted tool that allows various classes of users
within the enterprise to access trend-revealing information, automatically drill more deeply for additional answers, and systematically share business-driven information throughout the
enterprise. Explorer's Query Builder, which generates correct SQL, is a powerful vehicle for general business users as well as so-called power users.
Once a query returns data, it is ﬁltered through Explorer's Query Grid, a spreadsheet interface for formatting, grouping, ﬁltering and subtotaling results. The basic component for helping
users manipulate and present their results, Query builder is augmented by the following Explorer components:
Chart Builder, which dynamically links data to a chart and therefore allows the chart to be changed when the data change, provides users with wizards to help them build charts and
select from among 37 styles;
Report Builder, which is a Microsoft OLE 2.0 container and can therefore embed any OLE object (i.e., a Word document) within a report, provides default formats and mailing labels,
and automatically generates sections, headers, and footers;
Form Builder, a free-form blank template for developing data-entry screens and frames, it generates a graphical user interface that allows users to view information in a form-based
approach. It also supports numerous objects to help make forms easier and more exciting to use; and
Job Scheduler, which allows users or administrators to script decision-support chores, including the running of queries on different processors and at different times, and the printing of
reports.
Intelligent snapshot, a feature based on Explorer's ability to save data in any ODBC format, allows the administrator to set up the system to take, for example, a snapshot of IBM's DB2
RDBMS and save the results as an Oracle table.
Furthermore, with the help of the Explorer Administrator, an optional $199 component, IS can augment database security and tune each desktop for the skill-level of each user or group of
users. Offering strong LAN-based controls for the decision-support environment, these features include a query governor, which offers the ability to deﬁne the number of records a user can
query; the ability to display revoke messages, which prompt users when they attempt to perform unauthorized activities; and the ability to deﬁne user classes and groups and thereby
eliminate or show particular menu bars, dialogs, and icons.
A New Link To Performance
On October 23, 1995, Intersolv announced the acquisition of TechGnosis International, a Brussels, Belgium-based developer of a server-based database-independent architecture for client-
server connectivity. With this powerful technology, which connects any client front end to any database server across existing networks now used by about 4,000 customers, Intersolv
ofﬁcials say they plan to help the Virtual Data Warehouse to perform heterogeneous joins and launch the processing of agents. Equally important, the company plans to use the TechGnosis
engine to provide a layer that will enable administrators to add or remove sources, and automatically propagate changes to clients.
SequeLink, which is both database and network independent, resides between the database source and the client application, and links directly to existing networks rather than relying on
performance-degrading gateways. While enabling the Virtual Data Warehouse to support large user populations without reducing performance, SequeLink also provides several other
functions that contribute to the attractiveness and performance of the Virtual Data Warehouse. Among these, Aberdeen highlights:
SequeLink API, a set of C programming interfaces for developers;
ODBC ﬂexibility, which allows access from any desktop tools;
Cursor management, for minimizing network trafﬁc caused by SQL calls and data transfer;
Network services, the ability to send and recognize network packets and eliminate the need to use database communications products from other vendors;
Database integration, the ability to directly map SequeLink APIs to the database APIs, thus preserving native functionality and performance; and
Legacy integration, or support for numerous database systems, including relational and non-relational.
Competitive Landscape
Aberdeen believes that the Virtual Data Warehouse's principle differentiation is its ability to share its metadata layer with other tools, whether simple ad hoc query and reporting tools or
robust competitors, among them market leaders Cognos Corp. with Impromptu and Business Object's BusinessObjects. While these competitors also offer the ability to build semantic layers
that disguise the complexity of SQL and eliminate the need to understand set theory operations, these metadata layers are speciﬁc to the tool. However, Aberdeen maintains that both of these
competitors (in their present mature releases) have stronger features for allowing administrators to disseminate changes throughout the enterprise, a shortcoming that Intersolv will address
with the server technology from the TechGnosis acquisition.
But Aberdeen believes that a rapid re-stratiﬁcation of the query and reporting marketplace is now under way, making room for Intersolv to occupy a slot as a high-end query and reporting
tool. Business Objects, for example, is preparing the early 1996 release of Mercury, a decision-support system that combines intelligent metadata with desktop microcubes, essentially
creating a virtual multidimensional environment. However, with theses changes, Business Objects is moving some of its proven technology forward, but is essentially reinventing its tool (as
has Intersolv) and must therefore demonstrate its value in the ﬁeld. For its competitive rejoinder, Cognos is retooling Impromptu and its Powerplay desktop multidimensional database into a
single tool, and it must therefore undergo the usual stress testing of any software product in its ﬁrst release.
What Users Tell Aberdeen
Several early users indicate that the Virtual Data Warehouse is extremely beneﬁcial for building departmental-level decision-support environments and for quickly supplying business users,
each of whom may possess varying degrees of knowledge and sophistication, with immediate access to information. Several users say the Virtual Data Warehouse will likely eliminate the
need to build some departmental warehouses in the enterprise; others believe the enterprise can use the Virtual Data Warehouse while they are building a physical warehouse, and that the
Virtual Data Warehouse design can subsequently be enfolded within a physical warehouse.
Users give strong praise to the Explorer desktop. The interface's prompts, as well as the capacity for administrators to give users annotations, nicely supplement the tool's ability to allow a
user to build a query and perform subsequent analyses against it, essentially drilling down for additional information. By double clicking the right mouse button users can reveal additional
information, thus giving Explorer a multidimensional feel.
Moreover, administrators say they are encouraged by the acquisition of TechGnosis; Intersolv will now evolve the Virtual Data Warehouse into a more robust server-based solution. The new
architecture promises to optimize the transmission of data across networks and is designed to handle large volumes of data trafﬁc.
Conclusion
The fervor for data warehouses has been driven by the need among enterprises of all sizes to access information that has been dormant within both legacy and OLTP systems. Aberdeen
believes that by the end of the decade most enterprises will be using some form of complex decision support and will be selecting among a variety or blend of approaches.

By combining metadata, powerful Intersolv client-side ODBC drivers and server-based access technology, and query, analysis and reporting tools, Intersolv has delivered a technology that
can eliminate the need to build physical data warehouses for some applications. The Virtual Data Warehouse allows users to tap real-time source data, but protects these valuable systems
with a blend of source security and query governors.
Many organizations have put off their investigations of data warehouses because of the numerous and complex steps -- including modeling, training, hardware and software -- needed to build
the prototypes that are necessary for even measuring the value of a data warehouse. The Virtual Data Warehouse is an immediate solution with an immediate payback. Moreover, Aberdeen
believes that the Virtual Data Warehouse will help some organizations eliminate the need for a physical departmental data warehouse, transform third-party -- for example, ﬁnancial and
human resources -- applications into a data warehouse, and prepare enterprises for a step-by-step, cost-conscious progression into a complex decision-support environment of their choice.
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
| study_id | aberdeen-1995-intersolv-virtual-data-warehouse |
| title | Exploring Intersolv's Virtual Data Warehouse |
| author | Aberdeen Group |
| date | 1995-10-01 |
| type | product-profile |
| subject_domain | data-warehousing |
| methodology | industry-analysis,competitive-profiling,field-research |
| source_file | 1995-Exploring-Intersolv_s-Virtual-Data-Warehouse-pr-4.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group profile examining Intersolv's Virtual Data Warehouse approach, which provides unified access to distributed data sources without requiring physical data consolidation.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Documented an innovative but ultimately short-lived approach to data warehousing via federated metadata access; the virtual data warehouse concept was prescient but Intersolv was too small to dominate against Cognos and Business Objects. |
| **Relevance** | medium | The virtual/federated data warehouse concept evolved into modern data virtualization (Denodo, Starburst) and data fabric architectures still relevant in 2026; DataDirect ODBC drivers continue as Progress DataDirect; the architectural insight transfers even though the specific product is gone. |
| **Prescience** | medium | Aberdeen's prediction that enterprises would adopt complex decision support by 2000 proved correct; however the specific Intersolv platform did not achieve the high-end market position predicted—the company was acquired by Micro Focus for $534M in 1998 before reaching market leadership. |

### Prescience Detail

**Prediction 1:** Preface
- **Claimed:** Aberdeen believes that by the end of the decade most enterprises will be using some form of complex decision support to help develop a better understanding of customers.
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 1:** Enterprise decision support adoption by 2000
- **Result:** Data warehousing and business intelligence became mainstream by late 1990s. Gartner data warehouse market grew substantially; Oracle, Teradata, IBM competed heavily. Most large enterprises had BI/DSS by 2000 validating Aberdeen prediction.
- **Confidence:** verified
- **Notes:** Source: Dataversity history of data warehousing (2023); TROCCO data warehousing history. Prediction confirmed.

**Prediction 2:** Building A Virtual Warehouse
- **Claimed:** Aberdeen believes enterprises will be able to transform many virtually dormant data sources into vital information-delivery vehicles using SmartData technology.
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 2:** *(No matching outcome recorded)*
- **Result:** N/A
- **Confidence:** N/A
- **Notes:** N/A

**Prediction 3:** Executive Summary
- **Claimed:** Aberdeen believes the Virtual Data Warehouse will be sufficiently robust as a solution for departmental warehouse chores and for applications the enterprise considers vital but not necessarily mission critical.
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 3:** *(No matching outcome recorded)*
- **Result:** N/A
- **Confidence:** N/A
- **Notes:** N/A

**Prediction 4:** Executive Summary
- **Claimed:** Aberdeen believes the Virtual Data Warehouse will likely help refine and reduce the footprint of the physical data warehouse.
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 4:** *(No matching outcome recorded)*
- **Result:** N/A
- **Confidence:** N/A
- **Notes:** N/A

**Prediction 5:** Most enterprises using complex decision support by end of decade
- **Claimed:** Aberdeen predicted by end of the decade (by 2000) most enterprises would use some form of complex decision support to develop better understanding of customers
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 5:** Data virtualization vs physical warehouse outcome
- **Result:** Virtual/federated data access gained traction in 2000s as data virtualization (Composite Software, Denodo); physical data warehouses also proliferated. Both approaches coexist. Intersolv was acquired by Micro Focus for $534M in 1998; DataDirect ODBC technology survived as Progress DataDirect. Virtual warehouse concept evolved into data virtualization and later data fabric.
- **Confidence:** verified
- **Notes:** Source: CNET Micro Focus acquires Intersolv (1998); Polytomic data warehouse evolution. Partially correct: concept validated but physical warehouses also proliferated.

**Prediction 6:** Virtual Data Warehouse eliminates need for physical departmental warehouse for some organizations
- **Claimed:** Aberdeen believed metadata-driven Virtual Data Warehouse approach can help some organizations eliminate need for physical departmental data warehouse
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 6:** Intersolv query reporting market position outcome
- **Result:** Intersolv was acquired by Micro Focus for $534M in June 1998 before achieving high-end market leadership. The combined entity was renamed Merant. DataDirect ODBC technology continued; business intelligence market consolidated around Cognos (IBM), Business Objects (SAP), and Microsoft. Intersolv's prediction did not materialize as independent entity.
- **Confidence:** verified
- **Notes:** Source: CNET (1998-06-17); WSJ Micro Focus Intersolv; NYT (1998-06-18). Prediction not confirmed - acquired before reaching predicted position.

**Prediction 7:** Intersolv to occupy high-end query and reporting tool slot
- **Claimed:** Aberdeen predicted rapid re-stratification of query/reporting marketplace making room for Intersolv to occupy high-end query and reporting tool slot
- **Year:** 1995
- **Confidence at time:** medium

**Actual Outcome 7:** *(No matching outcome recorded)*
- **Result:** N/A
- **Confidence:** N/A
- **Notes:** N/A


### Entities Referenced (12 entities)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Intersolv Inc. | vendor | acquired | Acquired by Micro Focus in 1998 for $534M; combined entity renamed Merant; DataDirect product lin... |
| Aberdeen Group | analyst-firm | acquired | Aberdeen Group was acquired by Harte-Hanks in 2001, then by The Aberdeen Group brand was relaunch... |
| TechGnosis International | vendor | acquired | Acquired by Intersolv on October 23, 1995 for approximately $80 million. |
| Cognos Corp. | vendor | acquired | Acquired by IBM in January 2008 for approximately $5 billion; now operates as IBM Cognos. |
| Business Objects | vendor | acquired | Acquired by SAP on January 22, 2008 for approximately $6.8 billion; operates as SAP BusinessObjects. |
| DataDirect Technologies | vendor | active | DataDirect brand survived Intersolv/Merant/Micro Focus transitions; acquired by Progress Software... |
| IBM | vendor | active | IBM remains an active publicly traded technology corporation. |
| Microsoft | vendor | active | Microsoft remains an active publicly traded technology corporation. |
| Apple | vendor | active | Apple Inc. remains an active publicly traded technology corporation. |
| Oracle | vendor | active | Oracle Corporation remains an active publicly traded technology corporation. |
| Micro Focus | vendor | active | Micro Focus merged with HPE Software in 2017; acquired by OpenText in 2023. |
| Progress Software | vendor | active | Progress Software Corporation (Nasdaq: PRGS) remains actively traded. |

### Technologies Referenced (15 technologies)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Virtual Data Warehouse | architecture-pattern | Intersolv | evolved | The virtual data warehouse concept evolved into data virtualization and, more... |
| DataDirect SmartData | software-product | Intersolv / DataDirect | discontinued | Specific SmartData branding discontinued post-merger; metadata management cap... |
| DataDirect Explorer | software-product | Intersolv / DataDirect | discontinued | Explorer desktop product discontinued following Merant restructuring; capabil... |
| DataDirect ODBC Pack | software-product | Intersolv / DataDirect | active | ODBC driver product line continues under Progress DataDirect brand, supportin... |
| DataDirect SequeLink | software-product | TechGnosis / Intersolv | discontinued | SequeLink product was eventually discontinued after Intersolv/Merant transiti... |
| ODBC (Open Database Connectivity) | standard | Microsoft | active | ODBC remains an active and widely supported standard for database connectivit... |
| SQL (Structured Query Language) | standard | ANSI/ISO | active | SQL remains the dominant query language for relational databases; standardize... |
| RDBMS (Relational Database Management System) | category | Multiple | active | RDBMSs remain foundational; augmented by columnar stores (Redshift, BigQuery,... |
| Multidimensional Database | category | Multiple | evolved | Dedicated MDDBs largely replaced by columnar databases with OLAP extensions; ... |
| Metadata Management | practice | Multiple | active | Metadata management has grown in importance; modern data catalogs (Apache Atl... |
| Microsoft OLE 2.0 | standard | Microsoft | legacy | OLE 2.0 succeeded by COM, then .NET, then modern web embedding standards. Sti... |
| IBM DB2 | software-product | IBM | active | IBM Db2 remains an active product; modernized with cloud and containerized de... |
| Cognos Impromptu | software-product | Cognos | discontinued | Cognos Impromptu discontinued after IBM acquisition; capabilities merged into... |
| Business Objects BusinessObjects | software-product | Business Objects | active | BusinessObjects survived acquisition by SAP; continues as SAP BusinessObjects... |
| Business Objects Mercury | software-product | Business Objects | discontinued | Mercury was released but later discontinued; concept of microcubes evolved in... |

### Observation Summary

- Total observations: 51
- By type:
  - actual-outcome: 3
  - expert-opinion: 12
  - market-data: 6
  - technology-assessment: 23
  - viability-prediction: 7
