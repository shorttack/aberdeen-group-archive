Yes: your Mac mini M4 Pro with 48 GB unified memory is a very good fit for running Qwen3.6‑27B in 4‑bit form (OptiQ/Q4‑style) under Perplexity or other local runtimes, with enough headroom for longer contexts and multiple tools.

## Hardware fit

- Apple lists M‑series Pro/Max configs up to 48 GB unified memory; your 48 GB M4 Pro sits at the high end of that class.[1]
- Community and guide measurements for Qwen3.6‑27B show that 4‑bit/Q4 quantizations (Q4_K_M, OptiQ‑4bit, etc.) use roughly 15–18 GB of VRAM/unified memory for the model weights, plus additional overhead for KV cache and runtime.[2][3][4][5][6][7]
- Several Qwen 3.6 guides state that quantized 27B runs comfortably on Macs with 24 GB+ unified memory, and specifically call out M2/M3/M4 Pro or Max with 32 GB+ as good targets; 48 GB gives you substantial extra headroom beyond those recommendations.[5][8][9][10]

Net: with 48 GB unified memory, you’re in the “comfortable” zone, not just the bare‑minimum zone, for a 4‑bit Qwen3.6‑27B.

## What “OptiQ‑4bit” implies in practice

Most of the public measurements are for llama.cpp/gguf Q4_K_M or similar 4‑bit schemes, but the numbers are broadly representative:

- 4‑bit Qwen3.6‑27B weights: around 15–18 GB in memory depending on the exact quantization scheme (Q4_K_M vs ULaw/OptiQ variants).[3][4][6][7][2][5]
- FP8/8‑bit variants: ~22–30 GB, sometimes cited as the “full model” or FP8 sweet spot around 22–27 GB; still within your 48 GB if you stay modest on context length.[6][10][2]
- Full BF16: ~54–60 GB and up, which is beyond what a 48 GB Mac can do purely in‑memory without more aggressive offloading.[4][10][2][5]

So an OptiQ‑4bit build is squarely in the intended “consumer hardware” range your machine fits.

## Performance expectations on M4 Pro 48 GB

Looking at Mac‑oriented Qwen3.6 and generic 27B reports:

- Guides describe Qwen3.6‑27B Q4 quant as usable even on 24 GB unified memory Macs, with the caveat that 16 GB is too tight; they highlight 24–32 GB as the practical lower bound.[8][11][3][5]
- A 27B Q4 quant is typically used as an example of what runs well on M‑series Pro/Max Macs via Ollama/MLX; tables show ~17 GB VRAM for Q4_K_M and classify M‑series 24–36 GB as “comfortable.”[9][2][4][5][6][8]

Given that:

- Your 48 GB config will keep the OS, Perplexity client, and model runtime plus KV cache in memory without thrashing.  
- You should be able to run Qwen3.6‑27B‑OptiQ‑4bit with a reasonably long context (e.g., 8k–16k tokens) and still have room for tools and background processes, especially if you’re not running multiple 27B‑class models simultaneously.  

Real‑world: you should see throughput in the “practical daily use” range rather than the “barely limping along” behavior described for 16 GB systems.[11][12][3][5]

## Practical guidance for your setup

Based on the published Qwen 3.6 guides and Mac‑specific notes:

- Choose a 4‑bit or FP8/8‑bit variant (like your OptiQ‑4bit build); avoid full BF16 checkpoints on this machine.[10][2][4][5]
- Keep batch size modest (1–2) and context length reasonable if you’re running other heavy workloads; the KV cache for very long contexts can add several extra GB on top of weights.[2][3][4]
- If Perplexity (or another front‑end) lets you specify a “GPU / system memory cap” or similar, targeting ~28–32 GB for the model+cache on your 48 GB box is a sensible starting point, leaving 16–20 GB for everything else, which aligns with the “comfortable” margins in the hardware guides.[5][8][10][2]

If you tell me which local stack you plan to use behind Perplexity (Ollama, llama.cpp, MLX, LM Studio, etc.), I can suggest concrete flags (context length, batch, threads) tuned for a 48 GB M4 Pro.

Sources
[1] MacBook Pro (14-inch, M4 Pro or M4 Max, 2024) - Tech Specs https://support.apple.com/en-us/121553
[2] How to Run Qwen 3.6 Locally: 27B Dense vs 35B MoE (2026 Guide) https://codersera.com/blog/how-to-run-qwen-3-6-locally-2026/amp/
[3] Qwen3.6-27B is Flagship-Class with SWE-bench 77.2 - note https://note.com/hacklog_stealth/n/n4a1a74f3a555?hl=en
[4] The 27B Model That Beats a 397B Giant on Coding https://www.aimoneytools.net/blog/qwen3-6-27b-review-how-to-run
[5] Qwen3.6-27B: 27B Model Beats 397B on Coding (2026) https://www.buildfastwithai.com/blogs/qwen3-6-27b-review-2026
[6] Qwen3.6-27B Review: Dense 27B Beats 397B MoE (2026) https://localaimaster.com/models/qwen-3-6-27b
[7] Qwen3.6-27B GPU Requirements: VRAM & Cheapest GPU https://www.spheron.network/tools/gpu-recommender/Qwen/Qwen3.6-27B/
[8] How to Run Qwen 3.6-27B Locally: Mac, GPU, and Ollama Setup ... https://www.aimadetools.com/blog/how-to-run-qwen-3-6-27b-locally/
[9] Qwen 3.6 Complete Guide: 27B Dense, 35B-A3B MoE, and ... https://insiderllm.com/guides/qwen-3-6-local-ai-guide/
[10] Qwen 3.6-27B Complete Guide: 77.2% SWE-bench in a 27B Dense ... https://www.aimadetools.com/blog/qwen-3-6-27b-complete-guide/
[11] batiai/qwen3.6-27b https://ollama.com/batiai/qwen3.6-27b
[12] 16GB of VRAM was still not enough for daily use of Qwen3.6 27B ... https://note.com/edonack/n/nbbfebbb1104e?hl=en-US
[13] Ollama on Mac: Setup and Optimization Guide (2026) https://insiderllm.com/pdfs/ollama-mac-setup-optimization.pdf
[14] Run Qwen 3 Locally 2026: Ollama & LM Studio Setup Guide https://www.promptquorum.com/ar/local-llms/run-qwen-locally-guide-2026
[15] local-llm-guide/03-models/qwen-guide.md at main · Lingdas1/local ... https://github.com/Lingdas1/local-llm-guide/blob/main/03-models/qwen-guide.md

MLX-OPTIQ as MCP
mlx-optiq is the MLX‑native toolkit that produced your Qwen3.6‑27B‑OptiQ‑4bit build, and it’s designed exactly for Apple‑Silicon setups like your M4 Pro 48 GB, so the stack is a good match.[1][2][3][4]

## What mlx‑optiq actually is

- mlx‑optiq is an “optimizing quantizer” for MLX: it runs a sensitivity pass on each layer (KL‑divergence on calibration data), then assigns mixed bit‑widths (4/8 bits by default) per layer under a bits‑per‑weight budget.[3]
- OptiQ‑4bit Qwen3.6‑27B is a mixed‑precision MLX quant of the original Qwen/Qwen3.6‑27B model; sensitive layers are promoted to 8‑bit, robust ones stay at 4‑bit, but the on‑disk size stays within ~5% of a uniform 4‑bit MLX quant.[5][1][3]

In practice, that means: roughly “4‑bit sized” memory footprint with closer‑to‑8‑bit quality, and it runs in plain `mlx-lm` with no special runtime.[4][1][3]

## The specific Qwen3.6‑27B‑OptiQ‑4bit build

- The Hugging Face repo `mlx-community/Qwen3.6-27B-OptiQ-4bit` is the canonical MLX OptiQ quant for this model.[1][5]
- It’s described as a 4‑bit mixed‑precision quant, built with mlx‑optiq, and optimized as their “strongest dense quant” for Qwen3.6.[2][1]
- Model size is about 15–16 GB in MLX form (similar to other 4‑bit MLX 27B quants), which lines up with the 15–18 GB memory footprint we discussed earlier for 4‑bit Qwen3.6‑27B.[6][2][1]

Given your 48 GB unified memory, that leaves a lot of headroom for KV cache and the rest of the system.

## How it runs under MLX on your Mac

- mlx‑optiq quants are just standard MLX checkpoints; you load them with `mlx_lm.load` and generate with `mlx_lm.generate` as usual.[3][4]
- The per‑layer quantization info is stored in `config.json` under `quantization` plus an `optiq_metadata.json` sidecar, which mlx‑optiq uses for things like sensitivity‑aware LoRA or KV‑cache tweaks, but plain inference doesn’t require extra flags.[4][5]

On a 36 GB Mac they note that Qwen3.6‑27B‑OptiQ‑4bit fits with LoRA rank 8 and a relatively small `max-seq-length` (example at 512), which is a more constrained configuration than your 48 GB machine. With 48 GB unified memory you can:[2]

- Run this checkpoint comfortably with longer contexts and no fine‑tuning.  
- Still reserve space for tools, browser, and Perplexity’s process without hitting swap.  

## Recommended MLX / mlx‑optiq usage on 48 GB

If you’re driving this through MLX directly (or anything that wraps it, such as a local Perplexity backend):

- Model choice: stick with `mlx-community/Qwen3.6-27B-OptiQ-4bit` for general reasoning; only consider the more aggressive 3–3.7‑bit OptiQ variants if you later want to stack multiple big models at once.[7][8][1]
- Context length: you can push substantially beyond the 512 token example; community 4‑bit Qwen3.6‑27B MLX builds quote comfortable contexts in the tens of thousands of tokens on 48 GB machines before KV prefill becomes the limiting factor. A conservative starting point would be 16k–32k for heavy work, and higher if you’re willing to trade throughput for length.[9][6]
- Batch size: keep batch size at 1 (maybe 2) for interactive use so your KV cache doesn’t balloon; that’s consistent with MLX usage notes for large 4‑bit 27B models on Mac.[9][2]

If you’d like, I can sketch an example `mlx_lm` command line and a minimal Python snippet (with suggested `max_seq_length`, `max_tokens`, and `temperature`) tuned specifically for Qwen3.6‑27B‑OptiQ‑4bit on an M4 Pro 48 GB.  

What front‑end are you planning to drive this from: straight Python/MLX, a web UI (mlx‑optiq “lab”, Open WebUI, etc.), or an integration behind Perplexity’s local‑model connector?

Sources
[1] mlx-community/Qwen3.6-27B-OptiQ-4bit https://huggingface.co/mlx-community/Qwen3.6-27B-OptiQ-4bit
[2] Qwen3.6 on Apple Silicon: dense + MoE quants - mlx-optiq https://mlx-optiq.com/docs/qwen3.6
[3] quantize, fine-tune and serve LLMs on Apple Silicon - mlx-optiq https://mlx-optiq.com/docs/faq
[4] Using mlx-optiq quants · mlx-optiq https://mlx-optiq.com/docs/quants
[5] mlx-community/Qwen3.6-27B-OptiQ-4bit Reviews & Ratings https://llmsreview.com/models/mlx-community--qwen3.6-27b-optiq-4bit
[6] froggeric/qwen3.6-27b-mlx-4bit https://lmstudio.ai/froggeric/qwen3.6-27b-mlx-4bit
[7] Qwen3.6-27B-3bit-mlx · Hugging Face: 3 & 5 mixed quant ... https://www.reddit.com/r/LocalLLaMA/comments/1swrsst/qwen3627b3bitmlx_hugging_face_3_5_mixed_quant_for/
[8] osmapi/Qwen3.6-27B-Claude-Opus-Reasoning-Distill-v2 ... https://huggingface.co/osmapi/Qwen3.6-27B-Claude-Opus-Reasoning-Distill-v2-abliterated-OptiQ-3.7bpw-mlx
[9] mlx-community/Qwen3.6-27B-OBLITERATED-MLX-4bit https://huggingface.co/mlx-community/Qwen3.6-27B-OBLITERATED-MLX-4bit
[10] spicyneuron/Qwen3.6-27B-MLX-5.7bit-vision - Hugging Face https://huggingface.co/spicyneuron/Qwen3.6-27B-MLX-5.7bit-vision
[11] mlx-community/Qwen3.6-27B-OptiQ-4bit · Adding the kv_config.json ... https://huggingface.co/mlx-community/Qwen3.6-27B-OptiQ-4bit/discussions/2
[12] Qwen3.6-27B-Omnimerge-v4-MLX-VL-4bit huggingface.co api ... https://www.toolify.ai/ai-model/mannix-ita-qwen3-6-27b-omnimerge-v4-mlx-vl-4bit
[13] mlx-community/Qwen3.6-27B-4bit https://huggingface.co/mlx-community/Qwen3.6-27B-4bit
[14] majentik/Qwen3.5-27B-TurboQuant-MLX-4bit at main https://huggingface.co/majentik/Qwen3.5-27B-TurboQuant-MLX-4bit/blob/main/README.md
[15] mlx-community/Qwen3.6-27B-MTP-bf16 https://huggingface.co/mlx-community/Qwen3.6-27B-MTP-bf16

# Integration
You can integrate Qwen3.6‑27B‑OptiQ‑4bit behind Perplexity’s local‑model connector by exposing it as an OpenAI‑compatible HTTP server via `mlx_lm.server` (or `mlx_vlm.server` for vision) and then pointing Perplexity at that endpoint; your M4 Pro 48 GB has ample headroom for this setup.[1][2][3][4]

## Overall architecture

