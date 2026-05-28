# EOD Cleanup Note — 2026-05-28

**Purpose:** Pete's explicit ask — "STOP. Make yourself. a cleanup EOD note before PUSH." This note captures what shipped, what was deferred, where files live now, and what an incoming session needs to know to pick up cleanly.

**Author:** Computer (agent), per Pete's authorization to run the EOD GitHub push autonomously while Pete is away (~3 hours).
**Date:** 2026-05-28 (UTC end-of-day)

---

## What landed today (the headline)

Three big things shipped:

1. **Canonical layout decision** — the working wiki has moved from `~/Desktop/kastner_wiki/` to `~/Repos/kastner-aberdeen-wiki/`, off iCloud Drive. Pipeline scripts canonicalized at `~/Desktop/Archive/scripts/`; researcher scripts canonicalized inside the wiki at `scripts/`. The third "working location" (`~/Desktop/kastner_wiki/`) is now deprecated; schedule its rename to `.DEPRECATED_20260528/` after 2026-06-04. Decision document: `decisions/canonical_layout_decision_v1.md` (already on GitHub as commit `91d48e55`).

2. **Phases 1-6 refresh against the canonical wiki** — Phase 1+2 (data layer), Phase 4 (indices), Phase 5 (re-embed with bge-m3, 65 MB embeddings.parquet, zero iCloud dupes), Phase 6 (scaffolding). Phase 3 ran with `--skip-llm` after the first attempt hung on the tier-1 LLM; 10,246 wiki pages emitted clean, 459 tier-1 LLM regeneration deferred to v1.6.

3. **`kw_ask.py` patched to v4** — the v3 reader broke on Phase 5's updated embeddings schema (BinderException). v4 ships a reader matching the current schema; verified working on Pete's Mac (6 hits, 1.74s, qwen3.5:27b-mlx synthesis). Already on GitHub as `scripts/kw_ask_v4.py` (commit `c0183fa1`). In this EOD batch, `scripts/kw_ask.py` is being overwritten with v4's content so the canonical filename matches Pete's local install.

---

## The Three Locations (post-cleanup state)

| Concern | Path | Status as of 2026-05-28 EOD |
|---|---|---|
| Masters (source of truth) | `~/Desktop/Archive/archive_masters/` | Unchanged. Truth. |
| Wiki (canonical, live) | `~/Repos/kastner-aberdeen-wiki/` | **NEW canonical location.** Off iCloud. Mirror of `shorttack/kastner-aberdeen-wiki` (post-push). |
| Wiki (deprecated working) | `~/Desktop/kastner_wiki/` | **Stale after this push.** Schedule rename to `.DEPRECATED_20260528/` after 2026-06-04 (one-week grace window for any not-yet-noticed dependencies). |
| Pipeline scripts | `~/Desktop/Archive/scripts/` | Pete's invariant: "I prefer scripts at /Archive/scripts." Mirror to `shorttack/aberdeen-group-archive/scripts/`. |
| Researcher scripts | `~/Repos/kastner-aberdeen-wiki/scripts/` | The "researcher kit" — kw, bin/kw, kw_ask.py, kw_note.py (future), USER_GUIDE.md. Shipped in the wiki repo per Pete's quote: "shorttack/kastner-aberdeen-wiki has everything a researcher needs to run queries including scripts, notebook, and examples in Wiki." |

Any future verification query MUST go against `~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb`. The skill is being patched to v1.2 to reflect this; until that patch lands, the v1.1 skill still names `~/Desktop/kastner_wiki/` as canonical — read v1.2 first.

---

## Shape audit (canonical, after rebuild)

```
studies                : 1434
observations           : 23605
entities               : 3207
technologies           : 4312
studies_with_pub_year  : 1434
decades_covered        : 38   ← BUG (v_studies_by_decade — see Deferred §3)
high_prescience        : 109
prescience_scored      : 308 of 1434
```

Numbers match yesterday's post-v6+v6.1 baseline. No data drift in this session — only path migration and re-embed.

---

## Content drift discovery (DEFERRED to v1.6 §11)

After kw_ask v4 was confirmed working, the test query "what is the shape of the Kastner archive" still returned **stale v1.4 counts** (933 studies, 19,175 observations, 466 high-prescience). Root cause is NOT kw_ask — it's that five hand-authored narrative pages still contain v1.4 numbers in their `abstract` field inside `_master_studies.csv`:

- `study-2026-kastner-prescience-methodology-demo-0cdf48` — 933 / 19,175 / 466
- `study-kastner-technology-breadth-memoir-2026` — 915 / 2537 techs / 479 domains / 4628 mentions
- `study-2026-kastner-enterprise-ai-arc` — 947-study archive
- `study-volume-1-ch01-waiting-for-automation-1960-1969` — 947 studies
- `wiki/themes/kastner-prescience-market-rollup.md` — 933 / 19,175

These were authored when v1.4 was the current build. They retrieve cleanly (Phase 5 embedded them just fine), but the prose inside the abstract field is now historical. Decision: **do NOT auto-fix these in this session.** Pete prefers diff-review for narrative pages. Captured as WORKLIST §11 "Refresh five v1.4-narrative pages with v1.5.1 metrics (AI-assisted, diff-review)."

This is a non-bug. It's an example of Gotcha 7 (stale embeddings silently lie) at a different layer: the embeddings are correct, the *source text* is what's stale. Skill v1.2 should add a "Content drift" subsection under Gotcha 7.

---

## What's in this EOD push

### Commit 1 → `shorttack/aberdeen-group-archive`

