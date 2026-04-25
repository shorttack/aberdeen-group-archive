# Year 2000 Solutions Series Part 1 — Aberdeen Group lead article + 12-point Best Practices (PSK + Susan Irving + John R. Logan, Computerworld Custom Publication, 1997)

> Archived from: Y2K-CW-advertorial-11.pdf
> Original publication date: 1997-05
> Author: Peter S. Kastner and Susan L. Irving (lead article); Peter S. Kastner (12-point Best-Practice sidebar); John R. Logan (companion editorial); Anna Tortig and Computerworld Custom Publications staff (case studies)

---

## Original Document Text


===== Y2K-CW-advertorial-11.txt =====
MAKING THE TRANSITION IS EASY
     IF YOU’RE OUTFITTED RIGHT.


                                                                  Evolving to Year 2000 compliance and beyond is
                                                                  easy when you start with the best tool:
                                                                  MSM/2000. Designed by MS Millennium to
                                                                  maximize the productivity of teams engaged
                                                                  in this time-critical transition, MSM/2000 is a
                                                                  comprehensive suite of software tools that
                                                                  are already being deployed at one of
                                                                  Wall Street's largest firms.
                                                                  MSM/2000 manages all the phases of the date
                                                                  conversion. It automatically modifies source
                                                                  programs, JCL and other library statements,
                                                                  as well as compiles and checks out the
                                                                  modified programs.
                                                                  This interactive tool features:

                                                                  Aggressive MVS Inventory -
                                                                  Tells you what your production inventory is! The
                                                                  MSM/2000 Inventory Module automatically
                                                                  tracks the conversion progress and eliminates
                                                                  the necessity to "Freeze1' applications for the
                                                                  duration of the conversion effort.

                                                                  Substantive Impact Analysis -
                                                                  Reports to you what is at risk and what it will take
                                                                  to fix it!

                                                                  Sophisticated Parsing Approach -
                                                                  Utilizes base displacement approach - as
                                                                  opposed to text scan - to get 100% of all targets.

                                                                  Intuitive Seeding Process - Recommends
                                                                  to the user which are the best candidates for
                                                                  renovation!

                                                                  Comprehensive Regression Test Plan -
                                                                  Determines what’s been changed and what
                                                                  needs to be tested based on dependencies and
                                                                  interdependencies.

                                                                  Dynamic Run-Time Data Bridging Module-
                                                                  Virtually eliminates the compliance deadline for
                                                                  conversion! Your files are dynamically translated
                                                                  through MSM/2000’s closed loop utilizing the
                                                                  MVS/SSI.

                                                                  Evolve with an effective tool backed by highly
                                                                  advanced humans. The most important step you
                                                                  can take toward Year 2000 is selecting the right
                                                                  conversion partner to outfit you properly from the
                                                                  start. Our competition already knows who we
                                                                  are, and you should, too! Select MS Millennium,
                                                                  the company other conversion companies are
                                                                  calling for advice.

                                                                  Contact us today to see the
                                                                  MSM/2000 demonstrated!
   A Subsidiary of The Matlen Silver Group, Inc.
                                                                  Phone: (888) MSM-2003 Fax: (908) 469-2464
                                                                  E-mail: msm2000@msmillennium.com
   InWfT fillilflinn • ?7f) Dnvirisnn Avenue Somerset. NJ 08873   www.msmillenniijm com
                                              A Special Advertising Supplement




   DENIAL:                                                                     's not a solution,

                                                                                                                it's a gamble

                          hen the ghosts of the past come back     about competitive advantage as it is about technology’. In
                        to haunt us, it’s a scary situation.       fact, even executives whose roles have nothing to do with
                            In order to save memory — once         technology will find themselves playing pivotal roles in
                       one of the most precious components         finding Year 2000 solutions for their enterprises.
                      of a computer system — programmers              The key is to start searching for those solutions right
                     in the 1960s and 1970s represented the        away. Many organizations are waiting for a "magic pill’’
                    year in dates using two digits in code         technology to miraculously solve the Year
                    rather than four. This practice persisted      2000 date problem. This approach is at
                   into the 1980s and even the 1990s as firms      best a crapshoot, with potentially disas­
                  tried to maintain backward compatibility         trous implications.
                  with legacy systems — a practice that left
                 many two-digit date fields intact.
                    As a result, the year 2000 will appear to      I This Is Part 1 of a 2-part Solutions Series
                many systems as 00, not 2000, and will be            on the Year 2000. Look for Part 2,
               interpreted as 1900. And lately it seems as if an     which will discuss specific solutions,
              entire industry has arisen to gauge the impli­         In the June 2nd Issue of Computerworld.
             cations of this misinterpretation.



