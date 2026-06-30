---
name: duckdb-queries
description: "Open read-only DuckDB connections to Pete Kastner's Aberdeen archive and answer questions over it. Use when asked to query the archive, run DuckDB/SQL against kastner.duckdb, count/list studies-observations-entities-technologies, attach or scan parquet/master CSVs under ~/Repos or ~/Desktop/Archive, ask the wiki a question, run kw ask, or do semantic/RAG retrieval over the wiki. Prefers the 'Perplexity bridge v2' MCP connector for read-only SQL from chat; falls back to the duckdb CLI on the Mac via pc; wraps Pete's kw ask CLI for embedding/RAG questions."
license: MIT
metadata:
  author: pete-kastner
  version: '1.0'
---

# DuckDB Queries — Kastner Aberdeen Archive

Read-only query access to the Kastner Aberdeen archive: the 27-view DuckDB query
layer, the parquet exports, and the master CSVs — plus a wrapper around Pete's
`kw ask` RAG CLI for semantic/embedding questions.

## When to Use This Skill

- "Query the archive" / "run SQL against kastner.duckdb" / "how many studies/observations/entities/technologies"
- "Top prescient studies", "prescience by decade", "studies with high prescience"
- "Attach the parquet files" / "scan the master CSVs" / cross-file ad-hoc joins under `~/Repos` or `~/Desktop/Archive`
- "Ask the wiki ..." / "kw ask ..." / semantic search / RAG retrieval over wiki pages
- Any read-only analytical question over the archive

This skill is **read-only by contract**. Never write, INSERT, UPDATE, DELETE,
CREATE, or ATTACH read-write. For pipeline changes (master edits, rebuilds,
Pass C) use `kastner-archive-pipeline`, not this skill.

## Execution Paths (prefer connector, fall back to CLI)

There are three ways to run a query. Choose in this order:

### 1. MCP connector "Perplexity bridge v2" (DEFAULT for SQL from chat)
Already read-only, no setup, works from chat. Tools:
- `duckdb_query` — run one read-only statement (SELECT / WITH / DESCRIBE / EXPLAIN / SHOW / introspection PRAGMA). Auto-appends `LIMIT 100` if no top-level LIMIT.
- `duckdb_tables` — list all tables/views.
- `duckdb_describe` — `DESCRIBE <name>` for one relation.
- `bridge_info` — health/paths check.

Call via `call_external_tool(source_id="perplexity_bridge_v2_1598b152eeab4c7abc71b346b9005a2e", tool_name=..., arguments=...)`.
Always `describe_external_tools` once per tool before first call in a session.

If the connector is DOWN (`Name or service not known`, timeout, or non-200),
it is almost always the ngrok tunnel — see "Tunnel recovery" below — then fall
back to path 2 for the immediate query.

### 2. duckdb CLI on the Mac via `pc` (fallback, bulk, or local attach/scan)
Use when the connector is down, for bulk output, or to attach/scan parquet+CSV
across both roots. **Always open the DB read-only.**

```bash
pc device use 2B7787DE-86A2-5702-AD55-2FFA28AB9D56   # once per session
# run a query (api_credentials=["pc"] on every pc bash call):
pc bash -- '/opt/homebrew/bin/duckdb -readonly /Users/scott/Repos/kastner-aberdeen-wiki/db/kastner.duckdb -c "SELECT COUNT(*) FROM v_studies;"'
```

Quoting gotcha: nested quotes through `pc bash` mangle easily. For anything
non-trivial, write the SQL to a temp file first and `.read` it:

```bash
printf '%s\n' "SELECT ... ;" | pc files write /tmp/q.sql
pc bash -- '/opt/homebrew/bin/duckdb -readonly /Users/scott/Repos/kastner-aberdeen-wiki/db/kastner.duckdb -c ".read /tmp/q.sql"'
```

Or use the bundled helper `scripts/run_query.sh` (see below).

### 3. `kw ask` wrapper (semantic / RAG / embedding questions)
For natural-language questions that need retrieval + LLM synthesis (not exact
SQL), wrap Pete's CLI. **`kw` is not on the non-login PATH** — always call it by
absolute path `/Users/scott/bin/kw`.

```bash
pc bash -- '/Users/scott/bin/kw ask "what did Aberdeen get right about cloud computing?"'
```

Decision rule:
- Exact/quantitative ("how many", "list", "top N by score") → SQL (path 1 or 2).
- Interpretive/semantic ("what did they get right about X", "summarize the thesis") → `kw ask` (path 3).
- Mixed → run SQL for the numbers, then `kw ask` for the narrative.

## Canonical paths & constants

- Device: Mac mini (2) M4 Pro — `2B7787DE-86A2-5702-AD55-2FFA28AB9D56` (run `pc device use ...` first; `api_credentials=["pc"]` on every pc call).
- DuckDB: `/Users/scott/Repos/kastner-aberdeen-wiki/db/kastner.duckdb` (27 views)
- duckdb CLI: `/opt/homebrew/bin/duckdb` (open with `-readonly`)
- venv python w/ duckdb 1.5.4: `/Users/scott/Repos/mac_mcp_bridge/.venv/bin/python`
- kw CLI: `/Users/scott/bin/kw` (impl: `/Users/scott/Repos/kastner-aberdeen-wiki/bin/kw`)
- Wiki root (KW_ROOT): `/Users/scott/Repos/kastner-aberdeen-wiki`
- Archive root: `/Users/scott/Desktop/Archive`
- Archive repo (masters live at ROOT, not under master_csvs/): `/Users/scott/Desktop/Archive/aberdeen-group-archive`
- Parquet exports: `/Users/scott/Repos/kastner-aberdeen-wiki/data/*.parquet` and `.../data/_validated/*.parquet`
- MCP connector source_id: `perplexity_bridge_v2_1598b152eeab4c7abc71b346b9005a2e`
- MCP permanent URL: `https://dolphin-washer-slush.ngrok-free.dev/mcp`

