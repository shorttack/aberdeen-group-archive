# TPC Research 1982–1995: A Longitudinal Survey
## Kastner Archive Longitudinal Study — Prompt Document v3

> **Document type:** Longitudinal study prompt / research brief
> **Author:** Peter S. Kastner
> **Date:** 2026-06-07
> **Template source:** `2026-kastner-intel-longitudinal-776f7e` (Intel longitudinal study, archive-as-protagonist convention)
> **Proposed study slug:** `2026-kastner-tpc-longitudinal`
> **License:** CC-BY-4.0
> **v2 changes:** Incorporated live kw-ask results (2026-06-07). Added Aberdeen Transaction Services practice area; confirmed Stratus audit; added Tandem 1985 study; resolved entity slug proliferation; corrected TPC-A spec date (November 1989); added `dectp` and `stratus-tpf` technology slugs.
> **v3 changes (updated):** Added §9.1c memoir chapter assembly guide (ch05/ch06/ch07 study_ids, Westwood Midnight Ambush OBS refs, specsmanship bridge, WORKLIST §21 tagging gap note, DuckDB pull query). Original v3 changes: Incorporated three source documents attached by Pete (2026-06-07): Tandem TR 85.2 (1985 full technical report), DECtp DEC Journal Vol 3 No 1 Winter 1991, TPC Evolution memo (Levine/Gray/Kiss/Kohler, 1993). Added Appendix C with source text anchors. Updated THREAD-1 with 1985 pricing methodology distinction (terminals excluded). Updated THREAD-2/THREAD-7 with TPC Evolution data (8→42 members, tpmC metric, 5-transaction-type breakdown). Updated THREAD-5 with 33 K$/tps → 6 K$/tps arc from primary source. Updated §9.1 source studies table. Added Walt Kohler as named bridge figure (DEC Littleton, co-author DECtp Journal TPC-A paper and TPC Evolution memo). Kastner NOT named in DECtp Journal — his role is ecosystem participant/auditor, not journal author.

---

## 0. Purpose of this document

This prompt lays out the scope, source material, thematic threads, and assembly instructions for a longitudinal archive study of the Transaction Processing Council (TPC) and its benchmark ecosystem from 1982 through 1995.

The study covers:
1. The **Debit/Credit era** (1982–1988) — the informal benchmark that preceded TPC, including the 1985 Tandem Debit/Credit paper and Kastner's benchmark work at Stratus and DEC before formal standards existed
2. The **founding of TPC** (late 1988) and spec approval (November 1989)
3. **Kastner's dual roles** — as author of the Aberdeen ViewPoint on TPC benchmarks, and as founder of "Aberdeen Transaction Services" (the named practice area for TPC auditing)
4. **Stratus TPC-A audit** — confirmed in archive: Aberdeen audited Stratus's TPC-A submission specifically
5. **DECtp** — `dectp` technology slug confirmed in archive; Kastner's TPC-related role at Digital Equipment Corporation
6. **Aberdeen's published positions** on TPC-A, TPC-B, TPC-C benchmark results (1990–1995); TPC-D and TPC-H coverage to be verified
7. The **market impact** of benchmark-driven price/performance competition

This follows the **archive-as-protagonist convention** established in `2026-kastner-intel-longitudinal-776f7e`: every claim is bound to a filter spec executable against the master CSVs; threads have named exemplars; predictions have outcomes.

---

## 1. Why TPC as a longitudinal study

The TPC benchmark ecosystem is the single most personally connected topic in the Kastner archive. Unlike Intel (where Kastner is the analyst watching a company from outside), TPC is a topic where **Kastner is simultaneously**:

- An **early practitioner** running pre-standard Debit/Credit benchmarks at Stratus Computer and DEC (pre-1988), with DEC results published at CMG 1989
- An **industry participant** present at or proximate to TPC's founding (late 1988)
- The **founder of Aberdeen Transaction Services** — a named practice area within Aberdeen Group specifically for TPC benchmark auditing
- A **credentialed auditor** who personally audited multiple TPC benchmark runs for compliance, including specifically Stratus's TPC-A submission (confirmed in archive)
- The **author** of Aberdeen's primary 1992 ViewPoint on TPC benchmarks ("Better Performance and Lower Prices Through TPC Benchmarks")
- An **analyst** publishing Aberdeen's ongoing coverage of TPC-A, TPC-B, TPC-C results through the mid-1990s

No other single topic in the archive carries this combination of first-person participant, named-practice founder, auditor, and analyst roles. This makes TPC uniquely suited to a personal-longitudinal study that anchors archive findings to lived experience.

**Archive basis (confirmed via kw-ask 2026-06-07):**

| Study / Slug | Type | Date | Notes |
|---|---|---|---|
| `study-tandem-tr-85-2-debitcredit-1985-ca207a` | study | 1985 | Tandem Debit/Credit paper — earliest TPC-related archive source |
| `study-1992-tpc-benchmarks-vp-ed0e0d` | study | 1992-03-15 | Aberdeen VP — primary source |
| `1992-tpc-benchmarks-vp-745fa1` | study | 1992-03-15 | Archive copy (same document, two slugs — dedupe needed) |
| `tpc-a` | technology | — | TPC-A benchmark entity |
| `tpc-benchmark-a` | technology | — | TPC-A alternate slug |
| `tpc-c` | technology | — | TPC-C benchmark entity |
| `tpcc-benchmark` | technology | — | TPC-C alternate slug |
| `tpc-h` | technology | — | TPC-H benchmark entity |
| `tpc-h-benchmark` | technology | — | TPC-H alternate slug |
| `debit-credit` | technology | — | Debit/Credit benchmark entity |
| `tp1-et1-debit-credit` | technology | — | TP1/ET1 variant |
| `t88-05` | technology | — | 1988-era technology node |
| `dectp` | technology | — | DEC Transaction Processing platform — **confirmed in archive** |
| `stratus-tpf` | technology | — | Stratus Transaction Processing Facility — **confirmed in archive** |
| `tp-monitors` | technology | — | TP monitor category |
| `tps` | technology | — | Transactions-per-second metric |

**Entity slug proliferation (known issue — all refer to TPC):**
`transaction-processing-council` · `tpc-council` · `tpc-org` · `tpc` · `transaction-processing-performance-council`
The filter specs below use `OR` across all five to avoid undercounting.

---

## 2. Headline result (to be computed during assembly pass)

Before running the assembly pass, verify against the live DuckDB:

```bash
# Entity coverage across all TPC slugs
duckdb ~/Desktop/kastner_wiki/db/kastner.duckdb -c "
SELECT COUNT(*) AS tpc_obs
FROM v_observations
WHERE entity_id IN (
  'transaction-processing-council','tpc-council','tpc-org','tpc',
  'transaction-processing-performance-council'
);"

# Technology coverage across all TPC benchmark slugs
duckdb ~/Desktop/kastner_wiki/db/kastner.duckdb -c "
SELECT entity_id, COUNT(*) AS obs_count
FROM v_observations
WHERE entity_id IN (
  'tpc-a','tpc-benchmark-a','tpc-a-benchmark',
  'tpc-c','tpcc-benchmark',
  'tpc-h','tpc-h-benchmark',
  'tpc-benchmark','tech-tpc',
  'debit-credit','tp1-et1-debit-credit','t88-05',
  'dectp','stratus-tpf','tps','tp-monitors'
)
GROUP BY entity_id
ORDER BY obs_count DESC;"

# Study coverage
duckdb ~/Desktop/kastner_wiki/db/kastner.duckdb -c "
SELECT study_id, title, pub_year
FROM v_studies
WHERE LOWER(title) ILIKE '%tpc%'
   OR LOWER(title) ILIKE '%debit%credit%'
   OR LOWER(title) ILIKE '%transaction processing%'
ORDER BY pub_year ASC;"
```

