#!/usr/bin/env python3
"""
03_generate_vault_v2.py — Phase 3: Generate Obsidian Markdown vault (v1.5)

v2 corrections vs v1:
  - Uses real column names: entity_name (not canonical_name), tech_name,
    pub_year (derived in Phase 1)
  - Drops nonexistent `aliases` column from frontmatter
  - Expands entity frontmatter with entity_type, sector, status,
    years_active, successor, notes
  - Expands tech frontmatter with category, vendor, era,
    lifecycle_at_study, lifecycle_current, notes
  - Adds study-level prescience enum (study_prescience_enum) alongside
    obs-level numeric prescience_max/mean
  - Reads observations.parquet's joined prescience columns (Phase 1 v2 join)
  - Emits codes/ pages (NEW v1.5 surface)

Usage:
  python3 03_generate_vault_v2.py --wiki ~/Desktop/kastner_wiki \\
      [--skip-llm] [--limit-llm N] \\
      [--only-type {study,entity,technology,code}]
"""
from __future__ import annotations
import argparse
import json
import os
import re
import sys
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
    "code":       400,
    "stub":       500,
    "index":      1500,
}

CHAR_PER_TOKEN_RATIO = 3.5


def slugify(s: str) -> str:
    s = (s or "").strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "untitled"


def cap_text(text: str, tok_cap: int) -> str:
    char_cap = int(tok_cap * CHAR_PER_TOKEN_RATIO)
    if len(text) <= char_cap:
        return text
    return text[:char_cap].rsplit(" ", 1)[0] + "\n\n_(truncated to cap)_"


def yaml_value(v):
    """Render a Python value as a YAML scalar/list."""
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return "null"
    if isinstance(v, list):
        if not v:
            return "[]"
        return "[" + ", ".join(f'"{str(x)}"' for x in v) + "]"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v).replace('"', "'")
    return f'"{s}"'


def frontmatter(d: dict) -> str:
    lines = ["---"]
    for k, v in d.items():
        lines.append(f"{k}: {yaml_value(v)}")
    lines.append("---\n")
    return "\n".join(lines)


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, path)


def safe_str(v) -> str:
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return ""
    return str(v)


def safe_int(v, default=0) -> int:
    try:
        if v is None or (isinstance(v, float) and pd.isna(v)):
            return default
        return int(float(v))
    except (ValueError, TypeError):
        return default


# ---------------- emitters ----------------

def emit_entity(row, eobs, wiki: Path, e_top: set, do_llm: bool) -> dict:
    eid = row["entity_id"]
    name = safe_str(row.get("entity_name")) or eid
    slug = slugify(eid)
    page_path = wiki / "wiki" / "entities" / f"{slug}.md"
    occ = safe_int(row.get("occurrence_count"))
    is_tier1 = eid in e_top

    psc_obs = eobs.dropna(subset=["prescience_score"]) if "prescience_score" in eobs.columns else eobs.iloc[0:0]
    pmax = float(psc_obs["prescience_score"].max()) if len(psc_obs) else None
    pmean = float(psc_obs["prescience_score"].mean()) if len(psc_obs) else None

    fm = {
        "title": name,
        "slug": slug,
        "page_type": "entity",
        "tags": [f"type/entity", f"entity-type/{safe_str(row.get('entity_type')) or 'unknown'}"],
        "tier": 1 if is_tier1 else 2,
        "source_csv": "_master_entities.csv",
        "entity_id": eid,
        "entity_type": safe_str(row.get("entity_type")),
        "sector": safe_str(row.get("sector")),
        "status": safe_str(row.get("status")),
        "successor": safe_str(row.get("successor")),
        "years_active": safe_str(row.get("years_active")),
        "occurrence_count": occ,
        "prescience_max": pmax,
        "prescience_mean": round(pmean, 2) if pmean is not None else None,
        "prescience_obs_count": len(psc_obs),
    }

    body = [frontmatter(fm), f"# {name}\n"]
    notes = safe_str(row.get("notes"))
    if notes:
        body.append(f"> {notes}\n")

    # Top obs
    obs_sorted = eobs.sort_values(
        ["prescience_score", "obs_id"], ascending=[False, True], na_position="last"
    ).head(20) if len(eobs) else eobs

    if is_tier1 and do_llm:
        prompt_lines = [f"Entity: {name} ({eid})"]
        for col, lbl in [("entity_type", "Type"), ("sector", "Sector"),
                          ("status", "Status"), ("years_active", "Years")]:
            v = safe_str(row.get(col))
            if v:
                prompt_lines.append(f"{lbl}: {v}")
        prompt_lines.append("")
        prompt_lines.append("Top observations:")
        for _, o in obs_sorted.iterrows():
            ps = o.get("prescience_score")
            mv = safe_str(o.get("metric_value"))[:300]
            prompt_lines.append(f"- {mv}" + (f" (prescience={ps})" if pd.notna(ps) else ""))
        prompt = "\n".join(prompt_lines)
        res = llm.summarize("entity", prompt, system=llm.SYSTEM_PROMPT_ENTITY)
        if res["ok"]:
            body.append("\n## Summary\n")
            body.append(cap_text(res["text"], PAGE_CAPS["entity"]) + "\n")

    body.append("\n## Top observations\n")
    for _, o in obs_sorted.iterrows():
        ps = o.get("prescience_score")
        mv = safe_str(o.get("metric_value"))[:400]
        tag = f" `[ps={ps:.0f}]`" if pd.notna(ps) else ""
        sid = safe_str(o.get("study_id"))
        body.append(f"- {mv}{tag} — [[study-{sid}]]")
    body.append("")

    atomic_write(page_path, "\n".join(body))
    return {"slug": slug, "tier": fm["tier"], "type": "entity"}


