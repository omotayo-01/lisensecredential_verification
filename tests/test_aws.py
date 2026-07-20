from unittest.mock import patch, Mock
from verifier.aws import verify_aws
from unittest.mock import patch, Mock, MagicMock
print(verify_aws)
valid_candidate = {
    "candidate_name": "Yemi Olaniyan",
    "certificate_name": "AWS Certified Solutions Architect Associate",
    "issuing_body": "Amazon Web Services",
    "credential_id": "AWS123456",
    "badge_url": "https://www.credly.com/badges/REAL_BADGE/public_url",
    "issue_date": "2025-03-01",
    "expiry_date": "2028-03-01"
}

invalid_candidate = {
    "candidate_name": "Owoade Olaniyan",
    "certificate_name": "AWS Certified Solutions Architect Associate",
    "issuing_body": "Amazon Web Services",
    "credential_id": "AWS090959",
    "badge_url": "https://www.credly.com/badges/DOES_NOT_EXIST/public_url",
    "issue_date": "2024-03-01",
    "expiry_date": "2027-10-27"
}


@patch("verifier.aws.send_request")
def test_valid_aws(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_send_request.return_value = mock_response

    result = verify_aws(valid_candidate)

    assert result["verificationResult"]["status"] == "verified"


@patch("verifier.aws.send_request")
def test_invalid_aws(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_send_request.return_value = mock_response

    result = verify_aws(invalid_candidate)

    assert result["verificationResult"]["status"] == "unverified"