Target table (fill in after DuckDB runs):

| Metric | Value |
|---|---|
| TPC org entity observations | ___ |
| TPC benchmark technology observations (all slugs) | ___ |
| DECtp observations | ___ |
| Stratus-TPF observations | ___ |
| Studies with TPC in title | ___ |
| Date span | 1985 → ___ |
| Confirmed audit study (Stratus TPC-A) | confirmed |
| Aberdeen Transaction Services named in archive | confirmed |

---

## 3. The personal chronology (Kastner's TPC arc)

### 3.1 Stratus Computer — Debit/Credit era (circa 1982–1985)

**Context:** Before TPC existed, the informal "Debit/Credit" benchmark (also called ET1 and TP1) was loosely defined by a 1985 Datamation article authored anonymously by twenty-odd academics and industry developers. The benchmark updated a teller, branch, and account record and inserted a history-file record. Throughput was measured in TPS; price/performance was five-year lifecycle cost divided by throughput.

**Archive confirms:** `stratus-tpf` technology slug is present in the archive — Stratus's Transaction Processing Facility is already a tracked technology. The 1985 Tandem paper (`study-tandem-tr-85-2-debitcredit-1985-ca207a`) is the earliest archive source for the pre-TPC era.

**kw-ask confirmed:** Aberdeen audited Stratus's TPC-A submission specifically (sourced from `tpc-a` technology page).

**Questions to resolve in assembly:**
- What were Stratus's specific Debit/Credit / TPC-A results?
- What was Kastner's exact title and role at Stratus during the pre-TPC era?
- Does the Stratus audit appear in the memoir volumes?

**kw ask commands:**
```bash
kw ask "Stratus Computer TPC-A audit Aberdeen Transaction Services Kastner benchmark"
kw ask "stratus-tpf technology Stratus transaction processing fault tolerant benchmark results"
```

### 3.2 DEC / DECtp — Kastner at Digital (circa 1986–1988)

**Context:** Digital Equipment Corporation was a major Debit/Credit and early TPC-A participant. `dectp` technology slug confirmed in the archive. DEC published Debit/Credit results at CMG 1989 (sourced from `debit-credit` technology page in kw-ask).

**From the 1992 VP (verbatim):**
> "The VAX 6000-640 shows more than seven times the throughput (over 200 TPS-A) of 1988's top-of-the-line VAX 8830 (at 27 TPS running Debit/Credit, not TPC-A)."

This establishes the DEC 1988 Debit/Credit baseline: VAX 8830 at 27 TPS. The same system later achieved 200+ TPS-A under TPC-A — a 7× throughput improvement through software optimization (Rdb/VMS) and hardware refinement.

**kw ask commands:**
```bash
kw ask "dectp DEC transaction processing Digital Equipment Kastner role DECtp"
kw ask "VAX 8830 debit credit 27 TPS Digital Equipment CMG 1989"
kw ask "Rdb VMS DEC TPC-A benchmark improvement performance"
```

### 3.3 TPC Founding — late 1988; spec approval November 1989

**Two-phase timeline (corrected from v1):**
- **Late 1988:** TPC formed by concerned suppliers
- **November 1989:** TPC-A specification formally approved
- **January 1990:** First TPC-A result published (HP 960, $36.5 K$/TPS-A)

**From the 1992 VP (verbatim):**
> "In 1988, even suppliers realized that performance and price-performance claims were so outrageous that they banded together to form the Transaction Processing Council (TPC)."

**Archive note:** Five entity slugs exist for TPC (`transaction-processing-council`, `tpc-council`, `tpc-org`, `tpc`, `transaction-processing-performance-council`). The formal name was "Transaction Processing Council" not "Transaction Processing Performance Council" — the five-slug version may be a data-entry error in an observation that used the longer form. Flag for `_master_entities.csv` normalization.

**kw ask commands:**
```bash
kw ask "TPC founding 1988 Transaction Processing Council formation founding members suppliers"
kw ask "TPC-A specification approval November 1989 benchmark standard"
```

### 3.4 Aberdeen Transaction Services — Kastner as TPC Auditor (1990–1995)

**Archive confirms (from kw-ask `tpc-a` technology page):**
> "Peter Kastner utilized his OLTP technical depth and knowledge of TPC methodology to become an accredited benchmark auditor, establishing **'Aberdeen Transaction Services'** as a practice area. Aberdeen audited several TPC benchmarks, including **Stratus's TPC-A submission**."

This is a key finding: the auditing wasn't an informal Aberdeen activity — it was a named practice area, "Aberdeen Transaction Services," with Kastner as the lead accredited auditor. This elevates the personal participation thread significantly.

**From the 1992 VP (verbatim):**
> "As a final measure of compliance, the TPC strongly urges sponsors to use an outside benchmark auditor. Aberdeen Group has audited several TPC benchmarks."

**Questions to resolve:**
- When was "Aberdeen Transaction Services" founded? What was its formal scope?
- Which vendors (besides Stratus) submitted benchmarks that Aberdeen/ATS audited?
- What did the audit process involve — site visit, code review, configuration verification, FDR sign-off?
- Did ATS generate revenue for Aberdeen? Was it a consulting line or a research-support function?
- Are there archived Aberdeen ATS deliverables (audit reports, FDR sign-offs)?

**kw ask commands:**
```bash
kw ask "Aberdeen Transaction Services TPC audit practice area Kastner accredited auditor"
kw ask "TPC benchmark audit vendors Aberdeen 1990 1991 1992 1993 full disclosure report"
```

---

## 4. Thematic threads

Each thread has a name, a claim, a filter spec, and named exemplars. All filter specs target `_master_observations.csv` and are executable against the live DuckDB.

---

### THREAD-1 — Debit/Credit Pre-Standard Era (1982–1988)

**Claim.** Before TPC existed, the informal Debit/Credit / ET1 / TP1 benchmark documented raw OLTP throughput claims that were impossible to compare because the spec was imprecise. Measurements were "at best ambiguous and always the subject of intense controversy" (sourced from `tp1-et1-debit-credit` technology page in archive). Kastner was an early runner of these benchmarks at Stratus and DEC.

