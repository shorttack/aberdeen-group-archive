## 2026-06-22 — CompChem 1989 ingest + v1.9.0 release on both repos

**Session:** 2026-06-22 (AM new-day kickoff → PM CompChem ingest → PM v1.9.0 ship)
**Scope:** Recover one of three §1 missing sources; ship combined v1.9.0 release covering v1.8.0 substrate work + CompChem exemplar.

---

### What landed

**CompChem 1989 — Casale, "Conflicting Trends In Computational Chemistry"**

- **Study path:** NEW top-level `project_examples/conflicting-trends-computational-chemistry-fe5c31/` (Pete chose this over `other-authors/` to mark this as a project-examples exemplar — the first study under that bucket).
- **Date:** **1989-01 canonical** (Jan 1989 publication; May 1989 cover is a reprint of the same study — noted in metadata).
- **Author:** Charles T. Casale (Aberdeen co-founder).
- **License:** CC-BY-NC-SA-4.0 (Aberdeen archival material; conservative posture).
- **Extraction tallies:** 1 study / 24 entities / 10 technologies / **64 observations** / 31 codes / 165 figures.
  - Per Pete's directive: "no limit on observations" — extracted comprehensively from all 168 pages.
- **Validation:** All 5 CSV gate checks PASS (after in-place fix of 5 hardware-share rows where `tech_id` was initially placed in the `entity_id` column). All assembler validations PASS.
- **PDF source:** 8.5MB, 168 pages, ABBYY FineReader OCR.
- **Archive commit:** `a02c23f1` — 175-file tree commit via Git Data API batch pattern (create N blobs → POST `/git/trees` with base_tree + entries → POST `/git/commits` → PATCH `/git/refs/heads/main`; tree request body for 175 files = ~33KB JSON, well under limits).
- **Private repo commit:** `33a52bf3` — `aberdeen-1989/CompChem.pdf` (single-blob commit via `--input` JSON body for E2BIG safety).

**§1 missing-sources registry status:** Casale 1989 CLOSED. Two remain:
- Robbins 1991 ATM (open)
- Kastner 1987 Yankee Group Transaction Processing (open)

---

### v1.9.0 release decisions

- **Version tag:** v1.9.0 (skipping untagged v1.8.0 version number — v1.8.0 substrate work shipped at archive `f88107bf`/`3e4c1b66`/`6918d6e0` etc. but never received a tag or GitHub Release).
- **Repos tagged:** Archive + Wiki (sibling release). `kastner-restricted-sources` not tagged (private; no public release).
- **Release-notes scope:** **Combined** — v1.8.0 substrate silent-loss recovery (1087→1208 rows; F4 substrate-cap finding at ~470-480 articles absent additional source PDFs) + CompChem 1989 exemplar (first `project_examples/` study).
- **Notes pre-staged:** `RELEASE_NOTES_v1_9_0.md` at archive `71b8a385` + wiki `e018d1f1` (sibling).

**Mac-side release sequence (both repos):**

```bash
git pull origin main
git tag -a v1.9.0 -m "v1.9.0 — <title>"
git push origin v1.9.0
gh release create v1.9.0 \
  --title "v1.9.0 — <title>" \
  --notes-file RELEASE_NOTES_v1_9_0.md
```

- **Archive release:** https://github.com/shorttack/aberdeen-group-archive/releases/tag/v1.9.0
- **Wiki release:** https://github.com/shorttack/kastner-aberdeen-wiki/releases/tag/v1.9.0

Branch-protection bypass warnings flagged on both pushes — future commit-signing setup tracked as standing item.

---

### Gotchas reinforced this session

1. **Apostrophes in Python heredoc:** writing data with apostrophes inside `<<'PY'` blocks causes `SyntaxError`. Canonical fix: write data to a separate `.py` file (`write_obs.py` in this session) and execute it.
2. **`csv.QUOTE_ALL` mandatory** for all CSV writes (Section 16.5 of `archival-ingest` v20).
3. **Plain-text validation false-positive** when the header line exceeds 200 bytes with no newline in the probe window — manual verification required.
4. **GitHub URLs in messages:** use the connector via `api_credentials=["github"]` from `bash`, NOT `browser_task`. The session was reminded mid-flow.
5. **Validation-gate false REVIEWs** can be caught by re-reading the source ingest CSVs; the assembler flagged 5 rows where `tech_id` values were placed in the `entity_id` column for hardware-share observations. In-place fix + re-run was sufficient.

---

### Cost posture

- v1.8.0 cumulative: ~$34
- CompChem ingest: minimal incremental (extraction was deterministic, not LLM-scored — Pass C runs against masters later)
- Standing ceiling: $500 — comfortable headroom for Mac MCP Bridge Phase 0 + ongoing work.

---

### Carry-forward

- **Mac MCP Bridge — Phase 0 scaffolding** still pending (APPROVED 2026-06-20 PM; architecture docs at `docs/mac_mcp_bridge_architecture_v1.md` + `docs/promoted_mac.md` in archive).
- **A-step format-mismatch review CSV** (27 rows: 17 F0a + 7 F6 + 2 F3 + 1 F1) queued from v1.8.0 substrate work.
- **Source-PDF scouting** for 410 terminal `pdf_format_mismatch` rows — deferred future workstream.
- **CompChem Pass C scoring** — the 64 new observations will pick up Pass C scoring at the next pipeline run (canonical paths per `kastner-archive-pipeline` skill).
