# Enterprise Information Integration: The New Way to Leverage E-information (Second Edition)

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 2003-07 |
| Type | employer-record |
| Domain | EII; enterprise information integration; data integration; information aggregation; ETL; EAI |
| License | CC-BY-4.0 |

## Abstract

74-page Aberdeen Group second edition market report on Enterprise Information Integration (EII), the predecessor to SOA/ESB thinking. Author: Wayne Kernochan, Managing VP Platform Infrastructure. EII market sized at under $200 million, projected 80% growth in 2003. IBM leads with $60M EII revenue estimate; BEA $25M; Business Objects $15M. Report introduces Aberdeen EII Technology Segmentation Model covering EAI, database, XML messaging, and EII solution categories. Taxonomy of information aggregation tools: data migration, replication/ETL, data warehouses, operational data stores, EII, federated databases. MetaMatrix featured as case study supplier. SAP OEM deal with MetaMatrix for NetWeaver noted. Related markets: EAI $2.2B→$3.0B, content management $1.2B→$2.0B, portal $1.5B→$2.8B (2002-2004).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 27 |
| technologies.csv | 15 |
| observations.csv | 45 |
| codes.csv | 33 |

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

Aberdeen Group (2003). Enterprise Information Integration: The New Way to Leverage E-information (Second Edition).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-analysis; technology-segmentation; vendor-assessment; qualitative-research
