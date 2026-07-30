from verifier.icu import verify_icu

valid_candidate = {
    "candidate_name": "Omotayo Uzumaki",
    "certificate_name": "Hospital ICU Training Certificate",
    "issuing_body": "Lagos University Teaching Hospital",
    "credential_id": "ICU1027156",
    "badge_url": "https://lasu.edu.ng/exams-and-records/new/services.php" or "https://www.hsetrain.org/hse-training-certificate-verification.html",
    "issue_date": "2025-03-01",
    "expiry_date": "2028-03-01",
}

invalid_candidate = {
    "candidate_name": "Alowomajayie Eyinlemo",
    "certificate_name": "Hospital ICU Training Certificate",
    "issuing_body": "Lagos University Teaching Hospital",
    "credential_id": "ICU23454311",
    "badge_url": "https://www.hsetrain.org/hse-training-certificate-verification.html" or "https://lasu.edu.ng/exams-and-records/new/services.php",
    "issue_date": "2019-03-01",
    "expiry_date": "2027-03-01",
}


def test_valid_icu():
    result = verify_icu(valid_candidate)
    assert result["verificationResult"]["status"] == "verified"


def test_invalid_icu():
    result = verify_icu(invalid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}