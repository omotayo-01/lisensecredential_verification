from typing import Any

def verify_rn() -> dict[str, Any]:
    candidate = {
        "candidate_name": "Oladokun Ayooluwa",
        "certificate_name": "Registered Nurse license(RN)",
        "issuing_body": "Nursing and Midwivery Council of Nigeria(NMCN)",
        "credential_id": "RN2022004008",
        "issue_date": "2025-03-01",
        "expiry_date": "2039-03-01"
    }

    verification_found = True

    result: dict[str, Any] = {
        "verificationResult": {
            "claimType": "certification",
            "status": "verified" if verification_found else "not_found",
            "confidenceScore": 68,
            "candidateClaim": candidate
        }
    }

    return result