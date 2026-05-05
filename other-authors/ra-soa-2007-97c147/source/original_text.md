# SOA and Web Services Testing: How Different Can It Be? (Full Unabridged Version)

> Archived from: source/_raw_text.txt
> Original publication date: 2007-08
> Author: Aberdeen Group (Perry Donham)

---

## Original Document Text

SOA and Web Services Testing:
  How Different Can It Be?
            August 2007


        ~ Underwritten, in Part, by ~
SOA and Web Services Testing:
How Different Can It Be?
Page 2



                        Executive Summary
Testing and quality assurance (QA) pose unique challenges to organizations
deploying service oriented architectures (SOAs) and web services
applications. Unit and functional testing no longer are enough -- integration,
regression, and business process testing are critical new pieces of the
overall testing strategy. Add performance and security testing to the mix
and you have the ingredients for significant change in the QA department.
In this study of 240 end-users, Aberdeen Group research shows that Best-
in-Class (BIC) companies are taking a multi-pronged approach to the
problem by incorporating automation in the testing lab and process change
at the organizational level. More importantly, Best-in-Class companies are
increasing the involvement of business users in all phases of the
development lifecycle, and view quality not as something thatís done at the
end of the cycle, but as a horizontal attribute that spans multiple business
processes.

Best-in-Class Performance
For this report, Aberdeen used four primary performance criteria to              “Traditionally we rolled out
distinguish Best-in-Class companies from Industry Average and Laggard            functions and features as part of a
organizations:                                                                   software application. Now with
                                                                                 web services defined as
    •    Overall quality of deployed services:                                   standalone and atomic services,
         94% of the Best-in-Class reported an increase in software quality       we have to be more thorough in our
    •    Number of defects discovered in production code:                        understanding of business
         61% of the Best-in-Class recorded fewer defects                         requirements to translate into
                                                                                 specific unit web services as well
    •    Mean time to repair defects:                                            as to test for various scenarios to
         57% of the Best-in-Class saw reduced time to repair                     cater for most, if not all, of our
                                                                                 users out there - both internally and
    •    Maintainability of deployed services:                                   externally.”
         70% of the Best-in-Class said maintainability had improved               ~ Senior manager, retail sector

Competitive Maturity Assessment
Performance in the four KPIs used for this report is an indicator of the
maturity of an organization. Typical Best-in-Class organizations:
    •    Track business requirements throughout the project lifecycle (81%)
    •    Use design-time governance as a way to establish a culture of quality
         (48%)
    •    Have deployed automated testing tools for functional tests (49%)
    •    Measure quality in all phases of a project, not just in QA (70%)




© 2007 Aberdeen Group, Inc.                                                               Telephone: 617 723 7890
www.aberdeen.com                                                                                          041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 3


Required Actions
Testing assembled software in a SOA or web service environment is a
complex task. Take these steps to unravel the knot:
    •    Expand the focus of quality. Take an end-to-end perspective of
         services and test their interoperability across an entire business
         process. Best-in-Class organizations track both business
         requirements and quality across the entire enterprise, not on a
         service-by-service basis.
    •    Apply design-time governance. SOA and web services promise
         a library of tested, documented components that can be assembled
         into new applications. If a developer doesnít know about a service,
         he or she canít use it. Move toward an institutional awareness of
         governance by deploying tools and policies that foster re-use.
    •    Improve visibility of deployed services. Best-in-Class
         organizations are using monitoring and reporting tools on their
         production systems to give them a better understanding of what is
         going wrong ñ and also going right ñ in their deployed software.




© 2007 Aberdeen Group, Inc.                                                    Telephone: 617 723 7890
www.aberdeen.com                                                                               041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 4



Table of Contents
Executive Summary....................................................................................................... 2
    Best-in-Class Performance......................................................................... 2
    Competitive Maturity Assessment........................................................... 2
    Required Actions ......................................................................................... 3
Chapter One: Benchmarking the Best-in-Class ..................................................... 6
    Aberdeen Analysis ....................................................................................... 6
    Maturity Class Framework ........................................................................ 6
    Why Is Quality So Important?................................................................... 8
      Changing Everything................................................................................ 8
    The Best-in-Class PACE Model ................................................................ 9
Chapter Two: Benchmarking Requirements for Success ..................................11
    Competitive Assessment..........................................................................11
    Why QA is Coming Into Focus Now....................................................12
      Process.....................................................................................................13
      Organization ...........................................................................................14
      Testing Roles ..........................................................................................14
      Knowledge ..............................................................................................15
      Technology..............................................................................................15
      Performance ...........................................................................................16
Chapter Three: Required Actions .........................................................................18
    Laggard Steps to Success..........................................................................18
    Industry Average Steps to Success.........................................................18
    Best-in-Class Steps to Success ................................................................19
Appendix A: Research Methodology.....................................................................20
Appendix B: Related Aberdeen Research............................................................23
Featured Underwriters ..............................................................................................24


Figures
Figure 1: Best-in-Class Keys to Success for Quality ............................................. 7
Figure 2: Top Drivers for Focusing on QA............................................................. 8
Figure 3: Changes to Key QA Processes ................................................................8
Figure 4: Top Challenges in QA ..............................................................................13
Figure 5: Requirements-Based Testing Differentiates Best-in-Class
Companies ....................................................................................................................13
Figure 6: Using Governance to Drive Reusability ...............................................14
Figure 7: Software Testing Roles.............................................................................14
Figure 8: Training is an Indicator of Maturity .......................................................15
Figure 9: Technical Approaches to SOA and Web Services QA ....................16
Figure 10: The Best-in-Class Focus on Quality Across the Entire Lifecycle .17



© 2007 Aberdeen Group, Inc.                                                                                                        Telephone: 617 723 7890
www.aberdeen.com                                                                                                                                   041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 5




Tables
Table 1: Companies with Top Performance Earn Best-in-Class Status ........... 6
Table 2: The Best-in-Class PACE Framework .....................................................10
Table 3: Competitive Framework ...........................................................................12
Table 4: The PACE Framework...............................................................................21
Table 5: The Maturity Framework ..........................................................................21
Table 6: The Relationship Between PACE and the Competitive Framework
.........................................................................................................................................22




© 2007 Aberdeen Group, Inc.                                                                                                                   Telephone: 617 723 7890
www.aberdeen.com                                                                                                                                              041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 6



                    Chapter One:
             Benchmarking the Best-in-Class
Aberdeen Analysis                                                                Fast Facts
ìSOA and web service applications are un-testable,î was the comment              √ 94% of Best-in-Class
heard recently during a discussion of new methods for testing composite            organizations report an
applications. This new breed of software certainly poses unique challenges,        increase in the quality of
especially to organizations which are slow to move away from traditional           deployed services
ways of testing monolithic applications. A fundamental shift in viewpoint is     √ 61% of Best-in-Class
taking place at this time ñ the shift is moving away from old-style monolithic     companies saw a reduction in
applications toward business-driven software that is assembled from                the number of defects
components. This shift requires a parallel adjustment in not only the              discovered in production
mechanics of software testing, but also in the approach to testing.              √ 57% of Best-in-Class
                                                                                   reported a decrease in the
Maturity Class Framework                                                           time required to repair
                                                                                   defects
For this report, Aberdeen surveyed 240 end users involved in software
quality. In analyzing the data, four primary performance criteria were used
to distinguish Best-in-Class companies from Industry Average and Laggard
organizations:
    •     The number of defects discovered in production code
    •     The mean time required to repair defects
    •     The maintainability of deployed services
    •     The overall quality of deployed services
With the Best-in-Class companies identified, they were then compared to
the Industry Average and Laggard organizations (Table 1) in a number of key
areas.

Table 1: Companies with Top Performance Earn
Best-in-Class Status
         Definition of
                                        Mean Class Performance
        Maturity Class
                              • 61% saw a reduction in the number of defects
                                discovered in production
     Best-in-Class:           • 57% reported a decrease in the mean time to
   Top 20% of aggregate         repair defects
   performance scorers        • 71% saw an increase in code test coverage
                              • 94% reported an increase in the quality of
                                deployed software




© 2007 Aberdeen Group, Inc.                                                              Telephone: 617 723 7890
www.aberdeen.com                                                                                         041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 7


         Definition of
                                             Mean Class Performance
        Maturity Class
                                   • 46% saw a reduction in the number of defects
                                     discovered in production
    Industry Average:              • 31% reported a decrease in the mean time to
       Middle 50% of                 repair defects
   aggregate performance
                                   • 50% saw an increase in code test coverage
          scorers
                                   • 76% reported an increase in the quality of
                                     deployed software
                                   • 18% saw a reduction in the number of defects
                                     discovered in production
         Laggard:                  • 21% reported a decrease in the mean time to
      Bottom 30% of                  repair defects
   aggregate performance
                                   • 13% saw an increase in code test coverage
          scorers
                                   • 17% reported an increase in the quality of
                                     deployed software
                                                     Source: Aberdeen Group, August 2007

The Best-in-Class organizations profiled in this report have attacked the
problem from multiple angles. It isnít enough to just deploy automation, and
it isnít enough to simply rely on functional tests ñ QA for composite
applications needs a horizontal, process-oriented view, not the
vertical unit-test methods used in the past (Figure 1). A director in
the high-tech consulting field put it this way: ìThe tool-centric approach to
SOA QA burned us. We had to train on the test process first before we
became successful.î
The typical Best-in-Class company:
    •     Gets business users involved in all aspects of quality
    •     Uses automation to increase test coverage
    •     Sees quality as more than just an end-of-the-lifecycle task

Figure 1: Best-in-Class Keys to Success for Quality

                                                                                           “QA has become a much
            Business users               26%                    Best-in-Class              more continuous process
               involved                                         All Others
                                       19%                                                 rather than a ‘phase’ in the
                                                                                           development and
            Automated tools                               57%                              deployment lifecycle."
              for testing                      35%                                                ~ VP, Software firm

           Quality managed
                                                                      81%
             throughout
                                                              63%
              lifecycle

                              0%     20%     40%        60%         80%     100%

                                                     Source: Aberdeen Group, August 2007

© 2007 Aberdeen Group, Inc.                                                                         Telephone: 617 723 7890
www.aberdeen.com                                                                                                    041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 8


Why Is Quality So Important?
The QA function is a large part of any software development lifecycle.
Companies with formal, established QA processes often budget two to
three times the length of development time for QA testing. Any inefficiency
in the testing process can significantly affect the quality of the deployed
product and can also have a serious impact on the overall budget.
Reducing the number of defects is important, but it isnít the top reason that
most companies are looking to improve their performance in testing SOA
and web services applications (Figure 2). For all groups, cost was low on the
list of concerns. Only 22% of all companies surveyed indicated that reducing
the cost of testing was a key driver.

Figure 2: Top Drivers for Focusing on QA

              Decrease time                                       55%
                to deliver                                        56%

                   Reduce
                                                                       60%
                  number of
                                                                 52%
                   defects

              Reduce risk of
                                                  28%                 Best-in-Class
              deploying new
                                                           43%        All Others
               components

                               0%     20%           40%          60%           80%
                                                        Source: Aberdeen Group, August 2007


Changing Everything
Roughly one-third of respondents to this study indicated that they had not
made significant changes to their QA processes (Figure 3). Most were
making incremental changes on a project-by-project basis, employing
services-specific testing only when necessary.

Figure 3: Changes to Key QA Processes

                   QA has been completely                 20%         Best in Class
                        redesigned                 7%                 All Others


              Process changed project-by-                               51%
                        project                                                65%

            Testing SOA and w eb services
                                                                           62%
               differently for traditional
                                                                         54%
                       softw are

                                             0%     20%         40%      60%     80%
                                                        Source: Aberdeen Group, August 2007



© 2007 Aberdeen Group, Inc.                                                                   Telephone: 617 723 7890
www.aberdeen.com                                                                                              041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 9




Best-in-Class companies, however, are almost three times as likely as
Industry Average and Laggard organizations to have redesigned their entire
testing process. The Best-in-Class organizations have made the commitment
to services-based applications and have retooled their key processes to
reflect their new direction.
Many of the changes are focused on bringing quality to bear on the entire
lifecycle of the project by getting business users more involved. Doing this
requires the top-down commitment of the enterprise. The enterprise as a
whole must be willing to set aside the time for key players to be involved in
projects as they move from phase to phase, and to supply them with the
appropriate tools necessary. For example, 45% of Best-in-Class companies
use tools for tracking business requirements, compared to 35% of the
Industry Average and Laggard organizations.
ìTraditionally we rolled out functions and features as part of a software
application. Now with web services defined as standalone and atomic
services we have to be more thorough in our understanding of business
requirements. This allows us to translate those business requirements into
specific unit web services as well as to test for various scenarios that cater
for most (if not all) of our users both internally and externally,î said a senior
manager in the retail sector,

The Best-in-Class PACE Model
Aberdeen uses the PACE model to profile the top performing 20% of
companies ñ the Best-in-Class ñ in four areas:
    •    Pressures are external or internal pressures affecting an
         organization. These might be economic, technical, strategic, or
         competitive.
    •    Actions are the ways that an organization responds to pressures.
    •    Capabilities are the internal capabilities that an organization must
         have in order to take the specified actions.
    •    Enablers are the technical products, procedures, or designs
         necessary to carry out actions.
Table 2 shows the PACE profile of the Best-in-Class companies used for this
report.




© 2007 Aberdeen Group, Inc.                                                         Telephone: 617 723 7890
www.aberdeen.com                                                                                    041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 10


Table 2: The Best-in-Class PACE Framework

   Pressures         Actions        Capabilities              Enablers
• Decrease     • Implement • Quality and               • Defect tracking and
  the time       automated      requirements are         reporting applications
  required to    testing tools measured throughout • Production
  deliver new • Involve         the software lifecycle, monitoring and
  services and   business       not just in QA           reporting tools
  products       users in the • Separate               • Requirements
                 quality        environments are in      tracking software
                 process        place for functional
                                                       • Automated
                                and integration
                                                         orchestration and
                                testing
                                                         integration testing
                              • Key developers,          tools
                                business analysts, and
                                testers are trained in
                                new technologies
                                        Source: Aberdeen Group, August 2007

         Aberdeen Insights ñ What is Happening to QA?
As the emphasis shifts from IT to business as the driver for technology
change, the QA team is being asked to provide more than just functional
testing. A functional test wonít reveal how a new service interacts in an
end-to-end business process. Even updating a single service carries risk and
may require modeling to determine its impact. One company we spoke
with does not complete incremental updates to deployed services ñ every
change they make results in a new service in order not to upset the apple
cart.
Although everyone agrees that defects and time are important, risk is a
significant concern for organizations in the Industry Average and Laggard
categories. For these companies that are still early on the maturity curve
for SOA and web services, each additional service or component can
embody a large number of dependencies and the risk of damaging running
software can be high. Regression testing is done by only 39% of Laggard
organizations, so the risk for them is quite real.
Best-in-Class companies tend to be further along the maturity curve and
have learned the lessons of untested software. For them, the risk is known
and the emphasis is instead on improving the quality of their software.
In the words of an IT manager who has been there, ìOur initial experience
has been tedious in defining the new processes for testing SOA and web
services, with a higher learning curve for testers, however, the effort now
has started paying off.î




© 2007 Aberdeen Group, Inc.                                                       Telephone: 617 723 7890
www.aberdeen.com                                                                                  041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 11



               Chapter Two:
    Benchmarking Requirements for Success
                                                                                Fast Facts
Best-in-Class IT organizations are changing their QA processes to
encompass composite applications. These companies are also focusing on          √ Best-in-Class companies are
                                                                                  twice as likely to use
the quality of end-to-end business transactions instead of the more
                                                                                  automated requirements-
traditional functional testing of individual services.                            tracking tools than Laggard
       Case Study: Applying Quality End-to-End at iSOFT                           organizations
                                                                                √ 70% of Best-in-Class firms
                                                                                  measure quality throughout
 ìQA at iSOFT has changed to implement an end-to-end view of testing and          the project lifecycle, not just
 quality,î according to Phil Davies, Director of the LORENZO product unit         in testing
 at iSOFT. When the technology and platform of a current product had
                                                                                √ Nearly half (47%) of Best-
 reached the limits of extendibility, the company decided to build a new          in-Class companies use
 product from the ground up based on SOA, instead of re-engineering the           design-time governance to
 older version bit-by-bit.                                                        promote reuse of software
                                                                                  components versus an
 The change in technical strategy was a driver for process change as well.
                                                                                  average of 33% for other
 Adopting an end-to-end view of quality meant that test plans and scripts         organizations
 are written and validated earlier in the lifecycle. Automation has been
 introduced to handle an increased volume of testing.
 ìIt introduced other challenges. At first we learned more about the
 necessary process changes we needed,î said Davies. ìNow we have
 enough instrumentation in the process to understand quantitative quality
 measurement, track metrics, and view improvement.î
 Davies sees quality as a continuous process, where improvements are
 being incrementally made cycle-by-cycle. ìThis isnít our end state; there is
 always room for improvement. For example, we need to increase the
 amount of tooling and automation that we use, as well as shorten the
 feedback time so that we can implement improvements faster.î


Competitive Assessment
The aggregated performance of surveyed companies determined whether
they ranked as Best-in-Class, Industry Average, or Laggard. In addition to
having common performance levels, each class also shared characteristics in
five key categories: (1) process (detect and respond to changing conditions
without placing additional burdens on the organization); (2) organization
(corporate focus and collaboration among stakeholders); (3) knowledge
management (contextualizing data and exposing it to key stakeholders); (4)
technology (selection or appropriate tools and intelligent deployment of
those tools); and (5) performance measurement (ability of the organization
to measure the benefits of technology deployment and use the results to
improve key processes further). These characteristics (Table 3) serve as a
guideline for best practices and correlate directly with Best-in-Class
performance across the key metrics.


© 2007 Aberdeen Group, Inc.                                                           Telephone: 617 723 7890
www.aberdeen.com                                                                                      041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 12


Table 3: Competitive Framework
                     Best-in-Class            Average              Laggards
                    Requirements are managed throughout the software lifecycle
                              81%                72%                   54%
   Process
                        Automation is used for tracking business requirements
                              38%                28%                   21%
                         Design-time governance is used to foster culture of
Organization                                reusability
                              48%                39%                   26%
                     Key developers, business analysts, and architects are trained
 Knowledge                              in new technologies
                              57%                38%                   36%
                      Automated tools are used for functional testing SOA and
                                    web services components
                              48%                42%                   29%

 Technology            Orchestration and integration testing tools are in place
                              40%                27%                   19%
                     Automated tools are used to extract business logic and data
                              24%                18%                   13%
                    Quality is measured throughout the project lifecycle, not just
Performance                                   in QA
                              70%                58%                   49%

                                               Source: Aberdeen Group, August 2007


Why QA is Coming Into Focus Now
The adoption of SOA and/or web services at most companies has followed
a pattern: An initial commitment is made to dedicate resources to
examining SOA, followed by the establishmment of a center of excellence
or several pilot projects. In these scenarios, the number of deployed
services is small, and the complexity of testing is low.
Research done at Aberdeen over the past two years (see Appendix B) has
shown that organizations are moving now from the pilot stage to the
production stage. These organizations have started deploying significant
numbers of services, and are hitting a wall in terms of how they can
continue to improve the quality of their operations/processes/products.
What was easy in a small, self-contained pilot project is now difficult for
companies in the new environment with dozens or hundreds of deployed
services being used in multiple applications. It is natural to be facing hard
questions about quality and risk at this stage.
The top challenge cited by Best-in-Class companies related to SOA and
services testing was incomplete technical specifications, while the second
© 2007 Aberdeen Group, Inc.                                                          Telephone: 617 723 7890
www.aberdeen.com                                                                                     041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 13


challenge was tools related. Time budgeted for QA is not an issue for the
Best-in-Class, but it is the top concern of the Industry Average (Figure 4).

Figure 4: Top Challenges in QA

      Incomplete                                                        47%
       technical                                                   41%
     specifications                                                   45%

    QA tools not                                                 38%
 designed for SOA                                          33%
  or w eb services                                        32%

                                              23%                              Best-in-Class
  Not enough time
                                                                      42%      Industry Average
  alloted for testing                                     32%                  Laggard

                      0%         10%    20%         30%         40%          50%
                                                     Source: Aberdeen Group, August 2007


Process
One of the key differentiators of the Best-in-Class is that they place a heavy
emphasis on the business view of testing. This is consistent with Aberdeenís
observation from previous reports that there has been a fundamental shift
of emphasis away from IT as a principle driver of functionality, toward the
business user. ITís response to this shift has been to move toward SOA and
web services as a means of quickly responding to changing business
requirements.
Tracking business requirements is a key component of this new way of
building software. Best-in-Class companies use automation to manage those
requirements across the entire lifecycle of a project, not just during the
design phase (Figure 5). This capability becomes critical during regression
and orchestration testing, when a component that passes unit test may not
deliver the expected results from a business perspective.

Figure 5: Requirements-Based Testing Differentiates
Best-in-Class Companies


           Automation used                        38%            Best-in-Class
           to track business                28%                  Industry Average
             requirements                21%                     Laggard

              Requirements
                                                                             81%
                managed
                                                                       72%
             throughout the
                                                           54%
             project lifecycle

                               0%      20%    40%          60%         80%         100%

                                                     Source: Aberdeen Group, August 2007


© 2007 Aberdeen Group, Inc.                                                                       Telephone: 617 723 7890
www.aberdeen.com                                                                                                  041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 14


Organization
One way that Best-in-Class companies drive up the quality of deployed
services is by reusing tried and tested components (Figure 6). Design-time
governance is a way to build an organizational culture centered around
reuse.
Although governance can be a manual process, it is more typical to have an
automated toolset that matches requirements with existing code. When
workflow is added, change control and approval processes are greatly
simplified.
Industry Average and Laggard companies are not unaware of the advantage
this brings to quality. Fifty percent of these companies state that they plan
to implement design-time governance in the next twelve months.

Figure 6: Using Governance to Drive Reusability
               60%
                              49%
               50%
                                                  36%
               40%
               30%
               20%                                                  15%
               10%
                0%
                       Best-in-Class       Industry Average       Laggard

                                                        Source: Aberdeen Group, August 2007


Testing Roles
Best-in-Class companies rely more heavily on dedicated QA resources than
do the other groups (Figure 7). Organizationally, these companies are
further along the SOA maturity curve and are more likely to use dedicated
QA teams on their projects.

Figure 7: Software Testing Roles

                                                                             93%
              QA testers                                               79%
                                                                 70%

                                                       44%
              Developers                                  53%
                                                       45%

                                           24%
               End users                          37%
                                                 36%

            External beta             18%                       Best-in-Class
                                      17%                       Industry Average
               testers          5%                              Laggard

                           0%        20%         40%      60%      80%       100%
                                                        Source: Aberdeen Group, August 2007

© 2007 Aberdeen Group, Inc.                                                                   Telephone: 617 723 7890
www.aberdeen.com                                                                                              041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 15


Developers still play a key role in quality. For all groups it is important to
emphasize that quality is not just unit and functional testing ñ quality in a
mature organization encompasses the end-to-end assembled business
process, not simply individual services.
Interestingly, when asked if organizations test SOA and web services
components outside of the company, 40% of all respondents (although only
32% of Best-in-Class) said that they did. Incorporating an external service
into the test plan adds complexity and risk; a trend that we will watch
closely over the next several months.

Knowledge
Training in SOA and web services technologies is an area in which Best-in-
Class companies show a significant advantage (Figure 8). This isnít just about
testing: Business analysts and developers must be able to think in terms of             “Testers are now required
                                                                                        to know how to code as
assembled applications and business processes in order to understand how
                                                                                        well as being part of the
to build quality into their software. Once all of the key players are aligned to        QA process from start to
a services-based architecture they can apply quality across the end-to-end              finish."
business process.
                                                                                                    ~Manager,
                                                                                            telecommunications
Figure 8: Training is an Indicator of Maturity                                                       company

                      Key developers, business analysts, and testers are
                         trained in SOA and w eb services technology
               70%
                              60%
               60%
               50%
                                            35%              36%
               40%
               30%
               20%
               10%
                0%
                       Best-in-Class   Industry Average     Laggard

                                                  Source: Aberdeen Group, August 2007

Training all roles in an organization is another indicator of maturity. While
Best-in-Class companies are twice as likely to have already trained their
workers, both the Industry Average (57%) and Laggard (48%) companies
plan to take this step in the next twelve months.

Technology
Automated testing tools are a key differentiator for Best-in-Class (Figure 9).
Once the number of deployed services reaches more than a few dozen,
integration and regression testing becomes difficult without the help of
software.
Where and when automation become appropriate depends on the kind of
testing being done. While nearly all (94%) respondents report that they
perform functional testing of services (and over 80% are doing integration
© 2007 Aberdeen Group, Inc.                                                                      Telephone: 617 723 7890
www.aberdeen.com                                                                                                 041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 16


testing) the numbers drop rapidly as QA becomes more complicated. While
Best-in-Class companies are 50% more likely to do regression testing than              “We don't have a defined
Laggards (64% versus 38%), all of the groups are performing compliance                 strategy for testing services
(30%), orchestration (25%), and security testing (41%) at alarmingly low               and the organization is not
rates. Fifty percent of the Best-in-Class are executing performance tests.             in agreement on how to
                                                                                       test them. Some projects
                                                                                       use free tools, some use a
Figure 9: Technical Approaches to SOA and Web Services QA                              home-grown tool.
                                                                                       Performance testing is not
              Monitoring / reporting tools in                      60%                 always done. Security
                       production
                                                                50%                    testing really hasn't entered
                                                              45%
                                                                                       the picture yet either."
             Automated tools for SOA and                       48%                         ~Consultant, utilities
                                                             42%
             w eb services functional test             29%                                             industry

             Orchestration / integration test                40%
                                                    27%
                         tools                    19%

             Automated tools for extracting          24%     Best-in-Class
                                                   18%       Industry Average
                 business logic / data           13%         Laggard

                                            0%   20%   40%         60%   80%

                                                 Source: Aberdeen Group, August 2007

                      Aberdeen Insights ñ Technology

Automation is not an option when testing the complex interactions among
deployed services that are part of an end-to-end transaction. Even if a single
service passes unit and functional tests, the view of the quality of that service
is different depending on the individualís role in the company. A service that
has aced its functional tests may receive a thumbs-up from the development
and QA team and still fail miserably from the business userís perspective.
Composite applications also bring new challenges to integration testing, since
a single service might be used by multiple, non-connected use cases. QA and
change management teams must be able to model the results of new versions
of deployed services before sending them to production. While many
companies have developed in-house tools to cover these areas, commercial
applications are now entering the market that will assist the QA team in
these increasingly complex tasks. The best will tie together functionality with
requirements to provide a complete picture of the quality of a component.


Performance
Measurement is the key to change. Best-in-Class companies are much more
likely to measure the quality of a web service or SOA component across
the entire development lifecycle ñ from the definition of business
requirements to deployment and maintenance (Figure 10).


© 2007 Aberdeen Group, Inc.                                                                        Telephone: 617 723 7890
www.aberdeen.com                                                                                                   041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 17


ìFunctionality was the main objective earlier. Now, the focus is more on
how the service is exposed, invoked, its interoperability, how it is
orchestrated and governed, and managing change. Assembly of services with
the right version also needs to be tested. So it is now not only functionality,
but a host of non-functional and technical features that needs to be tested.
Testing of SOA and web services requires a different mindset,î said a vice
president of IT.
In support of this, the Best-in-Class are increasing their budget for quality at
a faster pace than all other respondents: 66% of the Best-in-Class indicated
that they have increased their spending on QA per project versus 50% of
the Industry Average and 14% of Laggards.

Figure 10: The Best-in-Class Focus on Quality Across
the Entire Lifecycle
               80%        70%
               70%
                                           58%
               60%                                          49%
               50%
               40%
               30%
               20%
               10%
                0%
                      Best-in-Class   Industry Average    Laggard

                                                 Source: Aberdeen Group, August 2007




© 2007 Aberdeen Group, Inc.                                                            Telephone: 617 723 7890
www.aberdeen.com                                                                                       041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 18



                           Chapter Three:
                          Required Actions
Based on the information in Chapters One and Two, readers should
determine whether their organizations fall into the ìLaggard,î ìIndustry
Average,î or ìBest-in-Classî category. The key to gaining value from this
report is moving your organization along the maturity path to Best-in-Class.
The following actions will help spur necessary performance improvements:
                                                                                 Fast Facts

Laggard Steps to Success                                                         √ 94% of the Best-in-Class
                                                                                   reported an increase in
    •    Establish integration testing. Take the next step in your QA              software quality
         journey by moving beyond unit and functional testing toward
                                                                                 √ 61% of the Best-in-Class
         integration testing of key services. The Best-in-Class are using
                                                                                   recorded fewer defects
         integration testing tools at double the rate of Laggard companies.
                                                                                 √ 57% of the Best-in-Class saw
    •    Build a culture of quality. Best-in-Class companies treat quality         reduced time to repair
         as an end-to-end process rather than as the last step in the software
         lifecycle. Adding quality to all phases of a project will prove         √ 70% of the Best-in-Class said
         beneficial; start by involving the business users in both the design      maintainability had improved
         and the execution of test plans.
    •    Automate. The Best-in-Class are leveraging automated testing
         tools at double the rate of Laggards (57% versus 29%). SOA and
         web services are too complex to rely on manual testing alone;
         automation will ease the burden on the test team and allow them to
         focus on more strategic work, as well as significantly improve code
         coverage of individual components.

Industry Average Steps to Success
    •    Expand the focus of quality. Take an end-to-end perspective on
         services and test the servicesí interoperability across the entire
         business process. Best-in-Class organizations track both business
         requirements and quality across the enterprise, not on a service-by-
         service basis. Use tools that provide end-to-end testing in addition
         to functional or interface tests.
    •    Apply design-time governance. SOA and web services provide
         a library of tested, documented components that can be assembled
         into new applications ñ but if a developer doesnít know about a
         service, he or she canít use it. Move toward an institutional
         awareness of governance by deploying tools and policies that foster
         re-use.
    •    Improve visibility of deployed services. Best-in-Class
         organizations are using monitoring and reporting tools on their
         production systems to give them a better understanding of what is
         going wrong ñ and what is also going right ñ in their applications.



© 2007 Aberdeen Group, Inc.                                                              Telephone: 617 723 7890
www.aberdeen.com                                                                                         041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 19


Best-in-Class Steps to Success
    •    Increase the use of governance. Leverage your existing design-
         time governance policies to increase the re-use of standardized,
         tested components, and then incorporating it into your change
         management process. Use run-time governance as an addition to
         your production monitoring capabilities to improve the granularity
         of measurement.
    •    Use modeling to mitigate risk. Modeling tools will help you
         uncover potential problems when upgrading or adding new services.
         Deploy these tools now to gain experience and insights before the
         need becomes critical.
    •    Focus on performance. Performance testing of composite
         applications is the next great frontier. As more services are pushed
         into production, measuring, modeling, and managing performance is
         becoming more critical. Donít ignore measurement of business
         process SLAs ñ in the end they will be the key indicator of a healthy
         application.
                              Aberdeen Insights – Summary
 The original hypothesis for this research was that automation would be the key to
 successfully testing SOA and web services components. While this certainly was
 validated by the experiences of nearly 250 companies, a second, equally important
 story emerged from the data. Research showed that the best companies are testing
 not only vertically (using unit and functional testing as their benchmark for quality)
 but are also testing horizontally across an entire business process.
 One key component of this approach is the involvement of the business user in
 more phases of the development lifecycle, and the extension of the reach of the QA
 team into earlier phases. While these have been characteristics of quality in other
 approaches to software development, they take on added power when applied to
 applications that are assembled from individual pieces instead of one large chunk
 of code.
 It’s the combination of people, process, and technology that make Aberdeen’s Best-
 in-Class stand out from the crowd. These organizations understand that a tool or
 process taken alone isn’t enough to drive quality throughout an organization.




© 2007 Aberdeen Group, Inc.                                                               Telephone: 617 723 7890
www.aberdeen.com                                                                                          041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 20



                         Appendix A:
                     Research Methodology
Between July and August 2007, Aberdeen Group examined the responses of
approximately 250 companies across a variety of geographies, industries and
company revenues.
Aberdeen supplemented this online survey effort with telephone interviews
with select survey respondents, gathering additional information on their
QA strategies, experiences, and results.
The study aimed to identify emerging best practices for quality assurance
and testing of SOA and web services-based applications, and to provide a
framework by which readers could assess their own organizationís
capabilities and maturity.
Responding enterprises included the following:
    •    Job title/function: About two-thirds of the survey respondents are
         in their organizationsí IT departments. The research sample
         included respondents with the following job titles: senior executives
         including CEO, COO, CFO, and VP (14%); CIO (6%); IT manager or
         director (37%); internal consultant (21%); and IT staff (18%).
    •    Industry: The research sample included respondents predominantly
         from high-technology industries and companies (representing 34%
         of the sample). A significant number of respondents were in the
         insurance industries (12%), finance and banking (18%), and
         telecommunications (12%).
    •    Geography: The survey respondents were distributed between
         North America (U.S., Canada, Mexico) 59%; Central and South
         America (2%); Asia/Pacific (20%); Europe, Middle East, and Africa
         (19%).
    •    Company size: Thirty two percent of respondents were from large
         enterprises (annual revenues above US$1 billion, including 19% over
         US$5 billion); 31% were from midsize enterprises (annual revenues
         between $50 million and $1 billion); and 37% of respondents were
         from small businesses (annual revenues of $50 million or less).
Solution providers recognized as sponsors of this report were solicited after
the fact and had no substantive influence on the direction of the report.
Their sponsorship has made it possible for Aberdeen Group to make these
findings available to readers at no charge.




© 2007 Aberdeen Group, Inc.                                                      Telephone: 617 723 7890
www.aberdeen.com                                                                                 041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 21



Table 4: The PACE Framework

PACE Key