def emit_technology(row, tobs, wiki: Path, t_top: set, do_llm: bool) -> dict:
    tid = row["tech_id"]
    name = safe_str(row.get("tech_name")) or tid
    slug = slugify(tid)
    page_path = wiki / "wiki" / "technologies" / f"{slug}.md"
    occ = safe_int(row.get("occurrence_count"))
    is_tier1 = tid in t_top

    psc_obs = tobs.dropna(subset=["prescience_score"]) if "prescience_score" in tobs.columns else tobs.iloc[0:0]
    pmax = float(psc_obs["prescience_score"].max()) if len(psc_obs) else None
    pmean = float(psc_obs["prescience_score"].mean()) if len(psc_obs) else None

    fm = {
        "title": name,
        "slug": slug,
        "page_type": "technology",
        "tags": [f"type/technology", f"category/{safe_str(row.get('category')) or 'unknown'}",
                 f"era/{safe_str(row.get('era')) or 'unknown'}"],
        "tier": 1 if is_tier1 else 2,
        "source_csv": "_master_technologies.csv",
        "tech_id": tid,
        "category": safe_str(row.get("category")),
        "vendor": safe_str(row.get("vendor")),
        "era": safe_str(row.get("era")),
        "lifecycle_at_study": safe_str(row.get("lifecycle_at_study")),
        "lifecycle_current": safe_str(row.get("lifecycle_current")),
        "occurrence_count": occ,
        "prescience_max": pmax,
        "prescience_mean": round(pmean, 2) if pmean is not None else None,
        "prescience_obs_count": len(psc_obs),
    }
    body = [frontmatter(fm), f"# {name}\n"]
    notes = safe_str(row.get("notes"))
    if notes:
        body.append(f"> {notes}\n")

    obs_sorted = tobs.sort_values(
        ["prescience_score", "obs_id"], ascending=[False, True], na_position="last"
    ).head(20) if len(tobs) else tobs

    if is_tier1 and do_llm:
        prompt_lines = [f"Technology: {name} ({tid})"]
        for col, lbl in [("category", "Category"), ("vendor", "Vendor"),
                          ("era", "Era"), ("lifecycle_current", "Lifecycle now")]:
            v = safe_str(row.get(col))
            if v:
                prompt_lines.append(f"{lbl}: {v}")
        prompt_lines.append("")
        prompt_lines.append("Top observations:")
        for _, o in obs_sorted.iterrows():
            ps = o.get("prescience_score")
            mv = safe_str(o.get("metric_value"))[:300]
            prompt_lines.append(f"- {mv}" + (f" (prescience={ps})" if pd.notna(ps) else ""))
        prompt = "\n".join(prompt_lines)
        res = llm.summarize("technology", prompt, system=llm.SYSTEM_PROMPT_TECH)
        if res["ok"]:
            body.append("\n## Summary\n")
            body.append(cap_text(res["text"], PAGE_CAPS["technology"]) + "\n")

    body.append("\n## Top observations\n")
    for _, o in obs_sorted.iterrows():
        ps = o.get("prescience_score")
        mv = safe_str(o.get("metric_value"))[:400]
        tag = f" `[ps={ps:.0f}]`" if pd.notna(ps) else ""
        sid = safe_str(o.get("study_id"))
        body.append(f"- {mv}{tag} — [[study-{sid}]]")
    body.append("")
    atomic_write(page_path, "\n".join(body))
    return {"slug": slug, "tier": fm["tier"], "type": "technology"}


