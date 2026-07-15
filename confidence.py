from typing import Literal

VerificationStatus = Literal["verified", "unverified", "No public verification method exists", "mismatch"]

def calculate_confidence(status: VerificationStatus) -> int:
    """
    Return a confidence score (0-100) based on the verification status.
    """

    scores = {
        "verified": 95-100,
        "possible_match": 70-94,
        "No public verification method exists": 30-69,
        "mismatch": 0-29,
    }

    return scores.get(status, 0)