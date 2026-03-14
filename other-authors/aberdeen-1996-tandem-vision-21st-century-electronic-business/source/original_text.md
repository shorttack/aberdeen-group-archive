# Tandem's Vision, Architecture, and First Products For 21st Century Electronic Business

> Archived from: https://web.archive.org/web/19970604103613/http://www.aberdeen.com:80/secure/profiles/tandem/tandem30.htm
> Original publication date: 1996-01-01
> Author: Aberdeen Group

---

## Original Document Text

The Wayback Machine - https://web.archive.org/web/19970604103613/http://www.aberdeen.com:80/secure/profiles/tandem/tandem30.htm

Tandem Computers Inc.
19191 Vallco Parkway, LOC 4-40
Cupertino, CA. 95014-2525
(408) 285-6000

# Tandem's Vision, Architecture, and First Products For 21st Century Electronic Business

## Executive Summary

As enterprises begin to absorb both the technology and the promises of the Worldwide Web, they should anticipate dramatic changes to many of their core processes and the need for computing architectures specifically designed to thrive when handling the twenty-first Century I/O loads in distributed and parallel processing.

Many on-line transaction processing (OLTP) applications, for example, will soon exhibit a high-bandwidth, resource-intensive blend of transaction processing called ITP, or Internet transaction processing. Various forms of Web-leveraging electronic commerce and Internet- and Intranet-enabled applications will require IS to weave in still-to-be-determined mixtures of voice, video, text and data with conventional OLTP. The days of 100 character transactions are over.

Aberdeen believes that this sea change will create forces that will overwhelm current I/O-limited computing systems and will therefore demand an architecture exceptionally adept at handling numerous, simultaneous, low-latency data transfers for both inter-processor and I/O communications, and at dynamically adjusting network bandwidth in response to fluctuations in "media rich" data traffic.

In other words, Tandem Computers' ServerNet is a pioneering system area network (SAN) and interconnection layer that now provides common hardware and software to processors and I/O nodes in Tandem's highly-parallel, benchmark-winning, systems. ServerNet is also being used to create today's hottest price-performing Intel Pentium Pro technologies and Microsoft NT clusters.

This Profile introduces the new ServerNet-driven Tandem Computers, its vision for electronic commerce and Web-related challenges, and its first set of powerful and proven ServerNet-enabled technologies, including its ServerWare project that will bring a rich portfolio of software — database and transaction processing middleware — from Himalaya to Windows NT Server. ServerWare will enable enterprises to prepare for and manage the "discontinuous performance leaps" demanded by trailblazing ITP applications.

## Internet Electronic Commerce Applications Will Benefit From ITP

Streamlining business processes has long been the goal of electronic commerce initiatives — ITP applications will make it possible. For example, by building a customer data warehouse, marketing executives will better target customers and tailor media- and data-rich content to individual users thus scaling down inefficient direct mail campaigns. For customers and prospects, ITP applications will bring better service and data access and for companies it will translate to more efficient, cost-effective operations — and greater customer satisfaction levels.

Aberdeen research has shown that the first generation of home-grown Internet solutions scaled poorly as eager companies patched together data warehousing, online transaction processing, databases and media content. These early explorers have learned that ITP software is highly complex, generally costs over $1 million to build and is not easily managed. To make matters worse, expanding Internet bandwidth and a rapidly growing Internet usership will further stress first-generation ITP applications and push the limits of conventional server I/O.

## Enabling ITP

Tandem's vision is to solve all of the major obstacles of ITP adoption including I/O bottlenecks, high-volume on-line transaction processing (OLTP), and architectural flexibility. Aberdeen believes Tandem's ServerNet enabled S-Series is well equipped for future high-volume fault-tolerant OLTP with scalability of an order of magnitude greater than any other server. Tandem's products have a proven OLTP track record and today account for:

- 70% of the world's money (US $2 trillion/day) transactions;
- 66% of all ATM and credit card transactions;
- 90% of the world's stock exchange transactions; and,
- 50% of all public e-mail transactions.

