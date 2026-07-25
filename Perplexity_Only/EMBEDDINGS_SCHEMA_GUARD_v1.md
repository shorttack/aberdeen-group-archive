# Embeddings Schema Guard — patch snippet + `kw verify` wiring

Companion to `scripts/verify_embeddings_schema_v1.py` (standalone checker, lives in
this archive repo). This doc exists because `kw_ask.py` and the `kw verify` launcher
live in the **wiki repo** (`shorttack/kastner-aberdeen-wiki`), not this one, so the
AUTO batch cannot edit them directly — Pete applies the snippets below on the Mac.

## Why this exists (Gotcha 9)

`05_compute_embeddings_v2.py` once emitted a 4-column schema
`(path, slug, embedding, dim)` when the canonical contract is 6 columns:

```
(page_path, page_type, slug, title, vector, dim)
```

`kw_ask.py` read the 6-column contract, crashed with a raw duckdb `BinderException`
on first live query, and the drift sat invisible until then. `05_compute_embeddings_v3.py`
fixed the producer side. This doc adds defense on the consumer side so a future
regression fails loudly and readably instead of crashing raw.

Three layers of defense (per the L273/274/275 worklist trio):
1. **Standalone script** `scripts/verify_embeddings_schema_v1.py` (this repo) — run manually or in CI-like checks.
2. **Mirror assertion inside `kw_ask.py`** (this doc, §1 below — apply on the Mac).
3. **`kw verify` launcher wiring** (this doc, §2 below — apply on the Mac).

---

## §1. Patch snippet for `kw_ask.py`

**Target file:** `~/Repos/kastner-aberdeen-wiki/scripts/kw_ask.py`
**Placement:** immediately after the embeddings parquet is loaded, before any query
runs against it. Per `Perplexity_Only/KW_ASK_FIX.md`, `kw_ask.py` imports `duckdb`
near line 30 and loads the embeddings shortly after — locate the line that reads
`embeddings.parquet` (search for `embeddings.parquet` or the `read_parquet(` call
against the embeddings path) and insert the assertion **right after** that load,
before the retrieval/query logic executes.

```python
# --- BEGIN schema guard (added per EMBEDDINGS_SCHEMA_GUARD_v1.md) ---
_EXPECTED_EMBEDDING_COLUMNS = {"page_path", "page_type", "slug", "title", "vector", "dim"}

def _assert_embeddings_schema(con, embeddings_parquet_path):
    """Fail fast and readably if the embeddings parquet schema has drifted.

    See Gotcha 9 in the kastner-archive-pipeline skill: a past producer bug
    shipped a 4-column schema that crashed retrieval with a raw BinderException.
    This turns that into a clear, actionable error instead.
    """
    cols = {
        r[0]
        for r in con.execute(
            "DESCRIBE SELECT * FROM read_parquet(?)", [str(embeddings_parquet_path)]
        ).fetchall()
    }
    missing = _EXPECTED_EMBEDDING_COLUMNS - cols
    unexpected = cols - _EXPECTED_EMBEDDING_COLUMNS
    if missing or unexpected:
        msg = [
            f"kw_ask: embeddings.parquet schema mismatch at {embeddings_parquet_path}",
            f"  expected: {sorted(_EXPECTED_EMBEDDING_COLUMNS)}",
            f"  actual:   {sorted(cols)}",
        ]
        if missing:
            msg.append(f"  MISSING: {sorted(missing)}")
        if unexpected:
            msg.append(f"  UNEXPECTED: {sorted(unexpected)}")
        msg.append(
            "  Likely cause: 05_compute_embeddings_*.py producer schema drift "
            "(Gotcha 9). Re-run Phase 5, or run "
            "scripts/verify_embeddings_schema_v1.py from the archive repo for a "
            "standalone diagnosis."
        )
        raise SystemExit("\n".join(msg))
# --- END schema guard ---
```

And the call site (drop this line right after the embeddings parquet path is known,
before it's queried):

```python
_assert_embeddings_schema(con, embeddings_parquet_path)
```

Adjust variable names (`con`, `embeddings_parquet_path`) to match whatever `kw_ask.py`
actually calls its duckdb connection and embeddings path variables — this is a
snippet to adapt, not a blind literal replacement, per the runbook's instruction not
to rewrite the whole file unseen.

---

## §2. `kw verify` launcher wiring

**Target file:** `~/Repos/kastner-aberdeen-wiki/bin/kw` (the launcher shim; per
`Perplexity_Only/KW_ASK_FIX.md` and `USER_GUIDE.md` §3, `kw` is the dispatcher and
`scripts/kw_ask.py` is the Python core). `kw verify` is the subcommand that currently
checks "the build is intact" (see `USER_GUIDE.md` §3: `# Verify the build is intact`).

Add the schema check as one more step in that verify path so a stale/drifted
embeddings file is caught by `kw verify` *before* anyone runs `kw ask` and hits a
raw crash.

If `bin/kw`'s `verify` case shells out to a Python verify script already, add a line
calling the new standalone checker:

```bash
# inside the `verify)` case of bin/kw, alongside the existing build-integrity checks
echo "Checking embeddings schema..."
python3 "${KW_ROOT:-$HOME/Repos/kastner-aberdeen-wiki}/../aberdeen-group-archive/scripts/verify_embeddings_schema_v1.py" \
  --wiki "${KW_ROOT:-$HOME/Repos/kastner-aberdeen-wiki}" \
  || { echo "kw verify: embeddings schema check FAILED (see above)"; exit 1; }
```

If `bin/kw`'s `verify` case is itself a small inline Python block rather than a
shell dispatch, the equivalent addition is to import and call the same assertion
used in §1 (`_assert_embeddings_schema`), or simply invoke
`verify_embeddings_schema_v1.py` as a subprocess and propagate its exit code:

```python
import subprocess, sys

result = subprocess.run(
    ["python3", str(archive_scripts_dir / "verify_embeddings_schema_v1.py"),
     "--wiki", str(wiki_root)],
)
if result.returncode != 0:
    print("kw verify: embeddings schema check FAILED")
    sys.exit(1)
```

**Note on repo boundary:** `verify_embeddings_schema_v1.py` lives in the
**archive repo** (`scripts/verify_embeddings_schema_v1.py`), not the wiki repo, so
the path Pete wires into `bin/kw` needs to point across repos — e.g. both cloned as
siblings under `~/Repos/`, or Pete copies the script into the wiki repo's own
`scripts/` directory if he'd rather keep `kw verify` self-contained. Either placement
works; pick whichever matches how `bin/kw` resolves its own script paths today.

---

## Acceptance checklist (for Pete, once applied on the Mac)

- [ ] `kw_ask.py` raises a clear `SystemExit` message (not a raw BinderException) if
      the embeddings schema drifts.
- [ ] `kw verify` fails loudly if the embeddings schema drifts, before any `kw ask`
      call would hit it.
- [ ] `python3 scripts/verify_embeddings_schema_v1.py` (this repo) still works
      standalone as a third, independent check.

## Source

- Worklist items L273 (script), L274 (kw_ask.py mirror), L275 (kw verify wiring),
  processed as part of the 2026-07-25/26 overnight AUTO batch.
- Gotcha 9, `kastner-archive-pipeline` skill (schema drift failure mode).
- `Perplexity_Only/KW_ASK_FIX.md` (kw_ask.py / bin/kw layout reference).
