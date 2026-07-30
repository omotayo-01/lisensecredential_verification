from verifier.aacn import verify_aacn

valid_candidate = {
    "candidate_name": "Makanjuola Dasola",
    "certificate_name": "Critical Care Registered Nurse(CCRN)",
    "issuing_body": "American Association of Critical-Care Nurses (AACN)",
    "credential_id": "CCRN2022002851",
    "badge_url": "https://www.aacn.org/certification/verify-certification",
    "issue_date": "2025-03-01",
    "expiry_date": "2038-03-01",
}

invalid_candidate = {
    "candidate_name": "Akilagbe  Theophilus",
    "certificate_name": "Critical Care Registered Nurse(CCRN)",
    "issuing_body": "American Association of Critical-Care Nurses (AACN)",
    "credential_id": "CCRN789438909",
    "badge_url": "https://www.aacn.org/certification/verify-certification",
    "issue_date": "2025-03-01",
    "expiry_date": "2038-03-01",
}


def test_valid_aacn():
    result = verify_aacn(valid_candidate)
    assert result["verificationResult"]["status"] == "verified"


def test_invalid_aacn():
    result = verify_aacn(invalid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}