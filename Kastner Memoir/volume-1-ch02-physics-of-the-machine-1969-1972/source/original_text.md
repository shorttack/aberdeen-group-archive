# Chapter 2: The Physics of the Machine (1969–1972)

> Archived from: MASTER-EBOOK-ASSEMBLED-v4.md (Chapter 2: The Physics of the Machine (1969-1972))
> Original publication date: 2026-05-14
> Author: Peter S. Kastner

---

## Original Document Text

# Chapter 2: The Physics of the Machine
### *(1969–1973)*

---

In March 1969, the center of my universe was a converted funeral home in Arlington, Massachusetts.

This was the headquarters of Philip Hankins Inc. (PHI), a company that looked like a grim New England curiosity from the outside but hummed with the energy of a frantic laboratory on the inside. I walked in as a 21-year-old junior programmer carrying a salary of $7,200 a year. In the grand scheme of the 1960s economy, that was respectable—actually higher than what many bank vice presidents earned at the time. But the most important number in my life wasn't my paycheck. It was $360.

That was the cost of exactly one hour of CPU time on PHI's IBM System/360 Model 65 service bureau.

In the unforgiving economics of 1969, twenty hours of machine time equaled my entire annual salary. This single equation defined the culture of the entire industry. Today, compute is essentially infinite and nearly free—at least until you start pricing AI tokens—while human talent is the scarce resource. In 1969, the inverse was absolutely true. Flesh and blood were cheap. The machine was a god that had to be fed with trembling efficiency. You didn't just "run" a program. You submitted it like a prayer, hoping it wouldn't burn a thousand dollars of company money on an infinite loop.

Those stakes shaped everything about how we worked, what we valued, and what we respected. If you want to understand why the programmers of that era wrote code the way they did, start with $360 an hour.

---

## The Rocket Scientists of Arlington

PHI was not a normal software house. The founder, Philip Hankins, and his engineering lead, David Moros, had cut their teeth writing navigation code for the Apollo lunar program. These were men for whom a bug didn't mean a system crash—it meant a spacecraft missing the moon. That DNA ran through everything they built.

Moros—dapper, polite, and relentlessly precise—presided over a collection of whiz kids and productive eccentrics spread across a ramshackle group of old houses and that repurposed funeral home. The atmosphere was half dormitory, half NASA mission control. Sloppy code was not merely an error there. It was a moral failing.

My real education at PHI came from a brilliant, abrasive mentor named Robert A. Siegel, who would later go on to architect the Wang VS operating system. Siegel didn't teach me syntax. He taught me physics. An applications programmer, he insisted, manages the physical resources of the machine: the spin of the disk, the cycle of core memory, the click of the card reader. You were not writing instructions; you were choreographing hardware.

We had no Stack Overflow, no Google, no online documentation. We had the IBM System/360 Reference Card—a dense fold-out cheat sheet roughly the size of a placemat—and yellow legal pads. I learned to read hexadecimal core dumps to find the ghost in the machine, and I learned the dark arts of Job Control Language (JCL).

> **Sidebar: Core Dumps and JCL**
>
> When a program failed catastrophically, the operating system "dumped" the entire contents of core memory to a printout—sometimes hundreds of pages of raw hexadecimal numbers. Reading a core dump meant navigating those pages to find where the program had gone wrong, what data had been in memory at the time, and which instruction had caused the crash. It was the debugging equivalent of reconstructing a car crash from skid marks.
>
> Job Control Language (JCL) was the command syntax used to tell the IBM operating system how to run a program: which tapes to mount, which disk packs to allocate, how much memory to reserve, what to do if the job failed. JCL was notoriously cryptic and unforgiving—a single misplaced comma could cause a job to fail and waste an expensive machine run. Mastering it was not glamorous, but it separated people who understood the system from those who merely used it.

The most memorable lesson Siegel taught me was something he called the One-Instruction Switch. Setting a binary flag in a program—a simple true/false indicator—normally required three steps: load the value from memory, change it, store it back. Three memory references. Three precious machine cycles. Siegel showed me a specific IBM instruction that could set the flag in a register directly, without touching memory at all. One instruction. Trivial in isolation. Transformative at scale, when you are processing millions of transactions at $360 an hour. And yes, you could do it in COBOL.

That was the culture: not just getting the right answer, but getting it with the minimum expenditure of machine resources. Efficiency was not an engineering preference. It was economic survival.

---

## The World Outside the Machine

My early assignments at PHI were constant reminders that software is not mathematics—it is a model of a much messier physical world. Two projects in particular drove that lesson home with force.

The first was for Cumberland Farms, the New England gas station and convenience store chain. I was designing a retail accounting system, and one challenge had nothing to do with clever algorithms. It was a mechanical problem: the pump counters of that era physically rolled over to zero once they hit 9,999 gallons. Like an odometer. My code had to detect that rollover and keep the accounting straight, reconciling the digital ledger against the paper cash transmittal forms to the penny. The system had to model not what the pump *should* have done, but what the pump's gears *actually* did.

