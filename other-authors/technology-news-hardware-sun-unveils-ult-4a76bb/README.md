# Sun Unveils UltraSPARC IV Processor

| Field | Value |
|-------|-------|
| Author | Jay Lyman, TechNewsWorld |
| Date | 2003-10-13 |
| Type | news-article |
| Domain | server-processors |
| License | CC-BY-4.0 |

## Abstract

TechNewsWorld article (Oct 13 2003, Jay Lyman) reporting Sun Microsystems' UltraSPARC IV unveiling at the 16th annual Microprocessor Forum in San Jose. The dual-threaded chip (two UltraSPARC III cores, on-chip memory controller supporting 16 GB DRAM, 8 MB L2 tags per core) was positioned as Sun's 'Throughput Computing' answer to Intel Itanium and IBM Power. Aberdeen Group research director Peter Kastner is a central skeptical-but-defensive voice: 'To Sun's installed base, UltraSPARC IV has to be competitive. It doesn't have to be world-beating,' and it would be 'foolish for Sun to exit processors' given 20 years of investment. Gartner VP Martin Reynolds argues the opposite — that Sun should exit chips. Harlan McGhan (Sun) previews 90nm with Texas Instruments and an 8-core/32-thread future chip.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 8 |
| observations.csv | 13 |
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

Jay Lyman, TechNewsWorld (2003). Sun Unveils UltraSPARC IV Processor.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

product-analysis, analyst-commentary
