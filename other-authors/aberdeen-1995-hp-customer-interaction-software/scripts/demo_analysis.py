#!/usr/bin/env python3
"""
demo_analysis.py — Referential Integrity Validation and Demo Analysis
Aberdeen Group Research Archive: HP CIS (1995)
Study ID: aberdeen-1995-hp-customer-interaction-software

Validates FK relationships across all CSVs and prints summary statistics.
"""

import csv
import sys
from pathlib import Path
from collections import defaultdict, Counter

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

STUDY_ID = "aberdeen-1995-hp-customer-interaction-software"


# ---------------------------------------------------------------------------
# Loader
# ---------------------------------------------------------------------------
def load_csv(filename: str) -> list[dict]:
    filepath = DATA_DIR / filename
    if not filepath.exists():
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)
    with open(filepath, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return rows


# ---------------------------------------------------------------------------
# Referential Integrity Checks
# ---------------------------------------------------------------------------
def check_referential_integrity(
    studies: list[dict],
    entities: list[dict],
    technologies: list[dict],
    observations: list[dict],
    codes: list[dict],
) -> list[str]:
    errors = []

    # Build sets of valid primary keys
    valid_study_ids = {r["study_id"] for r in studies}
    valid_entity_ids = {r["entity_id"] for r in entities}
    valid_tech_ids = {r["tech_id"] for r in technologies}

    # --- entities.study_id → studies.study_id ---
    for row in entities:
        if row["study_id"] not in valid_study_ids:
            errors.append(
                f"entities[{row['entity_id']}].study_id '{row['study_id']}' not in studies"
            )

    # --- technologies.study_id → studies.study_id ---
    for row in technologies:
        if row["study_id"] not in valid_study_ids:
            errors.append(
                f"technologies[{row['tech_id']}].study_id '{row['study_id']}' not in studies"
            )

    # --- observations.study_id → studies.study_id ---
    for row in observations:
        if row["study_id"] not in valid_study_ids:
            errors.append(
                f"observations[{row['obs_id']}].study_id '{row['study_id']}' not in studies"
            )

    # --- observations.entity_id → entities.entity_id (nullable) ---
    for row in observations:
        eid = row.get("entity_id", "").strip()
        if eid and eid not in valid_entity_ids:
            errors.append(
                f"observations[{row['obs_id']}].entity_id '{eid}' not in entities"
            )

    # --- observations.tech_id → technologies.tech_id (nullable) ---
    for row in observations:
        tid = row.get("tech_id", "").strip()
        if tid and tid not in valid_tech_ids:
            errors.append(
                f"observations[{row['obs_id']}].tech_id '{tid}' not in technologies"
            )

    # --- Uniqueness checks ---
    def check_unique(rows: list[dict], key: str, table: str):
        seen = set()
        for row in rows:
            val = row[key]
            if val in seen:
                errors.append(f"{table}.{key} duplicate value: '{val}'")
            seen.add(val)

    check_unique(studies, "study_id", "studies")
    check_unique(entities, "entity_id", "entities")
    check_unique(technologies, "tech_id", "technologies")
    check_unique(observations, "obs_id", "observations")
    check_unique(codes, "code_id", "codes")

    return errors


# ---------------------------------------------------------------------------
# Demo Analysis
# ---------------------------------------------------------------------------
def demo_analysis(
    studies: list[dict],
    entities: list[dict],
    technologies: list[dict],
    observations: list[dict],
    codes: list[dict],
) -> None:
    sep = "-" * 60

    print(sep)
    print("ABERDEEN GROUP RESEARCH ARCHIVE — HP CIS (1995)")
    print("Demo Analysis & Referential Integrity Report")
    print(sep)

    # --- Row counts ---
    print("\n[1] TABLE ROW COUNTS")
    print(f"  studies.csv          : {len(studies):>4} rows")
    print(f"  entities.csv         : {len(entities):>4} rows")
    print(f"  technologies.csv     : {len(technologies):>4} rows")
    print(f"  observations.csv     : {len(observations):>4} rows")
    print(f"  codes.csv            : {len(codes):>4} rows")

    # --- Study metadata ---
    study = studies[0]
    print(f"\n[2] STUDY METADATA")
    print(f"  ID         : {study['study_id']}")
    print(f"  Title      : {study['title']}")
    print(f"  Author     : {study['author']}")
    print(f"  Date       : {study['publication_date']}")
    print(f"  Type       : {study['study_type']}")
    print(f"  Domain     : {study['domain']}")
    print(f"  Methodology: {study['methodology']}")

    # --- Entity status breakdown ---
    status_counts = Counter(e["status"] for e in entities)
    print(f"\n[3] ENTITY STATUS BREAKDOWN ({len(entities)} entities)")
    for status, count in sorted(status_counts.items(), key=lambda x: -x[1]):
        print(f"  {status:<12}: {count}")

    # --- Entity type breakdown ---
    type_counts = Counter(e["entity_type"] for e in entities)
    print(f"\n[4] ENTITY TYPE BREAKDOWN")
    for etype, count in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  {etype:<22}: {count}")

    # --- Technology lifecycle breakdown ---
    current_counts = Counter(t["lifecycle_current"] for t in technologies)
    at_study_counts = Counter(t["lifecycle_at_study"] for t in technologies)
    print(f"\n[5] TECHNOLOGY LIFECYCLE AT STUDY")
    for stage, count in sorted(at_study_counts.items(), key=lambda x: -x[1]):
        print(f"  {stage:<12}: {count}")
    print(f"\n[6] TECHNOLOGY LIFECYCLE CURRENT")
    for stage, count in sorted(current_counts.items(), key=lambda x: -x[1]):
        print(f"  {stage:<12}: {count}")

    # --- Observation type breakdown ---
    obs_type_counts = Counter(o["observation_type"] for o in observations)
    print(f"\n[7] OBSERVATION TYPE BREAKDOWN ({len(observations)} observations)")
    for otype, count in sorted(obs_type_counts.items(), key=lambda x: -x[1]):
        print(f"  {otype:<30}: {count}")

    # --- Confidence breakdown ---
    conf_counts = Counter(o["confidence"] for o in observations)
    print(f"\n[8] OBSERVATION CONFIDENCE BREAKDOWN")
    for conf, count in sorted(conf_counts.items(), key=lambda x: -x[1]):
        print(f"  {conf:<12}: {count}")

    # --- Methodology code breakdown ---
    meth_counts = Counter(o["methodology_code"] for o in observations)
    print(f"\n[9] METHODOLOGY CODE BREAKDOWN")
    for meth, count in sorted(meth_counts.items(), key=lambda x: -x[1]):
        print(f"  {meth:<6}: {count}")

    # --- Key market data observations ---
    market_obs = [
        o for o in observations
        if o["observation_type"] in ("market-size", "market-assessment", "financial-metric")
    ]
    print(f"\n[10] KEY MARKET / FINANCIAL OBSERVATIONS ({len(market_obs)})")
    for o in market_obs:
        entity_label = f"[{o['entity_id']}] " if o["entity_id"] else ""
        print(f"  {o['obs_id']}: {entity_label}{o['metric_name']}")
        print(f"           Value: {o['metric_value']}")

    # --- Analyst predictions ---
    pred_obs = [o for o in observations if o["observation_type"] == "analyst-prediction"]
    print(f"\n[11] ANALYST PREDICTIONS ({len(pred_obs)})")
    for o in pred_obs:
        print(f"  {o['obs_id']}: {o['metric_name']}")
        print(f"           Value: {o['metric_value']}")

    # --- Entities with no observations (coverage check) ---
    obs_entity_ids = {o["entity_id"] for o in observations if o["entity_id"]}
    obs_tech_ids = {o["tech_id"] for o in observations if o["tech_id"]}
    uncovered_entities = [e for e in entities if e["entity_id"] not in obs_entity_ids]
    uncovered_techs = [t for t in technologies if t["tech_id"] not in obs_tech_ids]
    print(f"\n[12] COVERAGE CHECK")
    print(f"  Entities with observations    : {len(entities) - len(uncovered_entities)}/{len(entities)}")
    print(f"  Technologies with observations: {len(technologies) - len(uncovered_techs)}/{len(technologies)}")
    if uncovered_entities:
        print(f"  Entities WITHOUT observations ({len(uncovered_entities)}):")
        for e in uncovered_entities[:10]:
            print(f"    - {e['entity_id']} ({e['entity_name']})")
        if len(uncovered_entities) > 10:
            print(f"    ... and {len(uncovered_entities) - 10} more")

    # --- Code type coverage ---
    code_type_counts = Counter(c["code_type"] for c in codes)
    print(f"\n[13] CODE TYPES ({len(codes)} codes)")
    for ctype, count in sorted(code_type_counts.items()):
        print(f"  {ctype:<25}: {count}")

    print(f"\n{sep}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("Loading CSV files...")
    studies = load_csv("studies.csv")
    entities = load_csv("entities.csv")
    technologies = load_csv("technologies.csv")
    observations = load_csv("observations.csv")
    codes = load_csv("codes.csv")

    print("Running referential integrity checks...")
    errors = check_referential_integrity(
        studies, entities, technologies, observations, codes
    )

    if errors:
        print(f"\nREFERENTIAL INTEGRITY: FAILED ({len(errors)} error(s))")
        for err in errors:
            print(f"  ERROR: {err}")
        sys.exit(1)
    else:
        print("REFERENTIAL INTEGRITY: PASSED — no errors found\n")

    demo_analysis(studies, entities, technologies, observations, codes)
    print("Demo analysis complete.")


if __name__ == "__main__":
    main()
