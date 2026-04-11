# MGMT MEMO Volume 7, Number 5 — Digital's State of the Company Meeting

| Field | Value |
|-------|-------|
| Author | Digital Equipment Corporation (Richard Seltzer, editor) |
| Date | 1988-07-01 |
| Type | employer-record |
| Domain | enterprise-computing-strategy |
| License | CC-BY-4.0 |

## Abstract

Summaries of nine executive speeches delivered at Digital Equipment Corporation's May 5, 1988 State of the Company Meeting in Merrimack, NH, attended by over 600 senior managers. The theme was 'One Company, One Strategy, One Message — Leading the Way to Enterprise-Wide Computing,' with major sections on desktop/workstation strategy, transaction processing, DECwindows, database systems, and VAXcluster high availability. This document captures DEC at its revenue peak (~$11B, 120K+ employees) articulating a bold enterprise strategy that proved partially prescient and partially fatal.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 23 |
| technologies.csv | 28 |
| observations.csv | 48 |
| codes.csv | 32 |

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

Digital Equipment Corporation (Richard Seltzer, editor) (1988). MGMT MEMO Volume 7, Number 5 — Digital's State of the Company Meeting.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

oral-history, document-review
