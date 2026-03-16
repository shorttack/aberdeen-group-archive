# AMD's Gigahertz Equivalency: Confused Customers Accept Bad Science

## Executive Summary

Millions of unsophisticated PC buyers are confronted with a fire hose of sophisticated technology-speak, and feel intimidated, even though they want to make informed buying decisions that include PC performance. These buyers around the world seek the holy grail of a single performance metric for choosing PC processors, thinking they'll be able to select a microprocessor by, say, clock speed as measured in gigahertz (GHz) just like they select the next family car's motor by horsepower. But auto horsepower is measured by automobile-industry standards, while there is no single accepted performance metric that allows buyers to compare microprocessor performance across a wide spectrum of PC usage. And comparisons between processors certainly cannot be made between different processor architectures based on clock speed for the simple fact that different processor architectures do different amounts of work in each clock tick, not to mention application dependencies. Nevertheless, Advanced Micro Devices (AMD) last year deliberately took a step down a slippery slope of bad science when it named its Athlon XP line of microprocessor models with clock-speed gigahertz ratings equivalent, they said, to Intel's competing Pentium 4 (P4) based on a set of application benchmarks. AMD will undoubtedly pay a marketing price in 2002 for the bad science that has confused the market and many PC buyers, as it must soon retreat from the gigahertz equivalency positioning and take another performance rating approach.

What's the flaw in AMD's equivalency ratings? There are many discussed in this White Paper. The key reason is that the equivalency rating is a snapshot in a moment in time -- and time surely marches on in the computer industry -- making the gigahertz equivalency subject to increasing variance over time. For example, the AMD Athlon XP 2000+ processor announced last fall runs at 1.667GHz. The 2000+-equivalency rating is aimed at Intel's P4 2.0 GHz Willamette processor. In less than six months, the 2000+ equivalency rating is no longer factual and scientific based on: numerous application software performance improvements have been issued; the 2001 edition benchmarks used by AMD now have 2002 versions; and Intel introduced the P4 2.0A GHz Northbrook processor, which uses more cache and a new manufacturing process to deliver significantly greater benchmark performance at the same gigahertz as before.

The comparisons will only get worse over time as benchmarks, the operating systems, and applications evolve. Comparing the Athlon XP 2000+ model to the P4 2.0A Northwood -- the new higher-performing processor now in the market -- with the original "equivalent processor" Willamette is not justifiable on the benchmark science, is confusing the market, and could even result in trade-practice legal problems for AMD. Moreover, AMD's processor equivalency methodology is flawed at the core: it assumes a specific application usage model that does not apply to many users; it is platform specific, ignoring critical differences such as memory type; and the methodology uses system-level benchmarks including Input/Output, an approach not used to measure processors alone. There is a distinct Pinocchio factor that will grow over time.

Last October, AMD said it would seek a new means of rating performance through a True Performance Initiative. We applaud this step because AMD will be well served to have this gigahertz equivalency fiasco behind them. The fact is that AMD processors are quite efficient for lots of applications, and do not need the steroids of hokey equivalency to deserve market respect.

## Processor Performance Should Not Be Measured in Gigahertz

Gigahertz alone is a meaningless indicator of performance. It only tells us how often the processor clock ticks measured in billions of ticks per second. Gigahertz tells us nothing about how much work gets done in each clock tick. What buyers are really seeking is some measure of throughput -- how much useful, application work is accomplished per unit of time.

### Choosing a Usage Model

A usage model is the result of a workload characterization. The model makes assumptions about the application mix that PC users will be running on their machines. In the real world, the actual mix is very personal, and depends on what applications are used, for how long, and in the context of work, mobile, or at home. Since personalized usage models are impractical, PC processor manufacturers and the trade press typically report results on a variety of industry benchmarks across several usage categories -- your mileage will vary:

- **Office Productivity** -- Microsoft Office applications, anti-virus, and email;
- **Internet** -- web browsing, Macromedia Flash, Adobe Acrobat, Microsoft or Real media player;
- **Content Creation** -- paper and Internet content creation by either graphics workers or hobbyists, including applications such as Adobe Premier and Photoshop, Macromedia Dreamweaver, and Sonic Foundry's Sound Forge;
- **Entertainment/3D Gaming** -- 3D Winbench, 3DMark, Quake, others measured in frames per second.

