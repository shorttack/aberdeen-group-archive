# Canonical Layout Decision — Kastner Aberdeen Archive

**Date**: Thursday, May 28, 2026
**Author**: Pete Kastner + agent
**Status**: ACTIVE — supersedes yesterday's "Three Locations" framing in `kastner-archive-pipeline` skill v1.1
**Context**: Triggered by attempting Workflow C (refresh wiki content + embeddings) on the morning after the v6.1 pub_year backfill commit. Pre-flight discovered iCloud had silently created 2,845 duplicate `... 2.md` files under `~/Desktop/kastner_wiki/wiki/`, and inspection revealed the actual canonical wiki is `~/Repos/kastner-aberdeen-wiki/`, not `~/Desktop/kastner_wiki/` as yesterday's skill stated.

## TL;DR — the canonical layout

| Concern | Path | Role | Git? |
|---|---|---|---|
| **Wiki (live, queryable)** | `~/Repos/kastner-aberdeen-wiki/` | The wiki Pete queries with `bin/kw`. DuckDB at `db/kastner.duckdb`, parquets at `data/`, markdown at `wiki/`, researcher scripts at `scripts/`. | Yes — local clone of `shorttack/kastner-aberdeen-wiki` |
| **Wiki (iCloud-corrupted twin)** | `~/Desktop/kastner_wiki/` | **DEPRECATED.** Keep for 1 week, delete after 2026-06-04. Will be renamed `~/Desktop/kastner_wiki.DEPRECATED_20260528/` end of session. | Yes (irrelevant — deprecated) |
| **Pipeline scripts** | `~/Desktop/Archive/scripts/` | Scripts that operate ON the archive masters to BUILD the wiki. Run by Pete only. Examples: `01_load_csvs_v2.py`, `extract_pub_year_v2.py`, `apply_pub_year_v6_1.py`. **NOT shipped to the public wiki repo.** | No (mirrored to `shorttack/aberdeen-group-archive/scripts/`) |
| **Researcher scripts** | `~/Repos/kastner-aberdeen-wiki/scripts/` | Scripts that operate ON the published wiki to QUERY it. Ship with public release. Examples: `kw_ask.py`, `reembed.py`, `semantic_search.py`, `verify.py`, plus notebooks and examples. | Yes (in the wiki repo) |
| **Masters (source of truth)** | `~/Desktop/Archive/archive_masters/` | The master CSVs. **STATUS QUO** — keep here for now. Deferred move to `~/Repos/aberdeen-group-archive/` to a future session. | No (mirrored to `shorttack/aberdeen-group-archive/` root) |
| **Source-of-truth backups** | `~/Desktop/Archive/archive_masters/*.bak_<reason>_<utc-stamp>Z` | Per-edit backup snapshots. Stay co-located with masters. | No |

## The mental model

**Two kinds of scripts, two homes. Never mix them.**

1. **Pipeline scripts** live at `~/Desktop/Archive/scripts/` and operate on the archive to (re)build the wiki. The 01-06 phase chain (`01_load_csvs_v2.py` → `02_build_data_layer_v2.py` → `03_generate_vault_v2.py` → `04_generate_indices_v2.py` → `05_compute_embeddings_v2.py` → `06_emit_scaffolding_v1.py`) is the canonical example. Also: extract_* and apply_* one-off backfill scripts (extract_pub_year_v2.py, apply_pub_year_v6_1.py, etc.).

2. **Researcher scripts** live INSIDE the wiki repo at `~/Repos/kastner-aberdeen-wiki/scripts/` and operate on the published wiki to query it. They get a `bin/kw` CLI launcher. They ship to the public so external researchers can clone the wiki repo and have a complete kit. The public wiki repo is intentionally **self-contained**: wiki/ + data/ + db/ + bin/kw + scripts/ + notebooks + examples = "everything a researcher needs to run queries."

**The reason today's confusion happened**: `~/Repos/kastner-aberdeen-wiki/scripts/` currently contains a mix of (a) sandbox-built pipeline-flavored scripts with hardcoded `/home/user/workspace/...` paths that cannot run on the Mac, and (b) real researcher scripts that work. Needs weeding (deferred to its own task — see below).

## Two-repo public layout

