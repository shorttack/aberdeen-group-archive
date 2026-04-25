# InfoWorld — Dell sharpens blade attack: PowerEdge 1655MC server blades (Neel, 8-Apr-2002)

| Field | Value |
|-------|-------|
| Author | Dan Neel — InfoWorld Magazine |
| Date | 2002-04-08 |
| Type | trade-press-feature |
| Domain | server-blades-and-modular-computing |
| License | CC-BY-4.0 |

## Abstract

InfoWorld Magazine April 8, 2002 (circulation 225,047 weekly, San Mateo CA) feature by Dan Neel reporting on Dell's announcement at its spring analyst meeting in New York of the PowerEdge 1655MC server blades — Dell's first blade server entry, scheduled for third-quarter shipping. Article positions Dell as joining a 'groundswell' of competitors (HP, Compaq, others) capitalizing on IT executive interest in server blades. PowerEdge 1655MC hosts six dual-processor Intel Pentium III blades in a 5.25-inch rack — described as a precursor to Dell's future 'brick' servers (multiple servers per chassis, customer-assembled blocks of storage and memory). Quotes Peter Kastner, chief research officer of Aberdeen Group in Boston: 'Dell is trying to maintain a flexibility and an agility that is at the core of their business.' Notes 1655MC density limit (only 84 blades in standard rack vs. Compaq's hundreds), but Dell defends with VP Randy Groves saying competitors 'have focused on customers willing to sacrifice performance for space and power reasons. We don't see much of that.' Article notes Dell's parallel InfiniBand partnership with Microsoft. Dell hardware roadmap moves blade → modular brick → shared power/cooling decreasing data-center costs.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 6 |
| observations.csv | 11 |
| codes.csv | 42 |

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

Dan Neel — InfoWorld Magazine (2002). InfoWorld — Dell sharpens blade attack: PowerEdge 1655MC server blades (Neel, 8-Apr-2002).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

journalistic-reporting-with-analyst-quotes
