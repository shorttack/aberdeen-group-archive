# Moore's Law: True But Irrelevant

| Field | Value |
|-------|-------|
| Author | David Haskin (InternetNews.com) |
| Date | 2003-05-16 |
| Type | news-article |
| Domain | enterprise-pc-strategy |
| License | CC-BY-4.0 |

## Abstract

InternetNews.com piece pitting Gartner's Mark Margevicius ('no software coming anytime soon that needs more desktop performance') against Aberdeen Group's Peter Kastner, who disagrees. Kastner argues Windows 98/NT machines are obsolescent, corporate buyers should move to Office 2003 for collaboration productivity, and that the multi-process, multi-threaded workload of a modern PC ('40 processes going on when I'm checking email') will make CPU performance matter again on the desktop. He cautions IT managers that lengthening the desktop upgrade cycle is 'penny wise, pound foolish.'

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
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

David Haskin (InternetNews.com) (2003). Moore's Law: True But Irrelevant.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, analyst-debate
