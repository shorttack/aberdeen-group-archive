# Timex RAMP Interview for Maxtor Project

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner; David Hill |
| Date | 2003-04-16 |
| Type | market-study |
| Domain | enterprise-storage / consumer-manufacturing |
| License | CC-BY-4.0 |

## Abstract

Face-to-face RAMP interview with Robert (Bob) Lutz, Manager IT Operations at Timex (Middlebury CT), covering enterprise storage architecture, unwillingness to adopt additional storage tiers, and the critical insight that administrative costs dwarf hardware costs in storage decision-making. Timex had 6TB local / 10TB worldwide with 80% utilization and 80% inactive data, yet rated only 2/7 willingness to adopt low-cost disk. Lutz articulated that tight budgets and reduced headcount make adding a storage management tier more costly than the hardware savings — a foundational insight for the storage automation and hyperconverged infrastructure markets.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 13 |
| observations.csv | 35 |
| codes.csv | 45 |

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

Peter S. Kastner; David Hill (2003). Timex RAMP Interview for Maxtor Project.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

face-to-face-interview, market-research, vendor-evaluation
