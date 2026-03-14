#!/usr/bin/env python3
"""
Demo Analysis Script — Aberdeen Group Study 12
"New LIMD Technology: Speed Plus Real-World Experience" (1995)

This script demonstrates how to load, validate, and analyze the
Frictionless Data Package for the LIMD Technology study.

Usage:
    pip install pandas matplotlib
    python scripts/demo_analysis.py

Output:
    - Summary statistics printed to stdout
    - Two chart PNG files saved alongside the script:
        scripts/chart_benchmark_results.png
        scripts/chart_performance_claims.png
"""

import os
import sys
import csv
import json
from pathlib import Path
from collections import Counter, defaultdict

# ---------------------------------------------------------------------------
# Resolve paths relative to the script location (works from any CWD)
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent
PACKAGE_DIR = SCRIPT_DIR.parent
DATA_DIR = PACKAGE_DIR / "data"


def load_csv(filename):
    """Load a CSV file from the data directory and return a list of dicts."""
    filepath = DATA_DIR / filename
    if not filepath.exists():
        raise FileNotFoundError(f"Data file not found: {filepath}")
    with open(filepath, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_json(filepath):
    """Load a JSON file and return parsed content."""
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Section 1: Package Metadata
# ---------------------------------------------------------------------------
def print_package_metadata():
    pkg = load_json(PACKAGE_DIR / "datapackage.json")
    print("=" * 70)
    print("FRICTIONLESS DATA PACKAGE — METADATA")
    print("=" * 70)
    print(f"  ID        : {pkg.get('id')}")
    print(f"  Title     : {pkg.get('title')}")
    print(f"  Version   : {pkg.get('version')}")
    print(f"  Created   : {pkg.get('created')}")
    print(f"  Resources : {len(pkg.get('resources', []))}")
    print(f"  Keywords  : {', '.join(pkg.get('keywords', [])[:8])} ...")
    print()


# ---------------------------------------------------------------------------
# Section 2: Study Summary
# ---------------------------------------------------------------------------
def print_study_summary():
    studies = load_csv("studies.csv")
    study = studies[0]
    print("=" * 70)
    print("STUDY SUMMARY")
    print("=" * 70)
    for key, val in study.items():
        if val:
            print(f"  {key:<22}: {val}")
    print()


# ---------------------------------------------------------------------------
# Section 3: Entity Analysis
# ---------------------------------------------------------------------------
def analyze_entities():
    entities = load_csv("entities.csv")
    print("=" * 70)
    print(f"ENTITIES ({len(entities)} total)")
    print("=" * 70)

    status_counts = Counter(e["current_status"] for e in entities)
    print("  Status breakdown:")
    for status, count in sorted(status_counts.items(), key=lambda x: -x[1]):
        print(f"    {status:<15} : {count}")
    print()

    type_counts = Counter(e["entity_type"] for e in entities)
    print("  Type breakdown:")
    for etype, count in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"    {etype:<20} : {count}")
    print()

    print("  Entities by role:")
    role_groups = defaultdict(list)
    for e in entities:
        role_groups[e["role_in_study"]].append(e["entity_name"])
    for role, names in sorted(role_groups.items()):
        print(f"    [{role}]")
        for name in names:
            print(f"      - {name}")
    print()


# ---------------------------------------------------------------------------
# Section 4: Technology Lifecycle Analysis
# ---------------------------------------------------------------------------
def analyze_technologies():
    techs = load_csv("technologies.csv")
    print("=" * 70)
    print(f"TECHNOLOGIES ({len(techs)} total)")
    print("=" * 70)

    status_counts = Counter(t["lifecycle_status"] for t in techs)
    print("  Lifecycle status breakdown:")
    for status, count in sorted(status_counts.items(), key=lambda x: -x[1]):
        print(f"    {status:<15} : {count}")
    print()

    cat_counts = Counter(t["tech_category"] for t in techs)
    print("  Category breakdown:")
    for cat, count in sorted(cat_counts.items(), key=lambda x: -x[1]):
        print(f"    {cat:<30} : {count}")
    print()

    print("  Obsolete technologies (with successors):")
    for t in techs:
        if t["lifecycle_status"] == "obsolete" and t["successor_tech"]:
            print(f"    {t['tech_name']:<35} -> {t['successor_tech'][:50]}")
    print()

    print("  Evolved technologies (with successors):")
    for t in techs:
        if t["lifecycle_status"] == "evolved" and t["successor_tech"]:
            print(f"    {t['tech_name']:<35} -> {t['successor_tech'][:50]}")
    print()


