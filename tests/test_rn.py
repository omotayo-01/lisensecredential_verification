from unittest.mock import patch, Mock, MagicMock
from verifier.rn import verify_rn

valid_candidate = {
    "candidate_name": "Oladokun Ayooluwa",
    "certificate_name": "Registered Nurse license (RN)",
    "issuing_body": "Nursing and Midwifery Council of Nigeria (NMCN)",
    "credential_id": "RN2022004008",
    "badge_url": "https://www.credly.com/badges/REAL_BADGE/public_url",
    "issue_date": "2025-03-01",
    "expiry_date": "2039-03-01",
}

invalid_candidate = {
    "candidate_name": "Jesutofunmi Barnabas",
    "certificate_name": "Registered Nurse license (RN)",
    "issuing_body": "Nursing and Midwifery Council of Nigeria (NMCN)",
    "credential_id": "RN920209443",
    "badge_url": "https://www.credly.com/badges/DOES_NOT_EXIST/public_url",
    "issue_date": "2023-03-01",
    "expiry_date": "2024-03-01",
}


@patch("verifier.rn.send_request")
def test_valid_rn(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_send_request.return_value = mock_response

    result = verify_rn(valid_candidate)

    assert result["verificationResult"]["status"] == "verified"


@patch("verifier.rn.send_request")
def test_invalid_rn(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_send_request.return_value = mock_response

    result = verify_rn(invalid_candidate)

    assert result["verificationResult"]["status"] == "unverified"