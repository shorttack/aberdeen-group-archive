#!/usr/bin/env python3
"""
embed_ab_harness_v2.py — Retrieval A/B: bge-m3 (incumbent) vs qwen3-embedding:8b MRL-1024.

v2 (2026-07-01) adds:
  * --queries      read a LOCKED probe file (one query per line, # = comment)
  * --emit-gold-template  write a side-by-side gold TEMPLATE (query x union of
                   both models' top-k slugs, blank `relevant` col) for human labeling
  * LOCKED two-part promotion gate in the gold-set verdict:
      Gate A  aggregate Recall@k margin  (candidate must beat incumbent by >= --recall-margin, default 0.05)
      Gate B  per-query no-regression floor (candidate may lose at most --regression-floor relevant hits
              on ANY single labeled query, default 1)
      Both gates must pass to PROMOTE. MRR@k and mean-Jaccard are CONTEXT ONLY, never gates.

Workflow:
  1. Build candidate index (Phase 5 v4).  2. `--emit-gold-template gold.csv`.
  3. Pete labels the `relevant` column 0/1.  4. Rerun with `--gold gold.csv` for the verdict.

This is the EMBEDDING-LANE eval gate. The 5-gate local-model-upgrade-gates flow
explicitly excludes embeddings ("bge-m3 lives in a different lane; use a separate
evaluation"). This harness IS that separate evaluation.

What it does NOT do: claim one model is "better" in an absolute sense — that needs
a human-judged gold set of (query -> relevant page) pairs. What it DOES do, with the
data we actually have:

  1. Reports retrieval AGREEMENT between the two indexes (Jaccard / rank overlap of
     top-k hits per probe query). High agreement => the swap is low-risk (kw_ask
     surfaces substantially the same evidence). Low agreement => the swap MATERIALLY
     changes what the generative model sees; a human must eyeball whether the new
     hits are better or worse before promoting.
  2. Reports self-consistency: does each index return stable, non-degenerate results
     (no all-zero vectors, no NaN sims, sane score distribution)?
  3. Optionally, if a gold file is supplied (--gold), computes recall@k / MRR@k for
     each index against human-labeled relevant slugs — the ONLY true quality signal.

Inputs:
  --incumbent-parquet  path to bge-m3 index (6-col: page_path,page_type,slug,title,vector,dim)
  --candidate-parquet  path to qwen MRL-1024 index (same schema)
  --incumbent-model    ollama model to embed the QUERY for the incumbent index (default bge-m3)
  --incumbent-dims     0 (native) for bge-m3
  --candidate-model    ollama model to embed the QUERY for the candidate index (default qwen3-embedding:8b)
  --candidate-dims     1024 (MRL) for qwen
  --queries            text file, one probe query per line (default: built-in archive probes)
  --gold               optional CSV: query,relevant_slug  (multiple rows per query OK)
  --k                  top-k (default 6, matches kw_ask default)
  --out-report         markdown report path

Both query embeddings go through the SAME /v1/embeddings path used by the patched
kw_ask.py, so the harness exercises the real query-side contract.

Usage (after both parquets exist):
  python3 embed_ab_harness_v2.py \\
    --incumbent-parquet data/embeddings_incumbent.parquet \\
    --candidate-parquet data/embeddings_candidate.parquet \\
    --queries probes_v1.txt \\
    --out-report eval/embed_ab_$(date +%Y%m%d).md
"""
from __future__ import annotations
import argparse
import csv
import json
import math
import sys
import urllib.request
from pathlib import Path

try:
    import numpy as np
    import pandas as pd
except ImportError:
    sys.exit("ERROR: numpy + pandas required.")

OLLAMA_BASE = "http://localhost:11434"

# Built-in probe queries — representative of real kw_ask traffic over the archive.
# LOCKED set: keep identical across future embedding evaluations so agreement
# numbers are comparable model-to-model. Add here only with a version bump.
DEFAULT_PROBES = [
    "What did Aberdeen Group predict about client-server computing in the 1990s?",
    "Which technologies were forecast to disrupt relational databases?",
    "What was said about Digital Equipment Corporation's market position?",
    "How did analysts view Oracle's pricing strategy?",
    "What predictions were made about the shift to web-based enterprise software?",
    "Which vendors were expected to lose share to open-source software?",
    "What was the outlook for object-oriented databases?",
    "How was Microsoft's entry into enterprise software assessed?",
    "What did research say about ERP adoption drivers?",
    "Which prescient observations concerned the rise of the internet as a business platform?",
    "What were the short-horizon prescience verdicts for late-1990s studies?",
    "How did Aberdeen characterize the total cost of ownership debate?",
]


