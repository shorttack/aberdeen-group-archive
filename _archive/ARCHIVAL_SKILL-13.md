---
name: archival-ingest
description: >
  Batch-process historical research studies into structured, machine-readable
  archival datasets. Use when asked to archive studies, ingest research files,
  build a Frictionless Data Package, process files into metadata and Markdown,
  extract observations from studies, create structured datasets from research
  documents, or recurse a directory of study files. Handles PDF, Markdown, Word,
  and plain-text inputs. Produces five CSV tables (studies, entities, technologies,
  observations, codes), a datapackage.json descriptor, a schema_org.json discovery
  layer, a README.md, and a demo_analysis.py validation script for each study.
  Studies include document-level assessments: importance, relevance, and prescience
  ratings with rationales. Each study preserves the full original document text
  with appended Frictionless metadata and prescience assessment in source/original_text.md.
---

# Archival Ingest Skill

> **Purpose**: Read up to ten study files at a time from a directory, extract
> structured metadata and analytical observations, emit a complete Frictionless
> Data Package per study, then recurse through remaining files until the
> directory is fully processed.

---

## 1. Activation Triggers

Activate this skill when the user's request matches ANY of the following intents:

- "Archive these studies"
- "Ingest research files"
- "Process files into metadata and Markdown"
- "Build a Frictionless Data Package from my research"
- "Extract observations from these documents"
- "Recurse the directory and process all files"
- "Create structured datasets from my study files"
- "Batch-process my research library"

---

## 2. Environment & Tools Available

This skill runs inside Perplexity Computer's sandboxed execution environment.
You have access to:

| Capability | How to use it |
|---|---|
| **File system** | Read/write files via Python (`open()`, `os`, `pathlib`, `glob`) |
| **Python execution** | Full Python 3 with `csv`, `json`, `re`, `datetime`, `pathlib`, `hashlib`, `uuid` in stdlib. Use `pandas` if available. |
| **Web search** | Use `web_search` tool to verify entity outcomes, successor companies, technology lifecycle dates |
| **URL fetch** | Use `fetch_url` to pull reference material for cross-validation |
| **Notes** | Use `notes_write` / `notes_read` to persist state across recursion batches |

---

## 3. Input Expectations

The user will provide one of:

1. **A directory path** containing study files (PDF, .md, .txt, .docx)
2. **Individual file attachments** uploaded to the conversation
3. **A reference to files already in the sandbox** from a previous step

If the user provides a directory, discover all processable files:

```python
from pathlib import Path

SUPPORTED = {'.md', '.txt', '.pdf', '.docx', '.doc', '.rtf'}

def discover_files(root: str) -> list[Path]:
    """Recursively find all supported study files."""
    root = Path(root)
    files = []
    for ext in SUPPORTED:
        files.extend(root.rglob(f'*{ext}'))
    return sorted(files)
```

---

## 4. Batch Processing Protocol

### 4.1 Batch Size

Process files in batches of **up to 10 files per cycle**. This respects
context-window limits and ensures quality extraction.

### 4.2 Batch Loop

```
BATCH_SIZE = 10
all_files = discover_files(user_directory)
total = len(all_files)
processed = 0

while processed < total:
    batch = all_files[processed : processed + BATCH_SIZE]
    for file in batch:
        process_single_study(file)
    processed += len(batch)
    save_progress(processed, total)
    print(f"Processed {processed}/{total} files.")
```

### 4.3 Progress Persistence

After each batch, write a checkpoint file so processing can resume if
interrupted:

```python
import json
from datetime import datetime

def save_progress(processed_count, total_count, output_dir="output"):
    checkpoint = {
        "processed": processed_count,
        "total": total_count,
        "timestamp": datetime.utcnow().isoformat(),
        "status": "complete" if processed_count >= total_count else "in_progress"
    }
    with open(f"{output_dir}/_checkpoint.json", "w") as f:
        json.dump(checkpoint, f, indent=2)
```

---

## 5. Per-Study Processing Pipeline

For each study file, execute these steps **in order**:

### Step 1: Read and Parse the Source Document