Trade-offs from the '60s
lead to strategic decisions today
                                                                                                                   ILLUSTRATIONS BY TIM BRINTON
             he push by those early programmers for memory
         economy has today’s executives facing critical,
         strategic infrastructure decisions.                                     The lead article in this Solutions Series was co-written by
             Because the implications of wrong dates on a                        Peter S. Kastner and Susan L. Irving of Aberdeen Group Inc.,
           universal scale are not yet truly known, enterprise                   a market research and consulting firm in Boston. As Group
   IS management and supplier management cannot even                             Vice President of Aberdeen, and general manager of its
   fully describe the extent of the problem to their peers,                      commercial systems practice, Peter Kastner analyzes
   much less provide comprehensive solutions. Information                        trends in databases, OLTP, decision support, client/server
   systems today are so widely integrated that finding every                     architectures and distributed commercial systems devel­
   likely corrupt transaction resulting from bad-date calcu­                     opment. He also conducts studies in distributed systems
   lations is an immense challenge. Not finding and correct­                     planning, electronic commerce and database management
   ing bad date fields will disrupt business. And in some                        software issues for suppliers and user organizations. Susan
   cases, those disruptions will be severe.                                      Irving is senior analyst for Professional Services Research.
       Some analysts look at the Year 2000 problem and say                       By focusing on the economics of the business from the end­
   the sky is falling. Others say the problem will be less cat­                  user's perspective, she assists senior executives in analyz­
   aclysmic than originally thought. Either way, the                             ing the benefits of using professional services to achieve
   Aberdeen Group views the Year 2000 problem as much                            their enterprise objectives.



                                                                   THE
                                                        A Special Advertising Supplement




                                   Year 2000 problem will rock busi­        prises by ensuring Year 2000 safety.
                                  nesses with the same force as any         For this latter group, the problem
                                                sudden, unplanned           will be the catalyst for change that
                                                   for market change.       will in turn create opportunity.
                                                    Look at how the
                                                    competitive land­        Not just about software
                                                scape of the airline            The Year 2000 problem is not nec­
                                            industry has shifted             essarily about software. For a com­
                                 abruptly several times in the past 20       pany making consumer packaged
             By Peter Kastner    years due to regulatory changes, the       goods, the problem is about the gain
             and Susan Irving    use of computerized reservation sys­        — or loss — of shelf space. (No
                                 tems and scheduling schemes, and           superstore chain will let a vendor
              Aberdeen Group     international alliances. The catalyst       near its stores without proof of Year
                                 for each shift differed but the out­       2000 readiness for any integrated
                                                                                              inventory and provi­
                                                                                              sioning systems.) A
                                                                                              process company
        How Enterprise Executives Can Play                                                    may find that its Year
                                                                                              2000 problems are
                                                                                              about its ability to
    a Pivotal Role in the Year 2000 Solution                                                  efficiently and com­
                                                                                              petitively use its asset
                                                                                              base. A services com­
                                                                                              pany may find that
     Companies that are not      come was the same: a reshuffling of        Year 2000 bugs undermine its abil­
                                 industry players. Inevitably, the win­     ity to mine data marts for targeted-
                                 ners were the companies who found          customer marketing.
              Year 2000 safe     opportunity — not peril — in change.           For all businesses, the unifying
                                      In the same way, the Year 2000        theme is this: In the best case, the
    will see their competitive   problem will bring market disruption       Year 2000 problem is about deter­
                                 — perhaps upheaval — to technol­           mining competitive advantage; in the
                                 ogy-enabled enterprises and indus­         worst case, corporate viability.
           strengths eroded.     tries. The task of hammering out the           Why competitive advantage?
                                 competitive strategy and plan for sur­     Tightly integrated, Web-enabled
                                 vival will fall on the shoulders of        technology infrastructures are
                                        senior executives. Some of these    becoming the circulatory system of
                                    \     executives will delay making      companies. Global organizations are
                                  --■ty    decisions and find them­         interdependent on realtime, online
                                             selves in a reactive mode      worldwide information that can be
                                               as they scramble for         transmitted from Singapore to
                                                 resources and technol-     Atlanta with a single keystroke.
                                                    gy to ensure the            In many cases, these enterprises
                                                    continued opera­        are also technologically intertwined
                                                      tion of their busi­   with the operations of their cus­
                                                       nesses. Others       tomers, suppliers and distributors. If
                                                       will attempt to      this information flow is compromised,
                                                                            so is their business. And if there is
                                                         competitive        one thing the Year 2000 bug
                                                           footing of       promises, it is to compromise critical
                                                            their           information flows within and
                                                                            between enterprises.


4   THE YEAR 2000
           Ardes 2k” is the only proven
           millennium solution.
               The deadlines for Year 2000
           compliance cannot be missed. This
           innovative product gives your technology
           specialists the knowledge and resources they need to
           understand, and fix, your millennium problems.

               Ardes 2k was developed as the successful result of Data
           Dimensions' 5 years of practical experience with creating
           solutions for the millennium problem. It integrates proven
           strategies, processes, and tools based on experience evaluating
           and updating over 3 billion lines of code for hundreds of
           organizations, including over 30 Fortune 500 companies.
           It allows your organization to develop trained millennium
           experts quickly and easily, with quality support from a
           worldwide leader.

           Customizable, Scaleable, Tools-Neutral Technology
               Ardes 2k incorporates a tools-neutral process bound
           only by the best automation software available. The key is
           a unique Modular Repeatable Process (MRP) that can be
           customized for individual environments, dynamically scaled
           to any size organization, and configured to measure any
           quantifiable results. As a result, your cost and training time
           is effectively minimized, while your enterprise's productivity
           and efficiency is significantly increased.

           Innovative Automated Technology Transfer
               Data Dimensions' unique technological process lets you
           easily transfer Ardes 2k knowledge to your information
           systems personnel and effectively implement solutions. By
           utilizing CD-ROM and Internet technology, Ardes 2k Year
           2000 solutions are now available to a worldwide client base.

           Comprehensive Enterprise-Wide Solutions
               Ardes 2k is the most comprehensive millennium update
           package available. The easy-to-use format provides technical
           information that can be optimized for your enterprise
           environment via CD-ROM, Internet Web site access,
           complementary support tools, products and services.


But how?   Get Started Now
               Ardes 2k is the only proven solution that can help
           your organization meet the complex challenge of 21st century
           compliance.
               For more information, or to order Ardes 2k, call
           Data Dimensions at 800-499-1979, or visit our Web site at
           http://www.data-dimensions.com




                                             Dara dimensions inc
                                     2000 Skylne Tower • 10900 Ni 4th Street
                                                 Bellevue. Washington 98004
                                               A Special Advertising Supplement




    The same interdependence can be          in their area of responsibility and ensure      nature aware of this problem), must
 found in small and mid-sized companies      that their 1997 plans address these             have a persuasive business case for
 who use technology to secure relation­      issues thoroughly.                              Year 2000 funding outside an IT bud­
 ships with larger companies, to market       I CFOs need to be confident that they          get. If this is not possible, they must
 an amplified presence to targeted cus­         have all the information to make             be prepared to offer results-based
 tomers or to perform vital customer-ser­       informed funding decisions for the           business cases for saving one mission-
 vice functions. No company will be             next five years. They also need to           critical IT initiative while shelving
 unaffected — the difference will be the        know the potential impact on finan­          another to free up resources for the
 degree to which a particular company’s         cial statements and, if their company        Year 2000 transition. Prepare for
                                                                                             trade-offs.
                                                                                           > The Board of Directors must have
                           CIOs must have a persuasive                                       input if the funds to complete this




I
                                                                                             project will have an adverse affect on
       business case for Year 2000 funding                                                   three to five years of financial projec­
                                                                                             tions. They may also have a fiduciary
                                             outside an IT budget.                           responsibility to ensure that their
                                                                                             company is Year 2000 ready for busi­
                                                                                             ness. The lawyers are certain to sort
