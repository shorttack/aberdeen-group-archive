# An Overview of Internet Application Development (CA Sales Training June 1996)

> Archived from: INTERN~1.odp
> Original publication date: 1996-06-01
> Author: Peter S. Kastner

---

## Original Document Text

===== FILE: INTERN~1.odp =====
--- Slide/Page 1 ---
AberdeenGroup
1
An Overview of Internet
Application Development
Computer Associates Sales Training  -- 
June 1996
Peter S. Kastner
Vice President
Aberdeen Group, Inc.
One Boston Place
Boston, MA 02108
617/723/7890
Copyright Aberdeen Group - 1996


--- Slide/Page 2 ---
AberdeenGroup
2
Internet/Intranet Components
“Thin Client” Web Browser (e.g., NetScape)
WAN or LAN using TCP/IP Protocol
HyperText Transport Protocol (HTTP) server
Common Gateway Interface (CGI) scripts 
Firewall: ensure privacy of enterprise network
Application RDBMS
IBM Compatible
Mac Classic
Cloud
Firewall
Public Switch
Mainframe
Data
Router
Web
Server
Optional


--- Slide/Page 3 ---
AberdeenGroup
3
Client-Server vs. Internet Apps
Client-Server
Application runs on the desktop
Data is brought from the server to the desktop and displayed
Lots of session-oriented computing (e.g., OLTP)
Internet
Application runs on a server(s)
Presentation display is done by the client’s browser
No concept of a “session”
IBM Compatible
Mac Classic
Cloud
Firewall
Public Switch
Mainframe
Data
Router
Web
Server


--- Slide/Page 4 ---
AberdeenGroup
4
Current Internet Tools
Web / Browser
Common Gateway Interface (CGI)
Mail
FTP (File Transfer Protocol)
News Groups
Many Other Dinosaurs