Shape sanity check (current baseline): `v_studies` ≈ **1454**.

## The 27 views

Full catalog with one-line purpose in `references/views.md` — read it before
composing a query so you pick the right view instead of raw masters. Most-used:
`v_studies`, `v_observations`, `v_entities`, `v_technologies`,
`v_top_prescient_studies`, `v_studies_with_high_prescience`,
`v_prescience_by_decade`, `v_observations_with_prescience`,
`v_entity_studies`, `v_tech_studies`, `v_collection_overview`.

Discover columns with `duckdb_describe` (connector) or `DESCRIBE <view>` (CLI).

## Attaching / scanning parquet + master CSVs (path 2 only)

The DuckDB file already exposes the views; reach for raw files only for ad-hoc
cross-file work or to inspect a master not surfaced by a view.

```sql
-- parquet (preferred — typed, validated copies live under data/_validated/)
SELECT * FROM read_parquet('/Users/scott/Repos/kastner-aberdeen-wiki/data/_validated/studies.parquet') LIMIT 5;

-- master CSV at archive repo ROOT (note leading underscore; root, NOT master_csvs/)
SELECT COUNT(*) FROM read_csv_auto('/Users/scott/Desktop/Archive/aberdeen-group-archive/_master_observations.csv');
```

Master CSVs at archive repo root: `_master_studies.csv`, `_master_observations.csv`,
`_master_entities.csv`, `_master_technologies.csv`, `_master_codes.csv`,
`_master_entity_studies.csv`, `_master_tech_studies.csv`,
`_master_prescience_scores.csv`, `_master_quotations_prescience.csv`,
`_master_player_rebuttals.csv`, `_master_entity_field_conflicts.csv`,
`_known_entities.csv`, `_known_technologies.csv`.

Schemas of masters DIFFER from per-study schemas — for any master-shape
question consult `Perplexity_Only/MASTERS_NOTES.md` before trusting columns.

## Gotchas

- **Read-only always.** Connector enforces it; on the CLI you must pass `-readonly`. Never omit it.
- **`kw console` uses port 8765 — the SAME port as the MCP bridge.** Do not run `kw console` while the bridge is serving, or set `KW_CONSOLE_PORT` to something else.
- **`kw` absolute path.** `pc bash` is a non-login shell; `kw` resolves only at `/Users/scott/bin/kw`.
- **Quoting through `pc bash`.** Prefer `.read` from a temp SQL file written via `pc files write` for any query with quotes/commas.
- **DuckDB CLI quirk.** `information_schema.tables.table_type` values are `VIEW` / `BASE TABLE` — filter as strings; bare-word `VIEW` triggers a Binder Error.
- **Connector `Name or service not known` = tunnel/URL problem, never auth.** Auth failures return clean 401/403.

## Tunnel recovery (if the connector is down)

The MCP connector depends on the ngrok tunnel under launchd
(`com.kastner.ngrok.bridge`). If `bridge_info` fails:

```bash
pc bash -- '/usr/sbin/lsof -nP -iTCP:8765 -sTCP:LISTEN || echo NO_BRIDGE'   # bridge up?
pc bash -- 'curl -s http://127.0.0.1:4040/api/tunnels'                        # ngrok up?
```
launchctl/pkill are restricted under `pc bash`; if a restart is needed, hand
Pete the reset block (unload plist → `pkill -9 -f ngrok` → sleep → load plist)
from a real Mac terminal. For the immediate query, use path 2 (CLI) meanwhile.

## kw ask flag quick-ref

`--k N` (sources, default 6) · `--model NAME` (default qwen3.5:27b-mlx) ·
`--cloud` (Claude via pplx) · `--type study|entity|technology|theme|chapter|note` ·
`--no-notes` (archive only) · `--only-notes` (Pete's interpretive layer) ·
`--no-llm` (retrieval hits only) · `--no-stream` · `--temperature F` · `--max-tokens N`.
Sibling: `kw search QUESTION` (semantic search, no LLM).

## Examples

- "How many high-prescience studies?" → connector `duckdb_query`: `SELECT COUNT(*) AS n FROM v_studies_with_high_prescience;`
- "Top 10 most prescient studies" → `SELECT * FROM v_top_prescient_studies LIMIT 10;`
- "Prescience by decade" → `SELECT * FROM v_prescience_by_decade ORDER BY decade;`
- "What did Aberdeen get right about cloud?" → `pc bash -- '/Users/scott/bin/kw ask "what did Aberdeen get right about cloud computing?"'`
- "Count rows in the observations master" → path 2: `read_csv_auto('.../aberdeen-group-archive/_master_observations.csv')`
