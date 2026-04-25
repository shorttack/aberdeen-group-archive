# Aberdeen Group SNR Architecture Slide Set: Critical Technology Planning Areas, Three-Tier Plus Topology, Client-Server Hype vs Implementation (1992)

| Field | Value |
|-------|-------|
| Author | Aberdeen Group / Peter S. Kastner (presenter) |
| Date | 1992 |
| Type | aberdeen-presentation-slides |
| Domain | enterprise-architecture/three-tier-client-server |
| License | CC-BY-4.0 |

## Abstract

1992 Aberdeen Group 'SNR Architecture' slide deck (sparse OCR; original was a graphics-heavy presentation deck) outlining four 'Critical Technology Planning Areas' — Systems Software, Application Development, Acquisition, and Enterprise Topology — and presenting a 'Three-tier Plus' enterprise-topology model with 'state-of-the-art downsizing': enterprise server plus decision support; analytical system; replicated/departmental systems; PCs, Workstations, Macs, and Terminals at the edge. Also documents Aberdeen's 1992 stance that client-server has 'much hype but minimal application implementation' with at least six common definitions in use, and presents an 'enterprise spoke' interface set — Product Look-Up, Pricing Information, Order Entry, Master Database, and Current Inventory — bridging Production Systems to the enterprise edge. The deck is fragmentary in OCR but consistent with Aberdeen's 1991-1993 distributed-systems / Open OLTP analytical posture (Batches 22-24).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 2 |
| technologies.csv | 5 |
| observations.csv | 5 |
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

Aberdeen Group / Peter S. Kastner (presenter) (1992). Aberdeen Group SNR Architecture Slide Set: Critical Technology Planning Areas, Three-Tier Plus Topology, Client-Server Hype vs Implementation (1992).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

aberdeen-analyst-presentation-deck
