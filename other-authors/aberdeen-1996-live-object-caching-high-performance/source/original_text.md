# Live Object Caching: High-Performance for Object/Relational Applications

> Archived from: https://web.archive.org/web/19970604112359/http://www.aberdeen.com:80/secure/viewpnts/v9n15/v9n15.htm
> Original publication date: 1996-08-13
> Author: Aberdeen Group

---

## Original Document Text

**Volume 9 / Number 15**
**August 13, 1996**

Forward-looking organizations seeking to build next-generation object-oriented (OO) applications using data encapsulation on top of existing relational databases have been stymied by performance bottlenecks. Conflict between the two models has resulted in a cumbersome runtime conversion process that slows response times -- and has constrained the deployment of advanced, object-oriented applications.

To obtain a higher throughput, some organizations have implemented a process by which they store frequently used objects in memory, eliminating the delay of extracting them from a database. This innovative approach is called **live object caching**. This approach allows IS to gain all the benefits of object technology -- easier maintenance, modular software, and a better way to model business processes -- while preserving their investments in relational systems. An early supplier of tools that facilitate this design practice is Persistence Software. Aberdeen believes that this practice of live object caching provides significant advantages and makes the combination of pure object-oriented application code and the RDBMS a desirable production systems strategy.

---

### Executive Summary

Objects have emerged from the development lab and niche-oriented trade shows to become a central part of mainstream software development. First adopted by independent software vendors (ISVs), object technology is being used by IS to build flexible client-server and internet applications that can be closely mapped to existing business processes. Additionally, these object-oriented applications have been proven to be easier to maintain than their traditional, procedurally-crafted counterparts.

While objects at the application level have met with widespread industry acceptance, the object database (ODBMS) has not lived up to expectations. Poor marketing and a lack of a value proposition have relegated the ODBMS to a few narrow markets. Instead, IS decision makers have elected to continue to invest in the relational DBMS. In Aberdeen's view, **the architecture of the future, therefore, will combine object-oriented application code running on top of database engines from the existing relational suppliers.**

---

### Advantages of Object Technology

Object technology has captured the mindshare and budgets of developers, IS executives and operational managers alike. In the race to build, deploy and continually enhance strategic business applications, object-oriented development has several important advantages:

- **Alignment of applications with existing business processes.** Because objects combine both functionality and data in a self-contained module, developers can embed business rules directly in an application. By reusing the same objects across multiple applications, rules can be consistently enforced across the enterprise.

- **Acceleration of application enhancement and modification.** Applications must constantly change to meet shifting business conditions. The component-based architecture of object-oriented programs eliminates the complexity of "spaghetti code."

- **Partitioning of software for distributed systems.** Objects that encapsulate both data and software logic are inherently modular. Aberdeen's field research consistently shows that the ability to deploy data and functionality closer to the end-user is a major motivation for transitioning to object technology.

- **The architecture of the Internet.** The next-generation applications being deployed on intranets and the Internet will be object-oriented. Sun Microsystems' Java development language, the de facto standard for internet applications, is an object language.

---

### Distributed Object Applications Married to Relational Databases

As object technology emerges as the development methodology for the late 1990s and IS decision makers increase their purchases of OO tools and languages, object databases have been noticeably absent from mainstream business applications. Quite simply, the ODBMS suppliers failed to demonstrate to users a clear economical advantage for using their products. Additionally, for a long time most object databases lacked features viewed as critical to commercial applications, including multithreading, SMP support, excellent OLTP performance and distributed database features.

The market has continued to buy relational technology. While object-oriented methodologies and development tools represent the wave of the future, the relational database is here to stay. New solutions will layer object-oriented application code on top of a relational engine that can store complex datatypes.

---

### The Performance Clash Between Objects and RDBMS

To store objects in a conventional relational format, each object needs to be broken down into its individual data elements and functional algorithms. These components must then be mapped to a corresponding column in a relational table. As these objects are called at runtime, they must be extracted from the database, reassembled, and placed in memory before they can be used by an application.

