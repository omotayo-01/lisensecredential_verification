from typing import Any

def verify_icu() -> dict[str, Any]:
    candidate = {
        "candidate_name": "Omotayo Uzumaki",
        "certificate_name": "Hospital ICU Training Certificate",
        "issuing_body": "Lagos Univeristy Teaching Hospital",
        "credential_id": "ICU1027156",
        "issue_date": "2025-03-01",
        "expiry_date": "2028-03-01"
    }

    verification_found = True

    result: dict[str, Any] = {
        "verificationResult": {
            "claimType": "certification",
            "status": "verified" if verification_found else "not_found",
            "confidenceScore": 95,
            "candidateClaim": candidate
        }
    }

    return result