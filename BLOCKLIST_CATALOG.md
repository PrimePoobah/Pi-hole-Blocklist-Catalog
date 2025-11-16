# 🛡️ Pi-hole Blocklist Catalog

Curated, **Pi-hole v6+ compatible** blocklists from reputable, actively maintained sources.

All lists included are:

- 🌐 Served via **HTTPS**  
- 🧱 Hosts / Domain / Adblock compatible  
- 🔄 Actively maintained (≤12–18 months)  
- 🧪 Reasonably safe for Pi-hole v6+ (but always test in your own environment)

---

## 🔎 Quick Navigation

- [Legend](#-legend)
- [Recommended Baseline Lists](#-recommended-baseline-lists)
- [Ads](#-ads)
- [Adult](#-adult)
- [Crypto](#-crypto)
- [Malware](#-malware)
- [Mixed](#-mixed)
- [Phishing](#-phishing)
- [Suspicious / Threat-Intel](#-suspicious--threat-intel)
- [Telemetry](#-telemetry)
- [Implementation Notes](#-implementation-notes)

---

## 🧾 Legend

**Reputation Score (1–10)**  
- **10** – Long-standing, trusted, extremely stable, low false-positives  
- **8–9** – Strong, well-maintained, widely used  
- **6–7** – Good but more aggressive or specialized  

**Approx. Entries**  
- Based on published or commonly referenced domain totals  
- `—` = not published  

**Categories**  
Alphabetical, comma-separated (e.g., `ads, malware, tracking`)  

---

# ⭐ Recommended Baseline Lists  
*(Choose ONE as your main “daily driver” list)*

These lists offer the best balance of reliability, low breakage, maintenance quality, and broad protection.

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| **StevenBlack Unified Hosts** | [link](https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts) | ads, malware, suspicious, tracking | Long-standing unified list combining several reputable sources with deduplication. | Steven Black | Very active (Release: Nov 2025) | **10/10** | ~110k | Excellent stability & low breakage. Ideal baseline for most networks. |
| **Hagezi Multi Normal** | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/multi.txt) | ads, malware, phishing, suspicious, telemetry, tracking | Balanced, well-tuned multipurpose blocklist. | Hagezi | Active 2025 | **10/10** | ~267k | Great all-in-one list; frequently updated; Pi-hole compatible. |
| **OISD Small** | [link](https://small.oisd.nl) | ads, malware, tracking, telemetry | Lightweight curated list optimized for high stability. | OISD (sjhgvr) | Active 2025 | **10/10** | ~71k | Minimal breakage; excellent for home, education, corporate networks. |

---

# 📢 Ads

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| RPiList EasyList Extended | [link](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/easylist) | ads, tracking | DNS-converted ad/tracker list based on EasyList. | RPiList / SemperVideo | Active 2025 | 8/10 | — | Good ad blocking layer; use alongside a baseline list. |

---

# 🔞 Adult

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| OISD NSFW | [link](https://nsfw.oisd.nl) | adult, ads, tracking | NSFW variant of OISD for adult/porn domain filtering. | OISD (sjhgvr) | Active 2025 | 9/10 | — | Aggressive blocking; enable only where appropriate. |

---

# 🪙 Crypto

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Crypto | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/crypto.txt) | crypto, suspicious | Blocks malicious mining & scammy crypto-related domains. | The Blocklist Project | Active 2025 | 8/10 | — | Can block legitimate crypto platforms; use in high-risk groups. |

---

# 🦠 Malware

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Malware | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/malware.txt) | malware | Malware infrastructure aggregated from multiple threat sources. | The Blocklist Project | Active 2025 | 9/10 | — | Good general malware layer. |
| RPiList Malware | [link](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/malware) | malware | Maintained malware-related blocklist used widely in EU. | RPiList / SemperVideo | Active 2025 | 8/10 | — | Good complement to threat-intel feeds. |
| ThreatFox Hostfile | [link](https://threatfox.abuse.ch/downloads/hostfile/) | malware, phishing, suspicious | IOC-driven list of active C2, malware hosts, payload sites. | abuse.ch | Rolling 6 months | 9/10 | — | High-signal threat feed; recommended for security-focused groups. |
| URLHaus Hostfile | [link](https://urlhaus.abuse.ch/downloads/hostfile/) | malware, phishing, suspicious | Malware-distribution domains reported by global researchers. | abuse.ch | Updated multiple times daily | **10/10** | — (backed by huge DB) | One of the most effective malware blocklists available. |

---

# 🧩 Mixed

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| Hagezi Multi Pro | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/pro.txt) | ads, malware, phishing, suspicious, telemetry, tracking | More aggressive variant of Multi Normal. | Hagezi | Active 2025 | 8/10 | ~354k | Excellent privacy but higher FP rates; use cautiously. |
| OISD Big | [link](https://big.oisd.nl) | ads, malware, phishing, suspicious, telemetry, tracking | Large “mega list” combining many curated sources. | OISD | Active 2025 | 9/10 | ~438k | Heavy but powerful; monitor for breakage. |

---

# 🎣 Phishing

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Phishing | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/phishing.txt) | phishing | Phishing and credential-stealing domain list. | BlocklistProject | Active 2025 | 9/10 | — | Strong phishing protection. |
| Phishing Army | [link](https://phishing.army/download/phishing_army_blocklist.txt) | phishing | Aggregates multiple phishing feeds (OpenPhish, PhishTank). | Phishing Army | Updated daily | 9/10 | — | Excellent for high-risk targets. |

---

# ⚠️ Suspicious / Threat-Intel

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| BlocklistProject Ransomware | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/ransomware.txt) | malware, suspicious | Ransomware-related domains including C2 & payment sites. | BlocklistProject | Active 2025 | 8/10 | — | Helps block severe threats; minimal breakage. |
| BlocklistProject Scam | [link](https://raw.githubusercontent.com/blocklistproject/Lists/master/scam.txt) | phishing, suspicious | Fake shops, refund scams, tech-support scams. | BlocklistProject | Active 2025 | 8/10 | — | Good supplement for general protection. |
| Hagezi TIF | [link](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/tif.txt) | malware, phishing, suspicious | High-risk threat intel (C2s, hardened infra). | Hagezi | Active 2025 | 9/10 | — | Best for IT/admin or high-risk devices. |

---

# 📡 Telemetry

| Name | URL | Categories | Description | Maintainer | Updated | Rep | Entries | Notes |
|------|-----|------------|-------------|------------|---------|-----|---------|-------|
| RPiList Win10 Telemetry | [link](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Win10Telemetry) | telemetry, tracking | Blocks Windows telemetry & tracking endpoints. | RPiList / SemperVideo | Active 2025 | 8/10 | — | May affect Microsoft cloud services. |

---

# 🛠 Implementation Notes

## **Recommended Setup for Most Home / Education Networks**

### Choose ONE baseline:
- ⭐ **StevenBlack Unified Hosts**  
- ⭐ **Hagezi Multi Normal**  
- ⭐ **OISD Small**

### Add core security layers:
- 🦠 **URLHaus Hostfile**  
- 🕵️ **ThreatFox Hostfile**  
- 🎣 **Phishing Army**

### Optional (environment-specific):
- 🔞 OISD NSFW  
- 🪙 BlocklistProject Crypto  
- 🛑 BlocklistProject Malware/Phishing/Ransomware/Scam  
- 🔥 Hagezi Multi Pro / TIF  
- 🪟 RPiList Win10 Telemetry  

---

## **Pi-hole v6+ Group Strategy (Best Practice)**

- Create **separate groups** for heavy/aggressive lists:
  - Hagezi Multi Pro  
  - OISD Big  
  - URLHaus  
  - ThreatFox  
  - Hagezi TIF  

- Apply strict groups only to:
  - IT/Admin devices  
  - High-risk devices  
  - Lab/testing networks  

- Apply baseline + core security to:
  - Staff devices  
  - Student devices  
  - Guest Wi-Fi (after testing)

---

## **Monitoring & Maintenance**

- Review Pi-hole **Top Blocked Domains** frequently  
- Whitelist legitimate services as needed  
- Export logs to SIEM or dashboard for analysis  
- Update blocklists regularly (automation recommended)

---

*All “Updated” values and domain counts are approximate and based on public data and active project maintenance through 2024–2025. Always verify before production deployment.*

