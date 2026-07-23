from unittest.mock import patch, Mock, MagicMock
from verifier.pmp import verify_pmp

valid_candidate = {
    "candidate_name": "Esan Kemisola",
    "certificate_name": "Project Management Professional (PMP)",
    "issuing_body": "Project Management Institute (PMI)",
    "credential_id": "PMP70569w2982",
    "badge_url": "https://www.credly.com/badges/REAL_BADGE/public_url",
    "issue_date": "2020-02-10",
    "expiry_date": "2028-02-10",
}

invalid_candidate = {
    "candidate_name": "Johny Ekoro",
    "certificate_name": "Project Management Professional (PMP)",
    "issuing_body": "Project Management Institute (PMI)",
    "credential_id": "PMI9878w9872",
    "badge_url": "https://www.credly.com/badges/REAL_BADGE/public_url",
    "issue_date": "2020-02-10",
    "expiry_date": "2028-02-10",
}


@patch("verifier.pmp.send_request")
def test_valid_pmp(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_send_request.return_value = mock_response

    result = verify_pmp(valid_candidate)

    assert result["verificationResult"]["status"] == "verified"


@patch("verifier.pmp.send_request")
def test_invalid_pmp(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_send_request.return_value = mock_response

    result = verify_pmp(invalid_candidate)

    assert result["verificationResult"]["status"] == "unverified"