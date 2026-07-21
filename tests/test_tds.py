from unittest.mock import patch, Mock, MagicMock
from verifier.tds import verify_tds

valid_candidate = {
    "candidate_name": "Oseni Samuel",
    "certificate_name": "Tableau Desktop Specialist",
    "issuing_body": "Tableau",
    "credential_id": "TAB03168927",
    "badge_url": "https://www.credly.com/badges/REAL_BADGE/public_url",
    "issue_date": "2024-03-01",
    "expiry_date": "2029-03-03",
}

invalid_candidate = {
    "candidate_name": "Endo Watari",
    "certificate_name": "Tableau Desktop Specialist",
    "issuing_body": "Tableau",
    "credential_id": "TAB545432290",
    "badge_url": "https://www.credly.com/badges/DOES_NOT_EXIST/public_url",
    "issue_date": "2024-03-01",
    "expiry_date": "2029-03-03",
}


@patch("verifier.tds.send_request")
def test_valid_tds(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_send_request.return_value = mock_response

    result = verify_tds(valid_candidate)

    assert result["verificationResult"]["status"] == "verified"


@patch("verifier.tds.send_request")
def test_invalid_tds(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_send_request.return_value = mock_response

    result = verify_tds(invalid_candidate)

    assert result["verificationResult"]["status"] == "unverified"