# Storage & Storage Management: 1998 Practice Summary

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1998-05-01 |
| Type | other-research |
| Domain | enterprise-storage |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group's 1998 analysis of the enterprise storage market, arguing that storage must be treated as a system-level architectural decision — not a commodity — and introducing the concept of 'network storage' (any storage accessed over a network). The report covers SANs, NAS, Fibre Channel, RAID, tape technologies, and storage management software, forecasting that SANs would not become common until 1999 and that storage management software would be the critical differentiator. Supplier profiles cover 11 vendors including EMC, IBM, HP, VERITAS, Legato, and StorageTek.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 22 |
| technologies.csv | 13 |
| observations.csv | 22 |
| codes.csv | 25 |

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

Aberdeen Group (1998). Storage & Storage Management: 1998 Practice Summary.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis
