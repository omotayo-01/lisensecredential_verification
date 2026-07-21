from unittest.mock import patch, Mock, MagicMock
from verifier.icu import verify_icu

valid_candidate = {
    "candidate_name": "Omotayo Uzumaki",
    "certificate_name": "Hospital ICU Training Certificate",
    "issuing_body": "Lagos University Teaching Hospital",
    "credential_id": "ICU1027156",
    "badge_url": "https://www.credly.com/badges/REAL_BADGE/public_url",
    "issue_date": "2025-03-01",
    "expiry_date": "2028-03-01",
}

invalid_candidate = {
    "candidate_name": "Alowomajayie Eyinlemo",
    "certificate_name": "Hospital ICU Training Certificate",
    "issuing_body": "Lagos University Teaching Hospital",
    "credential_id": "ICU23454311",
    "badge_url": "https://www.credly.com/badges/DOES_NOT_EXIST/public_url",
    "issue_date": "2019-03-01",
    "expiry_date": "2027-03-01",
}


@patch("verifier.icu.send_request")
def test_valid_icu(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_send_request.return_value = mock_response

    result = verify_icu(valid_candidate)

    assert result["verificationResult"]["status"] == "verified"


@patch("verifier.icu.send_request")
def test_invalid_icu(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_send_request.return_value = mock_response

    result = verify_icu(invalid_candidate)

    assert result["verificationResult"]["status"] == "unverified"