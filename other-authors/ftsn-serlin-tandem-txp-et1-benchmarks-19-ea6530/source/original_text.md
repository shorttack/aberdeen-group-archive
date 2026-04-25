# Omri Serlin FTSN-33: Tandem Reports TXP ET1 Benchmarks 7.2-9.6 tps/CPU; Cites Stratus 1.0-1.1 tps/CPU (May 15, 1985)

> Archived from: Serlin-FTSN-5-15-1985.pdf
> Original publication date: 1985-05-15
> Author: Omri Serlin (FTSN newsletter)

---

## Original Document Text


===== Serlin-FTSN-5-15-1985.txt =====
    TANDEM REPORTS TXP BENCHMARKS

     Summary:  New ET1  benchmark data
:rom Icindem show the TXP ranging over
’.2-9.6 tps/CPU, and, according to Tan-
lem, show a significant edge over IBM's
PF2 in cost per tps.


    Tandem recently shared with FTSN
ome of the results of a series of ET1
enchmarks run on a 4-processor TXP
ystem.    ET1   is the   "debit/credit"
ransaction, as logically defined in the
rticle by "anon et al" in the 1   April


 Altos, CA 94023, USA, Tel.415/948-4516
      . FTSN-33                                Page 5                                 15 May   1985



       issue ot Datamation,   but with 1/5 the                Dennis McEvoy, Tandem's vice presi­
       database size, as follows (each record =         dent of software,   told FTSN that these
       100 bytes):                                      results proved a number of points.    Re­
                                                        lative to IBM's TPF2,    Tandem believes
             2 million account records                  its V.2 and V.5 cost/TPS are substantia­
             2000 teller records                        lly lower,    even though both cases are
             200 branch record                          coded in Cobol as opposed to assembly
                                                        language, mandated by TPF2. V.6, which
              The physical configuration consis­        utilizes IMF and Pathway, is much richer
        ted of a TXP system with four 4MB CPUs,         in functionality, and should be compared
        6 or 7 disks (two 128MB 4110s, two 300MB        to an IMS or IMS/Fastpath case, in which
       "4Tb 4s,  and either two or    three 168MB       case again Tandem has a cost/TPS edge.
        V8's), and one 6104 communications cont­
        roller operating under X.25 at an aggre­              (Tandem did not do the benchmarks
        gate of 76 Kbaud.    Each teller terminal       on TPF2 or IMS,    but based on data from
        represents a separate virtual circuit.          sources believed to be expert on these
        The system under test was driven by a           systems,    Tandem believes its price­
        separate, 2-TXP "load generator" system.        performance claims are justified).

             Several versions of the benchmark               Another point is that,     accepting
       program were tried,    including one in          previous results, which showed that the
       which each terminal was served by a              TXP runs about 2.5 times faster than the
       separate process,    and neither TMF nor         NS-II,  McEvoy feels that the new data
       Pathway were employed      ("Version 2");        points to a range of 1.9-3.8 tps/CPU for
       another ("Version 5") did utilize the            the NS-II (assuming the new B00/DP2
       standard Pathway requester/server model,         software);   this is much higher than the
       but no TMF;   and still another ("Version        1.0-1.1    tps/CPU reported by Stratus
       6")   employed both Pathway and TMF work­        (FTSN—32 p.6).
       ing with the new Guardian release       BOO
       and new DP2 disk process.      All non-TMF            Thirdly,    McEvoy   thinks    these
       versions used the seven-disk configura­          results prove that a 16-CPU TXP system
       tion; with TMF, only six disks could be          can do 100 tps, and that a 10-system FOX
       effectively used.                                network should therefore be able to do
                                                        the magic "1000 tps".
             Results were as follows:
                                                             The benchmark work was done by a
             Version     TPS/      Cost/TPS             group headed by Harald Sammer in Frank­
                       processor                        furt, W. Germany.  The group is informa­
biO          V.2         9.56 y    $33.7K               lly known as the "1000 tps"  group; its
             v*5         7.60      $39.2K               mission is to find ways in which Tandem
                   "new" 4.70*1    $58 K                standard hardware and software can be
                   "old" 3.17J     $80.6K               modified    to reach high    transaction
                                                        throughput.
        where the "old" V.6 used the Guardian
        A06 release with DP1.  Average response
        time of under 1 second is maintained in
        all cases.
                                                             Did you know?  ITOM also publishes
             Costs are calculated as suggested          the Superwicro newsletter,  which tracks
        in the anon et. al. article, by summing         business, market,   and product develop­
        the following elements:                         ments in MMP systems, other high-end
             Hardware purchase price                    microsystems,   and LAN-based systems.
             5-year maintenance costs                   For your free sample issue, please write
             Software initial license fees              on your company's letterhead,   or mail
             Software 5-year maintenance fees           your business card.


        ©Copyright 1985 ITOM Int'l Co., POB 1415, Los Altos, CA 94023, USA, Tel.415/948-4516


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | ftsn-serlin-tandem-txp-et1-benchmarks-19-ea6530 |
| title | Omri Serlin FTSN-33: Tandem Reports TXP ET1 Benchmarks 7.2-9.6 tps/CPU; Cites Stratus 1.0-1.1 tps/CPU (May 15, 1985) |
| author | Omri Serlin (FTSN newsletter) |
| date | 1985-05-15 |
| type | industry-newsletter |
| subject_domain | fault-tolerant-computing/transaction-processing-benchmarks |
| methodology | industry-newsletter-with-vendor-data |
| source_file | Serlin-FTSN-5-15-1985.pdf |
| license | CC-BY-4.0 |

### Abstract

Issue 33 of Omri Serlin's Fault-Tolerant Systems News (FTSN) newsletter, published May 15, 1985 by ITOM International (Los Altos, CA). Reports new Tandem ET1 benchmark data on a 4-processor TXP system, with TXP ranging 7.2-9.6 tps/CPU and (per Tandem) showing a significant cost-per-tps edge over IBM's TPF2. Three Guardian/Pathway/TMF software-stack configurations were tested ('V.2', 'V.5', 'V.6 new', 'V.6 old' with Guardian A06+DP1) producing 9.56 / 7.60 / 4.70 / 3.17 tps/processor and $33.7K / $39.2K / $58K / $80.6K cost-per-tps respectively. Database: 2M account records, 2,000 teller records, 200 branch records (1/5 the size of anon-et-al's Datamation specification). Tandem VP of Software Dennis McEvoy claims Tandem's V.2 and V.5 cost-per-tps is substantially lower than IBM TPF2 even though both are coded in COBOL (TPF2 mandates assembly), and that a 16-CPU TXP system can do 100 tps and a 10-system FOX network 1000 tps. The benchmark was run by Harald Sammer's 1000-tps group in Frankfurt. Notably, FTSN cross-references the Stratus result from FTSN-32 at 1.0-1.1 tps/CPU — making this newsletter a rare neutral cross-vendor 1985 ET1 data point that contextualizes Stratus's 1985-1986 TP1/ET1 claims (Batch 25 studies #5 and #7).

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Omri Serlin's FTSN was the canonical cross-vendor neutral fault-tolerant industry newsletter of the era; this issue places Stratus, Tandem, and IBM TPF2 on the same ET1 yardstick — irreplaceable analytical context for the 1985-1986 Stratus benchmark corpus. |
| **Relevance** | high | Direct cross-reference between Tandem TXP (7.2-9.6 tps/CPU) and the Stratus result (1.0-1.1 tps/CPU per FTSN-32) clarifies Stratus's relative competitive position in 1985 and motivates Stratus's 1986 ET1 spec + benchmark corpus (study #7). |
| **Prescience** | medium | Serlin's structured cost-per-tps + tps-per-CPU framing presaged the TPC-A/B/C standardized benchmarks (1988+) and remains the core measurement language of modern OLTP performance engineering. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (9)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Omri Serlin | person | active |  |
| Fault-Tolerant Systems News (FTSN) | publication | defunct | ITOM Int'l Co. |
| ITOM International Co. | firm | defunct | Los Altos CA |
| Tandem Computers | company | acquired | Compaq (1997), then HP (2002) |
| Stratus Computer | company | acquired | Stratus Technologies (now Penguin Solutions) |
| IBM Corporation | company | active |  |
| Dennis McEvoy | person | active |  |
| Harald Sammer | person | active |  |
| Datamation magazine | publication | active | Online only after 1997 print closure |

### Technologies Referenced (5)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Tandem TXP System | computer-system | Tandem | current-1985 | obsolete |
| IBM TPF2 (Transaction Processing Facility 2) | transaction-processing-system | IBM | current-1985 | active-as-z-tpf |
| ET1 Debit-Credit Benchmark | transaction-processing-benchmark | industry / Anon-et-al / Datamation | current-1985 | superseded-by-tpc-a |
| Tandem Guardian + Pathway + TMF Stack | operating-environment | Tandem | current-1985 | obsolete |
| Tandem FOX Inter-System Network | networking-architecture | Tandem | current-1985 | obsolete |

### Observation Summary

- Total observations: 7
- By type: benchmark-result: 3, commentary: 2, methodology: 1, affiliation: 1