| Path | Why |
|---|---|
| `WORKLIST.md` | v3 — clears "Done this session" (2026-05-27), adds today's done items, appends v1.6 items 5-11 |
| `_decisions_log.md` | Appends 2026-05-28 entry: canonical layout, Phases 1-6 refresh, kw_ask v4, shape audit (before+after), content drift, skills updates |
| `decisions/eod_2026_05_28_cleanup_note.md` | This file |
| `decisions/canonical_layout_decision_v1.md` | Already on GitHub as `91d48e55` — confirming presence; not re-pushed |

The skill v1.2 patch is delivered via `save_custom_skill` to the user-scope skill library, NOT committed to the archive repo (skills are user-scope, not part of the public archive).

### Commit 2 → `shorttack/kastner-aberdeen-wiki`

The 638-file batch. Inventory from the canonical wiki at `~/Repos/kastner-aberdeen-wiki/`:

| Bucket | Count | Notes |
|---|---|---|
| `wiki/**/*.md` | 622 modified + 14 new = 636 | Regenerated by Phase 3 (skip-llm) + Phase 4; 14 new Volume 1 study pages |
| `data/*.parquet` | 4 | embeddings.parquet (65 MB, base64-staged), studies.parquet (931 KB), pages_manifest.parquet (146 KB), _validated/studies.parquet (931 KB) |
| `db/kastner.duckdb` | 1 | 274 KB. Phase 2 output. |
| `scripts/kw_ask.py` | 1 | **Promoted** from `kw_ask_v4.py` (commit `c0183fa1`). Replaces v3. |
| `build_manifest.json` | 1 | Phase 1 build log |
| `.gitignore` | 1 | Removes one line (`phase3_full_run.log`) |
| **Skipped** | — | `scripts/kw_ask_v3.py.bak` (Pete's local rollback) |

Total: 66.0 MB. Single commit via Git Data API.

---

## Deferred items (going into WORKLIST v1.6 candidates)

1. **Tier-1 LLM regen for 459 deferred pages** (~4 hours). Caused by Phase 3 hang on first run; resolved by `--skip-llm`. These are study pages where the tier-1 LLM summary regeneration was skipped. Not a correctness issue — the pages exist, they just have older summaries.

2. **Refresh five v1.4-narrative pages with v1.5.1 metrics** (AI-assisted, diff-review). See "Content drift" above.

3. **`v_studies_by_decade` view bug** — already on WORKLIST §4c, reconfirmed today. Returns 38 rows (one per year with `'s'` suffix) instead of 6 decades. Patch: `((CAST(pub_year AS INTEGER)/10)*10) || 's' AS decade` in `02_build_data_layer_v2.py`.

4. **Schema contract enforcement** — add a verification step to `scripts/verify.py` that asserts `embeddings.parquet` has the columns kw_ask expects, fails loudly if not. Would have caught the BinderException before Pete hit it.

5. **Weed sandbox-path leftovers** in `~/Repos/.../scripts/` — there may be stale references to `~/Desktop/kastner_wiki` in script headers/comments. Audit and patch.

6. **Rename `~/Desktop/kastner_wiki/` → `.DEPRECATED_20260528/`** after 2026-06-04 (one-week grace).

7. **Public-wiki-repo push policy** — answered today: yes, the canonical wiki ships to `shorttack/kastner-aberdeen-wiki` on EOD. Codify in skill v1.2.

8. **`kw_note.py`** — Pete's reminded TODO. A script that takes `kw ask` output and creates a new wiki page or appends to an existing one. "That's how the corpus grows with new insights." Captured in current WORKLIST §6 "Permanent Notes workflow."

9. **Parser backlog** — June 2001 / f-4q04-* patterns, full filename-vs-text year audit (WORKLIST §4a, §4b).

---

## Pickup notes for the next session

When Pete returns and the next session begins:

1. **Read WORKLIST.md from `shorttack/aberdeen-group-archive` root** (sandbox via `gh api`). It will reflect this EOD push.

2. **Confirm Pete's local mirror is current.** Pete may need to:
   ```bash
   cd ~/Repos/kastner-aberdeen-wiki && git pull
   cd ~/Desktop/Archive/aberdeen-group-archive && git pull
   ```
   For the wiki repo, the pull will see no local-file changes (the working tree on Mac is what we just pushed) — but the embeddings.parquet and DuckDB files will refresh git's index. There should be NO conflict. If there is, the most likely cause is iCloud — see Gotcha 7 in `kastner-github` skill.

3. **Verify kw ask still works after the pull.** Run:
   ```bash
   kw ask "what is the shape of the Kastner archive"
   ```
   Expect 1434 studies (post-content-refresh, after WORKLIST §11 lands) OR continued 933/19,175 stale quote (because content drift is NOT yet fixed). Either is "working" as of today's EOD — the kw_ask code itself is functional.

4. **The next likely thread:** the content-drift refresh (WORKLIST §11) or tier-1 LLM regen (§1). Both are AI-assisted, both need Pete diff-review.

5. **Skill v1.2 is live in user-scope.** First action on next session start: confirm the skill loaded matches v1.2 metadata, not v1.1.

---

## Where to find this note

- **GitHub** (canonical, this commit): `shorttack/aberdeen-group-archive/decisions/eod_2026_05_28_cleanup_note.md`
- **Sandbox** (working copy): `/home/user/workspace/eod_2026_05_28/eod_2026_05_28_cleanup_note.md`
- **Pete's Mac**: after `git pull` of the archive repo, lives at `~/Desktop/Archive/aberdeen-group-archive/decisions/eod_2026_05_28_cleanup_note.md`

---

_End of cleanup note. Proceeding to push._
