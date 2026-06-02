"""
_llm_helper_v2.py — Hybrid LLM router for Phase 3 (v1.6, Qwen 3.6 upgrade)

Local qwen3.6:27b-mlx for entity/tech pages (~350 pages, free).
Cloud (Perplexity → Claude) for study + Volume 1 pages (~70 pages).

Used by 03_generate_vault_v2.py and indirectly by:
  - 04_generate_indices_v4.py   (PRESCIENT_INDEX template — model provenance)
  - 06_emit_scaffolding_v2.py   (README / AGENTS.md / chat-starter templates)
  - pre_filter_scoreable_obs_v5.py (scorer_version_target identifier)
  - run_prescience_calibration_v4.py (--models argparse default)

Importable, not a CLI.

LOCAL_MODEL upgrade history (forever-archive principle — do not delete):
  v1 (2026-05-26): "qwen3.5:27b-mlx" — Pete's first local model. Apache 2.0 27B MLX.
  v2 (2026-06-02): "qwen3.6:27b-mlx" — §11q upgrade. ~20 GB, MLX-native, +18% BenchLM /
                   +13% agentic vs 3.5. Honors "abort if no MLX" + "do not sacrifice KW
                   retrieval accuracy". 7-day overlap with v1 (no `ollama rm qwen3.5:27b-mlx`
                   before 2026-06-09).

Why this single source of truth matters (Gotcha 9): every consumer that writes the model
name into a generated artifact (wiki page, scorer_version, calibration manifest) MUST
import LOCAL_MODEL from here. Hardcoding the model string in a consumer creates a
producer/consumer contract drift — the runtime model is what _llm_helper calls; the doc
string is whatever the consumer hardcoded. They diverge silently. Fix once here, every
consumer picks it up at next run.

Pete's decision (2026-05-26): hybrid local+cloud.
Pete's decision (2026-06-02, §11q): Qwen 3.6 MLX upgrade, B-refactor consolidation.
"""
from __future__ import annotations
import json
import os
import subprocess
import time
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional

OLLAMA_BASE = os.environ.get("OLLAMA_BASE", "http://localhost:11434")

# -----------------------------------------------------------------------------
# Single source of truth for the local model name.
# Consumers importing LOCAL_MODEL from this module will pick up future upgrades
# automatically; never hardcode the string in a consumer script.
# -----------------------------------------------------------------------------
# §11q rollback (2026-06-02 14:36 EDT): pinned to qwen3.5:27b-mlx after evidence
# review showed Qwen 3.6 regresses on IFBench (instruction following) and GPQA
# Diamond — exactly the dimensions Phase 3 wiki generation and kw_ask synthesis
# rely on. 3.6 stays installed for soak/A-B testing through 2026-06-09; if no
# Phase-3 quality win shows up in side-by-side, `ollama rm qwen3.6:27b-mlx`
# reclaims the 20 GB. See decisions log §11q.
LOCAL_MODEL = "qwen3.5:27b-mlx"

# Convenience: a sortable scorer_version_target prefix for any caller that
# wants to tag artifacts with the model that produced them. Format mirrors
# pre_filter_scoreable_obs's existing convention (model + "_passC_v2").
def scorer_version_target(suffix: str = "passC_v2") -> str:
    """Construct a {model}_{suffix} identifier for provenance fields.

    Example: scorer_version_target("passC_v2") -> "qwen3.6:27b-mlx_passC_v2"
    """
    return f"{LOCAL_MODEL}_{suffix}"


LOCAL_TIMEOUT = 90
# Top-level payload flags for Ollama 0.24+ generate API.
# IMPORTANT: `think` and `keep_alive` MUST be top-level fields, not nested under
# `options` — Ollama 0.24 silently ignores them when nested. With Qwen 3.6 thinking
# models, an ignored `think:false` causes the entire visible response to be consumed
# by the <think>...</think> block and `.response` returns empty (eval_count > 0).
# Verified empirically 2026-06-02 on qwen3.6:27b-mlx via /api/generate.
LOCAL_TOPLEVEL = {
    "think": False,
    "keep_alive": "30m",
}
LOCAL_OPTIONS = {
    "temperature": 0.3,
    "num_ctx": 8192,
    "num_predict": 600,
}

CLOUD_TIMEOUT = 60
PPLX_BIN = os.environ.get("PPLX_BIN", "pplx")
PPLX_MODEL = "claude_sonnet_4_6"


# ---------------- local (Ollama) ----------------

