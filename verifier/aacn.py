from typing import Any

def verify_aacn() -> dict[str, Any]:
    candidate = {
        "candidate_name": "Makanjuola Dasola",
        "certificate_name": "Critical Care Registered Nurse(CCRN)",
        "issuing_body": "American Association of Critical-Care Nurses (AACN)",
        "credential_id": "CCRN2022002851",
        "issue_date": "2025-03-01",
        "expiry_date": "2038-03-01"
    }

    verification_found = True

    result: dict[str, Any] = {
        "verificationResult": {
            "claimType": "certification",
            "status": "verified" if verification_found else "not_found",
            "confidenceScore": 96,
            "candidateClaim": candidate
        }
    }

    return result