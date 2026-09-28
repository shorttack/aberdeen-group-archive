# Databases Longitudinal Study — Evidence Dossier (Gate 1 + Gate 3)

**Status:** Read-only evidence extraction and study organization. **No narrative written** (per Pete, 2026-07-09). This dossier is the structured input for a later drafting pass by Pete.
**Scope window:** 1970–2005 (obs beyond 2005 excluded from window counts; flagged where they appear).
**Source of truth:** live DuckDB `~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb` (Phases 1+2+0 rebuilt 2026-07-09; shape baseline 1504/24842/3288/4368). All counts SQL-derived; alias-consolidated.
**Deferred:** `kw ask` interpretive synthesis (needs local Ollama:11434, unreachable from the sandboxed shell) — planned as a future step to enrich narrative threads.
**Theme anchor techs already in archive:** `databases-rdbms` (theme rollup), `TECH-RDBMS-COMM` (commercial RDBMS on Unix), `oltp-tpc`, `commercial-benchmarks`.

---

## 0. Method & alias resolution

Vendor entities are heavily alias-fragmented in the masters. This dossier consolidates each vendor into one canonical cluster (read-only; **no master edits**) and reports consolidated totals with a per-alias appendix (§9) for transparency. Study↔vendor and study↔tech links live only in `_master_observations.csv` (the entity/tech masters have no `study_id` column).

**80/20 split (per Pete):** ~80% relational core = Ingres, Informix, Oracle, Sybase, DB2, RDB. ~20% remainder = Software AG, CA, IBM (as DB), CCA. NCR appears as both a DB-adjacent vendor (Teradata) and a hardware platform (Ch. 6) and consulting anchor (Ch. 8).

### Consolidated vendor volume (alias-resolved)

| Cluster | obs total | studies | first–last obs yr | obs in 1970–2005 |
|---|--:|--:|---|--:|
| Oracle | 406 | 74 | 1977–2026* | 345 |
| CA (incl. CA-Ingres) | 159 | 43 | 1980–2018* | 113 |
| Informix | 100 | 25 | 1980–2020* | 98 |
| NCR (incl. AT&T GIS, Teradata) | 85 | 32 | 1987–2025* | 81 |
| Sybase | 64 | 25 | 1990–2010* | 53 |
| Ingres (indep. RTI/ASK) | 16 | 5 | 1990–2011* | 15 |
| Software AG | 14 | 6 | 1991–2025* | 13 |
| DB2 (product-tagged) | 1 | 1 | 1995 | 1 |
| CCA | 1 | 1 | 2010 | 0 |

\* Post-2005 max years come from synthetic 2026 longitudinal/memoir studies (see §10 data-quality note). DB2 is under-tagged at the product level — most DB2 evidence rides inside IBM-platform and RDBMS-comparison studies (see §4, Ch.1-2).

---

## Chapter 1–2 — RDBMS adoption arc (the 80%): Prodding the market

**Chapter goal:** How Kastner/Aberdeen pushed enterprises to adopt the relational model, vendor-by-vendor (Ingres, Informix, Oracle, Sybase, DB2, RDB).

### Timeline (obs per 5-yr bucket, alias-resolved, 1970–2005)

| Cluster | '77 | '88 | '90 | '92 | '93 | '94 | '95 | '96 | '97 | '98 | '00 | '01 | '02 | '03 | '04 | '05 |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Oracle | 1 | 4 | 1 | 3 | 19 | 7 | 64 | 49 | 88 | 17 | 19 | 7 | 25 | 24 | 5 | 10 |
| Informix | – | – | – | – | 3 | 13 | 11 | 19 | 39 | 3 | 1 | 8 | – | – | – | – |
| Sybase | – | – | 2 | – | 4 | 8 | 16 | 10 | 5 | 5 | – | 1 | 1 | 1 | – | – |
| CA | – | – | – | – | 1 | 2 | 9 | 12 | 42 | 8 | – | 33 | – | – | 1 | 1 |
| NCR | – | 1(’87) | – | 21(’92) | 4 | 5 | 6 | 18 | 12 | 4 | – | – | 3 | – | – | 1 |
| Ingres | – | – | 6 | 1 | 4 | 4 | – | – | – | – | – | – | – | – | – | – |
| Software AG | – | – | – | – | 2 | – | 2 | 8 | – | – | – | – | – | – | – | – |

Read: RDBMS coverage peaks 1993–1997 (the client-server/RDBMS "jungle" years). Ingres evidence concentrates 1990–1994 then collapses (acquisition by CA). Oracle sustains across the whole arc.

### Top RDBMS-core studies (by relevant obs; ★ = Pete-authored)

