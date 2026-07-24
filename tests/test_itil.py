from unittest.mock import patch, Mock, MagicMock
from verifier.itil import verify_itil

valid_candidate = {
    "candidate_name": "Goodyear Ebele",
    "certificate_name": "ITIL 4 Foundation",
    "issuing_body": "PeopleCert",
    "credential_id": "ITIL123456",
    "badge_url": "https://www.credly.com/badges/REAL_BADGE/public_url",
    "issue_date": "2020-02-10",
    "expiry_date": "2027-02-10",
}

invalid_candidate = {
    "candidate_name": "Amidat Arobieke",
    "certificate_name": "ITIL 4 Foundation",
    "issuing_body": "PeopleCert",
    "credential_id": "ITIL8767899",
    "badge_url": "https://www.peoplecert.org/public-profile?ed=XCHu3ZqUTNLLpYuUFQv172TnbqU6MqoA",
    "issue_date": "2020-02-10",
    "expiry_date": "2028-02-10",
}


@patch("verifier.itil.send_request")
def test_valid_itil(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_send_request.return_value = mock_response

    result = verify_itil(valid_candidate)

    assert result["verificationResult"]["status"] == "verified"


@patch("verifier.itil.send_request")
def test_invalid_itil(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_send_request.return_value = mock_response

    result = verify_itil(invalid_candidate)

    assert result["verificationResult"]["status"] == "unverified"