```python
def read_study(filepath: Path) -> str:
    """Read file content. For PDF, extract text. For MD/TXT, read directly."""
    ext = filepath.suffix.lower()
    if ext in ('.md', '.txt'):
        return filepath.read_text(encoding='utf-8', errors='replace')
    elif ext == '.pdf':
        try:
            import fitz  # PyMuPDF
            doc = fitz.open(str(filepath))
            return '\n'.join(page.get_text() for page in doc)
        except ImportError:
            return f"[PDF extraction unavailable for {filepath.name}. Provide text version.]"
    elif ext in ('.docx', '.doc'):
        try:
            import docx
            doc = docx.Document(str(filepath))
            return '\n'.join(p.text for p in doc.paragraphs)
        except ImportError:
            return f"[DOCX extraction unavailable for {filepath.name}. Provide text version.]"
    else:
        return filepath.read_text(encoding='utf-8', errors='replace')
```

### Step 2: Generate Study ID

```python
import hashlib

def generate_study_id(filepath: Path) -> str:
    """Create a deterministic, short study ID from filename."""
    name = filepath.stem.lower().replace(' ', '-').replace('_', '-')
    short_hash = hashlib.md5(str(filepath).encode()).hexdigest()[:6]
    truncated = name[:40]
    return f"{truncated}-{short_hash}"
```

### Step 3: Extract Metadata -> `studies.csv`

Analyze the document text and extract:

| Field | Description | Example |
|---|---|---|
| `study_id` | Generated unique ID | `ie-andersen-expert-report-a1b2c3` |
| `title` | Full title of the study | `Expert Witness Report: IE v. Andersen Consulting` |
| `author` | Primary author(s) | `Peter S. Kastner` |
| `date` | Publication/creation date (ISO 8601) | `1999-06-01` |
| `type` | Study type | `expert-report`, `market-study`, `case-analysis`, `white-paper`, `benchmark` |
| `subject_domain` | Primary domain | `IT-litigation`, `PC-distribution`, `ERP-implementation` |
| `methodology` | Comma-separated methods | `industry-analysis, competitive-profiling, benchmarking, expert-opinion` |
| `source_file` | Original filename | `Kastner-Expert-Report-IE-v-Andersen.pdf` |
| `abstract` | 2-3 sentence summary | (AI-generated from document content) |
| `license` | Default to CC-BY-4.0 | `CC-BY-4.0` |
| `importance` | Historical significance at time of publication: `high`, `medium`, `low` | `high` |
| `importance_rationale` | 1-2 sentence justification for the importance rating | `First independent benchmark of AS/400 SAP R/3 performance; widely cited by IBM and SAP.` |
| `relevance` | Ongoing relevance to current practitioners, researchers, or AI systems: `high`, `medium`, `low` | `medium` |
| `relevance_rationale` | 1-2 sentence justification for the relevance rating | `ERP platform migration patterns remain applicable; specific hardware benchmarks are dated.` |
| `prescience` | Accuracy of forward-looking claims judged against actual outcomes: `high`, `medium`, `low`, `not-applicable` | `high` |
| `prescience_rationale` | 1-2 sentence justification for the prescience rating | `Predicted AS/400 longevity proved correct — platform still active as IBM i 30 years later.` |

**Extraction instructions for the AI:**

1. Look for title in the first 500 characters (headings, title pages).
2. Look for author names near the title or in signature blocks.
3. Identify dates from headers, footers, cover pages, or internal references.
4. Classify the study type based on document structure and language.
5. Generate abstract by summarizing the document's core argument in 2-3 sentences.
6. If metadata is ambiguous, flag it with `[REVIEW]` and proceed.

**Assessment instructions (importance / relevance / prescience):**

