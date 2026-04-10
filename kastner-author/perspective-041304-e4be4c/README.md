# Intel's Itanium: Ready and Desirable for Mainframe-Class Workloads

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | April 13, 2004 |
| Type | topic-analysis |
| Domain | Enterprise Computing / Server Platforms / Mainframe Migration |
| License | CC-BY-4.0 |

## Abstract

This Aberdeen Perspective piece evaluates whether Intel Itanium 2-based platforms can handle mainframe-class workloads and compares them to IBM zSeries mainframes. Drawing on Q1-2004 interviews and a survey of 98 mainframe users, the paper concludes that Itanium platforms are not only capable but in many cases desirable: users report superior performance/scalability, lower TCO, greater flexibility, and comparable robustness. Key findings include that ~40% of mainframe users are open to shifting to Itanium-based platforms; Xeon handles migrated mainframe workloads already in production; COBOL/FORTRAN/DB2 migration is surprisingly straightforward; and CICS/DL1/assembler migration requires significant effort. Aberdeen recommends 'surround, offload, or migrate' strategies over full 'replace' initiatives.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 2 |
| technologies.csv | 14 |
| observations.csv | 20 |
| codes.csv | 30 |

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

Peter S. Kastner (Apri). Intel's Itanium: Ready and Desirable for Mainframe-Class Workloads.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Q1-2004 in-depth qualitative interviews with U.S., European, and Asian users; quantitative survey of 98 qualified mainframe users