| GitHub repo | Audience | Contents |
|---|---|---|
| `shorttack/aberdeen-group-archive` (public) | Pete + automation | Master CSVs (at repo root), backup snapshots, pipeline scripts at `scripts/`, decisions log, worklist, EOD notes |
| `shorttack/kastner-aberdeen-wiki` (public) | External researchers | wiki/ (markdown pages), data/ (parquets), db/ (kastner.duckdb), bin/kw, scripts/ (researcher-facing), notebooks, examples, README/AGENTS.md/chat-starter |

These are intentionally separate. The archive repo is "raw materials + production tools." The wiki repo is "finished product + reader's kit."

## What got us here — the morning's investigation chain

1. **Pre-flight for Workflow C** (Phase 3-6 re-embed) discovered 2,845 `... 2.md` files in `~/Desktop/kastner_wiki/wiki/`. iCloud Desktop sync had silently duplicated almost every wiki markdown file at some prior point (likely during the v1.4 build or last week's pipeline runs). Phase 5 against that tree would have indexed 2x the corpus.
2. **Diff sweep confirmed** all 2,845 dupes are byte-for-byte identical to their originals and all originals exist — zero data loss risk. They're pure iCloud noise.
3. **Investigation of `kw ask`** revealed `bin/kw` lives at `~/Repos/kastner-aberdeen-wiki/bin/kw` (KW_ROOT defaults to `~/Repos/kastner-aberdeen-wiki`). So when yesterday's stale-numbers incident happened, `kw ask` was reading from `~/Repos/`, NOT from `~/Desktop/kastner_wiki/` as the skill stated.
4. **Cross-mount discovery**: `~/Repos/.../db/kastner.duckdb` views read parquets from absolute paths pointing at `/Users/scott/Desktop/kastner_wiki/data/`. So the Repos DuckDB's row counts were post-v6 (because they read live from Desktop parquets), but the Repos `embeddings.parquet` and wiki markdown were pre-v6 (because Phase 3+5 had never run against `~/Repos/`). That's the exact failure mode that produced "933 studies, 19,175 observations" with high confidence — DuckDB COUNT(*) was right, but the LLM retrieval saw the old pages.
5. **Decision**: rather than continue the cross-mount, retarget Phases 1-6 to `~/Repos/` so it becomes fully self-contained. Phase 1+2 ran cleanly today (CHECKPOINT 1 below). Phase 3-6 STOPPED before kickoff per Pete's instruction to record this decision first.

## CHECKPOINTS completed today (2026-05-28)

### CHECKPOINT 0 — Safety snapshot
Tagged `~/Repos/kastner-aberdeen-wiki` at `pre-v6-pipeline-20260528T130754Z`. Working tree was clean (nothing new since May 26).

### CHECKPOINT 1 — Phase 1 + 2 against `~/Repos/`
```bash
python3 ~/Desktop/Archive/scripts/01_load_csvs_v2.py \
  --archive ~/Desktop/Archive/archive_masters \
  --wiki    ~/Repos/kastner-aberdeen-wiki

python3 ~/Desktop/Archive/scripts/02_build_data_layer_v2.py \
  --wiki ~/Repos/kastner-aberdeen-wiki
```
**Result**: 12 parquets promoted to `~/Repos/.../data/`, 27 `v_*` views rebuilt. `v_studies` SQL now reads `/Users/scott/Repos/kastner-aberdeen-wiki/data/studies.parquet` — cross-mount eliminated.

**Shape audit post-CHECKPOINT-1**:
| studies | observations | entities | technologies | with_pub_year | high_prescience |
|---|---|---|---|---|---|
| 1,434 | 23,605 | 3,207 | 4,312 | 1,434 | 109 |

Matches the post-v6.1 baseline exactly.

### CHECKPOINT 2 — STOPPED (Phase 3-6 not run today)
Stopped at Pete's instruction to record this decision document before proceeding. Resume next session.

## What's deferred to future sessions

### Next session (resuming Workflow C against `~/Repos/`)
1. Run Phase 3 (markdown pages), Phase 4 (indices), Phase 6 (scaffolding) against `~/Repos/kastner-aberdeen-wiki`
2. Run Phase 5 (re-embed) — note: `05_compute_embeddings_v2.py` model needs to match what `bin/kw` retrieves with (kw mentions `bge-m3`; needs verification)
3. Verify `kw ask "what is the shape of the Kastner archive"` returns 1,434 / 23,605
4. Rename `~/Desktop/kastner_wiki/` → `~/Desktop/kastner_wiki.DEPRECATED_20260528/` (delete on or after 2026-06-04)

### Weed the Repos scripts dir
Current `~/Repos/kastner-aberdeen-wiki/scripts/` contains:
- `add_dec_longitudinal_pages.py` — purpose unclear (sandbox path? researcher script? pipeline?)
- `add_pass_a_v2_pages.py` — purpose unclear
- `kw_ask.py` — **KEEP** (researcher, called by bin/kw)
- `reembed.py` — **KEEP** (researcher) — sandbox paths inside, needs repath
- `refresh_data_layer.py` — **DELETE or REPATH** — hardcoded `/home/user/workspace/...` paths, can't run on Mac. Pipeline-flavored, doesn't belong here.
- `semantic_search.py` — **KEEP** (researcher)
- `verify.py` — **KEEP** (researcher)

Audit + classification + clean-up is its own ~30-minute task. Capture in v1.6 backlog.

### Move masters out of `~/Desktop/Archive/`?
**Decision: deferred to a future quiet session.** Tradeoffs documented above in the morning's conversation. Not urgent — no active iCloud incident on the masters directory itself.

### Patch the `kastner-archive-pipeline` skill
v1.1 (yesterday) has the "Three Locations" table backwards on which is canonical, and bakes in the wrong rebuild scripts. Needs:
- v1.2 update: canonical wiki = `~/Repos/kastner-aberdeen-wiki/`; deprecated twin = `~/Desktop/kastner_wiki/` (delete on/after 2026-06-04)
- Add the "two kinds of scripts, two homes" mental model
- Update every code block from `--wiki ~/Desktop/kastner_wiki` → `--wiki ~/Repos/kastner-aberdeen-wiki`
- Fix the shape-audit decade query (yesterday's `(CAST(pub_year AS INTEGER)/10)*10` returns float, not bucketed int — use `FLOOR(pub_year/10)*10` or `pub_year // 10 * 10`)
- Add "iCloud Desktop trap" as a top-of-skill blocker — never run anything long-lived under `~/Desktop/`
- Add this decision doc as a referenced artifact

### Resume v1.6 backlog
Unchanged from yesterday's wrap:
1. Parser fix in `01_load_csvs_v2.py` for "June 2001" + `f-4q04-*` filename patterns
2. Filename-vs-text year audit (catches silent misparses in [1970,2026])
3. Fix `v_studies_by_decade` view (groups by year, not decade)
4. Refresh stale wiki shape numbers — partially done at Phase 1+2 today, pending Phase 3+5+6
5. Author Prescience Methodology Demo study with `observation_count = 0`

## Open questions to revisit when relevant

- **Phase 5 embedding model lock-in.** `bin/kw` script comments mention `bge-m3` + `qwen3.5:27b-mlx`. `~/Repos/scripts/reembed.py` mentions `nomic-embed-text-v2-moe`. `~/Desktop/Archive/scripts/05_compute_embeddings_v2.py` may use yet another. They MUST agree — the retrieval index must be embedded with the same model the query uses, or `kw ask` returns garbage. Audit before next Phase 5 run.
- **Public wiki repo "researcher kit" completeness.** Pete's vision: clone + everything works. Today it almost works, but `reembed.py` has hardcoded sandbox paths. Audit: which researcher scripts actually run on a fresh clone? Document the gaps.
- **Two-repo coordination at EOD commits.** Today's pub_year v6.1 batch went to `shorttack/aberdeen-group-archive` (masters, scripts, decisions log). The wiki repo `shorttack/kastner-aberdeen-wiki` did NOT receive an update. After Phase 3-6 success, do we push refreshed parquets + db + markdown to the wiki repo? That's a big commit (parquets are ~60 MB combined). Policy needed.

## References

- Yesterday's EOD wrap: `current_session_context/turns/turn_NNNN.md` (in this session's context)
- Yesterday's decisions log: `_decisions_log.md` in `shorttack/aberdeen-group-archive` (commit `10115727`)
- Current `kastner-archive-pipeline` skill: v1.1 (skill_id `fe5dc1e1-e51d-4f60-88e7-4d2651afa18b`, dated 2026-05-27)
- v1.6 backlog: `future_work_v1.6.md` in `shorttack/aberdeen-group-archive`
