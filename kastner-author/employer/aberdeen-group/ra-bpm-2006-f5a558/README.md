# The Business Process Management Benchmark Report: Achieving Real Results through Monitoring and Performance Measurement

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner, Aberdeen Group |
| Date | 2006-08 |
| Type | employer-record |
| Domain | Business Process Management / Business Process Monitoring |
| License | CC-BY-4.0 |

## Abstract

Full 38pp Aberdeen BPM benchmark report by Peter Kastner. Survey of 160+ Global 5000 enterprises. Finds 94% of respondents moderately or very satisfied with BPM IT system results; average ROI 18%, ROA 10%, 9% revenue increase, 12% expense decrease, 2x IT value/budget ratio. BAM vs BPM-centric approaches equally valid; 57% chose all equally. Key challenge: management buy-in. BPM monitoring 'wags the tail' of BPM suite — monitoring component sufficient to pull through BPM suite sales. 42% still in planning stages. Sponsored by Tier1 Innovation and Value Chain International Limited.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 8 |
| observations.csv | 120 |
| codes.csv | 37 |

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

Peter S. Kastner, Aberdeen Group (2006). The Business Process Management Benchmark Report: Achieving Real Results through Monitoring and Performance Measurement.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Survey-based benchmark (N>160 Global 5000 enterprises); Aberdeen Competitive Framework; online survey July-August 2006 supplemented by telephone interviews