## Bringing Technology To The Vision

Nearly two years have passed since Tandem Computers exhibited a combination of industry leadership and prescience with the visionary introduction of ServerNet, a powerful system area network that has been specifically architected to respond to the 21st century I/O loads that will typically confront distributed and parallel processing.

Leveraging its deep institutional experience in parallel processing, Tandem constructed the interconnection software with a theoretical data-connection bandwidth of 150 terabytes per second, and designed it to be an integral part of just about any parallel-scaleable technology, whether shared memory, clustered, shared device, or shared nothing, and whether for its own systems or those of its allies and competitors.

Fast, powerful, and flexible, ServerNet delivers breakthroughs in the five key areas that the new breed of applications will require:

- Scalability, by logically and physically decoupling the processors from I/O devices, enabling systems to scale to thousands of processors and millions of device connections;
- Any-to-any direct connections, allowing data to flow directly from processor to processor, from processor to device, or from device to device, thus avoiding hardware and software bottlenecks, and shortening data paths, reducing the number of trips data makes within the systems, conserving memory bandwidth and reducing CPU cycles;
- Topology flexibility, by allowing ServerNet data routers to be configured in hypercubes, meshes and trees;
- Reliability, with fault tolerance and self-checking inherent to the ServerNet architecture; and
- Low latency, delivering fast I/O turnaround, which keeps the I/O highway running quickly and smoothly and delivers the bottom-line beneﬁt of quicker transaction response times.

## ServerNet and ITP

ServerNet's any-to-any direct connections will allow large video, data warehousing queries, and other large data objects to pass directly from Tandem's highly paralleled NonStop SQL to the network — avoiding I/O congestion and freeing up memory and CPU cycles. ServerNet's improved handling of heterogeneous data types will facilitate end-user interaction, and ITP in general, by improving database access, custom content and a highly visual commercial environment.

With ServerNet already incorporated in the company's hardware-redundant Integrity systems running Unix, and thus stress-tested and proven against real-world applications, ServerNet is now working in concert with the advanced parallel processing techniques in Tandem's newest high-end Himalaya servers. Starting with the delivery this quarter of the (ServerNet) S7000, which is built on the MIPS 4400 chip, Tandem will deliver its biggest performance punch with the S70000 in the first quarter of 1997. Based on the MIPS R10000 chip, the S70000 distributed-memory, multiprocessing NonStop Himalaya system will double the performance of its predecessor, the K20000, and slice costs by half — a proof point that the leaner, ServerNet-enriched company can deliver on its technological vision without losing focus on competitive demands for better price/performance.

Further enticements include stronger reliability and serviceability, ServerNet's 10-fold speed increase over the previous generation's Dynabus, and the early summer completion of application porting by Tandem independent software developers (ISVs).

But the sea change will also require new ISV efforts and Tandem is now aggressively seeking new applications for OLTP, retail, and the Web specifically aimed at the burgeoning electronic marketplace. Facing up to the many challenges of new ITP data types, Tandem itself is "postmodernizing" its NonStop SQL relational database with Informix Software's Illustra DataBlade modules, thus adding Internet-critical access to complex data, for example video, and the related functions necessary to access the data in high-volume video server applications.

## Table 1: Tandem's S-Series ServerNet-Enabled Servers

| Model | Processor | Nodes | Memory | I/O Expansion | Drive Bays | OS |
|-------|-----------|-------|--------|---------------|------------|-----|
| S100 | P6 200/256 x 1-2 | 1-16 | Up to 1GB | 8 | 11-12 | NT |
| S1000 | P6 200/512 x 1-8 | 1-16 | Up to 1GB | 15 | 17 | NT |
| S1000RM | P6 200/512 x 1-8 | 1-16 | Up to 1GB | 8 | 10 | NT |
| S7000 | MIPS R4400 150-MHz | 1-4080 | Up to 1GB | Unlimited | 16/cabinet | NSK |
| S70000 | MIPS R10000 200-MHz / P6 200/512 x 1-2 | 1-4080 | Up to 1GB | Unlimited | 16/cabinet | NSK |

