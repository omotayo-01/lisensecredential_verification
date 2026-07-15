from typing import Any

def verify_ctia() -> dict[str, Any]:
    candidate = {
        "candidate_name": "Olatunji Timothy",
        "certificate_name": "CompTIA Security+",
        "issuing_body": "CompTIA",
        "credential_id": "CTA2022002005",
        "issue_date": "2022-03-01",
        "expiry_date": "2028-08-01"
    }

    verification_found = True

    result: dict[str, Any] = {
        "verificationResult": {
            "claimType": "certification",
            "status": "Unverified" if verification_found else "not_found",
            "confidenceScore": 30,
            "candidateClaim": candidate
        }
    }

    return result