7. **Importance**: Evaluate the study's significance at the time it was published. Consider: Was it the first study of its kind? Did it address a critical industry question? Was the publisher (Aberdeen Group) influential in this domain? Was the study widely cited or referenced? Rate `high` if the study shaped industry decisions or filled a major knowledge gap; `medium` if it was a solid contribution within a crowded field; `low` if it was routine or narrowly scoped.
8. **Relevance**: Evaluate how useful the study remains today. Consider: Are the technologies, companies, or market dynamics still active? Do the analytical frameworks or methodologies transfer to current problems? Would a modern researcher, practitioner, or AI training pipeline gain value from this content? Rate `high` if substantially applicable today; `medium` if partially useful (e.g., methodology transfers but specifics are dated); `low` if primarily of historical/archival interest only.
9. **Prescience**: Evaluate the accuracy of the study's predictions and forward-looking assessments. Cross-reference `viability-prediction` observations against `actual-outcome` observations and web search results. Rate `high` if most predictions proved correct; `medium` if mixed; `low` if mostly wrong; `not-applicable` if the study made no forward-looking claims.
10. Write a concise rationale (1-2 sentences) for each rating. The rationale must reference specific evidence from the study content or verified outcomes.

### Step 4: Extract Entities -> `entities.csv`

Scan the document for organizations, companies, and institutions mentioned.

| Field | Description | Example |
|---|---|---|
| `entity_id` | Canonical lowercase hyphenated name | `intelligent-electronics` |
| `entity_name` | Display name | `Intelligent Electronics, Inc.` |
| `entity_type` | `company`, `firm`, `institution`, `agency`, `person` | `company` |
| `sector` | Industry sector | `PC-distribution` |
| `status` | Current status | `dissolved`, `active`, `merged`, `acquired`, `bankrupt` |
| `successor` | Successor entity if applicable | `GE -> Xerox` |
| `years_active` | Approximate years | `1982-1997` |
| `study_id` | FK to studies.csv | `ie-andersen-expert-report-a1b2c3` |
| `notes` | Additional context | `Exton, PA headquarters` |

**Extraction instructions:**

1. Identify every named organization in the document.
2. For each, determine type, sector, and role in the study.
3. Use `web_search` to verify current status and successor chains for key entities.
4. Deduplicate: if the same entity appears under multiple names (e.g., "Andersen Consulting" / "AC"), merge into one row with notes.

### Step 5: Extract Technologies -> `technologies.csv`

| Field | Description | Example |
|---|---|---|
| `tech_id` | Canonical lowercase hyphenated | `as400` |
| `tech_name` | Display name | `IBM AS/400` |
| `category` | `platform`, `application`, `protocol`, `language`, `framework` | `platform` |
| `vendor` | Primary vendor | `IBM` |
| `era` | Approximate era | `1988-2000` |
| `lifecycle_at_study` | Status when study was written | `mature`, `declining`, `emerging`, `obsolete` |
| `lifecycle_current` | Status now | `legacy-supported`, `obsolete`, `active` |
| `study_id` | FK to studies.csv | `ie-andersen-expert-report-a1b2c3` |
| `notes` | | `Renamed to iSeries, then IBM i` |

### Step 6: Extract Observations -> `observations.csv`

This is the **core analytical table**. Every factual claim, prediction,
benchmark result, or analytical judgment in the study becomes a row.

| Field | Description |
|---|---|
| `obs_id` | `{study_id}-OBS-{NNN}` |
| `study_id` | FK to studies.csv |
| `entity_id` | FK to entities.csv (nullable) |
| `tech_id` | FK to technologies.csv (nullable) |
| `observation_type` | See codes.csv: `strategy-classification`, `viability-prediction`, `actual-outcome`, `technology-assessment`, `benchmark-result`, `framework-factor`, `market-data`, `expert-opinion` |
| `year_observed` | Year the observation applies to |
| `metric_name` | What is being measured/claimed |
| `metric_value` | The value or classification |
| `confidence` | `high`, `medium`, `low`, `verified` |
| `methodology_code` | FK to codes.csv |
| `source_page` | Page/section reference in original document |
| `notes` | Additional context |

**Extraction instructions:**

