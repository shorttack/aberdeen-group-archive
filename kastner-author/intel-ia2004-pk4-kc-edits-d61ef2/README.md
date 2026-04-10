# Planning for Emerging Industry-Standard Platforms Computing Opportunities

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-07 |
| Type | white-paper |
| Domain | Enterprise IT Hardware / Semiconductor |
| License | CC-BY-4.0 |

## Abstract

Aberdeen white paper produced in collaboration with Intel Corporation analyzing the three critical technology building blocks arriving in 2003-2004: DDR2 memory, IPMI systems management, and serial I/O (PCI Express). Covers Xeon, Itanium 2, new chipsets (Lindenhurst, Nocona, Potomac/Twin Castle), and the transition from parallel PCI-X to PCI Express. Aimed at IT planners for 2004 server acquisitions.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 20 |
| observations.csv | 25 |
| codes.csv | 32 |

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

Peter S. Kastner (2003). Planning for Emerging Industry-Standard Platforms Computing Opportunities.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

expert-analysis; vendor collaboration
