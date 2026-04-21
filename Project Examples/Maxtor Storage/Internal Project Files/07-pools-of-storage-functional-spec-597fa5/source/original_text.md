# Pools of Storage Decision Tool — Functional Specification (Aberdeen Internal)

> Archived from: 07-Pools-of-Storage-Functional-Spec.txt
> Original publication date: 2003-11-26
> Author: Peter Kastner (executive sponsor); Jay Erikson (primary author)

---

## Original Document Text













Functional Specification

Aberdeen Internal Use Only

Do Not Share With Maxtor















November 26, 2003
Table of Contents
Overview	4
Purpose	4
Solution Framework	4
Competitive Framework	4
Financial Framework	4
Case for Action	4
Success Criteria	5
Reports	5
Navigation	5
Interface Design	5
Resources	6
Content Management	7
Development Environment	7
Timeframe	7
Cost	8
Related Documentation	8
Document Feedback	8
Document Version Control	8
Appendix A: System Workflow	9
Launch/Login Screen	9
Signup Screen	9
Introduction Screen	9
Solution Workflow Questions	10
Solution Workflow Response-Recommended Solution	10
Competitive Workflow Introduction/Transition	11
Initial Maturity Grid	11
Maturity Grid Survey Questions	11
Maturity Grid Results	12
Competitive Framework Diffusion Chart	12
Financial Workflow Introduction/Transition	12
KPI Input	13
KPI "As-Is" Position	13
KPI Change Level	14
KPI "To-be" Position	14
Case for Action Introduction/Transition	15
Results-Financial Benefit	15
Results-Case for Action	16
Appendix B: Gantt Chart	17

Overview
This document defines the functional requirements for the Pools of Storage Decision Tool ("system"). Specifically, it describes the purpose, success criteria, requirements, and parameters for developing the system. It also includes a system workflow-a screen-level description of the system as Appendix A. The purpose of this document is to serve as an agreement of understanding between the executive sponsors and developers on the functionality of the system.
This document contains internal comments which are not appropriate to share with the client, Maxtor Corp.  Under no circumstances is this document to be shared with the client.  A separate, sanitized version titled xxxxxxxxxxxxx is the official, public functional specification.
This document is a "living document" that will be updated during the project to reflect changes to requirements, processes, or interactions. A Document Version Control table is located at the end of the document to track changes to this Functional Specification.
Purpose
The Pools of Storage Decision Tool is a guided decision support tool. The tool is composed of four distinct stages: Solution Workflow, Competitive Workflow, Financial Framework, and Case for Action. 
Solution Framework
    - Purpose: Identify areas of business processes (e.g. Manufacturing information storage around new product introduction) and IT investment that offer the greatest business value and storage investment "optimization".
    - Output: The identification of a single, recommend business process where the application of Pools of Storage will have the greatest quantifiable business impact.
Competitive Framework
    - Purpose: Understand how the user compares to industry peers when evaluating the recommended business process.
    - Output: The location of the user's company on a capability maturity continuum for business process identified in the Solution Framework.
Financial Framework
    - Purpose: Identify the key performance indicator (KPI) for managing and measuring the business process identified in the Solution Framework, and evaluate the company's performance by entering financial data for the key performance indicator.
    - Output: The location of the user's company on a maturity continuum based on financial indicators.
Case for Action
    - Purpose: Evaluate the user's business and financial case, go-forward strategies, as well as the needed Pools of Storage frameworks and storage technologies to support those strategies.
    - Output: The optimal financial results of applying Pools of Storage to the business process identified in the Solution Framework, and a specific set of immediate action plans for the user to undertake to be prepared to exploit Maxtor's midline solution(s). This output is summarized in a Case for Action Report. 
Success Criteria
The success of the Pools of Storage Decision Tool will be defined by the tool's ability to meet the following criteria. The tool should:
    - Demonstrate best practices, ROI, and TCO savings through the use of a comprehensive enterprise Pools of Storage program.
    - Reinforce Maxtor's Pools of Storage strategy and lexicon.
    - Perform at a level that that reflects the quality of Aberdeen and Maxtor.
    - Generate highly qualified and information rich leads from users.
    - Build credibility with Maxtor about Aberdeen's ability to meet Maxtor's expectations and deliver the type of quality product required for a Center of Excellence.
