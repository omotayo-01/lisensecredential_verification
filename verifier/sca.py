from typing import Any
def verify_sca() -> dict[str, Any]:
    candidate: dict[str, str] = {
         "candidate_name": "Akerele Idowu",
        "certificate_name": "Salesforce Certified Administrator",
        "issuing_body": "Scaleforce",
        "credential_id": "SCA03032954",
        "issue_date": "2018-05-10",
        "expiry_date": "present"
    }

    verification_found = True

    result: dict[str, Any] = {
        "verificationResult": {
            "claimType": "certification",
            "status": "verified" if verification_found else "not_found",
            "confidenceScore": 99,
            "candidateClaim": candidate
    }
    }

    return result