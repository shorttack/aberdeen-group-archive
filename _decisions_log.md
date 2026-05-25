# Kastner IT Research Archive — Decisions Log

This file records curatorial decisions, data-hygiene actions, and structural choices made during the life of the archive. Entries are appended; nothing is rewritten in place. Each entry is timestamped and references the tarball backup taken before any mutation.

Companion files:
- [`README.md`](./README.md) — archive overview and quickstart
- [`CHANGELOG.md`](./CHANGELOG.md) — semver release history (if present)
- This file — full curatorial reasoning behind those releases

---

## v1.4 — 2026-05-23 / 2026-05-24

**Theme**: Weekend ingest of 490 new studies, two data-hygiene fixes, companion-wiki build.

### 2026-05-24 17:30 EDT — "32 missing studies" investigation: closed, none missing

**Context.** During v1.4 planning, the operator flagged "32 missing studies" as an open item from the 2026-05-23 ingest. Investigation across all seven bucket logs (mode1 buckets A–E, mode2 existing, phase1 progress) found **36 lines matching `FAIL|ERROR`**. Detailed inspection showed **all 36 are MuPDF library warnings** of the form:

- `MuPDF error: format error: cmsOpenProfileFromMem failed` — cosmetic ICC color-profile warning
- `MuPDF error: format error: No default Layer config` — optional-content layer warning

Both are non-fatal stderr messages emitted by MuPDF when *opening* a PDF; text extraction proceeds normally afterward. Counts by bucket:

| Bucket | total "error" lines | MuPDF noise | real errors |
|---|---:|---:|---:|
| A | 2 | 2 | 0 |
| D | 24 | 24 | 0 |
| E | 10 | 10 | 0 |

**No Python tracebacks, no exceptions, no `failed to process` lines across any log.**

**Disposition.** All 494 prepared folders ingested successfully (493 OK + 1 not-ready). The "32" was a phantom count; no studies are missing. Investigation closed. No action taken.

### 2026-05-24 13:00 EDT — Case-collision merge across entity & technology masters

**Context.** During v1.4 master regeneration we detected duplicate slug rows differing only in case (e.g. `JAVA` vs `java`, `Sun Microsystems` vs `sun microsystems`). The pre-merge masters had 1,443 studies; the deduped run produced 1,434 — a 9-row reduction.

**Action.** A case-folding merge was performed on the entity and technology caches; the canonical form (typically the first-seen capitalization or the one already in the deduped cache) was kept. The collision merge produced the following master counts:

| File | Pre-merge | Post-merge | Δ |
|---|---:|---:|---:|
| `_master_studies.csv` | 1,443 | 1,434 | −9 |
| `_master_entities.csv` | — | 3,207 | — |
| `_master_technologies.csv` | — | 4,313 | — |
| `_master_observations.csv` | — | 23,605 | — |

**Backup**: pre-merge tarball captured in the standard masters tarball cadence (`archive_masters_tarball`).

**Verify-then-write status.** ✅ Confirmed downstream. The vault built from the cleaned masters disambiguates remaining case-similar pairs at the slug layer (e.g. `java.md` / `java-2.md`) per the v3/v4 vault builder.

### 2026-05-24 19:38 EDT — Java/PDA carve-out (Option A: merge `java` → `JAVA`, drop misfiled row)

**Context.** The case-merge surfaced a second-order problem: `_master_technologies.csv` contained a row with `tech_id="java"` whose body content was clearly Java programming-language data (vendor "Sun Microsystems / Oracle", era "1.0 (initial release 1995)", notes citing Java 21 LTS) — but whose `tech_name` field said **"PDA (personal digital assistant)"**. The misfile likely originated upstream of master regeneration (an entity- or technology-extraction step that crossed a wire when two distinct tech rows were merged).

A separate `tech_id="JAVA"` row (uppercase) already existed in the master, correctly labeled "Java Programming Language", and is the canonical Java entry. PDA is already represented as `tech_id="pda"`, `tech_id="pda-hardware"`, and `tech_id="pda-mobile-devices"`.

**Option chosen: A — merge `java` → `JAVA` across reference tables, drop the misfiled row.** Rationale: creating a corrected lowercase `java` row would re-introduce a case collision identical to the one just merged. The uppercase `JAVA` row already contains the canonical Java metadata; the misfiled row's content is redundant with it.

**Script**: `fix_java_pda_carveout_v1.py` (dry-run-then-write; tar backup before any mutation; atomic .tmp+rename writes).