Reports
One key success factor is to generate highly qualified and information rich leads from users. Aberdeen will provide Maxtor withThe tool can generate a spreadsheet of registration data and user activity. Time and budget permitting, we may provide a web interface to allow Maxtor to pull lead generation data from a separate, secure web page.
The tool will generate a business case printout or .pdf of the user's assumptions, inputs, and resulting recommendations.
Navigation
The system will have sequential navigation through each stage. User choices will be recorded at the culmination of each stage; however, no user persistence will be developed for this project. If a user terminates a session before completing all stages, the user will have to start over.
The system will contain four introduction or transition pages between stages and a help page.
Interface Design
The Pools of Storage Decision Tool will be designed with Maxtor branding-colors, fonts and logos ("Maxtor look and feel"). The interface will have a "Power by Aberdeen" logo. 
Resources
Name	Role	Responsibilities
Peter Kastner	Executive Sponsor	Executive sponsor responsible for overall quality and delivery of program. Provide content for PoS Tool; review tool for application of Maxtor's strategy, lexicon, and benefits for end-users gained through PoS program.
Stan Elbaum	Executive Sponsor	Responsible for overall quality and delivery of the PoS Tool. Responsible for business and financial logic encapsulated in the tool.
David Hill	Analyst	Provide content for PoS Tool; review tool for application of Maxtor's strategy, lexicon, and benefits for end-users gained through PoS program.
Contractor	Analyst	Develop Maturity Grids
John Boyne	Project Manager	Project manager for entire Pools of Storage Executive Evangelism Program.
Jay Erikson	Developer	Develop application logic and data structure for PoS tool.
Michael Beganny	Developer	Develop Web pages-integration of design and application logic.
John McLaughlin	Developer	Design user interface with Maxtor brand, and general usability standards.
Kerri Conrad	Reviewer	Review tool for information architecture and usability design standards. Review tool for application of Maxtor's strategy, lexicon, and benefits for end-users gained through PoS program.
Beth Conant	Reviewer	Edit Maturity Grids, action items and storage recommendations. 

Content Management
Content will be developed by several individuals and should be reviewed and approved prior to entering the data into the database to avoid cost overruns. No content management system will be developed; all content will be manually entered into the database. Content updates may be sold as an update service to Maxtor.
Content Item	Responsible	Date
Solution Workflow Question (5 questions and 5 pools of possible answers); approximately 6 recommended solutions.	Stan	12/31/2003
18 Maturity Grids	David, Beth, contractor	12/31/2003
KPI (indicators and calculations)	Stan	12/31/2003
Action Items	David, Beth, contractor	12/31/2003
Storage Recommendations	David	12/31/2003
Introduction, transition text, and help text	Kerri	12/31/2003

Development Environment
The Pools of Storage Decision Tool will be built with Microsoft Active Server Pages (ASPs) connecting to a Microsoft SQL Server 2000 database. The system will run on Windows 2000 Servers.
The system will be designed for Internet Explorer 5.5 and higher on the Windows platforms. Other browsers on different platforms may access the system, however, full compatibility is not supported for other browsers or platforms. No plugins are required to use the system.
Production Environment
The system will run on Microsoft Internet Information Server (version?) under Windows Server 2000 or later and requires a connection to the database, therefore, no offline version is available; the system must be accessed via the Internet. 
Aberdeen will provide three months hosting for the Pools of Storage Decision Tool at which point Maxtor can assume hosting responsibilities or initiate an extended hosting agreement with Aberdeen.  Describe the Aberdeen-provided hosting environment here and the associated costs.
Describe the Aberdeen provided service levels (e.g., 8x5) during the hosting period.  Describe the problem escalation process for hardware, system software, network, and Aberdeen software.
Describe network performance characteristics and goals.  Presumably, you will be able to run on a 52Kbps dial-up.
Describe server performance characteristics.  I recommend we allow (X=100) X user threads, and "hold" sessions until a thread is open via time-out (15 minutes per screen) or completion.
Timeframe
The project has a planned duration of six weeks starting Monday, November 24, 2003 concluding Friday, January 16, 2004. A Gantt chart is included as Appendix B.
Cost
The planned cost for development of the Pools of Storage Decision Tool is $23,101.55. This cost is strictly for development and review of the tool, and does not include resources or budget for content development, support, or ongoing maintenance. Three months of hosting is included in the fee for the entire program.
Related Documentation
    - Proposal
    - Design document-System components, use cases, validation (to be developed)
    - Database design (to be developed)
