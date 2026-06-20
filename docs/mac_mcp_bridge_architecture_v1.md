# Mac MCP Bridge — Architecture Reference

**Status**: APPROVED 2026-06-20. Build scheduled (not yet started).
**Source discussion**: 2026-06-19 PM through 2026-06-20 PM (§11x continuation).
**Companion file**: `docs/promoted_mac.md` (Pete's original 1835-line architecture sketch, preserved verbatim in this repo for reference).

## Decision

Build a **read-only MCP bridge** that exposes Pete's archive + wiki to the Perplexity Mac app via stdio. **No local LLM in the loop.** Cloud Perplexity (Sonar Reasoning / GPT-5 / Opus 4.8) handles all reasoning and synthesis. The Mac handles data retrieval only.

The local-LLM path (Qwen3.5/3.6 + Rapid-MLX + MLX) is **deferred indefinitely** — possibly added later as one more tool inside the same bridge, never as a replacement.

## Why this path over the full local-LLM plan

| Dimension | Local Qwen3.5-35B-A3B | Cloud Perplexity + local data tools |
|---|---|---|
| Tool call latency | 10–15s (model thinks, then tool runs) | 1–3s (cloud thinks remote, local tool just queries) |
| Build complexity | Rapid-MLX + 20GB MLX model + FastMCP + Qwen tool-parser tuning | FastMCP + thin tool wrappers |
| Failure surfaces | MLX crashes, tool-parser misfires, KV cache OOM, model swap regressions | FastMCP process crashes |
| Memory resident | 19GB model + 5GB working | ~500MB Python process |
| Battery / heat | GPU pinned during inference | Negligible |
| Synthesis quality | Qwen3.5-35B-A3B (~Claude 3.5 Haiku tier) | Whatever cloud model is selected (substantially stronger) |
| Tool-call reliability | Qwen XML parsing — known weak spot | Frontier model native tool calling |
| Privacy | Archive content never leaves Mac | Archive content flows to Perplexity cloud as tool output |
| Offline capability | ✅ | ❌ |
| Cost per query | $0 marginal | Counts against Perplexity credits |
| Gate 0 risk | High (new model family, new server, OLLAMA_GOTCHAS) | Low (Python + existing patterns) |
| Build effort | 4–6 weeks + traps | 1–2 weeks |

**Privacy is a wash** for the public archive — it's already on GitHub. `kastner-restricted-sources` (private) would never be exposed through this MCP regardless.

**Offline** is theoretical for Pete's work pattern (always online, terminal stack always running).

**Credits** are the real cost downside, but each bridge query is one cloud model turn + cheap local tool calls, NOT the iterative thread-style burn that hit 63K credits in 4 days.

## Architecture

```
Perplexity Mac app (cloud Sonar/GPT/Claude does ALL synthesis)
         │ stdio
         ▼
   FastMCP bridge (Python, sandboxed to ~/Desktop/Archive/)
         │ direct in-process calls
         ▼
   ┌─────┴─────┬─────────────┬──────────────┐
   DuckDB     Archive CSVs   kw_ask        Wiki files
   (kastner    (master_*.csv) (existing     (markdown)
    .duckdb,                    Python)
    read-only)
```

**Transport**: stdio (per Perplexity Mac local-MCP support, confirmed at https://www.perplexity.ai/help-center/en/articles/11502712-local-and-remote-mcps-for-perplexity).
**Registration**: Perplexity Mac app → Settings → Connectors → Add Connector → Simple (or Advanced) tab, flat `{command, args, env}` JSON.
**Prerequisite**: PerplexityXPC helper app installed (one-time).
**Security boundary**: bridge process strictly scoped to `~/Desktop/Archive/`. Path sanitization on every file-read tool. DuckDB opened read-only.

## Tool surface (Phase 1 — read-only)

Six tools, each a thin wrapper around existing Pete code:

| Tool | Action | Existing code path |
|---|---|---|
| `duckdb_query` | Run read-only SQL against `kastner.duckdb` | `duckdb.connect(path, read_only=True)` |
| `duckdb_tables` | List tables + views | Built-in DuckDB metadata |
| `duckdb_describe` | Show schema for a table/view | `DESCRIBE <name>` |
| `kw_ask` | Semantic search over wiki via existing helper | `from kw_ask import ask` |
| `read_archive_file` | Read a file under `~/Desktop/Archive/` (sanitized) | `pathlib.Path.read_text()` |
| `list_prepared` | List `_prepared/` contents, optionally filtered by study | Existing logic |

**Each tool is 5–15 lines.** The heavy lifting already exists in Pete's Python helpers and DuckDB. The bridge adds schema declarations + a security boundary, not new functionality.

## Compatibility with existing workflows — full preservation

All current workflows remain unchanged:

- Terminal `kw_ask "..."` queries → same
- Obsidian Dataview tables refreshing on file change → same
- DuckDB CLI sessions for ad-hoc analysis → same
- Phase 1/3 pipeline rebuilds → same
- Pass C runs → same
- Wiki page generation → same
- `git push` workflows on either repo → same
- Master CSV edits → same

**What's added**: a stdio interface that lets cloud Perplexity execute the same code paths Pete already uses from the terminal.

### Concurrent access

DuckDB supports multiple concurrent readers when no writer is active. The bridge opens read-only, so:

| Scenario | Behavior |
|---|---|
| Pete terminal query + bridge idle | Fine |
| Pete terminal query + Perplexity via bridge simultaneously | Both work |
| Pete mid-rebuild (Phase 1/3 writing) + Perplexity via bridge | Bridge query waits or errors transiently during the write lock |
| Bridge open + Pete runs Phase 1 rebuild | Same — rebuild locks, bridge errors during the lock |

**Recommendation**: bridge opens a fresh DuckDB connection per query (cold open ~50ms, always-fresh data after rebuilds). Don't cache a long-lived connection.

Obsidian has zero conflict — it reads/writes markdown; bridge only reads.

## Build sequence

1. **Phase 0**: stub `mac_mcp_bridge/` directory in `~/Repos/` (NOT under `~/Desktop/` — iCloud trap). FastMCP scaffolding, `pyproject.toml`, README.
2. **Phase 1**: implement `duckdb_query` + `duckdb_tables` + `duckdb_describe`. Manual stdio test (echo MCP frames in/out) before any Perplexity wiring.
3. **Phase 2**: add `read_archive_file` + `list_prepared` with path sanitization. Unit tests for the sanitizer (reject `..`, absolute paths, symlink escapes).
4. **Phase 3**: add `kw_ask`. Verify it works with the bridge's process environment (PYTHONPATH to Pete's helpers, embeddings parquet location, etc.).
5. **Phase 4**: register connector in Perplexity Mac app. Smoke-test each tool from a real conversation.
6. **Phase 5** (future, separate decision): write/execute tools. Requires a different security review.
7. **Phase 6** (future, optional, possibly never): `qwen_synthesize` tool that wraps a local Rapid-MLX endpoint. Only if Phase 1–5 usage reveals a real need.

## Reference connector JSON (Perplexity Mac app)

Approximate shape (Advanced tab):

```json
{
  "command": "/Users/scott/.pyenv/shims/python3",
  "args": [
    "-m",
    "kastner_archive_mcp"
  ],
  "env": {
    "ARCHIVE_ROOT": "/Users/scott/Desktop/Archive",
    "KASTNER_DB": "/Users/scott/Repos/kastner-aberdeen-wiki/db/kastner.duckdb",
    "WIKI_ROOT": "/Users/scott/Repos/kastner-aberdeen-wiki",
    "PYTHONPATH": "/Users/scott/Desktop/Archive/scripts"
  }
}
```

Final paths and entry point TBD during Phase 0.

## Risks / open questions for build time

- **kw_ask import surface**: does it import cleanly without side effects (e.g., loading 100MB of embeddings at module import)? May need a lazy-load shim.
- **DuckDB read-only with views that reference parquet**: confirm read-only opens still resolve view definitions correctly. Test early in Phase 1.
- **FastMCP Python version**: confirm Pete's Python (3.13/3.14?) is compatible. FastMCP requires modern asyncio.
- **PerplexityXPC helper**: one-time install Pete needs to do before Phase 4. Surface this early.
- **Process lifetime**: Perplexity Mac launches the stdio process per session. Cold-start cost matters — defer all heavy imports until first tool call.
- **Path sanitization edge cases**: test against symlinks pointing outside the archive root. `Path.resolve()` + `is_relative_to()` is the pattern.

## Anti-goals

- ❌ Writing to the archive through the bridge (Phase 1–4)
- ❌ Local LLM synthesis (Phase 1–5)
- ❌ Exposing `kastner-restricted-sources` (private) through this MCP, ever
- ❌ Network-exposed MCP (Cloudflare Tunnel, custom-credentials) — not needed for stdio
- ❌ Replacing terminal workflows — bridge is **additive**

## Provenance

- Architecture sketch: `docs/promoted_mac.md` (Pete's 1835-line doc, 2026-06-19)
- Discussion sessions: 2026-06-19 §11x continuation; 2026-06-20 morning + afternoon
- Latency / memory math: 2026-06-20 morning research turn (Rapid-MLX benchmarks, M4 Pro memory bandwidth, Qwen3.5-35B-A3B MoE numbers)
- Approval: Pete, 2026-06-20 PM ("Approved. Put bridge on work list.")
