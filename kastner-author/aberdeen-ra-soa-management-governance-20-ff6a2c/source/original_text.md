# Management and Governance: Planning for an Optimized SOA Application Lifecycle

> Archived from: RA_SOAGov_3944_PKRS_040307a-8.pdf
> Original publication date: 2007-03-01
> Author: Peter S. Kastner and Rick Saia (Aberdeen Group)

---

## Original Document Text

SOURCE: RA_SOAGov_3944_PKRS_040307a-8.pdf

Management and Governance: Planning for an 
Optimized SOA Application Lifecycle 
 
Technology That Drives Lower  
Software Development and Lifecycle Costs 
 
 
 
 
March 2007 
 
— Underwritten, in Part, by — 
 
 
 
 
 
 
 
 
 

Management and Governance: Planning for an Optimized SOA Application Lifecycle 
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
Aberdeen Group • i 
Executive Summary 
This report examines the effectiveness of IT investments in three areas of a services-
oriented architecture (SOA): operations management; design and operations governance; 
and underlying changes in project management, development, testing, and application 
lifecycle management tools. 
Key Business Value Findings 
Between a third and half of the 950 companies we surveyed in 2006 are having serious 
difficulties getting their SOA-enabled applications into stable deployment. The survey 
for this report shows that the predominant reason for these difficulties is inexperience 
exacerbated by inadequate tools for the automated management and governance of the 
growing plethora and complexity of web services and applications under an SOA. 
There are four characteristics of the top-performing 20% of the companies — the Best in 
Class — in our survey: 
• 
The Best in Class are most likely (33%) to have more than two years experi-
ence with SOA technology; 
• 
68% of the Best in Class are achieving positive ROI on their SOA investments 
and are seeing lower application development costs under SOA, while 77% of 
the overall survey has yet to see an SOA payback achieved; 
• 
The Best in Class companies have implemented design-time governance and 
re-use policy to minimize lifecycle service costs compared to 26% overall. 
Close to half of the Best in Class have set minimizing application software 
lifecycle costs as a measurable management objective. 
• 
More than 80% of the Best in Class have implemented an automated solution 
to SOA operations and governance, typically with third-party software. 
Implications & Analysis 
There is a tangible cause and effect relationship between management and governance 
and overall software lifecycle costs:  
• 
Operationally, SOA introduces a myriad of new design, testing and performance-
related issues that can not readily be solved with prior technology or IT elbow 
grease;  
• 
Design-time governance is where programmers can be “encouraged” to re-use 
existing services, saving the initial coding time and long-term maintenance costs 
of writing new but duplicative program code;  
• 
Operational governance ensures that eligible services are given the resources 
they need, and that performance and security issues are managed. It also helps 
manage the complexity of loosely-coupled services running on multiple servers 
in a highly distributed fashion — the hallmark of a SOA. 

Management and Governance: Planning for an Optimized SOA Application Lifecycle 
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
ii • Aberdeen Group 
The inefficiencies caused by a lack of SOA management and governance lower IT per-
formance, raise current operating costs, and collar IT with long-term software mainte-
nance costs that will endure for decades. Fortunately, none of our survey participants 
will ignore investments in SOA management and governance. The Best in Class have 
it now and the Industry Average company is in the planning stage. 
Recommendations for Action  
Our extensive research in 2006 and for this report paint a clear approach to achieving 
superior results: 
• 
Experience Counts. Organizations that are dawdling with web services and with 
no firm enterprise plan for an SOA (and the technology investments that re-
quires) are falling behind their peers. Get the focused training necessary to bring 
not just specialists but the whole IT organization up to snuff, using outside ser-
vices where appropriate. SOA is not a fad. It will be with us for decades. 
• 
Design in SOA Management and Governance. Manageability of loosely-
coupled services, re-use policies, and security are all most economically designed 
in rather than bolted on after the fact. Technology for automating management 
and governance is proving its worth at Best in Class companies. 
• 
Focus on Application Lifecycle Costs. A systematic focus on the costs of de-
veloping and maintaining SOA services, which can be assisted with automation, 
will result in the appropriate methodologies and policies such as code re-use that 
drive lower costs of ownership. Without design-time governance, programmers 
will not re-use services, and lifecycle costs will balloon. The Best in Class com-
panies who are already using automated SOA management and governance are 
encouraged to take the next step in operational excellence by concentrating on 
processes to minimize costs across the application lifecycle. One area they 
should focus on is quality, which is a major aim of the SOA application lifecycle. 
 
 
 
 
 

Management and Governance: Planning for an Optimized SOA Application Lifecycle 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
Aberdeen Group  
 
Table of Contents 
 
Executive Summary ..............................................................................................i 
Key Business Value Findings................................................................................i 
Implications & Analysis..........................................................................................i 
Recommendations for Action ............................................................................... ii 
Chapter One: Issue at Hand.................................................................................1 
The Components of an SOA Life-Cycle Management Model...............................2 
Operational Management ..............................................................................3 
Governance...................................................................................................4 
Project Management, Development and  
Application Lifecycle Management Tools.......................................................4 
The Drivers for SOA Management and Control .............................................5 
Chapter Two: Key Business Value Findings.........................................................6 
Experience Counts ........................................................................................6 
IT Drivers for SOA Management and Governance ........................................6 
SOA Operations Challenges and Responses................................................7 
Chapter Three: Implications & Analysis................................................................9 
Process and Organization ...........................................................................10 
Technology Provides Leverage to the Best-in-Class Companies.................10 
Pressures, Actions, Capabilities, Enablers (PACE)...................................... 11 
Governance Views by Industry.................................................................... 11 
Chapter Four: Recommendations for Action ......................................................13 
Best in Class Next Steps .............................................................................13 
Industry Average Steps to Success .............................................................14 
Laggard Steps to Success...........................................................................14 
Featured Underwriters .......................................................................................16 
Appendix A: Research Methodology ..................................................................18 
 

               Management and Governance: Planning for an Optimized SOA Application Lifecycle 
 
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
Aberdeen Group 
 