## ServerNet and ServerWare Provide Malleability

Equally important, ServerNet is also the unyielding backbone supporting the revitalization of the company as a pioneering partner that is co-responsible for enriching Microsoft NT clusters with message-passing bandwidth to scale up to enterprise-class computing. Similarly, Tandem is licensing its enterprise-class value-adds to Compaq and Dell, who provide commodity Intel server technologies.

Demonstrating depth of commitment and vision, Tandem will be selling ServerNet-enabled, high-availability Intel/NT servers into its own installed base as well as to new customers. Running ServerWare designed for high-availability at near-commodity price points, the NT-based S100, S1000, and S1000RM are major departures for the new Tandem Computers.

With the combination of ServerNet and ServerWare software (see Figure 1), cost-sensitive IS planners can now choose the appropriate platform for current processing demands and be prepared to scale when necessary. As an application proves successful and draws more users, the enterprise can easily improve performance with cost-effective hardware increments. Moreover, armed with common ServerWare tools such as Tandem's highly parallelized and now portable TP monitor and NonStop SQL RDBMS, enterprises will be able to continue leveraging their skills as they grow.

Tandem's strategy — offering the ability to run combinations of ServerNet and ServerWare on Tandem's Himalaya systems, commodity Intel/NT servers, or ServerNet-enriched Microsoft NT clusters — accurately accesses and responds to the challenges that IS will face with ITP and other Web-enabled applications. Thus, IS planners will be able to mount their own multi-platform campaigns to meet new-applications challenges. For example, a company may choose to designate Intel/NT as the ideal platform for churning out HTML (hypertext markup language) pages on a Web server, with Tandem/NT clusters serving as the high-availability gateway server to the near-limitless I/O prowess of a NonStop Himalaya system processing the ins and outs of electronic commerce applications.

Given Tandem's demonstrated focus, its viable strategy, and the continued excellence of its architecture and products, Aberdeen believes that IS planners who are serious about protecting the enterprise from being blindsided by bandwidth deficiencies, would be well-served to give the new ServerNet-driven Tandem serious consideration.

## ServerWare

Although ServerNet technology will enable high-end transaction processing and massive throughput, no IS executive knows exactly what their ITP architecture will look like in the future because they don't know how much Internet bandwidth will be available, how much it will cost, or what the specific nature of their distributed applications will be. To address this uncertainty Tandem's multi-platform ServerWare middleware will let IS and ISVs develop, deploy, and partition a single ITP application a single time on the Himalaya or NT according to function and price/performance.

Writing an application only once is an appealing concept to both CIOs and CFOs because constructing an average corporate web site is complex and usually costs about $600,000 in custom coding alone — and costs are growing rapidly due to Web competition for an increasingly Web-sophisticated audience. To further reduce these costs, ITP planners will have literally thousands of ISPs to back them up as Tandem extends ServerWare to NT and NT clusters, along with using Microsoft's planned Wolfpack cluster technology to which Tandem has contributed.

ServerWare will be delivered as a multi-platform series of products in 1997 including an object relational database, TUXEDO, TP Objects, Java and a CICS-compatible transaction processing monitor. The essential strategy is to extend enterprise-level availability and reliability down the value chain to the commodity Intel/NT platform by using ServerNet interconnect technology for NT-to-Himalaya interoperability, and using ServerWare as common middleware for next-generation ITP.

## Target Markets

