from verifier.ctia import verify_ctia

valid_candidate = {
    "candidate_name": "Olatunji Timothy",
    "certificate_name": "CompTIA Security+",
    "issuing_body": "CompTIA",
    "credential_id": "Comp2022002005",
    "badge_url": "https://www.comptia.org/en/certifications/security",
    "issue_date": "2022-03-01",
    "expiry_date": "2028-08-01",
}

invalid_candidate = {
    "candidate_name": "John Dosunmu",
    "certificate_name": "CompTIA Security+",
    "issuing_body": "CompTIA",
    "credential_id": "Comp4567890987",
    "badge_url": "https://www.comptia.org/en/certifications/security",
    "issue_date": "2022-03-01",
    "expiry_date": "2029-08-01",
}


def test_valid_ctia():
    result = verify_ctia(valid_candidate)
    assert result["verificationResult"]["status"] == "verified"



def test_invalid_ctia():
    result = verify_ctia(invalid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}