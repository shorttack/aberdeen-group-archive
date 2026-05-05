# SOA and Web Services Testing: How Different Can It Be?

> Archived from: source/_raw_text.txt
> Original publication date: 2007-08
> Author: Aberdeen Group

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
development lifecycle, and view quality not as something that’s done at the
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
         into new applications. If a developer doesn’t know about a service,
         he or she can’t use it. Move toward an institutional awareness of
         governance by deploying tools and policies that foster re-use.
    •    Improve visibility of deployed services. Best-in-Class
         organizations are using monitoring and reporting tools on their
         production systems to give them a better understanding of what is
         going wrong – and also going right – in their deployed software.




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
Figure 3: Changes to Key QA Processes ................................................................ 8
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
“SOA and web service applications are un-testable,” was the comment              √ 94% of Best-in-Class
heard recently during a discussion of new methods for testing composite            organizations report an
applications. This new breed of software certainly poses unique challenges,        increase in the quality of
especially to organizations which are slow to move away from traditional           deployed services
ways of testing monolithic applications. A fundamental shift in viewpoint is     √ 61% of Best-in-Class
taking place at this time – the shift is moving away from old-style monolithic     companies saw a reduction in
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
problem from multiple angles. It isn’t enough to just deploy automation, and
it isn’t enough to simply rely on functional tests – QA for composite
applications needs a horizontal, process-oriented view, not the
vertical unit-test methods used in the past (Figure 1). A director in
the high-tech consulting field put it this way: “The tool-centric approach to
SOA QA burned us. We had to train on the test process first before we
became successful.”
The typical Best-in-Class company:
    •     Gets business users involved in all aspects of quality
    •     Uses automation to increase test coverage
    •     Sees quality as more than just an end-of-the-lifecycle task

Figure 1: Best-in-Class Keys to Success for Quality

                                                                                           “QA has become a much
            Business users               26%                    Best-in-Class
                                                                All Others
                                                                                           more continuous process
               involved                19%                                                 rather than a ‘phase’ in the
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
Reducing the number of defects is important, but it isn’t the top reason that
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
“Traditionally we rolled out functions and features as part of a software
application. Now with web services defined as standalone and atomic
services we have to be more thorough in our understanding of business
requirements. This allows us to translate those business requirements into
specific unit web services as well as to test for various scenarios that cater
for most (if not all) of our users both internally and externally,” said a senior
manager in the retail sector,

The Best-in-Class PACE Model
Aberdeen uses the PACE model to profile the top performing 20% of
companies – the Best-in-Class – in four areas:
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

         Aberdeen Insights – What is Happening to QA?
As the emphasis shifts from IT to business as the driver for technology
change, the QA team is being asked to provide more than just functional
testing. A functional test won’t reveal how a new service interacts in an
end-to-end business process. Even updating a single service carries risk and
may require modeling to determine its impact. One company we spoke
with does not complete incremental updates to deployed services – every
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
In the words of an IT manager who has been there, “Our initial experience
has been tedious in defining the new processes for testing SOA and web
services, with a higher learning curve for testers, however, the effort now
has started paying off.”




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
 “QA at iSOFT has changed to implement an end-to-end view of testing and          the project lifecycle, not just
 quality,” according to Phil Davies, Director of the LORENZO product unit         in testing
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
 “It introduced other challenges. At first we learned more about the
 necessary process changes we needed,” said Davies. “Now we have
 enough instrumentation in the process to understand quantitative quality
 measurement, track metrics, and view improvement.”
 Davies sees quality as a continuous process, where improvements are
 being incrementally made cycle-by-cycle. “This isn’t our end state; there is
 always room for improvement. For example, we need to increase the
 amount of tooling and automation that we use, as well as shorten the
 feedback time so that we can implement improvements faster.”


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
emphasis on the business view of testing. This is consistent with Aberdeen’s
observation from previous reports that there has been a fundamental shift
of emphasis away from IT as a principle driver of functionality, toward the
business user. IT’s response to this shift has been to move toward SOA and
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
emphasize that quality is not just unit and functional testing – quality in a
mature organization encompasses the end-to-end assembled business
process, not simply individual services.
Interestingly, when asked if organizations test SOA and web services
components outside of the company, 40% of all respondents (although only
32% of Best-in-Class) said that they did. Incorporating an external service
into the test plan adds complexity and risk; a trend that we will watch
closely over the next several months.

Knowledge
Training in SOA and web services technologies is an area in which Best-in-
Class companies show a significant advantage (Figure 8). This isn’t just about
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

                      Aberdeen Insights – Technology

