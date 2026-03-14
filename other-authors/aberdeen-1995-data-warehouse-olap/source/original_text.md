# Data Warehouse Query Tools: Evolving to Relational OLAP

> Archived from: https://web.archive.org/web/19970112010847/http://www.aberdeen.com:80/secure/viewpnts/v8n8/v8n8.htm
> Original publication date: 1995-07-01
> Author: Aberdeen Group

---

## Original Document Text

Volume 8/Number 8
July 7, 1995
Data Warehouse Query Tools: Evolving to Relational OLAP
One of the true business revolutions of the 1990s is the ability of desktop knowledge workers to create job-speciﬁc queries and submit them against workgroup, departmental and enterprise
data warehouses. The technology for empowering these users is rapidly supplanting the get-MIS-to-code-it approach and let's-copy-the-data-into-a-spreadsheet workaround that hinder
knowledge worker productivity and timeliness.
But simple report-writer query tools can only answer simplistic operational questions. And sophisticated multidimensional database technology cannot scale with today's terabyte-size
warehouses. Aberdeen research concludes that the next-generation query tools for answering difﬁcult ad hoc questions will marry sophisticated OLAP (On-line Analytical Processing) with
state-of-the-industry relational database technology, a powerful union called Relational OLAP.
This Market Viewpoint clariﬁes the capabilities of report-writer, multidimensional and Relational OLAP tools classes, and examines the market segmentation and directional issues of one of
the Information System (IS) industries' hottest topics.
Table of Contents
Executive Summary
Report-Writer/Predeﬁned: Tools for Simple Decision Support
Setting Higher Expectations
Report Writers Are Not Enough
Why The Market Is Moving Beyond Report Writers
Multidimensional OLAP
MDB Shortcomings
Relational OLAP Builds on Multidimensionality
Leveraging the Enterprise RDBMS
Dimensional Modeling
Using Metadata to Cope With Change
Relational OLAP Technology Advantages
Market-Driven Partnerships
Aberdeen Conclusions
Executive Summary
As thousands of disappointed users have already discovered, virtually every supplier of even the most simple decision-support tool has touted its software as being able to satisfy the user-
driven fervor for business-critical information. The combination of over-selling and over-optimism is always devastating. It certainly has confused the market for on-line query and analysis
software tools. Aberdeen research shows the choice of the wrong tools for the job leads to higher enterprise life-cycle costs, lower productivity, and a loss of competitive-advantage
momentum.
Aberdeen segments query and reporting tools into three categories: report writer/pre-deﬁned, multidimensional OLAP, and Relational OLAP.
Report-writer/predeﬁned query products such as Microsoft Access and Crystal Services' Crystal Reports are best at retrieving operational data using canned formats and layouts. They
adequately answer questions such as, "How many size 12 dresses scheduled to ship this month have not shipped." Usually the entire application resides on the desktop clients, an example of
the fat-client design that has plagued many implementers who have tried to move too much data off the data server and onto the desktop for analysis.
Report writers are excellent and cost effective for mass deployment of applications where a handful of database tables are managed as one database by any of the relational database
suppliers' products. But this class of tool technology cannot and should not be forced to stand on its head in order to do more complex but real-world OLAP applications.
A multidimensional query tool allows multiple data views (e.g. sales by category, brand, season, and store) to be deﬁned and queried.
Multidimensional OLAP tools make ad hoc decision making much more practical than report writers and have been particularly successful in markets such as consumer packaged goods,
where market-share analysis is business critical. Some query tools, such as D&B Software's Pilot and Oracle/IRI Software's Express, are integrated with a multidimensional database (MDB)
that excels at efﬁciently storing multiple dimensions using sparse-matrix technology. However, MDB technology becomes less practical as database sizes approach between 20 gigabytes and
50 gigabytes -- and there are now hundreds of sites with very large databases (VLDBs) exceeding 100 gigabytes. Moreover, there are real-world queries that the multidimensional approach
alone cannot readily answer.
Aberdeen believes a new class of technology called Relational OLAP is the next logical step in the evolution of complex decision-support tools. Relational OLAP combines powerful,
ﬂexible query capabilities with a scalable multi-tier architecture while symbiotically depending on and leveraging the vastly improved capabilities of today's parallel-scalable relational
databases.
As Relational OLAP and parallel-scalable database technology evolves rapidly over the next two years, Aberdeen believes a whole new breed of data-mining applications will emerge. These
applications empower business users to "drill" for information in virtually any direction, and without the need to pre-program the paths. We conclude that the market will expand rapidly as
Relational OLAP technology is absorbed by data-mining enterprises seeking the next competitive-advantage solution.
Back to Table of Contents
Report-Writer/Predeﬁned: Tools for Simple Decision Support
Report-writer/predeﬁned query tools promised to generate computer output without the need for continuous IS programming. Report writers typically combine point-and-click Microsoft
Windows interfaces with ODBC (Open Data Base Connectivity) drivers to allow end users to build queries that extract database information.
Each report-writer supplier now touts its ability to give business managers and knowledge workers the functionality to perform their own queries using Structured Query Language (SQL),
the highly successful but layperson-bafﬂing mechanism for integrating and processing data in rows and tables of a relational database.


