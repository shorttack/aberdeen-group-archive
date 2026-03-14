# Reconciling Client/Server Development and the Internet
> Archived from: https://web.archive.org/web/19971007163600/http://www.aberdeen.com:80/secure/impacts/3com/3com2.htm
> Original publication date: November 1996
> Author: Aberdeen Group (Tim Sloane)

---

## Original Document Text

**November 1996**

**Reconciling Client/Server Development and the Internet**

Corporations have made huge investments in Client/Server development, and are now wrestling with how these investments can be reconciled with the need to deploy Internet-based solutions. But in their rush to adopt everything Internet, many IS managers are creating "clean slate" projects using single-purpose Internet development tools. While in some instances this may be appropriate, Aberdeen research has shown that investments in pure Internet development tools are often short-sighted, duplicating development efforts already near completion, or even already deployed internally. The long-term cost implications are enormous. As is typical in any complex technology environment, deriving the "right answer" is only possible if the right questions are asked. The purpose of this Aberdeen Group report is to help IS professionals develop appropriate questions.

**Will the company deploy applications, or just data access?**

To really benefit from the connectivity the Internet provides, companies must offer their business partners and customers access to appropriate corporate information, not just republished, static data. Indeed, this trend is fast becoming a competitive imperative, as enterprises jockey for market share by offering information services to customers and partners via the Internet. Less common, but more compelling, is to distribute applications to customers that streamlines their operations, offering them knowledge your company has, while tightly coupling them to your systems and organization.

The Internet is ideal for publishing parts lists, catalogs, and product literature because pictures and explanatory graphics are a large part of the information content. Likewise, the Internet or an intranet is an ideal way to allow users to launch pre-defined queries against dynamic operational databases — applications that range from product selection criteria in 'Net orders to employee-driven Human Resource questions, and can even support simple OLTP.

Right now, 'Net applications are best suited where a simple Browser interface can request data for direct viewing, printing, and perhaps forwarding via e-mail. Client-server applications are still the best model where complex data analysis (e.g., OLAP) is needed; where the data retrieved must be further massaged and stored in other PC-based applications such as spread sheets or personal databases; where a sophisticated, windowed user interface makes sense (i.e., complex order entry); and, where distributed desktop/laptop databases must be synchronized (e.g., route sales and inventory management).

Excitingly, hybrid client-server/'Net applications are opening up new, labor-saving opportunities by retrieving free information off the Internet and incorporating it into a client-server application. Examples include on-line Yellow Pages, parcel tracking data, and zip+4 addresses from the Postal Service that lower shipping costs. Future best-of-breed applications will blend the ergonomics of the client-server model with the wealth of free data available from cyberspace.

**What is the Application Environment, Location, and Style?**

The nature of the applications that companies deploy will have a major bearing on system architecture. The Web browser is the 1990s 'client for the masses'. It provides the broadest access to the application, and implies that the application is executed on a centralized server (although it could also be executed as a browser Plug-in or Java applet in some combination). This solution nicely leverages current client/server development tools because most client/server tool vendors have enhanced their products to output HTML, which drives the Web browser. And since the Web browser supports a rich set of graphics, including tables, charts, full motion video, audio, or 3D models, almost any visualization methodology can be widely and easily deployed. Moreover, many suppliers are moving away from inefficient Common Gateway Interface scripts towards sophisticated Web-server-to-application-server partitioning.

On the other hand, client-server applications are better suited where data is frequently added, deleted, and updated under the user's control, as in on-line order entry. The concept of "sessions" is intrinsic to client-server, and many OLTP applications that involve updating multiple database tables in sequence cannot be easily done with browser/web-server technology.

Client-server developers should "do lunch" with their enterprises' Web Masters. These developers are likely to expand their technology horizons to include 'Net technology. 'Net applications presume a TCP/IP common-ground that opens doors particularly to suppliers – Electronic Data Interchange will become commonplace over the next 5 years. 'Net electronic mail, especially e-mail generated by an application, provides an inexpensive form of workflow and exception reporting. Free 'Net data sources can add customer demographic information that can add enormous value to a decision-support data mart. And publishing customer-support databases can allow customers to answer their own questions any time, from anywhere.

**Is a transition strategy possible that will leverage current assets and experience?**

