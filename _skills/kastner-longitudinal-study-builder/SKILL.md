---
name: kastner-longitudinal-study-builder
description: "Build longitudinal studies from Pete Kastner's Aberdeen archive in a fresh thread. Use when asked to create, scope, draft, or package a longitudinal study about an entity, technology, vendor, market category, or theme using the Kastner archive, DuckDB, kw ask, wiki pages, and master CSV evidence. v1.2 (2026-07-10) adds the persistent Entity Alias Map protocol — reuse per-cluster entity_alias_map_v1_<cluster>_only.csv (sap/oracle/sybase/informix/ingres/CA/ncr/software-ag/db2/cca) before rebuilding alias clusters; honor KEEP_SEPARATE judgment-call flags; extend via references/gen_alias_maps.py; record-only unless merge is separately approved. v1.1 (2026-07-10) adds the three-phase human-facing flow (Mode A): Phase 1 lock-in dossier, Phase 2 ingest Pete's enriched v2, Phase 3 narrative in Kastner's strong first-person voice with Unicode-superscript citations to an end Citations section (references/convert_citations.py); six-gate archive/wiki integration is Mode B. Enforces Pete's hard master-CSV safety rules."
metadata:
  version: "1.2"
  owner: "Pete Kastner"
---

# Kastner Longitudinal Study Builder

## When to Use This Skill

Use this skill when Pete asks to:

- Build a longitudinal study from the Kastner archive.
- Create a vendor or market-category arc such as Microsoft, HP, Linux/open systems, ERP/SAP, DEC/Tandem/Stratus, IBM, Oracle, Intel, or another archive topic.
- Scope the next longitudinal candidate.
- Produce a read-only candidate packet before writing.
- Draft or package a synthetic longitudinal study for the archive/wiki.
- Use a different model in a new thread to write or compare longitudinal analyses.

Do not use this skill for ordinary queue ingest, PDF extraction, Pass C scoring, or generic DuckDB lookups unless they are part of a longitudinal study build.

## Non-Negotiable Safety Rules

Pete's hard master-CSV rules apply throughout:

1. Do not change the number of master CSV files without Pete's explicit permission.
2. Do not change the number of columns in any master CSV without Pete's explicit permission.
3. Do not change the Mac or repo locations of any master CSV without Pete's explicit permission.
4. Value-only row edits still require dry-run, explicit review, backup, and audit.
5. Default to read-only evidence gathering. Do not write archive files until Pete approves the specific write plan.

Canonical current paths:

- Archive repo / canonical masters: `/Users/scott/Desktop/Archive/aberdeen-group-archive`
- Wiki repo / live query target: `/Users/scott/Repos/kastner-aberdeen-wiki`
- DuckDB: `/Users/scott/Repos/kastner-aberdeen-wiki/db/kastner.duckdb`

## Required Companion Skills

Load these before work begins:

- `duckdb-queries` for read-only SQL and `kw ask`.
- `kastner-archive-pipeline` for rebuild implications and phase discipline.
- `kastner-github` when committing or shipping changes.

If the task involves creating or editing a reusable skill, also load `create-skill`.

## Thread Protocol

Longitudinal studies are best built in a fresh thread so Pete can choose the writing model. In a new thread:

1. Restate the target topic and model preference if Pete supplied one.
2. State that the first phase is read-only candidate/evidence gathering.
3. Ask a clarifying question only if the target is ambiguous enough to change the query plan.
4. Otherwise proceed with a read-only candidate packet.

Keep terminal commands easy to copy/paste if Pete must run them. Say explicitly whether output should be pasted back.

## Two Delivery Modes

There are two ways this skill is used. Pick the mode from what Pete asks for.

- **Mode A — Human-facing study (the three-phase deliverable flow).** Pete wants a readable longitudinal study for people: a data dossier, then an enriched dossier, then a narrative in his voice. This is the default when Pete says "build a longitudinal study," "data extraction and study organization," "do a narrative in Kastner's voice," or attaches a dossier and asks for prose. **See "The Three-Phase Deliverable Flow" below — it is the canonical path and was proven end-to-end on the Databases study (2026-07-09/10).**
- **Mode B — Archive/wiki integration (the six-gate flow).** Pete wants the study packaged INTO the archive/wiki as a synthetic study or wiki page that `kw ask` can retrieve. Use the six-gate flow (below) only when integration is the explicit goal.

