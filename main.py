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
from verifier.ecc import verify_ecc
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
ican_candidate = {
    "candidate_name": "Oluwapelumi Oluwatimileyin",
    "certificate_name": "ICAN membership",
    "issuing_body": "Institute of Chartered Accountants of Nigeria (ICAN)",
    "credential_id": "ICAN19680306",
    "badge_url": "https://www.credly.com/badges/xxxxxxxxxxxxxxxx/public_url",
    "issue_date": "2025-03-01",
    "expiry_date": "2028-03-01",
}
ican_result = verify_ican(ican_candidate)
save_verification(ican_result)
add_to_review_queue(ican_result)

#Aacn
aacn_candidate = {
        "candidate_name": "Makanjuola Dasola",
        "certificate_name": "Critical Care Registered Nurse(CCRN)",
        "issuing_body": "American Association of Critical-Care Nurses (AACN)",
        "credential_id": "CCRN2022002851",
        "issue_date": "2025-03-01",
        "expiry_date": "2038-03-01"
    }
aacn_result = verify_aacn(aacn_candidate)
save_verification(aacn_result)
add_to_review_queue(aacn_result)
#Rn
rn_candidate = {
    "candidate_name": "Oladokun Ayooluwa",
    "certificate_name": "Registered Nurse license (RN)",
    "issuing_body": "Nursing and Midwifery Council of Nigeria (NMCN)",
    "credential_id": "RN2022004008",
    "badge_url": "https://www.credly.com/badges/xxxxxxxxxxxxxxxx/public_url",
    "issue_date": "2025-03-01",
    "expiry_date": "2039-03-01",
}

rn_result = verify_rn(rn_candidate)
save_verification(rn_result)
add_to_review_queue(rn_result)

#Icu
icu_candidate = {
    "candidate_name": "Omotayo Uzumaki",
    "certificate_name": "Hospital ICU Training Certificate",
    "issuing_body": "Lagos University Teaching Hospital",
    "credential_id": "ICU1027156",
    "badge_url": "https://www.credly.com/badges/xxxxxxxxxxxxxxxx/public_url",
    "issue_date": "2025-03-01",
    "expiry_date": "2028-03-01",
}

icu_result = verify_icu(icu_candidate)
save_verification(icu_result)
add_to_review_queue(icu_result)

#Ctia
ctia_candidate = {
  "candidate_name": "Olatunji Timothy",
    "certificate_name": "CompTIA Security+",
    "issuing_body": "CompTIA",
    "credential_id": "Comp2022002005",
    "badge_url": "https://www.credly.com/badges/xxxxxxxxxxxxxxxx/public_url",
    "issue_date": "2022-03-01",
    "expiry_date": "2028-08-01",
}
ctia_result = verify_ctia(ctia_candidate)
save_verification(ctia_result)
add_to_review_queue(ctia_result)

#Csm
csm_result = verify_csm()
save_verification(csm_result)

#Gpca
gpca_candidate = {
    "candidate_name": "Kaboom Kabaam",
    "certificate_name": "Google Professional Cloud Architect",
    "issuing_body": "Google Cloud",
    "credential_id": "GPCA123456789",
    "badge_url": "https://www.credly.com/badges/xxxxxxxxxxxxxxxx/public_url",
    "issue_date": "2025-05-10",
    "expiry_date": "None",
}
gpca_result = verify_gpca(gpca_candidate)
save_verification(gpca_result)
add_to_review_queue(gpca_result)

#Sca
sca_candidate = {
    "candidate_name": "Akerele Idowu",
    "certificate_name": "Salesforce Certified Administrator",
    "issuing_body": "Salesforce",
    "credential_id": "SCA03032954",
    "email": "AkereleIdowu03@gmail.com",
    "issue_date": "2018-05-10",
    "expiry_date": "present",
}

sca_result = verify_sca(sca_candidate)
save_verification(sca_result)
add_to_review_queue(sca_result)

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

#Ecc
ecc_candidate = {
    "candidate_name": "Ajeigbe William",
    "certificate_name": "Certified Ethical Hacker (CEH)",
    "issuing_body": "Ec-Council",
    "credential_id": "ECC2022002845",
    "badge_url": "https://www.credly.com/badges/xxxxxxxxxxxxxxxx/public_url",
    "issue_date": "2023-03-01",
    "expiry_date": "2027-03-01",
}

ecc_result = verify_ecc(ecc_candidate)
save_verification(ecc_result)
add_to_review_queue(ecc_result)

print(microsoft_result)
print(ecc_result)
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