from unittest.mock import patch, Mock, MagicMock
from verifier.cisco import verify_cisco

valid_candidate = {
    "candidate_name": "Oladotun David",
    "certificate_name": "Cisco Certified Network Associate",
    "issuing_body": "Cisco",
    "credential_id": "CCNA1-89024",
    "issue_date": "2025-01-15",
    "expiry_date": "2028-01-15",
}

invalid_candidate = {
    "candidate_name": "John Dodokire",
    "certificate_name": "Cisco Certified Network Associate",
    "issuing_body": "Cisco",
    "credential_id": "CCNA8-13901",
    "issue_date": "2024-01-15",
    "expiry_date": "2027-01-15",
}

@patch("verifier.cisco.send_request")
def test_valid_cisco(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_send_request.return_value = mock_response

    result = verify_cisco(valid_candidate)

    assert result["verificationResult"]["status"] == "verified"


@patch("verifier.cisco.send_request")
def test_invalid_cisco(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_send_request.return_value = mock_response

    result = verify_cisco(invalid_candidate)

    assert result["verificationResult"]["status"] == "unverified"