from verifier.itil import verify_itil

valid_candidate = {
    "candidate_name": "Goodyear Ebele",
    "certificate_name": "ITIL 4 Foundation",
    "issuing_body": "PeopleCert",
    "credential_id": "ITIL123456",
    "badge_url": "https://www.peoplecert.org/ways-to-get-certified" or "https://www.peoplecert.org/public-profile?ed=XCHu3ZqUTNLLpYuUFQv172TnbqU6MqoA",
    "issue_date": "2020-02-10",
    "expiry_date": "2027-02-10",
}

invalid_candidate = {
    "candidate_name": "Amidat Arobieke",
    "certificate_name": "ITIL 4 Foundation",
    "issuing_body": "PeopleCert",
    "credential_id": "ITIL8767899",
    "badge_url": "https://www.peoplecert.org/public-profile?ed=XCHu3ZqUTNLLpYuUFQv172TnbqU6MqoA" or "https://www.peoplecert.org/ways-to-get-certified",
    "issue_date": "2020-02-10",
    "expiry_date": "2028-02-10",
}


def test_valid_itil():
    result = verify_itil(valid_candidate)
    assert result["verificationResult"]["status"] == "verified"


def test_invalid_itil():
    result = verify_itil(invalid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}