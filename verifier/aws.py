from typing import Any
from verification import send_request
from confidence import calculate_confidence


def verify_aws(candidate: dict[str, Any]) -> dict[str, Any]:

    url = candidate["badge_url"]
    response = send_request(url)

    if isinstance(response, dict):
        status = "unverified"

    elif response.status_code == 404:
        status = "unverified"

    elif response.status_code == 200:
        print("Requested URL:", url)
        print("Final URL:", response.url)
        print("Page title/snippet:")
        print(response.text[:500])
        page = response.text or ""
        low = page.lower()

        # primary checks against raw page body
        cert_ok = candidate["certificate_name"].lower() in low
        name_ok = candidate["candidate_name"].lower() in low
        id_ok = candidate["credential_id"].lower() in low

        # if raw body doesn't include expected strings, check OpenGraph/meta tags
        if not (cert_ok or name_ok or id_ok):
            import re

            def extract_meta(prop_name: str) -> str:
                m = re.search(r'<meta[^>]+property=["\']%s["\'][^>]*content=["\']([^"\']+)["\']' % re.escape(prop_name), page, flags=re.I)
                if m:
                    return m.group(1).lower()
                m2 = re.search(r'<meta[^>]+name=["\']%s["\'][^>]*content=["\']([^"\']+)["\']' % re.escape(prop_name), page, flags=re.I)
                if m2:
                    return m2.group(1).lower()
                return ""

            og_title = extract_meta('og:title')
            og_desc = extract_meta('og:description')

            if og_title:
                cert_ok = cert_ok or (candidate["certificate_name"].lower() in og_title)
                name_ok = name_ok or (candidate["candidate_name"].lower() in og_title)
                id_ok = id_ok or (candidate["credential_id"].lower() in og_title)

            if og_desc:
                cert_ok = cert_ok or (candidate["certificate_name"].lower() in og_desc)
                name_ok = name_ok or (candidate["candidate_name"].lower() in og_desc)
                id_ok = id_ok or (candidate["credential_id"].lower() in og_desc)

        print("Status:", response.status_code)
        print("Certificate:", cert_ok)
        print("Name:", name_ok)
        print("Credential:", id_ok)
        if cert_ok and (name_ok or id_ok):
            status = "verified"
        else:
            status = "unverified"
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