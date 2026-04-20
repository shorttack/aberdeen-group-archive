# Is Sun's SPARC Architecture on Life Support?

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2009-06-17 |
| Type | memoir |
| Domain | memoir |
| License | CC-BY-4.0 |

## Abstract

Kastner blog post on OnComputersTips observing Sun's long-hyped Rock chip is apparently dead and that — with the pending Oracle-Sun merger and Solaris already on X64 commodity servers — the case for SPARC is gone. Kastner muses that Oracle has the opportunity to create a one-stop IT shop with the full hardware-to-application stack, unmatched since IBM exited the application software business 40 years earlier.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 6 |
| observations.csv | 7 |
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

Peter S. Kastner (2009). Is Sun's SPARC Architecture on Life Support?.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

oral-history
