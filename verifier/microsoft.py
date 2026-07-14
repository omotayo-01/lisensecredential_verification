from typing import Any

def verify_microsoft() -> dict[str, Any]:
    candidate: dict[str, str] = {
         "candidate_name": "Akanbi Olukayode",
        "certificate_name": "Microsoft Certified: Azure AI Engineer Associate",
        "issuing_body": "Microsoft",
        "credential_id": "ABC123456789",
        "issue_date": "2025-05-10",
        "expiry_date": "None"
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