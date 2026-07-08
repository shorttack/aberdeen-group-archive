#!/usr/bin/env python3
"""
06_emit_scaffolding_v1.py — Phase 6: README, AGENTS, chat-starter, Makefile,
verify + semantic_search scripts (v1.5).

Usage:
  python3 06_emit_scaffolding_v1.py --wiki ~/Desktop/kastner_wiki
"""
from __future__ import annotations
import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


README = """\
# Kastner Aberdeen Wiki — v1.5

Local-first research environment derived from the [aberdeen-group-archive](https://github.com/shorttack/aberdeen-group-archive)
master CSVs. Built by `kastner-wiki-builder` skill v2.

## What's new in v1.5

- **Prescience scores** from local `qwen3.5:27b-mlx` Pass C run (2026-05-26)
- New 8th master ingested: `_master_prescience_scores.csv`
- New DuckDB views: `v_studies_with_prescience`, `v_top_prescient_studies`,
  `v_prescience_by_decade`, `v_low_confidence_prescience`
- New page subdir: `wiki/_prescient.md` (top 50 most prescient studies)
- Frontmatter on every page: `prescience_max`, `prescience_mean`,
  `prescience_obs_count`

## Quick start

1. Open `wiki/` as an Obsidian vault.
2. Open `wiki/_index.md` and follow links.
3. From terminal: `python3 scripts/semantic_search.py "query"`.
4. From SQL: `duckdb db/kastner.duckdb` then `SELECT * FROM v_top_prescient_studies LIMIT 20`.

## File map

| Path | What |
|---|---|
| `wiki/` | Obsidian vault root — open this in Obsidian |
| `data/*.parquet` | Columnar copies of master CSVs |
| `db/kastner.duckdb` | Pre-built DuckDB with ~18 named views |
| `db/queries/*.sql` | Reusable query examples |
| `scripts/rebuild.py` | Full rebuild (rarely needed) |
| `scripts/verify.py` | Self-test |
| `scripts/semantic_search.py` | Local cosine-sim search |
| `build_manifest.json` | What was built, when, with what counts |
| `AGENTS.md` | LLM primer |
| `chat-starter.md` | Pre-warmed prompts |

## Rebuild

```bash
make rebuild
```

Or step-by-step:

```bash
python3 scripts/build/01_load_csvs_v1.py --archive ~/Desktop/Archive/aberdeen-group-archive --wiki .
python3 scripts/build/02_build_data_layer_v1.py --wiki .
python3 scripts/build/03_generate_vault_v1.py --wiki . [--skip-llm]
python3 scripts/build/04_generate_indices_v1.py --wiki .
python3 scripts/build/05_compute_embeddings_v1.py --wiki .
python3 scripts/build/06_emit_scaffolding_v1.py --wiki .
python3 scripts/verify.py --wiki .
```
"""


AGENTS = """\
# AGENTS.md — Kastner Aberdeen Wiki

LLM primer. Read this before answering questions against the wiki.

## What this repo is

A read-optimized snapshot of the Aberdeen Group archive (1979–2013) maintained
by Pete Kastner. Three persistent layers:

1. **Obsidian vault** at `wiki/` — human-friendly Markdown with wikilinks,
   Dataview queries, and YAML frontmatter.
2. **DuckDB** at `db/kastner.duckdb` — analytical queries against ~18 named views.
3. **Parquet** at `data/*.parquet` — direct columnar access.

## Prescience scoring (v1.5)

Every observation in `_master_observations.csv` may have a prescience score
0-5 assigned by `qwen3.5:27b-mlx` (Pass C, 2026-05-26). Calibration kappa
vs Claude Sonnet: **0.853**. Confidence is 1 (low) to 3 (high).

| Score | Meaning |
|---:|---|
| 0 | Stated trivia / non-claim |
| 1 | Routine observation; uninteresting in hindsight |
| 2 | Reasonable take at the time |
| 3 | Notably right call |
| 4 | Prescient; ahead of consensus |
| 5 | Remarkably prescient; called something major early |

## Query recipes

### Top 20 most prescient studies
```sql
SELECT title, pub_year, prescience_max, prescience_mean
FROM v_top_prescient_studies LIMIT 20;
```

### Prescient observations from a single study
```sql
SELECT obs_id, prescience_score, prescience_rationale, metric_value
FROM v_observations
WHERE study_id = '<id>' AND prescience_score >= 4
ORDER BY prescience_score DESC;
```

### High-prescience studies by decade
```sql
SELECT decade, high_prescience_studies, studies_scored
FROM v_prescience_by_decade;
```

## Naming conventions

- Slugs are lowercase-hyphenated and match CSV `*_id` columns.
- Study slugs are prefixed `study-`. Entities and technologies are not.
- Collection pages live at `wiki/collections/<type>.md`.
"""


