# Chapter 1: Waiting for Automation (1960-1969)

> Archived from: MASTER-EBOOK-ASSEMBLED-v4.md (Chapter 1: Waiting for Automation (1960-1969))
> Original publication date: 2026-05-14
> Author: Peter S. Kastner

---

## Original Document Text

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




---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | volume-1-ch01-waiting-for-automation-1960-1969 |
| title | Chapter 1: Waiting for Automation (1960-1969) |
| author | Peter S. Kastner |
| date | 2026-05-14 |
| type | memoir |
| subject_domain | memoir/volume-1 |
| methodology | oral-history |
| source_file | MASTER-EBOOK-ASSEMBLED-v4.md (Chapter 1: Waiting for Automation (1960-1969)) |
| license | CC-BY-4.0 |

### Abstract

Peter S. Kastner recounts his formative years growing up on Cape Cod running the bookkeeping department of his family's large restaurant, where the labor-intensive paper reconciliation problem planted the seed for a lifelong drive to automate commerce. He traces his path from Cornell University's Hotel School — where a failed punch-card tabulation experiment and an IBM 360/65 operations job deepened his technical grounding — through a year at MIT's computing center, where he encountered timesharing, early AI, and the first DEC minicomputers. The chapter closes with his contributions to Robert Chase's hotel-management simulation software at Cornell and his departure for Philip Hankins Inc. in Boston, still in pursuit of the paper problem that had never been solved.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | This chapter establishes Kastner's core intellectual motivation — automating paper-intensive business processes — and documents hands-on contact with IBM mainframes, early timesharing, AI research at MIT, and the dawn of minicomputing, all framed as lived experience from 1960–1968. |
| **Relevance** | high | The chapter provides deep primary-source context for 1960s computing infrastructure, the economics of batch processing, and the paper-intensive workflows that defined early automation targets, making it directly relevant to any study of computing history and business automation. |
| **Prescience** | high | Kastner's intuition in 1960 that commerce was absurdly labor-intensive and that machines should handle the paper proved foundational; his early identification of floating-point arithmetic as unsuitable for accounting and his observation that distributed remote job entry was effectively 'cloud' computing decades before the term existed demonstrate consistent foresight. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (20)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Peter S. Kastner | person | active |  |
| Massachusetts Institute of Technology (MIT) | institution | active |  |
| Cornell University | institution | active |  |
| IBM | company | active |  |
| Digital Equipment Corporation (DEC) | company | acquired | Compaq / HP |
| Federal Reserve Bank | agency | active |  |
| Philip Hankins Inc. (PHI) | company | unknown | [DEFERRED] |
| NCR | company | active |  |
| Stratus Computer | company | active |  |
| General Electric (GE) | company | active |  |
| Marriott | company | active |  |
| Intercontinental Hotels | company | active |  |
| Howard Johnson's | company | dissolved | [DEFERRED] |
| KFC (Kentucky Fried Chicken) | company | active |  |
| Project MAC (MIT) | institution | dissolved | MIT CSAIL |
| Robert M. Chase | person | active |  |
| Dave Pulleyn | person | unknown |  |
| Arlene Larsen | person | unknown |  |
| Kastner Family Restaurant (Cape Cod) | company | dissolved |  |
| Cornell School of Hotel Administration | institution | active |  |

### Technologies Referenced (24)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| IBM 360/65 | platform | IBM | emerging | legacy-end-of-life |
| IBM 1401 | platform | IBM | mature | legacy-end-of-life |
| IBM 7094 | platform | IBM | mature | legacy-end-of-life |
| IBM OS/360 | platform | IBM | growing | legacy-end-of-life |
| IBM Punch-Card Tabulating Equipment | platform | IBM | declining | legacy-end-of-life |
| FORTRAN | language | IBM / open standard | growing | active |
| IBM Assembler | language | IBM | growing | legacy-supported |
| PL/1 (Programming Language One) | language | IBM | emerging | legacy-end-of-life |
| COBOL | language | open standard | growing | legacy-supported |
| Multics Operating System | platform | MIT / GE / Honeywell | emerging | legacy-end-of-life |
| LISP (List Processing language) | language | MIT | emerging | active |
| ELIZA | application | MIT | emerging | legacy-end-of-life |
| Spacewar! Video Game | application | MIT | emerging | legacy-end-of-life |
| DEC PDP/8 | platform | Digital Equipment Corporation | emerging | legacy-end-of-life |
| HASP (Houston Automated Spooling Processor) | application | IBM / NASA | emerging | legacy-end-of-life |
| Batch Processing | platform | various | mature | legacy-supported |
| Timesharing (IBM 7094 / Project MAC) | platform | MIT / IBM | emerging | legacy-end-of-life |
| Magnetic Tape (800 bpi) | platform | IBM | mature | legacy-end-of-life |
| IBM 2311 Disk Pack | platform | IBM | emerging | legacy-end-of-life |
| Remote Job Entry (56 kbps telephone line) | protocol | IBM / Cornell | emerging | legacy-end-of-life |
| CDC 1604 | platform | Control Data Corporation | mature | legacy-end-of-life |
| Adding Machine / Mechanical Calculator | platform | various | mature | legacy-end-of-life |
| IBM 360/67 | platform | IBM | emerging | legacy-end-of-life |
| CHASE / CRASE / CHESS (Cornell Simulations) | application | Cornell University / Robert M. Chase | emerging | legacy-end-of-life |

### Observation Summary

- Total observations: 101
- By type: personal-recollection: 60, topic-insight: 20, expert-opinion: 11, market-data: 10