**Pre-mutation backup**: `/Users/scott/Desktop/Archive/archive_masters_backup_pre_java_fix_20260524_193807.tar.gz` (5.2 MB).

**Action.** 91 rows re-pointed and 1 row dropped:

| File | lowercase `java` rows pre | uppercase `JAVA` rows pre | post-merge upper count | dupe rows collapsed |
|---|---:|---:|---:|---:|
| `_master_observations.csv` | 54 | 2 | 56 | 0 |
| `_master_tech_studies.csv` | 28 | 1 | 29 | 0 |
| `_master_tech_field_conflicts.csv` | 7 | 0 | 7 | 0 |
| `_known_technologies.csv` | 1 | 1 | 1 | 1 |
| `_master_technologies.csv` | 1 (dropped) | 1 (kept) | 1 | — |

Master technology row count: **4,313 → 4,312**.

**Verify-then-write status.** ✅ Post-write greps confirm:
- 0 rows in `_master_technologies.csv` matching `^"java",`
- 1 row matching `^"JAVA",`
- 0 residual `"PDA (personal digital assistant)"` strings in `_master_technologies.csv`
- File line count = 4,313 (4,312 data rows + 1 header)

### 2026-05-23 / 2026-05-24 — Weekend bucket ingest (+490 studies)

**Mode**: Bucket-classifier-driven ingest using `archival-ingest` skill v20.

**Buckets processed**:
- mode1 buckets A, B, C, D, E (new material classified by content type)
- mode2 existing (re-evaluation of already-archived material)

**Disposition** (494 prepared folders): 493 OK + 1 not-ready. See "32 missing studies" entry above for the full investigation of the apparent fail count.

**Physical landing**: 493 of the 494 new studies are physically located in `prepared/` as of v1.4 release, fully registered in the masters and indexed in the companion wiki but not yet classified into `kastner-author/`, `other-authors/`, or `employer/*` subtrees. Promotion is a **v1.5 backlog item**.

**Prescience scoring**: All 370 of the newly-ingested studies marked as `[DEFERRED]` in `prescience` pending the Pass C scoring run, also a **v1.5 backlog item**.

### 2026-05-24 — Companion wiki (Kastner Aberdeen Wiki) v3/v4 build

**Output**: 8,960-page Obsidian vault at `../kastner_wiki/` (relative to `aberdeen-group-archive/`).

**Pages**:
- 1,434 study pages
- 3,207 entity pages
- 4,313 tech pages
- + index, dashboard, README, AGENTS.md, chat-starter.md, Bases

**Wikilinks**: 3,682 study→entity links + 5,253 study→technology links (emitted explicitly by the v4 builder so Dataview reverse-lookups work on entity and technology pages).

**Builder skill**: `kastner-wiki-builder` (custom user skill). v3 introduced explicit study→entity/tech wikilink emission; v4 removed empty Dataview blocks for observations (no observation pages exist in the vault) and replaced them with obs counts plus DuckDB SQL hints.

**Slug disambiguation**: One case-collision survived to the wiki layer and was disambiguated at slug emission time: `java.md` (Java Programming Language, the surviving uppercase `JAVA` master row) and `java-2.md` (a remnant pointing at PDA content prior to the master fix). The `java-2.md` page will resolve correctly on the next vault rebuild after a fresh DuckDB load against the v1.4 masters (deferred Pass C work).

**Backup**: `/Users/scott/Desktop/Archive/kastner_wiki_backup_v1.4_20260524_193848.tar.gz` (2.1 MB, 8,985 tarball entries = 8,960 pages + directories).

**DuckDB state at v1.4**: DuckDB build trails masters by one generation (still shows 3,242 entities / 4,337 techs). Per operator decision this is acceptable — the vault was built from the cleaned masters, and Pass C scoring (v1.5) will trigger a natural DuckDB rebuild against the v1.4 masters.

---

## Versioning conventions

- All mutation scripts versioned `_v1`, `_v2`, … from creation; bump on every revision.
- Every mutation is preceded by a tar backup of the affected directory, named with timestamp and reason.
- Verify-then-write: every script supports dry-run; commits are gated behind `--write` or equivalent.
- Atomic CSV writes: `.tmp` file + `os.replace()`; never edit in place.
- Excel is not trusted for CSV edits in this archive — Python with `csv.writer(quoting=QUOTE_ALL)` is the only sanctioned write path (per §16.5 of the ingest skill).
