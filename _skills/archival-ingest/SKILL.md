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
  layer, a README.md, and a demo_analysis.py validation script per study.
  Includes importance, relevance, and prescience ratings. v16 adds five Kastner
  collection types: video transcripts, memoirs, employer records, AI responses,
  and technology topic deep-dives. v17 adds mandatory CSV Write Validation Gate
  preventing base64, column-shift, and invalid-rating defects. Optimized with
  bundled assembler module, entity reuse cache, and incremental web verification
  cache.
metadata:
  version: '17'
  author: Peter S. Kastner
  repository: github.com/shorttack/aberdeen-group-archive
---

## Archival Ingest Skill v17

> **Purpose**: Read up to ten study files at a time from a directory, extract
> structured metadata and analytical observations, emit a complete Frictionless
> Data Package per study, then recurse through remaining files until the
> directory is fully processed.
>
> **Architecture**: Three-phase pipeline optimized for credit efficiency.
> Phase 1 (AI) extracts metadata and observations. Phase 2 (scripted) assembles
> all derivative files via `scripts/assembler.py` at zero credit cost. Phase 3
> (deferred web) verifies entities and predictions in a single batch pass with
> incremental caching across sessions.

---

### 1. Activation Triggers

Activate this skill when the user's request matches ANY of the following intents:

- "Archive these studies"
- "Ingest research files"
- "Process files into metadata and Markdown"
- "Build a Frictionless Data Package from my research"
- "Extract observations from these documents"
- "Recurse the directory and process all files"
- "Create structured datasets from my study files"
- "Batch-process my research library"
- "Archive this transcript"
- "Ingest memoirs / commentary / anecdotes"
- "Process employer records for [company name]"
- "Archive AI responses"
- "Process technology topic files"

---

### 2. Environment & Tools Available

| Capability | How to use it |
|---|---|
| **File system** | Read/write files via Python (`open()`, `os`, `pathlib`, `glob`) |
| **Python execution** | Full Python 3 stdlib. Use `pandas` if available. |
| **Bundled assembler** | `python scripts/assembler.py <command>` — handles all Phase 2 and Phase 3 operations. See Section 5B. |
| **Web search** | Use `web_search` only in Phase 3 (deferred batch verification). Never during Phase 1. |
| **URL fetch** | Use `fetch_url` for reference material if needed |

---

### 3. Input Expectations

The user will provide one of:

1. **A directory path** containing study files (PDF, .md, .txt, .docx)
2. **Individual file attachments** uploaded to the conversation
3. **A reference to files already in the sandbox** from a previous step

If the user provides a directory, discover all processable files:

```python
from pathlib import Path
SUPPORTED = {'.md', '.txt', '.pdf', '.docx', '.doc', '.rtf'}

def discover_files(root: str) -> list[Path]:
    root = Path(root)
    files = []
    for ext in SUPPORTED:
        files.extend(root.rglob(f'*{ext}'))
    return sorted(files)
```

---

### 4. Three-Phase Batch Processing Protocol

#### 4.1 Batch Size

Process files in batches of **up to 10 files per cycle**.

#### 4.2 Initialization

Before processing the first batch, initialize the caches:

```bash
python scripts/assembler.py cache-init output/
python scripts/assembler.py web-cache-init output/
```

This creates (or loads existing) `_known_entities.csv`, `_known_technologies.csv`,
and `_web_cache.json` in the output directory. On subsequent runs, previously
identified entities and technologies are available for reuse.

#### 4.3 Batch Loop

```
BATCH_SIZE = 10
all_files = discover_files(user_directory)
total = len(all_files)
processed = 0

while processed < total:
    batch = all_files[processed : processed + BATCH_SIZE]
    batch_dirs = []
    for file in batch:
        # Phase 1: AI extraction (credits consumed)
        # → Before extracting, check the entity/tech cache for known items
        # → Write studies.csv, entities.csv, technologies.csv, observations.csv
        # → Save raw cleaned text to source/_raw_text.txt
        study_dir = phase1_extract(file)
        batch_dirs.append(study_dir)
        # CSV Validation Gate (Section 16 — MANDATORY before Phase 2)
        validate_study_csvs(study_dir)  # Fixes in-place or halts
        # Phase 2: Script assembly (zero credits)
        run: python scripts/assembler.py assemble {study_dir}
        # Update reuse cache with this study's entities/technologies
        run: python scripts/assembler.py cache-update output/ {study_dir}
    # Batch quality checks (zero credits)
    run: python scripts/assembler.py validate {batch_dirs...}
    processed += len(batch)
    save_progress(processed, total)
```