1. Read the document systematically, section by section.
2. For every quantifiable claim (market share, revenue, growth rate, ranking), create a row.
3. For every qualitative judgment (strategy classification, viability prediction, technology assessment), create a row.
4. For every benchmark or comparison, create a row.
5. For framework components (e.g., a "six-factor analysis"), create one row per factor.
6. Cross-reference entity_id and tech_id with the tables created in Steps 4-5.
7. If a prediction was made, flag it as `viability-prediction`. Later (or via web search), add a separate `actual-outcome` row with `confidence: verified`.
8. Aim for 15-50 observations per study, depending on density.

### Step 7: Build Codes Table -> `codes.csv`

Define all controlled vocabulary used in the observations table.

| Field | Description |
|---|---|
| `code_id` | The code string used in observations.csv |
| `code_type` | `observation_type`, `methodology`, `confidence`, `lifecycle` |
| `label` | Human-readable label |
| `definition` | Clear definition of what this code means |

**Standard codes to always include:**

```csv
code_id,code_type,label,definition
strategy-classification,observation_type,Strategy Classification,"Categorization of an entity's business strategy"
viability-prediction,observation_type,Viability Prediction,"Expert prediction of entity's long-term survival"
actual-outcome,observation_type,Actual Outcome,"Verified historical outcome for an entity"
technology-assessment,observation_type,Technology Assessment,"Evaluation of a technology's maturity or fitness"
benchmark-result,observation_type,Benchmark Result,"Quantitative comparison against peers or standards"
framework-factor,observation_type,Framework Factor,"One component of a multi-factor analytical framework"
market-data,observation_type,Market Data,"Quantitative market statistic"
expert-opinion,observation_type,Expert Opinion,"Qualitative professional judgment"
industry-analysis,methodology,Industry Analysis,"Systematic analysis of industry structure and dynamics"
competitive-profiling,methodology,Competitive Profiling,"Detailed comparison of competing entities"
benchmarking,methodology,Benchmarking,"Comparison against industry standards or peers"
field-research,methodology,Field Research,"Primary data collection via interviews or surveys"
document-review,methodology,Document Review,"Analysis of existing documents and records"
statistical-analysis,methodology,Statistical Analysis,"Quantitative data analysis with statistical methods"
high,confidence,High Confidence,"Strong evidentiary basis; multiple corroborating sources"
medium,confidence,Medium Confidence,"Reasonable basis but limited corroboration"
low,confidence,Low Confidence,"Directional judgment with limited evidence"
verified,confidence,Verified,"Confirmed by subsequent events or independent sources"
```

Add study-specific codes as needed (e.g., specialized strategy types,
technology categories unique to a particular domain).

### Step 8: Generate `datapackage.json`