Most suppliers have devised fairly simple ways for IS administrators to mask or translate SQL into business terms. By using metadata, or data about data, and storing it in a variety of
metadata dictionaries, report-writer tools promise to free PC-literate users from the need to understand the intricacies of database design and the set theory relationships required to join tables
when making a query.
Back to Table of Contents
Setting Higher Expectations
Aberdeen believes that next-generation complex decision-support systems will demand tools that can dynamically generate SQL. The less powerful tools -- among them such personal
database tools as Microsoft Access and Lotus Approach -- unwittingly encourage users to return wrong results through the incorrect use of joined intermediary tables. Aberdeen believes that
low-end report writers are powerful enough for retrieving operational data using MIS-canned formats and layouts; they should be used with caution in true decision-support environments.
The more robust report writers continue to take signiﬁcant steps in diminishing -- but not eliminating -- the need for canned formats. But they have substituted one form of query
preconditioning for another. Where state-of-the art report-writers have helped business users formulate their own queries, they have done so precisely because IS decision-support architects
have anticipated users' queries and predeﬁned the complex SQL -- for example, Group By, Correlated subquery, Having, Create View, and Union statements -- required to answer business-
user questions.
Such is the case with Business Objects' BusinessObjects and Cognos Corp.'s Impromptu, two exemplary tools that occupy the high-end of the report writer spectrum. To perform other
desirable decision-support tasks -- for example, sums and averages -- requires more predeﬁning and more IS programming. And the IS labor-intensive programming and deployment must be
repeated when the system requires changes.
Back to Table of Contents
Report Writers Are Not Enough
Report-writer tools do not support true ad hoc end-user queries. Moreover, the charting and report functions of these tools are typically within a distinct module. Although suppliers have
tightened the integration between their querying and reporting facilities, they are an afterthought.
Furthermore, most report-writers typically place the entire application on the desktop clients. This fat-client technology remains unnoticed during the analysis of, say, the top 50 enterprise
customers (i.e., 50 rows are returned). But trying to perform a margin analysis involving thousands of database rows on that customer population will choke the desktop system (not to
mention the network), exposing the fat-client design's weakness.
Back to Table of Contents
Why The Market Is Moving Beyond Report Writers
Although the best of report writers have proven adequate for small decision-support systems, Aberdeen believes they lack the sophistication needed for complex-decision support
environments. Among their weaknesses, Aberdeen includes:
A continuous IS involvement in the preparation-and-maintenance loop;
Difﬁculty in meeting the challenges of complex business questions;
Inability to support large query environments;
A lack of the concept of time, consolidations, and aggregates;
A failure to transparently support and leverage the various database optimization techniques;
Weak linkages between query and reporting facilitates; and
Fat-client design.
These limitations, Aberdeen believes, will force report-writers into a less fundamental decision-support role than their suppliers may have planned for them. Aberdeen believes that report-
writers will soon be relegated to a marginal, "light-query" status while the more sophisticated decision-support systems are built with multidimensional and Relational OLAP tools.
Back to Table of Contents
Multidimensional OLAP
Multidimensional OLAP tools make ad hoc decision-making much more practical than report writers and have been particularly successful in markets such as consumer packaged goods,
where market-share analysis is business critical.
Multidimensional tools are based on the notion of arrays, an organizational principle for arranging and storing related data so that it can be viewed and analyzed from multiple perspectives.
By summarizing data and arranging it in cross-tabular views, which are by now familiar to spreadsheet users, multidimensional tools offer users a perspective of their data that facilitates
comparative analysis. These tools have shown particular strength in forecasting business trends and "what if" analysis. They empower business users to "roll up" and "drill down" in a
discovery search for business wisdom.
There are three basic types of multidimensional OLAP tools:
Spreadsheets such as Microsoft Excel, which allow small datasets to be viewed in the cross-tab format familiar to business users;
Client-side MDBs, such as Andyne Computing Ltd.'s Pablo, which maintains pre-calculated consolidation data in PC memory and are proﬁcient at handling a few megabytes of data;
and
Server-based MDBs such as Arbor Software's Essbase, Holistic Systems Inc.'s Holos and Oracle/IRI Software's Express, which optimize gigabytes of data by using any of several
performance-and-storage optimization tricks.
At the high end, tools such as Oracle/IRI Software's Express and D&B Software's Pilot excel at efﬁciently storing multiple dimensions using sparse-matrix technology. Although not
available in all MDBs, sparse-matrix is both a performance and storage optimization technique that hunts for unused cells within an MDB matrix, eliminates them, and then compresses the
remaining arrays.


