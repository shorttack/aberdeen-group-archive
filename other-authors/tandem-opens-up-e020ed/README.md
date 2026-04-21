# Tandem Opens Up

| Field | Value |
|-------|-------|
| Author | Barbara DePompa, InformationWeek #563 |
| Date | 1996-01-22 |
| Type | news-article |
| Domain | fault-tolerant-computing |
| License | CC-BY-4.0 |

## Abstract

InformationWeek issue #563 news article (Jan 22 1996) by Barbara DePompa on Tandem Computers Inc.'s strategic pivot under new CEO Roel Pieper. Tandem — the pioneer of fault-tolerant NonStop systems — had just named the 39-year-old Pieper president and CEO on Jan 8 1996, replacing founder Jim Treybig, who stepped down after a 72% quarterly-earnings drop amid product delays. Pieper, previously head of Tandem's UB Networks subsidiary since 1993 (and earlier at Unix System Labs and Software AG), aims to shift Tandem toward partnerships and component software that let Tandem's advanced software run on other vendors' hardware. The strategy targets Unix and Windows NT environments. Peter Kastner, analyst with Aberdeen Group Boston, endorses the pick: Pieper 'knows open systems and production computing requirements' thanks to his Unix Systems Labs and Software AG background. Tandem emphasizes NonStop and ServerNet technology partnerships going forward.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 4 |
| observations.csv | 6 |
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

Barbara DePompa, InformationWeek #563 (1996). Tandem Opens Up.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

vendor-commentary, analyst-commentary
