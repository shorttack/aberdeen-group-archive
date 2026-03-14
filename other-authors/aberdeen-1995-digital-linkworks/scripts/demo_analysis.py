#!/usr/bin/env python3
"""
demo_analysis.py
================
Demonstration analysis script for the Frictionless Data Package:
  aberdeen-1995-digital-linkworks

Study:  Digital LinkWorks: Delivering Solutions to MIS and End-Users
Author: Aberdeen Group, July 1995

Runs from the package root directory:
    python scripts/demo_analysis.py

No external dependencies beyond the Python standard library.
"""

import csv
import os
import sys
from collections import Counter
from pathlib import Path

# ── Helpers ───────────────────────────────────────────────────────────────────

PACKAGE_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PACKAGE_ROOT / "data"


def read_csv(filename: str) -> list[dict]:
    """Read a CSV from data/ and return a list of dicts."""
    path = DATA_DIR / filename
    if not path.exists():
        print(f"  [ERROR] File not found: {path}", file=sys.stderr)
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def divider(title: str, width: int = 70) -> None:
    print()
    print("=" * width)
    print(f"  {title}")
    print("=" * width)


def section(title: str) -> None:
    print()
    print(f"── {title} " + "─" * max(0, 65 - len(title)))


# ── Load data ─────────────────────────────────────────────────────────────────

studies      = read_csv("studies.csv")
entities     = read_csv("entities.csv")
technologies = read_csv("technologies.csv")
observations = read_csv("observations.csv")
codes        = read_csv("codes.csv")


# ── Analysis ──────────────────────────────────────────────────────────────────

def study_summary():
    divider("STUDY SUMMARY")
    if not studies:
        print("  No study records found.")
        return
    s = studies[0]
    print(f"  Study ID  : {s['study_id']}")
    print(f"  Title     : {s['title']}")
    print(f"  Author    : {s['author']}")
    print(f"  Date      : {s['date']}")
    print(f"  Type      : {s['type']}")
    print(f"  Domain    : {s['domain']}")
    print(f"  Methods   : {s['methodology']}")
    print(f"  Pages     : {s['page_count']}")
    print()
    print(f"  Abstract:")
    # Word-wrap at ~70 chars
    words = s["abstract"].split()
    line = "    "
    for word in words:
        if len(line) + len(word) + 1 > 74:
            print(line)
            line = "    " + word + " "
        else:
            line += word + " "
    if line.strip():
        print(line)


def entity_analysis():
    divider("ENTITY ANALYSIS")

    section(f"All entities ({len(entities)} total)")
    header = f"  {'entity_id':<10} {'name':<42} {'role':<28} {'current_status'}"
    print(header)
    print("  " + "-" * (len(header) - 2))
    for e in entities:
        print(f"  {e['entity_id']:<10} {e['name'][:40]:<42} {e['role'][:26]:<28} {e['current_status']}")

    section("Current status breakdown")
    status_counts = Counter(e["current_status"] for e in entities)
    for status, count in sorted(status_counts.items(), key=lambda x: -x[1]):
        bar = "█" * count
        print(f"  {status:<15} {bar} ({count})")

    section("Entities acquired after the study")
    acquired = [e for e in entities if e["current_status"] == "acquired"]
    for e in acquired:
        print(f"  • {e['name']}")
        note = e["status_note"]
        words = note.split()
        line = "      "
        for word in words:
            if len(line) + len(word) + 1 > 74:
                print(line)
                line = "      " + word + " "
            else:
                line += word + " "
        if line.strip():
            print(line)

    section("Active entities as of 2026")
    active = [e for e in entities if e["current_status"] == "active"]
    for e in active:
        print(f"  • {e['name']} ({e['role']})")


def technology_analysis():
    divider("TECHNOLOGY LIFECYCLE ANALYSIS")

    section(f"All technologies ({len(technologies)} total)")
    header = f"  {'tech_id':<10} {'name':<38} {'category':<28} {'lifecycle'}"
    print(header)
    print("  " + "-" * (len(header) - 2))
    for t in technologies:
        print(f"  {t['tech_id']:<10} {t['name'][:36]:<38} {t['category'][:26]:<28} {t['lifecycle_status']}")

    section("Lifecycle status breakdown")
    lc_counts = Counter(t["lifecycle_status"] for t in technologies)
    for lc, count in sorted(lc_counts.items(), key=lambda x: -x[1]):
        bar = "█" * count
        print(f"  {lc:<15} {bar} ({count})")

    section("Technologies with named successors")
    with_successor = [t for t in technologies if t.get("successor", "").strip()]
    for t in with_successor:
        print(f"  {t['name']}")
        print(f"    → {t['successor']}")

    section("Obsolete technologies")
    obsolete = [t for t in technologies if t["lifecycle_status"] == "obsolete"]
    for t in obsolete:
        print(f"  • {t['name']} ({t['vendor']})")

    section("Technologies by category")
    cat_counts = Counter(t["category"] for t in technologies)
    for cat, count in sorted(cat_counts.items(), key=lambda x: -x[1]):
        bar = "█" * count
        print(f"  {cat:<32} {bar} ({count})")