Figures 
Figure 1: SOA Application Integration Life-Cycle Stumbling Blocks .....................2 
Figure 2: Business Drivers for Investments in  
SOA Management and Governance ....................................................................5 
Figure 3: Length of Time Since First SOA Services Were Deployed....................7 
Figure 4: IT Drivers for SOA Management and Governance................................8 
Figure 5: SOA Governance Drivers by Industry .................................................12 
 
Tables 
Table 1: SOA Operations Challenges and Responses .........................................8 
Table 2: SOA Operations and Governance Competitive Framework....................9 
Table 3: Application Lifecycle Cost Changes by Maturity Framework – 2006.....10 
Table 4: Prioritized Pressures and Enablers....................................................... 11 
Table 5: PACE Framework .................................................................................19 
Table 6: Relationship between PACE and Competitive Framework ...................19 
 

Management and Governance: Planning for an Optimized SOA Application Lifecycle  
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
Aberdeen Group • 1 
Chapter One: 
Issue at Hand 
Key Takeaways 
• A strong focus on management and governance is a key to wringing the most savings 
out of SOA projects that use core middleware or extend from existing ERP systems. 
• The top stumbling blocks to SOA implementation and operation center around operations 
management and governance issues. 
• The key to application lifecycle cost control is governance, especially in driving service 
re-use at design time. 
 
berdeen research in 2006 watched the 90% of Global 10,000 organizations that 
have embarked on SOA journeys. The vast majority of IT executives and other 
senior executives are convinced that a service-oriented architecture (SOA) is the 
right technology path to improve IT agility and lower the 40% of IT budget 
dedicated to application integration. We can all salute that flag. 
The problem is that each organization’s “SOA journey” takes a different path. We have 
identified three major classifications to describe SOA strate-
gies: 
• 
SOA Lite, for the half that are calling web services 
“SOA”; 
• 
Enterprise SOA, for the 30% that are building 
around core SOA infrastructure middleware; and 
• 
ERP SOA, for the 20% that are building their 
SOAs from their ERP vendors’ SOA middleware ca-
pabilities. 
Importantly, while SOA may be the solution, it’s not a 
painless cure for the pain of integration. In fact, between a 
third and half of the 950 companies we surveyed in 2006 are 
having serious difficulties getting their SOA-enabled appli-
cations into stable deployment (Figure 1). These problems 
can be lumped into five major categories of yellow-flags for 
IT executives: 
1. Poor operational control of the loosely coupled 
applications, including security; 
2. Inadequate control over programmers: SOA application creation, re-use, 
and modification; 
3. Unanticipated deployment issues regarding performance and scaling, and 
testing issues caused by the new development methodologies inherent in Web 
services and SOA, and simplifying the inherent complexity in SOA; 
Competitive Framework 
Key 
The Aberdeen Competitive 
Framework defines enter-
prises as falling into one of 
the three following levels of 
practices and performance: 
Best in class (20%) —
practices that are the best 
currently being employed 
and significantly superior to 
the industry norm 
 Industry Average (50%) —
practices that represent the 
average or norm 
Laggards (30%) —practices 
that are significantly behind 
the average of the industry 
A 

Management and Governance: Planning for an Optimized SOA Application Lifecycle 
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
2 • AberdeenGroup 
4. Project management methodologies that have not kept up with SOA devel-
opment, testing, and deployment techniques, lowering ROI and raising costs 
due to inadequate application life-cycle management; and 
5. Inadequate ROI or difficulty in justifying the ROI of project expenditures. 
Based on Figure 1 and the 50% of companies that are not deploying SOA infrastructure 
software (i.e., SOA Lite), a significant minority of the Global 10,000 will encounter 
ongoing SOA operational issues and vexing development problems, which, in turn, 
will reduce the potential double-digit savings in application lifecycle costs under 
SOA. 
One key to SOA-based cost reduction is a strong focus on management and governance. 
Figure 1: SOA Application Integration Life-Cycle Stumbling Blocks 
31%
34%
35%
38%
39%
44%
0%
5% 10% 15% 20% 25% 30% 35% 40% 45% 50%
QA: Testing and deployment stage problems spill
over into production
Data management of SOA services is problematic
Debugging problems with complex services,
composites
SLAs: Scaling to production volumes, reliability &
availability
Security issues are different from older IT
Establishment of operational security, governance,
and management
 
Source: Aberdeen Group, January 2007 
The Components of an SOA Life-Cycle Management Model 
There are only bits and pieces of an IT product category called “SOA life-cycle manage-
ment”. That means IT executives will have to develop their own models for how their 
organizations will maximize productivity and minimize total life-cycle costs over the 
decades-long lives of their SOA applications portfolios and infrastructure investments. 
And the key really is to take a decades-long view. Why? Because the Pandora’s Box that 
is intractable software integration costs has been opened, and the industry will never re-
turn to the tightly-coupled, brittle applications and interfaces we have lived with since the 
appearance of client-server and relational databases in the early 1990s. 

