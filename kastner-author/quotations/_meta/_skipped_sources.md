# Skipped Sources Log

Sources reviewed but not ingested into `kastner_quotes_clean.csv` or as archival studies. Logged for future recovery if the underlying full text becomes available.

## Gated whitepapers (abstract-only landing pages)

### GRIC / Aberdeen "Take Control of Remote Access Costs"
- **Title**: Aberdeen Group: GRIC is Unifying Secure Remote Access Services
- **Author**: Peter S. Kastner, Executive Vice President and Chief Research Officer, Aberdeen Group
- **Date published**: 2003-09-01
- **Source URL**: http://searchnetworking.techtarget.com/whitepaperPage/0,293857,sid7_gci928522,00.html
- **Source archive**: `batch_20260419_quotes4/08_Aberdeen-Group-GRIC-is-Unifying-Secure-Remote-Access-Service.webarchive`
- **Reason skipped**: TechTarget lead-gen landing page — full whitepaper gated behind registration form. Only the title, date, abstract teaser, and Kastner author bio are on the page. No Kastner quotation text is available to extract, and there is insufficient content for an archival study package.
- **Recovery hint**: Check Wayback Machine for `searchnetworking.techtarget.com/whitepaperPage/0,293857,sid7_gci928522,00.html` or for any Aberdeen Group press archive of the GRIC whitepaper PDF. If the full PDF is recovered, ingest as a Kastner-authored archival study under `kastner-author/` with study type `white-paper`.
- **Abstract teaser (verbatim from landing page)**: "Free Aberdeen White Paper: TAKE CONTROL OF REMOTE ACCESS COSTS. Computer users outside of the firewall are definitely not well under control. On any given day, over 30% of U.S. knowledge workers are not in the home office and not behind the enterprise firewall's security. Telecommunications costs by these workers are going through the roof, yet are often hidden due to overlapping telecommunications services and service providers employed by most enterprises. Find out how to control and reduce remote access costs by 50% while improving remote productivity in this new Aberdeen whitepaper."
- **Batch**: Batch 4 (2026-04-19), file 08 of 10

---

## Machine-translated republications

### Massachusetts Attorney Lawyer (attorney2massachusetts.com) rebates article
- **Title**: Account customers discounts on technology for saving Trip often Fine Print
- **Source URL**: http://attorney2massachusetts.com/account-customers-discounts-on-technology-for-saving-trip-often-fine-print/
- **Source archive**: `batch_20260419_quotes5/04_Account-fine-print.webarchive`
- **Reason skipped**: Clearly a machine-translated republication of an English-language original (most likely a Boston Globe / Dallas Morning News rebates article from ~2003-2004). The text is heavily garbled ("More than 40 percent of consumers has never taken off exchange"), rendering any direct quote extraction unreliable. The same underlying Kastner rebate statistic (~40% never redeem) is already captured verbatim in the CSV at **row 296 (seq 146) Dallas Morning News 2003-07-03 'Rebate offers create fans, critics' by Doug Bedell** and would duplicate that row if re-extracted here. Of secondary note: this MT article attributes Kastner to 'Vericours, Inc.' (his post-Aberdeen consultancy) as well as to Aberdeen, suggesting the original source is likely a 2005+ article; however the mangled text cannot be reliably reconstructed.
- **Recovery hint**: Search for the original English article by keyword "Kastner Vericours 40 percent rebates never honored" on Boston Globe, Worcester T&G, or Dallas Morning News archives. A clean find would justify a new row and seq.
- **Batch**: Batch 5 (2026-04-19), file 04 of 10

---