Aberdeen applies a methodology to benchmark research that evaluates the business
pressures, actions, capabilities, and enablers (PACE) that indicate corporate behavior in
specific business processes. These terms are defined as follows:
Pressures — external forces that impact an organization’s market position, competitiveness,
or business operations (e.g., economic, political and regulatory, technology, changing
customer preferences, competitive)
Actions — the strategic approaches that an organization takes in response to industry
pressures (e.g., align the corporate business model to leverage industry opportunities, such
as product/service strategy, target markets, financial strategy, go-to-market, and sales
strategy)
Capabilities — the business process competencies required to execute corporate strategy
(e.g., skilled people, brand, market positioning, viable products/services, ecosystem
partners, financing)
Enablers — the key functionality of technology solutions required to support the
organization’s enabling business practices (e.g., development platform, applications,
network connectivity, user interface, training and support, partner interfaces, data cleansing,
and management)

                                                       Source: Aberdeen Group, August 2007

Table 5: The Maturity Framework

Maturity Framework Key

The Aberdeen Maturity Framework defines enterprises as falling into one of the following
three levels of practices and performance:
Best-in-Class (20%) — Application development practices that are the best currently being
employed and significantly superior to the industry norm, and result in the top industry
performance.
Industry norm (50%) — Application development practices that represent the average or
norm, and result in average industry performance.
Laggards (30%) — Application development practices that are significantly behind the
average of the industry, and result in below average performance
In the following categories:
Process — What is the scope of process standardization? What is the efficiency and
effectiveness of this process?
Organization — How is your company currently organized to manage and optimize this
particular process?
Knowledge — What visibility do you have into key data and intelligence required to manage
this process?
Technology — What level of automation have you used to support this process? How is this
automation integrated and aligned?
Performance — What do you measure? How frequently? What’s your actual performance?

                                                       Source: Aberdeen Group, August 2007


© 2007 Aberdeen Group, Inc.                                                                       Telephone: 617 723 7890
www.aberdeen.com                                                                                                  041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 22


Table 6: The Relationship Between PACE and the Competitive
Framework

PACE and Competitive Framework How They Interact
Aberdeen research indicates that companies that identify the most impactful pressures and
take the most transformational and effective actions are most likely to achieve superior
performance. The level of competitive performance that a company achieves is strongly
determined by the PACE choices that they make and how well they execute.

                                                   Source: Aberdeen Group, August 2007




© 2007 Aberdeen Group, Inc.                                                                 Telephone: 617 723 7890
www.aberdeen.com                                                                                            041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 23



                              Appendix B:
                       Related Aberdeen Research
Related Aberdeen research that forms a companion or reference to this
report includes:
      •     The SOA in IT Benchmark Report, December, 2005
      •     The Legacy Application Migration Benchmark Report, September 2006
      •     The Composite Applications Benchmark Report, December, 2006
      •     Modernizing Legacy Application: Maximizing the Investment, June 2007
      •     SOA Middleware Starts Where Web Services Leave Off, July 2007

Information on these and any other Aberdeen publications can be found at
www.Aberdeen.com.




                   Author: Perry Donham, Director, Enterprise Applications Research
                                   (perry.donham@aberdeen.com)

Founded in 1988, Aberdeen Group is the technology- driven research destination of choice for the global business
executive. Aberdeen Group has over 100,000 research members in over 36 countries around the world that both
participate in and direct the most comprehensive technology-driven value chain research in the market. Through its
continued fact-based research, benchmarking, and actionable analysis, Aberdeen Group offers global business and
technology executives a unique mix of actionable research, KPIs, tools, and services.
This document is the result of research performed by Aberdeen Group. Aberdeen Group believes its findings are
objective and represent the best analysis available at the time of publication. Unless otherwise noted, the entire
contents of this publication are copyrighted by Aberdeen Group, Inc. and may not be reproduced, stored in a retrieval
system, or transmitted in any form or by any means without prior written consent by Aberdeen Group, Inc.

© 2007 Aberdeen Group, Inc.                                                                                             Telephone: 617 723 7890
www.aberdeen.com                                                                                                                        041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 24



                     Featured Underwriters
This research study was made possible in part with the financial support of
our underwriters. These organizations share Aberdeenís vision of bringing
fact-based research to organizations worldwide at little or no cost.
Underwriters have no editorial or research rights and the facts and analysis
of this report remain an exclusive production and product of Aberdeen
Group.

                                               iTKO LISA offers Lifecycle
                                               Quality    governance    for
                                               testing     Service-Oriented
                                               Architectures (SOA). iTKO's
mission is to allow everyone involved in IT to own Complete, Collaborative,
and Continuous software quality. iTKO LISATM SOA Test Framework
performs unit, functional, regression, load and performance tests, without
requiring test coding or script maintenance, saving development and QA
teams effort while improving quality at every phase of development and
deployment. LISA provides live interaction with web apps, web services,
J2EE, .NET, Java objects, ESB, databases, and many more technologies.
Founded in 1999, the Dallas-based company's customers include Sun, Citi,
Cardinal          Health,       AMD,            TIBCO         and        i2.

For additional information on iTKO, Inc.:
1505 LBJ Freeway, Suite 150            Tel: 877.289.4856
Dallas, TX 75234                       www.itko.com
                                       info@itko.com


                                                  Mindreef provides award-
                                                  winning Web services and
                                                  SOA solutions that allow
                                                  organizations to drive
pervasive quality into SOA deployments, and accelerate service reuse and
business agility. Mindreef SOAPscope products reduce the complexities of
Web services and XML, empowering teams with prototyping, governance,
testing, diagnostics and support tools that improve SOA quality throughout
design-time, change-time and run-time. Mindreef solutions help analysts,
architects, developers, testers, operations and support staff to ensure
quality as they build, test, and deploy Web services and composite
applications. Mindreef products are used by over three thousand customers
at over 1,200 organizations worldwide, including 40 of the Fortune 100.

For additional information on Mindreef, Inc.:
22 Proctor Hill Road                   Tel: 603.465.2204
Hollis, NH 03049                       www.mindreef.com
                                       info@mindreef.com

© 2007 Aberdeen Group, Inc.                                                    Telephone: 617 723 7890
www.aberdeen.com                                                                               041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 25




                                                  Solstice Software is the
                                                  leading         provider       of
                                                  automated,            end-to-end
                                                  integration and SOA testing
                                                  software          for       large
                                                  organizations that require
                                                  visibility into complex systems
that support customer, partner and internal business applications. Solstice
Softwareís flagship product, Solstice Integra Suite, uniquely addresses the
testing challenges presented by todayís complex, full scale integration and
SOA implementations by validating end-to-end services and processes,
verifying critical middleware connections across applications and transports,
and simulating unavailable application components. Solstice Integra Suite
automates testing across the life cycle, enabling re-use and removing the
traditional obstacles to high levels of quality and speed to market.

For additional information on Solstice Software:
650 Naamans Road, Suite 207               Tel: 302.792.3049
Claymont, DE 19703                        www.solsticesoftware.com
                                          mbayliss@solsticesoftware.com




© 2007 Aberdeen Group, Inc.                                                           Telephone: 617 723 7890
www.aberdeen.com                                                                                      041207a
AberdeenGroup




                Enterprise Information Integration
                  The New Way to Leverage E-information




                              Second Edition
                                 July 2003
Aberdeen Group, Inc.
Aberdeen Group is a leading IT market analysis and positioning services firm that
helps information technology vendors establish leadership in emerging markets.
Aberdeen Group performs specific projects for a select group of domestic and in-
ternational clients. Each project requires a combination of strategic advice and
pragmatic, experience-based action plans. Assignments range from corporate and
product positioning and organizational planning to in-depth market segment re-
search. Aberdeen consults on mergers and acquisitions, corporate positioning and
investor relations, and transaction-processing benchmarks; in addition, it offers
special expertise in software and midrange computer markets.
In carrying out assignments, Aberdeen uses a proprietary, comprehensive, ana-
lytical framework providing fresh insight into the complex future of computing
and communications, both from technological and market-dynamics perspectives.
Aberdeen also offers retainer-fee programs to a group of continuing clients.
Aberdeen principals and staff are recognized industry figures with hundreds of
years of combined high-tech industry, research, and financial community experi-
ence among them. They are quoted extensively in industry trade and business
publications. Each staff member is a frequent conference and seminar speaker.
In addition to client-related research and consulting, Aberdeen publishes several
periodicals, Aberdeen Viewpoints, and Profiles, which summarize its analysis and
research findings.
To provide us with your feedback on this research, please go to
www.aberdeen.com/feedback.
The information contained in this publication has been obtained from sources Aberdeen believes to be reli-
able, but is not guaranteed by Aberdeen. Aberdeen publications reflect the analyst’s judgment at the time
and are subject to change without notice.
The trademarks and registered trademarks of the corporations mentioned in this publication are the property
of their respective holders.
Warning: This publication is protected by United States copyright law and international treaties. Unless oth-
erwise noted, the entire contents of this publication are copyrighted by Aberdeen Group, Inc. and may not be
reproduced, stored in a retrieval system, or transmitted in any form or by any means without prior written
consent. Unauthorized reproduction or distribution of this publication, or any portion of it, may result in severe
civil and criminal penalties, and will be prosecuted to the maximum extent necessary to protect the rights of
the publisher.
© 2003 Aberdeen Group, Inc., Boston, Massachusetts
              Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Table of Contents

  Preface ................................................................................................................ 1

  Chapter One: Executive Summary ...................................................................... 3

  Chapter Two: Summary of Findings..................................................................... 6

  Chapter Three: Market Definition and Dynamics ............................................... 10
     What Is EII, and How Does It Work?............................................................10
         EII Is New Technology ...........................................................................12
         EII in the User Site.................................................................................12
         Situations in Which Today’s Companies Often Feel a Need for EII........13
         Business Benefits of EII.........................................................................14
         Applying EII to Typical IT Tasks .............................................................15
         Criteria for Buying an EII Solution..........................................................18
         Critical Technology Factors....................................................................20
         Object, Multimedia, and Non-database Support ....................................20
         Specific Front-End Support....................................................................21
         Developer Support.................................................................................23
         Administrator Support ............................................................................23

  Chapter Four: EII As Part of Strategic Information Management ....................... 25
     A Brief Introduction to Strategic Information Management ...........................25
         What Is Information Aggregation, and Why Does It Matter? ..................26
         When to Apply What Information Aggregation Technology ....................30
         The State of the Art in Information Aggregation .....................................30
         Action Items...........................................................................................38

  Chapter Five: Market Forecast and Segmentation ............................................ 40
     Key Technologies for EII Initiatives...............................................................40
     Aberdeen EII Technology Segmentation Model............................................40
         EAI.........................................................................................................41
         Database Technologies..........................................................................42
         XML Messaging Technologies ...............................................................43
         Combinations of Technologies ...............................................................43
         Summarizing the Model .........................................................................44
     Growth Forecasts.........................................................................................47


                                                                                                           AberdeenGroup • i
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




          Table of Contents

               Chapter Six: Aberdeen Observations..................................................................49
                  Impact of Major IT Trends ............................................................................49
                      Application Servers................................................................................49
                      The Role of Java ...................................................................................49
                      Extensible Markup Language (XML) .....................................................50
                      Emphasis on Cost-Effective Administration ...........................................50
                      Enterprise Portals ..................................................................................50
                      Web Services ........................................................................................51
                  Supplier Success Factors ............................................................................52
                      Success Factors for Organizations........................................................52
                  Aberdeen Observations and Conclusions ....................................................54
                  Positioning and Capabilities .........................................................................54
                      Market Segmentation ............................................................................54
                      Technology Interdependency.................................................................54
                      Distribution and Implementation ............................................................55
                  Major Forces ................................................................................................56
                      Mergers and Acquisitions (M&A) ...........................................................56
                      Standardization and Integration.............................................................56
                  Success Factors...........................................................................................56
                  The Future ...................................................................................................56

               Chapter Seven: Supplier Profile .........................................................................58
                  MetaMatrix, Inc. ...........................................................................................59

               Author Profile......................................................................................................63

               Appendix A: Lexicon of Acronyms and Abbreviations .........................................64

               Appendix B: Related Aberdeen Research ..........................................................66

               Appendix C: Supplier Contact Information.........................................................67




ii • AberdeenGroup
            Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Figures

  Figure 1: EII in a Typical Architecture..................................................................11

  Figure 2: Example of Information Aggregation Architecture............................... 30

  Figure 3: EII Technology Segmentation Model .................................................. 44


Tables

  Table 1: Ways to Use EII in Strategic Initiatives................................................. 15

  Table 2: EII versus Traditional Approaches ........................................................ 18

  Table 3: EII Constituents and Their Data Needs ................................................ 21

  Table 4: Strategic Uses of Information Aggregation ........................................... 28

  Table 5: Taxonomy of Information Aggregation Tools......................................... 31

  Table 6: EII and Related Suppliers..................................................................... 45

  Table 7: EII and Related Suppliers.................................................................... 46

  Table 8: EII Supplier Revenues (Aberdeen Estimates, Projected over 2003) .... 47

  Table 9: Revenues for Markets Related to EII.................................................... 48




                                                                                             AberdeenGroup • iii
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Preface
Enterprise information integration (EII) is now a market separate
from enterprise application integration (EAI) and extract-transform-
load (ETL) solutions.
The main reason that companies now recognize a distinct need to
integrate information across the enterprise is that the overall pool of
proprietary enterprise information  as distinct from information
associated with specific packaged applications, Web databases, or
data mining sources  is now a key e-business differentiator. The
ability to leverage information from a wide variety of storage types,
environments, applications, databases, and files via enterprise portals
allows enterprises to deliver major value-add simultaneously to em-
ployees, partners, and customers.
A second reason to look closely at EII is that  as Aberdeen re-
search shows  firms are now at a critical stage in linking back-end
applications and data to their front-end Web sites. Three years of
fragmented efforts to link key applications one by one, followed by a
proliferation of enterprise portals that crisscross various back-end
data sources, have left companies with unnecessarily complex and
costly e-business architectures. The key to cutting administrative and
new application development costs is to implement a common soft-
ware infrastructure architecture  and EII infrastructure lies at the
core of such an architecture.
Third, the requirements of e-business are a superset of the require-
ments of traditional information processing. A narrow definition of
data integration as being concerned only with integrating informa-
tion within a company must change to encompass EII’s integration of
information between companies as well.
This report provides the reader with a clear understanding of the
forces influencing the market, as well as Aberdeen’s insights into the
real opportunities and benefits of EII and its future directions. The
second edition follows up the information published in May 2002 to
include major new suppliers and new trends. The report includes the
following:
•   Technology segmentation — An update to the Aberdeen
    segmentation model that indicates various technology
    approaches to EII and the suppliers supporting those technolo-
    gies

•   Market size and growth projections — Aberdeen’s most recent
    data on EII market size and growth



                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                          AberdeenGroup • 1
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   •    Issues and challenges — An outline of additional industry
                                        trends that are affecting EII initiatives

                                   •    Observations and conclusions

                                   •    Supplier profiles — A comprehensive list of the suppliers in this
                                        market

                                   The intended audience for this report is IT (information technology),
                                   corporate, and line-of-business management responsible for planning
                                   and managing initiatives for information integration, as well as
                                   communicating and interacting effectively with potential distributors
                                   and suppliers. This publication was designed to help these users
                                   understand the potential impact of information integration regarding
                                   the following:
                                   •    An enterprise’s total application portfolio

                                   •    Enterprise information strategies

                                   •    E-business planning and execution

                                   •    Present technologies, including Web services, which will under-
                                        pin corporate architectures over the next two to three years

                                   This publication profiles the key suppliers and products in the mar-
                                   ket. Aberdeen believes that this report will aid organizations in iden-
                                   tifying the technologies and attributes of EII products that can best
                                   fit their business requirements. It will also help organizations effec-
                                   tively plan EII acquisition strategies.




All print and electronic rights are the property of Aberdeen Group © 2003
2 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Chapter One:
Executive Summary
Aberdeen research shows that the motivator of many e-enterprises is
not only cost savings but also competitive advantage. A slight Web
site advantage can cause customers across a global market to estab-
lish relationships; a slight but persistent disadvantage can, even to-
day, cause 10% to 20% of the installed base to walk away.
To create and maintain competitive advantage, enterprises have now
moved beyond pretty graphics, informational displays, and rudimen-
tary order taking. They have also connected their back-end order-
processing (B-to-C) and supply chain (B-to-B) applications to the
Web site  and, in some cases, with other companies’ Web sites or
with e-marketplaces. However, most of these efforts maintain sepa-
rate, uncoordinated links to one or more Web sites.
To integrate information at the user-interface level, enterprises are
now implementing enterprise portals. A portal allows the enterprise
to display data applications and fully leverage all major business-
critical company databases. However, by itself, an enterprise portal
does little beyond show data in different formats side by side.
To fully leverage the connections between information from differ-
ent applications and databases, an enterprise needs an EII infrastruc-
ture to aggregate data and coordinate transactions across back-end
data sources. At its most powerful, EII lets all back-end information
be seen as if it came from one comprehensive, global database.
The resultant Web site-based informational applications, or e-
information, do more than show the latest company news. As with
portals, they can serve as free advertising, attracting the information
researcher who is hungry to find a one-stop shop. They can comple-
ment customer relationship management systems by providing the
information desired at each point in the customer’s buying decision
process. Within an organization, they can tie the company together
and ensure faster, better decision-making. In some cases, such as
stock market reports and analysis, they can serve as money genera-
tors in their own right.
Along with these competitive advantages come built-in cost savings
 not only the cost savings from doing everything over the Internet,
outsourced or consolidated, but also the IT cost savings from simpli-
fying the administration of the database/application connections and,
thereby, saving key administrative costs. Moreover, users report that
developers writing to a common high-level database interface save



                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                          AberdeenGroup • 3
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   significant time in both development and upgrading data-intensive
                                   applications that cross data sources.
                                   Of equal importance is a side benefit: e-information can unify the
                                   enterprise’s archipelagoes of data. Whereas data warehouses failed to
                                   persuade data fiefdoms to merge, the Web site manager now has the
                                   political power to enforce common data standards on company divi-
                                   sions that seek the selling power of its Web site  but only if that
                                   manager plans ahead via an e-information strategy.
                                   A further note: Wringing Web site-displayed informational applica-
                                   tions, or e-information, from existing databases is not easy. Hence,
                                   competitive advantage is more durable and differentiation is easier.
                                   An early example of EII’s potential comes from the field of em-
                                   ployee self-service applications. EII plus an enterprise portal delivers
                                   an immediate impact to the bottom line by eliminating the need for
                                   “information intermediaries” that stand between the individual em-
                                   ployee and the information that he or she needs.
                                   The benefits of employee productivity EII do not end with the bot-
                                   tom line. For example, employee-productivity solutions based on EII
                                   provide additional information to employees, such as company poli-
                                   cies and standards or information about the company’s products, and
                                   they can deliver critical cross-database information in a just-in-time
                                   fashion. This information, in turn, can give users the ability to make
                                   higher quality, more rapid decisions because they can base their de-
                                   cision making on higher quality data that is more up-to-date. Visu-
                                   alization and personalization of the information can improve the em-
                                   ployee’s comprehension of the data. Improved accuracy of the in-
                                   formation can reduce the risk that company employees — or the
                                   company itself — will violate government regulations.
                                   However, one of the main potential advantages of EII is not yet on
                                   users’ radar screens — the ability to provide a common administra-
                                   tive locus for all major enterprise databases. Aberdeen research
                                   shows that database administration costs now dominate the TCO
                                   (total cost of ownership) of applications below the 500-user level,
                                   and they continue to increase in importance for all sizes of applica-
                                   tions. Users correctly identify the ability to manage multiple data-
                                   bases with one common interface as a major source of cost savings,
                                   but they often look to application servers as a method to achieve
                                   cross-database administration. However, full-featured EII, with its
                                   greater knowledge of database content, is much better suited to pro-
                                   vide database administration not only across a few applications at the
                                   Web site but also across many or all databases within the enterprise
                                   and even outside of it.
                                   In Chapter Three, Aberdeen describes how EII suppliers are meeting
                                   the challenge of delivering a “virtual federated database.” Aberdeen


All print and electronic rights are the property of Aberdeen Group © 2003
4 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



finds that providing a scalable, robust, low-administrative-cost solu-
tion is a tough nut to crack, but today’s EII solutions already provide
strong value-add by allowing the identification of new cross-
database, cross-application, and even extra-enterprise sources of in-
formation and data interrelationships. Today’s suppliers are, on the
average, larger and better able to provide supporting services than a
year ago, so users no longer need fear the perils of being pioneers.




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                          AberdeenGroup • 5
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                   Chapter Two:
                                   Summary of Findings
                                   •    Currently, EII is a small market  less than $200 million in size
                                         that lacks visibility to IT buyers. Over the last year, however,
                                        EII visibility has grown dramatically; this growth is especially
                                        due to IBM’s announcement of its Information Integrator prod-
                                        ucts.

                                   •    Buyers are beginning to see EII as a strategic infrastructure de-
                                        cision that can improve the agility of IT and enhance IT’s ability
                                        to quickly adapt technology to the rapidly changing needs of the
                                        business — especially the needs of e-business.

                                   •    The business benefit of EII increases exponentially with succes-
                                        sive integration of each related application and database. The
                                        connections between each additional information source and all
                                        the others have typically not been examined in most enterprises,
                                        and these connections  especially when combined with busi-
                                        ness process software  allow employee empowerment, greater
                                        insights into competitive advantage, more rapid response to cus-
                                        tomer inquiries and orders, and more effective integration with
                                        the databases of supply chain partners.

                                   •    EII solutions can enable and support today’s three high-priority
                                        e-business initiatives — customer relationship management, e-
                                        business integration across the supply chain, and Web-based
                                        employee productivity applications. Moreover, they offer a way
                                        to speed up business-process-integration efforts by allowing
                                        simultaneous access to multiple databases attached to multiple
                                        applications.

                                   •    Partial deployment of intranet, extranet, and Internet applica-
                                        tions without EII increases the difficulties of implementing EII,
                                        but also increases the costs of failing to implement EII by in-
                                        creasing the costs of administering unnecessarily complex archi-
                                        tectures.

                                   •    The EII market is still new, and most EII suppliers are small
                                        ones, such as MetaMatrix, Venetica, XAware, Enosys, and
                                        Nimble Technologies. Over the past year, large firms have be-
                                        gun adding the technology  BEA is contracting with Enosys
                                        to provide EII as part of BEA’s Liquid Data for WebLogic ini-
                                        tiative, and IBM’s Xperanto EII project has resulted in the new
                                        IBM DB2 Information Integrator products.


All print and electronic rights are the property of Aberdeen Group © 2003
6 • AberdeenGroup
                     Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



•   EII-type functionality is a cornerstone of today’s more success-
    ful enterprise portals and of the Web services that enterprises are
    beginning to build. Initial EII implementations are project spe-
    cific and seek to simplify developer interfaces in which portals,
    Web services, and similar software makes cross-database que-
    ries.

•   Many EII suppliers have experience in data integration and data
    warehouse ETL. These suppliers’ experience in optimizing data-
    transmission performance across databases means that today’s
    EII solutions are by no means bleeding edge; in fact, they often
    offer the robustness and scalability of mature technologies. The
    advent of larger suppliers — such as BEA, Business Objects,
    and IBM — ensures that IT buyers will run fewer risks of sup-
    plier failure or inadequate service.

•   The potential of the EII market will mean that major hardware
    and database suppliers will continue to enter the market within
    the next two years, either by acquisition or by partnerships with
    existing EII suppliers. The entry of these suppliers will continue
    to increase EII’s visibility, allowing them to parlay advanced
    technology-based solutions and industry relationships into large-
    scale enterprise opportunities. If successful, these suppliers will
    fuel a $250 million-plus market over the next two years. In-
    creasingly, EII solutions will be incorporated in portal, EAI,
    business intelligence, and business-process-integration solu-
    tions, making EII a key technology in a $7.5 billion market.

•   Over the next two years, EII will begin to form part of a larger
    “information aggregation” market aimed at delivering tools for
    strategic, proactive information management. EII will be a key
    enabler for identifying, managing, and leveraging competitive-
    advantage proprietary information and information relation-
    ships.

•   EII can play an effective role in exposing enterprise data to out-
    side suppliers in supply chain and e-business integration solu-
    tions.

•   The strength of industry partnerships  professional services
    and systems integrator firms, enterprise portal and application
    suppliers, and system infrastructure suppliers  and of the con-
    sulting that EII suppliers provide on how to best utilize EII is as
    critical to EII implementers’ success as the technology that the
    suppliers offer. IT evaluators should be looking especially to
    those EII suppliers that continually enhance their capabilities
    across all three of these dimensions.



                                 All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 7
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   •    One key EII supplier technology differentiator is the degree to
                                        which a supplier uses XML (Extensible Markup Language)
                                        technology for inter-database integration. The XML approach
                                        makes it easier to deliver the resulting aggregated data to a wide
                                        variety of inter- and extra-enterprise audiences. Another is sup-
                                        port for SOAP and Web services.

                                   •    Finding the appropriate skills to execute an EII project is not
                                        always easy, as EII implementation requires in-depth knowledge
                                        of the structure of existing enterprise databases. This will pro-
                                        vide a business opportunity for professional service suppliers
                                        and for application service providers (ASPs) that offer EII inte-
                                        gration services.

                                   •    Evaluators should favor EII solutions that allow users to define
                                        the databases to be integrated and provide developer-friendly
                                        user interfaces for doing so; support a wide variety of databases;
                                        and provide customized support for “de facto standard” applica-
                                        tion interfaces (e.g., enterprise portals) and delivery mechanisms
                                        (e.g., XML).

                                   •    At present, no EII solution offers administration across data
                                        sources. However, this capability is a key value-add to many us-
                                        ers. EII’s ability to drive down database administration costs
                                        will reduce per-application TCO significantly.

                                   •    In many organizations, the same team that monitors the server
                                        farm should make the EII buying decision. This requirement
                                        stems from the fact that understanding the enterprise’s e-
                                        business architecture is key to effective implementation of EII
                                        and new applications that leverage EII.

                                   To fully reap the benefits of EII, evaluators should also apply the
                                   following assessment criteria:
                                   •    Extensibility and reusability — The integration process should
                                        be extensible and reusable for the project at hand, as well as for
                                        future projects. The tools should be designed in such a manner
                                        that users can extend the tool from a per-project basis to an on-
                                        going enterprisewide usage.

                                   •    Flexibility — The solution should be able to fit into an existing
                                        architecture and handle new technologies without massive
                                        rewrites and without involvement from the supplier.

                                   •    Efficiency — The solution should be capable of operating across
                                        a wide range of performance levels (e.g., very fast, fast, moder-




All print and electronic rights are the property of Aberdeen Group © 2003
8 • AberdeenGroup
                     Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



    ate, and overnight) and integration models (e.g., asynchronous
    messaging and synchronous transaction).

•   Interoperability and breadth — The solution should understand
    the relationships between various database technologies and
    provide interfaces to interdependent middleware technologies
    such as application servers.

•   Cost-effectiveness — In the long term, the solution should be
    able to contribute to an organization’s bottom line by reducing
    the cost and risk of developing and maintaining custom, one-off,
    EII solutions. The upside value of a common repository of in-
    formation for all major enterprise databases is immeasurable.

•   Ease of maintenance — In EII projects that involve the integra-
    tion of many data sources, maintaining independently coded
    modules for each integration process is extremely resource in-
    tensive and, hence, costly. Using a single, flexible, and consis-
    tent development framework for each process will greatly re-
    duce the amount of personnel resources needed to maintain and
    develop the system.

•   Deployment ease and efficiency — Deploying the runtime envi-
    ronment should be easy, and the EII solution should allow de-
    ployment to a wide variety of target systems, ensuring optimal
    use of the enterprise network. Upgrade deployment should also
    be simple.

•   Ease of administration — EII modules will be distributed
    widely across an enterprise  just as enterprise-packaged appli-
    cation modules are today  and conceivably across enterprises
    where a supply chain relationship exists. These integration mod-
    ules will need to be managed and administered with no less
    diligence than is applied to current systems, networks, data-
    bases, and applications.

•   Industry acceptability — A large number of partners should
    incorporate the EII technology and deliver solutions based on it.

•   Technological innovation — The solution should provide and
    fully exploit the latest integration technology.




                                 All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 9
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                   Chapter Three:
                                   Market Definition and Dynamics

                                   What Is EII, and How Does It Work?
                                   EII is software that provides a “database veneer” that makes dispa-
                                   rate data sources appear as one database. It allows users to apply data
                                   management transactions to the pooled data, at a corporate or enter-
                                   prise level, in order to support applications that manage, present, or
                                   analyze the data in new ways.
                                   Currently, EII has three key technical characteristics:
                                   •    It is a software infrastructure. It is not an application; it supports
                                        the creation of applications, such as enterprise portals, that dis-
                                        play and analyze combined data. As software infrastructure, EII
                                        forms a key part of any overall e-business architecture.

                                   •    It links the second and third tiers of a typical enterprise architec-
                                        ture in a “many-to-one-to-many” approach. In other words, EII
                                        gives a wide variety of second-tier Web applications running on
                                        the second tier of an e-business architecture access to multiple
                                        back-end and legacy databases and file systems running on the
                                        third tier.

                                   •    It provides an enterprise-scale, integrated approach. Unlike to-
                                        day’s point-to-point application-to-database links, EII provides
                                        a common infrastructure on which all links are built, incremen-
                                        tally if the customer wishes. This common infrastructure can de-
                                        liver more rapid development, more cost-effective centralized
                                        administration of data from multiple data sources, and more
                                        flexible presentation and analysis of more data sources.

                                   All EII products usually offer certain basic components:
                                   •    A directory — This “database about databases” contains infor-
                                        mation about the data stored in the databases and often contains
                                        the same information that is stored in each database’s data dic-
                                        tionary, as well as information about the data that is shared
                                        across databases. A directory may also include information
                                        about “normalized” versions of the data  i.e., data converted
                                        into a common format that is particularly suitable for passing on
                                        to users, Web sites, or enterprise portals.

                                   •    Conversion capabilities — An EII solution must often convert
                                        incoming data from nonrelational to relational format or from
                                        relational to object format. When updates to back-end databases


All print and electronic rights are the property of Aberdeen Group © 2003
10 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



    are involved in a transaction, an EII solution must also perform
    the “inverse” task of converting a common format back into the
    target database’s format. Note that current EII solutions that
    support updates do so under strict conditions and/or the user’s
    control.

•   A database veneer — To the user, the EII solution should look
    like a database and, if possible, to the developer and administra-
    tor as well. Therefore, the EII solution should at least support
    standard SQL and querying transactions.

•   Front- and back-end communications — The EII solution
    should have a way of communicating with front-end programs
    and with users via programmatic and communications invoca-
    tions. It also should be able to send transactions to and receive
    results from back-end databases.

Figure 1 shows how EII fits into a typical architecture.

Figure 1: EII in a Typical Architecture




                                            Source: Aberdeen Group, July 2003




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 11
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   EII Is New Technology
                                   The IT buyer should carefully distinguish an EII solution from an
                                   ETL engine for data warehousing, an EAI solution, or a content
                                   management system. An ETL engine (sometimes called a “data inte-
                                   gration” solution) allows multiple streams of data to be converted to
                                   a common data warehouse data format and be loaded into the ware-
                                   house “in bulk” or in short “bursts.” However, it does not deliver
                                   that data to external targets, such as an enterprise portal; it does not
                                   make the source data appear as one database; and it does not typi-
                                   cally emphasize transactional access to the data.
                                   An EAI solution passes data among multiple packaged applications.
                                   It does not deliver that data to other external targets, such as a Web
                                   site or enterprise portal, and it often operates at the level-of-business
                                   processes rather than at the data level.
                                   A content management system allows users to place a wide variety
                                   of rich-media data into a common database and to operate on that
                                   data as if it were a single database. The content management system
                                   requires that data be uploaded to a common database, whereas the
                                   EII solution leaves that data in place. The typical content manage-
                                   ment system focuses on a variety of data, such as text, rich media,
                                   and business rules, whereas most EII solutions currently focus on
                                   relational operations that act upon relational and nonrelational data.

                                   EII in the User Site
                                   EII solutions serve three masters: the developer, the administrator,
                                   and the user.
                                   In order to serve the developer, the EII solution provides a bridge
                                   between the components and business logic residing in the second
                                   tier of the e-business architecture and back-end data sources — that
                                   is, it allows the developer to treat multiple, disparate databases, data
                                   management systems, and files as one gigantic enterprisewide data-
                                   base.
                                   To aid the administrator, the EII solution often (but not always) pro-
                                   vides a “metadirectory” of data and object types (e.g., an XML data
                                   dictionary) across multiple data sources, plus specific tools that al-
                                   low the administrator to monitor, maintain, and implement security
                                   for the virtual federated database.
                                   To aid the user, the EII supports the kind of operations on the virtual
                                   federated database commonly found in SQL (Structured Query Lan-
                                   guage), usually querying (decision support) and sometimes
                                   add/remove/update (online transaction processing [OLTP]). These
                                   features allow support for e-commerce and B-to-B OLTP, enable
                                   Web analytics queries across databases, and abet enterprise portal



All print and electronic rights are the property of Aberdeen Group © 2003
12 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



display and a combination of information from various data sources
for employees, customers, and partners.

Situations in Which Today’s Companies Often Feel a
Need for EII
Aberdeen clients find that the data connectivity projects for which
EII is a new tool are no small tasks. Typically, the project scope is
greater than anticipated, and the data connectivity problems involve
heterogeneous environments. IT administrators usually must perform
these integration projects in a complex environment and must rely on
a rapidly changing technology infrastructure. Other frequently en-
countered issues include the following:
•   A hodgepodge of legacy systems

•   Multiple legacy databases from multiple suppliers

•   Disparate operating platform environments  MVS, Unix,
    Windows NT and XP, wide area network (WAN), local area
    network (LAN), and Internet

•   Heterogeneous and geographically dispersed database manage-
    ment and file systems

•   Many communications protocols, including SNA, TCP/IP,
    HTTP, and XML/SOAP

Finally, there is no guarantee that the data-level integration will have
integrated the applications’ business processes as a seamless whole
when the project is done. Today’s data connectivity solutions deal
with transactions on a per-application, per-database basis, and they
do not make it easy to handle business processes that involve differ-
ent databases or different applications.
By contrast, EII:
•   Supports transactions across databases and applications, making
    the implementation of business processes much easier

•   Makes the reuse of integration techniques across heterogeneous
    environments much easier

•   Gives users the ability to implement integration solutions with-
    out needing detailed knowledge of the application infrastruc-
    ture’s specific underlying technologies.