Management and Governance: Planning for an Optimized SOA Application Lifecycle  
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
Aberdeen Group • 3 
Not only is there no product category of SOA life-cycle management, there is no single, 
point-product solution either. That means IT 
executives will be cobbling together technol-
ogy over the near term until vendors catch up 
with more integrated product portfolios. 
IT executives can succeed in developing their 
SOA life-cycle management plans by con-
centrating on three areas: 
• 
Operational 
Management 
— 
How does a loosely-coupled SOA 
change the way applications oper-
ate, forcing changes in IT opera-
tions? 
• 
SOA Governance — How does 
an SOA affect application design 
standards, change run-time secu-
rity and compliance, testing, and 
impact the overall IT governance 
framework? 
• 
Project Management, Development and Application Life-Cycle Manage-
ment Tools — What process and technology changes are required to gain the 
maximum long-term productivity improvements from the impact of SOA on 
the application portfolio? 
Operational Management 
Whether or not an organization uses SOA infrastructure middleware such as an ESB, ap-
plications increasingly consist of composites of existing “legacy” applications, held to-
gether with a loosely-coupled IT infrastructure. SOA services have different workload 
characteristics than their predecessors. In addition, they behave differently and require 
new techniques — and likely new technology — to operate efficiently. Key areas of 
change include: 
• 
Integrating an SOA and its applications with existing enterprise systems man-
agement infrastructure to create a services-aware, end-to-end view of business 
processes; 
• 
Development of new procedures for application crash debugging and recov-
ery; 
• 
Testing and development of new capacity planning benchmarks, performance 
tuning, and revised response-time thresholds. SOA requires new testing meth-
odologies and testing technology; 
• 
Integration with first-tier IT help desk and vendors’ second- and third-tier sup-
port; 
• 
Incorporating SOA-specific security into the enterprise IT security plan; 
PACE Key — For more detailed descrip-
tion see Appendix A 
Aberdeen applies a methodology to benchmark 
research that evaluates the business pressures, 
actions, capabilities, and enablers (PACE) that 
indicate corporate behavior in specific business 
processes. These terms are defined as follows: 
Pressures — external forces that impact an 
organization’s market position, competitiveness, 
or business operations 
Actions — the strategic approaches that an 
organization takes in response to industry pres-
sures  
Capabilities — the business process competen-
cies required to execute corporate strategy  
Enablers — the key functionality of technology 
solutions required to support the organization’s 
enabling business practices  

Management and Governance: Planning for an Optimized SOA Application Lifecycle 
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
4 • AberdeenGroup 
• 
Development of service-aware Quality of Service requirements; and 
• 
Changes to service-level agreements to reflect these operational changes. 
Governance 
Governance in an SOA world implies a decision and accountability framework with 
strong auditing, conformance, and measurement capabilities that support compliance 
management. Organizations are applying governance throughout the application lifecy-
cle, especially during design and operations stages. Governance is meant to reduce risk 
and complexity around the common challenges associated with adopting SOA especially 
defining and reusing services, managing the lifecycle of service assets, and the measuring 
effectiveness of policies. 
At design time, governance can guide decisions on service re-use. The simple equation 
going forward is that more re-use will result in lower integration costs and the mainte-
nance costs that follow. Our survey for this report shows that about one-quarter of 
Global 10,000 organizations are employing design-time governance.  
During service operation, governance software supports the creation and modification of 
policies that trigger events and actions. It also controls and monitors service use by em-
ployees, customers, and business suppliers, as well as across business units. SOA opera-
tional issues become obvious as volumes scale, and especially when multiple applica-
tion service servers are required to support the workloads. 
Project Management, Development and 
Application Lifecycle Management Tools 
The SOA application development and maintenance lifecycle is different from prior soft-
ware lifecycles, even though organizations use the same phases of design, coding, test-
ing, quality assurance, and deployment. To us, SOA is a standards-based descendent of 
the object-oriented development techniques that became popular in the early 1990s. But 
object-oriented C++ applications never became widespread among the Global 10,000, 
even though the language did. Will the industry lose the opportunity for lower applica-
tion/service lifecycle costs as it did by failing to use the full re-use capabilities of object-
oriented C++? 
In a SOA, applications are no longer silos of program code; they’re incorporated into 
services. Nevertheless, the lifecycle revolves around the following long-used concepts 
and techniques, updated to use a services-centric view and with a keen eye to re-use: 
• 
Managing module versions of services and service components, including legacy 
applications; 
• 
Assessing and managing change impact on SOA operations and services; 
• 
Fostering re-use, quality, performance, and testing of services; 
• 
Employing SOA debugging, performance management, and recovery techniques; 
and 
• 
Integrating legacy custom programs, third-party independent software applica-
tions (e.g., ERP), and new application definition technology, especially BPM and 
related BPM models. 

Management and Governance: Planning for an Optimized SOA Application Lifecycle  
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
Aberdeen Group • 5 
Our recent survey on building better composite applications revealed that 75% of Best in 
Class organizations are unhappy with their application development tools and plan to 
supplement or replace this technology in the next six months. 
The Drivers for SOA Management and Control 
The most important driver in this survey is developing new business capabilities or prod-
ucts and services for the business (Figure 2). Best in Class companies are focusing more 
on managing IT complexity, which is increasing with the growing use of web services 
and SOA. 
Figure 2: Business Drivers for Investments in SOA Management and Governance 
41%
38%
47%
43%
34%
40%
50%
43%
30%
30%
44%
48%
36%
32%
36%
0%
10%
20%
30%
40%
50%
60%
Management of IT complexity
Development of new business capabilities or
new products and services
Re-usage of applications via Web Services
Speed of IT implementations
Alignment with the business
Laggard
Average
BIC
 
Source: Aberdeen Group, January 2007 
 
 

Management and Governance: Planning for an Optimized SOA Application Lifecycle 
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
6 • AberdeenGroup 
Chapter Two: 
Key Business Value Findings 
Key Takeaways 
• Get your organization up the SOA experience curve as soon as possible. 
• Dealing with SOA operational issues requires rethinking existing IT operations processes 
and updating them. 
• Third-party IT services are seen as a first response in bringing on needed experience 
and SOA best practices quickly. 
Experience Counts 
 
