# Microsoft: The Joker of Enterprise IS Computing

**Aberdeen Group Executive Viewpoint Vol.10 No.20 | ~September 1997**

## Study Metadata

| Field | Value |
|-------|-------|
| study_id | 1997-microsoft--the-joker-of-enterprise--158636 |
| title | Microsoft: The Joker of Enterprise IS Computing |
| author | John R. Logan |
| date | 1997-09-01 |
| type | executive-viewpoint |
| subject_domain | enterprise-computing-strategy |
| methodology | industry-analysis |
| source_file | 1997 Microsoft_ The Joker of Enterprise IS Computing evp.pdf |
| license | CC-BY-4.0 |

## Abstract

Aberdeen Group Vice President John R. Logan argues that Microsoft's historical desktop orientation is fundamentally incompatible with enterprise IS computing requirements. While acknowledging Microsoft's desktop excellence, Logan contends that NT Server and BackOffice have yet to demonstrate mission-critical production capability, and that Microsoft lacks the planning, support, product compatibility, and management culture required by senior enterprise IS executives. The brief is intended to help business executives and IS professionals build consensus on where—and where not—to deploy Microsoft products beyond the desktop.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | high | Aberdeen VP-level strategic viewpoint (Volume 10/Number 20) challenging Microsoft's enterprise ambitions; part of Aberdeen's broader 1997 campaign questioning NT enterprise readiness alongside Kastner's 'Emperor Has No Clothes' study. Logan's VP credential and Aberdeen's reach made this influential. |
| Relevance | medium | The structural argument—that a company's dominant DNA from one computing era does not automatically transfer to another—remains applicable to technology platform transitions (e.g., consumer cloud providers moving to enterprise AI). |
| Prescience | medium | Logan's skepticism about Microsoft's enterprise IS commitment proved partially correct: Windows 2000 and subsequent releases gradually addressed many enterprise requirements, but Microsoft's core DNA remained desktop/developer-oriented. The premise that enterprises needed to carefully scope Microsoft deployments foreshadowed the hybrid IT architectures that became standard. |

## Data Tables

| Table | Rows | Description |
|-------|------|-------------|
| studies.csv | 1 | Study metadata and assessments |
| entities.csv | 3 | Organizations referenced |
| technologies.csv | 5 | Technologies discussed |
| observations.csv | 15 | Extracted analytical observations |
| codes.csv | 21 | Controlled vocabulary |

## Quick Load (Python)

```python
import pandas as pd
obs = pd.read_csv("data/observations.csv")
print(obs.groupby("observation_type").size())
```

## Validation

```bash
frictionless validate datapackage.json
```

## Citation

John R. Logan. (1997). *Microsoft: The Joker of Enterprise IS Computing*. Aberdeen Group Executive Viewpoint, Vol.10/No.20.
Archived: https://web.archive.org/web/19980131061319/http://www.aberdeen.com:80/research/abstract/97090178.htm
License: CC-BY-4.0
