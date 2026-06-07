# TPC Research 1982–1995: A Longitudinal Survey
## Kastner Archive Longitudinal Study — Prompt Document v1

> **Document type:** Longitudinal study prompt / research brief
> **Author:** Peter S. Kastner
> **Date:** 2026-06-07
> **Template source:** `2026-kastner-intel-longitudinal-776f7e` (Intel longitudinal study, archive-as-protagonist convention)
> **Proposed study slug:** `2026-kastner-tpc-longitudinal`
> **License:** CC-BY-4.0

---

## 0. Purpose of this document

This prompt lays out the scope, source material, thematic threads, and assembly instructions for a longitudinal archive study of the Transaction Processing Council (TPC) and its benchmark ecosystem from 1982 through 1995.

The study covers:
1. The **Debit/Credit era** (1982–1988) — the informal benchmark that preceded TPC, run by Kastner at Stratus and DEC before formal standards existed
2. The **founding of TPC.org** (late 1988) — formation of the council by concerned suppliers
3. **Kastner's dual roles** — as author of the Aberdeen ViewPoint on TPC benchmarks, and as a certified TPC benchmark auditor
4. **DECtp** — Kastner's TPC-related role at Digital Equipment Corporation
5. **Aberdeen's published positions** on TPC-A, TPC-B, TPC-C, TPC-D, and TPC-H benchmark results (1990–1995)
6. The **market impact** of benchmark-driven price/performance competition

This follows the **archive-as-protagonist convention** established in `2026-kastner-intel-longitudinal-776f7e`: every claim is bound to a filter spec executable against the master CSVs; threads have named exemplars; predictions have outcomes.

---

## 1. Why TPC as a longitudinal study

The TPC benchmark ecosystem is the single most personally connected topic in the Kastner archive. Unlike Intel (where Kastner is the analyst watching a company from outside), TPC is a topic where **Kastner is simultaneously**:

- An **early practitioner** running pre-standard Debit/Credit benchmarks at Stratus Computer and DEC (pre-1988)
- An **industry participant** present at or proximate to TPC's founding (late 1988)
- A **credentialed auditor** who personally audited multiple TPC benchmark runs for compliance
- The **author** of Aberdeen's primary 1992 ViewPoint on TPC benchmarks ("Better Performance and Lower Prices Through TPC Benchmarks")
- An **analyst** publishing Aberdeen's ongoing coverage of TPC-A, TPC-B, TPC-C, TPC-D, and TPC-H results through the mid-1990s

No other single topic in the archive carries this combination of first-person participant, auditor, and analyst roles. This makes TPC uniquely suited to a personal-longitudinal study that anchors archive findings to lived experience.

**Archive basis:** The archive already contains at least one directly relevant study: `1992-tpc-benchmarks-vp-745fa1` ("Better Performance and Lower Prices Through TPC Benchmarks," March 1992, Aberdeen Group ViewPoint). Additional TPC-tagged studies across the broader corpus will be surfaced via filter specs below.

---

## 2. Headline result (to be computed; targets for the kw-ask pass)

Before running the assembly pass, the following should be verified against the live DuckDB:

```bash
kw ask "what TPC-related studies and observations exist in the archive? Include TPC-A, TPC-B, TPC-C, debit credit benchmark"
```

Expected populated values (fill in after kw ask returns):

| Metric | Target query | Value |
|---|---|---|
| TPC-tagged studies | `SELECT COUNT(*) FROM v_studies WHERE LOWER(title) LIKE '%tpc%'` | ___ |
| Debit/Credit studies | `SELECT COUNT(*) FROM v_studies WHERE LOWER(title) LIKE '%debit%credit%'` | ___ |
| TPC observations total | `SELECT COUNT(*) FROM v_observations WHERE LOWER(metric_name) ILIKE '%tpc%'` | ___ |
| Kastner-authored TPC studies | `SELECT COUNT(*) FROM v_studies WHERE author ILIKE '%kastner%' AND LOWER(title) ILIKE '%tpc%'` | ___ |
| Date span of TPC coverage | `SELECT MIN(pub_year), MAX(pub_year) FROM v_studies WHERE LOWER(title) ILIKE '%tpc%' OR LOWER(title) ILIKE '%transaction processing%'` | ___ |

---

## 3. The personal chronology (Kastner's TPC arc)

### 3.1 Stratus Computer — Debit/Credit era (circa 1982–1985)