```python
import json
from datetime import date

def build_datapackage(study_meta: dict, output_dir: str):
    """Generate Frictionless Data Package descriptor."""
    pkg = {
        "name": study_meta["study_id"],
        "title": study_meta["title"],
        "description": study_meta["abstract"],
        "version": "1.0.0",
        "created": date.today().isoformat(),
        "licenses": [{"name": "CC-BY-4.0", "path": "https://creativecommons.org/licenses/by/4.0/"}],
        "contributors": [{"title": study_meta["author"], "role": "author"}],
        "resources": [
            {
                "name": "studies",
                "path": "data/studies.csv",
                "schema": {
                    "fields": [
                        {"name": "study_id", "type": "string"},
                        {"name": "title", "type": "string"},
                        {"name": "author", "type": "string"},
                        {"name": "date", "type": "date"},
                        {"name": "type", "type": "string"},
                        {"name": "subject_domain", "type": "string"},
                        {"name": "methodology", "type": "string"},
                        {"name": "source_file", "type": "string"},
                        {"name": "abstract", "type": "string"},
                        {"name": "license", "type": "string"},
                        {"name": "importance", "type": "string"},
                        {"name": "importance_rationale", "type": "string"},
                        {"name": "relevance", "type": "string"},
                        {"name": "relevance_rationale", "type": "string"},
                        {"name": "prescience", "type": "string"},
                        {"name": "prescience_rationale", "type": "string"}
                    ]
                }
            },
            {
                "name": "entities",
                "path": "data/entities.csv",
                "schema": {
                    "fields": [
                        {"name": "entity_id", "type": "string"},
                        {"name": "entity_name", "type": "string"},
                        {"name": "entity_type", "type": "string"},
                        {"name": "sector", "type": "string"},
                        {"name": "status", "type": "string"},
                        {"name": "successor", "type": "string"},
                        {"name": "years_active", "type": "string"},
                        {"name": "study_id", "type": "string"},
                        {"name": "notes", "type": "string"}
                    ]
                }
            },
            {
                "name": "technologies",
                "path": "data/technologies.csv",
                "schema": {
                    "fields": [
                        {"name": "tech_id", "type": "string"},
                        {"name": "tech_name", "type": "string"},
                        {"name": "category", "type": "string"},
                        {"name": "vendor", "type": "string"},
                        {"name": "era", "type": "string"},
                        {"name": "lifecycle_at_study", "type": "string"},
                        {"name": "lifecycle_current", "type": "string"},
                        {"name": "study_id", "type": "string"},
                        {"name": "notes", "type": "string"}
                    ]
                }
            },
            {
                "name": "observations",
                "path": "data/observations.csv",
                "schema": {
                    "fields": [
                        {"name": "obs_id", "type": "string"},
                        {"name": "study_id", "type": "string"},
                        {"name": "entity_id", "type": "string"},
                        {"name": "tech_id", "type": "string"},
                        {"name": "observation_type", "type": "string"},
                        {"name": "year_observed", "type": "year"},
                        {"name": "metric_name", "type": "string"},
                        {"name": "metric_value", "type": "string"},
                        {"name": "confidence", "type": "string"},
                        {"name": "methodology_code", "type": "string"},
                        {"name": "source_page", "type": "string"},
                        {"name": "notes", "type": "string"}
                    ]
                }
            },
            {
                "name": "codes",
                "path": "data/codes.csv",
                "schema": {
                    "fields": [
                        {"name": "code_id", "type": "string"},
                        {"name": "code_type", "type": "string"},
                        {"name": "label", "type": "string"},
                        {"name": "definition", "type": "string"}
                    ]
                }
            }
        ]
    }
    with open(f"{output_dir}/datapackage.json", "w") as f:
        json.dump(pkg, f, indent=2)
```

### Step 9: Generate `schema_org.json`

```python
def build_schema_org(study_meta: dict, output_dir: str):
    """Generate Schema.org/Dataset JSON-LD for web discovery."""
    schema = {
        "@context": "https://schema.org",
        "@type": "Dataset",
        "name": study_meta["title"],
        "description": study_meta["abstract"],
        "creator": {"@type": "Person", "name": study_meta["author"]},
        "datePublished": study_meta["date"],
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "distribution": [
            {
                "@type": "DataDownload",
                "encodingFormat": "text/csv",
                "contentUrl": "data/observations.csv"
            }
        ],
        "keywords": study_meta.get("keywords", []),
        "temporalCoverage": study_meta.get("temporal_coverage", ""),
        "variableMeasured": [
            "strategy-classification",
            "viability-prediction",
            "technology-assessment",
            "benchmark-result"
        ]
    }
    os.makedirs(f"{output_dir}/schema", exist_ok=True)
    with open(f"{output_dir}/schema/schema_org.json", "w") as f:
        json.dump(schema, f, indent=2)
```

### Step 10: Generate `README.md`

Create a human-readable guide for the dataset including:

- Study metadata table (author, date, type, domain, license)
- Abstract
- Data tables summary with row counts
- Python load example using pandas
- Frictionless validation command
- Citation block with DOI placeholder
- Methodology summary

### Step 11: Generate `demo_analysis.py`

Create a standalone Python script that:

1. Loads all five CSV files
2. Prints study summary statistics
3. Validates referential integrity (every entity_id and tech_id in observations exists in their respective tables)
4. Checks that all observation_type codes exist in codes.csv
5. If viability predictions exist, cross-references them against actual outcomes and computes prediction accuracy
6. Reports results to stdout

