---
name: florida-changes
description: "Cache new evidence and required edits for Pete Kastner's FLORIDA System archive into PENDING-CHANGES.md instead of editing the published papers immediately. Use whenever new FLORIDA material arrives — a records-request response, an Auditor General or DOAH report, a court document, press coverage, an OCR of a scan, or Kastner's own analytical observation — and whenever he says 'log this', 'add to pending', 'run the pending changes', 'do the sweep', or asks what is outstanding on the FLORIDA archive. Prevents expensive per-item propagation across eight papers by batching corrections into scheduled sweeps."
license: MIT
metadata:
  author: peter-s-kastner
  version: '1.2'
  perplexity:
    connectors:
      - id: github_mcp_direct
        reason: The canonical archive lives in shorttack/aberdeen-group-archive; sweeps may need to read or commit there.
---

# FLORIDA Pending Changes

## Why this exists

The FLORIDA System archive is eight published papers plus a README, a SOURCES file, a chronology, a collection plan, and a records-requests log. A single new fact — a corrected attribution, a superseded cost figure — can touch five of them.

Propagating each fact as it arrives is expensive and produces inconsistent state, because a partial propagation leaves some files saying the old thing. Batching is cheaper and auditable: one pass, one date, one report of what could not be resolved.

**The default is: file it, log it, stop.** Editing published papers happens only on an explicit sweep instruction, or under the narrow exception in § 3.

## When to Use This Skill

Load when:

- New FLORIDA material arrives in any form — a records-request response, an audit report, a court filing, press coverage, an OCR of a scan, a mirrored source, an attachment.
- Kastner makes an analytical observation about the FLORIDA record that the archive should hold.
- He says any of: "log this," "add to pending," "cache that," "run the pending changes," "do the sweep," "what's outstanding."
- You are about to edit a published FLORIDA paper for any reason. Check the log first; the edit may belong in a sweep, and the log may already contain a conflicting pending item.

Do not load for FLORIDA work that creates no new claim and changes no existing one — reading a document to answer a question, drafting a records request, mirroring a source that only confirms what is already cited.

## The file

`~/Desktop/Archive/FLORIDA/PENDING-CHANGES.md`

Working scaffolding. Excluded from any GitHub push unless a deliberate decision is made to publish the archive's revision history.

Its sections, in order:

| § | Contents |
|---|---|
| 0 | **Blockers.** Conditions that make a sweep unsafe. Currently: two divergent copies of the corpus |
| 1 | How to read the table |
| 2 | **Pending** — three sub-tables: corrections to claims in print, new documentary facts, records-request state |
| 3 | Open questions the evidence raises. Research leads, not edits |
| 4 | Standing items not arising from new evidence |
| 5 | **Applied** — rows retired with their date |

## 1. On receiving new information

Do these three things and stop.

**Step 1 — File the source material.**

| Material | Destination |
|---|---|
| Source PDFs | `~/Desktop/Archive/FLORIDA/PDFs/` — Auditor General reports under `PDFs/auditor-general/` |
| OCR transcriptions | `sources/auditor-general/` or the appropriate `sources/` subdirectory, as `<number>.md` |
| Long structured extractions | `_working/` |
| Manifest entries | Update the manifest in the destination folder |

Scanned PDFs need OCR before they are useful. **OCR runs on Pete's Mac, never in the sandbox.** See § 1a.

### 1a. OCR — always local

**Standard, set August 24, 2026: OCR happens on the Mac.** Sandbox OCR costs credits for every page rendered and every page recognized, and it produces a worse artifact. The Mac has Tesseract 5.5.3, ocrmypdf 17.8.1, and Poppler already installed, twelve cores, and no per-page cost. Do not render PDFs to PNG in the sandbox and do not run Tesseract there. If the Mac is unreachable, say so and ask rather than silently falling back.

**The tool:** `~/Desktop/Archive/scripts/ocr_pdf_v1.sh`

```
ocr_pdf_v1.sh [-o DIR] [-j JOBS] [-p PARALLEL] [-l LANG] [-f] FILE_OR_DIR ...
```

Generalized from Pete's `~/ocr_run.sh`, which had its four inputs hardcoded. Same pipeline: ocrmypdf with `--skip-text --oversample 300 --optimize 1 --output-type pdf`, then per-page `pdftotext -layout` into Markdown with `## Page N` markers. Defaults are 3 files in parallel at 4 jobs each, tuned for the 12-core M4 Pro.

