#!/usr/bin/env python3
"""mainframe_dossier_extract_v1.py  — READ-ONLY Phase-1 evidence extraction.

IBM mainframe rebirth dossier. Scoped on mainframe-SPECIFIC technologies + the
Linux/Red Hat rebirth axis, NOT the generic `ibm` entity (which is everywhere).
Writes structured JSON the agent assembles into the Phase-1 dossier.

Read-only: DuckDB read_only=True.
"""
import duckdb, json
from pathlib import Path

DB = str(Path.home() / "Repos/kastner-aberdeen-wiki/db/kastner.duckdb")
OUT = Path.home() / "Desktop/Archive/mainframe_dossier_evidence.json"

# mainframe-SPECIFIC technology regex (platform lineage + Linux rebirth)
TECH_RE = (r"mainframe|\bs.?390\b|\bes.?9000\b|\b3090\b|\b4300\b|zseries|\bz.?series\b|"
           r"\bz.?os\b|\bz.?arch|system.?z|\bos.?390\b|\bmvs\b|\bvm\b.?cms|\bvse\b|"
           r"parallel.?sysplex|\bcmos\b.?mainframe|\bifl\b|integrated.?facility.?linux|"
           r"linux.*mainframe|mainframe.*linux|\bzvm\b|\brmf\b|\bcics\b|\bims\b|hercules")
# Linux / open-workload / Red Hat rebirth entities + the mainframe-adjacent players
ENT_RE = (r"red.?hat|\bsuse\b|linux|amdahl|hitachi.?data|comparex|platform.?solutions|"
          r"fundamental.?software|\bt3\b.?technologies")

con = duckdb.connect(DB, read_only=True)
def rows(sql, p=None): return con.execute(sql, p or []).fetchall()

techs = rows("SELECT tech_id, tech_name, vendor, era, lifecycle_at_study, lifecycle_current, occurrence_count "
             "FROM v_technologies WHERE regexp_matches(lower(tech_name||' '||tech_id), ?) ORDER BY occurrence_count DESC", [TECH_RE])
ents = rows("SELECT entity_id, entity_name, entity_type, sector, occurrence_count "
            "FROM v_entities WHERE regexp_matches(lower(entity_name||' '||entity_id), ?) ORDER BY occurrence_count DESC", [ENT_RE])
tech_ids=[t[0] for t in techs]; ent_ids=[e[0] for e in ents]
pe=",".join(["?"]*len(ent_ids)) or "NULL"; pt=",".join(["?"]*len(tech_ids)) or "NULL"
tf=f"(o.entity_id IN ({pe}) OR o.tech_id IN ({pt}))"; params=ent_ids+tech_ids

studies = rows(
  f"SELECT DISTINCT s.study_id, s.title, s.pub_year, s.type, s.author, s.study_prescience_enum, s.prescience_mean, "
  f"(SELECT COUNT(*) FROM v_observations o2 WHERE o2.study_id=s.study_id AND {tf.replace('o.','o2.')}) AS rel "
  f"FROM v_studies s JOIN v_observations o USING(study_id) WHERE {tf} ORDER BY rel DESC, s.pub_year", params+params)
obs = rows(
  f"SELECT o.obs_id,o.study_id,o.entity_id,o.tech_id,o.year_observed,o.observation_type,o.metric_name,o.metric_value,o.confidence "
  f"FROM v_observations o WHERE {tf} ORDER BY TRY_CAST(o.year_observed AS INT) NULLS LAST, o.study_id", params)
presc = rows(
  f"SELECT p.prescience_score,o.year_observed,o.study_id,o.metric_value "
  f"FROM v_observations o JOIN v_prescience_raw p USING(obs_id) WHERE {tf} "
  f"AND TRY_CAST(p.prescience_score AS INT)>=4 ORDER BY TRY_CAST(p.prescience_score AS INT) DESC, o.year_observed", params)
yr = rows(
  f"SELECT TRY_CAST(o.year_observed AS INT) y, COUNT(*) n FROM v_observations o WHERE {tf} "
  f"AND TRY_CAST(o.year_observed AS INT) BETWEEN 1980 AND 2026 GROUP BY y ORDER BY y", params)
con.close()

def pack(r,c): return [dict(zip(c,x)) for x in r]
out={"topic":"IBM Mainframe Rebirth",
 "technologies":pack(techs,["tech_id","tech_name","vendor","era","lifecycle_at_study","lifecycle_current","occ"]),
 "entities":pack(ents,["entity_id","entity_name","entity_type","sector","occ"]),
 "studies":pack(studies,["study_id","title","pub_year","type","author","presc_enum","presc_mean","rel_obs"]),
 "observations":pack(obs,["obs_id","study_id","entity_id","tech_id","year","obs_type","metric_name","metric_value","confidence"]),
 "high_prescience":pack(presc,["score","year","study_id","metric_value"]),
 "year_hist":pack(yr,["year","n"])}
OUT.write_text(json.dumps(out,indent=2,default=str))
print("WROTE",OUT)
print(f"techs={len(techs)} entities={len(ents)} studies={len(studies)} obs={len(obs)} high_presc={len(presc)}")
print("top techs:",[t[0] for t in techs[:12]])
print("top ents :",[e[0] for e in ents[:12]])
print("top studies:")
for s in studies[:12]:
    print(f"  {s[7]:>3} obs | {s[2]} | {s[5]:14s} | {s[0]}  {s[1][:52]}")
print("year hist:", [(y[0],y[1]) for y in yr])
