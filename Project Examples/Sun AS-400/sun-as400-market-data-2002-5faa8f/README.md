# Sun AS/400 RAMP Supporting Data: IBM Revenue, iSeries Pricing Benchmarks, Installed Base, and US Business Size Statistics

| Field | Value |
|-------|-------|
| Author | Peter Kastner |
| Date | 2002-04-20 |
| Type | benchmark |
| Domain | server-market-data |
| License | CC-BY-4.0 |

## Abstract

Consolidated analytical dataset backing the Sun AS/400 RAMP engagement. Includes: (a) IBM 2002 hardware financials — $33.4B revenue, $24.1B cost, $9.3B gross profit, 27.7% GM; platform revenue breakdown (zSeries $8.35B, iSeries $7.68B, pSeries $5.01B, xSeries $5.01B); iSeries model-to-Sun-equivalent mapping (250→Ultra 10, 270→220R, 820→V880, 830→4800, 840→6800); regional iSeries revenue breakdowns; enterprise app category CAGRs 2001-2005 (CRM 22%, EAS 12%, SCM 23%, B2B 26%); and Aberdeen's addressable-market decomposition ($1.87B total). (b) Detailed iSeries pricing benchmarks (181-row Appendix C) with TPM-C, SAP SD, and Notes benchmark estimates for each SKU. (c) World IT spending forecast 1999-2005 by region. (d) U.S. Business Statistics 1999 by firm size for IBM customer-size modeling.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 13 |
| observations.csv | 45 |
| codes.csv | 31 |

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

Peter Kastner (2002). Sun AS/400 RAMP Supporting Data: IBM Revenue, iSeries Pricing Benchmarks, Installed Base, and US Business Size Statistics.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-sizing, benchmarking, document-review