The two modes share the same evidence discipline; Mode A's Phase 1 = Gates 1+3, Phase 2 is the enrichment handoff, and Phase 3 = Gate 4. Mode B's Gates 5-6 are only reached if Pete later asks to integrate a Mode-A narrative into the archive.

## The Three-Phase Deliverable Flow (Mode A — canonical)

This is the flow Pete most often wants. Each phase produces a **versioned Markdown artifact** in `/home/user/workspace/` that is shared with Pete and becomes the input to the next phase. **Pause after each phase** — Pete reviews, sometimes hand-enriches, and returns the next version.

### Phase 1 — Lock in the dossier (data extraction + organization, NO narrative)

Goal: a complete, read-only evidence base organized to Pete's requested chapter outline, with **no interpretive prose**. This is Gates 1+3 fused into one deliverable.

Steps:

1. **Clarify scope up front** with `ask_user_question` when it changes the query plan. The four questions that mattered on the Databases build: (a) alias handling, (b) whether to foreground Pete's personal role / Path-B layer, (c) deliverable form (single dossier vs. dossier + CSVs), (d) timeframe bounds.
2. **Resolve aliases using the persistent alias maps (reuse before rebuild).** The masters are heavily alias-fragmented (Oracle had 6+ entity IDs, Informix ~10, CA ~9, Ingres/Sybase/NCR split). **Do not re-derive clusters from scratch** — a growing library of per-cluster alias maps already encodes this work. See the "Entity Alias Map" section below for paths, schema, and the reuse/extend/contribute protocol. In short: load any existing `entity_alias_map_v1_<cluster>_only.csv` for your topic's vendors and use its `alias_entity_id → canonical_entity_id` rows to build the read-only consolidation CTE; only build a new cluster map when none exists; always report **consolidated totals plus a per-alias appendix**. Alias resolution here is **analytical only** — never edit masters to merge unless Pete explicitly approves under `kastner-archive-pipeline`.
3. **Extract via SQL**, not `kw ask`, for everything quantitative: consolidated vendor/tech volume, 5-year-bucket timeline, per-chapter study inventories (title, year, study_id, type, obs count, ★=Pete-authored), representative verbatim observation quotes per chapter, and the prescience layer (enum + mean + n).
   - Write the extraction as a `.sql` file, push to the Mac (`pc push`), run read-only via `/opt/homebrew/bin/duckdb -readonly ... -c ".read <file>"`, and pull the output back. Do NOT hand-fire dozens of interactive queries.
   - **Runtime for Phase 1.** The extraction itself is SQL and requires no LLM. Interpretive synthesis over the extracted dossier defaults to cloud (breadth over the full archive context) but has two legitimate local warrants: (a) narrow entity-alias sanity checks where the answer is a lookup against `entity_alias_map_v1_*.csv`, and (b) `kw ask` retrieval passes when the sandbox blocks `localhost:11434` — in that case Hybrid (PPLX runtime) is a first-class substitute because it runs local without going through the bridge sandbox. Never route master-CSV-bound extraction through Hybrid until PPLX clears the standard fixture gates.
4. **Assemble a single chapter-mapped dossier** (`<TOPIC>_DOSSIER_v1.md`): §0 method + alias map + consolidated volume, one section per requested chapter with evidence tables and quotes, a per-alias appendix, a **data-quality / gaps** section (flag under-tagged or sparse threads honestly), and a full study_id index by chapter.
5. **Mark synthetic studies** (e.g. `2026-*` longitudinal and `volume-1-*` memoir chapters are Pete/Perplexity assemblies) so they are cited as scaffolding/secondary, not period-primary.
6. Share the dossier. **Pause.** Pete may return an enriched `v2`.

### Phase 2 — Dossier ingest (accept Pete's enriched dossier)

Goal: read whatever Pete hands back and make it the source of truth for the narrative.

