# Opteron's First Year All About Linux - But What About Later?

> Archived from: LinuxPlanet-Reports-Opteron-s-First-Year-All-About-Linux-But-What-About-Later-6.webarchive
> Original publication date: 2004-04-01
> Author: LinuxPlanet staff (reporter); Peter Kastner and Tom Halfhill (quoted sources)

---

## Original Document Text

SOURCE_URL: http://www.linuxplanet.com/linuxplanet/reports/5366/1/
MIME: text/html

LinuxPlanet - Reports - Opteron's First Year All About Linux - But What About Later? > IT internet.com/IT internet.com/CIO internet.com/Security internet.com/Networking internet.com/Storage CIO Update Database Journal Datamation Enterprise IT Planet Enterprise Networking Planet Enterprise Storage Forum eSecurity Planet Hardware Central Intranet Journal ISP Planet ITSMwatch IT Channel Planet Linux Planet ServerWatch VoIP Planet Wi-Fi Planet WinDrivers.com Network Map > Developer internet.com/Developer 15 Seconds 4GuysFromRolla.com ASP101 CodeGuru Developer.com DevX FlashKit.com Gamelan JARS JavaScript.com JavaScriptSource PHPBuilder.com ScriptSearch SharePoint Briefing VB Forums VB Wire Web3Beat WebDeveloper.com Webreference Network Map > News Internetnews.com Linux Today Network Map > Small Business Ecommerce Guide SmallBusinessComputing Webopedia WinPlanet Network Map > Personal Tech BlackBerryToday iPhoneGuide Jumbo Palm Boulevard PDAStreet PocketPCWire SharkyExtreme Smart Phone Today The List: ISPs Wi-FiHotSpotList WindowsMobileToday Network Map Events Freelance Jobs Partners > Solutions eBooks HotList Video Shop > Login Manage My Profile > Register Why Join? Home | Hardware | Internet News | Web Hosting | IT Management | Network Storage Search Power Search | Tips Front Door Discussion Interviews --> LinuxEngine Opinions Previews --> Reports Reviews Tutorials News Technology Jobs Browse by subject . Free Newsletter Linux Planet Linux Today More Free Newsletters END: MARCHEX --> Be a Commerce Partner Imprinted Promotions Colocation PDA Phones & Cases Premium Bandwidth Cell Phones Auto Insurance Quote Promote Your Website IP Services Web Design Logo Design Desktop Computers Dedicated Servers Online Universities Phone Cards internet.com IT Developer Internet News Small Business Personal Technology International --> Search internet.com Advertise Corporate Info Newsletters Tech Jobs E-mail Offers Build Hardware with Windows 7: Partners can unlock new value with a collection of new features introduced in Windows 7 that improve how users discover and interact with applications and devices connected to their PC. LinuxPlanet / Reports MARKETPLACE New Exclusive HP Rebates SYNNEX offers incredible discounts on HP desktop parts. Learn more now! www.SYNNEX.com DOWNLOAD the Windows 7 Release Candidate Test Windows 7 in your real environment. Discover the best tools and guidance. www.microsoft.com/springboard Download a Windows® Embedded Trial Get Connected Devices Faster to Market with Windows® Embedded. FREE TRIAL! Microsoft.com/WindowsEmbedded REPORT BUSINESS SOFTWARE PIRACY - REWARD Anonymously Report Piracy at your current/former Company and get a $1 Million reward! Help Stop Software Piracy with BSA. Advertise Here Opteron's First Year All About Linux But What About Later? Jacqueline Emigh Wednesday, April 28, 2004 10:49:07 AM "Opteron's first year has been all about Linux," said Christopher Rimer, an exec in AMD's Infrastructure Enablement Group. Over time, though, industry experts expect 64-bit x86 implementations from AMD and Intel to gravitate much more towards Microsoft Windows, without leaving Linux behind, either. Last week, AMD marked the first anniversary of its Opteron chip by joining the OSDL. Meanwhile, Hewlett-Packard, one of AMD's OEM partners, released two more systems capable of running either Linux or Windows. "It's my job to promote use of the Opteron chip across all operating environments, including open source along with proprietary systems," acknowledged AMD's Rimer in an interview last week. When the Opteron was first announced a year ago, multiple Linux distributions -- including SuSE Linux Enterprise Server (SLES) and TurboLinux -- had already been enabled with support for the new chip. "MandrakeSoft was almost there, and Red Hat was in beta with Opteron," according to Rimer, whose official title at AMD is senior alliance manager, ISV Infrastructure Alliances. "Over the past year, about 90 percent of Opteron's sales have been for Linux systems," he added. The two newly released Opteron-based systems from HP include LC 3000 clusters and the ProLiant DL 585 64-bit server. The LC 3000 clusters use the Opteron-based ProLiant DL 145 server, a platform first released in February. All of these ProLiant systems are able to run either Linux or Windows. Initially, though, about 85 to 90 percent of DL 585 sales will go to Linux users, estimated Steve Cumings, HP's group manager for ISS platform systems marketing, in another interview. "And we expect that upwards of 50 percent of (early) LC 3000 customers will be using Linux," according to Cumings. Cumings said that the DL 585 now has two main markets: high performance scientific apps, such as fluid dynamics and weather simulation; and financial brokerages. On the other hand, HP plans to sell the LC 3000 clusters "into all the industries -- government, finance, anyone who needs additional processing power," he maintained. The LC 3000 clusters are designed for "32-bit performance scalable to 64-bit environments," according to Cumings. HP also offers two series of lower-end IA-32 clusters, each based on Intel's 32-bit Xeon processor: LC 1000 clusters, made up of ProLiant DL140 servers; and LC 2000 clusters, using ProLiant DL360 servers. Despite the combined Linux and Windows support in the ProLiant series, however, HP has no intentions of porting its own proprietary HP-UX OS to Proliant, Cumings said. Sun Microsystems, another major OEM partner, is using the Opteron as the basis for servers able to run either Linux or Solaris. Meanwhile, however, HP's high-end, Intel-based Itanium 2 servers are running HP-UX and Windows Server 2003, with Linux and "OpenVMS on HP Integrity servers" to be added in the future, according to information posted on HP's Web site. Cumings contended during the interview that the Intel-based Itanium is "a pure 64-bit environment," with advantages that include support for up to 128 processors; the EPIC parallel architecture; a very large cache size; and higher availability. Beyond the popularity of the 64-bit AMD platform with Linux early adopters, industry analysts are finding AMD to be way ahead of Intel on 64-bit x86 technical development. "Although AMD has in the past introduced some innovations to the x86 architecture -- the 3DNow multimedia extensions being a prime example -- this is the first time AMD has truly steered the direction of the world's most important microprocessor architecture, which Intel invented and has kept closely guarded for 26 years," wrote Tom R. Halfhill, an analyst at In-Stat MDR, in a recent report. In an interview, Halhfill maintained that Intel had to reverse-engineer AMD's 64-bit chip in order to develop its own 64-bit extensions. "There's nothing illegal or unethical about reverse-engineering," Halfhill said. It's customary, though, for AMD to reverse engineer Intel's chips, instead of the other way around, he added. Intel came to the 64-bit x86 party later than Intel, Halfhill explained. "With the introduction of the Itanium, Intel decided to take 64-bit processing in a different direction. AMD is legally prohibited from cloning the Itanium, so they set about developing 64-bit extensions for the x86 platform. It's my understanding that Microsoft later said, 'Okay. We're going to do an implementation of Windows for x86.' By then, though, there wasn't time for Intel to develop from scratch." Halfhill noted that, in analyzing the 64-bit implementations of AMD and Intel, he discovered two instructions in AMD that don't appear in Intel's 64-bit Xeon. These instructions, known as LAHF and SAHF, are aimed at promoting multitasking efficiency by saving and restoring flags in the OS, he said. "AMD wasn't going to include these two instructions, but then changed its mind midway through," according to the analyst. Consequently, the two instructions don't appear in the AMD64 chips already released, but they will be included in AMD's upcoming 64-bit processors. OS compatibility won't be affected, but applications won't necessarily be able to run across mixed AMD and Intel 64-bit platforms unless programmers decide not to use the new AMD instructions, Halfhill said. Ultimately, though, Intel will probably incorporate the two instructions, too, he predicted. Analysts also assert that the balance of 64-bit x86 implementations will veer immensely toward Windows eventually. "64-bit (x86) is probably selling best right now in the scientific/technical space," said Peter Kastner, an analyst at the Aberdeen Group. "AMD is a big fish in the 64-bit pond, but this is a pond made up right now of only a few thousand enthusiasts," according to the analyst. Halfhill, however, foresees the possibility that when 64-bit x86 processors become entrenched, Linux might keep somewhat more than its customary 5 to 10 percent market share. Essentially, he said, that's because 64-bit x86 processors will be used to run the types of server applications that tend to popular among Linux networking fans. <SCRIPT language='JavaScript1.1' SRC="http://ad.doubleclick.net/adj/N5620.295.1877812604421/B3542751.7;abr=!ie;sz=728x90;click0=http://mjxads.internet.com/RealMedia/ads/click_lx.ads/intm/it/www.linuxplanet.com/linuxplanet/reports/5366/1/index/L7/536011308/468x60-2/WMBrands/VWire_Q209_1b/vwireq209leo.html/595645704d456d504744414141706247?;ord=536011308?"> </SCRIPT> <NOSCRIPT> <A HREF="http://mjxads.internet.com/RealMedia/ads/click_lx.ads/intm/it/www.linuxplanet.com/linuxplanet/reports/5366/1/index/L7/536011308/468x60-2/WMBrands/VWire_Q209_1b/vwireq209leo.html/595645704d456d504744414141706247?http://ad.doubleclick.net/jump/N5620.295.1877812604421/B3542751.7;abr=!ie4;abr=!ie5;sz=728x90;ord=536011308?"> <IMG SRC="http://ad.doubleclick.net/ad/N5620.295.1877812604421/B3542751.7;abr=!ie4;abr=!ie5;sz=728x90;ord=536011308?" BORDER=0 WIDTH=728 HEIGHT=90 ALT="Click Here"></A> </NOSCRIPT> Linux is a trademark of Linus Torvalds. home | search | help! | about us Search: Jupitermedia Corporation has two divisions: Jupiterimages and JupiterOnlineMedia Jupitermedia Corporate Info Copyright 2009 Jupitermedia Corporation All Rights Reserved. Legal Notices , Licensing , Reprints , & Permissions , Privacy Policy . Web Hosting | Newsletters | Tech Jobs | Shopping | E-mail Offers

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | linuxplanet-reports-opteron-s-first-year-40c423 |
| title | Opteron's First Year All About Linux - But What About Later? |
| author | LinuxPlanet staff (reporter); Peter Kastner and Tom Halfhill (quoted sources) |
| date | 2004-04-01 |
| type | press-article |
| subject_domain | amd64-linux-adoption |
| methodology | press-coverage, expert-opinion, competitive-profiling |
| source_file | LinuxPlanet-Reports-Opteron-s-First-Year-All-About-Linux-But-What-About-Later-6.webarchive |
| license | CC-BY-4.0 |