Both content creation and 3D gaming are extremely processor- and memory-access intensive, while the office productivity and Internet application benchmarks stress the entire system including I/O even though the processor may not be running at capacity.

In addition, the Standard Performance Evaluation Corporation has a widely accepted processor benchmark called SPECcpu 2000 that is designed "to provide a comparative measure of compute-intensive performance across the widest practical range of hardware". All of the major microprocessor manufacturers are members of and report results to SPEC.

## AMD's Processor Benchmark and Model Number Methodology

AMD's workload characterization white paper assumes a usage model in three equal parts:

- Office Productivity;
- Content Creation;
- 3D Gaming.

AMD selected a variety of PC applications including synthetic benchmarks to represent the workloads in the three above categories. These tests were then run on P4 machines running at 1.5, 1.6, 1.7, and 1.8GHz, and Athlon XP machines running at 1.33GHz (model 1500+), 1.4GHz (1600+), 1.47GHz (1700+), and 1.53 GHz (1800+). The results were then normalized, using the P4 at 1.5GHz as the "100%" normalization point.

The benchmark tests were audited by Arthur Andersen using the attestation standards of the American Institute of Certified Public Accountants.

With a straight face, we report that AMD's benchmark white paper concludes that AMD processors outperform Intel's Pentium 4, and therefore deserve the gigahertz equivalency model numbers assigned by AMD. However, Aberdeen Group is not persuaded by either the way the benchmark was conducted, nor the usefulness to buyers of the gigahertz equivalency ratings.

## Flaws in AMD's Benchmark Methodology

Aberdeen Group did not expect to find flaws in how AMD conducted the benchmarks that led to the gigahertz equivalency model numbers now in use, especially with an attestation letter from public accountants Arthur Andersen. Our complaints are not trivial: they strike at the vary nature of benchmark fairness. After all, the stated purpose of AMD's gigahertz equivalency benchmarks is to provide a scientific basis for what would otherwise be an exercise in mere "benchmarketing" -- the use of benchmarks to advance marketing purposes. Our examination focused on the overlaps between publicly reported results by Intel and AMD. These are Bapco's SYSmark 2001 and the Quake III game.

**No Full Disclosure:** Bapco's SYSmark 2001 rules state that any time SYSmark results are used in public, they must be reported to Bapco. There are no results reported to Bapco as of February 15 for the Athlon XP 2000+. SYSmark 2001 is particularly important because it counts for slightly more than one-third of the entire performance score used to derive gigahertz equivalency in AMD processors. Arthur Andersen's audit attestation is specifically about the 2000+.

**Microsoft Media Player Bug Fix:** AMD and Microsoft found and fixed a bug in Media Player, a component of SYSmark 2001, that caused Media Player not take advantage of inherent Athlon instructions. This fix will be available eventually in a Windows XP software patch. AMD included results both with and without the patch in its content creation results, a situation no real user would have.

**Inconsistent Results:** There are numerous small discrepancies between the SYSmark 2001 results reported in AMD's white paper and on their benchmark audit site and those reported on Bapco's site. While the differences are small, our experience suggests these are indications of repeatability problems, audit problems, or jumping the publication gun. The differences detract from and draw attention to what should be consistent and above board.

**Obsolete Benchmarks:** Winbench 2000 is a component of the entertainment suite. It measures processor-intensive graphics performance using Microsoft's DirectX 7.0 3D software. But all the AMD and Intel systems were tested with Windows XP, which comes with DirectX 8.1. It is unlikely that any real user, particularly a gamer, would load an older version of an operating system component. DirectX 8.1 is tested in this methodology using Madonion's 3DMark 2001.

**Intel Beats AMD-on-Intel:** Intel scores at Bapco beat the results reported by AMD for the same processor on SYSmark 2001. The same is true with Quake Demo Arena II. It should not be surprising that Intel knows how to tune its systems better than AMD. But the lower results achieved and reported by AMD do in turn improve AMD's gigahertz equivalency to Intel.

