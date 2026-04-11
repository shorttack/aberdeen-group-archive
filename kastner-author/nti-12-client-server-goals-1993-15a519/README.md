# Realistic Goals for Client-Server Computing

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner, John Logan, Thomas Willmott |
| Date | 1993-07-01 |
| Type | market-study |
| Domain | client-server-computing |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group defines and evaluates the client-server computing paradigm across five critical planning areas: client hardware options, scalable server architectures, legacy system roles, systems software transitions, and network infrastructure. The study covers current client-server implementations and traces the evolution to advanced designs including distributed relational and object-oriented databases, cascading server-to-server transactions, and intelligent high-speed networks. Aberdeen concludes that client-server drives the next-generation computing vision but warns that the installed base technology does not yet fully support the vision and that significant non-technical barriers—management vision, process reengineering, and training—must be overcome.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 33 |
| technologies.csv | 26 |
| observations.csv | 30 |
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

Peter S. Kastner, John Logan, Thomas Willmott (1993). Realistic Goals for Client-Server Computing.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, technology-assessment, vendor-profiling