operations are altered.                        is publicly held, be prepared with a          this one out.
   To minimize the risk ofyour business        communication strategy to share­            I Most important, the corporate leader
being compromised, you must start your         holders and the market at large for           — the president and/or CEO — will
Year 2000 transition now. Not being            1997 reporting.                               play a lead role in ensuring that this is
Year 2000 safe by the start of the mil­      I Controllers must check with their             not only an organizational priority,
lennium will erode the competitive             audit firm for critical input on how          but that the enterprise pulls together
strengths of companies who, in turn,           regulatory accounting rulings — for           in a war-time-like effort to meet the
will lose to industry' players who better      example, the Financial Accounting             non-negotiable deadline of Jan. 1,
manage this transition.                        Standards Board (FASB) in the U.S.            2000. This will involve early coordi­
                                               — will allow companies to treat these         nation with human resources, change
Executives in the spotlight                    extraordinary costs. FASB is likely           management and training.
     Executives can play pivotal roles in      to insist that publicly funded compa-         This list highlights only
ensuring Year 2000 safety for their            nies expense the costs of modifica­        some of the areas that an
enterprises. But to do so, they will need      tions and repairs for Year 2000            enterprise's executive
to do three things:                            corrections. In contrast, enterprises      team must focus on
  I Require that a comprehensive and           that replace technology will likely' be    today if they
    proactive plan is in place;                able to treat the new system costs as      are
  ► Secure trusted external assistance;        a capital expense.                         find
 I Insist that day-to-day' business oper­    I COOs must feel comfortable that
    ations experience minimal disruption.      Year 2000 transition plans will not
    Above all, executives must marshal         interrupt day'-to-day' business opera­
the collective Year 2000 efforts with a        tions. They must also ensure their
sense of real urgency. This urgency will       involvement in each criti­
send a signal to the rest of the organiza­     cal decision. COOs will
tion that becoming Year 2000 safe is a         also have an early' vantage
corporate priority, and that meeting the       point to see problems
millennium deadline is non-negotiable.         arise and should have con­
                                               tinued participation on the
   Because Year 2000 is a strategic busi­      Year 2000 transition team
