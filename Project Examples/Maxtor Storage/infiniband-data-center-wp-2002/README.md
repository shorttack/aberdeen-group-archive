# InfiniBand Architecture: Planning the Next-Generation Data Center

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-05-01 |
| Type | white-paper |
| Domain | data-center-interconnect |
| License | CC-BY-4.0 |

## Abstract

An Aberdeen Group executive white paper published in May 2002 arguing that InfiniBand Architecture (IBA) would replace PCI-based I/O as the dominant data center interconnect within two to three years. The paper evaluates IBA's switched-fabric design against existing SCSI, Fibre Channel, and Ethernet protocols, and predicts adoption beginning in large enterprise and HPC data centers. It identifies blade server and server clustering as the primary early use cases and calls on IT planners to begin phased IBA deployments in 2003.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 20 |
| technologies.csv | 14 |
| observations.csv | 32 |
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

industry-analysis,technology-assessment,expert-opinion
