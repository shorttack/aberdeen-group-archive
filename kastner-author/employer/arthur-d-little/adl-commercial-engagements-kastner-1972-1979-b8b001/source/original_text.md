# Kastner's ADL Commercial Engagements: Chase Manhattan TOOS, UFRJ Brazil Hospital, Houghton Mifflin, Ocean Spray, and Other Industry Studies (1972-1979)

> Archived from: ADLS-Chase-Manhattan-bank-2.docx; Memoir-Scratch-Pad-4.docx; PSK-technical-bio-ADL-5.docx
> Original publication date: 2025-04-01
> Author: Peter S. Kastner

---

## Original Document Text

=== ADLS-Chase-Manhattan-bank-2.txt ===
﻿ADLS Chase Manhattan bank
Background
Arthur D little was a consultant to chase Manhattan bank at the highest David Rockefeller levels. It came to our attention that chase had a significant problem in its trust operations department. Around 1972, chase began to replace its existing card oriented trust and securities handling system. The reason was simple the card handling was done by Univac 96-column cards, and Univac was getting out of the unit record business. 
Chase management made two prudent decisions: they bought a large volume of spare parts for their obsolescent Univac card machines, and they started a large IT project to bring trust processing onto their IBM 360/ mainframe. 
Fast forward a year. One long weekend, the janitorial staff made the decision to empty the locked closet containing the world's supply of univac unit record spare parts. Chase tracked those parts all the way out to the ocean where they were dumped at sea. At this point, an audit of the parallel IT project was called and Arthur D little was brought in. The IT project was a complete disaster there were 400 written COBOL programs. However, there was no system flow chart. ADL quick concluded the chief team would not complete the new trust operations system before the bank ran out of punch card machines. (I wish I was at that meeting.) 
One of the team numbers, Murray Sherry, who had been my boss at Phi, and had hired me into ADL, came up with the idea of using Cosmos to rapidly substitute for the floundering Chase effort.
Transition to TOOS—Trust Operating Operating System
I was one of the few people in the world who was fluent in Cosmos. However, I was deeply engaged as project leader in the Ocean Spray Cranberries project. With nowhere else to turn for substitution, I was yanked from the Ocean Spray project and put on an airplane to New York City. We were able to hire as a contractor Mary Ellen Holland as co developer of the Cosmos-based applications. Mary Ellen, known as Mel, had worked at marine Midland bank with cosmos and notably was the first woman to graduate from Columbia University with an MBA. She was one of those early brilliant technology women that you read about.
The TOOS Applications
Mel and I collaborated on everything. The application design was fairly straightforward. I was the lead on the securities application and Mel had the customer application. In a batch processing environment, the day’s transactions were validated in cosmos and sorted down into application and then processed in each application. Thus, price changes, stock splits, and dividends were processed before being needed in the customer applications for pricing and statements. After the updates, report records were reported and printed or sent as files to other applications.
Both the securities and customer applications were about the same size, 6000 punch cards. Each application resulted in a 12 million line Cobol application. The 6000 lines of code were well within my span of control it took roughly six months to design and program each application, which of course was done in parallel. Meanwhile, a Chase team was working on the conversion of the unit-record application and system testing.
Your eyebrows may have raised reading the last paragraph about that 12 million line Cobol application. Yes the Cobol framework was large but most of that code was for exception handling that the Cosmos programmer did not have to worry about. In reality, a 256K IBM 360/65 mainframe running the MVS operating system could process thousands of accounts per minute. 
Phasing Out
With all of the unit testing completed, ADL was able to meet a client's requirement that I participate as proposed in designing and implementing a hospital administration system in Rio de Janeiro. That yanked me off the Chase Manhattan Bank project before it went into production however I kept in touch and it did indeed go into production and to the best of my knowledge the cosmos code I wrote never caused an application rerun. That I am proud of.
Anecdotes
One of the project challenges was having to fit the data that formally fit on 96 column evac punch cards onto IBM 80 column cards. Choices were made and 1 turned out to be incorrect. Turns out David Rockefeller, chairman of the bank, required more than $99,999,999.99  for his quarterly Exxon dividends. I cheekily asked how big does it need to be. The answer was one more 9.
Mill Holland, who lived in the far reaches of Connecticut, often stayed with her sister in swanky midtown New York I had to be very careful not to drool while walking past the Renoirs in the sister's apartment, which looked like a Sotheby’s preview.
I was a bachelor in New York on expense account. I stayed at the Drake hotel and often ate at the quaint restaurants on what is now called billionaire row. Life was good.
There were times when I could leave the chase building and catch a 435 helicopter from South ferry and the airborne to Boston by 5:15. Those days are gone.
A few thoughts on ocean spray cranberries
1 the Burroughs 1700 was the small machine. the flaw at ocean spray was twofold 
A 1st the B 1700 only had 64 K of semiconductor memory however it had a virtual operating system. The configuration was specified by Burroughs and obviously the memory was inadequate,
B unfortunately, the virtual operating system with inadequate main memory did what it was designed to do: it paged to external storage, Which was very slow drum storage. It took 20 minutes to compile a simple program.