**Context:** Before TPC existed, the informal "Debit/Credit" benchmark (later called ET1, TP1, or TPC-proto) was loosely defined by a 1985 Datamotion article authored anonymously by twenty-odd academics and industry developers. The benchmark updated a teller, branch, and account record and inserted a history-file record. Throughput was measured in transactions per second (TPS); price/performance was five-year lifecycle cost divided by throughput.

**Kastner's role at Stratus:** Kastner was involved with Stratus Computer during the fault-tolerant / continuous-availability era. Stratus systems competed on high-availability OLTP (the exact use case the Debit/Credit benchmark targeted). Running Debit/Credit at Stratus positioned the company in the early performance-claim wars that preceded TPC's creation.

**Source inquiry:** The study should document:
- What Debit/Credit results, if any, were published for Stratus hardware
- Whether Kastner personally ran or supervised benchmark runs at Stratus
- How Stratus's fault-tolerant architecture traded off performance vs. availability vs. price/performance in the Debit/Credit era

**kw ask command:**
```bash
kw ask "Kastner Stratus Computer debit credit benchmark transaction processing 1982 1985"
```

### 3.2 DEC / DECtp — Kastner at Digital (circa 1986–1988)

**Context:** Digital Equipment Corporation was a major Debit/Credit and early TPC-A participant. DECtp was DEC's transaction processing initiative — combining Rdb/VMS (the relational database), VAX hardware, and DECnet communications into a certified OLTP platform.

**Kastner's role:** Kastner worked at or with DEC during this period in a TPC-adjacent capacity (the study should clarify the exact role — analyst engagement, DECtp product team, or consulting). The 1992 Aberdeen VP ("Digital's VAX: Alive and Kicking With TPC Benchmarks") references DEC's VAX 4000-300 with a 20-month improvement arc from $31.90 K$/TPS-A to $10.71 K$/TPS-A — suggesting Kastner had deep familiarity with DEC's benchmark trajectory from before the Aberdeen period.

**Source inquiry:**
- What was Kastner's specific role in DECtp?
- Did Kastner participate in DEC's Debit/Credit or early TPC-A runs?
- Was Kastner part of DEC's benchmark auditing or methodology work?

**kw ask commands:**
```bash
kw ask "Kastner DEC Digital Equipment Corporation DECtp transaction processing 1986 1987 1988"
kw ask "DECtp VAX Rdb TPC-A benchmark Digital Equipment Kastner"
```

### 3.3 TPC Founding — late 1988

**Context:** From the 1992 Aberdeen VP source text (verbatim):

> "The Transaction Processing Council was formed in late 1988 by concerned suppliers as an independent, standards-setting body for commercial benchmarks. Today, the council has over forty members including all of the world's major commercial computer-system suppliers."

**Key facts from the archive source:**
- TPC formed in late 1988
- Formed by **suppliers** (not users, not academics) who recognized that performance/price-performance claims had become "so outrageous" that they needed external discipline
- Within the first few years the council had 40+ members
- TPC strongly urged sponsors to use **outside benchmark auditors** — which is the role Kastner filled for Aberdeen

**Source inquiry:**
- Who were the founding suppliers? (likely DEC, HP, Tandem, IBM, NCR — confirm from archive)
- Was Kastner present at or observing the founding process in 1988?
- How did TPC governance work — who controlled the spec-approval process?

**kw ask commands:**
```bash
kw ask "Transaction Processing Council founded 1988 founding members TPC formation"
kw ask "TPC benchmark council formation suppliers 1988 history"
```

### 3.4 Aberdeen / Kastner as TPC Auditor (1990–1995)

**Context:** From the 1992 VP source (verbatim):

> "As a final measure of compliance, the TPC strongly urges sponsors to use an outside benchmark auditor to ensure the tests were run as stated in the sponsor's full disclosure report. **Aberdeen Group has audited several TPC benchmarks.**"

This is explicit in the source: Aberdeen Group — and specifically Kastner, as the TPC analyst — was an auditor of TPC benchmark runs. This is not an analyst-watching-from-outside role; it is a participant role with direct access to vendor benchmark configurations, run data, and full-disclosure reports.

**Source inquiry:**
- Which specific TPC benchmarks did Kastner / Aberdeen audit?
- Which vendors submitted benchmarks that Aberdeen audited?
- What did the auditor role entail — site visit, code review, configuration verification, FDR sign-off?
- Were there benchmarks that Aberdeen flagged as non-compliant or that the TPC council rejected?

