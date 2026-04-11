# Better Performance and Lower Prices Through TPC Benchmarks

> Archived from: 1992-TPC-Benchmarks-VP.docx
> Original publication date: 1992-03
> Author: Peter S. Kastner / Aberdeen Group

---

## Original Document Text

FILE: 1992-TPC-Benchmarks-VP.docx
============================================================
TPC Benchmarks Page
@MAIN HEAD = Better Performance and Lower Prices Through TPC Benchmarks
@INTRO TEXT = After three tumultuous years of supplier wrangling, bombast, progress, and refinement, users can now evaluate suppliers' performance claims using a standard set of definitive benchmarks. Having been badly burnt by lies, more lies, and "benchmarks" in the late 1980s ("benchmarketing"), buyers had little chance of fairly measuring or comparing online transactional database processing among competing suppliers.
In 1988, even suppliers realized that performance and price- performance claims were so outrageous that they banded together to form the Transaction Processing Council (TPC). Slow to start, the TPC benchmarks are now the de facto industry standard for measuring commercial performance and price-performance across suppliers. More importantly, TPC benchmark-driven competition between suppliers has resulted in startling improvements in price-performance that buyers can literally take to the bank.
In this technology Viewpoint, Aberdeen first clarifies what the various TPC benchmarks are, and then illustrates how they should be used.
@SUB HEAD = Executive Summary
@BODY TEXT1 = Performance benchmarks have shifted from being imprecise and highly suspect supplier sales tools to a robust and respected method for users to fairly and accurately compare competing computer systems. This positive trend now permits IS executives to make apples-to-apples comparisons, something previously impossible. While performance itself is not the most important acquisition criteria, the direct and indirect costs of undersizing or oversizing a computer can be material.
Three Transaction Processing Council benchmarks, particularly TPC-A, are now widely accepted metrics of performance and price-performance. Unlike past metrics, those of the TPC are unequivocally and comprehensively defined: Performance is a measure of system capacity expressed in transactions per second (TPS) where transactions are explicitly defined. Price is the sum of all the specified system and support components to achieve that capacity for a five-year period. Price-performance is the price divided by performance, and is typically expressed in K$/TPS, meaning thousands of dollars (price) per transaction-per-second (performance)
Buyers are getting two direct benefits from TPC-centered competition.
First, apart from competitive forces, the availability of comparison data is pressuring individual suppliers to deliver better performance more frequently, particularly through more efficient software. Faster software is effectively a free hardware upgrade. Second, competition among suppliers is improving price-performance at a startling rate, improving fivefold over the past two years and 35 percent so far this year alone. While some of these increases have been accomplished through price reductions, most have been the result of performance improvements. We expect buyers will see rapidly improving TPC-A price-performance at least through 1993.
There are three additional consequences of TPC-based competition. First, the traditional observation that small companies consistently offer the best price-performance is no longer the rule. Over the past 20 months, Digital Equipment, Hewlett-Packard, and IBM each has led with best price-performance, and have overtaken such suppliers as Sequent. In the first quarter of 1992 alone, price-performance leadership has changed six times, and has included new leaders Bull, Data General, and Sun Microsystems. Second, competition is squeezing price- performance into narrower ranges where large discrepancies between suppliers formerly existed. Finally, for at least the next 18 months, it will remain a buyer's market for TPC-A results.
@SUB HEAD = How It All Started
@BODY TEXT1 = A 1985 Datamation article anonymously written by twenty-odd academics and industry developers loosely defined a banking-oriented benchmark. Variously called ET1, Debit/Credit, and TP1, this benchmark updates a teller, branch, and account record and inserts a history-file record. The result of the benchmark was two metrics: throughput performance as measured in transactions per second (TPS), and price-performance calculated as the five-year life- cycle costs of ownership divided by the throughput.
By 1988, the imprecise Debit/Credit specification resulted in numerous publicly fought battles over interpretations of the benchmarks while press releases flooded the market with ever increasing, and farfetched, improvements in throughput and price-performance. Then, the emerging relational database suppliers crafted a database-only benchmark version called TP1. Within months, TP1 had so many variations and inconsistencies that the original 1985 intent was lost: the ability to evenly compare competing systems. Buyers and many industry analysts threw up their hands in disgust, effectively discounting all commercial performance claims as mere Benchmarketing.
@SUB HEAD = Introducing the TPC
@BODY TEXT1 = The Transaction Processing Council was formed in late 1988 by concerned suppliers as an independent, standards-setting body for commercial benchmarks. Today, the council has over forty members including all of the world's major commercial computer-system suppliers.
The product of the TPC is a series of trademarked benchmark specifications. Benchmark sponsors can use the TPC trademark in their marketing only if they have run their tests according to the detailed benchmark standards and submitted a detailed, full-disclosure report to reviewers -- industry competitors who are council members. The council has rejected several benchmark submittals as noncompliant.
As a final measure of compliance, the TPC strongly urges sponsors to use an outside benchmark auditor to ensure the tests were run as stated in the sponsor's full disclosure report. Aberdeen Group has audited several TPC benchmarks.
Although it is not required, virtually all TPC results reported to date use a relational database for storage. This is of obvious interest to the many IS developers who are specifying new applications built around an RDBMS.
@SUB HEAD = The ABC's of the TPC
@BODY TEXT1 = The TPC has defined three benchmarks and variations within individual benchmarks. The intent of the TPC is to define a suite of benchmarks that cover a broad range of computing activities including transaction processing, database processing, and decision support. The benchmarks are lettered starting with 'A'. TPC-A covers transaction processing, TPC-B covers database, and TPC-C covers a mixed transactional workload built around an order entry application.
@SUB HEAD = TPC-A
@BODY TEXT1 = TPC-A is a transaction-processing successor to the ill-fated 1985 Debit/Credit benchmark. Aberdeen Group views TPC-A as the most relevant of today's TPC benchmarks to commercial system buyers because it measures the performance and price-performance of an active network of online users. Many of our end-user clients are mandating TPC-A results in their new system requests for proposals.
TPC-A measures performance as the number of completed transactions per second where 90 percent or more of the transactions are finished in less than two seconds. Since 'users' submit transactions at an average rate of every ten seconds, there are at least ten active, connected TPC-A terminal users for every TPC-A transaction per second (TPS-A).
The TPC-A price is the sum of hardware, software, and maintenance costs for the server, the communications network, and terminals for a five-year period. Price-performance is calculated as the price divided by TPC-A, and is expressed as thousands of dollars per TPS-A (K$/TPS-A).
There are two variants of TPC-A: one for terminals connected via LAN and the other for terminals connected via WANs. The two should not be compared, since the WAN version is more difficult because of communications-bandwidth restrictions. Reflecting the market, most TPC-A sponsors have submitted results for the LAN variation, TPC-A local.
@SUB HEAD = TPC-B
@BODY TEXT1 = TPC-B is the database successor to TP1. It measures how many banking-type transactions can be completed per second. Performance is expressed as TPS-B, and price-performance is calculated like TPC-A and reported as K$/TPS-B. Not surprisingly, TPC-B results are most often touted by database and database hot-box suppliers.
The distinction between TPC-A and TPC-B is that in TPC-B there is no user-terminal network. This substantially reduces the processing overhead on the measured system as well as reducing the costs (there are no terminals to buy).
Aberdeen is frequently asked about the number of active, connected database users. TPC-B does not answer this question while TPC-A does.
@SUB HEAD = TPC-C
@BODY TEXT1 = The third TPS benchmark simulates an order-entry workload in an OLTP environment. Unlike the simpler A and B, the TPC-C benchmark includes a mixture of read-only and update-intensive database activities that simulate real-world applications.
The TPC-C benchmark specification is presently under public review, and Aberdeen expects approval this summer. Over time, we believe that TPC-C will become a very important and closely watched benchmark. But there can be no TPC-C results until the standard is approved and sponsors run their tests.
@MAIN HEAD = Digital's VAX: Alive and Kicking With TPC Benchmarks
@INTRO TEXT = While the press focuses on the still-to-be-announced Alpha Risc successor to Digital's bread-and-butter VAX product line, Digital Equipment has quietly and convincingly realigned and dramatically improved its price-performance. Digital, at least for now, offers the best commercial price-performance in the industry.
@SUB HEAD = Executive Summary
@BODY TEXT1 = Digital on March 15, 1992 quietly made a significant across-the-board price-performance realignment. As a result of this action:
- The VAX product line has been rationalized and squeezed into a narrow price-performance. As a result, buyers pay within 20% from the entry-level MicroVAX 3100 through the mainframe-class VAX 6000 model 640;
- The MicroVAX 3100 model 80 today has the industry's best price-performance as measured by the industry-standard TPC-A benchmarks;
- Since August of 1990, Digital has improved TPC-A throughput (performance) by about 50% while costs-per-transaction (price-performance) improved three-fold;
- The MicroVAX and VAX 6000 product lines are highly competitive with not only traditional rivals Hewlett-Packard and IBM, but also with hot-box suppliers such as Sequent.
Price-performance ranges from a low of $7.69 K$/TPS-A on the MicroVAX 3100 to a high of $10.71 for the MicroVAX 4000 model 300. IBM's AS/400 price-performance, for example, is 77% more expensive with the high-end model E70 than at the entry-level E10.
The VAX 6000-640 shows more than seven times the throughput (over 200 TPS-A) of 1988's top-of-the-line VAX 8830 (at 27 TPS running Debit/Credit, not TPC-A).
@MAIN HEAD = Hewlett-Packard: Gaining Respect
@BODY TEXT1 = When the TPC was founded in 1988, transaction processing to Hewlett-Packard meant timesharing with data integrity. HP did not consider itself among the industry's commercial performance or price-performance leaders. Recently, HP has taken to TPC benchmarks with fervor.
Figure 5 shows the 61 percent price-performance and 171 percent performance improvements of the HP 3000 midrange since January 1990.
@MAIN HEAD = Here Come the Hot Boxes
@BODY TEXT1 = Both Bull's DPX/2 and Sun's Sparcserver now lead in TPC-A price-performance, and they helped push the best TPC-A price-performance to well under $10K/TPS-A. Data General also led briefly with its AviiOn 5225.