2 The Burroughs smart terminals place at each of the four major cranberry processing centers were the state-of-the-art idea in 1972 they were keyboard based, could print complicated order forms with multiple copies, were programmable, and had cassette storage so work could be done offline without tying up a phone line to run the 300 bps modem  (long distance phone calls cost more than $1 a minute). The programming was done by a Burroughs recommended subcontractor. I was at chase Manhattan when all of the pieces of ocean spray cranberries were put together.




=== Memoir-Scratch-Pad-4.txt ===
﻿Memoir Scratch Pad

UFRJ
1 The UFRJ project called for ADL to provide hospital administration procedures including applications tailored to run on the universities Burroughs 6700 computer. Basically, ADL delivered manuals of procedures and the computer applications to administer a brand new 250 bid teaching hospital which had no staff.
 We came up with a terminal based design because the hospital was about 7 kilometers away from the university computer center at the design review the you have RJ administrators, who spoke English, hemmed and hawed but we eventually understood why we had to scrap the design. The proposed online terminals had to be paid for in U.S. dollars, and foreign exchange was a big problem for Brazil at that time. However, UFRJ had an answer for us: The application would be forms based, with batches of forms carried from the hospital to the computer center continually by new workers on bicycles paid the minimum wage this was social justice as it created jobs for the people near the favela (slum)  which the hospital was built  to support. Social justice in action.
We wrote the design documents in English and all of the application cobol code in English. Professional translators provided the proper documents for forms. The Burroughs 6700 was easy to use: much less grief than the IBM 360 for job control, for instance.
2 The manual labor on bicycles served as social purpose and was not different than what chase Manhattan bank was doing at the same time in New York except for the movement by bike.
3 The year of support… ohh the stories. Yes telex was used but it was not effective so I became an early Pan American frequent flyer making 3-4 overnight trips between Boston and Rio de Janeiro. Stayed in a hotel on the beach near Ipanema. took a taxi out to the university data center. There were a few bugs that were corrected and the last one turned out to be a system programming flaw. This took place in the ADL project off at the university. Our window air conditioner had been removed, and sweat dripped on my coding pad in the 104 degree heat.
the burroughs indexed sequential access method for cobol didn't work and I ended up writing a small program to prove that and brought the results back to Boston to get it fixed. One hitch was at the airport going home. Brazil is a very moral country and things like pornographic movies are strictly forbidden. however computer magnetic tapes are very sensitive and not designed for customs officers to pull the tape off the reel streaming onto the floor of the airport looking for the images of forbidden subjects. meanwhile I'm yelling in pigeon Portuguese that it's computer stuff and not anything else. eventually I retrieved the tape, wound it back up and could do nothing but take it back to Boston and hope it worked, and bless it the tape was still good. Remote support is a bitch.

