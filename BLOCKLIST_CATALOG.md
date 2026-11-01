# 🛡️ Pi-hole Blocklist Catalog (November 2026)
## High-Quality, Actively Maintained DNS Blocklists for Pi-hole v6+

This catalogue provides a curated, actively maintained collection of DNS blocklists used to block **ads**, **tracking**, **malware**, **phishing**, **telemetry**, **scams**, **ransomware**, **cryptomining**, and **suspicious domains**.

All blocklists listed here are intended to be:

- Pi-hole v6+ compatible (hosts or domain lists)
- Served via HTTPS
- Actively maintained (updated within ~12–18 months)
- Trusted within the security & privacy community
- Screened for low false positives (unless explicitly noted)

---

## 📅 Changes This Month (November 2026)

### ✅ Added

| Name | URL | Categories | Why Added | Suggested Use |
|-----|-----|------------|-----------|---------------|
| CERT Polska Warning List 🆕 | [link](https://hole.cert.pl/domains/v2/domains.txt) | phishing, scam, malware | National CERT-operated warning list of reported malicious domains, with a publicly accessible Pi-hole-compatible domain feed, an established reporting process and defined six-month retention. New to this catalogue, not a newly released project. | Additional phishing/fraud protection; especially relevant to Polish-language or Poland-facing networks |

### ❌ Removed

| Name | URL | Categories | Why Removed | Suggested Replacement |
|-----|-----|------------|------------|------------------------|
| URLHaus Hostfile | [link](https://urlhaus.abuse.ch/downloads/hostfile/) | malware | The public unauthenticated feed now returns HTTP 410 Gone. abuse.ch requires an individual Auth-Key for current exports, so this URL cannot be used as a public plug-and-play Pi-hole adlist. | HaGeZi TIF or RPiList Malware; authenticated URLhaus export for private deployments |
| ThreatFox Hostfile | [link](https://threatfox.abuse.ch/downloads/hostfile/) | malware, phishing | The public unauthenticated feed now returns HTTP 410 Gone. Current exports require an abuse.ch Auth-Key. The old URL would fail gravity updates. | HaGeZi TIF, DandelionSprout Anti-Malware or CERT Polska Warning List |

---

# 🧾 Legend & Reputation Scores

**Reputation Score (Rep)**  

- **10/10** — industry-leading, authoritative, highly trusted  
- **8–9/10** — strong, safe, actively maintained  
- **6–7/10** — aggressive or niche  

**🆕 NEW** — newly added to this catalogue in November 2026 (not necessarily newly published)  
**Entries** — source-published domain/rule totals or validated snapshots; `~` denotes an estimate or rounded independent observation, and `—` means no trustworthy count could be confirmed. Counts are per-list, not deduplicated across lists.

---

# ⭐ Recommended Baseline Blocklists
### Choose ONE as your primary daily-use Pi-hole filtering base.

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| StevenBlack Unified Hosts | [link](https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts) | ads, malware, tracking | Unified hosts file combining multiple curated sources. | Steven Black | 2026-10-29 | **10/10** | 76,736 | Very low false positives |
| Hagezi Multi Normal | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/multi.txt) | ads, malware, phishing, telemetry | Balanced multi-purpose DNS blocklist. | HaGeZi | 2026-11-01 | **10/10** | 175,760 | Excellent primary list |
| OISD Small | [link](https://small.oisd.nl) | ads, malware, tracking | Highly curated low-breakage DNS list. | OISD | 2026-11-01 | **10/10** | 59,208 | Recommended baseline |
| 1Hosts Lite | [link](https://badmojr.github.io/1Hosts/Lite/domains.txt) | ads, tracking | Lightweight DNS blocklist with minimal breakage. | 1Hosts | 2026-09-03 | 9/10 | ~203,000 | Alternative baseline; last published release September 2026 |

---

# 📢 Ad Blocking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| HaGeZi Ad-Shield | [link](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/share/ad-shield-adblock.txt) | ads, tracking | Targets domains associated with Admiral/Ad-Shield ad-block recovery and publisher monetization infrastructure. | HaGeZi | Checked 2026-11-01 | 8/10 | 627 | Aggressive; can break sites that depend on Ad-Shield. Use a dedicated Pi-hole group and test first |
| RPiList EasyList Extended | [link](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/easylist) | ads, tracking | DNS-adapted EasyList rules. | RPiList | Checked 2026-10-31 | 8/10 | ~182,920 | Moderate aggressiveness; approximate DNS rules, not cross-list-unique domains |

---

# 🔞 Adult Content Blocking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| OISD NSFW | [link](https://nsfw.oisd.nl) | adult | Adult site blocking list with low collateral damage. | OISD | 2026-10-29 | 9/10 | ~488,100 | Useful for family / education networks |

---

# 🪙 Cryptomining & Crypto Abuse Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Crypto | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/crypto.txt) | crypto | Cryptomining and crypto scam domains. | BlocklistProject | 2026-07-20 | 8/10 | 1,274 | Useful additional protection |
| Prigent Crypto | [link](https://v.firebog.net/hosts/Prigent-Crypto.txt) | crypto | Dedicated crypto mining host list. | Prigent | 2026-10-16 | 8/10 | 11,490 | Optional |

---

# 🦠 Malware Protection Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| RPiList Malware | [link](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/malware) | malware | Regional malware tracking domains. | RPiList | Checked 2026-10-31 | 8/10 | — | Active upstream; file exceeds available extraction limit, so the October estimate was not carried forward as an exact count |
| DandelionSprout Anti-Malware | [link](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt) | malware | Community maintained malware blocklist. | DandelionSprout | 2026-10-17 | 8/10 | ~12,600 | Optional |
| NoTrack Malware | [link](https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt) | malware | Malware domains used in the NoTrack project. | quidsup | 2026-09-07 | 7/10 | 125 | More aggressive; monitor for false positives |

---

# 🧩 Mixed / Combined DNS Blocklists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| Hagezi Multi Pro | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/pro.txt) | ads, malware | Larger version of Multi Normal list. | HaGeZi | 2026-11-01 | 9/10 | 213,387 | Advanced; HaGeZi's current recommended general-purpose tier |
| OISD Big | [link](https://big.oisd.nl) | ads, malware, phishing | Massive combined DNS blocklist. | OISD | 2026-10-29 | 9/10 | ~234,800 | Broader coverage while prioritizing low breakage |
| 1Hosts Xtra | [link](https://badmojr.github.io/1Hosts/Xtra/domains.txt) | ads, tracking, malware | Aggressive version of the 1Hosts blocklist for maximum filtering. | 1Hosts | 2026-09-03 | 9/10 | ~1,120,000 | Beta; higher false-positive risk than Lite |
| Hagezi Ultimate | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/ultimate.txt) | ads, malware, phishing | Most aggressive HaGeZi DNS blocklist. | HaGeZi | 2026-11-01 | 9/10 | 283,353 | Strict environments; highest breakage risk among HaGeZi Multi tiers |

---

# 🎣 Phishing Protection Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Phishing | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/phishing.txt) | phishing | Dedicated phishing domain list. | BlocklistProject | 2026-07 | 9/10 | ~190,215 | Stable security list with monitored upstream sources |
| Phishing Army Extended | [link](https://phishing.army/download/phishing_army_blocklist_extended.txt) | phishing | Large continuously updated phishing list. | Phishing Army | 2026-10-31 | 9/10 | 152,837 | Recommended |
| CERT Polska Warning List 🆕 | [link](https://hole.cert.pl/domains/v2/domains.txt) | phishing, scam, malware | Active malicious-domain warning feed operated by Poland's national CERT. | CERT Polska (NASK) | Checked 2026-11-01 | **10/10** | 126,165 | Nationally focused source; overlaps with larger phishing lists, use as an optional extra layer |

---

# ⚠️ Threat Intelligence & Suspicious Domains

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Ransomware | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/ransomware.txt) | ransomware | Domains related to ransomware infrastructure. | BlocklistProject | 2026-07-06 | 8/10 | 1,904 | Low false positives |
| BlocklistProject Scam | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/scam.txt) | scam | Fraud and scam domains. | BlocklistProject | 2026-07-18 | 8/10 | 8,527 | Protects against fake shops |
| Hagezi TIF | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/tif.txt) | malware, phishing | Threat intelligence focused list. | HaGeZi | 2026-11-01 | 9/10 | 1,868,103 | High security environments; designed as an add-on to a HaGeZi Multi tier |

---

# 📡 Telemetry & Privacy Blocklists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| HaGeZi Windows/Office Tracker | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/native.winoffice.txt) | telemetry, tracking | Blocks Microsoft native telemetry and tracking endpoints built into devices, services, applications, and operating systems. | HaGeZi | 2026-10-30 | 9/10 | 384 | Use through Pi-hole groups; may affect telemetry-dependent Microsoft features |

---

# 📍 CNAME Cloaking & Tracking Lists

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| Frogeye First-Party Trackers | [link](https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt) | tracking | Detects CNAME cloaked trackers. | Frogeye | 2026-10-25 | **10/10** | 14,797 | Essential modern tracker protection |

---

_This catalogue was reviewed on **November 1, 2026** for Pi-hole v6+ list compatibility, public reachability, project activity, and available published entry totals. Some large-source counts remain approximate; the RPiList Malware count is unverified._  
_The listed feeds represent **approximately 5.43 million reported or estimated entries**, **excluding RPiList Malware**, before cross-list deduplication. This is **not** a unique-domain total, and actual Pi-hole gravity counts will vary._