here is a high correlation in this survey between the overall maturity ranking in 
Aberdeen’s framework and experience with SOA technology (Figure 3). More 
than half of the Best in Class companies in our survey have at least 12 months of 
production experience with deployed applications under an SOA, while only 30% of the 
whole survey had this experience. But 20% of the Industry Average and Laggard compa-
nies in this survey had only six months or less of experience, twice as many as the Best in 
Class. 
Readers should consider this “experience counts” finding carefully. The good news is 
that there is light at the end of the tunnel for many companies riding the SOA learning 
curve. The challenge is how to best 
use the training period to best long-
term advantage. 
Finally, we note a prescient comment 
from a university IT manager, who 
stated: “The more experience we got, 
the more we realized what we didn’t 
know. That made us realize we 
needed outside help from services 
vendors and more peer-support ef-
forts.” 
IT Drivers for SOA Manage-
ment and Governance 
For 45% of the survey pool – and 46% of supply chain-oriented organizations -- the top 
driver for SOA management and governance is developing new business capabilities or 
new products and services (Figure 4). Management of IT complexity is second at 42% 
overall, yet a more apparent pressure for the Best in Class at 44%. This difference in pri-
ority is caused by the greater experience levels of the Best in Class. “The first applica-
tion-services server was a piece of operations cake”, a consumer products goods manu-
facturer told us. “But by the fifth server, we really did not know what was going on in-
side at any given moment, and that got scary quickly.” 
T 
“The more experience we got, the more we real-
ized what we didn’t know. That made us realize 
we needed outside help from services vendors 
and more peer-support efforts.” 
 ~ University IT manager 
 

Management and Governance: Planning for an Optimized SOA Application Lifecycle  
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
Aberdeen Group • 7 
Figure 3: Length of Time Since First SOA Services Were Deployed 
19%
19%
27%
18%
12%
10%
10%
19%
24%
33%
0%
5%
10%
15%
20%
25%
30%
35%
Plan to deploy in 2007
Less than six months
6-12 months
More than 12 months
More than 24 months
BIC
Overall
 
Source: Aberdeen Group, January 2007 
SOA Operations Challenges and Responses 
Standing in the way of optimized SOA operations is establishment of operational secu-
rity, governance, and management (Table 1). Twice as many survey respondents cite this 
as a top challenge over Best in Class companies. The key reason cited is the IT complex-
ity an SOA operations environment creates. The desire to manage IT complexity raises 
the challenge of establishing operational security, governance, and management. 
SOA security is the second challenge, with about the same numbers of Best in Class and 
all other respondents citing the differences and complexity that a loosely coupled, be-
hind-the-firewall SOA environment presents to IT operations. The third challenge: de-
bugging, caused by the different architecture of loosely-coupled SOA services compared 
to most prior IT applications using con-
ventional programming techniques. 
In response to these challenges, the top 
response, chosen by 45% of our sur-
vey, is to revise application lifecycle 
processes and responsibilities. This 
challenge is best illustrated by an auto-
motive parts manufacturer who told us, 
“With SOA, we were forced to rewrite 
whole chapters of our IT processes 
manual…and that’s not a bad thing”. 
Second, 41% of our survey have en-
gaged third-party IT services firms for consulting, evaluation, and assessment. But only 
25% of the Best in Class companies are taking this route since they tend to be more ex-
perienced. 
”With SOA, we were forced to rewrite whole 
chapters of our IT processes manual…and that’s 
not a bad thing.” 
 ~ Automotive parts manufacturer 
 

Management and Governance: Planning for an Optimized SOA Application Lifecycle 
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
8 • AberdeenGroup 
Figure 4: IT Drivers for SOA Management and Governance 
43%
34%
47%
41%
38%
30%
30%
43%
40%
50%
32%
36%
36%
44%
48%
0%
10%
20%
30%
40%
50%
60%
Speed of IT implementations
Alignment with the business
Re-usage of applications via Web
Services
Management of IT complexity
Development of new business capabilities,
products and services
Laggard
Average
BIC
 
Source: Aberdeen Group, January 2007 
Table 1: SOA Operations Challenges and Responses 
Challenges 
% Selected 
Responses to Challenges 
% Selected 
Establishment of operational secu-
rity, governance, and management 
45% 
Revised our application lifecycle 
process and responsibilities 
45% 
Security issues are different from 
those of older IT 
38% 
Engaged third-party IT services 
consulting, evaluation, and as-
sessments 
41% 
Debugging problems with complex 
services, composites 
37% 
 
Purchase or plan to purchase SOA 
operations management software 
28% 
SLAs: Scaling to production vol-
umes, reliability and availability 
37% 
 
Purchase or plan to purchase SOA 
security software 
26% 
Data management of SOA services 
is problematic 
33% 
Invested in additional operations 
and applications lifecycle training 
22% 
QA: Testing and deployment stage 
problems spill over into production 
31% 
 
Bought additional computer capac-
ity to minimize perform-
ance/capacity issues 
19% 
Source: Aberdeen Group, January 2007 
 

Management and Governance: Planning for an Optimized SOA Application Lifecycle  
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
Aberdeen Group • 9 
Chapter Three: 
Implications & Analysis 
Key Takeaways 
• 
Existing processes do not apply well to new SOA operations and governance issues 
and require changes. 
• 
Best in Class companies achieve performance excellence in SOA operations and gov-
ernance, partly through the use of SOA-specific technology. 
• 
Using operations, governance, and application lifecycle management technology, Best 
in Class companies are focused on ─ and achieving ─lower long-term costs. 
 
s shown in Table 2, survey respondents fell into one of three categories – Lag-
gard, Industry Average, or Best in Class — based on their characteristics in four 
key categories: (1) process (investment/payback metrics, SOA-specific processes 
and governance); (2) organization (SOA IT topology, governance philosophy); 
(3) knowledge (visibility into operations, governance, and lifecycle cost data); and (4) 
technology (scope of SOA management and governance automation, productivity tools). 
In each of these categories, survey results show that firms exhibiting Best in Class SOA 
operations and governance characteristics also enjoy Best in Class application lifecycle 
performance and payback on their companies’ SOA investments (Table 2). 
Table 2: SOA Operations and Governance Competitive Framework 
 
Laggards 
Industry Average 
Best in Class 
Process 
 
