---
name: archival-ingest
description: >
  Batch-process historical research studies into structured, machine-readable
  archival datasets. Use when asked to archive studies, ingest research files,
  build a Frictionless Data Package, extract observations, archive DCT
  spreadsheets, ingest PC pricing data, recurse a directory of study files,
  or update the companion Kastner Aberdeen Wiki. Handles PDF, Markdown,
  Word, Excel (.xls/.xlsx), and plain-text inputs. Produces five CSV tables,
  datapackage.json, schema_org.json, README.md, and demo_analysis.py per
  study. Includes importance, relevance, and prescience ratings. Supports
  six Kastner collection types: video transcripts, memoirs, employer
  records, AI responses, technology topics, and Digital Consumer Technology
  (DCT). v17 added the CSV Validation Gate. v18 added DCT and xls/xlsx.
  v19 adds Pass A structural verification (verification_method enum,
  predecessor-to-outcome lift), wiki propagation, schema normalization
  for legacy CSVs, and master regen integrity checks.
metadata:
  version: '19'
  author: Peter S. Kastner
  repository: github.com/shorttack/aberdeen-group-archive
---

## Archival Ingest Skill v19

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
- "Archive DCT spreadsheets"
- "Ingest PC pricing data"
- "Process weekly PC deals commentary"

---

### 2. Environment & Tools Available

| Capability | How to use it |
|---|---|
| **File system** | Read/write files via Python (`open()`, `os`, `pathlib`, `glob`) |
| **Python execution** | Full Python 3 stdlib. Use `pandas` if available. |
| **Bundled assembler** | `python scripts/assembler.py <command>` — handles all Phase 2 and Phase 3 operations. See Section 5B. The canonical assembler lives in the archive repo at `aberdeen-group-archive/_skills/archival-ingest/scripts/assembler.py` (not bundled in this skill). |
| **Web search** | Use `web_search` only in Phase 3 (deferred batch verification). Never during Phase 1. |
| **URL fetch** | Use `fetch_url` for reference material if needed |
| **Companion wiki repo** | `kastner-aberdeen-wiki/` — Obsidian + DuckDB + Parquet research environment. Updated after every archive push via the surgical-update flow in Section 18. Refresh scripts live at `kastner-aberdeen-wiki/scripts/refresh_data_layer.py` and `add_pass_a_v2_pages.py`. |
| **Archive-repo skill mirror** | `aberdeen-group-archive/_skills/archival-ingest/SKILL.md` — a copy of this skill is mirrored into the archive for provenance. Update with a separate small commit after `save_custom_skill`. |

---

### 3. Input Expectations

The user will provide one of:

1. **A directory path** containing study files (PDF, .md, .txt, .docx, .xls, .xlsx)
2. **Individual file attachments** uploaded to the conversation
3. **A reference to files already in the sandbox** from a previous step

If the user provides a directory, discover all processable files:

