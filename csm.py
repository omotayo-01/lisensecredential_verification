from typing import Any

def verify_csm() -> dict[str, Any]:
    candidate = {
        "candidate_name": "Olatunji Timothy",
        "certificate_name": "Certified Scrum Master(CSM)",
        "issuing_body": "Certified Scrum Alliance",
        "credential_id": "CSA029982927",
        "issue_date": "2022-03-01",
        "expiry_date": "2028-08-01"
    }

    verification_found = True

    result: dict[str, Any] = {
        "verificationResult": {
            "claimType": "certification",
            "status": "Possible match" if verification_found else "not_found",
            "confidenceScore": 70,
            "candidateClaim": candidate
        }
    }

    return result