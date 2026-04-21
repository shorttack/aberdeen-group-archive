# Using TeamQuest Performance Software to Align IT with Business Priorities

| Field | Value |
|-------|-------|
| Author | TeamQuest Corporation |
| Date | 2004-01-01 |
| Type | vendor-whitepaper |
| Domain | IT-performance-management |
| License | CC-BY-4.0 |

## Abstract

TeamQuest Corporation whitepaper (2004, 7 pages) positioning TeamQuest performance-management software (TeamQuest Analyzer, TeamQuest Reporter, TeamQuest Model, TeamQuest View) as a vehicle for aligning IT operations with business priorities. The paper walks through capacity planning methods (benchmarking, trending, modeling — both simulation and analytic), workload characterization, service-level management, and server-consolidation use cases. Peter Kastner, chief research officer at Aberdeen Group Inc., is quoted in support of the server-consolidation thesis: 'For a large corporation, it's fairly easy to get to millions of dollars in savings through recentralization of servers and expensive IT support.' Document targets enterprise IT operations managers pursuing consolidation and capacity planning; published date 2004, copyright © 2004 TeamQuest Corporation; pre-dates the 2018 TeamQuest acquisition by Helpsystems (now Fortra).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 4 |
| observations.csv | 5 |
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

TeamQuest Corporation (2004). Using TeamQuest Performance Software to Align IT with Business Priorities.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

vendor-whitepaper, analyst-quote
