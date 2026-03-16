# Availability of Client/Server WMS in 1994

> Frictionless Data Package — Archival Ingest Skill v13

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | `ie-appendix-jones-wms-memo-2e5d6c` |
| **Title** | Availability of Client/Server WMS in 1994 |
| **Author** | Dr. Katherine Jones |
| **Date** | 1999-06-07 |
| **Type** | Expert Report |
| **Domain** | Warehouse Management Systems |
| **Source File** | `IE-Appendix-Jones-WMS-Memo.txt` |
| **License** | CC-BY-4.0 |

## Abstract

Aberdeen Group ERP Research memo examining the availability of client/server warehouse management software (WMS) packages in the US marketplace in mid-1994. Concludes that no commercially available WMS was truly client/server-based at that time, with the first instance being Manhattan Associates PkMS in 1995.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Provides expert testimony establishing the state of WMS technology in 1994, relevant to the IE v. Andersen litigation timeline. |
| **Relevance** | low | WMS technology has evolved dramatically since 1994; the specific technology landscape described is purely historical. |
| **Prescience** | high | Correctly identified Manhattan Associates as a WMS pioneer and accurately characterized the pre-client/server state of warehouse management technology in 1994. |

## Data Package Contents

| File | Description | Rows |
|------|-------------|------|
| `data/studies.csv` | Study metadata | 1 |
| `data/entities.csv` | Organizations and persons referenced | 7 |
| `data/technologies.csv` | Technologies analyzed | 6 |
| `data/observations.csv` | Analytical observations | 15 |
| `data/codes.csv` | Controlled vocabulary definitions | 43 |
| `datapackage.json` | Frictionless Data Package descriptor | — |
| `schema/schema_org.json` | Schema.org JSON-LD for discovery | — |
| `source/original_text.md` | Full original document text | — |
| `scripts/demo_analysis.py` | Validation and analysis script | — |

## Key Findings

1. **No client/server WMS existed in 1994**: Despite the underlying technology being available, no commercially available WMS used true client/server architecture.
2. **Manhattan Associates PkMS (1995)**: First commercially released client/server WMS.
3. **Catalyst delayed entry**: Used Windows on RF handhelds in 1993-94 but did not ship true client/server until 1996.
4. **AS/400 was host-terminal**: AS/400-based WMS systems (JBA, CA BOSS) all used host-dumb terminal architecture.
5. **Aberdeen's definition**: Client/server means the user-facing portion runs locally while business logic runs on another computer.

## Methodology

- Document review and field research by Dr. Katherine Jones, Aberdeen Group ERP Research
- Systematic survey of WMS vendors active in 1994
- Part of Appendix III of the IE v. Andersen expert report by Peter S. Kastner

## Usage

```python
import pandas as pd

observations = pd.read_csv('data/observations.csv')
entities = pd.read_csv('data/entities.csv')
technologies = pd.read_csv('data/technologies.csv')

# Filter by observation type
tech_assessments = observations[observations['observation_type'] == 'technology-assessment']
print(f"Technology assessments: {len(tech_assessments)}")
```

## Validation

```bash
python scripts/demo_analysis.py
```

## Citation

```
Jones, Katherine. "Availability of Client/Server WMS in 1994." Memo to Peter Kastner,
Aberdeen Group ERP Research, June 7, 1999. Appendix III of Report of Peter S. Kastner,
In re: Intelligent Electronics, Inc. v. Andersen Consulting LLP.
```
