#!/usr/bin/env python3
"""
generate_baseline_v1.py — Capture Phase 0 baselines against the LIVE DuckDB.

Emits Perplexity_Only/audit_masters_baseline.json for 07_audit_masters_v1.py
to compare against on every future run.

Runs against a read-only DuckDB connection to ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb.
Sandbox execution uses a duckdb Python package if available; otherwise the caller
falls back to running this on the Mac.
"""
import json
import re
import sys
from pathlib import Path

# Baselines captured from live DuckDB probes on 2026-07-07 via
# perplexity_bridge_v2 (read-only). If run on the Mac, this file re-queries
# and overwrites; otherwise it emits the frozen values below.

FROZEN_BASELINE = {
    "captured_at_utc": "2026-07-07T17:05:00Z",
    "source": "perplexity_bridge_v2 read-only DuckDB probes (2026-07-07 AM, pre-cleanse)",
    "shape": {
        "studies": 1504,
        "observations": 24842,
        "entities": 3293,
        "technologies": 4376,
        "high_prescience": 876,
    },
    "collision_ratio": {
        "entities_distinct_norm": 2905,
        "entities_total": 3293,
        "entities_ratio": 0.8822,
        "technologies_distinct_norm": 4048,
        "technologies_total": 4376,
        "technologies_ratio": 0.9250,
        "threshold_drop_alert": 0.02,
    },
    "tech_congruence_grandfathered_count": 1577,
    "tech_congruence_grandfathered_note": (
        "1,577 tech_ids currently violate the ID-vs-name substring rule. Most are "
        "legitimate: TECH-XXX-NNN Pass-B codes whose numeric slugs bear no relation "
        "to their (correct) tech_names. The harness stores the current set by "
        "tech_id and alerts only on NEW violations, so Pass B can keep using "
        "TECH-XXX-NNN placeholders without triggering false positives while the "
        "8 confirmed mislabels (data-mining, microsoft-backoffice, sun-ultrasparc, "
        "audio-conferencing, webex-training-center, titanium, t2-04, tech-01) "
        "are fixed in Phase A. Post-Phase-A this list shrinks by 8."
    ),
    "entity_successor_bleed_grandfathered": [
        "ENT-S3-001",
        "intel",
        "stratus-technologies",
        "sybase",
    ],
    "entity_successor_bleed_note": (
        "4 entity rows carry successor strings matching the Compaq+HP DEC-fanout "
        "bleed pattern where the entity_name is not itself DEC-family. Fixed in "
        "Phase B (except ENT-S3-001 which is a legit IBM-Software-Division "
        "placeholder with wrong metadata; disposition TBD in Phase B review)."
    ),
    "phase_0_gates": {
        "collision_ratio_drop_alert_pp": 0.02,
        "collision_ratio_drop_fail_pp": 0.05,
        "new_tech_congruence_violation_alert": 1,
        "new_tech_congruence_violation_fail": 10,
        "new_successor_bleed_alert": 1,
        "new_successor_bleed_fail": 5,
    },
}


def _norm(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9]", "", (s or "").lower())