Good software, I was learning, doesn't just compute correctly. It anticipates the ways reality will deviate from the specification.

The second project was at Marine Midland Bank, in July 1969. While the rest of the world was transfixed by Apollo 11, I was quietly fixing what was one of the world's first Year 2000 (Y2K) bugs—thirty years early.

I was upgrading their bond portfolio system when someone asked a deceptively simple question: *What happens in January 1970 when a customer issues a 30-year bond?* The system had been designed with two-digit year fields. A bond issued in 1970 maturing in the year 2000 would be recorded as maturing in "00"—which the system would read as 1900 and promptly lose its mind. By expanding the maturity date field, I fixed the bug three decades before it became a global panic.

No one wrote a press release about it. We were just doing the job.

---

## Siegel's Law and the Economics of Attention

> **Sidebar: Why $360 an Hour Changed How Software Was Written**
>
> In 1969, most programmers did not sit at terminals typing code and watching it execute. That was timesharing, and it existed at universities and research labs—not typically at commercial service bureaus. At PHI, you wrote your program on a coding form, had it keypunched onto punch cards, submitted the card deck to the operations queue, and waited. Hours later, you retrieved your printout. If the program had failed, you analyzed the printout, found the bug, corrected the cards, and submitted again.
>
> This process had profound implications for how you thought about code. Every submission was a financial event. Careless programs that failed on the first run wasted not just time but real money. The discipline this imposed—thinking problems through completely before a single card hit the reader—was rigorous in ways that today's instant-feedback development environments simply do not replicate. You planned. You reviewed. You checked. Then you submitted.
>
> The culture Siegel embodied was the direct product of this economics. When computer time is the scarce resource, the programmer's job is to minimize consumption of that resource. Every unnecessary instruction, every inefficient loop, every redundant memory reference was a small theft from the company's budget. The One-Instruction Switch wasn't a trick; it was respect for the machine's cost.

---

## The Cosmos Factory

The soul of PHI was a system called the Customer Accounting System (CAS), which the team eventually renamed Cosmos. Someone had framed a copy of the Creedence Clearwater Revival album *Cosmos Factory* on the wall of the main room—part joke, part genuine pride of authorship. Cosmos was not an application in the conventional sense. It was a generator: a program that could produce millions of lines of architecturally sound COBOL code according to specifications, essentially automating the construction of other programs.

> **Sidebar: Why Code Generation Mattered**
>
> In 1969, most large application systems were built by teams of programmers writing COBOL by hand, one procedure at a time. Frederick Brooks had recently published *The Mythical Man-Month*, which argued that adding programmers to a late project makes it later—because the coordination cost of human communication grows faster than the productivity added. A team of 10 programmers doesn't produce 10 times the output of one programmer; the overhead of keeping them coordinated eats much of the gain.
>
> A code generator sidesteps this constraint. Once the templates and rules are right, the generator produces code faster than any team of programmers and with perfect architectural consistency. Cosmos allowed PHI to deploy systems at a scale and speed that would have been impossible with conventional programming teams. It was, in the language of its day, a force multiplier. In the language of ours, it was an early form of low-code development.

Working on Cosmos was genuinely exciting—the closest I had come so far to the automation dream that had started in that restaurant bookkeeping room. We were building a machine that built other machines. The stack of problems between human intention and computational outcome was getting shorter. In a year, a team of four built an entire bank checking account system.

---

## The Commute of Death

By 1972, the dream was cracking.

Wang Laboratories had acquired PHI, and the announcement came that the professional staff would be relocating to Wang's facility in Tewksbury, Massachusetts. On a map, Tewksbury is roughly twenty-five miles north of Boston. In the geography of my actual life, it was on the wrong side of the universe. My wife worked in Quincy, on the South Shore. Tewksbury was on the North Shore. The commute between them, through the center of Boston, in 1970s traffic, was a daily commitment of biblical proportions. We called it the Commute of Death.

It was not the machine that drove me out of PHI. It was the Massachusetts Turnpike and Route 128 at 7:30 in the morning.

Wang was, in its own right, a remarkable company—and a company I knew something about, since Moros himself was providing key technical leadership for Dr. An Wang's computing initiatives. I had nothing against Wang Laboratories. I just couldn't make the drive.

I was not the only one leaving. The PHI diaspora scattered toward safer harbors. I followed people I trusted—Murray Sherry and others—to Arthur D. Little Systems in Cambridge. We weren't exactly joining a consultancy so much as arriving as a small, seasoned rescue squad.

---

## What PHI Taught

The years from 1969 to 1973 constituted an education that no business school offered and no curriculum could have designed. The summary is brief but its implications ran for decades:

**Software is a model of physical reality, not a substitute for it.** Gas pump counters roll over. Bank systems use two-digit years. The world does not behave the way your specification assumes. Good code anticipates the gap. Application users matter.