Thus, for all of these issues and situations, EII provides added sim-
plicity leading to lower costs.



                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 13
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   Business Benefits of EII
                                   Aberdeen research shows that EII solutions can deliver not only cost
                                   savings but also a new kind of competitive advantage. As it becomes
                                   more difficult for e-enterprises to achieve differentiation via pack-
                                   aged or custom applications, the new frontier of competitive advan-
                                   tage becomes an IT organization’s ability to leverage proprietary
                                   information that its competitors cannot access. Much of this informa-
                                   tion is scattered across multiple databases, spreadsheets, and rich-
                                   media Web sites, making it difficult, if not impossible, to detect the
                                   connection between a customer’s existing product preferences and
                                   new products arriving via the supply chain and R&D. EII’s ability to
                                   amass metadata and carry out transactions across data sources allows
                                   the EII user to detect and display these key “relationships across data
                                   frontiers.”
                                   EII’s cost savings are nothing to sneeze at either. Many of today’s
                                   tasks in BI (business intelligence), CRM (customer relationship
                                   management), portals, and consolidation involve integrating business
                                   processes and information. In these cases, EII simplifies the devel-
                                   oper’s job by giving one interface and one set of metadata for all
                                   data sources, speeding the development of applications such as en-
                                   terprise portals. EII simplifies the administrator’s job by exposing
                                   key data that must be kept in synchronization across data sources.
                                   The benefits that EII delivers to the enterprise are often immediate.
                                   The ability to cross database boundaries, if used by applications,
                                   rapidly allows wider user access to key existing data for data mining,
                                   enterprise portals, or Web searches from inside or outside of the en-
                                   terprise. Establishing relationships between data sets across frontiers
                                   and data source types quickly enhances the data warehouse,
                                   empowering deeper data analysis and providing a more comprehen-
                                   sive view of the enterprise’s information assets. The development of
                                   today’s business-critical, data-intensive applications is speeded when
                                   programmers need only code for access to one data source rather
                                   than to several disparate ones. Key administrative costs show signifi-
                                   cant improvement the moment that administrators can manage data
                                   more easily across data-source frontiers.
                                   In real-world implementations, users are increasingly seeing specific
                                   instances of the following benefits:
                                   •    EII gives a broader picture of data to the user; e.g., by combin-
                                        ing data in Oracle and IBM DB2 databases.

                                   •    EII encourages IT administrators to identify data copies and re-
                                        lated data across databases, files, spreadsheets, and graphics and
                                        video. For the user, this means new insights into a company’s
                                        proprietary information  for example, an alert that a new



All print and electronic rights are the property of Aberdeen Group © 2003
14 • AberdeenGroup
                        Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



      product in which the customer has an interest is about to arrive
      and can be pre-ordered. For the administrator, this means a bet-
      ter understanding of the enterprise’s overall data relationships,
      so that, for example, the administrator can ensure that changes
      in one set of data changes other related data appropriately.

•     EII simplifies the developer’s job. Instead of writing custom
      code for each Java access to back-end data, the developer can
      write once for all accesses, whether they involve access to a sin-
      gle database or multiple ones. By combining EII with Web ser-
      vices, the developer can simplify the front end of the application
      (by making it a Web service) and the back end (by simplifying
      data access). By “abstracting” the interface to back-end data-
      bases, EII makes it easier to upgrade an application — there is
      “one application programming interface (API) to choke” when
      data access must be changed.

•     Although no EII products currently support this process, it
      should be possible to allow administrators to create scripts that
      perform database administration across databases and file sys-
      tems  for example, scheduling offline backup of Oracle and
      Microsoft databases in sequence, to load balance a backup.

Potentially, EII can be used as part of an overall IT strategy to iden-
tify, manage, and leverage the enterprise’s proprietary information
for competitive advantage (strategic information management). For a
full description of this idea, see Chapter Four.

Applying EII to Typical IT Tasks
When deftly used, a powerful EII tool can make a significant contri-
bution to many of an IT organization’s most critical tasks (Table 1).

Table 1: Ways to Use EII in Strategic Initiatives

Aim                              Way to Use EII
Integrate business processes     Write code in the applications to access an EII solu-
                                 tion rather than the databases so that the EII can
                                 determine if the transactions are part of a business
                                 process and update all data sources at the same
                                 time
Implement Web services inter-    Write a Web services front end to an EII solution
faces to existing information    rather than to each data source
Speed time to react to current   Provide an EII interface to the data for query
customer or supply chain data    purposes, bypassing the database server



                                     All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                            AberdeenGroup • 15
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   Aim                               Way to Use EII
                                   Speed time to develop new         Use an EII solution to front end for both the data ware-
                                   applications that leverage        house and other proprietary information, ensuring one
                                   proprietary information, such     set of code for all information access
                                   as portals
                                                                     Use an EII solution’s XML support to avoid coding
                                                                     object-to-relational translations or access to unstruc-
                                                                     tured data
                                   Audit all information in the      Create an EII metadata repository by importing (or
                                   enterprise for government         generating) metadata from the data warehouse, ETL
                                   requirements                      tools, and file systems and rich-media sites, and
                                                                     then write a SQL or Xquery query to the EII interface
                                   Cut IT costs                      Cut administrative costs by creating an administra-
                                                                     tive “veneer” over an EII tool that issues administra-
                                                                     tive commands to multiple data sources
                                                                     Cut development costs with an EII tool that allows
                                                                     developers to “write once” to supply data access to
                                                                     many applications
                                   Merge companies                   Combine the metadata of the two companies via an
                                                                     EII metadata repository
                                   Increase the amount of            Create EII across multiple databases that expands
                                   information available to users    the range of information available to an enterprise
                                                                     portal via the same interface
                                                                                    Source: Aberdeen Group, July 2003

                                   The following real-world examples show that EII is making a contri-
                                   bution:
                                         •   Merrill Lynch uses MetaMatrix to speed development and to
                                             allow analysts to access stock, product, and pricing data in
                                             IBM, Oracle, and Sybase databases.
                                         •   Aventis uses IBM to mine its Oracle databases and external
                                             nonrelational sources (genomics, proteomics) for drug re-
                                             search, and they are seeing significant speedups in R&D.
                                         •   Crystal Decisions uses IBM as an ISV to improve perform-
                                             ance in accessing large amounts of heterogeneous, distrib-
                                             uted data in thousands of data sources via Crystal Reports; it
                                             claims that response time has improved by up to 98%.

                                   Developments in the Database Market Drive the
                                   Need for EII
                                   The IT buyer should consider another reason for assessing EII tools:
                                   the state of the database, EBI (enterprise business integration), and
                                   portal markets.


All print and electronic rights are the property of Aberdeen Group © 2003
16 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



Periodically, database suppliers attempt to “own” the market by per-
suading organizations to migrate existing data to their database.
Organizations are perfectly willing to do so  after all, the cost of
administering multiple databases is a major and increasing compo-
nent of a summed IT total cost of ownership. However, moving all
key enterprise data onto Oracle, for example, has almost always
proven impossible to achieve. Legacy databases will continue to live.
As a result, organizations need a second-best alternative: to adminis-
ter, as far as possible, multiple databases as if they were from one
supplier. This alternative not only dramatically simplifies the job of
the database administrator but also eases the process of incorporating
a wide variety of data (spreadsheets, data in the form of text, multi-
media data) into the enterprise’s visible information portfolio. Thus,
a cross-database-supplier solution sharply reduces administrative
time required (and, hence, costs), and enlarges the scope of the data
administered.
At the same time, the need to aggregate data across databases and
deliver it to a wide variety of audiences is increasingly urgent. The
two key drivers of the market’s demand for cross-database solutions
are EBI and enterprise portals. As XML-based solutions proliferate,
they create a demand for more varied back-end data to feed to out-
side suppliers. Enterprise portals, by their nature, seek to display a
wide variety of data on a single screen, and ODBC- and JDBC-based
solutions simply require too much work of the programmer to be
implemented easily.
To meet these needs and overcome the difficulties associated with
existing solutions, EII acts as a many-to-many interface between the
user and multiple databases. Table 2 shows how this approach allows
the EII supplier to overcome the difficulties that have faced past ap-
proaches.




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 17
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                  Table 2: EII versus Traditional Approaches

                                   Single “Central”         Programmatic                  EII
                                   Database”                Interface (JDBC)
                                   Cannot keep up with      Can keep up only with         Can keep up with upgrades
                                   upgrades to other        upgrades common to all        common to all databases,
                                   databases                databases                     allows programming to covert
                                                                                          new data types to a standard
                                                                                          format, and allows users to
                                                                                          bypass the EII solution for key
                                                                                          new single-database features

                                   No programming           Low-level programming         High-level components and
                                   interface for cross-     interface for cross-          programming interface (in
                                   database-supplier        database-supplier             some cases, looking like a
                                   transactions             transactions                  single database) for cross-
                                                                                          database-supplier transac-
                                                                                          tions
                                   No provision for         No provision for handling     Directory that “tags” data that
                                   handling data defined    data defined in multiple      exists in multiple databases
                                   in multiple databases    databases

                                   No load balancing for    No provision for load         In many cases, built-in load
                                   transactions across      balancing for transactions    balancing for transactions
                                   multiple databases       across multiple databases     across multiple databases


                                                                                   Source: Aberdeen Group, July 2003




                                   Criteria for Buying an EII Solution
                                   EII solutions differ markedly in their ability to support developers,
                                   users, and administrators. Aberdeen recommends that IT buyers use
                                   different criteria according to which of these is the “main constitu-
                                   ency” for an e-business architecture. The following are key criteria
                                   for developers:
                                   •    Scalability of the development tools and of the applications built
                                        over the EII solution. Development tools should allow team and
                                        remote development (e.g., via a “developer network”); data-
                                        access mechanisms should provide optimization of queries and
                                        transactions.




All print and electronic rights are the property of Aberdeen Group © 2003
18 • AberdeenGroup
                     Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



•   Quality assurance to ensure robust e-business applications (e.g.,
    by providing the ability to persist data from the start of a cross-
    database transaction to the end, transparent to the developer).

•   Programmer productivity, by componentizing key EII opera-
    tions at the business level, allowing the developer to swiftly
    write EII-using applications, such as enterprise portals.

•   Flexibility to support a wide variety of platforms and architec-
    tures, by supporting open standards such as J2EE (Java 2 Enter-
    prise Edition), EJBs (Enterprise JavaBeans), and XML and by
    offering the ability to add new platforms and architectures easily
    and rapidly.

The following are key criteria for administrators:

•   Comprehensive cross-database administration features that al-
    low a database administrator to monitor and maintain multiple
    databases via EII as if they were one database, as well as coor-
    dinate with the database administration tools of back-end and
    legacy databases

•   Ability to monitor and tune transactions within the EII system in
    order to detect bottlenecks, preferably via a remote console

•   Connections to application-management and systems manage-
    ment products, such as CA Unicenter TNG

The following are key criteria for users:

•   Comprehensive support for a wide variety of back-end data-
    bases and other data sources

•   Easy “plugability” into front end e-commerce, B-to-B, and, es-
    pecially, enterprise portal implementations, as well as popular
    Web and application servers

•   Powerful cross-database transactional features, such as sophis-
    ticated querying

IT buyers should also consider the following overall criteria:

•   The supplier’s ability to serve as a “one-stop storefront” for
    system design and integration. The IT buyer should be espe-
    cially attentive and avoid “finger pointing” (the case in which
    multiple suppliers blame each other for a failure) because EII
    solutions typically involve complex connections to a wide vari-
    ety of supplier software.



                                 All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                        AberdeenGroup • 19
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   •    An EII solution’s ability to be a good foundation for a Web ser-
                                        vices architecture. Over the next two years, Web services im-
                                        plementations will become much more frequent, and EII must
                                        provide the standards support to integrate well with other up-
                                        coming Web services architecture components, such as a UDDI-
                                        based directory, as well as have the ability to access a wide vari-
                                        ety of intra- and extra-enterprise data sources that these Web
                                        services promise.

                                   Critical Technology Factors
                                   Aberdeen research has determined that the following five factors are
                                   key to understanding and differentiating EII solutions:
                                   •    Object and multimedia data support (including XML support)

                                   •    Non-database information access

                                   •    Specific support for front-end users and applications such as
                                        browser-based analytics, EBI, or enterprise portals

                                   •    Developer support

                                   •    Administrator support

                                   Object, Multimedia, and Non-database Support
                                   Data integration solutions will have a variety of constituents  in-
                                   ternal programs, Web site users, workgroups within the enterprise,
                                   partners/suppliers, internal workgroups or intranets via a LAN (local
                                   area network) or remotely, data miners, and IT administrators. These
                                   constituents vary widely in how they are accustomed to having data
                                   presented (Table 3). A good EII solution is, therefore, many-to-
                                   many: It draws data from a wide variety of data types, including ob-
                                   ject and multimedia ones, and delivers the data in a standardized
                                   format supported by each constituent.
                                   XML is the coming lingua franca (or common language) that allows
                                   this type of flexible response to a wide variety of constituents.
                                   Wrapping a transaction result in XML allows it to be delivered not
                                   only within the organization, where IT administrators can enforce
                                   XML support, but also to outside users via the Web, as well as part-
                                   ners and suppliers that are increasingly looking to XML for elec-
                                   tronic data interchange and EBI.
                                   The EII solution should also support access to text files, spread-
                                   sheets, graphics, video, and objects, as well as relational data. In-
                                   creasingly, business-critical data includes at least one of these non-
                                   traditional data types.



All print and electronic rights are the property of Aberdeen Group © 2003
20 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Table 3: EII Constituents and Their Data Needs

Constituent           Data Typically Accessed         Data Format Typically
                                                      Required
Internal              Relational                      Relational
programs
Web site users        Text, graphics, relational      HTML
Partners/suppliers    Relational, text                XML
Internal workgroups   Spreadsheet, text               HTML, graphical
or intranets
Data miners           Relational                      Graphical
Administrators        All types                       No requirements
                                             Source: Aberdeen Group, July 2003



Most EII suppliers are moderately advanced in supplying these fea-
tures. Most support access to a wide variety of data, although the
emphasis is usually on relational data. Most also have some variant
of XML support either available or planned. Few provide specific
support for a broad range of constituents.

Specific Front-End Support
Specific types of new solutions that many enterprises are implement-
ing call for specific support from an EII solution. The following are
major new application types that EII should support:
 •   Enterprise portals

 •   EBI

 •   Browser-based analytics

 Enterprise Portals
Today’s enterprise portal, via a rapid, straightforward implementa-
tion, allows the coordinated presentation and use of a much broader
range of information to B-to-C and B-to-B customers, as well as to
internal intranets and data miners. However, these connections work
best if integrated with the whole infrastructure of a Web’s architec-
ture. That includes the following:




                                   All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                          AberdeenGroup • 21
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   •    Middleware — e.g., Web servers, application servers, applica-
                                        tion messaging, and EAI

                                   •    Databases, as both second-tier caches and as “common” infor-
                                        mation stores

                                   •    Development tools and frameworks for rapid development and
                                        customization

                                   •    Hooks to integrate B-to-C and B-to-B supplier order processing

                                   •    XML formatting for Net market display

                                   •    Decision-support querying

                                   The EII solution stands between the enterprise portal and “common
                                   information store” databases, acting as a collection point for the data
                                   in order to forward it to the enterprise portal for display. The EII
                                   solution can also help with second-tier data caching, portal develop-
                                   ment, XML support, and querying across databases. In order to do so
                                   effectively, the EII solution can offer a caching database, its own
                                   development tools that are integrated with those of the enterprise’s
                                   portal-infrastructure solution, XML support, and its own querying
                                   facilities.

                                    EBI
                                   The EII solution can also serve to bypass the enterprise portal in pre-
                                   senting single-database and cross-database corporate information to
                                   partners and suppliers. By avoiding the user interface characteristic
                                   of an enterprise portal, the EII solution can simplify both many-
                                   database-to-one supplier and many-database-to-many-supplier inter-
                                   actions. However, this also means that the EII solution must supply
                                   the XML-standard support, tools for building connections on the
                                   supplier side, and security features characteristic of today’s EBI
                                   solutions.

                                    Browser-Based Analytics
                                   The promise of browser-based analytics is to extend the information
                                   analysis benefits of today’s data warehouses to a wider range of
                                   Web-based users and to simplify analysis so that it is not the prov-
                                   ince of a few highly skilled data miners. An EII solution can increase
                                   the scope and improve the ability to analyze real-time information of
                                   an analytics solution by allowing querying across a wide variety of
                                   data, not simply the data in a corporate data warehouse. To support
                                   browser-based analytics, EII solutions should supply some of the
                                   characteristics of a browser-based analytics solution in a cross-
                                   database situation  governors to avoid the “query from hell” that
                                   crowds out all other users from accessing a database, cost optimizers


All print and electronic rights are the property of Aberdeen Group © 2003
22 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



to maximize cross-database query performance, and tools to convert
back-end spreadsheet and relational data to graphical (pie chart, sta-
tistical) representations.
Most suppliers now provide specific features for browser-based ana-
lytics and portals, with fewer targeting EBI.

Developer Support
For both the developer and the administrator, the ideal EII solution
provides a “single database image,” in the same way that a good
clustering solution pretends that multiple systems are a “single-
system image.” This, in turn, means that the EII solution provides
most of the developer features of a high-end database  stored pro-
cedures, standard SQL support, a wide variety of APIs (including
support for ODBC, JDBC, and EJBs), and the ability to use the EII
solution’s directory to drive program design (e.g., by mapping direc-
tory “metadata” into common design tools such as Oracle’s and Ra-
tional’s design solutions). Note that the EII solution cannot offer one
of the advantages of the single database  the ability to run a pro-
gram inside the database’s process for high performance.
Most EII solutions are fairly far advanced in providing the developer
support that users need. Many solutions support stored procedures,
and they all support standard SQL. Some provide development tools
bundled with the application. Relatively few offer a full array of
high-end database APIs, and few provide mapping between the
metadata directory and design tools.

Administrator Support
Again, the EII solution should provide an image of a single database
to the administrator. However, this goal is much more difficult to
achieve for administrator support than for developer support. It ef-
fectively means that the EII solution must offer cross-database
backup/recovery, cross-database security, and interfaces to each da-
tabase’s own administrative tools for functions such as upgrade, re-
organization, and replication. The EII solution should also offer
SNMP (Simple Network Management Protocol) support to allow the
EII administrative tool to interact with common systems manage-
ment tools, such as CA Unicenter TNG.
Aberdeen characterizes the current administrator support tools of-
fered by EII suppliers as workable but basic. A few suppliers have
tools for transaction monitoring, user management, and security.
What is especially missing from all suppliers today is support for the
integration of these administrative tools with enterprise system and
network management facilities such as Unicenter TNG, Tivoli, or
OpenView. Current EII solutions are likely to be widely deployed in



                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 23
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   large-scale and highly distributed computing environments, so it is
                                   obvious that enterprise administrators will need to be able to manage
                                   EII nodes and modules just as they do distributed EBA (enterprise
                                   business application) system components.
                                   Notably, few, if any, EII suppliers provide support for cross-database
                                   administration scripting.




All print and electronic rights are the property of Aberdeen Group © 2003
24 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Chapter Four:
EII As Part of Strategic Information
Management
The proliferation of files, rich media, and traditional relational data,
as enterprise computing broadens in the number of users supported
and IT value-add, has become an inexorable long-term trend. Ways
to access this information are hindered by the differences in how this
information is stored, to the point where each Oracle database, group
of Excel spreadsheets, or Web site can require a separate program to
elicit data-based insights. Thus, the “frontiers” between information
sources delay competitive-advantage data analysis, add cost to the
process of creating queries and transactions across data boundaries,
and mire today’s efforts to leverage proprietary information into
long-term revenue enhancement in a hopeless game of “catch-up”
with enterprises’ growing cache of information.
Over the years, specialized tools and technologies have arrived that
tackle the problem of information frontiers. These technologies have
now reached a point of maturity in which the IT executive can use
them strategically, in what Aberdeen calls strategic information
management. The cross-frontier technologies that support strategic
information management are what Aberdeen calls information ag-
gregation technologies.
As an information aggregation tool, EII has an important role to play
in strategic information management, in concert with other such
tools. This chapter catalogs the other technologies that constitute
information aggregation, shows how EII and other information ag-
gregation tools can be used (singly or in combination) to abet strate-
gic information management, and examines the state of the art that
IT strategists can use today in attempting strategic information man-
agement.

A Brief Introduction to Strategic Information
Management
Today’s IT strategist, seeking to increase competitive advantage, can
focus primarily on the application resources or the data resources of
the enterprise. Until recently, it made most sense to focus on applica-
tions. Strategic solution management has sought to identify, manage,
leverage, and add to the application software that delivers value-add
to the enterprise, customer, or supply chain.
Over the last two years, IT organizations’ focus has shifted strongly
toward cost cutting. Cost squeezes at both ISVs (independent service


                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 25
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   vendors) and major IT shops have nearly halted the development of
                                   new, competitive-advantage applications or major Web efforts.
                                   Meanwhile, CIOs and ISV CEOs have resorted to cost-saving meas-
                                   ures, such as offshore development outsourcing. However, strategies
                                   based solely on cost savings typically reach a point of no return 
                                   the ultimate result of long-term cost cutting is a “hollowed-out” cor-
                                   poration.
                                   Today, the obvious place to search for a cost-effective, long-term
                                   advantage is, therefore, in proprietary information that competitors
                                   cannot readily duplicate. For example, Amazon.com may seek to
                                   combine information about customers’ preferences with information
                                   about upcoming book releases, notifying them when a new book of
                                   interest is about to be published. However, this information is usu-
                                   ally locked in widely differing and often aged data sources. In an-
                                   other example, much Wall Street investment research depends on
                                   data from sources that range from Excel spreadsheets to reports, up-
                                   to-the-minute news articles, Web pages, and historical stock data-
                                   bases. Simply writing new code or buying a packaged business
                                   intelligence application does not do the trick. The IT strategist also
                                   needs to focus on making the information more widely available;
                                   therefore, strategic information management is needed.
                                   Strategic information management has a short- and a long-term com-
                                   ponent. The short-term job of strategic information management is to
                                   deliver available information consistently, no matter the variations in
                                   user demand  “on-demand” information. Tools that support the
                                   short-term job include storage management and SAN (storage area
                                   network)/NAS (network-attached storage) management (especially
                                   virtualization), database and cross-database administration, system
                                   and systems file administration, and Web site administration.
                                   The long-term job of strategic information management is to iden-
                                   tify, manage, support the leveraging of, and add to the information
                                   resources of the enterprise. Tools that support the long-term job(s)
                                   include metadata repositories and cross-database administration.
                                   Tools that support the “information aggregation” discussed here are
                                   just beginning to surface, and tools that allow automated searches of
                                   sources of new proprietary or extra-enterprise information that can
                                   be used for competitive advantage are not yet visible in the market.

                                   What Is Information Aggregation, and Why Does
                                   It Matter?
                                   Information aggregation is Aberdeen’s term for a collection of tools
                                   and technologies that have arrived over the last seven years and that
                                   allow users to combine data across data-source frontiers. Information
                                   aggregation includes the following:



All print and electronic rights are the property of Aberdeen Group © 2003
26 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



•   Tools to move or copy data from multiple “source” data sources
    to a “target” aggregated-data repository, which can be used to
    carry out such operations as queries across differing data types

•   Tools to access data from multiple data sources and then com-
    bine it temporarily for specific purposes, such as cross-database
    queries

Aberdeen arbitrarily calls this “information aggregation” rather than
“information integration” for two reasons. First, compared with the
term “integration,” “aggregation” better captures the idea that data
can be combined both permanently and temporarily. Second, “infor-
mation integration” may be confused with “enterprise information
integration” — a new sub-technology of information aggregation —
as well as various recent efforts by suppliers to coin the terms data
integration, enterprise application integration, and information inte-
gration.
Information aggregation currently includes the following types of
tools:
•   Data migration and bulk download tools

•   Replication and ETL tools

•   Data warehouses and data marts

•   Enterprise operational data stores

•   Mid-tier operational data stores

•   EII tools

•   Federated databases

Any information integration technology delivers immediate benefits
to the enterprise. The ability to cross database boundaries used by
applications gives wider user access to key existing data for data
mining, enterprise portals, or Web searches from inside or outside
the enterprise. Establishing relationships between data sets across
frontiers and types of data sources empowers deeper data analysis,
leverages proprietary information more effectively for competitive
advantage, and provides a more comprehensive view of the enter-
prise’s information assets. Development is speeded when program-
mers need only to code for access to one data source rather than sev-
eral disparate ones. Administrators often cut costs by managing more
easily across data-source frontiers.
When IT administrators wish to manage information strategically,
information aggregation can play a key role in leveraging existing


                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 27
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   information. Information aggregation’s ability to establish relation-
                                   ships between data sets in widely different data sources helps the IT
                                   strategist identify key data and key “data connections” by placing
                                   that “information about information” in one place. Moreover, typical
                                   side effects of information aggregation tool use are the gathering of
                                   cross-data-source metadata and the ability to administer aggregated
                                   data and metadata. Thus, the information management strategist can

                                   Table 4: Strategic Uses of Information Aggregation

                                   Key Task                     Value-Add of Information Aggregation
                                   Identify                     ETL tools and data warehouses can create a cross-database
                                                                metadata repository.
                                                                EII tools can add file and rich-media data-source metadata.
                                   Manage                       Data warehouses and operational data stores, fed by data-
                                                                movement tools (data migration, data cache, ETL), allow full
                                                                administrative operations across at least one copy of aggre-
                                                                gated relational data sources and, sometimes, file and rich-
                                                                media data sources.
                                                                EII and federated databases potentially allow full administra-
                                                                tive operations across all copies of relational, file, and rich-
                                                                media data sources.
                                   Leverage                     Data warehouse, federated database, and EII APIs allow
                                                                broader, more quickly developed application access to rela-
                                                                tional data sources.
                                                                EII extends application access to file and rich-media data
                                                                sources.
                                                                Enterprise portals extend application access to a broader
                                                                range of users.
                                                                Operational data stores, federated databases, and EII can
                                                                allow update as well as query access.
                                   Find new use                 No effect (still a manual process)

                                                                           Source: Aberdeen Group, July 2003
                                   also identify and manage information across frontiers more effec-
                                   tively. Table 4 suggests specific ways in which specific information
                                   aggregation tools can be useful in each key strategic information
                                   management task.
                                   The culmination of these benefits occurs when an IT shop decides to
                                   implement full-fledged strategic information management. By apply-
                                   ing each information aggregation tool appropriately and strategi-
                                   cally, the IT strategist can potentially attain an “almost enter-


All print and electronic rights are the property of Aberdeen Group © 2003
28 • AberdeenGroup
                    Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



prisewide” metadata repository, an almost enterprisewide data-
source administration tool, and an almost enterprisewide informa-
tion-leveraging tool to constantly search the enterprise’s ever-
growing information store for new ways to combine the information
for competitive advantage.




                                All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                       AberdeenGroup • 29
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                   When to Apply What Information Aggregation
                                   Technology
                                   Figure 2 shows how information aggregation technologies can be
                                   combined in an overall architecture.

                                   Figure 2: Example of Information Aggregation Architecture




                                                             Source: Raining Data Inc. and Aberdeen Group, March 2003


                                   The State of the Art in Information Aggregation

                                   Data Migration and Mass Download Tools
                                   Data migration and mass download tools were the first information
                                   aggregation tools, and they linger in today’s ETL products that can
                                   also be used for bulk data migration and download. For example,
                                   Evolutionary Technologies Inc. (ETI) continues to provide data mi-
                                   gration capabilities in its “data integration” product.
                                   Moreover, the enterprise-database-supplier consolidation in the late
                                   1990s spawned several tools for migrating from one database to an-
                                   other  e.g., from Sybase and Informix to IBM relational databases


All print and electronic rights are the property of Aberdeen Group © 2003
30 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



or from these databases to Oracle. In addition, several major enter-
prise database suppliers offer tools to migrate files and/or rich-media
“objects” into their relational databases  e.g., Oracle and IBM 
or to move or copy large amounts of other data  e.g., IBM to move
IMS data into a DB2 database.
Most of these tools focus on migration from one relational database
to another. The general-purpose data migration and ETL tools are the
most flexible, allowing migration across suppliers and, in some
cases, across a wide array of data types. Therefore, they are often
preferred for long-term strategic information management because
they can be reapplied in many different cases in which permanent
data movement is desired or in which database consolidation will
likely be ongoing.
Table 5 shows one way to categorize information aggregation tech-
nologies.

Table 5: Taxonomy of Information Aggregation Tools

 Tool             Characteristics            Typical Uses Today
 Data migration   Typically move large       End use of a database by
 and mass         amounts of data at once,   moving it to another database
 download         either permanently or      (e.g., move to another data-
                  intermittently, almost     base supplier)
                  always “offline” (when
                                             Allow database operations
                  the target data store is
                                             (especially queries) to be
                  not operating)
                                             applied to a data source (e.g.,
                  Typically one source,      PC files) by moving/copying it
                  one target                 inside the database
                                             Backup and disaster recovery




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 31
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                     Tool               Characteristics              Typical Uses Today
                                     Replication and    Copy (one way) one           Refresh a data warehouse or
                                     ETL tools          piece of data at a time,     data mart from mission-critical
                                                        either continuously as       OLTP (online transaction
                                                        data changes or in           processing) relational data-
                                                        spurts, usually offline      bases, typically daily
                                                        Transform data to differ-    Reflect local-office data to a
                                                        ent format to improve its    central site for backup and
                                                        quality or to convert to a   querying (“mass-deployment”)
                                                        common format
                                                                                     Synchronize handheld/laptop
                                                        Typically multiple           and central databases
                                                        sources, one target
                                                                                     Copy data between embed-
                                                                                     ded databases for packaged
                                                                                     applications from different
                                                                                     suppliers to integrate busi-
                                                                                     ness processes (EAI)
                                     Data               Copy (one way) large         Support querying, data min-
                                     warehouses         amounts of data at a         ing, and business intelligence
                                     and data marts     time, usually daily, al-
                                                                                     Provide metadata repository
                                                        most always offline
                                                                                     of key business information
                                                        Typically multiple
                                                        sources, one target
                                                        Usually includes ETL tool
                                                        Allow querying of aggre-
                                                        gated data, but not up-
                                                        date
                                                        Often extremely large
                                                        (terabytes)
                                     Enterprise         Copy (one way), typically    Combine key customer and
                                     operational        changes in data (imme-       supply chain data to detect
                                     data stores        diately)  often from the    and query relationships
                                                        store/cache to multiple
                                                                                     Combine data from key busi-
                                                        targets, always online
                                                                                     ness applications to integrate
                                                        Typically multiple           business processes
                                                        sources, one target
                                                                                     Improve speed-to-react to
                                                        Often use replication or     business conditions (re-
                                                        ETL tool                     freshed more frequently than
                                                                                     data warehouse)
                                                        Allow querying and up-
                                                        date                         Improve visibility of current
                                                                                     (less than a week old) data
                                                        Often large, but not so
                                                        large as data warehouse




All print and electronic rights are the property of Aberdeen Group © 2003
32 • AberdeenGroup
                  Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



Tool          Characteristics             Typical Uses Today
Mid-tier      Copy (one way) changes      Combine key customer and
operational   in data (immediately)      supply chain data to detect
data stores   often from the              and query relationships
              store/cache to multiple
                                          Combine data from key busi-
              targets, always online
                                          ness applications to integrate
              Typically multiple          business processes
              sources, one target
                                          Improve speed-to-react to
              Often use replication or    business conditions (re-
              ETL tool                    freshed more frequently than
                                          data warehouse)
              Allow querying and up-
              date                        Improve visibility of current
                                          (less than a week old) data
              Smaller than enterprise
              operational data store      Improve performance and
                                          scalability of key applications
                                          and “composite” applications
EII           Leaves the data sources     Queries and updates across a
              as is                       wide variety of data sources
                                          (including file and rich media)
              Often uses real-time ETL
                                          without creating copies to
              tool
                                          synchronize
              Allows querying and
                                          Creates a more global meta-
              (less frequently) update
                                          data repository than any other
              Must transform data for     IA tool
              each query
                                          Allows cross-data-source
                                          development
                                          Potentially, allows cross-data-
                                          source administration



Federated     Leaves the databases as     Combines differing relational
database      is                          databases from the same
                                          supplier or two suppliers
              Allows querying and up-
              date
              Must transform data for
              each query


                                         Source: Aberdeen Group, July 2003




                               All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                      AberdeenGroup • 33
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                    Replication and ETL Tools
                                   If an IT organization chooses to copy data from a data source to data
                                   “target,” then changes in that data must likewise be copied from
                                   source to target. If an IT organization needs up-to-date sources and
                                   targets at all times, the data copies must be kept in synchronization
                                    every transaction must see the same value for the data at all times,
                                   no matter what copy is changed first. In OLTP situations, that means
                                   using two-phase commit technology (a technical method of achiev-
                                   ing two-way synchronization between two information bases). The
                                   drawback of this technology (as with all two-way synchronization
                                   technologies) is that it is low performance  it can take a long time
                                   to carry out a single multiple-copy update, much less a high-volume
                                   stream of them. Thus, in synchronized OLTP systems, only a few
                                   data copies are realistically possible.
                                   In data warehousing environments, the situation is simpler. The data
                                   warehouse is not intended as an OLTP environment; it is in no hurry
                                   to record changes to data items. Therefore, all a data warehouse
                                   needs is one-way synchronization, or data replication. The OLTP
                                   “feeder” databases record a change in the data and, at some later
                                   point, it is replicated to the copies in the data warehouse database.
                                   Of course, even in a data warehousing context, replication is not
                                   without cost. Updates that occur while the data warehouse is running
                                   means write locks that can slow querying. Selective updates of some
                                   data items, although related data items are not updated until the end
                                   of the day, may result in inconsistent data. However, these problems
                                   are typically easy to handle  slower querying by delaying updates
                                   until times of low querying (such as the end of the day)  enabling
                                   mass replication to update data all at once and inconsistent data to be
                                   avoided by careful data warehouse design. Deft use of replication,
                                   therefore, can result in far more timely data on which data miners
                                   can operate.
                                   Replication tools abound in the market, and the major database sup-
                                   pliers offer many of them. These tools may allow replication from
                                   multiple suppliers’ relational databases to a particular supplier’s da-
                                   tabase, but not vice versa. However, because it is easy to find an-
                                   other replication tool to perform “reverse replication,” one-way rep-
                                   lication is not a major drawback.
                                   ETL tools combine both data migration and replication tool technol-
                                   ogy. As with data migration technology, they allow the translation of
                                   data formats from widely different source formats into widely differ-
                                   ent target formats via a process of extracting, transforming (with
                                   cleansing), and loading. As with replication tools, they can copy data
                                   in real time and in small amounts. An ETL tool can be combined
                                   with replication technology to ensure that when data is changed, that
                                   change is sent on to the target database.


