# Survey: Composite Applications Used to Solve Integration Problems

| Field | Value |
|-------|-------|
| Author | James Powell, Enterprise Systems Journal (ESJ.com) |
| Date | 2007-01-16 |
| Type | news-article |
| Domain | enterprise-integration-SOA |
| License | CC-BY-4.0 |

## Abstract

Enterprise Systems Journal (esj.com) news article (Jan 16 2007) by James Powell summarizing an Aberdeen Group research report on composite applications as a pragmatic stepping-stone to full SOA. Aberdeen reports application integration consumes up to 40 percent of the typical IT budget; most organizations have not dived deep enough into SOA to have one fully implemented, so they are using composite applications — logic and data collected from multiple IT sources, coupled with web services standards — to keep up with rapidly-changing business needs. Peter S. Kastner, vice president of Aberdeen's Enterprise Technology research practice and primary author of the report, is quoted: 'Our research found that companies are targeting Web-based applications first — specifically portals and browser-based applications — when they're looking to build composite applications.' Kastner also stresses focusing on processes that differentiate the company: customer satisfaction, service delivery, low-cost supply, fast delivery.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 4 |
| observations.csv | 6 |
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

James Powell, Enterprise Systems Journal (ESJ.com) (2007). Survey: Composite Applications Used to Solve Integration Problems.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

analyst-report-summary
