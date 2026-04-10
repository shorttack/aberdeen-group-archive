# Intel's Itanium: Ready and Desirable for Mainframe-Class Workloads

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2004-03 |
| Type | white-paper |
| Domain | Server Hardware / Mainframe Migration / Intel Itanium |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Executive White Paper examining readiness of Intel Itanium-based platforms to handle mainframe-class workloads vs. IBM zSeries mainframes. Based on user interviews with Xeon/Itanium adopters and a survey of ~100 mainframe users. Finds Itanium ready and often desirable for mainframe-class workloads including batch, OLTP, data warehousing, and ERP; 40% of mainframe users open to migration. Key advantages: price/performance, flexibility, programmer productivity, lower TCO. Key barriers: migration risk and technology roadmap risk.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 19 |
| technologies.csv | 30 |
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

Peter S. Kastner (2004). Intel's Itanium: Ready and Desirable for Mainframe-Class Workloads.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

User interviews; mainframe user survey (n~100); secondary market data; vendor briefings