Using existing IT opera-
tions processes not 
adjusted for loosely-
coupled SOA architec-
ture and technology 
Some SOA operations 
processes have been 
planned or are in place; 
modest SOA governance 
activities 
SOA-tuned operations; IT 
governance accounts for 
SOA design and operations; 
application lifecycle cost 
awareness.  
Organization 
SOA has not caused a 
change in organization. 
Changes planned or 
newly implemented  
Roles and responsibilities 
revised for SOA operations 
and governance. 
Knowledge  
Limited SOA experience 
means no visibility of 
pitfalls ahead; modest 
problems due to limited 
scale, experience. 
Knowledge limited to key 
personnel and not scal-
able; challenged and 
reactive to unanticipated 
operations and govern-
ance crises. 
Experienced veterans who 
have widespread hands-on 
SOA production experience; 
management has changed 
goals and metrics based on 
experiences. 
Technology 
“SOA Lite” web ser-
vices; no special SOA 
operations; no IT gov-
ernance or SOA gov-
ernance automation; 
project-based ROI 
Increasing SOA middle-
ware use; plans and 
some  purchases of op-
erations, governance, 
and application lifecycle 
automation 
Enterprise middleware tech-
nology supplemented by 
SOA operations and gov-
ernance automation; lifecy-
cle-based application ROI 
 
Source: Aberdeen Group, January 2007 
A 

Management and Governance: Planning for an Optimized SOA Application Lifecycle 
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
10 • AberdeenGroup 
Process and Organization 
In the process category, companies in the survey that employ SOA operations automation 
products and SOA-related governance consistently achieve much higher ROI on their 
SOA investments. Some 40% of the Best in Class companies earned a payback of more 
than $1 million on their SOA investments, compared to 17% of the survey overall. Lag-
gard firms are trying to get by with both the existing processes and organization. 
Technology Provides Leverage to the Best-in-Class Companies 
Best in Class firms in our survey are employing SOA operations management software to 
automate the SOA-specific services they’re deploying, as well as SOA governance soft-
ware, typically an upgrade from an existing automated IT governance software package’s 
processes. The Best in Class companies are focusing on the entire life of an application 
“service”, from design through programming, testing, deployment, and into maintenance. 
We asked, “How has SOA development in the past year changed the IT costs of the ap-
plication/service lifecycle?” As Table 3 clearly shows, the automation investments by the 
Best in Class resulted in decreases in development costs in 2006 while the majority 
of Industry Average and Laggard companies are actually seeing their development 
costs increase. 
Importantly, 58% of Laggard firms are not taking action to treat SOA operations, gov-
ernance, and the resulting lifecycle costs as anything different from past processes. These 
companies are least likely to use SOA operational management, governance, and applica-
tion lifecycle management software. 
Table 3: Application Lifecycle Cost Changes by Maturity Framework – 2006 
 
Laggards 
Industry  
Average 
Best in 
Class 
No change 
55% 
43% 
12% 
Increased costs up to 5% 
24% 
14% 
4% 
Increased costs 6-10% 
2% 
12% 
4% 
Increased costs 11-20% 
4% 
8% 
4% 
Increased costs 21-30% 
 
2% 
8% 
Increased costs more than 30% 
7% 
1% 
 
Decreased costs up to 5% 
5% 
8% 
28% 
Decreased costs 6-10% 
2% 
7% 
12% 
Decreased costs 11-20% 
2% 
4% 
12% 
Decreased costs 21-30% 
 
 
8% 
Decreased costs more than 
30% 
 
1% 
8% 
Source: Aberdeen Group, January 2007 

Management and Governance: Planning for an Optimized SOA Application Lifecycle  
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
Aberdeen Group • 11 
Pressures, Actions, Capabilities, Enablers (PACE) 
Table 4 shows how operations, governance, and application lifecycle technologies map to 
the SOA-driving pressures that were listed in Chapter Two. These findings highlight is-
sues cited in previous Aberdeen research in 2006, namely: 
• 
The biggest challenge in corporate IT organizations is improving real-time visi-
bility into business operations; 
• 
Business is discovering the SOA as a technological foundation that can make 
businesses more nimble and business processes more flexible with less IT inter-
vention than prior approaches; and 
• 
As organizations gain more experience with SOA technology and methodologies, 
they realize that currently used approaches and methodologies do not match well 
with the best practices in using an SOA. 
Table 4: Prioritized Pressures and Enablers 
Priorities 
Prioritized Pressures 
Prioritized Enablers 
1 
Development of new business capabili-
ties, products, and services 
* Harnessing custom and third-party applica-
tions, such as ERP, under an SOA 
* Building composite applications 
2 
Management of IT complexity 
* Enterprise SOA middleware technology 
* SOA operations management technology 
* SOA governance technology 
3 
Re-use of applications via Web Services 
and SOA 
* Design-time governance software 
* Application lifecycle management software 
4 
Speed of IT implementations 
* Design-time governance software enables 
service reuse, quicker delivery 
* SOA governance and application lifecycle 
management software keep projects on track 
5 
Alignment with the business 
* Composite applications that span at least 
some of the following: legacy applications, 
ERP, best-of-breed applications, web-
hosted/On Demand applications, customers’ 
or suppliers’ applications 
* Design-time governance software enables 
service reuse, quicker delivery 
Source: Aberdeen Group, January 2007 
Governance Views by Industry 
Not all industries have the same view on the importance or management reason for a 
formal IT governance policy (Figure 5). The findings from our survey make it clear that 

Management and Governance: Planning for an Optimized SOA Application Lifecycle 
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
12 • AberdeenGroup 
governance of SOA design, operations, and policy management are critical factors in 
achieving process excellence and higher results, especially over time, to wit: 
• 
None of our survey participants will ignore governance going forward, even 
those whose companies have not implemented IT governance policies to date; 
• 
The Best in Class companies are most likely to have existing IT governance poli-
cies in place, updated to reflect the necessities of an SOA environment; and 
• 
The strong correlation between use of governance (and application lifecycle) 
automation and higher SOA investment payback, resulting in overall lower ap-
plication development costs. 
The public sector is driven by regulation. But the services industry is strongly driven to 
governance as a means of lowering application lifecycle costs. 
Figure 5: SOA Governance Drivers by Industry 
46%
26%
22%
40%
18%
46%
24%
19%
53%
24%
54%
38%
8%
31%
54%
0%
10%
20%
30%
40%
50%
60%
To ensure uniform and consistent application
of policy across the organization.
SOA governance is an update to our existing
IT governance process
Our management team demands clear policy
and accountability
We are striving to lower application lifecycle
costs: saving money over time.
Governance is mandated by government or
regulation.
supply chain
services
public
 
