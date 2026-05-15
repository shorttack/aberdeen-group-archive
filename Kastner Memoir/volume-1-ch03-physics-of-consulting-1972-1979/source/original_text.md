# Chapter 3: Eight Years in the Physics of Consulting (1972–1979)

> Archived from: MASTER-EBOOK-ASSEMBLED-v4.md (Chapter 3: Eight Years in the Physics of Consulting (1972-1979))
> Original publication date: 2026-05-14
> Author: Peter S. Kastner

---

## Original Document Text

# Chapter 3: Eight Years in the Physics of Consulting
### *(Arthur D. Little, 1972–1979)*

---

When I followed the caravan out of Arlington and into Arthur D. Little (ADL) in Cambridge, I thought I was just changing employers. In reality, I was changing planets.

At Philip Hankins Inc., we had lived inside the machine—spelunking through core dumps, timing disk-arm rotations, counting microseconds. The machine was the universe, and the universe had rules. At ADL, I discovered a more unnerving truth: most systems don't fail in the machine. They fail in the boardroom, the warehouse, or the customs shed at the airport.

The PHI diaspora had scattered when Wang Laboratories announced its plans to move us to Tewksbury. I followed people I trusted—Murray Sherry and others—to Arthur D. Little Systems, ADL's information technology practice. We weren't exactly joining a consultancy. We were arriving as a small, seasoned rescue squad, hired precisely because we knew how systems actually worked rather than how they were supposed to work.

That distinction would matter every single day for the next eight years.

---

## Chase Manhattan: The Cardboard Physics of Money

One of my major ADL assignments was a mission with a deceptively simple mandate: migrate Chase Manhattan Bank's securities processing operation—managing roughly twenty billion dollars in assets—from aging Univac hardware to IBM, without losing a single share or a single penny.

The Univac equipment was not merely old. It was archeologically obsolete. Spare parts, legend had it, had literally been dumped at sea. Whether the ocean floor really was a graveyard for Univac components didn't matter; the smell of irreversible obsolescence was real enough. When a platform is so dead that replacement hardware is unavailable at any price, you don't optimize the system. You get it off life support. And two Cosmos experts did that in a year, delivering 25 million lines of bug-free COBOL code.

> **Sidebar: The 96-Column Problem**
>
> Univac punch cards held 96 columns of data; IBM punch cards held 80. Sixteen columns may not sound like much, but every field in every record in Chase's systems had been designed to fill those 96 columns precisely—account numbers, transaction codes, dollar amounts, dates, all packed into a format that IBM hardware simply could not read or match. There was no compression algorithm that could reconcile the two formats elegantly. The only solution was to explode each 96-column Univac record into multiple 80-column IBM cards, rebuilding every field boundary in the process. It was the 1970s equivalent of migrating a database from one vendor's proprietary format to another—tedious, exact, and unforgiving of rounding errors.

The problem revealed itself most sharply in David Rockefeller's dividend records. His holdings were large enough that the standard dividend field—already stretched to its maximum under the Univac design—simply couldn't contain the numbers after the column-count reduction. We spent hours hunting for one more column, the information-systems equivalent of rifling through the couch for loose change. This was not elegant engineering. It was hand-to-hand combat with arithmetic.

During the parallel run—when both the dying Univac system and the new IBM system processed the same transactions simultaneously so we could compare results—theory evaporated and brute force took over. Chase assembled a small army of temporary workers and deployed them as a human audit engine, reprocessing days of transactions by hand to verify that the new system produced identical answers. Watching that room, I understood something that today's cloud architects sometimes forget: automation is usually born not from a love of elegance but from sheer exhaustion with manual labor. We were not building a monument to design purity. We were trying to ensure that a dividend check didn't bounce because a card had the wrong column count.

The architecture we eventually built ran for decades, surviving corporate mergers and hardware generations that would have startled everyone in that windowless parallel-run room. Somewhere deep in modern financial plumbing, there are DNA traces of that migration—field definitions and processing rules whose ancestry leads back to those 80 columns of cardboard.

---

## Rio: Social Justice by Bicycle

By 1975 I had become, in ADL's polite institutional phrasing, a "vetted asset." Once your name appears in a winning proposal, some clients decide they have purchased not merely a firm but a specific person. The Federal University Hospital in Rio de Janeiro was one of those clients: a turnkey hospital system to serve an urban poverty area. They had read my biography in the proposal and insisted I be on the project.