```python
from pathlib import Path
SUPPORTED = {'.md', '.txt', '.pdf', '.docx', '.doc', '.rtf', '.xls', '.xlsx'}

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

# After all batches complete + master regen:
#   1. Run Pass A structural verification (Section 17)
#   2. Propagate to wiki via surgical update (Section 18)
#   3. Run master regen integrity checks (Section 20)
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
directly. For DOCX, extract via python-docx. For .xls, extract via `xlrd`
(legacy Excel); for .xlsx, use `openpyxl`. For .doc (legacy Word), convert
with `soffice --headless --convert-to txt` then read the resulting .txt.

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

**Additional integrity checks (v19):**

- **Row-count parity**: After master regen, verify
  `len(master_observations) == sum(len(study_observations) for unique study_id)`.
  See Section 20 for the duplicate-study handling rules.
- **Verification-method coverage**: After Pass A runs, verify that 100% of
  `master_observations.csv` rows have a non-empty `verification_method` value
  drawn from the allowed enum (Section 17.1). Missing or unknown values must
  be set to `unverified` rather than left blank.

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
| **Row-count mismatch after master regen** | Apply Section 20.2 dedup-by-`study_id` rule. Confirm the 9 known cross-directory duplicates (Section 20.3) account for the gap. Halt if any unexplained delta remains. |
| **Schema divergence on legacy CSV** | Apply Section 19 normalization playbook (column rename map + required defaults). Never silently drop columns; preserve extension columns (e.g., `thread_tag`) in `notes`. |
| **Missing `verification_method`** | After Pass A v1 has run, all observation rows MUST carry a value. Treat blanks as `unverified` and emit a `[REVIEW]` log entry rather than failing the batch. |

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

#### 13.6 Digital Consumer Technology (DCT)

**Type code**: `dct` | **Methodology**: `market-tracking` | **Domain prefix**: `dct` | **Repo path**: `kastner-author/dct/`

**What belongs here**: Peter Kastner's 2002-2003 (and adjacent) PC retail / consumer technology tracking — weekly pricing snapshots, vendor lineups, CPU price series, shipment statistics, survey results, and accompanying weekly commentary docs. These describe the U.S. DCT (Digital Consumer Technology) market during the post-bubble PC price war era.

**Subtype field** (record in `notes` of `studies.csv`): 
- `dataset` — tabular xls/xlsx files (price tables, shipment data, surveys)
- `weekly` — doc/docx/txt commentary files pairing with a given week's data
- `aggregate` — multi-week pooled datasets (e.g., access PC Deals 2002-2003.xls)

**Metadata additions** (record in `notes` of `studies.csv`): `content_date` (ISO 8601 date or date range), `retailers_covered` (comma-separated), `vendors_covered` (comma-separated), `subtype`, `related_study_ids` (comma-separated; used to link weekly xls and weekly doc pairs by content date).

**Canonical retailer entities** (reuse these entity_ids; classify as `entity_type: company`, `sector: PC-retail`):

| entity_id | entity_name | Channel |
|---|---|---|
| `best-buy` | Best Buy (stores) | Brick-and-mortar |
| `bestbuy-com` | BestBuy.com | E-commerce |
| `circuit-city` | Circuit City (stores) | Brick-and-mortar |
| `circuitcity-com` | CircuitCity.com | E-commerce |
| `compusa` | CompUSA | Brick-and-mortar + online |
| `dell-online` | www.dell.com | Direct e-commerce |
| `hpshopping` | HP Shopping | Direct e-commerce |
| `gateway-online` | Gateway.com | Direct e-commerce |
| `sony-online` | Sony Style | Direct e-commerce |

**Canonical PCmaker entities** (reuse these entity_ids; sector `PC-manufacturing`): `dell`, `hewlett-packard`, `compaq`, `ibm`, `gateway-inc`, `sony`, `fujitsu`, `toshiba`, `alienware`, `emachines`, `vpr-matrix`, `apple-computer`.

**Extraction rules:**
1. **Dataset files (xls/xlsx):** Each distinct row/record becomes market data. Aim for aggregated observations (vendor × week, vendor × quarter, or category rollups) rather than per-SKU rows when the file exceeds 50 rows. For aggregate files (2,000+ rows), always aggregate; preserve full row-level data in `source/_raw_text.txt`.
2. **Weekly commentary docs:** Use observation_type `expert-opinion` for Kastner's market assessments. Link to the matching dataset study via `related_study_ids` (content-date match).
3. **observation_type** for price rows: `market-data`. For shipment counts: `market-data`. For survey responses: `market-data`. For Kastner commentary: `expert-opinion`.
4. **year_observed**: derive from the row's pricing date or survey date when available; fall back to study date.
5. **confidence**: `high` for sourced prices from vendor sites or published shipment data; `medium` for reported survey results; `low` for editorial interpretations.
6. **Technologies** captured from DCT files: processor generations (`intel-pentium-4`, `amd-athlon-xp`, `intel-celeron`), form factors (`desktop-pc`, `notebook-pc`, `thin-light-notebook`), OS (`windows-xp`, `windows-xp-pro`, `windows-xp-home`), optical drives (`dvd-cd-rw`).

**Repository layout:**

```
kastner-author/dct/
  {study_id}/              ← one directory per DCT study (xls or doc)
    data/...
    source/...
    ...