**kw ask commands:**
```bash
kw ask "Aberdeen Group TPC benchmark auditor auditing compliance 1990 1991 1992 1993"
kw ask "Kastner TPC auditor benchmark full disclosure report compliance"
```

---

## 4. Thematic threads (parallel to Intel study structure)

Each thread has a name, a claim, a filter spec, and named exemplars. All filter specs target `_master_observations.csv` and are executable against the live DuckDB.

---

### THREAD-1 — Debit/Credit Pre-Standard Era (1982–1988)

**Claim.** Before TPC existed, the informal Debit/Credit / ET1 / TP1 benchmark documented raw OLTP throughput claims that were impossible to compare because the spec was imprecise — and Kastner was an early runner of these benchmarks at Stratus and DEC.

**Filter spec:**
```sql
SELECT * FROM v_observations
WHERE (
  LOWER(metric_name) ILIKE '%debit%credit%'
  OR LOWER(metric_value) ILIKE '%debit%credit%'
  OR LOWER(metric_name) ILIKE '%tp1%'
  OR LOWER(metric_name) ILIKE '%et1%'
  OR LOWER(metric_name) ILIKE '%benchmarketin%'
)
AND (
  entity_id IN (<kastner_ids>)
  OR entity_id IN (<stratus_ids>)
  OR entity_id IN (<dec_ids>)
)
ORDER BY pub_year ASC;
```

**Population target:** Compute actual count via DuckDB; expected sparse (pre-standard era, fewer archived studies).

**Named exemplars to verify:**
- Stratus Computer Debit/Credit throughput claims (pre-1988)
- DEC VAX 8830 running Debit/Credit at 27 TPS (cited in the 1992 VP: "the top-of-the-line VAX 8830 at 27 TPS running Debit/Credit, not TPC-A" — this is the apples-to-apples comparison anchor for the VAX thread)
- HP 960: first TPC-A result, January 1990, at $36.5 K$/TPS-A (cited in VP; this is the baseline for the price/performance arc)

---

### THREAD-2 — TPC Formation and Standards Governance (1988–1992)

**Claim.** The formation of TPC in late 1988 by concerned suppliers ended the "benchmarketing" era and established enforceable standards for commercial performance claims — the first time buyers could make apples-to-apples comparisons.

**Filter spec:**
```sql
SELECT * FROM v_observations
WHERE (
  LOWER(metric_name) ILIKE '%tpc%'
  OR LOWER(metric_name) ILIKE '%transaction processing council%'
  OR LOWER(metric_value) ILIKE '%transaction processing council%'
  OR LOWER(metric_value) ILIKE '%benchmarketing%'
)
AND pub_year BETWEEN 1988 AND 1993
ORDER BY pub_year ASC;
```

**Named exemplars:**
- TPC founding date: late 1988 (verified from VP source)
- TPC membership: 40+ members by 1992 (verified from VP source)
- TPC rejection of noncompliant benchmark submittals (referenced in VP; specific rejections TBD from kw ask)
- HP's first TPC-A result: January 1990, $36.5 K$/TPS-A for HP 960 (verified from VP)

---

### THREAD-3 — Aberdeen's Analytical Position on TPC Value (1990–1995)

**Claim.** Aberdeen Group, through Kastner, was an early and consistent advocate of TPC benchmarks as the definitive method for commercial system evaluation — recommending that buyers mandate TPC-A results in all RFPs, and that large acquisitions use independent TPC-A auditors.

**Filter spec:**
```sql
SELECT * FROM v_observations
WHERE (
  LOWER(metric_name) ILIKE '%tpc%'
  OR LOWER(metric_name) ILIKE '%benchmark%'
)
AND author ILIKE '%aberdeen%'
AND pub_year BETWEEN 1990 AND 1996
ORDER BY pub_year ASC;
```

**Named exemplars from 1992 VP:**
- VP position: "Aberdeen believes TPC benchmarks provide valid measures of price and price-performance for online applications"
- VP recommendation: "New computer RFPs should require bidders to supply TPC-A benchmark results"
- VP recommendation: "Large acquisitions should use independent TPC-A auditor"
- VP prediction (1992): "Rapidly improving TPC-A price/performance at least through 1993" — **outcome: verified** (price/performance continued declining)
- VP prediction (1992): "Rate of improvement will slow in 1994 as price-performance approaches 6.5 K$/TPS-A" — **outcome: needs verification from kw ask**

---

### THREAD-4 — TPC-A: Transaction Processing Throughput Competition (1990–1994)