That is how I found myself in Rio, writing cost-accounting logic for a country sliding into a foreign exchange crisis.

On paper, our design was sleek: online terminals connecting the hospital to a central data center. In practice, Brazil's currency controls made importing American computer hardware nearly impossible. We adapted. I came to think of what we built as "social-justice computing": instead of terminals, we used paper forms; instead of data packets, we had young men on bicycles pedaling batch-input forms several kilometers from the hospital to the computer center. It was embarrassingly low-tech by Boston standards and exactly right for the constraints of Rio in 1975.

The acceptance testing phase drifted from professional rigor into something approaching tragic comedy. I debugged Burroughs code in 104-degree heat in our project office, whose air conditioners had been stripped from the building. My notes from that period were stained with sweat; the ink literally ran. At the airport on the way home, a customs inspector pulled a reel of magnetic tape from its canister and unspooled it onto the floor in search of forbidden images. He found none, because magnetic tape at 800 bits per inch looks nothing like a photograph no matter how earnestly you squint at it. But he had the authority stamp, and that was that.

It was the perfect metaphor for the entire engagement: the most sophisticated data structures we had could be rendered helpless by one bored man with an authority stamp. The technology was never the limiting factor. The operating environment was.

That trip permanently changed how I thought about systems. I stopped seeing software as a self-contained artifact and started seeing every system as a living organism embedded in a hostile environment—power outages, currency crises, bad roads, bad policy, bad luck. The software is a vital organ. It is never the whole creature.

---

## Invisible Factories

ADL deployed me as an itinerant diagnostician, sending me into industries I knew little about—paper mills, electric utilities, municipal police departments—with the expectation that I would understand the guts of their operations quickly enough to design meaningful systems for ADL proposals. It was not glamorous work. It was an education no business school offered.

**The Lucille Ball Problem**

At Continental Forest Industries, I walked into a paper mill that ran on continuous motion and brute force. The mill produced two-thousand-pound rolls of kraft paper—a relentless industrial ballet of steel and pulp moving at speeds that turned each roll into a one-ton projectile. The inventory-control problem wasn't about elegant data models. It was about space and time: the system had to decide, quickly and correctly, whether to ship each roll to a customer or divert it to the cardboard-making line. If the decision took too long, the floor ran out of space.

I thought of the old Lucille Ball chocolate-factory sketch—except the chocolates here weighed a ton and could kill someone. The software's job was to be an unseen choreographer in an industrial ballet where hesitation was fatal. No system review had ever felt quite so physical.

**The Five-Baud Solution**

At Wisconsin Electric, the challenge was more modest in scale but equally instructive. The client wanted remote meter reading across a rural service territory held together by party telephone lines and tight capital budgets. The "correct" engineering solution—dedicated data lines—was financially impossible and impractical.

> **Sidebar: Power-Line Communication**
>
> The solution we proposed was to use the power distribution lines themselves as a communication medium. Utility companies have long known that low-frequency signals can travel on the same cables that carry electricity, superimposed on the 60-Hz power current. By encoding meter readings as voltage fluctuations and transmitting at five baud—five bits of data per second, roughly the speed at which a telegraph key could be tapped—we could move readings from remote meters to the utility's data center without laying a single new wire. By modern standards, five baud is comically slow (a modern USB connection runs roughly a billion times faster). But bandwidth was not the point. The meters needed to report infrequently and honestly, not eloquently.

The lesson: the best solution fits the physical and economic constraints of the actual system, not the ambitions of the engineer designing it. Embracing appropriate technology—matching the solution to the infrastructure at hand—was not settling for second best. It was respecting reality.

**The Police Radio Problem**

Not all of my field assignments were comfortable in the literal sense. In Hampton, Virginia, I was sent to verify whether a police information system developed there could be transferred to St. Petersburg, Florida. Hampton was not a tourist-brochure town. When I checked into a small, distinctly seamy motel near police headquarters, the Vice Chief of Police handed me a portable police radio and a specific code to transmit if I needed to make an "officer needs assistance" call.

"Don't leave your room at night," he said.

That night I sat on the motel bed, the radio on the nightstand, listening to the police-band traffic. I had come to evaluate software intellectual property, and I was spending more mental energy on the integrity of the door lock than on the database schema. It was a vivid lesson in operating environment: the technology we were assessing would live in cities with crime rates, underfunded departments, and officers whose lives might one day depend on whether a warrant query came back correctly. The consequences of a specification error would not be measured only in dollars.

