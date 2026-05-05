# The Composite Applications Benchmark Report: How SOA Standards Are Accelerating Business Change

> Archived from: source/_raw_text.txt
> Original publication date: 2006-12
> Author: Rick Saia and Peter S. Kastner, Aberdeen Group

---

## Original Document Text

The Composite Applications Benchmark Report
   How SOA Standards Are Accelerating Business Change




                        December 2006


                  — Underwritten, in Part, by —
                                                              The Composite Applications Benchmark Report




                            Executive Summary



A
         pplication integration is a major IT headache and takes up about 40% of the
         typical IT budget, according to recent Aberdeen research. A typical enterprise’s
         business processes are found in multiple IT applications, and the service-oriented
         architecture (SOA), which can encompass web services as well as the
integration, business logic, and legacy technologies behind it, is seen as the technological
means to solving the application integration problem.
However, that research has found that most organizations have not dived deep enough
into SOA to have one fully implemented. So, they have turned to building composite
applications as fast as they can to deliver more value to line-of-business units, which
always takes higher priority over IT’s ability to deliver changes.
Composite applications contain logic and data collected from multiple IT sources and
harnessed with Web services standards such as XML, SOAP, and WS-*. These
applications are rapidly becoming the development standard of choice in all IT
organizations. However, our research has found that composite applications can be
built and implemented with Web services and SOA standards even if the
organization has yet to fully develop an SOA. This allows IT to respond to the pressure
of delivering more value to the business while helping ease the pains of technological
integration.

Key Business Value Findings
Here are three key findings from our research for this report:
   • Best in Class firms realize the inadequacy of their present development tools and
     are actively investing in new composite development technology.
   • An IT organization that wants to accelerate the delivery of more composite
     applications must invest in more targeted training or use outside IT services.
   • Companies looking to build more composite applications should look first to the
     web. Browser-based and portal applications are the most common first
     deliverables.

Implications & Analysis
The research results also yielded these insights:
Composite applications are delivering on IT business drivers of faster implementation,
business process transformation agility, and lower integration complexity and risk. But
composite application-building is not trivial. As one IT director told us, “ Be prepared
for integration to be more complex for IT, even if it simplifies it for the
business.”
IT shops with Java and Windows .Net can achieve the best ROI and lowest life-cycle
application maintenance costs with cross-platform composite development tools.
   • A common failure is charging ahead in spite of inadequate planning and training.


                               All print and electronic rights are the property of Aberdeen Group © 2006.
                                                                                        Aberdeen Group • i
The Composite Applications Benchmark Report



        Recommendations for Action
        Here are our chief recommendations for all organizations interested in developing and
        delivering composite applications:
            • Proper planning is a critical first step. While modest composite applications can
              be built in skunkworks projects, serious composites involving legacy applications
              and databases require careful consideration. About 15% of survey respondents left
              a lesson learned comment about how they underestimated or short-changed
              rigorous, staged project and technology planning.
            • Start small and grow with experience and confidence. Only a small percentage
              of survey respondents are confident that they can rapidly grasp the considerable
              integration challenges across multiple projects.
            • Invest in targeted training. Plan training around composite infrastructure layers
              such as user interface, message transport, and legacy application wrapping so
              specialists can ramp up experience and deliver quick return on value, Match the
              training activities or outside IT services carefully with the needed staff skills.
            • Bring in professional service partners to assist. One lesson learned from survey
              respondents: “Climbing the composite application technology mountain without an
              IT services guide is risky if not foolhardy,” a medical products executive says.
              And an insurance company executive chimed in that “service provider experienced
              personnel are worth their weight in gold, while the inexperienced are millstones”
            • Invest in the development tools needed for the long term. The design, software
              development, testing, quality assurance, and deployment technology and methods
              that worked with earlier application development methodologies are not optimized
              for building composite applications. Look to Best in Class companies, 65% of
              which are buying new composite application-related technology within the
              next six months. But one chastened financial services executive offered this sage
              advice regarding extensive tool functionality: “Don’t negate the automated code-
              generating capabilities of many modern tools by modifying the generated
              programs. It creates a maintenance nightmare.”




All print and electronic rights are the property of Aberdeen Group © 2006.
ii • Aberdeen Group
                                                                               The Composite Applications Benchmark Report




                                  Table of Contents
     How SOA Standards Are Accelerating Business Change............................... 1

Executive Summary ...............................................................................................i
   Key Business Value Findings ..........................................................................i
   Implications & Analysis ....................................................................................i
   Recommendations for Action.......................................................................... ii

Chapter One: Issue at Hand ................................................................................ 3
   What Are Composite Applications? ............................................................... 3

Chapter Two: Key Business Value Findings......................................................... 6
   Determining the Best in Class ....................................................................... 7
   The Value of Experience and Using the Right Tools ...................................... 8
   The Tools to Get the Job Done ...................................................................... 9
       Web Browser Information Delivery........................................................... 9
       Business Process Modeling ..................................................................... 9
       Legacy Application Modernization.......................................................... 10
       Data Migration and Information as a Service ......................................... 10
       SOA Middleware .................................................................................... 10

Chapter Three: Implications & Analysis............................................................. 12
   Challenges and Responses......................................................................... 14
   Approaches to SOA..................................................................................... 15
   The Landscape by Company Size............................................................... 16

Chapter Four: Recommendations for Action ...................................................... 17
   Best in Class Next Steps ............................................................................. 18
   Industry Average Steps to Success ............................................................. 18
   Laggard Steps to Success........................................................................... 19

Featured Underwriters ....................................................................................... 20

Appendix A: Research Methodology .................................................................. 21




                                      All print and electronic rights are the property of Aberdeen Group © 2006.
                                                                                              Aberdeen Group • 1
The Composite Applications Benchmark Report




                                                                            Figures

            Figure 1: Business Drivers for Building Composite Applications
            as Top Priority ....................................................................................................................... 4

            Figure 2: Desired Technology Outcomes from Composite Applications................................. 4

            Figure 3: Benefits from Developing and Deploying Composite Applications.......................... 6

            Figure 4: Percentage of Companies That Have Delivered
            Specific Composite Applications .......................................................................................... 10

            Figure 5: Companies That Have or Are Planning
            SOA Middleware Products ................................................................................................... 11

            Figure 6: Approaches to SOA and ROI Generated
            from Composite Applications ............................................................................................... 15

            Figure 7: Organizations Investing in
            Enterprise Service Bus (ESB) Middleware .......................................................................... 16


                                                                        Tables

            Table 1: Competitive Framework for Building Composite Applications .................................. 7

            Table 2: Organization Confidence in Building Composite Applications .................................. 8

            Table 3: Top Business and IT Drivers for Composite Applications ....................................... 12

            Table 4: PACE (Pressures, Actions, Capabilities, Enablers) ................................................ 13

            Table 5: Composite Application Development Challenges and Responses ......................... 14

            Table 6: PACE Framework ................................................................................................... 22

            Table 7: Relationship between PACE and Competitive Framework ..................................... 22




