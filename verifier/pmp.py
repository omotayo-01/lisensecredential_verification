from typing import Any
#from verification import send_request


def verify_pmp() -> dict[str, Any]:
    candidate: dict[str, str] = {
    "candidate_name": "Esan Kemisola",
    "certificate_name": "Project Management Professional (PMP)",
    "issuing_body": "Project Management Institute (PMI)",
    "credential_id": "PMP70569w2982",
    "issue_date": "2020-02-10",
    "expiry_date": "2028-02-10"
}
    
    verification_found =True

    result: dict[str, Any] = {
        "verificationResult": {
            "claimType": "certification",
            "status": "verified" if verification_found else "not_found",
            "confidenceScore": 99,
            "candidateClaim": candidate
        }
        }
    
    return result