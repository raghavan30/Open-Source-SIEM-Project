# 📌 Open-Source SIEM Project (ELK + Python)

## 📖 Overview
This project demonstrates the implementation of a Security Information and Event Management (SIEM) system using entirely open-source tools.

The system collects Ubuntu authentication logs (`auth.log`), processes them through the ELK stack (Elasticsearch, Logstash, Kibana), and detects brute-force login attempts using a custom Python detection script.

This project simulates a real-world SOC (Security Operations Center) monitoring environment.

---

## 🎯 Objective
Build a functional SIEM that:

- Collects Linux authentication logs
- Stores logs in Elasticsearch
- Visualizes events in Kibana
- Detects brute-force attacks using Python
- Demonstrates alerting capabilities
- Maintains structured documentation in GitHub

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| Ubuntu Linux | Log source |
| Elasticsearch (OSS) | Log storage & search engine |
| Logstash | Log ingestion & parsing |
| Kibana | Visualization & dashboards |
| Python 3 | Brute-force detection script |
| Git & GitHub | Version control & documentation |

---

## 🏗️ Architecture

```
/var/log/auth.log
        ↓
     Logstash
        ↓
  Elasticsearch (auth-logs index)
        ↓
     Kibana Dashboard
        ↓
 Python Brute-Force Detector
```

---

## ⚙️ Implementation Steps

### 1️⃣ Install ELK Stack

```bash
sudo systemctl status elasticsearch
sudo systemctl status logstash
sudo systemctl status kibana
```

---

### 2️⃣ Configure Logstash

- Input: `/var/log/auth.log`
- Output index: `auth-logs`
- Applied Grok filter for authentication parsing

---

### 3️⃣ Store Logs in Elasticsearch

```bash
curl -k -u elastic:<password> https://localhost:9200/_cat/indices?v
```

---

### 4️⃣ Visualize in Kibana

- Created Data View: `auth-logs`
- Used Discover to explore logs
- Built dashboard for:
  - Failed login attempts
  - Login trends over time
  - Source IP analysis

---

### 5️⃣ Python Brute-Force Detector

Script: `brute_force_detector.py`

Detection Logic:
- Search for `"Failed password"`
- Time window: Last 5 minutes
- Alert if attempts > 5 from same IP

Example Alert:

```
⚠️ ALERT: Possible brute-force attack detected from IP: 127.0.0.1
```

---

## 📂 Repository Structure

```
Open-Source-SIEM-Project/
│
├── brute_force_detector.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📦 Setup Instructions

### Clone Repository

```bash
git clone https://github.com/<your-username>/Open-Source-SIEM-Project.git
cd Open-Source-SIEM-Project
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Detection Script

```bash
python brute_force_detector.py
```

---

## 🔐 Security Considerations

- Elasticsearch secured with authentication
- TLS enabled for HTTPS communication
- Kibana encryption keys configured
- `.gitignore` excludes sensitive files

---

## 🚨 Features

- Real-time log ingestion
- Secure Elasticsearch communication
- Custom Kibana dashboards
- Python-based brute-force detection
- Fully open-source implementation

---

## 📌 Learning Outcomes

- ELK stack deployment
- Log parsing and indexing
- Elasticsearch querying
- Kibana visualization
- SIEM alerting concepts
- GitHub project structuring

---

## 👤 Author

**Raghavan M**

---

## ⭐ Project Status

✅ Completed – Functional Open-Source SIEM Implementation  
