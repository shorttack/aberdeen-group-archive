# Intel's Centrino: Don't Man the Barricades

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-03-01 |
| Type | expert-report |
| Domain | Enterprise Mobility / Wireless Networking |
| License | CC-BY-4.0 |

## Abstract

Aberdeen/Kastner expert editorial on Intel's Centrino platform launch (March 12, 2003). Analyzes Centrino as integrated mobile Pentium 4 + chipset + 802.11 wireless adapter. Warns IT executives against banning wireless notebooks (the 'barricade' metaphor) in response to rogue access point threats. Cites Aberdeen research showing 30 min/day productivity gains for campus workers; PricewaterhouseCoopers ROI data (6-month payback). Recommends embracing wireless via Cisco LEAP and Windows Server 2003 hardening rather than disabling Centrino's wireless capability.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 7 |
| observations.csv | 20 |
| codes.csv | 33 |

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

Peter S. Kastner (2003). Intel's Centrino: Don't Man the Barricades.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Expert opinion; Aberdeen Group research; industry interviews