Automation is not an option when testing the complex interactions among
deployed services that are part of an end-to-end transaction. Even if a single
service passes unit and functional tests, the view of the quality of that service
is different depending on the individual’s role in the company. A service that
has aced its functional tests may receive a thumbs-up from the development
and QA team and still fail miserably from the business user’s perspective.
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
the entire development lifecycle – from the definition of business
requirements to deployment and maintenance (Figure 10).


© 2007 Aberdeen Group, Inc.                                                                        Telephone: 617 723 7890
www.aberdeen.com                                                                                                   041207a
SOA and Web Services Testing:
How Different Can It Be?
Page 17


“Functionality was the main objective earlier. Now, the focus is more on
how the service is exposed, invoked, its interoperability, how it is
orchestrated and governed, and managing change. Assembly of services with
the right version also needs to be tested. So it is now not only functionality,
but a host of non-functional and technical features that needs to be tested.
Testing of SOA and web services requires a different mindset,” said a vice
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
determine whether their organizations fall into the “Laggard,” “Industry
Average,” or “Best-in-Class” category. The key to gaining value from this
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
         services and test the services’ interoperability across the entire
         business process. Best-in-Class organizations track both business
         requirements and quality across the enterprise, not on a service-by-
         service basis. Use tools that provide end-to-end testing in addition
         to functional or interface tests.
    •    Apply design-time governance. SOA and web services provide
         a library of tested, documented components that can be assembled
         into new applications – but if a developer doesn’t know about a
         service, he or she can’t use it. Move toward an institutional
         awareness of governance by deploying tools and policies that foster
         re-use.
    •    Improve visibility of deployed services. Best-in-Class
         organizations are using monitoring and reporting tools on their
         production systems to give them a better understanding of what is
         going wrong – and what is also going right – in their applications.



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
         becoming more critical. Don’t ignore measurement of business
         process SLAs – in the end they will be the key indicator of a healthy
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
framework by which readers could assess their own organization’s
capabilities and maturity.
Responding enterprises included the following:
    •    Job title/function: About two-thirds of the survey respondents are
         in their organizations’ IT departments. The research sample
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
our underwriters. These organizations share Aberdeen’s vision of bringing
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
Software’s flagship product, Solstice Integra Suite, uniquely addresses the
testing challenges presented by today’s complex, full scale integration and
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


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | soa-web-services-2007-c3297b |
| title | SOA and Web Services Testing: How Different Can It Be? |
| author | Aberdeen Group |
| date | 2007-08 |
| type | employer-record |
| subject_domain | SOA testing; web services QA; software quality assurance |
| methodology | survey; benchmark; n=240 end-users; qualitative interviews |
| source_file | source/_raw_text.txt |
| license | CC-BY-4.0 |

### Abstract

26-page Aberdeen Group benchmark report examining testing and quality assurance challenges for SOA and web services deployments. Unit and functional testing insufficient; integration, regression, business process, performance, and security testing all required. Survey of 240 end-users categorizes companies into Best-in-Class (top 20%), Industry Average (middle 50%), and Laggard (bottom 30%) using Aberdeen Competitive Framework and PACE model. Best-in-Class companies redesigned QA processes, use automated testing, involve business users throughout lifecycle, and track quality across entire project—not just at end.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Captures 2007 state of SOA/web services testing practices with concrete survey data; documents transition from monolithic to composite application testing methodology |
| **Relevance** | high | Directly addresses SOA QA maturity gap with quantitative benchmarks across three company tiers; useful for understanding adoption patterns |
| **Prescience** | high | Correctly anticipated that business user involvement in QA and automated orchestration testing would become standard practice; shift toward continuous QA now universal in DevOps |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (2)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | [DEFERRED] | [DEFERRED] |
| iSOFT Group | company | [DEFERRED] | [DEFERRED] |

### Technologies Referenced (6)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| SOA/Web Services Testing | testing-methodology |  | emerging | evolved |
| Automated Testing Tools (SOA) | testing-tools |  | growth | mature |
| Requirements Tracking Software | testing-tools |  | growth | mature |
| Design-Time Governance | governance |  | emerging | mature |
| Production Monitoring and Reporting Tools | operations |  | growth | mature |
| Service Oriented Architecture / Web Services | architecture |  | growth | evolved |

### Observation Summary

- Total observations: 26
- By type: survey-finding: 22, strategic-recommendation: 2, technical-claim: 1, benchmark: 1
