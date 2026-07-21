from unittest.mock import patch, Mock, MagicMock
from verifier.vcp import verify_vcp

valid_candidate = {
    "candidate_name": "Fashina Rebecca",
    "certificate_name": "VMware Certified Professional (VCP)",
    "issuing_body": "VMware",
    "credential_id": "VMW2022007764",
    "badge_url": "https://www.credly.com/badges/REAL_BADGE/public_url",
    "issue_date": "2023-04-14",
    "expiry_date": "2028-08-25",
}

invalid_candidate = {
    "candidate_name": "Jason Duolingo",
    "certificate_name": "VMware Certified Professional (VCP)",
    "issuing_body": "VMware",
    "credential_id": "VMW9909943365",
    "badge_url": "https://www.credly.com/badges/DOES_NOT_EXIST/public_url",
    "issue_date": "2023-04-14",
    "expiry_date": "2028-08-25",
}


@patch("verifier.vcp.send_request")
def test_valid_vcp(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_send_request.return_value = mock_response

    result = verify_vcp(valid_candidate)

    assert result["verificationResult"]["status"] == "verified"


@patch("verifier.vcp.send_request")
def test_invalid_vcp(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_send_request.return_value = mock_response

    result = verify_vcp(invalid_candidate)

    assert result["verificationResult"]["status"] == "unverified"