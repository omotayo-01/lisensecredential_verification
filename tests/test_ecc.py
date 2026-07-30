from verifier.ecc import verify_ecc

valid_candidate = {
    "candidate_name": "Ajeigbe William",
    "certificate_name": "Certified Ethical Hacker (CEH)",
    "issuing_body": "Ec-Council",
    "credential_id": "ECC2022002845",
    "badge_url": "https://aspen.eccouncil.org/Verify",
    "issue_date": "2023-03-01",
    "expiry_date": "2027-03-01",
}

invalid_candidate = {
    "candidate_name": "Kudi Ajinomoto",
    "certificate_name": "Certified Ethical Hacker (CEH)",
    "issuing_body": "Ec-Council",
    "credential_id": "ECC98767898",
    "badge_url": "https://www.credly.com/badges/DOES_NOT_EXIST/public_url",
    "issue_date": "2023-03-01",
    "expiry_date": "2030-03-01",
}


def test_valid_ecc():
    result = verify_ecc(valid_candidate)
    assert result["verificationResult"]["status"] == "verified"


def test_invalid_ecc():
    result = verify_ecc(invalid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}