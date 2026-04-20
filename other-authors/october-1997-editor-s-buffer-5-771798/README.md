# Editor's Buffer (October 1997)

| Field | Value |
|-------|-------|
| Author | Editor, Database Programming & Design (Miller Freeman) |
| Date | 1997-10-01 |
| Type | editorial |
| Domain | database-market |
| License | CC-BY-4.0 |

## Abstract

October 1997 editor's column in Database Programming & Design previewing the 1998 Object/Relational Summit. Notes 'The Aberdeen Group's Peter Kastner described well the tough competition facing database vendors not named IBM, Oracle, or Microsoft,' and discusses ODBMS adoption (Thomas Atwood) and Java's JDBC-first orientation.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
| technologies.csv | 4 |
| observations.csv | 6 |
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

Editor, Database Programming & Design (Miller Freeman) (1997). Editor's Buffer (October 1997).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, editorial-commentary
