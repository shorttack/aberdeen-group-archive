# Tech Watching Is Fast Becoming an Industry to Watch (Wall Street Journal, March 19, 1998)

| Field | Value |
|-------|-------|
| Author | William M. Bulkeley (The Wall Street Journal) |
| Date | 1998-03-19 |
| Type | news-article |
| Domain | it-industry-analyst-market-sizing |
| License | CC-BY-4.0 |

## Abstract

William M. Bulkeley writes in the Wall Street Journal (March 19, 1998, page B7) that U.S. computer-industry research firms' revenue will rise ~28% in 1998 to $3 billion (Gartner Group forecast). Profiles the major firms in a 'Who's Who' table: Aberdeen (35 analysts, marketing consulting/training, buyer=computer makers), Forrester (75, trend-spotting), Gartner Group (550, the giant), Giga Group (75), International Data (135), Intelliquest Info (market research), Meta Group (111), Yankee Group (100, telecom). Quotes Marsha Haugen (HP market research manager, $4M/year spend), Rick O'Coin (Aetna team leader), Robert Paquin (L.L. Bean VP information services, Meta client), John W. Harmon (GAO CIO, $100K/year Gartner), Deon Babiuk (IPL Energy Calgary, cut $60K Gartner spend), Leonard Tenner (Hewitt Associates CIO), Sherri Wolf (Adams Harkness Hill analyst: '80% recurring revenue, 15-20% pretax operating margins'), and George Colony (Forrester president: 'McKinsey-like consultants are selling time — they're like dentists'). 1997 revenue figures: Gartner $511.2M (+30%), Meta $51.2M (+38%), Forrester $40.4M (+62%).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 28 |
| technologies.csv | 1 |
| observations.csv | 19 |
| codes.csv | 30 |

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

William M. Bulkeley (The Wall Street Journal) (1998). Tech Watching Is Fast Becoming an Industry to Watch (Wall Street Journal, March 19, 1998).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

news-reporting, market-sizing, executive-interviews