All print and electronic rights are the property of Aberdeen Group © 2003
34 • AberdeenGroup
                       Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



Initially, ETL tools were targeted primarily at the data warehousing
market, but the advent of EAI has meant that ETL tools are also
packaged as part of EAI solutions, often as “adapters” that translate
between the data formats of major packaged applications such as
those provided by SAP and PeopleSoft. Recently, ETL tools have
appeared in the offerings of EII suppliers.
The wide array of ETL tools in the market is often from suppliers
that specialize in data warehousing add-ons, or EAI, or both  sup-
pliers such as Compuware, Data Junction, ETI, Sybase, TIBCO, and
webMethods. IT strategists should note that ETL tools are excep-
tionally flexible and, therefore, applicable as the base technology for
a wide variety of information aggregation needs.

 Data Warehouses and Data Marts
Data warehouses aggregate data primarily, and often exclusively, for
decision support. A data warehouse’s data is derived from outside
OLTP and “mixed” databases. The databases’ data is fed to the deci-
sion-support information base via either mass downloads involving
careful cleansing of the data (typically via an ETL tool) or by one-
way synchronization, in which changes in specific data items are
replicated in the data warehouse information base. Specialized que-
rying or analytics tools allow specialized “data miners” to access the
data and derive insights about patterns of sales or similar competi-
tive-advantage information. Data marts are smaller data warehouses
 often for specific functions within an enterprise — that feed a
large central data warehouse.
Experience has shown that the data warehouse has major limitations
that prevent it from serving as the ultimate information aggregation
of all data in the enterprise. First, it can grow only to a certain size
before performance becomes too poor; hundreds of terabytes may
sound like a large number, but the typical major organization stores
far more data than that. Second, in order to service the “query from
hell,” the data warehouse must focus on queries to the exclusion of
all other operations, including the updates that accompany key op-
erations, such as customer order entry. Third, holders of line-of-
business data or other data are often reluctant to register it in the data
warehouse’s metadata repository because it brings no immediate
business benefit. Fourth, refreshing a large data warehouse daily is a
massive operation that prevents warehouse usage for hours, so keep-
ing the warehouse more than one day or one week behind is, practi-
cally speaking, impossible.
Nevertheless, the data warehouse is often the best base on which to
begin implementing strategic information management. It is not only
the largest aggregation of data in the enterprise; it is also the largest
aggregation of metadata.


                                   All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                          AberdeenGroup • 35
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   All major enterprise database suppliers  IBM, Microsoft, Oracle,
                                   and Sybase  offer extensive data warehousing support, as does
                                   NCR-Teradata.

                                    Enterprise Operational Data Store
                                   The idea of the operational data store is to combine the key data
                                   from multiple data sources or “systems of record” in one database
                                   that  unlike a data warehouse  allows the updating of the data.
                                   An enterprise operational data store focuses on collecting business-
                                   wide, mission-critical data. This approach gives the enterprise opera-
                                   tional data store the ability to aggregate the data of a data warehouse
                                   and provide near real-time “data freshness,” giving users the ability
                                   to react to changes in business conditions  such as shifts in buying
                                   patterns  instantaneously. However, the price of adding updates is
                                   a sharp decrease in the amount of data that can be stored in the op-
                                   erational data store and the amount of sophisticated data mining that
                                   can be applied to it. In other words, in an enterprisewide operational
                                   data store, users can react more quickly to insights, but gain fewer of
                                   them.
                                   All enterprise databases can be used as enterprise operational data
                                   stores when combined appropriately with real-time ETL or replica-
                                   tion tools. The trick to successfully implementing an operational data
                                   store is not so much picking the right database as picking the right
                                   data to go into the database. However, the process of picking the
                                   right data is precisely what makes either an enterprise or a mid-tier
                                   operational data store such a valuable tool for strategic information
                                   management. All data is not equal; the strategic information manager
                                   needs to distinguish proprietary data that can be leveraged, and that
                                   type of data is frequently found in an operational data store.
                                   The idea of an enterprise operational data store, pioneered by suppli-
                                   ers such as Unisys, is now generally accepted across the industry,
                                   and most major enterprise database suppliers now offer support for
                                   implementation of enterprise operational data stores (often referred
                                   to simply as “operational data stores”). Note that many enterprise
                                   operational data stores combine only data from relational databases.

                                    Mid-tier Operational Data Stores
                                   A mid-tier operational data store is a recent idea with distinct merits
                                   for strategic information management. A high-performance database
                                   serves as a persistent, long-term cache, not only for one but also for
                                   several databases from one or several suppliers. This “cache” data-
                                   base, unlike most caches, provides all of the functionality of an op-
                                   erational data store. This functionality allows users not only to speed
                                   the performance of each data source but also to combine key data
                                   from each data source, reflecting changes to this key data back to all
                                   data sources. In other words, a mid-tier operational data store can


All print and electronic rights are the property of Aberdeen Group © 2003
36 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



provide all of the benefits of an enterprise operational data store (al-
though often on a smaller scale), as well as improved performance
and scalability for mission-critical databases and applications.
As with EII and EAI tools, the enterprise and mid-tier operational
data stores can store metadata about relationships across databases
and, therefore, provide users, administrators, and developers with the
benefits of an EII solution on a much smaller scale. In addition, EII
and operational data stores can be combined quite effectively. Recent
examples of mid-tier operational data stores include Raining Data’s
TigerLogic XML Data Management Server (XDMS) and Ipedo In-
formation Hub.

EII Tools
The potential for EII as an enabler of strategic information manage-
ment cannot be overestimated. EII can serve as the focal point for
gathering an unprecedented amount of metadata about the enter-
prise’s proprietary information. Potential EII tools can administer
across as wide a swath of the enterprise’s data sources as desired. EII
allows leveraging data relationships across data sources without the
effort of moving or copying the data.

 The Usefulness of Combining Mid-tier ODS and EII
Users should note that EII tools typically do not include any persis-
tence technology, so information that is extracted, transformed, and
integrated for each request can cause performance overhead com-
pared with an ODS — although the ODS does not permit access to
as large a data store as an EII tool. Thus, a combination of EII and an
operational data store is often a better combination of data-store size
and performance than either would be separately.
This is true not only for decision-support querying but also for tasks
such as order entry that require data updates. A mid-tier ODS’s abil-
ity to index data from other data sources allows users to not only
query these sources  an ability that all EII tools share  but also
insert, remove, and update them (actions that relatively few EII tools
permit).
Moreover, a combined EII/mid-tier ODS lets the information strate-
gist “have it your way”  (1) to merge data into an ODS, where
swift access to real-time data for rapid decision making is para-
mount; (2) apply a cross-data-source query rather than moving data,
when an ODS “tops out” or operational data must be combined with
data warehouse historical data; or (3) rapidly react to new floods of
data by moving some into the ODS and access the rest via EII.




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 37
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   Federated Database
                                   The federated database may well be an idea whose time has passed;
                                   however, it is still worth noting as an alternative approach to infor-
                                   mation aggregation that may yet pan out. The idea of a federated
                                   database is to provide the same data management software to differ-
                                   ent data sources. Thus, in Informix’s federated approach, the same
                                   version of Informix OnLine accesses object and relational data pre-
                                   viously served by different Informix databases, allowing the same
                                   queries, administration, etc., to be used on both data sets. Other vari-
                                   ants would allow the same operations across multiple suppliers’ data
                                   sources or across widely different data sources.
                                   The major difficulty so far with this one-size-fits-all approach is that
                                   it has proved very hard to make one operation fit all data sources —
                                   e.g., to make query optimization appropriate to relational data effec-
                                   tive in optimizing queries of video-heavy large Web objects. That is
                                   compounded by the fact that the amount and types of data in the
                                   typical enterprise are continually proliferating, so the federated data-
                                   base implementer is chasing a moving target.
                                   Periodically, an enterprise database supplier will propose to get
                                   around this problem by simply providing different “sub-database”
                                   software within the same database for each data type, then persuad-
                                   ing the organization to migrate all other data in the enterprise to its
                                   database. Three years ago, it looked as if Oracle might actually
                                   achieve this goal  but that was a market mirage. Data migration of
                                   all legacy databases and upgrading of all legacy applications, de-
                                   pending on each legacy database, is simply too hard for most if not
                                   all enterprises.
                                   The result is that, for now, the vision of one enterprise-standard da-
                                   tabase or of a federated database that can encompass all data sources
                                   is pretty much dead. Organizations can still apply a federated data-
                                   base to combine two existing data sources from the same supplier, if
                                   that supplier supports it, but that is only a minor step toward infor-
                                   mation aggregation.

                                   Action Items
                                   Clearly, today’s information aggregation tools have enormous poten-
                                   tial to support strategic information management by helping to iden-
                                   tify, manage, and leverage existing proprietary competitive-
                                   advantage data. Just as clearly, no one has combined these tools in an
                                   overall tool set to do this.
                                   The action item for IT buyers, therefore, is to assess existing infor-
                                   mation aggregation tools within their enterprises, supplement the
                                   tools where necessary, and create a long-range plan to use them to
                                   identify, manage, and leverage the enterprise’s data sources. A key


All print and electronic rights are the property of Aberdeen Group © 2003
38 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



to success in this effort is the implementation of EII not merely on a
per-project basis, but also as an ongoing effort to amass metadata
about all enterprise data sources, including nonrelational ones. The
political payoff for “data fiefdoms” that provide this metadata is
greater exposure to customers via the Web and greater cost cutting as
database administrators operate across data sources.
The action item for suppliers is to actually implement a full-fledged
information aggregation tool set. That would mean not only combin-
ing data migration/mass download, replication/ETL, data ware-
house/data mart, enterprise and mid-tier operational data store, and
EII tools, but also defining  and aiding customers in defining 
when to use each of these tools for strategic information manage-
ment.
In most cases, the pioneers of new computing technologies take the
arrows. Because the component technologies are already in most
cases field proven and well supported, all that the pioneers of strate-
gic information management risk is a relatively small added invest-
ment. By contrast, the benefits to the first mover are not only imme-
diate competitive advantage but also short- and long-term cost sav-
ings plus long-term entrenched competitive advantage.




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 39
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                   Chapter Five:
                                   Market Forecast and Segmentation

                                   Key Technologies for EII Initiatives
                                   As stated in Chapter Two, EII is a business issue and, if implemented
                                   correctly, should improve the overall bottom line. Moreover, taking
                                   the appropriate first steps on an EII project can have a significant, posi-
                                   tive effect on the final success of an entire information integration ini-
                                   tiative.
                                   By implementing EII solutions, enterprises can isolate their applica-
                                   tions from the extensive differences in back-end databases and un-
                                   derstand the potential of an open, heterogeneous, multisupplier com-
                                   puting infrastructure.
                                   Enterprises are increasingly adopting EII-type approaches as part of
                                   their efforts to identify and rationalize their information assets. Ear-
                                   lier efforts to create a “universal repository” containing metadata
                                   about all of a corporation’s data, typically as part of a data warehous-
                                   ing effort, failed because lines of business had no incentive to hand
                                   over control of their information assets to a corporate IT department.
                                   In contrast, today’s lines of business clearly have a strong bottom-
                                   line incentive to make their information available to new customers
                                   via the Web, partners and suppliers via EBI, and internal employees
                                   via employee self-service portals.
                                   The problem to date has been that information integration ap-
                                   proaches have been fragmented, sometimes incompatible, and typi-
                                   cally not so cost-effective as an overall EII solution.

                                   Aberdeen EII Technology Segmentation Model
                                   The Aberdeen EII segmentation model represents the various tech-
                                   nology components that often complement an EII tool in an overall
                                   solution. The aim of the model is to identify suppliers that are most
                                   likely to complement an EII solution. Aberdeen defines the various
                                   EII “complementary technologies” in order to provide a clear under-
                                   standing of the functionality provided by each technology category.
                                   Aberdeen research indicates that integrating an EII solution with
                                   related technologies will be the most attractive integration solution
                                   for enterprises that seek to integrate their information in a global,
                                   cost-effective way.
                                   Aberdeen notes the following complementary technologies:




All print and electronic rights are the property of Aberdeen Group © 2003
40 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



•     EAI technologies

•     Database technologies

•     Application server technologies

•     XML messaging technologies

EAI
EAI suppliers’ products offer the ability to pass data between enter-
prise applications. Their key technologies complementary to EII are
data transport, data integration, and business process support.

 Data Transport
In an EAI solution, data transport technology (“adapters” or ETL)
provides support for communications between objects and applica-
tions, providing greater performance than standard file transfers. In
addition, it provides flexibility in routing data or objects to many
recipients on multiple platforms, regardless of system or network
failures. Thus, EAI data transport can be useful in transporting data
between an EII solution and an enterprise application or in adding
application-specific data to the EII solution’s information base.

 Data Integration
In an EAI solution, data integration technology provides the ability
to manage a disparate set of application data sources and targets us-
ing a tool set. This tool set allows the user to seamlessly flow data
from step to step in a process without having to go outside of the
tool. A data integration product has the ability to manage an in-
creased volume or number of similar objects  for example, the
volume of data transformations or the number of users accessing a
data mart. The scalability of the data integration tool is linear  if
the volume of data transformations doubles, then the time to process
the data integrations should also double. A data integration product
can manage a nonlinear increase in difficulty — measured in the
workload of individuals or systems or in the functional limitations of
software — because of new intricacies when working with the inter-
relationships between or among objects.
The application of EAI data integration tools in EII is straightfor-
ward. Therefore, EAI data integration can serve as an alternative way
to combine data sources.

 Business Process Support
A business process flow is inherently composed of multiple, distinct,
work-based processes or steps. Usually, it is carried out over or
through multiple organizations and managerial levels within an en-


                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 41
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   terprise. Conceivably — and usually — not all of the personnel and
                                   organizations involved in the process will be users of the same line
                                   of business. The best process flow will need to reach out beyond its
                                   normally associated application boundaries to provide for enter-
                                   prisewide process-flow automation.
                                   In an EAI solution, support and integration are done at the level of
                                   business processes, not transactions. The solutions enable the easier
                                   reuse of the integration techniques across heterogeneous environ-
                                   ments; organizations can also implement integration solutions with-
                                   out needing detailed knowledge of the application infrastructure’s
                                   specific underlying technologies — a likely situation when the other
                                   application resides in a different company. This capability can be
                                   particularly useful when meshing an EII solution with the business
                                   processes in another company via EBI.

                                   Database Technologies
                                   Two sets of database supplier technologies are particularly useful as
                                   a complement to EII:
                                   •    Open veneers

                                   •    Integrated file and multimedia storage capabilities

                                    Open Veneers
                                   Sybase offers a product that provides a common front end to its own
                                   and other relational databases. This “veneer” lets developers write to
                                   a common SQL and allows users to issue the same transaction to any
                                   relational database. In combination with the integrated file and mul-
                                   timedia storage capabilities of suppliers such as Oracle, it allows
                                   relational access to a wide variety of data types. It does not allow the
                                   combination of data or a transaction to cross multiple suppliers’ da-
                                   tabases.
                                   An open veneer such as Sybase’s can significantly ease the EII solu-
                                   tion’s task of accessing multiple databases.

                                   Integrated File and Multimedia Storage Capabilities
                                   IBM/Informix (IDS), Oracle (Oracle8i and Oracle9i), and Microsoft
                                   (SQL Server 7.0 and 2000) have made a particular point of allowing
                                   users to fold both multimedia/object data and desktop files into their
                                   relational databases. IBM DB2 and Sybase Enterprise Server also
                                   provide some nonrelational-data-type and file access capabilities.
                                   These capabilities allow the user to fold nonrelational data into an
                                   existing database in order to give the EII solution easier access to a
                                   wide variety of information and to provide greater ability to combine




All print and electronic rights are the property of Aberdeen Group © 2003
42 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



that information by using the database’s cross-data-type-transaction
capabilities.

XML Messaging Technologies
XML is a descendant of SGML (Standard Generalized Markup Lan-
guage) and a sibling of HTML (HyperText Markup Language) 
both ISO (International Standards Organization) and Internet stan-
dards. XML was developed to add data management features similar
to those of SGML, but went beyond HTML by keeping the data and
its context or metadata together in the same “message.” As a result,
when the information displayed on a Web page is stored in XML, a
price change can be inserted on a Web page immediately by chang-
ing the data portion of the XML, without reprogramming the entire
page.
XML also provides great improvement in the portability of data,
inside and outside of the enterprise. By agreeing to accept the defini-
tion of data embodied in an XML message, another department, an
enterprise portal, or an outside supplier can access, display, or re-
spond to that data. To ease the use of this type of EBI in particular
industries, an abundance of XML dialects (properly termed “vocabu-
laries”) have emerged.
XML databases store data as XML objects in an object-oriented da-
tabase. Although XML databases do not replace enterprise-scale
databases, they are useful not only for permanent or “cache” storage
of XML data but also as a repository for XML information used in
XML-based interactions; as a second-tier or “cache” server for gen-
eral-purpose Web data processing; and as a “common language”
database for storing a wide variety of data types, such as files, mul-
timedia data, and relational data. In such small-to-medium scale da-
tabase situations, a typical advantage includes the storing of data in a
widely useful format, supporting key XML-using applications with
less customization and providing greater processing speed for trans-
actions involving XML.
XML messaging is, therefore, a highly flexible way for the EII solu-
tion to communicate with both front-end programs/users and back-
end databases. Moreover, an XML database can be a high-
performance way for the EII solution to store cache data and direc-
tory metadata.

Combinations of Technologies
Combinations of these technologies are often useful in particular EII-
related situations. Consider, for example, the products of Progress
Corp. The ObjectStore XML database can be used as a mid-tier
ODS. The PeerDirect InnerEdge and OuterEdge Server replication
solution can deliver high performance in ETL and data migra-


                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 43
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   tion/download. The SonicMQ XML messaging products support
                                   enterprise and cross-enterprise XML messaging infrastructure,
                                   allowing the exchange of information in such applications as EBI.
                                   The Progress OpenEdge “embedded infrastructure” allows
                                   organizations to apply the foregoing products plus an application
                                   server and enterprise database in creating scalable industry-specific
                                   applications rapidly.

                                   Summarizing the Model
                                   Figure 3 shows Aberdeen’s EII technology segmentation model,
                                   which can be used to categorize various EII and related offerings
                                   based on technology and functionality. The model also illustrates the
                                   interdependence of the various technologies.

                                   Figure 3: EII Technology Segmentation Model




                                                                                   Source: Aberdeen Group, July 2003




All print and electronic rights are the property of Aberdeen Group © 2003
44 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



Table 6 describes how the suppliers profiled in this report fit within
the Aberdeen segmentation model.

Table 6: EII and Related Suppliers

Aberdeen EII Segmentation Model
Technology Segmentation                Examples of Suppliers
EAI technology                         Actional, BEA, Celcorp, Crossweave, iWay,
                                       SeeBeyond, TIBCO, Viewlocity, Vignette, Vitria,
                                       webMethods, CNT, MITEM, Tempest, Candle,
                                       CommerceQuest, Compaq, Compuware, Darc
                                       Software, DataMirror, Dharma, ETI, IBM, Level
                                       8 Systems, Neon Systems, OST Business
                                       Rules, Percussion, Scribe Software, Sybase,
                                       Taviz Technology, Transoft, EnterWorks, Mer-
                                       cator, PTC, Software AG, WRQ
Database technology                    IBM, IBM/Informix, Microsoft, Oracle, Sybase

XML messaging                          Progress/Excelon, Ipedo, Metapa, Software AG
                                       (database); ArborText, Altova, and SoftQuad
                                       (publishing); DataChannel, Sequoia Software,
                                       Sybase, Bowstreet, SilverStream, Oracle, and
                                       iPlanet (enterprise portal); webMethods, InfoTe-
                                       ria, IBM, Sun, i4i, Whitehill, and Inera (EBI);
                                       Vitria, Contivo (EDI); HP, IBM, Sun, Microsoft
                                       (Web services)
EII solution                           Attunity, Business Objects, Ipedo, XAware,
                                       MetaMatrix, Venetica, BEA, Nimble Technolo-
                                       gies, IBM (Information Integrator)
                                            Source: Aberdeen Group, April 2003



Table 7 categorizes the EII suppliers based on the core technology
solutions that they provide.




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 45
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                  Table 7: EII and Related Suppliers

                                   Aberdeen EII Segmentation Model
                                   Technology Segmentation                    Examples of Suppliers
                                   EAI Technology                             Actional, BEA, Celcorp, Crossweave, iWay,
                                                                              SeeBeyond, TIBCO, Viewlocity, Vignette, Vitria,
                                                                              webMethods, CNT, MITEM, Tempest, Candle,
                                                                              CommerceQuest, Compaq, Compuware, Darc
                                                                              Software, DataMirror, Dharma, ETI, IBM, Level
                                                                              8 Systems, Neon Systems, OST Business
                                                                              Rules, Percussion, Scribe Software, Sybase,
                                                                              Taviz Technology, Transoft, EnterWorks, Mer-
                                                                              cator, PTC, Software AG, WRQ
                                   Database Technology                        IBM, IBM/Informix, Microsoft, Oracle, Sybase

                                   XML Messaging                              Progress/Excelon, Ipedo, Metapa, Software AG
                                                                              (database); ArborText, Altova, and SoftQuad
                                                                              (publishing); DataChannel, Sequoia Software,
                                                                              Sybase, Bowstreet, SilverStream, Oracle, and
                                                                              iPlanet (enterprise portal); webMethods, InfoTe-
                                                                              ria, IBM, Sun, i4i, Whitehill, and Inera (EBI);
                                                                              Vitria, Contivo (EDI); HP, IBM, Sun, Microsoft
                                                                              (Web services)
                                   EII Solution                               Attunity, Business Objects, Ipedo, XAware,
                                                                              MetaMatrix, Venetica, BEA, Nimble Technolo-
                                                                              gies, IBM (Information Integrator)
                                                                                  Source: Aberdeen Group, April 2003




All print and electronic rights are the property of Aberdeen Group © 2003
46 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Growth Forecasts
Most of the suppliers profiled in this report do not break out reve-
nues associated with “data integration”  a frequently used supplier
term for what we now call EII. Moreover, for suppliers, the dividing
line between EII, EAI, content management, and ETL tools for data
warehousing is frequently not a clear and precise one. Aberdeen has
assigned to EII only revenues in which the primary purpose of the
EII solution is to integrate data across databases for delivery to tar-
gets other than data warehouses. This category includes a small pro-
portion of the EAI and ETL markets, as well as projects that involve
an enterprise portal or EBI. Revenues from suppliers that do not pro-
vide a full-fledged EII solution are not included.
Based on available data regarding supplier revenue, Table 5 repre-
sents current market revenue and projected market growth. Aberdeen
believes that the overall market will grow by 80% in 2003, with
growth being especially fueled by the need to rationalize existing e-
business efforts. Web services will contribute significantly to EII
revenues over the next year, and they will be increasingly important
from 2004 onward.
These estimates are strongly dependent on the overall growth of the
high-tech sector of the economy. Specifically, if enterprises continue
to delay spending on new initiatives, such as business process auto-
mation, into the first quarter of 2004, these numbers will be overes-
timates. If enterprises advance new initiatives in the third quarter of
2003, then these numbers will be underestimates.
Table 8 shows that, as yet, no single supplier dominates the market.
Typically, suppliers do not release revenue figures. Therefore, these
Aberdeen estimates are based on the number of employees and the
number of years that a particular product has been offered.

Table 8: EII Supplier Revenues (Aberdeen Estimates,
Projected over 2003)

Supplier                          Revenues
Business Objects                  $15 million
Attunity                          $4 million to $7 million
BEA                               $25 million
XAware                            $4 million to $7 million
IBM                               $60 million
MetaMatrix                        $10 million



                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 47
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                   Nimble Technologies                    $4 million to $7 million
                                   Venetica                               $7 million to $10 million
                                                                                    Source: Aberdeen Group, July 2003

                                   Aberdeen believes that the professional services needed to success-
                                   fully implement an EII initiative will become more easily measurable
                                   as revenue over the next 6 to 12 months. However, Aberdeen’s field
                                   experience indicates that, for every dollar spent on software applica-
                                   tion licenses, $1.25 to $1.50 is spent on professional services to im-
                                   plement integration of the application and the resultant data.
                                   Table 9 shows our estimate of the size of closely related markets. As
                                   these markets expand and mature, their products increase the demand
                                   for EII as an integral part of the solution. Thus, EII’s impact extends
                                   far beyond its own market.

                                  Table 9: Revenues for Markets Related to EII

                                   Markets                         2002               2003              2004

                                   EAI                             $2.2 billion       $2.6 billion      $3.0 billion
                                   Content management              $1.2 billion       $1.6 billion      $2.0 billion
                                   Portal                          $1.5 billion       $2.2 billion      $2.8 billion
                                   Total                           $4.9 billion       $6.4 billion      $7.8 billion
                                                                                   Source: Aberdeen Group, April 2003




All print and electronic rights are the property of Aberdeen Group © 2003
48 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Chapter Six:
Aberdeen Observations

Impact of Major IT Trends
Aberdeen research shows that EII is on the critical path in corporate
efforts to achieve comprehensive, information-leveraging, e-business
architectures. Piecemeal efforts to link back-end databases to Web
sites, EBI, and enterprise portals have left a rat’s nest of point-to-
point connections between Web server, application server, or appli-
cations and back-end Web text/graphics, workgroup files, or enter-
prise databases. EII’s many-to-one-to-many approach is, therefore,
well suited to rationalizing connections between internal and external
users and key corporate information. However, its ability to do so is
strongly affected by today’s key IT trends, as described below.

Application Servers
Over the last two years, application servers have been steadily incor-
porating many of the middleware functions of an e-business architec-
ture, including load balancing, acting as a development framework
(hence, the increasing linkage of application servers and develop-
ment tool sets), and application management. One of the main selling
points of an application server has been that it is more manageable,
scalable, and efficient because application servers can integrate data
from a variety of heterogeneous sources, including back-office ap-
plications and databases. Therefore, over the next two years, many of
today’s EII solutions may possibly be incorporated in an application
server  as BEA WebLogic for Liquid Data already does (Enosys).
However, this might require the reprogramming of much of the exist-
ing code that is used to access back-end databases. Therefore, IT
buyers examining an application server that incorporates an EII solu-
tion should carefully assess its ability to support existing database
connections without recoding.

The Role of Java
Enterprise JavaBeans (EJB), the Java specification for server-side
components, has received significant interest because of its ability to
simplify and accelerate the development of business applications. By
providing services such as transaction and resource management,
persistence, mobility, versioning, scalability, and security, it enables
the easier development of robust, mission-critical applications that
access back-end databases — and using fewer developers. The wide
availability of EJB 2.0 components means that programming data
access in Java is becoming much easier, and EII is a complement that


                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 49
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   makes the job easier still. In other words, because Java is well suited
                                   for EII and vice versa, the continued adoption of Java improves the
                                   market for and usefulness of EII.

                                   Extensible Markup Language (XML)
                                   XML is now a de facto, as well as du jour, standard. All major sup-
                                   pliers provide XML functionality, and many smaller suppliers focus
                                   on XML-based messaging, allowing enterprises to not only
                                   communicate externally but also drive business processes internally
                                   (and externally). As noted above, XML is particularly well suited for
                                   EII solutions because it can provide a common language for trans-
                                   mitting transactions from back-end data sources to internal and ex-
                                   ternal users and programs. A proliferation of XML standards is caus-
                                   ing difficulties for users in implementing XML connections with
                                   particular customers, partners, and suppliers, but that does not dimin-
                                   ish the basic value proposition of EII. XML is, increasingly, a check-
                                   list item in EII solutions. A related upcoming standard is XQuery,
                                   which supports standardized querying on XML-formatted data.

                                   Emphasis on Cost-Effective Administration
                                   The economic downturn has caused enterprises to focus on rational-
                                   izing existing architectures for greater cost-effectiveness, rather than
                                   for building new e-business applications. A key area of concern is
                                   administration, as the costs of administrative personnel mount while
                                   hardware and networking costs decline. In response, suppliers have
                                   provided more automated and more administrator-friendly solutions.
                                   EII promises to reduce the administrative burden by offering a single
                                   administrative interface to multiple back-end databases, but, at pre-
                                   sent, the lack of administrative support in most EII solutions makes it
                                   appear that EII is an added cost burden rather than a cost savings. In
                                   fact, EII reduces administrative costs by simplifying user-to-database
                                   connections and making cross-database transactions more visible to
                                   the administrator. Over the next 18 months, increasing support for
                                   administration in EII products will allow administrators to begin to
                                   monitor multiple databases from different suppliers as one database.
                                   Moreover, connections to systems management tools will allow EII
                                   to take its proper place in overall systems administration.

                                   Enterprise Portals
                                   An enterprise portal allows the enterprise to coordinate the data dis-
                                   played across applications and to fully leverage all major business-
                                   critical company databases. Moreover, a portal allows the enterprise
                                   to expose these data to new markets, such as Net markets and ex-
                                   changes in general. Along with these competitive advantages come
                                   built-in cost savings — not only the cost savings derived from doing
                                   everything over the Internet (outsourced or consolidated) but also the


All print and electronic rights are the property of Aberdeen Group © 2003
50 • AberdeenGroup
                       Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



IT cost savings derived from simplifying the administration of the
database/application connections, thereby saving key administrative
costs. There is a side benefit of equal importance: e-information can
unify the enterprise’s “data islands.” However, both of these “data-
base benefits” will fail to emerge unless the enterprise portal uses EII
technology to provide cross-database operations and displays. There-
fore, EII is critical to the long-term success of enterprise portals.
Likewise, a successful enterprise portal is a prime “target of oppor-
tunity” for users seeking to apply EII to initial projects promising
major return on investment.

Web Services
Enterprises that take advantage of the Web in their businesses inevi-
tably begin to implement Web services. The fundamental idea of
Web services is to apply the tried-and-true idea of a service  a cen-
tral piece of software that carries out specific functions that its users
demand — to the Internet. The Web service is self-describing be-
cause it contains enough information about itself to allow any Web
user or Web application to find out what it does and then to use it,
making it a highly flexible service. The Web service’s ability to use
other Web applications to carry out complex tasks makes it feature
rich and offers enterprises a new way to mine the Web for competi-
tive-advantage applications and content.
Moreover, Web services allow IT to write one server version  no
client version is needed  that can be automatically deployed across
all the servers in the organization. It thereby becomes instantly avail-
able to the entire organization as well as global customers and a
partner base of millions. These technical advantages also lead to
broader business benefits, such as lowering the cost of doing busi-
ness, allowing companies to achieve much greater efficiencies from
using broadly available applications, and giving the organization
greater ability to adapt quickly to changing conditions. These advan-
tages are so great that Aberdeen expects implementing Web services
and upgrading existing applications to be Web services will be the
major new efforts of most enterprises over the next two years. EII
plays a role in this effort because it provides a common access point
from Web services to the “enterprise substrate”  key proprietary
information. However, in order to allow organizations to fully lever-
age EII’s potential in abetting Web services, EII solutions must pro-
vide SOAP support, frameworks supporting Web service develop-
ment tools, and, if possible, a Web service provider interface. For
further details, see the Aberdeen White Paper, EII and Web Services
(July 2002).




                                   All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                          AberdeenGroup • 51
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   Supplier Success Factors
                                   To meet long-term user flexibility needs, suppliers should continue
                                   to integrate various middleware technologies into a smoothly work-
                                   ing whole. The aim is to enable IT to create a distributed environ-
                                   ment in which applications and data move instantly, cost-effectively,
                                   and flexibly to where a user needs them.
                                   A supplier’s EII solution should be extensible and reusable for the
                                   project at hand, as well as for future projects. The tools should be
                                   designed in such a manner that users are able to extend the tool from
                                   a per-project basis to ongoing enterprisewide usage.
                                   In the long term, the EII supplier’s tools and solutions should be able
                                   to contribute to an organization’s bottom line by reducing the costs
                                   of application design, development, deployment, and, above all,
                                   maintenance. Suppliers should also satisfy overall user criteria, such
                                   as scalability and robustness.
                                   Outside resources should be leveraged through strategic partnerships.
                                   A potential bottleneck for present EII suppliers could be customer
                                   demand for services. In-house services adapted to EII, key partner-
                                   ships with systems integrators, as well as the professional services of
                                   major infrastructure suppliers, can alleviate this bottleneck. It is also
                                   important to build partnerships with suppliers of complementary
                                   software products (e.g., enterprise portal infrastructure suppliers).
                                   Achieving customer satisfaction and delivering an expanding set of
                                   products will differentiate the new market leaders. Today, few EII
                                   providers have embraced integration with enterprise management
                                   products.
                                   Suppliers should capitalize on increased interest in cost-effectiveness
                                   via solution consolidation. This trend provides EII suppliers with the
                                   opportunity to sell the ability to consolidate databases without the
                                   pain of physically merging them.
                                   An unplumbed area is the use of EII for an “information audit.” Ser-
                                   vice providers can use automatic “repository population” tools in EII
                                   solutions to walk into a customer site and gain a map of major data.
                                   This map, like asset management maps, can be highly useful in rec-
                                   ommending ways of better leveraging information.

                                   Success Factors for Organizations
                                   Successful organizations establish business goals to be achieved by
                                   the implementation of an EII technology (e.g., increased sales and
                                   reduced cost of customer service). They identify the appropriate EII
                                   technology required to meet these goals and create metrics to gauge
                                   the successful use of the EII technology.



All print and electronic rights are the property of Aberdeen Group © 2003
52 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