4A Background: ADL initially told me to pack for an 18 month assignment in Rio. They actually unwittingly proposed leaving my wife in Boston for a year and a half. And the project needed two more COBOL programmers; my wife, Kate, was a COBOL programmer so a deal was made: we got less than two stipends. The third programmer was Barbara Kruesi, a volunteer from ADLS. The project leader was Hans Nijkamp, a Dutchman hired for the project. It did not occur to me that the project did not require Hans, who had to work hard to look busy, and that I was perfectly capable of managing the technology side. I was probably viewed as too young and risky to be on this overseas project as an unproven manager. The project was slated to run 18 months and include a pharmacy inventory system. That was replaced with a migration of a Minnesota hospital system. In late September, and without disclosed reason, the project was told to finish by year end. So we worked harder to meet that schedule. Overall, the project team spirit was not great as we had the commute, a do-nothing project leader, the due date, and the business culture differences.
4B. Life in Rio de Janeiro was generally great. The exception was the daily commute across town in rush hour traffic, horrific air pollution, and Boston-level drivers. The good-to-great parts included
    • Living a block from the famous Leblon beach in a furnished apartment. We hired a Portugese-speaking maid to cook and keep house. That forced our Portugese along. Plus the project funded a language instructor to work with us during lunch hour.
    • Weekend use of the project VW hatchback. Peter, Kate, and Barbara went every point on the compass in that reliable car. We also travelled to Belo Horizonte with a Brazilian-American, to San Paulo, Salvador da Bahia, and a long weekend in Manaus in the Amazon. On exiting Brazil, we departed through Foz do Iguaçu on the Paraguay/Brazil/Argentina border, Buenos Aires, Ecuador, and Peru.
    • The military junta made the streets very safe day and night. We took advantage of off-work hours in a sub-tropical area with bars, beaches, and friendly people. Moreover, there’s not just one girl from Ipanema, they’re thousands on the beaches every weekend.

The ADL Proposals
Adl consultants would often propose transformational projects at the C-level and get funding to do a functional specification. In retrospect, I was brought in on about ten of these design opportunities and absorbed a great deal about businesses I knew nothing about. Designing a new system meant going out to factories and laboratories to see production lines, talk with users, and tease out the ROI opportunities. Many were never implemented, yet I gained the knowledge of how that particular problem could be automated: Some of these from my resume include:
    • Ocean Spray Cranberries started as an ADL consulting assignment
    • CitiBank late-1970s minicomputer SWIFT funds transfer
    • Wisconsin electric: remote meter reading using AC voltage fluctuation at five baud to avoid a telephone line connect
    • Production system for Parade magazine, then a Sunday newspaper insert nationwide
    • Kraft paper manufacturing for Continental Forest Industries: trees to cardboard at thousands of feet per  second.
Houghton-Mifflin deserves its own section. A classic story never told. HM was a big Honeywell shop. They needed a new order-entry and inventory control system. After a long development effort and some testing, it was decided that it would be convenient to cut over to the new system on January 1st. New accounting year and all that. We got the call in the early spring and put together a 4-man COBOL team working onsite until the job was done. HM’s system was so flawed that bookstores were refusing to pay invoices and the physical inventory at warehouses by auditors failed. The most important bed news was HM could not close its books, and the clock was ticking before the company would have to tell the NYSE to suspend its stock. In short, hair-on fire catastrophe with massive, public implications. The job entailed debugging, one-off programs to repair files and accounts, and a lot of late nights. Then, another disaster: HM had so much processing that it was sending a teenager in a van to run cards, tapes and disks to Honeywell’s regional data center down Boston’s famous Route 128. The kid flipped the van. “Cleanup on Rt. 128.” Meanwhile, someone started calling in bomb threats. The first few cleared the building for hours. By the fifteenth, it was no big deal. You know, the team never got recognition or a big thank you for a heroic effort that turned out well. That’s the problem with big stories nobody wants out in the public.
The bottom line is all those ADL design proposals pumped an enormous amount of industry application knowledge into my experience which proved invaluable later in market planning and market research.

The Big Picture
The totality of my ten year career as a programmer-analyst involved a wide breadth of industries, vendors, architectures, and computer technologies. Add in all the stock market expertise I gained in personal use as well as assignments such as Chase Manhattan, made it possible for me to look at the computer industry as a whole. Virtually all other analysts focused on a particular company or technology area. I could explain trends and how they impacted specific industries, or particular vendors’ product architectures. I had the experience and confidence to take it all on. In that I was unique, and I didn’t quite realize that until well into my Aberdeen career.

