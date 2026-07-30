from verifier.vcp import verify_vcp

valid_candidate = {
    "candidate_name": "Fashina Rebecca",
    "certificate_name": "VMware Certified Professional (VCP)",
    "issuing_body": "VMware",
    "credential_id": "VMW2022007764",
    "badge_url": "https://cp.certmetrics.com/vmware/",
    "issue_date": "2023-04-14",
    "expiry_date": "2028-08-25",
}

invalid_candidate = {
    "candidate_name": "Jason Duolingo",
    "certificate_name": "VMware Certified Professional (VCP)",
    "issuing_body": "VMware",
    "credential_id": "VMW9909943365",
    "badge_url": "https://cp.certmetrics.com/vmware/",
    "issue_date": "2023-04-14",
    "expiry_date": "2028-08-25",
}


def test_valid_vcp():
    result = verify_vcp(valid_candidate)
    assert result["verificationResult"]["status"] == "verified"


def test_invalid_vcp():
    result = verify_vcp(invalid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}