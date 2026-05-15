# Appendix: Career Timeline

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2026-05-14 |
| Type | memoir |
| Domain | memoir/volume-1 |
| License | CC-BY-4.0 |

## Abstract

A structured career timeline spanning Kastner's six-decade arc in computing, from 1960 bookkeeping frustrations through mainframe operation, consulting, vendor marketing, and co-founding Aberdeen Group. The appendix also documents key technology platform transitions witnessed first-hand, Aberdeen Group's complete financial history (1990–2006), and a detailed founding chronology of the Transaction Processing Performance Council (TPC).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 25 |
| technologies.csv | 21 |
| observations.csv | 90 |
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

Peter S. Kastner (2026). Appendix: Career Timeline.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

oral-history