All print and electronic rights are the property of Aberdeen Group © 2006.
2 • AberdeenGroup
                                                                           The Composite Applications Benchmark Report




                                               Chapter One:
                                              Issue at Hand

                • Enterprises are trying to develop and deploy applications that deliver value to the
                  business while dealing with the costs and headaches that come with IT integration.
Key Takeaways




                • Although composite applications are believed to go hand-in-hand with a service-oriented
                  architecture, many IT groups are building them first with web services to respond to the
                  delivery pressures from the business units.
                • The chief technological goal of composite applications is to help simplify the IT
                  infrastructure and allow for quicker and easier platform consolidation.




R
        ecent Aberdeen research has shown that application development and integration
        is a major IT headache, costing around 40% of the typical IT budget in a $1.3
        trillion global IT economy. A typical enterprise’s business processes are found in
        multiple IT applications, and the service-oriented architecture (SOA), which
includes web services, is seen as the technological means to solving the application
integration problem.
However, that research – of more than 2,000 companies over the past year – has found
that most organizations have not waded deep enough into the SOA “pool” to have a full
SOA in place. So, they have turned to building composite applications as fast as they can
to deliver more value to the line-of-business, which always takes higher priority over IT’s
ability to deliver changes.

What Are Composite Applications?
Composite applications contain logic and data collected from multiple IT sources and
harnessed with web services standards such as XML, SOAP, and WS-*. These
applications are rapidly becoming the development standard of choice in all IT
organizations.
Wikipedia defines a composite application as one “built by combining multiple services”
consisting of “functionality drawn from several different sources within” an SOA to
functionality, we would add data, since information management is critical to all
enterprise applications. But our research yields a more practical conclusion: Composite
applications can be built and implemented even if the organization has yet to fully
develop an SOA.
Why? To respond to the pressure of delivering more value to the business while
helping ease the pains of technological integration.
The research conducted for this report has borne out our definition. The top business
driver, or pressure, pushing composite applications to the front of the development
priority line is improving service to end users (Figure 1). And the chief technology
outcomes organizations are seeking? Simpler integration with the technology
infrastructure and a key to easier and faster platform consolidation (Figure 2).



                                           All print and electronic rights are the property of Aberdeen Group © 2006.
                                                                                                   Aberdeen Group • 3
The Composite Applications Benchmark Report



        Figure 1: Business Drivers for Building Composite Applications as Top Priority



                        Improve service to end users                                                 63%



           Reduce operating costs (including labor)                                            56%



              Simplify IT infrastructure and platforms                                   48%



                          Improve sales and revenue                          31%


                                                         0%   10%   20%   30%   40%    50%     60%    70%


                                                                       Source: Aberdeen Group, November 2006

        Figure 2: Desired Technology Outcomes from Composite Applications


            70%
                                                                                           60%
            60%
                                                                     49%
            50%           43%
                                                40%
            40%

            30%

            20%

            10%

             0%
                      Improved user       Replacement of       Allows easier and Simplify integration
                    interface for older   older integration     faster platform   with technology
                           apps               software           consolidation      infrastructure
                                             technology


                                                                       Source: Aberdeen Group, November 2006

        Our hypothesis for this report was that the IT norm for creating composite applications is
        creating “an application built by combining functionality and data drawn from several
        different sources, using web services within a SOA.” In other words, SOA standards such
        as XML, SOAP, and WS-* are allowing much more cost- and time-effective application
        integration than older approaches do, with better user interfaces, so that the ultimate goal




All print and electronic rights are the property of Aberdeen Group © 2006.
4 • AberdeenGroup
                                                              The Composite Applications Benchmark Report



of a full-blown SOA in which all applications are parts of services, is, rather, a secondary
goal.
Our survey for this report proved the hypothesis correct. Only 31% of respondents
identified building out their services architecture plans as a key technology outcome
their companies sought from building composite applications.
So, our first question to the Global 5000 for this report is: How do composite
applications, created with web services, fit into an overall services-oriented architecture,
and when will these composites be integrated into the long-term SOA for the
organization?       Our
                                              Competitive Framework Key
next questions focus
on how enterprises are The Aberdeen Competitive Framework defines enterprises as falling
choosing           their into one of the three following levels of practices and performance:
approaches, and what
                          Best in Class (20%) —practices that are the best currently being
factors, drivers, and employed and significantly superior to the industry norm
challenges distinguish
successful                Industry Average (50%) —practices that represent the average or
organizations from the norm
not so successful. In Laggards (30%) —practices that are significantly behind the average
the next two chapters, of the industry
we’ll     offer      the
answers and elaborate
on them. We will also detail how leading, that is, Best in Class, companies are facing the
issue of building composite applications, and how their approaches lead them to perform
better than Industry Average and Laggard companies within Aberdeen’s Competitive
Framework.




                               All print and electronic rights are the property of Aberdeen Group © 2006.
                                                                                       Aberdeen Group • 5
The Composite Applications Benchmark Report




                                                   Chapter Two:
                                            Key Business Value Findings

                             • Best in Class firms realize the inadequacy of their present development tools and are
        Key Takeaways




                               actively investing in new composite development technology.
                             • An IT organization that wants to accelerate the delivery of more composite applications
                               needs to invest in more targeted training or use outside IT services.
                             • Companies looking to build more composite applications should look to the web first.
                               Browser-based and portal applications dominate work that has been done so far.




        A
                 berdeen estimates that the average Global 1000 enterprise has produced 1.5
                 billion lines of program code over the past 30 years at a 2006 replacement cost of
                 $75 billion. The business focus for any organization should be on optimizing the
                 processes that make it unique, such as customer satisfaction, service delivery,
        low-cost supply, and fast delivery. Most enterprises are doing this by decomposing
        business processes into services under the guise of SOA technology, which is proving to
        lower life-cycle costs while improving agility.
        Aberdeen’s executive-level readers tell us that, working with an SOA mindset, teams of
        business users and IT technicians can readily identify the business process inefficiencies
        that will deliver a fast or large payback. According to the survey results for this report, IT
        practitioners are finding they can keep up with line-of-business agility and change
        requirements better by moving to an SOA-based approach using composite applications.
        In Figure 3, note that higher user satisfaction and quicker business reaction rate
        considerably higher than improving IT or merely lowering costs.



                60%
                                  51% 52%                 48%         All Respondents           48%
                50%                                                   Best in Class
                                                    41%
                                                                                                                   38%
                40%
                                                                                          28%
                30%                                                    25% 24%                               22%
                20%
                10%
                        0%
                                 Higher user     Quicker reaction     Improved IT        Lower costs         Improved
                                 satisfaction   by the business to   operations and                         application
                                                    competitive        processes                           performance
                                                     pressures

        Figure 3: Benefits from Developing and Deploying Composite Applications
                                                                                        Source: Aberdeen Group, November 2006

        Best in Class organizations scored higher than the average in most of these five
        categories, which demonstrates that while they recognize the impact composite