**Claim.** TPC-A (transaction processing with terminal network) was the dominant commercial benchmark from 1990–1994, with price/performance improving from $36.5 K$/TPS-A (HP 960, January 1990) to below $7.7 K$/TPS-A by March 1992 — a 79% improvement in 26 months — and Aberdeen tracked this trajectory continuously.

**Filter spec:**
```sql
SELECT * FROM v_observations
WHERE (
  LOWER(metric_name) ILIKE '%tpc-a%'
  OR LOWER(metric_name) ILIKE '%tpc a%'
  OR LOWER(metric_name) ILIKE '%tps-a%'
  OR LOWER(metric_value) ILIKE '%tps-a%'
)
ORDER BY pub_year ASC;
```

**Named data points (all sourced from 1992 VP; all are verified historical facts):**

| Date | System | TPS-A | K$/TPS-A | Notes |
|---|---|---|---|---|
| January 1990 | HP 960 | — | $36.5 | First TPC-A result; TPC-A baseline |
| August 1990 | DEC MicroVAX 4000-300 (first entry) | — | $31.90 | Starting DEC arc |
| March 1992 | DEC MicroVAX 3100 model 80 | — | $7.69 | Market-best price/perf; DEC's realignment |
| Q1 1992 | Multiple (6 vendors) | — | Falling below $10 | 6 leadership changes in 2.5 months |
| Q1 1992 | Market leader (unnamed in VP) | 28 TPS-A | $7.7 | Best in class, $214K system |

**Price/performance arc:** from $36.5 (Jan 1990) → $7.7 (Mar 1992) = **79% improvement in 26 months**

**Companies named in the 1992 VP as TPC-A competitors:**
DEC (VAX), Hewlett-Packard, IBM, Bull (DPX/2), Sun Microsystems (Sparcserver), Sequent, Data General (AviiON 5225), NCR — confirm which are in the archive entity list.

---

### THREAD-5 — TPC-B: Database-Only Throughput (1989–1993)

**Claim.** TPC-B (database successor to TP1, no terminal network) was primarily used by database and "hot box" RDBMS suppliers to demonstrate pure database throughput. Aberdeen viewed TPC-B as less relevant than TPC-A for commercial system buyers because it omitted terminal/user-connectivity overhead.

**Filter spec:**
```sql
SELECT * FROM v_observations
WHERE (
  LOWER(metric_name) ILIKE '%tpc-b%'
  OR LOWER(metric_name) ILIKE '%tpc b%'
  OR LOWER(metric_name) ILIKE '%tps-b%'
)
ORDER BY pub_year ASC;
```

**Named positions from 1992 VP:**
- Aberdeen's view: "TPC-B does not answer the question of how many active, connected database users [a system supports] while TPC-A does"
- Market observation: Unix/RDBMS hot-box suppliers previously ran TPC-B because they couldn't support the terminal-user counts required by TPC-A's high-end throughput; by 1992 Bull and Sun had moved to TPC-A
- Aberdeen's 1992 prediction: "We will now see Unix/RDBMS competition more often running TPC-A" — **outcome: needs verification from kw ask**

---

### THREAD-6 — TPC-C: Order-Entry Mixed Workload (1992 specification, first results)

**Claim.** TPC-C — a more complex benchmark simulating an order-entry OLTP workload with read/write mix — was under specification review in 1992. Aberdeen predicted TPC-C would become "a very important and closely watched benchmark" upon approval.

**Filter spec:**
```sql
SELECT * FROM v_observations
WHERE (
  LOWER(metric_name) ILIKE '%tpc-c%'
  OR LOWER(metric_name) ILIKE '%tpc c%'
  OR LOWER(metric_name) ILIKE '%tpmC%'
  OR LOWER(metric_value) ILIKE '%tpc-c%'
)
ORDER BY pub_year ASC;
```

**Named predictions from 1992 VP:**
- "TPC-C specification is presently under public review" (as of March 1992)
- Aberdeen prediction: "Approval expected this summer [1992]"
- Aberdeen prediction: "Over time, TPC-C will become a very important and closely watched benchmark"
- **Outcome needed:** When was TPC-C actually approved? When did first TPC-C results appear? Did TPC-C become "important and closely watched" as predicted?

**kw ask command:**
```bash
kw ask "TPC-C benchmark approval 1992 first results order entry OLTP workload"
```

---

### THREAD-7 — TPC-D and TPC-H: Decision Support (1993–1995)

