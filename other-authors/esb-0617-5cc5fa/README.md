# Enterprise Service Bus: an SOA Middleware Foundation

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 2006-06 |
| Type | employer-record |
| Domain | ESB; SOA middleware; enterprise application integration; SOA adoption |
| License | CC-BY-4.0 |

## Abstract

38-page Aberdeen Group benchmark report sponsored by Fiorano and IBM. Part of 'Next Steps in SOA Series'. ESB as messaging middleware for SOA. Survey findings on ESB adoption patterns across company sizes. Three SOA camps identified: SOA Lite, Enterprise SOA, SOA ERP. 90% of respondents will exit 2006 with SOA experience. ESB adoption concentrated in enterprises >$500M revenue. BEA Systems top primary ESB vendor (57% BIC), IBM WebSphere second (37%), webMethods third. Creates context for EAI-to-ESB transition. Covers hardware server forecasts driven by ESB deployment. Aberdeen PACE framework applied.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
| technologies.csv | 12 |
| observations.csv | 36 |
| codes.csv | 34 |

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

Aberdeen Group (2006). Enterprise Service Bus: an SOA Middleware Foundation.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

survey; benchmark; PACE framework; qualitative interviews; 2006
