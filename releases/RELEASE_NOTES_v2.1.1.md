# Aberdeen Archive v2.1.1 — Documentation & Provenance Cleanup

**Type:** Patch release. Documentation and repository-hygiene only — **no data, schema, or scoring change.** All corpus counts, masters, and prescience surfaces are identical to v2.1.

## What changed

- **README** rewritten for clarity and a neutral, product-facing engineering tone. Version numbers, counts, and factual history are unchanged; only framing was refined. Corpus statistics continue to live in the generated [`ARCHIVE_STATS.md`](../ARCHIVE_STATS.md).
- **Repository scope tightened.** Local development-only material (internal working notes and a curatorial log) is no longer tracked in the public tree; it remains part of the maintainer's local workflow. Structured artifacts, masters, per-study Frictionless packages, schemas, and skills are unchanged and fully public.
- **Companion wiki** (`kastner-aberdeen-wiki`) setup/user docs de-branded to vendor-neutral "optional cloud LLM" language; local-first Ollama configuration is unchanged.

## Unchanged since v2.1

- `_master_*.csv` (studies, entities, technologies, observations, prescience scores, short-horizon) — byte-identical to v2.1.
- Studies master remains 20 columns; per-study `studies.csv` remains 16 columns.
- Long-horizon (Pass C) and short-horizon (3y/5y) prescience surfaces unchanged.
- DOI series continues via Zenodo.

## Citation

> Kastner, Peter S. (2026). *Kastner IT Research Archive*, version 2.1.1. Licensed under CC-BY-4.0. DOI: 10.5281/zenodo.20245076.
