# For Mid-Size Enterprises SOA's Benefits Begin with IT

| Field | Value |
|-------|-------|
| Author | Rick Saia, Aberdeen Group |
| Date | 2006-01-10 |
| Type | employer-record |
| Domain | SOA Adoption/Mid-Size Enterprise Strategy |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Market Segment report analyzing mid-size enterprise (vs large enterprise) differences in SOA adoption. 70 mid-size organizations responded to December 2005 survey. Mid-size enterprises more IT-focused in SOA drivers (managing integration costs, app re-use via web services) while large enterprises more focused on business-IT alignment. Mid-size firms less IT-skilled (vs large) but have advantages: less complexity, easier access to best practices, less change management resistance. Only 16% of companies overall have >24 months SOA experience (17% mid-size). 15% have managed/completed at least 3 SOA projects (13% mid-size).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 7 |
| observations.csv | 35 |
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

Rick Saia, Aberdeen Group (2006). For Mid-Size Enterprises SOA's Benefits Begin with IT.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Market Segment analysis based on Aberdeen SOA in IT benchmark survey (N=70 mid-size respondents from Dec 2005 survey; companion to soa-in-it-e5b373)
