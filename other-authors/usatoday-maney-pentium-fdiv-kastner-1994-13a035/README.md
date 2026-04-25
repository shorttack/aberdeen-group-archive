# Intel May Get Chip on Its Shoulder (USA Today on IBM-Intel Pentium FDIV battle)

| Field | Value |
|-------|-------|
| Author | Kevin Maney (USA Today) |
| Date | 1994-12-13 |
| Type | trade-press-feature |
| Domain | semiconductor/Pentium-FDIV-bug/PC-industry-PR |
| License | CC-BY-4.0 |

## Abstract

Kevin Maney's USA Today feature (13 December 1994) on IBM's decision to halt Pentium PC shipments after its labs concluded the FDIV bug could surface in spreadsheet recalculations as often as once every 24 days (vs Intel's once-every-27000-years claim). Quotes Aberdeen Group analyst Peter Kastner: 'The whole industry will get bloodied... It won't do much good for anybody's PC sales now through Christmas. IBM is a large, respected name. If it says there's a problem, people will believe it.' Kastner is also quoted on usage-pattern realism ('Most people with a Pentium computer and a spreadsheet don't do anything near 15 minutes of recalculations a day. It's more like seconds worth.'). Other voices: Intel CEO Andy Grove, IBM lab head Bill Pullyblank, IBM spokesman Rob Wilson, Microprocessor Report editor Michael Slater, PC Week editor in chief Daniel Lyons, Lynchburg College math professor Thomas Nicely.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 15 |
| technologies.csv | 4 |
| observations.csv | 11 |
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

Kevin Maney (USA Today) (1994). Intel May Get Chip on Its Shoulder (USA Today on IBM-Intel Pentium FDIV battle).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

press-feature-with-analyst-quotes