All print and electronic rights are the property of Aberdeen Group © 2006.
6 • AberdeenGroup
                                                                  The Composite Applications Benchmark Report



applications can have on the business, they’re also much more adept at lowering costs
while simultaneously achieving other goals. Also note that Best in Class organizations
have governance processes in place to focus on line-of-business user satisfaction.
Table 1 shows the distinctions between the Best in Class, Industry Average, and Laggard
organizations in this survey.
Table 1: Competitive Framework for Building Composite Applications
                 Best in Class                Industry Average               Laggards
Process         Overwhelming emphasis        Strong emphasis on             Strong emphasis on
                on application’s             application’s importance       application’s importance
                importance to the            to the business in             to the business in
                business in prioritizing     prioritizing composite         prioritizing composite
                composite application        application development;       application development;
                development; strong          weaker but still strong        half place strong
                emphasis on planned ROI      emphasis on planned ROI        emphasis on planned
                                                                            ROI
Organization    Most designate either        Don’t have top priority for    Don’t have top priority for
                supply chain/B2B or          development, though            development, though
                customer service/e-          strong minorities favor        strong minorities favor
                commerce apps as first       customer service/e-            customer service/e-
                priority for building        commerce and supply            commerce and supply
                composite applications       chain/B2B applications         chain/B2B applications
Knowledge       Most are trained,            Most have multiple-            Little to no experience
                experienced, and             project experience but         and confidence to build
                confident in project-level   lack confidence or             serious composite
                budget and schedule          sufficient training, or miss   applications and/or
                estimates based on           budgets and schedules          routinely meet budgets
                experience gained on                                        and schedules
                multiple composite
                projects
Technology      MIDDLEWARE: Most use         MIDDLEWARE: Most use           MIDDLEWARE: Most use
                Enterprise Service Bus;      Enterprise Service Bus;        Enterprise Service Bus,
                many, but not most, use      many, but not most, use        but close to one-third are
                SOA security, governance,    SOA security, and              not planning to have any
                and management products      repository/registry            SOA middleware
                APPS DELIVERED:              APPS DELIVERED: Most           APPS DELIVERED: Most
                Nearly all have delivered    have delivered portal and      have delivered portal and
                portal and browser-based     browser-based                  browser-based
                applications                 applications                   applications
                                                                Source: Aberdeen Group, November 2006


Determining the Best in Class
For this report, Aberdeen determined its Best in Class organizations as the best 20% of
the survey population with the following quantitative and qualitative characteristics:



                                All print and electronic rights are the property of Aberdeen Group © 2006.
                                                                                        Aberdeen Group • 7
The Composite Applications Benchmark Report



             •   TIME. They can build a typical composite application in three months or less
                 (Industry Average: 3 to 9 months; Laggards: more than 9 months);
             •   NUMBER OF APPLICATIONS. They have delivered more than 11 composite
                 applications (Industry Average: 3 to 10; Laggards: Two or fewer);
             •   ROI. They have achieved greater than 25% ROI by building composite
                 applications (Industry Average: 11-25; Laggards: 10% or less).
             •   EXPERIENCE. Their IT organizations have more training, experience, and
                 confidence in project-level budget and schedule estimates based on multiple
                 composite projects.

        The Value of Experience and Using the Right Tools
        Nearly three-quarters of respondents from Best in Class organizations (71%) have the
        best possible experience level in building composite applications, compared with just
        21% of the entire survey pool (Table 2). This is not surprising given that most
        organizations are still learning about composite applications. In fact, most of those who
        selected this answer cited these three key growing pains in becoming more adept at
        composite applications:
             •   Only key staffers are able to lead composite projects. This highlights a need
                 for more training to enable more of the programming staff to complete projects.
             •   Composite technology and investments could be improved, which points to
                 the relative immaturity of tools IT programmers use today to aid in building and
                 developing composite applications, or the lack of investment in composite
                 technology. However, Best in Class organizations are a step ahead here: Nearly
                 two-thirds (65%) of the Best in Class plan to buy new composite application-
                 building technology in the next six months, versus only 25% of other
                 responding companies.
             •   Difficulty in testing and deployment stages of development, which implies
                 process immaturity. It also points to the unavoidable complexity that can lurk
                 behind glitzy web screens, causing unforeseen testing and performance issues.

        Table 2: Organization Confidence in Building Composite Applications
                                          Statement                                    % Who Answered
        Some experience but lack experience and confidence to routinely meet budgets        22%
        and schedules
        Trained, experienced, and confident in project-level budget and schedule            21%
        estimates based on multiple composite projects
        Multiple project experience but miss budgets and schedules                          16%
        Could use more training                                                             16%
        Lack experience and confidence to build serious composite applications              15%
        Multiple project experience but lack confidence                                     10%



All print and electronic rights are the property of Aberdeen Group © 2006.
8 • AberdeenGroup
                                                             The Composite Applications Benchmark Report



                                                           Source: Aberdeen Group, November 2006


