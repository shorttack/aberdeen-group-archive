# Kastner Aberdeen Wiki — User Guide

> A read-optimized research environment built from the master CSVs of the
> `shorttack/aberdeen-group-archive` repo. This guide is the cookbook for
> getting full value out of the wiki: DuckDB queries, Obsidian Dataview,
> semantic search, hybrid LLM workflows, and longitudinal analysis recipes.

**Companion files in this repo:**
- `AGENTS.md` — LLM primer (file map, naming conventions)
- `chat-starter.md` — pre-warmed prompts for AI assistants
- `README.md` — human-facing repo intro
- `Makefile` — common commands

---

## Contents

1. [What's in the wiki](#1-whats-in-the-wiki)
2. [Five ways to query](#2-five-ways-to-query)
3. [Setup (one-time)](#3-setup-one-time)
4. [Cookbook: DuckDB queries](#4-cookbook-duckdb-queries)
5. [Cookbook: Obsidian Dataview](#5-cookbook-obsidian-dataview)
6. [Cookbook: semantic search (bge-m3)](#6-cookbook-semantic-search-bge-m3)
7. [Cookbook: hybrid LLM research workflows](#7-cookbook-hybrid-llm-research-workflows)
8. [Cookbook: longitudinal & thesis workflows](#8-cookbook-longitudinal--thesis-workflows)
9. [Cookbook: citation discovery](#9-cookbook-citation-discovery)
10. [Cookbook: code & methodology dictionary](#10-cookbook-code--methodology-dictionary)
11. [Performance tips](#11-performance-tips)
12. [Schema reference](#12-schema-reference)
13. [Known limitations (v1.5)](#13-known-limitations-v15)

---

## 1. What's in the wiki

The wiki is **derived** from 1,434 archived studies spanning 1995-2024 from
the Aberdeen Group research archive. Phase 3 emits one Markdown page per
logical record:

| Surface | Count | Notes |
|---|---:|---|
| Studies | 1,434 | 109 LLM-enriched (Claude Sonnet 4.6); 1,325 templated |
| Entities | 3,207 | 200 LLM-enriched (local qwen3.5:27b); 3,007 templated |
| Technologies | 4,312 | 150 LLM-enriched (local qwen3.5:27b); 4,162 templated |
| Codes | 1,292 | Methodology, technology-category, and 32 other dictionary types |
| Collections | 6 | High-level groupings (memoir, AI-responses, transcripts, ...) |
| Decades | 8 | 1990s-2020s rollups (auto-derived from study `date`) |
| Bases (.base files) | 5 | Obsidian Bases queries — open in vault sidebar |
| _index.md | 1 | Vault home page |

**Prescience scoring (Pass C)** — 2,723 observations across 308 studies have
been numerically scored 0-5 for forward-looking accuracy:

| Score | Meaning | Count |
|---:|---|---:|
| 5 | Highly prescient — predicted future precisely | 719 |
| 4 | Substantially prescient — direction correct, details close | 966 |
| 3 | Partially prescient | 40 |
| 2 | Weak prescience | 78 |
| 1 | Minimal prescience | 74 |
| 0 | Not prescient / not applicable | 846 |

**Data layer**: Parquet files in `data/`, pre-built DuckDB at
`db/kastner.duckdb` with 27 named views (full catalog in §4).

**Semantic index**: `data/embeddings.parquet` — 1024-dim bge-m3 embeddings
for every emitted page.

---

## 2. Five ways to query

| Approach | Best for | Speed | Setup |
|---|---|---|---|
| **DuckDB SQL** | Aggregations, joins, longitudinal slices | Sub-second on full archive | `pip install duckdb` |
| **Obsidian Dataview** | Browsing while reading | Live, ~50ms | Install Obsidian + Dataview plugin |
| **Obsidian Bases** | Saved filtered views | Live | Obsidian core (no plugin) |
| **Semantic search** | Conceptual queries ("what did Aberdeen say about AI agents?") | ~1s after warmup | `pip install sentence-transformers` or ollama bge-m3 |
| **Hybrid LLM** | Synthesis questions over filtered subset | 10-60s | DuckDB + local Ollama or cloud LLM |

Each cookbook section below covers one approach with copy-paste examples.

---

## 3. Setup (one-time)

```bash
# Clone the wiki
git clone https://github.com/shorttack/kastner-aberdeen-wiki.git
cd kastner-aberdeen-wiki

# Verify the build is intact
make verify
# or: python3 scripts/verify.py

# Python deps for SQL examples
pip3 install duckdb pandas pyarrow

# Optional: semantic search via local ollama (recommended)
ollama pull bge-m3

# Optional: hybrid LLM workflows
ollama pull qwen3.5:27b-mlx   # or any 7B+ model
```

**Opening in Obsidian:**
1. Install [Obsidian](https://obsidian.md/) (free)
2. Open Vault → Open Folder → select `kastner-aberdeen-wiki/wiki/`
3. Install Dataview plugin: Settings → Community Plugins → Browse → "Dataview"
4. (Optional) Enable Bases: Settings → Core Plugins → Bases

---

## 4. Cookbook: DuckDB queries

The pre-built database at `db/kastner.duckdb` has 27 views. All examples
below are copy-paste runnable.

### View catalog

```python
import duckdb
con = duckdb.connect("db/kastner.duckdb", read_only=True)
print(con.execute("SELECT view_name FROM duckdb_views() WHERE schema_name='main' ORDER BY view_name").df())
```

The 27 views:

| View | Use |
|---|---|
| `v_studies` | Full studies master, with derived `pub_year`, `prescience_max/mean/obs_count` |
| `v_entities` | Full entities master, with `occurrence_count` |
| `v_technologies` | Full technologies master, with `occurrence_count` |
| `v_observations` | Full observations + joined prescience scores |
| `v_codes` | Code dictionary (methodology, tech category, 34 types) |
| `v_entity_studies`, `v_tech_studies` | Join tables (entity↔study, tech↔study) |
| `v_known_entities`, `v_known_technologies` | Canonical-name lookup tables |
| `v_collection_stats`, `v_collection_overview` | Per-study and aggregated collection stats |
| `v_prescience_raw` | Raw 2,723-row Pass C scores |
| `v_observations_with_prescience` | Obs filtered to those with numeric scores |
| `v_studies_with_prescience` | 308 studies that have any scored obs |
| `v_top_prescient_studies` | Studies with `prescience_max = 5` |
| `v_studies_with_high_prescience` | Studies with `prescience_max >= 4` (the tier-1 LLM set) |
| `v_high_holistic_prescience` | Studies where Pete tagged `prescience='high'` in CSV |
| `v_holistic_prescience_distribution` | enum distribution (high/medium/low/n-a) |
| `v_prescience_by_decade` | Decade breakdown of high-prescience study counts |
| `v_low_confidence_prescience` | 230 obs flagged confidence=1 (cloud sweep queue) |
| `v_studies_by_decade` | Decade counts |
| `v_entities_with_observation_count` | Entities sorted by occurrence |
| `v_technologies_by_lifecycle` | Techs with `lifecycle_at_study`, `lifecycle_current` |
| `v_observations_by_year` | Obs counts per `year_observed` |
| `v_codes_by_type` | Code type histogram |
| `v_methodology_codes` | 408 methodology codes |
| `v_technology_category_codes` | 8 technology-category codes |

### Example 1 — All studies with maximum prescience

```python
import duckdb
con = duckdb.connect("db/kastner.duckdb", read_only=True)

df = con.execute("""
    SELECT study_id, title, author, pub_year, prescience_mean
    FROM v_top_prescient_studies
    ORDER BY pub_year
""").df()
print(f"{len(df)} studies with at least one score=5 observation")
print(df.head(20))
```

### Example 2 — Most-frequently-mentioned entities (top 50)

```python
df = con.execute("""
    SELECT entity_id, entity_name, entity_type, sector, occurrence_count
    FROM v_entities_with_observation_count
    WHERE occurrence_count > 0
    ORDER BY occurrence_count DESC
    LIMIT 50
""").df()
print(df)
```

### Example 3 — Decade-by-decade prescience trend

```python
df = con.execute("""
    SELECT * FROM v_prescience_by_decade
""").df()
print(df)
# Columns: decade, high_prescience_studies, studies_scored, studies_total
```

### Example 4 — Technologies by lifecycle phase

```python
df = con.execute("""
    SELECT lifecycle_current, COUNT(*) AS n
    FROM v_technologies
    WHERE lifecycle_current IS NOT NULL AND lifecycle_current != ''
    GROUP BY lifecycle_current
    ORDER BY n DESC
""").df()
print(df)
```

### Example 5 — Entity co-occurrence (which entities show up together in studies?)

```python
df = con.execute("""
    SELECT
        a.entity_id AS entity_a,
        b.entity_id AS entity_b,
        COUNT(*) AS shared_studies
    FROM v_entity_studies a
    JOIN v_entity_studies b ON a.study_id = b.study_id AND a.entity_id < b.entity_id
    GROUP BY a.entity_id, b.entity_id
    HAVING shared_studies >= 3
    ORDER BY shared_studies DESC
    LIMIT 50
""").df()
print(df)
```

### Example 6 — Technology co-occurrence

```python
df = con.execute("""
    SELECT
        a.tech_id AS tech_a,
        b.tech_id AS tech_b,
        COUNT(*) AS shared_studies
    FROM v_tech_studies a
    JOIN v_tech_studies b ON a.study_id = b.study_id AND a.tech_id < b.tech_id
    GROUP BY a.tech_id, b.tech_id
    HAVING shared_studies >= 3
    ORDER BY shared_studies DESC
    LIMIT 50
""").df()
print(df)
```

### Example 7 — Most-prescient observations (the gold)

```python
df = con.execute("""
    SELECT obs_id, study_id, entity_id, tech_id, year_observed,
           metric_value, prescience_score, prescience_rationale
    FROM v_observations
    WHERE prescience_score = 5
    ORDER BY year_observed
    LIMIT 100
""").df()
for _, r in df.iterrows():
    print(f"[{r['year_observed']}] {r['study_id']} — {r['metric_value'][:100]}")
    print(f"  → {r['prescience_rationale'][:150]}\n")
```

### Example 8 — Studies authored by Peter Kastner (or any author)

```python
df = con.execute("""
    SELECT study_id, title, pub_year, type, prescience_max
    FROM v_studies
    WHERE LOWER(author) LIKE '%kastner%'
    ORDER BY pub_year
""").df()
print(f"{len(df)} Kastner-authored studies")
print(df)
```

### Example 9 — Studies citing a specific entity (e.g., Intel)

```python
df = con.execute("""
    SELECT s.study_id, s.title, s.pub_year, s.author
    FROM v_entity_studies es
    JOIN v_studies s ON es.study_id = s.study_id
    WHERE es.entity_id = 'intel'
    ORDER BY s.pub_year
""").df()
print(df)
```

### Example 10 — Studies citing a specific technology

```python
df = con.execute("""
    SELECT s.study_id, s.title, s.pub_year, s.author, s.prescience_max
    FROM v_tech_studies ts
    JOIN v_studies s ON ts.study_id = s.study_id
    WHERE ts.tech_id = 'bluetooth'
    ORDER BY s.pub_year
""").df()
print(df)
```

### Example 11 — Methodology codes referenced by observations

```python
df = con.execute("""
    SELECT o.methodology_code, c.label, COUNT(*) AS obs_count
    FROM v_observations o
    LEFT JOIN v_codes c ON o.methodology_code = c.code_id AND c.code_type = 'methodology'
    WHERE o.methodology_code IS NOT NULL AND o.methodology_code != ''
    GROUP BY o.methodology_code, c.label
    ORDER BY obs_count DESC
    LIMIT 30
""").df()
print(df)
```

### Example 12 — Holistic study-level prescience distribution

```python
df = con.execute("""
    SELECT * FROM v_holistic_prescience_distribution
""").df()
print(df)
```

### Example 13 — Find all high-prescience studies of a specific type

```python
df = con.execute("""
    SELECT study_id, title, author, pub_year, prescience_max, prescience_mean
    FROM v_studies
    WHERE type = 'aberdeen-report'
      AND prescience_max >= 4
    ORDER BY pub_year
""").df()
print(df)
```

### Example 14 — Observations from a specific year (longitudinal slice)

```python
df = con.execute("""
    SELECT obs_id, study_id, metric_value, prescience_score, prescience_rationale
    FROM v_observations
    WHERE year_observed = '2005'
      AND prescience_score >= 4
    ORDER BY prescience_score DESC, study_id
""").df()
print(df)
```

### Example 15 — Entity lifecycle status histogram

```python
df = con.execute("""
    SELECT status, COUNT(*) AS n_entities
    FROM v_entities
    WHERE status IS NOT NULL AND status != ''
    GROUP BY status
    ORDER BY n_entities DESC
""").df()
print(df)
```

### Example 16 — Multi-dimensional drill: prescient observations by tech category by decade

```python
df = con.execute("""
    WITH obs_with_tech AS (
        SELECT o.obs_id, o.tech_id, o.prescience_score, o.year_observed, t.category
        FROM v_observations o
        LEFT JOIN v_technologies t ON o.tech_id = t.tech_id
        WHERE o.prescience_score >= 4
          AND o.year_observed IS NOT NULL AND o.year_observed != ''
    )
    SELECT
        CAST(CAST(year_observed AS INTEGER) / 10 * 10 AS INTEGER) || 's' AS decade,
        category,
        COUNT(*) AS n_obs
    FROM obs_with_tech
    WHERE category IS NOT NULL AND category != ''
    GROUP BY decade, category
    HAVING n_obs >= 5
    ORDER BY decade, n_obs DESC
""").df()
print(df)
```

---

## 5. Cookbook: Obsidian Dataview

These queries live inside `.md` pages or in dedicated dashboard notes.
Open Obsidian, create a new note, and paste a query block.

### Example 17 — All tier-1 entities, ranked by occurrence

````markdown
```dataview
TABLE entity_type, sector, occurrence_count, prescience_max
FROM "wiki/entities"
WHERE tier = 1
SORT occurrence_count DESC
LIMIT 50
```
````

### Example 18 — Studies with prescience_max = 5

````markdown
```dataview
TABLE author, pub_year, prescience_mean, prescience_obs_count
FROM "wiki/studies"
WHERE prescience_max = 5
SORT pub_year ASC
```
````

### Example 19 — All Kastner-authored studies

````markdown
```dataview
TABLE pub_year, type, prescience_max, file.link AS Page
FROM "wiki/studies"
WHERE contains(lower(author), "kastner")
SORT pub_year ASC
```
````

### Example 20 — Entities in a specific sector (e.g., networking)

````markdown
```dataview
TABLE status, years_active, occurrence_count
FROM "wiki/entities"
WHERE contains(lower(sector), "networking")
SORT occurrence_count DESC
```
````

### Example 21 — Technologies in their current `mainstream` phase

````markdown
```dataview
LIST FROM "wiki/technologies"
WHERE lifecycle_current = "mainstream"
SORT occurrence_count DESC
```
````

### Example 22 — Dashboard: archive at a glance

Create `wiki/_dashboard.md` with multiple blocks:

````markdown
## Studies by decade

```dataview
TABLE length(rows) AS Count
FROM "wiki/studies"
WHERE pub_year
GROUP BY (floor(pub_year / 10) * 10) + "s" AS Decade
SORT Decade ASC
```

## Top 25 entities

```dataview
TABLE entity_type, sector, occurrence_count
FROM "wiki/entities"
WHERE occurrence_count > 0
SORT occurrence_count DESC
LIMIT 25
```

## Tier-1 studies (LLM-summarized)

```dataview
LIST FROM "wiki/studies"
WHERE tier = 1
SORT pub_year ASC
```
````

### Example 23 — Backlinks: find all studies that link to an entity

In any entity page (e.g., `wiki/entities/intel.md`), append:

````markdown
## Mentioned in

```dataview
LIST FROM [[]]
WHERE contains(file.outlinks, this.file.link)
SORT pub_year ASC
```
````

(Obsidian also gives you backlinks in the right sidebar automatically.)

---

## 6. Cookbook: semantic search (bge-m3)

The wiki ships with `data/embeddings.parquet` — 1024-dim bge-m3 embeddings
for every page. Use it for conceptual queries.

### Setup

```bash
ollama pull bge-m3
pip3 install duckdb pandas numpy requests
```

### Example 24 — Semantic search helper

Save as `scripts/semantic_search.py` (the build emits a stub; replace with this):

```python
#!/usr/bin/env python3
"""semantic_search.py — query bge-m3 embeddings index.

The embeddings.parquet schema is (path, slug, embedding, dim). page_type is
derived from the path segment (entities, studies, technologies, codes, etc.).
"""
import sys
import json
import requests
import duckdb
import numpy as np

OLLAMA_URL = "http://localhost:11434/api/embeddings"
MODEL = "bge-m3"

def embed(text: str) -> np.ndarray:
    r = requests.post(OLLAMA_URL, json={"model": MODEL, "prompt": text}, timeout=60)
    r.raise_for_status()
    return np.array(r.json()["embedding"], dtype=np.float32)

def _derive_type(path: str) -> str:
    # e.g. 'wiki/wiki/entities/intel.md' -> 'entity'
    parts = path.split("/")
    folder = parts[-2] if len(parts) >= 2 else ""
    return {
        "entities": "entity",
        "studies": "study",
        "technologies": "technology",
        "codes": "code",
        "collections": "collection",
        "decades": "decade",
        "themes": "theme",
        "bases": "base",
    }.get(folder, folder or "unknown")

def search(query: str, k: int = 10, page_type: str | None = None):
    q = embed(query)
    q /= np.linalg.norm(q) + 1e-9
    df = duckdb.sql("SELECT path, slug, embedding, dim FROM 'data/embeddings.parquet' WHERE dim > 0").df()
    df["page_type"] = df["path"].apply(_derive_type)
    if page_type:
        df = df[df["page_type"] == page_type].reset_index(drop=True)
    vecs = np.stack(df["embedding"].apply(np.array).values).astype(np.float32)
    vecs /= (np.linalg.norm(vecs, axis=1, keepdims=True) + 1e-9)
    sims = vecs @ q
    top = np.argsort(-sims)[:k]
    out = df.iloc[top][["slug", "page_type", "path"]].copy()
    out["score"] = sims[top]
    return out

if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "AI agents acting autonomously"
    print(search(q, k=15).to_string(index=False))
```

### Example 25 — Run a semantic query

```bash
python3 scripts/semantic_search.py "rural broadband economics"
# Top hits from all page types

python3 scripts/semantic_search.py "ATM versus Ethernet backbone"
# Surfaces 1995-1998 networking studies
```

### Example 26 — Semantic query restricted to studies only

Modify the call:

```python
from semantic_search import search
print(search("agentic AI", k=20, page_type="study").to_string(index=False))
```

### Example 27 — Find the page closest to another page (analogy queries)

```python
import duckdb, numpy as np
df = duckdb.sql("SELECT path, slug, embedding, dim FROM 'data/embeddings.parquet' WHERE dim > 0").df()
vecs = np.stack(df["embedding"].apply(np.array).values).astype(np.float32)
vecs /= (np.linalg.norm(vecs, axis=1, keepdims=True) + 1e-9)

# Find pages similar to a specific entity page
target = "intel"  # or any slug
idx = df[df.slug == target].index[0]
sims = vecs @ vecs[idx]
top = np.argsort(-sims)[1:11]  # skip self
print(df.iloc[top][["slug", "path"]])
```

---

## 7. Cookbook: hybrid LLM research workflows

Combine DuckDB filtering + local Ollama for synthesis. Cloud LLM (Claude
Sonnet via `pplx ask`) for cross-page reasoning.

### Setup

```bash
ollama pull qwen3.5:27b-mlx     # Or any 7B+ instruct model
# Pre-warm so first query is fast:
ollama run qwen3.5:27b-mlx "ready" --keepalive 30m
```

### Example 28 — Local LLM summarizes a filtered DuckDB result

```python
import duckdb
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3.5:27b-mlx"

def ask_local(prompt: str, temperature: float = 0.3) -> str:
    r = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": temperature, "num_ctx": 8192, "num_predict": 800},
    }, timeout=300)
    return r.json()["response"]

con = duckdb.connect("db/kastner.duckdb", read_only=True)
df = con.execute("""
    SELECT metric_value, prescience_rationale, year_observed
    FROM v_observations
    WHERE prescience_score = 5
      AND tech_id = 'bluetooth'
    ORDER BY year_observed
""").df()

context = "\n".join(f"[{r.year_observed}] {r.metric_value}\n  Rationale: {r.prescience_rationale}"
                    for _, r in df.iterrows())

prompt = f"""Below are Aberdeen Group observations about Bluetooth, all scored prescience=5
(highly accurate forecasts). Synthesize a 200-word retrospective on what
Aberdeen got right about Bluetooth's trajectory from 1999-2024.

OBSERVATIONS:
{context}
"""
print(ask_local(prompt))
```

### Example 29 — Cloud LLM (Claude Sonnet) for cross-study synthesis

If you have Perplexity CLI installed:

```bash
# Build a context bundle from DuckDB
python3 - <<'PY'
import duckdb
con = duckdb.connect("db/kastner.duckdb", read_only=True)
df = con.execute("""
    SELECT study_id, title, author, pub_year,
           study_prescience_rationale
    FROM v_high_holistic_prescience
    ORDER BY pub_year
""").df()
with open("/tmp/context.txt", "w") as f:
    for _, r in df.iterrows():
        f.write(f"[{r.pub_year}] {r.title} ({r.author})\n")
        f.write(f"  Rationale: {r.study_prescience_rationale}\n\n")
PY

# Send to Claude
pplx ask --model claude_sonnet_4_6 --file /tmp/context.txt \
  "Identify the 3 most consistent themes across these high-prescience Aberdeen studies. For each, name the theme, the timespan it covers, and 2-3 representative studies."
```

### Example 30 — RAG over the vault using semantic search + LLM

```python
from semantic_search import search   # from §6
import requests, json

def rag(question: str, k: int = 6) -> str:
    hits = search(question, k=k)
    # Load page content for each hit — path is relative to wiki repo root
    chunks = []
    for _, h in hits.iterrows():
        try:
            with open(h["path"]) as f:
                chunks.append(f"=== {h['slug']} ({h['page_type']}) ===\n{f.read()[:2000]}")
        except FileNotFoundError:
            continue
    context = "\n\n".join(chunks)
    prompt = f"""Answer using ONLY the Aberdeen Group archive material below.
Cite the page title in [[wikilink]] format when referencing.

QUESTION: {question}

CONTEXT:
{context}
"""
    r = requests.post("http://localhost:11434/api/generate", json={
        "model": "qwen3.5:27b-mlx", "prompt": prompt, "stream": False,
        "options": {"temperature": 0.2, "num_ctx": 32768, "num_predict": 1200},
    }, timeout=600)
    return r.json()["response"]

print(rag("What did Aberdeen predict about VoIP adoption in the early 2000s?"))
```

---

## 8. Cookbook: longitudinal & thesis workflows

These compose the primitives above into research-grade workflows.

### Example 31 — Vendor lifecycle: track an entity across decades

```python
import duckdb
con = duckdb.connect("db/kastner.duckdb", read_only=True)

entity_id = "3com"
df = con.execute(f"""
    SELECT s.pub_year, s.study_id, s.title,
           o.metric_value, o.prescience_score
    FROM v_entity_studies es
    JOIN v_studies s ON es.study_id = s.study_id
    LEFT JOIN v_observations o ON o.study_id = s.study_id AND o.entity_id = es.entity_id
    WHERE es.entity_id = '{entity_id}'
    ORDER BY s.pub_year, o.prescience_score DESC NULLS LAST
""").df()

# Group by year for a timeline
for year, sub in df.groupby("pub_year"):
    print(f"\n=== {year} ({sub.study_id.nunique()} studies) ===")
    for _, r in sub.head(3).iterrows():
        score = f" [P={int(r.prescience_score)}]" if r.prescience_score == r.prescience_score else ""
        print(f"  • {r.metric_value[:120] if r.metric_value else '(no obs)'}{score}")
```

### Example 32 — Technology cohort: track a tech category over time

```python
df = con.execute("""
    SELECT s.pub_year, t.tech_id, t.tech_name, t.lifecycle_at_study,
           COUNT(o.obs_id) AS obs_count,
           AVG(o.prescience_score) AS avg_prescience
    FROM v_technologies t
    JOIN v_tech_studies ts ON t.tech_id = ts.tech_id
    JOIN v_studies s ON ts.study_id = s.study_id
    LEFT JOIN v_observations o ON o.study_id = s.study_id AND o.tech_id = t.tech_id
    WHERE t.category = 'storage'
    GROUP BY s.pub_year, t.tech_id, t.tech_name, t.lifecycle_at_study
    ORDER BY s.pub_year, obs_count DESC
""").df()
print(df.head(40))
```

### Example 33 — Build a "what Aberdeen got right" report

```python
import duckdb
con = duckdb.connect("db/kastner.duckdb", read_only=True)

# Pull all score=5 observations grouped by entity
df = con.execute("""
    SELECT e.entity_name, COUNT(*) AS hit_count,
           MIN(s.pub_year) AS first_year,
           MAX(s.pub_year) AS last_year,
           STRING_AGG(DISTINCT o.metric_value, ' || ') AS sample_predictions
    FROM v_observations o
    JOIN v_entities e ON o.entity_id = e.entity_id
    JOIN v_studies s ON o.study_id = s.study_id
    WHERE o.prescience_score = 5
    GROUP BY e.entity_name
    HAVING hit_count >= 3
    ORDER BY hit_count DESC
""").df()

with open("/tmp/aberdeen_got_right.md", "w") as f:
    f.write("# What Aberdeen got right — multi-prescient entities\n\n")
    for _, r in df.iterrows():
        f.write(f"## {r.entity_name} ({r.hit_count} score-5 predictions, "
                f"{r.first_year}-{r.last_year})\n\n")
        for prediction in (r.sample_predictions or "").split(" || ")[:5]:
            f.write(f"- {prediction[:200]}\n")
        f.write("\n")

print("Wrote /tmp/aberdeen_got_right.md")
```

### Example 34 — Methodology evolution: how did Aberdeen's analytical methods change?

```python
df = con.execute("""
    WITH study_methods AS (
        SELECT s.pub_year, s.study_id, o.methodology_code, c.label
        FROM v_studies s
        JOIN v_observations o ON s.study_id = o.study_id
        LEFT JOIN v_codes c ON o.methodology_code = c.code_id AND c.code_type = 'methodology'
        WHERE o.methodology_code IS NOT NULL AND o.methodology_code != ''
          AND s.pub_year IS NOT NULL
    )
    SELECT
        CAST(pub_year / 10 * 10 AS INTEGER) || 's' AS decade,
        label,
        COUNT(DISTINCT study_id) AS n_studies
    FROM study_methods
    GROUP BY decade, label
    HAVING n_studies >= 3
    ORDER BY decade, n_studies DESC
""").df()
print(df)
```

---

## 9. Cookbook: citation discovery

### Example 35 — Studies that cite both Entity A and Tech B

```python
df = con.execute("""
    SELECT s.study_id, s.title, s.pub_year, s.author
    FROM v_studies s
    WHERE s.study_id IN (
        SELECT study_id FROM v_entity_studies WHERE entity_id = 'cisco'
    )
    AND s.study_id IN (
        SELECT study_id FROM v_tech_studies WHERE tech_id = 'voip'
    )
    ORDER BY s.pub_year
""").df()
print(df)
```

### Example 36 — Find pages that link to a specific entity (Obsidian-side)

In any Obsidian note:

````markdown
## Pages mentioning Intel

```dataview
LIST FROM [[intel]]
SORT file.name ASC
```
````

Or use the Obsidian Graph view (Cmd-G) and search for the entity slug.

### Example 37 — Reverse-lookup an observation to its source page

```python
obs_id = "obs-2005-abc-001"  # any obs_id
df = con.execute(f"""
    SELECT o.obs_id, o.study_id, o.entity_id, o.tech_id, o.metric_value,
           s.title, s.author, s.pub_year
    FROM v_observations o
    JOIN v_studies s ON o.study_id = s.study_id
    WHERE o.obs_id = '{obs_id}'
""").df()
print(df.iloc[0])

# Then in Obsidian, open:
#   wiki/studies/study-{study_id-slug}.md
```

---

## 10. Cookbook: code & methodology dictionary

The `_master_codes.csv` is the controlled vocabulary used across the archive.
1,292 codes across 34 types.

### Example 38 — Browse all code types

```python
df = con.execute("SELECT * FROM v_codes_by_type").df()
print(df)
```

### Example 39 — All methodology codes (408 entries)

```python
df = con.execute("""
    SELECT code_id, label, definition
    FROM v_methodology_codes
    LIMIT 50
""").df()
print(df)
```

### Example 40 — Find observations using a specific methodology

```python
code_id = "methodology-survey-quantitative"  # example
df = con.execute(f"""
    SELECT o.obs_id, o.study_id, o.metric_value, o.year_observed,
           s.title, s.author, s.pub_year
    FROM v_observations o
    JOIN v_studies s ON o.study_id = s.study_id
    WHERE o.methodology_code = '{code_id}'
    ORDER BY s.pub_year DESC
    LIMIT 30
""").df()
print(df)
```

### Example 41 — Technology categories (8 codes, the high-level taxonomy)

```python
df = con.execute("SELECT * FROM v_technology_category_codes").df()
print(df)
```

---

## 11. Performance tips

- **`db/kastner.duckdb` is the fast path** — open with `read_only=True` for concurrent shells.
- **Embeddings file is ~40MB** — load once, hold in memory if running many queries.
- **bge-m3 first query is slow** (~3-5s warmup). Keep ollama running with `--keepalive 30m`.
- **Cloud LLM calls cost time** — batch context and ask ONE large question rather than many small ones.
- **For Obsidian** — Dataview is fine for any single page; for archive-wide queries use DuckDB.
- **Parquet is your friend** — `read_parquet('data/studies.parquet')` works without the duckdb file.

```python
# Parquet-only access (no duckdb file required)
import duckdb
df = duckdb.sql("SELECT * FROM 'data/studies.parquet' WHERE pub_year >= 2010").df()
```

---

## 12. Schema reference

### `_master_studies.csv` / `v_studies` / `data/studies.parquet`

| Column | Type | Notes |
|---|---|---|
| `study_id` | str | Primary key |
| `title` | str | |
| `author` | str | |
| `date` | str | ISO YYYY-MM-DD or partial |
| `pub_year` | int | DERIVED from `date` in Phase 1 |
| `type` | str | Collection type |
| `subject_domain` | str | |
| `methodology` | str | |
| `source_file` | str | |
| `abstract` | str | |
| `license` | str | |
| `importance` | str | high/medium/low/n-a |
| `relevance` | str | high/medium/low/n-a |
| `study_prescience_enum` | str | DERIVED from `prescience` column |
| `study_prescience_rationale` | str | |
| `prescience_max` | float | DERIVED from Pass C scores |
| `prescience_mean` | float | DERIVED |
| `prescience_obs_count` | int | DERIVED |

### `_master_entities.csv` / `v_entities` / `data/entities.parquet`

| Column | Type | Notes |
|---|---|---|
| `entity_id` | str | Primary key |
| `entity_name` | str | Display name |
| `entity_type` | str | company/institution/individual/standards-body/etc |
| `sector` | str | |
| `status` | str | active/dissolved/acquired/etc |
| `successor` | str | Free-form chain |
| `years_active` | str | "1979-2010" or "1990-present" |
| `notes` | str | |
| `occurrence_count` | int | DERIVED — join count from v_entity_studies |

### `_master_technologies.csv` / `v_technologies` / `data/technologies.parquet`

| Column | Type | Notes |
|---|---|---|
| `tech_id` | str | Primary key |
| `tech_name` | str | |
| `category` | str | |
| `vendor` | str | |
| `era` | str | |
| `lifecycle_at_study` | str | emerging/mainstream/declining/etc as observed at study time |
| `lifecycle_current` | str | as of last archive update |
| `notes` | str | |
| `occurrence_count` | int | DERIVED |

### `_master_observations.csv` / `v_observations`

| Column | Type | Notes |
|---|---|---|
| `obs_id` | str | Primary key |
| `study_id` | str | |
| `entity_id` | str | nullable |
| `tech_id` | str | nullable |
| `observation_type` | str | |
| `year_observed` | str | nullable |
| `metric_name`, `metric_value` | str | |
| `confidence` | str | Source confidence (NOT prescience confidence) |
| `verification_method` | str | |
| `methodology_code` | str | → `v_codes` |
| `source_page` | str | |
| `notes` | str | |
| `collection` | str | |
| `thread_tag` | str | |
| `section` | str | |
| `legacy_obs_id` | str | Pre-normalizer IDs (audit) |
| `prescience_score` | float | DERIVED — joined from Pass C, 0-5 |
| `prescience_confidence` | int | DERIVED — 1-3 |
| `prescience_rationale` | str | DERIVED |

### Page frontmatter (Obsidian YAML)

All pages have these fields:

```yaml
title: "Display Name"
slug: "primary-key"
page_type: "entity"  # or study, technology, code, collection
tags: ["type/entity", "entity-type/company"]
tier: 1              # or 2 — controls Dataview filtering
source_csv: "_master_entities.csv"
```

Entity pages additionally carry: `entity_id`, `entity_type`, `sector`,
`status`, `successor`, `years_active`, `occurrence_count`,
`prescience_max`, `prescience_mean`, `prescience_obs_count`.

Study pages additionally carry: `study_id`, `author`, `date`, `pub_year`,
`type`, `subject_domain`, `methodology`, `source_file`, `license`,
`importance`, `relevance`, `study_prescience_enum`, `prescience_max`,
`prescience_mean`, `prescience_obs_count`.

Tech pages additionally carry: `tech_id`, `category`, `vendor`, `era`,
`lifecycle_at_study`, `lifecycle_current`, `occurrence_count`,
`prescience_max`, `prescience_mean`, `prescience_obs_count`.

---

## 13. Known limitations (v1.5)

These are documented in `v1.5_phase1_anomalies_v1.md` in the source archive.

1. **350/1,434 studies (24%) lack `pub_year`** — date column was empty or
   non-parseable. Affects decade-slice queries.
2. **1,890/3,207 entities (59%) have `occurrence_count=0`** — present in
   the entities master but not referenced in any observation. Often historical
   catalog entries.
3. **1,323/4,312 technologies (31%) have `occurrence_count=0`** — same root.
4. **Prescience coverage is partial** — only Bucket A+B (308 studies, 2,723
   obs) scored in Pass C. Bucket C+D coming in v1.6.
5. **6 collections, not the originally-planned 14** — `collection` vs `theme`
   conflation in master CSV; theme rollup pages are deferred to v1.6.
6. **Volume-1 chapter pages not yet emitted** — requires memoir source text
   integration. Deferred to v1.6.
7. **230 obs flagged confidence=1** — Pass C scored these with low confidence;
   they're queued for cloud-LLM sweep before being trusted. See
   `v_low_confidence_prescience`.
8. **1 orphan prescience score** — `obs_id` in Pass C output that doesn't
   exist in `_master_observations.csv`. Cosmetic; ignore.

---

## Quick reference card

| I want to... | Tool | Example # |
|---|---|---:|
| Find the most-prescient studies | DuckDB `v_top_prescient_studies` | 1 |
| Track an entity over time | DuckDB join through `v_entity_studies` | 31 |
| Browse while reading | Obsidian Dataview | 17-22 |
| Search by concept | bge-m3 semantic search | 25 |
| Synthesize across studies | hybrid DuckDB + local LLM | 28-30 |
| Find citations of an entity | DuckDB or Obsidian Graph | 9, 36 |
| Build a vendor history | DuckDB longitudinal slice | 31 |
| Understand methodology vocabulary | DuckDB `v_codes` | 38-41 |
| Get the actual numbers right | Always read `v1.5_phase1_anomalies_v1.md` first | §13 |

---

_Last updated: 2026-05-26 (v1.5 build)._
_Source archive: [shorttack/aberdeen-group-archive](https://github.com/shorttack/aberdeen-group-archive)._
_Wiki repo: [shorttack/kastner-aberdeen-wiki](https://github.com/shorttack/kastner-aberdeen-wiki)._
