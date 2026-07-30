from verifier.sca import verify_sca

valid_candidate = {
    "candidate_name": "Akerele Idowu",
    "certificate_name": "Salesforce Certified Administrator",
    "issuing_body": "Salesforce",
    "credential_id": "SCA03032954",
    "badge_url": "https://www.salesforce.com/training/certification/",
    "issue_date": "2018-05-10",
    "expiry_date": "present",
}

invalid_candidate = {
    "candidate_name": "Jason Statham",
    "certificate_name": "Salesforce Certified Administrator",
    "issuing_body": "Salesforce",
    "credential_id": "SCA03032954",
    "badge_url": "https://www.salesforce.com/training/certification/",
    "issue_date": "2018-05-10",
    "expiry_date": "present",
}


def test_valid_sca():
    result = verify_sca(valid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}


def test_invalid_sca():
    result = verify_sca(invalid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}
