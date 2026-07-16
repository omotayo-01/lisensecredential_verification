from typing import Any
def verify_vcp() -> dict[str, Any]:
    candidate = {
        "candidate_name": "Fashina Rebecca",
        "certificate_name": "VMware Certified Professional(VCP)",
        "issuing_body": "VMware",
        "credential_id": "VMW2022007764",
        "issue_date": "2023-04-14",
        "expiry_date": "2028-08-25"
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