# ❓ Frequently Asked Questions (FAQ)

---

### ⚖️ 1. Is a system like this legally compliant and defensible?
**Yes.** The architecture is designed around key global data protection principles:
* **Data Minimization:** Only critical, life-saving payload data (*Patient Summary* via HL7 FHIR R4) is routed during an emergency—not entire medical histories.
* **Vital Interest & Consent:** Under frameworks like **GDPR (Art. 9.2.c)**, processing health data is explicitly lawful when necessary to protect the vital interests of the data subject. In non-emergency scenarios, explicit pre-authorization by the sovereign citizen applies.
* **End-to-End Encryption & Qualified Recipients:** Payloads are encrypted client-side (AES-256) and can only be decrypted by authenticated, authorized medical endpoints or emergency responders.

---

### 🏛️ 2. What if national or regional authorities (e.g., EU / Italian FSE) decide to implement this within their official processes?
**That is the ultimate goal.** This project is a **Proof of Concept (PoC) and Architectural Blueprint**, not a proprietary or competing commercial service. If public administrations or international organizations integrate these zero-trust, P2P cross-border routing concepts into official frameworks (such as the European Health Data Space or MyHealth@EU), the PoC will have fulfilled its core mission of architectural facilitation.

---

### 🌐 3. Why use a P2P / Decentralized approach instead of a central global database?
A centralized global database of health records would be a catastrophic single point of failure, a primary target for cyberattacks, and a geopolitical nightmare regarding data sovereignty. A decentralized P2P routing approach ensures that:
1. **Data stays at the source** until explicitly needed.
2. **Jurisdictional sovereignty** is preserved via localized compliance checks (*Compliance-as-Code*).
3. **Off-grid and isolated facilities** (e.g., field hospitals, island clinics, maritime or aerospace nodes) can participate without requiring constant connection to a central state infrastructure.

---

### 🤖 4. Does this project use Artificial Intelligence? What about the EU AI Act?
The core simulator and routing engine are **100% deterministic code** (Python, JavaScript, AES-256 encryption, HL7 FHIR parsing). No AI models or LLMs run inside the routing pipeline, meaning it carries **zero AI-related compliance risks**. Should future modular extensions incorporate AI (e.g., automated clinical summary translation), a formal **EU AI Act Impact Assessment** will be provided.

---

# ❓ Domande Frequenti (FAQ - Italiano)

---

### ⚖️ 1. Uno strumento del genere è legalmente conforme e difendibile?
**Sì.** L'architettura è progettata attorno ai principali principi internazionali di protezione dei dati:
* **Minimizzazione del dato:** In emergenza viene instradato solo il dataset clinico essenziale (*Patient Summary* in formato HL7 FHIR R4), non l'intera storia clinica.
* **Interesse Vitale e Consenso:** Ai sensi del **GDPR (Art. 9.2.c)**, il trattamento dei dati sanitari è esplicitamente lecito per tutelare un interesse vitale dell'interessato. In contesti non urgenti, si applica la pre-autorizzazione del cittadino.
* **Crittografia End-to-End e Destinatari Qualificati:** Il dato viaggia cifrato alla fonte (AES-256) ed è decifrabile esclusivamente da nodi medici o soccorritori autenticati e autorizzati.

---

### 🏛️ 2. Cosa succede se le autorità pubbliche (es. UE o FSE) volessero integrarlo nei loro processi ufficiali?
**È esattamente l'obiettivo del progetto.** Questo repository è una **Proof of Concept (PoC) e un Blueprint Architetturale**, non un servizio commerciale concorrente. Se le Pubbliche Amministrazioni o i network europei/internazionali integreranno queste logiche di instradamento sicuro nei propri sistemi ufficiali, il progetto avrà raggiunto il suo scopo primario di stimolo e facilitazione.

---

### 🌐 3. Perché un approccio P2P/Decentralizzato anziché un database globale centralizzato?
Un database centralizzato mondiale dei dati sanitari rappresenterebbe un singolo punto di vulnerabilità critico e un problema insolubile di sovranità nazionale. L'approccio decentralizzato garantisce che:
1. **Il dato rimane alla fonte** finché non è strettamente necessario.
2. **La sovranità delle singole giurisdizioni** viene rispettata tramite controlli di compliance locali (*Compliance-as-Code*).
3. **Strutture isolate o temporanee** (ospedali da campo, cliniche su isole, navi o missioni) possono operare anche senza una connessione permanente a un'infrastruttura statale centrale.

---

### 🤖 4. Il progetto utilizza l'Intelligenza Artificiale? È conforme all'EU AI Act?
Il motore di simulazione e routing è composto da **codice 100% deterministico** (Python, JS, crittografia AES-256, standard FHIR). Non ci sono modelli IA in esecuzione nel flusso dei dati. Se in futuro verranno sviluppati moduli aggiuntivi basati su IA (es. traduzione automatica delle cartelle cliniche), verrà allegato un **AI Impact Assessment conforme all'EU AI Act**.
