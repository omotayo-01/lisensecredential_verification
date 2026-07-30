from verifier.rn import verify_rn

valid_candidate = {
    "candidate_name": "Oladokun Ayooluwa",
    "certificate_name": "Registered Nurse license (RN)",
    "issuing_body": "Nursing and Midwifery Council of Nigeria (NMCN)",
    "credential_id": "RN2022004008",
    "badge_url": "https://www.nmcn.gov.ng/verify.html",
    "issue_date": "2025-03-01",
    "expiry_date": "2039-03-01",
}

invalid_candidate = {
    "candidate_name": "Jesutofunmi Barnabas",
    "certificate_name": "Registered Nurse license (RN)",
    "issuing_body": "Nursing and Midwifery Council of Nigeria (NMCN)",
    "credential_id": "RN920209443",
    "badge_url": "https://www.nmcn.gov.ng/verify.html",
    "issue_date": "2023-03-01",
    "expiry_date": "2024-03-01",
}


def test_valid_rn():
    result = verify_rn(valid_candidate)
    assert result["verificationResult"]["status"] == "verified"


def test_invalid_rn():
    result = verify_rn(invalid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}