# DECtp 1988 — Prescience Argument of Record

**Subject study:** `dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836`
**Scoring:** importance = **high** · relevance = **high** · prescience = **high**
**Author of this note:** Peter S. Kastner
**Recorded:** 2026-06-13
**Note type:** prescience rationale (companion to `_master_studies.csv`)

---

## Why a separate note exists

The DECtp 1988 announcement is easy to misread through a static pass/fail lens — IBM mainframes are still here in some form, and DEC the company is not, so a naive reader will mark the study "low prescience" and move on. That reading misses the point. The DECtp announcement was an **inflection event** in commercial computing, and the inflections it set in motion are still load-bearing in 2026. This note is the argument of record for the high/high/high score and is referenced from `_master_studies.csv` `prescience_rationale`.

## The static reading (and why it is wrong)

The static reading goes: DEC predicted distributed transaction processing would displace mainframe TP; IBM didn't exit; DEC died; therefore the prediction failed. This treats the announcement as a single bet on company-versus-company survival. It is not. The announcement was a bet on **how the industry would measure, price, scale, and procure transaction processing for the next two decades**. On those terms, every component of the bet won.

## The 1985–1988 context buyers were actually living in

By the mid-1980s, enterprise buyers wanted **lower-cost transaction processing for local or departmental applications**. The mainframe was either too distant (the canonical Florida HHS example: a state agency could not get its TP workload close enough to its users) or too slow to develop against (mainframe app dev cycles were measured in quarters, not weeks). Buyers were ready to move; what they lacked was a defensible way to specify what they were buying.

There were **no good measures of TP performance** at the time. Vendor claims were unfalsifiable. Procurement committees had no rigorous specification language for "how much TP can this thing do, and at what cost per unit?"

Tandem's 1985 *Datamation* article changed the conversation. It proposed a rigorous specification: performance measured in **transactions per second (tps)**, and — critically — **price-performance measured in dollars per tps ($/tps)**. This was the first time the industry had a defensible procurement metric for TP.

## Kastner's path into the DECtp work

I worked on **Stratus' response to the Tandem article**, which gave me direct exposure to the rigor Tandem was proposing and to the gaps in everyone else's TP positioning. I brought that knowledge to **Digital Equipment Corporation**, which was already positioned with the right hardware story but had no answer on the software side. DEC had:

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

IBM's **October retort** mentioned tps numbers but conspicuously did NOT engage on price-performance or on scaling, especially against big mainframes. The discourse had moved, and IBM was responding to the new frame whether it liked the frame or not.

## The six inflection-point outcomes

The DECtp announcement was an inflection point that began six durable shifts in commercial computing:

1. **Focus on $/tps and price-performance** — that continued for two decades and became the default lens for TP procurement.
2. **RDBMS became the standard for TP benchmarks**, not specialized databases. The relational stack carried the benchmark story going forward.
3. **Scaling counts** — buyers came to expect that vendors prove their systems scale, not just that they run at a single point.
4. **Standardized TPC benchmarks** made buyer choices much easier. Procurement could compare like to like across vendors with confidence.
5. **DEC's TP business doubled in a year** following the announcement — historical revenue records confirm this. The bet paid for itself within DEC's own books.
6. **The TPC became the undisputed arbiter** of commercial benchmarks for the era. Vendors competed on TPC numbers because that's what buyers cited.

## Why this is high prescience, not high importance only

A study can be important without being prescient — a contemporaneous landmark is not the same as a forecast that came true. DECtp is both:

- **Importance: high** because the announcement was a contemporaneous landmark — it reframed how the industry measured and procured TP.
- **Relevance: high** because $/tps thinking, standardized benchmarks, RDBMS as the TP substrate, and scale-as-a-procurement-requirement are still load-bearing in 2026.
- **Prescience: high** because the announcement explicitly bet on **measurement, pricing, scale, RDBMS substrate, standardization, and DEC's own TP revenue trajectory** — and all six bets won, on the timelines the announcement implied.

The fact that DEC the company did not survive into the 2000s does not refute the prescience of the announcement. The DECtp **bets about the industry** won. The **bet about DEC's own survival as an independent company** was not part of the announcement.

## Sources used in forming this argument

- The press conference transcript and benchmark charts themselves (`dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836`)
- The 1985 Tandem *Datamation* article proposing the tps + $/tps specification
- IBM's October 1988 retort (cited in the DECtp transcript materials)
- TPC formation timeline (industry record)
- DEC TP business revenue trajectory (DEC's historical financial records)
- Peter S. Kastner's first-person recollection of working on Stratus' Tandem response and carrying that work into DEC

## How to cite this note

From `_master_studies.csv`, the `prescience_rationale` cell for `dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836` references this file:

> See `kastner-author/notes/dectp_prescience_rationale_2026_06_13.md` — six inflection-point outcomes (focus on $/tps, RDBMS as TP benchmark standard, scaling counts, standardized TPC benchmarks, DEC TP business doubled in a year, TPC became undisputed arbiter).

---

_Recorded as part of the §11u-cont Pass B reconciliation; the four [DEFERRED] prescience rows were resolved in the same batch (oracle-data-warehousing=medium, crossroads-launch=low, crossroads-june-variant=low, tandem-himalayan=medium, dectp-press-conference=high)._
