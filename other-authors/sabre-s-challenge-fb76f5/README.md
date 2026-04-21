# Sabre's Challenge

| Field | Value |
|-------|-------|
| Author | John Foley (InformationWeek) |
| Date | 1997-08-18 |
| Type | news-article |
| Domain | airline-reservations-client-server-migration |
| License | CC-BY-4.0 |

## Abstract

InformationWeek cover feature (August 18, 1997) on Sabre Group Holdings Inc. — spun off from AMR Corporation in late 1996 — and its challenge of expanding software offerings to attract new customers while modernizing a 25-year-old IBM TPF-based mainframe reservations system. System holds 4 TB of data on 400 airlines, 50 car-rental companies, and 35,000 hotels; at peak handles 5,200 messages/second; processed 350M reservations in 1996 at <2 second transaction time. Peter Kastner, Aberdeen Group analyst, explains the limitation: TPF is adept at handling reservations but 'adding new applications is problematic.' Sabre's answer is next-generation Sabre — a client-server surround strategy using Unix/Silicon Graphics servers and Oracle databases to extend the mainframe core. Travelocity (Sabre Interactive) is the flagship case. Thomas Cook (president, Sabre Technology Solutions) notes Sabre's goal of 15-25%/year non-airline revenue growth. Includes IBM 10-year Hong Kong airline deal (June 1997) among recent wins.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 4 |
| observations.csv | 10 |
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

John Foley (InformationWeek) (1997). Sabre's Challenge.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, executive-interview