```

All DCT studies live in one pooled directory. Linkage between matched xls/doc pairs is via the `related_study_ids` metadata field, not directory structure.

---

### 14. Collection Type Routing

Determine collection type before processing:

1. Video transcript? → Section 13.1
2. First-person narrative? → Section 13.2
3. Associated with a canonical employer? → Section 13.3
4. AI Q&A exchange? → Section 13.4
5. Content on a canonical topic? → Section 13.5
6. DCT spreadsheet or weekly PC-deals commentary? → Section 13.6
7. None of the above? → Standard research study (Sections 5-12)

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

##### Check 6: Verification Method Enum (v19)

After Pass A (Section 17) has run, every row in `observations.csv` and the
derived `master_observations.csv` MUST carry a `verification_method` value
from the allowed enum:

```python
VALID_VERIFICATION_METHODS = {
    'ingest-extraction',  # Default; claim sourced from the study text itself
    'web-source',         # Phase 3 web verification matched the claim
    'outcome-linkage',    # Predecessor→outcome lift filled the row
    'unverified',         # Explicitly unverifiable / no source matched
    'placeholder',        # Stub row reserved for future verification
    'cross-reference',    # Resolved by linking to another in-archive study
}
```

**On failure:** Set the value to `unverified` and log to `_validation_log.csv`
rather than failing the batch. Pre-Pass-A files may legitimately omit the
column; the check only fires once `verification_method` is present in the
header.

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
> 8. **(v19)** If the observations.csv schema includes a `verification_method`
>    column (i.e., Pass A v1 has run on the corpus), every row must carry a
>    value from the allowed enum: `ingest-extraction`, `web-source`,
>    `outcome-linkage`, `unverified`, `placeholder`, or `cross-reference`.
>    Default new Phase 1 rows to `ingest-extraction`. Never leave the field
>    blank — use `unverified` if no source can be cited.

---

### 17. Pass A Verification Pipeline (v19)

Pass A is a **structural** verification stage that runs after every cache
update + master regen. It uses no LLM and no external evidence — it
classifies each observation row by *how* it was sourced, then lifts
predecessor-row evidence into successor outcome rows where a deterministic
join is possible.

The output is a master corpus in which 100% of observation rows carry a
`verification_method` value, and every viability-prediction row is paired
(where possible) with a linked actual-outcome row via the
`_prediction_outcome_links.csv` join table.

#### 17.1 verification_method Enum

| value | meaning | how a row earns it |
|---|---|---|
| `ingest-extraction` | The claim was extracted directly from the study text during Phase 1. | Default for all freshly ingested rows; the study itself is the source. |
| `web-source` | A Phase 3 web verification matched and confirmed the claim. | Set during backfill when `_web_cache.json` returns a positive match. |
| `outcome-linkage` | The row's value was filled by predecessor→outcome lift. | A `viability-prediction` row and an `actual-outcome` row share `(entity_id, tech_id, metric_name)` and the outcome row is non-empty. |
| `unverified` | No source could be matched. The row is preserved but flagged. | Default fallback for any row that fails the other rules. |
| `placeholder` | Stub row reserved for future verification. | Phase 1 emits these for predictions whose outcome is `[DEFERRED]`. |
| `cross-reference` | Resolved by linking to another in-archive study. | Pass A's xref scan found a matching observation in a sibling study. |

#### 17.2 REVIEW Marker Triage Rules

Pass A scans for `[REVIEW]`, `[DEFERRED]`, and `[CORRUPT]` markers in every
text field and triages them deterministically:

1. **`[DEFERRED]` in `confidence` or `status`** → leave in place; Phase 3
   web verification owns these.
2. **`[REVIEW]` in `metric_value` or `notes`** → preserve, but downgrade
   the row's `verification_method` to `unverified` and log to
   `_pass_a_review_log.csv` with the originating study_id.
3. **`[CORRUPT]` anywhere** → halt Pass A for that study; refer to
   Section 16 (CSV Validation Gate) for repair before retrying.
4. **Bare `unknown`, `n/a`, `tbd`** → normalize to `unverified` in
   `verification_method`; leave the visible cell value untouched.

#### 17.3 Predecessor → Outcome Lift

Many studies emit a `viability-prediction` row at time `T` and a paired
`actual-outcome` placeholder row that gets filled in later — sometimes by
a different study. Pass A joins these deterministically:

```python
# Join key: (entity_id, tech_id, metric_name)
# When the outcome row has a real value, lift it onto the prediction row
# and write a join entry to _prediction_outcome_links.csv:
#
#   prediction_obs_id, outcome_obs_id, lift_status, confidence_after
#
# lift_status ∈ {verified, partially-verified, refuted, unmatched}
# confidence_after = max(prediction.confidence, outcome.confidence)
```

The join table is the single source of truth for the
`viability_predictions_status` DuckDB view (Section 18.3). Never inline
this logic into per-study scripts — always derive it centrally from
`master_observations.csv` so the wiki view stays consistent.

#### 17.4 When to Run

Run Pass A:

1. **After every `cache-update`** that touches `master_observations.csv`.
2. **After every backfill** (Phase 3, Section 10.4).
3. **After every bulk repair** that modifies observation rows.
4. **Before every archive commit** that includes regenerated master CSVs.

Pass A is idempotent — running it twice on a clean corpus produces the
same output. The reproducible invocation pattern is:

```bash
# No LLM, no external evidence — structural only.
python scripts/assembler.py pass-a output/
# Emits:
#   output/master_observations.csv  (with verification_method populated)
#   output/_prediction_outcome_links.csv
#   output/_pass_a_review_log.csv
```

#### 17.5 Ground-Truth Distribution (Reference)

Pass A v2 on the 949-study, 19,694-observation corpus (commit `7f0dad1c`)
produced this verification_method distribution. Use as a sanity check
when re-running Pass A on the full corpus — large deviations signal a
regression:

| verification_method | rows |
|---|---|
| ingest-extraction | 17,553 |
| web-source | 1,187 |
| outcome-linkage | 855 |
| unverified | 79 |
| placeholder | 16 |
| cross-reference | 4 |

Viability-prediction outcome rate: **46.1% verified+partially-verified**
(788 / 1,711). Significant drops in this rate after a re-run almost
always indicate that `_prediction_outcome_links.csv` failed to regenerate
or that a column rename broke the join.

---

### 18. Wiki Propagation Step (v19)

The companion repo `kastner-aberdeen-wiki` is the queryable, navigable
surface of the archive — Obsidian vault + Parquet exports + DuckDB +
embedding index. After every archive push that changes the master CSVs,
the wiki must be propagated.

#### 18.1 When

Run wiki propagation **immediately after** the archive `git push origin main`
that contains the regenerated masters and Pass A outputs. Verify the
archive HEAD landed (Section 20.4) before starting the wiki update.

#### 18.2 Surgical Update (Default)

Do **not** re-run the full `kastner-wiki-builder` skill for routine
master-CSV updates. The full rebuild regenerates 8,000+ pages and
discards manual edits. Use the surgical update flow instead:

| Step | Script | What it does |
|---|---|---|
| 1 | `scripts/refresh_data_layer.py` | Rebuilds all 7 Parquet files from the latest archive masters, then rebuilds `kastner.duckdb` including any new views (Section 18.3). |
| 2 | `scripts/add_pass_a_v2_pages.py` (or version-renamed equivalent) | Generates new tier-1 study pages introduced by this batch, plus entity and technology stub pages for any IDs that gained observation coverage. |
| 3 | (manual edits via `edit` tool) | Cross-link the new theme page from existing theme pages and from `_index.md`. Update `build_manifest.json`. |
| 4 | `scripts/verify.py` | Runs all 13 wiki integrity checks. All must PASS before commit. |

The full `kastner-wiki-builder` skill is only invoked when the schema
itself changes (e.g., a new master CSV table is introduced) or when the
vault is being rebuilt from scratch.

#### 18.3 DuckDB Views Added in v19

Both views are created by `refresh_data_layer.py` and must survive every
Parquet rebuild:

```sql
-- View 1: verification_method distribution across the corpus
CREATE OR REPLACE VIEW verification_method_distribution AS
SELECT verification_method, COUNT(*) AS row_count
FROM master_observations
GROUP BY verification_method
ORDER BY row_count DESC;

