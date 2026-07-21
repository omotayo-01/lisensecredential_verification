from unittest.mock import patch, Mock, MagicMock
from verifier.gpca import verify_gpca

valid_candidate = {
    "candidate_name": "Kaboom Kabaam",
    "certificate_name": "Google Professional Cloud Architect",
    "issuing_body": "Google Cloud",
    "credential_id": "GPCA123456789",
    "badge_url": "https://www.credly.com/badges/REAL_BADGE/public_url",
    "issue_date": "2025-05-10",
    "expiry_date": "None",
}

invalid_candidate = {
    "candidate_name": "Makinde Oluwaseyi",
    "certificate_name": "Google Professional Cloud Architect",
    "issuing_body": "Google Cloud",
    "credential_id": "GPCA545678092",
    "badge_url": "https://www.credly.com/badges/DOES_NOT_EXIST/public_url",
    "issue_date": "2029-05-10",
    "expiry_date": "None",
}


@patch("verifier.gpca.send_request")
def test_valid_gpca(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_send_request.return_value = mock_response

    result = verify_gpca(valid_candidate)

    assert result["verificationResult"]["status"] == "verified"


@patch("verifier.gpca.send_request")
def test_invalid_gpca(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_send_request.return_value = mock_response

    result = verify_gpca(invalid_candidate)

    assert result["verificationResult"]["status"] == "unverified"