# Decisions log entry — 2026-07-30 AM (kastner-new-day local-Mac migration + v2.2 worklist-CSV proposal)

**Date:** 2026-07-30 (AM session)
**Session arc:** Move the `kastner-new-day` skill off the multi-turn LLM round-trip through the bridge and onto a single self-verifying Mac-side script (following the `kastner-eod` pattern). Mid-project, surfaced a deeper problem — the append-only Markdown `WORKLIST.md` has become an undifferentiated 787-line backlog morass — and locked a v2.2 milestone to migrate the worklist to a CSV/DuckDB row store. This entry captures both so either thread can be recovered later.

**Outcome:**
- **v1 script SHIPPED** — `scripts/new_day_v1.sh` committed to `shorttack/aberdeen-group-archive` at commit [`61e1dbc6`](https://github.com/shorttack/aberdeen-group-archive/commit/61e1dbc6a9c27ebd7146fc45caaf7a7cc008bbf0). Skill revision + save deferred pending a dry-run on the Mac (Mac was intermittently offline during this session).
- **v2.2 milestone LOCKED** — retire the append-only Markdown worklist in favor of `_master_worklist.csv` + `_master_sessions.csv` + a DuckDB view; ship `scripts/wl` (row CLI) + `scripts/render_worklist.py` (Markdown view); cut `new_day_v2.sh` and `eod_v2.sh` off the CSV.

---

## Part 1 — kastner-new-day local-Mac migration (v1)

### Motivation

The `kastner-new-day` skill has been running as ~7–10 LLM tool calls per new-day event:

1. `gh api` fetch WORKLIST.md
2. Read + audit (WORKLIST in context, ~10k tokens)
3–5. Edit `**Last updated:**`, `## Next up`, `## Done this session`
6. `diff` to verify byte-preservation
7. shasum + mirror
8. Re-audit
9. Brief Pete

Every edit turn pulls the 787-line WORKLIST into context. Costly, and the byte-preservation invariants are enforced as *instructions to the LLM* rather than structurally — a rushed model could skip the diff gate silently.

### Design (mirrors `kastner-eod`)

**One self-verifying Mac-side script Pete runs in his own Terminal.** The LLM's remaining job per new-day is:

1. Read the prior session's decisions-log entry (~200 lines, one file).
2. Draft the focus paragraph and 2–3 next-up bullets.
3. Hand Pete the command:
   ```bash
   bash ~/Desktop/Archive/scripts/new_day_v1.sh < /tmp/new_day_payload.json
   ```
4. Read the JSON brief the script prints; relay to Pete.

### What `scripts/new_day_v1.sh` does

**Inputs** (JSON on stdin):
```json
{
  "focus":      "One-paragraph focus/changelog for the Last-updated line",
  "ship_state": null | "Full replacement text for **Current ship state:**",
  "next_up":    ["First bullet", "Second bullet", ...]
}
```

**Steps:**

1. **Preflight** — on `main`, working tree clean, in sync with `origin/main`, `gh` + `jq` + `python3` present, no pre-existing `WORKLIST_<YYYY_MM_DD>.md`.
2. **Fetch canonical WORKLIST** from `origin/main` via `gh api` (skill invariant #1: source of truth is origin, not the working tree). Save `/tmp/WORKLIST_<today>_pre_edit.md`.
3. **Pre-edit audit** — count `## ` sections, `- [ ]` open, `- [x]` done; assert anchor lines (`**Last updated:**`, `**Current ship state:**`, `## Next up`, `## Done this session`) all present.
4. **Parse stdin payload** (via env-var passthrough to Python so arbitrary quoting/backticks/backslashes in the focus paragraph survive intact).
5. **Edit ONLY four regions** — everything else byte-frozen:
   - (a) `**Last updated:**` line replaced with `YYYY-MM-DD <AM|PM> (<focus>)`
   - (b) `**Current ship state:**` line replaced only if `ship_state` non-null
   - (c) **PREPEND** a fresh `### <today> <AM|PM> focus — <focus_short>` sub-header + bullets at the TOP of `## Next up`. Historical narrative preserved byte-for-byte below.
   - (d) **PREPEND** a fresh `### <today> <AM|PM> — <focus_short>` sub-header + empty bullet at the TOP of `## Done this session`. Prior sessions preserved.
6. **Diff gate** — `diff` pre-edit vs edited; every hunk must fall inside the permitted line ranges (LU line, CS line only if ship_state provided, Next up body, Done insertion point). Any drift → rollback + `exit 4`.
7. **Post-edit re-audit** — section count unchanged, done-item count unchanged, open-item count = pre + expected delta (len(next_up), or 1 for the placeholder).
8. **Mirror** — `cp WORKLIST_<today>.md WORKLIST.md`; verify shasums match.
9. **Brief** — compact JSON on stdout: file paths, canonical source SHA, sha256, pre/post audit deltas, focus_short, next_action.

**Flags:**
- `--skip-fetch` — reuse working-tree `WORKLIST.md` (offline / `pc bash` sandbox has no network)
- `--skip-git-check` — skip clean/in-sync preflight (dry-run only)

**Exit codes:** 0 ok · 1 preflight · 2 fetch · 3 pre-edit audit · 4 edit/drift · 5 mirror.

Never commits, tags, or pushes. EOD batch commit remains `scripts/eod.sh`.

### Design decision reversed mid-session

The original skill text said the "Next up" body should be *replaced* each new-day with today's 2–3 concrete actions. The first offline dry-run against the isolated repo fired the audit gate with `done-item count changed: 46 → 18`. Investigation showed the current `## Next up` section is ~500 lines of *append-only* historical session narrative (nested code blocks, numbered lists, and 30+ `- [x]` items marking prior-session work kept as audit trail). The design was reversed to **prepend**, preserving all history. This matches Pete's actual practice — the skill's original "replace" text was aspirational, not the reality.

### Cost math

- **Current flow**: ~7–10 tool calls per new-day event, WORKLIST in context on ~3 of them, ~30k–50k tokens.
- **Local-script flow**: 2 tool calls (read prior decisions-log entry, hand Pete the command) + 1 brief turn. WORKLIST never enters model context. ~60–75% token savings per event.
- **Break-even**: at ~4–5 new-days/week, payback on build effort in ~3–4 weeks.
- **The safety case is stronger than the cost case.** The byte-diff gate and open-item reconciliation are now `exit 4` in bash, not `please-check` instructions to the model. The "losing carryover items" failure mode becomes structurally impossible, not just discouraged.

### Delivery

- `scripts/new_day_v1.sh` — committed at `61e1dbc6` (2026-07-30).
- Skill revision (`kastner-new-day` v2): **deferred to a follow-up session** — will describe the new LLM contract (read prior decisions-log entry → draft payload → hand Pete the command → relay JSON brief) and reference the script by path. Dry-run first when Mac is reliably online.

### Follow-ups (for `## Next up` on next new-day)

- Dry-run `scripts/new_day_v1.sh --skip-fetch --skip-git-check` in an isolated repo on the Mac against a copy of the current `WORKLIST.md`. Expected result: sections Δ=0, open Δ=+len(next_up), done Δ=0, diff gate clean.
- After dry-run passes, revise the `kastner-new-day` skill to delegate; save via `save_custom_skill`.

---

## Part 2 — v2.2 milestone: worklist-CSV migration (recoverable working item)

### The problem

`WORKLIST.md` is 787 lines, 131 `- [ ]` open items, 13 `## ` sections. It mixes four incompatible content types:

1. **Session narratives** — multi-paragraph focus blocks with nested code fences and numbered lists (e.g., line 31's "2026-07-08 focus" block runs ~40 lines).
2. **Actual open tasks** — `- [ ]` bullets scattered across `## v1.6 candidates`, `## v1.7 candidates`, `## v1.8+ / strategic`, `## Maintenance / hygiene`.
3. **Deferred/rejected items** — `## Not on the list / explicitly deferred`.
4. **Historical done audit trail** — 46 `- [x]` items plus multiple `## Session YYYY-MM-DD — Done this session` blocks.

Grep-based audits treat all 131 `- [ ]` bullets as equivalent, which they are not. Most are backlog *inventory*, not today's TODO. And the new-day skill's most expensive step — "figure out what next 2-3 concrete actions matter today" — requires the whole file in context, which is exactly what the local-Mac migration was supposed to eliminate.

### The proposed design

Move the task inventory to a queryable row store; keep Markdown as a rendered *view*, not the source of truth.

**Files at archive root (canonical location, `csv.writer(quoting=QUOTE_ALL)` per §16.5):**

- `_master_worklist.csv` — one row per task
- `_master_sessions.csv` — one row per session (the narrative focus blocks that currently live in `## Next up`)
- `WORKLIST.md` — regenerated by `scripts/render_worklist.py`, still committed for GitHub browsability, but nobody hand-edits it

**Proposed `_master_worklist.csv` schema:**

| column | type | notes |
|---|---|---|
| `id` | TEXT PK | Stable slug — e.g. `v1.8-full-tech-alias-sweep`. Never reused. |
| `title` | TEXT | One line, no markdown |
| `body` | TEXT | Optional multi-paragraph context (Markdown OK, escaped) |
| `section` | TEXT | Legacy source: `next-up` / `v1.6` / `v1.7` / `v1.8+` / `maintenance` / `deferred` |
| `target_release` | TEXT | `v1.6` / `v1.7` / `v2.2` / `strategic` / `hygiene` |
| `status` | TEXT | `open` / `in_progress` / `done` / `deferred` / `dropped` |
| `priority` | INT | 1 (today) / 2 (this week) / 3 (this release) / 4 (later) |
| `blocked_on` | TEXT | Comma-sep task IDs or free text |
| `owner` | TEXT | `pete` / `agent` / `either` |
| `estimate` | TEXT | `xs` / `s` / `m` / `l` / `xl` |
| `tags` | TEXT | Comma-sep: `pipeline`, `pass-c`, `wiki`, `skill`, `bridge`, `csv-migration`, ... |
| `session_added` | TEXT | `YYYY-MM-DD` |
| `session_closed` | TEXT | `YYYY-MM-DD` when marked done |
| `notes` | TEXT | Post-hoc annotations, links |

**Proposed `_master_sessions.csv` schema (session narratives):**

| column | type | notes |
|---|---|---|
| `session_date` | TEXT PK | `YYYY-MM-DD` |
| `apm` | TEXT | `AM` / `PM` |
| `focus_short` | TEXT | ≤80 char one-liner |
| `focus_body` | TEXT | Full paragraph (the current "Last updated" prose) |
| `ship_state_at_close` | TEXT | Snapshot of `**Current ship state:**` at EOD |
| `decisions_log_ref` | TEXT | Path to that day's `Archive/decisions/decisions_log_entry_...md` if any |

**New tooling:**

- `scripts/wl` — thin Python CLI: `wl add`, `wl close <id>`, `wl defer <id>`, `wl show --today`, `wl show --release v1.6`, `wl edit <id>`. Backed by DuckDB view over the CSVs.
- `scripts/render_worklist.py` — regenerates `WORKLIST.md` from the CSVs. Produces a Markdown file close enough to the current hand-authored one that the initial migration commit is a diff-review, not a rewrite.
- `scripts/new_day_v2.sh` — appends a row to `_master_sessions.csv`; prints the JSON brief with the priority-queue top from `wl show --today`. Kills the diff-gate complexity of v1 (a row insert has no "did we mangle byte X" risk).
- `scripts/eod_v2.sh` — closes rows the session touched (via `wl close`); commits the CSVs plus the regenerated `WORKLIST.md` in one batch.

### Trade-offs (honest)

**Wins**
- Query-based backlog surfacing kills the "read 787 lines to pick 2 items" cost.
- Real priority + release + tag facets — you can answer "what's still open for v1.6" without eyeballing.
- Matches existing archive architecture: master CSV + DuckDB view + Python CLI. Consistent with `kastner-archive-pipeline` and `duckdb-queries` skills.
- Snapshots become cheap (row-level audit, not full-file diffs).
- New-day/EOD scripts get simpler, not more complex.

**Costs**
- **One-time migration**: 131 open + 46 done items across 9 sections need to be classified into rows. This is ~half a day of Pete's judgment — the LLM can propose column values, but priority/release/tag on strategic v1.8+ items requires Pete's own plans. Some items are paragraphs, not rows — those go to `_master_sessions.csv` or get dropped.
- **`WORKLIST.md` as first-class human-editable file dies.** GitHub browsers get a rendered view. Semantic change worth explicit sign-off.
- **New skill surface** — `wl` CLI + render script + updated `kastner-new-day` + updated `kastner-eod` (must know how to close rows, not `- [ ]` toggles). ~2–3 shipping days spread across a week.
- **Risk of over-engineering the schema.** Wrong taxonomy at migration time = a week of fighting it. Mitigation: propose columns, get Pete's sign-off before writing a single row.

### Suggested sequencing

1. **Today (this session)** — finish the current new-day project as scoped. Deliver `scripts/new_day_v1.sh` (DONE, `61e1dbc6`), capture this decision (this file), revise+save skill (deferred). The v1 script becomes the *last version* of the Markdown-editing driver.
2. **Next session** — propose the CSV schema; get Pete's sign-off on columns + taxonomy. Draft `_master_worklist.csv` + `_master_sessions.csv` with the current 131+46 items classified. **This requires Pete's judgment session-by-session**, not agent-only.
3. **Session after that** — ship `scripts/wl` + `scripts/render_worklist.py`. Verify the rendered `WORKLIST.md` matches the current hand-authored one closely enough to commit as baseline.
4. **Session after that** — cut `new_day_v2.sh` + `eod_v2.sh` (row-based); retire the `- [ ]`/`- [x]` audit logic; update `kastner-new-day` skill to v3 and `kastner-eod` skill to a new minor version.

### Recoverable working item (drop into `## Next up` at next new-day)

> **v2.2 candidate: CSV/DuckDB worklist migration.** Retire the append-only Markdown worklist in favor of `_master_worklist.csv` + `_master_sessions.csv` + a DuckDB view. Ship `scripts/wl` (row CLI) and `scripts/render_worklist.py` (Markdown view). Cut `new_day_v2.sh` and `eod_v2.sh` off the CSV. **Migration: ~half-day of Pete's judgment on 131 open + 46 done items** to classify. Full design in `Archive/decisions/decisions_log_entry_2026_07_30_new_day_local_migration_and_worklist_csv_v1.md` — Part 2.

---

## Files touched this session

| repo | path | action |
|---|---|---|
| `shorttack/aberdeen-group-archive` | `scripts/new_day_v1.sh` | ADD (commit `61e1dbc6`) |
| `shorttack/aberdeen-group-archive` | `Archive/decisions/decisions_log_entry_2026_07_30_new_day_local_migration_and_worklist_csv_v1.md` | ADD (this file) |

## Deferred to next session

- `kastner-new-day` skill v2 revision (delegate to `scripts/new_day_v1.sh`).
- `save_custom_skill` call.
- Both require a Mac-online dry-run of the v1 script first — Mac was intermittently offline during this session; the script has NOT been end-to-end tested against a live WORKLIST fetch.
