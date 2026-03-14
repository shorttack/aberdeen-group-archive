# Aberdeen Group Research Archive

Private archive of Aberdeen Group analyst research studies (1995–1996), structured as [Frictionless Data Packages](https://frictionlessdata.io/).

## Structure

```
aberdeen-group-archive/
├── _master_studies.csv            # Index of all studies
├── _master_entities.csv           # 184 unique entities across studies
├── _master_technologies.csv       # 271 unique technologies across studies
├── aberdeen-group-inc/            # Company files / about Aberdeen Group
├── other-authors/                 # Studies by authors other than Peter S. Kastner
│   ├── aberdeen-1995-3com-lanplex-2500/
│   ├── aberdeen-1995-commercial-messaging/
│   ├── ... (14 studies)
│   └── aberdeen-1996-risc-unix-market/
└── kastner-author/                # Studies by Peter S. Kastner (author/co-author)
```

## Per-Study Structure

Each study is a self-contained Frictionless Data Package:

```
study-slug/
├── datapackage.json               # Frictionless descriptor
├── README.md                      # Human-readable documentation
├── data/
│   ├── studies.csv                # Study metadata (1 row)
│   ├── entities.csv               # Organizations with M&A status
│   ├── technologies.csv           # Technologies with lifecycle stage
│   ├── observations.csv           # Structured analytical observations
│   └── codes.csv                  # Controlled vocabulary
├── schema/
│   └── schema_org.json            # Schema.org Dataset metadata
└── scripts/
    └── demo_analysis.py           # Validation & analysis script
```

## Archive Stats

| Metric | Count |
|--------|-------|
| Studies | 14 |
| Total observations | 689 |
| Unique entities | 184 |
| Unique technologies | 271 |
| Validation errors | 0 |

## Ingestion

Studies processed using `ARCHIVAL_SKILL-11.md` — an archival-ingest skill for Perplexity Computer that reads PDF sources, extracts structured data, verifies entity statuses via web search, and produces validated Frictionless Data Packages.

## License

Private repository. All original Aberdeen Group content is proprietary.
