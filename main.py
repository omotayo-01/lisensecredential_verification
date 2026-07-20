from models import create_tables
from verification import save_verification
from verifier.microsoft import verify_microsoft
from verifier.cisco import verify_cisco
from verifier.aws import verify_aws
from verifier.ican import verify_ican
from verifier.icu import verify_icu
from verifier.rn import verify_rn
from verifier.aacn import verify_aacn
from verifier.ctia import verify_ctia
from verifier.csm import verify_csm
from verifier.gpca import verify_gpca
from verifier.sca import verify_sca
from verifier.pmp import verify_pmp
from verifier.itil import verify_itil
from verifier.tds import verify_tds
from verifier.rhcsa import verify_rhcsa
from verifier.vcp import verify_vcp
from review_queue import add_to_review_queue, get_review_queue
# Create the database table
create_tables()

# Microsoft
microsoft_candidate = {
   "candidate_name": "Akanbi Olukayode",
        "certificate_name": "Microsoft Certified: Azure AI Engineer Associate",
        "issuing_body": "Microsoft",
        "badge_url": "https://www.credly.com/badges/xxxxxxxxxxxxxxxx/public_url",
        "credential_id": "ABC123456789",
        "issue_date": "2025-05-10",
        "expiry_date": "None"
}
microsoft_result = verify_microsoft(microsoft_candidate)
save_verification(microsoft_result)
add_to_review_queue(microsoft_result)

# Cisco
cisco_candidate = {
"candidate_name": "Oladotun David",
        "certificate_name": "Cisco Certified Network Associate",
        "issuing_body": "Cisco",
        "credential_id": "CCNA123456",
        "issue_date": "2025-01-15",
        "expiry_date": "2028-01-15"
    }
cisco_result = verify_cisco(cisco_candidate)
save_verification(cisco_result)
add_to_review_queue(cisco_result)
# AWS
aws_candidate = {
    "candidate_name": "Yemi Olaniyan",
    "certificate_name": "AWS Certified Solutions Architect Associate",
    "issuing_body": "Amazon Web Services",
    "credential_id": "AWS123456",
    "badge_url": "https://www.credly.com/badges/xxxxxxxxxxxxxxxx/public_url",
    "issue_date": "2025-03-01",
    "expiry_date": "2028-03-01",
}

aws_result = verify_aws(aws_candidate)
save_verification(aws_result)
add_to_review_queue(aws_result)

#Ican
ican_result = verify_ican()
save_verification(ican_result)

#Aacn
aacn_result = verify_aacn()
save_verification(aacn_result)

#Rn
rn_result = verify_rn()
save_verification(rn_result)

#Icu
icu_result = verify_icu()
save_verification(icu_result)

#Ctia
ctia_result = verify_ctia()
save_verification(ctia_result)

#Csm
csm_result = verify_csm()
save_verification(csm_result)

#Gpca
gpca_result = verify_gpca()
save_verification(gpca_result)

#Sca
sca_result = verify_sca()
save_verification(sca_result)

#Pmp
pmp_result = verify_pmp()
save_verification(pmp_result)

#Itil
itil_result = verify_itil()
save_verification(itil_result)

#Tds
tds_result = verify_tds()
save_verification(tds_result)

#Rhcsa
rhcsa_result = verify_rhcsa()
save_verification(rhcsa_result)

#Vcp
vcp_result = verify_vcp()
save_verification(vcp_result)

print(microsoft_result)
print(cisco_result)
print(aws_result)
print(ican_result)
print(rn_result)
print(icu_result)
print(aacn_result)
print(ctia_result)
print(csm_result)
print(gpca_result)
print(sca_result)
print(pmp_result)
print(itil_result)
print(tds_result)
print(rhcsa_result)
print(vcp_result)
print("\nNeeds Review Queue")
print(get_review_queue())