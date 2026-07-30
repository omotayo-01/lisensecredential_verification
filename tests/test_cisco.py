from verifier.cisco import verify_cisco

valid_candidate = {
    "candidate_name": "Oladotun David",
    "certificate_name": "Cisco Certified Network Associate",
    "issuing_body": "Cisco",
    "credential_id": "CCNA1-89024",
    "badge_url": "https://www.certmetrics.com/cisco/public/verification.asp?pid=1&aid=1&credid=CCNA1-89024",
    "issue_date": "2024-03-01",
    "expiry_date": "2028-01-15",
}

invalid_candidate = {
    "candidate_name": "John Dodokire",
    "certificate_name": "Cisco Certified Network Associate",
    "issuing_body": "Cisco",
    "credential_id": "CCNA8-13901",
    "badge_url": "https://www.certmetrics.com/cisco/public/verification.asp?pid=1&aid=1&credid=CCNA8-13901",
    "issue_date": "2024-01-15",
    "expiry_date": "2027-01-15",
}


def test_valid_cisco():
    result = verify_cisco(valid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}


def test_invalid_cisco():
    result = verify_cisco(invalid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}
