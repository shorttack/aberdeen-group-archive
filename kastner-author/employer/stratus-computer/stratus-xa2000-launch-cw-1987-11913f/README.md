# Stratus Readies XA2000 Series to Take on Tandem High End — Computerworld, 2 February 1987 (PSK + Foster quoted)

| Field | Value |
|-------|-------|
| Author | James Connolly (Computerworld) |
| Date | 1987-02-02 |
| Type | press-article |
| Domain | fault-tolerant-computing-product-launch |
| License | CC-BY-4.0 |

## Abstract

Computerworld feature on the Stratus XA2000 launch (the same family advertised in the ABA Banking Journal ad above). Article reports Stratus is launching a 'full-scale attack' on Tandem with the XA2000 family, pitting the high end against Tandem's 10-month-old NonStop VLX flagship; both vendors claim 50+ transactions/second peak. **William E. Foster, Stratus CEO**, quoted: 'We are selling into a market that has an insatiable appetite for transactions per second' and 'Most new applications for computers tend to be on-line applications. That is really what is driving the market. While people are looking at an on-line application, they have to ask themselves what happens if this thing goes down.' **Peter S. Kastner, manager of marketing support programs for Stratus**, explains the floating-point coprocessor (Motorola 68881) is designed for financial-modeling applications, not scientific/engineering markets. Article reports Stratus officials anticipate near-simultaneous IBM announcement adding XA2000 to **System/88 product line** (under Stratus-IBM OEM). Models 110/120/130/140 use single 40-slot chassis, Motorola 16-MHz 68020 + 68881 coprocessor, VOS Release 6.0 with 32-bit data path, 64MB memory, 64KB cache, 128MB virtual address, 46GB disk. Pricing: $260K-$500K Model 110; $770K-$1.1M Model 140. Yankee Group's Thomas Henkel comments this is Stratus' first move into VLX/IBM 3090 class but questions long-term IBM-Stratus compatibility and Stratus' application/database depth for high-performance TP particularly in manufacturing.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 7 |
| observations.csv | 8 |
| codes.csv | 24 |

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

James Connolly (Computerworld) (1987). Stratus Readies XA2000 Series to Take on Tandem High End — Computerworld, 2 February 1987 (PSK + Foster quoted).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, competitive-profiling, expert-opinion
