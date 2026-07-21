from typing import Any
from verification import send_request
from confidence import calculate_confidence


def verify_itil(candidate: dict[str, Any]) -> dict[str, Any]:

    url = candidate["badge_url"]

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
            "candidateClaim": candidate,
        }
    }

    return result