def _live_capture(db_path: Path) -> dict:
    """Attempt live capture via duckdb Python package (Mac / duckdb-installed sandbox)."""
    try:
        import duckdb  # type: ignore
    except ImportError:
        return {}
    conn = duckdb.connect(str(db_path), read_only=True)
    try:
        shape = conn.execute("""
          SELECT
            (SELECT COUNT(*) FROM v_studies)                          AS studies,
            (SELECT COUNT(*) FROM v_observations)                     AS observations,
            (SELECT COUNT(*) FROM v_entities)                         AS entities,
            (SELECT COUNT(*) FROM v_technologies)                     AS technologies,
            (SELECT COUNT(*) FROM v_studies_with_high_prescience)     AS high_prescience;
        """).fetchone()
        ent_ratio = conn.execute("""
          SELECT COUNT(*) AS total,
                 COUNT(DISTINCT lower(regexp_replace(entity_name, '[^A-Za-z0-9]', '', 'g'))) AS distinct_norm
          FROM v_entities;
        """).fetchone()
        tech_ratio = conn.execute("""
          SELECT COUNT(*) AS total,
                 COUNT(DISTINCT lower(regexp_replace(tech_name, '[^A-Za-z0-9]', '', 'g'))) AS distinct_norm
          FROM v_technologies;
        """).fetchone()
        tech_congruence = conn.execute("""
          SELECT tech_id FROM v_technologies
          WHERE lower(regexp_replace(tech_name, '[^A-Za-z0-9]', '', 'g'))
            NOT LIKE ('%' || lower(regexp_replace(tech_id, '[^A-Za-z0-9]', '', 'g')) || '%')
            AND lower(regexp_replace(tech_id, '[^A-Za-z0-9]', '', 'g'))
            NOT LIKE ('%' || lower(regexp_replace(tech_name, '[^A-Za-z0-9]', '', 'g')) || '%')
          ORDER BY tech_id;
        """).fetchall()
        successor_bleed = conn.execute("""
          SELECT entity_id FROM v_entities
          WHERE successor ILIKE '%Compaq%' AND successor ILIKE '%HP%'
            AND entity_name NOT ILIKE '%DEC%' AND entity_name NOT ILIKE '%Digital Equipment%'
            AND entity_name NOT ILIKE '%Compaq%' AND entity_name NOT ILIKE '%Tandem%'
            AND entity_name NOT ILIKE '%HP %' AND entity_name NOT ILIKE '%Hewlett%'
            AND entity_name NOT ILIKE '%EDS%' AND entity_name NOT ILIKE '%3Com%'
            AND entity_name NOT ILIKE '%Palm%' AND entity_name NOT ILIKE '%Cray%'
            AND entity_name NOT ILIKE '%Alpha%' AND entity_name NOT ILIKE '%Digital%'
            AND entity_name NOT ILIKE 'HP'
          ORDER BY entity_id;
        """).fetchall()
        return {
            "shape": {
                "studies": shape[0], "observations": shape[1], "entities": shape[2],
                "technologies": shape[3], "high_prescience": shape[4],
            },
            "collision_ratio": {
                "entities_distinct_norm": ent_ratio[1], "entities_total": ent_ratio[0],
                "entities_ratio": round(ent_ratio[1] / ent_ratio[0], 4),
                "technologies_distinct_norm": tech_ratio[1], "technologies_total": tech_ratio[0],
                "technologies_ratio": round(tech_ratio[1] / tech_ratio[0], 4),
                "threshold_drop_alert": 0.02,
            },
            "tech_congruence_grandfathered_list": [r[0] for r in tech_congruence],
            "tech_congruence_grandfathered_count": len(tech_congruence),
            "entity_successor_bleed_grandfathered": [r[0] for r in successor_bleed],
        }
    finally:
        conn.close()


def main(argv: list) -> int:
    out = Path.home() / "Desktop/Archive/Perplexity_Only/audit_masters_baseline.json"
    db = Path.home() / "Repos/kastner-aberdeen-wiki/db/kastner.duckdb"
    if "--out" in argv:
        out = Path(argv[argv.index("--out") + 1])
    if "--db" in argv:
        db = Path(argv[argv.index("--db") + 1])

    baseline = dict(FROZEN_BASELINE)
    if db.exists():
        live = _live_capture(db)
        if live:
            # Merge — live shape wins; keep gates + notes from FROZEN.
            baseline.update(live)
            import datetime as _dt
            baseline["captured_at_utc"] = _dt.datetime.now(_dt.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
            baseline["source"] = f"live DuckDB at {db}"
        else:
            print(f"[WARN] duckdb Python package unavailable; emitting FROZEN baseline (2026-07-07 probe values).", file=sys.stderr)
    else:
        print(f"[WARN] {db} not found; emitting FROZEN baseline (2026-07-07 probe values).", file=sys.stderr)

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(baseline, indent=2, sort_keys=True))
    print(f"Wrote baseline: {out}")
    print(f"  Studies: {baseline['shape']['studies']}   Obs: {baseline['shape']['observations']}   Ent: {baseline['shape']['entities']}   Tech: {baseline['shape']['technologies']}")
    print(f"  Entity collision ratio: {baseline['collision_ratio']['entities_ratio']:.4f}")
    print(f"  Tech collision ratio:   {baseline['collision_ratio']['technologies_ratio']:.4f}")
    if "tech_congruence_grandfathered_list" in baseline:
        print(f"  Tech congruence grandfathered: {len(baseline['tech_congruence_grandfathered_list'])}")
    print(f"  Successor-bleed grandfathered: {len(baseline['entity_successor_bleed_grandfathered'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