| study_id | title | year | type | obs |
|---|---|--:|---|--:|
| `2026-kastner-oracle-longitudinal` | Oracle Across Four Decades (SYNTHETIC) ★ | 2026 | topic-analysis | 96 |
| `aberdeen-1995-oracle-interoffice` | Oracle InterOffice | 1995 | product-profile | 39 |
| `informix-universal-server-launch-object-relational-fb2cd4` | Informix Universal Server: First Object-Relational DBMS ★ | 1996 | transcript | 29 |
| `aberdeen-1996-oracle-network-computing-architecture` | Oracle's Network Computing Architecture | 1996 | market-study | 29 |
| `cab199-1-2-0cb163` | RDBMS Market Overview — CA Sales Training ★ | 1997 | market-study | 25 |
| `informix-competitive-update-kastner-rdbms-jungle-25604a` | Informix Competitive Update — Kastner "RDBMS Jungle" address ★ | 1994 | transcript | 22 |
| `rdbms-for-ibm-powera~1-7a44be` | Power Academy RDBMS Sales Training ★ | 1996 | benchmark | 22 |
| `1997-oracle8-the-database-for-network-computing-674c9d` | Oracle8: The Database for Network Computing ★ | 1997 | market-study | 20 |
| `1997-migrating-from-sybase-sql-server-4.-d7b1d0` | Migrating from Sybase SQL Server 4.9 to Informix | 1997 | vendor-profile | 18 |
| `nti-6-rdbms-technology-48f4aa` | RDBMS Report Card ★ | 1993 | market-study | 17 |
| `1997-oracle-developer-2000-client-server-development-en-5f98ce` | Oracle Developer/2000 | 1997 | market-study | 16 |
| `jungle-1-5-675c58` | Welcome to the RDBMS Jungle — Ch.1-5 ★ | 1995 | consulting-report | 12 |
| `jungle-6-7af8b7` | Welcome to the RDBMS Jungle — Ch.6 ★ | 1995 | consulting-report | 9 |
| `aberdeen-1995-universal-servers-rdbms-technology-next-decade` | Universal Servers: RDBMS for the Next Decade ★ | 1995 | technology-viewpoint | 10 |
| `1990-bull-rdbms-1990-and-2024-metadata-fe61bf` | Ingres/Sybase Customer-Satisfaction Survey (Bull) ★ | 1990 | survey-report | 9 |
| `aberdeen-1996-distributed-open-rdbms-buying-guide` | Distributed Open RDBMS Buying Guide 1996 | 1996 | market-study | 7 |
| `informdsa-9f8bcf` | Can Parallel-Scalable RDBMSs Break the Downsizing Logjam? ★ | 1995 | consulting-report | 6 |
| `1997-informix-metacube-4.0--relational-o-23491d` | Informix MetaCube 4.0: Relational OLAP | 1997 | product-profile | 3 |
| `ingres-windows-4gl-1990-gui-development-tools-75ade0` | Ingres Windows 4GL Launch (May 1990) ★ | 1990 | transcript | 4 |
| `sap-sybase-face-off-f2612e` | SAP, Sybase Face Off | 1996 | news-article | 4 |

### Representative evidence (verbatim observation text)

- **RDBMS Report Card (1993, ★):** "IS executives changing from hardware-oriented to software-platform-oriented decision criteria"; "RDBMS = primary software platform for enterprise IS infrastructure; unifies mainframe, midrange, and desktop"; per-vendor scorecard — "Ingres best-in-class; all others far behind," "First time Oracle demonstrated true technical leadership," "Sybase and Ingres best-in-class," "Reduces application development code by up to 35%."
- **"RDBMS Jungle" (1994–95, ★):** "RDBMS market is a 'jungle' with four vendors on a common playing field"; Kastner's vehicle metaphors — "Informix = Aerostar van (practical, profitable)," "Sybase = race car (fast, not yet a daily driver)," "Ingres = slow/late vehicle — losing the race"; "Massively parallel RDBMS systems will eclipse mainframes for large workloads"; "Walmart running terabyte-class RDBMS workloads."
- **Universal Servers (1995, ★):** object-relational / "RDBMS for the next decade" framing — the ORDBMS pivot.

### Prescience layer (scored)
| study_id | verdict | mean | n |
|---|---|--:|--:|
| `aberdeen-1995-universal-servers-rdbms-technology-next-decade` | high | 2.91 | 22 |
| `informdsa-9f8bcf` | high | 2.67 | 15 |
| `nti-6-rdbms-technology-48f4aa` (Report Card) | high | 2.00 | 21 |
| `jungle-1-5-675c58` | high | 0.91 | 32 |
| `jungle-6-7af8b7` | high | 0.88 | 33 |
| `cab199-1-2-0cb163` | medium | 1.54 | 54 |

---

## Chapter — Pete's market-prodding, OLTP, benchmarks & audits, and the TPC

**Chapter goal:** Kastner's OLTP work, benchmark/audit practice, and the TPC's role in improving RDBMS quality/performance. **Pete foregrounded** (memoir + employer-record + Path-B tagged).

