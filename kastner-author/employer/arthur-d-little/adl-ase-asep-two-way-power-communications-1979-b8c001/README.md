# ADL Client AS&E ASEP: Two-Way Power-Line Communications and Time-of-Day Metering (1979)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1979-01-01 |
| Type | employer-record |
| Domain | employer/arthur-d-little/utility-systems |
| License | CC-BY-4.0 |

## Abstract

Trade-press article (likely Computerworld 1979) profiling American Science & Engineering's ASEP system, a two-way power-line communications system controlled by a Data General Eclipse S-230 minicomputer with 256K core memory. Used by utilities (Florida Power Corp, Florida Power & Light, Wisconsin Electric Power, etc.) for time-of-day metering, residential air-conditioning/water-heater control, and brownout/blackout prevention. AS&E was a Cambridge MA Kastner-adjacent ADL client.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 7 |
| technologies.csv | 5 |
| observations.csv | 11 |
| codes.csv | 28 |

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

Peter S. Kastner (1979). ADL Client AS&E ASEP: Two-Way Power-Line Communications and Time-of-Day Metering (1979).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

document-review
