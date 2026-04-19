# Dell, Oracle & Linux: Your Next SAP Platform? A Major EBA Replacement Cycle is Underway

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner (Executive Vice President, Technology Research, Aberdeen Group) |
| Date | 2004-05-01 |
| Type | market-study |
| Domain | enterprise-business-applications |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Perspective on the April 28, 2004 Dell-SAP announcement. Argues that over 10,000 Y2K-generation RISC-Unix EBA systems are obsolete and ready for replacement, and positions the Dell/SAP/Oracle/Linux clustered-Intel stack (NetWeaver + mySAP/R3 + Oracle 9i RAC/10g + Dell|EMC SAN) as a lower-cost, standards-based successor. Notes a two-node Dell 6650 cluster delivered 9-16% better SD performance than 8-way RISC/Xeon/Itanium SMP at one-third the cost.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 17 |
| observations.csv | 27 |
| codes.csv | 23 |

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

Peter S. Kastner (Executive Vice President, Technology Research, Aberdeen Group) (2004). Dell, Oracle & Linux: Your Next SAP Platform? A Major EBA Replacement Cycle is Underway.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, competitive-profiling, expert-opinion, architecture-assessment
