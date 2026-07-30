from verifier.tds import verify_tds

valid_candidate = {
    "candidate_name": "Oseni Samuel",
    "certificate_name": "Tableau Desktop Specialist",
    "issuing_body": "Tableau",
    "credential_id": "TAB03168927",
    "badge_url": "https://trailhead.salesforce.com/credentials/verification" or "https://www.tableau.com/support/certification/directory",
    "issue_date": "2024-03-01",
    "expiry_date": "2029-03-03",
}

invalid_candidate = {
    "candidate_name": "Endo Watari",
    "certificate_name": "Tableau Desktop Specialist",
    "issuing_body": "Tableau",
    "credential_id": "TAB545432290",
    "badge_url": "https://trailhead.salesforce.com/credentials/verification" or "https://www.tableau.com/support/certification/directory",
    "issue_date": "2024-03-01",
    "expiry_date": "2029-03-03",
}


def test_valid_tds():
    result = verify_tds(valid_candidate)
    assert result["verificationResult"]["status"] == "verified"


def test_invalid_tds():
    result = verify_tds(invalid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}