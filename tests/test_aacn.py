from unittest.mock import patch, Mock, MagicMock
from verifier.aacn import verify_aacn

valid_candidate = {
    "candidate_name": "Makanjuola Dasola",
    "certificate_name": "Critical Care Registered Nurse(CCRN)",
    "issuing_body": "American Association of Critical-Care Nurses (AACN)",
    "credential_id": "CCRN2022002851",
    "badge_url": "https://www.credly.com/badges/REAL_BADGE/public_url",
    "issue_date": "2025-03-01",
    "expiry_date": "2038-03-01",
}

invalid_candidate = {
    "candidate_name": "Akilagbe  Theophilus",
    "certificate_name": "Critical Care Registered Nurse(CCRN)",
    "issuing_body": "American Association of Critical-Care Nurses (AACN)",
    "credential_id": "CCRN789438909",
    "badge_url": "https://www.credly.com/badges/DOES_NOT_EXIST/public_url",
    "issue_date": "2025-03-01",
    "expiry_date": "2038-03-01",
}


@patch("verifier.aacn.send_request")
def test_valid_aacn(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_send_request.return_value = mock_response

    result = verify_aacn(valid_candidate)

    assert result["verificationResult"]["status"] == "verified"


@patch("verifier.aacn.send_request")
def test_invalid_aacn(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_send_request.return_value = mock_response

    result = verify_aacn(invalid_candidate)

    assert result["verificationResult"]["status"] == "unverified"