def call_local(prompt: str, system: Optional[str] = None,
               retries: int = 2) -> dict:
    """Returns {ok, text, elapsed_sec, error}"""
    payload = {
        "model": LOCAL_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": LOCAL_OPTIONS,
        **LOCAL_TOPLEVEL,
    }
    if system:
        payload["system"] = system

    data = json.dumps(payload).encode("utf-8")
    url = f"{OLLAMA_BASE}/api/generate"

    last_err = ""
    for attempt in range(retries + 1):
        t0 = time.time()
        try:
            req = urllib.request.Request(
                url, data=data,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=LOCAL_TIMEOUT) as resp:
                body = resp.read().decode("utf-8")
            res = json.loads(body)
            elapsed = time.time() - t0
            return {
                "ok": True,
                "text": res.get("response", "").strip(),
                "elapsed_sec": round(elapsed, 2),
                "error": "",
                "model": LOCAL_MODEL,
            }
        except (urllib.error.URLError, urllib.error.HTTPError,
                TimeoutError, json.JSONDecodeError) as e:
            last_err = f"{type(e).__name__}: {e}"
            time.sleep(2 ** attempt)  # backoff
    return {
        "ok": False, "text": "", "elapsed_sec": 0.0,
        "error": last_err, "model": LOCAL_MODEL,
    }


# ---------------- cloud (pplx CLI) ----------------

def call_cloud(prompt: str, system: Optional[str] = None,
               retries: int = 2) -> dict:
    """Call Perplexity via pplx CLI. Returns same dict shape as call_local."""
    full = (system + "\n\n" + prompt) if system else prompt
    last_err = ""
    for attempt in range(retries + 1):
        t0 = time.time()
        try:
            proc = subprocess.run(
                [PPLX_BIN, "ask", "--model", PPLX_MODEL, full],
                capture_output=True, text=True, timeout=CLOUD_TIMEOUT,
            )
            elapsed = time.time() - t0
            if proc.returncode == 0 and proc.stdout.strip():
                return {
                    "ok": True,
                    "text": proc.stdout.strip(),
                    "elapsed_sec": round(elapsed, 2),
                    "error": "",
                    "model": PPLX_MODEL,
                }
            last_err = (proc.stderr or "no stdout").strip()[:300]
        except (subprocess.TimeoutExpired, FileNotFoundError) as e:
            last_err = f"{type(e).__name__}: {e}"
        time.sleep(2 ** attempt)
    return {
        "ok": False, "text": "", "elapsed_sec": 0.0,
        "error": last_err, "model": PPLX_MODEL,
    }


# ---------------- router ----------------

def summarize(page_type: str, prompt: str,
              system: Optional[str] = None) -> dict:
    """
    page_type ∈ {"entity", "technology", "study", "volume-1", "collection"}
    Local for entities/technologies. Cloud for studies, volume-1, collections.
    """
    if page_type in ("entity", "technology"):
        return call_local(prompt, system=system)
    elif page_type in ("study", "volume-1", "collection"):
        return call_cloud(prompt, system=system)
    else:
        # Default safe: local
        return call_local(prompt, system=system)


SYSTEM_PROMPT_ENTITY = """You are a careful research analyst summarizing an entity (company, vendor, organization, or person) from Aberdeen Group's archive. Write 3-5 short paragraphs grounded ONLY in the observations supplied. Cite observation IDs in [brackets] when claiming a specific fact. No marketing language. No speculation beyond the data. If prescience scores are supplied, note when an observation was prescient (score >= 4)."""

SYSTEM_PROMPT_TECH = """You are a careful research analyst summarizing a technology category from Aberdeen Group's archive. Write 3-5 short paragraphs covering: what it is, when Aberdeen first observed it, key vendors, adoption arc. Ground ONLY in supplied observations. Cite obs IDs in [brackets]. Note prescient observations (score >= 4)."""

SYSTEM_PROMPT_STUDY = """You are a careful research analyst summarizing a specific Aberdeen Group study. Write 4-6 short paragraphs: what the study examined, key findings (with obs IDs in [brackets]), most prescient observations (score >= 4 or 5) and why they mattered, what didn't age well. Ground in supplied observations only."""

SYSTEM_PROMPT_VOLUME1 = """You are summarizing a chapter of Pete Kastner's Volume 1 memoir, which spans his Aberdeen Group years. Write 5-8 short paragraphs preserving Pete's voice (terse, observational, comfortable with technical detail). Surface the most prescient calls (score >= 4) and any well-documented misses. Cite obs IDs in [brackets]."""

SYSTEM_PROMPT_COLLECTION = """You are summarizing one of Aberdeen Group's collection types (video transcripts, memoirs, employer records, AI responses, technology topics, DCT). Write 3-5 short paragraphs covering: what the collection is, time span, signature studies, prescient observations."""
