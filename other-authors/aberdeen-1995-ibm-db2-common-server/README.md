# Aberdeen Group — DB2 Common Server Relational Database Management System

**Study ID:** `aberdeen-1995-ibm-db2-common-server`
**Author:** Aberdeen Group
**Date:** November 1995
**Type:** Product Profile
**Domain:** Relational Database Management

---

## Overview

This dataset is a [Frictionless Data Package](https://specs.frictionlessdata.io/data-package/) archiving and structuring the Aberdeen Group research profile of IBM's DB2 Common Server Relational Database Management System (version 2), published in November 1995.

The original study evaluates DB2 as a distributed, open RDBMS (DORS) and positions it against competitors Oracle, Sybase, and Informix. Aberdeen advises IS buyers to take a fresh look at DB2 following the significant technology advances in version 2, including SMP enablement, enhanced replication, and distributed database support.

**Source (Wayback Machine):** https://web.archive.org/web/19970112012303/http://www.aberdeen.com:80/secure/profiles/ibm_db2/ibm_db2.htm

---

## Study Context

In 1995, the enterprise database market was being transformed by distributed, open RDBMS (DORS) platforms migrating workloads from mainframes to Unix workstations and PC-LANs. IBM's DB2 Common Server faced competition primarily from:

- **Oracle** — dominant market leader (still active, NYSE: ORCL)
- **Sybase** — major competitor (acquired by SAP in July 2010 for ~$5.8 billion; products continue as SAP ASE, SAP IQ)
- **Informix** — leading UNIX RDBMS (acquired by IBM in 2001 for $1 billion; active development delegated to HCLSoftware in 2017)

Aberdeen coined the term "DORS" (Distributed, Open RDBMS) as its evaluation framework with four key criteria: scalability, distributed-database support, flexibility, and administrative support and robustness.

---

## Key Findings from the Study

1. **DB2 v2 achieves competitive parity:** Version 2 added SMP enablement, two-phase commit, and enhanced query optimization to match major DORS competitors.
2. **TPC-C Benchmark:** DB2 delivered 3,119.16 tpmC at $349/tpmC on an 8-way IBM RS/6000 model J30.
3. **IBM financials (1994):** Total revenue $64.0 billion (+2% YoY); net profit $3 billion; software revenue $11.3 billion (estimated more than twice the largest dedicated software company at the time).
4. **OS/2 installed base:** IBM estimated over 10 million OS/2 users.
5. **DRDA ecosystem:** 11 third-party suppliers had implemented DRDA access to DB2 data.
6. **Aberdeen recommendation:** IS buyers should "take a new and closer look at DB2 for distributed, open production systems."

---

## File Structure

```
aberdeen-1995-ibm-db2-common-server/
├── datapackage.json          # Frictionless Data Package descriptor
├── README.md                 # This file
├── data/
│   ├── studies.csv           # Study-level metadata (1 row)
│   ├── entities.csv          # Companies/organizations mentioned (11 rows)
│   ├── technologies.csv      # Technologies with lifecycle info (35 rows)
│   ├── observations.csv      # All extracted observations (50 rows)
│   └── codes.csv             # Controlled vocabulary definitions (49 rows)
├── schema/
│   └── schema_org.json       # Schema.org Dataset metadata
└── scripts/
    └── demo_analysis.py      # Demonstration analysis script
```

---

## Data Tables

### `studies.csv`
One row per research study. Contains bibliographic metadata: title, author, date, type, domain, methodology, and abstract.

### `entities.csv`
Companies and organizations mentioned in the study. Includes current status (active/acquired/rebranded) verified as of March 2026. Key entities:

| Entity | Role | Status (2026) |
|--------|------|---------------|
| IBM | Subject | Active |
| Oracle | Competitor | Active |
| Sybase | Competitor | Acquired by SAP (2010) |
| Informix | Competitor | Acquired by IBM (2001); dev. delegated to HCLSoftware (2017) |
| Computer Associates | Ecosystem | Rebranded → CA Technologies → Broadcom (2018) |

### `technologies.csv`
Technologies, protocols, products, and standards referenced. Lifecycle statuses:
- **Active** (still in current use): SQL, ODBC, AIX, TCP/IP, CICS, HACMP, REXX, RACF, SNMP, TPC-C benchmark, Tuxedo, Lotus Notes (as HCL Notes), PowerBuilder
- **Legacy** (superseded but in some use): DRDA, X/Open CLI, DataPropagator, DataJoiner, DataHub, Windows NT, RS/6000, RS/6000 SP, SNA LU6.2, Encina, ADSM, Lotus Approach, NotesPump, FlowMark, VisualAge, DataBasic
- **Obsolete** (discontinued): OS/2 Warp

### `observations.csv`
50 structured observations extracted from the study. Each row captures a distinct factual claim, assessment, benchmark result, or recommendation with:
- `obs_type` — categorized type of claim
- `subject`, `predicate`, `object_value` — triple structure
- `numeric_value` / `unit` — for quantitative observations
- `sentiment` — positive/neutral/negative evaluative tone
- `confidence` — high/medium/low extraction confidence
- `verbatim_quote` — supporting text from the source

### `codes.csv`
Controlled vocabulary definitions for all coded fields used across the data tables.

---

## Usage

### Quick start with Python
```bash
pip install frictionless pandas
python scripts/demo_analysis.py
```

### Validate the package
```bash
pip install frictionless
frictionless validate datapackage.json
```

---

## Entity Status Verification Sources

- Sybase acquisition by SAP: https://www.sap.com/investors/en/financial-news/ad-hoc-news/2010/05/934992.html
- SAP Sybase product page: https://www.sap.com/products/acquired-brands/what-is-sybase.html
- Informix acquisition and HCL delegation: https://en.wikipedia.org/wiki/Informix
- Computer Associates / Broadcom: https://www.broadcom.com/

---

## License

Data structure and annotations: CC-BY-4.0
Original study content: Copyright © November 1995 Aberdeen Group, Inc., Boston, Massachusetts. All rights reserved. Original study reproduced here for archival and research purposes.

---

## Citation

Aberdeen Group. (1995). *DB2 Common Server Relational Database Management System*. Aberdeen Group, Boston, MA. Archived at: https://web.archive.org/web/19970112012303/http://www.aberdeen.com:80/secure/profiles/ibm_db2/ibm_db2.htm