**Source document note (v3).** The full Tandem TR 85.2 (February 1985) — now in hand — is more than the condensed Datamation article. It defines **three benchmarks**: Debitcredit (interactive OLTP), Scan (minibatch), and Sort (utility). Key methodological points:
- **Terminal count**: 100 terminals per TPS (100-second think time) — this is the 1985 framework, carried forward into the pre-TPC Debit/Credit era
- **Pricing methodology (1985)**: 5-year capital cost **EXCLUDING** communications lines, terminals, development, and operations. This is the **opposite** of what TPC-A later required. When TPC-A forced terminals into price/performance (40–60% of total cost per the 1993 TPC Evolution memo), it fundamentally changed the competitive landscape.
- **Transaction spec**: banking scenario, 4 tables (account, teller, branch, history), X.25 terminal, block-mode, Cobol, 95th-percentile 1-second response time
- **TPS throughput metric, 5-year capital cost, price/performance ratio** — the same three-axis framework Aberdeen used in its 1992 VP
- **Workload lineage**: TPC Evolution (1993) traces TPC-A's workload to a 1974 banking application, making Tandem 85.2 a mid-point in the lineage

**Archive anchors:**
- `study-tandem-tr-85-2-debitcredit-1985-ca207a` — 1985 Tandem paper; earliest archive source
- `debit-credit` — technology slug (DEC CMG 1989 results; multiple VAX configurations)
- `tp1-et1-debit-credit` — technology slug (broader TP1/ET1 lineage)
- `t88-05` — 1988-era technology node
- `stratus-tpf` — Stratus Transaction Processing Facility
- `dectp` — DEC Transaction Processing platform

**Filter spec:**
```sql
SELECT * FROM v_observations
WHERE entity_id IN (
  'debit-credit','tp1-et1-debit-credit','t88-05',
  'stratus-tpf','dectp'
)
   OR (
     LOWER(metric_name) ILIKE '%debit%credit%'
     OR LOWER(metric_name) ILIKE '%tp1%'
     OR LOWER(metric_name) ILIKE '%et1%'
     OR LOWER(metric_name) ILIKE '%benchmarketin%'
   )
ORDER BY pub_year ASC;
```

**Named exemplars:**
- DEC VAX 8830 at 27 TPS Debit/Credit (1988 baseline; source: 1992 VP)
- Tandem 1985 Debit/Credit paper (archive: `study-tandem-tr-85-2-debitcredit-1985-ca207a`)
- Stratus Debit/Credit results (pre-1990; to verify from kw-ask)
- HP 960 first TPC-A result January 1990 at $36.5 K$/TPS-A (the transition point from pre-standard to TPC era)
- **Pricing methodology shift**: 1985 Tandem paper excludes terminals from cost; TPC-A spec (1989) requires terminal inclusion — a deliberate change that made the price/performance metric reflect buyer-visible total cost. Research question: did Aberdeen's VP comment on this methodological shift?

---

### THREAD-2 — TPC Formation and Standards Governance (1988–1992)

**Claim.** The formation of TPC in late 1988 by concerned suppliers — followed by spec approval in November 1989 — ended the "benchmarketing" era and established enforceable standards for commercial performance claims. For the first time, buyers could make apples-to-apples comparisons.

**Archive anchors:**
- All five TPC org entity slugs: `transaction-processing-council`, `tpc-council`, `tpc-org`, `tpc`, `transaction-processing-performance-council`
- `benchmark-methodology` technology slug (returned in kw-ask results)

**Filter spec:**
```sql
SELECT * FROM v_observations
WHERE entity_id IN (
  'transaction-processing-council','tpc-council','tpc-org','tpc',
  'transaction-processing-performance-council'
)
   OR LOWER(metric_name) ILIKE '%benchmarketing%'
   OR LOWER(metric_name) ILIKE '%transaction processing council%'
ORDER BY pub_year ASC;
```

**Named exemplars:**
- TPC founding: late 1988 (verified from VP source)
- TPC-A spec approved: November 1989 (sourced from `tpc-benchmark-a`)
- **TPC membership arc** (v3 addition from TPC Evolution memo, primary source): **8 founding vendors** → **42 members by 1993**. This is the strongest evidence of TPC's institutional legitimacy growth.
- First TPC-A result: January 1990, HP 960, $36.5 K$/TPS-A
- TPC rejection of noncompliant benchmark submittals (referenced in VP; specific rejections TBD)
- **Walt Kohler** (DEC Littleton MA) — bridge figure. Co-authored the DECtp Journal paper on TPC-A multi-level analytical model (1991, with Hsu/Rogers/Bahaa-El-Din). Yun-Ping Hsu bio in same journal: "also participated in the TPC Benchmark A standardization activity during 1989." Kohler also co-authored the 1993 TPC Evolution memo (with Levine/Tandem, Gray/DEC SF Systems Center, Kiss/IBM). He connects the DEC TPC-A implementation, the 1989 spec work, and the 1993 argument for TPC-C.

---

### THREAD-3 — Aberdeen Transaction Services and the Auditor Role (1990–1995)

**Claim.** Aberdeen Group, under Kastner's leadership, established "Aberdeen Transaction Services" as a named TPC auditing practice. As an accredited auditor, Kastner personally audited multiple TPC-A submissions, including Stratus's — making Aberdeen one of the few independent audit firms in the early TPC ecosystem.

**Archive anchors:**
- `tpc-a` technology page (source of Aberdeen Transaction Services confirmation)
- `study-1992-tpc-benchmarks-vp-ed0e0d` (VP study where the auditor role is mentioned)
- `stratus-tpf` (Stratus platform audited by Aberdeen)

**Filter spec:**
```sql
SELECT * FROM v_observations
WHERE (
  LOWER(metric_name) ILIKE '%aberdeen transaction%'
  OR LOWER(metric_name) ILIKE '%benchmark auditor%'
  OR LOWER(metric_name) ILIKE '%audit%tpc%'
  OR LOWER(metric_name) ILIKE '%full disclosure%'
)
   OR (
  entity_id IN ('tpc-a','tpc-benchmark-a','tpc-a-benchmark')
  AND author ILIKE '%kastner%'
)
ORDER BY pub_year ASC;
```

**Named exemplars:**
- Aberdeen Transaction Services founded (date TBD from kw-ask)
- Stratus TPC-A audit (confirmed in archive; details TBD)
- VP recommendation (1992): "Large acquisitions should use independent TPC-A auditor"
- Aberdeen's auditing of "several TPC benchmarks" (VP source, March 1992)

---

### THREAD-4 — Aberdeen's Analytical Position on TPC Value (1990–1995)

**Claim.** Aberdeen Group, through Kastner, was an early and consistent advocate of TPC benchmarks as the definitive method for commercial system evaluation — recommending that buyers mandate TPC-A results in all RFPs.

**Filter spec:**
```sql
SELECT * FROM v_observations
WHERE entity_id IN (
  'tpc-a','tpc-benchmark-a','tpc-a-benchmark',
  'transaction-processing-council','tpc-council','tpc-org','tpc'
)
AND pub_year BETWEEN 1990 AND 1996
ORDER BY pub_year ASC;
```

**Named predictions from 1992 VP (all need outcome verification):**