Source: Aberdeen Group, January 2007 
 

Management and Governance: Planning for an Optimized SOA Application Lifecycle  
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
Aberdeen Group • 13 
Chapter Four: 
Recommendations for Action 
Key Takeaways 
• 
The larger the company, the greater the need for management by IT governance policy, 
preferably automated. 
• 
Focus on the long-term goal of lowering application lifecycle costs and avoid the ten-
dency to look to take a short-term project ROI while increasing long-term costs. 
• 
Since Best in Class companies are also the most experienced, proactively utilize train-
ing and IT services to speed up the learning curve. 
 
ost control of the application lifecycle is a long-term benefit worthy of manage-
ment’s attention. Best in Class companies in this survey are most likely to have 
well-defined processes for managing and governing SOA design and operations, 
including the use of application lifecycle management software and IT governance soft-
ware to automate the process. And, these companies are not paying lip service to the sub-
ject. To reinforce this point, users need both SOA operations management as well as 
governance. This is not an “either/or” choice, nor are the two mutually exclusive. 
As an airline IT executive told us: 
“There are too many moving parts in 
our IT operations not to have applica-
tions watching applications ─ and pro-
grammers. That’s the only way we can 
sleep at night.” 
Based on the information in Chapters 
Two and Three, readers should deter-
mine whether their organizations fall 
into the “Laggard”, “Industry Average,” 
or “Best in Class” categories. The key 
to gaining value from this report is 
moving your organization along the maturity path to Best in Class. The following actions 
will help spur necessary performance improvements: 
Best in Class Next Steps 
1. Build out your SOA infrastructure — methodically. 
Plan and deploy the SOA middleware — enterprise service bus, repository, secu-
rity, management and governance — needed to support your organization’s long-
term plans. That may well require an enterprise-level capital expenditure since 
the cost won’t fit into a project budget. Even many Best in Class firms have yet 
to complete this task. 
2. Tighten governance, especially at design time. 
C 
“There are too many moving parts in our IT op-
erations not to have applications watching appli-
cations ─ and programmers. That’s the only way 
we can sleep at night.” 
 ~ Airline IT executive 
 

Management and Governance: Planning for an Optimized SOA Application Lifecycle 
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
14 • AberdeenGroup 
With experienced companies reporting code re-use in the 50%-70% range under 
SOA, there is a lot of value to shoot for. However, it will cost more to develop 
reusable code. Employ tight project schedules and lifecycle-cost focused re-use 
planning as governance techniques. 
3. Aim for the application lifecycle cost “brass ring”. 
Focus programming governance efforts on a best-practices program to drive all 
aspects of lowering costs in the lifecycle of applications. 
Industry Average Steps to Success 
1. Upgrade from Web services to an Enterprise SOA infrastructure plan. 
The allure of improved IT agility using composite applications constructed with 
Web services should be tempered with the reality of a plan to quickly build out 
an Enterprise SOA infrastructure as described in Chapter 1. SOA infrastructure 
middleware is a prerequisite to scalable, well-mannered IT operations. 
2. Anticipate increasing complexity 
Survey participants tell us IT complexity (especially in operations) increases al-
most exponentially at first as more SOA services and servers are added. The in-
ternal costs of disruption can be high and hinder ongoing project roll-outs. Ac-
celerated training programs, SOA management software, and the judicious use of 
third-party IT services are the ingredients for getting over the complexity hump 
of the learning curve. 
3. Turn SOA governance plans into reality 
Every company in our survey believes there is an SOA governance process in 
their future. Many are at the planning stage. Automating SOA governance is an 
investment the vast majority of mid-size and large companies ought to make. 
4. Start planning for the control of application lifecycle costs 
This survey clearly demonstrates that design-time and programming extra effort 
can lower application lifecycle costs through code reuse at 50% and above. Start 
planning by measuring application lifecycle costs, examining whether current 
SOA development practices encourage “one time” programming or reuse. Con-
sider automated lifecycle management tools as part of the development govern-
ance process. 
Laggard Steps to Success 
1. Establish operational security, governance, and management policies and proc-
esses. 
The old, but true, adage is “you can’t manage what you can’t measure.” Too 
many Laggard organizations lack the process, let alone automation, for the proc-
ess. Start with SOA operations, then move to design governance, revising appli-
cation lifecycle processes and responsibilities along the way. 
2. Fix the lack of management support to drive SOA governance as a means to low-
ering lifecycle costs. 

Management and Governance: Planning for an Optimized SOA Application Lifecycle  
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
Aberdeen Group • 15 
More than one-third of Laggard organizations face management that is not con-
vinced of the long-term benefits of governance as a way to lower application 
lifecycle costs. This report is ammunition, but driving SOA governance will re-
quire more company-specific proof points. For example, a 50% code re-use un-
der SOA governance cuts the lines of code maintained in half permanently. 
3. Plan for the long haul. 
The ROI of too many SOA projects are justified under business-as-usual rules 
favoring project-based ROI. That approach won’t unlock the long-term value to 
the entire organization of lower application lifecycle costs or solve the manage-
ment of IT complexity issues driven by a growing use of SOA. Our 2006 surveys 
showed that companies following an “Enterprise SOA” strategy (see Chapter 1) 
can scale more easily with lower short- and long-term costs by investing in all 
aspects of SOA infrastructure software and in IT staff training. 
 
 
 
 

