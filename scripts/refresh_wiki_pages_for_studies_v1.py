#!/usr/bin/env python3
"""refresh_wiki_pages_for_studies_v1.py  — TARGETED Phase-3 page refresh.

Regenerate the wiki markdown pages for a SPECIFIC set of study_ids (with tier-1
LLM enrichment) WITHOUT re-running Phase 3 over the whole 1500-study corpus
(which is a ~6.5h tier-1 LLM run). This is the fast path for small study
batches: it drives the canonical Phase-3 emitter `emit_study` from the parquets
Phase 1 already wrote, but only for the studies you name.

WHY THIS IS SAFE:
- It imports and calls the *canonical* `emit_study` from 03_generate_vault_v3.py
  — identical page shape/frontmatter as a full run, no forked logic.
- It reads the SAME parquets a full Phase 3 reads (studies/observations in
  <wiki>/data), so prescience_max/mean/enum reflect the just-promoted scores.
- It only WRITES the pages for the named study_ids. No other page is touched.

AFTER THIS, still run (targeted):
  Phase 4 (indices)      — fast, regenerates index/base/dataview pages
  Phase 5 (embeddings)   — re-embed; bge-m3. Use --limit or the changed-only path.
  Phase 6 (scaffolding)  — refreshes README/AGENTS counts

USAGE:
  python3 refresh_wiki_pages_for_studies_v1.py \
      --wiki /Users/scott/Repos/kastner-aberdeen-wiki \
      --study-ids 2026-kastner-compaq-dell-pc-clones-split,2026-kastner-...   # comma list
  add --skip-llm to emit the scaffold only (no LLM), for a dry structural check.
"""
import argparse, importlib.util, sys
from pathlib import Path
import pandas as pd

BUILD_DIR = Path.home() / "Desktop/Archive/scripts/build"
PHASE3 = BUILD_DIR / "03_generate_vault_v3.py"


def load_phase3():
    spec = importlib.util.spec_from_file_location("phase3", PHASE3)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki", required=True)
    ap.add_argument("--study-ids", required=True, help="comma-separated study_ids")
    ap.add_argument("--skip-llm", action="store_true")
    a = ap.parse_args()

    wiki = Path(a.wiki)
    data = wiki / "data"
    ids = [s.strip() for s in a.study_ids.split(",") if s.strip()]

    p3 = load_phase3()

    studies = pd.read_parquet(data / "studies.parquet")
    obs = pd.read_parquet(data / "observations.parquet")

    # tier-1 set computed EXACTLY as the full Phase 3 does (prescience_max >= 4)
    tier1 = set(studies.loc[studies["prescience_max"].fillna(0) >= 4, "study_id"])

    sub = studies[studies["study_id"].isin(ids)]
    missing = set(ids) - set(sub["study_id"])
    if missing:
        sys.exit(f"ERROR: study_ids not found in studies.parquet: {sorted(missing)}")

    do_llm = not a.skip_llm
    print(f"targeted refresh: {len(sub)} studies  (LLM={'on' if do_llm else 'off'})")
    for _, row in sub.iterrows():
        sid = row["study_id"]
        study_obs = obs[obs["study_id"] == sid]
        local_do_llm = do_llm and (sid in tier1)
        res = p3.emit_study(row, study_obs, wiki, tier1, local_do_llm)
        tag = "tier-1 LLM" if local_do_llm else ("tier-1 no-llm" if sid in tier1 else "tier-2")
        pth = res.get("page_path") if isinstance(res, dict) else res
        print(f"  wrote {sid}  [{tag}]  -> {pth}")
    print("done. Now run Phase 4 (indices), Phase 5 (re-embed), Phase 6 (scaffolding).")


if __name__ == "__main__":
    main()