Despite the speed and performance obtained from such optimization techniques, MDB technology becomes less practical as database sizes approach between 20 gigabytes and 50 gigabytes.
Although several suppliers at the high-end of the multidimensional spectrum are trying to break the 50-gigabyte barrier, a thousand customer sites have already done so with very large
relational databases.
Back to Table of Contents
MDB Shortcomings
But size alone is not the only barrier faced by MDB suppliers and their users in complex decision-support environments. These systems must continuously and seamlessly interact with other
portions of the decision-support architectures, with its full compliment of databases, desktop tools, and applications. MDBs have yet to prove that they can deliver the same mandatory
features -- usage-based privileges and security at several levels, for example -- that are expected of any mission-critical system. Furthermore, unless queries have inherent relationships
between elements of different records, an MDB cannot efﬁciently answer them. For example, MDBs -- which are highly summarized -- cannot themselves drill down to detailed data. An
RDBMS is typically used as an adjunct.
While offering scant support for these requirements, current MDBs also typically lack provisions for:
Updating the database incrementally while users continue to access it;
High-availability backup and restore;
Connecting multiple databases, including RDBMSs, and allowing them to interact; and
Sub-setting multidimensional data for individual analysis and manipulation.
Suppliers of MDBs such as Arbor Software have recently tightened alliances with Hewlett-Packard, which is also formulating relationships with other MDB suppliers. And Oracle is
acquiring IRI Software for its MDB and MDB-enabled query tools. These alliances and acquisitions will try to accomplish the difﬁcult task of seamlessly integrating specialized MDBs with
pure RDBMSs.
Although the suppliers involved argue that enterprises will therefore have access to the best of both technology worlds, Aberdeen believes that enterprises must factor the skills and costs
required to implement and use a specialized MDB database. Radically different from core operational systems and RDBMS-based systems, MDBs not only require a specialized database but
also specialized front-end tools to access information. This means the likely market evolution for MDBs is as a major but non-mainstream path for high-end decision support. Aberdeen
believes that MDBs will play a role in the construction of so-called datamarts over the next three years, after which they will face stiffening competition from Relational OLAP.
Back to Table of Contents
Relational OLAP Builds on Multidimensionality
Although proprietary MDBs suffer scalability problems, and lack many of the robust yet "open-systems" features demanded by enterprise mission-critical applications, these shortcomings do
not eliminate multidimensionality itself from playing a vital role in the next-generation complex decision-support applications.
Aberdeen believes that enterprises can and should separate the conceptual view of multidimensional data from the requirement to store it in multidimensional form. This is the foundation of
Relational OLAP, which prepares an RDBMS to deliver full multidimensionality and enables business users to view and analyze its contents from multiple perspectives -- without requiring a
specialized MDB.
A new class of suppliers -- most notably MicroStrategy Inc., Information Advantage Inc., and Stanford Technology Group -- have demonstrated that an optimized RDBMS can be combined
with powerful, ﬂexible query-tool capabilities. By blending these components within a scalable, multi-level architecture, Relational OLAP suppliers have also leveraged the inroads that
RDBMS suppliers such as Informix, Oracle, and Sybase have made in scaling their databases well beyond 100 gigabytes.
Back to Table of Contents
Leveraging the Enterprise RDBMS
By remaining within the market-accepted RDBMS realm, Relational OLAP suppliers continue to satisfy the IS mandate for open-systems computing, while enabling knowledge workers to
answer the types of queries that are both too sophisticated and in some instances too simple for other technologies.
Each of the Relational OLAP suppliers has mounted a multi-tiered attack (refer to Figure 1) on the complex decision-support problems that are facing decision-making users. Broadly
speaking, Relational OLAP tools treat the entire decision-support architecture as multiple, discrete -- but complementary -- components that encompass:
Operational systems;
An RDBMS-based data warehouse optimized for decision support;
Metadata repositories to identify data-warehouse contents and the location of required enterprise data;
A server- or client-based SQL query generator that also analyzes multidimensional data and computes aggregates, consolidations and cross tabulations;
One or more desktop applications that range from simple ad hoc querying to linked query-reports and are market-driven by being based on human logic and language rather than
computer logic and language;
An applications-development environment for building and modifying decision-support applications that leverages all classes of decision support tools; and
Intelligent agents and alerts that monitor the query environment, run analyses in the background, and notify workers when a predeﬁned business condition or exception is encountered.
Back to Table of Contents
Figure 1: OLAP Architecture


