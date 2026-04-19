# Intel's Fall Developer Forum (IDF): Megahertz is Dead, Long Live Dual-Core (Revised)

| Field | Value |
|-------|-------|
| Author | Nathan Brookwood (Insight 64) |
| Date | 2004-09-16 |
| Type | market-study |
| Domain | microprocessors/multicore-transition |
| License | CC-BY-4.0 |

## Abstract

Insight 64 analyst report by Nathan Brookwood on Intel Fall 2004 IDF. Paul Otellini officially closed two decades of MHz-driven CPU scaling and announced the shift to multi-core parallelism. Analyzes the NetBurst power/performance trend, Pentium M Dothan (2GHz/21W, 140M transistors) versus Prescott (3.2GHz/82W, 125M) as exemplars of architecture over brute-force frequency, and the competitive bus-bandwidth disadvantage (3.2GB/s versus AMD's 13.2GB/s) if Intel used an inelegant dual-core design. Preserved in the Kastner archive as external reference material.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 13 |
| observations.csv | 18 |
| codes.csv | 25 |

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

Nathan Brookwood (Insight 64) (2004). Intel's Fall Developer Forum (IDF): Megahertz is Dead, Long Live Dual-Core (Revised).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, competitive-profiling, expert-opinion
