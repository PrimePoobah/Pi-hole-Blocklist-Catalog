# 🛡️ Pi-hole Blocklist Catalogue (December 2025 Edition)
## High-Quality, Actively Maintained DNS Blocklists for Pi-hole v6+

This Pi-hole blocklist catalogue provides a curated, actively maintained collection of DNS blocklists used to block ads, malware, phishing, tracking, telemetry, scams, ransomware, cryptomining, and suspicious domains. All blocklists listed here are:

- Pi-hole v6+ compatible (hosts, domains, or supported ABP-style lists)
- Served via HTTPS
- Actively maintained (updated within 12–18 months)
- Trusted within the security & privacy community
- Screened for low false positives
- Suitable for Pi-hole, Unbound, AdGuard Home, pfBlockerNG, and DNS-based filtering

---

## 🔎 Quick Navigation

- [Legend & Reputation Scores](#legend--reputation-scores)
- [Recommended Baseline Blocklists](#recommended-baseline-blocklists)
- [Ad Blocking Lists](#ad-blocking-lists)
- [Adult Content Blocking Lists](#adult-content-blocking-lists)
- [Cryptomining & Crypto Abuse Lists](#cryptomining--crypto-abuse-lists)
- [Malware Protection Lists](#malware-protection-lists)
- [Mixed / Combined DNS Blocklists](#mixed--combined-dns-blocklists)
- [Phishing Protection Lists](#phishing-protection-lists)
- [Threat Intelligence & Suspicious Domains](#threat-intelligence--suspicious-domains)
- [Telemetry & Privacy Blocklists](#telemetry--privacy-blocklists)
- [CNAME Cloaking & Tracking Lists](#cname-cloaking--tracking-lists)
- [Recommended Pi-hole Configurations](#recommended-pi-hole-configurations)
- [Removed This Month](#removed-this-month)

---

# 🧾 Legend & Reputation Scores

**Reputation Score (Rep)**
- 10/10 — industry-leading, authoritative, highly trusted
- 8–9/10 — strong, safe, actively maintained
- 6–7/10 — aggressive, niche, or advanced users only

**🆕 NEW** — added this month (December 2025)  
**Entries** — approximate number of domains blocked

---

# ⭐ Recommended Baseline Blocklists
### Choose at least ONE as your daily-use Pi-hole filtering base.

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| StevenBlack Unified Hosts | https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts | ads, malware, tracking, suspicious | Industry-leading unified hosts file combining multiple curated sources. | Steven Black | Active | 10/10 | ~110k | Very low false positives; ideal for all networks. |
| Hagezi Multi Normal | https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/multi.txt | ads, malware, phishing, telemetry, tracking | Balanced, well-maintained multi-purpose blocklist. | Hagezi | Active | 10/10 | ~267k | Excellent as a primary Pi-hole list. |
| OISD Small | https://small.oisd.nl | ads, malware, tracking, suspicious | Highly curated blocklist focusing on stability & minimal breakage. | OISD | Active | 10/10 | ~71k | Recommended for home, education, and enterprise. |
| 1Hosts (Lite) 🆕 NEW | https://badmojr.github.io/1Hosts/Lite/domains.txt | ads, tracking | Lean DNS list with a strong “low breakage” bias. | 1Hosts (badmojr) | Active | 9/10 | — | Great alternative baseline; start here before going heavier. |

---

# 📢 Ad Blocking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| AdAway Hosts | https://adaway.org/hosts.txt | ads, tracking | Popular mobile + DNS adblock hosts file. | AdAway | Active | 9/10 | — | Low false positives. |
| RPiList EasyList Extended | https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/easylist | ads, tracking | DNS conversion of EasyList-style web filters. | RPiList | Active | 8/10 | — | Moderate aggressiveness. |

---

# 🔞 Adult Content Blocking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| OISD NSFW | https://nsfw.oisd.nl | adult, ads, tracking | Blocks adult websites with low collateral impact. | OISD | Active | 9/10 | — | Ideal for education or family networks. |

---

# 🪙 Cryptomining & Crypto Abuse Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Crypto | https://raw.githubusercontent.com/blocklistproject/Lists/master/crypto.txt | crypto, suspicious | Cryptomining, scam coins, and crypto-abuse domains. | BlocklistProject | Active | 8/10 | — | Good for high-risk systems. |
| Prigent Crypto | https://v.firebog.net/hosts/Prigent-Crypto.txt | crypto, suspicious | Targeted cryptomining/crypto abuse list. | Prigent | Active | 8/10 | — | Optional but valuable; if Firebog is unreliable for you, consider mirroring. |

---

# 🦠 Malware Protection Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| URLHaus Hostfile | https://urlhaus.abuse.ch/downloads/hostfile/ | malware, suspicious | Premier malware distribution tracking list. | abuse.ch | Multiple daily | 10/10 | — | Essential for DNS-level malware blocking. |
| ThreatFox Hostfile | https://threatfox.abuse.ch/downloads/hostfile/ | malware, phishing | Threat intel feed with active malware IOCs. | abuse.ch | Continuous | 9/10 | — | High-value malware feed. |
| RPiList Malware | https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/malware | malware | Regional malware list with strong signal. | RPiList | Active | 8/10 | — | Solid additional layer. |
| OSINT.DigitalSide Latest Domains (Pi-hole format) 🆕 NEW | https://osint.digitalside.it/Threat-Intel/lists/latestdomains.piHole.txt | malware, suspicious | Rolling list of domains collected over the last 7 days (Pi-hole formatted). | OSINT.DigitalSide.IT | Active | 8/10 | — | High-signal feed; best for security-conscious networks. |
| FadeMind Risk Hosts | https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Risk/hosts | malware, suspicious | Risky domain list based on OSINT indicators. | FadeMind | Active | 8/10 | — | Aggressive. |
| DandelionSprout Anti-Malware | https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt | malware | Community-maintained malware blocklist. | DandelionSprout | Active | 8/10 | — | Optional. |
| NoTrack Malware (quidsup) | https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt | malware | Malware hosts from the NoTrack project. | quidsup | Mostly active | 7/10 | — | Mildly aggressive. |

---

# 🧩 Mixed / Combined DNS Blocklists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| Hagezi Multi Pro | https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/pro.txt | ads, malware, telemetry, phishing | Larger, more aggressive version of Multi Normal. | Hagezi | Active | 8/10 | ~354k | Use in separate Pi-hole groups. |
| OISD Big | https://big.oisd.nl | ads, malware, phishing, tracking | Massive unified DNS blocklist. | OISD | Active | 9/10 | ~438k | Ideal for advanced or strict filtering. |

---

# 🎣 Phishing Protection Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Phishing | https://raw.githubusercontent.com/blocklistproject/Lists/master/phishing.txt | phishing | Dedicated phishing domain blocklist. | BlocklistProject | Active | 9/10 | — | Reliable & high quality. |
| Phishing Army (Extended) | https://phishing.army/download/phishing_army_blocklist_extended.txt | phishing | Expanded phishing database updated daily. | Phishing Army | Daily | 9/10 | — | Recommended version. |

---

# ⚠️ Threat Intelligence & Suspicious Domains

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Ransomware | https://raw.githubusercontent.com/blocklistproject/Lists/master/ransomware.txt | malware, suspicious | Ransomware-related domains & portals. | BlocklistProject | Active | 8/10 | — | Low false positives. |
| BlocklistProject Scam | https://raw.githubusercontent.com/blocklistproject/Lists/master/scam.txt | phishing, suspicious | Tech support scams, fake shops, financial fraud. | BlocklistProject | Active | 8/10 | — | Good user-safety protection. |
| Hagezi TIF | https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/tif.txt | malware, phishing | High-risk threat intelligence feed. | Hagezi | Active | 9/10 | — | Use for admin/high-risk devices. |

---

# 📡 Telemetry & Privacy Blocklists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| RPiList Win10 Telemetry | https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Win10Telemetry | telemetry, tracking | Blocks Windows 10/11 telemetry. | RPiList | Active | 8/10 | — | May break some Microsoft cloud services. |
| WindowsSpyBlocker (Hosts - Spy) 🆕 NEW | https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt | telemetry, tracking | Hosts rules targeting Windows telemetry and tracking endpoints. | WindowsSpyBlocker (crazy-max) | Active | 8/10 | — | Use via Pi-hole groups; may impact some Microsoft services. |

---

# 📍 CNAME Cloaking & Tracking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| Frogeye First-Party Trackers | https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt | tracking | Detects first-party & CNAME-based trackers. | Frogeye | Active | 10/10 | — | Critical modern tracking protection. |

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
- Crypto lists (BlocklistProject Crypto; optionally Prigent Crypto)
- Telemetry lists **via Groups only**

---

## High-Security / Strict Filtering (SOC, Admin, Security Lab)

Use separate Pi-hole groups:
- OISD Big
- Hagezi Multi Pro
- Hagezi TIF
- URLHaus
- ThreatFox
- OSINT.DigitalSide Latest Domains (Pi-hole format)
- FadeMind Risk
- NoTrack Malware
- Phishing Army Extended
- WindowsSpyBlocker (Hosts - Spy)

Apply only to:
- Admin workstations
- High-risk systems
- Testing networks

---

# 🗑️ Removed This Month

These sources were removed from the catalog **in December 2025** due to deprecation, staleness, or reliability/quality concerns.

| Name | URL | Categories | Why Removed | Suggested Replacement |
|------|-----|------------|------------|------------------------|
| Disconnect Simple Ads | https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt | ads | Deprecated / no longer recommended for modern Pi-hole deployments. | AdAway Hosts, OISD Small, Hagezi Multi Normal |
| Disconnect Malvertising | https://s3.amazonaws.com/lists.disconnect.me/simple_malvertising.txt | malvertising | Deprecated / no longer recommended for modern Pi-hole deployments. | URLHaus Hostfile, ThreatFox Hostfile |

---

_This catalogue is fully updated and verified as of December 2025 for Pi-hole v6+ compatibility._

_Over 2,000,000 sites are blocked if using all the lists above_