### Benchmark lineage (chronological, verbatim)
- **Tandem TR 85.2 "A Measure of Transaction Processing Power" (1985)** `tandem-tr-85-2-debitcredit-1985-ca207a`: the Anon-et-al DebitCredit paper (Jim Gray + ~24 co-authors); "TPS — standard throughput metric defined to enable cross-vendor comparison"; "Whetstones, MIPS, MegaFLOPS … focus on CPU — they do not capture TP-system features"; **"Transaction Processing Performance Council formed 1988; TPC-A standardized DebitCredit-style benchmark published 1989."** Explicit Pete link: *"Kastner (then at Stratus) used ET-1/TP-1 as the standard Stratus-vs-Tandem price/performance comparison framework."*
- **Serlin FTSN-33 (1985)** `ftsn-serlin-tandem-txp-et1-benchmarks-19-ea6530`: ET-1 tps/CPU numbers; "16-CPU TXP can do 100 tps; 10-system FOX network can do 'magic 1000 tps.'"
- **Stratus ET1-vs-TP1 dossier (1986, ★ compiler)** `stratus-et1-tp1-tandem-dossier-1986-26871a`; **Stratus ET1 functional spec + benchmarks (1986)** `stratus-et1-functional-spec-and-benchmar-0c3172`; **Stratus Sales Support Competitive News (1987, ★ editor)** `stratus-sales-support-competitive-news-1-2aac8d`.
- **Kastner ghostwrites Yankee Group study (1987) "The Future of Transaction Processing"
- **DEC benchmark corpus (1987–88):** `dec-notes-tp1-debit-credit-thread-1987-1-5815dc` (DEC Rdb NOTES TP1 thread); `dec-debit-credit-guidelines-kohler-hsu-1-e228b4`; `dec-primer-comparing-debit-credit-tests--c30cfa` (★ Kastner, DEC CSG 1988); `dec-zahavi-debit-credit-vaxclusters-1988-1a9e2e`.
- **DEC "Blue Monday" internal sales training (1988, ★)** `dec-blue-monday-internal-sales-training-dectp-vs-ibm-0021cc` — 42 obs, the richest single OLTP artifact. Verbatim: "Kastner: TP market $21 billion/year, growing 2× rate of overall computer market"; "DEC debit-credit cost-per-transaction <1/3 IBM mainframe, ~2× Tandem"; "VAX 8830 RAMP-C TP throughput approaches IBM 3090 Model 200E"; "Kastner predicts DEC TP share will triple from <5% to ~15% by early 1990s." (Scored **low**, mean 1.95 / 42 — a Path-B candidate: authored optimism vs. later reality.)
- **DECtp launch primary source (1988):** `dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836` (Plaza Hotel, Olsen/Kirk/Glorioso).
- **TPC founding in August 1988 with Kastner as DEC executive, then Aberdeen Group founder