Junior Programmer at PHI
I was quite surprised to learn the high respect for Philip Hankins, Inc. (PHI) while researching my memoirs 55 years later. I never knew at the time that Hankins himself programmed parts of the Apollo moon project navigation system, which means I was truly working with rocket scientists.
I started as a junior programmer at PHI in March 1969 at a salary of $7,200 a year. A modest start but I was now a programmer at a professional services company with a data center. The computer operations career was behind me.
I quickly learned while watching customer printouts scroll by that I was not doing too badly: a study of bank officer titles and salaries informed me that many bank vice presidents earned in the $6,500 range. Lessoned Learned: titles are cheap.
I was hired to fix the PHI internal accounting system (see ADL bio), which was costing the company thousands of dollars a month in internal computer time charges. Lesson 1: computer time was $360 per CPU hour. In other words, 20 hours of computer time was equal to my annual pay. Computer time was precious and programmer time (human labor) was not. That equation is completely reversed today, of course, but for today we’re back in the 1960s reality.
PHI’s longstanding customer billing algorithm charged customers by CPU usage inside the application. Eventually, it was realized that the IBM System 360 MVT operating system was consuming a significant amount of billable CPU time running its own tasks and, in particular, user program input-output calls to the OS. Another problem was job step overhead; fewer steps cost less. One of the prime offenders was the PHI internal accounting system, a kluge of six COBOL programs and a Cosmos/CAS application. I was hired to optimize those programs to lower computing costs in the new computer-time billing algorithm which charged customers for I/O calls. Nobody in PHI professional services wanted to touch the code, so I was the luck new hire to get the job. It took about three months to shuffle and glue the six programs into two programs with internal sorts. Along the way, the wonderful data center systems programmers taught me a career’s worth of job control language, I/O minimization, dump reading, and other tricks of the trade. It was an invaluable apprentice’s opportunity on how to be good at the job. 
Apprenticeship was about the only way to learn more, especially practical technology. Things like setting a switch in a single instruction with no memory (slow!) reference. Literally, the tools of the trade were:
    • IBM System 360 reference card—assembler instructions
    • Coding forms for each computer language
    • Plastic templates for making flowcharts. (Sorry, no Visio then)
Moreover, there were no databases, no project management or estimating tools, no debugging aids besides a memory dump, no application libraries or tools except ones you made yourself. And you got one, maybe two computer jobs run in prime shift a day. This made night shift work particularly attractive for productivity through turnarounds.
It’s true. I see programmers today whip up a bunch of code and compile it without a glance, fix the compile problems, and try a unit test. Given the precious nature of computer time, my programmer generation always spent time looking for the keyboard error before the job was run.
After 90 days as a junior programmer (and no doubt whose performance was carefully watched), I was invited to join the PHI professional services division as a programmer/analyst.



=== PSK-technical-bio-ADL-5.txt ===
﻿PETER S. KASTNER Professional Biography (1979)
Mr. Kastner is a senior member of the staff of Arthur D. Little Systems, Inc., 
a division of Arthur D. Little, Inc. His responsibilities include systems design 
and implementation, project planning and management, and computer systems 
consulting assignments. While primarily specialized in many aspects of business 
systems, he is also experienced in law enforcement, hospital administration, accounting,
real-time systems, and minicomputer sizing, selection and procurement.
A large international bank [Chase Manhattan] required design consulting and implementation
expertise for a massive trust securities handling system. Mr. Kastner
managed and acted as lead designer of the securities subsystem.
He assisted in the design of the client account and conversion subsystems.
During the project implementation, Mr. Kastner managed and acted as chief
programmer for the securities subsystem. The application used the
COSMOS application management package to minimize development time.
Once converted, an IBM 360/65 processed 174,000 unique securities held
by over 25,000 trust clients with a combined value of over $10 billion [1975]. The 
securities subsystem manages these securities, producing sixty accounting, 
customer and management infor­mation reports. The project was done under severe time 
constraints as the existing punch-card-based system literally ran out of spare parts 
to keep it running. Using COSMOS, Mr. Kastner and another programmer had 25 million 
lines of debugged COBOL code ready in under a year.

