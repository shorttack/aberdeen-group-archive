# Industry Analyst Visionaries on 64-bit Computing

| Field | Value |
|-------|-------|
| Author | AMD (publisher) |
| Date | 2003-09-01 |
| Type | vendor-publication |
| Domain | amd64-x86-64-mainstream-adoption |
| License | CC-BY-4.0 |

## Abstract

AMD curates 64-bit-computing perspectives from major IT analysts ahead of the AMD64 (Opteron/Athlon 64) launch wave. Peter Kastner of Aberdeen Group provides one of the most explicit predictions: the majority of consumer 64-bit demand arrives by end of decade, and mainstream desktops will need full 64-bit RAM addressability by 2010 due to declining memory prices, additional OS features, and web services.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 6 |
| observations.csv | 8 |
| codes.csv | 25 |

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

AMD (publisher) (2003). Industry Analyst Visionaries on 64-bit Computing.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

expert-quote-aggregation, vendor-marketing
