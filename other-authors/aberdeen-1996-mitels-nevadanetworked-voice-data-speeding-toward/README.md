# Mitel's NeVaDa (Networked Voice and Data) – Speeding Toward Convergence

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | `aberdeen-1996-mitels-nevadanetworked-voice-data-speeding-toward` |
| **Author** | Aberdeen Group |
| **Date** | 1996-04-02 |
| **Type** | market-study |
| **Domain** | telecommunications-CTI |
| **License** | CC-BY-4.0 |
| **Source File** | 1996 Mitel NeVaDa Networked Voice Data speeding toward.pdf |

## Abstract

Aberdeen Group profiles Mitel Corporation's NeVaDa (Networked Voice and Data) platform, announced April 2, 1996, as a strategic move to transform Mitel's SX-2000 PBX into an integrated voice-data-video server on a broadband ATM/SONET enterprise backbone. The study documents the IT industry's growing demand for voice-data convergence, evaluates NeVaDa's modular collapsed-backbone topology with Madge Networks LAN switching, and assesses Mitel's competitive position and strategic risks in the emerging CTI market. Aberdeen concludes NeVaDa is a logical step toward convergence but notes Mitel must move quickly, secure ATM technology, and build credibility in the data networking community.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Documented an early enterprise voice-data convergence architecture at a critical juncture, when IT and telecom worlds were just beginning to merge; Mitel's PBX-to-call-server evolution path anticipated UCaaS by a decade, though DEC/Intel/Microsoft partnerships were not yet sufficient to make Mitel a household name in IT. |
| **Relevance** | medium | The architectural vision — converging voice, data, and video over a single enterprise backbone — directly predicts modern UCaaS, SD-WAN, and WebRTC paradigms. The analytical framework for evaluating PBX-to-IP migration remains applicable to ongoing legacy telephony modernization challenges. |
| **Prescience** | medium | Aberdeen correctly identified that voice-data convergence would succeed and that IT culture would ultimately define the model, but overestimated Mitel's ability to lead the space; Mitel went through multiple ownership changes and narrowly avoided extinction before becoming a significant Unified Communications vendor by the 2010s. |

## Data Tables

| Table | Rows | Description |
|-------|------|-------------|
| studies.csv | 1 | Study-level metadata with assessments |
| entities.csv | 7 | Organizations referenced in the study |
| technologies.csv | 7 | Technologies referenced in the study |
| observations.csv | 22 | Extracted analytical observations |
| codes.csv | 18 | Controlled vocabulary definitions |

### Observations by Type

| Type | Count |
|------|-------|
| actual-outcome | 3 |
| expert-opinion | 2 |
| framework-factor | 6 |
| market-data | 3 |
| strategy-classification | 2 |
| technology-assessment | 4 |
| viability-prediction | 2 |

## Quick Start

```python
import pandas as pd, os
base = os.path.dirname(os.path.abspath(__file__))
observations = pd.read_csv(os.path.join(base, "data/observations.csv"))
print(observations.groupby("observation_type").size())
```

## Validation

```bash
frictionless validate datapackage.json
```

## Citation

> Aberdeen Group. (1996, April 2). *Mitel's NeVaDa (Networked Voice and Data) – Speeding Toward Convergence*. Aberdeen Group, Inc., Boston, Massachusetts.
> Archived: https://web.archive.org/web/19970112011929/http://www.aberdeen.com:80/secure/profiles/mitel/mitel.htm
> Dataset DOI: [pending Zenodo deposit]

## Methodology

industry-analysis, competitive-profiling, field-research
