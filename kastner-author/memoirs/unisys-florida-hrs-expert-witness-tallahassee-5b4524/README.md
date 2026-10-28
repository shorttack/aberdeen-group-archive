# Unisys vs. Florida HRS — Expert Witness Memoir (Senate Chamber Tallahassee, c.1990-1991)

> **Correction, October 28, 2026 (PENDING-CHANGES row 49, Kastner, 2026-09-07).** Earlier versions of this package described the IBM/EDS proposal and the as-built FLORIDA system as "DB2 on mainframe." The database was IMS (IMS DB and IMS/TM), as the as-built review in Auditor General Report 13287 (pp. 15–16) and the FLORIDA archive README § 5 establish; no contemporaneous proposal document establishes DB2. DB2 has been replaced by IMS throughout; the `ibm-db2` technology association was replaced by `ibm-ims`.

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner (memoir); Perplexity AI (research context) |
| Date | 2026-01-12 |
| Type | memoir |
| Domain | IT-litigation; government-procurement; mainframe-vs-distributed-architecture |
| License | CC-BY-4.0 |

## Abstract

Peter S. Kastner recalls his expert-witness role in the Florida Department of Health and Rehabilitative Services (HRS) bid protest — Unisys vs. IBM/EDS — in the early 1990s. Kastner went through a box of computer paper to find the single IBM performance estimate sheet that proved the proposed mainframe plus IMS architecture could not support the required terminal counts and average response time, and testified in the Florida Senate Chamber in Tallahassee. Although Unisys lost the bid, the IBM/EDS implementation failed catastrophically — a $200 million fiasco involving system crashes during food stamp distribution, national records for error rates, and EDS suing for $46 million in unpaid bills. The fallout helped motivate Congress to pass two pieces of Senator William Cohen's IT-procurement reform legislation — the Information Technology Management Reform Act and the Federal Acquisition Reform Act (jointly the Clinger-Cohen Act of 1996) — which remain in force today. era: 1990s; mood: reflective; trigger: Perplexity research session January 2026 on government IT procurement disasters

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 17 |
| technologies.csv | 11 |
| observations.csv | 40 |
| codes.csv | 24 |

## Load with Python

```python
import pandas as pd
studies = pd.read_csv('data/studies.csv')
observations = pd.read_csv('data/observations.csv')
```

## Validate

```bash
frictionless validate datapackage.json
```

## Citation

Peter S. Kastner (memoir); Perplexity AI (research context) (2026). Unisys vs. Florida HRS — Expert Witness Memoir (Senate Chamber Tallahassee, c.1990-1991).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

oral-history, archival-research
