#!/usr/bin/env python3
"""
04_generate_indices_v2.py — Phase 4: Home, decades, collections, prescient (v1.5)

v2 corrections vs v1:
  - Reads collection_stats_agg.parquet (per-collection) not collection_stats
    (per-study) — fixes duplicate-collection-page bug
  - Uses pub_year (int) directly — no string coercion gymnastics
  - Emits a codes/ index page (NEW v1.5)
  - Adds bases for entities, technologies, codes alongside studies/prescience
  - Adds a holistic-prescience (study_prescience_enum='high') section to
    _prescient.md
"""
from __future__ import annotations
import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    sys.exit("ERROR: pandas required.")


VAULT_HOME = """\
---
title: "Kastner Aberdeen Wiki"
slug: "_index"
page_type: index
tier: 1
---

# Kastner Aberdeen Wiki

Built {built_at}. {studies} studies, {entities} entities, {technologies} \
technologies, {observations} observations ({prescience_obs} obs scored for \
prescience), {decades_count} decades, {collections_count} collections, \
{codes} codes.

## Top-level navigation

- [[_prescient]] — high-prescience studies (Pass C + holistic)
- [[_decades]] — by decade
- [[_collections]] — by collection
- [[_codes]] — methodology + technology-category dictionary

## Bases (Obsidian native views)

- [[bases/studies|All studies]]
- [[bases/entities|All entities]]
- [[bases/technologies|All technologies]]
- [[bases/prescience|Prescient studies (P_max ≥ 4)]]
- [[bases/codes|All codes]]
"""

PRESCIENT_INDEX = """\
---
title: "Prescient studies"
slug: "_prescient"
page_type: index
tier: 1
---

# Prescient studies

## Obs-level (Pass C, model={model})

Top 50 studies by `prescience_max` (≥4) then `prescience_mean`.

| Study | P_max | P_mean | Year |
|---|---:|---:|---:|
{rows_obs}

## Study-level (holistic enum = `high`)

Original-ingest holistic rating; complementary to the obs-level scores above.

| Study | Year | Type |
|---|---:|---|
{rows_holistic}
"""