# ---------------------------------------------------------------------------
# Section 5: Observations Analysis
# ---------------------------------------------------------------------------
def analyze_observations():
    obs = load_csv("observations.csv")
    print("=" * 70)
    print(f"OBSERVATIONS ({len(obs)} total)")
    print("=" * 70)

    type_counts = Counter(o["observation_type"] for o in obs)
    print("  Observation type breakdown:")
    for otype, count in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"    {otype:<30} : {count}")
    print()

    # Key benchmark results
    benchmarks = [o for o in obs if o["observation_type"] == "benchmark-result"]
    print("  Benchmark Results:")
    print(f"  {'Metric':<45} {'Value':<12} {'Unit'}")
    print(f"  {'-'*45} {'-'*12} {'-'*20}")
    for b in benchmarks:
        if b["metric_value"]:
            print(f"  {b['metric_name']:<45} {b['metric_value']:<12} {b['metric_unit']}")
    print()

    # Key performance claims
    perf = [o for o in obs if o["observation_type"] == "performance-claim"]
    print("  Performance Claims:")
    print(f"  {'Metric':<45} {'Value':<12} {'Unit'}")
    print(f"  {'-'*45} {'-'*12} {'-'*20}")
    for p in perf:
        if p["metric_value"]:
            print(f"  {p['metric_name']:<45} {p['metric_value']:<12} {p['metric_unit']}")
    print()

    # Hardware specs
    hw = [o for o in obs if o["observation_type"] == "hardware-spec"]
    print("  Hardware Specifications:")
    print(f"  {'Metric':<45} {'Value':<12} {'Unit'}")
    print(f"  {'-'*45} {'-'*12} {'-'*20}")
    for h in hw:
        if h["metric_value"]:
            print(f"  {h['metric_name']:<45} {h['metric_value']:<12} {h['metric_unit']}")
    print()

    # Section distribution
    section_counts = Counter(o["section"] for o in obs)
    print("  Observations by section:")
    for sec, count in sorted(section_counts.items(), key=lambda x: -x[1]):
        print(f"    {sec:<40} : {count}")
    print()


# ---------------------------------------------------------------------------
# Section 6: Codes Summary
# ---------------------------------------------------------------------------
def analyze_codes():
    codes = load_csv("codes.csv")
    print("=" * 70)
    print(f"CONTROLLED VOCABULARY ({len(codes)} codes)")
    print("=" * 70)
    type_counts = Counter(c["code_type"] for c in codes)
    for ctype, count in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  {ctype:<30} : {count} codes")
    print()


