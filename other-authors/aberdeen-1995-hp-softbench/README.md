# Aberdeen Group — HP C++ SoftBench 5.0 (1995)

**Study ID:** `aberdeen-1995-hp-softbench`  
**Package Version:** 1.0.0  
**Created:** 2026-03-13  

---

## Overview

This Frictionless Data Package archives and structures Aberdeen Group's December 1995 executive white paper:

> *"Hewlett-Packard's C++ SoftBench 5.0 -- A Powerful Platform for Professional Developers"*

The white paper evaluates HP's C++ SoftBench 5.0 integrated development environment (IDE) for object-oriented software development. Aberdeen argued that the time to adopt object technology had arrived and positioned SoftBench as an industrial-strength solution for professional developer teams.

**Source URL (Wayback Machine):** https://web.archive.org/web/19970112011047/http://www.aberdeen.com:80/secure/whtpaper/softbnch/softbnch.htm

---

## Study Details

| Field | Value |
|---|---|
| Title | Hewlett-Packard's C++ SoftBench 5.0 -- A Powerful Platform for Professional Developers |
| Author | Aberdeen Group |
| Date | December 1995 (1995-12-01) |
| Type | White Paper |
| Domain | Software Development Tools |
| Methodology | Industry Analysis, Competitive Profiling, Field Research |

---

## Repository Structure

```
aberdeen-1995-hp-softbench/
├── datapackage.json          # Frictionless Data Package descriptor
├── README.md                 # This file
├── data/
│   ├── studies.csv           # Study-level metadata (1 row)
│   ├── entities.csv          # Organizations mentioned + current status (15 rows)
│   ├── technologies.csv      # Technologies mentioned + lifecycle status (26 rows)
│   ├── observations.csv      # Structured claims and findings (45 rows)
│   └── codes.csv             # Reference codelist for all controlled vocabulary (36 rows)
├── schema/
│   └── schema_org.json       # Schema.org Dataset JSON-LD metadata
└── scripts/
    └── demo_analysis.py      # Python demo: load and analyze the data package
```

---

## Data Files

### `data/studies.csv`
Single-row table containing study-level metadata including title, author, date, type, domain, methodology, and abstract.

### `data/entities.csv`
All organizations and companies referenced in the study (15 entities), including:
- **Current status** as of 2026 (active, acquired, split, merged, dissolved)
- **Status notes** explaining corporate history (e.g., HP's 2015 split, Taligent's 1998 dissolution, Micro Focus acquired by OpenText 2023)

Key entity outcomes:
| Entity (1995) | Current Status | Notes |
|---|---|---|
| Hewlett-Packard | Split (2015) | Became HP Inc. (consumer) + HPE (enterprise) |
| Taligent | Dissolved (1998) | Absorbed into IBM January 1998 |
| Micro Focus | Acquired (2023) | Acquired by OpenText January 2023 |
| OSF | Merged (1996) | Merged with X/Open to form The Open Group |
| Sun Microsystems | Acquired (2010) | Acquired by Oracle Corporation |
| Informix | Acquired (2001) | Acquired by IBM; support ended April 2025 |

### `data/technologies.csv`
All technologies, products, standards, and platforms referenced in the study (26 items), with current lifecycle status:

| Status | Count | Examples |
|---|---|---|
| active | 5 | C++, Oracle DB, CICS, XEmacs, Micro Focus COBOL |
| legacy | 6 | COBOL, HP-UX, Solaris, CORBA, Sybase, CDE |
| largely-obsolete | 1 | DCE |
| obsolete | 11 | SoftBench, OODCE, HP DST, UIM/X, VUE, DB2/9000, etc. |
| discontinued | 1 | CommonPoint (Taligent) |

### `data/observations.csv`
45 structured observations extracted from the study covering:
- Market findings from Aberdeen field research
- Product claims about SoftBench features
- Analyst evaluations and recommendations
- Deployment patterns and service descriptions
- Vendor roadmap claims
- Risk and requirement findings

Observations span all four PDF pages and all major document sections.

### `data/codes.csv`
Reference codelist (36 rows) defining all controlled vocabulary values used across the data files:
- `observation_type` — 15 types (market-finding, product-claim, analyst-opinion, etc.)
- `sentiment` — 4 values (positive, negative, neutral, cautionary)
- `entity_status` — 6 values (active, acquired, split, merged, dissolved, successor-entity)
- `tech_lifecycle` — 5 values (active, legacy, largely-obsolete, obsolete, discontinued)
- `study_type`, `domain`, `methodology` — additional reference codes

---

## Key Findings (1995 Context)

