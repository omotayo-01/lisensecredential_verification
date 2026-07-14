from typing import Literal

VerificationStatus = Literal["verified", "unverified", "No public verification method exists"]

def calculate_confidence(status: VerificationStatus) -> int:
    """
    Return a confidence score (0-100) based on the verification status.
    """

    scores = {
        "verified": 95,
        "possible_match": 70,
        "not_found": 30,
        "mismatch": 0,
    }

    return scores.get(status, 0)