# Embedding-Upgrade Gates

Self-contained toolkit + methodology for deciding whether to swap the embedding
model behind `kw_ask` retrieval (currently **bge-m3, 1024-dim**). This is the
**embedding lane** — deliberately separate from the generative-LLM lane governed by
the `local-model-upgrade-gates` skill, which explicitly excludes embeddings.

**Core bias: status quo wins ties.** A candidate embedder must pass every gate, in
order, to earn promotion. Failing any gate keeps the incumbent. The blast radius of
a bad embedding swap is the entire retrieval surface (~10,900 pages re-embedded,
every `kw_ask` answer shifted), so the bar is high.

## Start here

1. Read `METHODOLOGY.md` — the full gate flow (0–4) and the LOCKED promotion hurdles.
2. When a candidate appears, work the gates in order. The auto-loading skill
   `embedding-upgrade-gates` (user scope) points back to this directory.

## The LOCKED promotion gate (one-line version)

Promote the candidate **only if BOTH**:
- **Gate A:** aggregate Recall@6 beats incumbent by **≥ +0.05**, AND
- **Gate B:** on **no single query** does the candidate lose more than **1** relevant hit.

MRR@6 and mean-Jaccard are **context only, never gates**.

## File map

| Path | Role | Status |
|---|---|---|
| `README.md` | this file — entry point + map | — |
| `METHODOLOGY.md` | gate flow 0–4, locked hurdles, anti-patterns | canonical |
| `probes_v1.txt` | 20 LOCKED probe queries | **FROZEN** — bump = re-baseline |
| `scripts/embed_ab_harness_v2.py` | agreement A/B + `--emit-gold-template` + `--gold` two-part gate | current |
| `scripts/build_gold_template_v1.py` | pre-fills the 12 original probes' labeling rows from the 2026-07-01 A/B | one-off |
| `gold/embed_gold_template_prefilled_v1.csv` | 12 probes pre-filled (118 rows), `relevant` col blank | awaiting labels |
| `baselines/bgem3_vs_qwen3emb8b_20260701.md` | first candidate's frozen record | baseline-to-beat |

## The standard candidate workflow (on the Mac — Pete drives)

Ollama must be running; both the incumbent snapshot and the candidate index parquet
must exist under `~/Repos/kastner-aberdeen-wiki/data/`.

```bash
cd ~/Repos/kastner-aberdeen-wiki

# Gate 3 step 1 — agreement A/B (no gold yet)
python3 <archive>/Perplexity_Only/embedding-upgrade-gates/scripts/embed_ab_harness_v2.py \
  --incumbent-parquet data/embeddings_bgem3.parquet \
  --candidate-parquet data/embeddings_qwen1024.parquet \
  --queries <archive>/Perplexity_Only/embedding-upgrade-gates/probes_v1.txt \
  --out-report ~/Desktop/Archive/eval/embed_ab_$(date +%Y%m%d).md

# Gate 3 step 2 — emit the FULL 20-probe labeling template
python3 .../scripts/embed_ab_harness_v2.py \
  --incumbent-parquet data/embeddings_bgem3.parquet \
  --candidate-parquet data/embeddings_qwen1024.parquet \
  --queries .../probes_v1.txt \
  --emit-gold-template ~/Desktop/Archive/eval/embed_gold_20probes.csv

# (Pre-filled shortcut: gold/embed_gold_template_prefilled_v1.csv already covers the
#  first 12 probes; either label that and append the 8 new probes' rows from the emit
#  above, or just label the full 20-probe emit.)

# Gate 3 step 3 — Pete labels the `relevant` column 1/0 by hand.

# Gate 3 step 4 — the verdict (two-part gate applied automatically)
python3 .../scripts/embed_ab_harness_v2.py \
  --incumbent-parquet data/embeddings_bgem3.parquet \
  --candidate-parquet data/embeddings_qwen1024.parquet \
  --queries .../probes_v1.txt \
  --gold ~/Desktop/Archive/eval/embed_gold_20probes.csv \
  --out-report ~/Desktop/Archive/eval/embed_gold_verdict_$(date +%Y%m%d).md
```

The verdict report prints **PROMOTE CANDIDATE** or **KEEP INCUMBENT** with per-gate
PASS/FAIL. If it says KEEP, archive the candidate index + the labeled gold report as
the next candidate's baseline and do nothing to the live index.

## Companion (not in this directory)

- `Perplexity_Only/OLLAMA_GOTCHAS.md` — the append-only landmine ledger. Gate 0 reads
  it. The embedding-relevant entry: Ollama `/api/embeddings` ignores `dimensions`;
  use `/v1/embeddings` + `dimensions:N` + L2-normalize for MRL truncation.
- Phase 5 v4 (`scripts/build/05_compute_embeddings_v4.py`) builds candidate indexes.
- Query side: `kw_ask` + `reembed` patched variants (see the swap run-pack).
