# Wiki v1.5 Rebuild Runbook (v1)

**Author**: PSK + Computer
**Date**: 2026-05-26
**Target**: Regenerate `~/Desktop/kastner_wiki/` from v1.5 masters
  (8 master CSVs including `_master_prescience_scores.csv`)

This is a **one-time, end-to-end rebuild**. It assumes Pass C has completed
and the prescience master has been rolled up.

---

## 0. Preconditions

Run on the **Mac** (`scott`), not the sandbox. All paths absolute.

| Check | Command | Expected |
|---|---|---|
| Pass C done | `ps aux \| grep run_prescience \| grep -v grep` | (empty) |
| Prescience master exists | `ls -la ~/Desktop/Archive/archive_masters/_master_prescience_scores.csv` | file present, ~2,723 rows |
| 8 masters in place | `ls ~/Desktop/Archive/archive_masters/_master_*.csv \| wc -l` | 8 |
| Ollama running | `curl -s localhost:11434/api/tags \| jq '.models[].name'` | qwen3.5:27b-mlx, nomic-embed-text |
| `pplx` CLI works | `pplx --help` | help text |
| Build scripts pulled | `ls ~/Desktop/Archive/aberdeen-group-archive/scripts/build/*.py \| wc -l` | 7 |

If any check fails, **halt** and resolve before continuing.

---

## 1. Pull the build scripts

```bash
cd /Users/scott/Desktop/Archive/aberdeen-group-archive
git pull
cp -v scripts/build/*.py /Users/scott/Desktop/Archive/scripts/
ls /Users/scott/Desktop/Archive/scripts/0*.py /Users/scott/Desktop/Archive/scripts/_llm_helper_v1.py
```

You should see all 7 scripts in `/Users/scott/Desktop/Archive/scripts/`.

---

## 2. Pass C roll-up (if not already done)

```bash
cd /Users/scott/Desktop/Archive
python3 scripts/roll_up_prescience_to_master_v1.py \
  --root /Users/scott/Desktop/Archive/prepared \
  --out /Users/scott/Desktop/Archive/archive_masters/_master_prescience_scores.csv
```

Expect ~2,723 rows + header. Verify:

```bash
wc -l ~/Desktop/Archive/archive_masters/_master_prescience_scores.csv
head -2 ~/Desktop/Archive/archive_masters/_master_prescience_scores.csv
```

---

## 3. Backup the existing wiki (safety net)

```bash
cd ~/Desktop
TS=$(date -u +%Y%m%dT%H%M%SZ)
tar czf kastner_wiki_pre_v1.5_${TS}.tar.gz kastner_wiki/
ls -lh kastner_wiki_pre_v1.5_${TS}.tar.gz
```

Then either rename or wipe the existing wiki target:

```bash
mv ~/Desktop/kastner_wiki ~/Desktop/kastner_wiki_v1.4_archived
mkdir -p ~/Desktop/kastner_wiki
```

---

## 4. Run phases 1-6

Each phase is independently re-runnable. If a phase fails, fix the underlying
issue and re-run **only that phase**.

### Phase 1 — Load and validate CSVs

```bash
cd /Users/scott/Desktop/Archive
python3 scripts/01_load_csvs_v1.py \
  --archive ~/Desktop/Archive/archive_masters \
  --output ~/Desktop/kastner_wiki
```

Expected: `~/Desktop/kastner_wiki/staging/*.parquet` written, prescience joined.

### Phase 2 — Data layer (DuckDB + Parquet)

```bash
python3 scripts/02_build_data_layer_v1.py \
  --output ~/Desktop/kastner_wiki
```

Expected: `data/*.parquet` promoted, `db/kastner.duckdb` built with ~18 views.

Spot-check:

```bash
duckdb ~/Desktop/kastner_wiki/db/kastner.duckdb \
  "SELECT COUNT(*) FROM v_studies_with_prescience;"
duckdb ~/Desktop/kastner_wiki/db/kastner.duckdb \
  "SELECT * FROM v_top_prescient_studies LIMIT 5;"
```

### Phase 3 — Vault generation (longest phase)

This is where the hybrid LLM kicks in. Ollama and `pplx` must both be live.

```bash
python3 scripts/03_generate_vault_v1.py \
  --output ~/Desktop/kastner_wiki \
  --tier1-limit 420
```

Expected: ~8,500 pages in `wiki/`. Tier-1 ~420 LLM-summarized; rest templated.

Mid-run monitoring (separate terminal):

```bash
find ~/Desktop/kastner_wiki/wiki -name '*.md' | wc -l
tail -f ~/Desktop/kastner_wiki/build_manifest.jsonl
```

### Phase 4 — Indices, decades, collections, bases

```bash
python3 scripts/04_generate_indices_v1.py \
  --output ~/Desktop/kastner_wiki
```

Expected: `_index.md`, `_prescient.md`, decades/, collections/, bases/*.base.

### Phase 5 — Embeddings (nomic-embed via Ollama)

```bash
python3 scripts/05_compute_embeddings_v1.py \
  --output ~/Desktop/kastner_wiki
```

Expected: `data/embeddings.parquet` ~8,500 rows × 768-dim vectors.

### Phase 6 — Scaffolding (README, AGENTS, Makefile, verify.py)

```bash
python3 scripts/06_emit_scaffolding_v1.py \
  --output ~/Desktop/kastner_wiki
```

Expected: `README.md`, `AGENTS.md`, `chat-starter.md`, `Makefile`,
`scripts/verify.py`, `scripts/semantic_search.py`, `build_manifest.json`.

---

## 5. Verify

```bash
cd ~/Desktop/kastner_wiki
python3 scripts/verify.py
```

Expected green output. Any red line → halt and investigate.

Also browse the vault in Obsidian:

```bash
open -a Obsidian ~/Desktop/kastner_wiki/wiki
```

Spot-check: `_index.md`, `_prescient.md`, a Volume 1 chapter, top-3 entities.

---

## 6. Push the wiki repo

Once verify is green and Obsidian looks right:

```bash
cd ~/Desktop/kastner_wiki
git init  # idempotent
git add -A
git commit -m "Wiki v1.5 — prescience-aware rebuild from 8 masters"
git remote add origin git@github.com:shorttack/kastner-aberdeen-wiki.git 2>/dev/null || true
git push -u origin main --force  # one-time build replaces v1.4
```

---

## 7. Makefile shortcuts (after Phase 6 writes it)

```bash
cd ~/Desktop/kastner_wiki
make rebuild      # phases 1-6 sequentially
make verify       # run verify.py
make duckdb       # rebuild db/kastner.duckdb only
make embeddings   # rebuild data/embeddings.parquet only
```

---

## 8. Rollback

If anything is wrong post-push:

```bash
rm -rf ~/Desktop/kastner_wiki
tar xzf ~/Desktop/kastner_wiki_pre_v1.5_*.tar.gz -C ~/Desktop/
```

And revert the wiki repo:

```bash
cd ~/Desktop/kastner-aberdeen-wiki  # if you have a clone there
git reset --hard v1.4-tag  # if v1.4 was tagged
git push -f
```

---

## Notes on hybrid LLM routing

`_llm_helper_v1.py` routes by `page_type`:

| page_type | Backend | Model |
|---|---|---|
| entity, technology | Local | Ollama `qwen3.5:27b-mlx` |
| study, volume-1, collection | Cloud | `pplx ask --model claude_sonnet_4_6` |

Local options: `temperature=0.3, num_ctx=8192, num_predict=600, think=False,
keep_alive=30m`. Two retries with exponential backoff. Any failure falls back
to the templated long-tail page (no halt).

Estimated tier-1 wall time: ~3-4 hours total (200 entities + 150 techs locally
~2-3 hr; 70 studies + 14 Volume 1 + 6 collections via cloud ~30-45 min).

---

## Counts at-a-glance (expected after v1.5 build)

| Artifact | Expected count |
|---|---:|
| `wiki/studies/*.md` | ~933 |
| `wiki/entities/*.md` | ~3,299 |
| `wiki/technologies/*.md` | ~4,283 |
| `wiki/volume-1/*.md` | 14 |
| `wiki/collections/*.md` | 6 |
| `wiki/decades/*.md` | 6 |
| Tier-1 LLM pages total | ~420 |
| `data/embeddings.parquet` rows | ~8,500 |
| DuckDB views | ~18 |
| `_master_prescience_scores.csv` rows | ~2,723 |
