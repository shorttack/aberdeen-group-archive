#!/usr/bin/env python3
"""future_studies_evidence_probe_v1.py  — READ-ONLY archive evidence tally.

For each of Pete's 7 candidate study ideas, resolve matching entities +
technologies (alias-aware via regex), then tally the evidence footprint:
distinct studies, observations, entity/tech counts, decade span, and prescience
signal. Writes a JSON summary the agent reads back to build the planning table.

Read-only: opens DuckDB with read_only=True. No writes to any master or the DB.
"""
import duckdb, json, re
from pathlib import Path

DB = str(Path.home() / "Repos/kastner-aberdeen-wiki/db/kastner.duckdb")

# Each idea: a regex over lower(name||' '||id) for entities AND technologies,
# plus optional extra tech/keyword regex. Kept broad; we report what matches.
IDEAS = {
    "crm_enterprise_apps": {
        "label": "CRM & HP enterprise app arc (Salesforce, Siebel, PeopleSoft, Vantive, Clarify...)",
        "ent_re": r"salesforce|siebel|peoplesoft|vantive|clarify|onyx|remedy|epiphany|kana|baan|jd.?edwards",
        "tech_re": r"\bcrm\b|customer relationship|sales force automation|\bsfa\b|call center|help.?desk",
    },
    "decision_support": {
        "label": "Arc of decision support (MicroStrategy/Saylor, ROLAP, Teradata, OLAP, BI, data analytics role)",
        "ent_re": r"microstrategy|saylor|teradata|cognos|business.?objects|hyperion|arbor|brio|informatica|sagent|red.?brick",
        "tech_re": r"rolap|molap|\bolap\b|data.?warehous|decision support|\bdss\b|business intelligence|\bbi\b|data mart|star schema|analytics",
    },
    "erp_beyond_sap": {
        "label": "ERP beyond SAP (Oracle Apps, PeopleSoft, Baan, JD Edwards, MFG/PRO, SSA...)",
        "ent_re": r"peoplesoft|baan|jd.?edwards|\bqad\b|\bssa\b|mfg.?pro|lawson|great.?plains|ramco|intentia|epicor|oracle.?applications",
        "tech_re": r"\berp\b|enterprise resource|\bmrp\b|manufacturing resource|supply chain",
    },
    "multiprocessor_transition": {
        "label": "Multiprocessor transition (uni->SMP; RISC vs CISC; VAX/Alpha, RS/6000, HP 9000, Sun SPARC/Motorola, NCR)",
        "ent_re": r"\bncr\b|sun.?micro|\bdec\b|digital.?equipment|hewlett|\bhp\b|mips.?computer|sequent|pyramid|encore",
        "tech_re": r"\brisc\b|\bcisc\b|\bsmp\b|multiprocess|symmetric.?multi|\bvax\b|\balpha\b|rs.?6000|\bpower\b|hp.?9000|\bpa.?risc\b|\bsparc\b|\bmips\b|68000|motorola.?680|uniprocess|superscalar",
    },
    "mainframe_rebirth": {
        "label": "IBM Mainframe rebirth (dinosaur criticism -> Linux repricing -> Red Hat)",
        "ent_re": r"\bibm\b|red.?hat",
        "tech_re": r"mainframe|\bs.?390\b|zseries|\bz.?series\b|\bz.?os\b|system.?z|\bos.?390\b|\bmvs\b|linux.*mainframe|ifl|integrated facility",
    },
    "pc_deals_rollup": {
        "label": "PC Deals rollup",
        "ent_re": r"\bdell\b|compaq|gateway|packard.?bell|\bemachines\b|micron|\bcdw\b|\bpc.?connection\b|insight.?enterprises",
        "tech_re": r"pc.?deal|desktop.?pc|retail.?pc|pc.?pricing|pc.?bundle|street.?price",
    },
    "kastner_on_wall_street": {
        "label": "Kastner on Wall Street (analyst quotes as sell-side went quiet)",
        "ent_re": r"morgan|goldman|merrill|lehman|salomon|bear.?stearns|first.?boston|hambrecht|montgomery.?securities|robertson.?stephens|alex.?brown",
        "tech_re": r"wall.?street|underwrit|sell.?side|equity.?research|ipo|initial.?public",
    },
    "network_management": {
        "label": "Network/systems management (HP OpenView, IBM/Tivoli, CA Unicenter, SNMP, enterprise mgmt frameworks)",
        "ent_re": r"tivoli|openview|open.?view|\bcabletron\b|\b3com\b|bay.?networks|synoptics|\bwellfleet\b|micromuse|concord.?communications|netscout|\bbmc\b|\bnetiq\b|computer.?associates|\bca\b.?unicenter|hewlett|\bibm\b|\bsolarwinds\b|\bloudcloud\b",
        "tech_re": r"network.?management|systems.?management|\bsnmp\b|\brmon\b|openview|open.?view|unicenter|tivoli|\bnms\b|element.?management|fault.?management|enterprise.?management|\bcmip\b|network.?monitor|\bitil\b|service.?management",
    },
}


