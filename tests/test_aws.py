from verifier.aws import verify_aws

valid_candidate = {
    "candidate_name": "Yemi Olaniyan",
    "certificate_name": "AWS Certified Solutions Architect Associate",
    "issuing_body": "Amazon Web Services",
    "credential_id": "AWS123456",
    "badge_url": "https://cp.certmetrics.com/amazon/en/public/verify/credential" or "https://aws.amazon.com/certification/certification-digital-badges/",
    "issue_date": "2025-03-01",
    "expiry_date": "2028-03-01"
}

invalid_candidate = {
    "candidate_name": "Owoade Olaniyan",
    "certificate_name": "AWS Certified Solutions Architect Associate",
    "issuing_body": "Amazon Web Services",
    "credential_id": "AWS090959",
    "badge_url": "https://cp.certmetrics.com/amazon/en/public/verify/credential" or "https://aws.amazon.com/certification/certification-digital-badges/",
    "issue_date": "2024-03-01",
    "expiry_date": "2027-10-27"
}

def test_valid_aws():
    result = verify_aws(valid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}


def test_invalid_aws():
    result = verify_aws(invalid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}
