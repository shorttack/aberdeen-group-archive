# Linuxcare, Inc. -- Enterprise Service and Support for All Things Linux

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1999-11-01 |
| Type | case-analysis |
| Domain | enterprise-linux-services |
| License | CC-BY-4.0 |

## Abstract

An Aberdeen Group company profile of Linuxcare, Inc. published in November 1999, assessing the startup's viability as the first enterprise Linux services and support company. The paper evaluates Linuxcare's four service pillars (24x7 support training porting and certification), its key OEM contracts with Dell IBM and Sun, and its Kleiner Perkins Caulfield and Byers backing. Aberdeen concludes that a credible enterprise Linux services market exists and recommends Linuxcare be considered by IT executives seeking Linux as an alternative enterprise OS.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 18 |
| technologies.csv | 8 |
| observations.csv | 28 |
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

Peter S. Kastner (1999). Linuxcare, Inc. -- Enterprise Service and Support for All Things Linux.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

company-profile,industry-analysis,primary-research
