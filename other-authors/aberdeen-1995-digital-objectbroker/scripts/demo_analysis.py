"""
demo_analysis.py
================
Demonstration analysis script for the Aberdeen Group (1995) study:
  "Digital's ObjectBroker -- Advanced Integration of Distributed Resources"
  Study ID: aberdeen-1995-digital-objectbroker

Reads the Frictionless Data Package CSVs from ../data/ and produces:
  1. Pricing comparison table
  2. Platform support breakdown (v2.5 vs v2.6 planned, by OS family)
  3. Technology lifecycle status distribution
  4. Entity acquisition timeline
  5. Observation category distribution
  6. Key numeric observations summary

Requirements: Python 3.8+, pandas (pip install pandas)
Usage: python scripts/demo_analysis.py
       (run from the package root: aberdeen-1995-digital-objectbroker/)
"""

import os
import sys
import csv
from pathlib import Path
from collections import Counter

# ---------------------------------------------------------------------------
# Path setup
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_csv(filename: str) -> list[dict]:
    """Load a CSV file from the data directory into a list of dicts."""
    path = DATA_DIR / filename
    if not path.exists():
        print(f"[ERROR] File not found: {path}")
        sys.exit(1)
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def separator(title: str, width: int = 70) -> None:
    print()
    print("=" * width)
    print(f"  {title}")
    print("=" * width)


# ---------------------------------------------------------------------------
# Load all tables
# ---------------------------------------------------------------------------
studies = load_csv("studies.csv")
entities = load_csv("entities.csv")
technologies = load_csv("technologies.csv")
platforms = load_csv("platforms.csv")
observations = load_csv("observations.csv")
codes = load_csv("codes.csv")

# ---------------------------------------------------------------------------
# 1. Study overview
# ---------------------------------------------------------------------------
separator("1. STUDY OVERVIEW")
study = studies[0]
print(f"  Study ID    : {study['study_id']}")
print(f"  Study #     : {study['study_num']}")
print(f"  Title       : {study['title']}")
print(f"  Author      : {study['author']}")
print(f"  Pub Date    : {study['pub_date']}")
print(f"  Study Type  : {study['study_type']}")
print(f"  Domain      : {study['domain']}")
print(f"  Methodology : {study['methodology']}")
print(f"  Archive URL : {study['archive_url']}")

# ---------------------------------------------------------------------------
# 2. Pricing summary
# ---------------------------------------------------------------------------
separator("2. PRICING SUMMARY (1995 USD)")
pricing_obs = [o for o in observations if o["obs_category"] == "pricing" and o["value_numeric"]]

# Column widths
print(f"  {'Subject':<40} {'Price':>12} {'Unit':<20}")
print(f"  {'-'*40} {'-'*12} {'-'*20}")
for o in sorted(pricing_obs, key=lambda x: float(x["value_numeric"] or 0)):
    if o["value_numeric"]:
        price = float(o["value_numeric"])
        print(f"  {o['subject']:<40} ${price:>11,.2f} {o['value_unit']:<20}")

# Ratio analysis
prices = {o["subject"]: float(o["value_numeric"]) for o in pricing_obs if o["value_numeric"]}
if "ObjectBroker Unix development pricing" in prices and "ObjectBroker runtime pricing" in prices:
    ratio_unix_pc = prices["ObjectBroker Unix development pricing"] / prices["ObjectBroker runtime pricing"]
    print(f"\n  Unix dev : PC runtime ratio  = {ratio_unix_pc:.1f}x")
if "ObjectBroker NT development pricing" in prices and "ObjectBroker runtime pricing" in prices:
    ratio_nt_pc = prices["ObjectBroker NT development pricing"] / prices["ObjectBroker runtime pricing"]
    print(f"  NT dev : PC runtime ratio    = {ratio_nt_pc:.1f}x")

# ---------------------------------------------------------------------------
# 3. Platform support breakdown
# ---------------------------------------------------------------------------
separator("3. PLATFORM SUPPORT BREAKDOWN (19 combinations)")

v25 = [p for p in platforms if p["availability"] == "v2.5"]
v26 = [p for p in platforms if p["availability"] == "v2.6-planned"]

print(f"\n  v2.5 (generally available) : {len(v25)} platforms")
print(f"  v2.6 (planned/forthcoming) : {len(v26)} platforms")
print(f"  Total                       : {len(platforms)} platforms")

# By OS family
print(f"\n  {'OS Family':<20} {'v2.5':>5} {'v2.6 planned':>12} {'Total':>7}")
print(f"  {'-'*20} {'-'*5} {'-'*12} {'-'*7}")
os_families_all = sorted(set(p["os_family"] for p in platforms))
for fam in os_families_all:
    c25 = sum(1 for p in v25 if p["os_family"] == fam)
    c26 = sum(1 for p in v26 if p["os_family"] == fam)
    print(f"  {fam:<20} {c25:>5} {c26:>12} {c25+c26:>7}")

# By port_by
print(f"\n  Ports by organization:")
port_counter = Counter(p["port_by"] for p in platforms)
for org, count in port_counter.most_common():
    pct = count / len(platforms) * 100
    print(f"    {org:<12} : {count:>2} platforms ({pct:.0f}%)")

# ---------------------------------------------------------------------------
# 4. Technology lifecycle status distribution
# ---------------------------------------------------------------------------
separator("4. TECHNOLOGY LIFECYCLE STATUS DISTRIBUTION (as of 2026)")