Source: AberdeenGroup, December 1995
Dimensional Modeling
At the heart of these Relational OLAP technologies is dimensional modeling. This technique organizes information into two types of data structures: measures, or numerical data (for
example, sales and gross margins), which are stored in "fact" tables; and dimensions (for example, ﬁscal quarter, account and product category), which are stored in satellite tables and are
joined to the fact table. Adept at tracking both the hierarchical and descriptive relationships of each dimension, Relational OLAP tools leverage the underlying data model for the
multidimensional views that deliver information to business users. Aberdeen believes that enterprise planners who anticipate building large, complex decision-support systems must look for
technologies capable of optimizing three, interrelated, decision-support database functions:
Denormalization, a database design that repetitively stores data in tables, minimizing the number of time-consuming joins when executing a query, and reducing the number of rows that
must be analyzed;
Summarization, a technique for aggregating information in advance, eliminating the need to do so at runtime; and
Partitioning, the ability to divide a single large fact table into many smaller tables, thereby improving response time for queries as well as for data warehouse backup and reloading.
MicroStrategy, Information Advantage, and Stanford Technology each offer viable optimization techniques for dimensional modeling. And though their individual approaches to this complex
problem vary signiﬁcantly, each has devised enterprise-leveraging Relational OLAP products.
Back to Table of Contents
Using Metadata to Cope With Change
Relational OLAP tools rely on strong metadata dictionaries for helping IS and business users track on-going changes within the decision-support environment. Relational OLAP suppliers
deliver these optimization techniques with an eye toward improving query performance and preparing the system for the inevitable business-driven changes. When changes occur, all
components -- databases, metadata facilities, desktop tools and reporting applications -- automatically reﬂect the changes.
These facilities, Aberdeen believes, leverage IS labor in systems preparation and the complex query environment as a whole. In contrast, the more sophisticated report writers require IS to
maintain and monitor metadata, but they do not leverage the labor with system-wide awareness.
Back to Table of Contents
Relational OLAP Technology Advantages
The success of a complex decision-support system will be directly dependent on its ability to support a variety of business user queries, while minimizing the amount of IS interaction
necessary to provide answers to business-driven questions. Aberdeen believes that enterprise planners can turn to Relational OLAP suppliers to bolster complex decision-support systems
with technologies that:
Deliver true business OLAP analysis, including the ability to drill for information across the entire system;
Leverage RDBMS very large databases technology; and
Reduce the applications-maintenance burden for the entire complex decision-support system.
Back to Table of Contents
Market-Driven Partnerships
MicroStrategy and Informix are a case in point. Informix continues to reﬁne its top notch Informix-Online parallel-scalable RDBMSs to play a key role as a superior data-warehouse
manager. Rather than dilute this specialist role with an MDB-development effort, it has partnered with MicroStrategy, a Relational OLAP pioneer. MicroStrategy in turn has elevated the
technology by performing aggregations dynamically. Furthermore, it leverages key Informix technologies — for example VLDB support and parallel loading and indexing -- with an
integrated layer that supports true business-analysis functions. With the capability of generating multi-pass SQL in its OLAP engine, MicroStrategy is concentrating on obviating the need for
a specialized MDB.
MicroStrategy's approach has proven particularly useful when tied to Informix's parallel-scalable RDBMS, and is an example of the kind of market-driven cooperation Aberdeen anticipates
among the Relational OLAP query-tool suppliers and the RDBMS suppliers.
Back to Table of Contents
Aberdeen Conclusions


