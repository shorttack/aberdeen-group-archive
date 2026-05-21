# Digital Equipment Corporation Longitudinal Study, 1985-Present

This directory is a v19-style archival-ingest package for a synthesized longitudinal study of Digital Equipment Corporation and its successor chain.

## Contents

- `data/studies.csv`: one study metadata row.
- `data/entities.csv`: 18 relevant entities.
- `data/technologies.csv`: 17 relevant technologies.
- `data/observations.csv`: 79 analytical, evidentiary, attribution, and verification observations.
- `data/codes.csv`: method and observation-type code definitions.
- `source/_raw_text.txt`: narrative source text used for this synthetic study.
- `source/original_text.md`: narrative plus metadata appendix.
- `schema/schema_org.json`: discovery metadata.
- `datapackage.json`: Frictionless Data Package descriptor.
- `scripts/demo_analysis.py`: validation and summary script.

## Verification Method Coverage

- `cross-reference`: 26
- `ingest-extraction`: 42
- `outcome-linkage`: 5
- `web-source`: 6

## Observation Types

- `actual-outcome`: 11
- `attribution-audit`: 6
- `coverage-analysis`: 8
- `evidence-example`: 10
- `market-data`: 2
- `methodology-note`: 1
- `strategy-classification`: 4
- `technology-lifecycle`: 17
- `thread-density`: 10
- `topic-insight`: 10

## Attribution Rule

This package preserves a strict attribution distinction. Do not credit all Aberdeen Group institutional observations to Peter S. Kastner. Read the `attribution_bucket` references in observation notes and the explicit attribution-audit rows.