lifecycle_counter = Counter(t["lifecycle_status"] for t in technologies)
total_techs = len(technologies)

print(f"\n  {'Status':<12} {'Count':>6} {'Pct':>6}  {'Technologies'}")
print(f"  {'-'*12} {'-'*6} {'-'*6}  {'-'*50}")
for status, count in sorted(lifecycle_counter.items(), key=lambda x: -x[1]):
    techs_with_status = [t["tech_name"] for t in technologies if t["lifecycle_status"] == status]
    pct = count / total_techs * 100
    print(f"  {status:<12} {count:>6} {pct:>5.0f}%  {', '.join(techs_with_status[:3])}{'...' if len(techs_with_status) > 3 else ''}")

obsolete_or_legacy = sum(1 for t in technologies if t["lifecycle_status"] in ("obsolete", "legacy"))
print(f"\n  Technologies now obsolete or legacy: {obsolete_or_legacy}/{total_techs} ({obsolete_or_legacy/total_techs*100:.0f}%)")

# ---------------------------------------------------------------------------
# 5. Entity acquisition / status timeline
# ---------------------------------------------------------------------------
separator("5. ENTITY STATUS OVERVIEW (as of 2026)")

print(f"\n  {'Entity':<35} {'Type':<16} {'Status (1995)':<14} {'Status (2026)'}")
print(f"  {'-'*35} {'-'*16} {'-'*14} {'-'*30}")
for e in sorted(entities, key=lambda x: x["entity_type"]):
    print(f"  {e['entity_name']:<35} {e['entity_type']:<16} {e['status_at_pub']:<14} {e['status_current']}")

acquired = [e for e in entities if e["status_current"] == "acquired"]
merged = [e for e in entities if e["status_current"] == "merged"]
active = [e for e in entities if e["status_current"] == "active"]
unknown = [e for e in entities if e["status_current"] == "unknown"]

print(f"\n  Entities acquired    : {len(acquired)}")
print(f"  Entities merged      : {len(merged)}")
print(f"  Entities still active: {len(active)}")
print(f"  Status unknown       : {len(unknown)}")
print(f"\n  Note: ALL key technology vendors (Digital, EDS, Tandem, Logica, Protosoft)")
print(f"        were acquired/merged within 3-17 years of this 1995 publication.")

# ---------------------------------------------------------------------------
# 6. Observation category distribution
# ---------------------------------------------------------------------------
separator("6. OBSERVATION CATEGORY DISTRIBUTION")

cat_counter = Counter(o["obs_category"] for o in observations)
total_obs = len(observations)

print(f"\n  {'Category':<24} {'Count':>6} {'Pct':>6}  {'Bar'}")
print(f"  {'-'*24} {'-'*6} {'-'*6}  {'-'*30}")
for cat, count in sorted(cat_counter.items(), key=lambda x: -x[1]):
    pct = count / total_obs * 100
    bar = "█" * int(pct / 3)
    print(f"  {cat:<24} {count:>6} {pct:>5.0f}%  {bar}")

print(f"\n  Total observations: {total_obs}")

# ---------------------------------------------------------------------------
# 7. Key numeric observations
# ---------------------------------------------------------------------------
separator("7. KEY NUMERIC OBSERVATIONS")

numeric_obs = [o for o in observations if o["value_numeric"]]
print(f"\n  {'Subject':<45} {'Value':>10} {'Unit':<20}")
print(f"  {'-'*45} {'-'*10} {'-'*20}")
for o in sorted(numeric_obs, key=lambda x: float(x["value_numeric"])):
    val = float(o["value_numeric"])
    if val > 100:  # skip small values for readability
        fmt_val = f"{val:,.0f}"
    else:
        fmt_val = f"{val:g}"
    print(f"  {o['subject'][:45]:<45} {fmt_val:>10} {o['value_unit']:<20}")

# ---------------------------------------------------------------------------
# 8. High-confidence analyst assessments
# ---------------------------------------------------------------------------
separator("8. ABERDEEN ANALYST ASSESSMENTS (from study)")

analyst_obs = [o for o in observations if o["obs_category"] == "analyst-assessment"]
for o in analyst_obs:
    print(f"\n  [{o['obs_id']}] {o['subject']}")
    print(f"  Observation: {o['observation']}")
    print(f"  Value: {o['value_text']}")

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
separator("SUMMARY")
print(f"""
  This Aberdeen Group product profile (August 1995) profiles Digital Equipment
  Corporation's ObjectBroker 2.5, an ORB implementation conforming to CORBA 1.2.

  Key findings extracted:
    - 50 structured observations across 8 categories
    - 19 technologies tracked (lifecycle: {obsolete_or_legacy}/{total_techs} now obsolete/legacy)
    - 19 platform combinations documented (15 v2.5 GA, 4 v2.6 planned)
    - 11 entities tracked ({len(acquired)} acquired, {len(merged)} merged, {len(active)} still active)
    - 3 price points documented ($149 / $980 / $5,000 per seat)

  Historical note: ObjectBroker itself became obsolete after Digital was
  acquired by Compaq in 1998. CORBA broadly declined in the 2000s as web
  services (SOAP, REST) and later microservices architectures displaced
  traditional ORB-based middleware.
""")

if __name__ == "__main__":
    pass  # Script runs on import for demo; all output above is top-level
