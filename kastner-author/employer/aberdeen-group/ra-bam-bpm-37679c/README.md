# The Business Activity Monitoring Benchmark Report: The Eyes and Ears of BPM

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner, Aberdeen Group |
| Date | 2006-08 |
| Type | employer-record |
| Domain | Business Activity Monitoring / Business Process Management |
| License | CC-BY-4.0 |

## Abstract

Benchmark report surveying 160+ Global 5000 enterprises on Business Process Monitoring (BPM and BAM). Finds 94% of respondents moderately or very satisfied with IT results of BPM implementations; average ROI 18%, ROA 10%, revenue increase 9%, expense decrease 12%. Best in Class companies are 50% more likely than Industry Average to focus on competition as driver. 42% of companies are in planning stages. Median investment $101K-$500K. Real-time defined variably: 25% of BIC capture process state in under 10 seconds. Key challenge: management buy-in. Sponsored report (sponsors section left blank in draft). Peter Kastner is Research VP and Co-Founder. DRAFT dated 08-15-06.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 2 |
| technologies.csv | 7 |
| observations.csv | 62 |
| codes.csv | 27 |

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

Peter S. Kastner, Aberdeen Group (2006). The Business Activity Monitoring Benchmark Report: The Eyes and Ears of BPM.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Survey-based benchmark (N>160 Global 5000 enterprises); Aberdeen Competitive Framework; online survey July-August 2006 supplemented by telephone interviews
