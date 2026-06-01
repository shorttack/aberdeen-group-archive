#!/usr/bin/env python3
"""
03_generate_vault_v1.py — Phase 3: Generate Obsidian Markdown vault (v1.5)

Walks the data/ Parquet files and emits one Markdown page per entity, tech,
study, plus collection/decade/theme/Volume-1 overview pages. Tier-1 pages
get LLM summaries via _llm_helper_v1.py (local qwen for entities/techs,
cloud for studies + Volume 1).

v1.5 delta vs v1:
  * Every page frontmatter gets prescience_max, prescience_mean,
    prescience_obs_count (when scored).
  * Tier-1 LLM prompts include prescience scores + rationales for the
    page's top observations.
  * New `prescient/` slug folder for the top 50 highest-prescient studies.
  * Tier-1 set explicitly includes studies with prescience_max >= 4.

Usage:
  python3 03_generate_vault_v1.py --wiki ~/Desktop/kastner_wiki \\
      [--skip-llm] [--limit-llm N] [--only-type {study,entity,technology,volume-1}]
"""
from __future__ import annotations
import argparse
import json
import os
import re
import sys
import textwrap
from datetime import datetime, timezone
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    sys.exit("ERROR: pandas required.")

sys.path.insert(0, str(Path(__file__).parent))
import _llm_helper_v1 as llm

PAGE_CAPS = {
    "entity":     1500,
    "technology": 1500,
    "study":      2000,
    "volume-1":   3500,
    "collection": 2500,
    "decade":     2000,
    "stub":       500,
    "index":      1500,
}


def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "untitled"


def frontmatter(d: dict) -> str:
    lines = ["---"]
    for k, v in d.items():
        if v is None or v == "" or (isinstance(v, list) and not v):
            continue
        if isinstance(v, list):
            lines.append(f"{k}: [{', '.join(json.dumps(x) for x in v)}]")
        elif isinstance(v, (int, float)):
            lines.append(f"{k}: {v}")
        elif isinstance(v, bool):
            lines.append(f"{k}: {str(v).lower()}")
        else:
            lines.append(f"{k}: {json.dumps(str(v))}")
    lines.append("---\n")
    return "\n".join(lines)


