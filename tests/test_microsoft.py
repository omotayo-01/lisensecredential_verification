from unittest.mock import patch, Mock
from verifier.microsoft import verify_microsoft
from unittest.mock import patch, Mock, MagicMock
print(verify_microsoft)
valid_candidate = {
    "candidate_name": "Akanbi Olukayode",
        "certificate_name": "Microsoft Certified: Azure AI Engineer Associate",
        "issuing_body": "Microsoft",
        "badge_url": "https://www.credly.com/badges/xxxxxxxxxxxxxxxx/public_url",
        "credential_id": "ABC123456789",
        "issue_date": "2025-05-10",
        "expiry_date": "None"
}

invalid_candidate = {
    "candidate_name": "Akinyemi Oyedeji",
    "certificate_name": "Microsoft Certified: Azure AI Engineer Associate",
    "issuing_body": "Microsoft",
    "credential_id": "ABC123456789",
    "badge_url": "https://www.credly.com/badges/DOES_NOT_EXIST/public_url",
    "issue_date": "2029-01-09",
    "expiry_date": "None"
}


@patch("verifier.microsoft.send_request")
def test_valid_microsoft(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_send_request.return_value = mock_response

    result = verify_microsoft(valid_candidate)

    assert result["verificationResult"]["status"] == "verified"


@patch("verifier.microsoft.send_request")
def test_invalid_microsoft(mock_send_request: MagicMock):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_send_request.return_value = mock_response

    result = verify_microsoft(invalid_candidate)

    assert result["verificationResult"]["status"] == "unverified"