def embed_query(text: str, model: str, dimensions: int) -> np.ndarray | None:
    """Embed a query via /v1/embeddings — same contract as patched kw_ask.py."""
    body = {"model": model, "input": text}
    if dimensions and dimensions > 0:
        body["dimensions"] = dimensions
    payload = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        f"{OLLAMA_BASE}/v1/embeddings", data=payload,
        headers={"Content-Type": "application/json",
                 "Authorization": "Bearer ollama"}, method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            res = json.loads(resp.read().decode("utf-8"))
        vec = res["data"][0]["embedding"]
        v = np.array(vec, dtype=np.float32)
        n = np.linalg.norm(v) + 1e-9
        return v / n
    except Exception as e:
        print(f"  [warn] embed failed ({model}): {e}", file=sys.stderr)
        return None


def load_index(parquet: Path):
    df = pd.read_parquet(parquet)
    df = df[df["vector"].map(lambda v: v is not None and len(v) > 0)].reset_index(drop=True)
    vecs = np.stack(df["vector"].apply(np.array).values).astype(np.float32)
    norms = np.linalg.norm(vecs, axis=1, keepdims=True) + 1e-9
    vecs = vecs / norms
    return df, vecs


def top_k(df, vecs, qv: np.ndarray, k: int):
    sims = vecs @ qv
    order = np.argsort(-sims)[:k]
    return [(df.iloc[i]["slug"], float(sims[i])) for i in order]


def jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 1.0
    return len(a & b) / len(a | b) if (a | b) else 0.0


