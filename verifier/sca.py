from typing import Any
from verification import send_request
from confidence import calculate_confidence
def verify_sca(candidate: dict[str, Any]) -> dict[str, Any]:

    url = candidate.get("badge_url") or "https://drm.my.salesforce-sites.com/services/apexrest/credential"

    status = "unverified"

    response = send_request(url)

    if isinstance(response, dict):
        status = "verified"

    elif response.status_code == 200:
        text = response.text.lower()

        if "captcha" in text:
            status = "No public verification method exists"

        elif "error" in text:
            status = "unverified"

        else:
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