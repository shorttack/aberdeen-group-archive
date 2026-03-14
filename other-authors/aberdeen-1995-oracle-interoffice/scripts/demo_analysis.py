#!/usr/bin/env python3
"""
demo_analysis.py — Demonstration analysis for the aberdeen-1995-oracle-interoffice data package.

Loads all CSVs from the data/ directory and produces summary statistics,
technology lifecycle breakdown, entity status summary, and observation type
distribution — illustrating how to work with this Frictionless Data Package.

Usage:
    python scripts/demo_analysis.py

Requirements:
    Python 3.8+, no external dependencies (uses only stdlib csv and collections).
"""

import csv
import os
from collections import Counter, defaultdict
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# ── Helpers ────────────────────────────────────────────────────────────────────

def load_csv(filename: str) -> list[dict]:
    path = DATA_DIR / filename
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def section(title: str) -> None:
    print("\n" + "=" * 72)
    print(f"  {title}")
    print("=" * 72)


def table(headers: list[str], rows: list[tuple], col_widths: list[int] = None) -> None:
    if col_widths is None:
        col_widths = [max(len(str(r[i])) for r in [headers] + list(rows)) + 2
                      for i in range(len(headers))]
    fmt = "  ".join(f"{{:<{w}}}" for w in col_widths)
    print(fmt.format(*headers))
    print("  ".join("-" * w for w in col_widths))
    for row in rows:
        print(fmt.format(*[str(v) for v in row]))


# ── Load data ──────────────────────────────────────────────────────────────────

studies       = load_csv("studies.csv")
entities      = load_csv("entities.csv")
technologies  = load_csv("technologies.csv")
observations  = load_csv("observations.csv")
codes         = load_csv("codes.csv")

study = studies[0]

# ══════════════════════════════════════════════════════════════════════════════
# 1. Study summary
# ══════════════════════════════════════════════════════════════════════════════
section("1. STUDY METADATA")
print(f"  ID           : {study['study_id']}")
print(f"  Title        : {study['title']}")
print(f"  Author       : {study['author']}")
print(f"  Date         : {study['date']}")
print(f"  Type         : {study['type']}")
print(f"  Domain       : {study['domain']}")
print(f"  Methodology  : {study['methodology']}")
print(f"  Pages        : {study['page_count']}")
print(f"  Contact      : {study['contact_email']}")
print(f"  Source URL   : {study['source_url']}")

# ══════════════════════════════════════════════════════════════════════════════
# 2. Entities summary
# ══════════════════════════════════════════════════════════════════════════════
section("2. ENTITIES — STATUS SUMMARY")

print(f"\n  Total entities: {len(entities)}\n")

table(
    ["Entity", "Role", "Status@Study", "Status@2026"],
    [(e["name"], e["role"], e["status_at_study"], e["current_status"]) for e in entities],
    col_widths=[36, 28, 14, 10],
)

status_2026 = Counter(e["current_status"] for e in entities)
print(f"\n  2026 status breakdown:")
for status, count in sorted(status_2026.items()):
    print(f"    {status:<12} : {count} entit{'y' if count == 1 else 'ies'}")

# ══════════════════════════════════════════════════════════════════════════════
# 3. Technology lifecycle breakdown
# ══════════════════════════════════════════════════════════════════════════════
section("3. TECHNOLOGIES — LIFECYCLE BREAKDOWN")

print(f"\n  Total technologies: {len(technologies)}\n")

lifecycle_groups = defaultdict(list)
for t in technologies:
    lifecycle_groups[t["lifecycle_status"]].append(t["name"])

lifecycle_order = ["active", "active-niche", "evolved", "superseded", "obsolete"]
for status in lifecycle_order:
    names = lifecycle_groups.get(status, [])
    if names:
        print(f"  [{status.upper()}]  ({len(names)} items)")
        for name in sorted(names):
            print(f"    • {name}")
        print()

# Category breakdown
categories = Counter(t["category"] for t in technologies)
print("  Category distribution:")
table(
    ["Category", "Count"],
    sorted(categories.items(), key=lambda x: -x[1]),
    col_widths=[36, 6],
)

