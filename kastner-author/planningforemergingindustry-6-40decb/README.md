# Planning for Emerging Industry-Standard Platforms (Executive White Paper)

| Field | Value |
|-------|-------|
| Author | Aberdeen Group (Peter S. Kastner) |
| Date | 2003-08-01 |
| Type | white-paper |
| Domain | industry-standard-servers/chipsets/memory/systems-management/I-O |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Executive White Paper sponsored by Intel surveying the 2004 generational transition in industry-standard (Intel Architecture) computing. Covers processors and enterprise chipsets (Xeon/Nocona, Itanium 2/Madison, E7501/E7205/E8870/Lindenhurst/Twin Castle, 875P Canterwood), memory evolution from DDR to DDR2 with mainframe-class memory mirroring/sparing/scrubbing, Intelligent Platform Management Initiative (IPMI 1.5) for heterogeneous datacenter management, and the major I/O transition from parallel PCI-X to serial PCI Express. Aberdeen predicts server consolidation, data-center utility computing, and continued IA market-share gain.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 26 |
| observations.csv | 32 |
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

Aberdeen Group (Peter S. Kastner) (2003). Planning for Emerging Industry-Standard Platforms (Executive White Paper).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, technology-assessment, roadmap-forecasting