Document Feedback
Provide feedback on this document to Jay Erikson at 970-232-7008 or via email at Jay.Erikson@Aberdeen.com.
Document Version Control
The following table tracks changes to this functional specification. Subsequent versions of this document will be renamed by appending the latest version number to the document. The original document title is PoS Functional Spec v1.0.doc.
Version	Date	Author	Revision Description
1.0	11/25/03	Jay Erikson	Original document version.
			
			
			
			

Appendix A: System Workflow
The following section describes the anticipated screens for the system:
Launch/Login Screen
Description	One screen that presents the user with a login form (username and password). Signup instructions and screen link also on launch page.
Data	    - Username
    - Password
Behavior	    1. The system displays a login form
    2. When the user clicks the submit button, the system authenticates the user.
    3. The system then forwards the user to the Introduction page.
Alternate Flow	Invalid username; invalid password; database unable to process query.

Signup Screen
Description	One screen that presents the user with registration form. 
Data	    - Fields TBD (some fields will be required)
Behavior	        1. The system displays a registration form
        2. When the user clicks the submit button, the system records the user's information in the database
        3. The system then logs the user in and forwards the user to the Introduction screen.
Alternate Flow	Incomplete form; password and password confirm fields don't match; invalid username (already exists); user navigates away from Sign Up screen; database unable to process query.
Link to privacy statement & About

Introduction Screen
Description	One screen that provides an introduction/overview to the tool and instructions for how to use the tool.
Data	None
Behavior	    1. Display overview and instructions.  Note:  strong warning to user not to quit before completing or else all is lost.
    2. User clicks next to advance to Solution Workflow Questions screen.

Solution Workflow Questions
Description	One screen that presents the user with five questions. Answers to the questions "describe" the user's company. Users must select an answer from a group of predefined choices. This is the first screen in the Solution Workflow stage.
Data	    - What is your ecosystem?
    - What is your role in that ecosystem?
    - What is the asset base of your company?
    - What is your geographical supply chain footprint?
    - How customized are your solutions?
Behavior	        1. Display questions (drop down) form-the groups of predefined choices are static, however the form is populated from a database.
        2. User clicks submit to advance to Solution Workflow Response screen.

Solution Workflow Response-Recommended Solution
Description	One screen that lists recommended solution and alternative solutions (output of Solution Workflow). This is the last screen in the Solution Workflow Stage. When the user clicks the Next button, the system records the user's answers in the database-this data may be used to enhance feedback "information rich leads" to Maxtor.
Data	    - Recommended solution.
Behavior	        1. The system processes user's responses to Solution Workflow questions and identifies a recommended solution.
        2. Display recommended solution and alternative solutions.
        3. User clicks next to advance to Competitive Workflow Introduction/Transition screen.
Alternate Flow	User clicks browser's back button to change answers in Solution Workflow Questions. 

Competitive Workflow Introduction/Transition
Description	One screen that provides a transition from the Solution Workflow stage with an introduction and instructions for the Competitive Workflow stage. This is the first screen of the Competitive Workflow stage.
Data	None
Behavior	    1. User clicks next to advance to Initial Maturity Grid screen.

Initial Maturity Grid
Description	One screen that displays the complete identified Maturity Grid.
Data	    - Identified Maturity Grid
Behavior	    1. The system processes the user's responses to the Solution Workflow questions and recommended solution and identifies the appropriate Maturity Grid.
    2. System displays appropriate Maturity Grid
    3. User clicks next to advance to Maturity Grid Survey  screen.

Maturity Grid Survey Questions
Description	A series of five screens that sequentially presents the five characteristics of the Maturity Grid. 
Data	    - Identified Maturity Grid
Behavior	    1. System displays one characteristic with definitions or examples of how the characteristic is demonstrated by industry peers.
    2. Users subjectively locate their company on a capability maturity continuum for each characteristic according to definitions or examples of how each characteristic is demonstrated by industry peers.
    3. User clicks submit to advance to the next characteristic. Repeat for each characteristic. The submit button for the final characteristic forwards the user to the Maturity Grid Results screen.

Maturity Grid Results
Description	One screen that displays their company's position for all five characteristics on the Maturity Grid. 
Data	    - Maturity Grid
    - User selections of where their company is located on the capability maturity continuum for each characteristic.
Behavior	    1. System displays Maturity Grid transposed with user selections.
    2. System calculates a survey position by adding characteristic weightings for all answers, then dividing the total for each position on the continuum by total possible points. The position on the continuum with the highest percent is designated the "Survey Position".
    3. User clicks next to advance to Competitive Framework Diffusion screen.