#### 4.4 Entity/Technology Reuse (Cross-Study Cache)

Before starting Phase 1 extraction for each study, query the reuse cache:

```bash
python scripts/assembler.py cache-lookup output/ --entities ibm,wang-laboratories,prime-computer
```

This returns known metadata (status, successor, lifecycle) for entities already
classified in prior studies. **Pass these known entities as context to the AI
during Phase 1 extraction** with this instruction:

> "The following entities have already been classified in prior studies.
> Reuse their entity_ids and metadata. Only extract new entities not in this list."

This reduces AI extraction work by ~15-20% for later batches in a corpus.

After Phase 1, update the cache:

```bash
python scripts/assembler.py cache-update output/ {study_dir}
```

#### 4.5 Progress Persistence

After each batch, write a checkpoint so processing can resume if interrupted.
The assembler does NOT handle checkpoints — use the same pattern as v14/v15.

---

### 5. Per-Study Processing Pipeline (Phase 1 — AI-Intensive)

For each study file, execute Steps 1-6 **in order**. These are the only steps
that consume credits. Steps 7-12 are handled by the assembler module.

#### Step 1: Read and Parse the Source Document

Read the file content. For PDF, extract text via PyMuPDF. For MD/TXT, read
directly. For DOCX, extract via python-docx.

**After extraction, save the cleaned raw text to `{study_dir}/source/_raw_text.txt`**
so the assembler can use it in Phase 2 without AI re-generation.

#### Step 2: Generate Study ID

```python
import hashlib
def generate_study_id(filepath: Path) -> str:
    name = filepath.stem.lower().replace(' ', '-').replace('_', '-')
    short_hash = hashlib.md5(str(filepath).encode()).hexdigest()[:6]
    return f"{name[:40]}-{short_hash}"
```

#### Step 3: Extract Metadata -> `studies.csv`

Analyze the document text and extract:

| Field | Description | Example |
|---|---|---|
| `study_id` | Generated unique ID | `ie-andersen-expert-report-a1b2c3` |
| `title` | Full title of the study | `Expert Witness Report: IE v. Andersen Consulting` |
| `author` | Primary author(s) | `Peter S. Kastner` |
| `date` | Publication/creation date (ISO 8601) | `1999-06-01` |
| `type` | Study type | `expert-report`, `market-study`, `case-analysis`, `white-paper`, `benchmark`, `transcript`, `memoir`, `employer-record`, `ai-response`, `topic-analysis` |
| `subject_domain` | Primary domain | `IT-litigation`, `PC-distribution`, `ERP-implementation` |
| `methodology` | Comma-separated methods | `industry-analysis, competitive-profiling, benchmarking, expert-opinion` |
| `source_file` | Original filename | `Kastner-Expert-Report-IE-v-Andersen.pdf` |
| `abstract` | 2-3 sentence summary | (AI-generated from document content) |
| `license` | Default to CC-BY-4.0 | `CC-BY-4.0` |
| `importance` | Historical significance: `high`, `medium`, `low` | `high` |
| `importance_rationale` | 1-2 sentence justification | `First independent benchmark of AS/400 SAP R/3 performance.` |
| `relevance` | Ongoing relevance: `high`, `medium`, `low` | `medium` |
| `relevance_rationale` | 1-2 sentence justification | `ERP migration patterns remain applicable; specific benchmarks dated.` |
| `prescience` | Prediction accuracy: `high`, `medium`, `low`, `not-applicable`, `[DEFERRED]` | `high` |
| `prescience_rationale` | 1-2 sentence justification | `Predicted AS/400 longevity proved correct.` |

**Extraction instructions:**