The Tools to Get the Job Done
Before starting to build enterprise applications, wise enterprises are rebuilding their
development methodologies — and often their development organizations. At 15 million
lines of code per average enterprise application, thousands of applications per enterprise,
and programmer productivity around 10 lines of debugged code per man-day with the
third-generation tools (e.g., C ++) most organizations are using, simple arithmetic says
we will not, in our lifetimes, rewrite the existing applications with today’s approaches.
Even offshoring the work will cost billions and result in huge test and deployment costs.
It’s not feasible unless the development technology changes.
While early progress can be made with a variety of SOA developer tools and
infrastructure middleware, the long-term development environment will involve these
five planned investments in technology and people skills: Web browser information
delivery, business process modeling, legacy application modernization, data migration
and information as a service, and SOA middleware: tying composite applications into
an enterprise SOA infrastructure.
Not investing in these five technologies will reduce the opportunity-payback curve
significantly over the next decade. Here are some key survey results for two of those
technologies.
Web Browser Information Delivery
Looking back a decade, the industry has come a long way from hand-coded HTML. The
browser is now the common denominator for delivering application functionality, and
most companies represented in the Aberdeen survey are already building and delivering
composite browser-based and portal applications, much more so than non browser-based
applications (Figure 4).
Portal technology enhances the “have it your way” user experience. For web application
developer productivity as well as user experience satisfaction, modern browser-based
application tools are essential.
Business Process Modeling
One of the biggest reasons for high enterprise integration costs over time is the fact that
the logic and rules for business processes are locked inside the source program code
itself. Changes require an analyst to document the process change, a programmer to
change the program, and a QA team to test that the changes did what the analyst wanted
and didn’t induce errors. With BPM, users and analysts can model the rules, data flow,
human and system interactions that make up a business process, often without a change-
order to IT. Life-cycle costs and cycle times are dramatically reduced because changing
the process means changing the model with a graphical tool.
Moving frequently changed business rules and parameters out to line-of-business control
under a BPM is an important step in unlocking long-term value while enhancing IT
agility.




                              All print and electronic rights are the property of Aberdeen Group © 2006.
                                                                                      Aberdeen Group • 9
The Composite Applications Benchmark Report



        Figure 4: Percentage of Companies That Have Delivered
        Specific Composite Applications



                        Browser-based applications                                              67%



                                  Portal applications                                      59%


             Background integration processes (no
                                                                             32%
                            GUI)


           Custom and ISV enterprise applications
                                                                         28%
                     (i.e., ERP, CRM)

                                                        0% 10% 20% 30% 40% 50% 60% 70% 80%


                                                                       Source: Aberdeen Group, November 2006

        Legacy Application Modernization
        Our recent study on Legacy Application Modernization shows the majority of IT
        practitioners are extending and surrounding enterprise applications with SOA
        middleware, preferring to leave those applications largely intact while incorporating the
        SOA glue that allows those applications to become part of a composite application or
        service. However, many companies are using the SOA “technology changeover” to
        modernize the application itself using automated technology to extract the logic and data
        for migration to a new software technology base.
        Data Migration and Information as a Service
        Aberdeen research consistently shows data migration as a challenge that IT practitioners
        underestimate. The SOA application makeover creates the opportunity to move off older
        databases and consolidate databases around SOA services. Simply put, enterprise data
        also needs to be extracted from applications and databases and presented to SOA services
        as the reliable data of record. Master data management and other computer science
        concepts are reducing duplicative data and making it more widely available for analysis
        and computing. In short, data migration technology has many advantages over the
        traditional, in-house data conversion and migration project-task approach.
        SOA Middleware
        Aberdeen’s prior SOA research indicated that the market recognizes SOA infrastructure
        middleware as a necessary and early investment. Companies represented in this study
        recognize that too. However, as in our prior research, we found there are three distinct
        approaches to SOA. One group embraces Web services but not SOA middleware. A
        second group (Figure 5) is building out an SOA infrastructure with middleware products,
        while the third group is using ERP vendors’ SOA middleware. We discuss these three
        approaches further in Chapter 3.


All print and electronic rights are the property of Aberdeen Group © 2006.
10 • AberdeenGroup
                                                                                    The Composite Applications Benchmark Report



Figure 5: SOA Middleware Products That Companies Have or Are Planning

60%         56%

50%
                               40%
40%                                                34%
                                                                                  28%
30%                                                                25%
                                                                                                                  22%
20%                                                                                                15%

10%

 0%
      Enterprise Service Repository/registry    SOA security   SOA governance SOA management   SOA hardw are   None planned
          Bus (ESB)                                                                             accelerators


                                                                                 Source: Aberdeen Group, November 2006

Best in Class enterprises identified in previous studies are installing certain suites of SOA
capabilities that are mandatory in the long run but can be skipped on a single project:
registry/repository, enterprise service bus, security, management, and governance. Given
that the objective is to reduce the 40% of IT budget spent on integration, we are confident
that the early investments in entire suites of SOA management and operational
capabilities will be recovered quickly, and at the lowest life-cycle costs.
A majority of organizations interested in integrating their composite applications
immediately into SOA middleware suites are using Java-based development toolsets such
as the Eclipse interactive development environment (IDE), third-party Java tools, and
cross-platform development tools that generate Java and Windows code.
Orchestrating the pieces of composite applications into manageable services that pass IT
governance muster requires enterprise-class middleware that supports SOA standards and
becomes the organization’s long-term infrastructure.




                                               All print and electronic rights are the property of Aberdeen Group © 2006.
                                                                                                      Aberdeen Group • 11
The Composite Applications Benchmark Report




                                                 Chapter Three:
                                            Implications & Analysis

                         •   Composite applications are delivering on IT business drivers of faster implementations,
        Key Takeaways




                             business process transformation agility, and lower integration complexity and risk.
                         •   IT shops with Java and Windows .Net can achieve the best ROI and lowest life-cycle
                             application maintenance costs with cross-platform composite development tools.
                         •   A common failure is charging ahead with inadequate planning and training.




        I   n Chapter One, we addressed the business reasons that make composite applications
            an IT priority. We also asked respondents to identify the IT business drivers and
            found a strong correlation between the two groups (Table 3). This signals a high level
            of business-IT alignment on the key issues affecting the business that would lead to
        the development of composite applications.
        Table 3: Top Business and IT Drivers for Composite Applications
                        Business Reasons           % Selected               IT Business Drivers             % Selected
         Improve service to end users                 63%             Need for faster implementations          52%
                                                                      (i.e., time to delivery)
         Reduce operating costs                       56%             Business process transformation          52%
         (including labor)
         Simplify IT                                  48%             Lower integration complexity             43%
         infrastructure/platforms                                     and risk
         Improve sales and revenue                    31%             Simplify IT software infrastructure      34%
                                                                      and/or applications
                                                                                  Source: Aberdeen Group, November 2006

        The predominant strategies,
        or actions, along with the                  PACE Key — For more detailed description, see Appendix A
        internal        capabilities                Aberdeen applies a methodology to benchmark research that evaluates
        (process competencies) and                  the business pressures, actions, capabilities, and enablers (PACE) that
                                                    indicate corporate behavior in specific business processes. These terms
        technological enablers, are                 are defined as follows:
        detailed in Table 4 as part
                                                    Pressures — external forces that impact an organization’s market
        of     Aberdeen’s    PACE
                                                    position, competitiveness, or business operations
        framework (See PACE
                                                    Actions — the strategic approaches an organization takes in response
        Key). Just as encouraging
                                                    to industry pressures
        as the alignment on drivers
        is organizations’ emphasis                  Capabilities — the business process competencies required to execute
                                                    corporate strategy
        on strategic actions; 80%
        prioritize development on                   Enablers — the key functionality of technology solutions required to
                                                    support the organization’s enabling business practices
        applications’ importance to
        the business. This came in


