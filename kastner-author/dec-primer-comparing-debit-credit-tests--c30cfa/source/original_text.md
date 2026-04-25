# A Primer on Comparing Debit Credit Tests (Kastner, DEC CSG, 1988)

> Archived from: DEC-debit-credit-primer-PSK-1988.pdf
> Original publication date: 1988-01-01
> Author: Peter S. Kastner — DEC Corporate Systems Group, Competitive Marketing Programs

---

## Original Document Text

A PRIMER ON COMPARING DEBIT CREDIT TESTS
BACKGROUND
AS debit credit has emerged as the defacto commercial/TP benchmark, more
business and engineering decisions have been made based on comparisons of
various vendor's debit credit reported results. This makes sense because debit
credit is supposed to be a well-defined benchmark [Datamation, April, 1985, "A
Measure of Transaction processing performance"] where vendor results can be
compared.  The reality is that every vendor has reported debit credit results
under different conditions, sometimes unspecified.

This primer is designed to level the playing field a bit by providing some
conditions which readers might apply to reported debit credit results. Serious
miscalculations in engineering specifications, market requirements, cost goals
and other activities can result if debit credit results are compared between
vendors without some consideration for the differences between the vendor's
testing and reporting methodology.

While the author is not recommending the 'normalization' of debit credit
results, I strongly urge anyone considering the comparison of vendor's products
based on debit credit to read on.

What you won't find here is results. This is not the forum to publish Digital
debit credit results.

DIGITAL EQUIPMENT
DEC uses three Styles of debit credit.     A full description of Digital debit
credit is available from the author.

Style 1 is a fully qualified debit credit where all presentation services
and database activity is handled by the system under test. We believe Digital
Style 1 to be the most rigorous implementation of debit credit. Style 1
results cannot be directly compared with any competitor's results. As a rule,
Digital engineering uses Style 1 as the metric for projecting database and
system performance.

Style 2 offloads forms and character processing to a front end VAX. The
front end cost is included in cost of ownership results. Because VAX
architecture, ACMS, DECintact etc. support such distribution, this is a
viable model and as rigorous as Style 1.

Style 3 assumes MicroVAXes or intelligent controllers are in the 'bank
branches' of the debit credit. This offloads character and forms presentation
services from the system under test and appreciably improves throughput,
and hence price/performance.  In general, Digital Style 3 results should
be used to compare DEC with other vendors since no other vendor tests the
costs of presentation services (which use 40% of the VUPS in a Style 1 test
of an 8700 ).

IBM
IBM has not generally reported debit credit results, depending on RAMP-C
to obscure comparative performance.

System/88
Tests based on Stratus ET-1, which is not debit credit.  IBM results were
obtained at 70% cpu utilization (an in-house rule), and do not (in spite
of published reports in FTSN) use data integrity features. Otherwise, see
the Stratus results for comments.

370 architecture
Testing on the 9370, 4381 and 3090 were conducted by DEC (CSG and HPS) using an
experienced contractor with extensive IBM experience.  The results were
obtained over a period of years using a consistent methodology. The results
can be directly compared between the 370 architecture machines, and probably
can b© extrapolated to other similar models not tested. Note that various
                    so^tware were used, and that such layered software tends to
get better over time.

The DEC-sponsored 370 architecture tests were run against 'qualified' (eg the
tests followed the letter and spirit of the Datamation debit credit benchmark
description)debit credit standards. Note that because IBM uses intelligent
terminals and controllers (3274/3270), IBM does not pay the async and forms
overhead that Digital does with Style 1 debit credit. Although somewhat
controversial within DEC, the 370 results can be compared to Digital Style 2 or
3 with distributed processing on MicroVAXes.

OneKay, a 1000 tps benchmark reported by IBM in late 1987 has been used
to extrapolate some 750 debit credit tps under IMS Fastpath. The author
believes this to be a bad conclusion.  Since IMS Fastpath uses in memory
databases with limited access capabilities, it is not reasonable to compare
such results with fully journaled disk-based debit credit. Second, no
presentation services were used. At 750 tps, some 22,500 field maps per
second are necessary for fully qualified debit credit.
System/3X
No debit credit results reported.   Digital is sponsoring tests of the System/38
and Silverlake.

TANDEM
Tandem's results are fully documented in a Tandem white paper on what they
called the TopGun benchmark (March 1987). Tandem disclosed the faults
mentioned below, which goes to prove that non-conformance to the debit credit
standard is OK as long as you tell people about it...just don't compare
the results to anything else.

Tandem reports from 2.5 tps per processor on the CLX to 6.5 tps per processor
on the VLX using the TopGun methodology commented on below.

Tandem uses 90%-2 second response times instead of 95%-l second standard.
Divide Tandem's reported results in half to get to 95%-l second.

Tandem simulated only 1000 tellers per 100 tps, not 10,000.   This saved memory,
communications buffer overhead and other unspecified costs.   Digital always
simulates the proper number of tellers and database sizes.
Tandem published the source code for their benchmark.  It shows that no
presentation services were used (because Tandem's screen COBOL is interpreted
and performance would have died). Therefore, Digital Style 3 is an
approximation of Tandem's tests.
The TopGun file distribution was highly artificial but completely balanced
for all-out performance. Be careful to ascertain the structure of Digital
tests on VAXclusters before comparing to Tandem's tests. Tandem uses physical
and logical partitioning by processor (which their software supports
completely. Digital tests which partition files on the Cluster so as to
minimize distributed lock manager overhead are the best comparisons to what
Tandem did.
The NonStop SQL code Tandem used had proprietary extensions which treated
the teller and branch files as having relative record keys. Presumably,
it's much easier to do a relative file I/O than a relational row retrieval.

In reality, a Style 1 qualified test of Tandem will likely show performance at
one-quarter of Tandem's published numbers, roughly comparable to Tandem's
tests.

From a price/performance standpoint, Tandem has used debit credit performance
as a CPU metric when deriving newly announced product price/performance. Tandem
will quote debit credit performance on new product entry configurations not
capable of handling the I/O of debit credit. Tandem derives
^t'!-fL\?^1,^P!r^°r^ance as measured in K$/tps by dividing the CLX CPU debit
cr. 1   mu     put (under unspecified conditions) into the entry system package
price.     ererore, the reader should avoid comparing Digital five year costs
of ownership for a full debit credit configuration against Tandem's
price/performance for an "entry” system.

STRATUS

Stratus ET-1 should not be confused with debit credit. Stratus, for obvious
marketing reasons, must appear to beat Tandem, and their numbers reflect
this war.  it is valid, however, to compare various Stratus machines using
ET-1 as a guideline.

Stratus does not use database journaling. Any long power failure, system
software crash or other non-hardware fault will lose transactions and leave
the databases in an inconsistent state. Stratus does not report journaling
numbers because their journaling is single threaded and peaks out at about
15-17 tps, killing the Stratus linear growth story. A Model 120 gets about
15 tps (Style 3 with some non-qualified areas as noted below) with journaling
for transaction protection. A model 140 doesn't do much better.

Like Tandem, Stratus ignores the presentation services part of debit credit.

Stratus also does injustice to the definition of the word random. Although
physical I/O's are done, there is extensive caching including even the account
file.
The author estimates a Stratus midrange Model 120 (2 MC68020's) will do
less than 8.5 Style 1 debit credit tps.


Peter S. Kastner
Corporate Systems Group
Competitive Marketing Programs
PDM1—2(El)
DTN 291-0364


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | dec-primer-comparing-debit-credit-tests--c30cfa |
| title | A Primer on Comparing Debit Credit Tests (Kastner, DEC CSG, 1988) |
| author | Peter S. Kastner — DEC Corporate Systems Group, Competitive Marketing Programs |
| date | 1988-01-01 |
| type | internal-competitive-marketing-paper |
| subject_domain | OLTP-benchmark-vendor-comparison |
| methodology | competitive-analysis-paper |
| source_file | DEC-debit-credit-primer-PSK-1988.pdf |
| license | CC-BY-4.0 |

### Abstract

Internal Digital Equipment Corporation Corporate Systems Group competitive marketing paper authored by Peter S. Kastner (Competitive Marketing Programs, PDM1-2(E1), DTN 291-0364) circa 1988. Provides DEC sales and marketing teams with a primer on interpreting and comparing Debit-Credit benchmark results across vendors (IBM, Tandem, Stratus, System/3X). Defines DEC's three styles of Debit-Credit: Style 1 (fully qualified, all presentation services in SUT — DEC's most rigorous; not directly comparable to competitors), Style 2 (forms/character offloaded to front-end VAX, cost included in COO), and Style 3 (MicroVAX or intelligent controllers in branches — recommended for vendor comparison since no other vendor tests presentation-services costs). Critiques IBM (RAMP-C obscures comparison; OneKay 1000-tps benchmark unfairly extrapolated to 750 Debit-Credit tps under IMS Fastpath), Tandem (TopGun March 1987: 90%/2-sec instead of 95%/1-sec, only 1000 tellers per 100 tps instead of 10,000, partitioned files, NonStop SQL relative-record-key extension), and Stratus (ET-1 ≠ Debit-Credit; no journaling; single-threaded logging caps at 15-17 tps; aggressive caching of account file). Provides DEC-eye estimates: Stratus Model 120 ≈ less than 8.5 Style-1 Debit-Credit tps. Notes Tandem reports 2.5 tps/processor on CLX to 6.5 tps/processor on VLX using TopGun. States Style 1 presentation services consume 40% of VUPS on an 8700. Document signed Peter S. Kastner, CSG Competitive Marketing Programs.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Kastner-authored DEC competitive-marketing primer — direct primary source from his DEC employer-era. Establishes his command of OLTP benchmark methodology and competitive analysis years before founding Aberdeen Group. Encodes the analytical voice and rigor that would later define his Aberdeen TPC-A audit and analyst practice. |
| **Relevance** | high | Concrete artifact of Kastner's DEC competitive-marketing role. References Style 1/2/3 framework which only makes sense in the context of the Kohler/Hsu engineering guidelines and Zahavi VAXcluster memo. Serves as Kastner's outward-facing competitive narrative built on the inward-facing engineering memos (Studies 1-3). |
| **Prescience** | high | Kastner's per-vendor critique structure — citing each vendor's specific non-conformance points — directly anticipated TPC-A/TPC-C full-disclosure audit reports. His insistence on apples-to-apples comparison (Style 3 vs. competitors' equivalent setup) prefigures the standardized TPC executive summary format. The Stratus journaling-throttle critique (15-17 tps cap) presaged the broader industry recognition that fault-tolerance must be designed for journaled throughput, not just cache speed. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (6)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Peter S. Kastner | person | active |  |
| Digital Equipment Corporation (DEC) | company | acquired | Compaq (1998), then HP (2002) |
| Tandem Computers | company | acquired | Compaq (1997), then HP (2002) |
| Stratus Computer | company | acquired | Stratus Technologies (now Penguin Solutions) |
| IBM Corporation | company | active |  |
| DEC Corporate Systems Group (CSG) | business-unit | internal | absorbed-into-Compaq-then-HP |

### Technologies Referenced (10)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Debit-Credit Benchmark | performance-benchmark | Anon-et-al / Tandem / Datamation | industry-defacto-standard | superseded-by-TPC-A-and-TPC-C |
| RAMP-C | performance-benchmark | IBM Corporation | vendor-proprietary | obsolete |
| IMS Fastpath | TP-database | IBM Corporation | active-product | legacy |
| IBM OneKay 1000-tps Benchmark (1987) | performance-benchmark | IBM Corporation | vendor-marketing-claim | obsolete |
| Tandem TopGun (March 1987) | performance-benchmark | Tandem Computers | vendor-marketing-claim | obsolete |
| Stratus ET-1 | performance-benchmark | Stratus Computer | vendor-marketing-claim | obsolete |
| Tandem NonStop SQL | relational-DBMS | Tandem Computers | active-product | renamed-HP-NonStop-SQL |
| VAX 8700 | minicomputer | Digital Equipment Corporation | production-shipping | discontinued |
| Stratus Model 120 | fault-tolerant-system | Stratus Computer | production-shipping | discontinued |
| IBM System/88 | fault-tolerant-system | IBM Corporation (OEM from Stratus) | production-shipping-OEM | discontinued |

### Observation Summary

- Total observations: 11
- By type: style_1_definition: 1, style_3_recommended: 1, vups_consumption: 1, tandem_response_time: 1, tandem_teller_undercount: 1, stratus_120_estimate: 1, stratus_journaling_cap: 1, tandem_clx_per_proc: 1, tandem_vlx_per_proc: 1, ibm_70pct_cpu_rule: 1, kastner_authorship: 1
