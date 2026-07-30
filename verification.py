from typing import Any
from requests import Response
import requests
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
        verification["confidenceScore"],
    ))
    conn.commit()
    conn.close()

    print("Verification saved to database.")
def send_request(url: str) -> Response | dict[str, str]:
    """
    Send a GET request to a certificate provider.
    """
    try:
        return requests.get(url, timeout=10)

    except requests.exceptions.SSLError as e:
        print(f"SSL error for {url}: {e}")
        # Retry once without certificate verification (some providers use cert chains
        # that aren't resolvable in the test environment). Prefer a verified request
        # but fall back to an insecure fetch so verifiers can still inspect content.
        try:
            resp = requests.get(url, timeout=10, verify=False)
            print(f"Retry succeeded for {url} with verify=False")
            return resp
        except requests.RequestException as e2:
            print(f"Insecure retry failed for {url}: {e2}")
            return {"error": "ssl"}
    except requests.exceptions.ConnectionError as e:
        print(f"connection error for {url}: {e}")
        return{
            "error": "timeout"
        }
    except requests.RequestException as e:
        print(f"connection error for {url}: {e}")
        return {
        "error": "request"
        }