The ServerNet/ServerWare strategy for Himalaya and NT will help Tandem penetrate companies implementing ITP applications for commerce, Intranets, Messaging, Computer Telephony Integration and media. Further, the flexible new architecture will bring high-end computing to: branch offices; franchises; and retail stores — distributed-site vertical markets that Tandem already understands. These multi-tier ITP customers will help drive demand for both Tandem's core high-end Himalaya at corporate and central sites and NT servers at distributed sites. On-line service providers are also an important market for Tandem; they represent the cutting edge of today's Internet electronic commerce. America Online is using Himalaya as a front-end to log-in and bill users before passing them along to lower-end and less expensive HTML servers. Alternatively, banks may keep customer account information on a central Himalaya and use NT as the branch office front-end. Aberdeen believes this strategy may well establish Tandem's ServerWare as an important, de facto, industry-standard platform for multi-tier, high-availability enterprise computing.

## Aberdeen Observations and Conclusions

Aberdeen believes Internet Transaction Processing will evolve more quickly than many have considered. By the year 2000, many enterprises will be collaborating internally on data-rich Intranets, and selling effectively with a new breed of multimedia-rich, infomercial style electronic stores. The IT resources to drive these applications will grow exponentially, there will be few resources available to re-invent a successful application implemented on the wrong architecture, and — as usual — competitive advantage will quickly come into play.

We are pleased with the direction Tandem has taken this year. As an example, to attract new Himalaya customers, Tandem has revamped its pricing structure for its hardware and software with a considerably lower life-cycle cost of ownership. We believe existing Himalaya users will surely be attracted to the dual-platform ServerWare strategy both as a flexible development environment and because the Tandem strategy will allow IS to use Himalaya as a front-end, a back-end or a peer to NT.

ServerNet is an important contribution to technology whose benefits will become more apparent as I/O-bandwidth quickly becomes both an internal and cross-system problem. Moreover, ServerNet's architecture has enormous scalability and flexibility built in — important attributes.

Potential buyers who thought the old Tandem was too expensive and too proprietary are now wrong on both counts. With commodity and Tandem-mission-ruggedized Intel/Microsoft NT server choices, IT organizations can take part in a surge of NT market growth. But as we have argued, NT will not scale to enterprise workloads in this century. That is where the Himalaya S-series servers comes in. Moreover, Tandem has thoroughly architected a common application operating environment that has investment protection which, when delivered soon, cannot be beaten. All of this points to a reinvigorated Tandem as a company with a new message worthy of attention.

AberdeenGroup, Inc.
One Boston Place
Boston, Massachusetts 02108 USA
Tel: 617.723.7890
Fax: 617.723.7897

Copyright © 1996 Aberdeen Group, Inc., Boston, Massachusetts
This Document is for Electronic Distribution Only
-- DO NOT COPY --

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-tandem-vision-21st-century-electronic-business |
| title | Tandem's Vision, Architecture, and First Products For 21st Century Electronic Business |
| author | Aberdeen Group |
| date | 1996-01-01 |
| type | white-paper |
| subject_domain | fault-tolerant-computing-electronic-commerce |
| methodology | industry-analysis, competitive-profiling, expert-opinion |
| source_file | 1996 Tandem's Vision, Architecture, and First Products For 21st Century Electronic Business.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group's 1996 profile of Tandem Computers analyzes the company's ServerNet system area network architecture and ServerWare middleware strategy as the foundation for Internet Transaction Processing (ITP) in the 21st century. The report evaluates Tandem's S-Series Himalaya servers, their multi-platform NT/Himalaya strategy, and predicts that Tandem's high-availability, high-throughput architecture will become the de facto platform for mission-critical electronic commerce and multi-tier enterprise computing.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | This study captured Tandem at a pivotal strategic inflection—rebranding from proprietary fault-tolerant systems toward commodity Intel/NT integration—one year before its $3 billion acquisition by Compaq. Aberdeen's identification of 'Internet Transaction Processing' as a new computing category proved prescient. |
| **Relevance** | medium | The NonStop architecture concepts (fault tolerance, parallel processing, high-availability OLTP) remain highly relevant in cloud and financial services computing; however the specific hardware and ServerNet details are obsolete. The ITP concept maps directly to modern high-frequency trading and real-time payment infrastructure. |
| **Prescience** | high | Aberdeen's prediction that ITP would dominate 21st-century computing proved correct—Tandem's NonStop technology survived acquisition by Compaq (1997) and HP (2002) and continues as HPE NonStop today, still running NYSE transactions and ATM networks. The ServerWare multi-platform strategy anticipated microservices and cloud-hybrid architectures. |