**Economics shape engineering culture more powerfully than aesthetics do.** The discipline of the PHI programmers—their obsession with instruction counts and memory efficiency, their contempt for waste—was not a personality trait. It was the rational response to $360 an hour. Change the economics, and you change the culture. (Something worth remembering as AI inference costs fall toward zero in the late 2020s.)

**Automation multiplied by systems beats automation multiplied by people.** Cosmos demonstrated that the right answer to Brooks's Law was not more programmers—it was tools that made each programmer more powerful. I had wanted machines to handle the paper since I was twelve. At PHI, I started to see how that actually worked.

I left my coding pad in Arlington, not as a repudiation of the work but as a recognition that the next chapter required a different kind of intelligence. The physics of the machine were now in my bones. It was time to learn the physics of organizations.

---

*Next: Chapter 3 — Eight Years in the Physics of Consulting*



---




---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | volume-1-ch02-physics-of-the-machine-1969-1972 |
| title | Chapter 2: The Physics of the Machine (1969–1972) |
| author | Peter S. Kastner |
| date | 2026-05-14 |
| type | memoir |
| subject_domain | memoir/volume-1 |
| methodology | oral-history |
| source_file | MASTER-EBOOK-ASSEMBLED-v4.md (Chapter 2: The Physics of the Machine (1969-1972)) |
| license | CC-BY-4.0 |

### Abstract

Kastner recounts his formative years (1969–1972) as a junior programmer at Philip Hankins Inc. (PHI), a service bureau in Arlington, Massachusetts where CPU time cost $360 per hour on an IBM 360/65. He describes the culture of rigorous efficiency shaped by those economics, key mentors including Robert Siegel, landmark early projects at Cumberland Farms and Marine Midland Bank (including an early Y2K fix), and the Cosmos code-generation system. The chapter ends with Wang Laboratories acquiring PHI and Kastner departing for Arthur D. Little Systems.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Establishes Kastner's foundational programming education, the economic context that shaped 1960s–70s software culture, and early encounters with code generation and Y2K-class problems. |
| **Relevance** | high | Directly documents the IBM 360/65 service-bureau era, COBOL programming culture, early code generation, and the PHI–Wang Laboratories relationship—all central to the memoir's arc. |
| **Prescience** | medium | Kastner's 1969 fix of a two-digit-year bug at Marine Midland anticipated the global Y2K crisis by 30 years, and his observation that falling AI inference costs will reprise the cheap-compute dynamic shows consistent forward-thinking. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (11)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Peter S. Kastner | person | active |  |
| Philip Hankins Inc. (PHI) | company | acquired | Wang Laboratories |
| Philip Hankins | person | unknown |  |
| David Moros | person | unknown |  |
| Robert A. Siegel | person | unknown |  |
| Wang Laboratories | company | dissolved |  |
| An Wang | person | unknown |  |
| Arthur D. Little Systems | firm | unknown |  |
| Murray Sherry | person | unknown |  |
| Marine Midland Bank | institution | acquired | HSBC |
| Cumberland Farms | company | active |  |

### Technologies Referenced (17)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| IBM System/360 Model 65 | platform | IBM | mature | legacy-end-of-life |
| IBM System/360 | platform | IBM | mature | legacy-end-of-life |
| COBOL | language | CODASYL/industry-standard | growing | legacy-supported |
| Cosmos (Customer Accounting System / CAS) | application | PHI (Philip Hankins Inc.) | growing | dissolved |
| Wang VS Operating System | platform | Wang Laboratories | emerging | legacy-end-of-life |
| Y2K / Year 2000 Two-Digit Year Bug | application | industry-wide | emerging | legacy-end-of-life |
| Job Control Language (JCL) | language | IBM | growing | legacy-supported |
| Punch Cards / Card Decks | platform | IBM | mature | legacy-end-of-life |
| Core Memory | platform | IBM | mature | legacy-end-of-life |
| Core Dump / Hexadecimal Core Dump | application | IBM | mature | legacy-end-of-life |
| IBM System/360 Reference Card | application | IBM | mature | legacy-end-of-life |
| Service Bureau Computing | platform | industry-wide | mature | legacy-end-of-life |
| Timesharing Systems | platform | various | emerging | legacy-end-of-life |
| Bond Portfolio System (Marine Midland) | application | PHI (Philip Hankins Inc.) | mature | dissolved |
| Retail Accounting System (Cumberland Farms) | application | PHI (Philip Hankins Inc.) | mature | dissolved |
| Code Generation / Automated Code Generation | framework | PHI (Philip Hankins Inc.) | emerging | active |
| Apollo Lunar Navigation Software | application | NASA | mature | legacy-end-of-life |

### Observation Summary

- Total observations: 77
- By type: personal-recollection: 40, expert-opinion: 18, topic-insight: 14, market-data: 5
