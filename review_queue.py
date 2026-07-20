from typing import Any

REVIEW_THRESHOLD = 80

review_queue: list[dict[str, Any]] = []


def add_to_review_queue(result: dict[str, Any]) -> None:
    """
    Add verification results with low confidence
    to the review queue.
    """

    verification = result["verificationResult"]

    if verification["confidenceScore"] < REVIEW_THRESHOLD:
        review_queue.append(result)


def get_review_queue() -> list[dict[str, Any]]:
    """
    Return all verification results
    that require manual review.
    """

    return review_queue