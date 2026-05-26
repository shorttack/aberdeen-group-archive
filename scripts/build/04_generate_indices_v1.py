#!/usr/bin/env python3
"""
04_generate_indices_v1.py — Phase 4: indices, decade/theme/collection pages,
Dataview queries, and Obsidian .base files (v1.5).

v1.5 delta: every index page surfaces prescience. New /prescient/ subdir lists
the top-N most prescient studies. New bases/prescience.base file.

Usage:
  python3 04_generate_indices_v1.py --wiki ~/Desktop/kastner_wiki
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


VAULT_HOME = """---
title: "Kastner Aberdeen Wiki — Home"
page_type: index
tier: 1
---

# Kastner Aberdeen Wiki

Local-first research environment built from the Aberdeen Group archive.
Built {built_at}. Builder v1.5 with LLM prescience scores.

## Browse
- [[_decades]] — by decade ({decades_count})
- [[_collections]] — by collection type ({collections_count})
- [[_prescient]] — most prescient studies (>= 4)
- [[_themes]] — thematic rollups
- Volume 1 memoir chapters: see `volume-1/`

## Counts
- Studies: {studies}
- Entities: {entities}
- Technologies: {technologies}
- Observations: {observations}
- Prescience-scored observations: {prescience_obs}

## Dataview: top 10 most prescient studies

```dataview
TABLE prescience_max, prescience_mean, prescience_obs_count, pub_year
FROM "studies"
WHERE prescience_max >= 4
SORT prescience_max DESC, prescience_mean DESC
LIMIT 10
```

## Dataview: highest occurrence entities

```dataview
TABLE occurrence_count
FROM "entities"
SORT occurrence_count DESC
LIMIT 20
```
"""


PRESCIENT_INDEX = """---
title: "Most Prescient Studies"
slug: "_prescient"
page_type: index
tier: 1
---

# Most Prescient Studies

Studies whose observations scored a 4 or 5 from `{model}` during Pass C
(2026-05-26 production run). Rank by max prescience, then mean.

```dataview
TABLE prescience_max AS "max", prescience_mean AS "mean",
      prescience_obs_count AS "scored obs", pub_year AS "year"
FROM "studies"
WHERE prescience_max >= 4
SORT prescience_max DESC, prescience_mean DESC, pub_year ASC
```

## Top 50 by Mean Prescience (>= 4)