def emit_study(row, study_obs, wiki: Path, tier1: set, do_llm: bool) -> dict:
    sid = row["study_id"]
    title = safe_str(row.get("title")) or sid
    slug = f"study-{slugify(sid)}"
    page_path = wiki / "wiki" / "studies" / f"{slug}.md"
    is_tier1 = sid in tier1

    psc = study_obs.dropna(subset=["prescience_score"]) if "prescience_score" in study_obs.columns else study_obs.iloc[0:0]
    pmax = float(psc["prescience_score"].max()) if len(psc) else None
    pmean = float(psc["prescience_score"].mean()) if len(psc) else None
    py = row.get("pub_year")
    py_int = safe_int(py) if py is not None else None

    fm = {
        "title": title,
        "slug": slug,
        "page_type": "study",
        "tags": ["type/study", f"collection/{safe_str(row.get('type')) or 'unknown'}"],
        "tier": 1 if is_tier1 else 2,
        "source_csv": "_master_studies.csv",
        "study_id": sid,
        "author": safe_str(row.get("author")),
        "date": safe_str(row.get("date")),
        "pub_year": py_int,
        "type": safe_str(row.get("type")),
        "subject_domain": safe_str(row.get("subject_domain")),
        "methodology": safe_str(row.get("methodology")),
        "source_file": safe_str(row.get("source_file")),
        "license": safe_str(row.get("license")),
        "importance": safe_str(row.get("importance")),
        "relevance": safe_str(row.get("relevance")),
        "study_prescience_enum": safe_str(row.get("study_prescience_enum")),
        "prescience_max": pmax,
        "prescience_mean": round(pmean, 2) if pmean is not None else None,
        "prescience_obs_count": len(psc),
    }
    body = [frontmatter(fm), f"# {title}\n"]
    abstract = safe_str(row.get("abstract"))
    if abstract:
        body.append(f"> {abstract}\n")
    if py_int:
        body.append(f"\n_Published {py_int}, author **{safe_str(row.get('author'))}**, "
                    f"type **{safe_str(row.get('type'))}**._\n")

    obs_sorted = study_obs.sort_values(
        ["prescience_score", "obs_id"], ascending=[False, True], na_position="last"
    ).head(25) if len(study_obs) else study_obs

    if is_tier1 and do_llm:
        prompt_lines = [f"Study: {title}", f"Author: {safe_str(row.get('author'))}",
                         f"Year: {py_int}", f"Type: {safe_str(row.get('type'))}",
                         f"Subject: {safe_str(row.get('subject_domain'))}"]
        if abstract:
            prompt_lines.append(f"Abstract: {abstract[:1500]}")
        prompt_lines.append("")
        prompt_lines.append("Top observations:")
        for _, o in obs_sorted.iterrows():
            ps = o.get("prescience_score")
            mv = safe_str(o.get("metric_value"))[:300]
            rat = safe_str(o.get("prescience_rationale"))[:200]
            line = f"- {mv}"
            if pd.notna(ps):
                line += f" (prescience={ps}"
                if rat:
                    line += f"; {rat}"
                line += ")"
            prompt_lines.append(line)
        prompt = "\n".join(prompt_lines)
        res = llm.summarize("study", prompt, system=llm.SYSTEM_PROMPT_STUDY)
        if res["ok"]:
            body.append("\n## Summary\n")
            body.append(cap_text(res["text"], PAGE_CAPS["study"]) + "\n")

    body.append("\n## Top observations\n")
    for _, o in obs_sorted.iterrows():
        ps = o.get("prescience_score")
        mv = safe_str(o.get("metric_value"))[:400]
        tag = f" `[ps={ps:.0f}]`" if pd.notna(ps) else ""
        body.append(f"- {mv}{tag}")
    body.append("")
    atomic_write(page_path, "\n".join(body))
    return {"slug": slug, "tier": fm["tier"], "type": "study"}


