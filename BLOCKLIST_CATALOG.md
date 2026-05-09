# 🛡️ Pi-hole Blocklist Catalog (May 2026)
## High-Quality, Actively Maintained DNS Blocklists for Pi-hole v6+

This catalogue provides a curated, actively maintained collection of DNS blocklists used to block **ads**, **tracking**, **malware**, **phishing**, **telemetry**, **scams**, **ransomware**, **cryptomining**, and **suspicious domains**.

All blocklists listed here are intended to be:

- Pi-hole v6+ compatible (hosts or domain lists)
- Served via HTTPS
- Actively maintained (updated within ~12–18 months)
- Trusted within the security & privacy community
- Screened for low false positives (unless explicitly noted)

---

## 📅 Changes This Month (May 2026)

### ✅ Added

None

### ❌ Removed

| Name | URL | Categories | Why Removed | Suggested Replacement |
|-----|-----|------------|------------|------------------------|
| WindowsSpyBlocker Spy Hosts | [link](https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt) | telemetry | Upstream list metadata shows a 2022 update date and an open maintenance-status issue; does not meet the ~12–18 month freshness standard. | RPiList Win10 Telemetry, HaGeZi Multi Normal / Ultimate |

---

# 🧾 Legend & Reputation Scores

**Reputation Score (Rep)**  

- **10/10** — industry-leading, authoritative, highly trusted  
- **8–9/10** — strong, safe, actively maintained  
- **6–7/10** — aggressive or niche  

**Entries** — approximate number of domains blocked

---

