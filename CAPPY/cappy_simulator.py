from __future__ import annotations

import argparse
import os

try:
    from .adapters import AwsCloudAdapter, AzureCloudAdapter, FSEAdapter, FhirAdapter, GoogleCloudAdapter, HealthDataGateway
    from .compliance import ComplianceEvaluator, RoutingPolicy
    from .models import Allergy, Consent, Encounter, HealthData, Medication, Observation, Patient
except ImportError:  # pragma: no cover - allows running the file directly
    import sys

    sys.path.append(os.path.dirname(__file__))
    from adapters import AwsCloudAdapter, AzureCloudAdapter, FSEAdapter, FhirAdapter, GoogleCloudAdapter, HealthDataGateway
    from compliance import ComplianceEvaluator, RoutingPolicy
    from models import Allergy, Consent, Encounter, HealthData, Medication, Observation, Patient


def sample_health_data() -> HealthData:
    patient = Patient(
        id="patient-001",
        name="Jane Doe",
        birth_date="1988-02-18",
        sex="female",
        country="IT",
        language="en",
    )

    return HealthData(
        patient=patient,
        observations=[
            Observation(
                code="8480-6",
                display="Systolic blood pressure",
                value=122,
                unit="mmHg",
                effective_date="2026-08-18",
            )
        ],
        medications=[
            Medication(
                name="Metformin",
                dose="500 mg",
                frequency="BID",
                start_date="2026-07-01",
            )
        ],
        allergies=[
            Allergy(substance="Penicillin", reaction="Rash", severity="moderate")
        ],
        encounters=[
            Encounter(
                id="enc-001",
                type="ambulatory",
                status="finished",
                start="2026-08-17T09:00:00Z",
                facility="Milan Clinic",
            )
        ],
        consents=[
            Consent(
                subject="patient-001",
                scope="clinical-routing",
                granted=True,
                jurisdiction="EU",
            )
        ],
        source="sample",
        source_system="demo",
        metadata={"demo": True},
    )


def sample_fhir_bundle() -> dict:
    return {
        "resourceType": "Bundle",
        "type": "collection",
        "entry": [
            {
                "resource": {
                    "resourceType": "Patient",
                    "id": "patient-001",
                    "name": [{"given": ["Jane"], "family": "Doe"}],
                    "gender": "female",
                    "birthDate": "1988-02-18",
                    "address": [{"country": "IT"}],
                    "communication": [{"language": {"text": "English"}}],
                }
            },
            {
                "resource": {
                    "resourceType": "Observation",
                    "status": "final",
                    "code": {
                        "coding": [{"code": "8480-6"}],
                        "text": "Systolic blood pressure",
                    },
                    "valueQuantity": {"value": 122, "unit": "mmHg"},
                    "effectiveDateTime": "2026-08-18",
                }
            },
            {
                "resource": {
                    "resourceType": "MedicationStatement",
                    "status": "active",
                    "medicationCodeableConcept": {"text": "Metformin"},
                    "effectivePeriod": {"start": "2026-07-01"},
                    "dosage": [{"text": "500 mg", "timing": {"code": {"text": "BID"}}}],
                }
            },
        ],
    }


def sample_smartwatch_cloud_sources() -> dict:
    """Return illustrative smartwatch-platform payloads for the cloud-to-FSE scenario."""
    return {
        "apple-healthkit": {
            "platform": "Apple HealthKit / Apple Watch",
            "measurements": [{"type": "heart_rate", "value": 72, "unit": "bpm"}],
            "authorization": "citizen-approved session",
        },
        "huawei-health-kit": {
            "platform": "Huawei Health Kit / Huawei Watch",
            "measurements": [{"type": "heart_rate", "value": 74, "unit": "bpm"}],
            "authorization": "citizen-approved session",
        },
    }