EII initiatives may involve integrating many sources and targets
while maintaining independently coded modules for each integration
process. This process is extremely resource intensive. Using a single,
flexible, and consistent framework for each process will greatly re-
duce the amount of personnel resources needed to maintain and de-
velop the system.
An EII solution should be built on an architecture that has the ability
to scale, support, and introduce new technologies within a globally
distributed environment. In addition, the solution should provide the
flexibility to add multiple servers as a system grows, as well as the
ability to use preconfigured components that “hook” into legacy da-
tabases.
Aberdeen advises IT buyers to demand that the EII suppliers define a
path toward an integrated overall architecture. Choose the supplier
with the best combination of a strong current solution, a good vision,
and a solid, open position within the industry. Plan to prototype
within the next six months and to spread EII across the enterprise
architecture within the following year.
When selecting EII suppliers, organizations should look for two
critical attributes:
    1. Does the supplier have in-depth knowledge of the major da-
       tabases to be integrated? Can the supplier demonstrate that
       the integration will be reliable, scalable, and possible? Is the
       supplier able to provide references that show systems in pro-
       duction?
    2. Does the supplier have credibility (e.g., systems in produc-
       tion) in claiming to be able to support all of the relevant in-
       formation integration initiatives in which your company ex-
       pects to engage? Does the supplier have the consulting ex-
       pertise or partnerships that can bring best practices from
       other integration implementations to bear on your business
       problems and opportunities?
The IT buyer should proactively involve users. The executives; busi-
ness analysts; financial, marketing, and support representatives; and
sales professionals who will eventually be using the information
need to be involved in the integration requirements. These individu-
als can provide helpful insight into actual usage patterns and what
will and will not be useful. Incorporating their opinions into the inte-
gration and deployment process also creates a sense of ownership
and excitement on the part of users for the new integrated application
systems.




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 53
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   Aberdeen Observations and Conclusions
                                   Aberdeen research shows that there now exists a distinct market for
                                   EII that is beginning the “high-end user per-project” stage. This
                                   market is driven by enterprises’ needs to rationalize existing access
                                   to multiple databases, both to cut administrative costs and to lever-
                                   age competitive-advantage, cross-database, proprietary information.
                                   EII solutions do this by providing many-to-one-to-many mechanisms
                                   to take a wide variety of back-end data sources, merge them into a
                                   common format, and pass them to a variety of front-end users and
                                   programs.
                                   EII solutions also provide specific value-add to enterprise portal and
                                   EBI solution upgrade. Enterprise portals’ focus on providing end-
                                   users with access to multiple information sources means that EII’s
                                   ability to provide cross-database data and/or support cross-database
                                   transactions simplifies the developer’s job and the portal’s architec-
                                   ture. EBI solutions can use EII to expose more data to the outside,
                                   with more control over a single (EII) exposure point.
                                   EII can also play an important role in Web services implementations.
                                   A “Web-servicized” EII solution can provide easier access by other
                                   Web services to local, remote, and cross-company data.

                                   Positioning and Capabilities

                                   Market Segmentation
                                   As a new market with relatively few entrants, EII also has relatively
                                   few segments. The most meaningful division is between suppliers
                                   that focus primarily on EII (e.g., MetaMatrix) and suppliers for
                                   which “data integration” is one among many middleware products or
                                   that focus strictly on business intelligence (e.g., Business Objects).
                                   Some suppliers focus on EII for content databases; others focus on
                                   EII across data marts and decision-support databases.
                                   As noted earlier, Aberdeen believes that the technology in the EII
                                   market is moving toward a full single database image or “veneer”
                                   that makes multiple databases look like a single database. As a result,
                                   suppliers that focus primarily on EII and can draw on knowledge of
                                   database technology are at a significant advantage in the next two
                                   years.

                                   Technology Interdependency
                                   Aberdeen research has indicated that one key criterion to being a
                                   long-time player in the EII market space is the ability to develop key
                                   alliances. These alliances provide complementary products, com-
                                   plementary services, efficient access to new markets, and joint ef-
                                   forts in development.


All print and electronic rights are the property of Aberdeen Group © 2003
54 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



Aberdeen research indicates that EII suppliers will benefit most not
from integration with each other’s technologies, but via partnerships
with full-function “infrastructure solutions” for particular enterprise
needs. Again, the most attractive partnerships will allow better sup-
port for enterprise portals, EBI, and Web services. Other useful part-
nerships will combine EII and a mid-tier ODS, or EII and EAI.
This is clearly a window of opportunity for Web infrastructure sup-
pliers such as Sun, IBM, BEA, and Sybase. By establishing partner-
ships with EII suppliers or acquiring EII solutions, these suppliers
can position themselves as a stronger long-term solution in enterprise
portals, EBI, and Web services. So far, IBM and BEA have been
quickest to respond. By contrast, suppliers such as Oracle and Mi-
crosoft have not shown a full appreciation of the potential of EII.
EII suppliers have begun to establish alliances with professional ser-
vice organizations (PSOs). The A-list comprises the Big Five PSOs
(Andersen Consulting, Deloitte & Touche, Ernst & Young, KPMG,
and PricewaterhouseCoopers) and industry service heavyweights
(e.g., HP and Sun). Aberdeen expects the extension and deepening of
those relationships over the next two years.

Distribution and Implementation
Many EII suppliers are young companies, in the range of one to four
years. The market’s awareness of most of these suppliers’ EII identi-
ties began in 2001. Thus, the EII suppliers discussed here, except for
Business Objects, BEA, and IBM, are still mostly in their formative
stages.
Among these newcomers, there is no common distribution model for
the EII market. All of these suppliers seek to define themselves as
software solution suppliers that rely on their own systems integration
efforts, third-party implementers, and training to address customer
implementation requirements. Sales models are primarily direct, yet
some companies have initiated alternative distribution or original
equipment manufacturer (OEM) strategies as significant future dis-
tribution and revenue-enhancing strategies. Direct sales capabilities
were limited at the start of 2003, but continue to significantly ex-
pand.
The established suppliers  IBM, BEA, and Business Objects 
have already established channels, which they are beginning to lev-
erage. Especially promising is the “services-led” model, in which EII
comes bundled with extensive services for system integration and
advice on strategic uses of EII and other software infrastructure tools
and services.




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 55
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   Major Forces

                                   Mergers and Acquisitions (M&A)
                                   Because it is such a new and small market, most “newcomer” EII
                                   suppliers have not had the capital to pursue acquisitions. Aberdeen
                                   expects that over the next two years, most M&A activity will con-
                                   tinue to center on larger “infrastructure solution” providers acquiring
                                   “newcomer” EII suppliers.
                                   In the case of full-function EII solutions, a barrier to these acquisi-
                                   tions is that being acquired by one provider locks the EII solution
                                   supplier out of the installed base of other providers  for example,
                                   being acquired by IBM might lock an EII supplier out of Oracle’s
                                   installed base. However, because these installed bases are far larger
                                   targets of opportunity than EII suppliers currently have, Aberdeen
                                   expects some acquisitions to proceed despite the barrier.

                                   Standardization and Integration
                                   EII solutions are and must be firmly founded on standards such as
                                   SQL, ODBC/JDBC, and EJB. A key future standard is XML, and
                                   Aberdeen expects all EII suppliers to wrap their transactions in XML
                                   over the next two years, if they have not done so already.
                                   As noted above, key targets for integration over the next two years
                                   will be application servers and Web services infrastructures. Appli-
                                   cation servers are already sources of legacy, cross-database code. In
                                   order to simplify the Web architecture, they will need to merge that
                                   code with code written directly on an EII framework. Some EII solu-
                                   tions that have not done so already will also need to define connec-
                                   tions to Web services infrastructure solutions as another data “tar-
                                   get,” as well as to define their solutions as Web services.

                                   Success Factors
                                   Suppliers must work toward achieving customer satisfaction.
                                   Delivering an expanding set of products will differentiate the new
                                   market leaders. Furthermore, when choosing an EII supplier, users
                                   should look for the critical attributes listed in User Success Factors.
                                   There were significant deployments in 2003, so IT buyers should
                                   expect to have enough reference accounts to interview.
                                   Organizations should apply the evaluation criteria cited in Chapter
                                   Two to ensure that they are implementing an integration platform
                                   that is flexible, extensible, and scalable.

                                   The Future
                                   Six enabling technologies will have a strong impact on EII solutions
                                   during 2003: application servers, Java, XML, database administra-


All print and electronic rights are the property of Aberdeen Group © 2003
56 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



tion technologies, enterprise portals, and Web services. These tech-
nologies are critical to delivering long-term value-add from an EII
implementation and to simplifying an e-business architecture using
EII.
Organizations need to coordinate their initiatives for EII and EBI as
well as EII and architecture rationalization or cost cutting. Doing so
correctly will avoid another decade of slow, costly, and mostly un-
necessary piece-by-piece data integration, and it will allow
organizations to invest the capital saved into key new initiatives,
such as Web services.




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 57
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                   Chapter Seven:
                                   Supplier Profile
                                   As noted above, many EII suppliers profiled in this report are small,
                                   recently created companies. The reader should, therefore, pay addi-
                                   tional attention to their partnerships to determine their ability to sup-
                                   port complex enterprise information architectures.




All print and electronic rights are the property of Aberdeen Group © 2003
58 • AberdeenGroup
                       Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




MetaMatrix, Inc.
680 Fifth Avenue
10th Floor
New York, NY 10019
(314) 739-3190, Ext. 120
www.metamatrix.com

Market Position
MetaMatrix sees itself as a provider of an “open, rapid-deployment
system” for helping enterprises “integrate data sources and manage
metadata” globally. MetaMatrix aims its EII solution especially at:
•   Financial services

•   Government

•   Migration services

•   Large and midsize systems integration companies

•   CRM/call center applications

•   Enterprise portals

•   ASPs

•   Business intelligence, knowledge management, and data ware-
    housing

•   B-to-B and B-to-C exchanges

•   Other custom applications

MetaMatrix’s full set of features, ability to tie in to formalized de-
velopment methodologies, and administrative support make it a
prime candidate for large enterprises with long-term EII, architecture
rationalization, and administrative cost-cutting plans, or for enter-
prises seeking to rapidly develop or upgrade complex, business-
critical, information-driven applications. MetaMatrix’s EII solution
is also appropriate for a range of more focused efforts, including
meshing with EAI solutions to coordinate business processes and
business rules or providing dynamic querying across relational and
rich-media “content” data such as Internet feeds or time series data,
as well as supporting EBI, enterprise portals, and BI/Web analytics.
Although MetaMatrix’s sophistication may make it “overkill” for



                                   All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                          AberdeenGroup • 59
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   small organizations, its breadth of functionality makes it useful for
                                   most if not all EII efforts of large enterprises.
                                   The MetaMatrix product set is a full-featured EII solution with
                                   MetaBase, a modeling tool based on MOF (OMG’s Meta-Object
                                   Facility), with a searching and browsing tool (MetaViewer), a re-
                                   pository manager (MetaData Repository Manager), and MetaMatrix
                                   Server, with transaction support, development features, administra-
                                   tive tools, a “single database image,” ETL “connectors,” and access
                                   control, as well as publish/subscribe capabilities. MetaMatrix differ-
                                   entiates its EII solution especially by its:
                                   •    Abstraction Layer — MetaMatrix allows creation of virtual da-
                                        tabases, which are a logical layer between the disparate data
                                        sources and the application developer or application. The layer
                                        integrates the information so that from the outside it looks like a
                                        single database to the developer or the application. Inside this
                                        layer, MetaMatrix metadata mappings point to the sources of
                                        each element.

                                   •    Two way XA-compliant transactions.

                                   •    Scalability owing to the solution to being entirely built in Java.

                                   •    Interoperability with a wide variety of front-end programs via
                                        XMI, JDBC, ODBC, SOAP, and XML support.

                                   •    Metadata management system based on standards such as MOF,
                                        XML Metadata Interchange (XMI), Common Warehouse Meta-
                                        Model (CWM), UML (Uniform Modeling Language), and other
                                        relevant OMG standards.

                                   •    A modeling tool that allows abstraction of existing metadata
                                        (improving programmer productivity by reducing custom cod-
                                        ing), as well as creation of user-defined “metamodels.”

                                   •    Sophisticated metadata-search, querying, and “connector” fea-
                                        tures.

                                   •    Ability to support business rules in the repository.

                                   Core Products
                                   MetaMatrix provides a “model-driven” EII solution that combines an
                                   enterprise metadata management system, MetaBase, with scalable
                                   query management technology. MetaMatrix offers two main prod-
                                   ucts, MetaBase — which can stand alone as an enterprise metadata
                                   management system — and MetaMatrix Information Integration
                                   Server. MetaBase includes:


All print and electronic rights are the property of Aberdeen Group © 2003
60 • AberdeenGroup
                     Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



•   MetaData Modeler, which uploads metadata from data sources,
    places them in a “model” format, and allows users to manage
    these models as well as creating models of their own

•   The ability to create an abstraction layer through virtual meta-
    data models

•   MetaBase Repository, which houses physical and virtual models
    in an XMI format and uses them to generate runtime models for
    the MetaMatrix Information Integration Server

•   Searchbase, a search tool that allows MetaData Modeler users to
    examine the contents of the MetaBase Repository in a flexible
    way

•   MetaViewer, a browser-based search tool accessing metadata
    models and data types across intranets or the Internet

MetaMatrix Server includes:
•   MetaMatrix Server, which provides user-definable virtual data-
    bases based on cross-database metadata, with views and support
    for SQL operations. MetaMatrix Server also allows developers
    to access data at a high “virtual metadata” level.

•   MetaMatrix Administration Console, a GUI-based administra-
    tive console that monitors MetaMatrix Server operations, allows
    administration of user accounts and access rights, and provides a
    log of transactions.

•   Query Builder, a utility that allows developers to create and test
    queries.

•   MetaMatrix Connector Development Kit, an SDK that allows
    developers to create connectors and test them on a simulated
    MetaMatrix Server, as well as against live data.

MetaMatrix Server can be deployed on J2EE-compliant application
servers such as IBM WebSphere, BEA WebLogic, SAP Application
Server, and JBoss-compliant open source application servers.
MetaMatrix Server provides support for Web services via
SOAP/XML, as well as access via ODBC and JDBC using SQL.
MetaMatrix’s EII solution allows cross-database access to relational
and legacy databases, unstructured data, packaged-application data-
bases, and XML-based messaging (e.g., data from across an organ-
izational boundary). As noted above, it offers an extensible connec-
tor framework for development of custom connectors as well as sup-
port for JDBC-style connectors from a number of partners.


                                 All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                        AberdeenGroup • 61
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   Services and Partnerships
                                   MetaMatrix provides consulting and training in how to create and
                                   use its models. MetaMatrix partners with Consulting and Integration
                                   Partners to provide support throughout the customer’s EII life cycle.
                                   MetaMatrix recently announced an OEM agreement with SAP to
                                   provide MetaMatrix Server embedded in SAP NetWeaver, SAP’s
                                   new Enterprise Services Architecture.

                                   Aberdeen Conclusions
                                   MetaMatrix’s EII solution is the Cadillac of today’s EII solutions —
                                   it is comprehensive in its feature set, able to support developers and
                                   administrators at a relatively high level, and includes sophisticated
                                   features for complex-application development. Thus, MetaMatrix
                                   may not be appropriate for medium-sized enterprises without the
                                   need for sophisticated modeling of multiple databases, but is highly
                                   suitable for the largest enterprises with complex information archi-
                                   tectures or a need to develop complex cross-database applications.
                                   Overall, MetaMatrix is clearly taking a leadership role among early
                                   entrants into the EII market in implementing the technology needed
                                   for EII to scale to the largest of enterprise needs and to provide a
                                   long-term enterprise information architecture. For these situations, IT
                                   buyers should look at MetaMatrix immediately.




All print and electronic rights are the property of Aberdeen Group © 2003
62 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Author Profile

Wayne Kernochan, Managing Vice-President,
Platform Infrastructure
Wayne Kernochan focuses on databases, development environments,
and proprietary hardware. His areas of coverage also include related
software infrastructure, such as enterprise portal infrastructure, con-
tent management infrastructure, enterprise information integration
solutions, and testing and software life cycle tools. He also contrib-
utes in related areas such as XML databases and tools, Web services,
frameworks, and database administration utilities.
Kernochan has 25 years of experience in computers, including 12 as
a programmer and technical manager in databases, development
tools, e-mail, and office automation, most recently at Prime Com-
puter. Before joining Aberdeen, Kernochan covered non-mainframe
computer technologies for The Yankee Group.
Kernochan holds a B.A. in Government from Harvard University, an
M.S. in Computer Science from Cornell University, and an M.B.A.
in Information Systems from Sloan School of Management at M.I.T.




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 63
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                   Appendix A:
                                   Lexicon of Acronyms and Abbreviations

                                   API                       Application Program Interface
                                   ASP                       Application Service Provider
                                   BI                        Business Intelligence
                                   CRM                       Customer Relationship Management
                                   EAI                       Enterprise Application Integration
                                   EBA                       Enterprise Business Application
                                   EBI                       e-business Integration
                                   EII                       Enterprise Information Integration
                                   EJB                       Enterprise JavaBeans
                                   ERP                       Enterprise Resource Planning
                                   ETL                       Extract, Transform, Load
                                   GUI                       Graphical User Interface
                                   HTML                      Hypertext Markup Language
                                   ITO                       International Standards Organization
                                   ITV                       Independent Software Vendor
                                   IT                        Information Technology
                                   J2EE                      Java 2 Enterprise Edition
                                   LAN                       Local Area Network
                                   LOB                       Line-of-Business
                                   OEM                       Original Equipment Manufacturer
                                   OLTP                      Online Transaction Processing
                                   PSO                       Professional Service Organization
                                   ROI                       Return on Investment
                                   SCM                       Supply Chain Management
                                   SDK                       Software Development Kit
                                   SGML                      Standard Generalized Markup Language
                                   SMB                       Small to Medium-Sized Businesses



All print and electronic rights are the property of Aberdeen Group © 2003
64 • AberdeenGroup
       Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



SNMP    Simple Network Management Protocol
SQL     Structured Query Language
TCO     Total Cost of Ownership
VAR     Value-Added Reseller
WAN     Wide Area Network
XML     Extensible Markup Language




                   All print and electronic rights are the property of Aberdeen Group © 2003
                                                                          AberdeenGroup • 65
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                   Appendix B:
                                   Related Aberdeen Research
                                   The following publication provides complementary market research
                                   relating to EII:
                                   Embedded Infrastructure Cost of Ownership Study (December
                                   2001)

                                   Information on this and any other Aberdeen publication can be found
                                   at www.aberdeen.com or by e-mail at info@aberdeen.com.




All print and electronic rights are the property of Aberdeen Group © 2003
66 • AberdeenGroup
                     Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Appendix C:
Supplier Contact Information
MetaMatrix, Inc.
680 Fifth Avenue, 10th Floor
New York, NY 10019
(314) 739-3190, Ext. 120
www.metamatrix.com




                                 All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                        AberdeenGroup • 67
                                       Aligning IT to Business Processes




  Aligning IT to Business Processes: How
      BPM is Complementing ERP and
            Custom Applications
    Implementing BPM now to ensure your ROI



                           May 2007




                      ~ Underwritten, in Part, by ~




All print and electronic rights are the property of Aberdeen Group © 2007.
                                                         Aberdeen Group • i
                                                           Aligning IT to Business Processes



                           Executive Summary



T
       he need to support new, agile business processes is the top pressure driving
       enterprise organizations, according to the latest results from Aberdeen’s Business
       Process Management Benchmark. The overwhelming concern from line of business
       executives and top management surrounds the lack of ROI in their ERP
investments. Over half of the respondents (51%) – mostly from small and mid-size
organizations ─ say their companies’ ERP systems or best-of-breed supply chain
solutions don’t provide adequate functionality! Some application software,
particularly custom applications common in the supply chain, retail areas, and on shop
floors are not designed to adapt or react to the rapid business process change and
distributed enterprise models on which enterprises operate today.
An overwhelming majority of organizations represented in the survey feel constrained in
their applications’ ability to meet business requirements. Here’s what they say about
their current application portfolios:
   • Only 15% believe their applications afford them the desired flexibility they
     need today.
   • Over 51% say they employ manual processes to get the job done, driving up
     G&A costs, delaying decisions, and impacting productivity.
   • Thirteen percent (13%) believe their applications offer little or no flexibility
     in meeting individual customer service requirements, and 21%, say their
     applications force them to limit service offerings.
As a result, more than 50% of those surveyed are turning to business process
management (BPM) in 2007 to help get the process right at the line-of-
business level. This move serves to blend and extend the value of the IT investments
already made (e.g. ERP). SOA technology and web services is the glue that 67%%
indicate they will use to tie BPM to ERP and other enterprise applications.”
Key Business Value Findings
   • There is a wider interest in BPM and
                                                       “Replacing our green-screen applications
     business intelligence tools than in SOA
     middleware software, especially in larger         with user-driven BPM front ends is
     companies.                                        something we should have done years
                                                       ago. It really works well for the business
   • More than two-thirds of supply chain-
                                                       and for IT.”
     intensive    industries,  such     as
     manufacturing, say their ERP systems
                                                                    ~ Retail company executive
     impede visibility since they require
     customized workarounds.
   • When IT does not align with business applications, users resort to labor-
     consuming spreadsheets and manual processes, visibly raising the cost of goods
     sold and inherently lowering productivity due to non-strategic work.




                All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                        Aberdeen Group • iii
                                                           Aligning IT to Business Processes


Implications & Analysis
  • Large organizations are 50% more likely to have invested in BPM tools and
    strategies over small and mid-size enterprises.
  • Mid-size organizations are more likely than small and large companies to cite
    organizational and technical impediments to progress.
  • Most supply chain-intensive industries such as manufacturing, retail, and
    distribution/logistics say their ERP or best-of-breed supply chain solutions don’t
    provide the functionality they want and need.
  • Best in Class organizations are far ahead of Industry Average and Laggard
    companies in adaptability of applications and ROI from their SOA investments.

Required Actions
  • Best in Class companies have the most experience with SOA and should rely on
    it to drive higher ROI from their investments in BPM, especially in process
    transformation projects that harness BPM, SOA, and other technologies (e.g.,
    mobile devices) to capture and manage cost-critical processes unique to the
    business, and in driving lower application lifecycle costs.
  • Industry Average organizations must focus on modernizing their application
    approaches to business process management, eschewing legacy mainframe
    applications (37% report still having mission critical apps on this platform) in favor
    of composite (e.g. ERP) or best-of-breed tools, with a special focus on PC- or
    browser-based user interfaces.
  • Laggard companies must investigate means to improve their business processes.
    First, they must have the right ERP or custom application instead of wasting IT to
    make the wrong application work the way the business needs it to work. They
    need to investigate and deploy BPM technologies which enable process discovery.
    Get outside consulting expertise to discover the potential of SOA and manually
    mapping your business processes would be a good start of a long-term plan to
    integrate BPM with back-end applications.




               All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                       Aberdeen Group • iv
                                                                                            Aligning IT to Business Processes




                                                Table of Contents
Aligning IT to Business Processes: How BPM is Complementing ERP and Custom Applications                                         i
Executive Summary ......................................................................................................iii
Key Business Value Findings.......................................................................................iii
Implications & Analysis ................................................................................................iv
Required Actions ..........................................................................................................iv
Chapter One: Benchmarking the Best in Class........................................................ 1
The Constraints of Older Applications ................................................................... 2
The Year of BPM and SOA Technology Marriage ................................................ 4
Chapter Two: Key Business Value Findings .............................................................. 6
BPM Technologies Lead the Way............................................................................. 7
Roadblocks to Process Improvement...................................................................... 8
Payback is Starting to Ramp ....................................................................................... 9
Chapter Three: Implications & Analysis.................................................................. 11
Process and Organization ......................................................................................... 12
Kinks in the SOA Supply Chain............................................................................... 12
Large Companies Show the Way in Technology Investments......................... 13
Organizational Impediments .................................................................................... 13
Chapter Four: Recommendations for Action......................................................... 15
Best in Class Next Steps........................................................................................... 15
Industry Average Steps to Success ......................................................................... 15
Laggard Steps to Success .......................................................................................... 16
Appendix A: Research Methodology........................................................................ 20
Appendix B: Related Aberdeen Research & Tools............................................... 22




                         All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                                    Aberdeen Group
                                                                                                      Aligning IT to Business Processes



                                                    Figures
Figure 1: Top Pressures Driving Service-Oriented Architectures.................... 2
Figure 2: Ability of Software Applications to Meet Business Requirements .. 3
Figure 3: Importance of IT Capabilities in Critical Business Process Performance 7
Figure 4: Infrastructure Middleware Tools Drawing Investment ...................... 7
Figure 5: Challenges with Applications for Key Business Processes ................ 9
Figure 6: Challenges in Starting or Implementing BPM/SOA............................ 10
Figure 7: Factors Resulting in Data Management Complexity ......................... 10



                                                      Tables
Table 1: Prioritized Pressures and Enablers ........................................................... 8
Table 4: PACE Framework....................................................................................... 21
Table 5: Relationship between PACE and Competitive Framework ............. 21




                            All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                                       Aberdeen Group
                                                                          Aligning IT to Business Processes

                                  Chapter One:
                           Benchmarking the Best in Class

                • Companies are discovering how BPM, combined with SOA, is helping provide the
Key Takeaways


                  flexibility and process control needed in business today.
                • ERP systems don’t provide adequate functionality and are driving companies to integrate
                  costly workarounds to support business.
                • An overwhelming majority of organizations surveyed feel constrained in their
                  applications’ ability to meet customers’ individual business requirements.




A
        s corporations face the pressures of global supply chains, shrinking profit
        margins, and the need to deliver tailored solutions and consistent service to
        customers, they need technology infrastructures that are more flexible and
        provide end-to-end process control. That’s why these corporations are
investing heavily in IT infrastructure middleware to link their fragmented infrastructures
and applications of the past in order to improve the business processes they need to
meet the pressures of the present.
Aberdeen research has found that business process management (BPM) and
service-oriented architecture (SOA) are key infrastructure areas that can improve
business processes by allowing a company to become more agile, decentralize critical
decision making, boost management visibility, and reduce costs.
.The following table reflects Aberdeen’s classification of companies that are meeting the
challenges head-on of supporting speed and agility through the use of technology
enablers and process improvements (Table 1).

Table 1: Best in Class PACE Framework

        Pressures              Actions               Capabilities                         Enablers
       • The need to         • Improve line of     • Providing one common view of        • Standalone BPM suite plus
         support new,          business chain        data and information for              SOA
         agile business        agility               enterprise users and partners       • BPM from SOA
         processes           • Improve speed of • User capability to configure             middleware vendor
                               IT                 process workflows that meet            • BPM from ERP vendor
                               implementations    unique requirements
                                                                                       • Realtime Business Process
                             • Give line of        • Access to applications that offer   Monitoring
                               business greater      a wider range of functions or
                                                                                       • Business activity
                               direct control        features than we know have
                                                                                         monitoring
                               over their IT       • Use applications that are more
                                                                                       • Business Process
                                                     intuitive and easier to learn
                                                                                         Monitoring
                                                   • Better integration with desktop
                                                     applications




                           All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                                   Aberdeen Group • 1
                                                                            Aligning IT to Business Processes

The need to support new, agile business processes is the chief pressure driving
organizations to start or implement an SOA-based system (Figure 1)

Figure 1: Top Pressures Driving Service-Oriented Architectures


       The need to support new, agile business processes                                           62%


         Current ERP system or best-of-breed supply chain
           solution does not provide desired functionality                             44%



           Lower cost integration and application upgrades                             43%


  There are critical user functions stored in legacy systems
  and composite applications are able to provide workflows                       34%
      that span legacy and ERP/supply chain systems


                                                               0%   10% 20% 30% 40% 50% 60% 70%

                                                                          Source: Aberdeen Group, May 2007

Tthe second pressure from nearly half of the respondents - mostly small and mid-size
organizations - say their companies’ ERP systems or best-of-breed supply chain
solutions don’t provide adequate functionality. Some application software,
particularly custom applications common in the supply chain, retail areas, and on the
manufacturing shop floor are not designed to handle the rapid business process change
and distributed enterprise models on which businesses operate today. This inability of
large expensive IT investments, such as ERP, to get real-time visibility down into
the factory floor is handicapping enterprises from being able to move as the
market shifts and demand changes.
The Constraints of Older Applications
An overwhelming majority of organizations represented in the Aberdeen survey feel
constrained in their applications’ ability to meet customers’ individual business
requirements (Figure 2).




                     All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                             Aberdeen Group • 2
                                                         Aligning IT to Business Processes




Figure 2: Ability of Software Applications to Meet Business Requirements


                                              My software applications
                                              allow me to quickly adapt
                                              to most customer
                                              requirements.
                13%
                            15%               My software applications
                                              force me to put limits on
                                              services I can offer.


                                              My software applications
                                              force me to employ some
                                21%           manual processes to
                                              meet customer
                                              requirements.
             51%
                                              My software applications
                                              offer little or no flexibility to
                                              meet individual customer
                                              service requirements.




Based on the Maturity Class Framework, Aberdeen established Best-in-Class
characteristics in four key categories: (1) process; (2) organization; (3)
performance management; and (4) technology.




             All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                     Aberdeen Group • 3
                                                                Aligning IT to Business Processes

Table 2: Competitive Framework

                                                    Best in      Industry
                        Characteristics                                           Laggard
                                                     class       average

                   Ability to integrate into any
Process            system possessing critical        70%           69%              51%
                   data or information

                   IT organization has or will
Organization       be using SOA or web
                   services to improve               67%           54%              55%
                   business processes
Performance
Measurement        Satisfaction of BPM tools         17%           6%               3%

                   SOA projects underway             54%            33%              32%
                   Standalone BPM suite with
Technology                                           66%            25%              50%
                   no SOA
                   BPM suite with SOA (plan
                                                     67%            25%              50%
                   to use)

The Year of BPM and SOA Technology Marriage
Aberdeen’s prior research indicated that 41% of all companies were to at least have
SOA strategies in place by the end of 2006, if they had not implemented them already.
The main factors driving the implementations were:
   •      A desire for new capabilities like cross-application process integration;
   •      Re-use of applications via web services; and
   •      Better management of IT complexity.
The 51% of companies whose applications force them to resort to manual processes to
meet customer requirements would be best served looking for vendors to provide
composite applications that tie together point solutions to enable a flexible industry-
or company-specific business process (One example: an integrated business planning
solution that can enable the balancing of supply and demand to maximize profit by
bridging sales and operations forecasting tools, constraint-based supply chain
applications, and financial systems) or in the case of small-to-medium size businesses
(SMB) to utilize vendors who can extend their existing core investments in office
tools, communication and document management systems.
Leading companies are looking to leverage BPM tools to build out front-end applications
that should be:
   •      Flexible from an end-user perspective;
   •      Equipped with a rich user interface that promotes productivity;
   •      Able to map well to line-of-business process requirements;
   •      Capable of integrating with their investments in back-end ERP and best-of-breed
          business process solutions.



                  All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                          Aberdeen Group • 4
                                                        Aligning IT to Business Processes

Over an application’s lifecycle, BPM can deliver dramatically lower software
maintenance costs due to the ease with which business units can change the process
and key process parameters without massive IT reprogramming and testing.
According to the 2007 Aberdeen Benchmark Report results, 2007 is shaping up
to be the year of BPM.




               All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                       Aberdeen Group • 5
                                                                            Aligning IT to Business Processes

                                       Chapter Two:
                                Key Business Value Findings

                  • When IT does not align with business applications, users resort to labor-consuming
Key Takeaways


                    spreadsheets and manual processes, invisibly raising the cost of goods sold.
                  • There is a wider interest in BPM and business intelligence tools than in SOA middleware
                    software, Enterprise Application Integration (EAI) and Master Data Management (MDM).
                  • More than two-thirds of supply chain-intensive industries, such as manufacturing, say
                    their ERP systems impede better visibility since they require customized workarounds.



A
       fter seeing several years of a recession-fueled lockdown in technology
       investment, Aberdeen is witnessing a renaissance in IT spending around core
       infrastructure middleware. From our 2006 and 2007 research, the key drivers
       for these investments - especially SOA and BPM - are that the underlying
technologies must deliver prompt and demonstrable business value, can be developed in
controllable projects, and will incrementally lower long-term maintenance costs.
That’s why we’re witnessing the following, taken from our research for this report:
                • 38% of companies surveyed have current SOA projects, another 29% say their IT
                  organizations are planning to start at least one project within the next 12 months.
                • 41% have SOA-based solutions already in place, with another 27% budgeted to
                  start building them within the next 12 months.
                • 63% believe it’s very important that their technologies, such as BPM, be able to
                  integrate into any system that provides critical data or information, which is what
                  an SOA can deliver (Figure 3).
But our survey also found that change comes
slowly. Some 63% of surveyed companies use
spreadsheets and 37% use legacy mainframe                              Change comes slowly. Two-
applications to manage critical business process                       thirds of surveyed companies
functions. This is a clear reflection of the half of                   use spreadsheets and 37% use
the companies in the survey whose software
                                                                       legacy mainframe applications
applications force them to employ manual
processes to meet customer requirements.                               to manage critical business
                                                                       process functions.
However, 54% of Best in Class companies
Aberdeen surveyed recognize this and are
investing in technologies that can improve
nimble processes.




                             All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                                     Aberdeen Group • 6
                                                                                Aligning IT to Business Processes

Figure 3: Importance of IT Capabilities in Critical Business Process
Performance


 Providing common view of
  data and information for
   enterprise users and                     32%                                66%
          partners


Ability to integrate into any
system with critical data or                  31%                               63%
         information



    Access to applications
    offering wider range of                                63%                              30%
    functions and features



                            0%               20%            40%           60%             80%        100%

                                Not Important      Somewhat Important    Very Important


                                                                               Source: Aberdeen Group, May 2007


BPM Technologies Lead the Way
Figure 4 shows the infrastructure middleware technologies in which the surveyed
companies are investing. There is an overwhelming preference for BPM technologies to
create and monitor business workflows, followed by the chief tools that assist with IT
integration: ESB, SOA middleware, and enterprise application integration (EAI).

Figure 4: Infrastructure Middleware Tools Drawing Investment

  60%             57%                    55%
  50%                                                         45%               45%
  40%

  30%                                                                                              25%
  20%
  10%
   0%
            Business process    Business intelligence or   ESB and SOA           EAI               MDM
            management (BPM)    business performance
                  tools         management/monitoring
                                        tools



                                                                         Source: Aberdeen Group, December 2006

Table 1 shows how these technologies map to the pressures driving SOA that were
listed in Chapter One. These findings highlight issues cited in the Aberdeen Composite
Applications Benchmark report:



                     All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                             Aberdeen Group • 7
                                                                 Aligning IT to Business Processes

    •    The biggest challenge in corporate IT organizations is improving real-time
         visibility into business operations;
    •    Business is discovering the SOA as a technological foundation that can make
         businesses more nimble and business processes more flexible with minimal IT
         intervention; and
    •    Sharing information with other parts of the organization, a key by-product of
         better business process management, is more reachable.

Table 1: Prioritized Pressures and Enablers

Priorities   Prioritized Pressures                  Prioritized Enablers

     1        The need to support new, agile        Æ Business process management (BPM)
              business processes                        tools for creating business
                                                        workflows
                                                    Æ Business intelligence or business
                                                        performance
                                                        management/monitoring tools

     2        Current ERP systems or supply         Æ BPM front-end to ERP or back-end
              chain best-of-breed solutions do          apps
              not provide the desired
              functionality.                        Æ Enterprise service bus (ESB) and
                                                        SOA middleware software with
                                                        composite applications
                                                    Æ Enterprise application integration
                                                        (EAI) middleware software

     3        Lower cost integration and            Æ Enterprise service bus (ESB) and
              application upgrades                      SOA middleware software
                                                    Æ Enterprise application integration
                                                        (EAI) middleware software with
                                                        composite applications

     4        There are critical user functions     Æ Composite applications that span at
              stored in legacy systems that users       least some of the following:
              need; composite applications are          spreadsheets, legacy applications,
              able to provide workflows that            ERP, best-of-breed applications,
              span legacy and ERP/supply chain          desktop applications, web-hosted/On
              systems;                                  Demand applications, customers’ or
                                                        suppliers’ applications
                                                               Source: Aberdeen Group, May 2007

Roadblocks to
Process Improvement
Still, improving business process visibility and integration capabilities doesn’t come
without its challenges (Figure 5). Companies surveyed indicate:




                  All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                          Aberdeen Group • 8
                                                                       Aligning IT to Business Processes

   •     ERP systems don’t provide the needed flexibility. Alarmingly, 75% of companies
         that are the biggest users of ERP systems cite this issue. Yet, only 33% of Best
         in Class companies are constrained by their ERP systems;
   •     Key application parameters and rules are locked inside program source code;
   •     A lack of centralized workflows associated with management life-cycles; and
   •     A lack of IT agility that forces interim paper workarounds to change business
         processes, with a resulting increase in labor and loss of management visibility.

Figure 5: Challenges with Applications for Key Business Processes


  ERP systems are unable to do what we want without
                   customization                                                      57%


   Key application parameters and rules are locked in
    program source code, making changes difficult
                                                                                    53%


       Many organizations and systems own workflows
          associated with life-cycle management                                     54%


     Business process changes result in interim paper
             workarounds until IT catches up                                    46%


                                                        0%     20%        40%         60%        80%

                                                               Source: Aberdeen Group, December 2006
Breaking technological and organizational
logjams can go a long way toward
improving business processes to meet                         “Once we realized how much effort was
today’s business demands. These issues                       going into doing things our ERP’s way,
also come up when we asked
                                                             the BPM solution to doing things our
respondents to cite the challenges they
face or will face in implementing an SOA-                    ‘own business’ way became obvious.”
based system (Figure 6), as well as the
                                                                     ~ Insurance company executive
factors that result in data management
complexity (Figure 7).

Payback is Starting to Ramp
These challenges may be preventing companies from realizing the full potential return
on investment (ROI) from SOA and BPM. Of course, these solutions are relatively new
on the IT scene and require much effort and a steep learning curve. For instance, only
19% of companies represented in Aberdeen’s Composite Applications Benchmark report
have had SOA-based solutions in place for more than a year, while another 22% were
implemented only within the last 12 months.
Already companies have shown an average return of about 9% based on an average
investment in SOA at around $730,000 while the mean payback to date is $798,000.


                   All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                           Aberdeen Group • 9
                                                                  Aligning IT to Business Processes

Figure 6: Challenges in Starting or Implementing BPM/SOA



                   Limited in-house IT skills                                          51%



  Limited vision/support or understanding
                                                                                       50%
    from the business side or leadership



       Data resides in too many places to
                                                                                 42%
              consolidate rapidly


                                                0%   10%    20%    30%     40%     50%     60%

                                                       Source: Aberdeen Group, December 2007

Figure 7: Factors Resulting in Data Management Complexity


     Proliferation of
   application-specific                                                           67%
       databases

    Interspersed data
      and business                                                               66%
        processes

   Legacy systems
    have inflexible,                                                       59%
  obsolete databases

                          0%         20%              40%                60%              80%


                                                       Source: Aberdeen Group, December 2006
When we separated the Best in Class
organizations from the rest of the survey
pool, the Best in Class are recouping                 “We missed some long-term recurring
averaging a return of more than twice                 cost savings in software maintenance by
their investment, while Industry Average              trying to get by with old development
and Laggard companies - have yet to                   tools.”
recover all they have invested. In spite of
these work-in-progress ROI results,                        ~ Petrochemical company executive
companies are continuing to invest
aggressively in these technologies.




                 All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                        Aberdeen Group • 10
                                                                                    Aligning IT to Business Processes

                                               Chapter Three:
                                          Implications & Analysis

                    •     Best in Class organizations are far ahead of Industry Average and Laggard companies
                          in their adaptability of applications and in their ROI from BPM and SOA investments.
Key Takeaways




                    •     Most supply chain-intensive industries such as manufacturing, retail, and
                          distribution/logistics say their ERP or best-of-breed supply chain solutions don’t provide
                          the functionality they want and need.
                    •     Large organizations are twice as likely to invest in data quality tools as small and mid-
                          size enterprises are.
                    •     Mid-size organizations are more likely than small and large companies to cite
                          organizational and technical impediments to progress.




H
         ow can an organization succeed in improving business processes? According to
         our survey results, success begins with knowledge and extends into
         implementation of BPM, SOA and master data management (MDM) tools. Table
         2 shows Aberdeen’s Competitive Framework for this report to distinguish
leading, or Best in Class, companies, from Industry Average and Laggard organizations.
We determined that:
                •       Best in Class organizations have
                        software applications that can allow                 Competitive Framework Key
                        them to adapt quickly to most                 The Aberdeen Competitive Framework
                        customer requirements                         defines enterprises as falling into one of the
                •       Industry Average companies have               three following levels of practices and
                        applications that force the use of            performance:
                        some manual processes to meet                 Best in Class (20%) —practices that are the
                        requirements.                                 best currently being employed and
                                                                      significantly superior to the industry average
                •       Laggard organizations find that
                        their applications offer little or no         Industry Average (50%) —practices that
                        flexibility  to    meet      individual       represent the average or norm
                        customer requirements or force the            Laggards (30%) —practices that are
                        organization to limit the services it         significantly behind the industry average
                        can offer.
Best in Class organizations are more likely to be aware of SOA, due largely to the
knowledge levels of their IT organizations and the support and commitment from the
business side or executive leadership. In short, these organizations are committed to
SOA as their platforms of the future. They are also the least likely to suffer from snags
in their ERP integration projects.




                                 All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                                        Aberdeen Group • 11
                                                              Aligning IT to Business Processes



Process and Organization
Commitment to and interest in SOA and BPM spell the difference between Best in Class
organizations and the rest of the survey pool. Facilitating that is that only 11% of these
companies believe they’re dealing with too much complexity for employees to handle, in
spite of the fact that close to half of them indicate they’re busy with several
technology/business process initiatives.
Further, only 24% of the Best in Class use
legacy mainframe applications to manage
                                                   Commitment to and interest in both
critical business processes, well below the
                                                   SOA and BPM spells the difference
39% of Industry Average. This highlights a
willingness and commitment by the Best in          between Best in Class organizations
Class to use more advanced applications,           and the rest of the survey pool.
such as best of breeds and Web-hosted
and On Demand tools.

Kinks in the SOA Supply Chain
For all the benefits SOA bring, companies that rely heavily on their supply chains
are least likely to use SOA, even though their benefits are more than apparent.
Here are some key survey findings on this group, which made up more than half of the
respondent pool:
   • 63% say the upfront costs for implementing SOA are higher because of a need for
     more design and architecture (56% of the entire survey pool cited this);
   • 63% say they lack the IT governance and process systems to ensure SOA success
     - full survey pool: 43% (Note: see Aberdeen’s Information Governance and Process
     Systems Benchmark Repor for additional informationt);
   • 63% say their current teams can’t adjust to the culture change that’s needed with
     reusable services (full survey pool: 45%); and
   • 58% say piloted projects were very expensive and yielded many lessons to learn.
     This was more than twice the entire survey pool (21%).
Even worse, these technological and organizational limitations may well impact
performance at many of these supply-chain-centric companies. For instance:
   • A whopping 93% cite inconsistency or outdated information in orders sent to
     manufacturers, compared with just 12% cited by the whole survey pool.
   • 69% cite data errors caused by manual updating, which can potentially affect
     purchase orders and inventory.
   • 67% say business process changes result in interim paper workarounds until
     IT catches up. In an age of tighter compliance with Sarbanes-Oxley and other
     business regulations, this finding points up the importance of SOA as a tool that
     can improve IT agility: the ability of IT to keep up with the business.




                All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                       Aberdeen Group • 12
                                                             Aligning IT to Business Processes

Large Companies Show the Way in Technology Investments
Close to three-quarters of large companies (annual revenue of more than $1 billion),
where the processes are more complex, are investing in BPM tools, as well as ESB and
SOA middleware software (Table 3). Most are also investing in EAI tools, and they are
twice as likely to spend on MDM and data quality tools than small and mid-size
organizations.
From these and other findings, it’s clear that larger organizations are showing the way
on these integration catalysts. They are also much more likely to have the right
functionality from their ERP systems and best-of-breed supply chain tools.
Most small and mid-size organizations represented in our survey say their ERP and
supply-chain tools don’t provide the functionality they want. Mid-size companies, in
particular, are unable to adjust to the rapid technology change underfoot, with 43%
citing this as a challenge and, 57% reporting that line-of-business executives’
expectations are too high for IT to meet, .

Table 3: Technology Investments by Organization Size
                                                     Small      Mid-size     Enterprise
 Business process management (BPM) tools for
                                                       55%         52%            76%
 creating business workflows
 Business intelligence or business performance
                                                       55%         48%            48%
 management/monitoring tools
 Enterprise Service Bus (ESB) and SOA
                                                       18%         35%            71%
 middleware software
 Enterprise application integration (EAI)
                                                       27%         35%            57%
 middleware software
 Master data management (MDM) tools                     9%         17%            43%
 Data quality tools                                     9%         17%            33%
 Event management tools                                14%         9%             19%
                                                    Source: Aberdeen Group, December 2006

Organizational Impediments
Many mid-market companies are in a tight spot when it comes to technical, financial, and
human resources, given their size, and that’s reflected in the survey. For instance, they
are more likely than larger or smaller organizations to cite challenges in these areas
(Figures 8 and 9). Companies with these symptoms need to look at personnel issues.




                All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                       Aberdeen Group • 13
                                                                         Aligning IT to Business Processes

Figure 8: Organizational Challenges to SOA Implementations



         60%                       57%
                                                           Small       Mid-Size      Large
         50%
                                            41%
                         38%
         40%
                                                                             31%
         30%
                                                                  19%
         20%
                                                                                     12%
         10%

          0%
                    Current IT team is unable to             Piloted projects were very
                    adjust to culture change of            expensive with lots of lessons
                     needed reusable services                          learned

                                                                Source: Aberdeen Group, December 2006

Figure 9: Application Challenges to Business Process Improvements

                                                                                               Large
Inconsistent or outdated information within orders that    5%
                                                                                               Mid-Size
                                                                       20%
              are sent to manufacturers                          12%                           Small


                                                                                    37%
                       Errors due to manual updating                                            57%
                                                                              30%


    Business process changes result in interim paper                                  41%
                                                                                             54%
            workarounds until IT catches up                                           42%


 Workflows associated with management of life-cycles                                               61%
                                                                                                      66%
  are owned by multiple organizations and systems                              33%


                                                      0%   10% 20% 30% 40% 50% 60% 70%

                                                                Source: Aberdeen Group, December 2006

Management alignment is another issue worth underlining. More than half the
companies using BPM report limited vision/support or understanding from
the business side and/or executive leadership. These companies go even further,
saying “We have realized that it requires not only buy-in but also strong commitment
from lines of business execs, not just IT.” Because BPM projects require active
participation during the development phase by the lines of business, plus ownership of
BPM changes once the system is in place, IT needs to negotiate appropriate expectation
levels with the business units before commencing initial BPM projects.




                   All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                          Aberdeen Group • 14
                                                                           Aligning IT to Business Processes

                                     Chapter Four:
                               Recommendations for Action

                 •   Best in Class companies have the most experience with SOA, and they should rely on it
                     to drive higher ROI from their investments in SOA and BPM.
Key Takeaways




                 •   Industry Average organizations must focus on modernizing their application approaches
                     to BPM, eschewing pure legacy mainframe applications in favor of composite or best-
                     of-breed tools.
                 •   Laggard companies must invest in more technology to improve BPM. Discovering the
                     potential of SOA by using external expertise would be a good start.


Best in Class Next Steps
                1) Drive more ROI from your SOA investments. Better returns come with maturity. As
                   your organization gains more experience with SOA, it will find ways to generate
                   higher returns on its investments. Look to consolidating services under SOA to
                   create a common back end to BPM-driven front-end applications.
                2) Make SOA better for the user. Improving the user experience is - or should be -
                   the top mission of any corporate IT organization. Utilize the superior SOA
                   knowledge within the IT staff to help the user - especially those in customer-
                   facing roles - become more productive. BPM and composite application
                   development tools can improve the usability and productivity of legacy
                   applications vastly.
                3) Focus on application life-cycle management costs. BPM and SOA are no longer two
                   distinct technologies that IT must integrate into custom solutions. Technology
                   suppliers are doing the integration, delivering products that start with BPM and
                   include the SOA transport and infrastructure, including composite application
                   technology to modernize legacy applications and, for the application providers,
                   SOA-enabled application versions that fit well with BPM.

Industry Average Steps to Success
                1) Get out of the old and into the new. Decrease your dependence on legacy
                   mainframe applications, desktop applications, and spreadsheets as keys to
                   business process improvement and replace them with more BPM-based,
                   composite and best-of-breed applications.
                2) Discover the potential for BPM in your organization. BPM holds the potential to
                   dramatically improve IT agility with rapidly changing line-of-business
                   requirements, and as a tool for critical process transformation.
                3) Is there interest in SOA? All but 5% of Industry Average organizations at least
                   have interest in the potential advantages of an SOA. But more than one-quarter
                   of Industry Average organizations in our survey that haven’t heard about SOA
                   want to know more (Only 36% have SOA solutions in place). The increase in
                   knowledge starts at the top; 61% of Industry Average companies cite limited
                   vision, support, or understanding of SOA from the business side or executive



                            All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                                   Aberdeen Group • 15
                                                          Aligning IT to Business Processes

      leadership, compared with only 37% of Best in Class companies. There are
      numerous SOA success stories across vertical markets to use as guideposts.

Laggard Steps to Success
  1) Make sure you have the right core application software. Trying to make due with
     the wrong software (e.g. ERP)— or a home-grown equivalent — creates a
     perpetual money hole in integration costs. After looking at the real costs of
     running your systems, consider replacing it or using BPM software to deliver a
     business-friendly front end to the transaction engine.
  2) Invest in more modern technology to improve management of critical processes with
     BPM. If you have the financial resources, spend some on best-of-breed or
     composite applications and modernize old legacy mainframe apps, especially the
     user interface, by extending the legacy applications with a BPM front end that
     matches what the business units really need. Pay for the investments in
     measurable productivity improvements just on reduced keystrokes and screen
     changes alone.
  3) Discover the potential of SOA. Chances are if you haven’t embarked on or are
     planning an SOA project, there is interest in the organization. If so, ramp up the
     internal knowledge on SOA and learn what an ESB and SOA middleware
     software can do to help improve business processes.
  4) Extend your already existing investments. The investment in office tools,
     communication systems, document management and knowledge managements
     systems exists. Implement your BPM tool strategy into these already existing
     applications and leverage your employee knowledge base.




              All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                     Aberdeen Group • 16
                                                             Aligning IT to Business Processes

                         Featured Underwriters
This research report was made possible, in part, with the financial support of our under-
writers. These individuals and organizations share Aberdeen’s vision of bringing fact
based research to corporations worldwide at little or no cost. Underwriters have no
editorial or research rights and the facts and analysis of this report remain an exclusive
production and product of Aberdeen Group.




                                                Appian is a leading provider of
business process management (BPM) technology that helps organizations design,
manage, and optimize their business processes. Appian Enterprise has revolutionized
process design with a modeling environment that is simple enough for business users
yet powerful enough for IT. Appian is the first BPM vendor to combine collaboration
and content management with process to create best practice business processes.
Appian's patent-pending Active Optimization Technology, which analyzes the in-flight
process data stream, not just stored data, helps companies stay ahead of the
competition.
For additional information on Appian Corporation:
8000 Towers Crescent Drive, 16th Floor Vienna, VA 22182
703-442-8844 or info@appian.com
www.appian,com




                All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                       Aberdeen Group • 17
                                                           Aligning IT to Business Processes




                                             CTSpace is a leading software-as-a-service
                                             provider     of     enterprise    content
                                             collaboration and business process
                                             management solutions. The Company
                                             maintains its corporate headquarters in
San Francisco and has offices in the UK, Germany, France, Austria and India. CTSpace
provides corporations with SaaS applications that manage communication and
information across projects. Key customers include GE, Shell Oil, Duke Energy, London
Underground, IKEA and BNP Paribas among others.
For additional information on CTSpace:
49 Stevenson, Suite 950 San Francisco, CA 94105
415-882-1888 or hkoenig@ctspace.com
www.ctspace.com




               All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                      Aberdeen Group • 18
                                                            Aligning IT to Business Processes




                                         Ramco is a global provider of software and
                                         services that create agile global-class business
                                         applications for a variety of enterprises.
                                         Ramco’s Business Process Delivery System
                                         (BPDS) enables fast, flexible deployment and
                                         change on demand of processes and
                                         applications for maximum flexibility – so when
your business changes your system changes too. The Ramco BPDS combines best in
class BPM capabilities with an integrated services environment and a repository of over
1,200 pre-built services for true end-to-end SOA based application development.
Ramco Systems has offices in nine countries and customers in 1,000 locations
worldwide across multiple verticals.
For additional information on Ramco Systems:
3150 Brunswick Pike, Lawrenceville, NJ 08648
609-620-4800 or info@rsc.ramco.com
www.ramco.com




                All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                       Aberdeen Group • 19
                                                            Aligning IT to Business Processes

                             Appendix A:
                        Research Methodology



O
         ver the last year, Aberdeen Group examined the technology use, investment
         plans, pressures, and challenges of more than 125 enterprises in such
         middleware solutions as Business Process Management (BPM) and Service-
         Oriented Architecture (SOA) as integration catalysts that can potentially
improve their business processes.
Responding executives and managers completed an online survey that included
questions designed to determine the following:
   •   The factors pushing companies to initiate or implement an SOA-based system;
   •   The challenges companies face in initiating or implementing an SOA;
   •   The amount of organizational investment in SOA and BPM and the payback from
       investments;
   •   The degree of importance organizations place on a set of technological
       capabilities that can impact the performance of critical business processes; and
   •   The degree of satisfaction with their investments in SOA and BPM solutions.
Aberdeen supplemented this online survey effort with telephone interviews with select
survey respondents, gathering additional information on middleware strategies,
experiences, and results.
The study aimed to identify emerging best practices for the use of these middleware
tools as integration catalysts in today’s modern IT infrastructures and provide a
framework by which readers could assess their own capabilities in these areas.
Responding enterprises included the following:
   •   Job title/function: The research sample included respondents from the
       following areas of the organization: information technology (53%), business
       process management (10%); other (13%); marketing (6%); sales (5%);
       logistics/supply chain (6%); finance (3%), customer service (2%) and
       manufacturing (1%). Job titles included the following: manager (24%);
       consultant (22%); senior management, such as CEO or COO (18%); staff (11%);
       director (11%); CIO (6%); vice president (6%); other (3%) and CFO (1%).
   •   Industry: The research sample included respondents predominantly from
       manufacturing and services industries, led by the following: finance, banking, and
       accounting (18%); high technology/software (14%); insurance, real estate, legal
       services (8%); transportation/logistics (8%); public sector (4%); publishing and
       media (4%); retail (4%); aerospace/defense (3%); apparel (3%); automotive (4%);
       education (3%); health, medical, and dental services (4%); and utilities
       (3%).Other responding sectors included computer equipment and peripherals;
       construction/engineering; consumer electronics, consumer packaged goods;
       food and beverage; medical devices; metals and metal products; mining/oil/gas;
       paper, lumber, and timber; pharmaceutical manufacturing, telecommunications
       services, and wholesale. The survey was supplemented with responses to a


                All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                       Aberdeen Group • 20
                                                                          Aligning IT to Business Processes

         select group of supply-chain companies in the discrete manufacturing, process
         manufacturing, distribution, and retail industries.
    •    Geography: About 45% of all study respondents were from North America
         (US, Canada, Mexico); 28% were from Europe; 20% from Asia/Pacific; 5% from
         the Middle East and Africa; and 3% from South America and the Caribbean.
    •    Company size: About 32% of respondents were from large enterprises (annual
         revenues above US$1 billion); 31% were from mid-size enterprises (annual
         revenues between $50 million and $1 billion); and 37% from small businesses
         ($50 million or less).
Solution providers recognized as sponsors of this report were solicited after the fact
and had no substantive influence on the direction of this benchmark report. Their
sponsorship has made it possible for Aberdeen Group to make these findings available
to readers at no charge.

 Table 4: PACE Framework

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
                                                                            Source: Aberdeen Group, 2007

 Table 5: Relationship between PACE and Competitive Framework

PACE and Competitive Framework How They Interact
Aberdeen research indicates that companies that identify the most impactful pressures and take the most
transformational and effective actions are most likely to achieve superior performance. The level of
competitive performance that a company achieves is strongly determined by the PACE choices that they
make and how well they execute.
                                                                            Source: Aberdeen Group, 2007




                    All print and electronic rights are the property of Aberdeen Group © 2007.
                                                                           Aberdeen Group • 21
                                                                        Aligning IT to Business Processes

                      Appendix B:
           Related Aberdeen Research & Tools

Related Aberdeen research that forms a companion or reference to this
report include:
     •      The Composite Applications Benchmark Report, December 2006
     •   The Legacy Application Modernization Benchmark Report; September
     2006
     •      2007 Aberdeen Benchmark Report, April 2007
     •      The Business Process Management Benchmark Report; August 2006
     •   Outsourcing Application Development and Maintenance; November
     2006
     •      Enterprise Service Bus and SOA Middleware; June 2006
     •      Achieving More Value from Enterprise Applications, May 2006
     •      The SOA in IT Benchmark Report; December 2005
Information on these and any other Aberdeen publications can be found at
www.Aberdeen.com.




      Author: Ralph A. Rodriguez, Senior VP & Research Director of Technology Markets,
      Ralph.rodriguez@aberdeen.com
Founded in 1988, Aberdeen Group is the technology- driven research destination of choice for the global business
executive. Aberdeen Group has over 100,000 research members in over 36 countries around the world that both
participate in and direct the most comprehensive technology-driven value chain research in the market. Through its
continued fact-based research, benchmarking, and actionable analysis, Aberdeen Group offers global business and
technology executives a unique mix of actionable research, KPIs, tools, and services.
This document is the result of research performed by Aberdeen Group. Aberdeen Group believes its findings are
objective and represent the best analysis available at the time of publication. Unless otherwise noted, the entire
contents of this publication are copyrighted by Aberdeen Group, Inc. and may not be reproduced, stored in a retrieval
system, or transmitted in any form or by any means without prior written consent by Aberdeen Group, Inc.




22
  THIS DOCUMENT IS FOR ELECTRONIC DELIVERY ONLY
                      The following acts are strictly prohibited:
                             • Reproduction for Sale
                             • Transmittal via the Internet
                     Copyright © 2007 Aberdeen Group, Inc. Boston, Massachusetts



Terms and Conditions
Upon receipt of this electronic report, it is understood that the user will and must fully comply with the
terms of purchase as stipulated in the Purchase Agreement signed by the user or by an authorized
representative of the user’s organization. Aberdeen has granted this client permission to post this report
on its Web site.

This publication is protected by United States copyright laws and international treaties. Unless otherwise
noted in the Purchase Agreement, the entire contents of this publication are copyrighted by Aberdeen
Group, Inc., and may not be reproduced, stored in another retrieval system, or transmitted in any form or
by any means without prior written consent of the publisher. Unauthorized reproduction or distribution of
this publication, or any portion of it, may result in severe civil and criminal penalties, and will be
prosecuted to the maximum extent necessary to protect the rights of the publisher.

The trademarks and registered trademarks of the corporations mentioned in this publication are the
property of their respective holders.

All information contained in this report is current as of publication date. Information contained in this
publication has been obtained from sources Aberdeen believes to be reliable, but is not warranted by the
publisher. Opinions reflect judgment at the time of publication and are subject to change without notice.


Usage Tips
Report viewing in this PDF format offers several benefits:
        • Table of Contents: A dynamic Table of Contents (TOC) helps you navigate through the
            report. Simply select “Show Bookmarks” from the “Windows” menu, or click on the bookmark
            icon (fourth icon from the left on the standard toolbar) to access this feature. The TOC is both
            expandable and collapsible; simply click on the plus sign to the left of the chapter titles listed
            in the TOC. This feature enables you to change your view of the TOC, depending on whether
            you would rather see an overview of the report or focus on any given chapter in greater
            depth.
        • Scroll Bar: Another online navigation feature can be accessed from the scroll bar to the right
            of your document window. By dragging the scroll bar, you can easily navigate through the
            entire document page by page. If you continue to press the mouse button while dragging the
            scroll bar, Acrobat Reader will list each page number as you scroll. This feature is helpful if
            you are searching for a specific page reference.
        • Text-Based Searching: The PDF format also offers online text-based searching capabilities.
            This can be a great asset if you are searching for references to a specific type of technology
            or any other elements within the report.
        • Reader Guide: To further explore the benefits of the PDF file format, please consult the
            Reader Guide available from the Help menu.
SOA Middleware Takes the Lead:
Picking Up Where Web Services
           Leaves Off

                July 2007

        ~ Underwritten, in Part, by ~
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 2


                        Executive Summary

Aberdeen analysis of approximately 400 companies over the past 18 months           Customer Quote
has shown a deep division between organizations that are deploying web
                                                                                   “We are going from 12,000
services based applications, what we call SOA Lite, and those that are             applications to hundreds of
building out full SOA middleware infrastructure. With two such different           services using an SOA. The
software investment profiles, we expect to see significantly different success.    lifecycle cost savings are already
                                                                                   flowing       through  in     lower
Organizations that are focusing on SOA infrastructure are outperforming            maintenance costs and faster
those that are deploying only web services. They are realizing lower               development cycles. This is turning
application lifecycle costs, better throughput for projects, and higher levels     into a major win for the business,
of user satisfaction.                                                              not just IT.”
                                                                                   ~ VP, Financial Services
Best-in-Class Performance
Three key performance indicators (KPIs) were used to identify those
companies that are succeeding in their application development efforts,
Aberdeenís Best-in-Class.

 KPI                                      Best-in-Class Performance
Application development costs             100% saw reduction
Application maintenance costs             72% saw reduction
User satisfaction in IT service levels    89% saw improvement

                                               Source: Aberdeen Group, July 2007


Competitive Maturity Assessment
Although prior Aberdeen research implied an even split between SOA
infrastructure and web services strategies, the closer focus of this study
revealed that Best-in-Class companies are building out SOA middleware
infrastructure by a margin of nearly two to one (Figure 1). The typical Best-
in-Class organization:
    •    Sees SOA applications as a way to improve service to end users
         (61%) and improve the agility of the IT department (60%);
    •    Is using SOA to simplify and standardize their development
         infrastructure (71%);
    •    Has deployed one or more ESBs (76%);
    •    Reports reductions in application development costs (100%);
    •    Is actively engaged in retraining their application development team
         (61%);
    •    Uses SOA middleware to make IT more agile in responding to new
         business requirements


© 2007 Aberdeen Group, Inc.                                                            Telephone: 617 723 7890
www.aberdeen.com                                                                                       041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 3


Required Actions
In spite of the perceived complexity of full-blown SOA infrastructures, there
are real savings available to those organizations willing to make the
investments in time and budget. Areas to focus on are:
    •    Simplify and standardize. The effort spent in rationalizing
         existing processes and applications, and decomposing them into
         components and services, will be rewarded by increased agility and
         reduced development costs.
    •    Concentrate on infrastructure. Web services will carry an
         organization only so far. Organizations that are investing in
         infrastructure report improved returns on those investments.
    •    Re-train the team. Donít expect IT to just ìget itî when it comes
         to SOA. The Best-in-Class recognize that SOA is a disruptive
         technology and are putting their money into building expertise.




© 2007 Aberdeen Group, Inc.                                                     Telephone: 617 723 7890
www.aberdeen.com                                                                                041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 4


Table of Contents
Executive Summary....................................................................................................... 2
    Best-in-Class Performance......................................................................... 2
    Competitive Maturity Assessment........................................................... 2
    Required Actions ......................................................................................... 3
Chapter One: Benchmarking the Best-in-Class ..................................................... 6
    Aberdeen Analysis ....................................................................................... 6
    Why Enterprises Are Focusing on SOA Middleware .......................... 7
    Maturity Class Framework ........................................................................ 9
    Best-in-Class PACE Model......................................................................... 9
Chapter Two: Benchmarking Requirements for Success ..................................11
    Competitive Assessment..........................................................................11
    Organizational Capabilities and Technology Enablers .......................13
      Process.....................................................................................................14
      Organization ...........................................................................................15
      Knowledge ..............................................................................................16
      Technology..............................................................................................17
      Performance ...........................................................................................19
Chapter Three: Required Actions .........................................................................20
    Laggard Steps to Success..........................................................................20
    Industry Norm Steps to Success ............................................................20
    Best-in-Class Steps to Success ................................................................21
Appendix A: Research Methodology.....................................................................22
Appendix B: Related Aberdeen Research............................................................25
Featured UnderwritersÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖÖ..26

Figures
Figure 1: What Technologies Are Being Used? ..................................................... 7
Figure 2: Top drivers for SOA and web services .................................................. 8
Figure 3: Trends in training and development tools ...........................................13
Figure 4: Best-in-Class places an emphasis on process......................................14
Figure 5: New and upgraded development environments ................................15
Figure 6: Retraining of application development teams .....................................16
Figure 7: Approaches to SOA and web services technology ...........................18
Figure 8: Application costs........................................................................................19




© 2007 Aberdeen Group, Inc.                                                                                                  Telephone: 617 723 7890
www.aberdeen.com                                                                                                                             041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 5



Tables
Table 1: Companies With Top Performance Earn ìBest-in-Classî Status:.... 9
Table 2: Best-in-Class PACE Framework ..............................................................10
Table 3: Competitive Framework ...........................................................................12
Table 4: PACE Framework .......................................................................................23
Table 5: Maturity Framework...................................................................................24
Table 6: Relationship between PACE and Competitive Framework ..............24




© 2007 Aberdeen Group, Inc.                                                                                         Telephone: 617 723 7890
www.aberdeen.com                                                                                                                    041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 6


                   Chapter One:
            Benchmarking the Best-in-Class
Aberdeen Analysis                                                                 Fast Facts
                                                                                  √ 100%      of  Best-in-Class
                                                                                    organizations report     an
While 90% of the Global 5000 have enthusiastically adopted plans and                improvement in application
projects to implement new applications using services-oriented technologies         development costs using
(i.e., SOA), Aberdeen research in ESB and SOA Middleware (June 2006) and            SOA
The Legacy Application Modernization Benchmark Report (September 2006)
                                                                                  √ User satisfaction, IT agility,
show a clear bifurcation of technology approaches to ìgetting to servicesî:         and reduction of operating
    •    Half are using Web services low-level technologies such as                 costs are key drivers for
                                                                                    deploying SOA applications
         Extended Markup Language (XML), Simple Object Access Protocol
         (SOAP), a UDDI repository, and the 30+ standards/open source
         code technologies commonly called ìWS-*î. These are open source
         and no cost to obtain. Arguing for this side, one pharmaceutical
         CIO told us, ìWe can bang together composite applications with
         web clients to our legacy applications as fast as the line-of-business
         asks. Satisfying the business is more important right now than a five-
         year SOA build-out planî. This half says Web services are SOA, in
         spite of industry and vendor definitions to the contrary
    •    The other half are investing in third-party infrastructure middleware
         including Enterprise Service Bus (ESB), registry/repository, security,
         management, and governance software unique to a Services-
         Oriented Architecture (SOA). On this side of the argument, a
         financial services technology VP said, ìWe are going from 12,000
         applications to hundreds of services using an SOA. The lifecycle cost
         savings are already flowing through in lower maintenance costs and
         faster development cycles. This is turning into a major win for the
         business, not just IT.î
For this study, we looked more closely at the approaches in use (Figure 1).
With two completely different software investment profiles, we expected
significantly different returns on investment.




© 2007 Aberdeen Group, Inc.                                                               Telephone: 617 723 7890
www.aberdeen.com                                                                                          041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 7

Figure 1: What Technologies Are Being Used?


                                       11%

   SOA using middleware
                                                           25%
      infrastructure
                                                                                              56%




                                                         23%
                                                                                                        LAG
   Web services, no SOA
                                                                       35%                              AVG
       middleware
                                                                                                        BIC
                                                                 28%




                                                   20%

  Mix of web services and
                                                                               40%
     SOA middleware
                                             17%




                            0%   10%          20%                30%         40%        50%     60%



                                                    Source: Aberdeen Group, July 2007


