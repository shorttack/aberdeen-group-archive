---
title: "Arguments with Reality"
subtitle: "Fifty Years in Computing, Consulting, and Consequence"
author: "Peter S. Kastner"
year: 2026
---

*For everyone who sorted the paper — and everyone who built the machines that finally handled it.*

---

## Contents

- Introduction: The Physics of the Machine
- Chapter 1: Waiting for Automation *(1960–1969)*
- Chapter 2: The Physics of the Machine *(1969–1972)*
- Chapter 3: Eight Years in the Physics of Consulting *(1972–1979)*
- Chapter 4: Prime Computer *(1979–1981)*
- Chapter 5: Stratus Computer — Six Years in the Fault-Tolerant Wars *(1981–1987)*
- Chapter 6: Digital Equipment Corporation — From Benchmarks to the TPC *(1987–1988)*
- Chapter 7: Founding Aberdeen Group *(1988–1997)*
- Chapter 8: The Go-Go Years — Aberdeen at Scale *(1998–2006)*
- Chapter 9: Expert Witness — Technology on Trial *(1992–2015)*
- Chapter 10: The Long View — What Fifty Years of Technology Markets Teach *(1966–2026)*
- Epilogue: The Argument with Reality
- Appendix: Career Timeline
- About the Author

---

# Introduction: The Physics of the Machine

I grew up sorting paper.

Every summer from age twelve, I worked in my family's restaurant on Cape Cod—a place that served more than a thousand diners a night and generated tens of thousands of paper slips to prove it. My job was to reconcile them: every drink, every appetizer, every bottle of wine, traced back to a check, matched to a cashier deposit, to the penny. It was tedious, it was irreducible, and it was everywhere. The Federal Reserve employed half a million people doing essentially the same thing—sorting, touching, re-touching checks as they moved through the American banking system. Making an airline reservation took a half-hour phone call and a trip to a travel agent to collect a physical ticket. Commerce was extraordinarily labor intensive.

I decided, before I left for college, that this was not how humanity should be spending its time.

That conviction—that machines should handle the paper and people should handle everything else—became the organizing principle of a fifty-year career spent inside the machine. What I did not know at twelve, and only gradually came to understand at MIT, in a converted funeral home in Arlington (MA)), across a securities migration at Chase Manhattan, inside the Stratus fault-tolerant lab in Marlborough (MA), through DEC’s enterprise war rooms, and over eighteen years co-founding and building Aberdeen Group, was that information technology is never just about technology. It is about the collision of systems with institutions, economics, and human nature. To work inside the machine is to discover that every information system is really an argument with reality.

This book is the memoir of that education.

## “What This Book Is”

**What This Book Is—and Is Not**

This is not a conventional history of the computer industry, though it passes through most of the major transitions that defined the last half-century: batch computing, timesharing, minicomputers, fault-tolerant OLTP, the client-server revolution, the open systems wars, PCs and the internet era, and the rise of the research industry that helped enterprises make sense of them.

This is not a standard business autobiography, though it follows one career from junior programmer to chief research officer of a firm that eventually grew to 150 analysts. It is, instead, an account from inside the machine room, the consulting engagement, the sales organization, the boardroom, and the analyst firm—an account of how technology actually entered institutions, what resisted it, what accelerated it, and why the outcome was so rarely determined by engineering alone.

Some of the stories are operational: Apollo veterans who taught me that sloppy code is a moral failing; a Y2K fix made in 1969, thirty years before it became a global panic; the benchmark we ran in secret using two IBM mainframes to ambush the enterprise computing industry. Some are organizational: why Aberdeen’s cooperative revenue model worked, what happened when venture capital changed the incentives, and why the company that acquired us paid a premium for a culture it could not preserve. Some are simply human: a customs inspector in Rio unspooling magnetic tape onto an airport floor, or a trade-show handoff that produced one of the more memorable T-shirts in Route 128 history.

## “How to Read This Book”

**How to Read This Book**

The chapters follow a broadly chronological arc, but they can also be entered independently. A reader interested mainly in the fault-tolerant wars at Stratus, the DEC benchmark campaign, or the founding and scaling of Aberdeen should be able to enter at those chapters without losing the thread.

For readers who go straight through, the through-line is simple: each era placed me inside a different kind of machine. Sometimes the machine was literal—a mainframe, a minicomputer, a fault-tolerant system, a benchmark lab. Sometimes it was an organizational machine—a bank operations center, a consulting firm, a high-growth vendor, a venture-backed research company. The lesson, repeated often enough to become conviction, was that technology works only when it aligns with the structure and incentives of the humans around it.

Five analytical frameworks developed during the Aberdeen years appear explicitly in the later chapters, but their outlines are visible much earlier—in the bookkeeping rooms of Cape Cod, the securities factory at Chase, the benchmark room in Westwood (MA), and the market battles of Prime, Stratus, and DEC. Readers who notice those patterns early will understand the larger argument of the book before it is formally stated.

A note on voice: the early chapters introduce Peter Kastner in the third person, because those events happened to a young man who could not yet have narrated them with the perspective the story requires. The later chapters shift into first person, once the work becomes less about being formed by events and more about helping shape them. The shift is deliberate.

An archive of primary materials from the Aberdeen years remains available on GitHub. There are tools to browse and query the research, which is one of the deepest available on the 1990s.

---

---


---


# Chapter 1: Waiting for Automation
### *A Student's Guide to the 1960s*

---

Peter S. Kastner was born in 1947 and grew up in Chatham, on Cape Cod, Massachusetts. His parents had purchased an old sea captain's house with a small attached restaurant, and over the next six years that modest establishment expanded into something remarkable: six dining rooms seating 575, cocktail lounges for 200, and an opera house for 300 more, with review shows and dancing. During the June-to-September season, it was common to have more than a thousand diners a night pass through the doors. It was a five-star destination.

It was also, from a bookkeeping standpoint, an absolute disaster.

---

## The Paper Problem (Cape Cod, 1960)

A table for two with a couple of drinks, an appetizer, entrees, dessert, and a bottle of wine would generate six separate pieces of paper before the couple left for the Opera House. Each piece of paper documented a transaction between a server and a food or beverage station. You could not get a drink at the bar without a paper slip tied back to the customer's check. Multiply that by a thousand diners and you have ten thousand pieces of paper produced every single evening—all of which had to be reconciled the next day.

Why go to this trouble? The answer, as Kastner learned early, is human nature. Servers are independent business people with the ability to collect cash from customers and merchandise from the bar and kitchen. Unless watched closely, some will help themselves. So, tedious as hell, young Peter spent his summers matching checks to receipts, hunting discrepancies, and balancing cashier deposits to the penny. It was Basic Business Controls 101, delivered at age twelve.

By his third summer, he had been promoted to manager of the bookkeeping department. The tools at his disposal were adding machines, pencils, and lined accounting workbooks. No matter how he racked his brain, he could not find a way to make the job faster, smarter, or less soul-crushing. Moving ten thousand pieces of paper around was neither a scalable economic activity nor one that seemed likely to help humanity achieve a higher level. He wanted machines to handle the paper.

This was, it turned out, a perfectly rational observation about the entire American economy. The Federal Reserve Bank employed nearly half a million people every night just to sort the checks moving through the financial system—physically returning each check to the bank on which it was drawn, where employees sorted them down by branch, then by account, then matched them with statements and mailed them out. Every single check was touched, at minimum, half a dozen times by human hands. Making an airline reservation required a half-hour telephone call and a trip to the travel agent to collect a physical ticket. Commerce was extraordinarily labor intensive, and almost nobody in 1960 thought there was anything unusual about that.

Peter Kastner did.

---

## Cornell, First Attempt (1965–1966)

He arrived at Cornell University's School of Hotel Administration in 1965 convinced he would find his automation answers there—and have a good time along the way. The first Friday concert featured The Beach Boys. The second featured The Rolling Stones. The fourth was Bob Dylan. On those counts, Cornell delivered.

On the automation front, not so much.

He took a job at the Hotel School's model hotel to learn how operations were supposed to work. No automation there: the front desk ran on an NCR paper-tape cash register, and cash procedures were nearly identical to what he had left behind on the Cape. There were no plans to change that.

His big opportunity came through the annual Hotel Ezra Cornell (HEC) weekend, a long-running tradition in which students produce and manage a full hotel experience for industry executives. The upper-class accounting team decided to try something ambitious: automate the books for HEC using a room full of donated IBM punch-card tabulating equipment. Kastner signed up immediately.

> **Sidebar: Punch-Card Tabulation—What It Could and Couldn't Do**
>
> IBM's punch-card tabulating machines of the 1960s were electromechanical sorters, collators, and accumulators—not computers in the modern sense. They could count, sort, and add columns of numbers encoded on 80-column cards, but they were programmed not by software but by physical wiring on a plugboard: you literally patched cables from one function to another like an old telephone switchboard. The team's plan—capture source transactions on punch cards and summarize them into balance sheet reports—was sound in theory but required the tabulator to perform conditional logic (if this transaction belongs to category A, add it to total A) that the machine's wiring simply could not execute with sufficient flexibility. Several months of effort produced an elegant design and an infeasible implementation.

After months of learning the equipment, designing the application, and attempting to wire the tabulator into doing what they needed, the team had to concede defeat. "Our eyes were bigger than what the technology could deliver," Kastner recalled later. The accounting team fell back on paper receipts and human bookkeepers—exactly the system he had left behind on the Cape.

He took a year off from Cornell. If he was going to solve the automation problem, he needed to understand computers at their foundation, not at the level of plug-wired tabulating machines. He would become a computer programmer. He took a job at the Massachusetts Institute of Technology (MIT) as a full-time computer operator while looking for a path into programming.

---

## MIT (1966–1967)

The computing center at MIT in 1966 ran three machines, and Kastner was trained to operate all of them.

> **Sidebar: MIT's Three Machines**
>
> - **IBM 1401**: A workhorse reader-printer. It ingested batches of punch-card decks, wrote them to magnetic tape at 800 bits per inch, and printed the output that came back from the mainframe. Think of it as the loading dock.
> - **IBM 7094**: The production mainframe. During most daytime hours it ran timesharing—dozens of academic users typing at alphanumeric terminals simultaneously. Off-peak, it rebooted into batch mode and ground through jobs queued on tape. The 7094's timesharing work was historically significant: the techniques developed here fed directly into the Multics operating system, which would resurface in Kastner's career a decade later at Stratus Computer.
> - **IBM 360/65**: A newer machine dedicated mostly to development. Base FORTRAN airflow-analysis code written on this machine was still embedded in climate models as late as the 2020s. It also had an attached graphics workstation with a trackball—an exotic luxury in 1966.
>
> The three machines together formed a pipeline: cards in, tape to the mainframe, results back to the 1401, paper out. This batch processing model—submit a job and wait—defined the economics of computing for the next decade.

Computer operations, Kastner learned, is factory work in a white coat. The rooms were noisy. The pressure to keep jobs moving through the pipeline was constant. The pay was modest. But the job had one perk that more than compensated: the ability to run programs on the operator's own accounts during quiet overnight hours. He taught himself FORTRAN and IBM assembler on the company dime—or rather, on the company's very expensive but idle CPU cycles.

MIT in 1966 was a riot of computing innovation, and the computer room was where it all came through. One night, a *Spacewar!* video game appeared permanently installed on the 360/65's graphics workstation. On a dull overnight shift, you could use a $5 million mainframe to play B&W video games. On another occasion, Kastner helped a cryptic researcher run classified simulations. "Things that go boom," the researcher said, and offered no further explanation.

More durably important was what was happening a block away at Project MAC—the Multiple Access Computer project—where Kastner's roommate worked. Project MAC was developing the foundations of timesharing and multiuser computing that would eventually produce the Multics operating system. In the hallways, researchers argued about artificial intelligence with a fervor that felt more like religion than engineering. LISP—the List Processing language—was being used to manipulate symbolic representations of knowledge; a program called ELIZA was having text-based conversations with users in ways that unnerved people who didn't know it had no inner life whatsoever. From the operator's console, Kastner had a useful vantage point on all of it: AI wasn't magic, it was just more code competing for time on the same machines that ran payroll and climate models.

Early Digital Equipment Corporation (DEC) PDP/8 minicomputers were appearing in labs around Cambridge. The glass-house era—when computing meant a centralized room behind locked doors—was beginning, almost invisibly, to crack.

After a heady year in Cambridge, he returned to Cornell with a dual credential: operations and programming. He wanted to put them to use.

---

## Cornell, Second Attempt (1967–1968)

There was exactly one university programming job open in the fall of 1967. It required experience in IBM's PL/1 programming language for a library project. Nobody had years of PL/1 experience in 1967, including Kastner, so the job went elsewhere.

> **Sidebar: Why PL/1 Was a Difficult Ask**
>
> IBM's PL/1 (Programming Language One) was designed in the mid-1960s as a unified language for both scientific computing and business data processing—essentially an attempt to merge FORTRAN's mathematical muscle with COBOL's structured data handling. It had the cryptic syntax of C or FORTRAN combined with the elaborate data-naming and file-management conventions of COBOL. It was powerful and, for 1967, extremely new. Asking for experienced PL/1 programmers was roughly equivalent to asking for experienced ChatGPT programmers in 2020. They did not yet exist in quantity.

He negotiated his way into a job operating Cornell's brand-new IBM 360/65 mainframe. The university had a firmly applied policy of paying students the federal minimum wage: two dollars an hour. Kastner interpreted that to mean $2.00 plus unlimited computer time at no additional charge. That made it a fair deal.

Operations manager Dave Pulleyn was relieved to have an experienced 360/65 hand, and immediately assigned Kastner to Sysgen Day.

> **Sidebar: What Is a Sysgen?**
>
> A systems generation (Sysgen) is the process by which a computer literally creates its own operating software from source code and configuration parameters. IBM at this time provided the source code for its operating systems to customers—a practice it would abandon in the 1980s as software became a separate business. The process required loading hundreds of punch-card decks in the correct sequence, waiting while the machine compiled itself into a working system, and hoping nothing went wrong. If it did, you started over. Cornell's Sysgen target was a modified version of IBM OS/360, the standard mainframe operating system, enhanced with the Houston Automated Spooling Processor (HASP), which managed the queue of jobs waiting to run. The day mostly consisted of Kastner and systems programmer Arlene Larsen sitting around while the machine did its work.

On the sunny morning of Saturday, September 23, 1967, Larsen wheeled in a tray of punch cards and a 2311 disk pack (13 megabytes—an enormous amount of storage by the standards of the day). They sat. The machine compiled itself. It was a success.

Cornell had originally planned to install an IBM 360/67, a timesharing-capable variant, to match what MIT was running on its 7094. IBM couldn't deliver the 360/67. Cornell scrambled and pivoted to an innovative workaround: remote job entry over a dedicated 56-kilobit telephone line from Upson Hall on campus to the data center at Langmuir Labs, a former GE research building off-campus. A CDC 1604 at Upson read student card decks and sent them to Langmuir; the 360/65 processed them and returned print-image files. The 360/65 was, in effect, Cornell's cloud—a concept that would not have a name for another forty years.

A few weeks later, on Halloween night, a fierce thunderstorm moved through Ithaca. Kastner was on duty when water began dripping from ceiling tiles directly onto the input-output electronics cabinet. He had three options: do nothing and call someone (while the machine shorted out); pull the Emergency Shutdown switch (which would physically disable the computer for days while IBM rewired it); or perform an orderly shutdown. He chose orderly shutdown, sprinted to find a plastic drop-cloth from a nearby construction site to shield the wet cabinet, and called for help. He was not fired.

With two shifts a week plus overtime, there was ample time to program. He wrote FORTRAN jobs for clients and coursework, automated a Statistics 101 lab exercise that had previously required hand-cranked mechanical calculators, and handed in a one-sheet printout to a grad-student instructor who had been expecting the usual stack of manually computed results. The grad student demanded an explanation. He became a consulting client.

And then there was CHASE.

---

## Simulation and the First Real Application (CHASE)

Robert M. Chase was an accounting professor at the Hotel School who had been working on something unusual: computer simulations that let student teams manage a virtual hotel, making pricing and staffing and inventory decisions and watching the financial consequences play out. He had named it CHASE—Cornell Hotel School Administration Simulation Exercise—and was building companion programs called CRASE (Cornell Restaurant Administration Simulation Exercise) and CHESS (Cornell Educational Strategic Simulation), the last of which was the first program in the Hotel School to run in real time.

Chase and Kastner had met when Chase taught him first-year accounting. Now Chase needed a programmer who understood both accounting and the 360/65. Kastner took on enhancing and debugging CHASE during the 1967–68 academic year.

