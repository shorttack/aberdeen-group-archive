# The Business Value in IT Outsourcing

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2006-05-25 |
| Type | white-paper |
| Domain | IT Outsourcing / Enterprise IT Management |
| License | CC-BY-4.0 |

## Abstract

Aberdeen research brief announcing a benchmark study on IT outsourcing business value, to be published late June 2006. Identifies five key drivers for outsourcing (core competency focus, cost savings, resource constraints, time-to-market, culture wars); describes a maturity model for outsourcing outcomes; classifies enterprises into three tiers: misaligned (~30%), sub-optimal (50-67%), and optimal (5-10%) outsourcing engagements. Author is Peter Kastner, VP Enterprise Integration Research.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 2 |
| technologies.csv | 6 |
| observations.csv | 18 |
| codes.csv | 30 |

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

Peter S. Kastner (2006). The Business Value in IT Outsourcing.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Research announcement/brief; hypothesis-driven benchmark study design; references prior Aberdeen survey data (2,000+ companies over 2 years); maturity model framework
