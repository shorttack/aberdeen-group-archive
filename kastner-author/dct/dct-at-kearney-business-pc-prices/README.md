# A.T. Kearney Benchmark: Flagship Business Desktop Price Tracking, Aug 2002 – Mar 2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-03-10 |
| Type | dct |
| Domain | dct |
| License | CC-BY-4.0 |

## Abstract

Six-date longitudinal price benchmark (Aug 20, Oct 2, Nov 8, Dec 2, Dec 17, 2002; Mar 10, 2003) tracking five flagship business desktop configurations on a standardized config (2.4 GHz P4, 256 MB DDR, 40 GB 7200 RPM HDD, CD-ROM, no monitor): Dell Optiplex GX260, Gateway E-4000 Special Deluxe, HP Compaq Evo D510 minitower (both SB and standard variants), and IBM NetVista M42 8303. Built for an A.T. Kearney consulting engagement to quantify the 7-month delta in street prices across Tier-1 vendors. Dell's price moved +$40 (+3%), Gateway +$350 (+35%), HP Compaq SB variant +$333, IBM -$20, HP standard +$196.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 2 |
| observations.csv | 33 |
| codes.csv | 23 |

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

Peter S. Kastner (2003). A.T. Kearney Benchmark: Flagship Business Desktop Price Tracking, Aug 2002 – Mar 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

benchmarking