def observation_analysis():
    divider("OBSERVATION ANALYSIS")

    section(f"Observation type breakdown ({len(observations)} total observations)")
    type_counts = Counter(o["observation_type"] for o in observations)
    for ot, count in sorted(type_counts.items(), key=lambda x: -x[1]):
        bar = "█" * count
        print(f"  {ot:<30} {bar} ({count})")

    section("Subject frequency (what is most observed)")
    subject_counts = Counter(o["subject"] for o in observations)
    for subj, count in sorted(subject_counts.items(), key=lambda x: -x[1]):
        bar = "█" * count
        print(f"  {subj[:40]:<42} {bar} ({count})")

    section("Product features for Digital LinkWorks")
    features = [o for o in observations
                if o["observation_type"] == "product-feature"
                and "LinkWorks" in o["subject"]]
    for i, obs in enumerate(features, 1):
        print(f"  {i:>2}. [{obs['dimension']}]")
        # wrap value_text
        words = obs["value_text"].split()
        line = "      "
        for word in words:
            if len(line) + len(word) + 1 > 74:
                print(line)
                line = "      " + word + " "
            else:
                line += word + " "
        if line.strip():
            print(line)

    section("Competitive assessments")
    comp = [o for o in observations if o["observation_type"] == "competitive-assessment"]
    for obs in comp:
        print(f"  Subject: {obs['subject']}")
        print(f"  Finding: {obs['value_text'][:120]}...")
        print()

    section("Analyst recommendations")
    recs = [o for o in observations if o["observation_type"] == "analyst-recommendation"]
    for obs in recs:
        print(f"  Subject   : {obs['subject']}")
        print(f"  Dimension : {obs['dimension']}")
        words = obs["value_text"].split()
        line = "  Text      : "
        for word in words:
            if len(line) + len(word) + 1 > 74:
                print(line)
                line = "              " + word + " "
            else:
                line += word + " "
        if line.strip():
            print(line)
        print()

    section("Numeric observations")
    numeric_obs = [o for o in observations if o.get("value_numeric", "").strip()]
    if numeric_obs:
        for obs in numeric_obs:
            print(f"  [{obs['obs_id']}] {obs['subject']} / {obs['dimension']}")
            print(f"    Value: {obs['value_numeric']} {obs['unit']}")
    else:
        print("  No numeric observations in this study.")

    section("Observations by source section")
    section_counts = Counter(o["source_section"] for o in observations)
    for sec, count in sorted(section_counts.items(), key=lambda x: -x[1]):
        bar = "█" * count
        print(f"  {sec[:45]:<47} {bar} ({count})")


def codes_summary():
    divider("CONTROLLED VOCABULARY SUMMARY")
    scheme_counts = Counter(c["scheme"] for c in codes)
    section(f"Codes per scheme ({len(codes)} total codes, {len(scheme_counts)} schemes)")
    for scheme, count in sorted(scheme_counts.items()):
        scheme_codes = [c for c in codes if c["scheme"] == scheme]
        print(f"  {scheme:<22} ({count} codes)")
        for c in scheme_codes:
            print(f"    · {c['code']:<30} {c['label']}")


def provenance():
    divider("DATA PROVENANCE")
    print("""
  Original Study
  ──────────────
  Title   : Digital LinkWorks: Delivering Solutions to MIS and End-Users
  Author  : Aberdeen Group, Inc.
  Date    : July 1995
  URL     : https://web.archive.org/web/19970108191558/
            http://www.aberdeen.com:80/secure/profiles/declink/declink1/declink.htm

  Package
  ───────
  Study ID  : aberdeen-1995-digital-linkworks
  Created   : 2026-03-13
  License   : ODC-By-1.0 (https://opendatacommons.org/licenses/by/1-0/)

  Entity & Technology Status Sources
  ───────────────────────────────────
  · DEC/Compaq/HP acquisition chain:
    https://www.globalspec.com/reference/43844/203279/a-brief-history-of-digital-compaq-and-hewlett-packard
    https://en.wikipedia.org/wiki/Compaq
  · Staffware/TIBCO acquisition:
    https://www.finextra.com/pressarticle/1438/tibco-completes-staffware-acquisition
  · FileNET/IBM acquisition:
    https://www.cnet.com/tech/tech-industry/ibm-to-pay-1-6-billion-for-filenet-1/
    """)


def main():
    print()
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║  Aberdeen Group Research Archive — Demo Analysis                    ║")
    print("║  Study 9: Digital LinkWorks (1995)                                  ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")

    study_summary()
    entity_analysis()
    technology_analysis()
    observation_analysis()
    codes_summary()
    provenance()

    divider("ANALYSIS COMPLETE")
    print(f"  Resources loaded from: {DATA_DIR}")
    totals = {
        "studies":      len(studies),
        "entities":     len(entities),
        "technologies": len(technologies),
        "observations": len(observations),
        "codes":        len(codes),
    }
    for name, count in totals.items():
        print(f"  {name:<16} {count} rows")
    print()


if __name__ == "__main__":
    main()
