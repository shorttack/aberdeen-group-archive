---
name: florida-changes
description: "Cache new evidence and required edits for Pete Kastner's FLORIDA System archive into PENDING-CHANGES.md instead of editing the published papers immediately. Use whenever new FLORIDA material arrives — a records-request response, an Auditor General or DOAH report, a court document, press coverage, an OCR of a scan or a completed OCR run folder, or Kastner's own analytical observation — and whenever he says 'log this', 'add to pending', 'run the pending changes', 'do the sweep', or asks what is outstanding on the FLORIDA archive. Prevents expensive per-item propagation across eight papers by batching corrections into scheduled sweeps."
license: MIT
metadata:
  author: peter-s-kastner
  version: '1.3'
  perplexity:
    connectors:
      - id: github_mcp_direct
        reason: The canonical archive lives in shorttack/aberdeen-group-archive; sweeps may need to read or commit there.
---

# FLORIDA Pending Changes

## Why this exists

The FLORIDA System archive is eight published papers — the main report (*The FLORIDA System: EDS, IBM, and the Collapse of a Landmark State Procurement*), *The Unisys Protests of RFP 88-74-BC*, *The Empty Center*, *One Bad RFP Away*, *One Model, Forty Years*, *Making It Workable*, the Webster Addendum, and *Processor Capacity Over Time* — plus support files: README, SOURCES, COLLECTION-PLAN, PENDING-CHANGES, records-request logs, findings notes (`AG-*-FINDINGS.md`, `DOAH-*`, `PRESENTMENT-1993-FINDINGS.md`, and others), and mirrored sources under `sources/`. A single new fact — a corrected attribution, a superseded cost figure — can touch five of them.

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

`~/Desktop/Archive/aberdeen-group-archive/FLORIDA/PENDING-CHANGES.md`

The archive root is `~/Desktop/Archive/aberdeen-group-archive/FLORIDA/` (git repo `shorttack/aberdeen-group-archive`). The **`.md` files in that folder are the definitive source** — not older copies in the Project files, the sandbox, or the empty legacy folder `~/Desktop/Archive/FLORIDA/`. All paths below are relative to this root unless absolute.

Working scaffolding. Excluded from any GitHub push unless a deliberate decision is made to publish the archive's revision history.

Its sections, in order:

| § | Contents |
|---|---|
| 0 | **Blockers.** Conditions that make a sweep unsafe. The two-divergent-copies blocker was resolved before the October 28, 2026 sweep; read the status line rather than assuming |
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
| Source PDFs | `PDFs/` — Auditor General reports under `PDFs/auditor-general/`, DOAH under `PDFs/DOAH/`, records responses under `PDFs/records-requests/`. **Do not create a new subfolder without asking.** **Large-file rule:** GitHub rejects files over 100 MB and `.gitignore` already excludes `PDFs/**/*_ocr.pdf`. A scan over ~90 MB stays in its preserved OCR run folder; record its absolute path and SHA-256 in SOURCES.md instead of copying it |
| OCR transcriptions | `sources/auditor-general/`, `sources/courts/`, `sources/records-requests/`, as `<number>.md` or `<case>-<doc>-<date>-ocr.md`. Prepend a provenance header: run ID, source SHA-256, page parity, QA status, citation-verification status, and pages flagged |
| Long structured extractions | `_working/` (does not exist yet — ask before creating) |
| Manifest entries | SOURCES.md, and the manifest in the destination folder where one exists |

Scanned PDFs need OCR before they are useful. **OCR runs on Pete's Mac, never in the sandbox.** See § 1a.

### 1a. OCR — always local

**Standard, set August 24, 2026, and still in force: OCR happens on the Mac.** Never render PDFs or run Tesseract in the sandbox. If the Mac is unreachable, say so and ask.

**The production runner (v2.2):** `~/Desktop/Memoirs/OpenCode/tools/florida/florida_ocr.py`, policy in `~/Desktop/Memoirs/OpenCode/.opencode/skills/florida-changes/references/production-ocr.md`. It replaces `~/Desktop/Archive/scripts/ocr_pdf_v1.sh`, which is legacy — do not use it for new material. Fixed OCRmyPDF profile (`--skip-text --oversample 300 --tesseract-pagesegmode 3 --optimize 0 --output-type pdf`), per-page Poppler extraction to `.md` and `.layout.md`, page-count parity, `qpdf --check`, source-unchanged check, run lock, never overwrite. It does not tune, choose models, or make citation claims. Long jobs are run by Pete in Terminal or OpenCode; the agent does not drive them.

**Intake from a completed run folder.** New scans arrive already processed under `~/Desktop/Memoirs/FLORIDA-documents/run_<timestamp>_prod/`. Before using one:

