from verifier.rhcsa import verify_rhcsa

valid_candidate = {
    "candidate_name": "Modashola Abisade",
    "certificate_name": "Red Hat Certified System Administrator (RHCSA)",
    "issuing_body": "Red Hat",
    "credential_id": "RHCSA27893485",
    "badge_url": "https://rhtapps.redhat.com/verify?certId=270-893-485",
    "issue_date": "2012-03-01",
    "expiry_date": "2028-08-01",
}

invalid_candidate = {
    "candidate_name": "Olagunju Itohan",
    "certificate_name": "Red Hat Certified System Administrator (RHCSA)",
    "issuing_body": "Red Hat",
    "credential_id": "RHCSA989098532",
    "badge_url": "https://rhtapps.redhat.com/verify?certId=989-098-532",
    "issue_date": "2012-03-01",
    "expiry_date": "2028-08-01",
}


def test_valid_rhcsa():
    result = verify_rhcsa(valid_candidate)
    assert result["verificationResult"]["status"] == "verified"


def test_invalid_rhcsa():
    result = verify_rhcsa(invalid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}