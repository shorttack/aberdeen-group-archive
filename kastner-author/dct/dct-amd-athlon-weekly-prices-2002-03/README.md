# AMD Athlon XP Weekly CPU Pricing, Jul 2002 – 2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-12-31 |
| Type | dct |
| Domain | dct |
| License | CC-BY-4.0 |

## Abstract

Weekly tracking of AMD Athlon XP 1800+, 2000+, 2100+, 2200+, 2400+, and 2600+ pricing across 40 selling dates from July 2002 through 2003, producing 155 model-week price observations. Captures AMD's competitive pricing posture against the Intel Pentium 4 in the consumer/channel CPU market during the peak of the PC price war.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 1 |
| technologies.csv | 6 |
| observations.csv | 12 |
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

Peter S. Kastner (2003). AMD Athlon XP Weekly CPU Pricing, Jul 2002 – 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking
