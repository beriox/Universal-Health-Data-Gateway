### 5. `README_IT.md` (Italiano - Per il contesto locale/EU)

```markdown
# 🌍 Universal Health Data Gateway (UHDG)
> **"Rendere i dati sanitari essenziali portatili, sicuri e disponibili ovunque."**

[🇬🇧 Read documentation in English](./README.md)

---

### 🚀 SIMULATORE INTERATTIVO LIVE
> **🌐 Prova la Demo:** **[Emergency Health Data Routing Simulator](https://beriox.github.io/Universal-Health-Data-Gateway/)**  
> *(Simula l'instradamento cifrato in tempo reale, i blocchi di conformità giurisdizionale e le potenziali integrazioni con piattaforme aperte come **OpenHospital** o software di onboarding per operatori di viaggio).*

---

### 💡 La Visione
In un ecosistema globale fortemente interconnesso, **la continuità del dato sanitario salvavita rappresenta ancora una sfida complessa**, specialmente durante viaggi, emergenze transfrontaliere, interventi d'elisoccorso, contesti di lavoro o missioni in aree geograficamente e infrastrutturalmente isolate.

Le infrastrutture pubbliche esistenti (come i portali EHR nazionali, i fascicoli regionali e le reti di interoperabilità transfrontaliere) svolgono un ruolo fondamentale. Tuttavia, incontrano spesso vincoli tecnici o normativi nell'integrare in tempo reale i dati provenienti da nodi eterogenei: cliniche indipendenti, centri diagnostici privati, laboratori specializzati, strutture di Paesi terzi o postazioni temporanee d'emergenza.

**UHC Gateway** nasce come middleware open source e neutrale per **affiancare e potenziare questi sistemi**, agendo come un orchestratore di compliance dinamica e di consenso del cittadino. Permette il passaggio sicuro e cifrato di flussi clinici tra sorgenti eterogenee e destinazioni globali, fornendo una copertura tecnologica e giuridica immediata ovunque si trovi la persona.

---

## ⚖️ Risoluzione dei Blocchi Regolatori e Interoperabilità

1. **Compliance-as-Code:** L'engine verifica in tempo reale se il canale e la destinazione soddisfano il set minimo di regole per la giurisdizione interessata (es. GDPR, EHDS, HIPAA, o framework locali) senza violare i processi decisionali e le sovranità nazionali.
2. **Delega d'Emergenza Programmabile:** Il cittadino rimane il proprietario della propria chiave crittografica e può pre-autorizzare il rilascio del *Patient Summary* essenziale (standard HL7 FHIR R4) solo in caso di emergenza verificata (es. personale medico, soccorritori o medici di bordo autenticati).
3. **Ponte per le Strutture Isolate e P2P:** Consente anche a strutture ospedaliere minori, cliniche private o stazioni mediche di ONG (come la rete *OpenHospital*) di accreditarsi come nodi sicuri della rete, garantendo il passaggio del dato senza costringere le amministrazioni a complessi stravolgimenti infrastrutturali.

---

## 🚀 Esecuzione Rapida del Prototipo (CLI)

```bash
pip install -r requirements.txt
python demo_sim.py
I dettagli dell'output generato dalla simulazione sono consultabili nel repository:

🔗 Visualizza output della demo (demo_output.txt)

🤝 Chiamata alla Community
Nota dell'Autore: Questo repository è un blueprint architetturale e un modello concettuale aperto. L'obiettivo è coordinare e coinvolgere la community open source (sviluppatori, architetti di sicurezza, esperti HL7 FHIR, ONG e organizzazioni di soccorso) per sviluppare insieme connettori, regole di compliance e integrazioni modulari.

Progetto di ricerca indipendente: prospetto-sanitario.blogspot.com

## 📊 Fonti Dati e Registro dei Nodi Sanitari Globali

Il simulatore e la matrice di routing utilizzano dataset geografici e clinici aperti e reali. Per garantire che l'instradamento d'emergenza rimanga ultra-veloce, il registro è organizzato in dataset prioritari e modulari:

### 1. Nodi d'Emergenza Primari (Alta Priorità)
Utilizzati per l'instradamento immediato e la gestione delle emergenze critiche.
* **Query OpenStreetMap Overpass (Ospedali Globali):**  
  🔗 [Query/Export Ospedali via Overpass Turbo](https://overpass-turbo.eu/?q=node%5B%22amenity%22%3D%22hospital%22%5D%3Bout%20body%3B)  
  *(Estrae a livello globale le strutture taggate con `amenity=hospital` o `healthcare=hospital`)*.

### 2. Nodi Clinici Specializzati e Secondari (Dataset Modulari)
Dedicati a diagnostica specialistica, analisi del sangue e servizi ambulatoriali (es. laboratori privati, centri prelievi, cliniche specialistiche).
* **Tassonomia Sanitaria OpenStreetMap:**  
  🔗 [Guida al Tagging Sanitario su OSM](https://wiki.openstreetmap.org/wiki/Key:healthcare)  
  *(Permette di filtrare sottocategorie come `healthcare=laboratory`, `healthcare=blood_donation` o `amenity=clinic`)*.
* **Registri Pubblici degli Endpoint FHIR:**  
  🔗 [Registro Ufficiale HL7 FHIR](https://registry.fhir.org/)  
  *(Endpoint FHIR R4 indicizzati pubblicamente per il puntamento diretto delle API)*.

---
💡 **Vuoi contribuire o registrare un nuovo nodo?**  
Strutture sanitarie, sviluppatori e ONG possono censire la propria sede semplicemente aggiungendo o aggiornando le informazioni della struttura direttamente su OpenStreetMap (utilizzando i tag amenity=hospital o healthcare=*), rendendola subito disponibile all'ecosistema aperto