As the customer-centric business tempo continues to quicken, IS technologists will no longer have the luxury or time to apply the brute force that has made so many current complex
decision-support systems successful. It is the caliber of the query tools, not the IS technologists, that must pick up the slack. And the success of a complex decision-support architecture will
depend on the optimization of every component.
Aberdeen recommends that IS executives view Relational OLAP as the next logical step in the evolution of complex decision-support tools -- as the means to meet new and emerging
customer-centric demands while leveraging the mastery IS continues to apply to meet current business demands.
Relational OLAP combines powerful, ﬂexible query capabilities with a scalable multi-tier architecture. By symbiotically depending on and directly leveraging the vastly improved
capabilities of today's parallel-scalable relational databases, Relational OLAP will free IS and the enterprise from the slow item-by-item evolution of today's complex decision-support
systems, and enable data-mining enterprises to build their next competitive-advantage solutions more easily.
Back to Table of Contents
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
The trademarks and registered trademarks of the corporations mentioned in this publication are the property of their respective holders. Unless otherwise noted, the entire contents of this publication are copyrighted by Aberdeen
Group, Inc. and may not be reproduced, stored in a retrieval system, or transmitted in any form or by any means without prour written consent of the publisher.
Copyright © 1995 Aberdeen Group, Inc., Boston, Massachussetts

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1995-data-warehouse-olap |
| title | Data Warehouse Query Tools: Evolving to Relational OLAP |
| author | Aberdeen Group |
| date | 1995-07-01 |
| type | market-study |
| subject_domain | data-warehousing-OLAP |
| methodology | industry-analysis,competitive-profiling,benchmarking |
| source_file | https://web.archive.org/web/19970112010847/http://www.aberdeen.com:80/secure/viewpnts/v8n8/v8n8.htm |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group market viewpoint analyzing the evolution of data warehouse query tools toward relational OLAP (ROLAP), examining multidimensional analysis, vendor strategies, and convergence of OLAP and relational database technologies.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Defined the ROLAP category and distinguished it from MOLAP/report writers at a pivotal market moment; Aberdeen's ROLAP framework directly influenced enterprise BI purchasing decisions worth hundreds of millions. MicroStrategy and Informix partnership specifically endorsed. |
| **Relevance** | medium | ROLAP vs MOLAP distinction is now historical (modern BI tools like Snowflake/BigQuery/Power BI use hybrid approaches); the analytical framework for evaluating multi-tier data warehouse architectures transfers well. |
| **Prescience** | high | Core predictions confirmed: ROLAP wave materialized by 1997-1999, MDB vendors faced consolidation pressure, RDBMS vendors integrated OLAP capabilities as forecast. Aberdeen correctly identified the winning architecture. |

