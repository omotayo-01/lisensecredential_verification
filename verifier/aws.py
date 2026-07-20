from typing import Any
from verification import send_request
from confidence import calculate_confidence

def verify_aws() -> dict[str, Any]:
    candidate = {
        "candidate_name": "Yemi Olaniyan",
        "certificate_name": "AWS Certified Solutions Architect Associate",
        "issuing_body": "Amazon Web Services",
        "credential_id": "AWS123456",
        "badge_url": "https://www.credly.com/badges/xxxxxxxxxxxxxxxx/public_url",
        "issue_date": "2025-03-01",
        "expiry_date": "2028-03-01"
    }

   
    

    url = ( candidate["badge_url"])

    response = send_request(url)

    if response is None:
        status = "No public verification method exists"

    elif response.status_code == 404:
        status = "unverified"

    elif response.status_code == 200:
        status = "verified"

    else:
        status = "unverified"

    result: dict[str, Any] = {
        "verificationResult": {
            "claimType": "certification",
            "status": status,
            "confidenceScore": calculate_confidence(status),
            "candidateClaim": candidate
        }
    }

    return result