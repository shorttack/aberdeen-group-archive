# The Data Warehouse: 2 Years Later... Lessons Learned

| Field | Value |
|-------|-------|
| Author | John D. Porter and John J. Rome, Arizona State University |
| Date | 1994-12-01 |
| Type | conference-paper |
| Domain | higher-education-data-warehousing |
| License | CC-BY-4.0 |

## Abstract

CAUSE 1994 Annual Conference paper (Orlando FL, Nov 29 - Dec 2 1994) by John D. Porter and John J. Rome of Arizona State University, retrospectively analyzing ASU's two-year-old integrated data warehouse project. The warehouse combined student, financial, and HR data — one of the first major client-server data warehouses in US higher education. Lessons-learned sections cover learning new technologies, understanding warehousing concepts, integrating data, designing the warehouse, marketing the idea, finding resources, 'officialness' of data, data administration impact, and data definition. Notable Kastner citation (Aberdeen Group): 'All companies will build [a data warehouse] in the next five years.' — an aggressive 1994 prediction about universal enterprise data-warehouse adoption.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 7 |
| technologies.csv | 2 |
| observations.csv | 8 |
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

John D. Porter and John J. Rome, Arizona State University (1994). The Data Warehouse: 2 Years Later... Lessons Learned.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

case-study, lessons-learned-retrospective