## Flaws in the Concept of Gigahertz Equivalency Methodology

Even if the benchmarks used to derive gigahertz equivalency were pristinely conducted, Aberdeen Group would still disagree with the concept that a single gigahertz equivalency expressed in a model number is applicable in the real world for more than a few days after the benchmark exercise is completed. The concept of gigahertz equivalency for setting a processor rating:

- Implies a fixed relationship over time, something that seldom happens in the fast-changing computer industry;
- Implies a strict workload usage model which may not be applicable;
- Mixes system performance on I/O with processor-intensive work, a poor way to judge the processor alone;
- Is totally platform dependent.

### Time Waits for No Computer

Tried to sell or give away that old 486 machine lately? Then you know that nobody wants it; it's as obsolete as a buggy whip. What happened? It still runs fine. What happened is the computer industry advanced. And as a result, what was cutting edge performance costing thousands is now a doorstop. The same applies to snapshot-in-time gigahertz ratings. Since AMD wrote its Benchmark and Model Numbering Methodology white paper in early October:

- Microsoft Windows XP was launched in mid-October. Since then, numerous application patches have been issued to make these applications more compatible with and perform better with Windows XP, including applications like Office 2000 that are included in AMD's benchmark suite. But AMD's methodology only uses the original Windows XP CD-ROM, allowing for no changes over time. Not realistic;
- One of those improved applications is Windows Media Player 7.0. AMD and Microsoft found a bug and fixed it. Performance will improve. This is the industry norm. Note that this particular change which favors AMD was incorporated in the results. But the bug was found after Arthur Andersen did its audit, so the improved numbers used to justify AMD's processor gigahertz equivalents stand out. That they changed in less than two months is our whole point: there will always be change. The same AMD processor will do more work in time because the application software will be more tailored to the processor. What is AMD to do? Issue little stickers to put on the processor heat sink that say an 1800+ is now an 1856+? Of course not;
- Some application improvements will benefit AMD alone, such as the Media Player bug mentioned above. Other applications changes will undoubtedly take advantage of Intel's unique P4 architecture and instructions, to the detriment of AMD's processor results. Thus, equivalency will be highly application dependent at best;
- The benchmarks underlying the AMD methodology are changing over time. Ziff Davis' Winstone 2001 has been replaced with Winstone 2002, acknowledging improvements and changes in the underlying applications themselves. It would not be realistic for AMD to freeze the benchmark suite, but if AMD does not, then the entire processor equivalency metric changes over time -- even while the clock rate stays the same.

These uncertainties and unrealities -- which deepen over time -- drive our deep distrust of the underlying methodology used by AMD to derive processor gigahertz-equivalent ratings.

### Workload Characterization: Nine to Five or Nine in the Morning to Nine at Night?

AMD's methodology presumes a workload that is one-third office, one-third digital content creation, and one third entertainment/gaming. Assuming Internet usage is measured in that mix, we believe AMD has the categories correct. It's the usage percentages that makes the difference: should gaming represent 33% or 15% or none? No one should play God with computer user's lives. But that means leaving the workload mix ratios up to the buyer, which implies not having a single processor performance metric on which to base processor equivalency.

### System Input/Output is Not Processor Performance

System platforms are changing, and thus are a poor way to measure a specific processor. For example, next year's 10,000 RPM mainstream disk drives will drive considerably higher performance in office productivity applications, with lesser improvements in content creation and entertainment. Should a faster disk alone lead to a faster gigahertz equivalency rating? What about already rated processors which can also benefit from faster I/O? What about the fact that the processor is idle -- zero gigahertz of work done -- while the disk is being accessed, and how should that affect processor ratings? AMD has chosen to include I/O intensive benchmarks such as Business Winstone 2001 even though these are system-level benchmarks designed to match Dell PCs versus Compaq, not AMD versus Intel processors.

### Platforms are Not Processors

In January, Intel delivered a new architecture variant to the P4, code-named Northwood. Same 2.0GHz as before (and faster models too), but performing better due to architectural improvements such as a larger cache and a new 130 nanometer manufacturing process. All subsequent P4's will build off of this new technology base. That means the Athlon 2000+ is matched against an old processor that no one is buying, making for bogus comparisons with the new 2.0A GHz Intel processor.

