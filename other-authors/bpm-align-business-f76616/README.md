# Aligning IT to Business Processes: How BPM is Complementing ERP and Custom Applications

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 2007-05 |
| Type | employer-record |
| Domain | BPM; SOA; ERP integration; application lifecycle management; supply chain |
| License | CC-BY-4.0 |

## Abstract

29-page Aberdeen Group benchmark report on BPM adoption, ROI, and ERP integration. Based on survey of 125+ enterprises. 51% of respondents say ERP systems don't provide adequate functionality. Only 15% believe applications afford desired flexibility. Over 50% turning to BPM in 2007. BPM investment leads middleware: 57% investing in BPM tools vs 45% ESB/SOA vs 25% MDM. SOA technology and web services cited by 67% as integration glue between BPM and ERP. Large companies 50% more likely to invest in BPM vs SMEs. Underwriters: Appian, CTSpace, Ramco.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 6 |
| observations.csv | 27 |
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

Aberdeen Group (2007). Aligning IT to Business Processes: How BPM is Complementing ERP and Custom Applications.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

survey; benchmark; n=125+ enterprises; qualitative interviews; Dec 2006