---

## The Forensic Turn

As the decade wore on, ADL stopped sending me to design new systems and started sending me as a consultant to explain why existing systems were on fire.

The same instincts that make a good applications programmer—paranoia, attention to edge cases, an obsession with what the logs actually say rather than what they should say—translate surprisingly well into forensic work. I kept detailed personal journals on every troubled engagement: a black-box recorder, in case we were later called as witnesses. More than once, we were.

**Houghton Mifflin** was a case in point. "Turn on the new system on January 1 bacause that's easy for accounting." The IT manager had already been fired. The company was weeks from being unable to close the books. The hardware was Honeywell—which meant every IBM-era tool and habit I had developed over a decade was suddenly useless. We managed to avert catastrophe, but the experience clarified something I had been sensing for years: the real danger in technology projects is rarely technical. It is political, managerial, and financial misalignment wrapped around a project that was mis-scoped, mis-priced, or mis-governed before the first line of code was written.

**United Shoe Machinery** made that point in neon. AKA Unmitigated Software Mess. ADLS management had decided to migrate code written for an IBM 4300 mainframe to a Data General Eclipse minicomputer—a move that violated the basic architectural physics of both platforms. The system was thrashing at every level: at the CPU, at the application layer, the disks, and in the boardroom.

> **Sidebar: Why Platform Migration Is Rarely "Just a Porting Exercise"**
>
> Moving an application from one hardware platform to another sounds simple in a project plan—"we will recompile the code on the new machine." In practice, every application contains thousands of implicit assumptions about the hardware it runs on: memory addressing modes, I/O channel behavior, interrupt timing, floating-point precision, and dozens of other details that are never documented because the original developers never imagined anyone would care. When you move to a different platform with different assumptions, every one of those implicit dependencies can become an explicit failure. The United Shoe migration had all of these problems simultaneously, on a system that was already in production and managing real business transactions. It was not a software project gone wrong. It was an architectural mismatch that had been approved by people who did not understand the physics.

Working with Frank Hawthorne, ADL Systems' GE-trained chief financial officer (CFO), I helped conduct a midyear audit of the firm's OEM (original equipment manufacturer) contracts. We uncovered a significant problem: management had been booking volume discounts as instant profit before the sales volume that would generate those discounts had actually been achieved. It was a classic earnings inflation—a pending liability that would eventually have to be reversed.

Reporting that number was one of the defining professional moments of my career. It crystallized a conviction that has never left me: bad accounting can kill a company faster than bad code.

---

## The Capitalist Awakening

By the end of my seven years at ADL, I had seen systems fail in nearly every way a system can fail: technically, organizationally, financially, politically. I had written code in Boston winters and Rio heat waves. I had interviewed paper-mill foremen, police dispatchers, bank auditors, and utility engineers. The education was real, deep, and impossible to simulate in a classroom.

But I had also been quietly developing a second education, in parallel: I had started trading Wang Laboratories stock options in my early twenties and was watching the rhythms of the technology market with increasing attention. The technology investment world was not abstract to me. I had seen these companies from the inside.

When I looked at ADL's business model through that investor's lens, I didn't like what I saw. The firm specialized in fixed-price, turnkey contracts at precisely the moment when the complexity of information systems was exploding beyond anyone's ability to scope them reliably. We capped our upside—a fixed fee—while leaving the downside wide open. If the project ran over, we absorbed the loss. If the client added requirements, we absorbed the loss. We were taking equity risk for consulting fees. This was not selling applications; it was fix-pricing custom development. I could see lawsuits coming.

At the same time, the minicomputer revolution was gathering force. Computing was escaping the glass house. DEC, Data General, Prime, and a dozen others were selling machines that real businesses could operate without a priesthood of systems programmers. The economic center of gravity was shifting from the people who built systems to the people who designed and sold them.

I felt like a man who had spent a decade mastering the kitchen knife—genuinely skilled at it, proud of the craft—only to realize that the real leverage had migrated to whoever designed the menu and owned the franchise. I could keep perfecting my technique. Or I could step into a role where I could shape the market itself.

I left Arthur D. Little and walked into the marketing offices of Prime Computer.

I left my coding pad behind. That was not a repudiation of the work. It was a recognition that the physics of the industry had changed. In the world I had been trained for, computer time was the scarce resource and human labor was cheap. By the end of the 1970s, that equation was inverting. Human judgment based on experience—the ability to understand the messy interface between technology and organizational reality—was becoming the scarce resource.

