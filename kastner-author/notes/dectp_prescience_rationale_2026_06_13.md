---
title: "DECtp 1988 — Player's Rebuttal to Scorer's Verdict"
author: "Peter S. Kastner"
recorded: "2026-06-13 11:53 EDT (15:53 UTC)"
subject_study: "dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836"
study_title: "DECtp Press Conference Transcript and Benchmark Charts, Plaza Hotel NYC, July 1988"
note_type: "player rebuttal to scorer verdict"
scorer_verdict: "low"
scorer_mean: 0.46
scorer_n_obs: 26
scorer_model: "sonar-reasoning-pro"
scorer_date: "2026-06-13"
tags:
  - kastner-author
  - notes
  - prescience-rebuttal
  - dectp
  - 1988
---

# DECtp 1988 — Player's Rebuttal to Scorer's Verdict

**Author:** Peter S. Kastner
**Recorded:** 2026-06-13, 11:53 EDT (15:53 UTC)
**Subject study:** `dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836` — *DECtp Press Conference Transcript and Benchmark Charts, Plaza Hotel NYC, July 1988*
**Note type:** player rebuttal to the scorer's verdict on prescience

## Context — what the scorer said

On 2026-06-13, the Pass C desktop scorer (`sonar-reasoning-pro`) evaluated the 26 observations from the DECtp Plaza Hotel press conference study and returned a study-level verdict of **prescience = low** (mean 0.46 across 26 scoreable observations; 22 of 26 observations scored 0). Under the kastner-archive-pipeline scorer-is-judge rule, that verdict is recorded in `_master_studies.csv` as the study-level prescience value.

This note is the player's rebuttal of record. The scorer scores; the player gives press commentary. The two coexist in the archive: the scorer's verdict in `_master_studies.csv.prescience`, this rebuttal in `_master_player_rebuttals.csv` referencing the file below.

## Why I disagree with the scorer

The low-prescience verdict rests on a **static pass/fail reading** of the DECtp announcement: the announcement implied distributed transaction processing would displace mainframe TP; IBM mainframes are still here in some form, and DEC the company is not; therefore the prediction failed. This treats the announcement as a single bet on company-versus-company survival.

It is not. The DECtp announcement was a bet on **how the industry would measure, price, scale, and procure transaction processing for the next two decades**. On those terms, every component of the bet won — and the scorer's per-observation lens, working from the transcript text in isolation, cannot see this structural argument.

## The 1985–1988 context buyers were actually living in

By the mid-1980s, enterprise buyers wanted **lower-cost transaction processing for local or departmental applications**. The mainframe was either too distant (the canonical Florida HHS example: a state agency could not get its TP workload close enough to its users) or too slow to develop against — mainframe app dev cycles were measured in quarters, not weeks. Buyers were ready to move; what they lacked was a defensible way to specify what they were buying.

There were **no good measures of TP performance** at the time. Vendor claims were unfalsifiable. Procurement committees had no rigorous specification language for "how much TP can this thing do, and at what cost per unit?"

Tandem's 1985 *Datamation* article changed the conversation. It proposed a rigorous specification: performance measured in **transactions per second (tps)**, and — critically — **price-performance measured in dollars per tps ($/tps)**. This was the first time the industry had a defensible procurement metric for TP.

## How I came into the DECtp work

I worked on **Stratus' response to the Tandem article**, which gave me direct exposure to the rigor Tandem was proposing and to the gaps in everyone else's TP positioning. I then brought that knowledge to **Digital Equipment Corporation**, which was already positioned with the right hardware story but had no answer on the software side. DEC had:

- A wide range of **compatible hardware** (VAX line, top to bottom)
- **Excellent distributed processing** capabilities
- **Networking** that actually worked across heterogeneous environments

What DEC lacked was a **transaction processing software engine and a database** that could carry the tps story credibly. The DECtp work assembled exactly that stack.

## What the DECtp benchmark did to IBM

The DECtp announcement caught IBM in a spotlight. The published benchmark results showed:

- **Poor TP performance on DB2** at the time
- **Poor scaling** as load was added, with corresponding processing power and unit cost
- **Embarrassing price-performance compared to DEC** (and to many others)

This was not a marketing skirmish. It was a public, comparative, rigorously specified result that buyers could read and procurement could cite. IBM had no immediate technical answer.

## The TPC formed within a month

Within roughly a month of the DECtp announcement, the **Transaction Processing Performance Council (TPC)** was formed as an **industry-standardization body**. The TPC took the subject seriously, moved buyer confidence into standardized TP benchmarks, and provided the institutional home for the $/tps language going forward.

IBM's **October retort** mentioned tps numbers but conspicuously did NOT engage on **price-performance** or on **scaling** — especially against big mainframes. The discourse had moved, and IBM was responding to the new frame whether it liked the frame or not.

## The six inflection-point outcomes

The DECtp announcement was an inflection point that began six durable shifts in commercial computing:

1. **Focus on price/performance — $/tps** — that continued for two decades and became the default lens for TP procurement.
2. **RDBMS became the standard for TP benchmarks**, not specialized databases. The relational stack carried the benchmark story going forward.
3. **Scaling counts** — buyers came to expect that vendors prove their systems scale, not just that they run at a single point.
4. **Standardized TPC benchmarks made buyer choices much easier.** Procurement could compare like to like across vendors with confidence.
5. **DEC's historical records say TP business doubled in a year** following the announcement. The bet paid for itself within DEC's own books.
6. **The TPC became the undisputed arbiter** of commercial benchmarks for the era. Vendors competed on TPC numbers because that's what buyers cited.

## Why the scorer missed this

The Pass C scorer reads observations one at a time. Each individual sentence from the press transcript reads as DEC marketing — bold claims about its own future market position. Read that way, observation by observation, most claims look unsupported by the historical record (DEC did not become the dominant TP vendor; DEC ceased to exist as an independent company).

But the **collective effect** of the announcement on the industry — the six outcomes above — is not visible at the per-observation level. It requires the structural reading: this was not a forecast about DEC's corporate survival; it was an industry-shaping intervention whose six bets all paid out on the timelines the announcement implied.

The fact that DEC the company did not survive into the 2000s does not refute the prescience of the announcement. The DECtp **bets about the industry** won. The **bet about DEC's own survival as an independent company** was not part of the announcement.

## How to cite this rebuttal

The binding is recorded in `archive_masters/_master_player_rebuttals.csv` row for `dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836`. That row points to this file. The scorer's verdict (low, mean 0.46) remains the canonical study-level prescience in `_master_studies.csv`; this note is the player's signed disagreement, preserved alongside the verdict for future readers.

---

*Recorded as part of the §11v continuation, 2026-06-13. Pass C scored 17 transcripts + DECtp Plaza Hotel; this rebuttal accompanies the Plaza Hotel verdict only. Blue Monday (`dec-blue-monday-internal-sales-training-dectp-vs-ibm-0021cc`) received scorer verdict medium (mean 2.02 over 41 scoreable obs) and is not rebutted.*
