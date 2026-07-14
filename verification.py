from typing import Any
from database.database import get_connection
def save_verification(result: dict[str, Any]) -> None:
    conn = get_connection()
    cursor = conn.cursor()

    verification: dict[str, Any] = result["verificationResult"]
    claim: dict[str, Any] = verification["candidateClaim"]

    cursor.execute("""
        INSERT INTO certificate_verifications (
            candidate_name,
            certificate_name,
            issuing_body,
            credential_id,
            issue_date,
            expiry_date,
            status,
            confidence_score
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        claim["candidate_name"],
        claim["certificate_name"],
        claim["issuing_body"],
        claim["credential_id"],
        claim["issue_date"],
        claim["expiry_date"],
        verification["status"],
        verification["confidenceScore"]
    )
    )
    conn.commit()
    conn.close()

    print("Verification saved to database.")

