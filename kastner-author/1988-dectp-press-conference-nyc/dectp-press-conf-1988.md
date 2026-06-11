---
study_id: dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836
title: "DECtp Press Conference Transcript and Benchmark Charts, Plaza Hotel NYC, July 1988"
author: "Digital Equipment Corporation (Kirk, Dallas; Olsen, Kenneth H.; Glorioso, Robert; Hughes, Bob)"
date: 1988-07-19
type: primary-source
subject_domain: transaction-processing-benchmarks
methodology: press-conference-transcript; debit-credit-benchmark; comparative-performance
source_file: DECtp-NYC-1988-07-cleaned.md
license: CC-BY-NC-SA-4.0
prescience: "[DEFERRED]"
---

# DECtp Press Conference Transcript and Benchmark Charts, Plaza Hotel NYC, July 1988

**Date:** 1988-07-19
**Venue:** Plaza Hotel, New York City
**Source:** Computer History Museum, catalogue #102717571, accession X2675.2004, Gift of Hewlett-Packard Company. U-Matic video, 00:58:18. Archive collection: Digital Equipment Corporation records / DEC libraries' A/V holdings.
**Transcript prepared by:** Peter S. Kastner (from CHM video; Kastner was present at the original event)

## Context

DEC's DECtp product launch press conference, the culmination of four press events over ten months. Presenters include Ken Olsen (President, DEC), Bob Glorioso (VP Engineering), and Bob Hughes (VP Marketing). Glorioso presents Debit-Credit benchmark results for VAX systems versus IBM and Tandem in two configurations (RDBMS and flat-file), supported by four projected benchmark charts. Hughes presents the price/performance business case. Kastner was present at the event as a Debit-Credit subject matter expert invited to take questions. He traveled to the event by helicopter with Olsen and Glorioso to the DEC private jet.

## Speakers

- **Dallas Kirk** — MC/moderator
- **Kenneth H. Olsen** — President, Digital Equipment Corporation (keynote)
- **Bob Glorioso** — VP Engineering, DEC (benchmark presentation)
- **Bob Hughes** — VP Marketing, DEC (price/performance business case)

## Images (benchmark charts, high-resolution)

Four benchmark charts were projected during the Glorioso presentation and are preserved as high-resolution images:

1. `media/DECtp-1988-tps-rdbms.png` — DECtp Price/Performance: Debit-Credit Relational Database Systems (TPS)
2. `media/DECtp-flatfiles-tps-1988-08.19.41.png` — DECtp Price/Performance: Debit-Credit Flat Files (TPS) — video frame
3. `media/DECtp-1988-price-performance.png` — At Outstanding Price/Performance (K$/TPS)
4. `media/DECtp-1988-avg-system-cost.png` — Digital's Price Performance Advantage: Average System Cost for Transaction Processing

## Observations

### Methodology (Glorioso, ~line 628–652)

**OBS-001** `methodology` · `dec` · `debit-credit` · 1988
Benchmark selection rationale: DEC consulted industry analysts on what to measure and received unanimous advice to use a widely recognized, easily duplicated benchmark with clearly specified time, cost, throughput, and recovery requirements. DEC chose the industry-standard Debit-Credit benchmark.
> "The best way to get valid performance measures is to use a widely recognized, easily understood, and easily duplicated benchmark in which time, cost, throughput, and recovery are clearly specified."

**OBS-002** `methodology` · `dec` · `debit-credit` · 1988
Debit-Credit benchmark spec as stated by Glorioso: one TPS = 100 tellers, 10 branches, one transaction per 100 seconds. 95th-percentile response time ≤ 1 second. Cost = 5-year hardware + software + maintenance exclusive of staff, divided by TPS.
> "95% of these transactions must be completed in one second or less. Cost per transaction is calculated by a formula which divides the five-year cost of hardware, software, and maintenance exclusive of staff by the number of transactions per second."

**OBS-003** `methodology` · `dec` · `debit-credit` · 1988
IBM systems benchmarked by DEC or by third parties. Tandem numbers are self-reported from Tandem's own Debit-Credit runs.
> "IBM systems were benchmarked by Digital or by third parties, and Tandem's numbers are based on data reported by them from their own debit credit runs."

