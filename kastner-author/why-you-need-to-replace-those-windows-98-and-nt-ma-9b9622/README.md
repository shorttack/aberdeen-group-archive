# Archival Ingest: Why You Need To Replace Those Windows 98 And NT Machines

**Archival Ingest Skill Version:** v13
**Ingest Date:** 2026-03-15
**Study ID:** `why-you-need-to-replace-those-windows-98-and-nt-ma-9b9622`

## Study Overview

| Field | Value |
|-------|-------|
| **Title** | Why You Need To Replace Those Windows 98 And NT Machines |
| **Author** | Peter S. Kastner (EVP & CRO, Consumer Digital Technology Practice, Aberdeen Group) |
| **Date** | 2003-05-05 |
| **Type** | Market Study |
| **Subject Domain** | Desktop Lifecycle Management |
| **Publication** | InternetWeek.com (CMP Media LLC) |
| **License** | CC-BY-4.0 |

## Abstract

Aberdeen Group analyst Peter S. Kastner argues that 50M+ aging PCs running Windows 98 and NT in corporate environments pose escalating security and compliance risks as Microsoft ends support. The article recommends an immediate PC replacement cycle citing Windows XP Pro SP1 stability, the Windows Server 2003 platform, Intel Springdale chipset and Centrino mobile platform, auditor scrutiny of unsupported systems, and potential legal liability for negligence. Published at a critical juncture of the Windows lifecycle transition in May 2003.

## Assessments

| Dimension | Rating | Summary |
|-----------|--------|---------|
| **Importance** | Medium | Timely call-to-action during a critical Windows lifecycle transition; articulated security and compliance risks enterprises were ignoring |
| **Relevance** | Low | Specific OS/hardware recommendations obsolete, but lifecycle management and security-compliance framework remain relevant templates |
| **Prescience** | High | Correctly predicted unsupported-OS security risks, auditor/regulatory compliance mandates (SOX, HIPAA, PCI-DSS), Intel platform trajectory, and laptop market dominance |

## Package Contents

```
why-you-need-to-replace-those-windows-98-and-nt-ma-9b9622/
├── README.md                  # This file
├── datapackage.json           # Frictionless Data Package descriptor
├── data/
│   ├── studies.csv            # Study metadata (1 record, 16 columns)
│   ├── entities.csv           # Extracted entities (8 records, 9 columns)
│   ├── technologies.csv       # Extracted technologies (16 records, 9 columns)
│   ├── observations.csv       # Coded observations (32 records, 12 columns)
│   └── codes.csv              # Code definitions (31 records, 4 columns)
├── schema/
│   └── schema_org.json        # Schema.org JSON-LD metadata
├── scripts/
│   └── demo_analysis.py       # Validation and analysis demo script
└── source/
    └── original_text.md       # Full original article text with metadata
```

## Data Summary

- **Entities:** 8 organizations and persons including Aberdeen Group, Microsoft, Intel, CMP Media LLC, Symantec, and Ford
- **Technologies:** 16 technologies spanning operating systems, server platforms, processors, chipsets, mobile platforms, malware, and protocols
- **Observations:** 32 coded observations covering market data, technology assessments, security assessments, expert opinions, viability predictions, actual outcomes, and strategy classifications

## Key Data Points

- 50M+ aging corporate PCs running Windows 98/NT
- Windows NT 4.xx end of support: June 30, 2003
- Windows 98/SE end of support: January 16, 2004
- Managed desktop price range: $1,250-$1,400
- Approximately 1/3 of corporate PC purchases were laptops
- Microsoft OS support lifecycle: 5 years after introduction

## Usage

### Validation

```bash
python scripts/demo_analysis.py
```

### Loading Data

```python
import pandas as pd

studies = pd.read_csv("data/studies.csv")
entities = pd.read_csv("data/entities.csv")
technologies = pd.read_csv("data/technologies.csv")
observations = pd.read_csv("data/observations.csv")
codes = pd.read_csv("data/codes.csv")
```

### Frictionless Data Package

```python
from frictionless import Package

package = Package("datapackage.json")
for resource in package.resources:
    print(f"{resource.name}: {resource.path}")
```

## Methodology

Observations were extracted using three methodology codes:
- **expert-opinion**: Professional judgments by Kastner and cited experts (auditors, lawyers)
- **industry-analysis**: Market data and industry statistics cited in the study
- **document-review**: Factual data from published vendor documentation and threat databases

## Citation

Kastner, Peter S. "Why You Need To Replace Those Windows 98 And NT Machines." InternetWeek.com, CMP Media LLC, May 5, 2003.

## License

This data package is released under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
