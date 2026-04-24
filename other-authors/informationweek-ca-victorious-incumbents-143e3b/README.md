# Victorious Incumbents Vow Change For CA

| Field | Value |
|-------|-------|
| Author | David Joachim |
| Date | 2001-09-01 |
| Type | news-article |
| Domain | CA-proxy-fight-Wyly-aftermath |
| License | CC-BY-4.0 |

## Abstract

InformationWeek reports the aftermath of the Sam Wyly proxy fight against Computer Associates' incumbent board (Charles Wang/Sanjay Kumar). Aberdeen Group analyst Peter Kastner argues CA's customer-facing changes were driven by a 'standing pejorative that CA screws its customers' rather than by Wyly pressure — CA was already 'tweaking sales and support organization' continuously. Customer Andrew Winer of Myers Industries voiced relief that splitting the company was averted. Date inferred from Wyly post-fight context [REVIEW].

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 2 |
| observations.csv | 5 |
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

David Joachim (2001). Victorious Incumbents Vow Change For CA.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

news-reporting, expert-quote-aggregation