- Pete typically returns a **`_v2` dossier** with material only he knows: private engagements, personal connections, off-archive facts (e.g. on the Databases build he added the Yankee Group ghostwrite, TPC founding/auditor role, the Software AG TP-1 audit for Roel Pieper, the Unisys/Florida-HRS expert-witness case, the CCA personal connection). **Read the attached v2 in full** before writing — do not write from your Phase-1 memory.
- Treat Pete-supplied facts as authoritative for voice/biography even when they are not in the archive. Where a claim is not archive-backed, keep it but do not attach a fake study citation — cite only real study_ids, and let Pete-supplied context stand on his authority.
- If v2 introduces new study_ids, verify they resolve in `v_studies`; if not, keep them but flag as unverified in the gaps note.
- **Runtime for Phase 2.** Reading the v2 dossier is a factual-extraction task and a natural fit for local when the enrichment is dense or Pete wants the ingest to be reproducible without cloud credits. Cloud remains the default when the v2 introduces material Pete wants cross-checked against the broader web (unverified study_ids, third-party names, dated engagements) — that check needs cloud retrieval and there is no privacy reason to withhold the v2 from it.

### Phase 3 — Narrative in Kastner's strong first-person voice, with superscript citations

Goal: a readable, human-facing longitudinal narrative written **in Pete's voice**, argued to whatever thesis Pete specified, with **inline superscript citation numbers pointing to an end-of-document Citations section**.

