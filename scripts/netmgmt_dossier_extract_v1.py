#!/usr/bin/env python3
"""netmgmt_dossier_extract_v1.py  — READ-ONLY Phase-1 evidence extraction.

Network/systems management longitudinal dossier. Tech-scoped (the honest signal),
plus management-specific entities (NOT broad IBM/HP). Writes a structured JSON
the agent assembles into the Phase-1 dossier.

Read-only: opens DuckDB read_only=True. No writes to masters or DB.
"""
import duckdb, json
from pathlib import Path

DB = str(Path.home() / "Repos/kastner-aberdeen-wiki/db/kastner.duckdb")
OUT = Path.home() / "Desktop/Archive/netmgmt_dossier_evidence.json"

# management-SPECIFIC technology regex (the honest signal that gave v2's 32/130)
TECH_RE = (r"network.?management|systems.?management|\bsnmp\b|\brmon\b|openview|open.?view|"
           r"unicenter|tivoli|element.?management|fault.?management|enterprise.?management|"
           r"\bcmip\b|network.?monitor|\bnms\b|service.?management|\bitil\b|patrol|"
           r"spectrum|netcool|micromuse")
# management-SPECIFIC vendor/product entities (exclude generic ibm/hp/sun rows)
ENT_RE = (r"tivoli|openview|open.?view|micromuse|concord.?communications|netscout|\bbmc\b|"
          r"\bnetiq\b|cabletron|\bwellfleet\b|synoptics|bay.?networks|computer.?associates|"
          r"\bca\b.?unicenter|remedy|peregrine|manageengine|solarwinds|smarts|aprisma|"
          r"loudcloud|opsware|riversoft|smarts|visionael")

con = duckdb.connect(DB, read_only=True)

def rows(sql, p=None): return con.execute(sql, p or []).fetchall()

# 1. resolve tech + entity ids
techs = rows("SELECT tech_id, tech_name, vendor, era, lifecycle_at_study, lifecycle_current, occurrence_count "
             "FROM v_technologies WHERE regexp_matches(lower(tech_name||' '||tech_id), ?) ORDER BY occurrence_count DESC", [TECH_RE])
ents = rows("SELECT entity_id, entity_name, entity_type, sector, occurrence_count "
            "FROM v_entities WHERE regexp_matches(lower(entity_name||' '||entity_id), ?) ORDER BY occurrence_count DESC", [ENT_RE])
tech_ids = [t[0] for t in techs]
ent_ids  = [e[0] for e in ents]

pe = ",".join(["?"]*len(ent_ids)) or "NULL"
pt = ",".join(["?"]*len(tech_ids)) or "NULL"
touch_filter = f"(o.entity_id IN ({pe}) OR o.tech_id IN ({pt}))"
params = ent_ids + tech_ids

# 2. touching studies with metadata
studies = rows(
  f"SELECT DISTINCT s.study_id, s.title, s.pub_year, s.type, s.author, "
  f"       s.study_prescience_enum, s.prescience_mean, "
  f"       (SELECT COUNT(*) FROM v_observations o2 WHERE o2.study_id=s.study_id AND {touch_filter.replace('o.','o2.')}) AS rel_obs "
  f"FROM v_studies s JOIN v_observations o USING(study_id) WHERE {touch_filter} "
  f"ORDER BY rel_obs DESC, s.pub_year", params+params)

# 3. observations (the evidence spine) — datable, with entity/tech, ordered by year
obs = rows(
  f"SELECT o.obs_id, o.study_id, o.entity_id, o.tech_id, o.year_observed, "
  f"       o.observation_type, o.metric_name, o.metric_value, o.confidence "
  f"FROM v_observations o WHERE {touch_filter} "
  f"ORDER BY TRY_CAST(o.year_observed AS INT) NULLS LAST, o.study_id", params)

# 4. prescience layer
presc = rows(
  f"SELECT o.obs_id, o.study_id, o.year_observed, o.metric_name, o.metric_value, "
  f"       p.prescience_score, p.rationale "
  f"FROM v_observations o JOIN v_prescience_raw p USING(obs_id) WHERE {touch_filter} "
  f"AND TRY_CAST(p.prescience_score AS INT) >= 4 ORDER BY TRY_CAST(p.prescience_score AS INT) DESC", params)

# 5. year histogram
yr = rows(
  f"SELECT TRY_CAST(o.year_observed AS INT) AS y, COUNT(*) n FROM v_observations o "
  f"WHERE {touch_filter} AND TRY_CAST(o.year_observed AS INT) BETWEEN 1980 AND 2026 "
  f"GROUP BY y ORDER BY y", params)

con.close()

def pack(rws, cols): return [dict(zip(cols, r)) for r in rws]
out = {
 "topic": "Network / Systems Management",
 "technologies": pack(techs, ["tech_id","tech_name","vendor","era","lifecycle_at_study","lifecycle_current","occ"]),
 "entities": pack(ents, ["entity_id","entity_name","entity_type","sector","occ"]),
 "studies": pack(studies, ["study_id","title","pub_year","type","author","presc_enum","presc_mean","rel_obs"]),
 "observations": pack(obs, ["obs_id","study_id","entity_id","tech_id","year","obs_type","metric_name","metric_value","confidence"]),
 "high_prescience": pack(presc, ["obs_id","study_id","year","metric_name","metric_value","score","rationale"]),
 "year_hist": pack(yr, ["year","n"]),
}
OUT.write_text(json.dumps(out, indent=2, default=str))
print("WROTE", OUT)
print(f"techs={len(techs)} entities={len(ents)} studies={len(studies)} obs={len(obs)} high_presc_obs={len(presc)}")
print("top techs:", [t[0] for t in techs[:10]])
print("top ents :", [e[0] for e in ents[:10]])
print("top studies (by rel_obs):")
for s in studies[:12]:
    print(f"  {s[7]:>3} obs | {s[2]} | {s[5]:8s} | {s[0]}  {s[1][:55]}")
