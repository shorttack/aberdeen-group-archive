# DEC RDB NOTES File Thread: TP1/Debit-Credit Benchmark Discussion (Dec 1987)

| Field | Value |
|-------|-------|
| Author | Multiple DEC engineers (Saghagen, Rowlands, Mascall, Hammond, Kittell, Smith) |
| Date | 1987-12-09 |
| Type | internal-discussion-thread |
| Domain | OLTP-benchmark-methodology-and-DBS-metrics |
| License | CC-BY-4.0 |

## Abstract

Internal DEC VAX Rdb/VMS NOTES file thread (Note 461) on the TP1 / Debit-Credit benchmark, captured December 1987. Thread initiated by Arild Saghagen (OSL09::ARILDS, Office & Infosystem Marketing) seeking RDB performance data for a finance-company sale where DEC and Wang were the final vendors and the customer asked about TP1 transaction rates against a 2x8550 cluster. Replies clarify TP1 = Debit-Credit = Gray benchmark (Rob Rowlands, BISTRO::ROWLANDS), point to internal Valbonne report TP_REPORT23.LN03 (HERON), warn that the spec leaves scope for 'artistic interpretation' (Tony Mascall, GYPSC::MASCALL). Charlie Hammond (SQM::HAMMOND, ZKO2-02) explains that TP1, Debit-Credit and Gray are all the same benchmark, lists ambiguities (95th/1-sec vs 2-sec, back-end vs terminal response, partitioning tricks). Richard Kittell (COOKIE::KITTELL, Database A/D) draws an analogy between unspecified TPS ratings and unspecified stereo frequency response — and forwards an April 1987 standardization draft by Kevin Smith (COOKIE::KSMITH) defining DBS Standard Metrics for FY87 and FY88: TPS (D/C, BATCH/END-TO-END, QUALIFIED/PEAK), $/TPS metrics (Host vs B/E System, Cost vs Price vs COO), database size metrics, and back-up rate metrics. Notes Rudy Downs hired as DBS Performance Manager. Document contemporaneous with the Kohler/Hsu Debit-Credit Guidelines memo and shows DEC's broader DBS group converging on standardized benchmark metrics — 8 months before TPC was founded.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 4 |
| observations.csv | 11 |
| codes.csv | 38 |

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

Multiple DEC engineers (Saghagen, Rowlands, Mascall, Hammond, Kittell, Smith) (1987). DEC RDB NOTES File Thread: TP1/Debit-Credit Benchmark Discussion (Dec 1987).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

internal-engineering-NOTES-thread
