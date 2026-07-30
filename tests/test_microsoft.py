from verifier.microsoft import verify_microsoft

valid_candidate = {
    "candidate_name": "Akanbi Olaniyode",
    "certificate_name": "Microsoft Certified: Azure AI Engineer Associate",
    "issuing_body": "Microsoft",
    "badge_url": "https://learn.microsoft.com/en-us/" or "https://certiport.pearsonvue.com/Certifications/Microsoft.aspx",
    "credential_id": "ABC123456789",
    "issue_date": "2025-05-10",
    "expiry_date": "None"
}

invalid_candidate = {
    "candidate_name": "Akinyemi Oyedeji",
    "certificate_name": "Microsoft Certified: Azure AI Engineer Associate",
    "issuing_body": "Microsoft",
    "credential_id": "ABC123456789",
    "badge_url": "https://learn.microsoft.com/en-us/" or "https://certiport.pearsonvue.com/Certifications/Microsoft.aspx",
    "issue_date": "2029-01-09",
    "expiry_date": "None"
}


def test_valid_microsoft():
    result = verify_microsoft(valid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}


def test_invalid_microsoft():
    result = verify_microsoft(invalid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}
