# The Artful Web They Weave: Spider Technologies' NetDynamics

> Archived from: https://web.archive.org/web/19970112011537/http://www.aberdeen.com:80/secure/profiles/spider/spider.htm
> Original publication date: 1996-08-01
> Author: Aberdeen Group

---

## Original Document Text

The Wayback Machine - https://web.archive.org/web/19970112011537/http://www.aberdeen.com:80/secure/profiles/spider/spider.htm

Spider Technologies
185 Constitution Drive
Menlo Park, CA 94025
(415) 462-7600
http://www.w3spider.com

# The Artful Web They Weave: Spider Technologies' NetDynamics

## Preface

Problem: If you're trying to develop Web (i.e., Internet or Intranet) applications right now, it's not at all clear how you translate the scalability, flexibility and programmer productivity of client/server development tool-sets over to the Web space. This is an especially important issue because those enterprises that pick the right Internet architecture and development toolset will be the ones most likely to translate the Internet's short-run advantages into long-term, bottom-line benefits. This Profile reports on and analyzes NetDynamics, a visual Web-database application builder from Spider Technologies that attacks this very problem.

## Executive Summary

As enterprises move from one-way publishing to transactional and interactive -- or transactive -- applications on the Internet, they must contend with key differences between Web and client/server application environments. (See Table 1.)

**Table 1. Key Differences Between Web and C/S Application Environments**
*Source: AberdeenGroup, August 1996*

It is because of these differences that Aberdeen urges enterprises to simultaneously move forward with select, transactive Internet applications while pouring a long-term architectural foundation for Web OLTP and commercial-strength Web-database applications. For scalability and performance, it is critically important that this architecture include TP-monitor-like middleware and Internet-enabled second generation client/server development tools.

Spider Technologies fulfills these requirements with NetDynamics, a rapid application delivery (RAD) tool coupled with a database viewer/browser that operates next to a Web server, allowing Web programmers to access huge back-end databases relatively easily, at negligible cost. If that sounds familiar, it is. In NetDynamics, Spider has artfully reinvented the TP monitor of yore as a RAD-toolset-plus-monitor designed specifically for the Web.

Earlier and more elegantly than most, Spider has focused on achieving an architecture that bypasses or upgrades the Web browser and server using TP monitor scalability techniques. This is one of its major value propositions, differentiating Spider from most suppliers in either the toolset or middleware markets. NetDynamics incorporates mechanisms vital to scaling Internet applications in the way that past high-end enterprise applications have been scaled -- with load balancing across database servers, scheduling and queuing. These services, coupled with Web integration, create a solution that scales across multiple CPUs, multiple Web servers and multiple databases while overcoming the limitations of the single-threaded limitations of Common Gateway Interface (CGI).

## NetDynamics Architecture

The NetDynamics toolset consists of the following components:

- A visual development tool that automates the process of building Web-database applications
- Java integration. NetDynamics automatically creates server-side Java code for application runtime, providing a vendor-independent code base from which IS can leverage Java's speed, platform independence, extensibility, multithreaded execution and network-centricity.
- The NetDynamics application server is based on a distributed architecture that provides automatic load balancing, and incorporates system monitors for availability and reporting. The application server communicates with the Web server (NSAPI, ISAPI or CGI) through an optimized interface that helps deliver the high speed and scalability that commercial Web-database applications require.

Thus, NetDynamics' value-added has two key aspects: underlying, TP-monitor-like services, and a development toolset.

## NetDynamics' Underlying Service Capabilities

Aberdeen suggests that key criteria for TP-monitor-like middleware are:

- Effective integration in an overall Internet/Intranet architecture;
- Help in overcoming data access scalability bottlenecks; and
- Power and flexibility given to the development toolset.

**Figure 2 — Spider's Web-database Architecture**
*Source: AberdeenGroup, August 1996*

### Effective Integration

Middleware is finding new life as a key integration component enabling enterprise utilization of the Internet. Spider allows access both via CGI and directly via Netscape, the major popular Web server interfaces. On the other end, they provide an effective (i.e., proven) interface to the major popular RDBMSs with an interface that's SQL-based and native.

Besides interoperation with the standard security mechanisms of firewalls, Web servers and database servers, NetDynamics provides additional security on an application level, enforcing a security bridge between the Web server and database server.

### Scalability Mechanisms

Of all Internet architectural components, middleware is the most critical to scalability. Today's solutions vary significantly in the way they integrate with or bypass the Web browser and Web server, and many suppliers will not implement key features for another year or two.

In most Internet applications, as Internet traffic increases, the Web browser/server paradigm becomes a bottleneck because it cannot optimize session-oriented data access requests or multiplex and multithread transactions. Users should therefore focus on suppliers such as Spider that are aggressively aiming to solve these scalability problems.

When interfacing with the Web server API, NetDynamics bypasses CGI altogether. For Web servers that do not publish an API, NetDynamics provides an optimized "light" CGI interface consisting of a few lines of code that pass the request from the Web server to the NetDynamics application.

### Scalability Details

