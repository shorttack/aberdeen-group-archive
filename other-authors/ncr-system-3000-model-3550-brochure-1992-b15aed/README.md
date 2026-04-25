# NCR System 3000 / Model 3550 Open Cooperative Computing Brochure (1992)

| Field | Value |
|-------|-------|
| Author | NCR Corporation (vendor product brochure) |
| Date | 1992 |
| Type | vendor-product-brochure |
| Domain | open-cooperative-computing/symmetric-multiprocessing |
| License | CC-BY-4.0 |

## Abstract

NCR Corporation 1992 product brochure for the NCR System 3000 family, with the NCR Model 3550 highlighted as 'the most powerful tightly-coupled system in the System 3000 family'. The brochure positions System 3000 as 'the broadest range of open, scalable systems in the computer industry today' — from uniprocessor to multiprocessor, tightly-coupled to loosely-coupled architectures — and pitches the 3550 as delivering 'several times the performance traditionally found in mainframe computers, for less cost'. Engineering specs: dual 64-bit system bus running at 25 MHz with 200 MB/sec aggregate bandwidth; up to 8 Intel486 50 MHz CPUs (claimed 320 MIPS); Micro Channel Enhanced I/O; RAID storage; hot-pluggable disks; dual-port memory; fault-resilient design. UNIX SVR4 operating system. This is the platform companion to the Batch 23 NCR 3000 cabinet engineering diagram (study fa564f) and is contemporaneous with Aberdeen's Open OLTP for Enterprise Managers white paper (study 3fc536) and the 1992-09 NCR Norge AS Open OLTP/RDBMS mini-seminar (study 7f5414).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 7 |
| observations.csv | 6 |
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

NCR Corporation (vendor product brochure) (1992). NCR System 3000 / Model 3550 Open Cooperative Computing Brochure (1992).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

vendor-product-collateral
