from unittest.mock import patch, Mock, MagicMock
from verifier.ecc import verify_ecc

valid_candidate = {
    "candidate_name": "Ajeigbe William",
    "certificate_name": "Certified Ethical Hacker (CEH)",
    "issuing_body": "Ec-Council",
    "credential_id": "ECC2022002845",
    "badge_url": "https://www.credly.com/badges/REAL_BADGE/public_url",
    "issue_date": "2023-03-01",
    "expiry_date": "2027-03-01",
}

invalid_candidate = {
    "candidate_name": "Kudi Ajinomoto",
    "certificate_name": "Certified Ethical Hacker (CEH)",
    "issuing_body": "Ec-Council",
    "credential_id": "ECC98767898",
    "badge_url": "https://www.credly.com/badges/DOES_NOT_EXIST/public_url",
    "issue_date": "2023-03-01",
    "expiry_date": "2030-03-01",
}


@patch("verifier.ecc.send_request")
def test_valid_ecc(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_send_request.return_value = mock_response

    result = verify_ecc(valid_candidate)

    assert result["verificationResult"]["status"] == "verified"


@patch("verifier.ecc.send_request")
def test_invalid_ecc(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_send_request.return_value = mock_response

    result = verify_ecc(invalid_candidate)

    assert result["verificationResult"]["status"] == "unverified"