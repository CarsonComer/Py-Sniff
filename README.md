# Py-Sniff
A Python-based network packet sniffer utilizing **Scapy** for targeted logging. Designed to filter network noise and export critical traffic data directly to a CSV file for security audits.

## Overview
Py-Sniff is a utility designed to capture live network traffic and log essential metadata—including MAC addresses, IP addresses, and protocols—into a CSV format for security analysis. This project was developed as a capstone to explore the intersection of network security and automation.

## 🛠 Prerequisites & Installation
* **Python 3.x**
* **Scapy Library:** Install the required dependencies using:
  ```bash
  pip install -r requirements.txt
  ```

## Crucial Usage Instructions
### Elevated Privileges Required
Because this script interacts with **raw network sockets**, it must be executed with root/administrative privileges. Standard users are restricted from sniffing network traffic by the Linux kernel for security reasons.

**To run the script correctly, use:**
  ```bash
  sudo python3 py_sniff.py
  ```

## About the Developer
* **Student Status:** I am currently a **Cybersecurity Major**. I want to preface that **I am not a professional programmer**; this project was created for the purpose of learning and testing.
* **Security Note:** As a student project, there may be bugs or security flaws present.
* **Disclaimer:** **USE AT YOUR OWN DISCRETION.** I am not responsible for any issues caused by running this script in a live or sensitive environment.