1. Look for title in the first 500 characters (headings, title pages).
2. Look for author names near the title or in signature blocks.
3. Identify dates from headers, footers, cover pages, or internal references.
4. Classify the study type. Use extended types (transcript, memoir, employer-record, ai-response, topic-analysis) when appropriate.
5. Generate abstract by summarizing the core argument in 2-3 sentences.
6. If metadata is ambiguous, flag with `[REVIEW]` and proceed.

**Assessment instructions:**

7. **Importance**: Was it the first of its kind? Did it shape industry decisions? Rate `high` / `medium` / `low`.
8. **Relevance**: Is it still useful today? Rate `high` / `medium` / `low`.
9. **Prescience**: Assess based on document text and general knowledge. Set `[DEFERRED]` if web verification is needed. Set `not-applicable` if no predictions were made.
10. Write a concise rationale (1-2 sentences) for each rating.

#### Step 4: Extract Entities -> `entities.csv`

| Field | Description | Example |
|---|---|---|
| `entity_id` | Canonical lowercase hyphenated name | `intelligent-electronics` |
| `entity_name` | Display name | `Intelligent Electronics, Inc.` |
| `entity_type` | `company`, `firm`, `institution`, `agency`, `person` | `company` |
| `sector` | Industry sector | `PC-distribution` |
| `status` | Current status or `[DEFERRED]` | `dissolved` |
| `successor` | Successor entity or `[DEFERRED]` | `GE -> Xerox` |
| `years_active` | Approximate years | `1982-1997` |
| `study_id` | FK to studies.csv | `ie-andersen-expert-report-a1b2c3` |
| `notes` | Additional context | `Exton, PA headquarters` |

**Extraction instructions:**

1. Identify every named organization in the document.
2. For each, determine type, sector, and role in the study.
3. **Check the reuse cache first.** If the entity exists in `_known_entities.csv`, reuse its entity_id and known metadata. Only extract metadata for genuinely new entities.
4. **[DEFERRED]** For new entities, set `status` and `successor` to `[DEFERRED]`. Do NOT call `web_search`. Exception: if the document itself states the entity's fate, record it directly.
5. Deduplicate: merge multiple names for the same entity into one row.

#### Step 5: Extract Technologies -> `technologies.csv`

| Field | Description | Example |
|---|---|---|
| `tech_id` | Canonical lowercase hyphenated | `as400` |
| `tech_name` | Display name | `IBM AS/400` |
| `category` | `platform`, `application`, `protocol`, `language`, `framework` | `platform` |
| `vendor` | Primary vendor | `IBM` |
| `era` | Approximate era | `1988-2000` |
| `lifecycle_at_study` | Status when study was written | `mature` |
| `lifecycle_current` | Status now or `[DEFERRED]` | `legacy-supported` |
| `study_id` | FK to studies.csv | `ie-andersen-expert-report-a1b2c3` |
| `notes` | | `Renamed to iSeries, then IBM i` |

**Check the reuse cache** for known technologies before extracting. Reuse `tech_id` and metadata for previously classified technologies.

#### Step 6: Extract Observations -> `observations.csv`

This is the **core analytical table**. Every factual claim, prediction,
benchmark result, or analytical judgment becomes a row.

| Field | Description |
|---|---|
| `obs_id` | `{study_id}-OBS-{NNN}` |
| `study_id` | FK to studies.csv |
| `entity_id` | FK to entities.csv (nullable) |
| `tech_id` | FK to technologies.csv (nullable) |
| `observation_type` | See codes table in assembler module |
| `year_observed` | Year the observation applies to |
| `metric_name` | What is being measured/claimed |
| `metric_value` | The value or classification |
| `confidence` | `high`, `medium`, `low`, `verified`, `[DEFERRED]` |
| `methodology_code` | FK to codes.csv |
| `source_page` | Page/section reference |
| `notes` | Additional context |

**Extraction instructions:**

1. Read the document systematically, section by section.
2. Create a row for every quantifiable claim, qualitative judgment, benchmark, or framework component.
3. Cross-reference entity_id and tech_id with Steps 4-5.
4. Flag predictions as `viability-prediction`. Create a placeholder `actual-outcome` row with `confidence: [DEFERRED]` and `metric_value: [DEFERRED]`.
5. Use `personal-recollection` for memoir content, `ai-exchange` for AI responses, `topic-insight` for topic analyses.
6. Aim for 15-50 observations per study.