Moreover, differences in chipsets, memory architecture and speed, device driver maturity, and countless other differences are unique to a specific platform, not to a specific processor. Many components in a platform will change during the production life of a processor chip, but the chip's inherent clock rate will not.

## Aberdeen Observations and Conclusions

Microprocessor performance measurement is a complex subject even for engineers, so consumers seeking a single metric tailored to their own specific usage workload need to be told it's impractical if not impossible. The closest the computer industry has come to an accepted processor benchmark is SPECcpu 2000, but that benchmark is not directly tied to specific PC applications. Nevertheless, before AMD goes too far down the True Performance Initiative road, we think a hard look at SPECcpu 2000 is in order.

Aberdeen has concerns about the inconsistencies and flaws in AMD's benchmarks measuring Intel and AMD systems. But there is no smoking gun, even though Arthur Andersen ought to explain the discrepancies between its audited results and what is reported at Bapco. We don't think Andersen's examination of these benchmarks will enhance consumer confidence in industry benchmark results.

We are in serious disagreement with AMD over the basic methodology used to determine processor gigahertz equivalency, believing it is fundamentally flawed in measuring processor apples and I/Oranges, using an arguable workload mix that will not stand the test of time. To us, the speed of light today -- and electrons in processors too -- ought to be the same speed tomorrow. AMD's methodology will not support that without becoming quaintly obsolete in another ninety days, as the methodology breaks down completely over time. Bad science in the name of customer advocacy is not the approach to market we would recommend.

Aberdeen is not alone in questioning gigahertz equivalency. Our close reading of the PC trade press and PC performance web sites shows an increasing skepticism, and we would not be surprised to see the press turn surly.

The AMD True Performance Initiative program, announced in October as truly strategic, has sunk beneath a wave of performance-equivalency press releases. Progress needs to be announced soon about TPI or else the initiative will appear to be a marketing ploy.

We have seen advertisements in Europe and on the web which take gigahertz ratings from sublime to ridiculous: naively reporting gigahertz-equivalent AMD model numbers as actual gigahertz. AMD will have achieved what some cynics believe is its strategy: feinting one way by arguing gigahertz ratings as meaningless, while hoping the market will "up clock" its products. This would be deceptive at best and downright illegal at worst. Meanwhile, buyers remain confused.

We agree with AMD that gigahertz alone are a poor measure of processor performance. But the gigahertz equivalency methodology baked into the model number as practiced by AMD is another meaningless indicator of performance. Aberdeen doubts this year will pass without a new performance measurement methodology from AMD, requiring a wholesale readjustment in model numbers -- past, present, and future.

---

### Footnotes

1. http://www.hcsdirect.com/products/processors/amdtbird18.htm
i. http://www.spec.org/
ii. http://www.amd.com/us-en/Processors/ProductInformation/0,,30_118_756_3734^3742~10280,00.html
iii. BAPCo license agreement requiring submission of Full Disclosure Reports (FDR) for any published SYSmark performance results.
iv. http://www.bapco.com/
v. One half of Office Productivity and two-thirds of Content Creation.
vi. http://athlonxp.amd.com/benchmarks/benchmarkCertification.jsp
vii. http://www.etestinglabs.com/benchmarks/3dwinbench/3dcontents.asp
viii. http://www.madonion.com/products/#3dmark2001
ix. http://www.intel.com/procs/perf/pentium4/
x. http://www.etestinglabs.com/bi/cont2001/200111/ccws2002.asp
xi. http://www.amd.com/us-en/Processors/SellAMDProducts/0,,30_177_3532_3839^3776,00.html

---

## Frictionless Data Package Metadata

- **Package**: `amd-profile01-db9623`
- **Profile**: Archival Ingest Skill v13
- **Source**: Aberdeen Group white paper, March 2002
- **Ingested**: 2026-03-16
- **Format**: Markdown transcription of original text document
- **Scope**: Lines 1-73 of source file (full document excluding Perplexity-generated metadata)
- **Character count**: ~23,000 characters
- **License**: CC-BY-4.0