Per input it emits:

| File | Use |
|---|---|
| `<base>_ocr.pdf` | Searchable PDF — original images with a text layer. **This is the artifact to keep.** It makes the scan greppable and quotable forever; sandbox OCR never produced one |
| `<base>.md` | Page-marked text in **reading order**. The default for reading and extraction |
| `<base>.layout.md` | Page-marked text with column geometry preserved. For tabular pages only |
| `<base>.sidecar.txt` | Raw Tesseract output; the source of `.md` |
| `<base>.log`, `_manifest.tsv` | Run log and one row per file |

**Why two text files, and why this matters.** These reports are two-column. `pdftotext -layout` preserves the geometry, which is correct for tables and actively wrong for prose — it interleaves the left and right columns onto the same physical line, producing sentences like "ation system that provides information and of controls relevant to the financial settlement of the." The first version of this script shipped with that defect and it was caught only by reading the output rather than trusting the exit code. Tesseract's own page segmentation gets reading order right, and ocrmypdf hands it over via `--sidecar` at no extra cost. **Verified August 24, 2026** on a six-page two-column report: 6 seconds, reading order clean, layout variant retained for the settlement tables.

**Always read a sample of the output before using it.** Exit code zero means the pipeline ran, not that the text is usable.

**The permission constraint that shapes the whole workflow.** The bridge's shell cannot write anywhere under `/Users/scott` — not the Desktop, not the home directory. It can write `/tmp`. `pc push` is unaffected and can write into the archive. So:

1. `pc bash 'bash ~/Desktop/Archive/scripts/ocr_pdf_v1.sh <input.pdf>'` — output lands in `/tmp/ocr_out`
2. `pc pull /tmp/ocr_out/<base>.md` into the sandbox
3. `pc push` the Markdown to `sources/...` and the `_ocr.pdf` to `PDFs/...`

When Pete runs it himself in Terminal, `-o` can point straight at the archive and steps 2 and 3 disappear.

**Budget and timeouts.** `pc bash` caps at 95 seconds and the executor frequently stops responding on long jobs. A 142-page scan takes several minutes. For anything beyond roughly 40 pages, hand Pete the command rather than driving it — one line he pastes into Terminal, then tell him what to say when it finishes. Chasing a hung bridge costs more than waiting for him.

**Step 2 — Write a findings note, but only if the material warrants analysis.**

A findings note is a standalone document in the archive root named for its subject, e.g. `AG-12581-13043-FINDINGS.md`. Write one when the material changes what the archive believes. Skip it when the material only confirms existing claims — a manifest line and a log row are enough.

**Runtime.** The FLORIDA archive contains no sensitive documents by Kastner's standing position — public records, court filings, audits, contemporaneous press, and analyst reconstruction. Findings-note drafting therefore has no privacy-driven reason to run local. Route by fit, not by sensitivity:

- **Cloud (default)** — long dossier reads, cross-document synthesis, and initial findings-note drafts where breadth of context matters. This is what cloud frontier models do best.
- **Local (Ollama on Mac, when warranted)** — narrow verification passes over a single OCR'd report where the question is bounded ("does 12581 ¶44 say the utilization figure came from the Department's consultant or the Auditor General?"). Cheap, reproducible, no credit spend, and the answer is a quote lookup, not synthesis.
- **Hybrid (PPLX runtime)** — not indicated for this workload. Its Privacy Gate exists for sensitive inputs the archive does not have, and it lacks fixture history for FLORIDA-style attribution reads. Reserve for the separate case of ad-hoc questions over material Kastner has explicitly marked as private outside the archive.

**Step 3 — Append rows to PENDING-CHANGES.md.**

One row per discrete change. Columns: `#`, `Change`, `Source`, `Targets`, `Priority`.

- **Change** — state the correction, not the evidence. A sweep operator should be able to act on the row without reopening the source.
- **Source** — pinpoint. `12581 ¶44`, not "the 1995 audit." Use printed paragraph numbers where the document has them; they are more stable than OCR page markers.
- **Targets** — name the files. `ALL` means every published paper plus README.
- **Priority** — `P1` a claim currently in print is wrong. `P2` a claim is under-supported or imprecise. `P3` additive, nothing currently wrong.

