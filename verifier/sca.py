from typing import Any
from verification import send_request
from confidence import calculate_confidence
def verify_sca(candidate: dict[str, Any]) -> dict[str, Any]:    
    email = "AkereleIdowu03@gmail.com"

    url = (
        "https://drm.my.salesforce-sites.com/services/apexrest/credential"
        f"?searchString={email}"
        "&browserName=Chrome"
        "&browserVersion=149"
        "&osName=Windows"
        "&osVersion=10"
        "&languageLocaleKey=en"
    )

    response = send_request(url)

    if response is None:
        status = "No public verification method exists"

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