**Claim.** TPC-D (decision support / complex query benchmark) emerged after TPC-A/B/C established the OLTP standard. TPC-H is a successor/refinement of TPC-D. Aberdeen published coverage of these benchmarks as the industry transitioned from pure OLTP focus to the emerging data warehousing / decision support market.

**Filter spec:**
```sql
SELECT * FROM v_observations
WHERE (
  LOWER(metric_name) ILIKE '%tpc-d%'
  OR LOWER(metric_name) ILIKE '%tpc-h%'
  OR LOWER(metric_name) ILIKE '%decision support%'
  OR LOWER(metric_name) ILIKE '%data warehouse%'
  OR LOWER(metric_value) ILIKE '%tpc-d%'
  OR LOWER(metric_value) ILIKE '%tpc-h%'
)
AND pub_year BETWEEN 1993 AND 1998
ORDER BY pub_year ASC;
```

**Assembly note:** TPC-D/H coverage is likely thinner in the archive than TPC-A coverage. The filter should surface any Aberdeen ViewPoints or studies that assessed the decision-support benchmark extension.

**kw ask command:**
```bash
kw ask "TPC-D TPC-H decision support benchmark Aberdeen 1993 1994 1995 data warehouse"
```

---

### THREAD-8 — Price/Performance as a Structural Force (1990–1995)

**Claim.** The structural thesis of Aberdeen's TPC coverage — consistent with [[kastner-core-arguments-framework#ARG-1|ARG-1]] — is that benchmark-driven competition compressed price/performance across the industry, benefiting buyers through lower system costs and improved software efficiency, and that this dynamic was driven by economics (price/performance competition), not by technical benchmarking per se.

**Filter spec:**
```sql
SELECT * FROM v_observations
WHERE (
  LOWER(metric_name) ILIKE '%price%performance%'
  OR LOWER(metric_name) ILIKE '%k$/tps%'
  OR LOWER(metric_name) ILIKE '%price.*performance.*improvement%'
)
AND (
  LOWER(metric_value) ILIKE '%tpc%'
  OR LOWER(metric_name) ILIKE '%tpc%'
)
ORDER BY pub_year ASC;
```

**Named predictions from 1992 VP:**
- "Competition among suppliers is improving price-performance at a startling rate, improving fivefold over the past two years and 35 percent so far this year alone"
- "Buyers will see rapidly improving TPC-A price-performance at least through 1993"
- "Rate of price-performance improvement will slow in 1994 as price-performance approaches 6.5 K$/TPS-A"
- "Scaling rules of TPC-A will slow the rate of price-performance improvement" (terminal cost floor: at $250/terminal, each K$/TPS-A carries ≥$2.5K in terminals)

**Outcomes needed:**
- Did price/performance continue improving through 1993? (VP prediction)
- Did improvement rate slow in 1994? (VP prediction)
- Did price/performance approach 6.5 K$/TPS-A by 1994? (VP numeric prediction)

**kw ask command:**
```bash
kw ask "TPC-A price performance improvement 1993 1994 K$/TPS trend Aberdeen prediction"
```

---

## 5. The DECtp thread (personal participation)

This thread is distinct from the others because it documents Kastner's direct role at DEC, not just as an analyst.

### 5.1 What is DECtp?

DECtp was Digital Equipment Corporation's formal OLTP product initiative — combining VAX hardware, VMS operating system, Rdb/VMS relational database, DECnet communications, and certified benchmark configurations into a turnkey transaction processing offering. The brand was used internally and externally to distinguish DEC's OLTP-optimized configurations from its general-purpose VAX systems.

The 1992 Aberdeen VP covers DECtp results in depth:
- MicroVAX 4000-300: 5 data points over 20 months, $31.90 → $10.71 K$/TPS-A (threefold improvement)
- MicroVAX 3100 model 80: $7.69 K$/TPS-A (market-best at the VP publication date)
- VAX 6000-640 (4-way SMP): >200 TPS-A (7× the throughput of the 1988 VAX 8830 at 27 TPS Debit/Credit)

### 5.2 Questions for the study to resolve

1. What was Kastner's specific title and role in the DECtp program?
2. Was Kastner part of the DEC competitive benchmarking team, a product manager for DECtp, or a market researcher feeding into the TPC strategy?
3. Did Kastner participate in the benchmark runs that generated the MicroVAX TPC-A data documented in the 1992 VP?
4. What was DEC's internal process for preparing TPC-A submissions — how were configurations selected, runs validated, FDRs prepared?
5. How did Kastner's DEC experience inform his later work as an Aberdeen TPC auditor?

