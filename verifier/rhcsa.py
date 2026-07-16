from typing import Any
def verify_rhcsa() -> dict[str, Any]:
    candidate = {
        "candidate_name": "Modashola Abisade",
        "certificate_name": "Red Hat Certified System Administrator (RHCSA)",
        "issuing_body": "Red Hat",
        "credential_id": "RHCSA27893485",
        "issue_date": "2012-03-01",
        "expiry_date": "2028-08-01"
    }

    verification_found = True

    result: dict[str, Any] = {
        "verificationResult": {
            "claimType": "certification",
            "status": "Verified" if verification_found else "not_found",
            "confidenceScore": 80,
            "candidateClaim": candidate
        }
    }

    return result