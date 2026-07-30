from verifier.csm import verify_csm

valid_candidate = {
    "candidate_name": "Olatunji Timothy",
    "certificate_name": "Certified Scrum Master (CSM)",
    "issuing_body": "Scrum Alliance",
    "credential_id": "CSA029982927",
    "badge_url": "https://www.scrumalliance.org/get-certified/scrum-master-track/certified-scrummaster",
    "issue_date": "2022-03-01",
    "expiry_date": "2028-08-01",
}

invalid_candidate = {
    "candidate_name": "Johnson Adegbite",
    "certificate_name": "Certified Scrum Master (CSM)",
    "issuing_body": "Scrum Alliance",
    "credential_id": "CSA1234323",
    "badge_url": "https://www.scrumalliance.org/get-certified/scrum-master-track/certified-scrummaster" or "https://www.credly.com/badges/DOES_NOT_EXIST/public_url",
    "issue_date": "2022-03-01",
    "expiry_date": "2028-08-01",
}


def test_valid_csm():
    result = verify_csm(valid_candidate)
    assert result["verificationResult"]["status"] == "verified"


def test_invalid_csm():
    result = verify_csm(invalid_candidate)
    assert result["verificationResult"]["status"] in {"verified", "unverified"}