Use `os.path.dirname(os.path.abspath(__file__))` for portable path resolution.

### Step 12: Generate `source/original_text.md`

Preserve the full original document text with appended structured metadata.
This file serves as the archival record: the complete study as authored,
followed by all machine-generated metadata for context.

**Structure of `source/original_text.md`:**

```markdown
# {Study Title}

> Archived from: {Wayback Machine URL or source_file}
> Original publication date: {date}
> Author: {author}

---

## Original Document Text

{Full extracted text from the source PDF/document, preserving paragraph breaks.
 Clean up OCR artifacts and formatting noise, but do not alter the author's words.
 Preserve section headings, bullet lists, and table structures as markdown.
 If the source has tables, render them as markdown tables.
 If text extraction is poor (scanned PDF), note: "[OCR quality: low — some text may be garbled]"}

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | {study_id} |
| title | {title} |
| author | {author} |
| date | {date} |
| type | {type} |
| subject_domain | {subject_domain} |
| methodology | {methodology} |
| source_file | {source_file} |
| license | {license} |

### Abstract

{abstract}

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | {importance} | {importance_rationale} |
| **Relevance** | {relevance} | {relevance_rationale} |
| **Prescience** | {prescience} | {prescience_rationale} |

### Prescience Detail

{For each viability-prediction observation in observations.csv, list:}

**Prediction {N}:** {metric_name}
- **Claimed:** {metric_value}
- **Year:** {year_observed}
- **Confidence at time:** {confidence}

**Actual Outcome {N}:** {corresponding actual-outcome metric_name}
- **Result:** {metric_value}
- **Confidence:** {confidence}
- **Notes:** {notes}

{If no predictions exist, write: "This study did not make forward-looking claims."}

### Entities Referenced ({count})

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
{One row per entity from entities.csv}

### Technologies Referenced ({count})

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|--------------------|
{One row per technology from technologies.csv}

### Observation Summary

- Total observations: {count}
- By type: {breakdown}
```

**Generation instructions:**

1. Extract the full text from the source document (PDF, DOCX, or text file).
2. Clean up extraction artifacts (repeated headers/footers, page numbers, Wayback Machine banners) but preserve the author's prose, structure, and data verbatim.
3. Convert to well-formatted Markdown: use `#` headings for section breaks, markdown tables for tabular data, `>` for block quotes.
4. Append the Frictionless metadata section using data from `studies.csv`, `entities.csv`, `technologies.csv`, and `observations.csv`.
5. The prescience section must pair each `viability-prediction` observation with its corresponding `actual-outcome` observation. Match by entity_id + tech_id or by topic.
6. Save to `source/original_text.md` within the study directory.

---

## 6. Output Directory Structure

For each study, create the following directory tree under `output/`:

```
output/
  {study_id}/
    README.md
    datapackage.json
    data/
      studies.csv
      entities.csv
      technologies.csv
      observations.csv
      codes.csv
    schema/
      schema_org.json
    source/
      original_text.md
    scripts/
      demo_analysis.py
```

---

## 7. Recursion & Multi-Study Orchestration

### 7.1 Directory Recursion

After processing each batch of 10 files, report progress and continue:

```
Processing batch 1/4 (files 1-10 of 37)...
  > study-alpha-a1b2c3: 23 observations, 8 entities, 5 technologies
  > study-beta-d4e5f6: 31 observations, 12 entities, 3 technologies
  ...
  > Batch 1 complete. Checkpoint saved.

Processing batch 2/4 (files 11-20 of 37)...
```

### 7.2 Cross-Study Accumulation

After all batches are complete, generate a **master index**:

- `_master_studies.csv` — All studies in one table
- `_master_entities.csv` — Deduplicated entities across all studies, with `study_id` showing which studies reference each entity
- `_master_technologies.csv` — Deduplicated technologies across all studies

This enables cross-study queries like: "Which entities appear in more than one study?" or "What technologies span multiple eras?"

### 7.3 Quality Checks

After each study, run automated validation:

