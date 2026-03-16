# Dell: Applying Its Business Value Model to Storage

## Frictionless Data Package

**Study ID:** `2004-05dell-storage-profile-editpk-051704f-78147f`

| Field | Value |
|---|---|
| **Title** | Dell: Applying Its Business Value Model to Storage |
| **Author** | David Hill; Peter Kastner |
| **Date** | 2004-05-01 |
| **Type** | Profile |
| **Subject Domain** | Enterprise Storage |
| **License** | CC-BY-4.0 |

## Document Assessment

| Dimension | Rating | Justification |
|---|---|---|
| **Importance** | medium | Documents Dell's strategic expansion from PCs/servers into enterprise storage through the EMC partnership; captures a pivotal moment in storage industry consolidation |
| **Relevance** | medium | Dell's storage strategy evolved significantly after the 2016 EMC acquisition; the standards-based and bundling approaches described remain relevant patterns |
| **Prescience** | medium | Correctly predicted standards-based storage would win over proprietary; the Dell-EMC partnership deepened into a full acquisition in 2016 |

## Summary

This Aberdeen Group profile examines Dell's application of its business value model to the enterprise storage market in 2004. The study analyzes Dell's three core strategies: (1) delivering industry-leading value through continuous price/performance improvement via supply chain management excellence, (2) driving industry standards through participation in organizations like FCLC, Serial ATA II, Serial Attached SCSI, and SNIA, and (3) moving high-end functionality downstream from data center to workgroup.

Key topics include the Dell|EMC CX series disk arrays (CX300/CX500/CX700 third-generation products), the new AX100 entry-level array combining Fibre Channel and SATA, PowerVault NAS solutions (775N/770N/745N) running Windows Storage Server 2003, PowerVault tape backup products (122T/132T/136T/160T), and a multi-vendor storage software portfolio featuring Legato Networker, VERITAS BackupExec/NetBackup, CommVault Galaxy, and Yosemite TapeWare.

## Historical Significance

- The Dell|EMC partnership, extended through 2008 in this document, ultimately led to Dell's $67 billion acquisition of EMC in 2016 -- the largest technology acquisition in history at that time.
- The document's emphasis on standards-based storage proved prescient: SATA became the dominant capacity-tier interface, and open standards drove industry-wide cost reductions.
- Several entities discussed have since undergone major changes: Brocade was acquired by Broadcom (2017), VERITAS was acquired by Symantec (2005) then spun off (2016), and Legato was absorbed into EMC.

## Package Contents

```
.
├── README.md                  # This file
├── datapackage.json           # Frictionless Data Package descriptor
├── data/
│   ├── studies.csv            # Study metadata (1 record, 16 fields)
│   ├── entities.csv           # Companies and organizations (14 records)
│   ├── technologies.csv       # Storage technologies and products (12 records)
│   ├── observations.csv       # Structured observations (35 records)
│   └── codes.csv              # Controlled vocabulary codes (29 records)
├── schema/
│   └── schema_org.json        # Schema.org JSON-LD metadata
├── source/
│   └── original_text.md       # Original document text with metadata
└── scripts/
    └── demo_analysis.py       # Python demo for loading and analyzing the data
```

## Observation Types

All observations use one of 8 canonical observation types:

| Type | Count | Description |
|---|---|---|
| `strategy-classification` | 6 | Dell's strategic approaches and positioning |
| `viability-prediction` | 3 | Forward-looking predictions about partnerships and technologies |
| `actual-outcome` | 3 | Verified outcomes paired with predictions |
| `technology-assessment` | 8 | Evaluations of specific products and technologies |
| `benchmark-result` | 3 | Quantitative performance measurements (CX generation improvements) |
| `framework-factor` | 6 | Components of Dell's business model and methodology |
| `market-data` | 3 | Survey data and market research findings |
| `expert-opinion` | 3 | Aberdeen analyst conclusions and judgments |

## Key Entities

- **Dell** -- Primary subject; applying SCM business model to storage
- **EMC** -- Storage partnership partner (co-branded CX/AX arrays)
- **Brocade** -- SAN switch partner (acquired by Broadcom 2017)
- **QLogic** -- SAN HBA partner (acquired by Cavium 2016, then Marvell 2018)
- **VERITAS** -- Backup software partner (acquired by Symantec 2005, spun off 2016)
- **CommVault** -- Backup software partner (continues independently)
- **Aberdeen Group** -- Publisher and analyst firm

## Usage

```python
python scripts/demo_analysis.py
```

Or load individual CSV files with any data analysis tool:

```python
import pandas as pd
observations = pd.read_csv("data/observations.csv")
```

## Pipeline

Processed by Archival Ingest Skill v13 on 2026-03-16.
