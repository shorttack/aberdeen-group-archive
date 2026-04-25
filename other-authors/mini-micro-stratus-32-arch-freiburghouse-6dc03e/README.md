# Mini-Micro Systems: Robert Freiburghouse on the Stratus/32 Architecture — VOS, StrataLINK, and 'Continuous Processing' (1982)

| Field | Value |
|-------|-------|
| Author | Robert Freiburghouse (Stratus Computer) |
| Date | 1982 |
| Type | trade-press-architectural-feature |
| Domain | fault-tolerant-computing/computer-architecture |
| License | CC-BY-4.0 |

## Abstract

1982 Mini-Micro Systems bylined feature article by Robert Freiburghouse (Stratus Computer's principal software architect, formerly of Multics PL/I compiler design) detailing the Stratus/32 architecture and 'continuous processing' design philosophy. Key architecture facts documented: up to 32 processing modules connected via StrataLINK high-speed coaxial link (32 Mbits/sec; 2.8 MB/sec dual / 1.4 MB/sec single); each processing module configurable as fully redundant, partially redundant, or non-redundant; each module contains two Motorola 68000 CPUs sharing memory plus one Z80 per peripheral controller; high-speed bus 125-nsec cycle, two parallel data/control paths 32-bit wide, 32 MB/sec potential (16 MB/sec actual at processor/memory boards) — vs VAX 11/780 at 13 MB/sec; CPU board self-checking with paired logic, full-redundant module survives any component failure without performance/data loss; failed boards replaceable by non-technical personnel without tools while system running; VOS distributed virtual OS makes all modules appear as single virtual computer; per-process address space 16 MB (4 MB VOS + 12 MB user). Typical Stratus/32 priced at $172,000 (4 MB memory, dual i43MB disks, 600 lpm printer, mag tape, COBOL + VOS licenses). This is the canonical first-party architectural reference for the Stratus/32 platform throughout the 1982 Stratus quote corpus (studies 1-3 of Batch 25).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 8 |
| observations.csv | 8 |
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

Robert Freiburghouse (Stratus Computer) (1982). Mini-Micro Systems: Robert Freiburghouse on the Stratus/32 Architecture — VOS, StrataLINK, and 'Continuous Processing' (1982).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

vendor-architect-byline-trade-press