All print and electronic rights are the property of Aberdeen Group © 2006.
12 • AberdeenGroup
                                                                  The Composite Applications Benchmark Report



far ahead of the second most popular strategic action, prioritizing based on planned ROI
(59%).
Table 4: PACE (Pressures, Actions, Capabilities, Enablers)

Prioritized                                     Prioritized                  Prioritized
Pressures          Prioritized Actions          Capabilities                 Enablers
Improve service Prioritize applications to      Adequate training and        Enterprise Service Bus
to end users    be developed by their           experience to meet project   and SOA middleware
                   importance to the            milestones; use of outside
                                                                             Third-party
                   business (cited by 80%       IT services to help
                                                                             development tools that
                   of survey respondents)       programming teams
                                                                             generate Java code
Reduce             Prioritize applications to   Adequate training and        Repository/registry
operating costs    be developed by their        experience to meet project   middleware
(including         planned ROI; measure         budget milestones;
                                                                             Third-party application
labor)             programmer productivity      outsource some composite
                                                                             development tools that
                                                development
                                                                             generate Java and
                                                                             Windows code from a
                                                                             single program source
Simplify IT        Prioritize applications to   Adequate training and        SOA security
infrastructure/    be developed through a       experience to meet project   middleware
platforms          risk/reward evaluation;      milestones; use of IT
                                                                             Eclipse IDE and third-
                   consider development         services to help design
                                                                             party Eclipse plug-ins
                   tool and platform            teams or assist in data
                   consolidation                migrations, conversions,
                                                or SOA installations
Improve sales      Prioritize applications to   Adequate training and        SOA governance
and revenue        be developed according       experience to meet project   middleware
                   to most amount of effort     milestones; use of IT
                                                                             Third-party
                   required; consider how       services to help in needed
                                                                             development tools that
                   web services can             areas, such as design,
                                                                             generate Windows
                   improve customer             programming, training, or
                                                                             code
                   satisfaction levels          project management
Competitive        Prioritize applications to   Adequate training,           SOA management
pressures (cited   be developed according       experience, and              middleware
by 24% of          to least amount of effort    confidence to meet tight
                                                                             Traditional 3GL
respondents)       required                     project deadlines; use of
                                                                             development tools
                                                IT services to help in
                                                areas to facilitate
                                                development and
                                                installation
                                                                Source: Aberdeen Group, November 2006

This supports a key finding from our recent Legacy Application Modernization
Benchmark Report, in which we found that Best in Class organizations had strong
enterprise-wide buy-in for SOA. The upshot here is that composite application



                                 All print and electronic rights are the property of Aberdeen Group © 2006.
                                                                                        Aberdeen Group • 13
The Composite Applications Benchmark Report



        development, since it’s linked with SOA, requires an organization-wide commitment,
        especially because of the extent of its impact.

        While the IT organization must clearly communicate the changes an SOA or composite
        application will bring and the value it can deliver, the line-of-business units must be fully
        aware of how it can work for the benefit of the entire business, especially in how it can
        facilitate the flow of information between services, or facilitate workflow.

        Challenges and Responses
        The top challenges respondents said their companies experience are linked tightly to the
        immaturity of the market for composite application development tools and the need for
        more expertise (Table 5). There is little wonder, then, that each of the top five responses
        to the challenges can be linked to those technological and skills challenges.

        Table 5: Composite Application Development Challenges and Responses
                Challenges             % Selected            Responses to Challenges              % Selected
        Required more technical               58%         Learned by experience; challenges         46%
        education or support than                         were not severe
        planned
        Composite application                 53%         Contracted for outside IT services or     40%
        development tools                                 outsourced the project
        Missed schedules                      38%         Expanded training and/or raised           38%
                                                          qualifications of staff
        Over budget                           30%         Bought new composite application-         34%
                                                          building technology
        Standards-based code did not          28%         Slowed our SOA implementation             28%
        work as planned                                   efforts until challenges overcome
                                                                       Source: Aberdeen Group, November 2006

        Our research shows enterprises are not building alone. More than three-quarters ─
        76% ─ are engaging outside services, with most either outsourcing some composite
        development work or assisting the programming teams. This dovetails with previous
        research on SOA and application development, in which Aberdeen found that enterprises
        are engaging outside services to install and tune the SOA infrastructure, look at the
        transformation opportunities SOA technology can enable, and transfer skills by working
        alongside internal IT teams.
        Outsourcing development work can also be a shrewd use of cash. In our recent
        benchmark report, Outsourcing Application Development and Maintenance, we found
        that Best in Class organizations are achieving better than a 50% ROI in outsourced
        application development and maintenance (However, outsourcing carries a different set
        of challenges and key performance measures, and requires special management skills that
        many firms admittedly lack, according to Aberdeen research findings).




All print and electronic rights are the property of Aberdeen Group © 2006.
14 • AberdeenGroup
                                                             The Composite Applications Benchmark Report




Approaches to SOA
Earlier this year, an Aberdeen benchmark report, Enterprise Service Bus: An SOA
Middleware Foundation, found users split into three technology camps in adopting
SOAs:
    •    SOA Lite, which is for users that are primarily deploying web services that do
         not require mission-critical capabilities such as high-volume scalability, high
         availability and failover, management, governance, and security;
    •    SOA ERP, which is used by companies that are choosing to deploy SOA
         surrounding their ERP application software; and
    •    Enterprise SOA, which requires and uses mission-critical SOA middleware
         capabilities.
This benchmark found that most organizations opt for SOA Lite or Enterprise SOA. But
half of those taking the SOA ERP route are generating more than 10% ROI from their
composite application implementations, while 55% of Enterprise SOA organizations are
getting double-digit payback (Figure 6). While SOA Lite remains the most popular
approach (with the least effort), less than half the companies in the survey that are using
SOA Lite are returning more than 10% on their investments. This finding indicates that
there is a higher return for organizations that take the two more involved approaches.
Figure 6: Approaches to SOA and ROI Generated from Composite Applications

                  % of Companies Using

   60%            % of Companies Generating        55%
                  More Than 10% ROI                                             50%
   50%                  45%
                 43%
   40%                                     36%

   30%
                                                                        21%
   20%

   10%

    0%
                  SOA Lite               Enterprise SOA                  SOA ERP

                                                           Source: Aberdeen Group, November 2006

