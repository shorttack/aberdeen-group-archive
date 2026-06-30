#!/usr/bin/env python3
"""
promote_l7_access_journeys_v1.py

L7 PROMOTION — replace the 122-row legacy monthly-average aggregation of the
DCT Access PC Deals study with the 249 model-extracted per-SKU price journeys,
stripping the `-mx` suffix so the canonical study_id keeps its identity.

This is the deferred L7 promotion proven in the 2026-06-27 smoke test. The
staged package (validated, byte-identical to the sandbox copy) lives at:
    ~/Desktop/Archive/Perplexity_Only/expand_pc_deals_smoke/mx_out/
        dct-access-pc-deals-2002-2003-mx/data/{observations,entities,
        technologies,studies}.csv

CANONICAL MASTERS (repo root — archive_masters/ is RETIRED, never touch it):
    ~/Desktop/Archive/aberdeen-group-archive/_master_*.csv

WHAT THIS SCRIPT DOES (4 masters, no prescience layer involved — the access
study is prescience=not-applicable, pure market-data):

  1. _master_observations.csv (17 col)
       - DELETE the 122 legacy rows  study_id == dct-access-pc-deals-2002-2003
       - INSERT 249 journey rows, re-keyed from the -mx package:
           study_id : strip "-mx"   -> dct-access-pc-deals-2002-2003
           obs_id   : strip "-mx"   -> dct-access-pc-deals-2002-2003-OBS-NNN
         mapping the staged 12-col schema into the canonical 17-col schema.

  2. _master_entity_studies.csv (2 col: entity_id, study_id)
       - ADD missing entity links for the 16 journey entities (legacy had 10).
         All 16 entity_ids already exist in the global _master_entities.csv.

  3. _master_tech_studies.csv (2 col: tech_id, study_id)
       - ADD missing tech links for the 9 journey technologies (legacy had 1).
         All 9 tech_ids already exist in the global _master_technologies.csv.
         This is the FK-density win: 1 -> 9 tech links.

  4. _master_studies.csv (16 col)
       - UPDATE the access study row's `methodology`, `source_file`, `abstract`,
         `importance_rationale`, `relevance_rationale` to the upgraded -mx text.
         study_id, type, prescience (=not-applicable), prescience_rationale
         are PRESERVED (the canonical identity + verdict do not change).

INVARIANTS (Pete's standing rules):
  - Dry-run is default; --commit is opt-in.
  - Backup every touched master BEFORE writing:
        <file>.csv.bak_promote_l7_access_<utc-stamp>Z
  - csv.QUOTE_ALL on every write.
  - Read back + assert column counts and row deltas after every write.
  - No new entity/tech rows are created (all already canonical) — verified
    defensively; the script ABORTS if any journey entity_id/tech_id is not
    found in the global tables.

EXPECTED DELTAS (dry-run will print these; --commit asserts them):
  observations   : -122 legacy +249 journeys  (net +127 for this study)
  entity_studies : +6   (10 -> 16)
  tech_studies   : +8   (1  -> 9)
  studies        : 0 row delta (1 row updated in place)
"""

import csv
import shutil
import sys
import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO = Path.home() / "Desktop/Archive/aberdeen-group-archive"
PKG  = (Path.home() /
        "Desktop/Archive/Perplexity_Only/expand_pc_deals_smoke/"
        "mx_out/dct-access-pc-deals-2002-2003-mx/data")

CANON_SID = "dct-access-pc-deals-2002-2003"
MX_SID    = "dct-access-pc-deals-2002-2003-mx"

M_OBS   = REPO / "_master_observations.csv"
M_ENTJ  = REPO / "_master_entity_studies.csv"
M_TECHJ = REPO / "_master_tech_studies.csv"
M_STUD  = REPO / "_master_studies.csv"
M_ENT   = REPO / "_master_entities.csv"
M_TECH  = REPO / "_master_technologies.csv"

P_OBS  = PKG / "observations.csv"
P_ENT  = PKG / "entities.csv"
P_TECH = PKG / "technologies.csv"
P_STUD = PKG / "studies.csv"

# Canonical 17-col observations header (source of truth: live master)
OBS_COLS = [
    "obs_id", "study_id", "entity_id", "tech_id", "observation_type",
    "year_observed", "metric_name", "metric_value", "confidence",
    "verification_method", "methodology_code", "source_page", "notes",
    "collection", "thread_tag", "section", "legacy_obs_id",
]