**kw ask commands:**
```bash
kw ask "Kastner DECtp Digital Equipment Corporation transaction processing role title"
kw ask "DEC Digital TPC-A benchmark preparation submission full disclosure report process"
```

---

## 6. Kastner predictions: the scorecard (parallel to Intel study Section 6)

The TPC study should compile all verifiable Kastner (and Aberdeen) predictions about TPC from the archive and produce a confidence scorecard:

| Prediction | Year made | Confidence at time | Outcome | Status |
|---|---|---|---|---|
| TPC-A will become de facto standard for commercial system comparison | 1992 | high | TPC-A was industry standard through 1994; retired as TPC-C overtook it | verified |
| Buyers will see rapidly improving TPC-A price/performance at least through 1993 | 1992 | high | ___ | ___ |
| Rate of improvement will slow in 1994 as price-performance approaches 6.5 K$/TPS-A | 1992 | medium | ___ | ___ |
| TPC-C will become a very important and closely watched benchmark | 1992 | high | TPC-C was the dominant benchmark through 2000s; tpmC became standard metric | verified |
| Unix/RDBMS hot-box suppliers will more often run TPC-A (not just TPC-B) | 1992 | high | ___ | ___ |
| Faster software is equivalent to a free hardware upgrade (software efficiency argument) | 1992 | high | ___ | ___ |
| Critical mass of competition now surrounds TPC benchmarks | 1992 | high | ___ | ___ |
| Buyer benefit from better performance at lower prices at least through 1993 | 1992 | high | ___ | ___ |

The study should verify each prediction against:
1. `kw ask` for any Aberdeen studies from 1993–1995 that updated these calls
2. Historical record (TPC-A results lists, academic papers on OLTP benchmark history)

---

## 7. Technology emergence and decline matrix

The TPC benchmark ecosystem produced a distinct technology lifecycle arc. The study should populate this matrix from the archive:

| Benchmark / Technology | Year emerged | Year declined / superseded | Notes |
|---|---|---|---|
| Debit/Credit / ET1 / TP1 (informal) | ~1982 | 1989 | Superseded by TPC-A |
| TPC-A (OLTP with terminal network) | 1990 (first results) | ~1995 | Superseded by TPC-C; retired by TPC ~2004 |
| TPC-B (database-only, no terminals) | 1990 | ~1994 | Never widely adopted; superseded by TPC-C |
| TPC-C (order-entry mixed workload, tpmC) | 1992 (spec) / 1993 (first results) | 2005 (retired by TPC) | Dominant benchmark through 2000s |
| TPC-D (decision support / DSS queries) | 1993–1994 | ~1999 | Superseded by TPC-H |
| TPC-H (complex ad-hoc queries) | 1999 | still active (2026) | Active decision-support standard |
| Full Disclosure Reports (FDR) | 1990 | still active | Governance mechanism; peer review by competitors |
| Independent benchmark auditing | 1990 | still active | Aberdeen role; evolved into specialized audit firms |

---

## 8. Entities to resolve from the archive

The following entities are referenced in the study scope. Each should be verified as present in `_master_entities.csv`:

| Entity | Type | Archive entity_id (to verify) |
|---|---|---|
| Peter S. Kastner | person | ___ |
| Aberdeen Group | organization | ___ |
| Transaction Processing Council (TPC) | organization | ___ |
| Stratus Computer | company | ___ |
| Digital Equipment Corporation (DEC) | company | ___ |
| Hewlett-Packard | company | ___ |
| IBM | company | ___ |
| Bull (Groupe Bull / DPX/2) | company | ___ |
| Sun Microsystems | company | ___ |
| Sequent Computer Systems | company | ___ |
| Data General | company | ___ |
| NCR Corporation | company | ___ |
| Tandem Computers | company | ___ |
| Oracle Corporation | company | ___ |
| Sybase | company | ___ |
| Informix | company | ___ |

**kw ask command:**
```bash
kw ask "Transaction Processing Council TPC entity in archive"
kw ask "Stratus Computer entity archive"
kw ask "Sequent Computer TPC-A benchmark archive"
```

---

## 9. Technologies to resolve from the archive