The core problem was a classic and infuriating one: FORTRAN was a scientific language that used floating-point arithmetic—the way scientists represent very large and very small numbers approximately. In science, being off by a fraction of a percent is fine. In accounting, where every debit must equal every credit to the penny, it is not fine at all. Kastner spent weeks hunting down the places where the imprecision of FORTRAN's scientific notation was making the simulation's books come out a few cents off—driving accountants batty and undermining the educational credibility of the whole exercise. He fixed it.

Chase's simulations eventually went far beyond Cornell: Intercontinental Hotels, Marriott, Howard Johnson's, and KFC all adopted them for management training. Hospitality schools worldwide used them for decades. In 2024, Chase was inducted into the Hotel School's Hall of Fame. It was legitimately important work, and Kastner's contribution to making the arithmetic honest was a small but real piece of it.

Yet for all that satisfaction, he still had not found the automation he was looking for. The simulations were elegant. They showed what computers could do for education. But they were not transforming how actual businesses processed their actual transactions. He and Cornell parted company.

---

## The Education, in Summary

He left Cornell in 1968 with three years of programming experience, two years of mainframe operations, a working knowledge of IBM's systems architecture from the machine-room floor up, and a conviction that had only deepened with every failed attempt to automate the Cape Cod restaurant from a college campus: that technology's job was to serve human purposes, not to impress other technologists.

The technology of the 1960s had limits, and those limits were real. Punch-card tabulators could not do conditional logic at scale. Timesharing was brilliant but fragile. FORTRAN's floating-point arithmetic was wrong for accounting. IBM could not always deliver what it had promised to universities that had planned around it. Every one of these obstacles had taught him something more useful than success would have: that a system is not just its code. It is its hardware constraints, its institutional context, its economic incentives, and the human beings who have to live with it every day.

He set his sights on Boston—the center of the computing universe in 1968—and took an application programming job at Philip Hankins Inc. (PHI), the largest data center in Boston and a serious software development house.

The paper problem was still unsolved. He was just getting started.

---

*Next: Chapter 2 — The Physics of the Machine*



---


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


# Chapter 4: Prime Computer
### *(1979–1981)*

---

I arrived at Prime Computer around Thanksgiving 1979, just as the place was turning from a scrappy minicomputer vendor into a fully-fledged Wall Street rocket ship.

From Prime Park on Route 9 in Natick, you could feel the acceleration in the parking lot: new glass going up, rental cars crowding the visitor spots, headhunters circulating in better suits than most of the engineers wore. In six years, CEO Ken Fisher had taken Prime from a $10 million hopeful to a serious growth franchise. By 1980 the company sat in the same analyst slide decks as DEC, Data General, and HP when people discussed who might challenge IBM from below.

That wasn't just editorial positioning. In 1980, Prime was the number-one moving stock on the New York Stock Exchange, up approximately 272 percent for the year. It was exactly the kind of name that made portfolio managers at the Boston Harbor Hotel lean over their Cobb salads and ask, *"So, what's your PR1ME position?"* Investor Relations VP Chuck Casale — who would later become my partner at Aberdeen Group — had an easy two years. When the stock is up 272 percent, the story sells itself.

I had come from eight years of building systems under fixed-price contracts, absorbing all the risk while the upside was capped. Prime was the other side of that equation. The upside here was visible in the parking lot every morning.

---

## What Prime Actually Sold

Prime's go-to-market engine was a hybrid of old-line mainframe discipline and Route 128 swagger. The company thought in classic minicomputer terms — named accounts, territorial sales offices, heavy sales-engineering overlay — but had learned to package all that around specific business problems rather than raw MIPS and megabytes.

You didn't sell a 750 or a 50-series. You sold "an on-line banking platform" or "an interactive engineering environment." The customer discovered only later that what they had actually bought was a Prime 750 running PRIMOS, Prime networking, and a 4GL database environment descended from an architecture called Pick.

> **Sidebar: What Was Prime INFORMATION?**
>
> Prime INFORMATION was a database and application development environment based on the Pick operating system, an architecture developed in the 1960s for inventory and distribution systems. Pick organized data into multi-value fields within what it called "dynamic arrays" — a structure that could hold variable numbers of entries in a single field, unlike the rigid column-and-row structure of relational databases.
>
> This was simultaneously Pick's greatest strength and its eventual weakness. For commercial applications in the early 1980s — banking, insurance, service bureaus — multi-value records mapped naturally to real-world data structures. A customer account could hold a variable number of transaction records. A purchase order could hold a variable number of line items. You didn't need to join tables. The data lived the way the business thought about it.
>
> The weakness: Pick/INFORMATION was proprietary. Every application built on it was a captive of Prime hardware. As open systems and relational databases grew through the 1980s, that lock-in became a liability rather than a feature. But in 1980, it was a clean narrative: faster application development, tighter integration, and no army of COBOL programmers required.

Against DEC's VAX ecosystem, the Prime argument was responsiveness: shorter application cycles, tighter integration, and the promise that a mid-sized regional bank could look like a national institution on a modest minicomputer footprint. VARs, OEMs, and independent software houses that built vertical packages on INFORMATION served as force multipliers. "PR1ME shops" were a club with their own language and lore, and the club felt exclusive in a good way.

There was one quiet operational superpower I noticed early: Prime maintained a one-to-one ratio of sales executives to sales administrators in its field offices. In most companies that ratio was much worse. In the quarter-end tornado—when contracts were flying and the SEC was watching—those admins were the ones who kept the paperwork inside legal guardrails. Unlike some of my later Aberdeen clients—Computer Associates and Informix come to mind—no one from Prime ever went to jail for cooking the books.

---

## The Circus Comes to Town

I came into Prime through Market Planning. Peter Schlegel — who ran the group and happened to be the brother of an ADL colleague — recruited me and handed me the commercial vertical markets to cover, working alongside Steve Franson.

That assignment lasted roughly as long as the Thanksgiving leftovers.

By Christmas, Schlegel had been given the job of launching Prime Office, the company's thrust into office automation, and moved to product planning. Franson became executive assistant to sales VP Bob Clausen and moved upstairs. I was left, nominally, with "all the commercial customers."

Then I learned the internal rules: if a customer did anything technical or scientific — CAD/CAM at Ford, avionics at General Dynamics — they belonged to the technical side of the house, not to my "commercial" territory. My glorious client roster shrank accordingly.

**The Lake Tahoe Education**

About a month in, I attended the annual sales kickoff at Lake Tahoe. Night one: Bob Clausen at the craps table, making thousand-dollar bets, thirty salespeople cheering around him. Day two: product roadmaps. Day three: skiing at Heavenly, followed by the awards banquet. Day four: back on the plane.

It was a perfect snapshot of the era. High confidence, high energy, absolute certainty that the good times would keep rolling. The machine was printing money, the stock was up 272 percent, and nobody wanted to hear about downside scenarios.

From the perspective of someone who had spent eight years at ADL pricing risk on fixed-fee contracts, the culture was exhilarating and slightly alarming in equal measure.

---

## Finding the Work That Mattered

The internal competition for territory eventually sorted itself out. Dick Tarulli, a district sales manager from Ohio who had beaten me for the director's job, reorganized along more conventional vertical lines. Government ended up with me — which turned out to be one of the more interesting assignments of my career.

We were encouraged to understand our markets globally. For government, that meant trips to England, France, Japan, and Australia.

In Cheltenham, I visited GCHQ — Britain's signals intelligence headquarters — where a Prime system was doing satellite photo analysis on the Iran-Iraq war. I'd been vetted by the CIA and MI6. The visit itself was unremarkable in the way that highly classified facilities always are on the surface: normal people in normal offices doing work that, once you understood it, was anything but normal.

In France, where government was roughly half the entire economy, every regional opportunity traced back to Paris. In Japan, the local Prime manager played gracious tour guide through a government landscape dense with ministries and procurement rituals. In Australia, Prime's most audacious dealer, Lionel Singer, had done something no one else in the minicomputer industry had managed: he had put Prime Computer in television commercials alongside the then-popular *Doctor Who*. It worked.

**PROMIS and the New Jersey Caper**

Back in the United States, the Reagan defense buildup was creating a steady tailwind. I got a *New York Times* quote. The first initiative that really caught our attention was PROMIS — a prosecutor case-management system developed by INSLAW, a Washington D.C. software company, using the same federal LEAA grant stream that had funded ADL's law enforcement systems work years earlier.