Not surprisingly, 71% of companies using SOA ERP are manufacturers, which are more
likely to use ERP software to help run their businesses.




                              All print and electronic rights are the property of Aberdeen Group © 2006.
                                                                                     Aberdeen Group • 15
The Composite Applications Benchmark Report



        The Landscape by Company Size
        The survey’s response pool was close to evenly distributed by company size, but the
        story lines between the three groups (large company: at least $1 billion in annual
        revenue; mid-size: $50 million to $1 billion; small: up to $50 million) reveal some
        interesting differences. For instance:
            • Half of large companies take the Enterprise SOA approach while 53% of small
              organizations prefer SOA Lite, which is not a surprise given the resource
              constraints that are endemic among small companies.
            • Nearly two-thirds (64%) of large companies cite a need for faster
              implementations as a key IT business driver in building composite applications,
              compared with 45% of mid-size enterprises and 47% of small organizations.
            • While only 32% of companies are building composite applications to extend the
              life of their legacy applications and assets, 48% of mid-market companies cited
              this, an indication that most are reluctant to invest more than they have to in
              upgrading their infrastructures.
            • Most large and mid-size organizations have implemented or are planning to install
              enterprise service bus (ESB) middleware (Figure 7).

        Figure 7: Organizations Investing in Enterprise Service Bus (ESB) Middleware



                  Large                                                                   71%




               Mid-Size                                                         60%




                  Small                                     37%



                          0%     10%      20%     30%      40%      50%      60%      70%       80%

                                                                      Source: Aberdeen Group, November 2006




All print and electronic rights are the property of Aberdeen Group © 2006.
16 • AberdeenGroup
                                                                           The Composite Applications Benchmark Report




                                      Chapter Four:
                                Recommendations for Action

                  •   To become even better, Best in Class organizations must build the experience level of
Key Takeaways




                      their IT staff through training and via the expertise of services partners.
                  •   Industry Average firms should focus much of their development on one or two critical
                      business processes to help maximize ROI while boosting development expertise.
                  •   Laggards need to focus most heavily on IT training, and place a stronger emphasis on
                      increasing user satisfaction and business success.




C
        omposite applications are helping companies fill pressing IT needs while they
        inch toward fulfilling their entire SOA strategies. Certainly, responding to
        competitive pressures in a global business climate fueled by information requires
        quick decision-making that can be hampered by a lack of adequate, state-of-the-
art technology. Indeed, Best in Class organizations recognize this, which is why they are
more likely to target composite application development at supply chain and customer-
facing functions.
This report has highlighted the keys to success for composite application development, as
well as the factors that hinder success. Our research has borne out these factors that are
critical to improved composite application development and delivery:
                • Proper planning is a critical first step. While modest composite applications can
                  be built in skunkworks projects, serious composites involving legacy applications
                  and databases require careful consideration.
                • Start small and grow with experience and confidence. Only a small percentage
                  of survey respondents are confident that they can rapidly grasp the considerable
                  integration challenges across multiple projects. And they are challenged with too
                  few trained staff.
                • Invest in targeted training. Plan training around composite infrastructure layers
                  such as user interface, message transport, and legacy application wrapping so that
                  specialists can ramp up experience and deliver quick return on value. This training
                  strategy implies matching the training activities and/or outside IT services
                  carefully with the needed staff skills.
                • Bring in professional service partners to assist in the effort. One lesson learned
                  from survey respondents is: “Climbing the composite application technology
                  mountain without an IT services guide is risky if not foolhardy,” as one medical
                  products executive told us.
                • Invest in the development tools needed for the long term. One key finding is
                  that the design, software development, testing, quality assurance, and deployment
                  technology and methods that worked with earlier application development
                  methodologies are not optimized for composite application development. Look to



                                           All print and electronic rights are the property of Aberdeen Group © 2006.
                                                                                                  Aberdeen Group • 17
The Composite Applications Benchmark Report



                the Best in Class companies, 65% of which are buying new composite application-
                related technology within the next six months.
        Here are our recommendations for companies in any of the three groups of the Aberdeen
        Competitive Framework for building composite applications.

        Best in Class Next Steps
             1) Build the experience level of IT staff.
                 Maintain or increase investment in IT developer training and encourage project
                 “post mortems” to document lessons learned that can benefit operations for
                 future development projects. Use these lessons to help develop and modify a
                 “project playbook.” As outlined above, implement a technology role-based
                 training program.
             2) Keep the focus on the application’s importance to the business.
                 The Best in Class adhere to this more than the Industry Average and Laggard
                 organizations. Since they’re twice as likely to recognize competitive pressures as
                 a driver for composite applications, they need to maintain or increase their
                 knowledge of the issues affecting their companies’ market positions. More
                 experience and training for developers can only enhance their ability to deliver
                 within a tight timeframe. Also, each composite project should add to the build-
                 out of the organization’s SOA strategy.
             3) Professional services partners can help.
                 Best in Class organizations were the least likely of the three Competitive
                 Framework groups to bring in outside help to enhance internal composite
                 application development skills. But if a services partner can do some of the work
                 while allowing IT staff to learn from them, that lessens the chance that you’ll
                 need to keep bringing them back for subsequent projects, which will boost
                 project ROI. This is especially important in small and mid-sized companies with
                 limited depth of Web services and SOA specialist skills.

        Industry Average Steps to Success
             1) Build the skills of the IT staff to shorten time to deployment.
                 Industry Average companies take, on average, about twice as long as the Best in
                 Class to complete a composite application project. Building experience through
                 organizational orientation toward composite-building specialists, increased
                 training, or small projects can help improve project delivery and allow IT to take
                 on bigger and more critical projects.
             2) Target specific business processes rather than take a “random” approach.
                 Unlike Best in Class firms represented in the Aberdeen survey, Industry Average
                 and Laggard companies are more likely to develop composite applications for
                 many business processes. To build success, focus on one or two process areas
                 that can provide the biggest boost for end-to-end process improvement within a
                 process area. By building out a business area in quick succession, staff re-



All print and electronic rights are the property of Aberdeen Group © 2006.
18 • AberdeenGroup
                                                           The Composite Applications Benchmark Report



      familiarization will be lower and code re-use will be higher, lowering project and
      overall costs.
  3) Look to IT service providers for help.
      Most Industry Average organizations rely on professional service partners to
      supplement the IT staff in such critical development functions as design,
      programming, legacy modernization, and data migration. Lean toward a service
      provider that can help boost the skill level of your IT staff.

