# Savant targets feds with Oracle database tool

| Field | Value |
|-------|-------|
| Author | John Moore, Federal Computer Week (FCW) |
| Date | 1997-06-08 |
| Type | news-article |
| Domain | database-administration-tools |
| License | CC-BY-4.0 |

## Abstract

Federal Computer Week article (Jun 8 1997) on Savant Corp. (Bethesda MD) pushing its Q Diagnostic Center product into the US federal government Oracle-database market. Customers already include the Justice Department and the Pension Benefit Guaranty Corp.; Savant plans GSA-schedule sales. Savant strategist Alec Glorieux projects federal will become 10% of company sales by year-end 1997. The product — inspired by founder William Wynn's DBA role on Army Corps of Engineers Automation Plan — provides a graphical overview of Oracle 7 database health, translating operational statistics into animated pictorial displays (e.g., a funnel showing average transaction wait time), and uses comparative-analysis rather than threshold-based methodology. Peter Kastner, group VP at The Aberdeen Group, observes: 'The graphical interface makes sense at a time when database vendors are under a lot of pressure to make their database tools easier to use.' Pricing starts at $3,900/database; supports Oracle 7.2/7.3, Windows 3.1/95/NT, Q Viewer on Win95/NT. Planned expansion into network and OS monitoring by fall 1997.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 5 |
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

John Moore, Federal Computer Week (FCW) (1997). Savant targets feds with Oracle database tool.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, analyst-commentary