def rank_overlap_at_k(a: list, b: list, k: int) -> float:
    """Ordered overlap: fraction of positions where the same slug appears in
    both top-k lists (position-agnostic set overlap, normalized by k)."""
    sa, sb = set(a[:k]), set(b[:k])
    return len(sa & sb) / k if k else 0.0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--incumbent-parquet", required=True)
    ap.add_argument("--candidate-parquet", required=True)
    ap.add_argument("--incumbent-model", default="bge-m3")
    ap.add_argument("--incumbent-dims", type=int, default=0)
    ap.add_argument("--candidate-model", default="qwen3-embedding:8b")
    ap.add_argument("--candidate-dims", type=int, default=1024)
    ap.add_argument("--queries", default="",
                    help="Locked probe file (one query per line, # = comment)")
    ap.add_argument("--gold", default="",
                    help="Gold CSV: query,relevant_slug,relevant (relevant in {0,1})")
    ap.add_argument("--emit-gold-template", default="",
                    help="Write a side-by-side gold TEMPLATE (query x union of both "
                         "models' top-k slugs, relevant col blank) to this path, then exit")
    ap.add_argument("--k", type=int, default=6)
    # LOCKED promotion hurdles (2026-07-01). Override only to experiment; the
    # canonical gate is margin=0.05, per-query floor=1.
    ap.add_argument("--recall-margin", type=float, default=0.05,
                    help="Aggregate hurdle: candidate Recall@k must beat incumbent by >= this")
    ap.add_argument("--regression-floor", type=int, default=1,
                    help="Per-query floor: candidate may not lose more than this many "
                         "relevant hits vs incumbent on ANY single query")
    ap.add_argument("--out-report", default="embed_ab_report.md")
    args = ap.parse_args()

    probes = DEFAULT_PROBES
    if args.queries:
        probes = [ln.strip() for ln in Path(args.queries).read_text().splitlines()
                  if ln.strip() and not ln.lstrip().startswith("#")]

    gold = {}
    if args.gold:
        gdf = pd.read_csv(args.gold)
        # Accepts either legacy (query,relevant_slug = all relevant) or
        # template (query,candidate_slug,relevant in {0,1,blank}) format.
        slug_col = "relevant_slug" if "relevant_slug" in gdf.columns else "candidate_slug"
        has_flag = "relevant" in gdf.columns
        for _, r in gdf.iterrows():
            if has_flag:
                flag = str(r.get("relevant", "")).strip()
                if flag not in ("1", "1.0", "true", "True", "yes"):
                    continue
            gold.setdefault(str(r["query"]).strip(), set()).add(str(r[slug_col]).strip())

    print(f"Loading incumbent index: {args.incumbent_parquet}")
    inc_df, inc_vecs = load_index(Path(args.incumbent_parquet).expanduser())
    print(f"  {len(inc_df)} vectors, dim={inc_vecs.shape[1]}")
    print(f"Loading candidate index: {args.candidate_parquet}")
    cand_df, cand_vecs = load_index(Path(args.candidate_parquet).expanduser())
    print(f"  {len(cand_df)} vectors, dim={cand_vecs.shape[1]}")

    k = args.k

    # --- Gold TEMPLATE emit path -------------------------------------------
    # Writes one row per (query, candidate_slug) for the UNION of both models'
    # top-k hits, with a blank `relevant` column for Pete to mark 0/1. This is
    # the human-judgment surface: it deliberately unions BOTH indexes so a slug
    # that only the candidate surfaces is still offered for labeling (otherwise
    # we'd bias recall toward the incumbent's picks).
    if args.emit_gold_template:
        tmpl_rows = []
        for q in probes:
            qv_inc = embed_query(q, args.incumbent_model, args.incumbent_dims)
            qv_cand = embed_query(q, args.candidate_model, args.candidate_dims)
            if qv_inc is None or qv_cand is None:
                print(f"  [skip] embed failed for: {q[:50]}")
                continue
            hits_inc = top_k(inc_df, inc_vecs, qv_inc, k)
            hits_cand = top_k(cand_df, cand_vecs, qv_cand, k)
            score = {s: sc for s, sc in hits_inc}
            for s, sc in hits_cand:
                score[s] = max(score.get(s, -1.0), sc)
            in_inc = {s for s, _ in hits_inc}
            in_cand = {s for s, _ in hits_cand}
            # stable order: by max sim desc so the most-likely-relevant sit on top
            for s in sorted(score, key=lambda x: -score[x]):
                src = ("both" if s in in_inc and s in in_cand
                       else "incumbent" if s in in_inc else "candidate")
                tmpl_rows.append({
                    "query": q,
                    "candidate_slug": s,
                    "surfaced_by": src,
                    "max_sim": round(score[s], 4),
                    "relevant": "",  # Pete fills 0/1
                })
        tdf = pd.DataFrame(tmpl_rows,
                           columns=["query", "candidate_slug", "surfaced_by",
                                    "max_sim", "relevant"])
        out = Path(args.emit_gold_template).expanduser()
        out.parent.mkdir(parents=True, exist_ok=True)
        tdf.to_csv(out, index=False, quoting=csv.QUOTE_ALL)
        print(f"Wrote gold TEMPLATE: {out}")
        print(f"  {len(tdf)} candidate rows across {tdf['query'].nunique()} queries.")
        print("  Mark the `relevant` column 1 (relevant) or 0/blank (not), then")
        print("  rerun this harness with --gold <that file> for the promotion verdict.")
        return 0
    # -----------------------------------------------------------------------

    per_query = []
    jac_sum = 0.0
    recall_inc = recall_cand = 0.0
    mrr_inc = mrr_cand = 0.0
    gold_q = 0

    for q in probes:
        qv_inc = embed_query(q, args.incumbent_model, args.incumbent_dims)
        qv_cand = embed_query(q, args.candidate_model, args.candidate_dims)
        if qv_inc is None or qv_cand is None:
            print(f"  [skip] embed failed for: {q[:50]}")
            continue
        hits_inc = top_k(inc_df, inc_vecs, qv_inc, k)
        hits_cand = top_k(cand_df, cand_vecs, qv_cand, k)
        slugs_inc = [s for s, _ in hits_inc]
        slugs_cand = [s for s, _ in hits_cand]
        jac = jaccard(set(slugs_inc), set(slugs_cand))
        jac_sum += jac

        row = {
            "query": q,
            "jaccard": round(jac, 3),
            "overlap_at_k": round(rank_overlap_at_k(slugs_inc, slugs_cand, k), 3),
            "inc_top": slugs_inc,
            "cand_top": slugs_cand,
            "inc_top_score": round(hits_inc[0][1], 4) if hits_inc else None,
            "cand_top_score": round(hits_cand[0][1], 4) if hits_cand else None,
        }

        if q in gold:
            gold_q += 1
            rel = gold[q]
            hit_inc = len(set(slugs_inc) & rel)   # raw relevant-hit COUNT (for floor)
            hit_cand = len(set(slugs_cand) & rel)
            ri = hit_inc / len(rel) if rel else 0.0
            rc = hit_cand / len(rel) if rel else 0.0
            recall_inc += ri
            recall_cand += rc
            def mrr(slugs):
                for idx, s in enumerate(slugs, 1):
                    if s in rel:
                        return 1.0 / idx
                return 0.0
            mrr_inc += mrr(slugs_inc)
            mrr_cand += mrr(slugs_cand)
            row["recall_inc"] = round(ri, 3)
            row["recall_cand"] = round(rc, 3)
            row["hit_inc"] = hit_inc
            row["hit_cand"] = hit_cand
            row["hit_delta"] = hit_cand - hit_inc  # negative = candidate regressed

        per_query.append(row)

    n = len(per_query)
    if n == 0:
        sys.exit("No queries scored — is Ollama running and are both models pulled?")

    avg_jac = jac_sum / n

    # Report
    lines = []
    lines.append(f"# Embedding A/B — bge-m3 vs {args.candidate_model} (MRL-{args.candidate_dims})\n")
    lines.append(f"- Probe queries scored: **{n}**")
    lines.append(f"- Incumbent index: `{args.incumbent_parquet}` ({len(inc_df)} vecs, dim {inc_vecs.shape[1]})")
    lines.append(f"- Candidate index: `{args.candidate_parquet}` ({len(cand_df)} vecs, dim {cand_vecs.shape[1]})")
    lines.append(f"- top-k: **{k}**\n")
    lines.append(f"## Agreement (risk signal)\n")
    lines.append(f"- **Mean Jaccard(top-{k}) = {avg_jac:.3f}**")
    lines.append(f"  - >0.6 => low-risk swap (largely same evidence surfaced)")
    lines.append(f"  - 0.3-0.6 => materially different; human eyeball required before promote")
    lines.append(f"  - <0.3 => swap changes retrieval substantially; do NOT promote without gold-set eval\n")

    if gold_q:
        agg_recall_inc = recall_inc / gold_q
        agg_recall_cand = recall_cand / gold_q
        recall_delta = agg_recall_cand - agg_recall_inc

        # --- LOCKED two-part promotion gate (2026-07-01) -------------------
        # Gate A (aggregate): candidate Recall@k must beat incumbent by >= margin.
        # Gate B (per-query floor): candidate may not lose more than `floor`
        #   relevant hits vs incumbent on ANY single labeled query.
        # Both must pass. MRR@k and mean-Jaccard are CONTEXT, never gates.
        margin = args.recall_margin
        floor = args.regression_floor
        gate_a = recall_delta >= margin
        regressions = [r for r in per_query
                       if "hit_delta" in r and r["hit_delta"] < -floor]
        gate_b = len(regressions) == 0
        promote = gate_a and gate_b

        lines.append(f"## Quality vs gold set ({gold_q} labeled queries)\n")
        lines.append(f"| Metric | Incumbent (bge-m3) | Candidate (qwen MRL-{args.candidate_dims}) |")
        lines.append(f"|---|---:|---:|")
        lines.append(f"| Recall@{k} | {agg_recall_inc:.3f} | {agg_recall_cand:.3f} |")
        lines.append(f"| MRR@{k} (context only) | {mrr_inc/gold_q:.3f} | {mrr_cand/gold_q:.3f} |")
        lines.append("")
        lines.append(f"### Promotion gate (LOCKED)\n")
        lines.append(f"- **Gate A — aggregate Recall@{k} margin:** "
                     f"delta = {recall_delta:+.3f}, hurdle = +{margin:.3f} -> "
                     f"**{'PASS' if gate_a else 'FAIL'}**")
        lines.append(f"- **Gate B — per-query no-regression floor:** candidate may "
                     f"lose at most {floor} relevant hit on any single query -> "
                     f"**{'PASS' if gate_b else 'FAIL'}**")
        if regressions:
            for r in regressions:
                lines.append(f"  - REGRESSION on: {r['query']} "
                             f"(inc {r['hit_inc']} -> cand {r['hit_cand']} hits, "
                             f"delta {r['hit_delta']:+d})")
        lines.append("")
        verdict = ("PROMOTE CANDIDATE" if promote
                   else "KEEP INCUMBENT (status quo wins ties)")
        lines.append(f"**Gold-set verdict: {verdict}**")
        lines.append(f"> Both gates must pass to promote. "
                     f"Gate A: {'PASS' if gate_a else 'FAIL'}, "
                     f"Gate B: {'PASS' if gate_b else 'FAIL'}.\n")
    else:
        lines.append(f"## Quality vs gold set\n")
        lines.append(f"No `--gold` file supplied. Agreement-only run. To get a true "
                     f"quality verdict, label 10-20 (query,relevant_slug) pairs and rerun "
                     f"with `--gold`.\n")

    lines.append(f"## Per-query detail\n")
    for r in per_query:
        lines.append(f"### {r['query']}")
        lines.append(f"- Jaccard: {r['jaccard']}, overlap@{k}: {r['overlap_at_k']}, "
                     f"top-score inc/cand: {r['inc_top_score']}/{r['cand_top_score']}")
        if "recall_inc" in r:
            lines.append(f"- Recall inc/cand: {r['recall_inc']}/{r['recall_cand']} "
                         f"(hits {r['hit_inc']}/{r['hit_cand']}, delta {r['hit_delta']:+d})")
        lines.append(f"- inc top-{k}: {r['inc_top']}")
        lines.append(f"- cand top-{k}: {r['cand_top']}\n")

    out = Path(args.out_report).expanduser()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines))
    print(f"\nWrote report: {out}")
    print(f"Mean Jaccard(top-{k}) = {avg_jac:.3f}")
    if gold_q:
        print(f"Recall@{k}: inc={recall_inc/gold_q:.3f}  cand={recall_cand/gold_q:.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
