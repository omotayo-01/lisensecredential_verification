from unittest.mock import patch, Mock, MagicMock
from verifier.ctia import verify_ctia

valid_candidate = {
    "candidate_name": "Olatunji Timothy",
    "certificate_name": "CompTIA Security+",
    "issuing_body": "CompTIA",
    "credential_id": "Comp2022002005",
    "badge_url": "https://www.credly.com/badges/REAL_BADGE/public_url",
    "issue_date": "2022-03-01",
    "expiry_date": "2028-08-01",
}

invalid_candidate = {
    "candidate_name": "John Dosunmu",
    "certificate_name": "CompTIA Security+",
    "issuing_body": "CompTIA",
    "credential_id": "Comp4567890987",
    "badge_url": "https://www.credly.com/badges/DOES_NOT_EXIST/public_url",
    "issue_date": "2022-03-01",
    "expiry_date": "2028-08-01",
}


@patch("verifier.ctia.send_request")
def test_valid_ctia(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_send_request.return_value = mock_response

    result = verify_ctia(valid_candidate)

    assert result["verificationResult"]["status"] == "verified"


@patch("verifier.ctia.send_request")
def test_invalid_ctia(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_send_request.return_value = mock_response

    result = verify_ctia(invalid_candidate)

    assert result["verificationResult"]["status"] == "unverified"