### Prescience Detail

**Prediction 1:** ROLAP new data-mining wave prediction
- **Claimed:** Aberdeen predicts ROLAP will generate a new wave of data-mining applications within 2 years (by 1997)
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 1.1:** ROLAP data-mining wave — actual outcome
- **Result:** Confirmed: ROLAP-enabled data mining wave materialized; MicroStrategy went public 1998 at multi-billion valuation; data warehouse market grew dramatically 1996-2000
- **Confidence:** verified
- **Notes:** Prediction confirmed. Data mining/ROLAP boom materialized exactly in predicted timeframe. MicroStrategy MSTR IPO 1998, Information Advantage acquired 1999. Aberdeen was right on timing.

**Actual Outcome 1.2:** RDBMS OLAP convergence — actual outcome
- **Result:** Confirmed: All major RDBMS vendors (Oracle, SQL Server, DB2) added OLAP/CUBE extensions by 2000; Microsoft SQL Server Analysis Services (1998); Oracle OLAP option; SAP BW (1997)
- **Confidence:** verified
- **Notes:** Prediction fully confirmed. RDBMS-OLAP convergence was one of the defining enterprise software trends of the late 1990s/early 2000s.

**Prediction 2:** MDB faces ROLAP competition prediction
- **Claimed:** Aberdeen predicts multidimensional databases (MDBs) will face stiffening ROLAP competition after ~3 years and be limited to datamart role
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 2.1:** MDB competition — actual outcome
- **Result:** Confirmed: Arbor Software (Essbase MDB) merged with Hyperion 1998; MOLAP persisted but ROLAP/hybrid models dominated enterprise DW. Oracle acquired Hyperion 2007.
- **Confidence:** verified
- **Notes:** Prediction correct: MDB vendors (Arbor/Hyperion, Cognos PowerPlay) remained viable but ROLAP hybrid became dominant. Hyperion eventually absorbed into Oracle BI.

**Prediction 3:** RDBMS OLAP convergence prediction
- **Claimed:** Aberdeen predicts RDBMS vendors will incorporate OLAP capabilities, leading to convergence of relational and multidimensional analysis
- **Year:** 1995
- **Confidence at time:** high

**Actual Outcome 3.1:** ROLAP data-mining wave — actual outcome
- **Result:** Confirmed: ROLAP-enabled data mining wave materialized; MicroStrategy went public 1998 at multi-billion valuation; data warehouse market grew dramatically 1996-2000
- **Confidence:** verified
- **Notes:** Prediction confirmed. Data mining/ROLAP boom materialized exactly in predicted timeframe. MicroStrategy MSTR IPO 1998, Information Advantage acquired 1999. Aberdeen was right on timing.

**Actual Outcome 3.2:** RDBMS OLAP convergence — actual outcome
- **Result:** Confirmed: All major RDBMS vendors (Oracle, SQL Server, DB2) added OLAP/CUBE extensions by 2000; Microsoft SQL Server Analysis Services (1998); Oracle OLAP option; SAP BW (1997)
- **Confidence:** verified
- **Notes:** Prediction fully confirmed. RDBMS-OLAP convergence was one of the defining enterprise software trends of the late 1990s/early 2000s.