### Prescience Detail

**Prediction 1:** ServerWare as industry-standard ITP platform
- **Claimed:** Aberdeen predicts ServerWare will become de facto industry-standard platform for multi-tier, high-availability enterprise computing
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 1:** ServerWare actual outcome
- **Result:** Tandem acquired by Compaq in 1997 for $3B before ServerWare fully deployed; NonStop architecture survived but ServerWare as branded middleware was discontinued
- **Confidence:** verified
- **Notes:** Partial: architecture survived; specific ServerWare brand did not

**Prediction 2:** ITP evolution speed
- **Claimed:** Aberdeen predicts ITP will evolve more quickly than many have considered; by 2000 enterprises will sell via multimedia-rich electronic stores
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 2:** ITP/e-commerce actual outcome by 2000
- **Result:** Dot-com boom confirmed Aberdeen's prediction; by 2000 major enterprises had deployed electronic commerce and intranet collaboration at scale
- **Confidence:** verified
- **Notes:** E-commerce grew from ~$7B in 1997 to ~$27B in 2000; Intranet deployment near-universal among Fortune 500

**Prediction 3:** Tandem viability as reinvigorated enterprise computing company
- **Claimed:** Aberdeen sees Tandem as reinvigorated company with new message worthy of attention; recommends IS planners evaluate ServerNet
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 3:** Tandem/NonStop actual outcome - 30-year view
- **Result:** HPE Integrity NonStop still active in 2026, still processing NYSE transactions and ATM networks; architecture validated over 30 years
- **Confidence:** verified
- **Notes:** Tandem -> Compaq (1997) -> HP (2002) -> HPE NonStop (2015-present); architecture continuously active


### Entities Referenced (8)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Tandem Computers Inc. | company | acquired | Compaq (1997) -> HP (2002) -> HPE NonStop (2015-present) |
| Aberdeen Group, Inc. | firm | acquired | Aberdeen (Harte-Hanks -> Informa) |
| Compaq Computer Corporation | company | acquired | Hewlett-Packard (2002) |
| Microsoft Corporation | company | active |  |
| Informix Software, Inc. | company | acquired | IBM (2001) |
| America Online (AOL) | company | acquired | Time Warner AOL -> Verizon Media -> Yahoo |
| Dell Computer Corporation | company | active |  |
| Hewlett-Packard Company | company | active | HP Inc. + HPE (split 2015) |

### Technologies Referenced (8)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Tandem ServerNet (SAN) | platform | Tandem | emerging | obsolete |
| Tandem NonStop Himalaya | platform | Tandem | mature | active |
| Tandem ServerWare | framework | Tandem | emerging | obsolete |
| NonStop SQL | platform | Tandem | mature | active |
| Microsoft Windows NT | platform | Microsoft | mature | obsolete |
| TUXEDO Transaction Monitor | application | Novell/BEA | mature | active |
| Internet Transaction Processing (ITP) | framework | Tandem/Aberdeen | emerging | obsolete |
| Informix Illustra DataBlade | application | Informix | emerging | obsolete |

### Observation Summary

- Total observations: 25
- By type: actual-outcome: 4; benchmark-result: 4; framework-factor: 5; market-data: 5; strategy-classification: 1; technology-assessment: 3; viability-prediction: 3

---

*Processed by Archival Ingest Skill v13 on 2026-03-14*
*Source URL (Wayback Machine): https://web.archive.org/web/19970604103613/http://www.aberdeen.com:80/secure/profiles/tandem/tandem30.htm*
