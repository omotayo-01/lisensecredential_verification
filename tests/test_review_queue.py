from review_queue import add_to_review_queue, get_review_queue, review_queue
from verifier.aws import verify_aws
from unittest.mock import patch, Mock, MagicMock


invalid_candidate = {
    "candidate_name": "Yemi Olaniyan",
    "certificate_name": "AWS Certified Solutions Architect Associate",
    "issuing_body": "Amazon Web Services",
    "credential_id": "AWS123456",
    "badge_url": "https://www.credly.com/badges/DOES_NOT_EXIST/public_url",
    "issue_date": "2025-03-01",
    "expiry_date": "2028-03-01",
}


@patch("verifier.aws.send_request")
def test_unverified_result_added_to_review_queue(mock_send_request: MagicMock):

    review_queue.clear() 

    mock_response = Mock()
    mock_response.status_code = 404
    mock_send_request.return_value = mock_response

    result = verify_aws(invalid_candidate)

    add_to_review_queue(result)

    assert len(get_review_queue()) == 1
    assert get_review_queue()[0]["verificationResult"]["status"] == "unverified"