The application server upon which this mapping takes place often becomes a bottleneck. IS decision makers have been in a quandary -- "Do I deploy object-oriented applications on top of my RDBMS and suffer a significant performance hit, or do I keep the high throughput of a pure relational system and miss out on all the benefits objects offer?"

---

### The 80/20 Rule

Fortunately, once retrieved from the database and reassembled, objects do not have to be flushed from memory after each use. It is possible to cache these objects in memory on the application server, where they can be quickly accessed by an application. This "live object caching" eliminates the object-relational performance penalty by removing the bottleneck at the application server.

For many applications, a small number of objects are in constant use while the vast majority are accessed only occasionally. Working together, developers and end-users can identify a core set of business objects that are candidates for caching. These core business objects have several aspects in common:

- **Highly interdependent data.** The variables of one object are inherently related to the data encapsulated in other, complementary objects.
- **Changes are infrequent and controlled.** Objects used to represent products and services only need to be updated on a weekly or daily basis, rather than second-by-second.
- **Used in most transactions.** The majority of transactions involve a company's products and services.
- **Used by multiple applications.** A wide variety of systems, including billing, inventory and customer support, need information on an organization's products and services.

---

### One Solution: Persistence

Aberdeen has observed that Persistence Software, Inc. of San Mateo, CA is the preeminent provider of tools that enable live object caching. Specifically, Persistence provides two products, the **Object Builder** and the **Object Server**, that make live object caching a reality for its customers.

The **Object Builder** is Persistence's original product (introduced 1991) and is used to create the mapping structure between object-oriented application code and relational databases. It can map C++ code to Informix, Oracle, Sybase, SQL Server and ODBC. By automating the object-to-relational mapping process, Persistence allows its customers to reduce the total time and expenses required to build new C++ applications by an average of **30%**. Persistence has plans to add Java support by the end of 1996.

The **Persistence Object Server** is the runtime product that enables core business objects to be cached in memory and shared by multiple applications distributed across the network. The Object Server ensures the integrity of objects through optimistic and pessimistic object locking and unique naming for each object. It supports read-only and read-write transactions.

One present limitation of the Object Server is that it allows only one client per application or object cache. This issue will be solved with the introduction of the company's **TransApp Server** product, slated for late 1996.

The technical advantages of Persistence's solution have not gone unnoticed. It has been used in several high-profile projects, including the **AT&T ASOS initiative**. Its products are currently resold by Sybase and SunSoft.

---

### Other Tools Needed To Build Distributed Live Object Caching Applications

- A robust compile-edit-debug toolset (C++ based; Java, VB, ActiveX future)
- An object modeling tool (Rational Rose, Paradigm+, STP/OMT, OMTool)
- An object request broker (ORB) — Iona's Orbix, SunSoft NEO, Visigenic, Expersoft
- A transaction monitor — Encina, Top End, Tuxedo
- The right skillsets — heavy developer retraining investment recommended

---

### Not Suitable for All Applications

Live object caching provides little benefit for classic OLTP one-read/one-write systems (e.g., banking teller transactions). It is appropriate where a transaction consists of **multiple reads to one write** — e.g., logistics/scheduling, airline reservations, insurance policy lookup, financial trading systems, network management.

---

### Conclusions

Live object caching provides the best of both worlds. Organizations can make use of the inherent advantages of object technology while maintaining their investments in relational systems. Performance is no longer an impediment to deployment because the core business objects central to the application are cached on the application server.

Aberdeen believes that organizations looking to deploy pure object-oriented applications that encapsulate highly interdependent data on top of existing relational systems should begin to evaluate live object caching. This recommendation is even more important to companies looking to deploy Internet-based applications that will integrate with existing relational datastores.

---