1. Read `COMPLETION.json`. Require a completed status and `TECHNICAL_PASS`; record the run ID, completion time, and `citation_verification` value.
2. Confirm a `PRESERVATION-RECEIPT-*.json` exists with its `.sha256`, and record the receipt ID. The durable run record is under `~/Desktop/Memoirs/OpenCode/florida-state/runs/<run>/`.
3. Read `page-qa.csv` and `validation/`; list every flagged page, and every page whose layout text is much longer than its default text (two-column or tabular).
4. Per document, under `<name>_<sha8>/ocr/`: `<name>_ocr.pdf` (searchable derivative), `<name>.md`, `<name>.layout.md`, `<name>.sidecar.txt` (diagnostic only), `ocrmypdf.stderr`. The unchanged original is in `_source-original/` and is the preservation master.
5. Leave the run folder untouched. Copy, never move.

**Which text file to read.** The v1.2 guidance ("`.md` is reading order, `.layout.md` for tables only") was written for `ocr_pdf_v1.sh` and is **reversed for v2.2 output**: the default `.md` from per-page `pdftotext` can scramble word order on single-column typed pages (verified November 21, 2026 on the 1992 EDS complaint), while `.layout.md` keeps lines intact. Read `.layout.md` for prose and tables alike, and spot-check the default `.md` only for two-column pages. Neither replaces the page image.

**Citation-grade rule.** `TECHNICAL_PASS` with `citation_verification: not_performed` means the text is usable for finding and drafting, **not for quoting**. Every quotation and figure taken from it is marked as unverified in the findings note and in the pending row's Source column (e.g. `Compl. Exh. B p. 44 (OCR, unverified)`), with a sweep precondition to check against the page image. Garbled regions are named by page.

**Always read a sample of the output before using it.** Exit code zero means the pipeline ran, not that the text is usable.

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

**Numbering.** Use the next number not already used in PENDING-CHANGES.md **or** proposed in any brief or findings note (search the archive for `| <n> |` first). Skip and say so rather than collide.

Update the status line at the top of the file: blockers, pending count, applied count.

In a session where Kastner asks to review first, draft the findings note and rows in the sandbox and show them; write to the Mac only after approval. Commits wait for the end-of-session batch.

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

The archive lives on Kastner's Mac mini (M5 Pro). Reach it through the Perplexity device tools (personal-computer skill), not the retired `pc` bridge.

- **Read** with the device shell (`bash_execute`); keep each output small — it truncates around 5 KB, so use `grep -c`, `head`, and `cut`, not `cat` on large files.
- **The device shell can write only to `/tmp`** — `mkdir` or `cp` anywhere under `/Users/scott` fails with "Operation not permitted" (re-verified November 21, 2026). `transfer_file_from_sandbox` can write into existing archive folders. Anything that must be created or copied on the Mac itself — new folders, large PDFs — is delivered as one self-verifying script in `/tmp` for Pete to run in Terminal. `/tmp` is for session files only; permanent files go under `~/Desktop` (Archive or Memoirs), which is backed up. Agent scratch and review copies go to `~/Desktop/Archive/Perplexity_Only` without asking.
- **Pull** a file into the sandbox with `share_local_file_with_sandbox`; **push** with `transfer_file_from_sandbox`. Edit large files in the sandbox and push back whole; do not make many small remote edits.
- Verify every push by size or checksum on the Mac.
- Do not touch unrelated uncommitted changes in the repo (check `git status` before writing; report, do not revert).
- No run outputs inside `_skills/`. No new directories without asking. Commits and pushes only in the end-of-session batch.

## 6. Examples

**A records response arrives with two report PDFs.**
OCR both on the Mac with the v2.2 runner — not in the sandbox. File the searchable PDFs under `PDFs/auditor-general/` and the transcriptions under `sources/auditor-general/`. Update the manifest. Write a findings note if the reports change what the archive believes. Append rows for each changed claim. Update the records-requests log with the response. Do not touch the papers.

**Kastner offers a technical reading of a configuration.**
Record his observation verbatim, then assess it — supporting what the evidence supports, correcting what it does not, and saying which is which. Put it in the findings note under a heading that attributes it to him. Log any resulting edit as a pending row.

**A figure in a published paper is superseded.**
P1 row. Name the old figure, the new one, the source, and every file carrying the old one. Do not patch it in one place — a number that appears in an executive summary and an appendix must change in both or in neither.

**Kastner says "run the pending changes."**
Check § 0. Work the table. Verify each edit. Move rows to § 5. Report the unresolved.

**A completed OCR run folder arrives (e.g. `run_20261121t161910Z_prod`, the 1992 EDS complaint).**
Run the § 1a intake checks. Read `.layout.md`. Search the archive for every figure, date, and name the document touches and classify each hit P1/P2/P3. Draft the findings note (pleading allegations vs. attached exhibits kept separate; OCR-unverified figures marked) and the rows. Propose filing: transcript to `sources/courts/`, scan left in the preserved run folder if over the size limit, SOURCES.md entry. Show the drafts; file only on approval.
