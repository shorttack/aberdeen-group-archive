# An Overview of Internet Application Development (CA Sales Training June 1996)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1996-06-01 |
| Type | employer-record |
| Domain | employer/aberdeen-group |
| License | CC-BY-4.0 |

## Abstract

'An Overview of Internet Application Development' — Peter S. Kastner presentation to Computer Associates Sales Training, June 1996. Introduces the Internet/intranet stack (thin-client browser, TCP/IP, HTTP, CGI, firewall, RDBMS) and contrasts Internet applications with traditional client-server. Early canonical analyst framing of the Web as an application-delivery platform delivered to a CA sales audience in the Netscape-dominant pre-IE3 era.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 6 |
| observations.csv | 10 |
| codes.csv | 29 |

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

Peter S. Kastner (1996). An Overview of Internet Application Development (CA Sales Training June 1996).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, executive-presentation, sales-force-education
