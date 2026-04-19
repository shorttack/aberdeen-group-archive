# Sun's AS/400 Market Opportunity — Aberdeen Presentation to Sun Microsystems

| Field | Value |
|-------|-------|
| Author | Peter Kastner |
| Date | 2002-04-20 |
| Type | white-paper |
| Domain | server-market-strategy |
| License | CC-BY-4.0 |

## Abstract

Companion executive presentation deck to the April 2002 Aberdeen-to-Sun iSeries market report. Summarizes AS/400 demographics (450,000 installed base, $10.27B revenue, 23% of IBM HW), competitive assessment of iSeries strengths and weaknesses, IBM's 2002 game plan, Sun's $1.87B addressable market across four segments (new customers $924M, consolidation $400M, applications $452M, upgrades $92M), and the recommended partner-led Linux-lever strategy. Two file variants (ppt and pdf) contain the same content; merged here.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 8 |
| observations.csv | 18 |
| codes.csv | 29 |

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

Peter Kastner (2002). Sun's AS/400 Market Opportunity — Aberdeen Presentation to Sun Microsystems.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, competitive-profiling, executive-presentation