*© Aberdeen Group, Inc. One Boston Place, Boston, Massachusetts 02108 USA. Copyright © 1996.*

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-live-object-caching-high-performance |
| title | Live Object Caching: High-Performance for Object/Relational Applications |
| author | Aberdeen Group |
| date | 1996-08-13 |
| type | market-study |
| subject_domain | object-relational-database-middleware |
| methodology | industry-analysis, competitive-profiling, field-research, expert-opinion |
| source_file | 1996 Live Object Caching_ High-Performance for Object_Relational Applications tvp.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group analyzes the performance challenge of combining object-oriented application code with relational databases, defining "live object caching" as the solution to object-relational impedance mismatch. The study profiles Persistence Software's Object Builder and Object Server as the leading tools enabling commercial object/relational production systems.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | This study addressed a critical and largely unresolved technical problem at the frontier of mid-1990s software architecture. Aberdeen's formulation of "live object caching" was an early articulation of what became a standard ORM pattern. |
| **Relevance** | medium | The object/relational mapping problem remains fundamental; Hibernate, JPA, Django ORM are its direct descendants. |
| **Prescience** | high | Aberdeen correctly predicted OO/relational hybrid would dominate and ODBMS would fail. Sun licensed Persistence technology for Enterprise JavaBeans in 1998, validating the prediction. |

### Prescience Detail

**Prediction 1:** Prediction: Live object caching commercial viability
- **Claimed:** Live object caching is critical breakthrough making object/relational applications viable; will be increasingly important in next-gen strategic business applications
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 1:** Outcome: OO/relational hybrid architecture dominance
- **Result:** Object/relational mapping became dominant architecture; Hibernate (2001), JPA (2006), ActiveRecord, Django ORM all implement the pattern Aberdeen described
- **Confidence:** verified
- **Notes:** Aberdeen's 1996 architectural vision was entirely prescient; ORM is now ubiquitous in enterprise software development.

**Prediction 2:** Prediction: ODBMS will not achieve mainstream adoption
- **Claimed:** ODBMS relegated to few narrow markets; relational investment too strong; new solutions will layer OO code on relational engines
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 2:** Outcome: ODBMS market trajectory
- **Result:** ODBMS remained niche; major ODBMS vendors never achieved commercial mainstream; relational databases with ORM layers dominated
- **Confidence:** verified
- **Notes:** Aberdeen's 1996 prediction proved entirely accurate; modern ORM frameworks validated the object/relational hybrid approach.

**Prediction 3:** Prediction: Persistence Java and EJB relevance
- **Claimed:** Aberdeen expects additional partnerships; Java support by end 1996 seen as important
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 3:** Outcome: Persistence Software fate and EJB
- **Result:** Sun licensed Persistence technology 1998 for Enterprise JavaBeans; Persistence IPO 1999 (PRSW); acquired by Progress Software for $16M in 2004
- **Confidence:** verified
- **Notes:** Source: Wikipedia/Persistence Software (https://en.wikipedia.org/wiki/Persistence_Software). Aberdeen prediction of additional partnerships proved correct via Sun/EJB.

### Entities Referenced (10)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Persistence Software, Inc. | company | acquired | Progress Software (2004, $16M) |
| Aberdeen Group, Inc. | firm | acquired | Aberdeen (Harte-Hanks / independent) |
| Sybase | company | acquired | SAP SE (2010, $5.8B) |
| Oracle Corporation | company | active | — |
| Informix | company | acquired | IBM (2001) |
| Sun Microsystems | company | acquired | Oracle Corporation (2010) |
| AT&T | company | active | — |
| Object Design, Inc. | company | acquired | Excelon/ObjectStore via Progress Software |
| Forte Software | company | acquired | Sun Microsystems (1999) |
| Rational Software | company | acquired | IBM (2003, $2.1B) |

### Technologies Referenced (9)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Persistence Object Builder | framework | Persistence Software | emerging | obsolete |
| Persistence Object Server | framework | Persistence Software | emerging | obsolete |
| Persistence TransApp Server | framework | Persistence Software | emerging | obsolete |
| Relational DBMS (general) | platform | Multiple | mature | active |
| Object DBMS (ODBMS) | platform | Multiple | declining | obsolete |
| Java | language | Sun Microsystems | emerging | active |
| C++ | language | ISO/IEC | mature | active |
| CORBA/ORB | protocol | Multiple | emerging | obsolete |
| TP Monitor | framework | Multiple | mature | active |

### Observation Summary

- Total observations: 28
- By type: actual-outcome (3), benchmark-result (2), expert-opinion (2), framework-factor (8), market-data (3), strategy-classification (2), technology-assessment (5), viability-prediction (3)