def sample_openhospital_payload(health_data: HealthData) -> dict:
    """Return a destination-neutral OpenHospital integration example."""
    return {
        "destination": "OpenHospital-compatible endpoint",
        "patient_id": health_data.patient.id,
        "clinical_summary": {
            "observations": [obs.__dict__ for obs in health_data.observations],
            "medications": [med.__dict__ for med in health_data.medications],
        },
        "authorization": "authorized emergency-care session",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the CAPPY health-data simulator in simulated mode.")
    parser.add_argument(
        "--simulated",
        action="store_true",
        help="Force the sample to run without external cloud credentials or live contracts.",
    )
    parser.add_argument(
        "--mode",
        choices=("simulated", "live"),
        default=None,
        help="Use simulated mode; live provider integrations are not implemented yet.",
    )
    return parser.parse_args()


def api_exchange(source: str, target: str, endpoint: str, payload: dict, method: str = "POST") -> dict:
    """Return an illustrative API-style exchange; no network request is sent."""
    return {
        "request": {
            "method": method,
            "source": source,
            "target": target,
            "endpoint": endpoint,
            "payload": payload,
        },
        "response": {
            "status": 202,
            "accepted": True,
            "message": f"{target.upper()} accepted the health-data exchange.",
            "transaction_id": f"tx-{source}-{target}-demo",
        },
    }


def main() -> None:
    args = parse_args()

    requested_mode = args.mode or os.getenv("UHDG_MODE")
    if requested_mode == "live":
        raise SystemExit(
            "Live integrations are not implemented in this sample yet. "
            "Use --simulated or omit --mode."
        )

    mode = "simulated"
    gateway = HealthDataGateway()
    gateway.register(FhirAdapter())
    gateway.register(FSEAdapter())
    gateway.register(AzureCloudAdapter())
    gateway.register(AwsCloudAdapter())
    gateway.register(GoogleCloudAdapter())

    data = sample_health_data()
    fhir_bundle = sample_fhir_bundle()
    policy = RoutingPolicy(jurisdiction="EU", allowed_regions=["IT", "DE", "FR"], requires_consent=True)
    evaluator = ComplianceEvaluator(policy)
    smartwatch_sources = sample_smartwatch_cloud_sources()
    openhospital_payload = sample_openhospital_payload(data)

    print(f"Demo mode: {mode}")
    if mode == "simulated":
        print("Simulated mode: no live cloud contracts or provider credentials are required.")
        print("Transport note: exchanges are illustrative in-memory messages; no HTTPS request is sent.")

    print("\nDemo journey:")
    print("1. Read health data from an EU healthcare structure using FHIR.")
    print("2. Check jurisdiction, consent, and routing rules before transmission.")
    print("3. Normalize data so a multi-cloud application can work with it.")
    print("4. Write normalized data to an EU healthcare structure using FHIR.")
    print("5. Prepare data for an FSE exchange from an authorized application or institution.")
    print("6. Prepare a temporary cloud transfer authorized by the citizen.")
    print("7. Illustrate smartwatch monitoring data read from a cloud platform and prepared for FSE.")
    print("8. Illustrate temporary cloud sharing for in-flight assistance or care in another country.")
    print("9. Illustrate routing an authorized clinical summary to an OpenHospital-compatible endpoint.")

    round_tripped = gateway.read("fhir", fhir_bundle)

    print("\nStep 1 - FHIR read from EU healthcare structure:", round_tripped.to_dict())
    print("Step 2 - Legal and routing decision:", evaluator.route_decision(data))
    print("Step 3 - Canonical HealthData model:", data.to_dict())
    print("Step 4 - FHIR write to EU healthcare structure:", gateway.write("fhir", data))

    fse_payload = gateway.write("fse", data)
    azure_payload = gateway.write("azure", data)
    aws_payload = gateway.write("aws", data)
    google_payload = gateway.write("google-cloud", data)

    print("\nStep 5 - FSE payload:", fse_payload)
    print("FSE API exchange example:", api_exchange("fhir", "fse", "/api/v1/clinical-ingest", fse_payload))
    print("\nStep 6 - Cloud payload examples:")
    print("Azure payload:", azure_payload)
    print("Azure API exchange example:", api_exchange("fhir", "azure", "/health/v1/records", azure_payload))
    print("AWS payload:", aws_payload)
    print("AWS API exchange example:", api_exchange("fhir", "aws", "/route/health-records", aws_payload))
    print("Google Cloud payload:", google_payload)
    print("Google Cloud API exchange example:", api_exchange("fhir", "google-cloud", "/v1beta1/health/ingest", google_payload))

    print("\nSmartwatch cloud -> FSE examples:")
    for platform_name, smartwatch_payload in smartwatch_sources.items():
        print(f"{platform_name} read example:", smartwatch_payload)
        print(
            f"{platform_name} -> FSE exchange example:",
            api_exchange(platform_name, "fse", "/api/v1/clinical-ingest/wearables", smartwatch_payload),
        )

    print("\nOpenHospital integration example:")
    print("OpenHospital-compatible payload:", openhospital_payload)
    print(
        "OpenHospital API exchange example:",
        api_exchange("authorized-source", "openhospital", "/api/v1/health-records", openhospital_payload),
    )

    print("Cross-system summary:", {
        "providers": ["fhir", "fse", "azure", "aws", "google-cloud"],
        "interop_pattern": "FHIR canonical model -> provider-specific envelopes",
        "status": mode,
    })


if __name__ == "__main__":
    main()