def emit_code(row, wiki: Path) -> dict:
    cid = row["code_id"]
    ctype = safe_str(row.get("code_type"))
    label = safe_str(row.get("label")) or cid
    defn = safe_str(row.get("definition"))
    slug = slugify(f"code-{cid}")
    page_path = wiki / "wiki" / "codes" / f"{slug}.md"

    fm = {
        "title": label,
        "slug": slug,
        "page_type": "code",
        "tags": ["type/code", f"code-type/{ctype or 'unknown'}"],
        "tier": 2,
        "source_csv": "_master_codes.csv",
        "code_id": cid,
        "code_type": ctype,
    }
    body = [frontmatter(fm), f"# {label}\n",
            f"_Type: **{ctype}** • ID: `{cid}`_\n"]
    if defn:
        body.append(f"\n{defn}\n")
    atomic_write(page_path, "\n".join(body))
    return {"slug": slug, "tier": 2, "type": "code"}


# ---------------- main ----------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki", required=True)
    ap.add_argument("--skip-llm", action="store_true",
                    help="Template-only; no LLM calls")
    ap.add_argument("--limit-llm", type=int, default=0,
                    help="Cap LLM calls per page-type (0 = no cap)")
    ap.add_argument("--only-type",
                    choices=["study", "entity", "technology", "code"],
                    help="Process only one page type (debug)")
    args = ap.parse_args()

    wiki = Path(args.wiki).resolve()
    data = wiki / "data"

    studies = pd.read_parquet(data / "studies.parquet")
    entities = pd.read_parquet(data / "entities.parquet")
    techs = pd.read_parquet(data / "technologies.parquet")
    obs = pd.read_parquet(data / "observations.parquet")
    codes = pd.read_parquet(data / "codes.parquet")

    # Coerce occurrence_count + prescience_max to numeric for sorting/filtering
    for col in ["occurrence_count"]:
        if col in entities.columns:
            entities[col] = pd.to_numeric(entities[col], errors="coerce").fillna(0).astype(int)
        if col in techs.columns:
            techs[col] = pd.to_numeric(techs[col], errors="coerce").fillna(0).astype(int)
    if "prescience_max" in studies.columns:
        studies["prescience_max"] = pd.to_numeric(studies["prescience_max"], errors="coerce")

    # ----- Tier-1 sets -----
    high_psc_studies = set(
        studies.loc[studies["prescience_max"].fillna(0) >= 4, "study_id"]
    )
    e_top = set(entities.sort_values("occurrence_count", ascending=False)
                       .head(200)["entity_id"])
    t_top = set(techs.sort_values("occurrence_count", ascending=False)
                     .head(150)["tech_id"])
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
        obs_by_e = obs.set_index("entity_id", drop=False) if "entity_id" in obs.columns else None
        for _, row in entities.iterrows():
            eid = row["entity_id"]
            if obs_by_e is not None and eid in obs_by_e.index:
                eobs = obs_by_e.loc[[eid]]
            else:
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
        obs_by_t = obs.set_index("tech_id", drop=False) if "tech_id" in obs.columns else None
        for _, row in techs.iterrows():
            tid = row["tech_id"]
            if obs_by_t is not None and tid in obs_by_t.index:
                tobs = obs_by_t.loc[[tid]]
            else:
                tobs = obs.iloc[0:0]
            local_do_llm = do_llm and (tid in t_top) and (
                args.limit_llm == 0 or llm_used < args.limit_llm)
            res = emit_technology(row, tobs, wiki, t_top, local_do_llm)
            pages_manifest.append(res)
            if local_do_llm:
                llm_used += 1
        print(f"  technologies: emitted {len(techs)}, tier-1 LLM={llm_used}")

    # ----- Codes (NEW v1.5) -----
    if args.only_type in (None, "code"):
        for _, row in codes.iterrows():
            res = emit_code(row, wiki)
            pages_manifest.append(res)
        print(f"  codes: emitted {len(codes)}")

    # ----- pages_manifest.parquet -----
    pm = pd.DataFrame(pages_manifest)
    pm.to_parquet(data / "pages_manifest.parquet", index=False)

    # ----- Append manifest -----
    manifest_path = wiki / "build_manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    manifest["phase_3"] = {
        "phase": 3,
        "phase_name": "generate_vault",
        "version": "v2",
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
    print(f"\n✓ Phase 3 complete. Pages: {len(pm)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
