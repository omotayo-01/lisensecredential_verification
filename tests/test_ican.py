from unittest.mock import patch, Mock, MagicMock
from verifier.ican import verify_ican

valid_candidate = {
    "candidate_name": "Oluwapelumi Oluwatimileyin",
    "certificate_name": "ICAN membership",
    "issuing_body": "Institute of Chartered Accountants of Nigeria (ICAN)",
    "credential_id": "ICAN19680306",
    "badge_url": "https://www.credly.com/badges/REAL_BADGE/public_url",
    "issue_date": "2025-03-01",
    "expiry_date": "2028-03-01",
}

invalid_candidate = {
    "candidate_name": "Nkechi Mariam",
    "certificate_name": "ICAN membership",
    "issuing_body": "Institute of Chartered Accountants of Nigeria (ICAN)",
    "credential_id": "ICAN23456903",
    "badge_url": "https://www.credly.com/badges/DOES_NOT_EXIST/public_url",
    "issue_date": "2025-03-01",
    "expiry_date": "2030-03-01",
}


@patch("verifier.ican.send_request")
def test_valid_ican(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_send_request.return_value = mock_response

    result = verify_ican(valid_candidate)

    assert result["verificationResult"]["status"] == "verified"


@patch("verifier.ican.send_request")
def test_invalid_ican(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_send_request.return_value = mock_response

    result = verify_ican(invalid_candidate)

    assert result["verificationResult"]["status"] == "unverified"