**OBS-004** `methodology-note` · `dec` · `debit-credit` · 1988
Stress-test variation: non-compliant relaxation of the Debit-Credit spec to explore maximum throughput. Response completion dropped from 95% to 90%; response time extended from 1.0 to 1.3 seconds; some recovery requirements relaxed. Glorioso notes this is still customer-friendly performance.
> "We dropped the response percentage from 95 to 90% and the response time from 1 to 1.3 seconds and relaxed some of the recovery requirements."
Result: 4-CPU VAX 8974 delivered 104 TPS flat-file under relaxed spec.

---

### Chart 1 — Debit-Credit RDBMS TPS (Glorioso, ~line 688–706)
*Image: `media/DECtp-1988-tps-rdbms.png`*

**OBS-005** `market-data` · `dec` · `dectp` · 1988
DECtp VAX 8830 Debit-Credit RDBMS TPS: 27 TPS (highest DEC RDBMS result; second bar from left on Chart 1). Glorioso: "truly competitive relational database performance."
> "up to 27 transactions per second on our large VAX 8830 systems — that's the second from the left on this chart."

**OBS-006** `market-data` · `ibm` · `dectp` · 1988
IBM 3090/200E Debit-Credit RDBMS TPS: 38 TPS (leftmost bar, Chart 1). IBM's highest RDBMS result; highest single-system number on the chart but at dramatically higher cost (see Chart 3).
> "IBM model 3090/200E, which is the leftmost bar on this chart, performance of only 38 transactions per second is achieved."

**OBS-007** `market-data` · `dec` · `dectp` · 1988
DEC VAX 8700 Debit-Credit RDBMS TPS: ~26 TPS. Image: Chart 1 bar read.

**OBS-008** `market-data` · `dec` · `dectp` · 1988
DEC VAX 8650 Debit-Credit RDBMS TPS: ~22 TPS. Image: Chart 1 bar read.

**OBS-009** `market-data` · `tandem-computers` · `dectp` · 1988
Tandem VLX 4-CPU Debit-Credit RDBMS TPS: ~18 TPS. Image: Chart 1 bar read.

**OBS-010** `market-data` · `dec` · `dectp` · 1988
DEC VAX 3600 Debit-Credit RDBMS TPS: 5 TPS (lowest DEC result; fourth bar from right on Chart 1).
> "From five transactions per second on the VAX 3600, that's the fourth bar from the right."

**OBS-011** `market-data` · `ibm` · `dectp` · 1988
IBM AS/400 and IBM 9370 Model 90 Debit-Credit RDBMS TPS range: 4–7 TPS. Glorioso characterizes this as "a limited performance range." Image: Chart 1 right-side bars.
> "IBM mid-range relational systems such as the IBM AS400 and 9370 Model 90 ... have a limited performance range of four to seven transactions per second."

---

### Chart 2 — Debit-Credit Flat Files TPS (Glorioso, ~line 708–726)
*Image: `media/DECtp-flatfiles-tps-1988-08.19.41.png`*

**OBS-012** `market-data` · `dec` · `dectp` · 1988
DEC 2× VAX 8810 cluster Debit-Credit flat-file TPS: 53 TPS (leftmost bar, Chart 2). Highest compliant result on the chart.
> "A configuration of two clustered VAX8810 — 53 transactions per second. That's the far left on this chart."

**OBS-013** `market-data` · `tandem-computers` · `dectp` · 1988
Tandem VLX 16-CPU Debit-Credit flat-file TPS: 52 TPS. Tandem's highest result requires 16 processors to match 2× DEC VAX 8810.
> "This compares with a 16-processor Tandem system rated at 52 transactions per second."

**OBS-014** `market-data` · `dec` · `dectp` · 1988
DEC VAX 8810 single-node Debit-Credit flat-file TPS: 28 TPS.
> "A single 8810 performs at 28 transactions per second."

**OBS-015** `market-data` · `dec` · `dectp` · 1988
DEC VAX 3600 Debit-Credit flat-file TPS: >6 TPS. Typical config ~$235K → $38K/TPS price/performance.
> "VAX 3600 ... performs over 6 transactions per second in the debit credit benchmark. A typical configuration of the Vax 3600 costs about $235,000, which translates to price performance of $38,000 per transaction per second."