Why Enterprises Are Focusing on SOA Middleware
SOA can be a complex journey. There must be compelling business reasons
to invest heavily in both time and money in new technology such as ESBs,
governance, and development environments.
The top three drivers for Best-in-Class are different than those of the
Industry Average and Laggard groups (Figure 2):
    •    Improve time to market and agility of the IT department in
         responding to new business requirements;
    •    Improve service to end users;
    •    Reduce operating costs.




© 2007 Aberdeen Group, Inc.                                                                           Telephone: 617 723 7890
www.aberdeen.com                                                                                                      041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 8

Figure 2: Top drivers for SOA and web services



                                                                              53%
  Improve time to market /
           agility
                                                                                          62%




                                               25%
   Reduce operating costs
                                                              39%


                                                                                                       ALL OTHERS
                                                                                                       BIC

                                                                41%
   Improve service to end
           users
                                                                                      61%




                                                                                           64%
    Develop new business
         capabilties
                                                              39%




                             0%   10%   20%          30%     40%        50%         60%          70%


                                              Source: Aberdeen Group, July 2007




© 2007 Aberdeen Group, Inc.                                                                       Telephone: 617 723 7890
www.aberdeen.com                                                                                                  041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 9


Maturity Class Framework
Aberdeen used three key performance criteria to distinguish Best-in-Class
companies from Industry Average and Laggard organizations:
    •    Application maintenance costs
    •    Application development costs
    •    User satisfaction levels

Table 1: Companies With Top Performance Earn
Best-in-Class Status:
  Definition of
  Maturity Class              Mean Class Performance
 Best-in-Class:               •   100% saw reduction in application
 Top 20% of aggregate             development costs
 performance scorers          •   72% showed reductions in application
                                  maintenance costs
                              •   89% saw improvements in user satisfaction
                                  levels
 Industry Average:            •   59% saw reduction in application development
 Middle 50% of                    costs
 aggregate                    •   57% showed reductions in application
 performance scorers              maintenance costs
                              •   69% saw improvements in user satisfaction
                                  levels
 Laggard:                     •   23% saw increases in application development
 Bottom 30% of                    costs
 aggregate                    •   26% showed increases in application
 performance scorers              maintenance costs
                              •   14% saw improvements in user satisfaction
                                  levels
                                                  Source: Aberdeen Group, July 2007


Best-in-Class PACE Model
Aberdeenís methodology for understanding the top performing 20% of
companies ñ the Best-in-Class ñ looks at business pressures, potential
actions, organizational capabilities, and technology enablers.
The Best-in-Class (BIC) view SOA as a business strategy for accelerating the
delivery of game-changing products and services, not as IT modernization.




© 2007 Aberdeen Group, Inc.                                                           Telephone: 617 723 7890
www.aberdeen.com                                                                                      041207a
    SOA Middleware Takes the Lead:
    Picking Up Where Web Services
    Leaves Off
    Page 10


    Table 2: Best-in-Class PACE Framework

         Pressures                Actions                Capabilities                      Enablers
      • Improve the         • Lower complexity       • Measure application       • SOA infrastructure
        agility of the IT     of IT integration        lifecycle costs             middleware (i.e., ESB,
        department to       • Simplify and           • Deploy SOA                  repository, SOA
        respond to new        standardize              management and              management, etc.)
        business              development              governance software       • Legacy application
        requirements          infrastructure                                       modernization tools
                                                     • Apply new
                            • Re-skill application     methodologies and         • Application lifecycle and
                              development              architectures to new        governance software
                              teams                    application                 automation tools
                            • Deliver existing         development (e.g.,        • Web services application
                              application              SOA)                        development tools
                              functionality to       • Upgrade/replace           • Packaged software
                              partners via web         development tools           applications with SOA
                              browsers                 across application          capabilities
                                                       lifecycle




                                                       Source: Aberdeen Group, July 2007




                      Aberdeen Insights – Which Approach Is Best?
     The need for new and changed business processes greatly exceeds the
     ability of IT to deliver in a timely fashion using traditional software
     development methodologies and technologies. To solve this supply-
     demand imbalance, more than 90% of Global 5000 IT organizations by the
     end of 2006 had embarked on using a new architecture (SOA) and new
     development technologies. But they are taking different technology
     approaches to accomplish the goals of lower IT integration complexity,
     faster development cycles, and lower application lifecycle costs. Even more
     confusing, everyone calls what they are doing ìSOAî.
     With such a deep divide between the two approaches to distributed
     applications, web services or full SOA infrastructure, we wanted to know
     which would yield the larger benefits in terms of application lifecycle costs,
     productivity, and user satisfaction. Best-in-Class organizations are
     twice as likely as the industry average to have focused on SOA
     middleware infrastructure rather than web services. Only 17%
,    indicated that they used a combination of full SOA and web services in
r    their application development.
    In the next chapter, we will see what the top performers are doing to
    achieve these gains.


    © 2007 Aberdeen Group, Inc.                                                                          Telephone: 617 723 7890
    www.aberdeen.com                                                                                                     041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 11


               Chapter Two:
    Benchmarking Requirements for Success

In the realm of composite application development, companies that are                    Fast Facts
focusing on building out SOA middleware infrastructure are outpacing those
that are relying soleley on simple web services in several key performance               √ Best-in-Class companies are
                                                                                           twice as likely to have
areas.
                                                                                           deployed SOA middleware
                                                                                           rather than just web services.
                                                                                         √ 39%       of    Best-in-Class
         Case Study: Standard components make the difference at CFS                        organizations        measure
                                                                                           application lifecycle cost,
 Clinical Financial Services, in Pennsylvania, saw a business opportunity in the           versus 13% of the Industry
 pharmaceutical clinical trials area. With a vision to replace cumbersome, error-          Average.
 prone paper-based payment systems, the team quickly designed, developed, and            √ 41% of Best-in-Class are
 deployed an end-to-end electronic payment service marketed to large                       using SOA management and
 pharmaceutical firms. Replacing a paper-based system with an all-electronic               governance software. Only
 process from data collection to bank EFTs resulted in significantly increased user        17% of Industry Average and
 satisfaction for CFS’s customers.                                                         7% of Laggard companies are
                                                                                           using these critical tools.
 “Standards are the key to the speed with which we able to go from idea to market,”
 according to VP Glen Slater. “Standard components, industry messaging standards,
 and standard processes let us rapidly assemble a robust application to bring our
 service to the pharma market.”
 For CFS, the promise of SOA came through with standard components that
 interacted with each other in a message-based environment and interfaced to off-
 the-shelf accounting applications. The company was able to deliver a fully functional
 product to the market in just fifteen months from the initial concept.


Competitive Assessment
Survey respondents fell into one of three categories ñ Laggard, Industry
Average, or Best-in-Class ó based on their characteristics in five key
categories: (1) process (how the organization itself changes to
accommodate new business requirements); (2) organization (large-scale
changes in the IT department of technology or procedure); (3) knowledge
(training of key personnel in new technologies); (4) technology (selection
or appropriate tools and intelligent deployment of those tools); and (5)
performance management (ability of the organization to measure the
benefits of technology deployment and use the results to improve key
processes further).




© 2007 Aberdeen Group, Inc.                                                                    Telephone: 617 723 7890
www.aberdeen.com                                                                                               041207a
 SOA Middleware Takes the Lead:
 Picking Up Where Web Services
 Leaves Off
 Page 12




Table 3: Competitive Framework
                               Laggards               Average                Best-in-class
                      Applying new methodologies and architecture such as SOA to new
 Process              application development
                                 36%                   45%                       72%
                      IT department has upgraded or replaced development tools to
 Organization         accommodate new services-based architectures
                                 26%                   28%                       53%
                      Have deployed SOA operations management software
                                 5%                    14%                       47%

                      Re-skill application development teams in SOA technologies
 Knowledge
                                 28%                    25%                      61%

                      Web services-specific application development tools
 Technology
                                 63%                    62%                      83%

                      SOA infrastructure middleware

                                 32%                    38%                      61%
                      SOA governance software
                                 7%                     17%                      41%

                      Systematically measuring application lifecycle costs
  Performance
                                 11%                   13%                       39%
                                                    Source: Aberdeen Group, July 2007




 © 2007 Aberdeen Group, Inc.                                                                 Telephone: 617 723 7890
 www.aberdeen.com                                                                                            041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 13


Organizational Capabilities and Technology Enablers
SOA has been described in many places as a journey. During the past
eighteen months of research on SOA at Aberdeen, we have watched both
the technologies and the organizations using them mature significantly. The
Best-in-Class companies are still leading the charge, and with more overall
experience under their belts, they are setting the pace for the rest of the
industry.
This trend is clear in several key areas. For example, on the development
side, 53% of the Best-in-Class have already upgraded or replaced their
development tools in order to take advantage of better ways to create
services-based applications. Only 28% of the Industry Average and 26% of
the Laggards have completed this important step. However, both of those
groups are planning on catching up, with roughly 50% planning on upgrades
during the next six months, versus 29% for the Best-in-Class (Figure 3).
We see a similar curve in the area of training. Sixty one percent of Best-in-
Class have already completed training of key contributors in SOA
technologies, versus less than 30% for the Industry Average and Laggards.
During the next six months, however, the latter two groups are looking at
training: Sixty nine and 55% respectively (Figure 3).
These trends provide some comfort for the Industry Average and Laggard
organizations that are in the planning stages, and we will examine specific
steps for each group to take in the following chapter.

Figure 3: Trends in training and development tools



                                                      29%
 Have trained development
                                               24%
           team
                                                                                        61%




                                                                                 55%
  Plan to train development
                                                                                               69%
             team
                                                            33%
                                                                                                           LAG
                                                                                                           AVG
                                                                                                           BIC
                                                26%

      Have upgraded tools                            28%

                                                                                53%




                                                                                54%

      Plan to upgrade tools                                             45%

                                                      29%



                              0%   10%   20%         30%          40%     50%         60%     70%    80%



                                                            Source: Aberdeen Group, July 2007
© 2007 Aberdeen Group, Inc.                                                                                      Telephone: 617 723 7890
www.aberdeen.com                                                                                                                 041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 14




Process
The Best-in-Class organizations have, in general, been on the SOA journey
longer and therefore have had more time to establish policies around their
application work. They are twice as likely as the Laggard companies to have
created new approaches to application development, such as designing for
re-use, recognizing that composite and service-oriented software is
fundamentally different than what has been done before.


Significantly, Best-in-Class are nearly four times more often actually
measuring what it costs to create and deploy applications. The old rubric,
ìYou canít manage what you donít measure,î is just as true in the software
world as it is elsewhere. The rigor of measure-change-repeat allows IT to
actively refine their processes with measurable results.



Figure 4: Best-in-Class places an emphasis on process




                                      13%


   Measuring application
                                  11%
      lifecycle costs


                                                          39%



                                                                                                   LAG
                                                                                                   AVG
                                                                                                   BIC



                                                        36%


    Implemented new
   approaches for SOA                                           45%
 application development

                                                                                       72%




                           0%   10%         20%   30%    40%      50%    60%     70%         80%


                                                        Source: Aberdeen Group, July 2007




© 2007 Aberdeen Group, Inc.                                                                              Telephone: 617 723 7890
www.aberdeen.com                                                                                                         041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 15


Organization
One way that Best-in-Class companies have shifted their thinking is in the
area of the development environment. While it is possible to create
services-based applications with nothing more than a text editor, the
optimal approach is to use purpose-built development environments. This
sort of fundamental change must come from the top down, and Best-in-
Class departments are twice as likely to have taken this important step.
Industry Average and Laggards also understand the benefits, however, and
two-thirds of each group indicate that they plan to roll out new
development environments in the next six months.



Figure 5: New and upgraded development environments




                                           26%



           In place                          28%



                                                                             53%



                                                                                          LAG
                                                                                          AVG
                                                                                          BIC



                                                                              54%



  Plan to implement                                              45%



                                                 29%




                      0%      10%   20%       30%        40%           50%          60%


                                            Source: Aberdeen Group, July 2007




© 2007 Aberdeen Group, Inc.                                                                     Telephone: 617 723 7890
www.aberdeen.com                                                                                                041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 16


Knowledge
Training, often the poor step-child of technology, or simply an afterthought,
instead is the underpinning of success for Best-in-Class IT organizations.
While less than a third of Laggard and Industry Average companies have
spent the time and money to retrain the IT staff, 61% of Best-in-Class have
made this critical investment.


Both SOA and web services application development pose unique challenges
to the skills of the department. It is tempting to assume that the smart
people you hired to write and manage applications in other technologies will
ìjust figure it out,î but across the board, companies are realizing that formal
retraining is worthwhile (Figure 6).



Figure 6: Retraining of application development teams




                                            29%



 Have retrained                      24%



                                                                            61%



                                                                                                    LAG
                                                                                                    AVG
                                                                                                    BIC



                                                                      55%



  Plan to retrain                                                                  69%



                                                  33%




                    0%   10%   20%         30%          40%     50%      60%      70%         80%


                                                          Source: Aberdeen Group, July 2007




© 2007 Aberdeen Group, Inc.                                                                               Telephone: 617 723 7890
www.aberdeen.com                                                                                                          041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 17


Technology
The seed of this research was an observation made over several SOA
studies: While everyone reported that they were implementing SOA
applications, about half were in fact developing web services, and the other
half were focusing on full SOA infrastructure. For this benchmark, we
hypothesized that organizations investing in SOA middleware, including
ESBs, repositories, governance, and registries, would outperform those
organizations concentrating on just web services in several key metrics. For
the purposes of this report, we defined web services as applications based
on XML, UDDI directories, SOAP, and WS* standards, but not using SOA.
The results support our hypothesis. As shown in Chapter 1, we measured
Best-in-Class on a number of key performance indicators such as
improvement in application development costs, user satisfaction, and the
number of completed projects. Once Best-in-Class was determined, we
looked at the technologies that the group uses (Figure 7).
Fifty six percent of Best-in-Class are focusing primarily on SOA
infrastructure, versus 31% of the Industry Average. Only 11% of the
Laggards are building and deploying SOA applications.
Another key differentiator is SOA governance software. As projects move
from pilot to production, the interaction of services across the ESB
increases. The number of combinations and permutations can quickly grow
to a number which humans canít manage. To handle the complexity, 41% of
Best-in-Class are using automated governance software, while only 17% of
Industry Average and 7% of Laggard organizations are doing so. One
explanation is that the latter two groups are simply following the Best-in-
Class in the SOA journey, and this is supported by noting that just under
70% are planning on implementing this functionality in the next six to twelve
months.
One of the challenges of SOA applications is in testing them. The QA
environment is quite a bit different than that for traditional applications.
Across the board, all groups indicate that deploying new testing
methodologies is a high priority in the next twelve months.




© 2007 Aberdeen Group, Inc.                                                     Telephone: 617 723 7890
www.aberdeen.com                                                                                041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 18

Figure 7: Approaches to SOA and web services technology

                                                           11%
                 Implementing SOA middleware                                   31%
                                                                                                      56%

                                                                       23%
                      Implementing web service                                      34%
                                                                             28%

                                                                   20%
   Using a combination of SOA and web services                                      34%
                                                                 17%




                                                      6%                                                              LAG
       Have deployed SOA governance software                     17%                                                  AVG
                                                                              29%                                     BIC

                                                                             28%
        Plan to deploy SOA governance software                                           38%
                                                                                          39%




                                                                                   33%
  Employing new approaches to SOA test and QA                          24%
                                                                                   33%

                                                                                                46%
 Plan to use new approaches to SOA test and QA                                                          59%
                                                                                                          61%

                                                 0%   10%        20%         30%         40%    50%   60%       70%


                                                                   Source: Aberdeen Group, July 2007

                               Aberdeen Insights – Technology

Best-in-Class companies understand that SOA is a complex approach to application
development, and they are making key investments not only in SOA middleware, but
also in enabling technologies such as automated testing software. Governance
practices, both run-time and design-time, are crucial parts of any SOA strategy; Best-
in-Class organizations are placing as much emphasis on them as they are on
middleware itself.
The mixed-technology approach, using a combination of web services and SOA
infrastructure, might seem an attractive middle ground, but the added complexity
makes for unnecessary stumbling blocks in the enterprise. Pick one or the other, and
stick with it.




© 2007 Aberdeen Group, Inc.                                                                                                 Telephone: 617 723 7890
www.aberdeen.com                                                                                                                            041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 19



Performance
They say that the proof is in the pudding, and in this study the proof is in
cost savings. One hundred percent of the Best-in-Class, those companies
that are concentrating on SOA middleware rather than web services, report
that application development costs have improved. While 59% of the
Industry Average have seen improvement, 0% of the Laggard group has.
Twenty three percent report that costs have increased (Figure 8).



Figure 8: Application costs

                                  0%
  Development cost: Improved                                                          59%
                                                                                                                 100%

                                                     19%
                   No change                                            38%
                                  0%

                                                          23%
                       Worse        3%
                                  0%




                                         7%
  Maintenance cost: Improved                                                         57%
                                                                                             72%
                                                                                                                               LAG
                                              12%
                   No change                                      32%                                                          AVG
                                                                28%
                                                                                                                               BIC
                                                            26%
                       Worse           4%
                                  0%




                                         7%
      Lifecycle cost: Improved                                    33%
                                                                                                         89%

                                            9%
                   No change                              22%
                                              11%

                                                                                                   78%
                       Worse                              22%
                                  0%

                                 0%                 20%             40%              60%        80%            100%     120%

                                                                              Source: Aberdeen Group, July 2007




© 2007 Aberdeen Group, Inc.                                                                                                     Telephone: 617 723 7890
www.aberdeen.com                                                                                                                                041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 20


                           Chapter Three:
                          Required Actions
Based on the information in Chapters One and Two, readers should
determine whether their organizations fall into the ìLaggardî, ìIndustry
Average,î or ìBest-in-Classî categories. The key to gaining value from this
report is moving your organization along the maturity path to Best-in-Class.
The following actions will help spur necessary performance improvements:

Laggard Steps to Success
    •    Upgrade development tools now. Couple training with either
         upgraded or new development environments that take advantage of
         SOA technology. The Best-in-Class have already completed this
         cycle and are seeing significantly lower application development
         costs.
    •    Move beyond web services. Simple web services suffice for some
         applications, but look to SOA to move to the next level of service.
         Avoid mixing web services and SOA: The added complexity will
         reduce your organizationís effectiveness.
    •    Deploy SOA governance software. Both run-time and design-
         time governance help unlock the promise of SOA. Without
         governance, SOA environments quickly devolve into a morass of
         functionally similar objects with multiple, possibly incompatible,
         versions. Change control is critical in a fully evolved SOA
         environment.

Industry Average Steps to Success
    •    Focus on infrastructure. While building out a SOA middleware
         infrastructure might seem daunting, in the long run the rewards
         reaped from it will include better productivity, a simplified
         application landscape, and higher levels of end-user satisfaction.
    •    Measure, adjust, and repeat. One clear indicator of Best-in-
         Class organizations is that they consistently measure organizational
         performance, make adjustments, and look for improvement. By not
         measuring key performance metrics such as application lifecycle
         costs, Industry Average companies cannot make intelligent decisions
         about IT investments.
    •     Donít skimp on training. Even though SOA applications are
         similar to earlier distributed architectures that you may have
         experience with, the differences are significant and require new
         approaches to design and development.




© 2007 Aberdeen Group, Inc.                                                     Telephone: 617 723 7890
www.aberdeen.com                                                                                041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 21


Best-in-Class Steps to Success
    •    Re-tool QA and test processes. Functional testing isnít enough
         for SOA applications; integration testing is an absolute requirement.
         Forward-thinking IT organizations are starting to reshape their
         thinking around QA to encompass the complexity of SOA.
    •    Focus on performance. As SOA deployments become more
         complex, bottlenecks will start to develop. Scalability and
         performance of SOA applications are complicated by the black-box
         approach to SOA components. Investing in performance
         methodologies now will pay off in improvements in SLAs and
         throughput later.


                          Aberdeen Insights – Summary

Over the past two years we have seen SOA technologies and the organizations using
them mature as work moved from pilot to production. Lessons learned during early
deployments are now being applied to new projects, and as the leading edge of the
technology change moves from small SOA environments to larger, more complex
systems, new challenges such as scalability and testability are emerging.
The divide between web services and full SOA is growing wider. Organizations must
re-evaluate their application strategy in the light of a more mature market and decide
if the path that they are on will support critical business requirements over the next
decade.
Upcoming Aberdeen reports will look closely at how Best-in-Class companies are
managing QA and testing of SOA and web services applications, and at approaches
to building performance into composite applications.




© 2007 Aberdeen Group, Inc.                                                              Telephone: 617 723 7890
www.aberdeen.com                                                                                         041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 22


                         Appendix A:
                     Research Methodology

Between April and May 2007, Aberdeen Group examined the responses of
more than 150 companies across a variety of geographies, industries and
company revenues.
Aberdeen supplemented this online survey effort with telephone interviews
with select survey respondents, gathering additional information on SOA
management strategies, experiences, and results.
The study aimed to identify emerging best practices for SOA operations
management and governance, and provide a framework by which readers
could assess their own organizationís capabilities and maturity.
Responding enterprises included the following:
    •    Job title/function: About two-thirds of the survey respondents are
         in their organizationsí IT departments. The research sample
         included respondents with the following job titles: senior executive
         (CEO, COO, CFO, VP) (25%); CIO (10%); IT manager or director
         (42%); internal consultant (7%), and IT staff (9%).
    •    Industry: The research sample included respondents predominantly
         from high-technology industries and companies. These represented
         20% of the sample. A significant number of respondents were in the
         transportation and logistics industries (8%), and finance and banking
         (9%).
    •    Geography: The survey respondents were distributed: North
         America (U.S., Canada, Mexico) 51%; Central and South America
         4%; Asia/Pacific 17%; Europe, Middle East, and Africa 28%.
    •    Company size: About 24% of respondents were from large
         enterprises (annual revenues above U.S. $1 billion, including 11%
         over U.S. $5 billion); 35% were from midsize enterprises (annual
         revenues between $50 million and $1 billion); and 41% of
         respondents were from small businesses (annual revenues of $50
         million or less).
Solution providers recognized as sponsors of this report were solicited after
the fact and had no substantive influence on the direction of this report.
Their sponsorship has made it possible for Aberdeen Group to make these
findings available to readers at no charge.
Solution providers recognized as sponsors of this report were solicited after
the fact and had no substantive influence on the direction of the report.
Their sponsorship has made it possible for Aberdeen Group to make these
findings available to readers at no charge.




© 2007 Aberdeen Group, Inc.                                                      Telephone: 617 723 7890
www.aberdeen.com                                                                                 041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 23


Table 4: PACE Framework

PACE Key

Aberdeen applies a methodology to benchmark research that evaluates the business
pressures, actions, capabilities, and enablers (PACE) that indicate corporate behavior in
specific business processes. These terms are defined as follows:
Pressures — external forces that impact an organization’s market position, competitiveness,
or business operations (e.g., economic, political and regulatory, technology, changing
customer preferences, competitive)
Actions — the strategic approaches that an organization takes in response to industry
pressures (e.g., align the corporate business model to leverage industry opportunities, such
as product/service strategy, target markets, financial strategy, go-to-market, and sales
strategy)
Capabilities — the business process competencies required to execute corporate strategy
(e.g., skilled people, brand, market positioning, viable products/services, ecosystem
partners, financing)
Enablers — the key functionality of technology solutions required to support the
organization’s enabling business practices (e.g., development platform, applications,
network connectivity, user interface, training and support, partner interfaces, data cleansing,
and management)

                                                          Source: Aberdeen Group, July 2007




© 2007 Aberdeen Group, Inc.                                                                       Telephone: 617 723 7890
www.aberdeen.com                                                                                                  041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 24


Table 5: Maturity Framework

Maturity Framework Key

The Aberdeen Maturity Framework defines enterprises as falling into one of the following
three levels of practices and performance:
Best-in-class (20%) — practices that are the best currently being employed and significantly
superior to the industry norm, and result in the top industry performance.
Industry norm (50%) —practices that represent the average or norm, and result in average
industry performance.
Laggards (30%) —practices that are significantly behind the average of the industry, and
result in below average performance
In the following categories:
Process — What is the scope of process standardization? What is the efficiency and
effectiveness of this process?
Organization — How is your company currently organized to manage and optimize this
particular process?
Knowledge — What visibility do you have into key data and intelligence required to manage
this process?
Technology — What level of automation have you used to support this process? How is this
automation integrated and aligned?
Performance — What do you measure? How frequently? What’s your actual performance?

                                                        Source: Aberdeen Group, July 2007

Table 6: Relationship between PACE and
Competitive Framework

PACE and Competitive Framework How They Interact
Aberdeen research indicates that companies that identify the most impactful pressures and
take the most transformational and effective actions are most likely to achieve superior
performance. The level of competitive performance that a company achieves is strongly
determined by the PACE choices that they make and how well they execute.

                                                        Source: Aberdeen Group, July 2007




© 2007 Aberdeen Group, Inc.                                                                    Telephone: 617 723 7890
www.aberdeen.com                                                                                               041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 25


                             Appendix B:
                      Related Aberdeen Research
Related Aberdeen research that forms a companion or reference to this
report include:
      •     Service-Oriented Architectures (October 2005)
      •     The SOA in IT Benchmark Report (December 2005)
      •     The Legacy Application Migration Benchmark Report (September
            2006)
      •     The Composite Applications Benchmark Report (December 2006)
      •     Management and Governance: Planning for an Optimized SOA
            Application Lifecycle (March 2007)
      •     Modernizing Legacy Applications: Maximizing the Investment (June
            2007)
Information on these and any other Aberdeen publications can be found at
www.Aberdeen.com.


                    Author: Perry Donham, Director, Enterprise Integration Research
                                    (perry.donham@aberdeen.com)
Founded in 1988, Aberdeen Group is the technology- driven research destination of choice for the global business
executive. Aberdeen Group has over 100,000 research members in over 36 countries around the world that both
participate in and direct the most comprehensive technology-driven value chain research in the market. Through its
continued fact-based research, benchmarking, and actionable analysis, Aberdeen Group offers global business and
technology executives a unique mix of actionable research, KPIs, tools, and services.
This document is the result of research performed by Aberdeen Group. Aberdeen Group believes its findings are
objective and represent the best analysis available at the time of publication. Unless otherwise noted, the entire
contents of this publication are copyrighted by Aberdeen Group, Inc. and may not be reproduced, stored in a retrieval
system, or transmitted in any form or by any means without prior written consent by Aberdeen Group, Inc.




© 2007 Aberdeen Group, Inc.                                                                                             Telephone: 617 723 7890
www.aberdeen.com                                                                                                                        041207a
SOA Middleware Takes the Lead:
Picking Up Where Web Services
Leaves Off
Page 26


                     Featured Underwriters
This research report was made possible, in part, with the financial support
of our under-writers. These individuals and organizations share Aberdeenís
vision of bringing fact based research to corporations worldwide at little or
no cost. Underwriters have no editorial or research rights and the facts and
analysis of this report remain an exclusive production and product of
Aberdeen Group.

                 BEA Systems, Inc. (Nasdaq: BEAS) is a world leader in
                 enterprise infrastructure software, delivering powerful
                 standards-based platforms for building enterprise
                 applications and managing Service-Oriented Architectures
                 even in heterogeneous IT environments. Customers
depend on BEA AquaLogicÆ, WebLogicÆ and TuxedoÆ product lines to
reduce IT complexity, leverage existing resources, and speed the delivery of
new services. Information about how BEA is enabling customers to
transform their business by building a Liquid Enterprise(TM) can be found at
www.bea.com.

For additional information on BEA Systems, Inc.:
2315 North First Street, San Jose, CA 95131
Tel: 800-817-4BEA
www.bea.com
nvalencia@bea.com


                                As Hitachi, Ltd.'s (NYSE: HIT) global
                              consulting company, Hitachi Consulting is a
                              recognized leader in delivering proven
business and IT solutions to Global 2000 companies. We leverage decades
of business process, vertical industry, and leading-edge technology
experience to understand each company's unique needs. From business
strategy development through application deployment, we are committed to
helping clients quickly realize measurable business value and achieve
sustainable ROI. Our SOA framework enables companies to deploy
enterprise-class business applications, regardless of where they are within
their implementation lifecycle. We offer a client-focused, collaborative
approach and transfer knowledge throughout each engagement.

Hitachi Consulting ó Inspiring your next success!Æ
For additional information on Hitachi Consulting:
2001 Bryan Street, Suite 3600, Dallas, TX 75201
Tel: 877-664-0010
www.hitachiconsulting.com
info@hitachiconsulting.com



© 2007 Aberdeen Group, Inc.                                                     Telephone: 617 723 7890
www.aberdeen.com                                                                                041207a
Modernizing Legacy Applications:
  Maximizing the Investment

                June 2007



         — Underwritten, in Part, by —
Modernizing Legacy Applications:
Maximizing the Investment
Page 2



                        Executive Summary

IT is under intense pressure to provide new ways for the business to access    “We are going from 12,000
data and functionality runnning on legacy platforms. Legacy code often         applications to hundreds of
embodies the core processes of the company, and simply rewriting it is both    services using an SOA. The
prohibitively expensive and disruptive. In many cases, the best thing to do    lifecycle cost savings are already
both from a performance and cost standpoint is to leave the legacy code        flowing through in lower
alone.                                                                         maintenance costs and faster
                                                                               development cycles. This is turning
Organizations that are SOA-enabling their legacy applications on the legacy    into a major win for the business,
platform are outperforming those that are using any other approach. They       not just IT.”
report better productivity, higher agility, and lower costs for legacy         ~ VP, Financial Services
integration projects.

Best in Class Performance
Four key performance indicators (KPIs) were used to identify those
companies that are succeeding in their legacy modernization efforts,
Aberdeen’s Best In Class (BIC):
    •    Overall cost of legacy integration projects
    •    Number of new applications delivered that are based on legacy
         applications
    •    Time-to-value for customer-facing projects
    •    Agility of IT in responding to new business requirements

Competitive Maturity Assessment
Each organization tailors its approach to legacy modernization based on
their application portfolio. The Best In Class in this study understand that
modernization projects are not just about technology; they also require
changes to key processes.
The typical Best In Class organization:
    •    Uses automation to extract business logic from legacy applications
         (61%)
    •    Is SOA-enabling their legacy applications on the legacy platform
         (33%)
    •    Is using SOA to increase the agility of the IT department in
         responding to new business requirements (40%)
    •    Has planned for the unique challenges of testing legacy application
         integration by putting new test processes into place (61%)
    •    Has SLAs in place for legacy interfaces (63%)
    •    Sees their legacy modernization projects as a long-term solution
         (91%)
© 2007 Aberdeen Group, Inc.                                                        Telephone: 617 723 7890
www.aberdeen.com                                                                                   041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 3


Required Actions
Legacy modernization projects touch core components of your business.
Take these steps to minimize the risk and maximize the investment:
    •    Automate. Most legacy applications are a mix of data and logic,
         and the interfaces are often not clearly defined. Using automated
         tools to extract business logic and data structure will let you focus
         on solving the business problem.
    •    Plan for test. Best In Class organizations are twice as likely as
         Industry Average or Laggards to have well-defined test processes
         for integration testing.
    •    Build a services layer on the mainframe. Exposing legacy
         packages through a services layer minimizes disruption to the
         business and reduces risk.




© 2007 Aberdeen Group, Inc.                                                      Telephone: 617 723 7890
www.aberdeen.com                                                                                 041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 4



Table of Contents
Executive Summary....................................................................................................... 2
    Best in Class Performance ......................................................................... 2
    Competitive Maturity Assessment........................................................... 2
    Required Actions ......................................................................................... 3
Chapter One: Benchmarking the Best in Class...................................................... 6
    Aberdeen Analysis ....................................................................................... 6
    Why Enterprises Are Focusing on Legacy Modernization.................. 7
    Maturity Class Framework ........................................................................ 9
    Best in Class PACE Model .......................................................................10
Chapter Two: Benchmarking Requirements for Success ..................................11
    Competitive Assessment..........................................................................11
    Organizational Capabilities and Technology Enablers .......................13
      Process.....................................................................................................14
      Organization ...........................................................................................15
      Knowledge ..............................................................................................16
      Technology..............................................................................................17
      Performance ...........................................................................................19
Chapter Three: Required Actions .........................................................................20
    Laggard Steps to Success..........................................................................20
    Industry Norm Steps to Success ............................................................20
    Best in Class Steps to Success ................................................................21
Featured Underwriters..............................................................................................22
Appendix A: Research Methodology.....................................................................24
Appendix B: Related Aberdeen Research............................................................27


Figures
Figure 1: What Approaches Are Being Used?........................................................ 6
Figure 2: Top drivers for legacy modernization efforts ....................................... 7
Figure 3: Modernization approach reflects organizational drivers .................... 8
Figure 3: Organizational view of modernization..................................................13
Figure 4: Best in Class place an emphasis on process ........................................14
Figure 5: Agreement among departments drives success .................................15
Figure 6: Training of developers, analysts, and architects .................................16
Figure 7: Technical approaches to legacy modernization..................................17
Figure 8: Best In Class see improvements in costs and productivity..............19




© 2007 Aberdeen Group, Inc.                                                                                                  Telephone: 617 723 7890
www.aberdeen.com                                                                                                                             041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 5




Tables
Table 1: Companies With Top Performance Earn “Best-in-Class” Status:.... 9
Table 2: Best-in-Class PACE Framework ..............................................................10
Table 3: Competitive Framework ...........................................................................12
Table 4: PACE Framework .......................................................................................25
Table 5: Maturity Framework...................................................................................25
Table 6: Relationship between PACE and Competitive Framework ..............26




© 2007 Aberdeen Group, Inc.                                                                                         Telephone: 617 723 7890
www.aberdeen.com                                                                                                                    041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 6



                            Chapter One:
                     Benchmarking the Best in Class
Aberdeen Analysis                                                                                                   Fast Facts
                                                                                                                    √ 61% of Best In Class
                                                                                                                      organizations report a
Legacy applications often contain the organization’s core business                                                    decrease in the cost of legacy
functionality and represent large capital investments in both dollars and                                             platform maintenance costs
manpower. Wholesale replacement of these applications is impractical for
                                                                                                                    √ 70% of Best In Class