-- View 2: viability-prediction outcome status, joined via
-- _prediction_outcome_links.csv produced by Pass A
CREATE OR REPLACE VIEW viability_predictions_status AS
SELECT p.obs_id        AS prediction_obs_id,
       p.study_id,
       p.entity_id,
       p.tech_id,
       p.metric_name,
       p.metric_value  AS prediction_value,
       o.metric_value  AS outcome_value,
       l.lift_status,
       l.confidence_after
FROM master_observations p
LEFT JOIN prediction_outcome_links l
       ON p.obs_id = l.prediction_obs_id
LEFT JOIN master_observations o
       ON l.outcome_obs_id = o.obs_id
WHERE p.observation_type = 'viability-prediction';
```

#### 18.4 Stub-Page Generation Rules

When new entity or technology IDs appear in the master CSVs:

1. Create a minimal Obsidian page at `entities/{entity_id}.md` (or
   `technologies/{tech_id}.md`) with YAML frontmatter (`name`, `type`,
   `sector`/`category`, `first_observed`, `last_observed`,
   `study_count`) and a `## Observations` Dataview block.
2. Set `tier: stub` in frontmatter so verify.py can distinguish stubs
   from hand-curated pages.
3. Do **not** overwrite an existing page whose `tier` is not `stub` —
   skip it and log to `_wiki_skip_log.csv`.

