<!-- BLOCKLIST_CATALOG.md -->

# 🛡️ Pi-hole Blocklist Catalogue (November 2025 Edition)
## High-Quality, Actively Maintained DNS Blocklists for Pi-hole v6+

This Pi-hole blocklist catalogue provides a curated, actively maintained set of DNS blocklists for blocking ads, trackers, telemetry, malware, phishing, cryptomining, and suspicious domains. All blocklists listed here are:

- Pi-hole v6+ compatible (hosts or domain lists)
- Served via HTTPS
- Actively maintained (updated within 12–18 months)
- Trusted within the security & privacy community
- Screened for low false positives
- Suitable for Pi-hole, Unbound, AdGuard Home, pfBlockerNG, and DNS-based filtering

---

## 🔎 Quick Navigation

- [Legend & Reputation Scores](#legend--reputation-scores)
- [Recommended Baseline Blocklists](#-recommended-baseline-blocklists)
- [Ad Blocking Lists](#-ad-blocking-lists)
- [Adult Content Blocking Lists](#-adult-content-blocking-lists)
- [Cryptomining & Crypto Abuse Lists](#-cryptomining--crypto-abuse-lists)
- [Malware Protection Lists](#-malware-protection-lists)
- [Mixed / Combined DNS Blocklists](#-mixed--combined-dns-blocklists)
- [Phishing Protection Lists](#-phishing-protection-lists)
- [Threat Intelligence & High-Risk Lists](#-threat-intelligence--high-risk-lists)
- [Telemetry & Privacy Blocklists](#-telemetry--privacy-blocklists)
- [CNAME Cloaking & Tracking Lists](#-cname-cloaking--tracking-lists)
- [Recommended Profiles & Grouping](#-recommended-profiles--grouping)

---

## 🧾 Legend & Reputation Scores

**Categories** may include:

- `ads` — advertising domains  
- `tracking` — analytics, tracking, cross-site profiling  
- `telemetry` — OS or application telemetry  
- `malware` — known malicious domains  
- `phishing` — credential theft, fake login pages  
- `crypto` — cryptomining, cryptojacking, crypto abuse  
- `mixed` — combination of ads, trackers, malware, and more  

**Reputation Score (Rep)**  
- 10/10 — industry-leading, authoritative, highly trusted  
- 8–9/10 — strong, safe, actively maintained  
- 6–7/10 — aggressive, niche, or advanced users only  

**🆕 NEW** — newly added or newly validated  
**Entries** — approximate number of domains blocked  

---

# ⭐ Recommended Baseline Blocklists
### Choose at least ONE as your daily-use Pi-hole filtering base.

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| StevenBlack Unified Hosts | https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts | ads, tracking, malware, fake news, gambling, porn (depending on variant) | Unified hosts file with multiple curated sources; widely trusted. | StevenBlack | Active | 10/10 | ~110k | Very low false positives; ideal for all networks. |
| Hagezi Multi Normal | https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/hosts/multi.txt | ads, tracking, malware, telemetry | Balanced, multi-source blocklist optimized for DNS firewalls. | Hagezi | Active | 10/10 | ~267k | Excellent as a primary Pi-hole list. |
| OISD Small | https://small.oisd.nl | ads, malware, tracking, scams | Carefully curated, small but powerful list. | OISD | Active | 10/10 | ~71k | Recommended for home, education, and enterprise. |
| 1Hosts (Lite) 🆕 NEW | https://raw.githubusercontent.com/badmojr/1Hosts/master/Lite/hosts.txt | ads, tracking | Lean baseline hosts list; privacy-focused with low breakage. | badmojr / 1Hosts | Active | 9/10 | — | Great alternative baseline to StevenBlack/OISD. |

---

# 📢 Ad Blocking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| AdAway Hosts 🆕 NEW | https://adaway.org/hosts.txt | ads, tracking | Mobile-focused but fully hosts-compatible blocklist. | AdAway | Active | 9/10 | — | Low false positives. |
| RPiList EasyList Extended | https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/easylist | ads, tracking | Derived from EasyList with DNS-friendly formatting. | RPiList | Active | 8/10 | — | Moderate aggressiveness. |

---

# 🔞 Adult Content Blocking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| RPiList Adult Content | https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/DomainSquatting | porn, adult content | Focused on blocking adult content and NSFW domains. | RPiList | Active | 8/10 | — | Recommended for family networks. |
| Hagezi NSFW | https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/hosts/nsfw.txt | porn, adult content | Hagezi's dedicated NSFW blocklist. | Hagezi | Active | 9/10 | — | Use with Pi-hole groups for kids/guest networks. |

---

# ⛏️ Cryptomining & Crypto Abuse Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| RPiList Crypto | https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Crypto | crypto, cryptomining | Blocks known cryptomining and crypto-abuse domains. | RPiList | Active | 8/10 | — | Helpful for lab and enterprise environments. |

---

# 🦠 Malware Protection Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| URLHaus Hostfile | https://urlhaus.abuse.ch/downloads/hostfile/ | malware | Hostfile of malware distribution domains observed by URLHaus. | abuse.ch | Multiple daily | 10/10 | — | Essential for DNS-level malware blocking. |
| ThreatFox Hostfile | https://threatfox.abuse.ch/downloads/hostfile/ | malware | ThreatFox threat intelligence hostfile of malicious domains. | abuse.ch | Continuous | 9/10 | — | High-value malware feed. |
| RPiList Malware | https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/malware | malware | German-centric plus global malware blocklist. | RPiList | Active | 8/10 | — | Solid additional layer. |
| FadeMind Risk Hosts 🆕 NEW | https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Risk/hosts | malware, suspicious | Extra hosts file focused on risky or malicious domains, based on OSINT indicators. | FadeMind | Active | 8/10 | — | Aggressive. |
| DandelionSprout Anti-Malware 🆕 NEW | https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt | malware | DNS/hosts-compatible anti-malware blocklist. | DandelionSprout | Active | 8/10 | — | Optional. |
| NoTrack Malware (quidsup) 🆕 NEW | https://gitlab.com/quidsup/notrack-blocklists/raw/master/malware.hosts | malware | Malware-focused hosts list maintained by NoTrack project. | quidsup | Mostly active | 7/10 | — | Mildly aggressive. |
| OSINT.DigitalSide Latest Domains 🆕 NEW | https://osint.digitalside.it/Threat-Intel/lists/latestdomains.txt | malware, suspicious | 7-day rolling list of malicious/suspicious domains from OSINT.DigitalSide. | OSINT.DigitalSide.IT | Active | 8/10 | — | High-signal malware feed; best for security-conscious networks. |

---

# 🧩 Mixed / Combined DNS Blocklists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| Hagezi Multi Pro | https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/hosts/pro.txt | ads, tracking, malware, telemetry | More aggressive multi-source list than Multi Normal. | Hagezi | Active | 9/10 | — | For advanced users and admin networks. |
| Hagezi TIF | https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/hosts/tif.txt | ads, tracking, malware, telemetry, phishing | Threat Intelligence Feeds bundle; very aggressive. | Hagezi | Active | 9/10 | — | Use for admin/high-risk devices. |

---

# 🎣 Phishing Protection Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| Phishing Army Extended | https://phishing.army/download/phishing_army_blocklist_extended.txt | phishing | Community-driven phishing blocklist (extended edition). | Phishing Army | Multiple daily | 9/10 | — | Strong phishing coverage. |
| BlocklistProject Phishing | https://raw.githubusercontent.com/blocklistproject/Lists/master/phishing.txt | phishing | Phishing-focused list from BlocklistProject. | BlocklistProject | Active | 8/10 | — | Good general phishing protection. |
| BlocklistProject Scam | https://raw.githubusercontent.com/blocklistproject/Lists/master/scam.txt | phishing, scam | Tech support scams, fake shops, financial fraud. | BlocklistProject | Active | 8/10 | — | Good user-safety protection. |

---

# 🔬 Threat Intelligence & High-Risk Lists

These lists are **more aggressive** and best suited for:

- Admin workstations
- Security operations
- Labs and sandboxes
- High-risk networks

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Crypto | https://raw.githubusercontent.com/blocklistproject/Lists/master/crypto.txt | crypto, abuse | Crypto-abuse, cryptomining, and scam-focused list. | BlocklistProject | Active | 8/10 | — | For security or lab use. |
| BlocklistProject Ransomware | https://raw.githubusercontent.com/blocklistproject/Lists/master/ransomware.txt | ransomware, malware | Ransomware-related domains. | BlocklistProject | Active | 8/10 | — | High-value in SOC/lab setups. |
| BlocklistProject Abuse | https://raw.githubusercontent.com/blocklistproject/Lists/master/abuse.txt | abuse, malware | General abuse/malware list. | BlocklistProject | Active | 8/10 | — | Complementary to other malware feeds. |
| BlocklistProject Fraud | https://raw.githubusercontent.com/blocklistproject/Lists/master/fraud.txt | fraud, phishing | Fraud and scam-related domains. | BlocklistProject | Active | 8/10 | — | Good for user safety. |
| BlocklistProject Malware | https://raw.githubusercontent.com/blocklistproject/Lists/master/malware.txt | malware | Dedicated malware list from BlocklistProject. | BlocklistProject | Active | 8/10 | — | Optional but valuable. |

---

# 📡 Telemetry & Privacy Blocklists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| RPiList Win10 Telemetry | https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Win10Telemetry | telemetry | Blocks Microsoft Windows telemetry and related endpoints. | RPiList | Active | 8/10 | — | May break some Microsoft cloud services. |
| WindowsSpyBlocker Spy Rules 🆕 NEW | https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt | telemetry, tracking | Hosts rules targeting Windows telemetry and tracking endpoints. | crazy-max / WindowsSpyBlocker | Active | 8/10 | — | Use via Pi-hole groups; may impact some Microsoft services. |

---

# 📍 CNAME Cloaking & Tracking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| Frogeye First-Party Trackers 🆕 NEW | https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt | tracking | Detects first-party CNAME-based trackers. | Frogeye | Active | 10/10 | — | Critical modern tracking protection. |

---

# 🧮 Recommended Profiles & Grouping

Use **Pi-hole groups** to apply the right lists to the right devices.

## Home / Family (Default Group)

Baseline:
- StevenBlack **or**
- Hagezi Multi Normal **or**
- OISD Small **or**
- 1Hosts (Lite)

Add:
- URLHaus
- ThreatFox
- RPiList Malware

Optional:
- Additional ad lists as needed
- AdAway
- Crypto lists

---

## High-Security / Strict Filtering (SOC, Admin, Security Lab)

Use separate Pi-hole groups:
- OISD Big
- Hagezi Pro
- Hagezi TIF
- BlocklistProject Malware
- BlocklistProject Ransomware
- BlocklistProject Phishing
- BlocklistProject Scam
- URLHaus
- ThreatFox
- FadeMind Risk
- NoTrack Malware
- OSINT.DigitalSide Latest Domains

Apply only to:
- Admin workstations
- High-risk systems
- Testing networks

---

  _This catalogue is validated for format, reachability, and maintenance signals as of November 2025 for Pi-hole v6+ compatibility._

  _Over 2,000,000 sites are blocked if using all the lists above_