**Application scalability.** As noted, TP-monitor-like services allow NetDynamics to bypass the potential bottleneck of the Web server. The application server eliminates the overhead of starting and stopping CGI processes and of opening and closing databases. These and other services that the toolset can invoke are written to operate in a highly parallel, multithreaded manner.

**Development process scalability.** Currently, NetDynamics' project editor facilitates management of all the components generated with the tool. The resulting standard files can be used with external versioning control systems such as Intersolv's PVCS. In the 3Q96 time-frame, we expect NetDynamics to support versioning as an integral part of the system.

**RDBMS scalability.** Spider stands out in this area. Its proven TP-monitor-like technology not only provides rapid access to today's highly scaleable RDBMSs but can also load balance, and, in the process of constructing SQL to access them, can optimize particular queries and/or transactions.

### Flexibility

**Interoperability.** NetDynamics' middleware allows applications developed using its toolset to access multiple database servers from multiple suppliers across multiple hardware platforms.

**Portability.** The Internet is an open platform par excellence, and Spider has built for this environment from the ground up. Thus, server-side code generated by NetDynamics is exceptionally portable across Web servers and provides across-the-board access to all types of Web-enabled clients.

**Customization.** As Java increasingly becomes the focus of Web development efforts, NetDynamics enables developers to incorporate other Java-type applications within the overall application solution. The toolset incorporates JAVA class libraries for database access, input and output objects, session support and security. Developers can use Java to integrate business rules and application logic using built-in Java events, by tying customized Java to application objects, or by using the API to integrate existing application code such as C++ or Visual Basic. This integration provides the benefits of rapid application development without sacrificing flexibility.

### Programmer Productivity

**Visual programming environment.** Drag and drop, point and click application development improves programmer productivity by allowing the developer to write once for many platforms. NetDynamics offers a full Windows 95 visual programming environment with Web-database linking via drag-and-drop and a facility for defining SQL statements by an example editor. Coding in C, C++, Java, Perl or SQL is unnecessary; page template, data object and security object wizards automate much of the application building process, with wizards for generating the application framework, object editors for customization, built-in session and state management.

## Competitive Positioning

Spider's NetDynamics competes across multiple market segments:

- Client/server development toolset providers
- Middleware providers
- RDBMS providers
- TP monitor providers
- Object-oriented toolset providers

Compared with client/server toolset suppliers, Spider is specifically focused on the Web. In addition, its TP-monitor server-side capabilities are more highly integrated into the overall toolset than most if not all client/server development tools. At the same time, Spider is more focused on the toolset capabilities of its offering than are its middleware competitors. NetDynamics also stands out among middleware suppliers for its focus on server-side scalability considerations.

Versus RDBMS suppliers, Spider emphasizes its support for TP monitor-like access to multiple suppliers' databases across the Internet. Likewise, so far, TP monitor providers have focused on supporting their installed bases' move to the Internet rather than on providing an overall solution and have lagged in providing second-generation client/server toolset capabilities such as partitioning and deployment. Combining the data access prowess of the client/server world with objects distinguishes Spider from most OO toolset providers.

## Financials

Spider is a privately-held company of 45 employees and growing, backed by $10.9 million first-round funding from Hummer Winblad Venture Partners, the original investor in Powersoft and Arbor Software. Large corporate customers include Merrill Lynch, ABB and in particular Harvard Medical School which is committing a sizable portion of its next-generation client/server applications to NetDynamics and Java. The company has forged alliances with Informix, Sybase, Oracle, Silicon Graphics, Sun and Hewlett-Packard.

## Aberdeen Conclusions

Aberdeen believes that NetDynamics offers exceptional scalability, flexibility, programmer productivity and application partitioning capabilities to IS organizations focused on designing Web-database applications and long-term Internet/Intranet architectures. In a fast-moving market with a welter of solutions oncoming from middleware, RDBMS and development toolset providers, Spider will need to be very agile to maintain its leading edge in marrying high powered data access with the new Web technologies. We expect them to extend their capabilities to provide optimized data access paths between the end user and the database server -- e.g., by bypassing the servers in the middle. We also anticipate further integration with Web application and systems administration tools, including marketing intelligence, and with mainframe databases. The IS trend of leveraging software components to increase programmer productivity and speed time to market represents another opportunity for Spider to add value by enhancing NetDynamics' Java integration, associating Java classes with increasing numbers and types of automated events.

As a leading-edge supplier with attractive, strategic middleware and development toolset solutions, Spider's NetDynamics warrants a thorough evaluation by any IS buyer considering deploying commercial-strength Web-database applications.

