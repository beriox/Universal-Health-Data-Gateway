# 🌐 Universal Health Data Gateway (UHDG)

> **"Decentralized, Zero-Trust Health Data Portability for Emergency & Off-Grid Environments."**

---

### 🚀 LIVE INTERACTIVE SIMULATOR

> **🌐 Try the Demo:** **[Emergency Health Data Routing Simulator](https://beriox.github.io/Universal-Health-Data-Gateway/)**  
> *(Simulates real-time encrypted routing, jurisdictional compliance blocks, and potential integrations with open platforms like **OpenHospital** or travel onboarding software).*

---

[🇮🇹 Leggi la documentazione in Italiano](./README_IT.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Standard: HL7-FHIR](https://img.shields.io/badge/Standard-HL7%20FHIR%20R4-blue.svg)](https://hl7.org/fhir/)
[![Architecture: Zero--Trust](https://img.shields.io/badge/Architecture-Zero--Trust-green.svg)](#)

---

### 💡 The Vision
In a world where a postal parcel is tracked in real-time across dozens of customs offices and carriers, **a human being's life-saving medical data remains locked behind regional or bureaucratic silos**—right when emergencies, travel, rescue missions, or humanitarian relief occur.

**UHDG** is an open-source, neutral middleware acting as a **dynamic compliance orchestrator and personal consent manager**. It enables seamless, encrypted, and legally compliant medical data flows between heterogeneous sources and global destinations across any jurisdiction.

---

NEWS:

The matrix now covers the entire globe and clearly states EU (GDPR/EHDS), American (HIPAA/PIPEDA), African (POPIA/Malabo), Asian (PDPA/APEC) and Oceanian laws!


---

## 🗺️ Architectural Scenario: "Emergency & Cross-Border Anywhere"

```text
                               ┌────────────────────────────────────────┐
                               │       CITIZEN / PATIENT (SOVEREIGN)    │
                               │  Zero-Knowledge Encryption (AES-256)   │
                               └───────────────────┬────────────────────┘
                                                   │
                                                   ▼
┌────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 UHDG COMPLIANCE & ROUTING ENGINE                               │
│  - Geo-Context Detection (GPS/Satellite)          - Dynamic Rule Checker (GDPR / HIPAA / EHDS) │
│  - Trust Handshake (CSA STAR / OID / eIDAS)       - Immutable Zero-Logging & Auditing          │
└───────┬──────────────────────────────────────────┬─────────────────────────────────────┬───────┘
        │                                          │                                     │
        ▼                                          ▼                                     ▼
┌───────────────────────┐              ┌─────────────────────────┐           ┌───────────────────────┐
│     DATA SOURCES      │              │     STORAGE VAULT       │           │     DESTINATIONS      │
├───────────────────────┤              ├─────────────────────────┤           ├───────────────────────┤
│ • Hospitals / FHIR    │              │ • Global/EU/National    │           │ • Volunteer Doctor /  │
│ • OpenMRS (NGOs)      │ ───────────► │   (Big5/Gaia-X/Aruba/...│ ────────► │   On-board Air Crew   │
│ • Fitness Apps / IoT  │              │ • On-Prem/Regional/Local|           │ • Google Health /     │
│ • PDF/OCR Import      │              │   (Hospital/USB Key/... |           │   EU Health Space     │
└───────────────────────┘              └─────────────────────────┘           │ • Anti-Anxiety Update │
                                                                             │   for Family at Home  │
                                                                             └───────────────────────┘

💻 Included Simulator (demo_sim.py)
This repository includes a Python prototype demonstrating the core pipeline:

Raw lab result ingestion.

Normalization to HL7 FHIR R4 (Observation).

Symmetric AES-256 (Fernet) encryption using client-managed keys.

Payload decryption verification for authorized endpoints.

🚀 Quickstart

# Clone the repo
git clone [https://github.com/beriox/Universal-Health-Data-Gateway.git](https://github.com/beriox/Universal-Health-Data-Gateway.git)
cd uhc-gateway

# Install dependencies
pip install -r requirements.txt

# Run simulation
python demo_sim.py

You can see the generated output there: https://github.com/beriox/Universal-Health-Data-Gateway/blob/main/demo_output.txt

🤝 Call for Maintainers & Contributors
Note from the Author: This repository serves as a conceptual framework and architectural blueprint. I am looking for developers, digital health experts, NGOs, and emergency response teams to take over active maintenance, build source adaptors, and expand compliance rules.

"Making health data portable, secure, and boundary-free."