def write_page(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(body)
    os.replace(tmp, path)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki", required=True)
    args = ap.parse_args()
    wiki = Path(args.wiki).resolve()
    data = wiki / "data"
    vault = wiki / "wiki"

    studies = pd.read_parquet(data / "studies.parquet")
    entities = pd.read_parquet(data / "entities.parquet")
    techs = pd.read_parquet(data / "technologies.parquet")
    obs = pd.read_parquet(data / "observations.parquet")
    coll_agg = pd.read_parquet(data / "collection_stats_agg.parquet")
    codes = pd.read_parquet(data / "codes.parquet")

    # Numeric coercions
    studies["pub_year"] = pd.to_numeric(studies["pub_year"], errors="coerce")
    if "prescience_max" in studies.columns:
        studies["prescience_max"] = pd.to_numeric(studies["prescience_max"], errors="coerce")
    if "prescience_mean" in studies.columns:
        studies["prescience_mean"] = pd.to_numeric(studies["prescience_mean"], errors="coerce")

    prescience_obs = int(obs["prescience_score"].notna().sum()) if "prescience_score" in obs.columns else 0
    decades_df = (studies.dropna(subset=["pub_year"])
                          .assign(dec=lambda d: (d["pub_year"] // 10 * 10).astype(int)))
    decades_count = decades_df["dec"].nunique()

    # ----- Home -----
    home = VAULT_HOME.format(
        built_at=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        decades_count=int(decades_count),
        collections_count=len(coll_agg),
        studies=len(studies),
        entities=len(entities),
        technologies=len(techs),
        observations=len(obs),
        prescience_obs=prescience_obs,
        codes=len(codes),
    )
    write_page(vault / "_index.md", home)

    # ----- Decades -----
    written = 0
    for dec, sub in decades_df.groupby("dec"):
        decade_lbl = f"{int(dec)}s"
        path = vault / "decades" / f"{decade_lbl}.md"
        sub_sorted = sub.sort_values(["prescience_max", "prescience_mean"],
                                     ascending=[False, False])
        body = [
            f'---\ntitle: "{decade_lbl}"\nslug: "{decade_lbl}"\npage_type: decade\ntier: 1\n---\n\n',
            f"# {decade_lbl}\n\n",
            f"{len(sub)} studies. {int(sub['prescience_max'].notna().sum())} have prescience scores.\n\n",
            "## High-prescience studies in this decade\n\n",
            "```dataview\n",
            "TABLE prescience_max, prescience_mean, prescience_obs_count\n",
            'FROM "studies"\n',
            f'WHERE pub_year >= {int(dec)} AND pub_year < {int(dec)+10}\n  AND prescience_max >= 3\n',
            "SORT prescience_max DESC\n",
            "LIMIT 25\n",
            "```\n\n",
            "## All studies\n",
        ]
        for _, r in sub_sorted.head(50).iterrows():
            pmax = r.get("prescience_max")
            tag = f" **[P_max={int(pmax)}]**" if pd.notna(pmax) else ""
            sid = r["study_id"]
            title = r.get("title") or sid
            body.append(f"- [[study-{sid}|{title}]]{tag}")
        write_page(path, "\n".join(body))
        written += 1
    print(f"  decades: {written} pages")

    # ----- Collections (per-collection from agg) -----
    for _, r in coll_agg.iterrows():
        coll_name = r["collection"]
        slug_coll = coll_name.replace(" ", "-")
        path = vault / "collections" / f"{slug_coll}.md"
        body = [
            f'---\ntitle: "{coll_name}"\nslug: "collection-{slug_coll}"\npage_type: collection\ntier: 1\nstudy_count: {int(r["study_count"])}\n---\n\n',
            f"# {coll_name}\n\n",
            f"**{int(r['study_count'])}** studies, "
            f"~{int(r['n_entities_sum'])} entity refs, "
            f"~{int(r['n_technologies_sum'])} tech refs, "
            f"~{int(r['n_observations_sum'])} observations.\n\n",
            "```dataview\n",
            "TABLE prescience_max, prescience_mean, pub_year, author\n",
            'FROM "studies"\n',
            f'WHERE contains(string(file.frontmatter.tags), "collection/{coll_name}")\n',
            "SORT prescience_max DESC, pub_year DESC\n",
            "```\n",
        ]
        write_page(path, "\n".join(body))
    print(f"  collections: {len(coll_agg)} pages")

    # ----- Codes index + a per-type Dataview slice -----
    codes_by_type = codes.groupby("code_type").size().sort_values(ascending=False)
    body = ['---\ntitle: "Codes"\nslug: "_codes"\npage_type: index\ntier: 1\n---\n\n',
            "# Codes\n\n",
            f"{len(codes)} codes across {len(codes_by_type)} types.\n\n"]
    for ct, n in codes_by_type.items():
        body.append(f"## {ct} ({n})\n")
        for _, cr in codes[codes["code_type"] == ct].sort_values("code_id").head(80).iterrows():
            body.append(f"- [[code-{cr['code_id']}|{cr.get('label', cr['code_id'])}]] — {cr.get('definition', '')[:120]}")
        body.append("")
    write_page(vault / "_codes.md", "\n".join(body))
    print(f"  codes index emitted ({len(codes)} codes)")

    # ----- Prescient index (combined) -----
    top_obs = (studies[studies["prescience_max"].fillna(0) >= 4]
               .sort_values(["prescience_max", "prescience_mean"],
                            ascending=[False, False])
               .head(50))
    rows_obs = []
    for _, r in top_obs.iterrows():
        rows_obs.append(
            f"| [[study-{r['study_id']}|{r.get('title') or r['study_id']}]] "
            f"| {int(r['prescience_max']) if pd.notna(r['prescience_max']) else ''} "
            f"| {round(r['prescience_mean'], 2) if pd.notna(r['prescience_mean']) else ''} "
            f"| {int(r['pub_year']) if pd.notna(r['pub_year']) else ''} |"
        )
    holistic = (studies[studies.get("study_prescience_enum", pd.Series([])).eq("high")]
                .sort_values("pub_year", na_position="last")
                .head(50)) if "study_prescience_enum" in studies.columns else studies.iloc[0:0]
    rows_holistic = []
    for _, r in holistic.iterrows():
        rows_holistic.append(
            f"| [[study-{r['study_id']}|{r.get('title') or r['study_id']}]] "
            f"| {int(r['pub_year']) if pd.notna(r['pub_year']) else ''} "
            f"| {r.get('type', '')} |"
        )
    write_page(vault / "_prescient.md",
               PRESCIENT_INDEX.format(
                   model="qwen3.5:27b-mlx",
                   rows_obs="\n".join(rows_obs) or "| (none) | | | |",
                   rows_holistic="\n".join(rows_holistic) or "| (none) | | |"))

    # ----- Decade + Collection navigation pages -----
    write_page(vault / "_decades.md",
               '---\ntitle: Decades\nslug: "_decades"\npage_type: index\n---\n\n# Decades\n\n' +
               "\n".join(f"- [[{int(d)}s]]" for d in sorted(decades_df["dec"].unique())))
    write_page(vault / "_collections.md",
               '---\ntitle: Collections\nslug: "_collections"\npage_type: index\n---\n\n# Collections\n\n' +
               "\n".join(f"- [[collection-{c.replace(' ', '-')}|{c}]]"
                        for c in coll_agg["collection"].tolist()))

    # ----- Bases -----
    bases_dir = vault / "bases"
    bases_dir.mkdir(parents=True, exist_ok=True)
    bases = {
        "prescience.base": """\
filters:
  - prescience_max >= 4
columns:
  - title
  - pub_year
  - prescience_max
  - prescience_mean
  - prescience_obs_count
  - study_prescience_enum
sort:
  - field: prescience_max
    direction: desc
  - field: prescience_mean
    direction: desc
""",
        "studies.base": """\
filters:
  - page_type = "study"
columns:
  - title
  - author
  - pub_year
  - type
  - importance
  - relevance
  - study_prescience_enum
  - prescience_max
sort:
  - field: pub_year
    direction: desc
""",
        "entities.base": """\
filters:
  - page_type = "entity"
columns:
  - title
  - entity_type
  - sector
  - status
  - years_active
  - occurrence_count
sort:
  - field: occurrence_count
    direction: desc
""",
        "technologies.base": """\
filters:
  - page_type = "technology"
columns:
  - title
  - category
  - vendor
  - era
  - lifecycle_at_study
  - lifecycle_current
  - occurrence_count
sort:
  - field: occurrence_count
    direction: desc
""",
        "codes.base": """\
filters:
  - page_type = "code"
columns:
  - title
  - code_type
sort:
  - field: code_type
    direction: asc
  - field: title
    direction: asc
""",
    }
    for name, content in bases.items():
        write_page(bases_dir / name, content)
    print(f"  bases: {len(bases)} files")

    # ----- Manifest -----
    manifest_path = wiki / "build_manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    manifest["phase_4"] = {
        "phase": 4,
        "phase_name": "generate_indices",
        "version": "v2",
        "ran_at": datetime.now(timezone.utc).isoformat(),
        "pages": {
            "decades": int(decades_df["dec"].nunique()),
            "collections": len(coll_agg),
            "codes_index": 1,
            "prescient_index": 1,
            "home": 1,
            "bases": len(bases),
        },
    }
    tmp = manifest_path.with_suffix(".json.tmp")
    with open(tmp, "w") as f:
        json.dump(manifest, f, indent=2, sort_keys=True, default=str)
    os.replace(tmp, manifest_path)
    print("✓ Phase 4 complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