--- Slide/Page 5 ---
AberdeenGroup
5
Web Browser Components
GUI presentation of text and graphics to end user
Interpret HTML into presentation components
Manage user navigation via links (i.e., Uniform Record 
Locators -- URLs -- such as http://www.blyth.com)
Keep track of users’ favorite URLs (e.g., bookmarks)
TCP/IP communications interface
Other functions
Internet News reading and posting
Internet e-mail
Proprietary add-ins like Java, RealAudio
So where is the transaction, business logic, and database?


--- Slide/Page 6 ---
AberdeenGroup
6
Why Have Applications Using 
Browsers?
Advantages: “Client for the Masses”
Low cost or no-cost
Multi-platform
“Thin client” = minimal configuration desktop
Disadvantages Today: “Not Baked”
Woefully simple user interface (today)
Lack of useful add-in standards (e.g., compatibility)
Security is lacking
Immaturity of development environments
No ties to desktop productivity apps (e.g., MS Office, 
Omnis DBMS)


--- Slide/Page 7 ---
AberdeenGroup
7
Web Browser Choices
Browsers are essentially free, but ...
Netscape sets the Web standards
HTTP
Secure-HTTP
Secure Sockets Layer
Java run-time engine
Mail
Groupware with Collabra acquisition
Credit Card Processing
with Mastercard, Visa, AMEX
Clearing House Relationships


--- Slide/Page 8 ---
AberdeenGroup
8
Internet Browsers Become Just 
Another Client
Client-server applications will not go away!
Aberdeen tells users to demand tools that 
automatically deploy to both clients and Internet 
browsers


--- Slide/Page 9 ---
AberdeenGroup
9
What is Java?
The emerging, de facto standard language for 
applications that run over the Internet
Developed by Sun Microsystems; licensed to most 
of the industry players (including Blyth)
A C++-based programming language for down-
loadable Browser applets
HTML request loads Applet from WebServer
Runtime executes the Applet
Java can also execute on the server 
Portable across many operating environments


--- Slide/Page 10 ---
AberdeenGroup
10
Resist the Siren-song of Java
Java is C++ without the hand grenades
Java is immature, will change dramatically over time
Browsers will change faster than any other piece of 
software
Beware of transaction processing
Where are the controls, auditability, security?
Conclusion:  most commercial apps are better off 
crafted from a powerful 4GL (e.g., OMNIS)


--- Slide/Page 11 ---
AberdeenGroup
11
Java Programming is 
Problematic Today
Sole-source from Sun Microsystems
Few deployment platforms; fewer development platforms; one 
3rd-party debugger
NO database access -- spec is not even out yet!
Lots of gotcha’s -- Truly immature
No Dates before January 1, 1970
No fixed decimal arithmetic (e.g., dollars and cents)
Limited print formatting
No multiple inheritance
Requires multi-threading -- not in DOS or Mac OS
No structures;  limited, byte-oriented I/O
Applet can only talk to its Mother’s Internet address
Weekly bug-fix releases


--- Slide/Page 12 ---
AberdeenGroup
12
Client-Server Has Advantages
Business Logic:  client-side, server-side or both
Data:  local or server-based databases -- or both
Presentation: Text, forms, windows -- whatever style 
is most ergonomic
Menus:  Logical organization of functions
Transactions and sessions are supported
Decision support
Systems management
Deployment
Security
etc.


--- Slide/Page 13 ---
AberdeenGroup
13
The Future of Commerce is the 
Internet
http://www.aberdeen.com


--- Slide/Page 14 ---
AberdeenGroup
14
Why Commerce
Not just for the money
Not just for marketing
Not just for sales
Fundamentally change your business !


--- Slide/Page 15 ---
AberdeenGroup
15
Opportunity & Growth
Internet commerce is growing at 400% per year
Worldwide sales of goods and services traded over 
the Internet will increase from $70 million in   1995 
to $250 billion in 2000, a compounded growth rate 
of over 400%


--- Slide/Page 16 ---
AberdeenGroup
16
Adoption Curve of
Fortune 2000
Business Change 
Communications Medium
E-mail 
Internet ?
Static Web Site
Active Web Site
New Markets &
                 Approaches
Not Connected
1996 State of the Market


--- Slide/Page 17 ---
AberdeenGroup
17
Corporate Internet Planning 
Today
Internet -- the World Wide Web (WWW)
Web for corporate presence
Web for marketing collateral
Web for publishing publicly available information
Cisco saves 25,000 support telephone calls a month
Intranet -- An intra-company Internet
Making enterprise information available to everybody who needs 
it via HTML publishing (instead of classic C-S app)
Human Resources
401K allocations
Universal desktop via Browser
Electronic mail


--- Slide/Page 18 ---
AberdeenGroup
18
Companies must leverage what they have:
HR
Mftg
Actg
Orders
Web Server
Any Web
Browser
Internet/
    Intranet
Intranet Leverage


--- Slide/Page 19 ---
AberdeenGroup
19
Internet Commerce Today
Catalogs / Malls (Web)
  5%
Marketing Material (Web)
85%
Franchise Building (Free Software)
10%
Simple Communications (e-mail)
95%
Electronic Data Interchange
  1%
Source: Aberdeen Group 1996
Business Process
% of Active Companies
(can do more than one)


--- Slide/Page 20 ---
AberdeenGroup
20
Key Differences
Client-Server Application
Mission-Critical
Serious applications that run 
the business
Architecture choices (i.e., 2-
Tier, 3-Tier)
Lots of databases and DB 
work
IT understands C-S basics 
and limitations
Internet Application
Extended Enterprise-wide
Trivial applications (but useful 
to many)
WebServer-to-lightweight 
Browser limits today
What’s a database?
IT novices in an immature 
environment


--- Slide/Page 21 ---
AberdeenGroup
21
Conclusions
Internet growth and impact is incredible
Internet can change business fundamentals
If you don’t  take the initiative -- your competitors will
The technology today is far from perfect --but it works!
CA has a clear vision for enhancing Unicenter and 
introducing Jasmine






---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | ca-internet-app-dev-sales-training-1996-48db9c |
| title | An Overview of Internet Application Development (CA Sales Training June 1996) |
| author | Peter S. Kastner |
| date | 1996-06-01 |
| type | employer-record |
| subject_domain | employer/aberdeen-group |
| methodology | industry-analysis, executive-presentation, sales-force-education |
| source_file | INTERN~1.odp |
| license | CC-BY-4.0 |

### Abstract

'An Overview of Internet Application Development' — Peter S. Kastner presentation to Computer Associates Sales Training, June 1996. Introduces the Internet/intranet stack (thin-client browser, TCP/IP, HTTP, CGI, firewall, RDBMS) and contrasts Internet applications with traditional client-server. Early canonical analyst framing of the Web as an application-delivery platform delivered to a CA sales audience in the Netscape-dominant pre-IE3 era.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Early (June 1996) analyst framing of Internet application development for a major enterprise-software sales force, delivered at the inflection point between client-server and Web architectures. |
| **Relevance** | medium | Content is foundational-education material; architectural contrasts remain interesting as a period piece. |
| **Prescience** | high | Kastner's 1996 framing of Web apps ('runs on a server(s); presentation by client browser; no session') turned out to be the dominant enterprise-application architecture within five years; his 'no concept of a session' framing foreshadowed the later shift to stateless REST. |

### Prescience Detail


**Prediction 1:** Thin-client dominance over time
- **Claimed:** Thin-client Web browser as presentation layer enables application architecture that runs on servers and presents via browser — foundational framing for the next decade of enterprise apps.
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 1:** Web-app architecture outcome
- **Result:** Web application architecture (server-side app + browser presentation) became the dominant enterprise-app architecture by ~2001 and remains so. Kastner prediction verified.
- **Confidence:** verified
- **Notes:** 

**Prediction 2:** CGI as interim scripting
- **Claimed:** CGI positioned as current server-side scripting standard; implicitly foreshadows need for richer application servers.
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 2:** CGI outcome
- **Result:** CGI was displaced by application servers (Java EE, PHP, Rails, Node, etc.) within a decade; Kastner's implicit pointer to limitations of raw CGI was correct.
- **Confidence:** verified
- **Notes:** 


### Entities Referenced (4)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Peter S. Kastner | person | active |  |
| Aberdeen Group | company | acquired-by-harte-hanks | Harte-Hanks (2007) |
| Computer Associates International, Inc. | company | renamed | CA Technologies (2006) -> Broadcom (2018) |
| Netscape Communications | company | acquired-dissolved | AOL (1999) -> brand retired |

### Technologies Referenced (6)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| HTTP (HyperText Transport Protocol) | protocol | IETF | emerging | mature |
| Common Gateway Interface (CGI) | framework | NCSA | emerging | obsolete |
| TCP/IP | protocol | IETF | mainstream | mature |
| Client-Server Architecture | framework | multiple | mainstream | displaced-by-web |
| Enterprise Firewall | platform | multiple | emerging | mature |
| Web Browser (thin client) | platform | Netscape/Microsoft | emerging | mature |

### Observation Summary

- Total observations: 10
- By type: actual-outcome: 3, viability-prediction: 2, framework-component: 1, comparative-analysis: 1, market-position: 1, role-definition: 1, employer-record: 1
