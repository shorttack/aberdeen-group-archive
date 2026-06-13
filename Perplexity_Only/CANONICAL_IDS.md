# CANONICAL_IDS.md — Authoritative Entity & Technology ID Cache

> **READ THIS FILE before assigning any entity_id or tech_id during extraction.**
> Wrong IDs are the #1 cause of post-merge cleanup work. Every variant in
> the "Common mistakes" column has been seen in the wild and required a
> patch to either an apply script or the masters themselves.

**Last updated:** 2026-06-12 (§11u-cont Pass B Completion).
**Scope:** Entities and technologies that have appeared in 2+ studies or
that have been the subject of a canonicalization fix. New one-off IDs do
not belong here until they recur.

---

## Entities

| Common name | Canonical `entity_id` | Common mistakes (DO NOT USE) |
|---|---|---|
| Peter S. Kastner (author/analyst) | `peter-s-kastner` | `pete-kastner`, `peter-kastner`, `ent-pete-kastner` |
| Aberdeen Group | `aberdeen-group` | `aberdeen`, `aberdeen-research`, `ent-aberdeen` |
| Oracle Corporation | `oracle-corporation` | `oracle`, `oracle-corp`, `ent-oracle` |
| SAP AG | `sap-ag` | `sap`, `sap-se`, `ent-sap` |
| Sybase, Inc. | `sybase-inc` | `sybase`, `sybase-corporation`, `ent-sybase` |
| Sun Microsystems | `sun-microsystems` | `sun`, `sun-micro`, `ent-sun` |
| IBM | `ibm` | `international-business-machines`, `ent-ibm` |
| Tandem Computers | `tandem-computers` | `tandem`, `tandem-corp`, `ent-tandem` |
| Compaq Computer | `compaq-computer` | `compaq`, `compaq-corp`, `ent-compaq` |
| Informix Software | `informix-software` | `informix`, `informix-corp`, `ent-informix` |
| Ingres Corporation | `ingres-corporation` | `ingres`, `ingres-corp`, `ent-ingres` |
| Silicon Graphics | `silicon-graphics` | `sgi`, `silicon-graphics-inc`, `ent-sgi` |
| Microsoft Corporation | `microsoft-corporation` | `microsoft`, `msft`, `ent-microsoft` |
| Apple Computer | `apple-computer` | `apple`, `apple-inc`, `ent-apple` |
| Hewlett-Packard | `hewlett-packard` | `hp`, `hewlett-packard-co`, `ent-hp` |
| Digital Equipment Corporation | `dec` | `digital`, `digital-equipment`, `ent-dec` |
| America Online | `aol` | `america-online`, `aol-inc`, `ent-aol` |
| Crossroads Software | `crossroads-software` | `crossroads`, `crossroads-inc`, `ent-crossroads` |
| Vantive Corporation | `ent-vantive` | `vantive`, `vantive-corp`, `vantive-corporation` |
| United Parcel Service | `ups` | `united-parcel-service`, `ent-ups` |
| IDC (Intl. Data Corporation) | `idc` | `intl-data-corp`, `ent-idc` |
| AT&T | `ent-att` | **`att-corporation`** (caught 2026-06-12 §11u-cont, study 13), `att`, `american-telephone` |
| Illinois (state, gov entity) | `ENT-ILL-001` | `illinois`, `state-of-illinois`, `ent-illinois` |
| Various map providers | `ENT-MAP-001` | `mapping`, `gis-provider` |

### Entity ID format conventions