Peter S. Kastner
Aberdeen Group
March 1992


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | 1992-tpc-benchmarks-vp-ed0e0d |
| title | Better Performance and Lower Prices Through TPC Benchmarks |
| author | Peter S. Kastner / Aberdeen Group |
| date | 1992-03 |
| type | white-paper |
| subject_domain | transaction processing benchmarks |
| methodology | market analysis; benchmark review; vendor comparison |
| source_file | 1992-TPC-Benchmarks-VP.docx |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Technology Viewpoint examining TPC benchmarks (TPC-A, TPC-B, TPC-C) as the de facto standard for measuring commercial performance and price-performance. Covers the history of Debit/Credit benchmarking, TPC formation in 1988, and detailed vendor comparisons across DEC VAX, HP, IBM AS/400, Sequent, Bull, Sun, and others. Concludes that TPC-A competition has driven a five-fold improvement in price-performance over two years and advocates that buyers mandate TPC-A results in RFPs.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | HIGH | Full manuscript of Aberdeen's seminal TPC benchmark viewpoint. The complete published text; excerpted slide versions are already in the archive as dectp92, hptpc92, ibmtpc92, tpc2-92. |
| **Relevance** | medium | Benchmark methodology still instructive for evaluating competitive performance claims. |
| **Prescience** | HIGH | Kastner's analysis of vendor trajectory proved largely correct: Unix/RDBMS suppliers emerged as price-performance leaders, VAX faded, and TPC benchmarks became lasting industry standards. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (8)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | acquired | Harte-Hanks (Aberdeen Group brand) |
| Peter S. Kastner | person | active |  |
| Digital Equipment Corporation | company | dissolved | Compaq (1998); subsequently HP |
| Hewlett-Packard (HP) | company | split | HP Inc. / HPE |
| IBM | company | active |  |
| Sequent Computer Systems | company | acquired | IBM (1999) |
| Groupe Bull | company | acquired | Atos (partially) |
| Sun Microsystems | company | acquired | Oracle (2010) |

### Technologies Referenced (9)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| TPC (Transaction Processing Performance Council) Benchmarks | benchmark | TPC (consortium) | emerging standard | active |
| Online Transaction Processing (OLTP) | application | various | dominant | current |
| Digital VAX/OpenVMS | platform | Digital Equipment Corporation | mature/declining | legacy |
| Relational Database (RDBMS) | application | various | dominant | current |
| Oracle Rdb | application | Digital Equipment Corporation / Oracle | active | legacy |
| IBM AS/400 | platform | IBM | active | legacy-supported |
| Unix Enterprise Servers | platform | various | emerging | legacy-supported |
| HP 3000 | platform | Hewlett-Packard | mature | end-of-life |
| HP 9000 | platform | Hewlett-Packard | active | legacy |

### Observation Summary

- Total observations: 32
- By type: market-analysis: 18, benchmark-result: 14