> **Sidebar: What Was PROMIS?**
>
> PROMIS (Prosecutor's Management Information System) was developed by INSLAW Inc. in the 1970s under a federal grant to automate the management of criminal cases. It tracked defendants, charges, hearings, evidence, and outcomes in a unified database — giving prosecutors and court administrators something they had never had before: a complete picture of where every case stood at any given moment.
>
> The Department of Justice awarded INSLAW a contract to deploy PROMIS across the federal prosecutor system. Prime won the hardware business for more than twenty systems. The story later grew considerably darker — INSLAW alleged that the Justice Department stole its software and sold it to foreign intelligence agencies, a claim that sparked years of congressional investigations and litigation. At the time we were selling the hardware, however, PROMIS was simply an impressive early example an appliactions-generator of information management in public safety: the kind of system I had been trying to build since my days at ADL working with police departments in Florida and Virginia.

The Prime field team launched my program to push PROMIS at the state level as well. One New Jersey bid became a minor operational legend. The local team managed to deliver only four of seven required proposal copies by the deadline — their copy shop had failed. Undeterred, they returned to the state house in Trenton after dark, found an unlocked window, and "delivered" the missing copies to the bid room.

A few weeks later I sat in corporate counsel Bernie Bradstreet's office while he patiently explained to the team why Prime would not be suing New Jersey over a clearly non-compliant bid. That was Prime in miniature: enormous initiative, occasionally creative interpretations of process, and just enough adult supervision to keep everyone out of jail.

**The White House**

The best résumé line from my Prime years arrived courtesy of Schlegel, who returned the favor of having recruited me by delivering Prime Office — running on a Model 750 — to the White House as the first office automation system at the federal executive level. I was on the periphery of that project, but it was the kind of reference account that stopped conversations cold in any sales meeting.

---

## The Market Research Rehearsal

In 1981, Tarulli assigned me to lead a project to define future product requirements for all of Prime's planned vertical markets — a pure market-research exercise with no delivery obligation attached. I spent months talking to customers, partners, and prospects, synthesizing what I heard into a structured product requirements document.

In retrospect, that project was a complete rehearsal for what I would spend a decade doing at Aberdeen Group. The analytical discipline — segment the market, identify the customer's actual problem, quantify the gap between what exists and what is needed, map the competitive landscape — was identical. The only difference was that at Prime I was doing it for an internal product planning audience rather than for paying clients.

The document still exists in my archive. Reading it now, it reads like an early Aberdeen report: structured, market-focused, and slightly more optimistic about the pace of technology adoption than events would warrant.

---

## The Fisher Departure and the Exit Signal

From inside Prime Park, Ken Fisher's "resignation" in 1981 never felt like a midlife sabbatical. It felt like the board blinking first in a long argument about direction and pace.

Fisher had built Prime into a genuine franchise by pressing advantages aggressively. By 1981 his instinct was to keep pressing — bigger architectural bets, more ambitious moves beyond the midrange comfort zone, an explicit push to make Prime a billion-dollar peer of DEC rather than a tidy niche player. The chairman and several directors were already worried about overreach: the capital intensity of Fisher's roadmap, the cultural strain of running the company as a permanent rocket ship, the risk of stretching the product line past what the engineering team could sustain.

Fisher left. The message from the hallways of Prime Park was clear enough: the next chapter would be a consolidation, probably under an imported IBM executive who would start by "professionalizing" the go-to-market machine I lived inside. The first thing such a leader typically does is reorganize staff marketing jobs.

I updated my résumé.

Not long after, a startup called Stratus Computer called.

---

## What Prime Taught

Two years at Prime completed an education that ADL had begun: the technology industry is not just a technical competition. It is an ecosystem of economics, vertical markets, market positioning, sales culture, and narrative.

At Prime I learned that the best technology does not automatically win. Prime INFORMATION was genuinely ahead of conventional COBOL-based systems for commercial applications in 1980. But it was proprietary. Every application it enabled created customer lock-in, which was an asset in good times and a trap in bad ones. When the relational database movement gathered force in the mid-1980s, Prime's application ecosystem — which was built on a non-relational, non-standard foundation — had nowhere to migrate. The lock-in that had been a competitive moat became a strategic prison.

> **A Note on Timing and Narrative**
>
> In 1980, the story that Prime told — tightly integrated hardware, OS, and application environment delivering faster results than IBM-compatible systems — was true and compelling. It was the story that Digital Equipment, Data General, and a dozen other minicomputer vendors were telling in different dialects. All of them were correct in the short run and almost all of them were wrong in the long run.
>
> The minicomputer era ended not because the hardware got worse, but because the economics of standardized x86 architecture and open operating systems overwhelmed the performance and integration advantages of proprietary platforms. The companies that read that shift early — and Prime's leadership was not among them — survived. The others became acquisition targets or museum pieces.
>
> This pattern — correct short-term story, wrong long-term architecture — would recur throughout the next two decades of my career at Aberdeen. Recognizing it became one of my core analytical skills.

I also learned something about sales culture that has stayed with me. The Prime salesforce was talented, aggressive, and genuinely believed in the product. But the culture of the Lake Tahoe kickoff — the craps table, the absolute conviction that the trajectory could only go up — was a leading indicator. Organizations that cannot imagine their own disruption usually get disrupted. Prime in 1980 could not imagine the world where an Intel-based server running Unix would render their minicomputer architecture economically irrelevant.

By the time I left for Stratus, I had a sharper sense of the question that would define the next decade of my analytical work: not "who is winning today?" but "what happens to today's winner when the economics change?"

---

*Next: Chapter 5 — Stratus Computer: Six Years in the Fault-Tolerant Wars*



---


# Chapter 5: Stratus Computer — Six Years in the Fault-Tolerant Wars
### *(1981–1987)*

---

I joined Stratus Computer on November 1, 1981, six weeks before the company announced its first product.

That timing was not accidental. I was hired as Manager of Marketing Development precisely because the company needed someone who could translate radical engineering into a market-moving story — and who could do it before the product was public. The engineering was extraordinary. The problem, as always, was making it matter in the marketplace. I landed running.

---

## The Problem That Created the Company

The computing world of 1981 had a problem it did not yet know how to name. Mainframes were powerful, but they were not built for uninterrupted operation. When a component in an IBM 4300 failed, the system crashed. You rebooted, recovered from logs, and restarted. In a batch-processing world, a thirty-minute recovery window was annoying but survivable. In the emerging world of ATM networks, airline reservation systems, and stock trading floors, thirty minutes was a catastrophe. Thirty seconds was unacceptable.

The industry had produced two competing answers.

**Tandem Computers**, founded in 1974 in Cupertino (CA), addressed the problem through software. Its NonStop architecture used pairs of processors, each with a complete copy of the application. Programmers had to explicitly write "checkpointing" code — periodic state saves — so the backup processor could pick up where the primary left off after a failure. Tandem was technically sound. It was also expensive in the currency that mattered most: programmer time.

**Stratus** took the opposite approach. The engineers in Natick (MA) decided that software should never know a failure had occurred. They built hardware-based fault tolerance using a **lockstep architecture**: four physical microprocessors doing the work of one, arranged in two pairs. A hardware comparator checked the results of each pair continuously. If one CPU failed, the comparator instantly took that pair offline and continued executing on the surviving pair — without losing a single clock cycle, without any software awareness of the event, without interruption of the running program.

> **Sidebar: What Is Fault-Tolerant Computing?**
>
> Most computers are designed on the assumption that hardware will be reliable most of the time, and that occasional failures are acceptable events that trigger recovery procedures — rebooting, restoring from backup, rerunning failed jobs. This assumption is workable for batch processing, where work can be interrupted and restarted.
>
> Fault-tolerant computing starts from the opposite assumption: for certain applications, *any* interruption is unacceptable. An ATM network that goes down for thirty minutes doesn't merely inconvenience customers; it processes zero transactions for thirty minutes — real revenue, real costs, real reputational damage. A stock exchange that drops off for ten seconds during peak trading creates legal and financial exposure.
>
> Fault tolerance is achieved in two broad ways. *Software fault tolerance*, as Tandem implemented it, requires the application developer to explicitly handle failure scenarios — detecting failures, saving state, switching to backup processes. This works but imposes significant development and testing burden.
>
> *Hardware fault tolerance*, as Stratus implemented it, hides failures from the software entirely. The application runs on hardware that has been designed to keep running through component failures. The software does not need to know a failure occurred because, from its perspective, nothing unusual happened. This approach costs more hardware but eliminates the programming complexity.
>
> The business case for both approaches was identical: calculate your cost of downtime per hour, compare it to the price premium for fault-tolerant hardware, and determine when the math works. Stratus's marketing job was to make that math vivid, personal, and unavoidable.

---

## The Pull-the-Plug Demonstration

We could not outspend IBM or Tandem on field sales. We had to be louder, faster, and more viscerally convincing. Trade shows became our proving ground.

The centerpiece of the Stratus demonstration was breathtakingly simple: we invited prospects to pull a CPU board out of a running system while it was processing transactions. The system did not crash. A red LED lit up on the failed component. The demonstration continued without interruption.

Ten seconds of theater replaced fifty pages of white papers.

The theater was not without its backstage drama. The evening before our public launch, VP of Hardware Gardner Hendrie could not reliably pull a board without crashing the system. Marketing had a sleepless night — as did Engineering. The culprit turned out to be the shiny Lexan plastic covers on the circuit boards, which generated static electricity when pulled from the slot. Dousing the demo-room carpet with water solved the launch-day problem, and Engineering Change Order #1 replaced the elegant plastic with cardboard.

The product launch was a success. The future of fault tolerance was briefly cardboard-covered.

---

## The Economics of Downtime

Marketing fault tolerance required building a new vocabulary for customers who had never been asked to quantify the cost of outages. Most IT managers in 1981 thought about systems in terms of performance and capacity. Availability was assumed; downtime was an operational embarrassment, not a financial metric.

We changed that by asking a single question: *What does one hour of downtime cost you?*

For an ATM network processing 10,000 transactions an hour at $40 average value, the arithmetic was straightforward. For a brokerage trading desk, the number was larger and more frightening. For a point-of-sale network at a large retailer, it translated directly into lost sales. We created direct-mail pieces with cost-of-downtime calculators customized by industry. We ran competitive displacement programs targeting Tandem users frustrated by the programming complexity of NonStop. The message was clean: *Keep your programmers. Change your hardware.*

The most powerful marketing development of my Stratus years was not a campaign or a brochure. It was a deal.

IBM came to us. After we nudged them.

IBM's sales force was watching their enterprise customers evaluate fault-tolerant systems, and IBM had nothing to offer them. After negotiations I contributed to but was not party to at the executive level, IBM agreed to rebrand the Stratus FT200 as the **IBM System/88**. Our marketing shifted overnight to a new anchor: *"The Technology IBM Chose."*

That single phrase neutralized every startup-risk objection. If your customer's primary concern was that Stratus was an unknown company with an uncertain future, you now had IBM's name on the machine. "No one ever got fired for buying IBM."

> **Sidebar: What the IBM OEM Deal Meant Strategically**
>
> Original equipment manufacturer (OEM) agreements — where one company's product is sold under another company's brand — were common in the minicomputer era. What made the IBM/Stratus deal remarkable was the direction: IBM, the most dominant technology brand in the world, was putting its name on a startup's product because it had no competitive alternative.
>
> For Stratus, it was validation that money couldn't buy. For IBM, it was a pragmatic solution to a gap in their portfolio. For prospects considering fault-tolerant systems, it answered the vendor-risk question entirely.
>
> The deal also created an interesting internal challenge: IBM's own salesforce now carried a product that competed with conventional IBM mainframes in certain use cases. We had to develop "battlecard" materials explaining the swim lanes — when to sell the System/88, when to sell a 3090, and how to keep the sale inside the IBM family rather than losing it to Tandem. The battlecards were essentially a conflict-resolution document for a company that was simultaneously our distributor and our competitor.

---

## The Debit-Credit Wars

By the mid-1980s the principal battlefield was banking and financial services, where ATM networks and point-of-sale authorization systems were expanding rapidly. Tandem and Stratus competed for every significant deal.

The competitive argument was sharp. Tandem claimed that our hardware approach was brute-force redundancy and that their software approach was architecturally elegant. We countered that their architectural elegance was being paid for by every application developer who had to write, test, and maintain recovery code. Our advantage was visceral: when a board failed, a red light came on. You pulled the board while the system kept running. You mailed it back to Stratus. No expensive on-site service engineer. No emergency maintenance contract clause.

We had turned hardware redundancy into a maintenance model. We called it "the board that mails itself."

The battlecard we developed for the IBM System/88 versus conventional IBM mainframes was particularly crisp. The argument centered on a concept we called the **"zero-code advantage"**: on a Stratus or System/88 system, you wrote standard COBOL or FORTRAN. Fault tolerance was invisible infrastructure. On Tandem, you paid a team of specialized programmers to write and maintain NonStop software. Total cost of ownership over five years — including programmer time, training, and ongoing maintenance — often reversed the hardware price advantage. We made that arithmetic easy to do and hard to argue with.

---

## A Men's Room Pivot

Sometimes the most important market planning does not happen in conference rooms.

I made one of the pivotal recommendations of my Stratus career in a men's room. The observation was simple: Rolm Corporation's digital PBX telephone systems needed exactly the reliability we provided. A PBX switching millions of calls was an always-on application if ever there was one. Telecommunications had the highest cost of downtime of any industry.

That insight, formalized and presented properly, led to a breakthrough in the telecom market. Stratus became embedded infrastructure for SS7 signaling and emerging digital switching systems, where five-nines uptime (99.999% — less than six minutes of downtime per year) was not a sales argument but an entry requirement for the contract.

The telecom DNA built in those years would eventually define Stratus's long-term trajectory, leading to its acquisition by Ascend and eventual integration into Nortel. The PBX observation in the men's room was the genesis of that arc.

---

## Cheyenne Mountain: The $50 Million Proof Point

In 1982, I received a cold call to present at Mitre Corporation, a federally funded research organization that works primarily with the Defense Department. Fifty silent engineers sat in the auditorium. They declined to state their requirements. I had one hour.

I made a calculated decision not to pitch fault tolerance alone. Instead I covered the full architecture: our programmable communications controllers, the modularity, the unusual data protocols we could handle, our spares strategy and field logistics. My assumption was that anyone who had arranged this meeting without stating requirements was dealing with a complex defense systems integration problem, not a simple uptime calculation.

The assumption was correct.

The meeting set off a slow chain reaction: Mitre brought in GTE Sylvania and Systems Development Corporation. The result, after an extended procurement process, was a landmark contract for NORAD — the North American Aerospace Defense Command.

By the late 1980s, Stratus had delivered $10 million in systems hardware and $40 million in spares to Cheyenne Mountain, Colorado, the granite-shielded nerve center monitoring the skies for nuclear threats.

The reference value of that contract was incalculable. When a prospect raised vendor risk — could they trust a startup for mission-critical infrastructure? — the answer wrote itself: if the United States Air Force trusted this machine inside a mountain during a nuclear threat, it could handle your department store's credit card authorizations.

---

## The Boss's Daughter

John Morgridge was my Vice President of Sales and Marketing at Stratus — ex-Honeywell, direct, likable, and very funny. He would later become Cisco's first non-founder CEO and build that company into a generation-defining enterprise.

After I had spent two and a half years running our trade show program, which kept me on the road, John called me in.

"Peter," he said, "I've got a management problem for you."

"How can I help?" I replied, with the wariness that phrase always deserves.

"Well, my daughter Kate's getting married next year, and I thought in the meantime she could do the trade shows for you. Free you up."

I considered this. "John, I take it the management problem is that if she's unhappy, you're unhappy?"

"You got that straight."

Kate Morgridge turned out to be excellent — organized, energetic, genuinely good at the work. Except for the first show, where she wore a T-shirt to a union work-site that read: *Stratus Computers Never Go Down On You.* She learned a great deal that day about human nature in the technology industry of the 1980s. We never discussed it further.

---

## The XA 2000 and the Exit

By 1987, I had been at Stratus for six years. The technology had matured from a regional curiosity to a recognized platform in financial services, telecommunications, and mission-critical retail. I led the market and product team for the **XA 2000** announcement — machines built on Motorola 68020 processors that delivered dramatic performance gains while preserving the lockstep fault-tolerant architecture.

Before departing for Digital Equipment Corporation, I left a parting gift to Stratus and the industry. John Logan, a former colleague from Prime who had settled at Yankee Group, retained me to ghostwrite a 100-page market research study titled *The Future of Transaction Processing*. Published in January 1987, the report predicted that the price-performance of microprocessor-based OLTP systems was about to explode — that Moore's Law was finally meeting the economics of departmental and/or distributed transaction processing, and that the displacement of the mainframe was inevitable.

Stratus later quoted that study in its 1987 annual report, which created a mildly interesting conflict of interest for my next employer. More on that in Chapter 7.

---

## What the Fault-Tolerant Wars Taught

Six years in a market that did not exist when I arrived produced a set of convictions that shaped everything I did afterward.

**Superior engineering is necessary but not sufficient.** Stratus's architecture was genuinely elegant — arguably more elegant than Tandem's, because it achieved the same outcome with less burden on application developers. But elegant architecture does not walk into a data center and sell itself. The pull-the-plug demonstration, the downtime calculator, the IBM OEM deal, the NORAD reference — these were the instruments that translated engineering advantage into market reality.

**Quantify the problem you solve.** "We prevent downtime" is a marketing claim. "Your ATM network loses $400,000 of transaction revenue per hour of outage, and our hardware costs $180,000 more than the alternative" is an argument. Stratus won deals when we made the second argument. We lost deals when the conversation stayed at the level of the first.

**The right market is not always the obvious one.** We launched into banking because the downtime math was visible and quantifiable. The telecom breakthrough — which ultimately defined Stratus's long-term position — came from a sideways observation in a men's room. Market planning that stays in conference rooms misses the oblique angles.

**Red lights sell more than white papers.** The most sophisticated technical sales tool we ever deployed was a demonstration that a customer could interrupt with their own hands. There is something irreplaceable about physical proof to humans. You could argue against a benchmark. You could not argue against the fact that the machine was still running after you had just pulled a CPU board out of it.

Stratus eventually transitioned from proprietary Motorola chips to Intel architectures, maintaining the lockstep edge as commodity hardware improved. The vision the company articulated in the 1980s — that computing infrastructure should be invisible, reliable, and self-healing — became the baseline expectation for digital commerce. Tandem disappeared into HP. Stratus survived as a specialized platform for environments where hardware failure cannot wait for a technician: remote oil rigs, manufacturing floors, telecom nodes.

The engineering approach evolved. The insight did not. In mission-critical computing, downtime is not merely expensive. It is unacceptable.

That is what Stratus proved, one pulled circuit board at a time.

---

*Next: Chapter 6 — Digital Equipment Corporation: Benchmarks, the TPC, and the Mainframe's Last Stand*



---


# Chapter 6: Digital Equipment Corporation — The Mainframe's Last Stand
### *(1987–1988)*

---

In late 1987 I arrived at Digital Equipment Corporation carrying two things no one knew about: an intimate technical knowledge of fault-tolerant computing from six years at Stratus, and fees from an $8,000 ghost-written market research study I had just finished for Yankee Group that predicted the gradual collapse of the mainframe's economic dominance.

My title was Marketing Executive — in DEC's idiosyncratic hierarchy, the highest-level individual contributor in marketing. My assignment, from a new group called Corporate Systems run by Bill Steul, was to "look around DEC for things that needed to be done to improve the enterprise position." It was an invitation to find a gap in the armor.

The gap was obvious the moment I started asking questions. Online Transaction Processing — OLTP, the heartbeat of banking, insurance, retail, and financial services — was still an IBM mainframe franchise. DEC had the VAX architecture, a genuine relational database in Rdb, and a transaction monitor. What it lacked was a competitive story backed by verifiable proof. I knew exactly where that proof was hiding.

---

## The Study Nobody Knew I Had Written

*The Future of Transaction Processing*, published by Yankee Group in January 1987, was my work. John Logan — a former colleague from Prime who had moved to Yankee Group — had hired me to write it for $8,000 and a month of late evenings. The report's central prediction: Moore's Law was finally meeting the economics of departmental transaction processing. Multiprocessor Intel 386 systems were appearing. The mainframe's cost-per-transaction advantage was evaporating. The displacement was not a matter of whether but when — and "when" was the early 1990s.

I arrived at DEC knowing the terrain. The DECtp (DEC Transaction Processing) launch was eight months out when I got there. I became, apparently, the Chair of the DECtp Task Force — a title I never actually received in writing, though I later found it attributed to me in historical accounts. What I knew at the time was that I was networking furiously across ten product groups, trying to convince a disparate collection of DEC engineers and marketers that we had a story capable of taking on IBM.

Our hand was stronger than most of the team realized: a multiprocessor VAX 8200, a transaction-friendly version of Rdb, DEC's relational database, and an acquired OLTP transaction monitor. The strategy wrote itself. Combine them, benchmark them against the IBM 3090 mainframe, and expose what I had already privately concluded was the SNA Tax — the hidden overhead buried in IBM's mainframe architecture that was costing enterprise customers millions of dollars they couldn't see.

---

## The Westwood Midnight Ambush

The DECtp marketing launch budget, excluding product R&D, totaled approximately $2 million — a staggering sum for a marketing program in 1988, and not previously disclosed. A significant slice of that went to a "blind" benchmark conducted through a CICS application consulting firm in Westwood, Massachusetts, using the Cullinet mainframe data center. (John Cullinane, from my PHI days years earlier, had built one of the first major commercial software companies. The world of Route 128 was always smaller than it appeared.)

The benchmark was a competitive intelligence operation run under cover. The objective was to measure IBM's highest possible throughput on a 3090 mainframe running DB2 — then compare it head-to-head against a DEC VAX under identical constraints. IBM's own systems analysts were brought in under contract and told in writing that IBM was to provide all reasonable services and tuning to maximize throughput. They knew a benchmark was being run. They had no idea DEC was the client behind the curtain.

> **Sidebar: What Is the Debit-Credit Benchmark?**
>
> The "debit-credit" benchmark was the standard yardstick for OLTP performance in the late 1980s. The test simulated a bank's account transaction processing: a program randomly selects an account, verifies the balance, debits or credits a specified amount, writes an audit record, and confirms the transaction within a strict response-time deadline. The benchmark measures **Transactions Per Second (TPS)** — how many complete debit-credit cycles the system can execute per second while maintaining response times under one second.
>
> The benchmark rules required 100 virtual terminals for every 1 TPS reported. To claim 100 TPS, you had to demonstrate the system could support 10,000 simultaneous virtual users. This was not merely a processing test; it was a systems test of the entire software stack under realistic load.
>
> The debit-credit benchmark had become the "four-minute mile" of enterprise computing — every serious OLTP vendor was obsessed with it, and the score on this single test could define a product's competitive position for years. I had extensive experience from Stratus vs. Tandem.

We used an IBM 3090-400 as the System Under Test and an IBM 3090-200 as the load driver — two of IBM's largest mainframes in the same room, running dedicated tests for hours at night and on weekends. In secret.

What we discovered was devastating to IBM's narrative and priceless to ours: the **SNA Tax**.

SNA — IBM's Systems Network Architecture — was the communications framework that connected IBM 3270 terminals to mainframe applications. Every terminal session required initialization overhead managed by VTAM, IBM's mainframe communications manager. The overhead was not theoretical: it took more than one full 3090 CPU-second just to log in a single 3270 terminal.

The math was punishing:

- 100 TPS target required 10,000 virtual terminals
- 10,000 terminals × 1 CPU-second = 10,000 CPU-seconds of session overhead
- On a four-processor 3090-400: well over an hour of clock time just to establish sessions before processing a single transaction

We also learned that DB2, IBM's flagship relational database, had been tuned almost exclusively for query workloads. Edgar Codd and Christopher Date — the IBM researchers who had invented the relational model — had designed it for the elegant retrieval of data. Transactional throughput was an architectural afterthought.

Richard Case, DEC's head of Competitive Analysis, was ecstatic. He had a color HP graphing plotter, I had the benchmark data, and together we could produce a presentation foil in under two hours showing the stark cost-performance gap between DEC and IBM. The VAX, running a proper OLTP database with a clean transaction architecture, was delivering comparable throughput to an IBM 3090 at a small fraction of the cost.

---

## The Press Event and the Slide That Changed the Room

When I stood before the industry analysts in Boston and the press corps in New York, I had one color slide. Everything else was black and white.

The color slide showed an enormous price difference — millions of dollars — between an IBM 3090-400 and a DEC VAX, with almost no performance difference. That single slide was worth every penny of the $2 million launch budget.

The first reaction in the room was exactly what I had expected and prepared for: "That's a sleazy, cheating way for DEC to act."

I held questions to the end deliberately. The presentation had been built to anticipate that objection and answer it before anyone had to ask. I walked through every step DEC had taken to make the comparison fair: the written instructions to IBM's own analysts, the open invitation to tune DB2 to its maximum, the identical workload running on both platforms, the auditable methodology. When the questions came, the objection had already been answered. The press and analysts accepted it. Sales improved measurably.

In October 1988, IBM rushed out a press announcement claiming DB2 now ran much faster than DEC's measurements. They had, predictably, spent their own nights and weekends closing the gaps we had exposed. The announcement of DB2 Version 2 was an acknowledgment that we had found something real.

> **Sidebar: "Specsmanship" and Why It Had to End**
>
> By 1988, the OLTP benchmark world had degenerated into what the industry called "specsmanship" — a competitive sport in which every vendor designed its own test, optimized every parameter, and published results that bore little resemblance to the performance customers would actually experience.
>
> A vendor could claim 500 TPS by selecting a workload that happened to exercise their architecture's strengths, configuring their system for maximum benchmark throughput rather than production reliability, and excluding overhead costs that would exist in real deployments. The result was a landscape where every vendor won its own benchmark and customers had no trustworthy basis for comparison.
>
> The debit-credit benchmark was widely used but not independently audited. Vendors could and did claim results that later proved unreproducible. The benchmark wars created noise rather than signal.

---

## The Transaction Processing Council

IBM's countermove crystallized what had been a growing conviction. The era of proprietary benchmarks had to end. Independent, audited, industry-standard performance tests were the only path to market credibility that could survive sustained competitive attack.

Omri Serlin, a respected OLTP analyst, had been pushing for exactly this for years. The industry was hesitant — no vendor wanted to step into a ring where they couldn't control the rules. The result was paralysis.

I told Bill Steul I was heading to Los Altos, California. Over dinner with Omri, I listened to his frustrations about the lack of initiative from the major players. There was a long pause.

"Omri," I said, "Digital Equipment would be pleased to be the first member of the Transaction Processing Council. Let's make some phone calls and get the rest off the fence."

That is exactly what happened. A week later, I leaked Digital's leadership position on the council to *MIS Week* (August 8, 1988). The disclosure served a precise purpose: once DEC's commitment was public, every other serious OLTP vendor faced a binary choice — join the standard or explain to customers why they refused to compete on a level field. The fence cleared quickly.

> **Sidebar: The TPC and Its Lasting Impact**
>
> The Transaction Processing Performance Council (TPC) became the authoritative standard-setting body for database and transaction processing performance. Its benchmarks — TPC-A, TPC-B, TPC-C (for order entry workloads), and later TPC-H (for decision support) — required:
>
> - **Full system pricing**: Results had to include hardware, software licenses, and maintenance — not just hardware
> - **Independent audit**: A certified auditor had to verify that the benchmark was run according to specification and that the reported configuration matched the measured system
> - **Public disclosure**: Complete system configuration, pricing, and benchmark methodology had to be published, allowing anyone to reproduce or challenge the results
>
> The TPC transformed the OLTP market. Vendors could no longer claim self-serving results. CIOs had objective, auditable data for procurement decisions. The benchmark became a standard item in every enterprise server RFP for the next decade.
>
> TPC-C, which measured throughput in a complex multi-table order-entry workload, became the definitive benchmark for OLTP server performance through the 1990s and into the 2000s. The results tables were published in trade press quarterly and tracked as closely as stock prices in the server market.

---

## Benchmark Auditor: A New Profession

One of the more unexpected chapters of my early Aberdeen years grew directly from the TPC's founding requirement for independent auditors.

The TPC needed certified third parties to verify benchmark submissions. I realized that my combination of technical depth in OLTP systems and the newly established TPC methodology made me an accredited auditor. The AICPA manual had a brief chapter on performance auditing. The secret was mundane: methodical process and impeccable notes.

I established Aberdeen Transaction Services (ATS) as a practice area. The billing rate was $15,000 for a couple of days of careful documentation work. The client list included Stratus (for TPC-A), Stratus/IBM (for their proprietary RAMP-C benchmark), and Groupe Bull, which required me to audit three models of DPS 7000 and 6000 systems across the United States, Italy, and France.

The European assignments had their characteristic texture. The French and Italian engineers were impressive in their technical tenacity and their frustration when terminal emulators misbehaved at critical moments. The accommodations, however, were world-class: I conducted one audit session while staying at the Trianon Palace Versailles, reviewing the benchmark logs at a desk overlooking the palace gardens while engineers a few blocks over wrestled with communications configurations.

The auditing practice ended with TPC-C, when the council began requiring "certified" auditors who had passed formal examinations and operated under authorized firms. It had been a productive and pleasantly remunerative sideline, but by then Aberdeen's core advisory practice had grown to the point where $15,000 benchmark audits were not the best use of time.

---

## What DEC Taught — And Missed

The DECtp campaign was a success. Jack Smith, DEC's senior marketing executive, would later tell peers that "DECtp was our most important launch after VAX." Sales into OLTP accounts improved. The TPC was founded. The mainframe's cost-performance advantage was documented, quantified, and published.

And yet.

DEC was, at the moment of this victory, a company beginning to lose the war it didn't know it was fighting. The VAX architecture was magnificent — one of the great minicomputer designs ever produced. But the battle we were winning was the minicomputer-versus-mainframe argument. The war that would define the 1990s was x86-versus-everything-else.

The Yankee Group study I had written in 1987 predicted that multiprocessor Intel 386 systems were "appearing on the horizon." By the time DECtp launched in 1988, those systems were already arriving. By 1990, Compaq and others were building servers that would deliver competitive OLTP throughput at a fraction of DEC's VAX pricing.

DEC beat IBM's mainframe pricing in the OLTP argument. Within four years, x86 servers would beat DEC's VAX pricing in the same argument, with the same methodology, using the same TPC benchmarks we had helped create. The irony was almost too neat to be credible.

Ken Olsen, DEC's founder, famously resisted Unix, workstations, and x86 architecture throughout the late 1980s and early 1990s. The company that had shown the industry how to use objective benchmarks to displace the mainframe would itself be displaced by a generation of vendors who used those same benchmarks to displace proprietary minicomputers.

I left DEC for Aberdeen with that observation fully formed. The research firm I was about to help build would spend much of the next decade documenting exactly that transition — the collapse of the proprietary minicomputer era and the rise of the open, standards-based, x86-dominated enterprise infrastructure that replaced it.

The mainframe had not been the last stand, it turned out. It was the second-to-last stand.

---

*Next: Chapter 7 — Founding Aberdeen Group*



---


# Chapter 7: Founding Aberdeen Group
### *(1990–1997)*

---

In late 1989, Chuck Casale called me at DEC with a proposition.

Casale and I had been colleagues at Prime Computer nearly a decade earlier, when he ran Investor Relations through the company's rocket-ship years and watched the stock climb 272 percent in a single year. He had since moved on to the analyst world and, with John Logan — the Harvard MBA who had published my Yankee Group study on transaction processing — had been assembling a team to build a technology research firm from scratch.

"You know the technical side," he said. "Logan knows the financial side. I know how companies tell their stories and raise money. We need all three."

Tom Willmott, from IDC, would cover networking and the remaining white space.

The name had already been market-tested. "Aberdeen Group" scored well on focus-group research: respondents rated it as "highly trusted, top-notch — but I just can't place it." That was exactly right. We wanted a name that sounded like it had always existed. We incorporated in 1988.

---

## The Landscape We Were Entering

The enterprise technology research market in 1990 was dominated by four firms: Gartner Group, International Data Corporation (IDC), Forrester Research, and Yankee Group — collectively known inside the industry as the FIGYs.

> **Sidebar: The FIGY Firms and Their Models**
>
> **Gartner Group** (founded 1979) had built a subscription model targeting CIOs with vendor evaluations and strategic technology guidance. Its Magic Quadrant framework — placing vendors in a two-axis chart of "ability to execute" and "completeness of vision" — became the industry's most recognizable analytical tool. Enterprise software vendors coveted placement in the Leaders quadrant; Gartner's analysts received enormous pressure around quarterly reviews.
>
> **IDC** (founded 1964) dominated market sizing and forecasting with quantitative reports on shipments, revenues, and market share. IDC owned the numbers. If you needed to tell a board that the database market was a $4 billion opportunity, you cited IDC.
>
> **Forrester Research** (founded 1983 by George Colony) carved out territory in business technology strategy, targeting both CIOs and business executives. Forrester's wave reports and research methodology were rigorous and widely read.
>
> **Yankee Group** (founded 1970) focused on telecommunications and networking. In the late 1980s, as networking became enterprise-critical, Yankee was required reading.
>
> All four operated on similar economics: large analyst headcount, expensive multi-year subscriptions, heavy travel for client visits, and annual conference revenue. Aberdeen entered this market in 1990 with a deliberately different approach.

Aberdeen was not attempting to replicate Gartner's vendor evaluation franchise or IDC's market-sizing machinery. We were building something more surgical: deep technical expertise in specific domains, delivered through concise published research that served as lead generation for high-margin advisory projects. The FIGYs sold subscriptions. We sold expertise. Those are different things.

---

## The Partner Structure: Division of the Technology Universe

The founding partnership divided the coverage landscape cleanly. I took system software, application software, and x86 servers. Casale owned scientific and high-performance computing, plus he held a registered financial analyst credential that created capabilities none of the others had. Logan covered minicomputers. Willmott handled networking and everything that didn't fit the other three buckets.

Four domains. Four specialists. One firm.

The specialization created the depth that differentiated us. But the structure that made the firm work was the revenue model — and it was more carefully engineered than most partnerships bother to design.

> **Sidebar: The Cooperative Revenue Architecture**
>
> Aberdeen's revenue-sharing model rewarded four distinct types of contribution:
>
> **Selling**: The partner who originated the relationship and closed the deal received a defined percentage. Business development was hard, relationship-intensive work, and the model explicitly compensated it.
>
> **Project Management**: The partner responsible for delivery received a management allocation. Often the same as the seller; sometimes different, based on technical expertise or geography.
>
> **Final Presentation**: Board-level or executive briefings carried their own allocation. We deliberately structured major deliverables as two-person presentations — the second seat received a cut. This peer-review-in-real-time ensured quality while creating learning opportunities for junior partners and exposing clients to multiple perspectives.
>
> **Project Participation**: Analysts and partners who contributed research, analysis, or content received participation shares. This prevented the firm from becoming a pure rainmaker economy where only sellers prospered.
>
> I called this structure a "cooperative hunter-killer community." Everyone ate. Rainmakers prospered because they captured selling premiums and typically led project management. But analysts and domain experts also built wealth through participation in multiple projects. The structure made hoarding irrational and collaboration economically beneficial.
>
> The alternative — an eat-what-you-kill model where individuals kept most of their revenue — would have destroyed the firm. Research requires review processes, quality control, and knowledge sharing. A purely individualist model produces mediocre work because no one has incentive to improve anyone else's output.

Office overhead, administration, and rent split equally. When a partner hired an analyst, that partner assumed the financial risk. The analyst's salary and allocated overhead became the hiring partner's personal responsibility. The reward for that risk: approximately 35% margin on analyst-generated revenue. If the analyst was productive, the hiring partner captured significant economics beyond their own direct output. If the analyst underperformed, the partner absorbed the loss.

This risk-reward structure ensured that hiring decisions were made carefully, that analysts were trained and deployed aggressively, and that the firm never accumulated unproductive headcount.

---

## My First Hires

My first two analyst hires were Wayne Kernochan and Ed Black, both of whom had worked with my wife. Both proved exceptional.

Kernochan brought deep expertise in database systems and data management — the kind of technical depth that meant he could look at a query optimizer's behavior and identify lock-escalation patterns that would cause performance degradation at scale. Black covered enterprise applications and business intelligence. Together, they became the cornerstone of my practice's expansion.

The profile we hired for was specific and deliberate: former vendor engineers, enterprise architects, systems designers — people who had built and broken things, not just observed and documented them. The ideal Aberdeen analyst could hold a technical conversation with a chief architect, review code, assess a performance benchmark critically, and spot architectural flaws in product designs. But ex-reporters also turned into valuable analysts.

Base salaries ran $52,000 for mid-level analysts in the early 1990s. Each analyst carried a margin quota of approximately $350,000 annually. Hit the quota and you qualified for a 30% bonus on overage, uncapped on the upside. Exceptional analysts could earn $250,000 to $350,000 in total compensation. Most described it as their best job ever.

---

## The Publishing Strategy: Give Away the Analysis, Sell the Judgment

Aberdeen's go-to-market strategy differed fundamentally from the FIGY firms' subscription models. We published research freely and used it as lead generation for advisory services.

Each report addressed a specific technology decision: *Should you deploy Windows NT or Unix for database servers? Which data warehouse architecture fits your requirements? How do Oracle, Sybase, and Informix compare for OLTP performance?*

We distributed reports through direct mail, conference presentations, technology vendor sponsorships (disclosed), and — crucially — one of the first research Internat websites with free downloads. At peak, Aberdeen's website ranked in the top 10 globally, per Alexa Internet. Yes, Aberdeen sat in daily hits where Google, Facebook, and Instagram sit today.

> **Sidebar: Why Free Research Was Heresy in 1990**
>
> In 1990, research firms universally treated published reports as products to sell, not marketing investments. Gartner's research was behind a subscription paywall. Forrester's documents were licensed content. The business model assumption was that research had intrinsic value that required payment to access.
>
> Aberdeen bet on the opposite assumption: in a world where information increasingly wants to be free, expertise and judgment are what clients will pay premium prices for. Give away the analysis. Sell the custom advice.
>
> This model anticipated content marketing by 15 years. It was deeply contrarian in 1990. By the mid-2000s it had become conventional wisdom.
>
> The web distribution strategy proved transformative. By 1995, Aberdeen's website was generating thousands of research downloads weekly. Each download captured an email address and company name, building a database of qualified prospects. Our inside sales team could call companies that had downloaded multiple reports on related topics, knowing they were actively evaluating relevant technology decisions. This was primitive by modern marketing automation standards — but in the mid-1990s it was sophisticated lead-generation machinery that none of our competitors had built.

The economics of the model were compelling. Publishing research cost primarily analyst time. Distribution costs were minimal. Advisory engagements, by contrast, carried 60-70% margins. A single $200,000 advisory project funded substantial research publication. Clients who read three Aberdeen reports before engaging for advisory work were qualified, educated buyers who understood our analytical style and trusted our technical depth. The advisory sale was easier because we had already proven value.

---

## My Coverage Domains: Six Frameworks

Within my domain of system software, application software, and x86 servers, six analytical themes shaped the research and defined Aberdeen's perspective through the 1990s.

**The Inevitability of Open Architecture.** Proprietary platforms were economically doomed. The cost advantages of standardized components manufactured at volume were overwhelming. This thesis was controversial in 1990 and obvious by 2000. The strategic implication: enterprises should minimize dependence on proprietary platforms and architect for platform replaceability. The lock-in that vendors sold as integration was a liability masquerading as a feature. We hired a Linux analyst as soon as Red Hat took off.

**Client-Server as Permanent Architectural Principle.** Client-server was not a temporary fad. Separating presentation from business logic from data management was correct system design. The specific technologies would change — terminals to PCs to browsers to mobile — but the logical separation would persist. We argued this when client-server was still being debated and before anyone had coined the term "microservices." The architecture anticipated what it would become.

**RDBMS as Universal Middleware.** Relational databases had won the data management battle. Hierarchical and network databases would remain niche. The combination of mathematical foundation, SQL flexibility, and ACID transaction guarantees made the relational model the universal standard for operational systems. My personal mission from 1985 to 1995 was championing the RDBMS that could handle both transactions *and* query/reporting — the killer combination that IT departments desperately needed and vendors were slow to fully deliver.

**Data as Competitive Advantage.** Data was becoming a strategic asset, not merely an operational record. Enterprises that could analyze customer behavior, market trends, and operational patterns faster than competitors had sustainable advantages. This thesis was ahead of its time in the early 1990s. The concepts of "big data" in the 2000s and AI/ML in the 2010s are extensions of exactly this insight: competitive advantage flows from better use of data. We built a data warehousing practice around this conviction before most enterprises knew what a data warehouse was. I have a slide circa 1991 of today's AI-driven analysis model.

**Integration Problem Acceleration.** As client-server architecture proliferated, integration complexity exploded. Every application had its own data format and API — if it had one at all. Point-to-point integration created N-squared complexity. The pattern was consistent and predictable: architectural proliferation creates integration pain, which creates demand for integration platforms, which creates new standards, which enables further proliferation. The enterprises that planned for integration from the start had manageable complexity. Those that treated it as an afterthought built technical debt that haunted them for decades.
**Spoke-Node-Ring** is a road map for integrating heterogeneous computer systems into an information network, yet it is also a business planning tool to overcome *integration problem acceleration*. At the heart are systems-of-record. Next layer out are *middle manager rings* where organizational productivity applications run, connected by peer-peer networks. *Productivity Nodes* access the middle ring, typically on a LAN in a department or distributed office. S-N-R is a Lego for building systems architectures which Aberdeen championed in the early 1990s.

---

## What Aberdeen Got Right — and What We Missed

Looking back from three decades later, Aberdeen's research had genuine prescience in several areas:

**Open Systems Transition** — We correctly called that proprietary platforms were doomed and that open architecture would dominate. The specific trajectory (Unix to Linux, RISC to x86, proprietary to commodity) played out largely as we described.

**Client-Server Persistence** — The architectural principle of separating presentation, logic, and data persisted even as implementation technologies changed completely. Web applications, mobile apps, and cloud services all follow client-server patterns with different technology stacks.

**RDBMS Dominance** — Relational databases remained dominant for operational systems through the 2010s. NoSQL databases carved out specific use cases but never displaced relational systems for enterprise applications.

**Data Warehousing Democratization** — Every significant enterprise eventually built data warehouses. The technologies evolved from Teradata to columnar stores to cloud warehouses, but the architectural pattern persisted exactly as we had argued.

**Integration as First-Class Problem** — Integration complexity did accelerate as predicted, driving massive investment in middleware, EAI, SOA, and eventually API management platforms. Clients who read our early research on this and acted on it avoided enormous technical debt.

Where our timing was less precise:

**Object Databases** — We underestimated how completely relational databases would dominate. Object databases captured negligible market share despite their theoretical elegance. The impedance mismatch between object-oriented programming and relational storage persisted, but enterprises chose object-relational mapping tools rather than native object databases. I never liked C++, but I underestimated how much the industry would tolerate the ORM solution rather than abandon SQL.

**Unix Fragmentation** — We expected Unix standardization to succeed more cleanly. Instead, Linux emerged as the dominant variant by winning on open licensing and community development, not technical standardization. The destination was right; the mechanism was different. Unix remained fragmented and different in every vendor's implementation.

**Web Application Speed** — We understood that browsers would become important clients but underestimated the speed at which the web transformed from document distribution to full application platform. The web moved faster than anyone predicted in the early 1990s, and we were slower than we should have been to recognize the depth of that shift. We were also off in touting thin-client hardware as the market chose client-server where the browser became ever-heavier and complex.

---

## The 1997 Inflection: Venture Capital

By 1997, Aberdeen had established strong profitability and market presence — $7 million in annual revenue with approximately 40% EBITDA margins (to partners, not the corporation). The partnership model was working. The cooperative revenue structure had prevented fragmentation. The analyst hiring strategy had built deep expertise across the coverage domains.

Then the venture capital world discovered the analyst market.

Multiple VCs approached Aberdeen with growth capital offers. The pitch was consistent: the internet was driving explosive demand for technology research; Aberdeen's publishing platform and analyst talent could scale dramatically with capital. We could build a direct sales force, expand analyst headcount, enter new coverage areas, and challenge Gartner and Forrester directly.

The partner group faced a fundamental choice. We could remain a profitable partnership, continuing the model that had worked for seven years. Or we could take institutional capital, pursue aggressive growth, and transform into a different kind of company.

The economic arguments for growth were attractive but not compelling. The research market was expanding rapidly. The established firms were trading at high revenue multiples. A successful exit — IPO or strategic acquisition — could generate wealth beyond what the partnership model would produce.

The arguments against centered on culture and control. Venture capital meant governance changes, growth imperatives, and pressure to build revenue ahead of profitability. The cooperative partnership model that had created our culture and quality standards would be difficult to maintain at larger scale with institutional investors expecting quarterly performance improvements.

The decision to pursue venture capital was accomplished in a 45 minute meeting of Kastner, Logan, and Wilmott. We chose growth. The VC idea was Wilmott's. My calculus was Wilmott would leave if we did not follow his plan, and I would be saddled with his overhead and people. A roll of the dice had less immediate downside.

That choice marked the end of Aberdeen as a partnership and the beginning of Aberdeen as a venture-backed research company. The model that had defined the first seven years — the domain specialization, the cooperative revenue structure, the risk-reward hiring model, the publishing-as-marketing strategy — provided the foundation. What the firm would become after 1997 is a different story, with different dynamics and different outcomes.

---

## What the Partnership Proved

The Aberdeen partnership model from 1990 to 1997 validated principles that remain relevant for anyone building specialized research or advisory firms in emerging technology markets.

**Specialization scales better than generalization.** Deep domain expertise created more defensible value than broad market coverage. Clients paid premium rates for analysts who truly understood the technical details of their specific problem.

**Cooperative economics prevent fragmentation.** The multi-layer revenue sharing model was complex to administer but essential for maintaining firm cohesion. Partners had strong incentives to collaborate rather than compete internally.

**Risk-reward on hiring aligns incentives.** Making hiring partners responsible for analyst productivity ensured careful decisions and effective deployment. The 35% margin reward made the risk worthwhile.

**Publishing generates better leads than cold calling.** Free research distribution built trust and demonstrated expertise before the sales conversation. Prospects who had consumed our research were easier to close and more satisfied clients.

**Technical credibility opens different doors.** Analyst depth in technical domains created opportunities with engineering organizations and technical executives that market analysis alone couldn't access. Our analysts could often install and configure the products they covered. That was unusual and valuable.

**Culture formation happens early and persists.** The cooperative, technically deep, publishing-centric culture established in the first few years shaped Aberdeen's identity even as the firm scaled and changed ownership. The soul of the institution was set in the partnership era.

**Finally:** each of the partners could have done fine in a solo practice. However, with the Aberdeen Group structure, we could charge more, be trusted more, and accomplish more — individually and collectively — than any of us could have done alone. The whole was genuinely greater than the sum of its parts.

That is the hardest thing to build and the easiest thing to destroy.

---

*Next: Chapter 8 — The Go-Go Years: Aberdeen at Scale, 1998–2006*



---



---


# Chapter 8: The Go-Go Years — Aberdeen at Scale
### *(1998–2008)*

---

By late 1998, Aberdeen Group crossed the threshold from partnership into something else entirely.

The venture capital was in. The growth mandate was on. The question was no longer "how do we build a sustainable, profitable research firm?" It was "how fast can we scale, and what does the exit look like?"

Both questions had good answers. The years between 1998 and the October 2006 acquisition by Harte-Hanks were the most professionally expansive and financially consequential of my career. They were also, at times, the most personally exhausting. We built something substantial. We navigated a market catastrophe. We sold at almost the last possible moment before a second catastrophe would have prevented the sale entirely.

---

## The Transformation: From Partnership to Corporation

The venture capital infusion was visible immediately. Office space expanded. Analyst recruiting accelerated. A subscription revenue model was built alongside the advisory practice. The partnership's cooperative revenue-sharing structure — the multi-layered system that had kept us aligned and collaborative for seven years — morphed to market-rate salaries and conventional bonus plans. This was not a failure of design; it was a necessity of scale. You cannot administer complex revenue splits across 100 analysts. You can across 12.

The analyst headcount tells the story cleanly:

- **1997**: ~30 analysts (partnership model)
- **2000**: ~120 analysts (peak of internet boom)
- **2001**: ~150 analysts (maximum scale, just before the crash)
- **2003**: ~40 analysts (post-crash consolidation)
- **2006**: ~19 analysts (recovered, positioned for exit)

Revenue and net profit tracked the same arc, and the audited numbers — courtesy of Ernst & Young through 2002 and BDO Seidman from 2006 — tell a story that is both more dramatic and more honest than the round-number estimates that circulate in industry lore:

| Year | Revenue | Net Profit/(Loss) |
|------|--------:|------------------:|
| 1997 | $7,218,357 | ($132,090) |
| 1998 | $9,353,282 | ($551,712) |
| 1999 | $14,103,430 | $732,472 |
| 2000 | $20,691,445 | $6,140 |
| 2001 | $14,900,607 | ($3,233,819) |
| 2002 | $9,380,528 | ($1,340,556) |
| 2003 | $6,468,691 | ($3,064,707) |
| 2004 | $5,107,002 | ($2,017,318) |
| 2005 | $8,652,215 | $868,498 |
| 2006 (Jan–Aug) | $10,828,756 | $3,971,626 |

*Sources: Ernst & Young (fiscal years 2002–2003); BDO Seidman (2004–2006)*

A few observations on what those numbers actually show.

The peak year was 2000 at $20.7 million in revenue. The partnership era numbers (1997: $7.2M) confirm that the venture capital story was real: revenue grew nearly three-fold from 1997 to 2000. The crash was equally real: from $20.7M in 2000, revenue fell to $5.1M in 2004 — a 75 percent decline over four years. The accumulated net losses from 2001 through 2004 totaled more than $9.6 million.

The recovery was genuine and rapid. Revenue more than doubled from 2004 to 2005 ($5.1M to $8.7M), and the first eight months of 2006 produced $10.8M in revenue at a net profit margin of nearly 37 percent. That profitability profile is what made the acquisition attractive.

The expansion into new coverage domains was real and necessary. Supply chain management. Customer relationship management. Human capital management. Vertical industry analysis in financial services, telecommunications, retail, manufacturing, and healthcare. Aberdeen at scale could cover problems that Aberdeen as a four-partner firm could not.

My own role shifted in the familiar direction: less direct client delivery, more research strategy, analyst development, and competitive positioning of the firm's capabilities. From 2003 to 2006, the Board asked me to step aside while Jamie Bedard created a new business model. I kept Intel as a retainer, and returned in 2006 to drive SOA research. The transition from practitioner to leader — and back again — is a standard arc in professional services. That doesn't make it comfortable either time.

---

## Enhanced Research Practices

Scale enabled methodological investments the partnership could never have funded.

**Benchmark Research Programs.** We developed systematic survey approaches reaching hundreds of enterprises on technology adoption patterns, deployment challenges, and satisfaction metrics. These benchmarks gave clients empirical grounding — not just what we thought they should do, but what their peers were actually doing, with statistical confidence. Aberdeen's benchmark reports became a signature product. CIOs used them to justify budget decisions. Vendors quoted them in sales materials and challenged our assumptions vigorously when the numbers didn't favor them. Either reaction was a sign of credibility.

**Best Practices Frameworks.** When a client's data warehouse deployment succeeded, we captured the architectural decisions, organizational structures, vendor selections, and project management approaches that contributed to success. These became reusable frameworks. This was knowledge management before that term became fashionable — systematic capture and reuse of insights across a larger analyst population that the partnership's informal knowledge-sharing couldn't replicate.

**Total Cost of Ownership Models.** TCO calculators for major technology categories became Aberdeen's most commercially potent tool. A well-built TCO model incorporated hardware, software licensing, implementation services, ongoing maintenance, staff training, and operational overhead over three-to-five year horizons. Clients could model different vendor and architecture choices with realistic projections.

TCO analysis was analytically honest work. The models favored whoever had the most efficient architecture and realistic licensing terms — which changed by category and customer context. Vendors who fared poorly in our models challenged our assumptions. Vendors who fared well quoted us in their sales decks. Both behaviors proved the models were landing.

> **Sidebar: How TCO Modeling Changed Vendor Conversations**
>
> Before rigorous TCO models were available, enterprise technology procurement was dominated by upfront hardware and software pricing. Sales teams competed on sticker price. The CIO who paid $2 million for Platform A rather than $3 million for Platform B appeared to have made the smart decision.
>
> TCO analysis revealed what the sticker price concealed. A platform that cost $1 million less to license might cost $3 million more to implement, $2 million more to staff, and $1.5 million more to maintain over five years. The "cheaper" option was more expensive by $5.5 million — but that arithmetic was invisible in a conventional procurement process.
>
> For enterprises, TCO analysis created a defensible methodology for choosing on five-year economics rather than initial price. For Aberdeen, it positioned our advisory work as quantitatively rigorous rather than qualitatively opinionated. Anyone can have a vendor preference. Very few people can build a credible model showing why.
>
> The limitation: TCO models are only as good as their assumptions. We were rigorous about documenting those assumptions and aggressive about making them visible. Vendors who disagreed with a TCO outcome usually disagreed with a specific assumption — and those conversations about assumptions were often more valuable to clients than the final number.

---

## The Internet Bubble: We Knew It, and It Didn't Help

Aberdeen's expansion from 1998 to 2001 coincided with the peak of the internet bubble. Technology spending had disconnected from economic reality. Enterprises invested in e-commerce infrastructure, web platforms, and integration technology with optimistic ROI assumptions that couldn't survive scrutiny. Every internet startup and every enterprise digital initiative needed analyst validation. Research market demand was irrational in the best possible direction for us.

We knew it was unsustainable. The analyst team made dark jokes about which internet business models would survive and which were burning venture capital on pure fiction. Several clients were clearly in the latter category. We told them so when asked directly. Not everyone asked.

Knowing a bubble exists doesn't mean you can time its deflation.

The NASDAQ peaked in March 2000. Revenue peaked the same year at $20.7 million — and then fell off a cliff. By 2001 revenue had dropped to $14.9 million, with a $3.2 million net loss. By 2002, hurt by the 9/11 attack aftermath, it was $9.4 million. By 2004, the trough year, Aberdeen generated just $5.1 million in revenue against a $2 million net loss — a quarter of peak revenue, with accumulated losses piling up.

We cut analyst headcount from approximately 150 in 2001 to roughly 40 by 2003. These were real people — colleagues who had built the firm through the growth years. The decisions were painful and unavoidable.

The downturn clarified what created durable value. Benchmark research based on survey data became less useful when response rates collapsed — companies in survival mode don't have time for analyst surveys. Deep technical advisory work held up but there were fewer analysts
. Enterprises still needed to solve complex integration, architecture, and vendor selection problems even with constrained budgets. The hard problems don't pause for recessions.

Aberdeen survived better than many competitors because we had maintained profitability through the growth years rather than burning cash to acquire market share. Our balance sheet could absorb revenue decline without existential crisis. Smaller research firms were acquired or shut down. We emerged from the downturn with less competition and a more realistic assessment of sustainable scale.

---

## The Predictions That Defined the Era

Throughout the go-go years I continued publishing analytical frameworks. Several proved directionally correct, with timing caveats.

**SOA as the Next Platform Transition.** By 2000 I was arguing that service-oriented architecture represented the decade's defining architectural shift, comparable to client-server in the 1990s. Applications would decompose into loosely coupled services communicating via standard protocols. The thesis was correct. The timeline was optimistic. The standards (SOAP, WSDL, UDDI) were immature. Organizational discipline to design and govern service interfaces effectively didn't exist yet in most enterprises.

By 2004–2005, SOA had reached peak hype. IBM, Oracle, BEA, Microsoft, and SAP were promoting SOA platforms with full-page trade press campaigns. Many enterprise SOA initiatives delivered disappointing results. By 2008–2010, REST APIs and lightweight service approaches were displacing heavyweight SOAP-based SOA. The architectural principles — loose coupling, service interfaces, message-based integration — were sound. The implementation technology evolved toward simpler forms of the same principles. That is a successful prediction with an imprecise timestamp.

**Open Source Enterprise Adoption.** I predicted early in the 2000s that open source would move from internet infrastructure (Linux, Apache, MySQL) into enterprise applications and middleware. The economic advantages were compelling: no license fees, transparent code for security audit, community-driven innovation. The adoption played out exactly as predicted across 2000–2006, with JBoss, MySQL, PostgreSQL, and eventually full LAMP stacks penetrating enterprise infrastructure.

The resistance was less from technical concerns than from procurement processes. Enterprise IT organizations were accustomed to paying vendors for software and support contracts. Open source required buying support separately, creating procurement complexity. My prediction was correct on trajectory; adoption took most of the decade rather than the 2–3 years I initially projected.

**Data Integration as Perpetual Tax.** I argued consistently that integration complexity would accelerate despite improved integration technologies. Each new application, each acquired company, each data source added to the integration burden. N-squared complexity is a mathematical property, not a solvable engineering problem.

This proved completely accurate. The integration technology market exploded across 2000–2006 with EAI platforms, ETL tools, data quality software, master data management systems, and SOA infrastructure. Despite better tools, integration remained expensive because application proliferation outpaced integration technology improvement. The framing — "data integration as perpetual tax" — resonated with clients experiencing this pain directly. It remains accurate in 2026.

**Consumerization of IT.** By 2004–2005 I was predicting that consumer technology would increasingly influence enterprise IT. Employees accustomed to Google's search elegance, Amazon's e-commerce simplicity, and consumer web application usability would demand similar experiences from enterprise systems. This would challenge traditional enterprise software vendors designed for trained power users, not casual end users.

The thesis explained the rise of Salesforce.com — which offered consumer-grade interfaces and eliminated complex installation — and predicted the coming mobile revolution. Smartphones were still BlackBerry keyboards in 2005, not iPhone touchscreens, but the direction was visible. By 2007–2008, consumerization of IT had become mainstream discussion in CIO circles. Aberdeen's early positioning on this trend provided credibility in advising enterprises on how to respond.

---

## The CEO Transition: Jamie Bedard

Tom Willmott had been effective as the firm's operational leader through the partnership era and early growth phase. By 2003, scaling to 150 employees, managing venture board expectations, and navigating the post-bubble downturn required different capabilities.

Jamie Bedard became Aberdeen's CEO in mid 2002. His leadership priorities were operational excellence, research productization, sales force professionalization, and financial discipline — exactly what the scaled organization needed. The Board asked me to step aside from 2003 to 2006 while Bedard restructured the business model. I returned in 2006 focused on SOA research, contributing to the revenue and profitability recovery visible in the 2005–2006 financials.

Bedard's style was more corporate and less collegial than the partnership era. This created friction with analysts who missed the informal partnership dynamics. It also created stability and predictability the scaled organization genuinely required. My relationship with Bedard was professional and productive. He respected the technical research practice. I provided input on research strategy and major client engagements while Bedard focused on operational management and board relations. The division worked.

> **Sidebar: What "Professional CEO" Transition Really Means**
>
> Every founder-led company that takes institutional capital faces a version of this conversation: the founders who built the culture and the business may not be the right people to scale it. This is not a criticism; it is an observation about different skill sets.
>
> Aberdeen's founding partners were exceptional at research, client advisory, domain expertise, and the cooperative relationship management that held a partnership together. Those are not the same skills as managing a 150-person organization through a market downturn, reporting to venture investors with quarterly performance expectations, and building a sales force with rigorous pipeline discipline.
>
> The Bedard transition was handled professionally by the standards of the industry. Willmott remained involved in a strategic advisory capacity. The founding partners maintained significant equity and leadership roles. The cultural friction was real but manageable.
>
> The inevitable tradeoff: institutional professionalism creates discipline and scalability at the cost of the informal energy, personal accountability, and cultural distinctiveness that define early-stage firms. You cannot have both at scale. Every company that succeeds eventually pays this price.

---

## The Harte-Hanks Acquisition

Aberdeen's sale process was an auction, which I think boosted interest and participation. Harte-Hanks, a marketing services and customer relationship management company, approached Aberdeen in early 2006 to participate. 

Their stated thesis: Aberdeen's research capabilities could enhance Harte-Hanks consulting services, and Harte-Hanks' sales force could expand Aberdeen's customer base. Harte-Hanks also owned a database of 4,500 US IT decision-makers that would complement Aberdeen's research distribution with buyer decisions.

The strategic logic was debatable. Aberdeen served CIOs, infrastructure architects, and development managers. Harte-Hanks served CMOs and marketing directors. The customer segments overlapped minimally. Aberdeen's technical research on databases, middleware, and integration architecture had little obvious synergy with Harte-Hanks' direct marketing and customer data services. The business cases were more adjacent than complementary.

But Harte-Hanks was willing to pay a substantial premium. The deal was a multi-tier auction, and they wanted to win. The Aberdeen stakeholders — founders, venture investors, and management — were ready to monetize after sixteen years. Financial logic trumped strategic skepticism.

The acquisition closed in October 2006 at a valuation of $42 million.

A year later, the financial crisis erupted and M&A markets froze. The transaction would not have happened at that valuation — or perhaps at any valuation — had negotiations been twelve months later. Timing is the most important variable in exit transactions, and most of it is luck. We were extraordinarily lucky.

The integration proceeded predictably for an acquisition with weak strategic logic:

- **Cross-selling mandates** attempting to sell Aberdeen research to Harte-Hanks' marketing clients, and vice versa — a mismatch the customer segments never accepted
- **Content marketing pivot** — Harte-Hanks wanted Aberdeen research repurposed as lead generation content for their consulting services, shifting output from independent analysis toward marketing-oriented content
- **Analyst retention challenges** — key analysts departed as Aberdeen's culture changed under new ownership
- **Brand dilution** — by 2010–2012, almost all of Aberdeen's published output was vendor-sponsored survey-based reports, essentially content marketing rather than independent research

I departed in mid 2007 after completing nine SOA studies in nine months. After 18 years building and leading the research practice, the Aberdeen I had co-founded no longer existed in any meaningful sense. The brand persisted. The substance had been absorbed into a different kind of company with different priorities. Today, Aberdeen is part of Ziff-Davis.

---

## What the Go-Go Years Proved

Looking back from nearly two decades, the Aberdeen arc from 1998 to 2006 confirmed several patterns about research firms, market cycles, and institutional growth that apply far beyond the technology research industry.

**Scale enables capabilities but dilutes culture.** The firm could conduct benchmark research, build sophisticated TCO models, and cover more domains at 150 analysts than at 30. The intimate collaboration and technical depth of the partnership era were harder to maintain at scale. The cooperative revenue-sharing model couldn't survive the transition to corporate compensation structures. You gain resources and reach. You pay in cultural distinctiveness.

**Growth capital changes the objective function.** Venture investment enabled expansion but created pressure for revenue growth and eventual exit. The sustainable profitability mindset of the partnership gave way to growth-oriented thinking that culminated in acquisition. The partners and investors made substantial returns. That was not wrong. But it changed what the firm optimized for, which changed what the firm was.

**Market cycles are brutal and non-negotiable.** The 2000–2004 downturn tested every assumption about sustainable growth. Revenue fell 75 percent from peak; accumulated losses exceeded $9.6 million over four years. Firms that had overextended failed. Aberdeen survived — with scars that informed subsequent strategy and a lasting humility about predicting technology adoption timelines.

**Technical depth remains differentiating.** Even as Aberdeen scaled and broadened, the engagements that created the most value were technically deep architecture and implementation advisory projects. Market sizing and trend analysis were commoditizing. Technical problem-solving for complex integration, performance, and architecture challenges retained premium pricing throughout every market cycle.

**Exit timing is mostly luck.** We closed in October 2006 at $42 million. The financial crisis arrived in 2007. Skilled negotiation and careful preparation set up the transaction. Fortune closed it.

The Aberdeen that existed from 1990 to 1997 as a partnership was more culturally distinctive and professionally interesting than the Aberdeen that existed from 1998 to 2006 as a scaled, venture-backed research company. The scaled Aberdeen created far more wealth. These tensions are fundamental to every entrepreneurial venture. There is no obviously correct answer about which path is preferable — only an honest accounting of what each path costs and what it delivers.

We built something significant. We navigated brutal cycles. We maintained technical credibility longer than most firms in our position. And we sold at the last possible moment before the crisis that would have made the sale impossible.

That is a good story, even when told honestly.

---

*Next: Chapter 9 — Expert Witness: Technology on Trial*



---


# Chapter 9: Expert Witness — Technology on Trial
### *(1992–2015)*

---

At some point in the early Aberdeen years, I received a phone call from a law firm I had never heard of.

They were looking for an expert witness in a complex commercial litigation involving enterprise database technology. The case required someone who understood relational databases at both the architectural and market level — not just what the technology did, but what it was worth, what it should have cost, and whether the claims being made about it in a contract dispute were technically credible.

I said yes. That decision opened a parallel career that would run alongside the Aberdeen research practice for more than two decades.

---

## What an Expert Witness Actually Does

Expert witness work is poorly understood outside the legal profession, and worth explaining before the cases themselves.

In American commercial litigation, parties to a dispute can retain qualified experts to provide two types of assistance: *consulting expert* work (confidential analysis and strategy advice to the attorneys, not disclosed to the opposing side) and *testifying expert* work (formal opinions presented in written reports, subjected to deposition, and potentially introduced as trial testimony). The distinction matters enormously. A consulting expert can be completely candid about weaknesses in a client's position — that's the job. A testifying expert must be prepared to defend every opinion under rigorous cross-examination, which means the analysis must be bulletproof.

The career path into expert witness work in technology cases ran through a small number of routes in the 1990s: former senior engineers with direct technical experience, former CIOs who had made major technology purchasing decisions, and — increasingly — technology analysts whose research credentials gave them recognized expertise in market standards and industry practice. Aberdeen's published research and my TPC work gave me credentials that courts found credible. I was an analyst, not an engineer, which turned out to be an advantage in many cases: I could speak to what the industry knew, what the market expected, and what competent technology practice looked like — the standards by which a disputed technology decision would be judged.

Over twenty-plus years I worked on a variety of cases. The subject matter ranged from database licensing disputes to software project failures to antitrust claims in the storage market. Several stand out for their complexity, their stakes, or what they taught.

---

## The Safeway Data Warehouse Case

The most significant litigation engagement of my expert witness career was a major antitrust and breach-of-contract dispute involving Safeway, one of the largest supermarket chains in North America, and a technology vendor. The dispute centered on data warehousing technology: what had been promised, what had been delivered, whether the competitive market analysis that had informed the deal was sound, and what damages were appropriate if it was not. i was second-seat to novice expert Hugh Bishop.

> **Sidebar: Data Warehousing as Legal Battleground**
>
> By the mid-1990s, data warehouses had become strategic infrastructure for large retailers. A properly designed warehouse could consolidate sales data from thousands of point-of-sale terminals, combine it with supplier and inventory data, and produce analytical reports enabling decisions about product placement, promotional pricing, and inventory management.
>
> For a chain the size of Safeway, the competitive implications were significant. Better analytical capability could translate directly into better purchasing negotiations, more effective promotions, and reduced inventory costs — all of which affected margins in a notoriously thin-margin business.
>
> When a data warehouse project failed or underperformed, the damages were calculable — but only with expert analysis that could quantify what a properly functioning system would have enabled versus what the failed system actually delivered. This required someone who understood both the technical architecture of data warehouses and the economics of the retail market they were intended to serve.

Our role in the Safeway engagement was as a damages expert. This required building an analytical model that could credibly answer: what was the market value of the technology that was contracted for, how did it differ from what was delivered, and what was the economic consequence of that gap? In this case, Safeway's Teradata data warehouse machine was effectively destroyed when the fire extinguishing system exploded into the closed computer room.

The work was technically demanding and methodologically rigorous. We drew directly on Aberdeen's research frameworks — the competitive landscape analysis, the TCO models, the performance benchmarking methodology — and applied them to the specific facts of the dispute. The research practice and the litigation practice were not separate disciplines; they used the same analytical tools in different contexts.

The Safeway engagement ran over three years, involved dozens of depositions, and produced hundreds of pages of expert reports. The technical and economic analysis was eventually admitted into evidence. 

The settlement terms were confidential. What I can say is that the case established the market value of enterprise data warehousing capabilities in terms that courts could understand and apply — which is the fundamental contribution of expert testimony in technology disputes.

---

## The Anatomy of a Software Project Failure

A different category of engagement involved post-mortem analysis of failed software projects. These cases were almost always disputes between an enterprise client who had paid a vendor to build or implement a system and a vendor who claimed the system had been delivered per specification.

The forensic methodology I had developed at ADL — the habit of keeping detailed records, the instinct for spotting scope creep and governance failures, the ability to read a project log the way a doctor reads a chart — proved directly applicable to expert witness work.

The pattern in failed IT projects was remarkably consistent across industries and decades:

**Scope was never locked.** The initial contract described a system at a level of abstraction that both parties could agree to, but left implementation details undefined. As development proceeded, the client's understanding of "what the system should do" diverged from the vendor's understanding of "what we contracted to deliver." Neither party was necessarily acting in bad faith; they were operating from different mental models of the same document.

**Requirements changed faster than the contract could accommodate.** Business environments change. A healthcare system under development in 2001 faced a different regulatory environment by 2003. An enterprise resource planning implementation that started in 1999 encountered the Y2K remediation priority in late 1998. Change orders were the legal mechanism for handling requirement changes, but change order negotiations consumed enormous energy and introduced adversarial dynamics into what should have been a collaborative relationship.

**Integration was underspecified.** The system being built almost always had to connect to existing systems that the new system's contract never adequately described. The data formats, transaction volumes, error handling requirements, and performance expectations of those integrations were discovered during implementation, not defined upfront. Integration scope became the site of the most damaging disputes.

**Testing was inadequate.** User acceptance testing was frequently rushed to meet contractual go-live dates. Defects that would have been caught in proper testing were discovered in production, where they were far more expensive to remediate and where they had already caused operational damage.

> **Sidebar: Why IT Projects Fail at Such Consistent Rates**
>
> The Standish Group has been tracking IT project outcomes since 1994. Their CHAOS Report findings have been remarkably consistent over three decades: roughly 30% of IT projects succeed as defined (delivered on time, on budget, with required features), 50% succeed partially (significant cost overruns, delays, or reduced scope), and 20% fail completely.
>
> These rates have improved modestly with agile methodologies, cloud deployment, and SaaS platforms, but the fundamental challenge persists: complex software development involves translating imprecise human requirements into precise machine instructions, under conditions of technical uncertainty, changing business environments, and organizational politics.
>
> Expert witnesses in software project disputes frequently find that the technical failure was real but not the root cause. The root cause was usually a governance failure: inadequate requirements definition, insufficient change management, misaligned incentives between client and vendor, or executive pressure that overrode technical judgment at critical decision points.
>
> In twenty years of expert witness work on software project failures, I encountered genuine technical incompetence perhaps five times. I encountered governance and organizational failures in every single case.

My expert reports in software project failures typically addressed three questions:

1. **What did the contract actually require?** This required careful reading of the contract documents, change orders, requirements specifications, and the contemporaneous communications between parties during negotiation. Contracts are frequently ambiguous; the question is what an objective, reasonable reader would understand the contract to mean given industry standards and practices.

2. **What was actually delivered?** This required technical assessment of the system as built: what functions it performed, where it failed to perform specified functions, and how the observed deficiencies compared to the contracted specification.

3. **What were the consequences?** Damages in failed IT projects typically include: the cost of the work paid for but not received; the cost of remediation; operational losses during the period when the system underperformed; and, in some cases, competitive disadvantage if the system failure affected market position.

The third question was the most analytically demanding and the one where Aberdeen's market research background was most directly valuable. Quantifying the competitive consequences of a technology failure required understanding what properly functioning technology would have enabled — which was exactly the kind of comparative analysis our research practice had performed for advisory clients.

---

## The Florida Welfare Bid
This is an incomplete account that I need to flesh out with more factual data to document the case in the state archives. The gist is EDS and IBM bid on a massive $200 million human services statewide client services application. The Request for Proposal (RFP) required specific terminal response times on average. Unisys, a losing bidder, contacted me to serve as an expert witness in proving a three-tier IBM mainframe system could not meet the RFP specifications. IBM delivered a box of computer paper with 525 performance simulation runs and nothing. I found the needle in the haystack, testified that IBM's own performance estimator said this system would have 20-30 second average response times. The protest lost and I went back to my day to day. What I have recently uncovered while preparing these memoirs is that: several state officials were indicted over the bid; the system was built at a $200 million cost; it failed acceptance tests with 20-30 second response times. Congress, which put up most of the lost millions, was very unhappy, held hearings, and passed two laws that prevent unfettered contracts like Florida's. I was vindicated.

---

## What the Courtroom Taught About Technology Markets

Expert witness work provided an unusual vantage point on technology markets. Most market participants — vendors, buyers, investors, analysts — experience markets through transactions that succeed. The work goes forward, the system gets built, the deal closes. Courts see markets through transactions that failed: the disputes, the misunderstandings, the governance breakdowns, the places where the standard practices of an industry proved inadequate to the specific circumstances of a particular deal.

Several observations recurred across cases spanning two decades:

**Contracts describe aspirations, not obligations.** Enterprise technology contracts are frequently written in language that both parties understand differently. The ambiguity is not always inadvertent — sometimes it is how deals get done when detailed specification would reveal irreconcilable disagreements about scope. The cost of that ambiguity is paid at implementation time, or in court.

**Technical credibility is the scarcest resource in technology disputes.** Most attorneys handling technology litigation understand the legal concepts deeply and the technology superficially. Most technology experts understand the technology deeply and the legal concepts superficially. The value of an expert who genuinely understands both the technical and the economic dimensions of a market is disproportionate to their fee.

**Organizational failure precedes technical failure.** In software project disputes, the technical problems that ended up in court were almost never the first sign of trouble. Before the code was bad, the governance was bad. Before the system failed, the communication between client and vendor had failed. Technology markets would generate fewer disputes if organizations paid the same attention to project governance that they pay to technical specification.

**Market research and litigation analysis use the same tools.** The analytical frameworks that Aberdeen used to advise clients on technology decisions — market definition, competitive comparison, TCO modeling, performance benchmarking — were the same frameworks courts needed to evaluate technology disputes. The translation was methodological: research conclusions are presented with confidence levels; legal opinions are presented with certainty. The underlying analysis is identical.

---

## The End of the Practice

My active expert witness practice wound down around 2015, concurrent with the transition away from the independent consulting work that had followed my Aberdeen departure. The case volumes had been significant and the work had been intellectually demanding in ways that complemented the research practice rather than competing with it.

The skills are not entirely retired. Every analysis I have done since 2015 carries the discipline that expert witness work instilled: defend every number, document every assumption, anticipate every objection. When you have spent years preparing analyses that will be subjected to rigorous adversarial challenge, you bring that standard of rigor to everything else.

The legal system is an imperfect instrument for resolving technology disputes. Judges and juries are asked to make technical judgments they are rarely equipped to make. The adversarial process, while appropriate for resolving disputed facts, is poorly designed for understanding complex technical systems where the truth is not binary. The expert witness system mediates these limitations — imperfectly, but better than the alternative of technical decisions made without any independent expertise at all.

What the work taught, above all, was this: the gap between what technology is supposed to do and what it actually does is where most of the interesting problems live. In research, that gap is called an "opportunity." In litigation, it is called a "dispute." The analysis required to understand it is the same either way.

---

*Next: Chapter 10 — The Long View: What Fifty Years of Technology Markets Teach*



---


# Chapter 10: The Long View — What Fifty Years of Technology Markets Teach
### *(1966–2026)*

---

In the summer of 1966, I sat at a console in MIT's computer room at two in the morning, teaching myself FORTRAN on a $5 million mainframe that cost $360 an hour to run.

In the spring of 2026, I can access more compute than that mainframe delivered — for essentially nothing — from a device that fits on my wrist and runs on a battery.

That inversion is the most important fact in the history of information technology. Everything else is commentary.

But commentary matters. Fifty years of watching this industry from the inside — as programmer, consultant, marketer, researcher, expert witness, and co-founder — produces a set of observations that I did not expect to be making when I started, and that I think remain useful to anyone navigating what comes next.

---

## The Inversion That Keeps Inverting

The $360/hour CPU of 1969 defined an entire economic culture. The machine was scarce and expensive. Human labor was abundant and cheap. Every technique I learned in those early years — JCL optimization, one-instruction switches, microsecond-level efficiency — was a response to that economics. The machine was a god that had to be fed with absolute efficiency. You did not "run" a program; you submitted it like a prayer.

The inversion of that equation happened gradually and then all at once (like bankruptcy. By the time I left PHI in 1972, minicomputers were democratizing access. By the time I joined Prime in 1979, compute was escaping the glass house. By the time I left Stratus in 1987, the x86 architecture was preparing to displace everything that had come before it. By the time Aberdeen was founded in 1988, the question was no longer whether proprietary platforms were doomed but how soon.

The inversion is still happening. Generative AI in 2026 is doing to knowledge work what the minicomputer did to batch processing in the 1970s: making a previously scarce resource suddenly abundant, cheaply accessible, and disruptive to every business model built on the assumption of scarcity. The impact is on workers, positive and negative.

The 12-year-old sorting 10,000 pieces of paper on Cape Cod would not be surprised. He always knew the machine would eventually handle the paper. What might surprise him is how long it took, and how many intermediate layers of partial automation preceded the full solution.

---

## Seven Patterns That Repeat

Fifty years of observation produces pattern recognition. Technology markets follow a small number of structural dynamics that recur across platforms, cycles, and decades. Here are the seven I consider most reliable.

**1. The economic winner displaces the technical winner.**

Every major platform transition in the period covered by this memoir was driven primarily by economics, not by superior engineering. The mainframe was not technically obsolete when minicomputers displaced it; it was economically uncompetitive for departmental workloads. The minicomputer was not technically obsolete when x86 servers displaced it; it was economically uncompetitive compared to commodity hardware manufactured at scale. Unix was not technically inferior to Linux; Linux won on licensing economics and community development.

The implication for technology strategists: technical superiority is a necessary but not sufficient condition for market leadership. The sufficient condition is technical adequacy combined with economic advantage. When a good-enough alternative becomes dramatically cheaper, the superior alternative loses. Every time.

**2. Proprietary platforms fund their own replacement.**

The pattern is consistent across every cycle I observed. A proprietary platform achieves market leadership through genuine innovation and tight integration. It captures high margins. Those high margins attract competitors who build open alternatives using commodity components. The commodity alternatives are initially inferior but improve rapidly because they benefit from the entire industry's engineering investment rather than one vendor's. The proprietary platform's margin advantage funds the research and development of the open alternative that eventually displaces it.

IBM funded the research that produced Unix. Proprietary minicomputer margins funded the x86 development that displaced minicomputers. The Internet boom funded the cloud infrastructure that commoditized enterprise servers. This pattern is so reliable that a new proprietary platform's success contains the seeds of its eventual displacement.

**3. Adoption timelines are always longer than technologists predict.**

In my experience across forty years of making and evaluating technology predictions, I cannot think of a single case where a correct architectural prediction came true on the timeline originally projected. SOA: directionally right, five years early. Open source enterprise adoption: directionally right, three years early. Web as application platform: directionally right, two years early. Consumerization of IT: directionally right, two years early.

The consistent mistake is underestimating the organizational friction that slows technology adoption. Technology transitions require not just technical capability but organizational competency, risk tolerance, procurement process adaptation, skills development, and executive conviction. All of these move more slowly than engineering capability.

The practical implication: if you are correct about a technology direction, start positioning three years before you expect mainstream adoption. If you wait until the direction is obvious, the opportunity has passed.

Informed Observation: AI adoption across large and small enterprises is much more a 2030s story than a 2020s story.

**4. The integration problem is permanent.**

Every architectural improvement creates new integration complexity. This is not a solvable problem; it is a structural property of technology ecosystems that grow through proliferation rather than replacement.

In the early 1990s I described this as the "integration tax" — a permanent overhead cost that enterprises pay regardless of how good their individual components become. The N-squared complexity of point-to-point integrations was visible and predictable in 1992. The development of EAI platforms, SOA, APIs, and microservices all addressed the integration problem without eliminating it. Each new integration architecture enabled a new generation of application proliferation that created a new generation of integration complexity.

The enterprises that fared best treated integration architecture as first-class infrastructure from the beginning. The enterprises that paid the highest integration tax were those that treated it as an afterthought — a problem to be solved after the interesting architecture decisions had already been made.

In 2026, as enterprises integrate AI inference engines with operational systems, the integration tax is being collected again on a new layer. The pattern is unchanged.

**5. Data advantage compounds.**

The thesis I argued at Aberdeen in the early 1990s — that data was becoming a competitive asset, not merely an operational record — has proven more important than even its most enthusiastic advocates expected.

The compounding effect operates at two levels. At the business level, organizations that invest early in data infrastructure have better analytical capabilities, which produce better decisions, which produce better outcomes, which generate more data to analyze. The advantage is self-reinforcing. Organizations that defer data infrastructure investment find themselves in a permanent catch-up position.

At the technology level, AI/ML systems improve with more data. The organizations that built large, well-governed data assets through the 1990s and 2000s are the same organizations most effectively deploying large language models and AI inference systems today. The data investments made for business intelligence thirty years ago are foundational assets for AI capability today. No one planned it that way. But the architecture was right.

The Kastner IT research archive would not be possible, nor the bulk of the facts in this memoir, if I had not started saving copies of my digital files, including press quotes. Data is only permanent if you have multiple copies in multiple physical and accessible locations. 

**6. The failure mode is almost never technical.**

In fifty years of watching technology projects succeed and fail — as consultant, advisor, and expert witness — I can count on one hand the projects that failed because of genuinely unsolvable technical problems. The overwhelming majority of failures involved some combination of: governance misalignment between client and vendor, scope that was never adequately defined, requirements that changed faster than the project could accommodate, executive pressure that overrode technical judgment at critical moments, and organizational resistance to the change that the technology required.

This observation is not a criticism of the technical professionals involved. It is a structural observation about complex systems that involve both technical and human components. The technical components can be specified, tested, and verified. The human components — politics, incentives, communication failures, misaligned expectations — are significantly harder to manage and much more likely to be the source of catastrophic failure.

The best technology architects I have known were also skilled organizational diagnosticians. They could look at a client organization and identify the political and governance constraints that would determine whether a technically sound architecture could actually be implemented. That judgment — understanding the human system that the technical system had to operate within — was the differentiating capability.

**7. The machine was never the hard part.**

This is the conclusion that the Cape Cod bookkeeping department, MIT, PHI, ADL, Prime, Stratus, DEC, Aberdeen, and twenty years of expert witness work all produced, from different angles.

Technology problems are tractable. Given sufficient engineering talent, time, and capital, virtually any technical challenge can be addressed. The problems that resisted solution — the integration challenges, the governance failures, the adoption delays, the organizational resistance — were human problems that required human solutions. Alignment of incentives. Clarity of communication. Organizational culture that supported rather than resisted change.

The machine does what it is told, precisely and relentlessly. The hard part is knowing what to tell it.

---

## On Artificial Intelligence: The View from 2026

I have watched the AI field from its inception. MIT in 1966 was alive with the energy of early AI research — LISP, ELIZA, Project MAC, researchers working on the foundations of machine learning and knowledge representation. My roommate worked around the corner from where Marvin Minsky was building the frameworks that defined the field for a generation.

That early AI required explicit knowledge representation: human experts encoding their understanding into rules, frames, and logical structures that machines could reason with. The fundamental limitation was that human knowledge is mostly tacit — we know far more than we can articulate. The expert systems of the 1980s encoded what experts could say, not what they actually knew.

The transformer architecture that enabled the current generation of large language models solved that problem through a different approach: instead of encoding knowledge, train a model on enough examples of human knowledge in use that the patterns emerge implicitly. The model does not know that water boils at 100°C because a rule was encoded; it knows it because it has processed millions of documents in which that fact appears in context.

> **Sidebar: From ELIZA to GPT — Six Decades of AI Development**
>
> **1966 — ELIZA** (MIT, Joseph Weizenbaum): The first chatbot, demonstrating that a program following simple pattern-matching rules could simulate conversation convincingly enough to fool users who knew it was a program. ELIZA worked by reflecting the user's own statements back as questions. It had no understanding of language; it had rules for manipulation of text. The Turing Test implications were unsettling.
>
> **1980s — Expert Systems**: Rule-based AI using explicit knowledge encoded by human experts. MYCIN (medical diagnosis), XCON (computer configuration), and hundreds of commercial systems. Commercially significant but limited by the knowledge acquisition bottleneck: encoding human expertise was slow, expensive, and produced brittle systems that failed outside their narrow design domain.
>
> **1990s — Machine Learning**: Statistical approaches that learned patterns from data rather than relying on explicit rules. Decision trees, neural networks, support vector machines. Required labeled training data and worked on specific well-defined tasks. The transition from rules to statistics.
>
> **2000s–2010s — Deep Learning**: Multi-layer neural networks trained on large datasets, enabled by GPU computing and large digital datasets. Image recognition, speech recognition, recommendation systems. AlexNet in 2012 demonstrated that deep learning could outperform human-engineered features on image classification.
>
> **2017 — Transformer Architecture**: "Attention is All You Need" (Vaswani et al., Google). Self-attention mechanisms that could process entire sequences in parallel rather than sequentially. This architectural innovation enabled training on vastly larger datasets efficiently.
>
> **2020–2026 — Large Language Models**: GPT series (OpenAI), Claude (Anthropic), Gemini (Google), and others. Trained on internet-scale text data. Demonstrate emergent capabilities — skills not explicitly trained — at sufficient scale. The first AI systems that feel qualitatively different from previous generations because they handle ambiguity, context, and implicit knowledge in ways that earlier systems could not.
>
> The thread from ELIZA to GPT-4 is six decades of compounding progress. Each generation solved problems the previous generation could not, while introducing new limitations and failure modes that the next generation would address.

What makes the current AI generation genuinely different from previous ones — and I say this as someone who has heard "this time is different" many times — is the combination of language fluency with broad knowledge and reasoning capability. Previous AI systems were narrow: excellent at specific tasks, useless at everything else. Large language models are broad: capable enough across a wide range of knowledge-work tasks to be genuinely useful as general-purpose cognitive tools.

That breadth is what changes the economics. A narrow AI system automates one task. A broad AI system augments one worker across many tasks. The economic calculus is different in kind, not just in degree.

The inversion this creates is precisely the 1969 inversion in reverse. In 1969: machine scarce and expensive, human labor abundant and cheap. In 2026: machine inference abundant and cheap, human judgment and creativity the scarce resource. The jobs that resist automation are not the jobs that require the most education or the most physical skill — they are the jobs that require the most contextual judgment, the most relationship management, the most ability to navigate ambiguous situations with incomplete information, the judgement.

---

## What I Got Right, and What I Missed

Honest accounting requires both columns.

**Got right:**

The open systems transition. The dominance of RDBMS for operational systems. The compounding value of data. The permanence of the integration problem. The pattern of proprietary platforms funding their own displacement. The consumerization of IT. The broad trajectory of AI from narrow tools toward general-purpose cognitive capability.

**Missed, or got the timing badly wrong:**

Object databases. The Linux path to Unix dominance (right destination, wrong mechanism). The speed of web transformation into full application platform. The emergence of public cloud as the dominant enterprise infrastructure model — I understood that compute was commoditizing but did not fully anticipate the degree to which infrastructure would migrate to shared utility services managed by Amazon, Microsoft, and Google rather than to enterprise-owned commodity hardware--or fail to come from established vendors like Dell, HP and IBM.

Most significantly: I underestimated how thoroughly the smartphone would transform enterprise IT. The consumerization thesis was correct, but I thought of it primarily in terms of user interface expectations migrating from consumer applications to enterprise applications. The deeper effect was that a billion people carrying always-connected computers in their pockets changed what enterprise applications needed to do, not just how they needed to look. The architecture implications of mobile-first, not just mobile-compatible, were larger than I recognized in 2005. The transactions-per-second numbers this decade are mind-boggling.

**The systematic bias:**

All of these misses share a common structure. I correctly identified the direction of change but underestimated the speed and completeness of the transition. Analysts who understand technology deeply tend to be conservative about adoption timelines because they understand the organizational friction in detail. The organizations that made the most money in technology transitions were often the ones that bet more aggressively on the direction being right than the detailed analysis of friction suggested was rational.

That is a permanent tension in technology analysis. The technically sophisticated analyst who understands why transitions are slow is often right about the friction and wrong about the endpoint. The analyst who ignores the friction and calls the direction boldly is often right about the endpoint and wrong about the timeline. The best prediction is the combination: confident direction with realistic timeline. It is harder to produce and easier to claim in retrospect than it appears.

---

## On Building Research Firms

The Aberdeen experience produced a set of observations about building specialized research and advisory practices that I think have lasting relevance.

**Specialization creates more defensible value than breadth.** The firms that maintained premium pricing across technology cycles were the ones with genuine depth in specific domains. Breadth is easier to approximate; depth requires investment and time that cannot be easily replicated.

**Cooperative economics prevent the fragmentation that kills most partnerships.** Firms built on eat-what-you-kill models fragment when successful rainmakers conclude they would earn more independently. The multi-layer revenue sharing model Aberdeen used was complex to administer but created genuine interdependency. Partners had financial incentive to help each other succeed, not just to succeed individually.

**Technical credibility opens different doors.** The engagements that created the most value — and generated the most referrals — were the ones where Aberdeen's technical depth allowed conversations that market-analysis firms could not have. An analyst who can look at a production database configuration and identify specific performance problems commands different pricing than an analyst who can describe market trends. Both are valuable; only one is scarce.

**The culture is set in the first three years.** Everything Aberdeen was and was not after 1997 traces back to what the founding partnership established between 1990 and 1993. The hiring profile, the publishing model, the technical depth standard, the cooperative revenue model — these became self-reinforcing once established. Culture change after scale is orders of magnitude harder than culture formation before scale.

**Free research as marketing is not an insight that depreciates.** The Aberdeen publishing model anticipated content marketing by fifteen years. The underlying principle — that demonstrating expertise before the sales conversation produces better clients and better outcomes than cold selling — has only become more important as buyers have more access to information and more resistance to traditional sales approaches. The mechanism for distributing research has changed entirely (from direct mail and early websites to search, social, and AI-mediated discovery). The principle has not.

---

## The Question the 12-Year-Old Was Asking

I began with a 12-year-old sorting 10,000 pieces of paper on Cape Cod, convinced that machines should handle this work so that people could do something better with their time.

The question was correct. The timeline was longer than he expected. The path was more indirect than anyone could have anticipated. The answer arrived in stages: punch-card tabulation, batch processing, online transaction processing, relational databases, client-server architecture, the web, mobile computing, cloud infrastructure, and now AI inference that can read, write, summarize, and reason at a level that would have been miraculous to the researchers at MIT in 1966.

The Federal Reserve Bank that employed half a million people to sort checks every night in 1960 employs a small fraction of that number today, for a vastly larger volume of transactions. The restaurant bookkeeping department that required three people working through the summer season to reconcile 10,000 pieces of paper can be automated by a POS system running on a tablet that fits in a hostess stand.

The paper has been handled. The machine did it.

What the 12-year-old did not anticipate was that handling the paper would not be the final answer. Once the machine handled the routine work, the question immediately became: what should humans do with the time and capability that automation freed? That question turns out to be harder than the automation question. It requires judgment, values, social structures, and economic arrangements that technology alone cannot provide.

In 2026, AI inference is handling the next layer of paper — the summarization, the pattern recognition, the first-draft generation, the routine analysis that knowledge workers have spent decades performing. The question is the same one the 12-year-old was asking, at a higher level of abstraction: now that the machine handles this, what should we do with the time?

That question does not have a technical answer. It never did.

---
##A Final Observation on the Industry I Loved
The information technology industry between 1966 and 2026 created more economic value, more social transformation, and more genuine improvement in everyday human capability than any other industry I can think of over a comparable sixty-year span. It also created immense waste, broken promises, vendor lock-in, failed projects, security failures, privacy violations, and disruptions imposed on millions of people who had no say in the technical decisions that reshaped their lives. Both things are true. Neither cancels the other.

The people inside this industry — engineers, marketers, researchers, executives, and customers willing to bet their institutions on systems not yet fully proven — worked with incomplete information, real disagreement, and more optimism than the evidence at any given moment strictly justified. Most of the time, that optimism was warranted. Sometimes it was not. But the balance was sufficient to build the industry as it exists: imperfect, consequential, inventive, and still accelerating.

I was fortunate to spend fifty years inside that machine, and more fortunate still to see it from several vantage points as the industry changed shape. I saw it from the machine room, the consulting engagement, the product war room, the executive suite, and the analyst firm. The privilege was not separate from the work. It was the work: to understand what was changing, why it was changing, and what those changes would demand of the organizations trying to live inside it.

If this book has an argument, it is that the machine has never been only the hardware, the software, or even the network. The machine is the whole system: the code, the economics, the institutions, the incentives, the ambitions, and the human beings who must make it work. To spend a life inside the machine is to learn that progress is real, waste is real, and wisdom lies in telling the difference.

*Epilogue follows.*



---


# Epilogue: The Argument with Reality

The check-sorting problem is solved.

The half-million Federal Reserve employees who spent every night touching paper have been replaced by electronic clearing that settles transactions in seconds. Airlines no longer print physical tickets. Restaurant reconciliation runs on a tablet. The labor-intensive commerce that defined the world of my childhood is gone—not gradually diminished, but essentially eliminated across a single working lifetime.

I should feel vindicated. I went looking for automation at twelve years old and spent fifty years helping build it. By any reasonable measure, we delivered.

And yet the deeper lesson of those fifty years is not about what the machines accomplished. It is about what remained stubbornly, persistently, irreducibly human.

---

## What Endured

Every era of computing history I participated in followed the same pattern: a genuine technical breakthrough—timesharing, fault tolerance, relational databases, client-server architecture, the web—that was real and consequential, followed by a period of organizational resistance, economic friction, and human misalignment that made the actual adoption slower, messier, and more expensive than any engineer had predicted.

The mainframe didn't fall to the minicomputer because the engineering was better. It fell because the economics inverted and the culture of the glass house could not adapt quickly enough. The proprietary minicomputer didn't fall to Unix because open standards were intellectually obvious—they were obvious to many of us by 1985. It fell because the margin compression was mathematically inevitable and no vendor found a durable strategy against commodity hardware. The fault-tolerant niche Stratus occupied was not defended by patents; it was defended by the difficulty of making "uptime" feel viscerally real to a buying committee, and by the "pull the board" demonstration that made it so.

The pattern persists. Cloud computing, SaaS, and AI are all genuine technical transitions. They will also encounter the same organizational inertia, the same misaligned incentives, the same gap between what the architecture enables and what the enterprise is willing to reorganize itself to achieve. The infrastructure will move faster than the institution, as it always has.

---

## What I Got Right, and What I Missed

Aberdeen's research in the 1990s was prescient in the ways that matter most: the open systems transition, the persistence of client-server architecture, the dominance of relational databases, the democratization of analytics, the acceleration of integration complexity. We were occasionally wrong on timing—the web moved faster than any of us predicted, and object databases held on longer in our mental models than the market warranted.

The larger miss was cultural, not analytical. We correctly forecast the technology transitions and largely misforecast the human ones. We predicted that Unix would standardize cleanly; instead, Linux won on licensing, not elegance. We predicted that data analytics would become a strategic capability; it did, but later than we thought, and the organizational resistance to cross-functional data integration was deeper and more durable than our frameworks fully captured.

The same honest accounting applies to Aberdeen itself. We built the firm's first seven years on a cooperative model that aligned incentives, rewarded depth, and produced genuinely differentiated work. We correctly understood that published research was a marketing asset, not just a product—a conviction that anticipated content marketing by fifteen years. We correctly understood that technical credibility opened doors that market analysis could not.

What we underestimated was how thoroughly growth capital changes the character of an institution. The venture-backed Aberdeen was a different firm from the partnership-era Aberdeen—more capable in some dimensions, less distinctive in most of the ones that had mattered. The Harte-Hanks acquisition created wealth and destroyed culture, more or less simultaneously. That tradeoff is probably the most honest summary of the go-go years.

---

## The Inversion That Keeps Inverting

In 1969, CPU time on an IBM System/360 Model 65 cost $360 per hour. My annual salary was $7,200. The machine was the scarce resource; human labor was cheap. Every decision I made as a programmer—every microsecond saved, every instruction eliminated, every core dump decoded—was an act of economic conservation.

By the time I left Aberdeen in 2008, the inversion was nearly complete. Compute was abundant. The scarce resource was judgment: the ability to understand what a technology actually does in the hands of a real organization, with real politics, real budgets, and real people who will use it correctly some of the time and subvert it the rest.

As of 2026, the inversion has gone further still. AI inference runs on commodity hardware. Foundation models are available to any developer with a credit card. I'm using them. The constraint is no longer whether the machine can do the thing. The constraint is whether the human organization can decide what to do, govern how to do it, and absorb the consequences of doing it at scale.

That is exactly the problem I encountered at a restaurant on Cape Cod in 1960. It is the same problem I encountered at Chase Manhattan, at Stratus, at DEC, and at Aberdeen. The technology changes. The physics of organizations does not.

To live inside the machine for fifty years is to learn that the technology is only one part of the system. The rest is economics, institutions, incentives, and human nature. That was the education.

*An archive of primary materials from my career and especially the Aberdeen years is available at [GitHub](https://github.com/shorttack/aberdeen-group-archive/tree/main).*


---


---

# About the Author

**Peter S. Kastner** spent fifty years inside the information technology industry — not as a spectator, but as a participant at each of its defining inflection points.

He grew up in Chatham, Massachusetts, where his family operated one of Cape Cod's landmark restaurants. It was there, sorting 10,000 pieces of paper a night in the bookkeeping department, that he formed the conviction that would drive his career: machines should handle the routine work, so that people could do something better with their time.

He trained as a computer operator at the Massachusetts Institute of Technology in 1966 — the same building where ELIZA was being built and Project MAC was laying the foundations of modern timesharing — and taught himself to program on IBM mainframes overnight, on his own operator account, at $360 an hour. He returned to Cornell University, where he had begun studying at the School of Hotel Administration, and continued his undergraduate education while operating Cornell's IBM System 360/65 and writing some of the university's first commercial software applications.

His professional career began at Philip Hankins Inc. in Arlington, Massachusetts — a "hot house" of elite talent whose alumni went on to shape Wang Laboratories, application packages, the Apollo program's software heritage, and the earliest generation of enterprise computing. From there he moved to Arthur D. Little Systems in Cambridge, where eight years of management consulting took him to Chase Manhattan Bank, a federal university hospital in Rio de Janeiro, municipal police departments in Florida and Virginia, a paper mill in Louisiana, a publisher in crisis, and a utility running remote meter reading over power lines at five baud.

He left consulting for vendor marketing, joining Prime Computer in 1979 during its years as the NYSE's top-performing stock, then Stratus Computer in 1981 where he spent six years in the fault-tolerant computing wars against Tandem and IBM. At Stratus he helped build marketing — which IBM eventually OEM'd as the IBM System 88 — and developed the competitive marketing frameworks that made reliability tangible to enterprise buyers who had never seen a computer that repaired itself while running.

At Digital Equipment Corporation from 1987 to 1988 he led the DECtp initiative, conducting a secret midnight benchmark against IBM's largest mainframes that became one of the most discussed competitive moves in the minicomputer era. He was a founding member of the Transaction Processing Performance Council — the TPC — which brought audited transparency to database performance claims and established standards still in use today.

In 1988 he co-founded Aberdeen Group in Boston with two Prime colleagues, Chuck Casale, John Logan, and Tom Willmott. Over eighteen years as Chief Research Officer, he built the firm's research practice from a four-person partnership to a 150-analyst organization, pioneering the model of publishing research findings as lead generation for advisory engagements — a practice now called content marketing. Aberdeen's benchmark research methodology, TCO modeling frameworks, and Best Practices databases defined the gold standard for enterprise technology research through the 1990s and early 2000s. The firm was acquired by Harte-Hanks in October 2006.

Alongside his Aberdeen career, Kastner maintained an active expert witness practice for more than twenty years, testifying and advising in a half-dozen commercial technology disputes involving database licensing, software project failures, storage market antitrust claims, and computer forensics.

He lives in Savannah, Georgia.

---

# Appendix: Career Timeline

## The Arc at a Glance

| Period | Role | Organization | Key Event |
|--------|------|-------------|-----------|
| 1960–1965 | Bookkeeper (summer) | Family restaurant, Chatham, MA | Sorting 10,000 receipts/night; the founding frustration |
| 1965–1966 | Student / Hotel operator | Cornell University | Hotel Ezra Cornell punch-card failure; MIT decision |
| 1966–1967 | Computer operator | MIT | IBM 7094, 360/65; ELIZA; self-taught FORTRAN & assembler |
| 1967–1968 | Computer operator / programmer | Cornell University | 360/65 SysGen; CHASE simulation; first paying clients |
| 1969–1973 | Applications programmer | Philip Hankins Inc. (PHI), Arlington MA | $360/hour CPU; Cumberland Farms; First Chicago DDA; Marine Midland Y2K fix; Cosmos/CAS code generator |
| 1973–1979 | Senior consultant | Arthur D. Little Systems, Cambridge MA | Chase Manhattan ($20B migration); Rio hospital; police systems; ADL design projects/paper mills; Houghton Mifflin rescue |
| 1979–1981 | Market Planning executive | Prime Computer, Natick MA | Prime #1 NYSE stock 1980 (+272%); commercial vertical markets |
| 1981–1987 | Marketing executive | Stratus Computer, Marlborough MA | Pair-and-Spare architecture; IBM OEM System 88; fault-tolerant wars vs. Tandem; XA 2000 launch; John Morgridge |
| 1987–1988 | Senior Marketing Executive | Digital Equipment Corporation (DEC), Maynard MA | DECtp launch; secret IBM 3090 benchmark; TPC co-founding (1988); DECtp "most important launch after VAX" |
| 1919–2006 | Co-founder & Chief Research Officer | Aberdeen Group, Boston MA | Partnership founding; cooperative revenue model; benchmark research; TCO & SNR frameworks; VC infusion (1998); bubble/crash; Harte-Hanks acquisition (Oct 2006) |
| 1992–2015 | Expert witness (parallel) | Independent practice | ~40 engagements; Safeway data warehouse; software project forensics; storage antitrust; computer forensics |
| 2006–present | Independent consultant / author | — | Post-Aberdeen Intel advisory; private equity & startup coaching; these memoirs; AI adoption startup |

---

## Key Technology Platform Transitions Witnessed First-Hand

| Year | Transition | Kastner's Vantage Point |
|------|-----------|------------------------|
| 1966 | Mainframe batch → timesharing | MIT/Cornell operator, IBM 7094 |
| 1969–72 | Service bureau → programmatic automation | PHI, IBM 360 |
| 1973–79 | Mainframe → minicomputer displacement begins | ADL advisory |
| 1979–81 | Minicomputer peak; 4GL emergence | Prime Computer |
| 1981–87 | Fault-tolerant computing goes commercial | Stratus vs. Tandem vs. IBM |
| 1987–90 | VAX/Unix vs. mainframe; OLTP benchmark era | DEC, TPC founding |
| 1990–97 | Client-server; RDBMS dominance; x86 rise | Aberdeen partnership years |
| 1997–2001 | Internet boom; e-commerce infrastructure | Aberdeen scaled years |
| 2001–03 | Bubble crash; SOA emergence | Aberdeen downturn navigation |
| 2004–08 | Consumerization of IT; SaaS emergence | Aberdeen final years |
| 2008–15 | Cloud infrastructure; mobile-first | Expert witness / Intel advisory |
| 2015–26 | AI/ML maturation; generative AI | Long view / these memoirs |

---

## Aberdeen Group: Key Metrics

| Year | Revenue | Net Profit/(Loss) | Analyst Headcount | Event |
|------|--------:|------------------:|------------------:|-------|
| 1990 | Startup | — | 4 partners | Founding |
| 1993 | Growing | — | ~12 | Partnership model at scale |
| 1997 | $7.2M | ($132K) | ~30 | Venture capital idea |
| 1998 | $9.4M | ($552K) | ~60 | Post-VC expansion begins |
| 1999 | $14.1M | $732K | ~90 | Internet boom acceleration |
| 2000 | $20.7M | $6K | ~120 | Peak revenue |
| 2001 | $14.9M | ($3.2M) | ~150 | Max headcount; NASDAQ crash |
| 2002 | $9.4M | ($1.3M) | ~80 | Crash consolidation underway |
| 2003 | $6.5M | ($3.1M) | ~40 | Post-crash trough |
| 2004 | $5.1M | ($2.0M) | ~30 | Revenue trough |
| 2005 | $8.7M | $868K | ~19 | Recovery; profitability restored |
| 2006 (Jan–Aug) | $10.8M | $3.97M | ~19 | Acquired by Harte-Hanks (Oct) |

*Sources: Ernst & Young (2002–2005); BDO Seidman (2006–2008)*

---

## The TPC: A Founding Chronology

| Date | Event |
|------|-------|
| 1987 | Kastner ghostwrites *The Future of Transaction Processing* for Yankee Group; predicts microprocessor OLTP dominance |
| 1988 | DECtp blind benchmark vs. IBM 3090; SNA Tax discovered |
| Jun 1988 | DEC announces benchmark results; IBM responds with DB2 v2 on Oct. |
| Aug 1988 | Kastner commits DEC as first TPC member to Omri Serlin over dinner |
| Aug 8,1988 | DEC TPC leadership leaked to MIS Week; TPC publicly launched |
| 1989 | TPC-A (debit-credit) standard published; first audited results |
| 1990 | TPC-B published |
| 1992 | TPC-C (order-entry) published — the definitive OLTP benchmark |
| 1992–95 | Kastner serves as independent TPC benchmark auditor; clients include Stratus, IBM, Groupe Bull |
| Post-1995 | TPC requires certified auditors; Kastner exits auditing practice |
| Present | TPC continues publishing benchmarks (TPC-H, TPC-DS, TPC-E) used across the industry |

