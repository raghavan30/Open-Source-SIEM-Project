# 📌 Open-Source SIEM Project (ELK + Python)

## 📖 Overview
This project demonstrates the implementation of a Security Information and Event Management (SIEM) system using entirely open-source tools.

The system collects Ubuntu authentication logs (auth.log), processes them through the ELK stack (Elasticsearch, Logstash, Kibana), and detects brute-force login attempts using a custom Python script.

---

## 🎯 Objective
Build a functional SIEM that:
- Collects Linux authentication logs
- Stores logs in Elasticsearch
- Visualizes events in Kibana
- Detects brute-force attacks using Python
- Demonstrates alerting capabilities

---

## 🛠️ Technologies Used
- Ubuntu Linux
- Elasticsearch (OSS)
- Logstash
- Kibana
- Python 3
- Git & GitHub

---

## 🏗️ Architecture
auth.log → Logstash → Elasticsearch → Kibana → Python Detection Script

---

## ⚙️ Implementation Steps

### 1️⃣ Install ELK Stack
Installed and verified:
sudo systemctl status elasticsearch
sudo systemctl status logstash
sudo systemctl status kibana

### 2️⃣ Configure Logstash
- Input: /var/log/auth.log
- Output index: auth-logs

### 3️⃣ Store Logs in Elasticsearch
Verify:
curl -k -u elastic:<password> https://localhost:9200/_cat/indices?v

### 4️⃣ Visualize in Kibana
- Created Data View: auth-logs
- Used Discover to explore logs
- Built dashboards for failed logins

### 5️⃣ Python Brute-Force Detector
Script: brute_force_detector.py

Detection Logic:
- Search for "Failed password"
- Time window: Last 5 minutes
- Alert if attempts > 5 from same IP

Example Alert:
⚠️ ALERT: Possible brute-force attack detected from IP: 127.0.0.1

---

## 📂 Repository Structure
Open-Source-SIEM-Project/
│
├── brute_force_detector.py
├── requirements.txt
├── .gitignore
└── README.md

---

## 📦 Setup Instructions

Clone:
git clone https://github.com/<your-username>/Open-Source-SIEM-Project.git
cd Open-Source-SIEM-Project

Create virtual environment:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Run detection:
python brute_force_detector.py

---

## 🚨 Features
- Real-time log ingestion
- Secure Elasticsearch communication
- Kibana dashboards
- Python-based brute-force detection
- Open-source implementation

---

## 📌 Learning Outcomes
- ELK stack deployment
- Log parsing and indexing
- Elasticsearch querying
- Kibana visualization
- SIEM alerting concepts
- GitHub project management

---

## 👤 Author
Raghavan M

---

## ⭐ Project Status
Completed – Functional Open-Source SIEM Implementation