Laggard Steps to Success
  1) Invest in targeted IT training.
      Only 16% of Laggard companies say they have multiple project experience. This
      is a red flag for their IT groups as well as the rest of these organizations.
      Laggards would be best off engaging in small projects that can gradually lift the
      experience and confidence levels of their development groups. Interesting
      statistics from the survey: 65% of Laggards said implementing composite
      applications required more technical education or support than they had planned.
  2) Keep the focus on SOA.
      Alarmingly, 39% of Laggard organizations said challenges in their composite
      application work slowed their SOA implementation efforts. But higher
      percentages said they learned from experience and brought in IT services
      providers to assist in their efforts. Up-skilling the IT staff can help keep both
      composite application projects and SOA strategies on track. Taking your eye off
      the SOA ball can only further delay reaping the benefits SOA can bring.
  3) Place business success and end-user happiness at the top of the priority list.
      Most Best in Class and Industry Average companies cited higher user
      satisfaction and quicker enterprise reaction to competitive pressures as benefits
      from composite application development. Laggards need to maintain that focus if
      they are to boost their competitiveness. Happiness is not just “warm fuzzies.”
      One interviewee told us that composite application development projects drove
      considerably higher end-user productivity, especially by re-working screens and
      transaction workflow for repetitive tasks.




                            All print and electronic rights are the property of Aberdeen Group © 2006.
                                                                                   Aberdeen Group • 19
The Composite Applications Benchmark Report




                                    Featured Underwriters

        This research report was made possible, in part, with the financial support of our
        underwriters. These organizations share Aberdeen’s vision of bringing fact based
        research to corporations worldwide at little or no cost. Underwriters have no editorial or
        research rights and the facts and analysis of this report remain an exclusive production
        and product of Aberdeen Group.




                                  iTKO, Inc. offers a complete software suite for testing Service-
        Oriented Architectures (SOA). iTKO's mission is to allow everyone involved in IT to
        own Complete, Collaborative, and Continuous software quality. iTKO LISA TM Complete
        SOA Test Platform performs unit, functional, regression, load and performance tests,
        without requiring test coding or script maintenance, saving development and QA teams
        effort while improving quality at every phase of development and deployment. LISA
        provides live interaction with web apps, web services, J2EE, .NET, Java objects, ESB,
        databases, and many more technologies. Founded in 1999, the Dallas-based company's
        customers include Sun, Capgemini, Cardinal Health, AMD, TIBCO, and i2.
        For additional information on iTKO:
        1505 LBJ Freeway, Suite 250; Dallas, TX 75234
        1-877-289-4856 or info@itko.com
        http://www.itko.com




                                            Nexaweb’s Enterprise Web 2.0 solutions enable
        enterprises to rapidly deploy Richer, Thinner, Faster applications over the Web.
        Specifically, applications built with Nexaweb deliver the high performance and robust
        functionality of client/server software with the universal reach, no-install deployment and
        centralized management of browser-based applications. With Nexaweb, building
        enterprise-strength RIA solutions using Ajax and Java UI applications that access legacy
        and service-oriented data systems is simple. And because it’s done in a unified
        declarative XML development environment, it doesn’t require re-writing code. Only
        Nexaweb’s comprehensive Enterprise Web 2.0 solutions are backed by an established
        methodology and reference architecture proven by more than 5,000 successful global
        deployments.
        For additional information on Nexaweb:
        One Van de Graaff Drive; Burlington, MA 01803
        781-345-5500 or (fax) 781-345-5501, or info@nexaweb.com
        http://www.nexaweb.com




All print and electronic rights are the property of Aberdeen Group © 2006.
20 • AberdeenGroup
                                                             The Composite Applications Benchmark Report




                              Appendix A:
                         Research Methodology



F
        rom October to December 2006, Aberdeen Group examined the services parts
        management procedures, experiences, and intentions of nearly 135 enterprises in
        the a variety of industries, most from the manufacturing and services sectors.
Responding executives, directors, and managers completed an online survey that
included questions designed to determine the following:
    •    Organization experience with developing composite applications;
    •    The business and IT factors driving composite application development; and
    •    The key performance indicators (KPIs) that separated leading, or Best in Class,
         companies from others in composite application development.
Aberdeen supplemented this online survey effort with telephone interviews with select
survey respondents, gathering additional information on composite application
development strategies, experiences, and results.
The study aimed to identify emerging best practices for developing and delivering
composite applications and provide a framework by which readers could assess their own
composite application development capabilities.
Responding enterprises included the following:
•   Job title/function: The research sample included respondents with the following job
    titles or functions: manager (28%); senior management, such as CEO, CFO or COO
    (14%); director (17%); consultant (14%); vice president (7); CIO (4%); and staff and
    other (16%).
•   Industry: The research sample included respondents predominantly from
    manufacturing industries. High technology and software manufacturers represented
    19% of the sample, followed by finance/banking/accounting (9%); public sector
    organizations (9%); transportation/logistics (8%); computer equipment and
    peripherals (6%); insurance, real estate and legal services (5%); industrial equipment
    manufacturing (4%); and retail(4%). Other sectors responding included
    aerospace/defense,               apparel,             automotive,            chemicals,
    construction/architecture/engineering, consumer durable goods, consumer packaged
    goods, distribution, education, food/beverage, health/medical/dental services,
    medical devices, metal and metal products, mining/oil/gas, pharmaceutical
    manufacturing,           publishing/media,          telecommunications         services,
    travel/hospitality/restaurant, utilities, and wholesale.
•   Geography: Forty-three percent of study respondents were from North America.
    Remaining respondents were from Europe (28%), Asia Pacific (23%), Middle
    East/Africa (3%), and South/Central America and the Caribbean (3%).
