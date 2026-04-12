# State Street RAMP Interview for Maxtor Project

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner; David Hill |
| Date | 2003-04-01 |
| Type | market-study |
| Domain | enterprise-storage / financial-services |
| License | CC-BY-4.0 |

## Abstract

Face-to-face RAMP (Rapid Analysis Market Profiling) interview with Prithwi R. Thakuria, VP Information Technology Data Management Services at State Street (Westwood MA), covering Unix SAN storage architecture, willingness to adopt low-cost ATA disk, EMC Symmetrix/DMX infrastructure, and backup/restore practices. State Street had ~1TB Unix storage, all on SAN, 70-80% FC, with EMC Symmetrix RAID-1 and planned DMX upgrade. Thakuria rated 7/7 likelihood to purchase low-cost disk despite SLA obligations to investment management clients, citing TCO savings. The interview captures the financial sector's early-mover posture toward midline storage and the multi-silo purchasing decision structure of large banks.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 10 |
| observations.csv | 35 |
| codes.csv | 42 |

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

Peter S. Kastner; David Hill (2003). State Street RAMP Interview for Maxtor Project.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

face-to-face-interview, market-research, vendor-evaluation