Management and Governance: Planning for an Optimized SOA Application Lifecycle 
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
16 • AberdeenGroup 
Featured Underwriters 
This research report was made possible, in part, with the financial support of our under-
writers. These individuals and organizations share Aberdeen’s vision of bringing fact 
based research to corporations worldwide at little or no cost. Underwriters have no edito-
rial or research rights and the facts and analysis of this report remain an exclusive pro-
duction and product of Aberdeen Group. 
Actional products from Progress Software pro-
vide enterprise-grade SOA management capabilities, including service and message flow 
monitoring, SLA governance, versioning, and security ─ at extremely low overhead and 
thus minimal impact on system performance. Every enterprise building or testing an SOA 
will require the capabilities available in Actional products; whether they are starting to 
expand early SOA projects, or have a fully deployed enterprise-grade SOA using ESBs, 
application servers, or other technologies. 
For more information on Actional products from Progress Software, contact: 
Sales Department 
Progress Software Corporation 
14 Oak Park Drive; Bedford, MA 01730 USA 
1 866-438-7664 (US toll free) 
1-781-280-4000 
Fax: 1-781-999-7202 
http://www.progress.com/actional 
 or http://www.actional.com 
eval@progress.com 
 
 
 
 
 
 
 

Management and Governance: Planning for an Optimized SOA Application Lifecycle  
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
Aberdeen Group • 17 
 
iTKO LISA offers a complete Lifecycle Quality governance for 
testing Service-Oriented Architectures (SOA). iTKO's mission is to allow everyone in-
volved in IT to own Complete, Collaborative, and Continuous software quality. iTKO 
LISATM SOA Test Framework performs unit, functional, regression, load and perform-
ance tests, without requiring test coding or script maintenance, saving development and 
QA teams effort while improving quality at every phase of development and deployment. 
LISA provides live interaction with web apps, web services, J2EE, .NET, Java objects, 
ESB, databases, and many more technologies. Founded in 1999, the Dallas-based com-
pany's customers include Sun, Capgemini, Cardinal Health, AMD, TIBCO, and i2. 
For more information on iTKO, contact: 
iTKO, Inc. (Interactive TKO) 
1505 LBJ Freeway, Suite 250; Dallas, TX 75234 
1-877-289-4856 
http://www.itko.com 
info@itko.com 
 
Mindreef provides Web services and SOA 
testing solutions that allow organizations to drive pervasive quality into SOA deploy-
ments, and accelerate service reuse and business agility. Mindreef’s award-winning 
SOAPscope and SOAPscope Server reduce the complexities of Web services and XML, 
empowering teams with prototyping, compliance, testing, diagnostics, and support tools 
that improve SOA quality throughout design-time, change-time and run-time. Mindreef 
solutions help analysts, architects, developers, testers, operations and support staff to en-
sure quality as they build, test, and deploy Web services and composite applications. 
Mindreef products are used by over three thousand customers at over 1,200 organizations 
worldwide, including 40 of the Fortune 100. 
For more information on Mindreef contact: 
Mindreef, Inc. 
22 Proctor Hill Road, Hollis, NH 03049 
1-603-465-2204 
http://www.mindreef.com  
info@mindreef.com 
 
 

Management and Governance: Planning for an Optimized SOA Application Lifecycle 
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
18 • AberdeenGroup 
Appendix A: 
Research Methodology 
etween November 2006 and January 2007, Aberdeen Group examined the SOA 
management strategies of more than 200 companies across a variety of geogra-
phies, industries and company revenues. 
Aberdeen supplemented this online survey effort with telephone interviews with select 
survey respondents, gathering additional information on SOA management strategies, 
experiences, and results. 
The study aimed to identify emerging best practices for SOA operations management and 
governance, and provide a framework by which readers could assess their own organiza-
tion’s capabilities and maturity. 
Responding enterprises included the following: 
• 
Job title/function: About half of the survey respondents are in their organiza-
tions’ IT departments. The research sample included respondents with the fol-
lowing job titles: senior executive (CEO, COO, CFO, VP) (13%); CIO (11%); IT 
manager or director (32%); internal consultant (21%), and IT staff (8%). 
• 
Industry: The research sample included respondents predominantly from manu-
facturing industries and companies with a supply-chain focus (wholesale, retail, 
distribution, high tech). These represented 52% of the sample, of which 53% 
were manufacturing. Services industries including banking, brokerage, insurance, 
and health care represented 40% of the survey. Public sector (government and 
education) represented 8% of the survey. 
• 
Geography: The survey respondents were distributed: North America (U.S., 
Canada, Mexico) 57%; Central and South America 4%; Asia/Pacific 16%; 
Europe, Middle East, and Africa 24%. 
• 
Company size: About 46% of respondents were from large enterprises (annual 
revenues above US$1 billion, including 27% over US$5 billion); 38% were from 
midsize enterprises (annual revenues between $50 million and $1 billion); and 
28% of respondents were from small businesses (annual revenues of $50 million 
or less). 
Solution providers recognized as sponsors of this report were solicited after the fact and 
had no substantive influence on the direction of this report. Their sponsorship has made it 
possible for Aberdeen Group to make these findings available to readers at no charge. 
B 

