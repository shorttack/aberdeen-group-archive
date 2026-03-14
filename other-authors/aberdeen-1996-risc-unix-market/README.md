# Commercial, Multiuser RISC/Unix 1995: High Growth and HP Dominate

**Aberdeen Group Market Viewpoint — Volume 9, Number 5**

---

## Study Metadata

| Field            | Value |
|------------------|-------|
| **Study ID**     | `aberdeen-1996-risc-unix-market` |
| **Title**        | Commercial, Multiuser Risc/Unix 1995: High Growth and HP Dominate |
| **Author**       | Aberdeen Group |
| **Date**         | 1996-02-12 |
| **Type**         | market-study |
| **Domain**       | commercial-unix-platforms |
| **Methodology**  | market-analysis, competitive-profiling, revenue-benchmarking |
| **Source File**  | `1995-Commercial-Multiuser-Risc_Unix-1995_-High-Growth-and-HP-Dominate-mvp-3.pdf` |
| **License**      | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) |
| **Archived URL** | https://web.archive.org/web/19970112010549/http://www.aberdeen.com:80/secure/viewpnts/v9n5/v9n5.htm |

---

## Abstract

This Aberdeen Group Market Viewpoint (Volume 9, Number 5, February 12, 1996) presents
the firm's sixth annual review and analysis of the worldwide commercial, multiuser
RISC/Unix systems market. The study measures market size and growth by end-user revenue
for core system platform components — RISC-based multiuser servers with attached mass
storage, Unix operating system and systems software licenses, and direct installation
and maintenance services — deployed for production OLTP, decision support, and batch
processing workloads. The methodology combines primary field research (IS-executive
interviews), revenue benchmarking against supplier-reported and estimated figures, and
competitive profiling of the leading and niche platform vendors.

Key findings reveal that the worldwide commercial RISC/Unix market reached **$14.3 billion**
in 1995, a **43% increase** over 1994's $10.0 billion, far outpacing PC market growth (25%)
and mainframe growth (~5%). Hewlett-Packard dominated with **$7.0 billion** in revenue
(57% growth, **49% share**), maintaining its position as number-one for the sixth consecutive
year. IBM ranked second at **$2.75 billion** (45% growth, 19% share) driven largely by its
RS/6000 SP massively-parallel system and ISSC professional services engagements. Sun
Microsystems placed third at **$1.3 billion** (35% growth, 9% share). Digital Equipment
Corporation posted the **highest growth rate (73%)** reaching $475 million, anchored by a
world-record TPC-C result of over 11,000 tpmC achieved in conjunction with Oracle.

Among the unique-strength suppliers: SNI/Pyramid $825M (+10%), Data General $620M (+11%),
ICL/Fujitsu $340M (flat), Bull $300M, and Tandem $250M (+32%). By contrast, the top three
Intel/Unix suppliers (AT&T GIS/NCR, Unisys, Sequent) combined for only **$2.26 billion** —
roughly one-fifth of the top-three RISC/Unix total of $11.05 billion — with AT&T GIS and
Unisys both posting significant losses and revenue declines. Microsoft NT Server failed to
displace RISC/Unix for business-critical production applications in 1995 due to scalability
and stability issues; NT 4.0 was not expected until April 1996.

Aberdeen's forward-looking conclusions project **continued 40%+ growth** for the RISC/Unix
market in 1996, driven by expansion of production applications already deployed and movement
of 1995 prototypes into production. The study predicts HP will further increase its market
share, that NT Server will complement rather than displace RISC/Unix, and that all major
RISC/Unix suppliers except IBM will transition to 64-bit operating environments during 1996.
Four product agenda items — production Unix functionality advances, 64-bit transitions,
workgroup interoperability (Novell NetWare and NT Server), and MPP platform maturation —
are prescribed for all leading suppliers in 1996.

---

## Data Tables Summary

| File | Rows | Description |
|------|------|-------------|
| `data/studies.csv` | 1 | Study metadata and abstract |
| `data/entities.csv` | 36 | Organizations mentioned in study (vendors, media, research firms) |
| `data/technologies.csv` | 29 | Platforms, processors, OS, applications, and frameworks |
| `data/observations.csv` | 66 | Market data, expert opinions, predictions, benchmarks |
| `data/codes.csv` | 27 | Controlled vocabulary for observation types, methodologies, confidence, lifecycle |

### Entity Coverage
- **RISC/Unix Platform Vendors**: HP, IBM, Sun Microsystems, Digital Equipment Corp,
  SNI/Pyramid, Siemens Nixdorf, Pyramid Technology, Data General, ICL/Fujitsu, Bull,
  Tandem, Stratus, Motorola, Concurrent, Cray, Amdahl, Harris, Silicon Graphics
- **Intel/Unix Vendors**: AT&T GIS/NCR, Unisys, Sequent, Compaq
- **Software/RDBMS**: Oracle, Informix, Sybase, SAP, BAAN, PeopleSoft, Lawson
- **OS/Platform Software**: Microsoft, Novell
- **Media**: Forbes Magazine
- **Research/Services**: Aberdeen Group, IBM ISSC, AT&T Corporation

