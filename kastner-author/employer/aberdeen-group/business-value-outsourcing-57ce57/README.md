# The Business Value in IT Outsourcing

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner, Aberdeen Group |
| Date | 2006-05-25 |
| Type | employer-record |
| Domain | IT Outsourcing / IT Organizational Maturity |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Hypothesis paper (6pp) previewing planned benchmark on IT outsourcing business value. Identifies five drivers for IT outsourcing: core competency focus, cost savings, IT resource constraints, time-to-market pressure, and culture wars. Hypothesizes up to 30% of IT outsourcing engagements are seriously misaligned. Finds 50-67% of contracts running at sub-optimal levels. Estimates only 5-10% of multi-million dollar IT outsourcing agreements drive all anticipated business value. Uses IT maturity model: Best-in-Class (20%), Average (50%), Laggard (30%). Best-in-Class measure ROI after every application change (50%) vs. Laggard (25%).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 2 |
| technologies.csv | 5 |
| observations.csv | 17 |
| codes.csv | 33 |

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

Peter S. Kastner, Aberdeen Group (2006). The Business Value in IT Outsourcing.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Benchmark survey (2,000+ companies surveyed on IT in past two years); qualitative interviews; IT maturity model
