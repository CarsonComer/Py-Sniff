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

## 📈 Project Adversity & Learning
The most significant hurdle in this project was **overestimating my initial Python proficiency.** While I understood basic syntax, applying it to real-time network data was a steep learning curve.

* **The Challenge:** Translating raw packet data into a readable CSV format required a deeper understanding of the Scapy library than I initially anticipated.
* **The Pivot:** I shifted from trying to "code fast" to "learning deep," spending extra time in the Scapy documentation to ensure the parser handled various protocols correctly.
* **The Result:** This project significantly improved my ability to troubleshoot logical errors and reinforced my understanding of Linux file permissions and network security constraints.

## About the Developer
* **Student Status:** I am currently a **Cybersecurity Major**. I want to preface that **I am not a professional programmer**; this project was created for the purpose of learning and testing.
* **Security Note:** As a student project, there may be bugs or security flaws present.
* **Disclaimer:** **USE AT YOUR OWN DISCRETION.** I am not responsible for any issues caused by running this script in a live or sensitive environment.