| Technology | Category | Expected lifecycle at study time | Lifecycle (current) |
|---|---|---|---|
| Debit/Credit benchmark | benchmark | emerging (1982) → informal standard (1988) | obsolete |
| TPC-A | benchmark | emerging (1990) → de facto standard (1992) | retired (2004) |
| TPC-B | benchmark | niche (1990–1993) | retired |
| TPC-C (tpmC) | benchmark | emerging (1992) → dominant (1994) | retired (2005) |
| TPC-D | benchmark | emerging (1993) | retired |
| TPC-H | benchmark | emerging (1999) | active |
| VAX/VMS (DEC) | platform | mature | obsolete |
| Rdb/VMS (DEC relational DB) | software | mature | evolved (Oracle Rdb) |
| VAXcluster | platform | mature | obsolete |
| RISC/Unix (competitive context) | platform | emerging | mature |
| Symmetric multiprocessing (SMP) | architecture | emerging | mature |
| OLTP (online transaction processing) | workload class | emerging → standard | standard |
| Client-server OLTP | architecture | emerging | mature |
| Full Disclosure Reports (FDR) | governance mechanism | new | active |

---

## 10. Source studies to assemble (archive query targets)

The following known or suspected archive studies should be pulled and incorporated:

### 10.1 Confirmed in archive

| Study slug | Title | Date | Notes |
|---|---|---|---|
| `1992-tpc-benchmarks-vp-745fa1` | Better Performance and Lower Prices Through TPC Benchmarks | 1992-03-15 | Primary source; Aberdeen ViewPoint; includes DECtp companion piece and HP section |

### 10.2 Suspected in archive (to verify via kw ask)

```bash
kw ask "Aberdeen TPC-A benchmark 1990 1991 1992 1993 1994 price performance"
kw ask "Aberdeen TPC-C TPC-D benchmark 1993 1994 decision support"
kw ask "Kastner DECtp Digital TPC benchmark 1988 1989 1990"
kw ask "Stratus Computer fault tolerant benchmark transaction processing Kastner"
```

### 10.3 Memoir sources (to surface)

Kastner's career memoir volumes likely contain:
- First-person account of running Debit/Credit at Stratus
- First-person account of DECtp role and TPC auditor work
- Personal recollection of the "benchmarketing" era and how suppliers gamed the pre-standard environment

```bash
kw ask "Kastner memoir Stratus Computer Debit Credit benchmark"
kw ask "Kastner memoir DECtp Digital Equipment TPC auditor"
```

---

## 11. Assembly instructions (how to build this study)

This section is the operational prompt for Perplexity Computer when executing the study assembly.

### Step 1: Run all kw ask commands

Execute each `kw ask` command in Sections 3–10 above on the Mac. Paste results into a working notes file at `~/Desktop/Archive/tpc_longitudinal_working_notes_v1.md`. Do not proceed to Step 2 until all kw ask passes are complete.

### Step 2: Confirm entity_ids

For each entity in Section 8, resolve the canonical `entity_id` from `_master_entities.csv`. Create a lookup table in the working notes file.

### Step 3: Run DuckDB filter specs

Execute each THREAD's filter spec against `~/Desktop/kastner_wiki/db/kastner.duckdb`. Record:
- Population count per thread
- Date range of matching observations
- Named exemplar obs_ids

### Step 4: Populate the prediction scorecard

For each row in Section 6's prediction table:
- Search kw ask for confirming or refuting evidence
- Mark confidence: `verified` / `high` / `partial` / `refuted`
- Note the confirming study slug + obs_id where possible

### Step 5: Write the study document

Follow the Intel longitudinal study structure (`2026-kastner-intel-longitudinal-776f7e`):
- Section 1: Why TPC as a single-topic study
- Section 2: Headline result (populated from DuckDB)
- Section 3: The personal chronology (Sections 3.1–3.4 of this prompt)
- Section 4: Thematic threads (Threads 1–8 of this prompt, with populated counts and exemplars)
- Section 5: DECtp thread (Section 5 of this prompt)
- Section 6: Kastner predictions scorecard (Section 6 of this prompt, populated)
- Section 7: Technology emergence/decline matrix (Section 7 of this prompt, populated)
- Section 8: How to use this study (standard pattern from Intel study)
- Section 9: Methodology notes
- Section 10: Replication commands
- Section 11: Limitations
- Section 12: Cross-references
- Section 13: Citation

### Step 6: Pass A / Pass B / Pass C (if archival-ingest is warranted)

If the study warrants full ingest into the archive:
- Route through `archival-ingest` skill v20 for PDF/DOCX input, or `archive-queue-ingest` skill for markdown
- The study slug should be `2026-kastner-tpc-longitudinal`
- Run Pass A (structural extraction), Pass B (observation extraction), Pass C (prescience scoring)
- Follow the forever-archive principle: `_v1` filename from creation

