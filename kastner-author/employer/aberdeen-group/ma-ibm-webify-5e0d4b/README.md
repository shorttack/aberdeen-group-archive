# IBM + Webify = Industry SOA Application Jumpstart

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2006-08-03 |
| Type | employer-record |
| Domain | SOA; vertical market applications; enterprise software M&A; application development |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Market Alert analyzing IBM Software Group's August 2006 acquisition of Webify Solutions, a provider of pre-built vertical-market SOA application components. Kastner argues the acquisition catalyzes the nascent market for industry-specific SOA development. Key analysis: 90% of Global 5000 businesses will exit 2006 with SOA activities underway; half are building SOA using 'SOA Lite' (web services + lightweight tools). Kastner distinguishes 'SOA Lite' from 'Enterprise SOA' (with ESB, repository, management, governance). Webify provides pre-built customizable SOA service components for insurance, healthcare, banking, and telecom. IBM with Webify is described as 'in a category of one.' Kastner recommends enterprise application programmers in healthcare and insurance evaluate IBM-Webify vs. Eclipse or Microsoft Visual Studio on lifecycle lines-of-code metric.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 15 |
| observations.csv | 18 |
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

Peter S. Kastner (2006). IBM + Webify = Industry SOA Application Jumpstart.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Aberdeen Market Alert — analyst commentary on IBM acquisition of Webify Solutions