Mr. Kastner designed, programmed and installed three sales analysis
systems for a major publisher [Houghton Mifflin]. One system grouped product sales by
geographic region in order to measure textbook acceptance at individual colleges. 
The second system analyzed company sales and produced detailed reports for a 
publisher's association. The aggregated industry statistics were compared to 
the company’s actual performance. The third system measured trade sales and 
certain product lines against budgets and forecasts. Mr. Kastner also assisted 
in the installation of the publishers remote-batch order processing and inventory 
control system. All work was performed on a Honeywell system 2000 in COBOL.
Before starting those projects, Mr. Kastner participated in a failed project 
stabilization effort for the customer’s new order entry and inventory management system,
which had been prematurely placed in production. Once remediated, more that 100 days
of production had to be re-run so the company could meet its NYSE reporting obligations.

For a food products manufacturer [Ocean Spray Cranberries], Mr. Kastner participated as lead analyst in a study plan for the automation of the company's financial and accounts
system, including order entry, inventory control, invoicing, shipping and
sales analysis. Working with a user committee, he developed the functional
specifications for each application. A hardware evaluation selected a Burroughs B1700 computer with programs using Forte II and NDL, with TC500 intelligent terminals in four locations across the country. A telecommunications study chose the most cost-effective means of transmitting to remote sites. After the study was approved by company management, Mr. Kastner managed the development of detail application design specifications. He subsequently managed the implementation and installation of the five systems at plants across the country. The five applications were order entry, inventory control, shipping, invoicing and sales analysis. The system was complicated by government contract accounting, several kinds of promotional price discounting, and differences in raw and processed product accounting. Interfaces exist to accounts receivable, general ledger, material requirements and standard cost applications. The project required five man-years of effort.

Mr. Kastner designed, managed and assisted in the programming of a salesman incentive bonus system for a mutual insurance company [Mass Mutual]. The system applies a decision table to each category of sales and maintains a history of sales by salesman. A tanked transaction edit concept was used to store transactions during the month, prior to updating the system master files. Written in ANSI COBOL, the sales incentive system
runs on an IBM 370/135 under DOS/VS.
Mr. Kastner was the lead analyst responsible for the conceptualization,
functional specification and systems architecture design of an on-line
order processing and inventory control system for the American subsidiary
of a major Canadian telephone equipment manufacturer [Nortel]. The system was
designed to operate on an IBM 370/158 using CICS and a TOTAL database.
Six remote plants and warehouses were connected to the system. The
applications included order entry, inventory control, stock replenishment
accounts receivable and invoicing.
Mr. Kastner designed, implemented and installed the cost accounting module
in a basic accounting system for the Federal University Hospital [UFRJ] in
Rio de Janeiro, Brazil. The system processes payroll, inventory and
other entries and reports on current and year-to-date expenses against
budget and prior periods. The cost system features a general ledger
subsystem which reports on all hospital revenue and expenses. Implemented
on a Burroughs B67OO in COBOL, the system runs daily with weekly, monthly
and annual reporting. The documentation includes extensive user procedures.
As technical leader for the Brazilian project, Mr. Kastner also contributed
to the design and implementation of a payroll/personnel and a patient
census system. He provided a year of remote and on-site customer support.

For an ADL client hospital in Brazil [UFRJ], Mr. Kastner directed the installa­tion 
of a hospital inventory control system. The system was converted
from a Burroughs B3500 to operate on a B6700 in a university environment.
He developed operations procedures, run-time job control and installed
the system. He managed the program changes necessary to tailor the system
to the Brazilian hospital environment, including manual methods and
procedures, and translation to Portuguese.