def q(con, sql, params=None):
    return con.execute(sql, params or []).fetchall()


def resolve_ids(con, view, id_col, name_col, pattern):
    rows = q(con, f"SELECT {id_col}, {name_col}, occurrence_count FROM {view} "
                  f"WHERE regexp_matches(lower({name_col} || ' ' || {id_col}), ?) "
                  f"ORDER BY occurrence_count DESC", [pattern])
    return rows


def main():
    con = duckdb.connect(DB, read_only=True)
    out = {}
    for key, spec in IDEAS.items():
        ents = resolve_ids(con, "v_entities", "entity_id", "entity_name", spec["ent_re"])
        techs = resolve_ids(con, "v_technologies", "tech_id", "tech_name", spec["tech_re"])
        ent_ids = [e[0] for e in ents]
        tech_ids = [t[0] for t in techs]

        # studies + obs touching any of these entities OR techs
        study_ids = set()
        obs_count = 0
        if ent_ids or tech_ids:
            placeholders_e = ",".join(["?"] * len(ent_ids)) or "NULL"
            placeholders_t = ",".join(["?"] * len(tech_ids)) or "NULL"
            rows = q(con,
                f"SELECT DISTINCT o.study_id FROM v_observations o "
                f"WHERE o.entity_id IN ({placeholders_e}) OR o.tech_id IN ({placeholders_t})",
                ent_ids + tech_ids)
            study_ids = {r[0] for r in rows}
            obs_rows = q(con,
                f"SELECT COUNT(*) FROM v_observations o "
                f"WHERE o.entity_id IN ({placeholders_e}) OR o.tech_id IN ({placeholders_t})",
                ent_ids + tech_ids)
            obs_count = obs_rows[0][0]

        # decade span + prescience of the touching studies
        decade_span, hi_presc, mean_presc = None, 0, None
        if study_ids:
            sp = ",".join(["?"] * len(study_ids))
            yr = q(con, f"SELECT MIN(CAST(pub_year AS INT)), MAX(CAST(pub_year AS INT)) "
                        f"FROM v_studies WHERE study_id IN ({sp}) AND pub_year IS NOT NULL", list(study_ids))
            if yr and yr[0][0]:
                decade_span = f"{yr[0][0]}-{yr[0][1]}"
            hp = q(con, f"SELECT COUNT(*) FROM v_studies WHERE study_id IN ({sp}) "
                        f"AND study_prescience_enum='high'", list(study_ids))
            hi_presc = hp[0][0]
            mp = q(con, f"SELECT ROUND(AVG(prescience_mean),2) FROM v_studies "
                        f"WHERE study_id IN ({sp}) AND prescience_mean IS NOT NULL", list(study_ids))
            mean_presc = mp[0][0]

        out[key] = {
            "label": spec["label"],
            "n_entities": len(ents),
            "top_entities": [(e[0], e[1], e[2]) for e in ents[:8]],
            "n_technologies": len(techs),
            "top_technologies": [(t[0], t[1], t[2]) for t in techs[:8]],
            "n_studies": len(study_ids),
            "n_observations": obs_count,
            "decade_span": decade_span,
            "high_prescience_studies": hi_presc,
            "mean_prescience": mean_presc,
        }
    con.close()
    outp = Path.home() / "Desktop/Archive/future_studies_evidence.json"
    outp.write_text(json.dumps(out, indent=2))
    print("WROTE", outp)
    # also print a compact summary
    for k, v in out.items():
        print(f"\n### {k}")
        print(f"  studies={v['n_studies']}  obs={v['n_observations']}  "
              f"entities={v['n_entities']}  techs={v['n_technologies']}  "
              f"span={v['decade_span']}  high_presc={v['high_prescience_studies']}  mean={v['mean_prescience']}")
        print(f"  top entities: {[e[0]+'('+str(e[2])+')' for e in v['top_entities'][:6]]}")
        print(f"  top techs:    {[t[0]+'('+str(t[2])+')' for t in v['top_technologies'][:6]]}")


if __name__ == "__main__":
    main()