### Abstract

LinuxPlanet feature assessing AMD Opteron's first year in market. Peter Kastner of Aberdeen Group characterizes Opteron as strong in scientific/technical Linux workloads but as 'a pond of only a few thousand enthusiasts'; Tom Halfhill counters that once 64-bit x86 is entrenched, Linux may retain a larger mindshare than Windows on the platform. Article maps near-term Opteron/Linux coupling and longer-term Windows x86-64 threat.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Early-deployment snapshot of AMD64/Opteron adoption before Intel's EM64T response, with Kastner sizing the 2004 addressable base as small and Linux-skewed. |
| **Relevance** | low | x86-64 is now universal; article is historical. Useful as a data point on how analysts sized early AMD64 demand. |
| **Prescience** | high | Kastner's framing — small early enthusiast pond now, mainstream Windows adoption to follow — tracked with subsequent reality: Intel released EM64T in 2004-2005, Windows x64 shipped in 2005, and x86-64 reached mainstream parity on Windows within two years. |

### Prescience Detail


**Prediction 1:** OS share trajectory on x86-64
- **Claimed:** Windows likely to dominate x86-64 once mainstream, though Linux may retain higher share than on 32-bit
- **Year:** 2004
- **Confidence at time:** medium

**Actual Outcome 1:** Intel's x86-64 response timing
- **Result:** Intel shipped EM64T (64-bit extension) in Xeon/Pentium 4 in 2004-2005; Windows x64 Edition shipped April 2005
- **Confidence:** verified
- **Notes:** Validates Kastner trajectory


### Entities Referenced (6)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | dissolved | Harte-Hanks -> (brand defunct 2020s) |
| Peter S. Kastner | person | active |  |
| Advanced Micro Devices (AMD) | company | active |  |
| Intel Corporation | company | active |  |
| Microsoft Corporation | company | active |  |
| Tom R. Halfhill | person | active |  |

### Technologies Referenced (3)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| AMD Opteron | platform | AMD | emerging | legacy-superseded |
| AMD64 / x86-64 | platform | AMD | emerging | mature-ubiquitous |
| Linux | platform | community/Linus Torvalds | maturing | dominant-server |

### Observation Summary

- Total observations: 4
- By type: market-data: 2, viability-prediction: 1, actual-outcome: 1