Yes! Aberdeen Group firmly believes that 'Net commercial applications ought to be built with Web-enabled versions of today's client-server development environments. Quite simply, users need to let the development-tool suppliers do the complex work in a fast-changing world. The alternative of a dual c-s and 'Net tool strategy is long-term IS-labor cost-prohibitive. And new-breed tools built around Java are stuck with the current limitations of the Java language and class libraries, and are just not suited for complex transaction processing today.

Smart IT development managers should beware the tendency towards tool proliferation, particularly now, when 'Net development seems suddenly important. Aberdeen Group believes that rather than thinking of client-server development tools as last generation, buyers should carefully consider the many benefits of a single-tool strategy, and look anew at the best-of-breed client-server tool suppliers.

— Tim Sloane

---

AberdeenGroup, Inc.
One Boston Place, Boston, Massachusetts 02108 USA
Tel: 617.723.7890 | Fax: 617.723.7897

Copyright © 1996 Aberdeen Group, Inc., Boston, Massachusetts
This Document is for Electronic Distribution Only — REPRODUCTION PROHIBITED

---

## Frictionless Data Package Metadata
> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-3com-reconciling-clientserver-development-internet |
| title | Reconciling Client/Server Development and the Internet |
| author | Aberdeen Group |
| date | November 1996 |
| type | impact-report |
| subject_domain | client/server computing / Internet development strategy |
| methodology | analyst-commentary |
| sponsor | 3Com Corporation |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group impact report examining how corporations should reconcile existing client/server development investments with emerging Internet-based application deployment. Authored by analyst Tim Sloane, it argues against dual-tool strategies and advocates for Web-enabled client/server tools rather than pure Internet or Java-based approaches. Sponsored by 3Com.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | medium | Captures the 1996 inflection point in enterprise IT architecture as the Web disrupted client/server paradigms. The 3Com sponsorship is notable. |
| Relevance | high | Directly relevant to enterprise application architecture evolution; the investment-protection vs. new-platform debate recurs in every major technology transition. |
| Prescience | high | Core prediction that Web-enabled CS tools would prevail over dual-tool and Java-only strategies proved accurate. EDI-over-Internet prediction confirmed within 5 years. App-server architecture prediction confirmed. |

### Prescience Detail

| Prediction (November 1996) | Outcome (Verified) |
|----------------------------|--------------------|
| EDI will become commonplace over the Internet within 5 years | Confirmed: AS2 standardized in 2002; Internet-based EDI became mainstream |
| Java not suited for complex transaction processing in 1996 | Confirmed for era: J2EE addressed this by 1999–2001 |
| Suppliers moving from CGI to app-server partitioning | Confirmed: WebSphere, Tomcat, JBoss, IIS displaced CGI by 2000 |
| Web-enabled CS tools are the right path (single-tool strategy) | Partially confirmed: Web-enabled CS tools did evolve; but new web frameworks also proliferated (ASP.NET, Spring, Rails) |
| Browser = 'client for the masses'; server-centric execution | Confirmed: Modern SaaS is exactly this model |

### Entities Referenced

| entity_id | entity_name | type | status |
|-----------|-------------|------|--------|
| 3COM | 3Com Corporation | vendor | acquired by HP 2010; integrated into HPE Aruba |
| ABERDEEN-GROUP | Aberdeen Group | analyst-firm | active |
| TIM-SLOANE | Tim Sloane (analyst) | person | unknown |

### Technologies Referenced

| tech_id | tech_name | lifecycle_at_study | lifecycle_current |
|---------|-----------|-------------------|-------------------|
| CLIENT-SERVER | Client/Server Computing | mature | legacy |
| WEB-BROWSER | Web Browser (HTML) | growth | mature |
| JAVA | Java Language | emerging | mature |
| CGI | Common Gateway Interface | growth | legacy |
| OLAP | Online Analytical Processing | growth | mature |
| OLTP | Online Transaction Processing | mature | mature |
| EDI | Electronic Data Interchange | mature | legacy |
| INTRANET | Corporate Intranet | emerging | mature |
| WEB-CS-TOOLS | Web-Enabled CS Dev Tools | growth | legacy |
| APP-SERVER | App Server Architecture | emerging | mature |

### Observation Summary

| observation_type | count |
|-----------------|-------|
| strategy-classification | 2 |
| viability-prediction | 4 |
| actual-outcome | 4 |
| technology-assessment | 7 |
| market-data | 1 |
| expert-opinion | 7 |
| **Total** | **25** |
