# Aberdeen Group – IBM's AS/400 and SAP's R/3 (1995)

**Study ID:** `aberdeen-1995-ibm-as400-sap-r3`  
**Study Number:** 11  
**Title:** IBM's AS/400 and SAP's R/3: Making the Complex and Slow Both Simple and Fast  
**Author:** Aberdeen Group  
**Date:** September 1995  
**Type:** Product Profile  
**Domain:** Enterprise Computing / ERP  
**Methodology:** Industry Analysis, Competitive Profiling, Benchmarking  

**Original Source (Wayback Machine):**  
https://web.archive.org/web/19970604114147/http://www.aberdeen.com:80/secure/profiles/ibm_sap/ibm_sap.htm

---

## Overview

This Frictionless Data Package archives a 1995 Aberdeen Group product profile examining the partnership between IBM's AS/400 Division and SAP AG. The study evaluated the combination of IBM's AS/400 Advanced Series servers (powered by the new 64-bit PowerPC AS RISC processors) and SAP's R/3 version 3.0 enterprise resource planning suite as a compelling platform for enterprise reengineering.

The partnership was announced in September 1995. SAP planned a beta rollout to select customers in November 1995, controlled release in Q1 1996, and general availability in Q2 1996. The study argued that the combination offered a unique value proposition: the implementation simplicity of the AS/400 combined with the leading-edge business functionality of SAP R/3.

---

## Key Findings from the Study

### Market Position (as of 1995)
- IBM had shipped over **325,000 AS/400 systems** worldwide since launch
- IBM AS/400 Division **1994 revenues: ~$13 billion**, representing **~35% of all IBM division profits**
- AS/400 revenue grew **25%** in the year prior to publication
- SAP became the **first packaged-application vendor to capture $1 billion in annual revenue**
- SAP America showed **~100% year-over-year revenue growth**
- R/3 accounted for **two-thirds of SAP's worldwide revenues** and **>85% of North American revenues**
- SAP invested **20–25% of revenues** in R&D

### Technology Claims (64-bit RISC advantage)
Aberdeen cited that a 64-bit RISC-based AS/400, versus an equivalently configured non-64-bit system, could:
- Support **more than 2× the users**
- Handle **up to 5× the transaction workload**
- Address databases **orders-of-magnitude greater in size**

### Target Market
- IBM and SAP initially targeted enterprises with **>$300 million revenue**
- Future volume market: **$50–$500 million** midrange companies

---

## Package Structure

```
aberdeen-1995-ibm-as400-sap-r3/
├── datapackage.json          # Frictionless Data Package descriptor
├── README.md                 # This file
├── data/
│   ├── studies.csv           # Study metadata (1 row)
│   ├── entities.csv          # Organizations with current status (12 rows)
│   ├── technologies.csv      # Technologies with lifecycle info (11 rows)
│   ├── observations.csv      # All extracted observations (106 rows)
│   └── codes.csv             # Controlled vocabulary (34 codes)
├── schema/
│   └── schema_org.json       # Schema.org Dataset descriptor
└── scripts/
    └── demo_analysis.py      # Python demonstration analysis script
```

---

## Data Tables

### studies.csv
Single row with study metadata including title, author, date, type, domain, methodology, abstract, and source URL.

### entities.csv (12 entities)
| Entity | Type | Status (2026) |
|--------|------|---------------|
| IBM Corporation | vendor | active |
| IBM AS/400 Division | product-division | folded → IBM Power Systems |
| SAP AG | vendor | rebranded → SAP SE (2014) |
| SAP America Inc. | subsidiary | active |
| ISSC (IBM Integrated Systems Solutions) | subsidiary | rebranded → IBM Global Services |
| Unisys | vendor | active |
| Digital Equipment Corporation (DEC) | vendor | acquired → Compaq → HP |
| Hewlett-Packard | vendor | active (split into HP Inc. / HPE) |
| Bull SA | vendor | acquired → Atos (2014) |
| ICL (International Computers Limited) | vendor | acquired → Fujitsu (1990/1998) |
| Siemens (IT division) | vendor | rebranded → Fujitsu Siemens → Fujitsu |
| Aberdeen Group Inc. | analyst-firm | acquired → Harte-Hanks (2001) |