# ---------------------------------------------------------------------------
# Section 7: Charts (optional — requires matplotlib)
# ---------------------------------------------------------------------------
def generate_charts():
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
    except ImportError:
        print("  [skipping charts — matplotlib not installed]")
        print("  Install with: pip install matplotlib")
        print()
        return

    obs = load_csv("observations.csv")
    techs = load_csv("technologies.csv")

    # ---- Chart 1: Benchmark Results Bar Chart ----
    benchmarks = [
        o for o in obs
        if o["observation_type"] == "benchmark-result" and o["metric_value"]
    ]
    # Filter to tpmC benchmarks for clean chart
    tpmc_obs = [b for b in benchmarks if "tpmC" in b.get("metric_unit", "")]
    if tpmc_obs:
        labels = [b["metric_name"].replace("-", "\n").replace("_", "\n") for b in tpmc_obs]
        values = [float(b["metric_value"]) for b in tpmc_obs]

        fig, ax = plt.subplots(figsize=(10, 5))
        colors = ["#20808D" if v == max(values) else "#BCE2E7" for v in values]
        bars = ax.barh(labels, values, color=colors, edgecolor="white", linewidth=0.5)
        ax.set_xlabel("tpmC (Transactions Per Minute, TPC-C)", fontsize=10)
        ax.set_title(
            "TPC-C Benchmark Results — LIMD Study (Aberdeen Group, 1995)\n"
            "11,456 tpmC record by Digital/Oracle marked in teal",
            fontsize=11, fontweight="bold"
        )
        for bar, val in zip(bars, values):
            ax.text(val + 50, bar.get_y() + bar.get_height() / 2,
                    f"{val:,.0f}", va="center", fontsize=9)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(axis="x", alpha=0.3, linestyle="--")
        plt.tight_layout()
        chart1_path = SCRIPT_DIR / "chart_benchmark_results.png"
        fig.savefig(chart1_path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"  Saved: {chart1_path}")

    # ---- Chart 2: Technology Lifecycle Pie Chart ----
    status_counts = Counter(t["lifecycle_status"] for t in techs)
    colors_map = {
        "obsolete": "#A84B2F",
        "evolved": "#20808D",
        "active": "#437A22",
        "ubiquitous": "#1B474D",
    }
    labels_pie = list(status_counts.keys())
    sizes = [status_counts[l] for l in labels_pie]
    colors_pie = [colors_map.get(l, "#848456") for l in labels_pie]

    fig2, ax2 = plt.subplots(figsize=(7, 5))
    wedges, texts, autotexts = ax2.pie(
        sizes, labels=labels_pie, colors=colors_pie, autopct="%1.0f%%",
        startangle=140, pctdistance=0.75,
        wedgeprops={"edgecolor": "white", "linewidth": 2}
    )
    for autotext in autotexts:
        autotext.set_fontsize(10)
    ax2.set_title(
        "Technology Lifecycle Status\nAberden Group LIMD Study (1995) — as of 2026",
        fontsize=11, fontweight="bold"
    )
    plt.tight_layout()
    chart2_path = SCRIPT_DIR / "chart_technology_lifecycle.png"
    fig2.savefig(chart2_path, dpi=150, bbox_inches="tight")
    plt.close(fig2)
    print(f"  Saved: {chart2_path}")

    # ---- Chart 3: Performance Claims Comparison ----
    perf_claims = [
        o for o in obs
        if o["observation_type"] == "performance-claim"
        and o["metric_unit"] == "x-times"
        and o["metric_value"]
    ]
    if perf_claims:
        labels_p = []
        vals_p = []
        colors_p = []
        for p in perf_claims:
            name = p["metric_name"].replace("-", " ").replace("_", " ").title()
            if len(name) > 40:
                name = name[:40] + "…"
            labels_p.append(name)
            vals_p.append(float(p["metric_value"]))
            colors_p.append("#20808D" if float(p["metric_value"]) >= 100 else "#BCE2E7")

        fig3, ax3 = plt.subplots(figsize=(11, 6))
        bars3 = ax3.barh(labels_p, vals_p, color=colors_p, edgecolor="white")
        ax3.set_xlabel("Performance Improvement (× times vs baseline)", fontsize=10)
        ax3.set_title(
            "Performance Claims — LIMD Technology (Aberdeen Group, 1995)\n"
            "Teal bars indicate ≥100× improvements",
            fontsize=11, fontweight="bold"
        )
        for bar, val in zip(bars3, vals_p):
            ax3.text(val + 0.5, bar.get_y() + bar.get_height() / 2,
                     f"{val:g}×", va="center", fontsize=9)
        ax3.spines["top"].set_visible(False)
        ax3.spines["right"].set_visible(False)
        ax3.grid(axis="x", alpha=0.3, linestyle="--")
        plt.tight_layout()
        chart3_path = SCRIPT_DIR / "chart_performance_claims.png"
        fig3.savefig(chart3_path, dpi=150, bbox_inches="tight")
        plt.close(fig3)
        print(f"  Saved: {chart3_path}")

    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print()
    print("Aberdeen Group — Study 12: LIMD Technology (1995)")
    print("Demo Analysis Script")
    print()

    print_package_metadata()
    print_study_summary()
    analyze_entities()
    analyze_technologies()
    analyze_observations()
    analyze_codes()

    print("=" * 70)
    print("CHARTS")
    print("=" * 70)
    generate_charts()

    print("=" * 70)
    print("KEY FINDINGS SUMMARY")
    print("=" * 70)
    print("""
  Context (1995):
  - Database sizes growing ~10× every 2-3 years; >100 databases over 100GB
  - 32-bit architecture limits addressable memory to <2GB (hard ceiling)
  - Digital Equipment Corp. (Alpha + VLM64) had 6-month head start shipping
    64-bit servers with Unix as of December 1995

  LIMD Definition:
  - ≥5 GB main memory + RDBMS software exploiting in-memory storage

  Benchmark Highlights:
  - Digital/Oracle TPC-C record: 11,456 tpmC at $286/tpmC
  - 1 GB RAM ≈ 1,300 additional tpmC (strong correlation)
  - Non-LIMD systems face scaling ceiling at ~5,000 tpmC

  Performance Gains:
  - General LIMD improvement: 20–40× over disk-based systems
  - 5-way join speedup: 105× (reported by tester)
  - Oracle 3-4-5-way join vs non-LIMD Oracle-on-Alpha: >200×
  - Sybase System 11 vs System 10 (same hardware): 3–5×
  - Order-of-magnitude improvement forecast for next 2 years

  Hardware (Alpha 8200/8400):
  - Alpha 8200: 6 CPUs, 6 GB RAM max
  - Alpha 8400: 12 CPUs, 14 GB RAM max
  - Both: 8.5 TB storage max
  - Memory Channel cluster bus: 100 MB/s

  Current Status (2026):
  - LIMD evolved → SAP HANA, Oracle TimesTen, SingleStore, Redis
  - VLM64/Alpha: obsolete (HP absorbed DEC 2002)
  - 64-bit computing: universal (ubiquitous)
  - TPC-C: still active (records now exceed 800M tpmC)
    """)

    print("  Source: Aberdeen Group Technology Viewpoint Vol. 8 No. 15")
    print("  URL: https://web.archive.org/web/19970112010820/")
    print("       http://www.aberdeen.com:80/secure/viewpnts/v8n15/v8n15.htm")
    print()


if __name__ == "__main__":
    main()