- mlx‑optiq quants like `mlx-community/Qwen3.6-27B-OptiQ-4bit` are standard MLX checkpoints and “just work” with `mlx_lm.load` and `mlx_lm.generate`.[2][4][1]
- The MLX ecosystem exposes an OpenAI‑compatible server via `mlx_lm.server` (for text) or `mlx_vlm.server` (for VLMs), which is exactly what other agents and UIs (Pi, Hermes, etc.) use.[3][5]
- Perplexity’s local‑connector layer can talk to any OpenAI‑style `/v1/chat/completions` or `/v1/completions` API, so the integration pattern is:
  - Run `mlx_lm.server` with Qwen3.6‑27B‑OptiQ‑4bit on your Mac.  
  - Configure Perplexity’s connector with `base_url = http://127.0.0.1:8080/v1` (or your chosen host/port) and `model = "mlx-community/Qwen3.6-27B-OptiQ-4bit"` (or a custom ID you define).  

This is the same pattern used in the MLX community docs for other clients (Pi, Hermes), just substituting Perplexity as the OpenAI client.[5][3]

## Starting the MLX / OptiQ server

### 1. Install MLX LM (and optionally mlx‑optiq)

- The Qwen3.6‑27B OptiQ HF page shows usage via `mlx_lm`:[2]
  - `pip install mlx-lm` (or `uv tool install mlx-lm` if you’re using `uv`).  
- If you want KV‑cache sensitivity passes and mixed‑precision KV serving (optional optimization), follow the `mlx-optiq` docs:[6][1]

### 2. Run Qwen3.6‑27B‑OptiQ‑4bit as a server

From the MLX community discussions and examples for 4‑bit Qwen models:[7][3]

- Example for a similar 4‑bit Qwen3.6 MLX model shows:

  - Install MLX LM:
    - `uv tool install mlx-lm`  
  - Start an OpenAI‑compatible server:
    - `mlx_lm.server --model "mlx-community/Qwen3.6-27B-4bit"`[3]

For your OptiQ quant, you do the same with the OptiQ repo:

- Start server (text‑only variant, OpenAI‑compatible):  

  - `mlx_lm.server --model "mlx-community/Qwen3.6-27B-OptiQ-4bit" --host 127.0.0.1 --port 8080`  

  This exposes an OpenAI‑style API at `http://127.0.0.1:8080/v1`, matching the pattern used for other MLX 4‑bit Qwen3.6 models.[4][3]

### 3. Optional: OptiQ KV‑cache optimization

The OptiQ docs for Qwen3.6 show an additional step for KV‑cache quantization and serving, which can reduce memory usage and improve throughput:[1]

- Run a one‑time KV sensitivity pass:

  - `optiq kv-cache mlx-community/Qwen3.6-27B-OptiQ-4bit --target-bits 5.0 --candidate-bits 4,8 -o ./kv/qwen36_27b`[1]

- Then serve with mixed‑precision KV:

  - `optiq serve --model mlx-community/Qwen3.6-27B-OptiQ-4bit --kv-config ./kv/qwen36_27b/kv_config.json --max-tokens 32768 --temp 0.6 --top-p 0.95`[1]

`optiq serve` presents an HTTP interface with similar semantics; you’d just point Perplexity at the `optiq serve` URL instead of `mlx_lm.server`. On a 48 GB Mac, this extra KV optimization is nice but not strictly necessary for single‑user interactive use.

## Wiring it into Perplexity’s connector

Because MLX’s server is OpenAI‑compatible, you configure Perplexity’s “custom / local model” profile roughly the same way other tools (Pi, Hermes) point to an MLX server:[5][3]

- Base URL: `http://127.0.0.1:8080/v1` (or your custom host/port).  
- API key: can be a placeholder like `none` if Perplexity allows a dummy value; MLX doesn’t enforce auth out of the box, and this is how MLX examples configure other clients with “no real key.”[3]
- Model ID: `mlx-community/Qwen3.6-27B-OptiQ-4bit` (or whatever you choose to label it inside Perplexity; the server will accept that ID if you pass it as `model`).  
- API type: “OpenAI Chat Completions” (`/v1/chat/completions`) — MLX server exposes that style of endpoint in its current OpenAI‑style mode, as shown in the MLX community docs and Qwen MLX integration docs.[8][9][3]

Once configured, Perplexity will:

- Send chat prompts to your MLX server using OpenAI’s JSON schema (messages, temperature, top_p, etc.).  
- Receive Qwen3.6‑27B‑OptiQ‑4bit completions as if it were a normal OpenAI / local‑LLM backend, but all inference stays on your M4 Pro via MLX.  

## Suggested settings for this model on your M4 Pro 48 GB

Drawing from the Qwen3.6 + MLX examples and OptiQ docs:[2][5][3][1]

- `max_tokens` per completion: 1024–4096 as a practical default; OptiQ’s example uses `--max-tokens 32768` for heavy use, which you can support with 48 GB if you don’t run multiple big jobs in parallel.[1]
- `temperature`: 0.4–0.7 for general reasoning (OptiQ serves example uses 0.6).[1]
- `top_p`: 0.9–0.95 (OptiQ example uses 0.95).[1]
- Context length: if exposed as `max_model_len`/similar in the server options, 16k–32k is a good starting compromise; Qwen3.6‑27B can technically go much higher but KV cache RAM will ramp quickly.[10][1]

These are all configurable either on the MLX server command line or in Perplexity’s model profile, depending on how your Enterprise connector UI is implemented.

Would you prefer a concrete, copy‑paste set of terminal commands for starting the MLX server at login (e.g., via a small launchd service or shell script) so Qwen3.6‑27B‑OptiQ‑4bit is always available as a Perplexity backend when your Mac boots?

