from unittest.mock import patch, Mock, MagicMock
from verifier.rhcsa import verify_rhcsa

valid_candidate = {
    "candidate_name": "Modashola Abisade",
    "certificate_name": "Red Hat Certified System Administrator (RHCSA)",
    "issuing_body": "Red Hat",
    "credential_id": "RHCSA27893485",
    "badge_url": "https://www.credly.com/badges/REAL_BADGE/public_url",
    "issue_date": "2012-03-01",
    "expiry_date": "2028-08-01",
}

invalid_candidate = {
    "candidate_name": "Olagunju Itohan",
    "certificate_name": "Red Hat Certified System Administrator (RHCSA)",
    "issuing_body": "Red Hat",
    "credential_id": "RHCSA9890985",
    "badge_url": "https://www.credly.com/badges/DOES_NOT_EXIST/public_url",
    "issue_date": "2012-03-01",
    "expiry_date": "2028-08-01",
}


@patch("verifier.rhcsa.send_request")
def test_valid_rhcsa(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_send_request.return_value = mock_response

    result = verify_rhcsa(valid_candidate)

    assert result["verificationResult"]["status"] == "verified"


@patch("verifier.rhcsa.send_request")
def test_invalid_rhcsa(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_send_request.return_value = mock_response

    result = verify_rhcsa(invalid_candidate)

    assert result["verificationResult"]["status"] == "unverified"