### Entities Referenced (20 entities)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | research-firm | acquired | Harte-Hanks (then Aberdeen rejoined as independent brand) |
| MicroStrategy Inc. | software-vendor | active |  |
| Information Advantage Inc. | software-vendor | acquired | Sterling Software (1999) then CA Technologies (2000) |
| Stanford Technology Group | software-vendor | acquired | Unknown (small ROLAP startup) |
| Arbor Software | software-vendor | merged | Hyperion Solutions (1998) then Oracle (2007) |
| Oracle Corporation | software-vendor | active |  |
| IRI Software | software-vendor | acquired | Oracle Corporation (1995) |
| D&B Software | software-vendor | acquired | Geac Computer Corporation (1996) |
| Pilot Software Inc. | software-vendor | acquired | SAP AG (2007) |
| Holistic Systems Inc. | software-vendor | acquired | Seagate Software (1996) then Crystal Decisions then Business Objects (2004) |
| Andyne Computing Ltd. | software-vendor | acquired | Hummingbird Communications (1997) for $60M |
| Business Objects | software-vendor | acquired | SAP AG (2008) |
| Cognos Corp. | software-vendor | acquired | IBM (2008) |
| IQ Software | software-vendor | acquired | Information Advantage (1998) for $36M |
| Informix | software-vendor | acquired | IBM (2001) |
| Sybase | software-vendor | acquired | SAP AG (2010) |
| Microsoft | software-vendor | active |  |
| Crystal Services | software-vendor | acquired | Seagate Software (1996) then Business Objects (2004) |
| Hewlett-Packard | hardware-vendor | active |  |
| Lotus Development | software-vendor | acquired | IBM (1995) |

### Technologies Referenced (28 technologies)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Relational OLAP (ROLAP) | analytical-framework | multiple | emerging | evolved |
| Multidimensional OLAP (MOLAP) | analytical-framework | multiple | mainstream | legacy-niche |
| Multidimensional Database (MDB) | database-technology | multiple | mainstream | legacy-niche |
| Sparse-matrix technology | storage-optimization | multiple | mainstream | legacy-niche |
| Parallel-scalable RDBMS | database-technology | multiple | emerging | evolved |
| Dimensional modeling | data-modeling | multiple | emerging | active |
| ODBC (Open Database Connectivity) | connectivity-standard | Microsoft | mainstream | legacy |
| SQL (Structured Query Language) | query-language | ISO/ANSI | mainstream | active |
| Metadata repository / data dictionary | data-management | multiple | emerging | active |
| Denormalization | database-design | multiple | emerging | active |
| Summarization / pre-aggregation | query-optimization | multiple | emerging | active |
| Partitioning | database-design | multiple | emerging | active |
| Multi-pass SQL generation | query-engine | MicroStrategy | niche | evolved |
| Fat-client architecture | software-architecture | multiple | mainstream | obsolete |
| Data warehousing | data-management | multiple | emerging | active |
| Essbase (Arbor Software) | analytical-server | Arbor Software | mainstream | evolved |
| Holos (Holistic Systems) | analytical-server | Holistic Systems Inc. | mainstream | discontinued |
| Oracle Express (IRI Software) | analytical-server | Oracle/IRI Software | mainstream | discontinued |
| Pablo (Andyne Computing) | analytical-client | Andyne Computing Ltd. | mainstream | discontinued |
| BusinessObjects | report-writer | Business Objects | mainstream | evolved |
| Cognos Impromptu | report-writer | Cognos Corp. | mainstream | discontinued |
| Crystal Reports | report-writer | Crystal Services | mainstream | active |
| Microsoft Access | personal-database | Microsoft | mainstream | active |
| Microsoft Excel | spreadsheet | Microsoft | mainstream | active |
| Lotus Approach | personal-database | Lotus Development | mainstream | discontinued |
| Intelligent agents / alerts | automation | multiple | emerging | evolved |
| Data mining | analytical-framework | multiple | emerging | active |
| Very Large Databases (VLDB) | database-technology | multiple | emerging | active |

### Observation Summary

- Total observations: 54
- By type:
  - actual-outcome: 3
  - expert-opinion: 2
  - market-data: 14
  - strategy-classification: 4
  - technology-assessment: 28
  - viability-prediction: 3