CHAT_STARTER = """\
# Chat starter — Kastner Aberdeen Wiki

20 pre-warmed prompts. Triple mode: natural-language + SQL + Dataview.

## 1. What were the 5 most prescient studies?

**SQL**
```sql
SELECT title, pub_year, prescience_max, prescience_mean
FROM v_top_prescient_studies
ORDER BY prescience_mean DESC LIMIT 5;
```

**Dataview**
~~~dataview
TABLE prescience_max, prescience_mean, pub_year
FROM "studies"
WHERE prescience_max >= 4
SORT prescience_mean DESC
LIMIT 5
~~~

## 2. Show prescient observations about Oracle

**SQL**
```sql
SELECT o.obs_id, o.prescience_score, o.metric_value, o.prescience_rationale
FROM v_observations o
WHERE o.entity_id = 'oracle' AND o.prescience_score >= 4
ORDER BY o.prescience_score DESC;
```

## 3. Which decade had the most prescient calls?

```sql
SELECT decade, high_prescience_studies
FROM v_prescience_by_decade
ORDER BY high_prescience_studies DESC;
```

## 4-20

(See `AGENTS.md` for query recipes; remaining prompts grow with usage.)
"""


MAKEFILE = """\
.PHONY: rebuild phase1 phase2 phase3 phase4 phase5 phase6 verify clean

ARCHIVE ?= ~/Desktop/Archive/aberdeen-group-archive

rebuild: phase1 phase2 phase3 phase4 phase5 phase6 verify

phase1:
\tpython3 scripts/build/01_load_csvs_v1.py --archive $(ARCHIVE) --wiki .

phase2:
\tpython3 scripts/build/02_build_data_layer_v1.py --wiki .

phase3:
\tpython3 scripts/build/03_generate_vault_v1.py --wiki .

phase3-fast:
\tpython3 scripts/build/03_generate_vault_v1.py --wiki . --skip-llm

phase4:
\tpython3 scripts/build/04_generate_indices_v1.py --wiki .

phase5:
\tpython3 scripts/build/05_compute_embeddings_v1.py --wiki .

phase6:
\tpython3 scripts/build/06_emit_scaffolding_v1.py --wiki .

verify:
\tpython3 scripts/verify.py --wiki .

clean:
\trm -rf wiki/ data/*.parquet db/ build_manifest.json
"""


VERIFY = '''#!/usr/bin/env python3
"""scripts/verify.py — Self-test for v1.5 wiki build."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

try:
    import duckdb
    import pandas as pd
except ImportError:
    sys.exit("ERROR: install duckdb + pandas")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki", required=True)
    args = ap.parse_args()
    wiki = Path(args.wiki).resolve()
    fails = []
    warns = []

    # 1. Required dirs
    for d in ("wiki", "data", "db"):
        if not (wiki / d).exists():
            fails.append(f"missing dir: {d}")

    # 2. Parquet files load
    parquets = ["studies", "entities", "technologies", "observations",
                "prescience_scores", "known_entities", "known_technologies",
                "collection_stats"]
    for name in parquets:
        p = wiki / "data" / f"{name}.parquet"
        if not p.exists():
            fails.append(f"missing parquet: {name}.parquet")
            continue
        try:
            df = pd.read_parquet(p)
            if len(df) == 0:
                warns.append(f"{name}.parquet has 0 rows")
        except Exception as e:
            fails.append(f"parquet read failed for {name}: {e}")

    # 3. DuckDB opens, views work
    db = wiki / "db" / "kastner.duckdb"
    if db.exists():
        try:
            con = duckdb.connect(str(db))
            for v in ["v_studies_with_prescience", "v_top_prescient_studies",
                      "v_prescience_by_decade", "v_observations_with_prescience"]:
                n = con.execute(f"SELECT COUNT(*) FROM {v}").fetchone()[0]
                if n == 0:
                    warns.append(f"view {v} returned 0 rows")
            con.close()
        except Exception as e:
            fails.append(f"DuckDB failure: {e}")

    # 4. Manifest exists
    mp = wiki / "build_manifest.json"
    if not mp.exists():
        fails.append("missing build_manifest.json")
    else:
        m = json.loads(mp.read_text())
        for ph in ("phase_1", "phase_2", "phase_3", "phase_4"):
            if ph not in m:
                fails.append(f"manifest missing {ph}")

    # 5. _prescient.md page exists
    if not (wiki / "wiki" / "_prescient.md").exists():
        fails.append("missing wiki/_prescient.md")

    print("=" * 60)
    print(f"VERIFY: {len(fails)} fails, {len(warns)} warns")
    print("=" * 60)
    for f in fails:
        print(f"  FAIL  {f}")
    for w in warns:
        print(f"  WARN  {w}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
'''


