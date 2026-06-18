# Decisions Log — 2026-06-18 (Thursday)

**Session theme:** Methodology-demo v2.0 regen + Phase 6 hardening + §11v D6 prescience architecture map.

---

## Decision 1 — Methodology-demo: regenerate as new study (v2.0), not in-place patch

**Context:** Previous methodology-demo (`2026-kastner-prescience-methodology-demo-0cdf48`) was authored before 3-year and 5-year short-horizon prescience were added. Pete: *"We added 3- and 5-year. The language will be harder to patch than generate new."*

**Decision:** Treat as a new study with new slug `2026-kastner-prescience-methodology-demo-v2-0cdf49`. D3-preauthorized addition to `_master_studies.csv` (row 1452 → 1453).

**Rationale:** One-and-done so the science looks methodical. Patching the prior page would have produced a chimera doc; a clean v2.0 reads as a deliberate methodology update.

**Outcome:** Shipped via 4 commits (archive `0a88d455`, wiki `49f33d3f`, archive `53fc748c` surgical re-embed, archive `229843c4` Phase 6 v5).

---

## Decision 2 — Pass C race condition: surgical re-embed, not full Phase 5 rerun

**Context:** Phase 5 captured the auto-stub page Phase 3 had produced for the v2.0 study slug. The hand-authored page landed on disk via `git pull` AFTER Phase 5 had read its file list at start. Result: embeddings.parquet held the stale stub, `kw ask` missed the v2.0 retrieval.

**Decision:** Write `reembed_single_page_v1.py` to surgically replace one row of `data/embeddings.parquet` using DuckDB COPY (read-where-not-slug UNION new row) + tmpfile + atomic rename + row-parity check + backup. Do NOT re-run full Phase 5 (~15 min, would re-embed 10,439 rows).

**Rationale:** Schema-contract verified against Gotcha 9 (6-col contract `page_path, page_type, slug, title, vector, dim`). Atomic write means no risk of corrupting the live index. Row-parity check (10,439 → 10,439) means we know we replaced exactly one row.

**Outcome:** `kw ask` now retrieves v2.0 at top (score 0.499). Shipped as commit `53fc748c`. **Adds Gotcha 13 candidate**: Phase 5 reads file list at start; mid-flight git pulls race.

---

## Decision 3 — Phase 6 v5: harden against .gitignore clobber

**Context:** Phase 6 v1 (`06_emit_scaffolding_v1.py`) ran cleanly but clobbered `.gitignore`, reducing it from 17 lines (with Python + `.bak_*` patterns + warning comment) to a 3-line stub. Gotcha 8 active: Phase 6 ANY hand-edit to README/AGENTS/chat-starter/.gitignore/Makefile/verify.py/semantic_search.py is overwritten on rerun.

**Decision:** Bump Phase 6 to v5 with three fixes: (1) `.gitignore` template expanded from 3-line → 17-line with Python + `.bak_*` patterns + warning comment; (2) `LOCAL_MODEL` fallback corrected from stale `qwen3.6:27b-mlx` → `qwen3.5:27b-mlx`; (3) all script-name references bumped v2→v5 and `--wiki` path corrected to `~/Repos/`.

**Rationale:** v4 was the prior version in repo; v5 is one bump above to keep version monotonic. Pete asked for one-and-done — embedding the gitignore content INTO the script template means rerunning Phase 6 won't re-introduce the regression.

**Outcome:** Shipped as commit `229843c4`. Rerun confirms `.gitignore` is additions-only vs HEAD. Gotcha 8 is NOT fully solved (other templates remain hand-edit-hostile) but `.gitignore` specifically is now safe.

---

## Decision 4 — §11v D6 prescience architecture audit: ship the MAP, not a new findings report

**Context:** Pete flagged "audit the entire prescience architecture locally on the Mac and at GitHub. It used to be simple. Now, I don't think I can explain the process or the files used." A prior findings report exists at `Archive/decisions/prescience_architecture_audit_v1.md` (2026-06-15) with F1-F10 enumerated. Gates v1.7.0 ship.

**Decision:** Write the missing **architecture MAP** at `Perplexity_Only/PRESCIENCE_ARCHITECTURE.md` — companion to (not replacement for) the findings report. The findings report says *what's broken*; the architecture map says *how the system actually works*.

**Rationale:** Pete's stated problem is explanatory, not diagnostic. He has the F1-F10 list. What he doesn't have is one document where the file inventory, schemas, Path A/B flows, Phase 1 join contract, and lag points are all laid out side by side. Two docs, two purposes — neither subsumes the other.

**Outcome:** Shipped as commit `0f5c9d71`. 376 lines, 9 sections. Key content: 8-point lag-point map (L1-L8), Path A and Path B ASCII flow diagrams, Rule A rollup math, Phase 1 pass-through invariant (the thing that makes Path B work), v1.7.0 ship gate (F2/F3/F6/F7 must close).

---

## Shape audit (post-session, archive_masters truth)

| metric | value | delta vs morning |
|---|---:|---:|
| studies | 1,453 | +1 (methodology-demo v2.0) |
| observations | 23,926 | 0 |
| entities | 3,276 | 0 |
| technologies | 4,361 | 0 |
| decades_covered | 6 | 0 |
| v_studies_with_high_prescience | 865 | 0 (v2.0 = not-applicable per Rule A) |
| wiki pages | 10,383 | +1 |
| embedding rows | 10,439 | +1 |
| kw ask retrieves v2.0 at top | yes (score 0.499) | new |

---

## Commits shipped (chronological)

| Commit | Repo | Contents |
|---|---|---|
| `0a88d455` | aberdeen-group-archive | v2.0 source markdown + `add_methodology_demo_v2_study_row_v1.py` |
| `49f33d3f` | kastner-aberdeen-wiki | Hand-authored v2.0 wiki page + patched `RELEASE_NOTES_v1_6_2.md` |
| `53fc748c` | aberdeen-group-archive | `reembed_single_page_v1.py` (surgical embedding repair) |
| `229843c4` | aberdeen-group-archive | `06_emit_scaffolding_v5.py` (fix .gitignore + qwen3.5 fallback) |
| `0f5c9d71` | aberdeen-group-archive | `Perplexity_Only/PRESCIENCE_ARCHITECTURE.md` (§11v D6 map) |

---

## Open follow-ups

- **v1.7.0 ship gate:** F2 (commit promote script), F3 (`row_class` column decision), F6 (cloud parse-fail retag), F7 (preseed_skip SH treatment) all still open. Pete decisions needed on F3 + F7.
- **Mac-side uncommitted:** scaffolding regen + indices + .gitignore + embeddings.parquet need to ship to wiki repo — NOT done this session; deferred to next.
- **Gotcha 13 candidate:** "Phase 5 reads file list at start; mid-flight git pulls race." Surgical re-embed script handles the single-page case. Should be folded into `kastner-archive-pipeline` skill.
