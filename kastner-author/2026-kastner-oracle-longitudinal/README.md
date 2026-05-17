# Oracle Corporation Across Four Decades of the Kastner Archive: RDBMS Dominance, Office Futures, Applications Conquest, and the Cloud Pivot

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner (assembled with Perplexity Computer using archival-ingest v16) |
| Date | 2026-05-17 |
| Type | topic-analysis |
| Domain | computing-industry-history |
| License | CC-BY-4.0 |

## Abstract

A longitudinal archive study of Oracle Corporation across four decades of the Kastner IT Research Archive. Oracle is the second most-referenced company in the archive — 327 observations across 73 distinct studies spanning 1988 to 2026, with 215 Oracle-vendor technology rows. The study decomposes Oracle coverage into eleven thematic threads: RDBMS market leadership, TPC benchmark contests, Oracle Office/InterOffice (the first document-summarization product — a harbinger of AI two decades ahead of its time), Developer/2000 and development tools, Oracle Applications/E-Business Suite, the PeopleSoft hostile acquisition, Network Computing Architecture, Oracle8/8i/9i/10g database evolution, Larry Ellison leadership and competitive style, the Sun Microsystems acquisition, and the cloud pivot and OCI buildout. Headline findings: Oracle InterOffice (1995) offered automated document summarization — the earliest AI-adjacent feature documented in the archive; the PeopleSoft acquisition (2003–2004) was the defining hostile-takeover of the enterprise software era; Oracle's core RDBMS franchise survived every predicted displacement (object-relational, NoSQL, cloud-native) and remains dominant in 2026. This is the third longitudinal single-entity study in the archive, following the Intel and IBM builder templates.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 18 |
| technologies.csv | 41 |
| observations.csv | 91 |
| codes.csv | 32 |

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

Peter S. Kastner (assembled with Perplexity Computer using archival-ingest v16) (2026). Oracle Corporation Across Four Decades of the Kastner Archive: RDBMS Dominance, Office Futures, Applications Conquest, and the Cloud Pivot.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

archive-mining,longitudinal-single-entity,prediction-vs-outcome-scorecard,thematic-thread-decomposition,wiki-driven-replication