def write_page(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(body)
    os.replace(tmp, path)


def cap_text(text: str, cap_tokens: int) -> str:
    # Rough cap: 1 token ≈ 4 chars. Truncate with pointer.
    cap_chars = cap_tokens * 4
    if len(text) <= cap_chars:
        return text
    return text[:cap_chars] + "\n\n...[truncated. See DuckDB or source data.]\n"


# ---------------- entity pages ----------------

def emit_entity(row, obs_for_entity: pd.DataFrame, wiki: Path,
                tier1_set: set, do_llm: bool) -> dict:
    eid = row["entity_id"]
    slug = slugify(eid)
    is_tier1 = eid in tier1_set
    page_path = wiki / "wiki" / "entities" / f"{slug}.md"

    aliases = []
    if row.get("aliases"):
        aliases = [a.strip() for a in str(row["aliases"]).split(";") if a.strip()]
    occ = int(row.get("occurrence_count") or 0)

    # Prescience aggregate over this entity's observations
    psc_obs = obs_for_entity.dropna(subset=["prescience_score"])
    pmax = float(psc_obs["prescience_score"].max()) if len(psc_obs) else None
    pmean = float(psc_obs["prescience_score"].mean()) if len(psc_obs) else None

    fm = {
        "title": row.get("canonical_name", eid),
        "slug": slug,
        "page_type": "entity",
        "aliases": aliases,
        "tags": ["type/entity"],
        "tier": 1 if is_tier1 else 2,
        "source_csv": "_master_entities.csv",
        "occurrence_count": occ,
        "prescience_max": pmax,
        "prescience_mean": round(pmean, 2) if pmean is not None else None,
        "prescience_obs_count": len(psc_obs),
    }

    body = [frontmatter(fm), f"# {row.get('canonical_name', eid)}\n"]

    # Top 20 observations (prefer high-prescience first)
    sample = obs_for_entity.sort_values(
        ["prescience_score", "obs_id"], ascending=[False, True], na_position="last"
    ).head(20)

    if is_tier1 and do_llm:
        prompt_obs = []
        for _, o in sample.iterrows():
            ps = o.get("prescience_score")
            mv = str(o.get("metric_value", ""))[:300]
            ps_tag = f" [P={int(ps)}]" if pd.notna(ps) else ""
            prompt_obs.append(f"- [{o['obs_id']}]{ps_tag} {mv}")
        prompt = (
            f"Entity: {row.get('canonical_name', eid)}\n"
            f"Aberdeen Group observations (P=prescience score 0-5):\n"
            + "\n".join(prompt_obs)
        )
        res = llm.summarize("entity", prompt, system=llm.SYSTEM_PROMPT_ENTITY)
        if res["ok"]:
            body.append("## Summary\n")
            body.append(cap_text(res["text"], PAGE_CAPS["entity"]) + "\n")
        else:
            body.append(f"<!-- LLM error: {res['error']} -->\n")
    body.append("## Observations\n")
    for _, o in sample.iterrows():
        ps = o.get("prescience_score")
        ps_tag = f" **[P={int(ps)}]**" if pd.notna(ps) else ""
        body.append(f"- `{o['obs_id']}`{ps_tag} — {str(o.get('metric_value',''))[:400]}")
        if pd.notna(o.get("study_id")):
            body.append(f"  → [[study-{slugify(o['study_id'])}|{o['study_id']}]]")
    body.append("")
    if len(obs_for_entity) > 20:
        body.append(f"_See DuckDB `v_observations` filtered by entity_id='{eid}' for all {len(obs_for_entity)} observations._\n")
    write_page(page_path, "\n".join(body))
    return {"slug": slug, "tier": fm["tier"], "type": "entity"}


# ---------------- technology pages ----------------

def emit_technology(row, obs_for_tech: pd.DataFrame, wiki: Path,
                    tier1_set: set, do_llm: bool) -> dict:
    tid = row["tech_id"]
    slug = slugify(tid)
    is_tier1 = tid in tier1_set
    page_path = wiki / "wiki" / "technologies" / f"{slug}.md"
    occ = int(row.get("occurrence_count") or 0)

    psc_obs = obs_for_tech.dropna(subset=["prescience_score"])
    pmax = float(psc_obs["prescience_score"].max()) if len(psc_obs) else None
    pmean = float(psc_obs["prescience_score"].mean()) if len(psc_obs) else None

    fm = {
        "title": row.get("canonical_name", tid),
        "slug": slug,
        "page_type": "technology",
        "tags": ["type/technology"],
        "tier": 1 if is_tier1 else 2,
        "source_csv": "_master_technologies.csv",
        "occurrence_count": occ,
        "prescience_max": pmax,
        "prescience_mean": round(pmean, 2) if pmean is not None else None,
        "prescience_obs_count": len(psc_obs),
    }
    body = [frontmatter(fm), f"# {row.get('canonical_name', tid)}\n"]

    sample = obs_for_tech.sort_values(
        ["prescience_score", "obs_id"], ascending=[False, True], na_position="last"
    ).head(20)

    if is_tier1 and do_llm:
        prompt_obs = []
        for _, o in sample.iterrows():
            ps = o.get("prescience_score")
            ps_tag = f" [P={int(ps)}]" if pd.notna(ps) else ""
            prompt_obs.append(f"- [{o['obs_id']}]{ps_tag} {str(o.get('metric_value',''))[:300]}")
        prompt = (
            f"Technology: {row.get('canonical_name', tid)}\n"
            f"Aberdeen Group observations:\n" + "\n".join(prompt_obs)
        )
        res = llm.summarize("technology", prompt, system=llm.SYSTEM_PROMPT_TECH)
        if res["ok"]:
            body.append("## Summary\n")
            body.append(cap_text(res["text"], PAGE_CAPS["technology"]) + "\n")
        else:
            body.append(f"<!-- LLM error: {res['error']} -->\n")
    body.append("## Observations\n")
    for _, o in sample.iterrows():
        ps = o.get("prescience_score")
        ps_tag = f" **[P={int(ps)}]**" if pd.notna(ps) else ""
        body.append(f"- `{o['obs_id']}`{ps_tag} — {str(o.get('metric_value',''))[:400]}")
    body.append("")
    if len(obs_for_tech) > 20:
        body.append(f"_See DuckDB `v_observations` filtered by tech_id='{tid}' for all {len(obs_for_tech)} observations._\n")
    write_page(page_path, "\n".join(body))
    return {"slug": slug, "tier": fm["tier"], "type": "technology"}


# ---------------- study pages ----------------

def emit_study(row, obs_for_study: pd.DataFrame, wiki: Path,
               tier1_set: set, do_llm: bool) -> dict:
    sid = row["study_id"]
    slug = "study-" + slugify(sid)
    is_tier1 = sid in tier1_set
    page_path = wiki / "wiki" / "studies" / f"{slug}.md"

    psc = obs_for_study.dropna(subset=["prescience_score"])
    pmax = float(psc["prescience_score"].max()) if len(psc) else None
    pmean = float(psc["prescience_score"].mean()) if len(psc) else None

    fm = {
        "title": row.get("title") or sid,
        "slug": slug,
        "page_type": "study",
        "tags": ["type/study", f"collection/{row.get('type','unknown')}"],
        "tier": 1 if is_tier1 else 2,
        "source_csv": "_master_studies.csv",
        "study_id": sid,
        "pub_year": row.get("pub_year"),
        "prescience_max": pmax,
        "prescience_mean": round(pmean, 2) if pmean is not None else None,
        "prescience_obs_count": len(psc),
    }
    body = [frontmatter(fm), f"# {row.get('title') or sid}\n"]
    body.append(f"**Study ID**: `{sid}`  ")
    if row.get("pub_year"):
        body.append(f"**Year**: {row['pub_year']}  ")
    body.append(f"**Type**: {row.get('type', 'unknown')}\n")

    sample = obs_for_study.sort_values(
        ["prescience_score", "obs_id"], ascending=[False, True], na_position="last"
    ).head(25)

    if is_tier1 and do_llm:
        prompt_obs = []
        for _, o in sample.iterrows():
            ps = o.get("prescience_score")
            ps_tag = f" [P={int(ps)}]" if pd.notna(ps) else ""
            rat = str(o.get("prescience_rationale", ""))[:200] if pd.notna(o.get("prescience_rationale")) else ""
            rat_tag = f" — rationale: {rat}" if rat else ""
            prompt_obs.append(f"- [{o['obs_id']}]{ps_tag} {str(o.get('metric_value',''))[:300]}{rat_tag}")
        prompt = (
            f"Study: {row.get('title') or sid} ({row.get('pub_year', 'unknown')})\n"
            f"Observations with prescience scores (P=0-5):\n"
            + "\n".join(prompt_obs)
        )
        res = llm.summarize("study", prompt, system=llm.SYSTEM_PROMPT_STUDY)
        if res["ok"]:
            body.append("## Summary\n")
            body.append(cap_text(res["text"], PAGE_CAPS["study"]) + "\n")
        else:
            body.append(f"<!-- LLM error: {res['error']} -->\n")

    body.append("## Top observations (by prescience)\n")
    for _, o in sample.iterrows():
        ps = o.get("prescience_score")
        ps_tag = f" **[P={int(ps)}]**" if pd.notna(ps) else ""
        body.append(f"- `{o['obs_id']}`{ps_tag} — {str(o.get('metric_value',''))[:400]}")
    body.append("")
    write_page(page_path, "\n".join(body))
    return {"slug": slug, "tier": fm["tier"], "type": "study"}


# ---------------- main ----------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki", required=True)
    ap.add_argument("--skip-llm", action="store_true",
                    help="Template-only; no LLM calls")
    ap.add_argument("--limit-llm", type=int, default=0,
                    help="Cap LLM calls per page-type (0 = no cap)")
    ap.add_argument("--only-type",
                    choices=["study", "entity", "technology"],
                    help="Process only one page type (debug)")
    args = ap.parse_args()

    wiki = Path(args.wiki).resolve()
    data = wiki / "data"

    studies = pd.read_parquet(data / "studies.parquet")
    entities = pd.read_parquet(data / "entities.parquet")
    techs = pd.read_parquet(data / "technologies.parquet")
    obs = pd.read_parquet(data / "observations.parquet")

    # ----- Tier-1 sets -----
    high_psc_studies = set(
        studies.loc[studies["prescience_max"].fillna(0) >= 4, "study_id"]
    )
    # Top 200 entities by occurrence
    e_top = set(
        entities.sort_values("occurrence_count", ascending=False, key=lambda s: pd.to_numeric(s, errors="coerce"))
                .head(200)["entity_id"]
    )
    # Top 150 technologies
    t_top = set(
        techs.sort_values("occurrence_count", ascending=False, key=lambda s: pd.to_numeric(s, errors="coerce"))
             .head(150)["tech_id"]
    )
    print(f"Tier-1 sets — studies:{len(high_psc_studies)}, "
          f"entities:{len(e_top)}, techs:{len(t_top)}")

    pages_manifest: list[dict] = []
    do_llm = not args.skip_llm

    # ----- Studies -----
    if args.only_type in (None, "study"):
        llm_used = 0
        for _, row in studies.iterrows():
            sid = row["study_id"]
            study_obs = obs[obs["study_id"] == sid]
            local_do_llm = do_llm and (sid in high_psc_studies) and (
                args.limit_llm == 0 or llm_used < args.limit_llm)
            res = emit_study(row, study_obs, wiki, high_psc_studies, local_do_llm)
            pages_manifest.append(res)
            if local_do_llm:
                llm_used += 1
        print(f"  studies: emitted {len(studies)}, tier-1 LLM={llm_used}")

    # ----- Entities -----
    if args.only_type in (None, "entity"):
        llm_used = 0
        # build entity → obs index by entity_id column on observations
        if "entity_id" not in obs.columns:
            print("  [warn] observations.parquet missing entity_id; entity obs lookup will be empty")
            obs_by_e = pd.DataFrame()
        else:
            obs_by_e = obs.set_index("entity_id", drop=False)
        for _, row in entities.iterrows():
            eid = row["entity_id"]
            try:
                eobs = obs_by_e.loc[[eid]] if eid in obs_by_e.index else obs.iloc[0:0]
            except KeyError:
                eobs = obs.iloc[0:0]
            local_do_llm = do_llm and (eid in e_top) and (
                args.limit_llm == 0 or llm_used < args.limit_llm)
            res = emit_entity(row, eobs, wiki, e_top, local_do_llm)
            pages_manifest.append(res)
            if local_do_llm:
                llm_used += 1
        print(f"  entities: emitted {len(entities)}, tier-1 LLM={llm_used}")

    # ----- Technologies -----
    if args.only_type in (None, "technology"):
        llm_used = 0
        if "tech_id" not in obs.columns:
            obs_by_t = pd.DataFrame()
        else:
            obs_by_t = obs.set_index("tech_id", drop=False)
        for _, row in techs.iterrows():
            tid = row["tech_id"]
            try:
                tobs = obs_by_t.loc[[tid]] if tid in obs_by_t.index else obs.iloc[0:0]
            except KeyError:
                tobs = obs.iloc[0:0]
            local_do_llm = do_llm and (tid in t_top) and (
                args.limit_llm == 0 or llm_used < args.limit_llm)
            res = emit_technology(row, tobs, wiki, t_top, local_do_llm)
            pages_manifest.append(res)
            if local_do_llm:
                llm_used += 1
        print(f"  technologies: emitted {len(techs)}, tier-1 LLM={llm_used}")

    # ----- pages_manifest.parquet -----
    pm = pd.DataFrame(pages_manifest)
    pm.to_parquet(data / "pages_manifest.parquet", index=False)

    # ----- Append manifest -----
    manifest_path = wiki / "build_manifest.json"
    with open(manifest_path) as f:
        manifest = json.load(f)
    manifest["phase_3"] = {
        "phase": 3,
        "phase_name": "generate_vault",
        "ran_at": datetime.now(timezone.utc).isoformat(),
        "pages_emitted": len(pm),
        "by_type": pm.groupby("type").size().to_dict() if len(pm) else {},
        "tier1_counts_planned": {
            "study": len(high_psc_studies),
            "entity": len(e_top),
            "technology": len(t_top),
        },
        "skip_llm": args.skip_llm,
        "limit_llm": args.limit_llm,
    }
    tmp = manifest_path.with_suffix(".json.tmp")
    with open(tmp, "w") as f:
        json.dump(manifest, f, indent=2, sort_keys=True, default=str)
    os.replace(tmp, manifest_path)

    print(f"\nPhase 3 complete. Pages: {len(pm)}. Manifest: {manifest_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
