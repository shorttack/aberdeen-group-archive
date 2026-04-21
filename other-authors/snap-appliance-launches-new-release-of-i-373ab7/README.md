# Snap Appliance Launches New Release of its Unified Software Platform — GuardianOS v3.1

| Field | Value |
|-------|-------|
| Author | Adaptec/Snap Appliance press release (Computerworld Australia) |
| Date | 2004-12-07 |
| Type | press-release |
| Domain | storage-NAS-iSCSI |
| License | CC-BY-4.0 |

## Abstract

Adaptec/Snap Appliance press release (Dec 7 2004, published on Computerworld Australia) announcing GuardianOS v3.1 — the Linux-based unified-storage platform powering Snap Servers (320GB to 30TB). Key enhancements: enhanced iSCSI support with 50%+ performance improvements over v3.0, new Server-to-Server Synchronization (S2S v2), full NDMP backup-protocol support, expanded global namespace capabilities, and integration with Adaptec's storage portfolio (Snap was acquired by Adaptec in June 2004). Peter Kastner of the Aberdeen Group provides the third-party endorsement: 'Snap Appliance's S2S v2 is a full-featured replication-for-the-masses solution that will give enterprises the opportunity to protect and easily move data without the significant investment or complexity that was required in the past. Together with the GuardianOS v3.1, Snap has a solid software offering for its departmental and enterprise servers that can continue to scale as the company expands its hardware product line.' The announcement also positions Snap against higher-end block-storage SAN vendors (EMC, NetApp) by combining NAS and iSCSI in a single appliance, a convergence that became standard in the storage industry over the following decade.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 6 |
| observations.csv | 7 |
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

Adaptec/Snap Appliance press release (Computerworld Australia) (2004). Snap Appliance Launches New Release of its Unified Software Platform — GuardianOS v3.1.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

press-release, analyst-endorsement