ness problem, rather than a technology'        to forestall these problems.
problem, each member of a senior exec­       > CIOs and Chief Technol­
utive team needs to identify critical          ogy Officers, or CTOs
issues resulting from the Year 2000 bug        (two positions that are by


6    THE YEAR 2000 • A Computerworld Custom Publ<
                                              A Special Advertising Supplement




Year 20©0 B©st Practice Recommendations
                                                                       Check hardware, systems software and networking
                                                                   ■ • compliance. Conventional fixes treat Year 2000 prob­
    This list of executive best practices, culled
                                                                  lems only in applications. There are date-field problems in
    by Aberdeen Group from Year 2000 transi­                      networking and hardware equipment and systems software
    tion efforts, service providers and top Web                   that often times are not inventoried — and, ultimately, not
    sites, will grow - and change in emphasis -                   fixed. Executives need to feel comfortable that their project
    as we near Year 2000 transition triggers.                     team is addressing technologies outside of applications.
                                                                  Executives should insist on vendor documentation and certi­
                                                                  fication of the Year 2000-readiness of their equipment. This
     Start immediately! The Year 2000 problem is large,           compliance documentation should also be secured for all
1  • complex and, as yet, undefined. The only given is that it
will get bigger for enterprises that take a wait-and-see
                                                                  purchased applications.
                                                                          Insist on seeing external partner compliance plans,
approach. The cost of external support will skyrocket as
resources are claimed and quality will suffer as companies
                                                                  8     • updates and completion milestones. And be pre­
                                                                  pared to make your own plans available to partners.
rush towards a solution. An early start will give enterprises     Ironically, the enterprises that are the most advanced in link­
time to deploy solutions strategically, rather than reactively.   ing their operations to the operations of their vendors, cus­
       Stop wounding Year 2000 messengers. Word in the            tomers and distributors are most at risk for corrupt data.
2    • IT cubicles is that there are lots of wounded Year 2000
messengers. Don’t be surprised if information about the real
                                                                  Executives need to ensure that all external links are Year
                                                                  2000 safe — and that they can provide this safety back.
magnitude of resource requirements for this project has not             Put the community of Year 2000 resources to work.
yet reached executives in your company.                            cJ'o Encourage the project team to use (if they don’t
       Send lawyers, guns and money. (Substitute "accoun-         already) the Internet communities that have sprung up to
3   • tants” for "guns" and your company has the start of the
resources required for a Year 2000 effort). Issues need to be
                                                                  tackle the problem. In addition, regional user groups offer a
                                                                  lot of valuable shared experiential advice.
understood throughout the organization. Accountants can                    Beware the Law of Unintended Consequences.
provide details on current regulatory thinking on how to
treat project costs — answers that may impact an (expensed)
                                                                  »      • Getting to Year 2000 compliance will likely require
                                                                  new software versions of compilers, operating systems, utili­
repair vs. a (capitalized) replace decision. Lawyers will edu­    ties and other infrastructure software. Expect problems
cate themselves on an enterprises potential exposure from         induced from the infrastructure changes before you even
the transfer of corrupt data or the inability to deliver prod­    change one line of Year 2000 source code. Also, plan for per­
uct due to a technology error.                                    formance tuning as part of the test cycle.
      Request funding for the whole project upfront.              cjl <1 Staff a post-2000 SWAT team. There will be lots of
4    • Using best estimates and all the trusted external assis­
tance they can secure, CIOs should develop five-year project
                                                                   11 U o work to do after 1/1/2000. Even the best efforts may
                                                                  not trap and fix all dates. And some disruptions from bad
 estimates (assuming two years of post-2000 conversion            dates will not be discovered for months. There will also be
  work) for unique Year 2000 transition requirements. This        unanticipated sources of external data that could corrupt
  will be a thankless task as you present this to the board.      your information. A team should be rested, ready and eager
  But laying out the magnitude of the task ahead will allow       to tackle whatever comes up as the century changes.
other critical enterprise resource decisions and planning to      ■fl       Save the blame for January 1, 2000. Many com-
be accomplished. Estimating total costs will also strengthen       I 4m • panies are currently engaged in time-wasting dis­
your case for management, rather than IT, funding later on.       cussions aimed at affixing blame for the problem. Companies
       Treat this as a war-time effort. Fostering a sense of      should not blame anyone — yet. Casting blame today diverts
5    • urgency and common purpose throughout your orga­
nization will lead to a more focused and comprehensive
                                                                  attention away from the real need to fix the date problem
                                                                  quickly, effectively and comprehensively. On Jan. 1, 2000,
effort to meet the non-negotiable deadline. This is not just an   the finger will most likely be pointing at vintage 1997 deci­
IT conversion; it is a matter of competitive viability.           sion-makers who refused to acknowledge this problem and
       Secure trusted outside resources quickly. Many ven-        who did not allocate the proper resources and time early
6    • dors are vying for your Year 2000 transition business.
In 12 months, this will be a seller’s market. When assessing
                                                                  enough to fix the problem.
                                                                  4        Don’t use misfits and re-treads. Give the troops
vendors, ask them what they will not be able to do for your                fighting the Year 2000 war a rosy picture of their
business. The best sendee providers will tell you this.           post-war career path.


                                                                  THE YEAR 2000 • A Computerworld Custom Publication           7
                                        SPECIAL ADVERTISING SUPPLEMENT




                               Year 2000 Issues:
                                 Understanding
                               Will Lead to Action
                                      By John R. Logan, President, Aberdeen Group, Inc.

         erhaps one of the most startling aspects                      Where possible, replace all technology com­
         about
         plans are
         sionals the Year
                     in    2000—
                        place
                  believe that    problem
                                        fewisbe
                                   but can
                                 these        IShow  few­
                                                  profes
                                                 accom-          ponents that cannot effectively support Year 2000




 P
         plan  to dealhave
         enterprises          it. Yes, technicalrealistic
                        witha comprehensive,       repair        safe date codes. (Replacement may appear more
                                                                 costly than repair — until risk factors, lost oppor­
                                                                 tunity costs and financial considerations are taken
                                                                 into account.) Appoint a Year 2000 task force to
 plished in time, within budget and without                      make implementation decisions right away. (And
 disrupting business operations.                                 yes, this will be a high-stress position. The impact
    Even those enterprises that are well on the way              of many Year 2000-related decisions are difficult, if
 to fixing their legacy applications are pulling staff           not impossible, to quantify.)
 off high-priority application development and
 implementation projects, because the assessment                        For non-compliant applications and compo­
 phase of their Year 2000 repair efforts has started             nents that must be repaired because they cannot be
 to uncover more problem areas than originally                   replaced, determine the lowest level of functional­
anticipated.                                                     ity your enterprise must have from them. Put these
    As these new technical problems surface, even                “good-enough” repaired applications in place as
the most competent senior enterprise executives                  quickly as possible (but by November 1998 at the
are not prepared to proactively manage the Year                  latest) to be able to take the additional corrective
2000 repair process. No organization confronting                 actions required to keep your business operative.
a crisis can long afford to tolerate this type of sit­
uation.                                                                Plan to test, re-test and re-test again until
   Executives, both in IS and at senior operations               your entire information infrastructure is proven
levels, still do not feel they thoroughly understand             safe. Be sure to test date-format interfaces with
the issues involved in managing through the Year                 business partners and government agencies with
2000 problem.                                         /          whoni you electronically/ exchange data.
   Even more unsettling is the fact that, as their
knowledge increases, all they see are higher                     \ J Work only with hardware, software and pro­
expenses that are not <covered by today’s budgets.               fessional service suppliers who have a long-term
                         this formula often translates
In the private sector, this                                      commitment to your success. Managing through
into lower profits; in the public sector, it translates          Year 2000 issues — technical, business and legal —
into budget overruns that must be explained to                   will be a tough battle. You will need allies and
skeptical oversight boards.                                      trusted advisors upon whom you can depend.

Look at the long term                                 \             Every Year 2000 management action plan must
   To manage through the Year 2000 transition,                   project the timing and costs required to establish
you must realize that it is a long-term extended                 the desired levels of functionality and quality for
enterprise information infrastructure and opera-                 your enterprise’s information infrastructure today
tions business issue. Once the true scope of the                 and through the millennium transition. Quite a
problem is understood, there are four actions that               challenge — and one for which you will need to
should be part of every plan:                                    employ your very best management skills.
     Time to call HP.
                    For the information technology         the latest Internet-enabled, client-server technology that
ONLY 1,006
DAYS LEFT           executives who hear nothing but        prepares for the future instead of echoing the past.
doom and gloom about the coming of the year 2000,          With our world-class partners, we can help provide
we offer a brighter picture: one that includes an          everything you need, from decision support and

opportunity to re-think, perhaps re-engineer, and most     data warehousing applications to mission critical

definitely provide your enterprise with more flexibility   environments. The bottom line: if you haven’t contacted
and power titan ever before. Since you need to fix the     us already, it’s time to do it now. Capitalize on chaos.
Year 2000 problem anyway, we suggest you do it using       Call 1-800-1IP-KNOWS.


                                                                                                             HEWLETT®
                                                                                                             PACKARD
                                                  A Special Advertising Supplement




                                               working and business issues.                      Enterprise executives can play a piv­
                                                   Because there are so many pieces to       otal role in the Year 2000 solution by
                                               the Year 2000 puzzle, executives should       bringing to the surface critical business
                                               engage a trusted professional services        issues that result from Year 2000 repair
                                               provider to help them navigate the busi­      strategies — and developing and exe­
                                               ness and technology decisions.                cuting the proactive plans needed to
                                                  One attractive option is the consult­      deal with these issues.
                                               ing arm of your audit partner — or a             The upshot is that solving the Year
                                               firm referred to you by them. This firm       2000 problem involves high-level plan­
                                               has a stake in the ongoing viability of       ning and accelerated execution. The
                                              your business, understands the inner           challenge today is for executives to
                      Year 2000 solutions.     workings ol your operations, and is           devise a realistic solution for their
                   Many others exist. For      positioned to continue to apply the best      enterprise (and their enterprises part­
                instance, who will be          practice learning from its collective "Year   ners), secure adequate resources to sup­
        responsible for ensuring that any     2000 projects. Although this firm will         port this effort, find trusted external
 technologically linked vendors, cus­         not provide one-stop shopping services,        consultants, vendors and tools before
tomers, suppliers or distributors are also    it will be in a position to understand         these resources are claimed, and ensure
Y:ar 2000 safe and will not be able to        where to secure additional resources.          an active forum for the escalation of crit­
corrupt the information in your sys­              If your audit firm’s consulting prac­      ical business decisions that must be
tems? And as Year 2000 problems               tice is unavailable, there are many other      decided by senior management.
become operationally apparent and             top-notch consulting and conversion               Executives that meet Year 2000 chal­
business-changing decisions need to be        firms who can provide support. A list of       lenges head-on will lead their enter­
made, who will be responsible for cor­        such vendors can be found at the Web           prises through a more graceful
porate-wide employee communications?          sitewww.year2000.com . Insist on refer­        transition into the next millennium
    This list also does not account for the   ences from consulting companies with           while gaining competitive ground on
equally critical work of the project team,    applicable experiences to ensure that          rivals who are not Year 2000 ready. 2
including finding and using tools to cor­     you have not merely found an oppor­
rect bad dates, developing and verify­        tunist in a three-year market.
ing lists of Year 2000-compliant                  Whomever you choose for external
hardware, software and networking             assistance, you need to secure that rela­
vendors (both for existing systems and        tionship ASAP. By mid-1997, there will
replacement options), and managing
staff morale on a project where the
                                              be little capacity left in the industry.
                                              This will drive conversion prices up and
                                                                                                    COMPUTERWORLD
                                                                                                     Custom Publications
nature of the work is often monotonous        quality down, and will jeopardize the
                                                                                               This Solutions Series on the Year 2000
and career-limiting.                          chances of many companies for a safe             issue was created by Computerworld
                                              Year 2000 transition.                            Custom Publications. For reprints, con­
Obtain outside help                                                                            tact Heidi Broadley at (508) 820-8536
   Most companies, lacking the                Conclusion                                       or at heidi_broadley @ cw.com.
resources, time or comprehensive                  Aberdeen Group believes that there           The Aberdeen Group is at (617) 723-
knowledge to address the breadth of           will be enterprises who gain from their          7890. Peter Kastner can be contacted
Year 2000 problems, will require exter­       Year 2000 solutions by ensuring that             by E-mail at kastner @ aberdeen.com.
nal assistance for their Year 2000 tran­      their technology infrastructures con­            Questions or comments on the second
sitions. Yet there are no one-stop            tinue to enable, rather than disable, their      story in this supplement should be for­
shopping options for such solutions;          business objectives through the millen­          warded to managing editor Peter
                                              nium transition.                                 Bochner at (508) 820-8289 or
                    todaj''s providers
                                                                                               peter_bochner @ cw.com.
                     are focusing on              And because no company is an
                      application conver­     island, these internal technology infra­         Part 2 of this Series will deal with spe­
                                                                                               cific solutions to handle the various
                        sion issues, while    structures often encompass external
                                                                                               pieces of the Year 2000 puzzle. It will
                          overlooking         partners — vendors, customers and dis­           appear in the June 2nd issue of Com­
                             hardware,        tributors — who must also be able to             puterworld. Editorial inquiries should be
                                 net­         share data that is not corrupt.                  addressed to Peter Bochner.
                                                     A Special Advertising Supplement



                                 f
                                                 a lousy job, but            There's neither visible return on
                                             somebody s got to do        investment for management nor glory
                                           it . . . managing year        For the troops in the trenches. But
                                             2000 date-change            there are penalties galore, particularly
                                             projects, that is.          for CIOs. Thomas D. Oleson, an ana­
                                             The Year 2000 prob-         lyst at International Data Corp, in
                                          lem presents IT profes­        Framingham, Mass., puts it bluntly:
                                      sionals with immense               “For CIOs, this is a career-ending
                              project management and organiza­           project if they screw it up."
         By Anna Tortig     tional challenges. First they have to            And screw-ups could have dire
                            convince CEOs and other top man­             repercussions for an organization
                            agers that they should fork over SI          when it comes to Year 2000. “This is
                            million or more to rectify a problem         a stay-in-business situation,” says
                            that was in fact created by data pro­        Wayne Johnson, senior project man­
                                                                                           ager at Reliastar
                                                                                           Financial Corp., a
                                                                                           life insurance and

         Management: Key to                                                                annuities company in
                                                                                           Minneapolis that in
                                                                                           the next 21 months
         **-*-*-** —                                          “Its
i cai                                                                                      will pump $39 mil­
                                                                                           lion into changing
                                                                                            15 million to 20 mil­
                                                                                           lion lines of code
                            cessing departments. Then they have           across all its applications. Notes
               There are
                            to convince programmers to put the            Johnson: "It touches just about any
                            brakes on career advancement and              line of code we have."
        penalties galore,   take on the boring, tedious and time­             Because it started early, Reliastar
                            consuming task of checking thou­              should be safe. But IDC’s Oleson
 particularly for CIOs.     sands and thousands ol lines of               estimates that 10% of large corpora­
                            computer code for any potential fail­         tions will not finish the task of con­
                            ures when the clock strikes 12 on             version by the year 2000 deadline.
                            Jan. 1, 2000.                                 Others, he notes, will meet the dead-




                            Inventory   Planning &
                                                      Conversion   Testing    Implement
                            & Impact    Scheduling




                                                                                           Source: Kappelman & Cappei. 1996



                                               THE YEAR 2000 • A Computerworld Custom Publication                      11
                                                                   A Special Advertising Supplement




  line but will still be finding bugs after                     of concern varies by industry. In the       charge of the situation.
  the fateful day. (Perhaps long after.                         insurance field, where dates are in            Those who were in charge reported
  Bugs don’t always show up right away.                         nearly every line of code, 78% of IS        that they were spending less than a third
  In a program Oleson wrote as an insur­                        managers consider the date-change           of their time on the project. Only 16%
  ance actuary in the 1960s, "the bugs                          problem a major concern. In banking,        were devoting more than 90% of their
  didn’t show up until the end of the                           64% of IS executives feel that way. But     time. That means most Year 2000 man­
  1970s," he notes, "because we didn’t go                       in the manufacturing segment, only          agers are not devoting full-time atten­
  down that branch of the program.’’)                           41% of IS executives, 20% of CFOs and       tion to the project, and, according to the
                                                                                                            study’s author, "if these figures are even
                                                                                                            half true, they portend of a serious
                                     Only 16% of those heading up                                           degree of very negative year 2000-




 I
                                                                                                            related consequences."
           Year 2000 projects are devoting                                                                     The SIM report also suggests that
                                                                                                            important projects, particularly in the
                                                   more than 90% of their time.                             area of application development, may


     What will happen to the laggards —                          10% of CEOs believe that Year 2000 is      r                                       -p
 the companies that don't make the dead­                        a major business issue.                            You're in good
 line? Theresa O'Neil, vice president of
 marketing, data warehousing, for Plat­
                                                                    CIOs tend to see the problem as a
                                                                major business issue more often than
                                                                                                                   hands with ...
 inum Technology, offers one scenario.                          CEOs or CFOs. (That’s understand­                   Several insurance companies
  [They’ll return to paper forms, because                       able, since they’re the ones whose              have begun issuing Year 2000
    eir computers won’t process the right                       careers are on the line.) But there are         insurance policies to cover busi­
    formation,” she says. "Payroll and                          many other blind spots in the recogni­          ness disruptions that may result
    counting will get done, but other                           tion of the problem.                            when systems are converted to
   pplications will get put on hold.”                                                                           handle the date change.
                                                                IS leads in awareness                               These insurers are expected
                                                                   According to a study by the Society          to be very selective in insuring
  Is your company's executive management
                                                                for Information Management (SIM),               companies. If a company does
aware of the real risks involved in this project?
                  Total: 157 responses
                                                                based in Chicago, the perceived level of        not have a comprehensive Year
           Yes                                                  organizational Year 2000 awareness              2000 plan, or il it does have one
                                                                does not extend much beyond the IS              but does not execute it, it might
                                                                department. The study noted a very low          not be able to collect.
                                                                incidence of reported discussions with              So tar users seem less than
                                                                auditors and legal staff, two groups that       bowled over by the policy. One
                                                                should be involved early in attacking           attendee at a Year 2000 confer­
                                                                the problem. It also said that CIOs and         ence said. "I can just see going
                                                                project managers may be reluctant to            up to my boss and saying. ‘Our
                                                                carry word of the problem outside the           systems don’t work. But don’t
                                                                IS department because they are uncom­           worry, we re covered."’
    Comment: One in four executive managers are                 fortable about the problem's origins.               But il nothing else, such an
     unaware of the real risks of the Y2K project.                 The study detected other concerns.           insurance policy may be "bril­
The question is, who’s going to bring them up to speed?
                         SOURCE: Year 2000 Information Center   One problem pertained to those head­            liant in terms of raising manage­
                                                                ing up Year 2000 projects. For instance,        ment awareness," says Don
    Of course, the good news is that                            61% of those in charge of Year 2000             Estes, a 'tear 2000 consultant in
most corporate managers — CEOs,                                 projects have had the assignment for six        Lexington, Mass. “Nowyou can
COOs and CFOs — are already aware                               months or less; only 11% have been in           go to the CFO and speak in
of the problem and understand the con­                          the saddle for more than 12 months.             terms he understands.
sequences of not complying in time. But                         Worse, about 35% of organizations
according to an IDC study, the degree                           polled appeared to have no one in
                                                                                                            L

12     THE YEAR 2000 • A Computerworld Custom Publication
                                                            A Special Advertising Supplement




be ignored as a result of the focus on
Year 2000. The flip side may be true as
well. Europe, notes O’Neil of Platinum
Technology, "is having a heck ol a time
getting corporate buy-in on the Year
2000 issue. Their focus is on the issue of
European currency.”
    Leon Kappelman, co-leader of the
SIM 2000 Working Group and an asso­
ciate professor at the University of North
Texas, says it is crucial to assess the risks
— "If it has anything to do with a chip, it
is potentially at risk,” — and convey that
message to management. He said it may
be enough to familiarize CEOs with the
ramifications of the matter by setting up
a test of a mission-critical system and
showing what will happen if the com­
pany doesn’t change its code. In other
cases, outside pressure (for example,
from an industry group) may be
required. The Securities Industry Asso­
ciation has created a Year 2000 commit­
tee to ensure that securities companies,
banks, stock exchanges and their busi­
ness partners are compliant. The group
plans to conduct a compliance test of
Wall Street companies in early 1999.
    But for CIOs, getting a message
across to top management can be tough.
CIOs who are currently involved in
Year 2000 projects say that when they
brought their boss the bad news, the                     Roland Laferriere, CIO of BJ’s Whole­         chagrined when he explained the root
initial reaction was negative. "The reac­                sale Club, a membership-only ware­            of the problem to the president of BJ’s.
tion by most CEOs is the same: Why                       house club headquartered in Natick,           "CEOs understand what happened, but
did DP do this in the first place?” says                 Mass. Laferriere admits to having felt        still can’t comprehend why,” he says.
                                                                                                           Dave lacino, the project manager of
                      Solving this has the highest priority in my organization                         BankBoston’s millennium management
                                   Responses of 156 CIOs and IS managers                               team, reports encountering the same
                                                                                                       anger and denial when he first went to
                                Neutral (neither agree nor disagree)                                   the Board. But those emotions were
                                                            Disagree or disagree somewhat              quickly replaced by the realization that
                Strongly or totally agree
                                                                                                       the problem was real. "Because the
                                               N/A or I don't know
                                                                                                       CTO had done his spadework people
                                                                                                       knew how to spell millennium,” he
                                                                                                       says. "Funds were committed almost on
                                                                                                       the spot.”
                                                                                                            Pressured CIOs can tty to turn this
                                                                                                       tension-ridden situation to their favor
                                                                                                       through careful project management,
                                                                                                       starting with their initial efforts to gain


                                                                                    THE YEAR 2000 • A Computerworld Custom Publication         13
                                                A Special Advertising Supplement




 the ear of top management. For them,        Year 2000 failure on a key application.                      identifying fields and testing the pro­
 the best strategy may be to anticipate         "We did a slow, gradual preparation,                      grams. They are taking an inventory' of
 management’s questions and explain the      told them what it will cost us and how it                    all programs and tables and identifying
 date-change problem in a way they can       will affect operations and business                          how much of the code needs to be
 easily understand: an article from a        plans," says Laferriere. "The more you                       changed. The company also hired three
 business publication or by illustrating a   can prepare and anticipate questions,                        contract Cobol programmers, since pro­
                                             the better."                                                 grams written in Cobol — the leading
                                                At sporting goods maker Converse                          language for business applications and
                                             Inc., in North Reading, Mass., talks on                      programs in banking and insurance —
          Even the feds                      how to handle the issue began a year                         lie at the heart of many millennium
                                             ago. CIO Vincent Cafferelli spent a                          problems.
          see the light
           Even the federal government.
       which is wrestling with some
       legacy systems so old that                       Anything that has anything to do
       replacement parts are no longer
      available, seems to be emphasiz­                                            with a chip is potentially at risk.
      ing management skills over tech­
      nology as the key to Year 2000
      compliance. "The enormous              good deal of time with top management                          At Converse, all systems that were
      challenge ... is not technical: it     reviewing the history' of the problem,                      used regularly needed some changes.
      is, rather, managerial," said Joel     why it takes so much time and effort to                     "That amounts to thousands of pro­
      Willcmssen, director of the            correct, and what the repercussions                         grams, and 75% of our financial sys­
      information resources manage­          might be.                                                   tems,” says Cafferelli. Some of the
      ment, accounting and informa­              Cafferelli’s plan was to get the CEO                    individual programs only required a
      tion management division of the        on board first, then to talk to the CFO                     total of 5% of the code to be changed,
      Government Accounting Office           and senior executives of departments.                       others 25% or more.
      (GAO), in testimony Feb. 24            Showing management some articles                               The issue also forced Converse to
      before the Subcommittee on             from business publications convinced                        decide whether to replace its 10-year-
      Government Management,                 them it wasn’t just a case of a computer                    old mainframe, which handles order
      Information and Technology, in         glitch, but something that "affects the                     processing, with a client/server system.
      the House of Representatives.          bottom line,” he says.                                      "We had to resolve this issue before
      (GAO is the congressional                  Converse has allocated about 30% of                     tackling the Year 2000 problem. The
      investigating agency.)                 its programming staff primarily to its                      choice was to put in a new sj'stem or
          "Whether agencies succeed or       mainframe systems, going through code,                      change this system over the next three
     fail will be largely influenced by
     the quality of executive leader­                    How much do you estimate it will cost to make your organization's
     ship and program management."                                 information systems Year 2000-compliant?
     Willcmssen added. "It will be                                              Responses of 136 CIOs and IS managers
     imperative for top agency man­
                                                                                  $2.5 million to $5 million
     agement — including the agency
     head and the CIO — to not only                                                               $500,000 to $2.5 million

     be fully aware of the importance                   $10 million to $20 million                             less than $50,000

     ol this undertaking, but to com­                                                   $20 million
                                                    $5 million to $10 million                                          $50,000 to $500,000
     municate this awareness and                                                             I

     urgency to all agency personnel
     in such a way that everyone
     understands why Year 2000
     compliance is so important."




14    THE YEAR 2000 • A Computerworld Custom Publication
years,” Cafferelli says. "We decided to      nologies Ltd., a software services
change the mainframe because . . .           provider in Bangalore, India. BJ's does
changing to client/server was too risky.”    the final testing in-house.
Converse aims to complete its Tear 2000         "Our business plans would have
conversion by January 1999, giving it        been significantly impacted if we tried to
12 months to work the bugs out. Cost to      do this in-house,” says Tom AAcAIahon,
resolve the issue: $750,000.                 manager of systems services for BJ’s.
   For a firm reengineering its business     IS management felt that contract­
with client/server systems, whose soft­      ing out the bulk of the work was
ware accommodates four-digit dates, the      the best way to ensure that BJ’s
date-change problem has essentially dis­     would both meet its target com­
appeared. "A lot of our mainframe sys­       pliance date and not slow new
tems are being moved to client/server,       development efforts. The current
so that aided the Year 2000 part of our      schedule calls for BJ’s 10
reengineering process,” says Frank           mainframe applications           /
Gladwell, IS managerat Berry Network          — which contain 6 mil-
Inc., a Dayton, Ohio, national marketer      lion lines of source code      IraSF
of Yellow Pages advertising and a sub­        — to be converted by          \\tft
sidiary of Bell South. Berry and Bell        July. By then, 80% of its '
South each have teams working on the         systems will be Tear 2000-         vB
date-change problem, which impacts           compliant. BJ’s is converting      Vfl
fewer than 5% of Berry's programs, "so       other desktop systems and in-        ”
we’re close to being done,” Gladwell         store POS systems itself.
says. Berry runs articles in the monthly        Laferriere figures that BJ’s is not        billion distributor of paper supplies
company newsletter to keep employees         only ahead of its competitors in date         completed an analysis showing that less
up-to-date on its Year 2000 progress.        conversion, but it also has reduced con­      than 5% of its code in affected programs
                                             version expenses 50-60% over standard         required change. The company is now
Killing two birds with one stone             U.S. prices of $ 1.10 to $ 1.50 per line of   conducting a pilot project with two tool
   Datapro Information Services Co., a       code. "A critical part of the project was     vendors and an outsourcer. When the
market research firm in Delran, N.J.,        minimizing our staff’s exposure to long­      project is completed, in the second
has already solved its Year 2000 issue       term, laborious, boring work that is not      quarter, "we will develop a plan to see if
with client/server systems, says Martin      career-enhancing,” he says.                   we can handle this in-house,” said pro­
Levine, director of technology. "With           Cafferelli agrees that a Year 2000         ject director Bob Niedzwiecki.
us, it wasn’t a Year 2000 issue, but an
issue that our business system needed
new functions, so we took care of the                                  How should a CIO who hasn't




                                             I
Year 2000 problem at the same time,”
he says. "We’ve reengineered our sys­               started Y2K repair efforts go into the
tems, not only fixing dates but improv­
ing the system as well.”                                        CEO's office? With resignation in hand.
   The biggest challenge in date con­
version is figuring out how one piece of
code in one program affects one in           solution especially taxes programmers.           Niedzwiecki advises CIOs who
another program. Tracking such ripple        "Programmers tire easily and get slower       haven’t begun Year 2000 plans to con­
effects is a seemingly endless task, since   as the project progresses. It is extremely    duct an impact analysis ... immediately.
testing every branch of every program is     tedious work. They must check to see if       BJ’s CIO Laferriere puts it more
impossible, from the standpoints of          programs fall through the date field.”        bluntly: “Ifyou haven’t already started,
money and time. To relieve its own pro­          United Stationers Supply Co., Inc.        go in with your resignation in hand.” 3
gramming staff of such tedious work,         of Des Plaines, Ill., is currently deciding
BJ’s decided to outsource mainframe          whether it needs to outsource part of its        Anna Tortig i> afreelance writer in Cambridge,
conversion work to ITL-Infosys Tech-         Year 2000 work. In February the $2.3          AfaM., who coeero technology and related ivuco.


                                                                THE YEAR 2000 • A Computerworld Custom Publication                       15


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | y2k-computerworld-aberdeen-psk-irving-19-5bcd20 |
| title | Year 2000 Solutions Series Part 1 — Aberdeen Group lead article + 12-point Best Practices (PSK + Susan Irving + John R. Logan, Computerworld Custom Publication, 1997) |
| author | Peter S. Kastner and Susan L. Irving (lead article); Peter S. Kastner (12-point Best-Practice sidebar); John R. Logan (companion editorial); Anna Tortig and Computerworld Custom Publications staff (case studies) |
| date | 1997-05 |
| type | advertorial-magazine-supplement |
| subject_domain | Y2K-enterprise-IT-management |
| methodology | Aberdeen Group authored the lead article 'How Enterprise Executives Can Play a Pivotal Role in the Year 2000 Solution' and a 12-point 'Year 2000 Best Practice Recommendations' sidebar in a Computerworld special advertising supplement co-sponsored by HP, Data Dimensions (Ardes 2k), and MS Millennium (MSM/2000). Logan contributed a separate editorial 'Year 2000 Issues: Understanding Will Lead to Action.' Case studies of BJ's Wholesale Club, Datapro, and United Stationers complete the Part 1 supplement (Part 2 promised in CW June 2 issue). |
| source_file | Y2K-CW-advertorial-11.pdf |
| license | CC-BY-4.0 |

### Abstract

Kastner is identified as Group Vice President of Aberdeen Group and 'general manager of its commercial systems practice' covering databases, OLTP, decision support, client/server architectures and distributed commercial systems development. PSK and Susan Irving co-author the lead, framing Y2K as 'as much about competitive advantage as it is about technology' and warning that 'tightly integrated, Web-enabled technology infrastructures are becoming the circulatory system of companies.' The 12-point Best Practice Recommendations attributed to Aberdeen include: 'Start immediately!'; 'Stop wounding Year 2000 messengers'; 'Send lawyers, guns and money'; 'Treat this as a war-time effort'; 'Secure trusted outside resources quickly. By mid-1997, there will be little capacity left in the industry'; 'Insist on seeing external partner compliance plans'; 'Beware the Law of Unintended Consequences'; and 'Save the blame for January 1, 2000'. PSK's rolodex of CXO targets (CFO, COO, CIO/CTO, Controller, Board of Directors, CEO) anticipates the modern multi-stakeholder cybersecurity-incident playbook.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | PSK + Irving co-authored Aberdeen lead article and 12-point Best Practices in a national Computerworld Custom Publication — peak-audience Y2K positioning piece for Aberdeen's commercial systems practice in 1997. |
| **Relevance** | high | Documents PSK's 1997 title (Group VP Aberdeen, GM commercial systems practice) and direct content authorship at the height of the Y2K crisis 30 months before the deadline. |
| **Prescience** | high | PSK + Irving's framing of Y2K as a competitive-advantage event affecting shelf-space, asset-base efficiency, and data-mining capability anticipates how 21st-century cybersecurity incidents (e.g., 2017 Equifax, 2021 Colonial Pipeline) are now framed in board rooms. The 'extended enterprise' partner-compliance recommendation (Best Practice #8) anticipates modern third-party / supply-chain cybersecurity audit programs (SOC 2 vendor questionnaires, SBOM mandates). The 'rest, ready and eager' post-2000 SWAT team (#11) anticipates the modern incident-response retainer. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (12)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Peter S. Kastner | person | active |  |
| Aberdeen Group | firm | acquired | Harte-Hanks (2007); Spiceworks Ziff Davis |
| Susan L. Irving | person | active |  |
| John R. Logan | person | active |  |
| Computerworld | publication | active | IDG |
| Hewlett-Packard Company | company | split | Split into HPE + HP Inc. 2015 |
| Data Dimensions, Inc. | company | defunct | Acquired 2000s |
| MS Millennium | company | defunct | Subsidiary of Matlen Silver Group |
| BJ's Wholesale Club, Inc. | company | active |  |
| Datapro Information Services Co. | firm | defunct | Absorbed by Gartner late 1990s |
| United Stationers Supply Co., Inc. | company | active | Now Essendant |
| Financial Accounting Standards Board (FASB) | regulatory-body | active |  |

### Technologies Referenced (6)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Year 2000 (Y2K) date-rollover bug | software-defect-class | industry-wide | active-remediation | remediated |
| MSM/2000 (MS Millennium toolset) | Y2K-tool | MS Millennium | shipping-Y2K-era | deprecated |
| Ardes 2k (Data Dimensions Y2K platform) | Y2K-tool | Data Dimensions Inc. | shipping-Y2K-era | deprecated |
| IBM mainframe (S/370 / S/390 / zSeries) | mainframe | IBM | shipping | shipping |
| Client-server computing architecture | system-architecture | industry-standard | emerging | legacy |
| Three-tier (and 'three-tier plus') architecture | system-architecture | industry-standard | emerging | shipping |

### Observation Summary

- Total observations: 12
- By type: strategic-recommendation: 2, supplier-context: 2, kastner-title: 1, kastner-coverage-scope-1997: 1, co-author-irving: 1, competitive-quote: 1, forecast: 1, market-observation: 1, forecast-deadline: 1, kastner-coauthor-prior-batch-context: 1
