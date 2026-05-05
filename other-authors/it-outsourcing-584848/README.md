# Mid-Market Must Flex More Muscle in IT Outsourcing

| Field | Value |
|-------|-------|
| Author | Rick Saia |
| Date | 2006-09-05 |
| Type | employer-record |
| Domain | IT outsourcing; mid-market enterprises; service level management; governance |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Market Segment report analyzing IT outsourcing practices at mid-size enterprises versus Best in Class organizations. Key finding: 25% of mid-market respondents admitted their companies have not been successful with IT outsourcing; none of the Best in Class cited lack of success. Report analyzes four stages prone to planning errors: creation of quantitative business case, contract pricing negotiations, governance, and ongoing operational management. Best in Class outperform mid-market across all four stages. Three recommendations: (1) Get the RFP right — know requirements, costs, and desired advantages; (2) Don't be afraid to look outside for help — use independent consultants and legal assistance; (3) Improve relationship management — dedicate management time and hold one person accountable for the outsourcing relationship.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 2 |
| technologies.csv | 5 |
| observations.csv | 15 |
| codes.csv | 29 |

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

Rick Saia (2006). Mid-Market Must Flex More Muscle in IT Outsourcing.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Aberdeen Market Segment report based on survey data from The Business Value of IT Outsourcing Benchmark Report (July 2006)
