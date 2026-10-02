# 🛡️ Pi-hole Blocklist Catalog (October 2026)
## High-Quality, Actively Maintained DNS Blocklists for Pi-hole v6+

This catalogue provides a curated, actively maintained collection of DNS blocklists used to block **ads**, **tracking**, **malware**, **phishing**, **telemetry**, **scams**, **ransomware**, **cryptomining**, and **suspicious domains**.

All blocklists listed here are intended to be:

- Pi-hole v6+ compatible (hosts or domain lists)
- Served via HTTPS
- Actively maintained (updated within ~12–18 months)
- Trusted within the security & privacy community
- Screened for low false positives (unless explicitly noted)

---

## 📅 Changes This Month (October 2026)

### ✅ Added

None

### ❌ Removed

| Name | URL | Categories | Why Removed | Suggested Replacement |
|-----|-----|------------|------------|------------------------|
| Disconnect Simple Ads | [link](https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt) | ads | Legacy Disconnect S3 list with no current freshness metadata. Disconnect has identified `services.json` as its current tracker-protection dataset, so this list no longer meets the catalogue's ~12–18 month freshness standard. | HaGeZi Multi Normal or RPiList EasyList Extended |
| Disconnect Malvertising | [link](https://s3.amazonaws.com/lists.disconnect.me/simple_malvertising.txt) | ads, malware | Legacy list that remains reachable but is no longer maintained and does not meet the catalogue's freshness standard. | URLHaus, HaGeZi TIF, or a recommended baseline list |

---

# 🧾 Legend & Reputation Scores

**Reputation Score (Rep)**  

- **10/10** — industry-leading, authoritative, highly trusted  
- **8–9/10** — strong, safe, actively maintained  
- **6–7/10** — aggressive or niche  

**🆕 NEW** — newly added this month (October 2026)  
**Entries** — unique domains or blocking rules parsed from the current published list; `~` indicates an approximate count where the upstream does not expose a reliable live total

---

# ⭐ Recommended Baseline Blocklists
### Choose ONE as your primary daily-use Pi-hole filtering base.

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| StevenBlack Unified Hosts | [link](https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts) | ads, malware, tracking | Unified hosts file combining multiple curated sources. | Steven Black | 2026-09-27 | **10/10** | 74,760 | Very low false positives |
| Hagezi Multi Normal | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/multi.txt) | ads, malware, phishing, telemetry | Balanced multi-purpose DNS blocklist. | HaGeZi | 2026-10-01 | **10/10** | 200,656 | Excellent primary list |
| OISD Small | [link](https://small.oisd.nl) | ads, malware, tracking | Highly curated low-breakage DNS list. | OISD | 2026-10-01 | **10/10** | 57,372 | Recommended baseline |
| 1Hosts Lite | [link](https://badmojr.github.io/1Hosts/Lite/domains.txt) | ads, tracking | Lightweight DNS blocklist with minimal breakage. | 1Hosts | 2026-09-03 | 9/10 | ~203k | Alternative baseline |

---

# 📢 Ad Blocking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| HaGeZi Ad-Shield | [link](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/share/ad-shield-adblock.txt) | ads, tracking | Targets domains associated with Admiral/Ad-Shield ad-block recovery and publisher monetization infrastructure. | HaGeZi | Active | 8/10 | 426 | Aggressive; can break sites that depend on Ad-Shield. Use a dedicated Pi-hole group and test first |
| RPiList EasyList Extended | [link](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/easylist) | ads, tracking | DNS-adapted EasyList rules. | RPiList | 2026-10-01 | 8/10 | ~171.7k | Moderate aggressiveness |

---

# 🔞 Adult Content Blocking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| OISD NSFW | [link](https://nsfw.oisd.nl) | adult | Adult site blocking list with low collateral damage. | OISD | Daily | 9/10 | ~481.4k | Useful for family / education networks |

---

# 🪙 Cryptomining & Crypto Abuse Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Crypto | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/crypto.txt) | crypto | Cryptomining and crypto scam domains. | BlocklistProject | 2026-07-20 | 8/10 | 1,274 | Useful additional protection |
| Prigent Crypto | [link](https://v.firebog.net/hosts/Prigent-Crypto.txt) | crypto | Dedicated crypto mining host list. | Prigent | Active | 8/10 | 11,491 | Optional |

---

# 🦠 Malware Protection Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| URLHaus Hostfile | [link](https://urlhaus.abuse.ch/downloads/hostfile/) | malware | Malware distribution domain tracking. | abuse.ch | 2026-10-01 | **10/10** | ~430 | Essential malware protection |
| ThreatFox Hostfile | [link](https://threatfox.abuse.ch/downloads/hostfile/) | malware, phishing | Threat intelligence IOC domain feed. | abuse.ch | 2026-09-30 | 9/10 | ~44.7k | High value feed |
| RPiList Malware | [link](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/malware) | malware | Regional malware tracking domains. | RPiList | 2026-10-01 | 8/10 | ~1.05M | Optional layer |
| DandelionSprout Anti-Malware | [link](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt) | malware | Community maintained malware blocklist. | DandelionSprout | 2026-09-19 | 8/10 | ~12.4k | Optional |
| NoTrack Malware | [link](https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt) | malware | Malware domains used in the NoTrack project. | quidsup | 2026-09-07 | 7/10 | 125 | More aggressive; monitor for false positives |

---

# 🧩 Mixed / Combined DNS Blocklists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| Hagezi Multi Pro | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/pro.txt) | ads, malware | Larger version of Multi Normal list. | HaGeZi | 2026-10-01 | 9/10 | 231,053 | Advanced; HaGeZi's current recommended general-purpose tier |
| OISD Big | [link](https://big.oisd.nl) | ads, malware, phishing | Massive combined DNS blocklist. | OISD | Daily | 9/10 | ~244.5k | Broader coverage while prioritizing low breakage |
| 1Hosts Xtra | [link](https://badmojr.github.io/1Hosts/Xtra/domains.txt) | ads, tracking, malware | Aggressive version of the 1Hosts blocklist for maximum filtering. | 1Hosts | 2026-09-03 | 9/10 | ~1.12M | Beta; higher false-positive risk than Lite |
| Hagezi Ultimate | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/ultimate.txt) | ads, malware, phishing | Most aggressive HaGeZi DNS blocklist. | HaGeZi | 2026-10-01 | 9/10 | 287,640 | Strict environments; highest breakage risk among HaGeZi Multi tiers |

---

# 🎣 Phishing Protection Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Phishing | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/phishing.txt) | phishing | Dedicated phishing domain list. | BlocklistProject | Active | 9/10 | 190,215 | Stable security list with monitored upstream sources |
| Phishing Army Extended | [link](https://phishing.army/download/phishing_army_blocklist_extended.txt) | phishing | Large continuously updated phishing list. | Phishing Army | 2026-10-01 | 9/10 | ~148.3k | Recommended |

---

# ⚠️ Threat Intelligence & Suspicious Domains

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Ransomware | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/ransomware.txt) | ransomware | Domains related to ransomware infrastructure. | BlocklistProject | 2026-07-06 | 8/10 | 1,904 | Low false positives |
| BlocklistProject Scam | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/scam.txt) | scam | Fraud and scam domains. | BlocklistProject | 2026-07-18 | 8/10 | 8,527 | Protects against fake shops |
| Hagezi TIF | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/tif.txt) | malware, phishing | Threat intelligence focused list. | HaGeZi | 2026-10-01 | 9/10 | 2,384,850 | High security environments; designed as an add-on to a HaGeZi Multi tier |

---

# 📡 Telemetry & Privacy Blocklists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| HaGeZi Windows/Office Tracker | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/native.winoffice.txt) | telemetry, tracking | Blocks Microsoft native telemetry and tracking endpoints built into devices, services, applications, and operating systems. | HaGeZi | 2026-09-27 | 9/10 | 384 | Use through Pi-hole groups; may affect telemetry-dependent Microsoft features |

---

# 📍 CNAME Cloaking & Tracking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| Frogeye First-Party Trackers | [link](https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt) | tracking | Detects CNAME cloaked trackers. | Frogeye | 2026-09-20 | **10/10** | 14,483 | Essential modern tracker protection |

---

_This catalogue is fully verified as of **October 1, 2026** for Pi-hole v6+ compatibility._  
_Using all lists above loads approximately **~6.94 million rule entries before cross-list deduplication**._
