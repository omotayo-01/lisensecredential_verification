from typing import Literal

VerificationStatus = Literal[
    "verified",
    "unverified",
    "No public verification method exists",
    "possible match",
]
def calculate_confidence(status: VerificationStatus) -> int:
    """
    Return a confidence score (0-100) based on the verification status.
    """

    scores = {
        "verified": 98,
        "possible match": 82,
        "No public verification method exists": 50,
        "unverified": 10,
    }

    return scores.get(status, 0)