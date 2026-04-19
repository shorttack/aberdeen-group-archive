# interBiz Solutions BizWorks Profile — Management Command and Control for the E-World

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1999-01-01 |
| Type | employer-record |
| Domain | employer/aberdeen-group |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group analyst profile (c. 1999) of interBiz Solutions, the new application software and services division of Computer Associates, and its BizWorks framework for cross-enterprise application integration. The profile positions BizWorks as the infrastructure that would tie best-of-breed applications and processes together, leveraging CA's Unicenter TNG management, Jasmine object database, 3D visualization, and Neugents pattern-recognition agents. Argues that enterprises should 'buy' BizWorks rather than 'make' equivalent integration themselves.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 5 |
| observations.csv | 15 |
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

Peter S. Kastner (1999). interBiz Solutions BizWorks Profile — Management Command and Control for the E-World.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

competitive-profiling, technology-assessment
