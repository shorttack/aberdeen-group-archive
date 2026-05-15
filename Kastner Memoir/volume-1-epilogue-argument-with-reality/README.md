# Epilogue: The Argument with Reality

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2026-05-14 |
| Type | memoir |
| Domain | memoir/volume-1 |
| License | CC-BY-4.0 |

## Abstract

Kastner reflects on fifty years in computing, observing that every technical breakthrough—from timesharing to the web to AI—has been slowed by organizational inertia, misaligned incentives, and the stubbornly human character of institutions. He offers an honest accounting of what Aberdeen got right (open systems, client-server, relational databases) and what it missed (the speed of the web, the depth of organizational resistance to data integration, and the culture-destroying effects of growth capital). The epilogue concludes that the fundamental constraint in computing has always been not the machine but the human organization around it.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 7 |
| technologies.csv | 10 |
| observations.csv | 41 |
| codes.csv | 26 |

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

Peter S. Kastner (2026). Epilogue: The Argument with Reality.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

oral-history