**After Step 6:** Save the raw cleaned text to `{study_dir}/source/_raw_text.txt`.

---

### 5B. Phase 2: Script Assembly (Zero Credits)

After Phase 1 completes for each study, run the bundled assembler:

```bash
python scripts/assembler.py assemble {study_dir}
```

This executes Steps 7-12 automatically:

| Step | Output | Method |
|---|---|---|
| 7 | `data/codes.csv` | Standard codes + study-specific codes scanned from observations |
| 8 | `datapackage.json` | Frictionless descriptor from studies.csv row 1 |
| 9 | `schema/schema_org.json` | Schema.org/Dataset JSON-LD |
| 10 | `README.md` | Human-readable guide from CSV data |
| 11 | `scripts/demo_analysis.py` | Reusable template (runtime self-discovery) |
| 12 | `source/original_text.md` | Raw text + CSV metadata appendix |

Then update the reuse cache:

```bash
python scripts/assembler.py cache-update output/ {study_dir}
```

---

### 6. Output Directory Structure

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
      _raw_text.txt         ← preserved for re-assembly after backfill
    scripts/
      demo_analysis.py
  _known_entities.csv       ← cross-study entity reuse cache
  _known_technologies.csv   ← cross-study technology reuse cache
  _web_cache.json           ← incremental web verification cache
  _checkpoint.json
```

---

### 7. Recursion & Multi-Study Orchestration

#### 7.1 Directory Recursion

After processing each batch of 10 files, report progress and continue.

#### 7.2 Cross-Study Accumulation

After all batches complete, generate master indices:

- `_master_studies.csv` — All studies in one table
- `_master_entities.csv` — Deduplicated entities (derived from `_known_entities.csv`)
- `_master_technologies.csv` — Deduplicated technologies (derived from `_known_technologies.csv`)

#### 7.3 Quality Checks (Per-Batch)

Run after each batch completes Phase 2:

```bash
python scripts/assembler.py validate output/study-1/ output/study-2/ ...
```

Checks: referential integrity, code coverage, completeness, consistency.
Flag failures with `[REVIEW]` and continue.

---

### 8. User Interaction Protocol

#### 8.1 Before Processing

1. Confirm the directory path or files to process
2. Show file count: "Found {N} study files. Processing in batches of 10."
3. Report cache status: "{X} known entities, {Y} known technologies from prior sessions."
4. Ask: "Shall I proceed?"

#### 8.2 During Processing

```
Processing: Kastner-Expert-Report-IE-v-Andersen.pdf
  -> Study ID: ie-andersen-expert-report-a1b2c3
  -> Extracted: 19 entities (12 from cache, 7 new), 8 technologies, 29 observations
  -> Phase 2 assembled, cache updated
```

#### 8.3 After Each Batch

```
Batch 1 complete: 10/37 files processed
  -> 247 total observations extracted
  -> Cache: 89 known entities, 34 known technologies
  -> 3 items flagged [REVIEW]
```

#### 8.4 After All Batches

```
All 37 files processed.
  -> 37 study packages in output/
  -> Cache: 142 entities, 67 technologies
  -> Starting deferred web verification (Phase 3)...
```

---

### 9. Error Handling

| Error | Action |
|---|---|
| File unreadable | Log to `_review_log.csv`, skip, continue |
| Ambiguous metadata | Use filename as title, mark `[REVIEW]`, continue |
| PDF extraction unavailable | Request text version or skip with log |
| Entity status unknown | Mark `[DEFERRED]`, resolve in Phase 3 |
| Duplicate study detected | Log duplicate, process only first instance |

---

### 10. Phase 3: Deferred Web Verification

Runs **once** after all batches complete. Uses the incremental web cache
so returning entities from prior sessions are not re-searched.

#### 10.1 Check Cache for Needed Verifications

```bash
python scripts/assembler.py web-cache-check output/ \
  --entities ibm,wang-laboratories,prime-computer \
  --techs as400,hp-3000 \
  --preds study1-OBS-007,study2-OBS-012