| Prediction | Year | Confidence | Outcome needed |
|---|---|---|---|
| TPC-A will become de facto standard | 1992 | high | verified (TPC-A dominated through 1994–1995) |
| Buyers will see rapidly improving TPC-A price/perf through 1993 | 1992 | high | ___ |
| Rate of improvement will slow in 1994 as P/P approaches 6.5 K$/TPS-A | 1992 | medium | ___ |
| TPC-C will become "very important and closely watched" | 1992 | high | verified (tpmC dominated 1993–2005) |
| Unix/RDBMS hot-boxes will more often run TPC-A | 1992 | high | ___ |
| Faster software = free hardware upgrade (software efficiency argument) | 1992 | high | ___ |
| Oracle, IBM, and Tandem/HP will dominate TP markets through 1990s | (implicit, kw-ask sourced) | high | verified (per archive: `tpc-benchmark-a`) |

**kw ask commands:**
```bash
kw ask "Aberdeen TPC-A prediction 1993 1994 price performance trend verification"
kw ask "TPC-A 6.5 K dollars TPS price performance 1994 actual result"
```

---

### THREAD-5 — TPC-A: Price/Performance Competition Arc (1990–1994)

**Claim.** TPC-A drove a 79% improvement in K$/TPS-A from January 1990 to March 1992, and continued improving through 1993–94. This was the most dramatic benchmark-driven price/performance compression in enterprise computing history to that date.

**v3 addition — primary source arc from TPC Evolution (1993):** The full price/performance arc from the Levine/Gray/Kiss/Kohler memo is:
- **$33 K$/tps** in 1989 (at TPC-A spec approval, baseline)
- **$6 K$/tps** in 1993
- **Throughput**: exceeded **1,000 tps** by 1993
- This is an 82% improvement in four years — consistent with the 79% VP data (which measured a shorter window, Jan 1990 to March 1992).

The TPC Evolution memo also documents **six specific problems with TPC-A** that made it obsolete by 1993: (1) pricing model loopholes (package pricing, prepaid maintenance); (2) terminal domination of P/P metric (40–60% of cost); (3) ad hoc client-server configurations; (4) specialized features (Oracle7 discrete transactions as a TPC special); (5) P/P improvement outpacing customer purchasing reality; (6) benchmarketing games 1987–1990. These six problems are research material for Thread 5's arc and the THREAD-2 governance thread.

**Archive anchors:**
- `study-1992-tpc-benchmarks-vp-ed0e0d` — primary source; all VP data points
- `tpc-a` — technology entity
- `tpc-benchmark-a` — alternate slug
- `tps` — transactions-per-second metric entity

**Filter spec:**
```sql
SELECT * FROM v_observations
WHERE entity_id IN (
  'tpc-a','tpc-benchmark-a','tpc-a-benchmark','tps'
)
   OR LOWER(metric_name) ILIKE '%tps-a%'
   OR LOWER(metric_name) ILIKE '%k$/tps%'
ORDER BY pub_year ASC;
```

**Named data points (all sourced from 1992 VP; all verified historical facts):**

| Date | System | TPS-A | K$/TPS-A | Delta |
|---|---|---|---|---|
| January 1990 | HP 960 | — | $36.5 | Baseline (first TPC-A result) |
| August 1990 | DEC MicroVAX 4000-300 (entry) | — | $31.90 | DEC arc start |
| Q1 1992 (6 changes) | Multiple vendors | — | <$10 | 6 leadership changes in 2.5 months |
| March 1992 | DEC MicroVAX 3100 model 80 | — | $7.69 | Market-best; DEC price realignment |
| March 1992 | Market leader (unnamed) | 28 TPS-A | $7.7 | $214K system; 79% improvement from 1990 |

**The DEC arc in detail (from VP):**
DEC MicroVAX 4000-300 from August 1990 → March 1992: 5 data points, 3 price cuts, 1 performance increase (+50%), resulting in $31.90 → $10.71 K$/TPS-A. The performance improvement came from Rdb/VMS software efficiency, not hardware.

**Companies named in 1992 VP as TPC-A competitors:**
DEC, HP, IBM, Bull (DPX/2), Sun Microsystems (Sparcserver), Sequent, Data General (AviiON 5225)

**Market structure note (from kw-ask `tpc-benchmark-a`):**
"DEC participated in the 1989 standardization activity but did not achieve their goal of TP market leadership; Oracle, IBM, and Tandem/HP dominated the markets through the 1990s." This is a forward-looking correction to the 1992 VP's optimistic DEC framing.

**kw ask commands:**
```bash
kw ask "TPC-A benchmark results 1990 1991 1992 1993 price performance leaders HP DEC IBM Bull Sun"
kw ask "DEC MicroVAX TPC-A 1990 1991 1992 Rdb VMS performance improvement arc"
```

---

### THREAD-6 — TPC-B: Database-Only Throughput (1989–1993)

**Claim.** TPC-B (database successor to TP1, no terminal network) was primarily used by database and "hot box" RDBMS suppliers to demonstrate pure database throughput. Aberdeen viewed TPC-B as less relevant than TPC-A for commercial system buyers.

**Filter spec:**
```sql
SELECT * FROM v_observations
WHERE entity_id IN ('tpc-benchmark','tech-tpc')
   OR LOWER(metric_name) ILIKE '%tpc-b%'
   OR LOWER(metric_name) ILIKE '%tps-b%'
ORDER BY pub_year ASC;
```

**Note:** No dedicated `tpc-b` technology slug appeared in the kw-ask results — this may mean TPC-B observations are filed under `tpc-benchmark` (generic) or not tagged at all. The filter casts wide.

**Named positions from 1992 VP:**
- Aberdeen: TPC-B does not answer the question of how many active, connected database users a system supports (TPC-A does)
- Market: Unix/RDBMS hot-box suppliers ran TPC-B because they couldn't support the terminal-user counts required by TPC-A
- Aberdeen 1992 prediction: "We will now see Unix/RDBMS competition more often running TPC-A" — **outcome: needs kw-ask verification**

---

### THREAD-7 — TPC-C: Order-Entry Mixed Workload (1992 spec → dominant 1993–2005)

**Claim.** TPC-C — a more complex benchmark simulating an order-entry OLTP workload with read/write mix — was approved in 1992 and became the dominant commercial benchmark through 2005. Aberdeen predicted this outcome correctly in March 1992.

**Archive anchors:** `tpc-c` · `tpcc-benchmark` (both confirmed in kw-ask)

**Filter spec:**
```sql
SELECT * FROM v_observations
WHERE entity_id IN ('tpc-c','tpcc-benchmark')
   OR LOWER(metric_name) ILIKE '%tpc-c%'
   OR LOWER(metric_name) ILIKE '%tpmc%'
ORDER BY pub_year ASC;
```

**Named predictions from 1992 VP:**
- "TPC-C specification is presently under public review" (March 1992)
- Aberdeen prediction: "Approval expected this summer [1992]"
- Aberdeen prediction: "Over time, TPC-C will become a very important and closely watched benchmark"