time and cost reasons.
                                                                                                                      companies have clearly
Faced with competing pressures to preserve the investment in legacy                                                   documented legacy packages
applications and platforms, to provide new IT services to support changing                                            and data structures
business requirements, and to minimize disruption to existing processes, IT                                         √ 90% of Best In Class see
typically responds in one of two general ways:                                                                        their legacy modernization
                                                                                                                      projects as a long-term,
     •       Extend/surround, to provide new interfaces to the legacy                                                 strategic plan
             application, either on the mainframe or off, in order to open it up to
             web services or SOA middleware;
     •       Re-host, moving the entire legacy application to a new platform
             while preserving the existing code base.
Figure 1 shows that Best In Class organizations more often choose to leave
packages on the legacy platform and use software adapters or a services
layer to provide access to other SOA applications.

     Figure 1: What Approaches Are Being Used?


                                                     15%
      SOA-Enable on the legacy
                                                   14%
             platform
                                                                                           33%




                                                           17%
    SOA-enable off of the legacy
                                             8%
            platform
                                                                 19%
                                                                                                              LAG
                                                                                                              AVG
                                                                                                              BIC
                                                                                   27%

 Extend with messaging software                                                            33%

                                                                       21%




                                                                                           33%

         Re-host or migrate code                                                                  39%

                                                                       21%



                                   0%   5%   10%   15%       20%             25%     30%    35%   40%   45%



                                                                             Source: Aberdeen Group, June 2007



© 2007 Aberdeen Group, Inc.                                                                                                 Telephone: 617 723 7890
www.aberdeen.com                                                                                                                            041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 7


Why Enterprises Are Focusing on Legacy
Modernization

     Agility is at the top of the list for Best In Class organizations trying to
     bring their legacy applications into a modern architecture. This means
     the ability to rapidly build services, based on legacy functionality and
     data, that provide solutions to new business problems. While cost is a
     consideration, it is not the driving factor for this group (Figure 2).

Figure 2: Top drivers for legacy modernization efforts



                                                       17%
   Open legacy applications
      and data to new
         applications                                                    26%




                                                                                           37%
 Reduce overall IT operation                                                                                 Others
          costs                                                                                              BIC
                                                                         26%




                                                             20%

        Increase agility of IT
                                                                                                 40%




                                 0%   5%   10%   15%     20%       25%         30%   35%     40%       45%



                                                                   Source: Aberdeen Group, June 2007

     Key drivers for the Industry Average and Laggard groups center more
     around cost, and this is reflected in their overall approach to legacy
     modernization. While Best In Class organizations are leveraging their
     SOA infrastructure to provide interfaces into their legacy applications,
     Industry Average and Laggard companies opt for re-hosting, which
     moves the legacy code base to a less expensive hardware platform
     (Figure 3).




© 2007 Aberdeen Group, Inc.                                                                                           Telephone: 617 723 7890
www.aberdeen.com                                                                                                                      041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 8


Figure 3: Modernization approach reflects organizational drivers

  50%
              47%

  45%


                                                     40%
  40%



  35%



  30%



  25%                                                               Reduce IT operation cost

                                      20%                           Increase agility of IT
  20%
                              18%


  15%



  10%



   5%



   0%
                    Re-host                 Extend

                                                     Source: Aberdeen Group, June 2007



Operational costs can be a significant driver. As Larry Munini, President of
Genesys, a human-capital management (HCM) software vendor in business
for 26 years puts it, “This code is our business. It’s what we do. But at the
end of the day, our customers don’t care what lights up their web
browser.” Moving COBOL packages from the mainframe to less expensive
Intel platforms resulted in major cost savings. Where performance was
essential, VSAM files were left in place.
Choosing re-hosting on a cost basis alone may lead to disappointment. Of
those organizations that chose this approach, only 19% reported a
reduction in the cost of legacy integration projects. Forty two percent said
that their legacy infrastructure capital costs had decreased.




© 2007 Aberdeen Group, Inc.                                                                    Telephone: 617 723 7890
www.aberdeen.com                                                                                               041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 9




Maturity Class Framework
Aberdeen used four key performance criteria to distinguish Best in Class
companies from Industry Average and Laggard organizations:
    •    Overall cost of legacy integration projects
    •    Number of new applications delivered that are based on legacy
         applications
    •    Time-to-value for customer-facing projects
    •    Agility of IT in responding to new business requirements


With Best In Class identified, we then looked at how the group compared
to the Industry Average and Laggard organizations (Table 1).

Table 1: Companies With Top Performance Earn “Best-in-Class”
Status
  Definition of
  Maturity Class              Mean Class Performance
 Best in Class:               •    46% saw reduction in legacy integration costs
 Top 20% of aggregate         •    43% reported an increase in the number of
 performance scorers               new application delivered that were based on
                                   legacy packages
                              •    61% saw a decrease in the cost of maintenance
                                   for legacy platforms
 Industry Average:            •    9% saw reduction in legacy integration costs
 Middle 50% of                •    21% reported an increase in the number of
 aggregate                         new application delivered that were based on
 performance scorers               legacy packages
                              •    30% saw a decrease in the cost of maintenance
                                   for legacy platforms
 Laggard:                     •    13% saw increases in legacy integration costs
 Bottom 30% of                •    8% reported a decrease in the number of new
 aggregate                         application delivered that were based on legacy
 performance scorers               packages
                              •    5% saw a decrease in the cost of maintenance
                                   for legacy platforms
                                                       Source: Aberdeen Group, 2007




© 2007 Aberdeen Group, Inc.                                                           Telephone: 617 723 7890
www.aberdeen.com                                                                                      041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 10



Best in Class PACE Model
Aberdeen uses the PACE model to profile the top performing 20% of
companies – the Best In Class – in four areas:
    •    Pressures: External or internal pressures affecting an organization.
         These might be economic, technical, strategic, or competitive.
    •    Actions: The ways that an organization responds to pressures.
    •    Capabilities: The internal capabilities that an organization must have
         to take the specified actions.
    •    Enablers: Technical products, procedures, or designs necessary to
         carry out actions.
The Best in Class are using SOA and web services to quickly respond to
new business requirements by extending legacy packages and data out to
the enterprise.

Table 2: Best-in-Class PACE Framework

     Pressures                Actions              Capabilities                      Enablers
  • Improve the         • Extend legacy       • Services-based              • Third-party adapters for
    agility of the IT     code to provide       infrastructure is in          legacy systems
    department            new interfaces to     place                       • SOA/web services layer on
    when                  service-based       • Business and IT               the mainframe
    responding to         architectures         processes are aligned       • Automated tools for
    new business        • Surround legacy     • Legacy applications           extracting legacy data and
    requirements          applications with     and interfaces are well       business logic
                          messaging             defined                     • Middleware platforms for
                          middleware
                                                                              rehosting
                        • Re-host legacy
                          code


                                                                          Source: Aberdeen Group, June 2007


                         Aberdeen Insights – Which Approach Is Best?
        Aberdeen research of over 400 companies in the past 18 months has shown
        that Best In Class IT organizations have embraced SOA as a way to rapidly
        develop and deploy solutions to new business problems. In the realm of
        legacy applications, this approach is paying off: Companies that are
        leveraging their investment in SOA are outperforming their competitors by
        using it to build new applications based on legacy code and data.
        Re-hosting remains an attractive alternative for those organizations that are
        sensitive to cost, but only 19% of respondents who chose re-hosting
        reported a decrease in the overall cost of IT integration projects.


© 2007 Aberdeen Group, Inc.                                                                        Telephone: 617 723 7890
www.aberdeen.com                                                                                                   041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 11



               Chapter Two:
    Benchmarking Requirements for Success

Best In Class IT organizations are leveraging both their investment in legacy             Fast Facts
platforms and their existing SOA infrastructure. They are focusing on
extending their legacy applications on the mainframe by building a services               √ Best In Class companies are
                                                                                            twice as likely as other
layer that exposes legacy data and packages.
                                                                                            groups to use automated
                                                                                            tools for extracting business
                                                                                            logic and data structures
         Case Study: Standard components make the difference at CFS                       √ 43% of Best In Class
 Brian Digman, CIO of the Enterprise Services Division of the State of New York             organizations use third-party
 Department of Taxation and Finance, faced mounting costs, an aging staff of                services adapters for legacy
                                                                                            applications, versus 28% of
 COBOL programmers, systems that weren’t much younger, tens of millions of lines
                                                                                            the Laggards group
 of legacy code, proprietary databases, and a workflow that included multiple paper
 steps. There were few web interfaces, and a significant backlog of work.                 √ Twice as many Best In
                                                                                            Class companies versus all
 The vision: Adopt an SOA approach to modernization using XML to facilitate                 others have deployed a SOA
 communication, provide new ways to access existing applications and data, and              or web services layer on the
 eliminate as much paper processing as possible. Starting with a pilot project              mainframe
 focused on handling exceptions in sales tax processing, the team architected an
 SOA solution that wraps business components with new web-based interfaces,
 keeping COBOL in place where it made sense, and used XML as a common
 language for messaging. Automating the workflow helped remove paper from the
 picture. XML also provided ways to build tax forms on the fly on web clients, both for
 internal processing and for taxpayer use, and to hook into other systems such as
 interactive voice response. By moving most processing to memory, performance
 increased dramatically. On a key inbound processing step, throughput went from
 18,000 transactions per hour to over 60,000.
 “The ROI was staggering,” says Digman. “We removed the paper, reduced our
 exception backlog by 60%, and lowered the cost of labor by using standard
 packages instead of custom code. SOA is now helping DTF transform our highest-
 volume system, personal income tax, from batch to transactional processing using
 XML, electronic forms, and middleware for business process orchestration.”.


Competitive Assessment
Survey respondents fell into one of three categories – Laggard, Industry
Average, or Best in Class — based on their characteristics in five key
categories: (1) process (how the organization itself changes to
accommodate new business requirements); (2) organization (large-scale
changes in the IT department of technology or procedure); (3) knowledge
(training of key personnel in new technologies); (4) technology (selection
or appropriate tools and intelligent deployment of those tools); and (5)
performance management (ability of the organization to measure the
benefits of technology deployment and use the results to improve key
processes further).


© 2007 Aberdeen Group, Inc.                                                                     Telephone: 617 723 7890
www.aberdeen.com                                                                                                041207a
     Modernizing Legacy Applications:
     Maximizing the Investment
     Page 12




Table 3: Competitive Framework
                           Laggards                 Average                Best-in-class

 Process            Legacy applications and interfaces are documented

                              54%                       56%                     70%
                    Integration processes are defined
                              45%                       41%                     62%
                    Testing processes for legacy integration are defined
                              40%                       33%                     61%

                    Business and IT processes are aligned
 Organization
                              41%                       49%                     60%

                    Key developers, business analysts, and architects are trained
 Knowledge
                              38%                       35%                     51%

                    Third-party adapters for legacy applications
 Technology
                              28%                       36%                     43%

                    SOA / Web services layer on the mainframe

                              15%                       12%                     32%
                     Automated tools for extracting business logic and data
                              19%                       20%                     38%

                     Integrated development environments (IDEs) aimed at legacy systems

                              25%                       35%                     56%

                    Service level agreements (SLAs) for legacy interfaces are in place
 Performance
                              30%                       43%                     63%
                                                        Source: Aberdeen Group, June 2007




     © 2007 Aberdeen Group, Inc.                                                            Telephone: 617 723 7890
     www.aberdeen.com                                                                                       041207a
    Modernizing Legacy Applications:
    Maximizing the Investment
    Page 13



    Organizational Capabilities and Technology Enablers
    SOA has been described in many places as a journey. During the past
    eighteen months of research on SOA at Aberdeen, we have watched both                                                    “After looking through all of
    the technologies and the organizations using them mature significantly. The                                             the code running on the
    Best In Class companies are still leading the charge, and with more overall                                             mainframe, we discovered that
    experience under their belts, they are setting the pace for the rest of the                                             40% of it was unused…and
    industry. Over half of the Best In Class organizations are either working on                                            about 10% of it nobody knew
,   or have completed at least one legacy modernization project, versus fewer                                               what it was supposed to do.”
r   than a quarter of Laggards (Figure 3).
                                                                                                                            ~ Manager, SOA modernization
    All groups see their modernization efforts as a long-term solution. Industry                                            vendor
    Average and Laggards, trailing Best In Class in experience, are also likely to
    be running proof-of-concept and pilot projects.

    Figure 4: Organizational view of modernization




                                                        32%

     Experience: One or more
      modernization projects
                                                                          52%




                                                                                                                   Others
                                                                                                                   BIC




                                                                                            74%

      Modernizationis a long-
      term, strategic solution
                                                                                                      90%




                                 0%   10%   20%   30%         40%   50%         60%   70%     80%   90%     100%



                                                                            Source: Aberdeen Group, June 2007




    © 2007 Aberdeen Group, Inc.                                                                                                  Telephone: 617 723 7890
    www.aberdeen.com                                                                                                                             041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 14



Process
The Best In Class organizations have, in general, been on the SOA
journey longer and therefore have had more time to establish policies
around their application work. This maturity is reflected in an
emphasis on process versus the Industry Average and Laggard groups
(Figure 4).

One of the challenges in any work on legacy code is that, over time,
layers upon layers of application logic have been added, and it isn’t
always easy to tease out the functionality that is actually being used.
As the manager at a modernization vendor said of a client’s project,
“After looking through all of the code running on the mainframe, we
discovered that around 40% of it was unused…and about 10% of it
nobody knew what it was supposed to do.”

Testing is another stumbling block encountered by Industry Average
and Laggard organizations. Trying to apply old test methodology to
new architectures such as SOA and web services will quickly result in
friction in the lifecycle process. Best In Class companies are about
twice as likely as others to have clearly defined testing processes in
place.

Figure 5: Best in Class place an emphasis on process


                                                                   46%

      Integration testing
                                                     33%
    processes are in place
                                                                                   61%




                                                                   45%
                                                                                                           LAG
  Integration processes are
                                                             41%                                           AVG
            defined
                                                                                                           BIC
                                                                                       62%




                                                                           54%

     Legacy interfaces are
                                                                   46%
         documented
                                                                                               70%




                              0%   10%   20%   30%         40%       50%         60%         70%     80%


                                                                 Source: Aberdeen Group, June 2007




© 2007 Aberdeen Group, Inc.                                                                                      Telephone: 617 723 7890
www.aberdeen.com                                                                                                                 041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 15



Organization
Organizational maturity is reflected in how well IT interfaces with
other departments in the company. This is especially important in the
area of legacy modernization: IT is touching what is likely a key piece
of the business. Service-level agreements (SLAs) are a way to make
certain that both IT and the business agree on what will be delivered
as part of the modernization effort, and how it will perform. Best In
Class companies are using this tool by a margin of two to one over
Laggards, and 50% more often than the Industry Average (Figure 5).


Figure 6: Agreement among departments drives success




                                                  30%


  SLAs for legacy interfaces
                                                              43%
           in place


                                                                                 63%



                                                                                             LAG
                                                                                             AVG
                                                                                             BIC



                                                           41%



 Business and IT are aligned                                         49%



                                                                             60%




                               0%   10%   20%   30%     40%         50%    60%         70%



                                                        Source: Aberdeen Group, June 2007




© 2007 Aberdeen Group, Inc.                                                                        Telephone: 617 723 7890
www.aberdeen.com                                                                                                   041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 16



Knowledge
Both SOA and web services application development pose unique
challenges to the skills of the department, and adding legacy languages
and databases to the mix further complicates the issue.

Best In Class organizations are well along in their training efforts, with
both Laggard and Industry Average following by six months. Where
the knowledge resides is vastly different. Best In Class companies are
drastically reducing their spending levels on outsourcing and
professional services, while no such reduction was reported for the
other two groups (Figure 6).

Figure 7: Training of developers, analysts, and architects


                                                          35%
    Developers, analysts,
    architects trained now
                                                                         51%




                                                                               55%
         Planning to train
                                                                   46%


                                                                                                     Others
                                                                                                     BIC

                                  7%
  Decrease in spending on
        outsourcing
                                                                   46%




                                              24%
  Decrease in spending on
   professional services
                                                                                         71%




                             0%   10%   20%         30%     40%      50%         60%   70%     80%


                                                                  Source: Aberdeen Group, June 2007




© 2007 Aberdeen Group, Inc.                                                                                   Telephone: 617 723 7890
www.aberdeen.com                                                                                                              041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 17



Technology

Best In Class organizations are relying on automation to assist them
in extracting both business logic (61%) and data structures (38%,
double the rate of Laggard and Industry average) as they bring their
legacy applications into line with their SOA and web services
architecture. This is reflected in the high percentage of Best In Class
having documented their legacy interfaces; one of the byproducts of
extraction tools is a complete specification of the underlying code or
data.

Alongside their modernization efforts, Best In Class are continuing to
invest in SOA infrastructure. Twice as many Best In Class
companies are deploying SOA service layers on the mainframe, with
48% indicating that spending on SOA platforms is their number one
or two funding priority over the next 12 months.

One of the challenges of SOA applications is in testing them. The QA
environment is quite a bit different than that for traditional
applications. Across the board, all groups indicate that deploying new
testing methodologies is a high priority in the next twelve months.


Figure 8: Technical approaches to legacy modernization


     Third party adapters for                                  32%
     SOA and web services                                                  43%




    Middleware platforms for                             27%
          re-hosting                                                             46%




   SOA/Web services on the                 13%
        mainframe                                              32%
                                                                                                          Others
                                                                                                          BIC

      Automated tools for                         19%
    extracting business logic                                        38%




  IDEs geared toward legacy                        20%
          systems                                                                       56%




   Data extraction/migration                                               42%
             tools                                                                            61%


                                0%   10%         20%     30%         40%          50%    60%        70%


                                                                     Source: Aberdeen Group, June 2007




© 2007 Aberdeen Group, Inc.                                                                                        Telephone: 617 723 7890
www.aberdeen.com                                                                                                                   041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 18


                         Aberdeen Insights – Technology
Best In Class companies understand that legacy applications can be especially
challenging to bring into line with more modern architectures. They are using
automation to speed up the design and development cycle and fully document
packages and data structures, and are leveraging third-party adapters for commercial
applications.
Legacy specific development environments are also a key to peak performance, with
Best In Class organizations using them at double the rate of other groups. These
IDEs make it easier for developers to focus on the business logic of the application
rather than the mechanics of developing on the legacy platform.




© 2007 Aberdeen Group, Inc.                                                            Telephone: 617 723 7890
www.aberdeen.com                                                                                       041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 19




Performance
Overall, Best In Class organizations reported decreases in costs for
development, maintenance, and infrastructure (Figure 8). Productivity
of mainframe developers was improved by use of specialized IDEs and
third-party adapters that expose legacy data and packages. This
emphasis on productivity is reflected by the Best In Class’ emphasis
on in-house application development, 57% versus 28% of the Industry
Average.

Figure 9: Best In Class see improvements in costs and
productivity

   Legacy capital costs:                                  27%
        Increased                7%


                                                   20%
         Decreased                                                          44%




   Maintenance costs:                               21%
        Increased                      12%
                                                                                                          Others
                                                                                                          BIC
                                                                30%
         Decreased                                                                            61%




  Developer productivity:              12%
        Increased                                                     38%


                                             17%
         Decreased                     12%


                            0%   10%         20%          30%         40%         50%   60%         70%


                                                                      Source: Aberdeen Group, June 2007




© 2007 Aberdeen Group, Inc.                                                                                        Telephone: 617 723 7890
www.aberdeen.com                                                                                                                   041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 20



                           Chapter Three:
                          Required Actions
Based on the information in Chapters One and Two, readers should
determine whether their organizations fall into the “Laggard”, “Industry
Average,” or “Best in Class” categories. The key to gaining value from this
report is moving your organization along the maturity path to Best in Class.
The following actions will help spur necessary performance improvements:

Laggard Steps to Success
    •    Automate. Use automated extraction tools to pull apart your
         legacy applications. They will provide clean interfaces to the
         underlying code, and will let you see what is really going on in each
         package.
    •    Understand what you are delivering. Best In Class
         organizations know that service level agreements are not just for
         B2B relationships. Use SLAs to provide a basis for measuring the
         performance of individual services. The SLA lets you focus on those
         components that need the most attention.
    •    Use adapters. Third-party adapters, especially for commercial
         vertical applications, will save both time and money in your
         modernization efforts. Best In Class companies use adapters for
         commodity packages, and focus their efforts on the custom parts of
         the application.

Industry Norm Steps to Success
    •    Document the interfaces. Spend the time to thoroughly
         document the packages and data structures of your legacy
         applications. Whether you opt for rehosting or extending, this step
         will pay off in
    •    Don’t focus just on cost. Getting code off of the mainframe will
         almost certainly save money in the short term. Best In Class
         organizations, however, understand that cost is not the only
         component of a successful architecture. Look to agility as a key
         driver for your modernization efforts.
    •    Switch      development       tools.     Integrated    development
         environments that are designed for legacy systems will dramatically
         improve the productivity of your application developers. Forty
         percent of Best In Class report an increase in productivity, and 56%
         say that they use legacy IDEs, versus 12% of Industry Average
         reporting improvement, and 35% using IDEs.




© 2007 Aberdeen Group, Inc.                                                      Telephone: 617 723 7890
www.aberdeen.com                                                                                 041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 21



Best in Class Steps to Success
    •    Continue to look at governance. Both run-time and design-time
         governance help unlock the promise of SOA. Without governance,
         SOA environments quickly devolve into a morass of functionally
         similar objects with multiple, possibly incompatible, versions.
         Change control is critical in a fully evolved SOA environment. Just
         under half of Best In Class organizations cite governance as their
         top concern.
    •    Re-tool QA and test processes. Functional testing isn’t enough
         for SOA applications; integration testing is an absolute requirement.
         Forward-thinking IT organizations are starting to reshape their
         thinking around QA to encompass the complexity of SOA, and
         realize that integration testing must be built into the design of new
         services.
    •    Focus on performance. As SOA deployments become more
         complex, bottlenecks will start to develop. Scalability and
         performance of SOA applications are complicated by the black-box
         approach to SOA components. Investing in performance
         methodologies now will pay off in improvements in SLAs and
         throughput later.


                          Aberdeen Insights – Summary
SOA and web services architectures can be complex, and the addition of legacy
application and processes can further complicate the issue. While it may seem
overwhelming, Best In Class organizations use process and technology to succeed.
Automated extraction tools and defined interfaces let them understand the application
landscape and focus on the key components of their legacy packages. SLAs help
them manage the services created from the legacy packages.
What is perfectly clear is that mainframes, COBOL, and decades-old code are not
going away. The core business processes encapsulated in that 25-year-old code are
being given new life in high-performance message-based architectures.




© 2007 Aberdeen Group, Inc.                                                             Telephone: 617 723 7890
www.aberdeen.com                                                                                        041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 22



                     Featured Underwriters
This research report was made possible, in part, with the financial support
of our under-writers. These individuals and organizations share Aberdeen’s
vision of bringing fact based research to corporations worldwide at little or
no cost. Underwriters have no editorial or research rights and the facts and
analysis of this report remain an exclusive production and product of
Aberdeen Group.




                                 Service Oriented Architecture (SOA) is an
architectural style that supports integrating your business as linked services
or repeatable business tasks and the outcomes they bring. SOA builds upon
existing IT investments to facilitate unprecedented business flexibility to
respond quickly and economically to fast-changing opportunities and threats.
SOA is best approached via a roadmap of incremental, incremental projects.
IBM is the recognized leader in SOA with expertise in aligning business and
IT processes, a thriving ecosystem of SOA business partners, thousands of
worldwide industry-specific SOA engagements, unmatched breadth and
depth of products, and a complete portfolio of professional services for
SOA. More information at www.ibm.com/soa.




                                            INFINITE Software Migrates
and Modernizes IBM Mainframe and iSeries applications using sophisticated
software and time-tested services. Our solution recompiles Legacy source
into native executables on Linux, UNIX or Windows. Data can be written
directly to Oracle or SQL Server. The migrated code runs on the newly
hosted server as it did before, but is now web-enabled, graphical and easily
integrated with other object-oriented applications in the enterprise. BI tools
are built-in to modernize reporting capabilities. Our methodology means
the project is fast, efficient and virtually risk free. Please visit
www.infinitesoftware.com.




                                     Micro Focus, a member of the FTSE
250, provides innovative software that allows companies to dramatically
improve the business value of their enterprise applications. Micro Focus
Enterprise Application Modernization and Management software enables
customers' business applications to respond rapidly to market changes and
embrace modern architectures with reduced cost and risk. For additional
information please visit www.microfocus.com.
© 2007 Aberdeen Group, Inc.                                                      Telephone: 617 723 7890
www.aberdeen.com                                                                                 041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 23




                                        Relativity Technologies is the
leading provider of Enterprise Application Modernization and Application
Portfolio Management solutions. Over 325 organizations—including seven
of the ten largest financial services providers—have relied on our software
platform to increase the efficiency and flexibility of the applications that
automate their core business operations. The Modernization Workbench®
delivers this value by enabling organizations to understand, manage,
modernize, and maintain applications throughout the enterprise. For more
information, please visit www.relativity.com.




© 2007 Aberdeen Group, Inc.                                                    Telephone: 617 723 7890
www.aberdeen.com                                                                               041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 24



                         Appendix A:
                     Research Methodology

Between April and May 2007, Aberdeen Group examined the responses of
more than 300 companies across a variety of geographies, industries and
company revenues.
Aberdeen supplemented this online survey effort with telephone interviews
with select survey respondents, gathering additional information on legacy
modernization strategies, experiences, and results.
The study aimed to identify emerging best practices for legacy application
modernization projects, and provide a framework by which readers could
assess their own organization’s capabilities and maturity.
Responding enterprises included the following:
    •    Job title/function: About two-thirds of the survey respondents are
         in their organizations’ IT departments. The research sample
         included respondents with the following job titles: senior executive
         (CEO, COO, CFO, VP) (20%); CIO (7%); IT manager or director
         (42%); internal consultant (15%), and IT staff (13%).
    •    Industry: The research sample included respondents predominantly
         from high-technology industries and companies. These represented
         27% of the sample. A significant number of respondents were in the
         insurance industries (11%), and finance and banking (17%).
    •    Geography: The survey respondents were distributed: North
         America (U.S., Canada, Mexico) 62%; Central and South America
         2%; Asia/Pacific 16%; Europe, Middle East, and Africa 20%.
    •    Company size: About 25% of respondents were from large
         enterprises (annual revenues above US$1 billion, including 14% over
         US$5 billion); 35% were from midsize enterprises (annual revenues
         between $50 million and $1 billion); and 40% of respondents were
         from small businesses (annual revenues of $50 million or less).
Solution providers recognized as sponsors of this report were solicited after
the fact and had no substantive influence on the direction of the report.
Their sponsorship has made it possible for Aberdeen Group to make these
findings available to readers at no charge.




© 2007 Aberdeen Group, Inc.                                                     Telephone: 617 723 7890
www.aberdeen.com                                                                                041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 25



Table 4: PACE Framework

PACE Key

Aberdeen applies a methodology to benchmark research that evaluates the business
pressures, actions, capabilities, and enablers (PACE) that indicate corporate behavior in
specific business processes. These terms are defined as follows:
Pressures — external forces that impact an organization’s market position, competitiveness,
or business operations (e.g., economic, political and regulatory, technology, changing
customer preferences, competitive)
Actions — the strategic approaches that an organization takes in response to industry
pressures (e.g., align the corporate business model to leverage industry opportunities, such
as product/service strategy, target markets, financial strategy, go-to-market, and sales
strategy)
Capabilities — the business process competencies required to execute corporate strategy
(e.g., skilled people, brand, market positioning, viable products/services, ecosystem
partners, financing)
Enablers — the key functionality of technology solutions required to support the
organization’s enabling business practices (e.g., development platform, applications,
network connectivity, user interface, training and support, partner interfaces, data cleansing,
and management)

                                                         Source: Aberdeen Group, June 2007

Table 5: Maturity Framework

Maturity Framework Key

The Aberdeen Maturity Framework defines enterprises as falling into one of the following
three levels of practices and performance:
Best in class (20%) — Application development practices that are the best currently being
employed and significantly superior to the industry norm, and result in the top industry
performance.
Industry norm (50%) — Application development practices that represent the average or
norm, and result in average industry performance.
Laggards (30%) — Application development practices that are significantly behind the
average of the industry, and result in below average performance
In the following categories:
Process — What is the scope of process standardization? What is the efficiency and
effectiveness of this process?
Organization — How is your company currently organized to manage and optimize this
particular process?
Knowledge — What visibility do you have into key data and intelligence required to manage
this process?
Technology — What level of automation have you used to support this process? How is this
automation integrated and aligned?
Performance — What do you measure? How frequently? What’s your actual performance?

© 2007 Aberdeen Group, Inc.                                                                       Telephone: 617 723 7890
www.aberdeen.com                                                                                                  041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 26


                                                     Source: Aberdeen Group, June 2007

Table 6: Relationship between PACE and Competitive
Framework

PACE and Competitive Framework How They Interact
Aberdeen research indicates that companies that identify the most impactful pressures and
take the most transformational and effective actions are most likely to achieve superior
performance. The level of competitive performance that a company achieves is strongly
determined by the PACE choices that they make and how well they execute.

                                                     Source: Aberdeen Group, June 2007




© 2007 Aberdeen Group, Inc.                                                                 Telephone: 617 723 7890
www.aberdeen.com                                                                                            041207a
Modernizing Legacy Applications:
Maximizing the Investment
Page 27



                              Appendix B:
                       Related Aberdeen Research
Related Aberdeen research that forms a companion or reference to this
report include:
      •     Service-Oriented Architectures (October 2005)
      •     The SOA in IT Benchmark Report (December 2005)
      •     The Legacy Application Migration Benchmark Report (September
            2006)
      •     The Composite Applications Benchmark Report (December 2006)
      •     Management and Governance: Planning for an Optimized SOA
            Application Lifecycle (March 2006)
      •     SOA Middleware Starts Where Web Services Leave Off (June 2007)
Information on these and any other Aberdeen publications can be found at
www.Aberdeen.com.


                    Author: Perry Donham, Director, Enterprise Integration Research
                                    (perry.donham@aberdeen.com)

Founded in 1988, Aberdeen Group is the technology- driven research destination of choice for the global business
executive. Aberdeen Group has over 100,000 research members in over 36 countries around the world that both
participate in and direct the most comprehensive technology-driven value chain research in the market. Through its
continued fact-based research, benchmarking, and actionable analysis, Aberdeen Group offers global business and
technology executives a unique mix of actionable research, KPIs, tools, and services.
This document is the result of research performed by Aberdeen Group. Aberdeen Group believes its findings are
objective and represent the best analysis available at the time of publication. Unless otherwise noted, the entire
contents of this publication are copyrighted by Aberdeen Group, Inc. and may not be reproduced, stored in a retrieval
system, or transmitted in any form or by any means without prior written consent by Aberdeen Group, Inc.




© 2007 Aberdeen Group, Inc.                                                                                             Telephone: 617 723 7890
www.aberdeen.com                                                                                                                        041207a


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | ra-soa-2007-97c147 |
| title | SOA and Web Services Testing: How Different Can It Be? (Full Unabridged Version) |
| author | Aberdeen Group (Perry Donham) |
| date | 2007-08 |
| type | employer-record |
| subject_domain | SOA/Web Services Quality Assurance and Testing |
| methodology | Survey-based benchmark (N~240-250); Aberdeen Maturity Class Framework; online survey July-August 2007 supplemented by telephone interviews |
| source_file | source/_raw_text.txt |
| license | CC-BY-4.0 |

### Abstract

Full 180pp unabridged version of the SOA/Web Services testing benchmark report. Study of 240 end-users involved in software quality. Best-in-Class (BIC) companies show 94% increase in deployed software quality, 61% reduction in defects, 57% faster repair times, 71% increase in code test coverage. Key finding: automation alone is insufficient — BIC companies test horizontally across entire business processes, not just vertically via unit testing. BIC companies 3x more likely to have redesigned their testing process. 45% of BIC use business requirements tracking tools vs 35% for others. File also contains appended Aberdeen reports: Enterprise Information Integration (July 2003), BPM Matching IT to Business Processes (Dec 2006), SOA Middleware Takes the Lead (July 2007), and Modernizing Legacy Applications (June 2007).

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Landmark testing benchmark for SOA era; full unabridged version with vendor data, extended survey appendices, and case studies not in abridged version. Core contribution to understanding SOA QA maturity. |
| **Relevance** | medium | Directly addresses the central challenge of SOA adoption era — how to ensure quality in composite/assembled applications vs. monolithic software. |
| **Prescience** | medium | Predicted the shift from vertical unit testing to horizontal end-to-end business process testing; anticipates DevOps-style continuous quality and governance-driven reuse patterns. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (6)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | [DEFERRED] | [DEFERRED] |
| Perry Donham | person | active |  |
| iTKO Inc. | company | [DEFERRED] | [DEFERRED] |
| Mindreef Inc. | company | [DEFERRED] | [DEFERRED] |
| Solstice Software | company | [DEFERRED] | [DEFERRED] |
| iSOFT Group | company | [DEFERRED] | [DEFERRED] |

### Technologies Referenced (11)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| SOA and Web Services Testing | framework |  | emerging | mature |
| iTKO LISA SOA Test Framework | testing-tool | iTKO | growth | legacy |
| Mindreef SOAPscope | testing-tool | Mindreef | growth | legacy |
| Solstice Integra Suite | testing-tool | Solstice Software | growth | legacy |
| Design-Time Governance | framework |  | emerging | mature |
| Requirements Tracking Software | tool |  | growth | mature |
| Defect Tracking and Reporting Applications | tool |  | growth | mature |
| Production Monitoring and Reporting Tools | tool |  | growth | mature |
| Automated Orchestration and Integration Testing Tools | testing-tool |  | emerging | mature |
| Regression Testing | methodology |  | growth | mature |
| Automated Functional Testing for SOA/Web Services | testing-tool |  | growth | mature |

### Observation Summary

- Total observations: 100
- By type: survey-statistic: 77, kpi: 12, methodology: 7, vendor-profile: 2, business-finding: 1, case-study: 1