```

Returns only IDs not already verified. First run: most items need verification.
Subsequent runs: only newly encountered entities/technologies.

#### 10.2 Execute Web Searches (AI Credit Cost)

For items needing verification, use batched `web_search` calls:

1. **Entity status** (5 entities per query): "{Company A} {Company B} {Company C} current status acquired merged dissolved"
2. **Technology lifecycle** (5 per query): "{Tech A} {Tech B} end of life current status"
3. **Prediction outcomes** (1 per unique topic): "{subject} actual outcome result"

#### 10.3 Store Results in Cache

Save verification results to `_web_verification_results.json`, then:

```bash
python scripts/assembler.py web-cache-store output/ _web_verification_results.json
```

#### 10.4 Backfill All Studies

```bash
python scripts/assembler.py backfill output/ _web_verification_results.json
```

This updates all `[DEFERRED]` fields across all study CSVs, regenerates
`original_text.md` files to reflect backfilled data, and changes any
remaining `[DEFERRED]` values to `unknown [REVIEW]`.

---

### 11. Example: Expected Output for IE v. Andersen Study

- `studies.csv`: 1 row (importance/relevance/prescience ratings with rationales)
- `entities.csv`: ~19 rows (IE, Andersen, Ingram Micro, Tech Data, etc.)
- `technologies.csv`: ~8 rows (AS/400, HP 3000, SAP R/3, OS/2, etc.)
- `observations.csv`: ~29 rows (strategy classifications, viability predictions, etc.)
- `codes.csv`: ~18 rows (auto-generated by assembler)
- `datapackage.json`: Complete Frictionless descriptor (auto-generated)
- `schema/schema_org.json`: Google Dataset Search-compatible (auto-generated)
- `README.md`: Human-readable guide (auto-generated)
- `scripts/demo_analysis.py`: Runnable validation (template copy)

---

### 12. Publication Pipeline (Post-Processing)

After all studies are processed, guide the user through:

1. **GitHub**: Push each study package to the primary repository (`shorttack/aberdeen-group-archive`)
2. **Zenodo**: Archive the GitHub repo to get a DOI per version
3. **Hugging Face**: Upload as a dataset for ML discoverability
4. **Internet Archive**: Backup deposit for permanent preservation

---

### 13. Extended Collection Types (v14+)

Five specialized types for the Kastner personal archive. Each follows the
same Phase 1 → Phase 2 → Phase 3 pipeline. Type-specific extraction rules below.

#### 13.1 Transcripts of Videos

**Type code**: `transcript` | **Methodology**: `oral-history` | **Domain prefix**: `video-transcript`

**What belongs here**: Verbatim transcriptions of Kastner video recordings — conferences, interviews, panels, webinars, lectures, demos.

**Metadata additions** (in `notes` of `studies.csv`): `video_url`, `recording_format` (conference/interview/panel/webinar/lecture/demo), `transcript_source` (auto-generated/manual/ai-assisted), `duration_minutes`.

**Extraction rules:**
1. Mark Kastner's speech as first-person. Tag other speakers with `[SPEAKER: Name]`.
2. Each substantive claim becomes an observation (`expert-opinion` or `personal-recollection`).
3. Use `source_page` for timestamps (e.g., `00:04:32`).
4. Verbatim quotes in `metric_value` (up to 200 chars); longer in `notes`.

#### 13.2 Memoirs, Commentary, and Anecdotes

**Type code**: `memoir` | **Methodology**: `oral-history` | **Domain prefix**: `memoir`

**What belongs here**: First-person narratives not tied to a formal document — recollections, anecdotes, reflections, commentary.

**Metadata additions**: `era` (decade/period), `mood` (reflective/critical/celebratory/analytical), `trigger` (what prompted the memoir).

**Extraction rules:**
1. Each distinct memory/anecdote = one observation (`personal-recollection`).
2. Extract named individuals as `entity_type: person`.
3. Tag tone in `notes`: `positive`, `critical`, `neutral`, `regretful`.
4. Flag living individuals in unflattering context with `[PRIVACY-REVIEW]`.

#### 13.3 Employers Section

**Type code**: `employer-record` | **Methodology**: `document-review` or `oral-history` | **Domain prefix**: `employer/{company-id}`

**Canonical employers:**

| entity_id | entity_name | Kastner role era |
|---|---|---|
| `phi-computer-services` | PHI Computer Services | 1969-1972 |
| `wang-laboratories` | Wang Laboratories | 1969-1972 |
| `arthur-d-little` | Arthur D. Little (ADL) | 1972-1979 |
| `prime-computer` | Prime Computer | Market Planning |
| `stratus-computer` | Stratus Computer | Marketing |
| `yankee-group` | Yankee Group | Ghost writer |
| `DEC` | Digital Equipment | Marketing |
| `aberdeen-group` | Aberdeen Group | Co-founder, CRO |
| `obian-group` | Obian Group | Consulting |
| `adoptex-ai` | Adoptex.ai | Founder, COO |

**Metadata additions**: `employer_id`, `kastner_role`, `record_subtype`, `confidentiality`.

**Extraction rules:**
1. Link every record to one canonical employer.
2. Extract or infer Kastner's title/role.
3. Add `career_significance` field: `high` / `medium` / `low`.
4. For photos, create lightweight `.md` metadata files (not full CSV packages).

#### 13.4 What AI Says

**Type code**: `ai-response` | **Methodology**: `ai-dialog` | **Domain prefix**: `ai-response`

**What belongs here**: Preserved Q&A exchanges between Kastner and AI systems.

**Metadata additions**: `ai_system`, `ai_model`, `question_by`, `session_date`, `exchange_count`, `kastner_verdict`.

**Extraction rules:**
1. One observation per Q&A turn (`ai-exchange`).
2. Question text in `metric_name` (truncated 200 chars).
3. Response summary in `metric_value`; full response in `original_text.md`.
4. Flag verifiable errors with `[HALLUCINATION]` in `notes`.

#### 13.5 Topics: Technology Deep-Dives

**Type code**: `topic-analysis` | **Methodology**: `industry-analysis` | **Domain prefix**: `topic`

**Canonical topics:**

| topic_id | Topic | Era |
|---|---|---|
| `oltp` | Online Transaction Processing | 1980s-1990s |
| `commercial-benchmarks` | Commercial Benchmarks | 1985-2000 |
| `client-server` | Client-Server Computing | 1988-1998 |
| `decision-support` | Decision Support Systems | 1988-2000 |
| `application-development` | Application Development | 1990-2005 |
| `soa-bpm-edi` | SOA, BPM, and EDI | 1995-2010 |
| `e-commerce` | E-Commerce | 1995-2005 |
| `internet` | Internet and Web Technologies | 1993-2005 |
| `personal-pcs` | Personal Computers | 1980-2000 |
| `enterprise-pcs` | Enterprise PCs | 1985-2000 |

**Metadata additions**: `topic_id`, `content_origin` (kastner/outside), `kastner_role_in_topic`, `thought_leadership_score` (1-5).

**Extraction rules:**
1. Declare `content_origin`. Kastner content → `kastner_content/`; third-party → `outside_content/`.
2. Tag distinctive/contrarian positions as `topic-insight` with `confidence: high`.
3. Cross-topic links in `notes`: `cross-topic: commercial-benchmarks`.

---

### 14. Collection Type Routing

Determine collection type before processing:

1. Video transcript? → Section 13.1
2. First-person narrative? → Section 13.2
3. Associated with a canonical employer? → Section 13.3
4. AI Q&A exchange? → Section 13.4
5. Content on a canonical topic? → Section 13.5
6. None of the above? → Standard research study (Sections 5-12)

**Process once under the primary type only.** For multi-type documents, add
lightweight cross-reference entries in secondary collections — do NOT re-run
the full extraction pipeline.

**Cross-reference format:**

```csv
xref_study_id,primary_collection,primary_path,secondary_topics,notes
aberdeen-memoir-a1b2c3,memoir,output/aberdeen-memoir-a1b2c3/,"oltp,commercial-benchmarks","Cross-ref only"
```

---

### 15. Master Collection Index

After all processing and Phase 3 verification:

```
output/
  _MASTER_INDEX.md
  _master_studies.csv
  _master_entities.csv        ← derived from _known_entities.csv
  _master_technologies.csv    ← derived from _known_technologies.csv
  _collection_stats.csv
  _known_entities.csv         ← reuse cache (persists across sessions)
  _known_technologies.csv     ← reuse cache (persists across sessions)
  _web_cache.json             ← verification cache (persists across sessions)