### technologies.csv (11 technologies)
| Technology | Category | Status (2026) |
|------------|----------|---------------|
| AS/400 Advanced Series | hardware-platform | renamed → IBM i |
| PowerPC AS (64-bit RISC) | processor | superseded → POWER architecture |
| OS/400 V3R6 | operating-system | renamed → IBM i OS |
| SAP R/3 v3.0 | erp-suite | superseded → SAP S/4HANA |
| SAP R/2 | erp-suite | superseded → SAP R/3 |
| DB2/400 | database | active (Db2 for i) |
| ABAP/4 Development Workbench | development-tool | active (ABAP) |
| Three-Tier Client-Server Architecture | architecture | active |
| R/3 Repository / SAP Information Model | development-tool | superseded → SAP BTP |
| IBM System/3X line | hardware-platform | superseded → AS/400 |
| Windows GUI (3.1 / NT) | operating-system | active |

### observations.csv (106 rows)
Covers:
- **Financial metrics** (8 rows): IBM AS/400 Division revenue, profits, growth; SAP revenue milestones, growth rates, R&D spending
- **Market data** (5 rows): systems shipped, target enterprise sizes, ICOEs, customer penetration
- **Performance claims** (3 rows): 64-bit RISC advantages vs 32-bit systems
- **Product specs** (63 rows): Full Table 1 – all 7 AS/400 Advanced Series models (40S, 50S, 53S, 400, 500, 510, 530) with processors, memory, disk, users, TPm
- **Product modules** (22 rows): Full Table 2 – all SAP R/3 modules across Accounting, Logistics, Human Resources, and Industry Solutions
- **Partnership** (1 row): IBM-SAP announcement date
- **Competitive claims** (2 rows): analyst recommendations
- **Customer data** (2 rows): Global 100 penetration, beta trial demand

### codes.csv (34 codes)
Controlled vocabulary covering: study_type, domain, methodology, entity_type, entity_status, tech_status, tech_category, and obs_type.

---

## Entity Status Notes

- **SAP AG → SAP SE**: Converted to European Company (Societas Europaea) on 7 July 2014, following 99% shareholder approval at the AGM on 21 May 2014.
- **Bull SA → Atos**: Atos acquired Bull in August 2014 for approximately €620 million (~$844 million).
- **ICL → Fujitsu**: Fujitsu acquired 80% of ICL in 1990 for $1.26 billion; became sole shareholder in 1998; ICL brand dropped 2002.
- **ISSC → IBM Global Services**: IBM's professional services arm was rebranded as IBM Global Services in 1996.
- **IBM AS/400 Division**: Folded into IBM's broader systems organization; AS/400 platform renamed iSeries (2000), System i (2006), IBM i (2008); still active.
- **DEC**: Acquired by Compaq in 1998; Compaq acquired by HP in 2002.

---

## Technology Lifecycle Notes

- **AS/400 → iSeries → System i → IBM i**: Platform still active. SAP R/3 on IBM i continued for decades.
- **PowerPC AS → POWER**: The PowerPC AS processor architecture evolved into IBM's POWER line, which remains active today.
- **OS/400 → IBM i OS**: Renamed along with the platform; still in active development.
- **SAP R/3 → SAP ERP (ECC) → SAP S/4HANA**: R/3 mainstream maintenance ended; S/4HANA is the current platform.
- **DB2/400 → Db2 for i**: Still active and integral to IBM i.
- **ABAP/4 → ABAP**: SAP's development language remains central to SAP development.

---

## Usage

### Load with Python (frictionless)
```python
from frictionless import Package

pkg = Package("datapackage.json")
studies = pkg.get_resource("studies").read()
entities = pkg.get_resource("entities").read()
observations = pkg.get_resource("observations").read()
```

### Run the demo analysis
```bash
python scripts/demo_analysis.py
```

### Load with pandas
```python
import pandas as pd

studies = pd.read_csv("data/studies.csv")
entities = pd.read_csv("data/entities.csv")
technologies = pd.read_csv("data/technologies.csv")
observations = pd.read_csv("data/observations.csv")
codes = pd.read_csv("data/codes.csv")
```

---

## Citation

Aberdeen Group. (1995, September). *IBM's AS/400 and SAP's R/3: Making the Complex and Slow Both Simple and Fast*. Aberdeen Group, Inc., Boston, MA. Archived at: https://web.archive.org/web/19970604114147/http://www.aberdeen.com:80/secure/profiles/ibm_sap/ibm_sap.htm

---

## License

Data package structure and annotations: Open Data Commons Attribution License (ODC-BY).  
Original study content: Copyright © 1996 Aberdeen Group, Inc., Boston, Massachusetts. All rights reserved. Reproduced here for archival and research purposes.
