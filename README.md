# 🌐 Universal Health Data Gateway (UHDG)

> **"To make critical health data portable, secure, and available anywhere."**

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
In a highly interconnected global ecosystem, **ensuring the continuity of life-saving health data remains a complex challenge**—especially during international travel, cross-border emergencies, aeromedical retrievals, or missions in geographically isolated areas.

While existing public infrastructures (such as National EHR portals and cross-border interoperability networks) play a fundamental role, they often face technical or regulatory constraints when integrating real-time data from heterogeneous nodes: independent clinics, private diagnostic centers, third-country facilities, or temporary emergency stations.

**UHDG** is an open-source, neutral middleware designed to **complement and enhance these systems**, acting as a dynamic compliance orchestrator and personal consent manager. It enables the secure, encrypted flow of essential clinical data between diverse sources and global destinations, providing immediate technological and legal coverage wherever the citizen is located.

---

**🌍 UPDATE:** The compliance routing matrix now covers the entire globe, seamlessly integrating frameworks from the EU (GDPR/EHDS), Americas (HIPAA/PIPEDA), Africa (POPIA/Malabo), Asia (PDPA/APEC), and Oceania!

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
│ • Hospitals / FHIR    │              │ • Global/Regional/Nation│           │ • Volunteer Doctor /  │
│ • OpenMRS (NGOs)      │ ───────────► │   Clouds (Big5/Gaia-X/..│ ────────► │   On-board Air Crew   │
│ • Fitness Apps / IoT  │              │ • On-Prem/Regional/Local│           │ • Multi-Cloud Health /│
│ • PDF/OCR Import      │              │   (Hospital/USB Key/... │           │   EU Health Space /.. │
└───────────────────────┘              └─────────────────────────┘           │ • Status Update for   │
                                                                             │   Family / Next of Kin│
                                                                             └───────────────────────┘

💻 Included Simulator (CLI)This repository includes a Python prototype (demo_sim.py) demonstrating the core pipeline:  Raw lab result ingestion.  Normalization to HL7 FHIR R4 (Observation).  Symmetric AES-256 (Fernet) encryption using client-managed keys.  Payload decryption verification for authorized endpoints.  🚀 QuickstartBash# Clone the repo
git clone [https://github.com/beriox/Universal-Health-Data-Gateway.git](https://github.com/beriox/Universal-Health-Data-Gateway.git)
cd Universal-Health-Data-Gateway

# Install dependencies
pip install -r requirements.txt

# Run simulation
python demo_sim.py
You can see the generated output here:🔗 View demo_output.txt  🤝 Call for Maintainers & ContributorsNote from the Author: This repository serves as a conceptual framework and architectural blueprint[cite: 3]. I am looking for developers, digital health experts, NGOs, and emergency response teams to take over active maintenance, build source adaptors, and expand compliance rules[cite: 3].

## 📊 Data Sources & Global Health Node Registry

The simulator and routing matrix leverage real-world, open-access geographical and clinical datasets. To keep emergency routing fast and lightweight, the registry is structured into prioritized datasets:

### 1. Primary Emergency Nodes (High Priority)
Used for immediate emergency routing and critical payload delivery.
* **OpenStreetMap Overpass Query (Global Hospitals):**  
  🔗 [Query/Export Hospitals via Overpass Turbo](https://overpass-turbo.eu/?q=node%5B%22amenity%22%3D%22hospital%22%5D%3Bout%20body%3B)  
  *(Filters global entities tagged with `amenity=hospital` or `healthcare=hospital`)*.

### 2. Specialized & Secondary Clinical Nodes (Modular Datasets)
For specialized diagnostics, blood testing, and ambulatory services (e.g., blood banks, private laboratories, specialist clinics).
* **OpenStreetMap Healthcare Taxonomy:**  
  🔗 [OSM Healthcare Tagging Guidelines](https://wiki.openstreetmap.org/wiki/Key:healthcare)  
  *(Allows filtering sub-categories like `healthcare=laboratory`, `healthcare=blood_donation`, or `amenity=clinic`)*.
* **Public FHIR Endpoints & Directories:**  
  🔗 [HL7 FHIR Official Registry Directory](https://registry.fhir.org/)  
  *(Publicly indexed FHIR R4 server endpoints for direct API handshake)*.

---
💡 **Want to contribute or register a new node?**  
Healthcare providers, developers, and NGOs can register their facility simply by adding or updating their location directly on OpenStreetMap (using amenity=hospital or healthcare=* tags), making it instantly available to the open network.