```

---

### 16. CSV Write Validation Gate (v17)

**MANDATORY.** Every CSV file written during Phase 1 (studies.csv, entities.csv,
technologies.csv, observations.csv) MUST pass through this validation gate
immediately after being written to disk. If any check fails, the file MUST be
rewritten before proceeding to Phase 2.

> **Background (April 2026 incident):** Subagent-based parallel processing
> produced 132 base64-encoded CSV files, 35 column-shifted files, and 49 files
> with invalid rating/confidence values. This corrupted the entire 506-study
> corpus and required a multi-session manual repair. This gate prevents
> recurrence.

#### 16.1 When to Run

Run the validation gate:

1. **After every Phase 1 CSV write** — immediately after writing each of the
   four CSVs (studies, entities, technologies, observations) for a study.
2. **After every backfill operation** (Phase 3, Section 10.4).
3. **After any batch repair or bulk update** to existing CSV files.
4. **Before any git commit** that includes CSV files.

#### 16.2 Validation Checks

For every CSV file written, run all five checks **in order**. Halt on the
first failure for that file.

##### Check 1: Plain-Text Guard (Anti-Base64)

Read the first 200 bytes of the file as raw bytes.

```python
def check_plain_text(filepath: str) -> bool:
    with open(filepath, 'rb') as f:
        head = f.read(200)
    # Base64-encoded files lack commas and newlines in the header region
    if b',' not in head or b'\n' not in head:
        return False  # FAIL: likely base64
    # Additional check: base64 alphabet dominates
    text = head.decode('utf-8', errors='replace')
    alnum = sum(c.isalnum() or c in '+/=' for c in text)
    if alnum / max(len(text), 1) > 0.85:
        return False  # FAIL: base64 density too high
    return True