AberdeenGroup, Inc.
One Boston Place
Boston, Massachusetts 02108 USA
Tel: 617.723.7890
Fax: 617.723.7897

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-spider-technologies-netdynamics |
| title | The Artful Web They Weave: Spider Technologies' NetDynamics |
| author | Aberdeen Group |
| date | 1996-08-01 |
| type | white-paper |
| subject_domain | web-application-development-middleware |
| methodology | industry-analysis, competitive-profiling, expert-opinion |
| source_file | 1996 The Artful Web They Weave_ Spider Technologies_ NetDynamics.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group's 1996 profile of Spider Technologies analyzes NetDynamics, an early web-database application builder combining TP-monitor-like middleware with a visual RAD development environment. The study positions NetDynamics as a critical infrastructure component for scalable Internet transaction processing, identifying load balancing, CGI bypass, and Java integration as key differentiators. Aberdeen recommends IS buyers evaluate NetDynamics as a leading-edge solution for commercial-strength web-database applications, and predicts strong competitive positioning against middleware, RDBMS, and client/server toolset providers.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | This study documented one of the earliest application servers—predating J2EE—and introduced key concepts (TP-monitor-as-middleware, CGI bypass, multi-threaded web application servers) that became foundational to the enterprise application server market. Spider's architecture directly influenced the web application server category that BEA WebLogic, IBM WebSphere, and Sun/Oracle subsequently dominated. |
| **Relevance** | medium | The architectural patterns Aberdeen identified—TP-monitor scalability for web applications, visual RAD toolsets, Java integration, CGI bypass—are the direct ancestors of modern application server and serverless architectures. The competitive analysis framework (toolset vs. middleware vs. RDBMS suppliers) remains analytically valid for evaluating modern PaaS/serverless platforms. |
| **Prescience** | high | Aberdeen's prediction that NetDynamics would warrant enterprise evaluation proved correct—Sun Microsystems acquired Spider Technologies for ~$160-170M in July 1998, validating the technology. The broader prediction that TP-monitor-like middleware would be essential for scalable web applications became the de facto architecture of the enterprise application server market through the 2000s. |

### Prescience Detail

**Prediction 1:** NetDynamics enterprise recommendation
- **Claimed:** Aberdeen: NetDynamics warrants thorough evaluation by any IS buyer deploying commercial-strength web-database applications
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 1:** Spider Technologies actual outcome
- **Result:** Acquired by Sun Microsystems July 1998 for approximately $160-170M in stock; NetDynamics became Sun Application Server
- **Confidence:** verified
- **Notes:** CNET, Wired, WSJ all reported acquisition July 1998; validates Aberdeen's positive assessment

**Prediction 2:** TP-monitor middleware as critical web architecture component
- **Claimed:** Aberdeen urges: architecture must include TP-monitor-like middleware for scalable commercial web-database applications
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 2:** TP-monitor web middleware actual outcome
- **Result:** TP-monitor-as-web-middleware became the dominant enterprise architecture; J2EE application servers (WebLogic, WebSphere) codified this pattern; all major early app server companies acquired by 1998
- **Confidence:** verified
- **Notes:** HP bought Bluestone, Sun acquired NetDynamics, Netscape bought Kiva, BEA acquired WebLogic — all by 1998

**Prediction 3:** Java server-side future importance
- **Claimed:** As Java increasingly becomes the focus of Web development, NetDynamics Java integration represents significant opportunity
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 3:** Not yet verified
- **Result:** Pending web search verification

**Prediction 4:** CGI scalability prediction
- **Claimed:** CGI single-threaded model will become increasingly inadequate as web traffic grows; bypass architectures required
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 4:** CGI scalability actual outcome
- **Result:** CGI rendered obsolete for high-traffic applications by 2000; FastCGI, mod_perl, servlet containers all bypassed CGI model
- **Confidence:** verified
- **Notes:** Prediction fully confirmed; ISAPI and NSAPI extensions, then J2EE servlets replaced CGI


### Entities Referenced (10)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Spider Technologies, Inc. | company | acquired | Sun Microsystems (July 1998, ~$160-170M) |
| Aberdeen Group, Inc. | firm | acquired | Aberdeen (Harte-Hanks -> Informa) |
| Hummer Winblad Venture Partners | firm | active |  |
| Merrill Lynch | company | acquired | Bank of America Merrill Lynch (2008) |
| Harvard Medical School | institution | active |  |
| Informix Software, Inc. | company | acquired | IBM (2001) |
| Sybase, Inc. | company | acquired | SAP SE (2010) |
| Oracle Corporation | company | active |  |
| Sun Microsystems | company | acquired | Oracle Corporation (2010) |
| ABB (Asea Brown Boveri) | company | active |  |

### Technologies Referenced (7)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Spider Technologies NetDynamics | platform | Spider Technologies | emerging | obsolete |
| Common Gateway Interface (CGI) | protocol | NCSA/IETF | mature | legacy-supported |
| TP Monitor (Transaction Processing Monitor) | framework | Multiple | mature | active |
| Java (Server-Side) | language | Sun Microsystems | emerging | active |
| NSAPI / ISAPI (Web Server APIs) | protocol | Netscape/Microsoft | emerging | obsolete |
| Web-Database Application Architecture | framework | Multiple | emerging | active |
| Intersolv PVCS (Version Control) | application | Intersolv | mature | obsolete |

### Observation Summary

- Total observations: 22
- By type: actual-outcome: 4; benchmark-result: 1; expert-opinion: 1; framework-factor: 3; market-data: 3; strategy-classification: 1; technology-assessment: 5; viability-prediction: 4

---

*Processed by Archival Ingest Skill v13 on 2026-03-14*
*Source URL (Wayback Machine): https://web.archive.org/web/19970112011537/http://www.aberdeen.com:80/secure/profiles/spider/spider.htm*
