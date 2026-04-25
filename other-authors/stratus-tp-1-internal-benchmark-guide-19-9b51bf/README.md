# Stratus 'TP-1 Performance Model' internal benchmark guide (1983, Stratus internal)

| Field | Value |
|-------|-------|
| Author | Stratus Computer engineering (uncredited) |
| Date | 1983 |
| Type | internal-engineering-document |
| Domain | fault-tolerant-OLTP-benchmarks |
| License | CC-BY-4.0 |

## Abstract

Earliest Stratus internal performance document recovered in the corpus. Defines the TP-1 model and walks through small relative file (2.9 tps; 69% CPU; 18.0 disk I/O/sec), large relative file (2.3 tps; 94.7% CPU), and large indexed file configurations (1.5-1.8 tps depending on memory and server-queue topology). Key observations: cache utilization significantly impacts performance; performance is most affected by disk type/number/file size; multiple server copies greatly improve performance; server priority should exceed requester priority. The Stratus-vs-Tandem comparison section sits behind the TP-1 model definition. Predates the FTSN-32/FTSN-33 1985 Stratus 1.0-1.1 tps/CPU figures cited in Batch 25 — TP-1 is essentially Stratus's pre-ET1 internal predecessor benchmark.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 2 |
| technologies.csv | 4 |
| observations.csv | 5 |
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

Stratus Computer engineering (uncredited) (1983). Stratus 'TP-1 Performance Model' internal benchmark guide (1983, Stratus internal).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Stratus internal performance-measurement document defining the TP-1 model (Requester/Server with COBOL/TPF requester and PL/1 server, transactions initiated by delay interval, no screen I/O, duplicated servers, varied file sizes/types). Reports 1.5-2.9 tps results across small/large relative and indexed file configurations on non-duplexed Stratus systems, then closes with Stratus-vs-Tandem observations.
