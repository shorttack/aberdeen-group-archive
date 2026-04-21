# The traditional ESB gets weaved into an SOA fabric

| Field | Value |
|-------|-------|
| Author | Rich Seeley, SearchWebServices / TechTarget |
| Date | 2006-12-21 |
| Type | news-article |
| Domain | soa-esb-middleware |
| License | CC-BY-4.0 |

## Abstract

SearchWebServices / TechTarget article (Dec 21 2006, Rich Seeley) on the evolution of the enterprise service bus (ESB) category, triggered by the launch of webMethods Fabric 7.0. Peter S. Kastner, VP Enterprise Integration at Aberdeen Group, is a central voice. His key findings: (1) EAI is not dead — 'We found almost nobody who is willing to abandon their investments in EAI just to buy an ESB'; (2) 'My hypothesis going into the year was that the EAI companies would take it on the chin. The reality is the vast majority of their customers are fairly easily connecting SOA via adapters to their EAI fabric or infrastructure' — Kastner publicly updates his prior prediction; (3) BPM-ESB convergence is widespread: 'We're seeing at this point that roughly 50 percent of the Global 5000 are actively engaged in business process management development.' AMR Research's Bill Swanton and webMethods CTO Marc Breissinger round out the SOA-BPM-ESB convergence narrative. Burton Group's 'middleware fabric' terminology is cited.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 7 |
| observations.csv | 10 |
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

Rich Seeley, SearchWebServices / TechTarget (2006). The traditional ESB gets weaved into an SOA fabric.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

product-analysis, analyst-commentary, industry-trend-analysis