# ══════════════════════════════════════════════════════════════════════════════
# 4. Observations summary
# ══════════════════════════════════════════════════════════════════════════════
section("4. OBSERVATIONS — TYPE DISTRIBUTION")

print(f"\n  Total observations: {len(observations)}\n")

obs_types = Counter(o["observation_type"] for o in observations)
table(
    ["Observation Type", "Count", "Pct"],
    [(ot, cnt, f"{cnt/len(observations)*100:.1f}%")
     for ot, cnt in sorted(obs_types.items(), key=lambda x: -x[1])],
    col_widths=[26, 6, 6],
)

# Subject frequency
subjects = Counter(o["subject"] for o in observations)
print("\n  Top subjects by observation count:")
table(
    ["Subject", "Obs Count"],
    subjects.most_common(10),
    col_widths=[44, 10],
)

# ══════════════════════════════════════════════════════════════════════════════
# 5. Numeric observations
# ══════════════════════════════════════════════════════════════════════════════
section("5. NUMERIC OBSERVATIONS")

numeric_obs = [o for o in observations if o.get("value_numeric")]
if numeric_obs:
    table(
        ["Obs ID", "Subject", "Dimension", "Value", "Unit"],
        [(o["obs_id"], o["subject"][:28], o["dimension"][:28],
          o["value_numeric"], o["unit"]) for o in numeric_obs],
        col_widths=[8, 30, 30, 15, 12],
    )
else:
    print("  No numeric observations found.")

# ══════════════════════════════════════════════════════════════════════════════
# 6. Technology roadmap items (planned features)
# ══════════════════════════════════════════════════════════════════════════════
section("6. PRODUCT ROADMAP OBSERVATIONS (from study text)")

roadmap_keywords = ["roadmap", "planned", "intend", "eventual", "will", "tomorrow"]
roadmap_obs = [
    o for o in observations
    if any(kw in o["value_text"].lower() for kw in roadmap_keywords)
    and o["observation_type"] in ("product-feature", "analyst-assessment")
]
for o in roadmap_obs:
    print(f"\n  [{o['obs_id']}] {o['subject']} / {o['dimension']}")
    # Word-wrap at ~70 chars
    text = o["value_text"]
    words = text.split()
    line = "    "
    for word in words:
        if len(line) + len(word) + 1 > 74:
            print(line)
            line = "    " + word + " "
        else:
            line += word + " "
    if line.strip():
        print(line)

# ══════════════════════════════════════════════════════════════════════════════
# 7. Electronic Economic Community mentions
# ══════════════════════════════════════════════════════════════════════════════
section("7. ELECTRONIC ECONOMIC COMMUNITY — KEY OBSERVATIONS")

eec_obs = [
    o for o in observations
    if "electronic economic community" in o["value_text"].lower()
    or o["subject"].lower() == "electronic economic community"
]
for o in eec_obs:
    print(f"\n  [{o['obs_id']}] {o['observation_type']} | section: {o['source_section']}")
    text = o["value_text"]
    words = text.split()
    line = "    "
    for word in words:
        if len(line) + len(word) + 1 > 74:
            print(line)
            line = "    " + word + " "
        else:
            line += word + " "
    if line.strip():
        print(line)

# ══════════════════════════════════════════════════════════════════════════════
# 8. Controlled vocabulary summary
# ══════════════════════════════════════════════════════════════════════════════
section("8. CONTROLLED VOCABULARY — SCHEME SUMMARY")

scheme_counts = Counter(c["scheme"] for c in codes)
table(
    ["Scheme", "Codes"],
    sorted(scheme_counts.items(), key=lambda x: -x[1]),
    col_widths=[28, 6],
)

print(f"\n  Total codes: {len(codes)}")

# ══════════════════════════════════════════════════════════════════════════════
# Done
# ══════════════════════════════════════════════════════════════════════════════
section("ANALYSIS COMPLETE")
print(f"""
  Package : aberdeen-1995-oracle-interoffice
  Studies : {len(studies)}
  Entities: {len(entities)}
  Techs   : {len(technologies)}
  Obs     : {len(observations)}
  Codes   : {len(codes)}
""")
