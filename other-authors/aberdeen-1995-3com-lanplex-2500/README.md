# 3Com's LANplex 2500: Profiling the Consummate Ethernet/FDDI Workgroup Switch

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1995-09-01 |
| Type | product-profile |
| Domain | LAN-switching |
| License | CC-BY-4.0 |

## Abstract

This Aberdeen Group product profile, published September 1995, evaluates 3Com's LANplex 2500 Ethernet/FDDI workgroup switch approximately nine months after its December 1994 market introduction. Using primary user research across hospitals, financial institutions, universities, and manufacturing firms, combined with competitive analysis against Cisco Systems, Bay Networks, and ALANTEC, Aberdeen assessed the 2500's technical architecture, ISE-chip ASIC performance (565K pps forwarding rate), management capabilities (RMON, Transcend Enterprise Manager), and investment-protection roadmap. Key findings confirm the LANplex 2500 as the market's most capable Ethernet/FDDI workgroup switch at its price point, outperforming competitors on switching performance, feature set, and modular design while leveraging 3Com's established LANplex 6000 installed base. The study predicts that Fast Ethernet (100BaseTX) and OC-3 ATM uplink cards will ship in Q1 1996, that FDDI backbones will remain prominent in enterprise planning through the mid-1990s, and that 3Com's 6-to-9-month competitive lead is under pressure as rivals intensify development efforts. The report frames these findings within 3Com's three-stage High-Performance Scalable Networking (HPSN) vision, positioning the LANplex 2500 as Stage 2 of a migration path from collapsed backbones through distributed LAN switching toward eventual ATM adoption.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
| technologies.csv | 15 |
| observations.csv | 40 |
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

Aberdeen Group (1995). 3Com's LANplex 2500: Profiling the Consummate Ethernet/FDDI Workgroup Switch.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

product-profiling, user-research, competitive-analysis