1. **Aberdeen's OO endorsement:** Aberdeen firmly endorsed object technology adoption in 1995, concluding that "with appropriate levels of training and support -- the time to implement object technology is now."

2. **Four critical success factors:** Aberdeen identified four prerequisites for successful OO adoption: robust tools, adequate training, implementation expertise, and a trusted leadership vendor. Missing any one factor significantly increased risk of failure.

3. **SoftBench positioning:** Aberdeen characterized C++ SoftBench as "an industrial-strength option" covering the full SDLC from analysis through testing, with 80+ encapsulated third-party tools.

4. **CodeAdvisor as an innovation:** Aberdeen described the new CodeAdvisor module as "an elegant way to teach new C++ developers the subtleties of OO programming" that would "significantly accelerate object adoption timetables."

5. **HP's financials as a trust signal:** Aberdeen cited HP's $25 billion in annual revenues as evidence that HP had the resources to serve as a reliable long-term software partner.

6. **CommonPoint and Taligent:** HP was porting Taligent's CommonPoint C++ framework to HP-UX. Taligent dissolved in January 1998; CommonPoint was discontinued.

---

## Technology Lifecycle Notes

Several technologies prominent in this 1995 study have since become obsolete:

- **SoftBench** was discontinued with HP-UX developer tools and is no longer available.
- **HP-UX** reached end-of-life on December 31, 2025.
- **DCE** was largely replaced by web services and REST.
- **CORBA** survives in limited legacy deployments but was supplanted by web services.
- **CommonPoint** was discontinued when Taligent was dissolved into IBM in 1998.
- **C++** remains widely active with C++23 published and C++26 in progress.
- **COBOL** remains in extensive use in mainframe and legacy financial systems.

---

## Entity Status Notes

- **HP split (2015):** Hewlett-Packard divided into HP Inc. (personal computers and printers) and Hewlett Packard Enterprise (servers, networking, software, services) on November 1, 2015.
- **Taligent dissolved (1998):** The Apple/IBM/HP joint venture was formally dissolved January 1998; engineering teams became IBM employees. Source: [Taligent Company History](https://www.wildcrest.com/Potel/Portfolio/InsideTaligentTechnology/WW87.htm)
- **Micro Focus acquired (2023):** OpenText closed acquisition of Micro Focus on January 31, 2023. Source: [OpenText press release](https://investors.opentext.com/press-releases/press-releases-details/2023/OpenText-Buys-Micro-Focus/default.aspx)
- **OSF merged (1996):** Open Software Foundation merged with X/Open to form The Open Group. Source: [The Open Group Wikipedia](https://en.wikipedia.org/wiki/The_Open_Group)
- **Sun Microsystems acquired (2010):** Oracle completed acquisition of Sun on January 27, 2010. Source: [Oracle press release](https://www.oracle.com/corporate/pressrelease/oracle-buys-sun-042009.html)
- **Informix acquired (2001):** IBM acquired Informix in 2001; IBM ended continuing support April 30, 2025. Source: [IBM support page](https://www.ibm.com/support/pages/continuing-support-ibm-informix-ends-30-april-2025)

---

## Usage

### Python (with frictionless library)
```python
from frictionless import Package

pkg = Package("datapackage.json")
studies = pkg.get_resource("studies").read()
observations = pkg.get_resource("observations").read()
```

### Demo Analysis Script
```bash
python scripts/demo_analysis.py
```

The demo script loads all CSV files, prints summary statistics, and shows example analyses including observation type distribution, sentiment breakdown, and technology lifecycle counts.

---

## Reproducibility

All source data is extracted from the archived PDF. Entity and technology status information was verified via web search in March 2026 against sources including:
- [HP split announcement (investor.hp.com)](https://investor.hp.com/news-events/news/news-details/2015/HP-Board-of-Directors-Approves-Separation/default.aspx)
- [Taligent history (wildcrest.com)](https://www.wildcrest.com/Potel/Portfolio/InsideTaligentTechnology/WW87.htm)
- [OpenText acquires Micro Focus (opentext.com)](https://investors.opentext.com/press-releases/press-releases-details/2023/OpenText-Buys-Micro-Focus/default.aspx)
- [The Open Group on Wikipedia](https://en.wikipedia.org/wiki/The_Open_Group)
- [Oracle acquires Sun (oracle.com)](https://www.oracle.com/corporate/pressrelease/oracle-buys-sun-042009.html)
- [IBM Informix end of support (ibm.com)](https://www.ibm.com/support/pages/continuing-support-ibm-informix-ends-30-april-2025)

---

*Copyright © 1995 Aberdeen Group, Inc., Boston, Massachusetts. Original document rights reserved by Aberdeen Group. This data package is created for archival and research purposes.*
