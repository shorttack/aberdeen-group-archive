# Embedding-Upgrade Gates

A self-contained toolkit and methodology for deciding whether to swap the embedding
model behind a retrieval-augmented archive. Built for the Aberdeen Group archive's
`kw_ask` retrieval layer (currently **bge-m3, 1024-dim**), but the method and scripts
generalize to any RAG corpus where an embedding-model change would re-shape what the
generative model retrieves.

**Core bias: status quo wins ties.** A candidate embedder must pass every gate, in
order, to earn promotion. Failing any gate keeps the incumbent. The blast radius of
a bad embedding swap is the entire retrieval surface — the whole corpus must be
re-embedded and every downstream answer shifts — so the bar is deliberately high.

## Start here

1. Read `METHODOLOGY.md` — the full gate flow (0–4) and the locked promotion hurdles.
2. When a candidate model appears, work the gates in order.

## The locked promotion gate (one-line version)

Promote the candidate **only if BOTH**:
- **Gate A:** aggregate Recall@6 beats the incumbent by **≥ +0.05**, AND
- **Gate B:** on **no single query** does the candidate lose more than **1** relevant hit.

MRR@6 and mean-Jaccard are **context only, never gates**.

## File map

| Path | Role |
|---|---|
| `README.md` | this file — entry point + map |
| `METHODOLOGY.md` | gate flow 0–4, locked hurdles, anti-patterns |
| `probes_v1.txt` | 20 locked probe queries (FROZEN — a bump requires re-baselining) |
| `scripts/embed_ab_harness_v2.py` | agreement A/B + `--emit-gold-template` + `--gold` two-part gate |
| `scripts/build_gold_template_v1.py` | pre-fills a labeling template from a recorded A/B run |
| `gold/embed_gold_template_prefilled_v1.csv` | example labeling template (12 probes, `relevant` column blank) |

## Standard candidate workflow

The retrieval index must already exist as a parquet with the 6-column schema
`page_path, page_type, slug, title, vector, dim`. Build the incumbent snapshot and
the candidate index as separate parquets (never overwrite the live index during
evaluation). A local Ollama serving both embedding models is assumed; adjust
`--incumbent-model` / `--candidate-model` for other backends.

```bash
# Gate 3 step 1 — agreement A/B (no gold yet)
python3 scripts/embed_ab_harness_v2.py \
  --incumbent-parquet data/embeddings_incumbent.parquet \
  --candidate-parquet data/embeddings_candidate.parquet \
  --queries probes_v1.txt \
  --out-report eval/embed_ab_$(date +%Y%m%d).md

# Gate 3 step 2 — emit the labeling template (union of both models' top-k hits)
python3 scripts/embed_ab_harness_v2.py \
  --incumbent-parquet data/embeddings_incumbent.parquet \
  --candidate-parquet data/embeddings_candidate.parquet \
  --queries probes_v1.txt \
  --emit-gold-template eval/gold_template.csv

# Gate 3 step 3 — a human labels the `relevant` column 1/0.

# Gate 3 step 4 — the verdict (two-part gate applied automatically)
python3 scripts/embed_ab_harness_v2.py \
  --incumbent-parquet data/embeddings_incumbent.parquet \
  --candidate-parquet data/embeddings_candidate.parquet \
  --queries probes_v1.txt \
  --gold eval/gold_template.csv \
  --out-report eval/embed_gold_verdict_$(date +%Y%m%d).md
```

The verdict report prints **PROMOTE CANDIDATE** or **KEEP INCUMBENT** with per-gate
PASS/FAIL. On KEEP, archive the candidate index and the labeled gold report as the
next candidate's baseline and leave the live index untouched.

## A note on the dimension contract

The live index, the query-time embedding call, and every stored vector must agree on
dimensionality. Some candidate models are natively larger (e.g. 4096-dim) but support
Matryoshka (MRL) truncation to a smaller size that preserves the incumbent schema.
When using Ollama for MRL truncation, note that the native `/api/embeddings` endpoint
ignores the `dimensions` parameter — use the OpenAI-compatible `/v1/embeddings`
endpoint with `dimensions: N`, and L2-normalize the truncated vectors before cosine
similarity. Verify the returned vector length with a two-request preflight probe
before committing to a full corpus re-embed.
