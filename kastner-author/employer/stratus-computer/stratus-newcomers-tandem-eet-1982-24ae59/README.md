# Newcomers Invade Fault-Tolerant Field, But Tandem Has Big Lead — Electronic Engineering Times, 24 May 1982 (PSK quoted)

| Field | Value |
|-------|-------|
| Author | Electronic Engineering Times staff |
| Date | 1982-05-24 |
| Type | press-article |
| Domain | fault-tolerant-computing-market-entry |
| License | CC-BY-4.0 |

## Abstract

Electronic Engineering Times feature article examining new entrants challenging Tandem Computers' overwhelming dominance of the fault-tolerant computer-systems market. Newcomers profiled: **Stratus Computers (Natick, MA)**, **August Systems (Tigard, OR)**, and **Synapse Computers (Milpitas, CA)**. Stratus is identified as the biggest threat to Tandem, having begun shipments in February 1982. **Peter Kastner, manager of marketing development at Stratus**, claims the company has already "taken away some orders from Tandem" — selling to a dairy company and a shoe-store chain. Stratus output of four systems per month is below Tandem's pace, but Kastner argues Stratus will become a heavyweight based on design features superior to the leader's, and on price (minimum-configuration Stratus ~$110,000 below the $260,000 equivalent Tandem package). Kastner contrasts Stratus' hardware-based 32-bit architecture with Tandem's software-based 'Guardian' approach (parallel processors with periodic review and Encompass transaction tracking). Article also includes 32-bit-architecture debate (Tandem's Jerry Peterson argues 16-vs-32 bits is irrelevant for transaction throughput; Larry Roberts of Hambrecht & Quist predicts Tandem will ship 32-bit within 18 months). Strategic Business Services projects $2.6B FT hardware/peripherals annual market by 1988; Dataquest forecasts $5B annual including software by 1985. SIAC's John McGee describes the established-vendor switching cost barrier facing newcomers.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 6 |
| observations.csv | 10 |
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

Electronic Engineering Times staff (1982). Newcomers Invade Fault-Tolerant Field, But Tandem Has Big Lead — Electronic Engineering Times, 24 May 1982 (PSK quoted).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, competitive-profiling, expert-opinion