COMMIT = "--commit" in sys.argv
TS = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")


def die(msg):
    sys.exit(f"ABORT: {msg}")


def read_csv(path):
    with open(path, newline="") as f:
        r = csv.reader(f)
        header = next(r)
        rows = list(r)
    return header, rows


def read_dicts(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path, header, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        w.writerows(rows)


def backup(path):
    bak = path.with_suffix(f".csv.bak_promote_l7_access_{TS}")
    shutil.copy2(path, bak)
    return bak


def banner(t):
    print("\n" + "=" * 70)
    print(t)
    print("=" * 70)


# ---------------------------------------------------------------------------
# Pre-flight
# ---------------------------------------------------------------------------
banner(f"L7 ACCESS PROMOTION  —  mode: {'COMMIT' if COMMIT else 'DRY-RUN'}  —  {TS}")

for p in (REPO, PKG, M_OBS, M_ENTJ, M_TECHJ, M_STUD, M_ENT, M_TECH,
          P_OBS, P_ENT, P_TECH, P_STUD):
    if not p.exists():
        die(f"required path missing: {p}")

# Guard against the retired archive_masters path sneaking in
if "archive_masters" in str(REPO) and "aberdeen-group-archive" not in str(REPO):
    die("REPO points at the RETIRED archive_masters dir")

# ---------------------------------------------------------------------------
# Load global canonical entity/tech ids (defensive: journeys must reference
# only ids that already exist; this promotion creates NO new entity/tech rows)
# ---------------------------------------------------------------------------
global_ent = {r["entity_id"] for r in read_dicts(M_ENT)}
global_tech = {r["tech_id"] for r in read_dicts(M_TECH)}

pkg_obs = read_dicts(P_OBS)
if len(pkg_obs) != 249:
    die(f"staged package has {len(pkg_obs)} obs, expected 249")

pkg_ent_ids = sorted({r["entity_id"] for r in pkg_obs if r["entity_id"]})
pkg_tech_ids = sorted({r["tech_id"] for r in pkg_obs if r["tech_id"]})

missing_ent = [e for e in pkg_ent_ids if e not in global_ent]
missing_tech = [t for t in pkg_tech_ids if t not in global_tech]
if missing_ent:
    die(f"journey entity_ids missing from global _master_entities.csv: {missing_ent}")
if missing_tech:
    die(f"journey tech_ids missing from global _master_technologies.csv: {missing_tech}")

print(f"journey distinct entity_ids: {len(pkg_ent_ids)} (all canonical) -> {pkg_ent_ids}")
print(f"journey distinct tech_ids  : {len(pkg_tech_ids)} (all canonical) -> {pkg_tech_ids}")

# obs_id uniqueness + FK within package
pkg_obs_ids = [r["obs_id"] for r in pkg_obs]
if len(set(pkg_obs_ids)) != len(pkg_obs_ids):
    die("duplicate obs_id in staged package")
for r in pkg_obs:
    if r["entity_id"] and r["entity_id"] not in pkg_ent_ids:
        die(f"package-internal entity FK break: {r['obs_id']}")
    if r["tech_id"] and r["tech_id"] not in pkg_tech_ids:
        die(f"package-internal tech FK break: {r['obs_id']}")

# ---------------------------------------------------------------------------
# 1. OBSERVATIONS  — delete 122 legacy, insert 249 journeys (12 -> 17 col)
# ---------------------------------------------------------------------------
banner("1) _master_observations.csv")
obs_header, obs_rows = read_csv(M_OBS)
if obs_header != OBS_COLS:
    die(f"observations header mismatch.\n got: {obs_header}\n exp: {OBS_COLS}")

oidx = {c: i for i, c in enumerate(obs_header)}
legacy_obs = [r for r in obs_rows if r[oidx["study_id"]] == CANON_SID]
existing_mx = [r for r in obs_rows if r[oidx["study_id"]] == MX_SID]
print(f"legacy access obs found : {len(legacy_obs)} (expected 122)")
print(f"existing -mx access obs : {len(existing_mx)} (expected 0)")
if len(legacy_obs) != 122:
    die(f"expected 122 legacy access obs, found {len(legacy_obs)}")
if existing_mx:
    die(f"unexpected {len(existing_mx)} -mx access obs already in master; "
        "this promotion assumes a clean first promotion")

# Build the 249 canonical journey rows (17-col), re-keyed (strip -mx)
def mx_to_canon(s):
    return s.replace(MX_SID, CANON_SID)

new_obs_rows = []
seen_obs_ids = set()
for r in pkg_obs:
    obs_id = mx_to_canon(r["obs_id"])
    if not obs_id.startswith(CANON_SID + "-OBS-"):
        die(f"unexpected obs_id after re-key: {obs_id}")
    if obs_id in seen_obs_ids:
        die(f"duplicate re-keyed obs_id: {obs_id}")
    seen_obs_ids.add(obs_id)
    row = {
        "obs_id": obs_id,
        "study_id": CANON_SID,
        "entity_id": r["entity_id"],
        "tech_id": r["tech_id"],
        "observation_type": r["observation_type"],   # market-data
        "year_observed": r["year_observed"],
        "metric_name": r["metric_name"],
        "metric_value": r["metric_value"],
        "confidence": r["confidence"],                # high
        "verification_method": "ingest-extraction",   # matches legacy convention
        "methodology_code": r.get("methodology_code", "market-tracking") or "market-tracking",
        "source_page": r["source_page"],
        "notes": r["notes"],
        "collection": "",                              # match legacy (empty)
        "thread_tag": "",
        "section": "",
        "legacy_obs_id": "",                           # new model-extracted, no legacy counterpart
    }
    new_obs_rows.append([row[c] for c in OBS_COLS])

# new master obs = (all rows except the 122 legacy) + 249 journeys
kept = [r for r in obs_rows if r[oidx["study_id"]] != CANON_SID]
final_obs = kept + new_obs_rows
print(f"master obs before        : {len(obs_rows)}")
print(f"  - removed legacy        : {len(legacy_obs)}")
print(f"  + inserted journeys     : {len(new_obs_rows)}")
print(f"master obs after          : {len(final_obs)}  (net {len(final_obs)-len(obs_rows):+d})")
assert len(final_obs) == len(obs_rows) - 122 + 249

# ---------------------------------------------------------------------------
# 2. ENTITY_STUDIES  — add missing links (10 -> 16)
# ---------------------------------------------------------------------------
banner("2) _master_entity_studies.csv")
ej_header, ej_rows = read_csv(M_ENTJ)
if ej_header != ["entity_id", "study_id"]:
    die(f"entity_studies header mismatch: {ej_header}")
existing_ej = {(r[0], r[1]) for r in ej_rows}
legacy_ej = sorted(e for (e, s) in existing_ej if s == CANON_SID)
print(f"legacy entity links: {len(legacy_ej)} -> {legacy_ej}")
add_ej = [[e, CANON_SID] for e in pkg_ent_ids if (e, CANON_SID) not in existing_ej]
print(f"adding {len(add_ej)} entity links (expected 6): {[r[0] for r in add_ej]}")
final_ej = ej_rows + add_ej
print(f"entity_studies before/after: {len(ej_rows)} -> {len(final_ej)} (net {len(add_ej):+d})")

# ---------------------------------------------------------------------------
# 3. TECH_STUDIES  — add missing links (1 -> 9)
# ---------------------------------------------------------------------------
banner("3) _master_tech_studies.csv")
tj_header, tj_rows = read_csv(M_TECHJ)
if tj_header != ["tech_id", "study_id"]:
    die(f"tech_studies header mismatch: {tj_header}")
existing_tj = {(r[0], r[1]) for r in tj_rows}
legacy_tj = sorted(t for (t, s) in existing_tj if s == CANON_SID)
print(f"legacy tech links: {len(legacy_tj)} -> {legacy_tj}")
add_tj = [[t, CANON_SID] for t in pkg_tech_ids if (t, CANON_SID) not in existing_tj]
print(f"adding {len(add_tj)} tech links (expected 8): {[r[0] for r in add_tj]}")
final_tj = tj_rows + add_tj
print(f"tech_studies before/after: {len(tj_rows)} -> {len(final_tj)} (net {len(add_tj):+d})")

# ---------------------------------------------------------------------------
# 4. STUDIES  — update the access study row in place (preserve identity+verdict)
# ---------------------------------------------------------------------------
banner("4) _master_studies.csv")
st_header, st_rows = read_csv(M_STUD)
sidx = {c: i for i, c in enumerate(st_header)}
pkg_study = read_dicts(P_STUD)[0]   # the -mx study row

target_idx = [i for i, r in enumerate(st_rows) if r[sidx["study_id"]] == CANON_SID]
if len(target_idx) != 1:
    die(f"expected exactly 1 access study row, found {len(target_idx)}")
ti = target_idx[0]
before = list(st_rows[ti])

# Fields we refresh from the -mx package (content upgrade).
# Identity + verdict fields are intentionally NOT touched.
UPDATE_FIELDS = ["methodology", "source_file", "abstract",
                 "importance", "importance_rationale",
                 "relevance", "relevance_rationale"]
for fld in UPDATE_FIELDS:
    if fld in pkg_study and fld in sidx:
        st_rows[ti][sidx[fld]] = pkg_study[fld]

# Hard-preserve identity + verdict
assert st_rows[ti][sidx["study_id"]] == CANON_SID
st_rows[ti][sidx["study_id"]] = CANON_SID            # never the -mx id
if "prescience" in sidx:
    st_rows[ti][sidx["prescience"]] = before[sidx["prescience"]]
if "prescience_rationale" in sidx:
    st_rows[ti][sidx["prescience_rationale"]] = before[sidx["prescience_rationale"]]
if "type" in sidx:
    st_rows[ti][sidx["type"]] = before[sidx["type"]]

changed = [st_header[i] for i in range(len(st_header))
           if st_rows[ti][i] != before[i]]
print(f"study row updated in place; changed fields: {changed}")
print(f"  prescience preserved: {st_rows[ti][sidx['prescience']]!r}")
print(f"studies row count: {len(st_rows)} (unchanged)")

# ---------------------------------------------------------------------------
# Commit or dry-run
# ---------------------------------------------------------------------------
banner("SUMMARY")
print(f"observations  : {len(obs_rows)} -> {len(final_obs)}   (net {len(final_obs)-len(obs_rows):+d}; -122 legacy +249 journeys)")
print(f"entity_studies: {len(ej_rows)} -> {len(final_ej)}   (net {len(add_ej):+d})")
print(f"tech_studies  : {len(tj_rows)} -> {len(final_tj)}   (net {len(add_tj):+d})")
print(f"studies       : {len(st_rows)} (1 row updated in place)")

if not COMMIT:
    print("\nDRY-RUN only — no files written. Re-run with --commit to apply.")
    sys.exit(0)

# --- backups ---
banner("BACKUPS")
for p in (M_OBS, M_ENTJ, M_TECHJ, M_STUD):
    print("backup:", backup(p))

# --- writes ---
banner("WRITES")
write_csv(M_OBS, OBS_COLS, final_obs)
write_csv(M_ENTJ, ej_header, final_ej)
write_csv(M_TECHJ, tj_header, final_tj)
write_csv(M_STUD, st_header, st_rows)

# --- read-back assertions ---
banner("READ-BACK VERIFICATION")
h, rb = read_csv(M_OBS)
assert h == OBS_COLS, "obs header changed on read-back"
canon_after = [r for r in rb if r[oidx["study_id"]] == CANON_SID]
mx_after = [r for r in rb if r[oidx["study_id"]] == MX_SID]
print(f"obs: total {len(rb)}, access(canon) {len(canon_after)} (expect 249), access(-mx) {len(mx_after)} (expect 0)")
assert len(canon_after) == 249 and len(mx_after) == 0 and len(rb) == len(final_obs)

h, rb = read_csv(M_ENTJ)
assert h == ["entity_id", "study_id"]
print(f"entity_studies: {len(rb)} (expect {len(final_ej)}); access links {sum(1 for r in rb if r[1]==CANON_SID)} (expect 16)")
assert sum(1 for r in rb if r[1] == CANON_SID) == 16 and len(rb) == len(final_ej)

h, rb = read_csv(M_TECHJ)
assert h == ["tech_id", "study_id"]
print(f"tech_studies: {len(rb)} (expect {len(final_tj)}); access links {sum(1 for r in rb if r[1]==CANON_SID)} (expect 9)")
assert sum(1 for r in rb if r[1] == CANON_SID) == 9 and len(rb) == len(final_tj)

h, rb = read_csv(M_STUD)
acc = [r for r in rb if r[sidx["study_id"]] == CANON_SID]
print(f"studies: {len(rb)}; access rows {len(acc)} (expect 1); prescience {acc[0][sidx['prescience']]!r}")
assert len(acc) == 1 and len(rb) == len(st_rows)

print("\nAll read-back assertions PASSED. L7 promotion committed.")
print("NEXT: run Phase 1 + Phase 2 to rebuild the DuckDB, then Phases 3-6 "
      "(wiki pages/indices/re-embed/scaffolding). Shape audit before & after.")
