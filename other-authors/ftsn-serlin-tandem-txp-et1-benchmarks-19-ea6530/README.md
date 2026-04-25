# Omri Serlin FTSN-33: Tandem Reports TXP ET1 Benchmarks 7.2-9.6 tps/CPU; Cites Stratus 1.0-1.1 tps/CPU (May 15, 1985)

| Field | Value |
|-------|-------|
| Author | Omri Serlin (FTSN newsletter) |
| Date | 1985-05-15 |
| Type | industry-newsletter |
| Domain | fault-tolerant-computing/transaction-processing-benchmarks |
| License | CC-BY-4.0 |

## Abstract

Issue 33 of Omri Serlin's Fault-Tolerant Systems News (FTSN) newsletter, published May 15, 1985 by ITOM International (Los Altos, CA). Reports new Tandem ET1 benchmark data on a 4-processor TXP system, with TXP ranging 7.2-9.6 tps/CPU and (per Tandem) showing a significant cost-per-tps edge over IBM's TPF2. Three Guardian/Pathway/TMF software-stack configurations were tested ('V.2', 'V.5', 'V.6 new', 'V.6 old' with Guardian A06+DP1) producing 9.56 / 7.60 / 4.70 / 3.17 tps/processor and $33.7K / $39.2K / $58K / $80.6K cost-per-tps respectively. Database: 2M account records, 2,000 teller records, 200 branch records (1/5 the size of anon-et-al's Datamation specification). Tandem VP of Software Dennis McEvoy claims Tandem's V.2 and V.5 cost-per-tps is substantially lower than IBM TPF2 even though both are coded in COBOL (TPF2 mandates assembly), and that a 16-CPU TXP system can do 100 tps and a 10-system FOX network 1000 tps. The benchmark was run by Harald Sammer's 1000-tps group in Frankfurt. Notably, FTSN cross-references the Stratus result from FTSN-32 at 1.0-1.1 tps/CPU — making this newsletter a rare neutral cross-vendor 1985 ET1 data point that contextualizes Stratus's 1985-1986 TP1/ET1 claims (Batch 25 studies #5 and #7).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
| technologies.csv | 5 |
| observations.csv | 7 |
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

Omri Serlin (FTSN newsletter) (1985). Omri Serlin FTSN-33: Tandem Reports TXP ET1 Benchmarks 7.2-9.6 tps/CPU; Cites Stratus 1.0-1.1 tps/CPU (May 15, 1985).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-newsletter-with-vendor-data