### Pete's OLTP consulting & the "Open OLTP" evangelism
- `bbn1989-1e6838` OLTP Market Research for BBN Advanced Computers (1989, ★, 19 obs)
- `encore-b7c40d` OLTP Market Analysis for Encore Series 90 (1990, ★, 12 obs); `1991-encore-and-metadata-47f414` follow-on strategy (1991, ★)
- `bull1990-d-c-benchmarks-8b5d9c` Bull DPS 9000/7000 Debit-Credit Benchmark (1989, ★)
- **"Open Online Transaction Processing: An Enterprise Manager's Guide"** — Aberdeen paper `aberdeen-open-online-transaction-process-ea272f` (1991, ★) + **Korean translation** `aberdeen-open-oltp-enterprise-managers-k-3fc536` (1991/92, ★; scored **high** 2.54/13)
- `ncr-norge-open-oltp-rdbms-seminar-1992-0-7f5414` NCR Norge Open OLTP/RDBMS seminar, Oslo (1992, ★ lead lecturer)
- **Aberdeen appointment** `aberdeen-press-advisory-kastner-appointm-efd58c` (1988) — "Kastner to head new **Transaction Services** Business Unit" (institutional origin of Pete's OLTP franchise).

### Memoir layer (career context, 2026 synthetic — mark as such)
`volume-1-ch05-stratus-fault-tolerant-wars-1981-1987`, `volume-1-ch06-dec-mainframes-last-stand-1987-1988`, `volume-1-ch08-aberdeen-go-go-years-1998-2006`, `volume-1-ch10-the-long-view-1966-2026`, `volume-1-appendix-career-timeline`, `dec-resume-performance-review-3-1f133b` (1987), `psk-niopubs-3d103b` (publications list).

**TPC quality-improvement thread (for narrative):** the arc is documented end-to-end — DebitCredit (1985 Anon-et-al) → ET-1/TP-1 vendor wars (Stratus/Tandem/DEC 1985–88) → TPC founded 1988 → TPC-A 1989 → TPC-C SMP high-water marks (`1997-informix-and-silicon-graphics-reach-98e6ea`, Informix+SGI) and TPC-C tpmC price/perf cited throughout the 1996 NT/SMP studies (§Ch.6). Kastner as TPC-A, -B benchmark auditor.

---

## Chapter — Hardware platforms

**Chapter goal:** major platform vendors + transitions: single→multiprocessor, minicomputer→microprocessor, the Unix wars, the emergence of x86.

### Tech clusters present
- **x86 / IA:** `intel-x86`, `intel-80x86`, `intel-486`, `x86-32`, `ia-architecture`, `industry-standard-servers`, `smp-intel`, `intel-xeon-mp`, `amd-opteron`, `amd64`, `em64t-intel64`
- **RISC/Unix & MP:** `alpha-processor`, `att-unix-svr4`, `64-bit-unix`, `digital-unix`/`tru64-unix`, `unix-aix`, `big-iron`, `TECH-RDBMS-COMM` (commercial RDBMS on Unix)
- **mini→micro:** `embedded-microprocessor`, RISC/Unix market studies

### Key studies (chronological)
| study_id | title | year | thread |
|---|---|--:|---|
| `nti-2-open-systems-1dd3af` | Open Systems: A Technology Status Report ★ | 1993 | Unix wars / AT&T-Sun alliance |
| `nti-3-pc-and-ws-1993-17d49b` | PCs and Workstations: Vying for the 1990s Desktop ★ | 1993 | mini→micro, x86 486 |
| `aberdeen-1996-risc-unix-market` | Commercial Multiuser RISC/Unix 1995: HP Dominates | 1996 | RISC/Unix peak (medium, 1.05/55) |
| `aberdeen-1996-digital-debunks-ntsmp-scalability-myth` | Digital Debunks the NT/SMP Scalability Myth ★-adjacent | 1996 | single→MP, NT/SMP, TPC-C tpmC (high, 1.76/21) |
| `aberdeen-1996-digital-debunks-ntsmp-scalability-myth` | (companion) `aberdeen-1996-debunking-ntsmp-scalability-myth` | 1996 | SMP scaling |
| `1996-sequent-38f0b1` | Emerging Technologies: Assessing Strategic Benefits ★ | 1996 | Sequent NT/SMP to 28 CPUs |
| `2001-compaq-tru64-unix-and-oracle9i-clusters-reduce-cos-17b4b2` | Compaq Tru64 + Oracle9i Clusters | 2001 | 64-bit Unix + DB clustering |
| `2003-dell-and-oracle-boldly-predict-the-demise-of-big-i-073fba` | Dell & Oracle Predict Demise of Big Iron | 2003 | x86 commoditization (medium, 3.7/10 — highest scored) |
| `technology-news-hardware-amd-s-opteron-a-ecf5a9` | AMD's Opteron at the One-Year Mark | 2004 | x86-64 emergence |
| `2010-intel-ia-continuum-wp-1-2-fc5653` | Intel's IA Continuum Strategy | 2010* | x86 broadening (outside window — context only) |

### Representative evidence
- Unix wars: "Response to AT&T/Sun Unix alliance threat"; "Acquired USL (Unix System 5.4) and DR-DOS author Digital Research" (1993).
- mini→micro / x86: "Vast majority will move to MS-DOS 6.0 and Windows 4.0 on Intel 486" (1993); "PC approaches workstation in client-server/multiuser" (1993).
- single→MP + TPC-C: 1996 NT/SMP study carries tpmC price/perf rows — "6,712 tpmC at $65/tpmC (NT, 4-way Pentium Pro, MS SQL Server)," "8,311 tpmC at $95/tpmC (UnixWare, 4-way, Sybase+Tuxedo)," "5,774 tpmC at $198/tpmC (AIX, 8-way, Sybase)"; "64-bit NT needed for full high-end capability"; "Sequent scaled NT to 28 processors."
- x86 endgame: "Dell and Oracle boldly predict the demise of big iron" (2003).
- Kastner quotations on RDBMS, RDBMS vendors, TPC benchmarks

**Cross-link:** hardware evidence is DB-coupled throughout (tpmC = RDBMS-on-platform), so this chapter shares evidence with Ch.1-2 and the OLTP chapter.

---

## Chapter — Enterprise applications requiring third-party database services

**Chapter goal:** how enterprise apps (ERP: SAP, Baan, PeopleSoft; D&B; Siebel) depended on a third-party RDBMS.

### Key studies
| study_id | title | year | note |
|---|---|--:|---|
| `1993-hercules-sap-28344a` | HP 9000 for SAP R/3 at Hercules ★ | 1993 | **canonical exemplar** — 28 obs; platform+DB selection |
| `aberdeen-1995-ibm-as400-sap-r3` | AS/400 + SAP R/3 | 1995 | SAP on AS/400 |
| `sequent-sap-sequen~1-7f70e4` | The Strategic R/3 Solution for the Enterprise | 1996 | Sequent SMP for SAP |
| `sap-sybase-face-off-f2612e` | SAP, Sybase Face Off | 1996 | app vs DB tension |
| `aberdeen-1996-baan-changes-rules-erp-game` | BAAN Dynamic Enterprise Modeling | 1996 | Baan ERP |
| `aberdeen-1995-upgrading-isv-methodology-enterprise-application-development` | ISV Methodology for Enterprise App Dev ★ | 1995 | app-dev methodology |
| `1997-vertical-industry-solutions-baan-leads-in-innovati-f12724` | Vertical Industry Solutions: Baan | 1997 | vertical ERP |
| `aberdeen-1996-app-dun-bradstreet-software-smartstrtogether-better` | D&B SmartStream Distributed Enterprise | 1996 | financials app |
| `1997-the-compaq-siebel-global-alliance-an-e-roach-to-cu-458c35` | Compaq-Siebel Global Alliance | 1997 | CRM app + platform |

### Decisive evidence (Hercules SAP, ★ 1993)
- **"Rewriting proprietary mainframe database to Unix required Oracle adoption"** — the exact "app forces a third-party RDBMS" mechanism.
- "HP is RISC/Unix reference port for both SAP and Oracle; Oracle's most important multiuser platform in revenue."
- "Applications grow at 30-40% per year for first three years after initial SAP R3 installation."
- "Implement three-tier-plus topology instead of planned two-tier; two-tier has 'fatal flaws' for distributed enterprises."
- Outcome-tagged: "SAP R3 became dominant ERP platform worldwide."

---

## Chapter — Integration & application-development issues (ITT Hartford / NCR consulting example)

**Chapter goal:** integration and app-dev issues, using Pete's ITT Hartford / NCR consulting engagement as the worked example.

### Anchor study
`itthar-1-4-32f824` — **"Making the Corporate Platform Decision (ITT Hartford)"**, consulting-report, **1995**, 12 observations, scored **high** (mean 2.67 / 9). Complete decision-framework case.

### Full observation set (verbatim)
| obs | type | evidence |
|---|---|---|
| OBS-001 | strategic-assessment | Windows 95 runaway desktop-OS choice; GA timing later than required |
| OBS-002 | recommendation | Dual workgroup-OS strategy (Windows NT/AS + Novell NetWare) is pragmatic |
| OBS-003 | recommendation | System/network management, esp. distributed software management, needs ongoing planning |
| OBS-004 | expert-opinion | Windows 95 market winner; huge ISV support; works with NT or NetWare; 16-bit compatibility |
| OBS-005 | competitive-position | IBM OS/2 Warp: little ISV support or commitment |
| OBS-006 | strategic-assessment | **Overwhelming business case for a Common IT Platform across ITT Hartford business units** |
| OBS-007 | expert-opinion | Platform decision made systematically and professionally; tough choices made |
| OBS-008 | expert-opinion | Platform stack enumerated: desktop OS; app/DB OS; network OS; net mgmt; desktop apps; groupware; office automation; 3270 emulator; email; group calendar; platform management |
| OBS-009 | recommendation | **Consultant is an objective outsider** for high-risk, high-cost, conflicting-answer decisions |
| OBS-010 | expert-opinion | Background: **1994 Commercial Lines Coop review — Stay with AT&T Cooperation?** (the NCR/AT&T thread) |
| OBS-011 | viability-prediction | Windows 95 not shipping May 1995; may be delayed |
| OBS-012 | actual-outcome | Windows 95 shipped Aug 24, 1995; became dominant desktop OS |

### Supporting Pete/NCR integration evidence
- `oracle-att-ncr-pittsburgh-seminar-letter-98b0a4` (1993) & `oracle-att-ncr-customer-driven-seminar-t-b9f539` (1993, 8-city tour) — **Pete keynote**, Oracle × AT&T-NCR "Customer-Driven Information Solutions."
- App-dev toolset thread: `nti-5-development-toolsets-0e71c5` (1993, ★), `nti-12-client-server-goals-1993-15a519` "Realistic Goals for Client-Server Computing" (1993), `aberdeen-1996-3com-reconciling-clientserver-development-internet` (1996), `ca-internet-app-dev-sales-training-1996-48db9c` (1996, ★).

---

## Chapter — The remainder (the 20%): other databases (Software AG, CA, IBM, CCA)

### Software AG (14 obs / 6 studies)
`aberdeen-1996-software-ag-digital-high-performance-solutions` (1996) — "Software AG and Digital: High-Performance Solutions Throughout the Enterprise" (ADABAS/Digital). Also referenced in RDBMS Report Card ("Software AG, Informix, Oracle lead"). Memory: a mainframe TP1 benchmark audit for Roel Pieper of Sotware AG was one of Kastner's first Aberdeen clients.

### Computer Associates (159 obs / 43 studies — incl. CA-Ingres, Unicenter, Jasmine)
Two obs peaks: 1997 (42) and 2001 (33). Pete had a deep CA relationship (sales training + retainer):
- `cab199-1-2-0cb163` RDBMS Market Overview — CA Sales Training (1997, ★, 25 obs)
- `carepo-kastner-unicenter-jasmine-1996-1d5ffe`, `caunic-ltr98-80140d`, `1997-ca-s-unicenter-tng-framework-pk-apr-50d15f` (Unicenter/Jasmine)
- `ca-y2k-cfo-executive-exchange-1997-c59ca4`, `cacustsell98-3b53c6`, `caprop1-98-5d69fd`, `1999-retainer-contract-d3a385`, `caprop99-86144f`, `letter-to-sanjay-kumar-ca-world-2001-d60b1b` (relationship/employer-record trail)
- CA-Ingres product line: `ENT-CA-INGRES` "CA-Ingres + Jasmine" (bridges to the Ingres story in Ch.1-2)

### IBM (as database: DB2) — under-tagged at product level
`ent-ibm-db2` carries only 1 direct obs, but DB2 evidence is embedded in comparison/training studies: `rdbms-for-ibm-powera~1-7a44be` (Power Academy RDBMS training, ★), `ibm-rs6000-midran~1-88f049` (RS/6000 RDBMS training, ★), and RDBMS Report Card ("Worst-in-class across all platforms (DB2, OS/2 Data Manager)"). **Gap flagged** — see §10.
- Kastner as bid protest expert witness on projected poor DB2 performance in Florida HHS welfare system case volume-1-ch09-expert-witness-technology-on-trial-1992-2015][study-unisys-florida-hrs-expert-witness-tallah-5b4524]
* kw ask "list studies that mention IBM DB2 RDBMS in any way" --k 16
[kw ask] retrieve: 1363 ms — synthesizing…
Based on the provided sources, the following studies mention IBM DB2 RDBMS (including specific versions like DB2 for AIX, DB2/6000, DB2 Common Server, and DB2 Universal Database):