Management and Governance: Planning for an Optimized SOA Application Lifecycle  
 
 
All print and electronic rights are the property of Aberdeen Group © 2007. 
Aberdeen Group • 19 
Table 5: PACE Framework 
PACE Key 
Aberdeen applies a methodology to benchmark research that evaluates the business pressures, actions, 
capabilities, and enablers (PACE) that indicate corporate behavior in specific business processes. These 
terms are defined as follows: 
Pressures — external forces that impact an organization’s market position, competitiveness, or business 
operations (e.g., economic, political and regulatory, technology, changing customer preferences, competi-
tive) 
Actions — the strategic approaches that an organization takes in response to industry pressures (e.g., align 
the corporate business model to leverage industry opportunities, such as product/service strategy, target 
markets, financial strategy, go-to-market, and sales strategy) 
Capabilities — the business process competencies required to execute corporate strategy (e.g., skilled 
people, brand, market positioning, viable products/services, ecosystem partners, financing) 
Enablers — the key functionality of technology solutions required to support the organization’s enabling 
business practices (e.g., development platform, applications, network connectivity, user interface, training 
and support, partner interfaces, data cleansing, and management)  
Source: Aberdeen Group, January 2007 
Table 6: Relationship between PACE and Competitive Framework 
PACE and Competitive Framework How They Interact 
Aberdeen research indicates that companies that identify the most impactful pressures and take the most 
transformational and effective actions are most likely to achieve superior performance. The level of com-
petitive performance that a company achieves is strongly determined by the PACE choices that they make 
and how well they execute. 
Source: Aberdeen Group, January 2007 
 
 
 
 
 
 

 
Aberdeen Group, Inc. 
260 Franklin Street 
Boston, Massachusetts 
02110-3112 
USA 
Telephone: 617 723 7890 
Fax: 617 723 7897 
www.aberdeen.com 
© 2007 Aberdeen Group, Inc. 
All rights reserved 
March 2007 
Founded in 1988, Aberdeen Group is the technology- 
driven research destination of choice for the global  
business executive. Aberdeen Group has over 150,000 
research members in over 36 countries around the world 
that both participate in and direct the most comprehen-
sive technology-driven value chain research in the  
market. Through its continued fact-based research, 
benchmarking, and actionable analysis, Aberdeen Group 
offers global business and technology executives a 
unique mix of actionable research, KPIs, tools,  
and services. 
 
The information contained in this publication has been obtained from sources Aberdeen believes to be reliable, but 
is not guaranteed by Aberdeen. Aberdeen publications reflect the analyst’s judgment at the time and are subject to 
change without notice.  
The trademarks and registered trademarks of the corporations mentioned in this publication are the property of their 
respective holders. 
Appendix B: 
Related Aberdeen Research & Tools 
Related Aberdeen research that forms a companion or reference to this report include: 
• 
The Composite Applications Benchmark Report, December 2006 
• 
The Legacy Application Modernization Benchmark Report; September 2006 
• 
The Business Process Management Benchmark Report; August 2006 
• 
Outsourcing Application Development and Maintenance; November 2006 
• 
Enterprise Service Bus and SOA Middleware; June 2006 
• 
The SOA in IT Benchmark Report; December 2005 
Information on these and any other Aberdeen publications can be found at 
www.Aberdeen.com. 
 

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
• 
Table of Contents: A dynamic Table of Contents (TOC) helps you navigate through the 
report. Simply select “Show Bookmarks” from the “Windows” menu, or click on the bookmark 
icon (fourth icon from the left on the standard toolbar) to access this feature. The TOC is both 
expandable and collapsible; simply click on the plus sign to the left of the chapter titles listed 
in the TOC. This feature enables you to change your view of the TOC, depending on whether 
you would rather see an overview of the report or focus on any given chapter in greater 
depth. 
• 
Scroll Bar: Another online navigation feature can be accessed from the scroll bar to the right 
of your document window. By dragging the scroll bar, you can easily navigate through the 
entire document page by page. If you continue to press the mouse button while dragging the 
scroll bar, Acrobat Reader will list each page number as you scroll. This feature is helpful if 
you are searching for a specific page reference. 
• 
Text-Based Searching: The PDF format also offers online text-based searching capabilities. 
This can be a great asset if you are searching for references to a specific type of technology 
or any other elements within the report.  
• 
Reader Guide: To further explore the benefits of the PDF file format, please consult the 
Reader Guide available from the Help menu.


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-ra-soa-management-governance-20-ff6a2c |
| title | Management and Governance: Planning for an Optimized SOA Application Lifecycle |
| author | Peter S. Kastner and Rick Saia (Aberdeen Group) |
| date | 2007-03-01 |
| type | benchmark-report |
| subject_domain | soa-management-governance-application-lifecycle |
| methodology | survey-benchmarking, best-practices-analysis, expert-opinion |
| source_file | RA_SOAGov_3944_PKRS_040307a-8.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group benchmark report co-authored by Peter Kastner and Rick Saia (PKRS) examining the effectiveness of IT investments across operations management; design and operations governance; and underlying changes in project management, development, testing, and application lifecycle management tools for SOA. Survey of 200+ companies (Nov 2006-Jan 2007) finds that between a third and half of the 950 companies surveyed in 2006 are having serious difficulties getting SOA-enabled applications into stable deployment, with inadequate management/governance tools the predominant cause. Best-in-Class (top 20%) characteristics: 33% have >2 years SOA experience; 68% achieve positive SOA ROI vs. 77% of overall sample yet to see payback; design-time governance and re-use policy implemented; 80%+ have automated SOA operations and governance solutions.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Kastner co-authored Aberdeen benchmark of an emerging mid-2000s discipline (SOA governance) that became the foundation of modern API governance, service-mesh policy enforcement, and software-supply-chain management. |
| **Relevance** | high | Design-time governance, re-use policy, and automated lifecycle/governance tools remain central to API and microservices platforms a decade later. |
| **Prescience** | high | Kastner and Saia's central claim — that SOA management and governance are inseparable from total software lifecycle costs and that the Best-in-Class invest early in automation — was fully validated by the API gateway, service mesh, and platform-engineering movements of the 2015-2025 period. The 'collar IT with long-term software maintenance costs that will endure for decades' warning is now the central rationale for modern platform-engineering investment. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (4)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | acquired | Harte-Hanks (2007); Spectrum Equity (2017) |
| Peter S. Kastner | person | active |  |
| Rick Saia | person | active |  |
| Mindreef, Inc. | company | acquired | Progress Software (2008) |

### Technologies Referenced (6)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| SOA Management and Governance | category | industry | growth | evolved-to-api-governance |
| Design-Time Governance | discipline | industry | growth | active |
| Operational SOA Governance | discipline | industry | growth | evolved-to-service-mesh |
| Application Lifecycle Management (ALM) | category | industry | growth | active |
| Aberdeen PACE Framework | methodology | Aberdeen Group | active | legacy |
| Mindreef SOAPscope / SOAPscope Server | tool | Mindreef | mature | discontinued |

### Observation Summary

- Total observations: 17
- By type: market-data: 12, expert-opinion: 4, biographical: 1
