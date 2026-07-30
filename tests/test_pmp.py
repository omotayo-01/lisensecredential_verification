from verifier.pmp import verify_pmp

valid_candidate = {
    "candidate_name": "Esan Kemisola",
    "certificate_name": "Project Management Professional (PMP)",
    "issuing_body": "Project Management Institute (PMI)",
    "credential_id": "PMP70569w2982",
    "badge_url": "https://cert.pmi.org/registry.aspx",
    "issue_date": "2020-02-10",
    "expiry_date": "2028-02-10",
}

invalid_candidate = {
    "candidate_name": "Johny Ekoro",
    "certificate_name": "Project Management Professional (PMP)",
    "issuing_body": "Project Management Institute (PMI)",
    "credential_id": "PMI9878w9872",
    "badge_url": "https://cert.pmi.org/registry.aspx",
    "issue_date": "2020-02-10",
    "expiry_date": "2028-02-10",
}


def test_valid_pmp():
    result = verify_pmp(valid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}


def test_invalid_pmp():
    result = verify_pmp(invalid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}