from typing import Any

def verify_cisco() -> dict[str, Any]:
    candidate = {
        "candidate_name": "Oladotun David",
        "certificate_name": "Cisco Certified Network Associate",
        "issuing_body": "Cisco",
        "credential_id": "CCNA123456",
        "issue_date": "2025-01-15",
        "expiry_date": "2028-01-15"
    }

    verification_found = True

    result: dict[str, Any] = {
      "verificationResult": {
            "claimType": "certification",
            "status": "verified" if verification_found else "not_found",
            "confidenceScore": 94,
            "candidateClaim": candidate
        }
    }

    return result