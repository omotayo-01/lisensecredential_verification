from review_queue import add_to_review_queue, get_review_queue, review_queue
from verifier.aws import verify_aws


invalid_candidate = {
    "candidate_name": "Yemi Olaniyan",
    "certificate_name": "AWS Certified Solutions Architect Associate",
    "issuing_body": "Amazon Web Services",
    "credential_id": "AWS123456",
    "badge_url": "https://aws.amazon.com/certification/certification-digital-badges/" or "https://cp.certmetrics.com/amazon/en/public/verify/credential",
    "issue_date": "2025-03-01",
    "expiry_date": "2028-03-01",
}


def test_unverified_result_added_to_review_queue():
    review_queue.clear()

    result = verify_aws(invalid_candidate)

    add_to_review_queue(result)

    assert len(get_review_queue()) == 1
    assert get_review_queue()[0]["verificationResult"]["status"] == result["verificationResult"]["status"]