# IBM's AS/400 Versus Microsoft's NT Server: The Challenge That Is Not

**Aberdeen Group Product Viewpoint — January 15, 1996**

## Study Metadata

| Field | Value |
|-------|-------|
| Study ID | aberdeen-1996-ibm-as400-vs-microsoft-nt-server |
| Author | Aberdeen Group |
| Date | 1996-01-15 |
| Type | product-viewpoint |
| Domain | midrange-computing-platform-competition |
| License | CC-BY-4.0 |
| Importance | high |
| Relevance | medium |
| Prescience | high |

## Abstract

Aberdeen Group analyzes Microsoft's challenge to IBM's AS/400 installed base, arguing that the AS/400 with over 350,000 installations will retain its dominance in midrange commercial computing against Microsoft's NT Server (BackOffice). Aberdeen presents four economic and technical reasons why the challenge will fail: higher total cost for NT due to fat-client PCs, lack of match with AS/400 customer culture, absence of proven migration economics, and AS/400 Advanced Series' superior 64-bit RISC capabilities — predicting the debate will be viewed as 'the challenge that was not' by 1997.

## Data Tables

| Table | Rows | Description |
|-------|------|-------------|
| studies.csv | 1 | Study-level metadata with assessment ratings |
| entities.csv | 9 | Organizations mentioned in the study |
| technologies.csv | 10 | Technologies evaluated |
| observations.csv | 31 | Structured analytical observations |
| codes.csv | 24 | Controlled vocabulary definitions |

## Quick Load (Python)

```python
import pandas as pd
obs = pd.read_csv('data/observations.csv')
print(obs[obs['observation_type']=='viability-prediction'][['metric_name','metric_value']])
```

## Validation

```bash
frictionless validate datapackage.json
```

## Citation

Aberdeen Group. (1996). *IBM's AS/400 Versus Microsoft's NT Server: The Challenge That Is Not*
(Volume 9, Number 3). Aberdeen Group, Boston MA.
Archived: https://web.archive.org/web/19970112010618/http://www.aberdeen.com:80/secure/viewpnts/v9n3/v9n3.htm
DOI: [pending Zenodo deposit]

## Methodology

Industry analysis, competitive profiling, TPC-C benchmarking, and field research.
Uses quantitative TCO modeling (5-year lifecycle costs, per-seat hardware and staffing costs)
and TPC-C V3 published results to compare AS/400 vs NT Server economics.
