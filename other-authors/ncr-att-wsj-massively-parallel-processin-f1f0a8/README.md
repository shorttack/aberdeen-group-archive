# NCR/AT&T Wall Street Journal Full-Page Ad Featuring Aberdeen Group / Kastner Endorsement of Commercial Massively-Parallel Processing

| Field | Value |
|-------|-------|
| Author | NCR Corporation / AT&T Company (advertiser) |
| Date | 1993-11-08 |
| Type | full-page-print-ad |
| Domain | commercial-massively-parallel-processing/data-warehouse-marketing |
| License | CC-BY-4.0 |

## Abstract

NCR (an AT&T Company) full-page advertisement on page B9 of the Wall Street Journal, Monday, November 8, 1993, anchored by a substantial Peter S. Kastner / Aberdeen Group endorsement quote: 'NCR is demonstrating not only that (parallel processing) is ready for commercial applications now, but that it is an attractive alternative encompassing what modern users are demanding: a robust computing environment, an open operating system, interoperability with other suppliers' systems, flexible expansion, and attractive price/performance.' The ad claims more than 400 NCR System 3600 and DBC/1012 (Teradata) systems installed at over 180 of the world's most successful companies, positions NCR as ten years into commercial massively-parallel processing, and announces fifth-generation hardware and software while competitors had yet to announce their first generation. A 'Share of Commercial Parallel Processing Market' callout cites Aberdeen Group as the source. This is a Kastner-anchored third-party-endorsement artifact in a top-tier business newspaper, contemporary with the Aberdeen Open OLTP white-paper corpus.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 5 |
| observations.csv | 7 |
| codes.csv | 31 |

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

NCR Corporation / AT&T Company (advertiser) (1993). NCR/AT&T Wall Street Journal Full-Page Ad Featuring Aberdeen Group / Kastner Endorsement of Commercial Massively-Parallel Processing.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

advertising-collateral-with-third-party-endorsement