*   **[[study-2026-kastner-ibm-longitudinal]]** – Discusses IBM's database stack (including DB2) as a durable revenue engine, TPC benchmark participation, the maturity of DB2 for TP versus IMS/CICS-VSAM, mainframe + DB2 strategies, and modern cloud/containerized deployments.
*   **[[study-dec-blue-monday-internal-sales-training-dectp-vs-ibm-0021cc]]** – Notes that IBM DB2 for Transaction Processing (TP) was still maturing while many customers remained on IMS/CICS-VSAM.
*   **[[study-jungle-6-7af8b7]]** – Covers improvements in DB2 for AIX 2, Data Propagator for mainframe-RS6000, CICS/Ensina/Tuxedo OLTP, HACMP and SP2 scalability, and modest data warehouses on SMP or SP2.
*   **[[study-jungle-1-5-675c58]]** – Highlights new-found competitiveness in DB2 regarding parallel/scalable PQS and SP2, triggers/stored procedures, and strong proprietary replication; notes IBM as the largest overall DBMS supplier.
*   **[[study-aberdeen-1996-ibm-transformation-business-machines-information-service]]** – Describes DB2 as a follower in RDBMS functionality and performance compared to Oracle, Sybase, and Informix.
*   **[[study-volume-1-ch06-dec-mainframes-last-stand-1987-1988]]** – States that DB2 had been tuned almost exclusively for query workloads rather than transactional throughput, referencing the relational model design by Edgar Codd and Christopher Date.
*   **[[study-10ibmiss-f66945]]** – Listed as a source containing observations regarding IBM DB2 (specific content not detailed in summary).
*   **[[study-1997-ibm-business-intelligence-family-pr-43c37e]]** – Identifies DB2 as the core underlying RDBMS for all IBM BI Family products.
*   **[[study-aberdeen-1995-universal-servers-rdbms-technology-next-decade]]** – Mentions DB2 Relational Extenders for text, imaging, audio, and video, noting it was not yet deep in architecture or sophisticated client-server toolsets at the time.
*   **[[study-1988-encore-oltp-market-tps-needs-deee45]]** – Cites performance limitations of DB2 (as IBM's mainframe relational database) for decision support workloads at that time.
*   **[[study-rdbms-for-ibm-powera~1-7a44be]]** – Analyzes DB2 for AIX Version 2, its bundling with hardware, DRDA/ODBC support, scalability on SMP to MPP SP2, and the perception of DB2/6000.
*   **[[study-ibmrs6k-05561e]]** – Listed as a source containing observations regarding IBM DB2 (specific content not detailed in summary).
*   **[[study-aberdeen-1995-ibm-db2-common-server]]** – A product profile evaluating IBM's DB2 Common Server, its competitive positioning against Oracle/Sybase/Informix, integration with Lotus Notes, DataPropagator functionality, and multimedia extenders.
*   **[[study-ibm-rs6000-midran~1-88f049]]** – Discusses RS/6000 with DB2 as neither the fastest nor least expensive option and notes RDBMS ISV fears regarding customer switching to low-priced DB2.
*   **[[study-1997-dec-linkworks-webworker---an-object-db2d2a]]** – References DB2 alongside grid computing and internet enterprise integration.
*   **[[study-nti-6-rdbms-technology-48f4aa]]** – Recommends a new IBM CEO focus on RDBMS as a top priority and notes DB2 was "worst-in-class" across all platforms compared to competitors.
*   **[[study-1997-data-mining-buying-guide-71e463]]** – Mentions DB2 in the context of commercial data mining platforms and vendor selection.
*   **[[study-1998-hp-high-availability-and-metadata-7d1276]]** – Lists DB2 as a recommended technology (though specific details are not elaborated in the summary).
*   **[[study-nti-9-mainframe-role-1993-77fc40]]** – States that DB2 did not have the functionality of Oracle, Ingres, or Sybase midrange competitors.
*   **[[study-1997-ibm-extended-transaction-systems-fa-0369fa]]** – Discusses very-large-database data warehousing with DB2, large data types (up to 2 GB), Relational Extenders, and multimedia/XML support in DB2 UDB.
*   **[[study-dbmspr~1-7c854e]]** – Predicts DB2 Universal Database Version 5.0 will expand share on IBM servers and emerge as a BI and e-commerce leader.
*   **[[study-ibmtpc92-c32789]]** – Listed as a source containing observations regarding IBM DB2 (specific content not detailed in summary).
*   **[[study-kastner-technology-breadth-memoir-2026]]** – Includes DB2 in a theme rollup of Databases & RDBMS with 349 mentions.
*   **[[study-1997-ibm-information-integration-family--29351c]]** – Describes DB2 serving as a hub for heterogeneous replication when combined with DataJoiner and DataPropagator.
*   **[[study-2026-kastner-enterprise-ai-arc]]** – Mentions IBM DB2 Text Extender in the context of unstructured text storage and query.

--- Sources ---
0.633  ibm-db2                                           technology
0.632  t5-08                                             technology
0.620  ent-ibm-db2                                       entity
0.618  t88-04                                            technology
0.607  db2-aix                                           technology
0.605  study-aberdeen-1995-ibm-db2-common-server         study
0.604  db2-6000                                          technology
0.603  db2                                               technology
0.595  tech-ets-005                                      technology
0.584  ibm-sp2                                           technology
0.584  databases-rdbms                                   technology
0.583  tech-iif-005                                      technology
0.582  db2-mvs                                           technology
0.579  ibm-db2-text                                      technology
0.578  db2-universal-database                            technology
0.575  db2-parallel-edition                              technology
[kw ask] filter: all, k=16, model=qwen3.5:27b-mlx, think=off

### CCA (Computer Corporation of America)
`computer-corporation-of-america` — 1 obs (2010, outside window). **Sparse**; likely needs manual sourcing from Pete's memory or restricted-sources for the 1970s-80s Model 204 era. wayne Kernochan and Pete's wife Kate worked at CCA **Gap flagged.**

---

## 9. Per-alias appendix (transparency)

**Oracle** (consolidated 406): oracle-corporation 276, oracle 104, oracle-corp 21, e90-05 2, ENT-ORACLE-DB4 2, ENT-NOV-006 1, + 8 zero-obs IDs (ENT-ORACLE, ENT-ORA-001, ENT-ORACLE-DB, ENT-IRP-004, ENT-PS-015, ENT-BO-004, ENT-SB-002, oracle-norge-as).
**CA** (159): computer-associates 119, computer-associates-international 33, computer-associates-ca 2, ca-technologies 2, ENT-NOV-005 1, ENT-CA-INGRES 1, ENT-CA 1, + 4 zero (computer-associates-international-ca-ingres, computer-associates-2, ENT-PS-011, ca-ingres).
**Informix** (100): informix-software 30, informix 22, informix-corporation 17, ENT-INF-001 12, ENT-SGI-001 8, ENT-INFORMIX 6, ENT-MC-001 3, informix-corp 2, + 3 zero (ENT-INFMX, ENT-O2-002, ENT-PS-003).
**NCR** (85): ncr-corporation 62, ncr-teradata 5, att-gis 5, ncr 5, ncr-corp 3, att-gis-ncr 2, teradata 2, ncr-norge-as 1, + 3 zero (teradata-corp-1979, teradata-corp, ncr-korea).
**Sybase** (64): sybase 43, sybase-inc 9, ENT-SYB-001 6, e90-04 3, ENT-SYBASE 1, ENT-SYBASE-DB 1, powersoft-sybase 1.
**Ingres** (16, independent): ingres-corporation 7, ingres 5, e90-03 (RTI) 4, + 2 zero (ask-ingres, ask-ingres-corp). *(CA-Ingres counted under CA.)*
**Software AG** (14): software-ag 13, e91-17 1.
**DB2** (1): ent-ibm-db2 1. **CCA** (1): computer-corporation-of-america 1.

*Alias consolidation is analytical only — no master rows were edited. If Pete wants these merged in the masters, that is a separate, gated change under `kastner-archive-pipeline`.*

---

## 10. Data-quality notes & gaps (for the drafting pass)

1. **DB2 under-representation** — only 1 product-level obs on `ent-ibm-db2`. DB2's real presence is inside RDBMS-comparison and IBM-training studies. Before drafting Ch.1-2's DB2 sub-arc, consider a targeted pull of DB2 mentions in observation text (grep `metric_value` for "DB2") and/or a Pete-memory supplement. **Recommend a `kw ask` pass here once Ollama is reachable.**
2. **CCA sparse** — 1 obs, 2010, outside window. The 1970s–80s CCA/Model 204 story is essentially absent from the archive; will need manual sourcing.
3. **RDB present but modest** — DEC Rdb has dedicated techs (`rdb`, `digital-rdb`, `koda`) and rides the DEC OLTP corpus (Blue Monday, NOTES TP1 thread) rather than standalone studies. Oracle Rdb (post-1994 acquisition) tech `oracle-rdb` exists — bridges RDB into the Oracle cluster.
4. **Synthetic 2026 studies** — `2026-kastner-oracle-longitudinal`, `2026-kastner-dec-longitudinal-22d177`, and the `volume-1-*` memoir chapters are Pete/Perplexity assemblies (archival-ingest v16). They're excellent scaffolding and outcome-tagging but should be cited as synthetic/secondary, not period-primary sources.
5. **Prescience anchors for narrative tension:** highest-scored in-window = Dell/Oracle "demise of big iron" (2003, 3.7), Universal Servers ORDBMS (1995, 2.91), Open OLTP guide (1991, 2.54), ITT Hartford (1995, 2.67). Lowest = DEC Blue Monday (1988, 1.95, low) → a natural Path-B "authored optimism vs. reality" beat.
6. **Deferred `kw ask` step:** interpretive synthesis of (a) the market-prodding thesis, (b) the TPC quality-improvement arc, (c) DB2 gap-fill — to run when local Ollama is available or Pete runs it directly.

---

## 11. Study inventory index (all cited study_ids, by chapter)

- **Ch.1-2 RDBMS core:** 2026-kastner-oracle-longitudinal; aberdeen-1995-oracle-interoffice; informix-universal-server-launch-object-relational-fb2cd4; aberdeen-1996-oracle-network-computing-architecture; cab199-1-2-0cb163; informix-competitive-update-kastner-rdbms-jungle-25604a; rdbms-for-ibm-powera~1-7a44be; 1997-oracle8-the-database-for-network-computing-674c9d; 1997-migrating-from-sybase-sql-server-4.-d7b1d0; nti-6-rdbms-technology-48f4aa; 1997-oracle-developer-2000-client-server-development-en-5f98ce; jungle-1-5-675c58; jungle-6-7af8b7; aberdeen-1995-universal-servers-rdbms-technology-next-decade; 1990-bull-rdbms-1990-and-2024-metadata-fe61bf; aberdeen-1996-distributed-open-rdbms-buying-guide; informdsa-9f8bcf; 1997-informix-metacube-4.0--relational-o-23491d; ingres-windows-4gl-1990-gui-development-tools-75ade0; sap-sybase-face-off-f2612e; inforx95-3-9a45fe; informix-dsa-presentation-2-8d5fa3; oracle-data-warehousing-launch-multimedia-spatial-d63644; sybase-xi-launch-boats-analogy-multiple-databases-79c9ee
- **OLTP / TPC / benchmarks (Pete):** tandem-tr-85-2-debitcredit-1985-ca207a; ftsn-serlin-tandem-txp-et1-benchmarks-19-ea6530; stratus-et1-tp1-tandem-dossier-1986-26871a; stratus-et1-functional-spec-and-benchmar-0c3172; stratus-sales-support-competitive-news-1-2aac8d; dec-notes-tp1-debit-credit-thread-1987-1-5815dc; dec-debit-credit-guidelines-kohler-hsu-1-e228b4; dec-primer-comparing-debit-credit-tests--c30cfa; dec-zahavi-debit-credit-vaxclusters-1988-1a9e2e; dec-blue-monday-internal-sales-training-dectp-vs-ibm-0021cc; dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836; bbn1989-1e6838; encore-b7c40d; 1991-encore-and-metadata-47f414; bull1990-d-c-benchmarks-8b5d9c; aberdeen-open-online-transaction-process-ea272f; aberdeen-open-oltp-enterprise-managers-k-3fc536; ncr-norge-open-oltp-rdbms-seminar-1992-0-7f5414; aberdeen-press-advisory-kastner-appointm-efd58c; 1997-informix-and-silicon-graphics-reach-98e6ea
- **Hardware platforms:** nti-2-open-systems-1dd3af; nti-3-pc-and-ws-1993-17d49b; aberdeen-1996-risc-unix-market; aberdeen-1996-digital-debunks-ntsmp-scalability-myth; aberdeen-1996-debunking-ntsmp-scalability-myth; 1996-sequent-38f0b1; 2001-compaq-tru64-unix-and-oracle9i-clusters-reduce-cos-17b4b2; 2003-dell-and-oracle-boldly-predict-the-demise-of-big-i-073fba; technology-news-hardware-amd-s-opteron-a-ecf5a9; nti-9-mainframe-role-1993-77fc40; nti-4-nextgen-os-timing-1993-a45049; nti-11-distributed-midrange-servers-1993-dedd19
- **Enterprise apps / third-party DB:** 1993-hercules-sap-28344a; aberdeen-1995-ibm-as400-sap-r3; sequent-sap-sequen~1-7f70e4; sap-sybase-face-off-f2612e; aberdeen-1996-baan-changes-rules-erp-game; aberdeen-1995-upgrading-isv-methodology-enterprise-application-development; 1997-vertical-industry-solutions-baan-leads-in-innovati-f12724; aberdeen-1996-app-dun-bradstreet-software-smartstrtogether-better; 1997-the-compaq-siebel-global-alliance-an-e-roach-to-cu-458c35
- **ITT Hartford / NCR integration:** itthar-1-4-32f824; oracle-att-ncr-pittsburgh-seminar-letter-98b0a4; oracle-att-ncr-customer-driven-seminar-t-b9f539; nti-5-development-toolsets-0e71c5; nti-12-client-server-goals-1993-15a519; aberdeen-1996-3com-reconciling-clientserver-development-internet; ca-internet-app-dev-sales-training-1996-48db9c
- **Remainder (Software AG / CA / IBM-DB2 / CCA):** aberdeen-1996-software-ag-digital-high-performance-solutions; carepo-kastner-unicenter-jasmine-1996-1d5ffe; caunic-ltr98-80140d; 1997-ca-s-unicenter-tng-framework-pk-apr-50d15f; ca-y2k-cfo-executive-exchange-1997-c59ca4; cacustsell98-3b53c6; caprop1-98-5d69fd; 1999-retainer-contract-d3a385; caprop99-86144f; letter-to-sanjay-kumar-ca-world-2001-d60b1b; ibm-rs6000-midran~1-88f049; ent-ibm-db2; computer-corporation-of-america
- **Memoir / career (synthetic 2026):** volume-1-ch05-stratus-fault-tolerant-wars-1981-1987; volume-1-ch06-dec-mainframes-last-stand-1987-1988; volume-1-ch08-aberdeen-go-go-years-1998-2006; volume-1-ch10-the-long-view-1966-2026; volume-1-appendix-career-timeline; dec-resume-performance-review-3-1f133b; psk-niopubs-3d103b volume-1-ch09-expert-witness-technology-on-trial-1992-2015

---

*Generated read-only from kastner.duckdb on 2026-07-09. Supporting query outputs: `db_study_extract_v1_out.md`, `db_study_quotes_v1_out.md`. Extraction SQL: `db_study_extract_v1.sql`, `db_study_quotes_v1.sql`.*