# ⭐ Recommended Baseline Blocklists
### Choose ONE as your primary daily-use Pi-hole filtering base.

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| StevenBlack Unified Hosts | [link](https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts) | ads, malware, tracking | Unified hosts file combining multiple curated sources. | Steven Black | 2026-05-08 | **10/10** | 82,623 | Very low false positives |
| Hagezi Multi Normal | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/multi.txt) | ads, malware, phishing, telemetry | Balanced multi-purpose DNS blocklist. | HaGeZi | Active | **10/10** | ~151k | Excellent primary list |
| OISD Small | [link](https://small.oisd.nl) | ads, malware, tracking | Highly curated low-breakage DNS list. | OISD | Active | **10/10** | ~56k | Recommended baseline |
| 1Hosts Lite | [link](https://badmojr.github.io/1Hosts/Lite/domains.txt) | ads, tracking | Lightweight DNS blocklist with minimal breakage. | 1Hosts | 2026-05-09 | 9/10 | ~92.5k | Alternative baseline |

---

# 📢 Ad Blocking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| AdAway Hosts | [link](https://adaway.org/hosts.txt) | ads, tracking | Popular mobile and DNS ad blocking hosts file. | AdAway | Active | 9/10 | ~6.5k | Low false positives |
| Disconnect Simple Ads | [link](https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt) | ads | Conservative DNS ad block list. | Disconnect | Active | 9/10 | ~2.7k | Optional but recommended |
| Disconnect Malvertising | [link](https://s3.amazonaws.com/lists.disconnect.me/simple_malvertising.txt) | ads, malware | Blocks malicious advertising infrastructure. | Disconnect | Active | 9/10 | ~2.7k | Adds malvertising protection |
| RPiList EasyList Extended | [link](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/easylist) | ads, tracking | DNS-adapted EasyList rules. | RPiList | Active | 8/10 | ~124k | Moderate aggressiveness |

---

# 🔞 Adult Content Blocking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| OISD NSFW | [link](https://nsfw.oisd.nl) | adult | Adult site blocking list with low collateral damage. | OISD | Active | 9/10 | ~454k | Useful for family / education networks |

---

# 🪙 Cryptomining & Crypto Abuse Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Crypto | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/crypto.txt) | crypto | Cryptomining and crypto scam domains. | BlocklistProject | Active | 8/10 | ~23.8k | Useful additional protection |
| Prigent Crypto | [link](https://v.firebog.net/hosts/Prigent-Crypto.txt) | crypto | Dedicated crypto mining host list. | Prigent | Active | 8/10 | ~11.5k | Optional |

---

# 🦠 Malware Protection Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| URLHaus Hostfile | [link](https://urlhaus.abuse.ch/downloads/hostfile/) | malware | Malware distribution domain tracking. | abuse.ch | 2026-04-27 | **10/10** | ~400–500 | Essential malware protection |
| ThreatFox Hostfile | [link](https://threatfox.abuse.ch/downloads/hostfile/) | malware, phishing | Threat intelligence IOC domain feed. | abuse.ch | Active | 9/10 | ~56.6k | High value feed |
| RPiList Malware | [link](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/malware) | malware | Regional malware tracking domains. | RPiList | Active | 8/10 | ~944k | Optional layer |
| FadeMind Risk Hosts | [link](https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Risk/hosts) | malware | OSINT-derived risky domains. | FadeMind | Active | 8/10 | ~2.2k | Aggressive list |
| DandelionSprout Anti-Malware | [link](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt) | malware | Community maintained malware blocklist. | DandelionSprout | 2026-04-29 | 8/10 | ~12.3k | Optional |
| NoTrack Malware | [link](https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt) | malware | Malware domains used in the NoTrack project. | quidsup | 2026-04-22 | 7/10 | ~141 | More aggressive |

---

# 🧩 Mixed / Combined DNS Blocklists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| Hagezi Multi Pro | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/pro.txt) | ads, malware | Larger version of Multi Normal list. | HaGeZi | Active | 8/10 | ~189k | Advanced |
| OISD Big | [link](https://big.oisd.nl) | ads, malware, phishing | Massive combined DNS blocklist. | OISD | Active | 9/10 | ~331k | Very aggressive |
| 1Hosts Xtra | [link](https://badmojr.github.io/1Hosts/Xtra/domains.txt) | ads, tracking, malware | Expanded version of the 1Hosts blocklist and the current replacement for Pro. | 1Hosts | Active | 9/10 | ~1.08M | Advanced filtering |
| Hagezi Ultimate | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/ultimate.txt) | ads, malware, phishing | Most aggressive HaGeZi DNS blocklist. | HaGeZi | Active | 9/10 | ~292k | Strict environments |

---

# 🎣 Phishing Protection Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Phishing | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/phishing.txt) | phishing | Dedicated phishing domain list. | BlocklistProject | Active | 9/10 | ~190k | Reliable |
| Phishing Army Extended | [link](https://phishing.army/download/phishing_army_blocklist_extended.txt) | phishing | Large continuously updated phishing list. | Phishing Army | Daily | 9/10 | ~158k | Recommended |

---

# ⚠️ Threat Intelligence & Suspicious Domains

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Ransomware | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/ransomware.txt) | ransomware | Domains related to ransomware infrastructure. | BlocklistProject | Active | 8/10 | ~1.9k | Low false positives |
| BlocklistProject Scam | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/scam.txt) | scam | Fraud and scam domains. | BlocklistProject | Active | 8/10 | ~1.3k | Protects against fake shops |
| Hagezi TIF | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/tif.txt) | malware, phishing | Threat intelligence focused list. | HaGeZi | Active | 9/10 | ~974k | High security environments |

---

# 📡 Telemetry & Privacy Blocklists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| RPiList Win10 Telemetry | [link](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Win10Telemetry) | telemetry | Blocks Windows telemetry domains. | RPiList | Active | 8/10 | ~45 | May affect some Microsoft services |

---

# 📍 CNAME Cloaking & Tracking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| Frogeye First-Party Trackers | [link](https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt) | tracking | Detects CNAME cloaked trackers. | Frogeye | Active | **10/10** | ~31.6k | Essential modern tracker protection |

---

_This catalogue is fully verified as of **May 2026** for Pi-hole v6+ compatibility._  
_Using all lists above loads approximately **~5.1 million rule entries before deduplication**._
