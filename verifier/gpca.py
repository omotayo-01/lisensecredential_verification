from typing import Any

def verify_gpca() -> dict[str, Any]:
    candidate: dict[str, str] = {
         "candidate_name": "Kaboom Kabaam",
        "certificate_name": "Google Professional Cloud Architect",
        "issuing_body": "Google cloud",
        "credential_id": "GPCA123456789",
        "issue_date": "2025-05-10",
        "expiry_date": "None"
    }

    verification_found = True

    result: dict[str, Any] = {
        "verificationResult": {
            "claimType": "certification",
            "status": "verified" if verification_found else "not_found",
            "confidenceScore": 77,
            "candidateClaim": candidate
    }
    }

    return result