A well-known minicomputer manufacturer [Digital Equipment] required assistance in developing
a payroll/personnel system for the corporation. Mr. Kastner designed,
programmed, tested and installed an on-line inquiry and update program
which processes new hires, terminations, leaves of absence, and all
individual field changes. Running on a DEC-10 computer, the payroll/
personnel data base is protected by extensive restart and recovery
routines. All input and output are handled through conversational CRT
terminal methods including prompting. Each transaction is thoroughly
edited by the program using edit tables loaded from data files at run-time.
Mr. Kastner participated as senior software engineer in a study to determine
the requirements for a computer-assisted dispatching (CAD) system for the
Police Department of a major Florida city [St. Petersburg]. The study encompassed a site
survey, hardware and software evaluation and recommendations, functional
specifications, systems architecture specification, and a multi-phased
implementation plan with specific recommendations for grant funding
requests. He was responsible for performing the hardware and the
software evaluation. The city’s IBM 370/135 computer was determined
to be the most cost-effective means of implementing the system. The
software evaluation led to his recommendation of transferring a
dispatching system from another city [Hampton, VA], installing it under CICS, and
modifying the software. Mr. Kastner was a major contributor to the
other areas of the study.
Mr. Kastner was the major contributor to a study of the computer-assisted
dispatching requirements for a major Florida city [St. Petersburg] fire department. He
prepared functional specifications; hardware requirements analysis for
computer hardware, dispatcher terminals and mobile status terminals;
software estimates; and a five-year implementation plan. Fire dispatching,
in this case, differed from police dispatching in that specific fire
units are computer recommended based on a data base containing geographical
references and a pre-fire plan for every building in the city. Key
building data is transmitted to the mobile terminals while the fire
equipment is enroute to the fire.
Mr. Kastner managed the preparation of a proposal to an international
bank [Citibank] to automate world-wide funds transfers with a network of minicomputers.
The system had stringent reliability and availability requirements, which
required state-of-the-art hardware and control software. The application
processed funds transfers through a star network with interfaces to Federal
Reserve, CHIPS, SWIFT, Bankwire and the bank's own network of 250 overseas
branches. A complex database allowed current and historical transactions
access through multiple inverted indices.
For an ADL client, a Midwestern newspaper chain [Parade Magazine], Mr. Kastner
contributed to a study of the company’s business systems. He assisted as lead
analyst in defining applications which warranted automation, developing
an overall systems architecture, selecting a central computer system
and remote intelligent terminal hardware, and in establishing the company’s
data processing organization. He prepared functional specifications
for the priority applications and evaluated business systems software packages.

As vendor support manager, Mr. Kastner is responsible for the management
of our OEM relationship with Data General Corporation, Digital Equipment Corp., 
and Hewlett-Packard. He is responsible for minicomputer configuration manufacturability, hardware and 
software ordering and scheduling, customer site planning, and installation. He acts as
technical consultant on Data General products, including new product
evaluation.
As vendor support manager, Mr. Kastner contributed to the ADLS Public Safety 
Group’s projects. The company developed custom, fault-tolerant minicomputer systems 
for police dispatching (e.g., 911 calls)including Boston, Philadelphia, Minneapolis, 
Aurora (CO), and St Petersburg (FL). Developed under federal funding and LEAA 
regulations, these systems typically used state-of-the-art mobile communications 
to police (and fire) units.
For a large science and engineering development company [American Science and Engineering],
Mr. Kastner led a team in auditing the FORTRAN source of a pioneering Computer-Aided 
Tomography (CAT)scanning product. This early hospital diagnostic tool took particular 
steps to avoid exposing patients to excess radiation in spite of any kind of system failure.
For an Arthur D. Little project, Mr. Kastner participated in a team writing FORTRAN programs
for a United States Navy ship design study [CASDOS].
Mr. Kastner has a secret clearance, and he serves as the Security Officer of ADLS.
Philip Hankins, Inc. (PHI)
Prior to joining ADLS, Mr. Kastner was a senior programmer/analyst
with the Professional Services division of PHI Computer Services, Inc., a 
subsidiary of Wang Laboratories.
Mr. Kastner converted an Accounts Receivable system from DOS COBOL to
OS/MVT on a 360/65. Several enhancements were made to the system to
link receivables with general ledger, provide additional cash control
and management reports. The conversion process included combining six
programs into two major processing modules. These new programs cut the
system operating costs by one half.
Mr. Kastner helped design, and later programmed, the internal accounting
system for PHI Computer Services, Inc. He developed interfaces to
proprietary and general ledger systems; programmed the contract status and
machine time accounting systems; designed and programmed a travel expense
accounting system; and programmed a labor cost system. All of these
systems were written in OS/360 COBOL to run on a large system 360 computer.
The machine-time accounting and contract status reporting systems were
programmed by Mr. Kastner. Based on reduced SMF data from a 360/65, the
machine accounting system bills CPU time; channel I/O time; disk storage;
tape, disk, card and printer time. Rates were based on job priority and
a complicated discount schedule. The contract status system bills
professional service labor and expenses on a contract basis. A common
invoice is prepared based on input from the machine time and contract
status systems.