#### 18.5 Cross-Link Policy

When a new theme page is added (e.g., the `pass-a-v2-verification-pipeline`
theme), cross-link it from:

1. `_index.md` — under the appropriate section.
2. `build_manifest.json` — append to the `themes` array.
3. Every existing theme page whose content materially overlaps. Use
   `grep` to find candidate pages; add a single bullet under
   `## Related themes` (create the section if absent). Never duplicate
   an existing link.

#### 18.6 Verification & Commit

After surgical update, run:

```bash
cd kastner-aberdeen-wiki && python scripts/verify.py
# Expect: all 13 checks PASS
git add -A && \
  git -c user.name="Peter S. Kastner" \
      -c user.email="pete.kastner@bluebridgegrp.com" \
      commit -m "Propagate archive <archive-commit-sha> to wiki" && \
  git push origin main 2>&1 | tail -10
# Verify HEAD landed via Section 20.4.
```

Reference state: wiki commit `b0f0302` (8,716 pages) propagated archive
commit `7f0dad1c`.

---

### 19. Schema Normalization Playbook (v19)

Legacy or externally contributed `observations.csv` files often drift from
the canonical 12-column schema. v19 codifies a deterministic
normalization pass that runs *before* the CSV Validation Gate (Section 16).

#### 19.1 Canonical 12-Column Schema (Reference)

```
obs_id, study_id, entity_id, tech_id, observation_type,
year_observed, metric_name, metric_value, confidence,
methodology_code, source_page, notes
```

After Pass A v1, a 13th column `verification_method` is appended.

#### 19.2 Common Drift Patterns & Column Map

| Legacy / external column | Canonical column | Notes |
|---|---|---|
| `year` | `year_observed` | Direct rename. |
| `claim_text` | `notes` | Prefix the value with `[thread:XXX] ` if a `thread_tag` column was present (Section 19.4). |
| `source_ref` | `source_page` | Direct rename. |
| `claim` | `metric_value` | Only when paired with `claim_text`; otherwise treat as `metric_name`. |
| `confidence_score` (numeric 1-9) | `confidence` | Map per Section 16.2 Check 3 (7-9→high, 4-6→medium, 1-3→low). |
| `method` | `methodology_code` | Direct rename. |

#### 19.3 Required Defaults

If a column exists in the canonical schema but is missing from the input,
fill with the documented default (do NOT leave blank):

| column | default | rationale |
|---|---|---|
| `confidence` | `medium` | Conservative midpoint for unscored claims. |
| `verification_method` | `ingest-extraction` | Caller asserts the value came from the study text. |
| `methodology_code` | `industry-analysis` | Most common Kastner methodology; safe fallback. |
| `collection` | `<study-collection>` | Inherit from the parent study's `studies.csv` `subject_domain` prefix. |

#### 19.4 Extension Columns to Preserve

Some legacy CSVs carry useful extension columns that are NOT in the
canonical schema. These must be preserved by folding into `notes` rather
than dropped:

- `thread_tag` → prepend `[thread:<value>] ` to the existing `notes`
  value. This preserves cross-study thread linkage that downstream
  Obsidian Dataview queries depend on.
