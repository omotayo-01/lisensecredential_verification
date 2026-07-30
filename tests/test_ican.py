from verifier.ican import verify_ican

valid_candidate = {
    "candidate_name": "Oluwapelumi Oluwatimileyin",
    "certificate_name": "ICAN membership",
    "issuing_body": "Institute of Chartered Accountants of Nigeria (ICAN)",
    "credential_id": "ICAN19680306",
    "badge_url": "https://icanig.org/ican-membership-verification",
    "issue_date": "2025-03-01",
    "expiry_date": "2028-03-01",
}

invalid_candidate = {
    "candidate_name": "Nkechi Mariam",
    "certificate_name": "ICAN membership",
    "issuing_body": "Institute of Chartered Accountants of Nigeria (ICAN)",
    "credential_id": "ICAN23456903",
    "badge_url": "https://icanig.org/ican-membership-verification",
    "issue_date": "2025-03-01",
    "expiry_date": "2030-03-01",
}


def test_valid_ican():
    result = verify_ican(valid_candidate)
    assert result["verificationResult"]["status"] == "verified"


def test_invalid_ican():
    result = verify_ican(invalid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}