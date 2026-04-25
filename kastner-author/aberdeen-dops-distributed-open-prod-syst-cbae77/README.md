# Aberdeen Group — Distributed Open Production Systems: The Next Generation Begins (1993)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner — Vice-President, Aberdeen Group, Inc. |
| Date | 1993-06-01 |
| Type | conference-presentation |
| Domain | distributed-systems-architecture |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group conference presentation deck delivered by Peter S. Kastner (Vice-President, Aberdeen Group) circa 1993 titled 'Distributed Open Production Systems: The Next Generation Begins.' Boston office at 92 State Street, (617) 723-7890. Defines Downsizing as migrating computer-based functions from central mainframe to dispersed computing systems and operationally as moving MIS function down the organization. Presents the Spoke-Node-Ring Planning Model based on three buyer demands: Distributed Systems, Open Systems, Production-Quality Applications. Centerpiece is a complex multi-vendor distributed-application diagram showing: a Stratus Encina/DCE/Sybase/VOS Order Processing node coordinating with IBM S/390 CICS/DCE/DB2/DRDA/MVS/ESA Credit Admin; RS/6000 Encina/DCE/Informix Warehouse Distribution; HP 9000 Encina/DCE/Allbase/HP-UX Resource Planning (MRP); Pyramid Ui-AHas Ingres/Unix 5.4 MP Order Processing — all linked via Encina/DCE distributed transactions. Defines Intelligent Applications as those that 'use more system services and hide the complexities' (comm network, data location, how/where things get done). Six Technology Combinations: standalone Unix; single-source database; production distributed databases; communications to open & proprietary; mainframes treating world as peers; distributed data integrity. Future enablers: SQL Access Group's database interoperability, OSF's Distributed Computing Environment (DCE), IBM's endorsement of DCE, new products for distributed production systems.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 13 |
| technologies.csv | 10 |
| observations.csv | 12 |
| codes.csv | 40 |

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

Peter S. Kastner — Vice-President, Aberdeen Group, Inc. (1993). Aberdeen Group — Distributed Open Production Systems: The Next Generation Begins (1993).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Aberdeen-Group-presentation-deck