Sources
[1] Qwen3.6 on Apple Silicon: dense + MoE quants - mlx-optiq https://mlx-optiq.com/docs/qwen3.6
[2] mlx-community/Qwen3.6-27B-OptiQ-4bit https://huggingface.co/mlx-community/Qwen3.6-27B-OptiQ-4bit
[3] mlx-community/Qwen3.6-27B-4bit · Discussions - Hugging Face https://huggingface.co/mlx-community/Qwen3.6-27B-4bit/discussions
[4] Using mlx-optiq quants · mlx-optiq https://mlx-optiq.com/docs/quants
[5] spicyneuron/Qwen3.6-27B-MLX-5.7bit-vision - Hugging Face https://huggingface.co/spicyneuron/Qwen3.6-27B-MLX-5.7bit-vision
[6] quantize, fine-tune and serve LLMs on Apple Silicon - mlx-optiq https://mlx-optiq.com/docs/faq
[7] mlx-community/Qwen3.6-27B-4bit https://huggingface.co/mlx-community/Qwen3.6-27B-4bit
[8] MLX Community https://huggingface.co/mlx-community
[9] MLX LM - Qwen https://qwen.readthedocs.io/en/latest/run_locally/mlx-lm.html
[10] How to Run Qwen 3.6 Locally: 27B Dense vs 35B MoE (2026 Guide) https://codersera.com/blog/how-to-run-qwen-3-6-locally-2026/amp/
[11] leonsarmiento/Qwen3.6-27B-4bit-mlx - Hugging Face https://huggingface.co/leonsarmiento/Qwen3.6-27B-4bit-mlx
[12] Qwen3.6-27B-OptiQ-4bit MLX fails with KeyError ' ... https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues/1926
[13] Coding locally with Pi Coding agent and open weights models (April ... https://www.ovidiudan.com/2026/04/26/pi-local-open-weights.html
[14] README.md · mlx-community/perplexity-ai-r1-1776-bf16 at 7a03df98d6569d5b34f84babe64ddf266f83cc1c https://huggingface.co/mlx-community/perplexity-ai-r1-1776-bf16/blame/7a03df98d6569d5b34f84babe64ddf266f83cc1c/README.md
[15] mlx_lm_perplexity.py https://gist.github.com/awni/33a5315e0a5b91ea2cd032af39a624d8
[16] Add files using upload-large-folder tool · mlx-community/ ... https://huggingface.co/mlx-community/perplexity-ai-r1-1776-2bit/commit/1b00d7e222c6aa2e533b7aa9e5625cb4a6a07fcc
[17] raw https://huggingface.co/YTan2000/Qwen3.6-27B-TQ3_4S/raw/main/README.md

#Terminal Commnads
Here’s a concrete, minimal path: install MLX‑LM, start a Qwen3.6‑27B‑OptiQ‑4bit server on `localhost:8080`, and then point Perplexity’s connector at `http://127.0.0.1:8080/v1` with an OpenAI‑compatible anofile.[1][2][3][4][5]

## 1. One‑time setup: install MLX‑LM (with server)

In Terminal:

```bash
# Option A: plain pip (simple, global)
pip install --upgrade "mlx-lm[server]"
```

The `mlx-lm[server]` extra pulls in the OpenAI‑compatible HTTP server.[3][4][5]

If you prefer `uv`:

```bash
# If you use uv tooling
uv tool install "mlx-lm[server]"
```

(You already have Python + tooling; this just ensures the server binary is present.)

## 2. Start the Qwen3.6‑27B‑OptiQ‑4bit MLX server

From the Hugging Face page and MLX server docs, models are served like:[4][5][1][3]

```bash
mlx_lm.server \
  --model "mlx-community/Qwen3.6-27B-OptiQ-4bit" \
  --host 127.0.0.1 \
  --port 8080 \
  --max-tokens 4096 \
  --context-size 16384 \
  --temp 0.6 \
  --top-p 0.95
```

Notes:

- `--model` uses the HF repo name; MLX will download and cache it automatically the first time.[5][1]
- `--max-tokens` is the per‑response cap; 4096 is a solid starting point.[6][4]
- `--context-size` sets the maximum context; 16384 is conservative for 48 GB but roomy for analysis. You can raise this later if you want huge transcripts.[7][4]

To keep it simple while testing, you can even start with defaults:

```bash
mlx_lm.server --model "mlx-community/Qwen3.6-27B-OptiQ-4bit"
```

which will bind on `localhost:8080` with default generation settings, as shown in the MLX server docs and examples.[3][4][5]

## 3. Quick local sanity check (optional)

From a different Terminal window:

```bash
curl http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer not-needed" \
  -d '{
    "model": "mlx-community/Qwen3.6-27B-OptiQ-4bit",
    "messages": [
      {"role": "user", "content": "Say hello from Qwen3.6-27B-OptiQ-4bit in one sentence."}
    ],
    "max_tokens": 64,
    "temperature": 0.6,
    "top_p": 0.95
  }'
```

MLX’s server implements an OpenAI‑style `/v1/chat/completions` API; the `api_key` is not actually required, which is why examples use placeholders like `not-needed` or `local`.[2][8][9][3]

You should see a JSON response with a `choices[0].message.content` field containing the reply.

## 4. Perplexity connector configuration (conceptual)

In Perplexity’s Enterprise / local‑model settings, create a new “OpenAI‑compatible” or “custom” provider:

- Base URL: `http://127.0.0.1:8080/v1`[2][5][3]
- API key: any dummy string (e.g., `local-qwen36`), since the MLX server doesn’t enforce it.  
- Model name: `mlx-community/Qwen3.6-27B-OptiQ-4bit` (to match what the server expects in the `model` field).[8][5][3]

Perplexity will then send normal OpenAI‑style chat requests to your MLX server, which Qwen3.6‑27B‑OptiQ‑4bit will answer locally on the M4 Pro.

## 5. Optional: OptiQ KV‑cache optimization later

When you want to squeeze even more out of the 48 GB, mlx‑optiq’s Qwen3.6 guide shows:

```bash
# One-time KV sensitivity/quant pass
optiq kv-cache mlx-community/Qwen3.6-27B-OptiQ-4bit \
  --target-bits 5.0 \
  --candidate-bits 4,8 \
  -o ./kv/qwen36_27b

# Serve with mixed-precision KV
optiq serve \
  --model mlx-community/Qwen3.6-27B-OptiQ-4bit \
  --kv-config ./kv/qwen36_27b/kv_config.json \
  --max-tokens 32768 \
  --temp 0.6 \
  --top-p 0.95
```

which exposes another HTTP endpoint you can use instead of `mlx_lm.server`. For a first pass, I’d stick with `mlx_lm.server` until you’re happy with behavior.[10][7]

If you tell me whether you’d like this wrapped in a tiny shell script (e.g., `run-qwen36-optiq.sh` living in `~/bin`) and whether you use `zsh` with any custom env managers (pyenv/uv), I can write the exact script body tailored to your environment.

Sources
[1] mlx-community/Qwen3.6-27B-OptiQ-4bit https://huggingface.co/mlx-community/Qwen3.6-27B-OptiQ-4bit
[2] A Job Postings Tool: A Guide to MLX-LM Server and Tool Use with ... https://medium.com/@levchevajoana/a-job-postings-tool-a-guide-to-mlx-lm-server-and-tool-use-with-the-openai-client-edb9a5d75b4c
[3] MLX - Liquid Docs https://docs.liquid.ai/deployment/on-device/mlx
[4] Running OpenClaw on Apple Silicon with MLX https://contracollective.com/blog/mlx-openclaw-apple-silicon-local-agent-runtime-2026
[5] mlx-lm/mlx_lm/SERVER.md at main https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md
[6] robertobissanti/EngGPT2-16B-A3B-MLX-4bit - Hugging Face https://huggingface.co/robertobissanti/EngGPT2-16B-A3B-MLX-4bit
[7] Qwen3.6 on Apple Silicon: dense + MoE quants - mlx-optiq https://mlx-optiq.com/docs/qwen3.6
[8] MLX LM + OpenAI Client https://gist.github.com/awni/bcd59f342d5be8a9d6b4268d0c782d25
[9] mlx_lm_openai.md https://gist.github.com/sugatoray/f4c351ffeb525ad909576b7dedefbdc5
[10] Using mlx-optiq quants · mlx-optiq https://mlx-optiq.com/docs/quants
[11] LLM Fine-tuning with MLX https://medium.com/@jackcheang5/llm-fine-tuning-with-mlx-93012221dea6
[12] Run Your Own AI - AnthonyLewis.com https://anthonylewis.com/2025/06/01/run-your-own-ai/
[13] Getting up and running with LLMs on Apple Silicon (M2 and MLX) https://medium.com/@dr.junghoonson/getting-up-and-running-with-llms-on-apple-silicon-m2-and-mlx-223cfe2a3413
[14] vllm-mlx/docs/getting-started/installation.md at main - GitHub https://github.com/waybarrios/vllm-mlx/blob/main/docs/getting-started/installation.md
[15] Running Local Hugging Face Models with MLX-LM and the ... https://medium.com/@levchevajoana/running-local-hugging-face-models-with-mlx-lm-and-the-agno-agentic-framework-de134259d34d
[16] opencode on GLM-4.7-Flash-4bitをMacBookで動かす #mlx-lm - Qiita https://qiita.com/the_haigo/items/df4905a742264004a0b4


# Script
I created a runnable zsh launcher script in your workspace at `/Users/scott/Desktop/Archive/run-qwen36-optiq.zsh` and made it executable.[1][2]

## Run it

Use this in Terminal:

```bash
cd /Users/scott/Desktop/Archive
./run-qwen36-optiq.zsh
```

That launches `mlx_lm.server` with default settings for `mlx-community/Qwen3.6-27B-OptiQ-4bit` on `127.0.0.1:8080`, with `max_tokens=4096`, `context_size=16384`, `temperature=0.6`, and `top_p=0.95`.[1]

## Override settings

You can swap models or tune runtime settings without editing the script:

```bash
MODEL=mlx-community/Qwen3.6-27B-OptiQ-4bit PORT=8081 CONTEXT_SIZE=32768 ./run-qwen36-optiq.zsh
```

Or pass a different model as the first argument:

```bash
./run-qwen36-optiq.zsh mlx-community/Qwen3.6-27B-4bit
```

The script accepts environment overrides for `HOST`, `PORT`, `MAX_TOKENS`, `CONTEXT_SIZE`, `TEMP`, and `TOP_P`, and it checks that `mlx_lm.server` is installed before starting.[1]

## Connector target

Once the script is running, point Perplexity’s local connector to:

- Base URL: `http://127.0.0.1:8080/v1`.[3][4]
- Model: `mlx-community/Qwen3.6-27B-OptiQ-4bit` unless you started the script with a different model name.[1]

## Verify quickly

Open a second Terminal and test the local endpoint:

```bash
curl http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer local" \
  -d '{
    "model": "mlx-community/Qwen3.6-27B-OptiQ-4bit",
    "messages": [{"role": "user", "content": "Reply in one short sentence."}],
    "max_tokens": 64
  }'
```

MLX’s server exposes an OpenAI‑compatible chat endpoint, so a successful JSON response means Perplexity should be able to connect as well.[4][3]

Would you like the next step to be a `launchd` plist so this comes up automatically at login?

Sources
[2] MLX - Liquid Docs https://docs.liquid.ai/deployment/on-device/mlx
[3] mlx-lm/mlx_lm/SERVER.md at main https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md

# Local Model Selection
On a Mac mini M4 Pro with 48 GB, the sweet spot for a **local instruction‑following model to pair with Perplexity Computer** is a strong 14B–32B class instruct model (Qwen or Mistral) in 4–5‑bit quantization, with a smaller 3–9B model available for “heartbeat”/light tasks.[1][2]

Below is a concrete, Mac‑specific plan.

***

## Hardware and capacity

Your 48 GB M4 Pro can comfortably host:

- A **32B model at 4‑bit quantization** while leaving plenty of RAM for the OS and Perplexity’s agents/tools.[2]
- Multiple **8–14B models at Q4/Q5** side‑by‑side (e.g., one “serious” model + one small, very fast model).[1]

This is well above the 16–24 GB configurations most public guides assume, so you can push into the higher‑quality tier without starving the system.[3][4]

***

## Primary “serious work” model (tool‑calling & instructions)

Criteria that matter most with Perplexity Computer:

- Reliable **tool calling** (file edits, shell, browser, etc.).
- Strong **instruction following** (multi‑step commands, constraints).
- Enough “headroom” to keep other models and tools running.

Recommended starting candidates:

- **Qwen 2.5 / Qwen3 32B Instruct (Q4)**  
  - Real‑world tests on M4 Pro 64 GB show ~18–19 GB usage at 4‑bit, with good throughput and a big jump in reasoning and instruction‑following compared to 7–8B models.[2]
  - On 48 GB, that leaves ~25–28 GB for OS, Perplexity Computer, and auxiliary processes, which is more than adequate.  
  - Qwen 2.5+/3 series are widely recommended in local‑LLM circles as “near‑frontier quality” in their parameter class.[5][6][1]

- **Mistral‑Small / Mistral‑Small‑3.x‑Instruct (24B) (Q4)**  
  - Community benchmarks call out Mistral‑Small 24B as beating or matching frontier APIs on many instruction tasks while still being Apple‑silicon‑friendly.[7][1]
  - Slightly lighter than 32B Qwen but still very capable for structured workflows.

If you want a single “main” local model for Computer to delegate substantial file and system work to, I would test **Qwen 2.5/3 32B‑Instruct in Q4** first, then Mistral‑Small‑24B‑Instruct as a second candidate.

***

## Secondary “heartbeat” / lightweight model

Perplexity Computer will often need a model for:

- Short classification, parsing, or routing (“is this spam?”, “what is the file type?”).  
- Very frequent, cheap checks where latency matters more than raw IQ.

A small model is ideal here:

- **Qwen3 4B or 8B Instruct**  
  - Frequently recommended as the default “local heartbeat” model: fast, robust, easy to fit even on 16 GB machines.[6][1]
  - On 48 GB, you can run this alongside a 24–32B model without noticing the memory footprint.

- **Llama 3.2 3B / Gemma 3–4B / Phi‑4‑mini**  
  - All are viable if you prefer Meta/Google/Microsoft ecosystems; they trade a bit of capability for speed and tiny memory use.[8][1]

Pattern that has worked well in similar Mac‑mini setups:

- **Small model (3–9B) for heartbeats/routing**, always on.  
- **Bigger model (14–32B) for “real” edits, planning, and multi‑tool workflows.**[1]

***

## Practical test protocol (very relevant to Computer)

Before trusting a local model as a Computer backend, run a focused **tool‑calling test**:

1. Load the model via your local server layer (Ollama, LM Studio, MLX) with OpenAI‑compatible API.  
2. Send a task that *forces* the model to use tools instead of faking work, e.g.:  
   - “Open the file `/tmp/test.txt`, replace the word ‘draft’ with ‘final’ everywhere, and tell me exactly how many replacements you made.”  
3. Check three things over 5 runs:
   - Did it actually invoke the file tool (not just claim to)?  
   - Did it return a **specific** count?  
   - Was the count **correct**?

Guides for OpenClaw and similar agent stacks emphasize that a model that passes this kind of test consistently is safe for “real work”; one that hallucinates or skips the tool is “heartbeat‑only” regardless of size.[1]

Run this test on:

- Qwen 32B Instruct (Q4).  
- Mistral‑Small‑24B Instruct (Q4).  
- Your chosen small model (Qwen3 4B or Llama 3.x 3B) to see whether it can also handle light edits.

***

## Integration notes for Perplexity Computer

At a high level (without going into your exact wiring):

- Expose your local models via **OpenAI‑style HTTP endpoints**; Computer can then target them as named models in its orchestration layer.[9][10]
- Use a **“merge” or routing mode** in your local gateway (LM Studio/OpenClaw‑style) so that:
  - Easy tasks default to the small model.  
  - Harder, long‑context tasks go to the 24–32B model (or stay on cloud frontier models until the local candidate has “earned trust”).[1]
- Keep the **small model always loaded**; start/stop the big model depending on your current Computer workflows to manage thermals and power.

This lets you experiment without ripping out the frontier models that Computer already uses for research and long‑context reasoning.[11][12][9]

***

## Concrete “first stack” for your 48 GB M4 Pro

If you want a specific initial combination to try:

- **Primary local agent model:**  
  - Qwen 2.5 or Qwen3 32B Instruct, Q4 quantization.  
- **Secondary heartbeat model:**  
  - Qwen3 4B or 8B Instruct (or Llama 3.2 3B if you prefer that ecosystem).  
- **Runtime:**  
  - LM Studio or Ollama for easy management on Apple silicon, with MLX under the hood where available.[13][14][7]

Would you rather optimize this stack for **maximum local autonomy** (doing as much as possible off‑cloud) or for **latency and responsiveness** while still leaning on Computer’s frontier models for the heavy lifting?

Sources
[1] Best Local Models for OpenClaw in LM Studio (Mac Mini M4 ... https://mrprompts.substack.com/p/best-local-models-for-openclaw-in
[2] I Asked My AI Agent to Set Up a Local LLM. Here's What It Did. https://robertheubanks.substack.com/p/i-asked-my-ai-agent-to-set-up-a-local
[3] Mac Mini M4 or Pro for local LLM tasks? | Christian Stocker https://www.linkedin.com/posts/chregu_mac-mini-m4-or-pro-for-local-llm-tasks-activity-7289627142215098368-KWPc
[4] Recommendations for local AI models with OpenCLAW? https://www.facebook.com/groups/1577315533418837/posts/1643178380165885/
[5] Best local LLM for Mac Mini M1 Pro? https://www.facebook.com/groups/openclawusers/posts/671600012668942/
[6] Best LLMs for Mac Mini M4 16GB RAM — Top 5 Ranked (2026) https://modelfit.io/blog/best-llm-mac-mini-m4-16gb/
[7] Best LLM Local for Mac Mini M4 : r/LocalLLM https://www.reddit.com/r/LocalLLM/comments/1ju64ue/best_llm_local_for_mac_mini_m4/
[8] Local AI on M-Chip Macbooks? - Hardware Hub https://forum.level1techs.com/t/local-ai-on-m-chip-macbooks/220407
[9] Introducing Perplexity Computer https://www.perplexity.ai/hub/blog/introducing-perplexity-computer
[10] Perplexity's new Computer is another bet that users need ... https://techcrunch.com/2026/02/27/perplexitys-new-computer-is-another-bet-that-users-need-many-ai-models/
[11] Perplexity Computer integrates 19 AI models for research, ... https://www.facebook.com/groups/aisuccessslab/posts/3494532020695158/
[12] Perplexity Computer: What I Built in One Night (Review ... https://karozieminski.substack.com/p/perplexity-computer-review-examples-guide
[13] How I Built a Local LLM System on 16GB of RAM — And ... https://pub.towardsai.net/how-i-built-a-local-llm-system-on-16gb-of-ram-and-why-it-actually-works-c289ecd2020f
[14] Best Local AI to run on Mac mini M4 Pro? : r/LocalLLM https://www.reddit.com/r/LocalLLM/comments/1r1sobm/best_local_ai_to_run_on_mac_mini_m4_pro/
[15] Everything is Computer https://www.perplexity.ai/hub/blog/everything-is-computer

#Autonomy Strategy
For maximum autonomy, you want to push as much as possible onto one or more strong local models and treat cloud models as “specialized consultants” rather than the default brain.[1]

Given your 48 GB M4 Pro and Perplexity Computer, I’d optimize around:

***

## Overall autonomy strategy

- Run a **high‑end local “agent brain”** (32–70B, quantized) that can plan, reason, and orchestrate tools without constant cloud fallbacks.[2][1]
- Keep a **small, always‑on local model** for routing/heartbeats so Computer can do frequent checks and simple tasks entirely offline.[1][2]
- Use cloud frontier models only when explicitly requested or when you hit well‑defined local limits (context length, certain coding edge cases, etc.).[1]

With 48 GB unified memory you are in the “serious local AI agent” tier; guides explicitly call this the sweet spot for running 32B and even quantized 70B models for 24/7 agents like OpenClaw.[2][1]

***

## Model sizing for 48 GB autonomy

Empirical rules of thumb from Apple‑silicon tuning:

- macOS + background processes reserve ~4 GB.[2]
- You want your largest model to stay under about **60–70% of total RAM** to leave room for KV cache, tools, and applications.[1]

On a 48 GB M4 Pro that means:

- ~44 GB available for models,[2]
- Practical comfort zone: a **32B model at Q4/Q5** or even a **70B model at Q2–Q4** if you’re willing to accept slower throughput.[1][2]

This matches current advice that a 48 GB Mac mini M4 Pro can run Llama‑3‑class 70B quantized or Qwen2/3 32B at good quality for autonomous agents.[3][2][1]

***

## Autonomy‑first primary model

If autonomy is the goal, you care less about marginal latency and more about making the local model good enough that it rarely “needs” a cloud fallback.

Based on current local‑LLM guidance for Apple silicon:

- **Tier 1 (maximum autonomy, slower): Quantized 70B model**  
  - Example: **Llama 3.x 70B‑Instruct, Q4** on disk/RAM.[2][1]
  - Fits into the 44 GB effective budget with Q4 quantization; you’ll see slower tokens/sec but significantly better robustness on complex reasoning and multi‑tool workflows than 7–13B models.[1][2]
  - For a 24/7 agent, you’d probably cap context length to avoid blowing out KV cache.

- **Tier 2 (balanced autonomy + practicality): Qwen2/3 32B‑Instruct (Q4)**  
  - Guides for Mac mini M‑series explicitly call out **Qwen2 32B (Q4)** as a sweet‑spot model for “serious local AI” on 32–48 GB Macs.[3][2]
  - At Q4 it typically uses high‑teens to low‑20s GB of RAM in practice, leaving ample headroom for Perplexity Computer, tools, and even a second model.[2][1]
  - Autonomy‑wise, a well‑configured 32B Qwen‑class model will handle the vast majority of agent tasks (planning, file edits, shell, simple RAG) without cloud help.

If your priority is sustained, reliable autonomy over “fastest possible response,” I’d start with **Qwen2.5/3 32B‑Instruct Q4 as the main agent brain**, then experiment with a 70B Q4 model once you’re comfortable with thermal/latency trade‑offs.

***

## Secondary local model for routing and light work

To make autonomy efficient rather than just possible:

- Keep a **small (3–8B) local model always resident** for:
  - Heartbeat checks, classification, “is this worth escalating?”  
  - Short prompts and cheap transformations (e.g., quick regex‑like rewrites, tag extraction).

Given current recommendations:

- **Qwen3 4B or 8B Instruct** are strong small‑model choices that fit easily on much smaller Macs and are used in agent frameworks as default local workers.[3][1]
- These models will barely dent your 48 GB budget alongside the 32B model; they help you avoid waking the “big brain” for trivial tasks.

This two‑model layout (big 32–70B + small 3–8B) is exactly what many OpenClaw‑style autonomous setups use on Mac minis for near‑fully local operation.[1][2]

***

## How this maps onto Perplexity Computer

In an autonomy‑first configuration, you’d ideally:

- Register your **big local model as the default “agent model”** for tool‑calling chains where privacy/offline operation is important.  
- Register your **small local model as the default router/utility model** for light tasks and frequent checks.  
- Keep **cloud models opt‑in**: either selected explicitly per‑task (“use GPT‑4o for this research sprint”) or triggered under well‑defined conditions (e.g., context > N tokens, or certain benchmarked failure modes).

From an operational perspective, this makes your Mac mini into the “local brain” that Perplexity Computer leans on first, with cloud models in a secondary role for frontier‑level tasks.

***

To tune this properly, the next key question is: are you willing to tolerate significantly slower responses (e.g., 1–3 tokens/sec for hard tasks) in exchange for running something like a 70B model locally, or do you want to cap at 32B to keep interaction speeds closer to “comfortable human conversation”?

Sources
[1] Best Mac for AI in 2026: Run Local LLMs on a Budget https://www.refurb.me/blog/best-mac-for-ai
[2] Best Mac Mini for Running Local LLMs and OpenClaw https://blog.starmorph.com/blog/best-mac-mini-for-local-llms
[3] The Best Local LLMs To Run On Every Mac (Apple Silicon) https://apxml.com/posts/best-local-llm-apple-silicon-mac
[4] Best LLM Local for Mac Mini M4 : r/LocalLLM https://www.reddit.com/r/LocalLLM/comments/1ju64ue/best_llm_local_for_mac_mini_m4/
[5] What are the best local LLM models for Hermes on a Mac ... https://www.facebook.com/groups/1283855437217819/posts/1337464105190285/
[6] Best local LLM for Mac Mini M1 Pro? https://www.facebook.com/groups/openclawusers/posts/671600012668942/
[7] Your Local LLM Is 3x Slower Than It Should Be https://www.youtube.com/watch?v=qmAbco38pXA
[8] Mac Mini M4 for Ottodev with local model https://thinktank.ottomator.ai/t/mac-mini-m4-for-ottodev-with-local-model/455
[9] Mac Mini M4 or Pro for local LLM tasks? | Christian Stocker https://www.linkedin.com/posts/chregu_mac-mini-m4-or-pro-for-local-llm-tasks-activity-7289627142215098368-KWPc

#Registration With Perplexity Computer
To do that in practice, you need to make your local model look like a dependable **tool-calling endpoint**, then tell Perplexity Computer to route agent work to it by default at the subtask/model settings layer rather than only selecting it ad hoc in a prompt.[1][2]

## What “register” means

In Perplexity Computer, model assignment is part of its multi-model orchestration: Computer can choose specific models for specific subtasks, and users can manually assign which models handle which parts of a task.[2][3][1]

So “register your big local model as the default agent model” usually means:

1. Expose the model through an **OpenAI-compatible API** endpoint.[4][5]
2. Ensure the model reliably emits valid **tool/function calls** in the format your serving layer expects.[6][7]
3. Add that endpoint to the layer Computer can reach, then make it the preferred model for agent/tool-execution subtasks rather than leaving routing entirely automatic.[1][2]

## Local serving setup

For local hosting, the simplest path is a serving layer such as Ollama or llama-cpp/OpenAI-compatible servers, because local tool-calling support is commonly exposed through OpenAI-style chat/function APIs.[5][4]

Two practical patterns are common:

- **Ollama-compatible path**: run a tool-capable model and expose it through the local API, then place a gateway or MCP/tool wrapper in front of it if needed.[4]
- **vLLM / llama.cpp / LM Studio path**: expose the model with explicit tool-calling support; some stacks need parser flags such as Mistral-specific tool parsers or auto-tool-choice switches to make downstream agents recognize calls correctly.[6]

If the server emits plain text instead of structured tool calls, Computer will treat it as a chat model, not a dependable agent model.[6]

## Model choice for tool chains

For tool-calling specifically, recent practical evaluation found **Qwen 3 14B** and **Qwen 3 8B** among the strongest local options for tool selection accuracy, while Qwen 2.5 was noted as a good speed/performance tradeoff.[7]

That matters because your “big local model” should not just be smart; it must be **obedient about calling tools**. A 32B model that occasionally narrates fake actions is worse for an agent chain than a smaller model that consistently emits valid tool calls.[7][6]

## Registration workflow

A concrete workflow looks like this:

1. **Stand up the model endpoint.**  
   Example target: `http://your-mac-mini:port/v1` with an OpenAI-style `/chat/completions` interface.[5][4]

2. **Use a tool-capable instruct model.**  
   Prefer a Qwen-family instruct model first for this use case, because current local testing shows the Qwen family leading among open models for tool calling.[7]

3. **Verify tool-call behavior outside Perplexity first.**  
   Send a request with one or two declared tools, then confirm the response contains an actual structured tool call rather than prose saying it “would” use a tool.[5][6]

4. **Connect that endpoint through the integration layer Computer supports.**  
   Perplexity Computer supports connectors and also lets users bring their own tools through an MCP server URL, which is the cleanest documented way to expose proprietary or custom capabilities into Computer.[2]

5. **Set routing preferences inside Computer.**  
   Because Computer allows users to choose which models handle which subtasks, assign your local model to the sub-agent class responsible for tool execution, code/file operations, or “agent” work, and leave research/long-context tasks on cloud models if needed.[3][1][2]

## Configuration pattern

A good autonomy-first pattern on your Mac mini is:

- **Default agent/tool model:** Qwen 32B or another strong local instruct model, served locally.[8][7]
- **Default utility/router model:** small local Qwen 4B–8B for cheap checks.[7]
- **Cloud exceptions only:** research, ultra-long context, or tasks where Computer’s built-in frontier routing still clearly outperforms local.[3][1]

Example policy in plain English:

- “Use Local-Qwen-32B for file operations, shell actions, structured extraction, and all tool-calling chains.”  
- “Use Local-Qwen-8B for heartbeat checks and lightweight classification.”  
- “Escalate to cloud only for long-context synthesis or web-scale research.”[1][2][7]

## Failure testing

Before making it the default, test five cases:

- Read a local file and return a count.  
- Edit a file and confirm the diff.  
- Call two tools in sequence.  
- Refuse a nonexistent tool instead of hallucinating it.  
- Recover after a malformed tool result.[6][7]

If it fails any of those intermittently, keep it as a secondary model until the serving stack or parser configuration is fixed, because many “bad model” reports are actually bad tool-parser or endpoint-format issues.[6]

## One caution

Perplexity’s public materials clearly state that Computer can choose specific models for subtasks and that users can manually assign model roles, but they do not publicly document every UI step for registering a fully custom local model as a first-class built-in model in the same way as Perplexity-hosted models.[2][1]

So in practice, the reliable path today is usually to expose your local model through **BYO tools/MCP or an OpenAI-compatible layer that your orchestration stack can call**, then make that local endpoint the default for agent execution in your own routing policy.[4][2][5]

Would you like a **step-by-step Mac mini recipe** next, using either Ollama, LM Studio, or llama.cpp as the local endpoint?

Sources
[1] Introducing Perplexity Computer https://www.perplexity.ai/hub/blog/introducing-perplexity-computer
[2] I Tested Perplexity Computer for Weeks. Here's the PM Playbook https://www.news.aakashg.com/p/perplexity-computer-guide-product-managers
[3] Perplexity Computer: What I Built in One Night (Review ... https://karozieminski.substack.com/p/perplexity-computer-review-examples-guide
[4] LLM with function calling? Only OpenAI models have ... https://www.reddit.com/r/LocalLLaMA/comments/1cl6ocx/llm_with_function_calling_only_openai_models_have/
[5] Tools - OpenAI Agents SDK https://openai.github.io/openai-agents-python/tools/
[6] Locally hosted LLM is not able to call tools - Questions https://community.n8n.io/t/locally-hosted-llm-is-not-able-to-call-tools/138631
[7] Tool Calling with Local LLMs: A Practical Evaluation https://www.docker.com/blog/local-llm-tool-calling-a-practical-evaluation/
[8] The Best Local LLMs To Run On Every Mac (Apple Silicon) https://apxml.com/posts/best-local-llm-apple-silicon-mac
[9] Perplexity Computer for Beginners: Everything You Need to ... https://www.youtube.com/watch?v=EHpAQwXmseQ
[10] Perplexity Computer: Multi-Model AI Agent Guide https://www.digitalapplied.com/blog/perplexity-computer-multi-model-ai-agent-guide
[11] How should I choose which AI model to use for a particular task https://www.youtube.com/watch?v=Sgfb3QwWiZM
[12] Best use cases for each model? : r/perplexity_ai https://www.reddit.com/r/perplexity_ai/comments/1iq8c55/best_use_cases_for_each_model/
[13] Perplexity Launches Computer, A Multi-Model AI System ... https://pulse2.com/perplexity-launches-computer-a-multi-model-ai-system-that-creates-and-executes-entire-workflows/
[14] Perplexity Computer Complete Guide: 19 Models, 15 ... https://www.the-ai-corner.com/p/perplexity-computer-complete-guide
[15] The Ultimate Guide to Local AI and AI Agents (The Future is ... https://www.youtube.com/watch?v=mNcXue7X8H0
[16] Everything is Computer https://www.perplexity.ai/hub/blog/everything-is-computer

#Wiring Perplexity to Ollama
You can’t yet point Perplexity Computer directly at an Ollama model with “add MCP server here” in the UI, but you *can* put Qwen3.5‑27B behind an MCP‑aware bridge and then let Computer interact with that stack the same way it talks to other MCP tools. The key is: Qwen runs in Ollama, an MCP “host” process sits in front of it, and that host is what Computer (or any MCP client) connects to.[1][2]

Below is the practical way to do that on your Mac mini.

***

## Big picture: what you’re wiring up

- **Ollama**: runs `qwen3.5:27b` locally on `localhost:11434` with its chat API (`/api/chat`).[1]
- **MCP bridge/host**: a small service that exposes Ollama as an MCP model provider and can also load additional MCP servers (e.g., Zapier, filesystem, Git, etc.).[2][3]
- **Perplexity Computer**: talks to that MCP host as “the place where models + tools live” and then routes tool‑calling chains into Qwen3.5 via the host.

You’re effectively saying: “For this Computer, my MCP host is the local integration hub; its primary model is Qwen3.5‑27B on Ollama.”

***

## Step 1 – Make sure Qwen3.5‑27B is tool‑ready in Ollama

1. Pull and run the model via Ollama (you’re already doing this, but for completeness):  
   ```bash
   ollama pull qwen3.5:27b
   ollama run qwen3.5:27b
   ```  
   The model library confirms Qwen3.5 is designed for strong tool use and agentic workloads when served through frameworks like OpenClaw and Hermes agents.[1]

2. Test tool calling against Ollama’s API *before* you bring MCP into the picture.  
   - Send a `POST` to `http://localhost:11434/api/chat` with:
     - A system message that tells Qwen it can and should use tools.  
     - A `tools` block in the format your bridge expects (many bridges use OpenAI‑style `tools` schemas).  
   - Confirm Qwen3.5 responds with structured tool calls (function name + JSON args) rather than just natural language.[4]

That test is important because MCP bridges typically assume the upstream model already has good function/tool‑calling behavior; they just translate MCP tools into that model’s tool schema.[5][2]

***

## Step 2 – Choose an MCP host/bridge for Ollama

You need something that:

- Speaks **MCP on one side**.  
- Speaks **Ollama’s `/api/chat`** on the other side (or OpenAI‑compatible if you put a shim in front of Ollama).[2]

Two current options that are documented for this:

- **Dedicated Ollama↔MCP bridge** (e.g., “ollama‑mcp” type tools):  
  Guides show how to point such a bridge at `localhost:11434` and have it expose the chosen model as an MCP “model provider,” plus register any MCP servers you want as tools.[3][2]

- **General Python MCP host** using an SDK, with Ollama wired in as the model:  
  The pattern from Qwen3 + MCP tutorials is:
  - Run the model on Ollama.  
  - Write a small Python app that:
    - Talks to Ollama via HTTP,  
    - Wraps Qwen3.5 in a model abstraction that understands tools,  
    - Registers one or more MCP servers as tools,  
    - Exposes everything via MCP.[5]

Either way, you end up with an MCP host listening on a port like `localhost:8718` or similar, which Qwen3.5 uses as its tool‑aware environment.[2]

***

## Step 3 – Configure the MCP host to use Qwen3.5‑27B as its main model

In the host/bridge config you typically specify:

- The **model name** in Ollama: `"qwen3.5:27b"`.[1]
- The **Ollama URL**: `http://localhost:11434`.  
- Tool support: make sure the bridge is using either Qwen’s native function‑calling format or an OpenAI‑style format that Qwen3.5 understands.[4][5]

A typical configuration (pseudocode, but structurally accurate) looks like:

```jsonc
{
  "model": {
    "provider": "ollama",
    "model_name": "qwen3.5:27b",
    "base_url": "http://localhost:11434"
  },
  "mcp": {
    "servers": [
      {
        "id": "filesystem",
        "command": "node",
        "args": ["./node_modules/@modelcontextprotocol/server-fs/bin/cli.js", "--root", "/Users/you/Projects"]
      },
      {
        "id": "zapier",
        "command": "mcp-zapier",
        "args": ["--config", "zapier.json"]
      }
    ]
  }
}
```

The exact syntax depends on the host you choose, but you’re always telling it:

- “Use **this Ollama model** for all LLM calls.”  
- “These MCP servers are the tools you’re allowed to call.”

The tutorial video you saw referenced this pattern explicitly: Qwen3 on Ollama + MCP server config + a short Python harness to tie them together.[5]

***

## Step 4 – Point Perplexity Computer at your MCP host

Perplexity’s public docs and third‑party guides all emphasize that Computer can “bring your own tools” via MCP, and that you can select which models handle which subtasks. The missing piece is simply:[6][7][8]

- Where, in the Computer UI or config, you declare: “Here is my MCP server URL.”

The public writeups don’t show every menu and button click, but they are explicit that:

- Computer can connect to external tools and MCP servers as part of its agent environment.[7][9][6]
- You can choose specific models for specific subtasks, and override the default router when you care which model is used.[10][6][7]

Once the MCP host is reachable from the Mac mini that Computer is running on:

1. **Add the MCP server** in the Computer configuration (the same place you would connect other MCP servers such as GitHub, Zapier, or local FS; exact UI text depends on the current build).  
2. In the **model/sub‑agent settings**, assign:
   - That MCP host as the environment containing tools.  
   - Qwen3.5‑27B (as configured in the host) as the default model for “agent” or “tool‑calling” subtasks.

From Computer’s perspective, it doesn’t need to know about Ollama directly; it just knows “this MCP environment has a model I can ask to plan and call tools.”

***

## Step 5 – Sanity‑check from Computer’s side

Once wired up:

- Ask Computer to perform a **purely local task** that obviously needs filesystem or local‑tool access, like editing a file in a directory that only your MCP filesystem server exposes.  
- Watch that:
  - The request routes to your MCP host.  
  - The host uses Qwen3.5‑27B through Ollama.  
  - Tools are invoked via MCP (filesystem, Zapier, etc.).[2][5]

If Qwen responds with prose instead of tool calls, or tools aren’t triggered, the bug is in the tool‑calling configuration (system prompt or schema) between the host and Ollama, not in Computer itself.[11]

***

## Practical hints specific to Qwen3.5 + MCP

- Community experience: you **need a Qwen3‑family model**, not older Qwen 2.5 or generic Llama models, because Qwen3’s instruction tuning and system prompt patterns are explicitly optimized for tool usage. You already have that with 3.5‑27B, which is ideal.[11][4]
- Several MCP users report that adding a **specific “tool‑use enabling” system prompt snippet** is necessary with Qwen variants for them to consistently emit correct tool calls; once added, tool calling becomes reliable.[11][5]
- If you ever hit a wall with Ollama’s parser around tools, you can swap to a llama.cpp‑based server (Unsloth’s Qwen3.5‑27B GGUF + `llama-server`) and keep the rest of the MCP host configuration the same.[4][11]

***

Because the Computer UI details are evolving quickly and not all screens are documented in public blog posts, the **only part I can’t give you is the exact button labels** where you paste the MCP URL. What I can say confidently from the docs is that once you have an MCP host that exposes Qwen3.5 via MCP, Computer is designed to treat that host as just another tool/model environment and let you route subtasks to it.[9][6][7]

If you tell me whether you prefer to build the MCP host in **Python** or via an existing **off‑the‑shelf Ollama↔MCP bridge**, I can outline a very concrete configuration file and system prompt tailored to Qwen3.5‑27B on your Mac mini.

Sources
[1] qwen3.5 https://ollama.com/library/qwen3.5
[2] Ollama MCP: How to Connect Local LLMs to Any MCP Server https://www.morphllm.com/ollama-mcp
[3] Running LLMs Locally Just Got Way Better - Ollama + MCP https://www.youtube.com/watch?v=GAyNvq6Ayps
[4] Qwen3.5 - How to Run Locally https://unsloth.ai/docs/models/qwen3.5
[5] How-To Use Qwen3 with MCP and Tool-Use with Ollama https://www.youtube.com/watch?v=mNqMHG-58t4
[6] Introducing Perplexity Computer https://www.perplexity.ai/hub/blog/introducing-perplexity-computer
[7] I Tested Perplexity Computer for Weeks. Here's the PM Playbook https://www.news.aakashg.com/p/perplexity-computer-guide-product-managers
[8] Perplexity Computer Complete Guide: 19 Models, 15 ... https://www.the-ai-corner.com/p/perplexity-computer-complete-guide
[9] Everything is Computer https://www.perplexity.ai/hub/blog/everything-is-computer
[10] Perplexity Computer: Multi-Model AI Agent Guide https://www.digitalapplied.com/blog/perplexity-computer-multi-model-ai-agent-guide
[11] Unable to get MCP working using local model via Ollama https://www.reddit.com/r/mcp/comments/1kqsf02/unable_to_get_mcp_working_using_local_model_via/
[12] Ollama - OpenClaw https://docs.openclaw.ai/providers/ollama
[13] jonigl/mcp-client-for-ollama: Harness the power ... https://github.com/jonigl/mcp-client-for-ollama

#Focus on MLX Support
MLX isn’t strictly “required,” but on Apple silicon it’s the **fastest, most hardware‑native way** to run big local models like Qwen3.5‑27B, and that has very direct benefits for an always‑on agent like Perplexity Computer.[1][2][3]

***

## What MLX is

- **Apple’s tensor library for M‑series chips** (MLX and its `mlx-lm` / `mlx-vlm` tooling) is designed specifically for Apple’s unified memory and GPU architecture.[2][4]
- It can load models directly from Hugging Face (e.g., `mlx-community/Qwen3.5-27B-4bit`, `…-8bit`) and run them with quantization tuned for Macs.[5][6][2]

Compared to generic backends like llama.cpp or frameworks compiled for many targets, MLX uses Apple‑specific tricks (single address space tensors, efficient GPU/CPU sharing) to reduce copies and overhead.[3][2]

***

## Why MLX matters on a Mac mini M4 Pro

On your hardware, MLX gives you three important advantages:

1. **Speed and throughput**  
   - Users running Qwen3.5‑35B on Apple silicon report about **1.8–2× faster generation** after switching from Ollama/llama.cpp to MLX.[1]
   - Benchmarks show MLX can be **2–3× faster than llama.cpp** on M‑series Macs for many LLMs because it keeps tensors in a unified address space and drives the GPU more efficiently.[3]

   For an autonomous agent that may generate thousands of tokens per job, this is the difference between “background task finishes in minutes” vs “takes all afternoon.”

2. **Memory efficiency and bigger models**  
   - MLX is used to host quantized 27B–35B and even larger models (Qwen3.5‑27B‑4bit, Qwen3.5‑27B‑8bit) comfortably on 16–24 GB Macs; with 48 GB you have plenty of headroom.[6][5]
   - Apple‑optimized quantization (MLX‑specific 3–8‑bit formats) plus unified memory let you run a **large “agent brain”** (27B–35B) and still leave RAM for Perplexity Computer, tools, and a smaller heartbeat model.  

3. **Advanced features for future‑proofing**  
   - MLX stacks are where you see early support for things like **multi‑token prediction (MTP)** and speculative decoding for Qwen3.6, giving **1.4–2.2× speed‑ups** with no accuracy loss.[7]
   - Vision‑language support (Qwen3.5/3.6 VL) and high‑quality 4‑bit quantizations are often published first or in best form as MLX variants.[8][5][7]

For an “autonomy‑first” Perplexity Computer, those speed + capacity gains directly increase how much work you can safely push to the local model.

***

## MLX and Qwen3.5‑27B specifically

For your exact model family:

- There are **MLX‑native builds of Qwen3.5‑27B** (4‑bit, 8‑bit, GPTQ Int4) published on Hugging Face (`mlx-community/Qwen3.5-27B-4bit`, `…-8bit`, etc.).[9][5][6]
- People have already demonstrated Qwen3.5‑35B/27B running via MLX on Apple silicon and seeing ~2× speed vs Ollama, purely from switching the backend.[5][1]
- Ollama itself now ships **MLX‑backed variants** of some Qwen3.5 models (`qwen3.5:27b-mlx-bf16` and similar), which is essentially Ollama acknowledging “if you’re on a Mac, the MLX path is the high‑performance one.”[10]

So even if you stay in Ollama for convenience, picking the `…-mlx-…` variant of Qwen3.5‑27B makes Ollama use MLX under the hood for better performance on the M4.[10]

***

## Why it matters to Perplexity Computer and MCP

Computer’s agent workflows can be very **token‑intensive**:

- Multi‑step plans, long chain‑of‑thought (Qwen3.5 thinks by default with `<think>…</think>`), and tool‑heavy tasks can easily run into thousands of tokens.[11][9]
- As you lean into local autonomy, more of those chains will run on your Mac mini rather than frontier cloud models.

Using MLX here gives you:

- **Higher sustained throughput per watt** → you can keep a 27B–35B model loaded 24/7 without feeling like the machine is bogged down.[4][3]
- **Lower latency for each tool‑call step**, which compounds in long chains (e.g., a 10‑tool workflow where each step is 2× faster is very noticeable).  
- More comfortable headroom to add a **small heartbeat model** and MCP servers (filesystem, Git, Zapier, etc.) alongside the big model.

From the Computer/MCP side, MLX is just “another OpenAI‑style or custom HTTP endpoint”; the difference is that the server behind that endpoint is actually saturating your M4 GPU and memory architecture efficiently.

***

## When you absolutely want MLX

For your use case (Qwen3.5‑27B as main agent brain on a 48 GB M4 Pro), MLX support moves from “nice to have” to “strongly recommended” when:

- You want to run **one large local brain nearly all the time** (27B–35B) rather than spinning it up only occasionally.  
- You expect **long‑horizon reasoning or heavy chain‑of‑thought** (which Qwen3.5 does by default) and don’t want 5–10k tokens of reasoning to turn into prohibitive latency.[9][1]
- You care about maximizing the **useful life of this Mac mini as your local AI box**, and want access to newer features like MTP or more efficient quantizations as they land for Qwen3.6/4.0.[7][3]

In other words: you can keep Ollama as the orchestration surface (and for compatibility with MCP bridges), but using MLX‑backed Qwen builds—or moving the heavy model to a pure MLX server—makes your “local autonomy” Computer substantially more capable on the same hardware.

Would you like a minimal, concrete path next: either (a) switching your current Ollama `qwen3.5-27B` to an MLX variant, or (b) standing up a dedicated MLX HTTP server for Qwen3.5‑27B that you can then plug into your MCP host?

Sources
[1] Qwen3.5:35b on Apple Silicon: How I Got 2x Faster ... https://www.reddit.com/r/LocalLLaMA/comments/1rezq19/qwen3535b_on_apple_silicon_how_i_got_2x_faster/
[2] ml-explore/mlx-lm: Run LLMs with MLX https://github.com/ml-explore/mlx-lm
[3] Apple's MLX Runs Local LLMs 3x Faster Than llama.cpp — ... https://pub.towardsai.net/apples-mlx-runs-local-llms-3x-faster-than-llama-cpp-until-your-context-hits-40k-715ec441afbb
[4] Everything you wanted to know about Apple's MLX https://www.reddit.com/r/LocalLLaMA/comments/1l7yrni/everything_you_wanted_to_know_about_apples_mlx/
[5] mlx-community/Qwen3.5-27B-4bit https://huggingface.co/mlx-community/Qwen3.5-27B-4bit
[6] mlx-community/Qwen3.5-27B-8bit – Run On-Device with ... https://trymirai.com/local-models/mlx-community-qwen3-5-27b-8bit
[7] Qwen3.6 - How to Run Locally https://unsloth.ai/docs/models/qwen3.6
[8] froggeric/qwen3.6-27b-mlx-4bit https://lmstudio.ai/froggeric/qwen3.6-27b-mlx-4bit
[9] mlx-community/Qwen3.5-27B-GPTQ-Int4 https://huggingface.co/mlx-community/Qwen3.5-27B-GPTQ-Int4
[10] qwen3.5:27b-mlx-bf16 https://ollama.com/library/qwen3.5:27b-mlx-bf16
[11] Everything is Computer https://www.perplexity.ai/hub/blog/everything-is-computer
[12] [Feature Request] Add Qwen3.5 architecture support #1136 https://github.com/ml-explore/mlx-lm/issues/1136
[13] Run Qwen3.6 27B 2x Faster on M5 Max — Native MTP on ... https://www.youtube.com/watch?v=Bd0q3cOWY90
[14] Run Qwen3.6-27B on Mac with oMLX: Fast Setup + ... https://www.youtube.com/watch?v=pZMZ9_39308

Yes: there are MLX‑optimized Qwen3.5‑27B builds you can use as an instruct/agent model, and a pre‑built MLX server (Rapid‑MLX) is exactly what you want to sit between those weights and Perplexity Computer.[1][2][3]

***

## Qwen3.5‑27B MLX “instruct” availability

### Official MLX support for Qwen

- The Qwen team explicitly supports **MLX LM** on macOS and publishes MLX checkpoints in their org; they recommend searching Hugging Face repo names with `-MLX` to find Apple‑ready variants.[4]
- Qwen3.5‑27B itself is a **“medium” hybrid model in the 3.5 family** (27B dense) and is widely used as a general chat/agent model (not code‑only), so MLX quants of it are effectively “instruct” by design.[5][6]

### Concrete MLX variants of 27B

You have multiple MLX‑flavored 27B options:

- **Qwen3.5‑27B MLX quants**  
  - There are MLX‑optimized 4‑bit “OptiQ” variants such as `Qwen3.5-27B-OptiQ-4bit` that fit comfortably in ~15–16 GB and are positioned specifically for **long‑form reasoning** on Apple silicon.[7]
  - Community conversions like `Qwen3.5-27B-Heretic-MLX-8bit` exist as well, targeting Apple silicon with tuned sampling defaults.[8]

- **Qwen3.5‑27B in Rapid‑MLX’s model list**  
  - Rapid‑MLX ships with aliases like `qwen3.5-27b` and treats it as a **general‑purpose agent/coding model** with full tool‑calling support.[9][1]
  - Benchmarks show `qwen3.5-27b 4bit` at ~15.3 GB and ~39 tok/s on 32–36 GB M‑series desktops, explicitly recommended as a sweet spot for local coding/agent workloads.[10][1]

Functionally, those are your Qwen3.5‑27B **MLX instruct/agent models**: tuned for chat/agents, running on Apple’s MLX stack, exposed via OpenAI‑compatible servers.

***

## Pre‑built MLX server: Rapid‑MLX

Given your constraints, **Rapid‑MLX** is the most sensible pre‑built MLX server layer:

- It is an **OpenAI‑compatible local inference server** built specifically for Apple Silicon, using MLX under the hood.[2][11][10]
- It supports **Qwen3.5 and Qwen3.6 families**, including `qwen3.5-27b`, via simple aliases (`rapid-mlx serve qwen3.5-27b`).[1][9]
- Benchmarks on M‑series machines show it as **2–4× faster than Ollama** on the same models, thanks to MLX and additional optimizations.[12][9][1]

Key features that matter for Perplexity Computer:

- **OpenAI API surface**: drop‑in compatible with tools that expect `/v1/chat/completions` and `/v1/models`.[11][9]
- **Tool‑calling parsers**: Rapid‑MLX ships with 17 specialized parsers, including one for **Qwen tool‑call formats**, and hits **100% tool‑calling success** on Qwen3.5‑27B in PydanticAI/LangChain harnesses.[9][11][12]
- **Prompt cache and reasoning separation**: it can cache KV and split chain‑of‑thought reasoning into a separate field, which plays nicely with agentic setups (you can keep CoT hidden but still benefit from it).[11]

On a 48 GB M4 Pro, Rapid‑MLX’s own sizing table recommends **Qwen3.5‑27B 4‑bit** (or Qwen3.6‑35B‑A3B 4‑bit) as the realistic agent brain; with your RAM, you’re in the “local autonomy is real” tier.[10][1]

***

## Putting this together for your (B) path

Given all that, the shortest path aligned with what you asked:

1. **Install Rapid‑MLX** on the Mac mini:  
   ```bash
   pip install "rapid-mlx[vision]"
   ```  
   This gives you the server and model registry, including Qwen3.5/3.6 aliases.[9][11]

2. **Serve Qwen3.5‑27B via MLX**:  
   ```bash
   rapid-mlx serve qwen3.5-27b --port 8088
   ```  
   Rapid‑MLX will download the appropriate MLX quant (typically a 4‑bit ~15 GB variant) and expose an OpenAI‑style API with **tool calling wired for Qwen3.5**.[1][9]

3. **Front it with MCP / connect to Perplexity**:  
   - Run Rapid‑MLX either directly as a Connector in Perplexity (if/when the Mac app supports an OpenAI‑style local endpoint as a connector), or via a thin MCP client wrapper that talks to `http://localhost:8088` and is registered as a Connector in Perplexity’s **Connectors → Advanced** JSON.[13][14][11]
   - In Computer, choose that connector as the **brain for agent/tool‑calling tasks**, while leaving frontier models available for research and long‑context.

Net effect: you’re no longer running Qwen3.5‑27B through Ollama; you’re running an **MLX‑optimized 27B instruct/agent model** through Rapid‑MLX, which is measurably faster, has better tool‑calling handling, and integrates cleanly via OpenAI‑style APIs and MCP.

If you’d like, I can next draft a minimal **connector JSON skeleton** for Perplexity that assumes a `rapid-mlx` server on `localhost:8088` and shows how you’d wire it in as your “Qwen‑MLX agent” connector.

Sources
[1] 在Mac 上跑AI，Rapid-MLX 可能是目前最快的选择 https://deepseek.csdn.net/6a31f8fa10ee7a33f27e355b.html
[2] raullenchai/Rapid-MLX: The fastest local AI ... https://github.com/raullenchai/Rapid-MLX
[3] mlx-community/Qwen3.5-27B-GPTQ-Int4 https://huggingface.co/mlx-community/Qwen3.5-27B-GPTQ-Int4
[4] MLX LM - Qwen https://qwen.readthedocs.io/en/latest/run_locally/mlx-lm.html
[5] Qwen3.5 27B vs Qwen3 VL 8B Instruct https://playground.roboflow.com/models/compare/qwen3-5-27b-vs-qwen3-vl-8b-instruct
[6] Qwen3.5 - How to Run Locally https://unsloth.ai/docs/models/qwen3.5
[7] Qwen3.5 on Apple Silicon: six mlx-optiq quants https://mlx-optiq.com/docs/qwen3.5
[8] TheCluster/Qwen3.5-27B-Heretic-MLX-8bit · Hugging Face https://huggingface.co/TheCluster/Qwen3.5-27B-Heretic-MLX-8bit
[9] Rapid-MLX Review: 4x Faster Local LLM Server for Mac — andrew ... https://andrew.ooo/posts/rapid-mlx-fastest-apple-silicon-llm-server/
[10] Best Local AI Server for Mac? Rapid-MLX Install, Performance ... https://techjupjup.com/en/ai/rapid-mlx-local-ai-server/
[11] Rapid-MLX - Local AI Inference for Apple Silicon https://www.everydev.ai/tools/rapid-mlx
[12] Rapid-MLX Is 2.6x Faster Than Ollama on Apple Silicon https://awesomeagents.ai/news/rapid-mlx-local-llm-apple-silicon/
[13] Perplexity MCP Server https://docs.perplexity.ai/docs/getting-started/integrations/mcp-server
[14] How to Connect MCP Servers (Connectors) to Perplexity on Mac https://www.youtube.com/watch?v=N6zDakTSs4Y
[15] froggeric/Qwen3.6-27B-MLX-8bit https://huggingface.co/froggeric/Qwen3.6-27B-MLX-8bit
[16] Qwen3.6 - How to Run Locally https://unsloth.ai/docs/models/qwen3.6
[17] Run Qwen3.6-27B on Mac with oMLX: Fast Setup + ... https://www.youtube.com/watch?v=pZMZ9_39308
[18] Qwen3.5:35b on Apple Silicon: How I Got 2x Faster ... https://www.reddit.com/r/LocalLLaMA/comments/1rezq19/qwen3535b_on_apple_silicon_how_i_got_2x_faster/

#JSON Skeleton
Yes — for Perplexity’s **Advanced** connector form, the JSON is a flat object with `command`, `args`, and optional `env`; you do **not** wrap it in `mcpServers` because Perplexity uses the Server Name field in the UI for that outer key.[1][2]

## Minimal skeleton

Paste this into **Perplexity Mac app → Settings → Connectors → Add Connector → Advanced** after you install the local helper app.[3][4]

```json
{
  "command": "YOUR_COMMAND_HERE",
  "args": [
    "YOUR_ARG_1_HERE",
    "YOUR_ARG_2_HERE"
  ],
  "env": {}
}
```

This matches the documented shape used by Perplexity connector examples for local MCP servers.[2][4][1]

## Rapid-MLX style example

If your MCP bridge is launched by a command-line wrapper that points at a local Rapid‑MLX server on `localhost:8088`, the skeleton would look like this:

```json
{
  "command": "python3",
  "args": [
    "/Users/YOURNAME/bin/qwen_mcp_bridge.py",
    "--model-endpoint",
    "http://127.0.0.1:8088/v1"
  ],
  "env": {
    "MODEL_NAME": "qwen3.5-27b"
  }
}
```

Perplexity’s local MCP setup expects the connector entry to start a local process, and that process is what should expose the MCP tools to the app.[1][3]

## Remote MCP variant

If instead your bridge is exposed as a **remote MCP endpoint**, Perplexity examples show a pattern using `npx` with `mcp-remote` and the endpoint URL.[5]

```json
{
  "command": "npx",
  "args": [
    "-y",
    "mcp-remote",
    "https://YOUR-MCP-ENDPOINT.example.com/mcp"
  ],
  "env": {}
}
```

That is the right pattern only if you already have a remote MCP server URL; it is **not** the right format for talking directly to Rapid‑MLX’s OpenAI API.[5]

## Important distinction

Rapid‑MLX by itself is an **OpenAI-compatible inference server**, not automatically an MCP server, so Perplexity cannot consume `http://127.0.0.1:8088/v1` directly as an Advanced connector unless you put a thin MCP bridge in front of it.[6][7]

So your working path is:

- Rapid‑MLX runs Qwen locally at `localhost:8088`.[7][8]
- A small MCP bridge process starts from the connector JSON and forwards model/tool requests to Rapid‑MLX.[2][3]
- Perplexity sees only that bridge as the connector.[3]

## Recommended starter JSON

For your situation, this is the cleanest **placeholder skeleton** to work from:

```json
{
  "command": "python3",
  "args": [
    "/Users/YOURNAME/mcp/qwen-rapid-mlx-bridge.py",
    "--rapid-mlx-url",
    "http://127.0.0.1:8088/v1",
    "--model",
    "qwen3.5-27b"
  ],
  "env": {}
}
```

Use any Server Name you want in the UI, such as `Qwen3.5-27B MLX`.[1][2]

## What you still need

Before this will run, you need one actual executable bridge script or package because Perplexity connectors launch **processes**, not raw HTTP model endpoints.[2][3]

The next practical step is to define that bridge in one of two ways:

- A **Python MCP bridge** that talks to Rapid‑MLX over OpenAI API.  
- A prebuilt **remote MCP wrapper** if your chosen MLX server package already exposes MCP.

Would you like me to draft the **matching Python bridge stub** next, so the JSON points to something real?

Sources
[1] How to Connect MCP Servers (Connectors) to Perplexity on ... https://www.youtube.com/watch?v=N6zDakTSs4Y
[2] Shadcn MCP for Perplexity Desktop https://www.shadcn.io/mcp/perplexity
[3] Local and Remote MCPs for Perplexity https://www.perplexity.ai/help-center/en/articles/11502712-local-and-remote-mcps-for-perplexity
[4] Set Up a Local MCP Server for Perplexity (macOS Guide) https://dev.to/moefqy/set-up-a-local-mcp-server-for-perplexity-macos-guide-548m
[5] Install MCP Integration - Perplexity Desktop - The Cleanup Crew https://cleanupcrew.ai/install?tool=perplexity-desktop
[6] raullenchai/Rapid-MLX: The fastest local AI ... https://github.com/raullenchai/Rapid-MLX
[7] Rapid-MLX Review: 4x Faster Local LLM Server for Mac — andrew ... https://andrew.ooo/posts/rapid-mlx-fastest-apple-silicon-llm-server/
[8] 在Mac 上跑AI，Rapid-MLX 可能是目前最快的选择 https://deepseek.csdn.net/6a31f8fa10ee7a33f27e355b.html
[9] mcp-perplexity - PyPI https://pypi.org/project/mcp-perplexity/0.3.3/
[10] File App Connectors for Perplexity Pro subscribers https://www.perplexity.ai/help-center/en/articles/11185364-file-app-connectors-for-perplexity-pro-subscribers
[11] perplexity-mcp MCP server — MCP Registry - drio https://www.getdrio.com/mcp/perplexity-mcp-jsonallen
[12] App Connectors | Perplexity Help Center https://www.perplexity.ai/help-center/en/collections/15347354-app-connectors
[13] Official Perplexity MCP Server https://www.pulsemcp.com/servers/perplexity
[14] perplexity-mcp-server/mcp-config.json.example at main · cyanheads/perplexity-mcp-server https://github.com/cyanheads/perplexity-mcp-server/blob/main/mcp-config.json.example
[15] Integrate JSON and Perplexity AI to create automation https://buildship.com/integrations/apps/json-and-perplexity
[16] package.json - Sukarth/perplexity-web-mcp-bridge · GitHub https://github.com/Sukarth/perplexity-web-mcp-bridge/blob/main/package.json
[17] perplexity-ai-app/package.json at main · inulute/perplexity-ai-app https://github.com/inulute/perplexity-ai-app/blob/main/package.json
[18] Perplexity Ask MCP Server https://github.com/perplexityai/modelcontextprotocol

#Python Stub for MCP
Yes — here is a minimal **Python MCP bridge stub** that Perplexity can launch over stdio, plus the matching connector JSON. Perplexity’s Advanced connector launches a local process using `command` + `args`, and stdio is the standard pattern for local MCP servers in the Python SDK ecosystem.[1][2][3][4]

## Files and connector

Create a file such as `/Users/YOURNAME/mcp/qwen_rapid_mlx_bridge.py` with this content:

```python
from mcp.server.fastmcp import FastMCP
import os
import json
import requests

mcp = FastMCP("Qwen Rapid-MLX Bridge")

RAPID_MLX_URL = os.environ.get("RAPID_MLX_URL", "http://127.0.0.1:8088/v1")
MODEL_NAME = os.environ.get("MODEL_NAME", "qwen3.5-27b")


def _chat(messages, tools=None, tool_choice="auto"):
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False
    }
    if tools:
        payload["tools"] = tools
        payload["tool_choice"] = tool_choice

    r = requests.post(
        f"{RAPID_MLX_URL}/chat/completions",
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload),
        timeout=120
    )
    r.raise_for_status()
    return r.json()


@mcp.tool()
def qwen_chat(prompt: str) -> str:
    """Send a plain prompt to the local Qwen model via Rapid-MLX and return the text response."""
    result = _chat([{"role": "user", "content": prompt}])
    msg = result["choices"][0]["message"]
    return msg.get("content", "")


@mcp.tool()
def qwen_tool_test(prompt: str) -> str:
    """Test whether the local Qwen model returns structured tool-call capable output."""
    tools = [
        {
            "type": "function",
            "function": {
                "name": "echo_tool",
                "description": "Echo back the provided text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string"}
                    },
                    "required": ["text"]
                }
            }
        }
    ]

    messages = [
        {
            "role": "system",
            "content": "If a tool is available and useful, call it instead of describing what you would do."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    result = _chat(messages, tools=tools, tool_choice="auto")
    msg = result["choices"][0]["message"]

    if "tool_calls" in msg and msg["tool_calls"]:
        return json.dumps(msg["tool_calls"], indent=2)

    return msg.get("content", "")


if __name__ == "__main__":
    mcp.run()
```

This follows the documented Python MCP pattern: define tools with `FastMCP`, then let the host communicate with the server over stdio when it launches the script.[2][5][6]

Use this connector JSON in Perplexity Advanced:

```json
{
  "command": "python3",
  "args": [
    "/Users/YOURNAME/mcp/qwen_rapid_mlx_bridge.py"
  ],
  "env": {
    "RAPID_MLX_URL": "http://127.0.0.1:8088/v1",
    "MODEL_NAME": "qwen3.5-27b"
  }
}
```

That shape matches Perplexity’s Advanced connector format: a flat object with `command`, `args`, and optional `env`.[4][7]

## What this bridge does

This stub does **not** make Rapid‑MLX itself into an MCP server; instead, it creates a small local MCP server that exposes a couple of tools, and those tools call your Rapid‑MLX OpenAI‑compatible endpoint underneath.[8][9][2]

In other words:

- Perplexity talks MCP over stdio to `qwen_rapid_mlx_bridge.py`.[3][1]
- The bridge talks HTTP to `http://127.0.0.1:8088/v1/chat/completions` on Rapid‑MLX.[9][10]
- Qwen3.5‑27B answers locally through MLX.[10][11]

## What it is good for

This minimal version is mainly a **proof-of-plumbing** bridge:

- `qwen_chat` verifies that Perplexity can launch a local MCP server and get a local-model answer back.[2][3]
- `qwen_tool_test` verifies that your Rapid‑MLX Qwen endpoint can emit tool-call shaped JSON when tools are supplied in OpenAI format, which Rapid‑MLX specifically supports for Qwen3.5/3.6 models.[12][8]

It is not yet a full “Computer brain” because the model is still wrapped as tools callable by Perplexity, rather than Perplexity directly delegating all planning to that model.

## Next step for a fuller bridge

If you want to go one level further, the next bridge version should add:

- A real **filesystem MCP tool** or passthrough to another MCP server.[13][14]
- A loop that:
  1. Sends available tools to Qwen via Rapid‑MLX,  
  2. Detects returned `tool_calls`,  
  3. Executes the selected MCP tool,  
  4. Sends the tool result back to Qwen,  
  5. Returns the final answer.  

That is the standard OpenAI‑plus‑MCP interaction model shown in MCP Python examples.[5][15]

## Small install note

This script assumes you install:

```bash
pip install "mcp[cli]" requests
```

The MCP Python SDK documents `FastMCP` server construction and stdio usage for local subprocess-style integration.[1][2]

Would you like me to draft the **second-stage version** that includes a real filesystem tool and a proper tool-call execution loop?

Sources
[1] Modelcontextprotocol/python-sdk https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/clients/stdio_client.py
[2] Building your server https://modelcontextprotocol.io/docs/develop/build-server
[3] Local and Remote MCPs for Perplexity https://www.perplexity.ai/help-center/en/articles/11502712-local-and-remote-mcps-for-perplexity
[4] Shadcn MCP for Perplexity Desktop https://www.shadcn.io/mcp/perplexity
[5] Hands-on MCP: An Introduction to Building MCP Servers with Python https://zenn.dev/shineos/articles/mcp-server-building-tutorial?locale=en
[6] Building Model Context Protocol (MCP) Servers with stdio https://dev.to/elsayed85/building-model-context-protocol-mcp-servers-with-stdio-a-complete-guide-513k
[7] How to Connect MCP Servers (Connectors) to Perplexity on ... https://www.youtube.com/watch?v=N6zDakTSs4Y
[8] raullenchai/Rapid-MLX: The fastest local AI ... https://github.com/raullenchai/Rapid-MLX
[9] Rapid-MLX Review: 4x Faster Local LLM Server for Mac — andrew ... https://andrew.ooo/posts/rapid-mlx-fastest-apple-silicon-llm-server/
[10] 在Mac 上跑AI，Rapid-MLX 可能是目前最快的选择 https://deepseek.csdn.net/6a31f8fa10ee7a33f27e355b.html
[11] MLX LM - Qwen https://qwen.readthedocs.io/en/latest/run_locally/mlx-lm.html
[12] Rapid-MLX - Local AI Inference for Apple Silicon https://www.everydev.ai/tools/rapid-mlx
[13] openai-mcp-agents - PyPI https://pypi.org/project/openai-mcp-agents/
[14] chuk-mcp-runtime · PyPI https://pypi.org/project/chuk-mcp-runtime/0.2.1/
[15] GitHub - Robinson777-prog/mcp-server: 4-openai-integration https://github.com/Robinson777-prog/mcp-server
[16] Build an MCP client https://modelcontextprotocol.io/docs/develop/build-client
[17] MCP Servers - OpenAI Agents SDK https://www.aidoczh.com/openai-agents-python/ref/mcp/server/index.html
[18] Discovering MCP Servers in Python | CodeSignal Learn https://codesignal.com/learn/courses/developing-and-integrating-a-mcp-server-in-python/lessons/getting-started-with-fastmcp-running-your-first-mcp-server-with-stdio-and-sse
[19] Practical Guide to MCP (Model Context Protocol) in Python https://dev.to/m_sea_bass/practical-guide-to-mcp-model-context-protocol-in-python-ijd
[20] FastMCP Examples: Build Python MCP Servers for LLM Tools https://mcpmarket.com/server/fastmcp-examples
[21] Integrating MCP Servers to an OpenAI Agent | CodeSignal Learncodesignal.com › learn › courses › lessons › integrating-the-mcp-server-wit... https://codesignal.com/learn/courses/developing-and-integrating-a-mcp-server-in-python/lessons/integrating-the-mcp-server-with-an-openai-agent
[22] python-sdk/examples/snippets/servers/lowlevel/basic.py at ... https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/lowlevel/basic.py
[23] MCP - Model Context Protocol - Client | Python & OpenAI https://www.youtube.com/watch?v=uzMSzStbvz4

#Local MCP Server With Tools
Yes — the next useful version is a **local MCP server with real tools** such as filesystem read/write, while also exposing your Rapid‑MLX/Qwen endpoint as a planning helper. Perplexity’s Mac app can run local MCP servers, and filesystem access is one of the supported use cases it explicitly calls out.[1][2]

## Better bridge design

The clean design is:

- Perplexity launches your local MCP server over **stdio**.[3][1]
- That server exposes actual tools like `read_file`, `write_file`, and `list_dir` using FastMCP’s normal tool pattern.[4][5]
- One extra tool, `qwen_plan`, sends prompts to your Rapid‑MLX server so Perplexity can use the local Qwen model for planning or summarizing file results.[6][7]

That is simpler and more reliable than trying to build a recursive “LLM calls MCP which calls LLM which calls MCP” loop inside one first draft.

## Bridge stub

Use this as `/Users/YOURNAME/mcp/qwen_filesystem_bridge.py`:

```python
from mcp.server.fastmcp import FastMCP
from pathlib import Path
import os
import json
import requests

mcp = FastMCP("Qwen Filesystem Bridge")

ROOT = Path(os.environ.get("MCP_ROOT", str(Path.home()))).resolve()
RAPID_MLX_URL = os.environ.get("RAPID_MLX_URL", "http://127.0.0.1:8088/v1")
MODEL_NAME = os.environ.get("MODEL_NAME", "qwen3.5-27b")


def safe_path(rel_path: str) -> Path:
    p = (ROOT / rel_path).resolve()
    if ROOT not in p.parents and p != ROOT:
        raise ValueError(f"Path escapes MCP_ROOT: {rel_path}")
    return p


def chat_qwen(messages):
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False
    }
    r = requests.post(
        f"{RAPID_MLX_URL}/chat/completions",
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload),
        timeout=120
    )
    r.raise_for_status()
    data = r.json()
    return data["choices"][0]["message"].get("content", "")


@mcp.tool()
def list_dir(rel_path: str = ".") -> str:
    """List files and directories under a relative path inside MCP_ROOT."""
    p = safe_path(rel_path)
    if not p.exists():
        return f"Path does not exist: {rel_path}"
    if not p.is_dir():
        return f"Not a directory: {rel_path}"
    items = []
    for child in sorted(p.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower())):
        kind = "dir" if child.is_dir() else "file"
        items.append(f"{kind}\t{child.relative_to(ROOT)}")
    return "\n".join(items)


@mcp.tool()
def read_file(rel_path: str, max_chars: int = 12000) -> str:
    """Read a UTF-8 text file under MCP_ROOT."""
    p = safe_path(rel_path)
    if not p.exists():
        return f"File does not exist: {rel_path}"
    if not p.is_file():
        return f"Not a file: {rel_path}"
    text = p.read_text(encoding="utf-8")
    return text[:max_chars]


@mcp.tool()
def write_file(rel_path: str, content: str, overwrite: bool = False) -> str:
    """Write a UTF-8 text file under MCP_ROOT."""
    p = safe_path(rel_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists() and not overwrite:
        return f"Refusing to overwrite existing file: {rel_path}"
    p.write_text(content, encoding="utf-8")
    return f"Wrote {len(content)} chars to {rel_path}"


@mcp.tool()
def append_file(rel_path: str, content: str) -> str:
    """Append UTF-8 text to a file under MCP_ROOT."""
    p = safe_path(rel_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as f:
        f.write(content)
    return f"Appended {len(content)} chars to {rel_path}"


@mcp.tool()
def qwen_plan(task: str, context: str = "") -> str:
    """Ask the local Qwen model to produce a concise plan or analysis."""
    messages = [
        {
            "role": "system",
            "content": "You are a concise local planning assistant. Prefer short, actionable answers."
        },
        {
            "role": "user",
            "content": f"Task:\n{task}\n\nContext:\n{context}"
        }
    ]
    return chat_qwen(messages)


if __name__ == "__main__":
    mcp.run()
```

FastMCP automatically turns decorated Python functions into MCP tools, and Perplexity’s Mac app can run local MCP servers as commands once the helper is installed.[5][1][4]

## Connector JSON

Use this in Perplexity **Advanced**:

```json
{
  "command": "python3",
  "args": [
    "/Users/YOURNAME/mcp/qwen_filesystem_bridge.py"
  ],
  "env": {
    "MCP_ROOT": "/Users/YOURNAME/Documents",
    "RAPID_MLX_URL": "http://127.0.0.1:8088/v1",
    "MODEL_NAME": "qwen3.5-27b"
  }
}
```

Perplexity’s connector UI expects a flat `command` / `args` / `env` object, and then you enable that MCP under **Sources** when you want it available in a conversation.[8][1]

## Why this version is better

This second-stage version gives you something immediately useful:

- Perplexity can **list, read, write, and append** files in a controlled directory on your Mac through MCP.[2][1]
- It can also call your **local Qwen model** for planning against those files via Rapid‑MLX.[7][9]
- You keep the security boundary tight by restricting access to `MCP_ROOT`, which matches Perplexity’s local-MCP model of exposing only a subset of local resources.[1]

## What it still does not do

It still does **not** make Qwen the global hidden planner inside Perplexity Computer. Instead, it gives Perplexity explicit MCP tools, one of which is “ask my local Qwen model.” That is the practical pattern supported by Perplexity’s local MCP mechanism today.[2][1]

To go beyond this, you would typically add more domain tools:

- `search_notes` for Obsidian vaults.  
- `run_sql` for DuckDB.  
- `git_status` / `git_diff` for repositories.  
- `summarize_file_with_qwen` as a higher-level convenience wrapper.

## Install notes

You’ll need:

```bash
pip install fastmcp requests
```

FastMCP is a widely used Pythonic way to build MCP servers, and the Perplexity Mac app simply needs a runnable local command that exposes tools over stdio.[5][1]

Would you like the next step to be an **Obsidian + DuckDB version** of this bridge, since that seems closer to your actual working environment?

Sources
[1] Local and Remote MCPs for Perplexity https://www.perplexity.ai/help-center/en/articles/11502712-local-and-remote-mcps-for-perplexity
[2] Local and Remote MCPs for Perplexity https://www.perplexity.ai/help-center/en/articles/11502712-local-and-remote-mcps-for-perplexity.html
[3] Building your server https://modelcontextprotocol.io/docs/develop/build-server
[4] PrefectHQ/fastmcp: 🚀 The fast, Pythonic way to build MCP ... https://github.com/prefecthq/fastmcp
[5] PrefectHQ/fastmcp: 🚀 The fast, Pythonic way to build MCP ... https://github.com/PrefectHQ/fastmcp
[6] raullenchai/Rapid-MLX: The fastest local AI ... https://github.com/raullenchai/Rapid-MLX
[7] Rapid-MLX Review: 4x Faster Local LLM Server for Mac — andrew ... https://andrew.ooo/posts/rapid-mlx-fastest-apple-silicon-llm-server/
[8] Shadcn MCP for Perplexity Desktop https://www.shadcn.io/mcp/perplexity
[9] 在Mac 上跑AI，Rapid-MLX 可能是目前最快的选择 https://deepseek.csdn.net/6a31f8fa10ee7a33f27e355b.html
[10] filesystem - FastMCP https://gofastmcp.com/python-sdk/fastmcp-server-providers-filesystem
[11] FastMCP Filesystem Provider Setup - Part 9/9 https://www.youtube.com/watch?v=FIjkm1vF84I
[12] Trying Out MCP? Here's How I Built a Local Server Using ... https://medium.com/@noopurtiwari01/trying-out-mcp-heres-how-i-built-a-local-server-using-python-and-fastmcp-0364ca5068b6
[13] Perplexity AI MCP server Integration https://www.youtube.com/watch?v=jePIkhFSwXo
[14] filesystem https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_server_config-v1-sources-filesystem
[15] The FastMCP Client https://gofastmcp.com/clients/client
[16] Perplexity Using MCP Filesystem https://www.youtube.com/watch?v=O7g-RkihOvs
[17] MCP Python SDK https://pypi.org/project/mcp/1.2.1/
[18] Perplexity MCP Zerver Server https://mcpservers.org/servers/wysh3/perplexity-mcp-server
[19] Building and deploying a Python MCP server with ... https://circleci.com/blog/building-and-deploying-a-python-mcp-server-with-fastmcp/
[20] GitHub - fastmcp-me/fastmcp-python: 🚀 The fast, Pythonic way to build MCP servers and clients https://github.com/fastmcp-me/fastmcp-python

#Integration With Obsidian and Duckdb
Yes — the most practical pattern is one MCP server that exposes three families of tools: **Obsidian vault tools**, **DuckDB query tools**, and an optional **Qwen local planner** backed by Rapid‑MLX. That fits Perplexity’s local MCP model well because it can securely reach files and databases on your Mac through a helper-launched local server.[1][2][3][4]

## Architecture

Use one local MCP server with:

- `search_obsidian`, `read_note`, `write_note` for your vault.  
- `duckdb_query`, `duckdb_tables`, `duckdb_describe` for your database.  
- `qwen_plan` for local synthesis/planning via your MLX endpoint.[2][3]

This keeps the interface simple for Perplexity while matching your actual working stack of Obsidian plus DuckDB.[1]

## Python bridge

Create `/Users/YOURNAME/mcp/obsidian_duckdb_bridge.py`:

```python
from mcp.server.fastmcp import FastMCP
from pathlib import Path
import os
import json
import requests
import duckdb

mcp = FastMCP("Obsidian DuckDB Bridge")

VAULT_ROOT = Path(os.environ.get("OBSIDIAN_VAULT", str(Path.home() / "Documents"))).resolve()
DUCKDB_PATH = os.environ.get("DUCKDB_PATH", str(Path.home() / "data.duckdb"))
RAPID_MLX_URL = os.environ.get("RAPID_MLX_URL", "http://127.0.0.1:8088/v1")
MODEL_NAME = os.environ.get("MODEL_NAME", "qwen3.5-27b")


def safe_vault_path(rel_path: str) -> Path:
    p = (VAULT_ROOT / rel_path).resolve()
    if VAULT_ROOT not in p.parents and p != VAULT_ROOT:
        raise ValueError(f"Path escapes OBSIDIAN_VAULT: {rel_path}")
    return p


def chat_qwen(messages):
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False
    }
    r = requests.post(
        f"{RAPID_MLX_URL}/chat/completions",
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload),
        timeout=120
    )
    r.raise_for_status()
    data = r.json()
    return data["choices"][0]["message"].get("content", "")


def run_duckdb(sql: str, limit: int = 200):
    con = duckdb.connect(DUCKDB_PATH, read_only=False)
    try:
        wrapped = f"SELECT * FROM ({sql}) AS q LIMIT {limit}"
        rows = con.execute(wrapped).fetchall()
        cols = [d[0] for d in con.description]
        return {"columns": cols, "rows": rows}
    finally:
        con.close()


@mcp.tool()
def search_obsidian(query: str, max_results: int = 20) -> str:
    """Search markdown notes in the Obsidian vault by filename and content."""
    results = []
    q = query.lower()

    for path in VAULT_ROOT.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        score = 0
        if q in path.name.lower():
            score += 3
        if q in text.lower():
            score += 1

        if score > 0:
            results.append((score, path.relative_to(VAULT_ROOT), text[:400]))

    results.sort(key=lambda x: (-x[0], str(x[1]).lower()))
    results = results[:max_results]

    if not results:
        return "No matching notes found."

    lines = []
    for score, rel_path, snippet in results:
        lines.append(f"{rel_path} [score={score}]")
        lines.append(snippet.replace("\n", " ")[:300])
        lines.append("")
    return "\n".join(lines).strip()


@mcp.tool()
def read_note(rel_path: str, max_chars: int = 16000) -> str:
    """Read a markdown note from the Obsidian vault."""
    p = safe_vault_path(rel_path)
    if not p.exists():
        return f"Note does not exist: {rel_path}"
    if not p.is_file():
        return f"Not a file: {rel_path}"
    return p.read_text(encoding="utf-8", errors="ignore")[:max_chars]


@mcp.tool()
def write_note(rel_path: str, content: str, overwrite: bool = False) -> str:
    """Write a markdown note into the Obsidian vault."""
    p = safe_vault_path(rel_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists() and not overwrite:
        return f"Refusing to overwrite existing note: {rel_path}"
    p.write_text(content, encoding="utf-8")
    return f"Wrote note: {rel_path} ({len(content)} chars)"


@mcp.tool()
def append_note(rel_path: str, content: str) -> str:
    """Append text to a markdown note in the Obsidian vault."""
    p = safe_vault_path(rel_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as f:
        f.write(content)
    return f"Appended to note: {rel_path} ({len(content)} chars)"


@mcp.tool()
def duckdb_tables() -> str:
    """List tables and views in the DuckDB database."""
    sql = """
    SELECT table_schema, table_name
    FROM information_schema.tables
    WHERE table_schema NOT IN ('pg_catalog', 'information_schema')
    ORDER BY table_schema, table_name
    """
    result = run_duckdb(sql, limit=500)
    lines = [f"{r[0]}.{r[1]}" for r in result["rows"]]
    return "\n".join(lines) if lines else "No tables found."


@mcp.tool()
def duckdb_describe(table_name: str) -> str:
    """Describe columns for a given table or view."""
    con = duckdb.connect(DUCKDB_PATH, read_only=False)
    try:
        rows = con.execute(f"DESCRIBE {table_name}").fetchall()
        return "\n".join(" | ".join(str(x) for x in row) for row in rows)
    finally:
        con.close()


@mcp.tool()
def duckdb_query(sql: str, limit: int = 200) -> str:
    """Run a SELECT query against DuckDB and return JSON rows."""
    result = run_duckdb(sql, limit=limit)
    cols = result["columns"]
    rows = [dict(zip(cols, row)) for row in result["rows"]]
    return json.dumps(rows, ensure_ascii=False, indent=2, default=str)


@mcp.tool()
def qwen_plan(task: str, context: str = "") -> str:
    """Ask the local Qwen model to produce a concise plan, summary, or synthesis."""
    messages = [
        {
            "role": "system",
            "content": "You are a concise research and planning assistant. Be specific, structured, and brief."
        },
        {
            "role": "user",
            "content": f"Task:\n{task}\n\nContext:\n{context}"
        }
    ]
    return chat_qwen(messages)


if __name__ == "__main__":
    mcp.run()
```

FastMCP automatically exposes decorated Python functions as MCP tools, which is exactly the lightweight pattern used for custom knowledge-work servers.[3][2]

## Connector JSON

Use this in **Perplexity Mac app → Settings → Connectors → Add Connector → Advanced**:[1]

```json
{
  "command": "python3",
  "args": [
    "/Users/YOURNAME/mcp/obsidian_duckdb_bridge.py"
  ],
  "env": {
    "OBSIDIAN_VAULT": "/Users/YOURNAME/Documents/ObsidianVault",
    "DUCKDB_PATH": "/Users/YOURNAME/data/research.duckdb",
    "RAPID_MLX_URL": "http://127.0.0.1:8088/v1",
    "MODEL_NAME": "qwen3.5-27b"
  }
}
```

Perplexity’s Advanced connector format is a flat JSON object with `command`, `args`, and optional `env` variables for the launched local process.[5][1]

## What this enables

Once enabled in Perplexity, you can issue prompts like:

- “Search my Obsidian vault for notes about hybrid retrieval and summarize the best three.”  
- “List DuckDB tables and inspect anything related to analyst briefings.”  
- “Query the `vendor_history` table for DEC references, then draft a note into Obsidian.”  

Those are good fits for MCP because Perplexity can orchestrate local files and databases without needing direct shell access, while keeping the data flow narrowly scoped to the tools you expose.[4][3][1]

## Recommended refinements

For your environment, I would refine this in four ways:

- Restrict `duckdb_query` to **SELECT/CTE only** for safety.  
- Add `search_obsidian_regex` or tag-aware search for frontmatter and `[[wikilinks]]`.  
- Add `duckdb_export_csv` for moving query results into your document workflow.  
- Add `summarize_note_with_qwen` and `synthesize_query_with_qwen` wrappers so Perplexity can ask the local model for structured summaries without repeating glue steps.[3]

## Useful alternative

DuckDB now also has a **community MCP extension** that can attach to MCP servers or publish database resources using the `mcp://` scheme, which is interesting if you later want DuckDB itself to participate more directly in your MCP fabric rather than only sitting behind Python tools.[6]

Would you like me to tighten this into a **safer production version** with SELECT-only SQL, frontmatter/tag search, and CSV export?

Sources
[1] Local and Remote MCPs for Perplexity https://www.perplexity.ai/help-center/en/articles/11502712-local-and-remote-mcps-for-perplexity
[2] PrefectHQ/fastmcp: 🚀 The fast, Pythonic way to build MCP ... https://github.com/PrefectHQ/fastmcp
[3] Building a Knowledge Work Stack with FastMCP https://www.prefect.io/blog/building-a-knowledge-work-stack-with-fastmcp-instead-of-microsoft-office
[4] Local and Remote MCPs for Perplexity https://www.perplexity.ai/help-center/en/articles/11502712-local-and-remote-mcps-for-perplexity.html
[5] Shadcn MCP for Perplexity Desktop https://www.shadcn.io/mcp/perplexity
[6] duckdb_mcp – DuckDB Community Extensions https://duckdb.org/community_extensions/extensions/duckdb_mcp.html
[7] AI编程_claude中的MCP_duckdb - 辰令- 博客园 https://www.cnblogs.com/ytwang/p/19660405
[8] filesystem https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_server_config-v1-sources-filesystem
[9] GitHub - ochsec/mcp-perplexity: MCP Server for the Perplexity API. https://github.com/ochsec/mcp-perplexity
[10] mcp-server-duckdb-fastmcp 1.1.1 on PyPI - Libraries.io https://libraries.io/pypi/mcp-server-duckdb-fastmcp
[11] FastMCP Filesystem Provider Setup - Part 2/9 https://www.youtube.com/watch?v=wBYnUGXyYp4
[12] Perplexity AI MCP server Integration https://www.youtube.com/watch?v=jePIkhFSwXo
[13] FastMCP Filesystem Provider Setup - Part 8/9 https://www.youtube.com/watch?v=Km58am3EfUU
[14] Perplexity MCP Server https://docs.perplexity.ai/docs/getting-started/integrations/mcp-server
[15] Filesystem Provider https://gofastmcp.com/servers/providers/filesystem
[16] MCP Tutorial (Clearly Explained) - Claude Desktop, Perplexity, Notion & Filesystem https://www.youtube.com/watch?v=0-0BR3H28ic
[17] FastMCP — the best way to build an MCP server with Python https://www.youtube.com/watch?v=rnljvmHorQw

