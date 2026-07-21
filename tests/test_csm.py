from unittest.mock import patch, Mock, MagicMock
from verifier.csm import verify_csm

valid_candidate = {
    "candidate_name": "Olatunji Timothy",
    "certificate_name": "Certified Scrum Master (CSM)",
    "issuing_body": "Scrum Alliance",
    "credential_id": "CSA029982927",
    "badge_url": "https://www.credly.com/badges/REAL_BADGE/public_url",
    "issue_date": "2022-03-01",
    "expiry_date": "2028-08-01",
}

invalid_candidate = {
    "candidate_name": "Johnson Adegbite",
    "certificate_name": "Certified Scrum Master (CSM)",
    "issuing_body": "Scrum Alliance",
    "credential_id": "CSA1234323",
    "badge_url": "https://www.credly.com/badges/DOES_NOT_EXIST/public_url",
    "issue_date": "2022-03-01",
    "expiry_date": "2028-08-01",
}


@patch("verifier.csm.send_request")
def test_valid_csm(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_send_request.return_value = mock_response

    result = verify_csm(valid_candidate)

    assert result["verificationResult"]["status"] == "verified"


@patch("verifier.csm.send_request")
def test_invalid_csm(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_send_request.return_value = mock_response

    result = verify_csm(invalid_candidate)

    assert result["verificationResult"]["status"] == "unverified"