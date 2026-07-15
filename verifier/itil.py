from typing import Any
def verify_itil() -> dict[str, Any]:
    candidate: dict[str, str] = {
    "candidate_name": "Goodyear Ebele",
    "certificate_name": "ITIL 4 Foundation",
    "issuing_body": "PeopleCert",
    "credential_id": "ITIL123456",
    "issue_date": "2020-02-10",
    "expiry_date": "2027-02-10"
}
    
    verification_found =True

    result: dict[str, Any] = {
        "verificationResult": {
            "claimType": "certification",
            "status": "Possible match" if verification_found else "not_found",
            "confidenceScore": 70,
            "candidateClaim": candidate
        }
        }
    
    return result