# Digital's Multia Enterprise Client: Finally Someone Listened

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1995-12-01 |
| Type | product-profile |
| Domain | enterprise-desktop-computing |
| License | CC-BY-4.0 |

## Abstract

This Aberdeen Group product profile evaluates Digital Equipment Corporation's Multia 'enterprise client' desktop, introduced in late 1995 with both Alpha 64-bit RISC and Intel Pentium 100 models. The study employs product profiling, technology assessment, and competitive analysis to position Multia as a turn-key universal client that addresses the longstanding IS requirement for a single desktop capable of simultaneously accessing mainframes, Unix servers, PC servers, and the World Wide Web via pre-configured emulators and multiple communications protocols. Key findings include that Multia is priced $500–$800 above a comparable PC but justifies the premium through integrated interoperability, centralized IS desktop management, pre-configured terminal emulators (3270, VT 340/420, Netscape Navigator, Rumba, Kea!), a photo-album-size footprint, and chip-upgradeable dual Alpha/Intel architecture. Aberdeen concludes that Digital is the only major computer vendor that listened to enterprise IS requirements and predicts that Multia's centralized management capabilities will meaningfully reduce IS staffing and support costs at remote sites, and that the new 'market-oriented Digital' has finally arrived as a credible enterprise client vendor.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 25 |
| observations.csv | 36 |
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

Aberdeen Group (1995). Digital's Multia Enterprise Client: Finally Someone Listened.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

product-profiling, technology-assessment, competitive-analysis
