# Can Parallel-Scalable RDBMSs Break the Downsizing Logjam?

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner / Aberdeen Group |
| Date | 1995 |
| Type | consulting-report |
| Domain | database technology; parallel computing; RDBMS architecture |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group analysis arguing that parallel-scalable RDBMS technology can resolve the 'downsizing logjam' caused by exploding information demand. Covers SMP, cluster and MPP architectures; fine-grain multiprocessor support; parallel administration; dynamic resource scalability; and selection criteria for parallel-scalable RDBMSs. 23-slide deck used in Informix sales training.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 2 |
| technologies.csv | 5 |
| observations.csv | 20 |
| codes.csv | 27 |

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

Peter S. Kastner / Aberdeen Group (1995). Can Parallel-Scalable RDBMSs Break the Downsizing Logjam?.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

expert-analysis; vendor briefing