**v3 addition — TPC-C technical specification from primary source (TPC Evolution, September 1993):**
The Levine/Gray/Kiss/Kohler memo documents TPC-C's design rationale and full spec:
- **Metric**: **tpmC** (transactions per minute C) — not tpsC; the unit change reflects the more realistic transaction mix
- **Transaction types (5)**: New-Order 43.5%, Payment 43.5%, Delivery 4.4%, Order-Status 4.4%, Stock-Level 4.4%
- **Table count**: 9 tables (versus 4 in Debit/Credit and TPC-A)
- **Workload weight**: described as ~10× heavier than TPC-A
- **Scenario**: wholesale supplier with full-screen UI and location transparency
- **TPC-C improvements vs. TPC-A**: no terminal-domination pricing problem; mixed read/write workload; multi-type transaction ratios fixed; no benchmarketing loop-holes for package pricing
- **Approved**: 1992; first results published by 1993

**Outcome (historical, verifiable):**
- TPC-C approved: 1992 (within the predicted window)
- First TPC-C results: 1993
- tpmC became the dominant OLTP metric through the 1990s and 2000s
- TPC-C retired by TPC in 2005
- **Prediction status: verified**

---

### THREAD-8 — TPC-D and TPC-H: Decision Support (1993–present)

**Claim.** TPC-D (decision support benchmark) emerged as the industry transitioned from pure OLTP to data warehousing. TPC-H is TPC-D's successor and remains active as of 2026.

**Archive anchors:** `tpc-h` · `tpc-h-benchmark` (both confirmed in kw-ask)

**Note:** No `tpc-d` technology slug appeared in kw-ask results — TPC-D may be unfiled or subsumed under `tpc-h`. The filter should check both.

**Filter spec:**
```sql
SELECT * FROM v_observations
WHERE entity_id IN ('tpc-h','tpc-h-benchmark')
   OR LOWER(metric_name) ILIKE '%tpc-d%'
   OR LOWER(metric_name) ILIKE '%tpc-h%'
   OR LOWER(metric_name) ILIKE '%decision support%benchmark%'
AND pub_year BETWEEN 1993 AND 2000
ORDER BY pub_year ASC;
```

**kw ask command:**
```bash
kw ask "TPC-D TPC-H decision support benchmark Aberdeen 1993 1994 1995 data warehouse emergence"
```

---

### THREAD-9 — Price/Performance as a Structural Force (ARG-1 application)

