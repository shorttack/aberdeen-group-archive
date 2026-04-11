# RS/6000 RDBMS Sales Training

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1995-01-01 |
| Type | benchmark |
| Domain | RDBMS-competitive-analysis, midrange-servers |
| License | CC-BY-4.0 |

## Abstract

An IBM sales training deck prepared by Aberdeen Group in 1995 providing competitive intelligence on the midrange RISC/UNIX market and the major RDBMS vendors. The document profiles IBM RS/6000, HP, Digital, Sun, and AT&T GIS as hardware platforms, then positions IBM's RS/6000 and DB2/6000 against Oracle, Informix, Sybase, and other database competitors. It gives IBM sales representatives detailed strengths, weaknesses, and tactical selling tips for each competitor.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 15 |
| technologies.csv | 25 |
| observations.csv | 31 |
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

Peter S. Kastner (1995). RS/6000 RDBMS Sales Training.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

competitive-profiling, industry-analysis, benchmarking, expert-opinion