### Observation Type Distribution
| Type | Count |
|------|-------|
| market-data | 26 |
| viability-prediction | 10 |
| technology-assessment | 10 |
| expert-opinion | 11 |
| benchmark-result | 2 |
| actual-outcome | 0 (predictions not yet verifiable at publication; many subsequently verified) |

---

## Key Market Findings (1995)

| Vendor | Revenue | Growth | Market Share |
|--------|---------|--------|--------------|
| Hewlett-Packard | $7.0B | +57% | 49% |
| IBM | $2.75B | +45% | 19% |
| Sun Microsystems | $1.3B | +35% | 9% |
| SNI/Pyramid | $825M | +10% | 6% |
| Data General | $620M | +11% | 4% |
| Digital Equipment Corp | $475M | +73% | 3% |
| ICL/Fujitsu | $340M | flat | 2% |
| Bull | $300M | — | 2% |
| Tandem | $250M | +32% | 2% |
| **Total Market** | **$14.3B** | **+43%** | — |

| Intel/Unix Vendor | Revenue | YoY |
|-------------------|---------|-----|
| AT&T GIS/NCR | ~$1.0B | -9% |
| Unisys | $620M | -26% |
| Sequent | $540M | +20% |
| **Top-3 Total** | **$2.26B** | — |

---

## Python Load Example

```python
import pandas as pd
import os

DATA_DIR = "data"   # relative to this README

studies      = pd.read_csv(os.path.join(DATA_DIR, "studies.csv"))
entities     = pd.read_csv(os.path.join(DATA_DIR, "entities.csv"))
technologies = pd.read_csv(os.path.join(DATA_DIR, "technologies.csv"))
observations = pd.read_csv(os.path.join(DATA_DIR, "observations.csv"))
codes        = pd.read_csv(os.path.join(DATA_DIR, "codes.csv"))

# Market data observations for 1995
market_data = observations[
    (observations["observation_type"] == "market-data") &
    (observations["year_observed"] == 1995)
]

# Revenue observations for HP
hp_revenue = observations[
    (observations["entity_id"] == "hewlett-packard") &
    (observations["metric_name"].str.contains("revenue", case=False))
]

# All viability predictions
predictions = observations[observations["observation_type"] == "viability-prediction"]
print(predictions[["obs_id", "year_observed", "metric_name", "metric_value"]])
```

---

## Validation

Run the included validation script:

```bash
python scripts/demo_analysis.py
```

The script will:
- Load all five CSV files
- Report row counts and study metadata
- Validate referential integrity (all entity_id, tech_id, methodology_code references)
- Verify code coverage (all codes used in observations exist in codes.csv)
- Print market revenue summary tables
- Report entity status distribution and technology lifecycle summary

### Frictionless Data Validation

```bash
pip install frictionless
frictionless validate datapackage.json
```

---

## Methodology

Aberdeen's annual commercial RISC/Unix market review combines three methodologies:

1. **Revenue Benchmarking**: End-user revenue for core platform components (RISC-based
   multiuser systems + attached storage + Unix OS + installation/maintenance services).
   Explicitly excludes RDBMS, applications, networking, professional services, internet
   servers, file/print servers, and workstations.

2. **Competitive Profiling**: Detailed analysis of each major vendor's strategy, product
   roadmap, distribution approach, and competitive positioning through Aberdeen's market
   intelligence.

3. **Field Research**: IS executive interviews conducted throughout 1995 to capture
   buying motivations, platform selection rationale, and implementation experience.

---

## Citation

```
Aberdeen Group. (1996, February 12). Commercial, Multiuser Risc/Unix 1995:
  High Growth and HP Dominate. Aberdeen Group Market Viewpoint, 9(5).
  [Archived] https://web.archive.org/web/19970112010549/http://www.aberdeen.com:80/secure/viewpnts/v9n5/v9n5.htm
  Licensed under CC-BY-4.0. Dataset DOI: [pending Zenodo deposit]
```

---

## File Structure

```
aberdeen-1996-risc-unix-market/
├── README.md                      ← This file
├── datapackage.json               ← Frictionless Data Package descriptor
├── data/
│   ├── studies.csv                ← 1 row: study metadata + abstract
│   ├── entities.csv               ← 36 rows: organizations mentioned
│   ├── technologies.csv           ← 29 rows: platforms, OSes, apps
│   ├── observations.csv           ← 66 rows: all factual claims and predictions
│   └── codes.csv                  ← 27 rows: controlled vocabulary
├── schema/
│   └── schema_org.json            ← Schema.org/Dataset JSON-LD for discovery
└── scripts/
    └── demo_analysis.py           ← Validation and analysis script
```

---

*Processed as part of the Aberdeen Group Archival Ingest project. Source: Aberdeen Group, Inc., One Boston Place, Boston MA 02108 USA. Copyright © 1996 Aberdeen Group, Inc. Dataset license: CC-BY-4.0.*