SEMANTIC_SEARCH = '''#!/usr/bin/env python3
"""scripts/semantic_search.py — Local cosine-sim search over the wiki."""
from __future__ import annotations
import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path

try:
    import pandas as pd
    import numpy as np
except ImportError:
    sys.exit("ERROR: install pandas + numpy")


OLLAMA_BASE = os.environ.get("OLLAMA_BASE", "http://localhost:11434")


def embed_query(text: str, model: str = "nomic-embed-text") -> list[float]:
    payload = json.dumps({"model": model, "prompt": text}).encode("utf-8")
    req = urllib.request.Request(
        f"{OLLAMA_BASE}/api/embeddings", data=payload,
        headers={"Content-Type": "application/json"}, method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))["embedding"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--wiki", default=".")
    args = ap.parse_args()
    wiki = Path(args.wiki).resolve()

    df = pd.read_parquet(wiki / "data" / "embeddings.parquet")
    df = df[df["dim"] > 0]
    M = np.vstack(df["embedding"].to_list())
    q = np.array(embed_query(args.query))
    sims = M @ q / (np.linalg.norm(M, axis=1) * np.linalg.norm(q) + 1e-9)
    df = df.assign(sim=sims).sort_values("sim", ascending=False).head(args.top)
    for _, r in df.iterrows():
        print(f"{r['sim']:.4f}  {r['path']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki", required=True)
    args = ap.parse_args()
    wiki = Path(args.wiki).resolve()

    (wiki / "scripts").mkdir(parents=True, exist_ok=True)
    (wiki / "scripts" / "build").mkdir(parents=True, exist_ok=True)

    files = {
        "README.md": README,
        "AGENTS.md": AGENTS,
        "chat-starter.md": CHAT_STARTER,
        "Makefile": MAKEFILE,
        ".gitignore": "*.tmp\n.obsidian/workspace*\n.DS_Store\n",
        "scripts/verify.py": VERIFY,
        "scripts/semantic_search.py": SEMANTIC_SEARCH,
    }
    for rel, content in files.items():
        p = wiki / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        tmp = p.with_suffix(p.suffix + ".tmp")
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(content)
        os.replace(tmp, p)
        print(f"  [write] {rel}")

    # Make verify + semantic_search executable
    for s in ["scripts/verify.py", "scripts/semantic_search.py"]:
        os.chmod(wiki / s, 0o755)

    # Update manifest
    mp = wiki / "build_manifest.json"
    with open(mp) as f:
        manifest = json.load(f)
    manifest["phase_6"] = {
        "phase": 6,
        "phase_name": "emit_scaffolding",
        "ran_at": datetime.now(timezone.utc).isoformat(),
        "files_written": list(files.keys()),
    }
    manifest["build_completed_at"] = datetime.now(timezone.utc).isoformat()
    tmp = mp.with_suffix(".json.tmp")
    with open(tmp, "w") as f:
        json.dump(manifest, f, indent=2, sort_keys=True, default=str)
    os.replace(tmp, mp)
    print("Phase 6 complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
