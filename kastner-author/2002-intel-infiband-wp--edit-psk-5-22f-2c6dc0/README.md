# InfiniBand Architecture: Planning the Next-Generation Data Center

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-05 |
| Type | white-paper |
| Domain | Enterprise IT Hardware / Networking / Data Center Architecture |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Executive White Paper providing a comprehensive overview of the emerging InfiniBand Architecture (IBA) for data center IT planners. Covers IBA components (HCA, TCA, switches/routers), comparison to PCI/PCI-X, IP over InfiniBand, storage over InfiniBand (SCSI, SAN, NAS), server scaling via clustering and blade servers, deployment transition planning, and early-adopter field research indicating 50% TCO reduction for database clusters. Recommends beginning evaluation in 2002 and phased deployment in 2003.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 20 |
| technologies.csv | 16 |
| observations.csv | 22 |
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

Peter S. Kastner (2002). InfiniBand Architecture: Planning the Next-Generation Data Center.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

expert-analysis; early-adopter field research