For a large mid-Western bank [First Chicago], Mr. Kastner assisted in the design and
programming of a correspondent bank demand deposit accounting system.
Each of the fourteen correspondents had a custom-tailored application
based on run-time parameters and a flexible model application software.
The system language was COSMOS, a proprietary package which greatly
improves programmer productivity. Mr. Kastner programmed the interface to
an on-line check processing front-end, and the validation and update
portions of the DDA system.
Mr. Kastner designed and programmed a retail gas station accounting 
system for a chain of gas stations {Cumberland Farms]. Written in IBM COBOL, the system
processes dally cash transmittal forms which are proved to pump meter
readings. Periodic physical inventory double checks reported oil,
accessory and TBA sales. Weekly and monthly management reports are
produced to highlight sales trends.
For a regional bank [Marine Midland], Mr. Kastner designed and implemented application
changes to a bond portfolio analysis system, allowing 30-year bonds to be traded in
1970. This served as an early introduction to Year 2000 issues everyone faced
decades later.
Mr. Kastner designed modifications to the PHI Payroll package to allow
on-line batch entry and concurrent master file processing. The client,
a large commercial bank, had trouble meeting deadlines for its 460
customers with a strictly batch system. The design allowed for any
customer's payroll to be released for posting once a batch or batches
of timecards were entered and edited. To make the approach
work, significant problems in the areas of exclusive record access,
restart, and recovery had to be solved.
Mr. Kastner attended Cornell University and the University of California at Berkeley. 
He has formal training in project management, accounting, data base systems, 
control of material flow, and telecommunications.
Additionally, he has attended specialized courses sponsored by IBM,
Burroughs and Data General. He is a member of ACM.


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | adl-commercial-engagements-kastner-1972-1979-b8b001 |
| title | Kastner's ADL Commercial Engagements: Chase Manhattan TOOS, UFRJ Brazil Hospital, Houghton Mifflin, Ocean Spray, and Other Industry Studies (1972-1979) |
| author | Peter S. Kastner |
| date | 2025-04-01 |
| type | employer-record |
| subject_domain | employer/arthur-d-little/commercial-systems |
| methodology | oral-history, document-review |
| source_file | ADLS-Chase-Manhattan-bank-2.docx; Memoir-Scratch-Pad-4.docx; PSK-technical-bio-ADL-5.docx |
| license | CC-BY-4.0 |

### Abstract

