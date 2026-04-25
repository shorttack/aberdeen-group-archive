# Stratus ET1-vs-TP1 competitive-intel dossier: Tandem-authored Tandem-vs-Stratus price/performance circular and Stratus internal correspondence

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner (compiler, Stratus Sales Support); Bill Ojile (Stratus Minneapolis); Tandem Computers (included competitive piece) |
| Date | 1986-01-14 |
| Type | competitive-intelligence |
| Domain | fault-tolerant-computing-benchmarks |
| License | CC-BY-4.0 |

## Abstract

A four-page Stratus competitive-intelligence dossier compiled by Peter Kastner (then Stratus Sales Support) documenting how Tandem was attacking Stratus on transaction price/performance using the ET-1/TP-1 benchmarks (the DebitCredit benchmark by a different name). Includes (a) a handwritten January 2, 1985 cover letter from Bill Ojile of Stratus Minneapolis transmitting the Tandem piece to 'Bill' (internal); (b) a January 14, 1986 electronic memo from Bill Ojile to Peter Kastner asserting that the ET-1 benchmark is 'about 2 times as easy as TP-1'; and (c) the Tandem-authored 'Tandem versus Stratus price/performance' competitive circular claiming Tandem TXP price/performance 50% better than Stratus XA600. Artifact of Kastner's Stratus competitive-analysis work; directly precedes the May 1987 Kastner-edited Sales Support newsletter.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 7 |
| observations.csv | 11 |
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

Peter S. Kastner (compiler, Stratus Sales Support); Bill Ojile (Stratus Minneapolis); Tandem Computers (included competitive piece) (1986). Stratus ET1-vs-TP1 competitive-intel dossier: Tandem-authored Tandem-vs-Stratus price/performance circular and Stratus internal correspondence.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

competitive-intelligence, benchmark-comparison, document-review