Competitive Framework Diffusion Chart
Description	A calculation of diffusion of user selections in the Maturity Grid Survey Questions. The system identifies the location of each answer on the continuum to indicate how unified or dispersed a company may be for all characteristics of the recommended solution. This is the last screen in the Competitive Workflow Stage. When the user clicks the Next button, the system records the user's answers in the database.
Data	    - User selections of where their company is located on the capability maturity continuum for each characteristic.
Behavior	        1. The system processes user's responses and displays the diffusion results.
        2. User clicks next to advance to Financial Workflow Introduction/Transition screen.
Notes	Future version of the tool may superimpose benchmark data on the screen if the user so chooses.  Design for this future now.

Financial Workflow Introduction/Transition
Description	One screen that provides a transition from the Competitive Workflow stage with an introduction and instructions for the Financial Workflow stage. This is the first screen in the Financial Workflow stage.
Data	None
Behavior	    1. User clicks next to advance to Key Performance Indicator (KPI) Input screen.

KPI Input
Description	One screen that identifies the ideal KPI for managing and measuring the recommended business process identified in the Solution Framework.
Data	    - All possible KPIs and formulas for calculating ratio
Behavior	    1. The system displays a KPI input form.
    2. User enters two numbers, which represent the numerator and denominator of the KPI ratio. 
    3. User clicks submit to advance to KPI "As-Is" Position screen.
Notes	Consider displaying benchmark or normative data to assist the user.

KPI "As-Is" Position
Description	One screen that displays the KPI boundaries for each position on the maturity grid continuum, the calculated KPI position determined by data from the KPI Input screen, and the Survey Position determined in the Maturity Grid Results.
Data	    - Identified KPI
    - KPI boundaries for each position on grid-static KPI values based on identified Maturity Grid.
    - KPI position of user's company from KPI Input
    - Survey Position for user's company from Maturity Grid Results.
Behavior	    1. The system processes KPI input values and displays a capability maturity continuum with lower and upper KPI boundaries for each position on the grid, the position of the user's company based on values from the KPI Input screen and the Survey Position for the user's company based on Maturity Grid results.
    2. User clicks next to advance to KPI Change Level screen.

KPI Change Level
Description	One screen that provides risk/return analysis displaying changes in KPI values resulting from increasing risk levels.
Data	    - Current KPI position of user's company based on the values provided from the KPI Input screen.
    - KPI boundaries for next three levels moving up the capability maturity curve from the user's current position.
Behavior	        1. System displays risk/return analysis.
        2. User selects one of three possible risk categories: conservative, normal, and aggressive-each with it's own level of return commensurate with risk level.
        3. User clicks submit to advance to KPI "To-be" Position screen.

KPI "To-be" Position
Description	One screen that displays the KPI boundaries for each position on the maturity grid continuum, the calculated KPI position determined by data from the KPI Input screen, the Survey Position determined in the Maturity Grid Results, and the new "To-be" KPI position based on the user's selection on the KPI Change Level screen. This is the last screen in the Financial Workflow Stage. When the user clicks the Next button, the system records the user's answers in the database.
Data	    - Identified KPI
    - KPI boundaries for each position on grid-static KPI values based on identified Maturity Grid.
    - KPI position of user's company from KPI Input
    - Survey Position for user's company from Maturity Grid Results.
    - "To-be" KPI position of user's company based on the user's selection on the KPI Change Level screen.
Behavior	        1. User clicks next to advance to Case for Action Introduction/Transition screen.

Case for Action Introduction/Transition
Description	This is the first screen in the Case for Action stage. This is the first screen in the Case for Action stage.
Data	None
Behavior	    1. User clicks next to advance to Results-Financial Benefit screen.

Results-Financial Benefit
Description	One screen that displays optimal financial results in operating profit, annual cash flow, and one time cash flow by applying Pools of Storage to the business process identified in the Solution Framework.
Data	    - Identified KPI
    - User data from KPI Input screen
    - Predetermined equations for how changes to KPI affect operating profit, annual cash flow, and one time cash flow.
Behavior	        1. The system calculates and displays changes to operating profit, annual cash flow, and one time cash flow based on changes to KPI from user selection on KPI Change Level screen.
        2. User clicks next to advance to Results-Case for Action screen.