Voice rules (Kastner's "strong voice"):

> **Canonical voice spec:** `Perplexity_Only/kastner_voice_prompt_v1.md` (archive repo, Pete-provided 2026-07-15) is the definitive reference — the full Identity / Voice Architecture / 8 rhetorical moves / diction / 6-lens framework. **Read it before drafting any Kastner-voice narrative.** The rules below are the working distillation. **Pete's standing guidance (2026-07-15): draw from the prompt as a palette; do NOT slavishly hit every item every time.** Deploy each move only where it earns its place — not every study needs a literary allusion or a supply-chain telescope.

Core (always on):
- **First person throughout** ("I," "my franchise"). Confident, opinionated, plain-spoken; short declarative punches mixed with longer analytical sentences. Practitioner-who-became-an-analyst authority — never academic-outsider.
- **The we/I split:** "we/we believe/we recommend" for firm (Aberdeen) positions; "I believe / I conclude / my conclusion is" for personal expert judgment. Own the opinion explicitly.
- **State the thesis in a prologue and return to it** — Pete argues to a point, he does not hedge to neutrality. Favor the Contrarian Opening: lead with what the data shows vs. what the marketing says.
- **Own the misses as squarely as the hits.** A "what I got right / what I got wrong" reckoning is part of the voice, not an afterthought. Distinguish scorer prescience from Pete-authored Path-B verdicts.
- **The Data Anchor — concrete numbers over adjectives.** TPS, tpmC, dollars-per-transaction, market sizes, percentage shares, prescience means. "Turn the marketing into arithmetic." Prefer ranges/thresholds over false precision. Drop weakening qualifiers ("somewhat," "perhaps," "it could be argued").
- **No invented facts.** Every period claim traces to a real study_id (Phase-1 dossier) or a Pete-supplied fact (Phase-2 v2). Mark gaps explicitly rather than papering over them.

Draw-from-as-warranted (the 8 signature moves — use where they fit, not by rote):
- **Proof-Point Dismantling:** walk a vendor's benchmark/capability claims one by one, show why the methodology/comparison/timeline is flawed, end each with a pithy dismissal ("We'll keep our money in a real bank." "No big deal.").
- **Supply-Chain Telescope:** zoom from the technology out to its position in the global economic system — second- and third-order effects.
- **Historical Through-Line:** connect the present to structural patterns across decades; cite Pete's own prior Aberdeen work by date ("Aberdeen's Market Viewpoint in November 1995 said...") — using REAL study_ids only.
- **Customer-Centric Reframe:** redirect vendor-focused points back to the IT executive deciding today — real costs, risks, timelines.
- **Direct Address:** occasional fourth-wall breaks ("Mark down March 12th, 2003 on your computer-history calendar").
- **Cultural/literary allusion:** sparingly, only to make a hard point vivid (Sagan, Andersen, military/weather metaphors) — never decoration.
- **Register-shift** to fit the passage: informed-conversational default, up to formal-analytical for the methodological spine, down to blunt-editorial for the verdicts.
- **Diction markers:** "price/performance" (always slashed), "Bottom line:" as a verdict header, "Make no mistake," "sea change," "leading-edge," em-dash asides, precision parentheticals. Define any acronym on first use.
- **Temporal calibration:** period sections use period vocabulary; retroject no current terminology. From the 2026 vantage you may draw on outcomes Pete predicted.
- **Do not worry about length** unless Pete caps it. Add sections for continuity where the arc needs them.

Citation mechanics (**the locked format**):

- Draft with inline `[study-<id>]` tags immediately after each sentence carrying that evidence (easy to author and to machine-convert).
- Then convert to **Unicode superscript numbers** in first-appearance order, with an end-of-document `## Citations` section mapping each number to its `study-<id>`. Use a small deterministic script (see `references/convert_citations.py`) — never renumber by hand.
  - Unicode superscripts (¹ ² ³ … ⁵⁰) render in any Markdown viewer, not just HTML.
  - Collapse consecutive duplicate cites to one marker; join distinct adjacent cites with a thin space (e.g. ⁵³ ⁵⁴).
  - The Citations list may show bare `study-<id>` slugs; if Pete wants a human-facing render (PDF/DOCX), offer to swap in study titles + years with the slug in monospace after.
- Keep a provenance footer describing the citation scheme and flagging synthetic-study usage + any deferred `kw ask` enrichment.

Share the narrative (`<TOPIC>_NARRATIVE_v1.md`). Rewrites (voice, citation format, length) bump the version and reuse the same `share_file` `name` for version history.

**Runtime for Phase 3.** Cloud is the current default because no locked fixture yet exists for Kastner-voice narrative drafting, and voice fidelity to `kastner_voice_prompt_v1.md` is the accuracy criterion that matters. This is under active revision:

- The Databases study (`DB_LONGITUDINAL_DOSSIER_v2.md` → `RDBMS_NARRATIVE_KASTNER_v1.md`) is the designated Phase-3-narrative fixture pending Pete's approval. Once frozen, it becomes the yardstick.
- The Lane-C bakeoff runs cloud frontier vs. current Ollama incumbent (Qwen 3.5 27B MLX) vs. PPLX Qwen 3.8 27B via Hybrid, judged by Pete on voice + factual fidelity. See `local-model-upgrade-gates` → Kastner-voice narrative workload.
- **The 64GB M5 Pro Mac mini (arriving October 2026) changes what “local” can mean for this workload.** At 64GB unified memory a substantially larger MLX model becomes viable — rerun the bakeoff after cutover with any new candidate that clears Gates 0–4.
- Until the bakeoff concludes, run local narrative drafts in parallel with cloud on any study Pete authorizes as a comparison; do not silently substitute.

### `kw ask` availability caveat (both phases)

`kw ask` needs local Ollama on `localhost:11434`, which the **sandboxed `pc bash` shell cannot reach** (localhost socket connect is blocked). So during extraction, rely on **read-only SQL** (fully current) and treat `kw ask` interpretive synthesis as a **deferred enrichment step** Pete runs directly, or that runs when the environment allows. Note it in the dossier/narrative gaps section rather than blocking on it.

## Entity Alias Map (reuse this before rebuilding clusters)

The archive carries a growing library of **per-cluster entity alias maps** that already encode the alias-resolution work for major vendors. When a new narrative touches a vendor that already has a map, **reuse it** rather than re-deriving clusters from the masters. This keeps canonical-survivor choices consistent across studies and saves the whole Phase-1 alias probe.

### Where the maps live

- Canonical location (archive repo root): `~/Desktop/Archive/aberdeen-group-archive/entity_alias_map_v1_<cluster>_only.csv`
- Mirror in `scripts/` for the ones shipped with an apply script.
- As of 2026-07-10 the library covers: `sap` (the original), plus `oracle`, `sybase`, `informix`, `ingres`, `computer-associates`, `ncr`, `software-ag`, `ibm-db2`, `cca`. Check the repo root for the current set before assuming a cluster is missing:
  ```bash
  ls ~/Desktop/Archive/aberdeen-group-archive/entity_alias_map_v1_*_only.csv
  ```

### Schema (9 columns, one file per cluster, one CANONICAL_SURVIVOR per file)

`alias_entity_id, alias_entity_name_as_stored, alias_occ, alias_study_refs, disposition, canonical_entity_id, confidence, source_rule, review_notes`

- `disposition` is one of `CANONICAL_SURVIVOR` | `MERGE_INTO` | `KEEP_SEPARATE`.
- `alias_occ` == `alias_study_refs` == distinct `study_id` count from `_master_entity_studies.csv` for that `entity_id`.
- Survivor = the highest-study-ref id in the cluster.
- `KEEP_SEPARATE` rows are NOT aliases: subsidiaries (e.g. `oracle-norge-as`, `ncr-norge-as`), persons (`paul-wahl-sap`), and flagged judgment calls (see below).

### How to USE a map in Phase 1 (read-only consolidation)

Build the analytical consolidation CTE straight from the map instead of hand-listing ids:

```python
# read the cluster map -> {alias_entity_id: canonical_entity_id} for MERGE_INTO + CANONICAL_SURVIVOR
import csv
def cluster_ids(path):
    keep, merge = set(), {}
    for r in csv.DictReader(open(path)):
        if r["disposition"] in ("CANONICAL_SURVIVOR", "MERGE_INTO"):
            merge[r["alias_entity_id"]] = r["canonical_entity_id"]
    return merge   # every alias id -> its canonical survivor
```

Then the SQL consolidation groups observations by the canonical id. Report consolidated totals AND the per-alias appendix (the map rows ARE the appendix). Respect `KEEP_SEPARATE`: do not fold those ids into the survivor in the analytical rollup unless Pete rules otherwise for this study.

### Judgment calls carried in the maps (honor the flags)

Some clusters carry `confidence=low/medium` `KEEP_SEPARATE` rows that are genuine open questions Pete has not ruled on. Do not silently merge them; surface them in the dossier gaps note and ask if it matters for the study. Known open ones (2026-07-10):

- **NCR:** whether the AT&T-GIS era (`att-gis`, `att-gis-ncr`) and Teradata (`teradata*`, `ncr-teradata`) fold into `ncr-corporation` or stand as distinct entities.
- **CA vs Ingres:** whether CA-Ingres ids (`ca-ingres`, `ENT-CA-INGRES`, `computer-associates-international-ca-ingres`) belong to the CA cluster or the independent Ingres story.
- **Sybase:** whether `powersoft-sybase` (the 1995 Powersoft/PowerBuilder acquisition) is its own product identity.

### How to EXTEND / CONTRIBUTE a map

- **New cluster (no map exists):** build it with the same schema. The generator pattern lives at `references/gen_alias_maps.py` (drives from a probe of `_master_entities.csv` + `_master_entity_studies.csv`; survivor = max study-refs; persons/subsidiaries/ambiguous -> `KEEP_SEPARATE` with a review note). Emit `entity_alias_map_v1_<cluster>_only.csv`.
- **Newly discovered alias for an existing cluster:** add a `MERGE_INTO` row (bump nothing else); keep one survivor.
- These maps are **record-only** by default. Any actual master merge is a separate, explicitly-approved step under `kastner-archive-pipeline` (dry-run -> Pete review -> `--commit`), driven by `scripts/apply_entity_aliases_v2_sap.py` (which reads exactly this schema, one cluster file at a time).
- Ship new/updated maps through the EOD `kastner-github` batch, not mid-session.

## Six-Gate Flow (Mode B — archive/wiki integration)

Use this only when the explicit goal is to package a study INTO the archive/wiki. The build has six gates:

1. Candidate packet.
2. Scope and thesis approval.
3. Evidence extraction.
4. Draft longitudinal study.
5. Packaging plan.
6. Optional archive/wiki integration after explicit approval.

Stop for Pete review after gates 1, 2, and 5.

## Gate 1: Candidate Packet

Goal: prove the topic has enough longitudinal signal before writing.

Use read-only DuckDB or `kw ask` only. Prefer exact SQL for counts and `kw ask` for synthesis.

Produce a short packet with:

- Candidate title.
- Topic definition: included entities, technologies, aliases, and exclusions.
- Year span and decades covered.
- Number of distinct studies.
- Number of observations.
- Count of observations attached to high-prescience studies.
- Top supporting studies by relevant observation count.
- Top related entities and technologies.
- Potential pitfalls: alias collisions, overbroad topic, already-existing longitudinal page, sparse decades, or source contamination.

Suggested SQL pattern:

```sql
WITH obs AS (
  SELECT
    o.obs_id,
    o.study_id,
    o.entity_id,
    o.tech_id,
    TRY_CAST(o.year_observed AS INTEGER) AS obs_year,
    s.title,
    s.pub_year,
    s.study_prescience_enum,
    s.prescience_mean
  FROM v_observations o
  JOIN v_studies s USING (study_id)
  WHERE TRY_CAST(o.year_observed AS INTEGER) BETWEEN 1960 AND 2026
    AND (
      o.entity_id IN ('<entity-id-1>', '<entity-id-2>')
      OR o.tech_id IN ('<tech-id-1>', '<tech-id-2>')
    )
)
SELECT
  MIN(obs_year) AS first_year,
  MAX(obs_year) AS last_year,
  MAX(obs_year) - MIN(obs_year) AS span_years,
  COUNT(DISTINCT (obs_year // 10) * 10) AS decades,
  COUNT(DISTINCT study_id) AS studies,
  COUNT(*) AS observations,
  SUM(CASE WHEN study_prescience_enum = 'high' THEN 1 ELSE 0 END) AS high_prescience_obs
FROM obs;
```

For exact local queries, use the `duckdb-queries` skill. Open the database read-only.

## Gate 2: Scope and Thesis Approval

Before writing the study, propose:

- Working title.
- Included IDs.
- Excluded IDs.
- Timeframe.
- Three to five candidate thesis statements.
- Proposed section outline.
- Expected output type: markdown study draft, wiki page draft, or archive package.

Ask Pete to approve or revise the scope. Do not proceed to drafting until the scope is approved.

## Gate 3: Evidence Extraction

After scope approval, extract evidence into a compact working dossier:

- Chronological timeline: 10-20 turning points.
- Study inventory: top 10-25 studies with title, year, study_id, prescience enum, and why relevant.
- Observation inventory: best representative observations by decade and subtheme.
- Entity/technology graph: top co-occurring entities and technologies.
- Prescience layer: where Aberdeen/Pete was early, right, wrong, or ambiguous.
- Counterevidence: studies or observations that complicate the thesis.

Use `kw ask` to synthesize interpretive arcs only after SQL has established the evidence base.

## Gate 4: Draft Longitudinal Study

Default output is Markdown unless Pete requests another format.

Recommended structure:

```markdown
# <Title>

## Abstract

## Research question

## Scope and method

## Chronological arc

## What the archive got right

## What the archive missed or overestimated

## Vendor/category strategy implications

## Key evidence table

## Open questions and next work
```

Writing rules:

- Keep claims grounded in archive evidence.
- Distinguish scorer prescience from Pete-authored Path B rebuttals where relevant.
- Use `study_id`, title, and year in evidence tables.
- Do not invent missing facts. Mark gaps explicitly.
- Prefer a concise analytical narrative over a raw dump of observations.

## Gate 5: Packaging Plan

Before writing files into the archive or wiki, present a packaging plan:

- Target file path(s).
- Whether this is a synthetic/generated study, a wiki page only, or both.
- Whether any master CSV value edits are proposed.
- Whether Phase 1-6 rebuild steps are required.
- Whether embeddings need recomputing.
- Commit plan for archive repo and wiki repo.

Stop and ask Pete for explicit approval.

## Gate 6: Optional Archive/Wiki Integration

Only after approval:

- If creating a wiki-only page, write under the wiki repo and run the necessary downstream phases, usually Phase 5 if retrieval should see it.
- If creating a synthetic archive study, use the archive pipeline's established package conventions and get explicit approval for any master value edits.
- Do not add master CSV files, columns, or relocate masters unless Pete explicitly approves those exact changes.
- After any wiki markdown changes, consider Phase 5 embeddings stale until recomputed.

Use the canonical phase chain when a full or partial rebuild is needed. **Prefer the orchestrator** `pipeline_canonical_v3.sh` (pins the Python interpreter; see `kastner-archive-pipeline` Gotcha 14) over hand-invoking phases. Canonical script versions as of 2026-07-09:

| Phase | Script |
|---|---|
| 1 | `scripts/build/01_load_csvs_v3.py` |
| 2 | `scripts/build/02_build_data_layer_v5.py` |
| 0 | `scripts/build/07_audit_masters_v1.py` (regression gate, runs after Phase 2) |
| 3 | `scripts/build/03_generate_vault_v3.py` (tier-1 LLM, ~6.5h) |
| 4 | `scripts/build/04_generate_indices_v6.py` |
| 5 | `scripts/build/05_compute_embeddings_v3.py` |
| 6 | `scripts/build/06_emit_scaffolding_v2.py` |

Always defer to `kastner-archive-pipeline` for the authoritative version chain and rebuild discipline — it is updated more often than this table.

## Candidate Ranking Heuristic

When Pete asks for "next candidates," rank topics by:

- Year span.
- Decades covered.
- Distinct study count.
- Observation count.
- High-prescience observation count.
- Topic coherence after alias cleanup.
- Whether a longitudinal page already exists.
- Writing value: likely to produce a coherent argument rather than a generic vendor profile.

Exclude or down-rank archive-self entities such as `aberdeen-group`, `peter-s-kastner`, and duplicate person aliases unless Pete explicitly wants a meta-study.

## Known Strong Candidate Families

Previously identified strong candidates include:

- Microsoft enterprise-platform evolution.
- Hewlett-Packard and the post-minicomputer enterprise vendor arc.
- DEC/Tandem/Stratus fault-tolerant computing lineage.
- ERP and SAP R/3 lifecycle.
- Linux and open-systems disruption.

Treat these as starting points, not as fixed priorities. Re-query the archive in the new thread before writing.

## Output Discipline

For a candidate packet, answer in chat.

For a long draft, write a Markdown file and share it, unless Pete asks to paste inline.

For EOD or commits, follow `kastner-github`: stage known files only, avoid bycatch, and use clear commit messages.

## Example User Prompts

- "Use this skill to build the Microsoft longitudinal study." (Mode A, all three phases)
- "Data extraction and study organization short of narrative writing." (Mode A, Phase 1 only)
- "Now do a narrative for humans in Kastner's voice using the dossier." (Mode A, Phase 3)
- "Rewrite the narrative with superscript citation numbers to an end-of-document Citations section." (Phase 3 citation-format pass)
- "Scope HP as the next longitudinal candidate."
- "Draft the ERP/SAP R/3 longitudinal study, but do not write archive files yet."

## Worked Example: The Databases Study (2026-07-09/10)

The canonical end-to-end run of Mode A, referenceable as the template:

- **Phase 1:** `DB_LONGITUDINAL_DOSSIER_v1.md` — 80/20 RDBMS focus, alias-resolved (Oracle 406 obs/74 studies consolidated from 6+ IDs, etc.), 5-yr timeline, six chapter inventories, Pete-authored ★ layer, prescience scores, per-alias appendix, gaps note. Extraction via `db_study_extract_v1.sql` + `db_study_quotes_v1.sql` run read-only on the Mac.
- **Phase 2:** Pete returned `DB_LONGITUDINAL_DOSSIER_v2.md` adding the Yankee Group ghostwrite, TPC founding/auditor role, Software AG TP-1 audit for Roel Pieper, Unisys/Florida-HRS expert-witness case, and the CCA personal connection.
- **Phase 3:** `RDBMS_NARRATIVE_KASTNER_v1.md` — prologue + 9 chapters in Pete's first-person voice, thesis = "database/RDBMS performance work was the high point of the Aberdeen career." `v2` converted 116 inline tags → 66 unique Unicode-superscript citations + end `## Citations` section via `convert_citations.py`.
