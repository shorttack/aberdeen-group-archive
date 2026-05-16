# Kastner's Core Arguments and Framework: A Wiki-Driven Synthesis from the Aberdeen-Group-Archive

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner (assembled with Perplexity Computer using archival-ingest v18) |
| Date | 2026-05-16 |
| Type | topic-analysis |
| Domain | research-methodology |
| License | CC-BY-4.0 |

## Abstract

A wiki-driven framework study extracting twelve core arguments that recur across Peter S. Kastner's documented career (1969-2026) and binding each argument to a queryable proof cluster drawn from the 19,382-row master observations table of the Kastner IT Research Archive. The framework is the one Kastner himself articulates in Chapter 10 of the 2026 memoir (Seven Patterns That Recur) extended with five derived arguments covering reliability marketing, category creation, analyst methodology, content marketing, and the compute-judgment inversion. Each argument carries a filter spec against _master_observations.csv that returns the supporting rows, named exemplars, counter-evidence, and a confidence histogram. The study is designed to become a living wiki hub: arguments link out to proof studies via Obsidian wikilinks, and any reader can re-execute the filters to audit population claims at row-level granularity. This makes the framework empirically self-defending: criticism must engage with specific rows, not assertions. Total population: 1,606 supporting observations, 1,410 at confidence partially-verified or better (87.8%), 6 refuted observations (0.37%), spanning the 1960s-2020s.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 21 |
| technologies.csv | 18 |
| observations.csv | 148 |
| codes.csv | 28 |

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

Peter S. Kastner (assembled with Perplexity Computer using archival-ingest v18) (2026). Kastner's Core Arguments and Framework: A Wiki-Driven Synthesis from the Aberdeen-Group-Archive.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

archive-mining,observation-cluster-attribution,framework-synthesis,wiki-driven-replication
