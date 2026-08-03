# 🛡️ Pi-hole Blocklist Catalog (August 2026)
## High-Quality, Actively Maintained DNS Blocklists for Pi-hole v6+

This catalogue provides a curated, actively maintained collection of DNS blocklists used to block **ads**, **tracking**, **malware**, **phishing**, **telemetry**, **scams**, **ransomware**, **cryptomining**, and **suspicious domains**.

All blocklists listed here are intended to be:

- Pi-hole v6+ compatible (hosts or domain lists)
- Served via HTTPS
- Actively maintained (updated within ~12–18 months)
- Trusted within the security & privacy community
- Screened for low false positives (unless explicitly noted)

---

## 📅 Changes This Month (August 2026)

### ✅ Added

| Name | URL | Categories | Why Added | Suggested Use |
|-----|-----|------------|-----------|---------------|
| HaGeZi Windows/Office Tracker 🆕 | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/native.winoffice.txt) | telemetry, tracking | Actively maintained Windows and Microsoft Office telemetry list that replaces the stale RPiList Win10 Telemetry list. | Windows-heavy networks; deploy through a dedicated Pi-hole group |

### ❌ Removed

| Name | URL | Categories | Why Removed | Suggested Replacement |
|-----|-----|------------|------------|------------------------|
| AdAway Hosts | [link](https://adaway.org/hosts.txt) | ads, tracking | The endpoint remains reachable, but the hosts file has not received a substantive list update since 2023 and no longer meets the catalogue's freshness standard. | Disconnect Simple Ads or one recommended baseline list |
| FadeMind Risk Hosts | [link](https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Risk/hosts) | malware | The specific add.Risk list has not received a substantive update within the required ~12–18 month freshness window. | HaGeZi TIF, URLHaus, or ThreatFox |
| RPiList Win10 Telemetry | [link](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Win10Telemetry) | telemetry | The specific telemetry file was last substantively updated in 2022, despite the wider RPiList repository remaining active. | HaGeZi Windows/Office Tracker |

---

# 🧾 Legend & Reputation Scores

**Reputation Score (Rep)**  

- **10/10** — industry-leading, authoritative, highly trusted  
- **8–9/10** — strong, safe, actively maintained  
- **6–7/10** — aggressive or niche  

**🆕 NEW** — newly added this month (August 2026)  
**Entries** — unique domains or blocking rules parsed from the current published list

---

# ⭐ Recommended Baseline Blocklists
### Choose ONE as your primary daily-use Pi-hole filtering base.

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| StevenBlack Unified Hosts | [link](https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts) | ads, malware, tracking | Unified hosts file combining multiple curated sources. | Steven Black | 2026-08-02 | **10/10** | 99,275 | Very low false positives |
| Hagezi Multi Normal | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/multi.txt) | ads, malware, phishing, telemetry | Balanced multi-purpose DNS blocklist. | HaGeZi | 2026-08-03 | **10/10** | 182,238 | Excellent primary list |
| OISD Small | [link](https://small.oisd.nl) | ads, malware, tracking | Highly curated low-breakage DNS list. | OISD | 2026-08-03 | **10/10** | 56,064 | Recommended baseline |
| 1Hosts Lite | [link](https://badmojr.github.io/1Hosts/Lite/domains.txt) | ads, tracking | Lightweight DNS blocklist with minimal breakage. | 1Hosts | 2026-08-03 | 9/10 | 209,784 | Alternative baseline |

---

# 📢 Ad Blocking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| Disconnect Simple Ads | [link](https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt) | ads | Conservative DNS ad block list. | Disconnect | 2026-07-31 | 9/10 | 2,700 | Optional but recommended |
| Disconnect Malvertising | [link](https://s3.amazonaws.com/lists.disconnect.me/simple_malvertising.txt) | ads, malware | Blocks malicious advertising infrastructure. | Disconnect | 2026-07-31 | 9/10 | 2,735 | Adds malvertising protection |
| RPiList EasyList Extended | [link](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/easylist) | ads, tracking | DNS-adapted EasyList rules. | RPiList | 2026-08-03 | 8/10 | 154,357 | Moderate aggressiveness |

---

# 🔞 Adult Content Blocking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| OISD NSFW | [link](https://nsfw.oisd.nl) | adult | Adult site blocking list with low collateral damage. | OISD | 2026-08-03 | 9/10 | 487,897 | Useful for family / education networks |

---

# 🪙 Cryptomining & Crypto Abuse Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Crypto | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/crypto.txt) | crypto | Cryptomining and crypto scam domains. | BlocklistProject | 2026-07-20 | 8/10 | 1,274 | Useful additional protection |
| Prigent Crypto | [link](https://v.firebog.net/hosts/Prigent-Crypto.txt) | crypto | Dedicated crypto mining host list. | Prigent | 2026-08-03 | 8/10 | 11,491 | Optional |

---

# 🦠 Malware Protection Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| URLHaus Hostfile | [link](https://urlhaus.abuse.ch/downloads/hostfile/) | malware | Malware distribution domain tracking. | abuse.ch | 2026-08-03 | **10/10** | 356 | Essential malware protection |
| ThreatFox Hostfile | [link](https://threatfox.abuse.ch/downloads/hostfile/) | malware, phishing | Threat intelligence IOC domain feed. | abuse.ch | 2026-08-03 | 9/10 | 49,000 | High value feed |
| RPiList Malware | [link](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/malware) | malware | Regional malware tracking domains. | RPiList | 2026-08-03 | 8/10 | 1,052,962 | Optional layer |
| DandelionSprout Anti-Malware | [link](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt) | malware | Community maintained malware blocklist. | DandelionSprout | 2026-07-09 | 8/10 | 11,732 | Optional |
| NoTrack Malware | [link](https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt) | malware | Malware domains used in the NoTrack project. | quidsup | 2026-06-16 | 7/10 | 123 | More aggressive |

---

# 🧩 Mixed / Combined DNS Blocklists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| Hagezi Multi Pro | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/pro.txt) | ads, malware | Larger version of Multi Normal list. | HaGeZi | 2026-08-03 | 8/10 | 217,642 | Advanced |
| OISD Big | [link](https://big.oisd.nl) | ads, malware, phishing | Massive combined DNS blocklist. | OISD | 2026-08-03 | 9/10 | 433,066 | Very aggressive |
| 1Hosts Xtra | [link](https://badmojr.github.io/1Hosts/Xtra/domains.txt) | ads, tracking, malware | Expanded version of the 1Hosts blocklist and the current replacement for Pro. | 1Hosts | 2026-08-03 | 9/10 | 1,107,946 | Advanced filtering |
| Hagezi Ultimate | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/ultimate.txt) | ads, malware, phishing | Most aggressive HaGeZi DNS blocklist. | HaGeZi | 2026-08-03 | 9/10 | 271,740 | Strict environments |

---

# 🎣 Phishing Protection Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Phishing | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/phishing.txt) | phishing | Dedicated phishing domain list. | BlocklistProject | 2026-07-06 | 9/10 | 190,215 | Reliable |
| Phishing Army Extended | [link](https://phishing.army/download/phishing_army_blocklist_extended.txt) | phishing | Large continuously updated phishing list. | Phishing Army | 2026-08-03 | 9/10 | 155,981 | Recommended |

---

# ⚠️ Threat Intelligence & Suspicious Domains

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Ransomware | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/ransomware.txt) | ransomware | Domains related to ransomware infrastructure. | BlocklistProject | 2026-07-06 | 8/10 | 1,904 | Low false positives |
| BlocklistProject Scam | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/scam.txt) | scam | Fraud and scam domains. | BlocklistProject | 2026-07-18 | 8/10 | 8,527 | Protects against fake shops |
| Hagezi TIF | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/tif.txt) | malware, phishing | Threat intelligence focused list. | HaGeZi | 2026-08-03 | 9/10 | 2,162,771 | High security environments |

---

# 📡 Telemetry & Privacy Blocklists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| HaGeZi Windows/Office Tracker 🆕 | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/native.winoffice.txt) | telemetry, tracking | Blocks Windows and Microsoft Office native telemetry and tracking endpoints. | HaGeZi | 2026-08-01 | 9/10 | 389 | Use through Pi-hole groups; may affect telemetry-dependent Microsoft features |

---

# 📍 CNAME Cloaking & Tracking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| Frogeye First-Party Trackers | [link](https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt) | tracking | Detects CNAME cloaked trackers. | Frogeye | 2026-08-02 | **10/10** | 14,547 | Essential modern tracker protection |

---

_This catalogue is fully verified as of **August 2026** for Pi-hole v6+ compatibility._  
_Using all lists above loads approximately **~6.89 million rule entries before cross-list deduplication**._
****
