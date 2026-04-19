# Leaving Well Enough Alone: Enterprise Application Integration's Impact on ROI

| Field | Value |
|-------|-------|
| Author | Aberdeen Group (Katherine Jones, Tom Dwyer, Peter S. Kastner) |
| Date | 2001-07-01 |
| Type | white-paper |
| Domain | enterprise-software/integration-roi |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Executive White Paper arguing that integrated enterprise application suites deliver superior ROI vs. best-of-breed point solutions. Built on interviews with a dozen IT professionals (Credit Suisse First Boston, Beneficial Life, Carreckers, Indian Motorcycle, State of Michigan, etc.). Documents 40-70% of IT budget on integration, Nike's $400M SAP+Siebel+i2 failed integration, 18-24 mo integrated-suite vs 3-6 mo single point vs 16-20 mo four-point integration timelines, and 3-10x license fees for full integration. This is the VENDOR-NEUTRAL version; study 7 is the Oracle-sponsored rewrite of the same research.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 27 |
| technologies.csv | 8 |
| observations.csv | 22 |
| codes.csv | 24 |

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

Aberdeen Group (Katherine Jones, Tom Dwyer, Peter S. Kastner) (2001). Leaving Well Enough Alone: Enterprise Application Integration's Impact on ROI.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, customer-interview, document-review