**Claim.** The structural thesis — consistent with [[kastner-core-arguments-framework#ARG-1]] — is that benchmark-driven competition compressed price/performance across the enterprise computing industry, benefiting buyers through lower system costs and improved software efficiency. This dynamic was driven by **economics** (the benchmark made price/performance visible), not by technical benchmarking per se.

**Filter spec:**
```sql
SELECT * FROM v_observations
WHERE (
  LOWER(metric_name) ILIKE '%price%performance%'
  OR LOWER(metric_name) ILIKE '%k$/tps%'
  OR LOWER(metric_name) ILIKE '%price.*performance.*improvement%'
)
AND entity_id IN (
  'tpc-a','tpc-benchmark-a','tpc-a-benchmark',
  'transaction-processing-council','tpc-council','tpc-org','tpc'
)
ORDER BY pub_year ASC;
```

**Named predictions requiring outcome verification:**
- "Improving fivefold over the past two years" (by March 1992, from initial 1990 baseline) — **verified**: $36.5 → $7.7 = 79% drop = 4.7× improvement
- "Buyer benefit from better performance at lower prices at least through 1993" — **needs verification**
- "Rate of improvement will slow in 1994 as price-performance approaches 6.5 K$/TPS-A" — **needs verification**
- "Scaling rules of TPC-A will slow improvement" (terminal cost floor at $250/terminal = $2.5K minimum per K$/TPS-A) — **needs verification**

---

## 5. The DECtp thread (personal participation)

### 5.1 What is DECtp?

DECtp (`dectp` technology slug confirmed in archive) was Digital Equipment Corporation's formal OLTP product initiative — combining VAX hardware, VMS operating system, Rdb/VMS relational database, DECnet communications, and certified benchmark configurations into a turnkey transaction processing offering.

**Performance arc from 1992 VP:**
- MicroVAX 4000-300: 5 data points over 20 months, $31.90 → $10.71 K$/TPS-A (threefold improvement)
- MicroVAX 3100 model 80: $7.69 K$/TPS-A (market-best at VP publication date, March 1992)
- VAX 6000-640 (4-way SMP): >200 TPS-A (7× the 1988 VAX 8830 Debit/Credit baseline of 27 TPS)

**Market outcome (from kw-ask `tpc-benchmark-a`):**
"DEC participated in the 1989 standardization activity but did not achieve their goal of TP market leadership; Oracle, IBM, and Tandem/HP dominated the markets through the 1990s."

This is the study's most significant prediction-vs-outcome tension: the 1992 VP presents DEC as a price/performance leader; the archive's retrospective view is that DEC did not sustain TP market leadership despite that momentary lead.

### 5.2 Questions to resolve during assembly

1. What was Kastner's specific title and role in the DECtp program?
2. Was Kastner a DEC employee, contractor, or Aberdeen analyst engaged with the DEC account?
3. Did Kastner participate in the DEC CMG 1989 Debit/Credit publication?
4. How did DEC lose TP market leadership despite leading TPC-A price/performance in 1992?
5. What role did the DEC-Compaq acquisition (1998) play in the DECtp story?

**kw ask commands:**
```bash
kw ask "DECtp Kastner Digital Equipment Corporation transaction processing role personal involvement"
kw ask "DEC Digital TP market loss Oracle IBM Tandem 1993 1994 1995 transaction processing leadership"
kw ask "VAX 8830 Debit Credit 1988 1989 CMG publication DEC"
```

---

## 6. Kastner predictions and positions: the scorecard

| Prediction / Position | Source | Year | Confidence at time | Outcome | Status |
|---|---|---|---|---|---|
| TPC-A will become de facto standard | 1992 VP | 1992 | high | TPC-A dominated through 1994–95 | verified |
| Buyers will see rapidly improving TPC-A price/perf through 1993 | 1992 VP | 1992 | high | ___ | ___ |
| Rate of improvement slows in 1994, approaches 6.5 K$/TPS-A | 1992 VP | 1992 | medium | ___ | ___ |
| TPC-C will become "very important and closely watched" | 1992 VP | 1992 | high | tpmC dominant 1993–2005 | verified |
| Unix/RDBMS hot-boxes will more often run TPC-A | 1992 VP | 1992 | high | ___ | ___ |
| Faster software = free hardware upgrade | 1992 VP | 1992 | high | ___ | ___ |
| DEC has "best commercial price-performance" (March 1992) | 1992 VP | 1992 | high | DEC did not sustain TP leadership | partial (short-term verified; long-term refuted) |
| Oracle, IBM, Tandem/HP dominate TP through 1990s | kw-ask (`tpc-benchmark-a`) | ~1994+ | high | verified (per archive) | verified |

**Note on the DEC prediction:** The 1992 VP correctly identified DEC's momentary price/performance leadership. The archive's `tpc-benchmark-a` retrospective notes that DEC did not achieve its goal of TP market leadership — DEC's position eroded through the 1990s as Oracle+HP, IBM, and Tandem consolidated the market. The 1992 VP was accurate as of March 1992; it was overtaken by events (DEC's financial difficulties, the Alpha RISC transition, eventual Compaq acquisition in 1998).

---

## 7. Technology emergence and decline matrix

| Benchmark / Technology | Emerged | Declined / Superseded | Current status |
|---|---|---|---|
| Debit/Credit / ET1 / TP1 (informal) | ~1982 | 1989 (TPC-A spec) | obsolete |
| TPC-A (OLTP with terminal network) | Nov 1989 (spec) / Jan 1990 (first results) | ~1995 (TPC-C overtook) / retired ~2004 | retired |
| TPC-B (database-only, no terminals) | 1990 | ~1993–94 (never widely adopted) | retired |
| TPC-C (order-entry mixed workload, tpmC) | 1992 (spec) / 1993 (first results) | Retired 2005 by TPC | retired |
| TPC-D (decision support DSS queries) | ~1993–94 | ~1999 (superseded by TPC-H) | retired |
| TPC-H (complex ad-hoc queries) | 1999 | still active | **active** |
| DECtp (DEC OLTP platform) | ~1986 | ~1998 (Compaq acquisition) | obsolete |
| Stratus-TPF (Stratus Transaction Processing Facility) | ~1982 | ___ (when?) | ___ |
| Full Disclosure Reports (FDR) | 1990 (TPC requirement) | still active | **active** |
| Aberdeen Transaction Services (ATS) | ~1990 | ___ (when dissolved?) | ___ |
| VAX/VMS (competitive platform) | 1977 | ~2000 (HP-DEC era end) | obsolete |
| Rdb/VMS (DEC RDBMS) | ~1984 | Evolved into Oracle Rdb | evolved |
| TP monitors (CICS, Tuxedo, ACMS) | 1970s | still relevant | mature |

---

## 8. Entities to resolve from the archive

| Entity | Type | Archive slug (verified) | Notes |
|---|---|---|---|
| Transaction Processing Council (TPC) | organization | `tpc` / `tpc-council` / `tpc-org` / `transaction-processing-council` | **5 slugs — normalization needed** |
| Peter S. Kastner | person | ___ | verify slug |
| Aberdeen Group | organization | ___ | verify slug |
| Aberdeen Transaction Services | organization/practice | ___ | may be sub-entity of Aberdeen; verify |
| Stratus Computer | company | ___ | `stratus-tpf` technology confirmed; entity slug? |
| Digital Equipment Corporation | company | ___ | `dectp` technology confirmed; entity slug? |
| Hewlett-Packard | company | ___ | verify slug |
| IBM | company | ___ | verify slug |
| Bull (Groupe Bull / DPX/2) | company | ___ | verify slug |
| Sun Microsystems | company | ___ | verify slug |
| Sequent Computer Systems | company | ___ | verify slug |
| Data General | company | ___ | verify slug |
| Tandem Computers | company | ___ | verify slug |
| NCR Corporation | company | ___ | verify slug |
| Oracle Corporation | company | ___ | verify slug |

**kw ask command:**
```bash
kw ask "Stratus Computer entity archive slug Tandem Sequent Data General Bull Sparcserver TPC-A 1992"
```

---

## 9. Source studies to assemble

### 9.1 Confirmed in archive

| Slug | Title | Date | Status |
|---|---|---|---|
| `study-tandem-tr-85-2-debitcredit-1985-ca207a` | Tandem Debit/Credit TR 85-2 | 1985 | In archive + Pete has full TR |
| `study-1992-tpc-benchmarks-vp-ed0e0d` | Better Performance and Lower Prices Through TPC Benchmarks | 1992-03-15 | Primary anchor |
| `1992-tpc-benchmarks-vp-745fa1` | (same document, second slug — dedupe flag) | 1992-03-15 | Dedupe pending |
| `study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c` | DTJ v03-01 TP and Fault Tolerant | 1991 | In archive |

**Note:** `study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c` appeared in kw-ask results (similarity 0.583). This 1991 source may contain pre-TPC-A fault-tolerant benchmarking context relevant to the Stratus thread.

### 9.1b Pete-held source documents (not yet ingested — attached 2026-06-07)

These three documents were attached by Pete during the v3 session. They are committed to `kastner-author/2026-kastner-tpc-sources/` in the archive repo. They should be routed through `archive-queue-ingest` for formal ingestion when ready.

| File | Description | Archive repo path |
|---|---|---|
| `A-Measure-of-Transaction-Processing-Power-Tandem-85.2.pdf` | Tandem TR 85.2, February 1985. Full technical report behind the Datamation April 1, 1985 article. Defines Debitcredit, Scan, Sort benchmarks. Authors: Anon et al. Workload lineage for TPC-A. | `kastner-author/2026-kastner-tpc-sources/A-Measure-of-Transaction-Processing-Power-Tandem-85.2.pdf` |
| `DECtp-DEC-Journal-1991-q1-2.pdf` | Digital Technical Journal Vol 3 No 1, Winter 1991. Theme: Transaction Processing, Databases, and Fault-tolerant Systems. Contains Kohler/Hsu/Rogers/Bahaa-El-Din paper on DEC TPC-A implementation. Kastner NOT named — his role is ecosystem participant/auditor. | `kastner-author/2026-kastner-tpc-sources/DECtp-DEC-Journal-1991-q1-2.pdf` |
| `TPC_Evolution-3.txt` | "The Evolution of TPC Benchmarks: Why TPC-A and TPC-B are Obsolete." Levine (Tandem), Gray (DEC SF Systems Center), Kiss (IBM), Kohler (DEC Littleton). SFSC Technical Report 93.1, September 1993. Primary source for TPC membership arc (8→42), tpmC metric, TPC-C spec rationale, six TPC-A problems. | `kastner-author/2026-kastner-tpc-sources/TPC_Evolution-3.txt` |

### 9.1c Memoir chapters with confirmed TPC-era first-person content

Three memoir chapters cover the TPC era directly and should be read alongside the Aberdeen studies during assembly. Their observations are in `v_observations` but carry **no `tech_id` or `entity_id` TPC tags** — a known extraction gap tracked as WORKLIST §21. Pull them by `study_id` directly, not by slug.

| study_id | Chapter | Dates | Key TPC content |
|---|---|---|---|
| `volume-1-ch05-stratus-fault-tolerant-wars-1981-1987` | Ch05 | 1981–1987 | Stratus vs. Tandem competitive context; Kastner's Debit/Credit benchmark experience origins; fault-tolerant TP market framing |
| `volume-1-ch06-dec-mainframes-last-stand-1987-1988` | Ch06 | 1987–1988 | **Westwood Midnight Ambush** (OBS-016 to OBS-035): blind DEC vs. IBM 3090 Debit/Credit benchmark; specsmanship sidebar (OBS-034/035); DECtp press event and sales impact (OBS-032); Kastner's direct Debit/Credit role |
| `volume-1-ch07-founding-aberdeen-1988-1997` | Ch07 | 1988–1997 | Aberdeen founding; Aberdeen Transaction Services auditor role **not yet present in extracted observations** — content gap flagged in WORKLIST §21 |

**DuckDB query to pull all three chapters during assembly:**
```bash
duckdb ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb -c "
SELECT obs_id, study_id, entity_id, tech_id, obs_type, year_observed,
       metric_name, metric_value
FROM v_observations
WHERE study_id IN (
  'volume-1-ch05-stratus-fault-tolerant-wars-1981-1987',
  'volume-1-ch06-dec-mainframes-last-stand-1987-1988',
  'volume-1-ch07-founding-aberdeen-1988-1997'
)
ORDER BY study_id, obs_id;"
```

**Note on ch06 OBS-034/035 (specsmanship sidebar):** These two observations are the direct narrative bridge between the pre-TPC benchmarketing era and TPC's founding rationale. They belong in THREAD-1 and THREAD-2 of the study.

---

### 9.2 To surface via kw-ask

```bash
kw ask "Aberdeen ViewPoint TPC 1993 1994 1995 benchmark price performance"
kw ask "DTJ Digital Technical Journal TP fault tolerant 1991 benchmark"
kw ask "Kastner memoir TPC auditor Aberdeen Transaction Services personal account"
kw ask "Tandem Computers TPC-A TPC benchmark 1990 1991 1992 1993"
```

---

## 10. Open questions (to answer during assembly)

1. **Aberdeen Transaction Services:** When was ATS formally established? When (if ever) was it dissolved? What was its revenue/scope?
2. **Audit roster:** Beyond Stratus, which vendors did ATS audit? Are audit deliverables in the archive?
3. **DECtp role:** What was Kastner's exact title? When did the engagement begin/end?
4. **DEC's TP decline:** How did DEC go from March 1992 price/performance leader to "did not achieve TP market leadership"? What specific events caused this?
5. **TPC-D coverage:** Does the archive contain Aberdeen material on TPC-D? The kw-ask returned no `tpc-d` slug.
6. **Prediction verification:** The 6.5 K$/TPS-A prediction for 1994 — what did TPC-A actually reach?
7. **Memoir coverage:** Do the Kastner memoir volumes cover the TPC era in first-person detail? Which chapters?
8. **Slug normalization:** The five TPC entity slugs should be resolved to one canonical ID. Which is preferred? (`tpc-council` is probably the cleanest.)

---

## 11. Assembly instructions

### Step 1: Run all kw-ask commands in Sections 3–9

Execute each command on the Mac. Paste results into `~/Desktop/Archive/tpc_longitudinal_working_notes_v1.md`.

### Step 2: Run DuckDB filter specs for all threads

Execute each THREAD's filter spec. Record population count, date range, named exemplar obs_ids.

```bash
# Shape audit first (mandatory baseline)
duckdb ~/Desktop/kastner_wiki/db/kastner.duckdb -c "
SELECT
  (SELECT COUNT(*) FROM v_studies) AS studies,
  (SELECT COUNT(*) FROM v_observations) AS observations,
  (SELECT COUNT(*) FROM v_entities) AS entities,
  (SELECT COUNT(*) FROM v_technologies) AS technologies;"
```

### Step 3: Populate the prediction scorecard (Section 6)

For each blank row: search kw-ask for confirming/refuting evidence. Mark confidence. Note confirming study slug + obs_id.

### Step 4: Resolve entity slugs (Section 8)

Confirm canonical entity_id for each entity. Flag the TPC five-slug normalization as a masters-edit backlog item.

### Step 5: Write the study document

Follow `2026-kastner-intel-longitudinal-776f7e` structure:
- Section 1: Why TPC as a study
- Section 2: Headline result (populated)
- Section 3: The personal chronology (Kastner's TPC arc)
- Section 4: Thematic threads (populated with counts + exemplars)
- Section 5: DECtp personal participation thread
- Section 6: Prediction scorecard (populated)
- Section 7: Technology emergence/decline matrix (populated)
- Section 8: How to use this study
- Section 9: Methodology notes
- Section 10: Replication commands
- Section 11: Limitations
- Section 12: Cross-references
- Section 13: Citation

### Step 6: Flag for archival-ingest or archive-queue-ingest

When the study document is complete:
- Route through `archive-queue-ingest` skill (it's markdown; no need for heavyweight PDF/DOCX path)
- Proposed slug: `2026-kastner-tpc-longitudinal`
- Run Pass A → Pass B → Pass C per `archival-ingest` skill if prescience scoring is wanted
- File under `kastner-author/` in the repo

---

## 12. Cross-references (for the final study document)

- `study-tandem-tr-85-2-debitcredit-1985-ca207a` — earliest archive source (1985)
- `study-1992-tpc-benchmarks-vp-ed0e0d` — primary Aberdeen source (1992)
- `study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c` — 1991 fault-tolerant TP source
- [[kastner-core-arguments-framework]] — ARG-1 (economic winner displaces technical winner) is the structural lens; TPC is a perfect ARG-1 case study: the economic argument (price/performance transparency) beat the technical argument (proprietary benchmark gaming)
- [[kastner-top-100-economic-calls]] — TPC-related calls may appear
- [[kastner-prescience-methodology-demo]] — methodology for scoring predictions
- [[dec-rdbms-strategy-1990]] — DEC's RDBMS/TPC strategy context
- [[intel-corporation-longitudinal]] — Intel was not a TPC-A leader (x86 + NT emerged as the dominant TPC-C platform by mid-1990s, after the TPC-A era)
- DECtp memoir chapters (when located)
- Stratus memoir chapters (when located)

---

## 13. Citation (proposed)

Kastner, P. S. (2026). _TPC Research 1982–1995: A Longitudinal Survey of the Transaction Processing Council and Its Benchmark Ecosystem._ Aberdeen Group Archive, study `2026-kastner-tpc-longitudinal`. CC-BY-4.0. Companion wiki page: `tpc-benchmarks-longitudinal`.

---

## Appendix A: Source text anchors from the 1992 TPC Benchmarks VP

Verbatim passages from `study-1992-tpc-benchmarks-vp-ed0e0d` that anchor Threads 1–9:

**On the pre-TPC era:**
> "A 1985 Datamotion article anonymously written by twenty-odd academics and industry developers loosely defined a banking-oriented benchmark. Variously called ET1, Debit/Credit, and TP1..."

**On supplier chaos driving TPC:**
> "In 1988, even suppliers realized that performance and price-performance claims were so outrageous that they banded together to form the Transaction Processing Council (TPC)."

**On Aberdeen's auditor role:**
> "The TPC strongly urges sponsors to use an outside benchmark auditor. Aberdeen Group has audited several TPC benchmarks."

**On the price/performance arc:**
> "Price-performance has plummeted from $36.5 K$/TPS-A for the HP 960 in early 1990 to $7.7 K$/TPS-A for today's market leader."

**On software as the performance driver:**
> "The VAX performance improvement came from new efficiencies in VMS and Rdb, Digital's relational database. Software performance improvements essentially add capacity to existing sunk-cost hardware. They are the equivalent of a free midlife hardware kicker."

**On DEC's VAX 8830 Debit/Credit baseline:**
> "The VAX 6000-640 shows more than seven times the throughput (over 200 TPS-A) of 1988's top-of-the-line VAX 8830 (at 27 TPS running Debit/Credit, not TPC-A)."

**On TPC-C:**
> "The TPC-C benchmark specification is presently under public review, and Aberdeen expects approval this summer [1992]. Over time, we believe that TPC-C will become a very important and closely watched benchmark."

**On the terminal cost floor:**
> "Even with give-away terminal pricing at $250 a piece, each K$/TPS-A has at least $2.5K worth of terminals."

---

## Appendix B: kw-ask results incorporated in v2 (2026-06-07)

The following findings from the 2026-06-07 kw-ask session were incorporated into this v2 prompt:

1. **Aberdeen Transaction Services** confirmed as a named practice area (source: `tpc-a` technology page)
2. **Stratus TPC-A audit** confirmed specifically (source: `tpc-a` technology page)
3. **`dectp` technology slug** confirmed in archive (source: kw-ask entity results)
4. **`stratus-tpf` technology slug** confirmed in archive (source: kw-ask entity results)
5. **5 competing TPC entity slugs** identified; normalization flagged
6. **`study-tandem-tr-85-2-debitcredit-1985-ca207a`** (1985) confirmed as earliest archive source
7. **`study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c`** (1991) confirmed as relevant source
8. **TPC-A spec date corrected** to November 1989 (first results: January 1990)
9. **DEC TP market outcome** — archive's `tpc-benchmark-a` notes DEC did not achieve TP market leadership despite 1992 price/performance lead; Oracle, IBM, Tandem/HP dominated
10. **`benchmark-methodology`** technology slug confirmed (relevant to Thread 2 governance)
11. **DebitCredit controversy** confirmed — "at best ambiguous and always the subject of intense controversy" (source: `tp1-et1-debit-credit`)
12. **`tp-monitors`** technology slug confirmed (relevant to Thread 1 and DECtp thread)

---

*End of prompt document v2. Ready for assembly pass after remaining kw-ask commands are run.*

## Appendix C: Source text anchors from the three Pete-held documents (v3 additions)

### C.1 Tandem TR 85.2 (February 1985) — "A Measure of Transaction Processing Power"

**Three benchmarks defined:**
- **Debitcredit** (interactive OLTP) — the one that became the basis of TPC-A
- **Scan** (minibatch — scan-and-update of all accounts for a given teller)
- **Sort** (utility — sort the teller table by balance)

**Debitcredit transaction workload:**
Four database tables: account (100,000 rows), teller (10 per branch), branch (1), history (dynamic). A transaction performs: debit/credit to account balance, update teller and branch, write history record. 100 terminals per TPS, each with 100-second think time.

**Pricing methodology (1985 paper):**
> "5-year system cost" = capital cost only, **excluding** communication lines, terminals, system development, maintenance staff, floor space, power, cooling, operations. The 1985 paper **deliberately excluded terminals** from the price/performance metric. TPC-A reversed this.

**Response time requirement:**
> 95th-percentile response time ≤ 1 second at stated TPS load.

**The Datamation bridge:**
> This is the full technical report behind the condensed Datamation article "A Measure of Transaction Processing Power" published April 1, 1985. The TR predates and enables the 1985 public benchmark era.

---

### C.2 DECtp DEC Journal Vol 3 No 1, Winter 1991 — "Transaction Processing, Databases, and Fault-tolerant Systems"

**Primary paper for this thread:**
Kohler/Hsu/Rogers/Bahaa-El-Din, "Performance Evaluation of Transaction Processing Systems" (pp. 45–57). Describes DEC's TPC Benchmark A implementation in two configurations:
- **tpsA-Local**: all four database partitions on one VAX node
- **tpsA-Wide**: distributed across multiple nodes (4-node cluster)

Uses a **multi-level analytical model** validated against DEC hardware measurement results.

**Yun-Ping Hsu bio (from journal, primary source):**
> "Yun-Ping Hsu also participated in the **TPC Benchmark A standardization activity during 1989**."

This single sentence confirms DEC's participation in writing the TPC-A spec — connecting Walt Kohler's Littleton team to the 1989 standards body.

**Walt Kohler's institutional position:**
DEC Western Research Laboratory, Littleton MA. Kohler appears in both the DECtp Journal (1991) on TPC-A performance and the TPC Evolution memo (1993) as a co-author arguing TPC-C is needed. He is the single clearest named bridge between DEC's TPC-A work and TPC's evolution to TPC-C.

**Kastner's role in relation to this journal:**
Kastner is NOT named in the journal. His role is as a **DECtp ecosystem participant, CMG presenter, and later TPC auditor** — not a DEC employee or journal contributor. The journal documents the DEC technical context Kastner was operating in as an external analyst/auditor.

**Other DECtp Journal papers of note:**
- Bernstein/Emberton/Trehan: DECdta architecture (DEC Distributed Transaction Architecture)
- Speer/Storm: ACMS and DECintact transaction monitors
- Laing/Johnson/Landau: DECdtm VMS kernel transaction management
- Bruckert/Alonso/Melvin: VAXft 3000 fault-tolerant system

---

### C.3 TPC Evolution memo (September 1993) — "The Evolution of TPC Benchmarks: Why TPC-A and TPC-B are Obsolete"

**Authors:** Levine (Tandem Computers), Gray (DEC SF Systems Center), Kiss (IBM), Kohler (DEC Littleton MA)
**Document:** SFSC Technical Report 93.1, September 1993

**TPC membership arc (primary source):**
> "The TPC has grown from 8 founding vendors to more than 42 member companies."

**TPC-A price/performance arc (primary source):**
> "TPC-A price-performance has improved from 33 K$/tps in 1989 to under 6 K$/tps today [1993], and throughput has exceeded 1000 tps."

**Workload lineage:**
> "The TPC-A workload is derived from a 1974 banking application." (Debitcredit is the 1985 Tandem formalization of this workload; TPC-A is the 1989 standardized version.)

**"Benchmarketing" era documented:**
> "The benchmarketing games of Debit/Credit and TP1 occurring from 1987 to 1990."

**Six problems with TPC-A documented in this memo:**
1. Pricing model loopholes: package pricing and prepaid maintenance exclusions inflate apparent price/performance
2. Terminal domination: terminals represent 40–60% of total system price; terminal price gaming dominates P/P results
3. Ad hoc client-server: vendors configure special-purpose client networks not representative of buyer deployments
4. Specialized DBMS features: e.g., Oracle7 discrete transactions (a TPC "special" acknowledged in results footnotes)
5. P/P improvement outpacing reality: benchmark improvement rates far exceed customer purchasing reality
6. The metric has become a marketing tool rather than a buying guide

**TPC-C technical specification (from this memo):**
- Metric: **tpmC** (transactions per minute C)
- Five transaction types with fixed ratios: New-Order 43.5%, Payment 43.5%, Delivery 4.4%, Order-Status 4.4%, Stock-Level 4.4%
- Nine database tables (vs. 4 for TPC-A/Debitcredit)
- Wholesale supplier scenario with full-screen UI and location transparency
- Approximately 10× heavier workload than TPC-A
- Approved 1992; first results published 1993

---

*End of prompt document v3. Three source documents committed to `kastner-author/2026-kastner-tpc-sources/`. Ready for assembly pass after remaining kw-ask commands are run.*