- Any other unknown column → append `; <col_name>=<value>` to `notes`.

#### 19.5 Auto-Normalize vs. Ask User

| Situation | Action |
|---|---|
| Column rename matches the table in Section 19.2 exactly | **Auto-normalize** — apply the map silently and log the change. |
| Missing column with a documented default (Section 19.3) | **Auto-normalize** — apply the default and log. |
| Extension column matches Section 19.4 pattern | **Auto-normalize** — fold into `notes` and log. |
| Unknown column with non-trivial content (>50% non-null) | **Ask the user** — present the column name, sample values, and propose a mapping. |
| Two source columns collide on the same canonical target | **Ask the user** — show both source values for a sample row and ask which wins. |
| Row count after normalization differs from input | **Halt** — never silently drop rows; surface the discrepancy. |

All normalization decisions are logged to `_schema_normalization_log.csv`
in the output directory.

---

### 20. Master Regen Integrity Checks (v19)

The 220-row phantom discrepancy investigated during the Pass A v2 work
exposed three failure modes that v19 makes explicit checks. These run as
part of every master regen.

#### 20.1 Row-Count Parity Check

The expected invariant after master regen is:

```
len(master_observations.csv) ==
    sum(len(study_observations) for study_id in unique_study_ids)
```

where `unique_study_ids` deduplicates across both `kastner-author/` and
`other-authors/` directories. **Per-directory totals will NOT match the
master** — duplicate study_ids exist by design (Section 20.3) and the
master keeps only one copy.

#### 20.2 Dedup-by-study_id Rule

When the same `study_id` appears in two directories, the master keeps the
first occurrence in this priority order:

1. `kastner-author/` wins over `other-authors/`.
2. If both are in the same directory tier (shouldn't happen), the lexically
   earlier file path wins; log a `[REVIEW]` entry.

The dedup is done on `study_id` alone, NOT on filename or content hash. If
two copies share a `study_id` but differ in observation content (Section
20.3 documents one such case), the discrepancy is logged but the dedup
proceeds — manual reconciliation is owned by a separate task, not by
master regen.

#### 20.3 Known Duplicate study_ids (Reference)

Nine `study_id` values are known to exist in both `kastner-author/` and
`other-authors/` directories. Their presence in both directories is
expected and does not indicate corruption:

```
1997-ca-s-unicenter-tng-framework-pk-apr-50d15f
2001-hp-cpq-merger-collection-edbca1
... (7 more — see archive _ops/duplicate_study_ids.csv for the full list)
```

One known content mismatch: `1997-marathon-s-endurance-4000` — both
copies have 21 observation rows but the content differs. This is tracked
in `_ops/duplicate_study_ids.csv` with a `content_match: false` flag and
is NOT auto-resolved.

#### 20.4 Slug Normalization Mismatches

Watch for these slug-collision sources:

- **Apostrophes**: `o'reilly` vs `oreilly` — canonical form drops the
  apostrophe.
- **Hash-suffix collisions**: when the 6-char `study_id` hash collides
  across two regen runs (rare but observed), the existing slug wins;
  newer file gets a `-2` suffix and a `[REVIEW]` log entry.
- **Underscore vs hyphen**: always normalize to hyphen.

#### 20.5 Reference State

Treat archive commit **`7f0dad1c`** on `shorttack/aberdeen-group-archive`
`main` as the v19 reference state:

- 949 studies
- 19,694 observation rows in `master_observations.csv`
- 100% `verification_method` coverage (distribution in Section 17.5)
- 46.1% viability-prediction verified+partial rate (788 / 1,711)
- Zenodo DOI: `10.5281/zenodo.20245076`
- Wiki sibling commit: `b0f0302` (8,716 pages)

After any master regen, verify the HEAD with:

```bash
cd aberdeen-group-archive && git log origin/main -1 --oneline
# Push warnings about "Bypassed rule violations" or "Changes must be made
# through a pull request" are expected and DO NOT indicate failure.
# The push succeeded if `git log origin/main` shows the new SHA.
```

If row counts or verification distribution diverge materially from
Section 17.5 without an explicit intentional change, halt and
investigate before pushing.

---
