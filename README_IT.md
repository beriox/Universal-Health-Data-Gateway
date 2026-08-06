### 5. `README_IT.md` (Italiano - Per il contesto locale/EU)

```markdown
# 🌍 Universal Health Data Gateway (UHC)
> **"Un Google Translate diplomatico, regolatorio e anti-ansia per la salute globale."**

[🇬🇧 Read documentation in English](./README.md)

---

### 💡 La Visione
In un mondo in cui un pacco spedito dall'altra parte del pianeta viene tracciato in tempo reale tra decine di dogane e vettori, **i dati sanitari salvavita di un essere umano rimangono murati in silos regionali o burocratici**, proprio nel momento dell'emergenza, di un viaggio, di un intervento di elisoccorso o di una missione umanitaria.

**UHC Gateway** è un middleware open source e neutrale che agisce come un **orchestratore di compliance dinamica e di consenso del cittadino**. Permette il passaggio di flussi clinici tra sorgenti eterogenee e destinazioni globali in modo legalmente ineccepibile, cifrato ed esteso a qualsiasi giurisdizione.

---

## ⚖️ Come risolve la "Palude Regolatoria"

1. **Compliance-as-Code:** L'engine verifica in tempo reale se il canale e il provider di destinazione soddisfano il set minimo di regole per la zona geografica corrente (es. GDPR, FSE, EHDS).
2. **Delega d'Emergenza Programmabile:** L'utente può pre-autorizzare il rilascio del *Patient Summary* essenziale solo in caso di emergenza verificata (es. medico di bordo o elisoccorso autenticato tramite federazione d'identità).
3. **Tranquillità Distribuita:** Consente l'invio di notifiche di stato di cura ai familiari a casa, rielaborando il dato nel rispetto della normativa della loro giurisdizione di destinazione.

---

## 🚀 Esecuzione Rapida del Prototipo

```bash
pip install -r requirements.txt
python demo_sim.py

You can see the generated output there: https://github.com/beriox/Universal-Health-Data-Gateway/blob/main/demo_output.txt


🤝 Chiamata alla Community
Nota dell'Autore: Questo repository è un segnaposto concettuale e un blueprint architetturale. L'obiettivo è delegare e coordinare la community open source (sviluppatori, esperti FHIR, ONG e soccorritori) per costruire insieme connettori, regole di compliance e integrazioni.

p.s. mio side-project:
https://prospetto-sanitario.blogspot.com/
