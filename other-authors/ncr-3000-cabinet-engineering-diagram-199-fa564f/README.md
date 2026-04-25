# NCR 3000 Server Cabinet Engineering Diagram (1992): Intel486 50MHz Multiprocessor Boards, Micro Channel, Hot-Pluggable Storage

| Field | Value |
|-------|-------|
| Author | NCR Corporation (engineering documentation) |
| Date | 1992 |
| Type | engineering-diagram |
| Domain | server-hardware-architecture |
| License | CC-BY-4.0 |

## Abstract

NCR Corporation engineering diagram from 1992 documenting the NCR 3000 server cabinet design: processor boards each carrying two 50MHz Intel486 microprocessors, memory boards, eight Primary Micro Channel slots (with eight Optional slots on the Optional Side), 6.75-inch hot-pluggable fans, hot-pluggable internal SCSI fixed disks (up to 14 full-height or 28 half-height), 4 full-height or 8 half-height removable devices on each side, standard 525MB QIC tape and 1.44MB flex disk, optional 600MB CD-ROM and 1.3GB Digital Audio Tape, power back-up system batteries, security lock, and a local peripheral board for VGA monitor / mouse / keyboard / diagnostic monitor / parallel printer. The artifact provides concrete platform context for the Aberdeen Open OLTP white-paper claims about low-cost commercial multiprocessor platforms, X/Open compliance, and downsizing-from-mainframe value propositions of 1991-1992. Companion to the Norway 1992 OLTP seminar deck which references the NCR Model 3550 (UNIX V.4 multiprocessor up to eight i486-50MHz, ~320 MIPS, supporting 1,000+ workstations).

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

NCR Corporation (engineering documentation) (1992). NCR 3000 Server Cabinet Engineering Diagram (1992): Intel486 50MHz Multiprocessor Boards, Micro Channel, Hot-Pluggable Storage.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

vendor-engineering-documentation