Kastner's commercial-systems engagements at Arthur D. Little Systems, 1972-1979. Covers (a) Chase Manhattan Bank Trust Operating Operating System (TOOS) using COSMOS and IBM 360/65 to replace failing UNIVAC card-based trust system; (b) UFRJ Brazil teaching hospital administration on Burroughs B6700 (forms-based bicycle-courier batch design); (c) Houghton Mifflin Honeywell-2000 sales analysis and crisis-mode order-entry remediation; (d) Ocean Spray Cranberries Burroughs B1700 financial/order-entry system; (e) Citibank international funds-transfer minicomputer network proposal; (f) Mass Mutual COBOL incentive bonus on IBM 370/135; (g) Nortel North American order processing on IBM 370/158 CICS+TOTAL; (h) Parade Magazine business-systems study; (i) DEC payroll-personnel on DEC-10; (j) AS&E CAT-scanning audit; (k) US Navy CASDOS ship design.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Comprehensive personal record of Kastner's decade-long ADL career across major commercial systems including a billion-dollar Chase trust system. Documents the technology transitions of the 1970s commercial computing era. |
| **Relevance** | high | Several themes remain pertinent: legacy migration crises, COBOL technical debt, internationalization of IT systems, and the transition from card-based to online transaction processing. |
| **Prescience** | not-applicable | Memoir / employer-record content; no forward predictions made. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (28)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Arthur D. Little, Inc. | firm | operating | [DEFERRED] |
| Arthur D. Little Systems, Inc. (ADLS) | firm | dissolved | [DEFERRED] |
| Chase Manhattan Bank | company | merged | JPMorgan Chase (2000) |
| UNIVAC / Sperry Rand | company | merged | Unisys (1986) |
| IBM | company | operating | [DEFERRED] |
| Federal University of Rio de Janeiro (UFRJ) | institution | operating | [DEFERRED] |
| Burroughs Corporation | company | merged | Unisys (1986) |
| Ocean Spray Cranberries | company | operating | [DEFERRED] |
| Houghton Mifflin | company | merged | Houghton Mifflin Harcourt |
| Honeywell Information Systems | company | sold | Bull / NEC (1991) |
| Massachusetts Mutual Life Insurance Company | company | operating | [DEFERRED] |
| Nortel Networks (Northern Telecom) | company | dissolved | Avaya / Ciena / others (2009 BK) |
| Citibank | company | operating | [DEFERRED] |
| Parade Magazine | company | ceased | [DEFERRED] |
| Digital Equipment Corporation (DEC) | company | acquired | Compaq (1998) -> HP (2002) |
| American Science & Engineering (AS&E) | company | operating | [DEFERRED] |
| United States Navy | agency | operating | [DEFERRED] |
| Cumberland Farms | company | operating | [DEFERRED] |
| Continental Forest Industries | company | [DEFERRED] | [DEFERRED] |
| Wisconsin Electric Power Company | company | operating | [DEFERRED] |
| Mary Ellen 'Mel' Holland | person | [DEFERRED] | [DEFERRED] |
| Murray Sherry | person | [DEFERRED] | [DEFERRED] |
| David Rockefeller | person | deceased | [DEFERRED] |
| Hans Nijkamp | person | [DEFERRED] | [DEFERRED] |
| Barbara Kruesi | person | [DEFERRED] | [DEFERRED] |
| Kate Kastner | person | [DEFERRED] | [DEFERRED] |
| Peter S. Kastner | person | operating | [DEFERRED] |
| First Chicago Corporation | company | merged | Bank One -> JPMorgan Chase |

### Technologies Referenced (25)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| COSMOS application management package | framework | PHI / Wang Laboratories | mature | legacy-end-of-life |
| IBM 360/65 | platform | IBM | mature | legacy-end-of-life |
| IBM 370/135 | platform | IBM | mature | legacy-end-of-life |
| IBM 370/158 | platform | IBM | mature | legacy-end-of-life |
| IBM DOS/VS | platform | IBM | mature | legacy-end-of-life |
| IBM MVS Operating System | platform | IBM | mature | legacy-supported |
| IBM Customer Information Control System (CICS) | platform | IBM | emerging | operating |
| TOTAL database | platform | Cincom Systems | emerging | legacy-end-of-life |
| Burroughs B1700 | platform | Burroughs | emerging | legacy-end-of-life |
| Burroughs B6700 | platform | Burroughs | mature | legacy-end-of-life |
| Burroughs B3500 | platform | Burroughs | mature | legacy-end-of-life |
| Burroughs TC500 intelligent terminal | platform | Burroughs | emerging | legacy-end-of-life |
| Honeywell 2000 | platform | Honeywell | mature | legacy-end-of-life |
| DEC PDP-10 (DECsystem-10) | platform | Digital Equipment Corporation | mature | legacy-end-of-life |
| ANSI COBOL | language | ANSI | mature | operating |
| FORTRAN | language | ANSI | mature | operating |
| Forte II language | language | Burroughs | emerging | legacy-end-of-life |
| NDL (Network Definition Language) | language | Burroughs | emerging | legacy-end-of-life |
| CHIPS (Clearing House Interbank Payments System) | protocol | CHIPS | emerging | operating |
| SWIFT | protocol | SWIFT | emerging | operating |
| Bankwire | protocol | interbank | emerging | superseded |
| Federal Reserve wire network | protocol | Federal Reserve | emerging | operating |
| IBM System/360 assembler | language | IBM | mature | legacy-end-of-life |
| IBM System Management Facilities (SMF) | framework | IBM | mature | operating |
| Univac 96-column punch card | platform | Univac | superseded | obsolete |

### Observation Summary

- Total observations: 37
- By type: architecture-decision: 15, personal-recollection: 9, historical-fact: 5, practice-attribution: 3, outcome: 3, performance-claim: 2