Update the status line at the top of the file: blockers, pending count, applied count.

**Then stop.** Do not edit the published papers.

## 2. On a sweep instruction

1. **Check § 0 first.** If a blocker stands, resolve it or report that the sweep cannot safely proceed. Applying edits to the wrong copy of the corpus is worse than applying none.
2. Work § 2 top to bottom: P1, then P2, then P3.
3. For each row, edit every file in Targets. Verify the change landed — read it back, do not trust the write.
4. Move the row to § 5 with the date and the files touched.
5. Report what could not be resolved and why.

Prefer one file-rewrite pass per target file over many small edits to the same file.

## 3. The exception

A factual error that would mislead a reader who opens the file **today** gets fixed immediately and logged directly into § 5 as applied.

That means a dead link presented as live, a figure attributed to the wrong source, a claim the evidence now contradicts. It does not mean a figure that is merely superseded by a better one, or an addition that makes the argument stronger. Those wait.

When in doubt, log it and say so in your reply. The cost of waiting is low; the cost of a half-applied correction is a corpus that contradicts itself.

## 4. Standards this archive holds itself to

These are Kastner's, learned from the archive's own errors. Apply them to every row you write.

- **Name who measured a figure.** "Report 12581 measured 95 percent CPU utilization" was wrong; the figure came from a consultant the Department hired, and the 65 percent comparison was industry data the Department itself supplied. Attribution errors are the most common failure mode here and the hardest to see.
- **Do not silently correct.** When the archive was wrong, the correction says so and says what the error was. The README's methodology note carries a worked example of why.
- **Label inference as inference.** Analyst judgment is recorded as analyst judgment, never as documentary evidence.
- **Press paraphrase migrates into analysis and hardens there**, especially when it is shorter and reads better. A claim that flatters the argument gets less scrutiny than one that complicates it.
- **Do not combine figures of different units.** A press-reported target of 12,000 terminals and a documented count of 16,000 network devices of four classes are not a series, and the growth rate between them is not printable.
- **Concede exogenous causes squarely.** It usually sharpens the structural argument rather than weakening it.
- **A link to a government document is not preservation.** Mirror anything load-bearing. Verify a retrieval directly rather than trusting a cache — a cached fetch once reported a page live that returned 404 on direct request.

## 5. Working on the Mac

The archive lives on Kastner's Mac. Use `pc` with `api_credentials=["pc"]`.

- The Mac shell is sandboxed: **no network access, and no writes anywhere under `/Users/scott`** — `mkdir` and `touch` both return "Operation not permitted" on the Desktop and in the home directory. `/tmp` and `/private/tmp` are writable. Download in the sandbox and `pc push` across; `pc push` has full permission and creates intermediate directories.
- Consequently, anything that must *produce* files on the Mac either writes to `/tmp` and is pushed into place, or is delivered as a script for Pete to run himself. The second pattern is the house style — see his `kastner-eod` skill, which emits one self-verifying script rather than round-tripping through the bridge.
- Edit large files by `pc pull` → edit in the sandbox → `pc push` back. Do not attempt many small `pc files edit` calls.
- **The bridge times out often.** A `pc push` that returns a `mac_path` and a matching `size_bytes` succeeded even if the verification read afterward fails. Retry a push that returned nothing; do not retry one that returned a receipt.
- Prefer working files in place over copying them off the device.

## 6. Examples

**A records response arrives with two report PDFs.**
OCR both on the Mac with `ocr_pdf_v1.sh` — not in the sandbox. File the searchable PDFs under `PDFs/auditor-general/` and the transcriptions under `sources/auditor-general/`. Update the manifest. Write a findings note if the reports change what the archive believes. Append rows for each changed claim. Update the records-requests log with the response. Do not touch the papers.

**Kastner offers a technical reading of a configuration.**
Record his observation verbatim, then assess it — supporting what the evidence supports, correcting what it does not, and saying which is which. Put it in the findings note under a heading that attributes it to him. Log any resulting edit as a pending row.

**A figure in a published paper is superseded.**
P1 row. Name the old figure, the new one, the source, and every file carrying the old one. Do not patch it in one place — a number that appears in an executive summary and an appendix must change in both or in neither.

**Kastner says "run the pending changes."**
Check § 0. Work the table. Verify each edit. Move rows to § 5. Report the unresolved.