That was the asset I intended to compound.

---

*Next: Chapter 4 — Prime Computer*



---




---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | volume-1-ch03-physics-of-consulting-1972-1979 |
| title | Chapter 3: Eight Years in the Physics of Consulting (1972–1979) |
| author | Peter S. Kastner |
| date | 2026-05-14 |
| type | memoir |
| subject_domain | memoir/volume-1 |
| methodology | oral-history |
| source_file | MASTER-EBOOK-ASSEMBLED-v4.md (Chapter 3: Eight Years in the Physics of Consulting (1972-1979)) |
| license | CC-BY-4.0 |

### Abstract

Peter Kastner recounts his eight years (1972–1979) at Arthur D. Little (ADL) in Cambridge, where he shifted from machine-level programming at Philip Hankins Inc. to broad-based consulting across banking, healthcare, manufacturing, utilities, and public safety. Through engagements at Chase Manhattan Bank, a Rio de Janeiro hospital, Continental Forest Industries, Wisconsin Electric, Hampton VA Police, Houghton Mifflin, and United Shoe Machinery, he developed a systems-failure taxonomy centered on organizational, political, and financial misalignment rather than purely technical failure. The chapter closes with Kastner’s capitalist awakening: watching the minicomputer revolution invert the economics of computing, he left ADL for Prime Computer, trading a coding pad for a market-shaping role.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Documents formative consulting methodology across seven major engagements spanning banking, healthcare, manufacturing, utilities, and public safety, establishing Kastner’s enduring conviction that systemic failure is organizational rather than technical. |
| **Relevance** | high | Rich primary-source account of 1970s IT consulting practice, platform migration physics, and early minicomputer economics directly relevant to computing history and technology strategy. |
| **Prescience** | high | Kastner’s 1979 observation that fixed-price custom development exposed consulting firms to equity-level risk while capping upside presaged the wave of project litigation that struck ADL and peers in the 1980s–1990s. |

### Prescience Detail


**Prediction 1:** Lawsuit risk from fixed-price custom development
- **Claimed:** ADL was taking equity risk for consulting fees on fixed-price custom development; Kastner could see lawsuits coming.
- **Year:** 1978
- **Confidence at time:** high


### Entities Referenced (21)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Arthur D. Little | firm | dissolved |  |
| Arthur D. Little Systems | firm | dissolved |  |
| Peter S. Kastner | person | active |  |
| Philip Hankins Inc. | firm | dissolved |  |
| Philip Hankins | person | unknown |  |
| Wang Laboratories | company | dissolved |  |
| Murray Sherry | person | unknown |  |
| Chase Manhattan Bank | company | acquired | JPMorgan Chase |
| David Rockefeller | person | unknown |  |
| Univac | company | acquired | Unisys |
| IBM | company | active |  |
| Continental Forest Industries | company | unknown |  |
| Wisconsin Electric | company | acquired | We Energies |
| Hampton, Virginia Police Department | agency | active |  |
| St. Petersburg, Florida Police Department | agency | active |  |
| Houghton Mifflin | company | acquired | HarperCollins |
| Honeywell | company | active |  |
| Frank Hawthorne | person | unknown |  |
| Data General | company | acquired | EMC Corporation |
| Prime Computer | company | acquired | Computervision/Parametric Technology |
| Digital Equipment Corporation (DEC) | company | acquired | Compaq/HP |

### Technologies Referenced (9)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| COBOL | language | industry-standard | mature | legacy-supported |
| Univac 96-Column Punch Card | platform | Univac | declining | legacy-end-of-life |
| 96-Column Card Format | platform | Univac | declining | legacy-end-of-life |
| IBM 4300 Mainframe | platform | IBM | mature | legacy-end-of-life |
| Data General Eclipse Minicomputer | platform | Data General | growing | legacy-end-of-life |
| Power-Line Carrier Communication | protocol | industry-standard | emerging | active |
| Automatic Meter Reading (AMR) | application | industry-standard | emerging | active |
| Magnetic Tape (800 bpi) | platform | industry-standard | mature | legacy-end-of-life |
| Honeywell Computer System | platform | Honeywell | mature | legacy-end-of-life |

### Observation Summary

- Total observations: 78
- By type: personal-recollection: 40, expert-opinion: 22, topic-insight: 11, market-data: 4, viability-prediction: 1
