# Videoconferencing Boost — Intel TeamStation

| Field | Value |
|-------|-------|
| Author | Mary E. Thyfault |
| Date | 1998-05-04 |
| Type | news-article |
| Domain | PC-based-videoconferencing-room-systems |
| License | CC-BY-4.0 |

## Abstract

InformationWeek reports Intel's TeamStation room videoconferencing system — based on standard PC technology and priced at $9,999 ($11,999 with monitor) versus the $20,000 typical for proprietary room systems. Caterpillar Financial deployed in 12+ cities. Aberdeen Group analyst Peter Kastner explains how PC-based filtering produces 'less jerky video' over low-speed lines and predicts the technology will be 'fundamental to communications in the 21st century.'

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 6 |
| observations.csv | 7 |
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

Mary E. Thyfault (1998). Videoconferencing Boost — Intel TeamStation.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

news-reporting, expert-quote-aggregation, vendor-spokesperson, customer-case
