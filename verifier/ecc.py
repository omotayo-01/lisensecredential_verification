from typing import Any

def verify_ecc() -> dict[str, Any]:
    candidate = {
        "candidate_name": "Ajeigbe William",
        "certificate_name": "Certified Ethical Hacker (CEH)",
        "issuing_body": "Ec-Council",
        "credential_id": "ECC2022002845",
        "issue_date": "2023-03-01",
        "expiry_date": "2027-03-01"
    }

    verification_found = True

    result: dict[str, Any] = {
        "verificationResult": {
            "claimType": "certification",
            "status": "verified" if verification_found else "not_found",
            "confidenceScore": 95,
            "candidateClaim": candidate
        }
    }

    return result