1. **Referential integrity**: Every `entity_id` in observations.csv exists in entities.csv
2. **Code coverage**: Every `observation_type` and `methodology_code` in observations.csv exists in codes.csv
3. **Completeness**: studies.csv has no empty required fields
4. **Consistency**: Date formats are ISO 8601, IDs are lowercase-hyphenated

Flag any failures with `[REVIEW]` and continue processing.

---

## 8. User Interaction Protocol

### 8.1 Before Processing

1. Confirm the directory path or files to process
2. Show the file discovery count: "Found {N} study files in {path}. Processing in batches of 10."
3. Ask: "Shall I proceed, or would you like to exclude any files?"

### 8.2 During Processing

For each study, provide a brief status line:

```
Processing: Kastner-Expert-Report-IE-v-Andersen.pdf
  -> Study ID: ie-andersen-expert-report-a1b2c3
  -> Extracted: 19 entities, 8 technologies, 29 observations
  -> Output: output/ie-andersen-expert-report-a1b2c3/
```

### 8.3 After Each Batch

Report cumulative progress and any items flagged for review:

```
Batch 1 complete: 10/37 files processed
  -> 247 total observations extracted
  -> 3 items flagged [REVIEW] (see _review_log.csv)
  -> Continuing to batch 2...
```

### 8.4 After All Batches

Provide a final summary:

```
All 37 files processed.
  -> 37 study packages created in output/
  -> Master index: output/_master_studies.csv (37 rows)
  -> Master entities: output/_master_entities.csv (142 unique entities)
  -> 12 items flagged for manual review (output/_review_log.csv)
  -> Validation: 35/37 passed integrity checks
```

---

## 9. Error Handling

| Error | Action |
|---|---|
| File unreadable (corrupt PDF, encoding error) | Log to `_review_log.csv`, skip file, continue |
| Ambiguous metadata (no clear title/author) | Use filename as title, mark `[REVIEW]`, continue |
| PDF extraction unavailable | Request user provide text version, or skip with log |
| Entity status unknown | Mark as `status: unknown`, flag for web_search verification |
| Duplicate study detected (same content, different filename) | Log duplicate, process only first instance |

---

## 10. Web Search Integration

Use `web_search` strategically during entity extraction:

1. **Verify company status**: "Is [Company Name] still active or dissolved?"
2. **Find successor entities**: "[Company Name] acquired by" or "[Company Name] merged with"
3. **Confirm technology lifecycle**: "[Technology Name] end of life" or "[Technology Name] current status"
4. **Cross-validate predictions**: If the study made predictions, search for actual outcomes

Limit to **3 web searches per study** to maintain processing speed.
Batch web searches across entities when possible.

---

## 11. Example: Expected Output for IE v. Andersen Study

Given the IE v. Andersen expert report as input, the skill should produce:

- `studies.csv`: 1 row (the Kastner report, June 1999; includes importance/relevance/prescience ratings with rationales)
- `entities.csv`: ~19 rows (IE, Andersen, Ingram Micro, Tech Data, MicroAge, Inacom, ComputerLand, GE, Xerox, etc.)
- `technologies.csv`: ~8 rows (AS/400, HP 3000, SAP R/3, OS/2, Windows 95, etc.)
- `observations.csv`: ~29 rows (strategy classifications, viability predictions, actual outcomes, technology assessments, QA benchmarks, six-factor framework)
- `codes.csv`: ~18 rows (all observation types, methodology codes, confidence levels)
- `datapackage.json`: Complete Frictionless descriptor
- `schema/schema_org.json`: Google Dataset Search-compatible metadata
- `README.md`: Human-readable guide with citation block
- `scripts/demo_analysis.py`: Runnable validation showing 100% prediction accuracy

---

## 12. Publication Pipeline (Post-Processing)

After all studies are processed, guide the user through:

1. **GitHub**: Push each study package as a directory in a single repository
2. **Zenodo**: Archive the GitHub repo to get a DOI per version
3. **Hugging Face**: Upload as a dataset for ML discoverability
4. **Internet Archive**: Backup deposit for permanent preservation

Provide the exact commands/steps for each platform when the user is ready.
