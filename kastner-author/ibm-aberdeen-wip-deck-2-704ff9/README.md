# IBM-Aberdeen: Storage Change Brings Opportunities (Sales Team Workshop)

| Field | Value |
|-------|-------|
| Author | Aberdeen Group (Peter S. Kastner et al.) |
| Date | 2004-01-01 |
| Type | market-study |
| Domain | IBM-storage-ILM-aberdeen-sales |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group sales team workshop deck prepared for IBM on Storage Pools and Information Lifecycle Management (ILM). Introduces Aberdeen's DSET C-level framework (Drivers, Strategies, Enablers, Technology) and demonstrates how research agenda sponsorship, value assessment tools, and installed base assessments accelerate IBM storage sales through Aberdeen's ~150,000 registered user research community. Flag: Aberdeen-Confidential / internal IBM enablement.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 6 |
| observations.csv | 12 |
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

Aberdeen Group (Peter S. Kastner et al.) (2004). IBM-Aberdeen: Storage Change Brings Opportunities (Sales Team Workshop).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, framework-development, sales-enablement
