# 🛡️ Pi-hole Blocklist Catalog (January 2026)
## High-Quality, Actively Maintained DNS Blocklists for Pi-hole v6+

This catalogue provides a curated, actively maintained collection of DNS blocklists used to block **ads**, **tracking**, **malware**, **phishing**, **telemetry**, **scams**, **ransomware**, **cryptomining**, and **suspicious domains**.

All blocklists listed here are intended to be:

- Pi-hole v6+ compatible (hosts or domain lists)
- Served via HTTPS
- Actively maintained (updated within ~12–18 months)
- Trusted within the security & privacy community
- Screened for low false positives (unless explicitly noted)

---

## 🆕 Changes This Month (January 2026)

### ✅ Added
| Name | URL | Categories | Why Added | Suggested Use |
|------|-----|------------|-----------|---------------|
| Disconnect Simple Ads 🆕 | [link](https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt) | ads | Conservative, reputable, low false-positive ad coverage. | Optional but recommended (safe add-on). |
| Disconnect Malvertising 🆕 | [link](https://s3.amazonaws.com/lists.disconnect.me/simple_malvertising.txt) | ads, malware | Focused malvertising coverage from a reputable privacy/security org. | Optional add-on for stronger malvertising protection. |

### ❌ Removed
| Name | URL | Categories | Why Removed | Suggested Replacement |
|------|-----|------------|------------|------------------------|
| OSINT.DigitalSide Latest Domains (Pi-hole format) | [link](https://osint.digitalside.it/Threat-Intel/lists/latestdomains.piHole.txt) | malware, suspicious | Reliability issue (connection refused / unreachable for automated gravity updates). | URLHaus Hostfile, ThreatFox Hostfile |

---

# 🧾 Legend & Reputation Scores

**Reputation Score (Rep)**  
- **10/10** — industry-leading, authoritative, highly trusted  
- **8–9/10** — strong, safe, actively maintained  
- **6–7/10** — aggressive, niche, or advanced users only  

**🆕 NEW** — newly added/returned this month (January 2026)  
**Entries** — approximate number of domains blocked  

---

# ⭐ Recommended Baseline Blocklists
### Choose ONE as your primary daily-use Pi-hole filtering base.

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| StevenBlack Unified Hosts | [link](https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts) | ads, malware, tracking, suspicious | Industry-leading unified hosts file combining multiple curated sources. | Steven Black | Active | **10/10** | ~110k | Very low false positives; ideal for all networks. |
| Hagezi Multi Normal | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/multi.txt) | ads, malware, phishing, telemetry, tracking | Balanced, well-maintained multi-purpose blocklist. | Hagezi | Active | **10/10** | ~267k | Excellent as a primary Pi-hole list. |
| OISD Small | [link](https://small.oisd.nl) | ads, malware, tracking, suspicious | Highly curated blocklist focusing on stability & minimal breakage. | OISD | Active | **10/10** | ~71k | Recommended for home, education, and enterprise. |
| 1Hosts (Lite) | [link](https://badmojr.github.io/1Hosts/Lite/domains.txt) | ads, tracking | Lean DNS list with a strong “low breakage” bias. | 1Hosts (badmojr) | Active | 9/10 | — | Great alternative baseline; start here before going heavier. |

---

# 📢 Ad Blocking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| AdAway Hosts | [link](https://adaway.org/hosts.txt) | ads, tracking | Popular mobile + DNS adblock hosts file. | AdAway | Active | 9/10 | — | Low false positives. |
| Disconnect Simple Ads 🆕 NEW | [link](https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt) | ads | Clean, stable, minimal false positives. | Disconnect | Active | 9/10 | — | Optional but recommended; very low noise. |
| Disconnect Malvertising 🆕 NEW | [link](https://s3.amazonaws.com/lists.disconnect.me/simple_malvertising.txt) | ads, malware | Blocks malicious ad networks and exploit-driven ad servers. | Disconnect | Active | 9/10 | — | Optional; strong malvertising coverage. |
| RPiList EasyList Extended | [link](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/easylist) | ads, tracking | DNS conversion of EasyList-style web filters. | RPiList | Active | 8/10 | — | Moderate aggressiveness. |

---

# 🔞 Adult Content Blocking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| OISD NSFW | [link](https://nsfw.oisd.nl) | adult, ads, tracking | Blocks adult websites with low collateral impact. | OISD | Active | 9/10 | — | Ideal for education or family networks. |

---

# 🪙 Cryptomining & Crypto Abuse Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Crypto | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/crypto.txt) | crypto, suspicious | Cryptomining, scam coins, and crypto-abuse domains. | BlocklistProject | Active | 8/10 | — | Good for high-risk systems. |
| Prigent Crypto | [link](https://v.firebog.net/hosts/Prigent-Crypto.txt) | crypto, suspicious | Targeted cryptomining/crypto abuse list. | Prigent | Active | 8/10 | — | Optional but valuable; if Firebog is unreliable for you, consider mirroring. |

---

# 🦠 Malware Protection Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| URLHaus Hostfile | [link](https://urlhaus.abuse.ch/downloads/hostfile/) | malware, suspicious | Premier malware distribution tracking list. | abuse.ch | Multiple daily | **10/10** | — | Essential for DNS-level malware blocking. |
| ThreatFox Hostfile | [link](https://threatfox.abuse.ch/downloads/hostfile/) | malware, phishing | Threat intel feed with active malware IOCs. | abuse.ch | Continuous | 9/10 | — | High-value malware feed. |
| RPiList Malware | [link](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/malware) | malware | Regional malware list with strong signal. | RPiList | Active | 8/10 | — | Solid additional layer. |
| FadeMind Risk Hosts | [link](https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Risk/hosts) | malware, suspicious | Risky domain list based on OSINT indicators. | FadeMind | Active | 8/10 | — | Aggressive. |
| DandelionSprout Anti-Malware | [link](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt) | malware | Community-maintained malware blocklist. | DandelionSprout | Active | 8/10 | — | Optional. |
| NoTrack Malware (quidsup) | [link](https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt) | malware | Malware hosts from the NoTrack project. | quidsup | Mostly active | 7/10 | — | Mildly aggressive. |

---

# 🧩 Mixed / Combined DNS Blocklists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| Hagezi Multi Pro | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/pro.txt) | ads, malware, telemetry, phishing | Larger, more aggressive version of Multi Normal. | Hagezi | Active | 8/10 | ~354k | Use in separate Pi-hole groups. |
| OISD Big | [link](https://big.oisd.nl) | ads, malware, phishing, tracking | Massive unified DNS blocklist. | OISD | Active | 9/10 | ~438k | Ideal for advanced or strict filtering. |

---

# 🎣 Phishing Protection Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Phishing | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/phishing.txt) | phishing | Dedicated phishing domain blocklist. | BlocklistProject | Active | 9/10 | — | Reliable & high quality. |
| Phishing Army (Extended) | [link](https://phishing.army/download/phishing_army_blocklist_extended.txt) | phishing | Expanded phishing database updated daily. | Phishing Army | Daily | 9/10 | — | Recommended version. |

---

# ⚠️ Threat Intelligence & Suspicious Domains

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Ransomware | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/ransomware.txt) | malware, suspicious | Ransomware-related domains & portals. | BlocklistProject | Active | 8/10 | — | Low false positives. |
| BlocklistProject Scam | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/scam.txt) | phishing, suspicious | Tech support scams, fake shops, financial fraud. | BlocklistProject | Active | 8/10 | — | Good user-safety protection. |
| Hagezi TIF | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/tif.txt) | malware, phishing | High-risk threat intelligence feed. | Hagezi | Active | 9/10 | — | Use for admin/high-risk devices. |

---

# 📡 Telemetry & Privacy Blocklists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| RPiList Win10 Telemetry | [link](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Win10Telemetry) | telemetry, tracking | Blocks Windows 10/11 telemetry. | RPiList | Active | 8/10 | — | May break some Microsoft cloud services. |
| WindowsSpyBlocker (Hosts - Spy) | [link](https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt) | telemetry, tracking | Hosts rules targeting Windows telemetry and tracking endpoints. | WindowsSpyBlocker (crazy-max) | Active | 8/10 | — | Use via Pi-hole groups; may impact some Microsoft services. |

---

# 📍 CNAME Cloaking & Tracking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| Frogeye First-Party Trackers | [link](https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt) | tracking | Detects first-party & CNAME-based trackers. | Frogeye | Active | **10/10** | — | Critical modern tracking protection. |

---

# 🛠 Recommended Pi-hole Configurations

## Best All-Around (Home, School, Work)

Choose at least ONE baseline list:
- StevenBlack Unified
- Hagezi Multi Normal
- OISD Small
- 1Hosts (Lite)

Add core security feeds:
- URLHaus
- ThreatFox
- Phishing Army Extended
- Frogeye First-Party Trackers
- BlocklistProject Phishing

Optional:
- AdAway
- Disconnect Simple Ads 🆕
- Disconnect Malvertising 🆕
- Crypto lists (BlocklistProject Crypto; optionally Prigent Crypto)
- Telemetry lists via Groups only

---

## High-Security / Strict Filtering (SOC, Admin, Security Lab)

Use separate Pi-hole groups:
- OISD Big
- Hagezi Multi Pro
- Hagezi TIF
- URLHaus
- ThreatFox
- FadeMind Risk
- NoTrack Malware
- Phishing Army Extended
- WindowsSpyBlocker (Hosts - Spy)

Apply only to:
- Admin workstations
- High-risk systems
- Testing networks

---

_This catalogue is fully updated and verified as of January 2026 for Pi-hole v6+ compatibility._
_Over 2,000,000 sites are blocked if using all the lists above_
