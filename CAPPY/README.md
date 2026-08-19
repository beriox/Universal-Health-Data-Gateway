<p align="center">
   <img src="CAPPY.png" alt="CAPPY, the capybara healthcare routing mascot" width="180" />
</p>

# 🦫 CAPPY: Capybara Adaptive Payload Processing for You

> *The universal, decoupled, citizen-centric emergency health data routing engine.*


### 🗺️ Navigation Map (Start Here)

If you are visiting this repository for the first time, use this quick map:

* 📄 **[`MANIFEST.md`](../MANIFEST.md)** – Strategic vision, architecture, and emergency use cases.
* 🔌 **[`INTEGRATIONS.md`](INTEGRATIONS.md)** – JSON/FHIR R4 code examples (FSE 2.0, Google, Azure, AWS).
* 🌐 **[`ROADMAP.md`](ROADMAP.md)** – Global localization presets (`AirCappy`, `FseCappy`, `WearyCappy`, etc.).
* 🛫 **[AirCappy prototype](https://beriox.github.io/Universal-Health-Data-Gateway/)** – UHDG's interactive example of emergency, geographic, and compliance-aware routing.
* 🧩 **Core module placeholders:** [`AirCappy`](AirCappy/), [`FseCappy`](FseCappy/), [`CappyHospital`](CappyHospital/), [`WearyCappy`](WearyCappy/).
* 🤖 **[`Contributors Guidelines`](../.github/PROJECT-CONTEXT.md)** – Context rules for AI code assistants & contributors.


### 🚀 Quick Start
```bash
python cappy_simulator.py
```

The script runs in simulated mode by default; cloud connection variables are not required or used.

### Explicit simulated mode

```bash
python3 "CAPPY/cappy_simulator.py" --simulated
```

The complete example output is available in [`demo-output.txt`](demo-output.txt), so the
interop flow can be reviewed directly on GitHub without running Python.

There is no live mode yet. Supplying credentials or `UHDG_MODE=live` does not create a real
connection; the script rejects live mode explicitly until transport, authentication, endpoint
configuration, and provider-specific clients are implemented.

## What the journey demonstrates

The demo is intentionally understandable as a health-data journey, even for readers who do not
work with APIs every day:

1. Read a record from an EU healthcare structure through FHIR.
2. Check jurisdiction, consent, and routing rules before transmission.
3. Normalize the record into the shared `HealthData` model.
4. Prepare a FHIR record for an EU healthcare structure.
5. Prepare an FSE exchange for an authorized application or institution.
6. Prepare a temporary cloud transfer authorized by the citizen.
7. Illustrate smartwatch monitoring data read from a cloud platform and prepared for FSE.
8. Illustrate temporary cloud sharing for in-flight assistance or care in another country.
9. Illustrate routing an authorized clinical summary to an OpenHospital-compatible endpoint.

The last steps print illustrative API messages, but do not send HTTPS requests. They show the
shape of a future integration while keeping this proof of concept safe to run locally.

## More paths

Future pathways, integration notes, and modular project directions are collected in
[`ROADMAP.md`](ROADMAP.md). This keeps the CAPPY entry point concise while preserving the larger architecture for contributors and future project teams.

The current illustrative source/destination adapters are grouped under [`WearyCappy`](WearyCappy/)
and [`FseCappy`](FseCappy/). They can be imported by the simulator, but do not call vendor or
public-authority APIs yet.