**OBS-016** `market-data` · `dec` · `dectp` · 1988
Stress-test (non-compliant variation): 4-CPU VAX 8974 delivered 104 TPS flat-file with relaxed spec (90% in 1.3 sec, relaxed recovery). See OBS-004 for methodology note.
> "a four-processor VAX8974 delivers 104 transactions per second in a flat file application."

---

### Chart 3 — K$/TPS Price/Performance (Hughes, ~line 1076–1086)
*Image: `media/DECtp-1988-price-performance.png`*

**OBS-017** `market-data` · `ibm` · `dectp` · 1988
IBM 3090/200E Debit-Credit price/performance: $8,700 K$/TPS. Highest cost-per-TPS on the chart by an order of magnitude.
> "There's an $8.7 million IBM 3090 doing 38 transactions per second in a debit credit environment."
Image: leftmost blue bar, Chart 3.

**OBS-018** `market-data` · `dec` · `dectp` · 1988
DEC VAX 8830 Debit-Credit price/performance: $1,800 K$/TPS.
> "VAX 8830 for 1.8 million." Hughes: "price performance at half the cost of a comparable IBM system."
Image: first green bar, Chart 3.

**OBS-019** `market-data` · `dec` · `dectp` · 1988
DEC VAX 8820 Debit-Credit price/performance: $1,500 K$/TPS. Image: Chart 3 bar read.

**OBS-020** `market-data` · `dec` · `dectp` · 1988
DEC VAX 6240 Debit-Credit price/performance: $1,000 K$/TPS. Image: Chart 3 bar read.

**OBS-021** `market-data` · `tandem-computers` · `dectp` · 1988
Tandem VLX 4-CPU Debit-Credit price/performance: $1,800 K$/TPS. Image: Chart 3 blue bar (Tandem); same K$/TPS as DEC VAX 8830 but at lower absolute TPS.

**OBS-022** `market-data` · `dec` · `dectp` · 1988
DEC VAX 6220 Debit-Credit price/performance: $700 K$/TPS. Lowest K$/TPS on the chart — best price/performance result shown. Image: rightmost green bar, Chart 3.

---

### Chart 4 — Average System Cost for TP (Glorioso, ~line 762–766)
*Image: `media/DECtp-1988-avg-system-cost.png`*

**OBS-023** `market-data` · `dec` · `dectp` · 1988
Digital average TP system cost: $50K. Image: Chart 4 green bar.

**OBS-024** `market-data` · `tandem-computers` · `dectp` · 1988
Tandem average TP system cost: $112.5K — 2.25× Digital's average cost.
> "On average, the cost of a Tandem system doing the same TP job is double the cost of a Digital system."
Image: Chart 4 purple bar.

**OBS-025** `market-data` · `ibm` · `dectp` · 1988
IBM average TP system cost: $187.5K — 3.75× Digital's average cost.
> "The cost of an IBM system doing the same job is triple the cost of a Digital system."
Image: Chart 4 blue bar.

---

### Kastner connection (personal-recollection)

**OBS-026** `personal-recollection` · `dec` · `dectp` · 1988
Peter S. Kastner was present at the DECtp press conference as a Debit-Credit subject matter expert, invited to take questions from the press. He traveled to the event by helicopter with Ken Olsen and Bob Glorioso to the DEC private jet. Kastner prepared this transcript and the four benchmark chart images from the Computer History Museum video recording (CHM catalogue #102717571). His memoir account of the DECtp era is in `volume-1-ch06-dec-mainframes-last-stand-1987-1988` (Westwood Midnight Ambush, OBS-016 to OBS-035).

---

## Source metadata

- **Archive:** Computer History Museum
- **Catalogue number:** 102717571
- **Accession:** X2675.2004
- **Format:** U-Matic video, 00:58:18
- **Credit line:** Gift of Hewlett-Packard Company
- **Archive collection:** Digital Equipment Corporation records
- **Archive hierarchy:** DEC libraries' A/V holdings
- **Language:** English
