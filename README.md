# Historical IP Finder

Track historical A records for any domain using SecurityTrails API.

---

## About

**Historical IP Finder** is a lightweight Python tool that allows security researchers,
bug bounty hunters, and network analysts to fetch historical A records of domains. 
Discover all IP addresses associated with a domain over time and understand its hosting changes.

---

## Features

- Query historical DNS A records for any domain.
- Output unique IP addresses in a clean format.
- Minimal dependencies, fast and easy to use.
- Integrates easily into recon or pentesting workflows.

---

## Installation

```bash
git clone https://github.com/vux06/Historical-ip-finder.git
cd historical-ip-finder
pip install -r requirements.txt
```
---

## API Key

Before using the tool, add your SecurityTrails API key in the script.
Open historical_ip_finder.py and replace the placeholder:

```api_key = "YOUR_API_KEY"```
