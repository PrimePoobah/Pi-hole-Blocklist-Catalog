# 🛡️ Pi-hole Blocklist Catalog  
<sub><code>material-icons: security</code> • Curated, Pi-hole v6+ compatible blocklists</sub>

This catalog aggregates **actively maintained**, **Pi-hole-compatible** blocklists from reputable sources.  
All URLs are:

- 🌐 Served over **HTTPS**
- ✅ In **hosts** or **domain-only / Adblock**-compatible formats
- 🧪 Suitable for **Pi-hole v6+**

---

## 🔎 Quick Navigation  
<sub><code>material-icons: travel_explore</code></sub>

- [Legend](#-legend)
- [Ads](#-ads)
- [Adult](#-adult)
- [Crypto](#-crypto)
- [Malware](#-malware)
- [Mixed (combo lists)](#-mixed)
- [Phishing](#-phishing)
- [Suspicious / Threat-Intel](#-suspicious)
- [Telemetry](#-telemetry)
- [Implementation Notes](#-implementation-notes)

---

## 🧾 Legend  
<sub><code>material-icons: menu_book</code></sub>

- **Reputation (1–10)**  
  - 10 – Long-lived, widely trusted, very actively maintained, low false-positive history  
  - 8–9 – Strong, well-maintained, popular in the community  
  - 6–7 – Good quality but either newer, niche, or more aggressive (higher FP risk)

- **Approx. Entries**  
  - Rough domain/host counts where published by the project or widely referenced  
  - “—” means the project doesn’t clearly publish a count

- **Category values** (always sorted alphabetically):
  - `ads`, `adult`, `crypto`, `malware`, `phishing`, `suspicious`, `telemetry`, `tracking`, plus combinations.

---

## 📢 Ads  
<sub><code>material-icons: campaign</code></sub>

| Name | URL | Categories | Description | Maintainer | Last Updated* | Reputation | Approx. Entries | Notes |
|------|-----|------------|-------------|------------|---------------|-----------|-----------------|-------|
| RPiList EasyList Extended | `https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/easylist` | ads, tracking | DNS-converted EasyList variant focused on advertising and tracking domains. | RPiList / SemperVideo | Active (2025) | 8/10 | — | Solid ad/tracking layer; moderate size. Test alongside other large lists to avoid over-blocking. |

---

## 🔞 Adult  
<sub><code>material-icons: explicit</code></sub>

| Name | URL | Categories | Description | Maintainer | Last Updated* | Reputation | Approx. Entries | Notes |
|------|-----|------------|-------------|------------|---------------|-----------|-----------------|-------|
| OISD NSFW | `https://nsfw.oisd.nl` | adult, ads, tracking | Domain list focused on porn/shock/adult sites; NSFW superset of OISD Small. | OISD (sjhgvr) | Active (2025) | 9/10 | — | Strong adult/NSFW block; may block adult-adjacent but legitimate sites. Use only where adult blocking is explicitly required. |

---

## 🪙 Crypto  
<sub><code>material-icons: currency_bitcoin</code></sub>

| Name | URL | Categories | Description | Maintainer | Last Updated* | Reputation | Approx. Entries | Notes |
|------|-----|------------|-------------|------------|---------------|-----------|-----------------|-------|
| BlocklistProject Crypto | `https://raw.githubusercontent.com/blocklistproject/Lists/master/crypto.txt` | crypto, suspicious | Targets crypto-related abuse such as malicious mining and scammy crypto services. | The Blocklist Project | Active (2025) | 8/10 | — | Can interfere with some legitimate exchanges/wallets. Consider assigning to a specific “high-risk” or “untrusted devices” group. |

---

## 🦠 Malware  
<sub><code>material-icons: bug_report</code></sub>

| Name | URL | Categories | Description | Maintainer | Last Updated* | Reputation | Approx. Entries | Notes |
|------|-----|------------|-------------|------------|---------------|-----------|-----------------|-------|
| BlocklistProject Malware | `https://raw.githubusercontent.com/blocklistproject/Lists/master/malware.txt` | malware | Focused malware domain list from several threat sources, tuned for DNS blocking. | The Blocklist Project | Active (2025) | 9/10 | — | Strong general malware layer; good default security list with relatively low false-positive rate. |
| RPiList Malware | `https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/malware` | malware | German-maintained list blocking domains known to distribute malware. | RPiList / SemperVideo | Active (2025) | 8/10 | — | Good complement to other malware feeds; may be somewhat aggressive on “shady” download sites. |
| ThreatFox Hostfile | `https://threatfox.abuse.ch/downloads/hostfile/` | malware, phishing, suspicious | Hostfile of domain-based IOCs (C2, payload delivery, malware infra) from ThreatFox (abuse.ch). | abuse.ch (ThreatFox) | Rolling 6-month window | 9/10 | — | High-quality threat-intel feed. Excellent for security-focused networks; occasional FPs on newly-compromised but later-cleaned domains. |
| URLHaus Hostfile | `https://urlhaus.abuse.ch/downloads/hostfile/` | malware, phishing, suspicious | Hostfile of domains used to distribute malware URLs reported to URLHaus. | abuse.ch (URLHaus) | Updated multiple times per day | 10/10 | — (backed by a DB of millions of URLs) | One of the best current malware feeds. Heavy but very high-value; consider a dedicated “high-risk” group in Pi-hole. |

---

## 🧩 Mixed  
<sub><code>material-icons: layers</code> – combo lists (ads + tracking + malware + more)</sub>

| Name | URL | Categories | Description | Maintainer | Last Updated* | Reputation | Approx. Entries | Notes |
|------|-----|------------|-------------|------------|---------------|-----------|-----------------|-------|
| Hagezi Multi Normal | `https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/multi.txt` | ads, malware, phishing, suspicious, telemetry, tracking | Balanced multi-purpose blocklist combining numerous sources; tuned for normal daily use. | Hagezi | Active (2025) | 10/10 | ~267,000 | Excellent “do-most-things” list. Use the **Adblock format**, which is Pi-hole-compatible. Great as a primary baseline. |
| Hagezi Multi Pro | `https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/pro.txt` | ads, malware, phishing, suspicious, telemetry, tracking | More aggressive variant of Multi Normal, blocking additional ad/tracking and shady infrastructure. | Hagezi | Active (2025) | 8/10 | ~354,000 | **Aggressive blocking—test before production.** Consider for privacy-focused devices or a separate “strict” group. |
| OISD Big | `https://big.oisd.nl` | ads, malware, phishing, suspicious, telemetry, tracking | Large combination list aggregating many curated sources; covers ads, tracking, malware, and more. | OISD (sjhgvr) | Active (2025) | 9/10 | ~438,000 (approx.) | Very capable single “mega list”. Some reports of over-blocking; monitor logs and maintain an allowlist. |
| OISD Small | `https://small.oisd.nl` | ads, malware, tracking, telemetry | Reduced-size OISD variant focusing on the most important domains while remaining lighter. | OISD (sjhgvr) | Active (2025) | 10/10 | ~71,000 (approx.) | **Great default for home networks.** Good balance of coverage vs. breakage; pair with dedicated malware/phishing feeds. |
| StevenBlack Unified Hosts | `https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts` | ads, malware, suspicious, tracking | Long-standing unified hosts file aggregating several reputable sources (AdAway, MVPS, etc.) and deduplicating. | Steven Black | Very active; latest release Nov 2025 | 10/10 | ~110,000 (base unified) | Mature, widely used project. Substantial size; avoid piling on too many other “mega lists” to keep FPs and resource usage reasonable. |

---

## 🎣 Phishing  
<sub><code>material-icons: phishing</code></sub>

| Name | URL | Categories | Description | Maintainer | Last Updated* | Reputation | Approx. Entries | Notes |
|------|-----|------------|-------------|------------|---------------|-----------|-----------------|-------|
| BlocklistProject Phishing | `https://raw.githubusercontent.com/blocklistproject/Lists/master/phishing.txt` | phishing | Focused phishing list (credential-stealing sites, scam login pages, etc.). | The Blocklist Project | Active (2025) | 9/10 | — | Clean, focused phishing protection; relatively low false-positive rate. Good add-on to a mixed list. |
| Phishing Army | `https://phishing.army/download/phishing_army_blocklist.txt` | phishing | Dedicated phishing blocklist aggregating multiple feeds (e.g., PhishTank, OpenPhish). | Phishing Army (Andrea Draghetti) | Updated daily (ongoing) | 9/10 | — | Widely used for phishing protection. Excellent choice for strong anti-phishing coverage; pair with logging for rare FPs. |

---

## ⚠️ Suspicious / Threat-Intel  
<sub><code>material-icons: warning_amber</code></sub>

| Name | URL | Categories | Description | Maintainer | Last Updated* | Reputation | Approx. Entries | Notes |
|------|-----|------------|-------------|------------|---------------|-----------|-----------------|-------|
| BlocklistProject Ransomware | `https://raw.githubusercontent.com/blocklistproject/Lists/master/ransomware.txt` | malware, suspicious | Domains associated with ransomware operations (C2, payment portals, distribution). | The Blocklist Project | Active (2025) | 8/10 | — | Focused on high-risk domains. Low chance of impacting normal browsing; recommended where security is a priority. |
| BlocklistProject Scam | `https://raw.githubusercontent.com/blocklistproject/Lists/master/scam.txt` | phishing, suspicious | Targets scam domains (tech-support scams, refund fraud, fake shops, etc.). | The Blocklist Project | Active (2025) | 8/10 | — | Useful “safety net” for non-technical users; generally minimal impact on legitimate sites. |
| Hagezi Threat Intelligence Feeds (TIF) | `https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/tif.txt` | malware, phishing, suspicious | Threat-intel-driven blocklist (TIF) for high-risk infrastructure beyond general ad/tracking. | Hagezi | Active (2025) | 9/10 | — | Strong extra-hardening layer. Best for networks where malware targeting and C2 blocking are key concerns. May be overkill for very casual home setups. |

---

## 📡 Telemetry  
<sub><code>material-icons: sensors</code></sub>

| Name | URL | Categories | Description | Maintainer | Last Updated* | Reputation | Approx. Entries | Notes |
|------|-----|------------|-------------|------------|---------------|-----------|-----------------|-------|
| RPiList Win10 Telemetry | `https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Win10Telemetry` | telemetry, tracking | Focused list aimed at blocking Windows 10 telemetry and tracking endpoints/domains. | RPiList / SemperVideo | Active (2025) | 8/10 | — | Good choice if you specifically want to reduce Microsoft telemetry. Test carefully—can affect some cloud-based features. |

---

## 🛠 Implementation Notes  
<sub><code>material-icons: build_circle</code></sub>

### Suggested Baseline for a Home / Small-Org Network

1. **Pick one “mixed” baseline list:**
   - ✅ **Hagezi Multi Normal** – or –  
   - ✅ **OISD Small**

2. **Add security-focused lists:**
   - ✅ **URLHaus Hostfile**  
   - ✅ **ThreatFox Hostfile**  
   - ✅ **Phishing Army**

3. **Optional hardening (per client group):**
   - 🔐 **BlocklistProject** Malware / Phishing / Scam / Ransomware  
   - 🔞 **OISD NSFW** (only where adult blocking is required)  
   - 🧪 **Hagezi Multi Pro** + **Hagezi TIF** for strict / admin / lab devices  
   - 🪟 **RPiList Win10 Telemetry** for Windows-heavy environments

### Grouping Strategy (Pi-hole v6+)

- Put **aggressive lists** (Hagezi Pro, TIF, OISD Big, ThreatFox, URLHaus) into their own **Pi-hole groups**.
- Apply those groups only to:
  - Admin endpoints
  - Lab / testing devices
  - High-risk user segments
- Use **moderate lists** (e.g., OISD Small or Hagezi Multi Normal + one malware feed) for:
  - General staff / student devices
  - Guest Wi-Fi (with careful testing)

### Monitoring & Tuning

- Use Pi-hole’s **Query Log** and **Top Blocked Domains** to:
  - Quickly spot legitimate services being blocked.
  - Add domains to **whitelists** where appropriate.
- For large environments, consider:
  - Exporting query logs to a SIEM or central logging.
  - Creating a simple **block/allow request workflow** for end-users.

---

\* **“Last Updated”** values are approximate and based on observed project activity (commits/releases) in 2024–2025.  
Always verify current status directly from the project’s repository or homepage before relying on any list in production.