- Plain canonical names use bare slug: `oracle-corporation`, `aberdeen-group`.
- The `ent-` prefix is used when the bare slug would collide with a tech ID, or for short/ambiguous names (`ent-vantive`, `ent-att`, `ent-pete-kastner` is NOT used — Pete's canonical is the bare `peter-s-kastner`).
- The `ENT-XXX-NNN` uppercase numeric form is used for institutional/governmental entities that lack a clean slug (states, gov agencies, generic provider buckets).
- **DO NOT** invent new `ent-XXXX` IDs without checking the existing master first. Run:
  ```bash
  grep -i "<name-fragment>" ~/Desktop/Archive/archive_masters/_master_entities.csv
  ```

---

## Technologies

| Common name | Canonical `tech_id` | Common mistakes (DO NOT USE) |
|---|---|---|
| Enterprise Application Integration | `enterprise-application-integration-eai` | `eai`, `eai-integration` (caught earlier in §11u-cont), `ent-app-integration` |
| Sybase Replication Server | `SYBASE-REPSERVER` | `sybase-replication-server` (caught earlier in §11u-cont), `sybase-repserver` (case-sensitive!), `repserver` |
| PowerPC | `powerpc` | **`ibm-powerpc`** (caught 2026-06-12 §11u-cont, study 13), `power-pc`, `tech-powerpc` |
| OLTP (Online Transaction Processing) | `oltp` | `online-transaction-processing`, `on-line-tp`, `tech-oltp` |
| Data Warehousing | `data-warehousing` | `data-warehouse`, `dw`, `tech-data-warehousing` |
| TPC-C benchmark | `tpc-c` | `tpcc`, `tpc-benchmark-c`, `tech-tpc-c` |
| Massively Parallel Processing | `mpp` | `massively-parallel-processing`, `tech-mpp` |
| Client-Server | `client-server` | `client/server`, `client-server-architecture`, `tech-client-server` |
| Sybase System 11 | `sybase-system-11` | `sybase-11`, `system-11`, `tech-sybase-system-11` |
| Sybase Adaptive Server Enterprise | `sybase-ase` | `ase`, `adaptive-server`, `sybase-adaptive-server`, `tech-sybase-ase` |
| Sybase IQ | `sybase-iq` | `iq`, `sybase-iq-server`, `tech-sybase-iq` |

### Tech ID format conventions

- Bare slug for established names: `powerpc`, `oltp`, `data-warehousing`.
- **Uppercase form** (`SYBASE-REPSERVER`) appears for a handful of legacy IDs. The case is significant — DuckDB and the join tables treat IDs as case-sensitive strings.
- **Do not prefix** with vendor unless the vendor is part of the name (`sybase-system-11` yes; `ibm-powerpc` NO — PowerPC was an IBM/Apple/Motorola consortium, not solely IBM).
- The `tech-` prefix is **not standard** for technology IDs. Don't add it.

---

## Anti-pattern catalog (the variants that have actually bitten us)

This section exists to make wrong IDs greppable. If a future agent searches
for `att-corporation` or `ibm-powerpc` because that's what their LLM
suggested, this file should turn up.

| Wrong | Right | Caught in |
|---|---|---|
| `att-corporation` | `ent-att` | 2026-06-12 §11u-cont, study 13 (CNBC Tech Edge) |
| `ibm-powerpc` | `powerpc` | 2026-06-12 §11u-cont, study 13 (CNBC Tech Edge) |
| `vantive` | `ent-vantive` | 2026-06-12 §11u-cont (earlier in batch) |
| `eai-integration` | `enterprise-application-integration-eai` | 2026-06-12 §11u-cont (earlier in batch) |
| `sybase-replication-server` | `SYBASE-REPSERVER` | 2026-06-12 §11u-cont (earlier in batch) |
| `pete-kastner` | `peter-s-kastner` | Multiple prior sessions |
| `sgi` (alone) | `silicon-graphics` | Multiple prior sessions |
| `digital` (alone) | `dec` | Multiple prior sessions |

---

## Procedure: adding a new canonical ID

1. **Check first.** `grep -i "<name>" ~/Desktop/Archive/archive_masters/_master_entities.csv` (or technologies). If a canonical already exists, use it. If a near-variant exists, that's the canonical — propose a merge, don't add a duplicate.
2. **Choose the slug.** Lowercase, hyphen-separated, no vendor prefix unless the vendor name is part of the entity's common name. Use `ent-` prefix only if there is a slug collision with a tech ID.
3. **Add the row** to the master (8-col schema, no `study_id` — see `MASTERS_NOTES.md`).
4. **Add a row** to this file under the appropriate table with at least 1 anticipated "common mistake" variant. If no mistakes are anticipated, omit from CANONICAL_IDS — this file is for repeat-offender IDs only.
5. **Update `_master_entity_studies.csv`** or `_master_tech_studies.csv` with the M:N pair for this study.

---

## How to use this file at extraction time

The LLM (qwen3.5:27b-mlx in the current pipeline) does not know about
this file unless it is loaded into its context. Two patterns:

**Pattern A (preferred, used in `archival-ingest` v20 §11):** Pre-flight
the per-study cache by loading this file's content into the system prompt
as the "canonical ID cache". The model is then constrained to use only
canonical IDs (or to propose new ones explicitly).

**Pattern B (fallback, used in this session for spot fixes):** Run the
extraction, then run a post-extraction grep against this file's "wrong"
column and patch the per-study CSVs before merging. This is what we did
for `att-corporation` → `ent-att` and `ibm-powerpc` → `powerpc` in
§11u-cont study 13.

---

**Maintained by:** Pete Kastner + Perplexity Computer.
**Pairs with:** `MASTERS_NOTES.md` (schema), `PIPELINE_QUICKREF.md` (commands).
