# Application Lifecycle Management: Used by the Best of the Best in Class

| Field | Value |
|-------|-------|
| Author | Rick Saia; Peter S. Kastner |
| Date | 2007-03-08 |
| Type | employer-record |
| Domain | SOA governance; application lifecycle management; SOA management; cost reduction |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Perspective finding that IT organizations actively engaged in application lifecycle management (ALM) for SOA outperform even Best in Class organizations on cost reduction. Key quantitative findings: ALM-focused organizations (12% of survey) decreased SOA development costs over last 12 months at 68% rate vs. 46% for Best in Class and 25% for all respondents. Investment in ALM: $2.68M average with $3.45M payback (+29% ROI) vs. all respondents: $1.37M investment with $1.18M payback (-14% ROI). 48% of ALM companies have annual revenue >$1B. 57% have had SOA services deployed >1 year. 29% have >100 SOA services deployed vs. 11% overall. Top challenge: establishment of operational security, governance, and management (45%). Top response: revised application lifecycle processes and responsibilities (45%).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 8 |
| observations.csv | 31 |
| codes.csv | 28 |

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

Rick Saia; Peter S. Kastner (2007). Application Lifecycle Management: Used by the Best of the Best in Class.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Aberdeen Perspective based on survey data from SOA Management and Governance Benchmark Report (February 2007). ~1,000 company survey from 2006.