```

**On failure:** Attempt base64 decode. If decode produces valid CSV, replace
the file with decoded content and re-run all checks. If decode fails, flag
`[CORRUPT]` and re-extract from source.

##### Check 2: Column Count Consistency

Read the header row, count fields. Then verify every data row has the same
number of fields.

```python
import csv
def check_column_count(filepath: str) -> tuple[bool, str]:
    with open(filepath, 'r', newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        expected = len(header)
        for i, row in enumerate(reader, start=2):
            if len(row) != expected:
                return False, f"Row {i}: expected {expected} cols, got {len(row)}"
    return True, "OK"
```

Expected column counts:

| File | Columns | Header |
|---|---|---|
| `studies.csv` | 16 | study_id, title, author, date, type, subject_domain, methodology, source_file, abstract, license, importance, importance_rationale, relevance, relevance_rationale, prescience, prescience_rationale |
| `entities.csv` | 9 | entity_id, entity_name, entity_type, sector, status, successor, years_active, study_id, notes |
| `technologies.csv` | 9 | tech_id, tech_name, category, vendor, era, lifecycle_at_study, lifecycle_current, study_id, notes |
| `observations.csv` | 12 | obs_id, study_id, entity_id, tech_id, observation_type, year_observed, metric_name, metric_value, confidence, methodology_code, source_page, notes |

**On failure:** Identify shifted columns using the `license` field as an anchor
(must equal `CC-BY-4.0` in studies.csv). Realign fields and rewrite.

##### Check 3: Enum Value Validation

Verify that fields with controlled vocabularies contain only valid values.

```python
VALID_ENUMS = {
    'studies.csv': {
        'license': {'CC-BY-4.0'},
        'importance': {'high', 'medium', 'low'},
        'relevance': {'high', 'medium', 'low'},
        'prescience': {'high', 'medium', 'low', 'not-applicable', '[DEFERRED]'},
    },
    'observations.csv': {
        'confidence': {
            'high', 'medium', 'low', 'verified', '[DEFERRED]',
            # Post-backfill values (valid after Phase 3):
            'partially-verified', 'refuted', 'unknown [REVIEW]',
        },
    },
}
```

**On failure:** Normalize the value:
- Numeric ratings (1-9) → map to `high` (7-9), `medium` (4-6), `low` (1-3)
- Uppercase → lowercase (e.g., `HIGH` → `high`, `Medium` → `medium`)
- `CF-HIGH`, `CF-MEDIUM`, `CF-LOW` → `high`, `medium`, `low`
- Any other invalid value → flag `[REVIEW]` and log to `_validation_log.csv`

##### Check 4: QUOTE_ALL Enforcement

All CSV files MUST be written with `csv.QUOTE_ALL` to prevent field-splitting
on embedded commas, newlines, or quotes.

```python
import csv
def write_csv_safe(filepath: str, header: list, rows: list[list]):
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(header)
        writer.writerows(rows)
```

**This is the ONLY permitted CSV write method.** Never use `f.write()`,
`pandas.to_csv()` without `quoting=csv.QUOTE_ALL`, or string concatenation
to produce CSV files.

##### Check 5: Abstract Sanity (studies.csv only)

The `abstract` field must contain prose (2-3 sentences), not a filename,
path, or base64 blob.

```python
def check_abstract(abstract: str) -> bool:
    if not abstract or len(abstract) < 30:
        return False  # Too short to be a real abstract
    if '/' in abstract and '.' in abstract.split('/')[-1]:
        return False  # Looks like a file path
    if abstract.startswith('data:') or '==' in abstract[-4:]:
        return False  # Looks like base64
    return True
```

**On failure:** Re-generate abstract from `source/_raw_text.txt`.

#### 16.3 Validation Log

All validation failures are logged to `_validation_log.csv` in the output
directory:

```csv
timestamp,study_id,file,check,status,detail,action_taken
2026-04-12T20:30:00,study-abc123,observations.csv,enum-validation,FAIL,"confidence='CF-HIGH' in row 3","normalized to 'high'"
```

#### 16.4 Batch Validation Command

To validate all CSVs in a study directory at once:

```python
def validate_study_csvs(study_dir: str) -> dict:
    """Run all 5 checks on all 4 CSVs. Returns {file: [failures]}."""
    results = {}
    csv_files = ['studies.csv', 'entities.csv', 'technologies.csv', 'observations.csv']
    for csv_name in csv_files:
        path = os.path.join(study_dir, 'data', csv_name)
        if not os.path.exists(path):
            results[csv_name] = ['MISSING']
            continue
        failures = []
        if not check_plain_text(path):
            failures.append('base64-encoded')
        ok, msg = check_column_count(path)
        if not ok:
            failures.append(f'column-shift: {msg}')
        # Enum checks per file type...
        # QUOTE_ALL check...
        if csv_name == 'studies.csv':
            # Abstract check...
            pass
        results[csv_name] = failures if failures else ['PASS']
    return results
```

#### 16.5 Subagent Instructions

When using subagents for parallel processing, include this **mandatory
instruction** in every subagent objective:

> **CSV OUTPUT RULES (MANDATORY):**
> 1. All CSV files MUST be written using Python's `csv.writer` with
>    `quoting=csv.QUOTE_ALL`. Never use string concatenation or
>    `pandas.to_csv()` without explicit `quoting=csv.QUOTE_ALL`.
> 2. NEVER base64-encode CSV content. Write plain UTF-8 text only.
> 3. After writing each CSV, verify it by reading back the first 3 rows
>    with `csv.reader` and confirming the column count matches the header.
> 4. Rating fields (importance, relevance, prescience) must be lowercase
>    strings: `high`, `medium`, `low`, `not-applicable`, or `[DEFERRED]`.
> 5. Confidence must be lowercase: `high`, `medium`, `low`, `verified`,
>    or `[DEFERRED]`.
> 6. License must be exactly `CC-BY-4.0`.
> 7. If any validation fails, fix and rewrite before returning results.

---
