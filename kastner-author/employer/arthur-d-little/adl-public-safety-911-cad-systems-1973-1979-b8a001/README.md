# ADL Public Safety / 911 CAD Systems: Boston, Philadelphia, Minneapolis, Aurora, and St. Petersburg (1973-1979)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2025-08-15 |
| Type | employer-record |
| Domain | employer/arthur-d-little/public-safety-CAD |
| License | CC-BY-4.0 |

## Abstract

Kastner's role at Arthur D. Little Systems (ADLS) on the federally-funded LEAA-grant 911 computer-aided dispatch (CAD) systems built in the 1970s. ADLS designed a fault-tolerant dual-Data-General-Eclipse minicomputer dispatch architecture first deployed in Boston, then migrated to Philadelphia, Minneapolis, and Aurora CO. As vendor support manager, Kastner led hardware configuration, procurement, burn-in, and installation for all four cities. He separately led ADL's design of the St. Petersburg FL 911 dispatch on the city's IBM 370/135 with CICS, recommending and modifying the Hampton Roads VA dispatch system for transfer.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 20 |
| technologies.csv | 9 |
| observations.csv | 23 |
| codes.csv | 31 |

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

Peter S. Kastner (2025). ADL Public Safety / 911 CAD Systems: Boston, Philadelphia, Minneapolis, Aurora, and St. Petersburg (1973-1979).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

oral-history, document-review, industry-analysis