•   Company size: About 34% of respondents were from large enterprises (annual
    revenues above US$1 billion); 32% were from midsize enterprises (annual revenues



                              All print and electronic rights are the property of Aberdeen Group © 2006.
                                                                                     Aberdeen Group • 21
The Composite Applications Benchmark Report



             between $50 million and $1 billion); and 34% of respondents were from small
             businesses (annual revenues of $50 million or less).
        Solution providers recognized as sponsors of this report were solicited after the fact and
        had no substantive influence on the direction of The Composite Applications Benchmark
        Report. Their sponsorship has made it possible for Aberdeen Group to make these
        findings available to readers at no charge.

        Table 6: PACE Framework

        PACE Key

        Aberdeen applies a methodology to benchmark research that evaluates the business pressures, actions,
        capabilities, and enablers (PACE) that indicate corporate behavior in specific business processes. These
        terms are defined as follows:
        Pressures — external forces that impact an organization’s market position, competitiveness, or business
        operations (e.g., economic, political and regulatory, technology, changing customer preferences,
        competitive)
        Actions — the strategic approaches that an organization takes in response to industry pressures (e.g., align
        the corporate business model to leverage industry opportunities, such as product/service strategy, target
        markets, financial strategy, go-to-market, and sales strategy)
        Capabilities — the business process competencies required to execute corporate strategy (e.g., skilled
        people, brand, market positioning, viable products/services, ecosystem partners, financing)
        Enablers — the key functionality of technology solutions required to support the organization’s enabling
        business practices (e.g., development platform, applications, network connectivity, user interface, training
        and support, partner interfaces, data cleansing, and management)


                                                                             Source: Aberdeen Group, November 2006


        Table 7: Relationship between PACE and Competitive Framework

        PACE and Competitive Framework How They Interact
        Aberdeen research indicates that companies that identify the most impactful pressures and take the most
        transformational and effective actions are most likely to achieve superior performance. The level of
        competitive performance that a company achieves is strongly determined by the PACE choices that they
        make and how well they execute.

                                                                             Source: Aberdeen Group, November 2006




All print and electronic rights are the property of Aberdeen Group © 2006.
22 • AberdeenGroup
                                   Appendix B:
                        Related Aberdeen Research & Tools

       Related Aberdeen research that forms a companion or reference to this report includes:
       •    The Legacy Application Modernization Benchmark Report (September 2006)
       •    Outsourcing Application Development and Maintenance Benchmark Report (October
            2006)
       •    The Business Process Management Benchmark Report (August 2006)
       •    The Business Value of IT Outsourcing Benchmark Report (July 2006)
       •    Enterprise Service Bus and SOA Middleware (June 2006)
       •    Achieving More Value from Enterprise Applications Benchmark Report (May 2006)
       •    The SOA in IT Benchmark Report (December 2005)
       •    Building Better Composite Applications Research Brief (October 2006)
       •    Enterprise Applications: Build or Buy? (June 2006)
       Information on these and any other Aberdeen publications can be found at
       www.aberdeen.com.




Aberdeen Group, Inc.                             Founded in 1988, Aberdeen Group is the technology-
260 Franklin Street                              driven research destination of choice for the global
Boston, Massachusetts                            business executive. Aberdeen Group has over 100,000
02110-3112                                       research members in over 36 countries around the world
USA                                              that both participate in and direct the most
                                                 comprehensive technology-driven value chain research
Telephone: 617 723 7890                          in the
Fax: 617 723 7897                                market. Through its continued fact-based research,
www.aberdeen.com                                 benchmarking, and actionable analysis, Aberdeen Group
                                                 offers global business and technology executives a
© 2006 Aberdeen Group, Inc.                      unique mix of actionable research, KPIs, tools,
All rights reserved                              and services.
December 2006

The information contained in this publication has been obtained from sources Aberdeen believes to be reliable, but
is not guaranteed by Aberdeen. Aberdeen publications reflect the analyst’s judgment at the time and are subject to
change without notice.
The trademarks and registered trademarks of the corporations mentioned in this publication are the property of their
respective holders.


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | ra-composite-apps-289c2f |
| title | The Composite Applications Benchmark Report: How SOA Standards Are Accelerating Business Change |
| author | Rick Saia and Peter S. Kastner, Aberdeen Group |
| date | 2006-12 |
| type | employer-record |
| subject_domain | SOA/Composite Applications |
| methodology | Survey benchmark (N~135 enterprises; online survey + telephone interviews; Oct-Dec 2006; Aberdeen Competitive Framework) |
| source_file | source/_raw_text.txt |
| license | CC-BY-4.0 |

### Abstract

Application integration consumes ~40% of typical IT budget. Most enterprises have not fully implemented SOA but are building composite applications using web services standards (XML, SOAP, WS-*) to respond to line-of-business demands. Best in Class firms build apps in under 3 months and achieve >25% ROI. Survey of ~135 enterprises from manufacturing and services sectors. Aberdeen Competitive Framework used to segment Best in Class (20%), Industry Average (50%), and Laggards (30%).

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Landmark 2006 benchmark on composite application development, provides specific ROI metrics and competitive segmentation. Co-authored by two key Aberdeen analysts covering the SOA-to-composite transition era. |
| **Relevance** | medium | Directly quantifies composite app development performance, SOA middleware adoption rates, and ESB investment patterns across company sizes. Rich survey data on challenges and ROI. |
| **Prescience** | medium | Correctly predicted composite apps as bridge to full SOA; ESB as mandatory infrastructure; Java/.NET cross-platform tools as dominant approach. Foresaw SOA Lite/Enterprise SOA/SOA ERP segmentation. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (5)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Rick Saia | person | active |  |
| Peter S. Kastner | person | active |  |
| Aberdeen Group | organization | acquired |  |
| iTKO Inc. | organization | active |  |
| Nexaweb Technologies | organization | acquired |  |

### Technologies Referenced (17)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Composite Applications | application-architecture | vendor-neutral | emerging | mature |
| Enterprise Service Bus (ESB) | middleware | vendor-neutral | growth | mature |
| XML/SOAP/WS-* Standards | standards | vendor-neutral | growth | mature |
| SOA Repository/Registry | middleware | vendor-neutral | growth | mature |
| SOA Security Middleware | middleware | vendor-neutral | growth | mature |
| SOA Governance Middleware | middleware | vendor-neutral | growth | mature |
| SOA Management Middleware | middleware | vendor-neutral | growth | mature |
| SOA Hardware Accelerators | hardware | vendor-neutral | niche | legacy |
| Eclipse IDE | development-tool | IBM/open-source | growth | mature |
| BPEL (Business Process Execution Language) | standards | vendor-neutral | growth | legacy |
| Java/J2EE | platform | Sun/vendor-neutral | mature | mature |
| Microsoft .NET | platform | Microsoft | growth | mature |
| Legacy Application Modernization | methodology | vendor-neutral | growth | mature |
| Master Data Management (MDM) | data-management | vendor-neutral | emerging | mature |
| Browser-Based and Portal Applications | application-type | vendor-neutral | growth | mature |
| iTKO LISA Complete SOA Test Platform | testing | iTKO | niche | legacy |
| Ajax/RIA (Rich Internet Applications) | web-technology | vendor-neutral | growth | mature |

### Observation Summary

- Total observations: 90
- By type: survey-finding: 65, adoption-rate: 13, competitive-framework: 9, roi-finding: 3
