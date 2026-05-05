# Matching IT to Business Processes: How BPM is Complementing ERP and Custom Applications (Abridged)

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 2006-12 |
| Type | employer-record |
| Domain | BPM / SOA / ERP Integration |
| License | CC-BY-4.0 |

## Abstract

Abridged benchmark report on BPM complementing ERP and custom applications. Key finding: only 19% of companies say their applications afford desired flexibility. 49% resort to manual processes. 44% say ERP/supply chain solutions don't provide adequate functionality. Aberdeen forecasts 90% of companies had SOA strategies in place by end of 2006. 40% have current SOA projects; 42% have SOA solutions in place. Best in Class average SOA ROI of 73% on mean investment of $880K. Large organizations 50% more likely to invest in BPM than small/mid-size. 63% use spreadsheets for critical business process functions. More than two-thirds of supply-chain-intensive industries say ERP impedes visibility.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 9 |
| observations.csv | 55 |
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

Aberdeen Group (2006). Matching IT to Business Processes: How BPM is Complementing ERP and Custom Applications (Abridged).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Survey-based benchmark (N>125 enterprises); Aberdeen Competitive Framework; online survey November-December 2006 supplemented by telephone interviews