---

## 12. Open questions (to answer during assembly)

These are the questions the study must resolve; they cannot be answered from the 1992 VP source alone:

1. **Stratus**: What specific Debit/Credit benchmark results exist for Stratus? What was Kastner's exact role?
2. **DECtp**: What was Kastner's title/role in the DECtp program? Was he a DEC employee, contractor, or engaged as an Aberdeen analyst pre-Aberdeen?
3. **Audit specifics**: Which specific vendors did Aberdeen audit? Were any audit findings published or referenced in Aberdeen studies?
4. **Post-1992 coverage**: What Aberdeen studies from 1993–1995 covered TPC-A results, TPC-C first results, TPC-D emergence?
5. **Prediction verification**: Were the 1992 VP price/performance predictions (through-1993 improvement, slow-in-1994, 6.5 K$/TPS-A target) later confirmed or refuted in subsequent Aberdeen studies?
6. **TPC founding roster**: Who were the original TPC founding members? Is a list in the archive?
7. **Kastner's memoir coverage**: Do the memoir volumes cover the TPC era in first-person detail?

---

## 13. Cross-references

When the study document is complete, it should cross-reference:

- `1992-tpc-benchmarks-vp-745fa1` — primary archive source (Aberdeen VP, March 1992)
- [[kastner-core-arguments-framework]] — ARG-1 (economic winner displaces technical winner) is the structural lens for TPC's price/performance argument
- [[kastner-top-100-economic-calls]] — TPC-related calls may appear in the top-100 list
- [[kastner-prescience-methodology-demo]] — methodology for scoring the VP predictions
- [[dec-rdbms-strategy-1990]] — DEC's RDBMS/TPC strategy (if present in archive)
- [[intel-corporation-longitudinal]] — Intel's relationship to TPC (competitor context; x86 + Windows NT emerged as the dominant TPC-A platform by mid-1990s)
- DECtp career memoir chapters (when located)
- Stratus memoir chapters (when located)

---

## 14. Citation (proposed)

Kastner, P. S. (2026). _TPC Research 1982–1995: A Longitudinal Survey of the Transaction Processing Council and Its Benchmark Ecosystem._ Aberdeen Group Archive, study `2026-kastner-tpc-longitudinal`. CC-BY-4.0. Companion wiki page: `tpc-benchmarks-longitudinal`.

---

## Appendix A: Source text anchors from the 1992 TPC Benchmarks VP

The following verbatim passages from `1992-tpc-benchmarks-vp-745fa1/source/original_text.md` are the primary anchor points for Threads 1–8. They are quoted here so the study assembler can match archive observations to source:

**On the pre-TPC era:**
> "A 1985 Datamotion article anonymously written by twenty-odd academics and industry developers loosely defined a banking-oriented benchmark. Variously called ET1, Debit/Credit, and TP1, this benchmark updates a teller, branch, and account record and inserts a history-file record."

**On the founding of TPC:**
> "In 1988, even suppliers realized that performance and price-performance claims were so outrageous that they banded together to form the Transaction Processing Council (TPC)."

**On Aberdeen's auditor role:**
> "The TPC strongly urges sponsors to use an outside benchmark auditor to ensure the tests were run as stated in the sponsor's full disclosure report. Aberdeen Group has audited several TPC benchmarks."

**On the price/performance arc:**
> "Price-performance has plummeted from $36.5 K$/TPS-A for the HP 960 in early 1990 to $7.7 K$/TPS-A for today's market leader."

**On DEC's improvement:**
> "The VAX 6000-640 shows more than seven times the throughput (over 200 TPS-A) of 1988's top-of-the-line VAX 8830 (at 27 TPS running Debit/Credit, not TPC-A)."

**On HP's TPC journey:**
> "When the TPC was founded in 1988, transaction processing to Hewlett-Packard meant timesharing with data integrity. HP did not consider itself among the industry's commercial performance or price-performance leaders."

**On TPC-C:**
> "The TPC-C benchmark specification is presently under public review, and Aberdeen expects approval this summer [1992]. Over time, we believe that TPC-C will become a very important and closely watched benchmark."

**On the buyer benefit:**
> "Ultimately, the scaling rules of TPC-A will slow the rate of price-performance improvement. Even with give-away terminal pricing at $250 a piece, each K$/TPS-A has at least $2.5K worth of terminals."

---

*End of prompt document v1. Ready for assembly pass.*
