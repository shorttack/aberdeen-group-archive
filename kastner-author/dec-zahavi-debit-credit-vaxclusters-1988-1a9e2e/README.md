# DEC Zahavi Memo: Debit-Credit Benchmark on VAXclusters (March 1988)

| Field | Value |
|-------|-------|
| Author | Bill Zahavi, DEC TP Systems Performance Analysis (HYPER::BZAHAVI) |
| Date | 1988-03-04 |
| Type | internal-engineering-memo |
| Domain | VAXcluster-OLTP-architecture |
| License | CC-BY-4.0 |

## Abstract

Internal Digital Equipment Corporation interoffice memorandum dated 4-March-1988 by Bill Zahavi (TP Systems Performance Analysis, MR01-1/A65, DTN 297-7795, HYPER::BZAHAVI) addressed to @DC_VAXCLUSTER and @GROUP, on implementing the Debit-Credit benchmark on VAXclusters. Identifies the Distributed Lock Manager (DLM) as the major obstacle: only one cluster member owns locks for a given file, and the Debit-Credit specification's requirement that 15% of teller activity address other-branch accounts forces inter-node CI bus traffic. Distinguishes flat-file (RMS, Hash) from formal-database (DBMS, Rdb) implementations. Discusses partitioning strategies (cluster-member-A owns files-A, etc.) and the asymmetric statistics: 7.5% of cross-branch traffic lands on a different cluster member's locks for a 2-member cluster. Acknowledges that DECintact works only with flat files (RMS, Hash) while ACMS works best with DBMS and Rdb. Proposes that without 2-Phase Commit (2PC), only certain types of applications can be distributed using formal databases — explicitly referencing Phil Bernstein's prior memo. Closes by calling for cross-functional cooperation between TP, Databases, and VMS groups for both short and long-term solutions, and asks the document be treated as a 'living document.' Direct technical companion to the Kohler/Hsu guidelines (Study 1) and the broader DEC OLTP performance-engineering corpus.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 8 |
| observations.csv | 8 |
| codes.csv | 36 |

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

Bill Zahavi, DEC TP Systems Performance Analysis (HYPER::BZAHAVI) (1988). DEC Zahavi Memo: Debit-Credit Benchmark on VAXclusters (March 1988).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

engineering-analysis-memo
