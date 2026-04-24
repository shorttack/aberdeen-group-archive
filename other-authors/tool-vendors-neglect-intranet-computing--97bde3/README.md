# Tool vendors neglect intranet needs (Kastner three-year IT predictions)

| Field | Value |
|-------|-------|
| Author | Douglas Hayward |
| Date | 1996-10-30 |
| Type | news-article |
| Domain | intranet-tools-browser-vs-Windows-client-1996 |
| License | CC-BY-4.0 |

## Abstract

Computing UK article by Douglas Hayward interviewing Peter Kastner (Aberdeen Group VP) in London during a BMC Software visit. Kastner delivers a set of three-year industry predictions: intranet-development delayed until tool vendors treat browsers as equal to Windows clients; Novell will struggle as intranet directory services obviate NDS; object-oriented and internet-based technology will temporarily raise then reduce IT ownership costs; network-computer vendors will bundle WordPerfect once Corel rewrites it in Java. Closes with Kastner's 1973 Chase Manhattan Y2K-noncompliant-code admission.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
| technologies.csv | 10 |
| observations.csv | 9 |
| codes.csv | 25 |

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

Douglas Hayward (1996). Tool vendors neglect intranet needs (Kastner three-year IT predictions).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

news-reporting, analyst-predictions, expert-interview