| Study | Max | Mean | Year |
|---|---:|---:|---:|
{rows}
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
    coll = pd.read_parquet(data / "collection_stats.parquet")

    # Stats for home
    prescience_obs = int(obs["prescience_score"].notna().sum()) if "prescience_score" in obs.columns else 0
    decades = (studies.assign(
        dec=pd.to_numeric(studies["pub_year"], errors="coerce") // 10 * 10
    ).dropna(subset=["dec"]))
    decades_count = decades["dec"].nunique()

    home = VAULT_HOME.format(
        built_at=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        decades_count=int(decades_count),
        collections_count=len(coll),
        studies=len(studies),
        entities=len(entities),
        technologies=len(techs),
        observations=len(obs),
        prescience_obs=prescience_obs,
    )
    write_page(vault / "_index.md", home)

    # Decades
    written = 0
    for dec, sub in decades.groupby("dec"):
        decade_lbl = f"{int(dec)}s"
        path = vault / "decades" / f"{decade_lbl}.md"
        sub_sorted = sub.sort_values(["prescience_max", "prescience_mean"],
                                     ascending=[False, False])
        body = [
            f"---\ntitle: \"{decade_lbl}\"\nslug: \"{decade_lbl}\"\npage_type: decade\ntier: 1\n---\n\n",
            f"# {decade_lbl}\n\n",
            f"{len(sub)} studies. {int(sub['prescience_max'].notna().sum())} have prescience scores.\n\n",
            "## High-prescience studies in this decade\n\n",
            "```dataview\n",
            f"TABLE prescience_max, prescience_mean, prescience_obs_count\n",
            f"FROM \"studies\"\n",
            f"WHERE startswith(string(pub_year), \"{int(dec)}\")\n  AND prescience_max >= 3\n",
            f"SORT prescience_max DESC\n",
            f"LIMIT 25\n",
            "```\n\n",
            "## All studies\n",
        ]
        for _, r in sub_sorted.head(50).iterrows():
            pmax = r.get("prescience_max")
            tag = f" **[P_max={int(pmax)}]**" if pd.notna(pmax) else ""
            body.append(f"- [[study-{r['study_id']}|{r.get('title', r['study_id'])}]]{tag}")
        write_page(path, "\n".join(body))
        written += 1
    print(f"  decades: {written} pages")

    # Collections
    for _, r in coll.iterrows():
        coll_name = r["collection"]
        path = vault / "collections" / f"{coll_name}.md"
        sub = studies[studies["type"] == coll_name]
        body = [
            f"---\ntitle: \"{coll_name}\"\nslug: \"collection-{coll_name}\"\npage_type: collection\ntier: 1\n---\n\n",
            f"# {coll_name}\n\n",
            f"{len(sub)} studies in this collection. Source CSV: `_collection_stats.csv`.\n\n",
            "```dataview\n",
            f"TABLE prescience_max, prescience_mean, pub_year\n",
            f"FROM \"studies\"\n",
            f"WHERE type = \"{coll_name}\"\n",
            f"SORT prescience_max DESC, pub_year DESC\n",
            "```\n",
        ]
        write_page(path, "\n".join(body))
    print(f"  collections: {len(coll)} pages")

    # Prescient index
    top = (studies[studies["prescience_max"].fillna(0) >= 4]
           .sort_values(["prescience_max", "prescience_mean"],
                        ascending=[False, False])
           .head(50))
    rows = []
    for _, r in top.iterrows():
        rows.append(
            f"| [[study-{r['study_id']}|{r.get('title', r['study_id'])}]] "
            f"| {int(r['prescience_max']) if pd.notna(r['prescience_max']) else ''} "
            f"| {round(r['prescience_mean'], 2) if pd.notna(r['prescience_mean']) else ''} "
            f"| {r.get('pub_year', '')} |"
        )
    write_page(vault / "_prescient.md",
               PRESCIENT_INDEX.format(model="qwen3.5:27b-mlx", rows="\n".join(rows)))

    # Decades + collections index pages
    write_page(vault / "_decades.md",
               "---\ntitle: Decades\npage_type: index\n---\n\n# Decades\n\n" +
               "\n".join(f"- [[{int(d)}s]]" for d in sorted(decades["dec"].unique())))
    write_page(vault / "_collections.md",
               "---\ntitle: Collections\npage_type: index\n---\n\n# Collections\n\n" +
               "\n".join(f"- [[collection-{c}]]" for c in coll["collection"].tolist()))

    # Bases (Obsidian native data view)
    bases_dir = vault / "bases"
    bases_dir.mkdir(parents=True, exist_ok=True)
    write_page(bases_dir / "prescience.base", """\
filters:
  - prescience_max >= 4
columns:
  - title
  - pub_year
  - prescience_max
  - prescience_mean
  - prescience_obs_count
sort:
  - field: prescience_max
    direction: desc
  - field: prescience_mean
    direction: desc
""")
    write_page(bases_dir / "studies.base", """\
filters:
  - page_type = "study"
columns:
  - title
  - pub_year
  - type
  - prescience_max
sort:
  - field: pub_year
    direction: desc
""")

    # Manifest
    manifest_path = wiki / "build_manifest.json"
    with open(manifest_path) as f:
        manifest = json.load(f)
    manifest["phase_4"] = {
        "phase": 4,
        "phase_name": "generate_indices",
        "ran_at": datetime.now(timezone.utc).isoformat(),
        "pages": {
            "decades": int(decades["dec"].nunique()),
            "collections": len(coll),
            "prescient_index": 1,
            "home": 1,
            "bases": 2,
        },
    }
    tmp = manifest_path.with_suffix(".json.tmp")
    with open(tmp, "w") as f:
        json.dump(manifest, f, indent=2, sort_keys=True, default=str)
    os.replace(tmp, manifest_path)
    print("Phase 4 complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
