# kw ask duckdb fix — diagnosis and options

## Diagnosis

**Root cause:** `/opt/homebrew/bin/python3` (Python 3.14) is missing the `duckdb` and `requests` modules that `kw_ask.py` needs.

**Why it worked before but broke:** the wiki repo's `requirements.txt` was written for Python 3.11 and pinned versions may never have been installed against the current Python 3.14 (Homebrew upgraded). Also — Homebrew's Python 3.14 is PEP 668 "externally managed", so a bare `pip install duckdb` refuses to run without either `--break-system-packages` or a venv.

**Missing modules** (as of 2026-07-08 probe):
- `duckdb` — REQUIRED by `kw_ask.py` (line 30)
- `requests` — REQUIRED by `kw_ask.py` for Ollama HTTP calls

**Present modules:** `pandas 3.0.3`, `numpy 2.4.6`.

**Not affected:** the Phase 1-6 pipeline scripts. They use `pandas` and the `duckdb` command-line binary (`/opt/homebrew/bin/duckdb`), not the Python `duckdb` module. Last night's overnight run proves this — Phase 1 v3 loaded 12 masters cleanly using pandas alone.

## Option A: quick fix — `--break-system-packages`

**One command.** Safe if you don't care that Homebrew Python is not strictly isolated. This is the same install pattern that `pandas` and `numpy` are already using on your Mac — they were installed globally at some point.

```bash
/opt/homebrew/bin/python3 -m pip install --break-system-packages duckdb requests
```

Verify:

```bash
/opt/homebrew/bin/python3 -c "import duckdb, requests; print(f'duckdb {duckdb.__version__}, requests {requests.__version__}')"
```

Then `kw ask` works again:

```bash
kw ask "what is the shape of the Kastner archive"
```

**Risk:** PEP 668 says a future `brew upgrade python` could break your global site-packages. Practically that just means you'd re-run the pip install after any Homebrew Python version bump. Low risk given how rare that is.

## Option B: proper venv

More work but the "right" way. Creates a `.venv` inside the wiki repo and updates the `kw` shim to source it.

```bash
# Create venv
cd ~/Repos/kastner-aberdeen-wiki
/opt/homebrew/bin/python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate
```

Then edit `/Users/scott/bin/kw` to add near the top (after the shebang):

```bash
# Activate wiki venv if present
if [ -f "${KW_ROOT:-$HOME/Repos/kastner-aberdeen-wiki}/.venv/bin/activate" ]; then
  source "${KW_ROOT:-$HOME/Repos/kastner-aberdeen-wiki}/.venv/bin/activate"
fi
```

**Cost:** ~5 minutes. Also downloads torch, sentence-transformers, and other heavy deps from `requirements.txt` you may not need.

## Recommendation

**Option A** for tonight — one command, get `kw ask` working now, move on. Revisit Option B next week if you want cleaner isolation.

## Also worth doing later (add to backlog)

- `requirements.txt` needs a refresh: says Python 3.11 (actual is 3.14), missing `requests`.
