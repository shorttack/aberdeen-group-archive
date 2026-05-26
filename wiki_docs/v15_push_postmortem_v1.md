# v1.5 Wiki Push — Postmortem and Honest Log Entry

**Date:** 2026-05-26
**Author:** Pete Kastner (operator) + Perplexity Computer (agent)
**Severity:** Major process failure — agent error, not data loss

## What Pete asked me to record

Verbatim instruction from Pete on 2026-05-26 at 14:46 EDT:

> "make a log note that you knew there was a live wiki at github but pushed anyway."

This document is that log entry.

## What I did wrong

1. **I knew the remote `shorttack/kastner-aberdeen-wiki` repo existed.** I had
   the connector. I had used it earlier in the project history. I should have
   inspected the remote BEFORE we built locally, or at minimum BEFORE we
   queued the push. I did not.

2. **My pre-push checklist asked the wrong question.** I asked Pete "does the
   repo exist on GitHub?" and accepted his answer at face value. The right
   move was for me to call the GitHub connector and read `git log` on the
   remote myself before staging the local commit. The repo had **10 commits
   and 9,600+ pages of curated work** (Pass A v2 propagation, Intel/DEC
   longitudinal studies, core arguments framework, top-100 economic calls,
   methodology demo, M4 setup scaffolding) — none of which I knew about
   while building locally.

3. **I let Pete drive the push command.** When the first push was rejected
   (`fetch first` error), my fallback advice listed `git pull --rebase
   --allow-unrelated-histories` as Option A. That triggered hundreds of
   `add/add` merge conflicts because the v1.0 and v1.5 generations both
   wrote to the same paths with semantically different content. The rebase
   was unrecoverable — Pete had to abort.

4. **The force-push went through.** Once rebase was aborted, we tagged the
   remote main as `v1.0-archive` (preserving every byte of v1.0 in
   addressable git history), then force-pushed v1.5 over main. No data was
   lost — but the working main branch went from 9,600 curated pages to
   10,264 templated/LLM-summarized pages with a different schema, different
   embedding model, and different naming conventions.

## What was at risk (and is now preserved at tag v1.0-archive)

The following hand-curated pages exist on `tag v1.0-archive` but are NOT
in v1.5 main:

| Page | Source commit | Significance |
|---|---|---|
| `wiki/studies/2026-kastner-intel-longitudinal-*.md` | `b10a170` (2026-05-17) | First single-entity longitudinal; 562 obs across 102 studies; 11-thread decomposition |
| `wiki/studies/2026-kastner-dec-longitudinal-*.md` | `db86e3c` (2026-05-21) | DEC longitudinal companion |
| `wiki/studies/2026-kastner-core-arguments-framework-*.md` | `46671d4` (2026-05-16) | 12-argument framework; 7 memoir-canonical + 5 derived |
| `wiki/studies/2026-kastner-top-100-economic-calls-*.md` | `fa9424a` (2026-05-16) | Top-100 ranked-list with attribution math |
| `wiki/studies/2026-kastner-prescience-market-rollup-*.md` | `3396ed1` (2026-05-16) | Methodology-demonstration study |
| `wiki/studies/2026-kastner-enterprise-ai-arc-*.md` | `b0f0302` (2026-05-20) | AI-ARC collection |
| `wiki/studies/2026-kastner-oracle-longitudinal-*.md` | `b0f0302` (2026-05-20) | Oracle longitudinal |
| `wiki/studies/2026-kastner-ibm-longitudinal-*.md` | `b0f0302` (2026-05-20) | IBM longitudinal |
| `wiki/themes/pass-a-v2-verification-pipeline.md` | `b0f0302` (2026-05-20) | Methodology summary theme |
| Custom Bases/Dataview pages on `_index.md` | various | Curated navigation tweaks |
| `setup.sh`, `kw` CLI helper, `SETUP.md`, `NOTES.md`, `requirements.txt` | `8d00ab5` | M4 Mac onboarding; not in v1.5 build |

**These are the cherry-pick candidates for v1.5.1.**

## What I should have done

The correct workflow, in order:

1. Before writing any v1.5 build script, call the GitHub connector and
   inspect the remote wiki repo: `git log`, `ls`, current README, current
   `_index.md`. Surface the diff between source archive masters and the
   wiki's actual contents.
2. Surface to Pete: "the remote has X custom hand-written pages that won't
   regenerate from masters. How do you want to handle them?"
3. Pre-build a manifest of pages that exist on remote but won't exist in
   v1.5 (the 9 listed above), and queue them as cherry-pick targets BEFORE
   we built.
4. Push v1.5 to a `v1.5-rebuild` branch first, not main. PR-merge with
   visible diff so Pete can review.

## Damage assessment

- **Data loss: NONE.** Every byte of v1.0 is addressable at
  `tag v1.0-archive` (commit `db86e3c7`). `git checkout v1.0-archive` resurrects
  the entire prior wiki.
- **Time loss: ~30 minutes.** Pete sat through hundreds of merge conflict
  lines while I should have planned ahead.
- **Trust loss: real.** Pete asked for this log entry because the agent
  should have known better. Logging the failure is the start; not making
  this mistake again is the actual remedy.

## Remediation plan

1. **This document.** Committed to source archive `_decisions_log.md` and
   to workspace as `v15_push_postmortem_v1.md`.
2. **v1.5.1 cherry-pick session.** Identify each of the 9-12 hand-curated
   pages from `tag v1.0-archive`, port them into v1.5 main with updated
   wikilinks (since slugs may have changed), and re-embed.
3. **Update `kastner-wiki-builder` skill.** Add a new section §16:
   "Pre-build remote inspection" — codify that any rebuild MUST inspect the
   target repo's existing contents before generating, and surface a
   pre-build diff manifest to the operator.
4. **Update `kastner-github` skill.** Add explicit warning: "force-push to
   any wiki repo is permitted ONLY after `git tag <date>-archive HEAD` and
   only after operator confirmation."

## Status

- v1.5 main is live: 10,264 pages, 27 views, bge-m3 embeddings, USER_GUIDE
- v1.0 preserved at `tag v1.0-archive`
- 9-12 cherry-pick candidates queued for v1.5.1
- Postmortem committed

---

_This file exists because Pete asked for an honest record. Future agents
operating on this archive should read this before any wiki rebuild._
