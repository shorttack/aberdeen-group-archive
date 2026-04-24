# Urban Wi-Fi Gridlock Predicted To Arrive in 2004 (Kastner/Aberdeen report)

| Field | Value |
|-------|-------|
| Author | eWEEK staff |
| Date | 2003-10-27 |
| Type | news-article |
| Domain | wifi-interference-urban-hotspots-2003 |
| License | CC-BY-4.0 |

## Abstract

eWEEK coverage of Peter Kastner (Aberdeen) report 'The Urban Wi-Fi Crash of 2004' predicting urban Wi-Fi interference gridlock. Kastner (senior analyst at Boston-based Aberdeen) argues that more powerful/advanced 802.11 flavors won't help users because they are automatically 'dumbed down' by other access points. Notes purchases shifting to 802.11g for throughput but without solving the interference problem. Framed as threatening hot-spot users in urban shadows of overlapping access points.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 6 |
| observations.csv | 6 |
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

eWEEK staff (2003). Urban Wi-Fi Gridlock Predicted To Arrive in 2004 (Kastner/Aberdeen report).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

news-reporting, analyst-report-summary
