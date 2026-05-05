# A Fault-Tolerant Transaction Processing Environment (Stratus/32, IEEE Database Engineering, June 1983)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner — Stratus Computer, Inc. |
| Date | 1983-06-01 |
| Type | technical-article |
| Domain | fault-tolerant-computing-OLTP |
| License | CC-BY-4.0 |

## Abstract

Peer-reviewed article by Peter S. Kastner of Stratus Computer, Inc., published in IEEE Computer Society Technical Committee on Database Engineering Bulletin (June 1983, Vol.6 No.2, pp.20-28). Describes the Stratus/32 multiprocessor fault-tolerant system architecture for commercial on-line transaction processing (OLTP). Each processing module contains paired self-checking logic (Motorola 68000 CPUs, memory, disk controllers), with up to 32 modules connected via the StrataLINK high-speed coaxial link. Stratus's Virtual Operating System (VOS) presents the federation as a single virtual computer, with transparent file/process distribution. Key software components covered: VOS file system, StrataNET networking, Transaction Processing Facility (TPF) with multi-tasking servers and START/COMMIT/ABORT primitives, two-phase commit protocol with 'Phase I Commit' flag, mirrored disks for write durability, and the Forms Management Facility. The article documents Stratus's continuous-processing thesis: hardware-detected failures with redundant pair-and-spare partners eliminate the need for checkpoint/restart programming at user or system level. This is Kastner's primary published technical exposition of Stratus architecture during his Stratus marketing tenure.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 7 |
| technologies.csv | 14 |
| observations.csv | 28 |
| codes.csv | 23 |

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

Peter S. Kastner — Stratus Computer, Inc. (1983). A Fault-Tolerant Transaction Processing Environment (Stratus/32, IEEE Database Engineering, June 1983).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis,technical-architecture-description,document-review
