# Network Monitor — Sipar Security

A lightweight, open-source network monitoring tool for real-time device tracking,
event logging, and ARP spoofing detection.

![Status](https://img.shields.io/badge/status-active%20development-yellow)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Features

- **Device Detection** — Discovers devices on your network via MAC address and IP
- **Real-Time Tracking** — Continuous scans every 10 seconds for online/offline status
- **Event Logging** — Timestamped logs for every connection and disconnection event
- **Web Dashboard** — Browser-based UI accessible via localhost
- **ARP Spoofing Detection** — Detects spoofing attempts *(in progress)*

---

## Requirements

- Python 3.8+
- Linux / Windows / macOS
- Root or Administrator privileges (required for ARP scanning)

---

## Installation

```bash
# Clone the repository
git clone https://github.com/siparsecurity/network-monitor.git
cd network-monitor

# Install dependencies
pip install -r requirements.txt

# Run the tool
sudo python main.py
```

---

## Usage

Once running, open your browser and go to:
http://localhost:5000

The dashboard will show all detected devices, their status, and event logs.

---

## Project Structure
network-monitor/
├── main.py              # Entry point
├── scanner.py           # Network scanning module
├── detector.py          # ARP spoofing detection (in progress)
├── logger.py            # Event logging
├── dashboard/           # Web UI
│   ├── templates/
│   └── static/
├── requirements.txt
└── README.md

---

## Roadmap

- [x] Device detection via ARP scan
- [x] Online/offline status tracking
- [x] Event logging with timestamps
- [x] Web dashboard UI
- [ ] ARP spoofing detection
- [ ] Email/SMS alerts
- [ ] Device naming and tagging
- [ ] Export logs to CSV

---

## About

Built by **Sipar Security** — a cybersecurity company from Pakistan focused on
practical, accessible security tools.

- 🌐 siparsecurity.com *(coming soon)*
- 📧 siparsecurity@gmail.com
- 💼 [LinkedIn](https://linkedin.com/company/siparsecurity)

---

## License

MIT License — see [LICENSE](LICENSE) for details.