Results-Case for Action
Description	One screen summarizing the Case for Action . displaying the desired "To-be" state and the definitions or examples of how each characteristic is demonstrated by industry peers. Action items for how to attain the desired position. Storage considerations relating action items to Pools of Storage frameworks and storage technologies to support those strategies. This is the last screen in the Case for Action Stage. When the user clicks the Next button, the system records the user's answers in the database.
Data	    - The desired position on the capability maturity continuum, including definitions or examples of how each characteristic is demonstrated by industry peers
    - Action items for attaining the desired position
    - Storage considerations
    - Identified KPI
    - User data from KPI Input screen
    - Predetermined equations for how changes to KPI affect operating profit, annual cash flow, and one time cash flow.
Behavior	        1. The system displays the desired "To-be" state and the definitions or examples of how each characteristic is demonstrated by industry peers.
        2. The system displays a specific set of immediate action plans for the user to undertake to achieve the desired "To-be" state and to be prepared to exploit Maxtor's midline solution(s).
        3. The system will generate a take-away in the form of a PDF or other format for capturing the full set of the user's guided decision visit.
        4. Pools of Storage frameworks and storage technologies to support those strategies.


Appendix B: Gantt Chart





---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | 07-pools-of-storage-functional-spec-597fa5 |
| title | Pools of Storage Decision Tool — Functional Specification (Aberdeen Internal) |
| author | Peter Kastner (executive sponsor); Jay Erikson (primary author) |
| date | 2003-11-26 |
| type | employer-record |
| subject_domain | midline-storage / ILM / software-development / Aberdeen-internal |
| methodology | document-review |
| source_file | 07-Pools-of-Storage-Functional-Spec.txt |
| license | CC-BY-4.0 |

### Abstract

Internal Aberdeen Group functional specification for the Pools of Storage Decision Tool — explicitly marked 'Do Not Share With Maxtor.' Version 1.0 dated November 25 2003 describing a guided decision support web application built in Microsoft ASP/SQL Server 2000 targeting Internet Explorer 5.5+ on Windows. The tool has four stages: Solution Workflow (recommend business process); Competitive Workflow (maturity grid positioning); Financial Framework (KPI analysis); and Case for Action (ROI/TCO calculation with PDF output). Planned development cost $23101.55 over 6 weeks with Aberdeen hosting 3 months.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Primary internal specification document for the most innovative deliverable in the Aberdeen-Maxtor engagement — the first Aberdeen research-delivery-by-simulation tool. Contains frank internal commentary not meant for the client including notes on content development cost control and future product roadmap for superimposing benchmark data. Represents Aberdeen's first attempt at a guided decision support tool for category marketing. |
| **Relevance** | high | The functional specification describes a decision support tool architecture (guided workflow + maturity grid + KPI analysis + Case for Action PDF output) that is recognizable in modern SaaS marketing tools assessment tools and maturity model platforms. The lead generation model (registration gating + rich user data to client) is still the standard model for gated B2B tools. |
| **Prescience** | not-applicable | The functional specification itself makes no market predictions — it is a software requirements document. The forward-looking innovation is the product concept itself (research-as-simulation). Prescience of the broader decision tool concept is addressed in File 6 (After-Action) observations. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (11)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | acquired | Aberdeen/Harte-Hanks |
| Peter S. Kastner | person | active | [none] |
| Stan Elbaum | person | unknown [REVIEW] |  |
| David Hill | person | unknown [REVIEW] |  |
| John Boyne | person | unknown [REVIEW] |  |
| Jay Erikson | person | unknown [REVIEW] |  |
| Michael Beganny | person | unknown [REVIEW] |  |
| John McLaughlin | person | unknown [REVIEW] |  |
| Kerri Conrad | person | unknown [REVIEW] |  |
| Beth Conant | person | unknown [REVIEW] |  |
| Maxtor Corporation | company | unknown [REVIEW] |  |

### Technologies Referenced (6)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Microsoft Active Server Pages (ASP) | framework | Microsoft | mature | legacy |
| Microsoft SQL Server 2000 | platform | Microsoft | mature | legacy |
| Windows 2000 Server | platform | Microsoft | mature | legacy |
| Internet Explorer 5.5+ | platform | Microsoft | mature | discontinued |
| Pools of Storage Decision Tool | application | Aberdeen Group / Maxtor | in-development | historical |
| Aberdeen Maturity Grid Framework | framework | Aberdeen Group | emerging | active |

### Observation Summary

- Total observations: 20
- By type: employer-record: 20
