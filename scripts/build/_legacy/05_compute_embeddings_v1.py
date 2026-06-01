#!/usr/bin/env python3
"""
05_compute_embeddings_v1.py — Phase 5: nomic-embed page embeddings (v1.5)

Walks every emitted Markdown page, embeds (title + frontmatter + first 500
tokens) via Ollama's nomic-embed-text. v1.5 unchanged from v1 conceptually
but routes through Ollama for local execution.

Usage:
  python3 05_compute_embeddings_v1.py --wiki ~/Desktop/kastner_wiki \\
      [--model nomic-embed-text]

Requires:
  ollama pull nomic-embed-text   (~274 MB)
"""
from __future__ import annotations
import argparse
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    sys.exit("ERROR: pandas required.")


OLLAMA_BASE = os.environ.get("OLLAMA_BASE", "http://localhost:11434")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def embed(text: str, model: str) -> list[float] | None:
    payload = json.dumps({"model": model, "prompt": text}).encode("utf-8")
    req = urllib.request.Request(
        f"{OLLAMA_BASE}/api/embeddings", data=payload,
        headers={"Content-Type": "application/json"}, method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            res = json.loads(resp.read().decode("utf-8"))
        return res.get("embedding")
    except Exception as e:
        print(f"  [warn] embed failed: {e}")
        return None


def collect_pages(vault: Path) -> list[dict]:
    pages = []
    for p in vault.rglob("*.md"):
        text = p.read_text(encoding="utf-8", errors="replace")
        m = FRONTMATTER_RE.match(text)
        if m:
            fm_raw, body = m.group(1), m.group(2)
        else:
            fm_raw, body = "", text
        # Trim to ~500 tokens of body (rough: 2000 chars)
        body_trim = body[:2000]
        embed_input = (fm_raw + "\n" + body_trim).strip()
        pages.append({
            "path": str(p.relative_to(vault.parent)),
            "slug": p.stem,
            "embed_input": embed_input,
        })
    return pages


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki", required=True)
    ap.add_argument("--model", default="nomic-embed-text")
    ap.add_argument("--limit", type=int, default=0,
                    help="Cap pages embedded (0 = all)")
    args = ap.parse_args()

    wiki = Path(args.wiki).resolve()
    vault = wiki / "wiki"
    data = wiki / "data"
    data.mkdir(parents=True, exist_ok=True)

    pages = collect_pages(vault)
    if args.limit:
        pages = pages[:args.limit]
    print(f"Embedding {len(pages)} pages using {args.model}...")

    rows = []
    t0 = time.time()
    for i, p in enumerate(pages, 1):
        vec = embed(p["embed_input"], args.model)
        rows.append({
            "path": p["path"],
            "slug": p["slug"],
            "embedding": vec or [],
            "dim": len(vec) if vec else 0,
        })
        if i % 100 == 0:
            print(f"  [{i}/{len(pages)}] {time.time()-t0:.1f}s elapsed")

    df = pd.DataFrame(rows)
    out = data / "embeddings.parquet"
    df.to_parquet(out, index=False)
    print(f"Wrote {out} — {len(df)} rows")

    # Manifest
    manifest_path = wiki / "build_manifest.json"
    with open(manifest_path) as f:
        manifest = json.load(f)
    manifest["phase_5"] = {
        "phase": 5,
        "phase_name": "embeddings",
        "ran_at": datetime.now(timezone.utc).isoformat(),
        "model": args.model,
        "pages_embedded": len(df),
        "pages_with_vector": int((df["dim"] > 0).sum()),
        "elapsed_sec": round(time.time() - t0, 1),
    }
    tmp = manifest_path.with_suffix(".json.tmp")
    with open(tmp, "w") as f:
        json.dump(manifest, f, indent=2, sort_keys=True, default=str)
    os.replace(tmp, manifest_path)
    print("Phase 5 complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
