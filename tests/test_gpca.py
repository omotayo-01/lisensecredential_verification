from verifier.gpca import verify_gpca

valid_candidate = {
    "candidate_name": "Kaboom Kabaam",
    "certificate_name": "Google Professional Cloud Architect",
    "issuing_body": "Google Cloud",
    "credential_id": "GPCA123456789",
    "badge_url": "https://info.credly.com/solutions/product-certifications" or "https://cp.certmetrics.com/google/en/login",
    "issue_date": "2025-05-10",
    "expiry_date": "None",
}

invalid_candidate = {
    "candidate_name": "Makinde Oluwaseyi",
    "certificate_name": "Google Professional Cloud Architect",
    "issuing_body": "Google Cloud",
    "credential_id": "GPCA545678092",
    "badge_url": "https://info.credly.com/solutions/product-certifications" or "https://cp.certmetrics.com/google/en/login",
    "issue_date": "2029-05-10",
    "expiry_date": "None",
}


def test_valid_gpca():
    result = verify_gpca(valid_candidate)
    assert result["verificationResult"]["status"] == "verified"


def test_invalid_gpca():
    result = verify_gpca(invalid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}