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
        "badge_url": "https://learn.microsoft.com/en-us/" or "https://certiport.pearsonvue.com/Certifications/Microsoft.aspx",
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
        "badge_url": "https://www.certmetrics.com/cisco/public/verification.asp?pid=1&aid=1&credid=CCNA123456",
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
    "badge_url": "https://cp.certmetrics.com/amazon/en/public/verify/credential" or "https://aws.amazon.com/certification/certification-digital-badges/",
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
    "badge_url": "https://www.icanig.org/ican/verify",
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
        "badge_url": "https://www.aacnnursing.org/",
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
    "badge_url": "https://www.nmcn.gov.ng/",
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
    "badge_url": "https://www.luth.gov.ng/",
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
    "badge_url": "https://www.comptia.org/en/certifications/security",
    "issue_date": "2022-03-01",
    "expiry_date": "2028-08-01",
}
ctia_result = verify_ctia(ctia_candidate)
save_verification(ctia_result)
add_to_review_queue(ctia_result)

#Csm
csm_candidate = {
    "candidate_name": "Olatunji Timothy",
    "certificate_name": "Certified Scrum Master (CSM)",
    "issuing_body": "Scrum Alliance",
    "credential_id": "CSA029982927",
    "badge_url": "https://www.scrumalliance.org/get-certified/scrum-master-track/certified-scrummaster",
    "issue_date": "2022-03-01",
    "expiry_date": "2028-08-01",
}
csm_result = verify_csm(csm_candidate)
save_verification(csm_result)
add_to_review_queue(csm_result)

#Gpca
gpca_candidate = {
    "candidate_name": "Kaboom Kabaam",
    "certificate_name": "Google Professional Cloud Architect",
    "issuing_body": "Google Cloud",
    "credential_id": "GPCA123456789",
    "badge_url": "https://info.credly.com/solutions/product-certifications",
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
    "badge_url": "https://www.salesforce.com/training/certification/",
    "email": "AkereleIdowu03@gmail.com",
    "issue_date": "2018-05-10",
    "expiry_date": "present",
}

sca_result = verify_sca(sca_candidate)
save_verification(sca_result)
add_to_review_queue(sca_result)

#PMP
pmp_candidate = {
    "candidate_name": "Esan Kemisola",
    "certificate_name": "Project Management Professional (PMP)",
    "issuing_body": "Project Management Institute (PMI)",
    "credential_id": "PMP70569w2982",
    "badge_url": "https://www.pmi.org/certifications/certification-resources/verify-pmp",
    "issue_date": "2020-02-10",
    "expiry_date": "2028-02-10",
}
pmp_result = verify_pmp(pmp_candidate)
save_verification(pmp_result)
add_to_review_queue(pmp_result)

#Itil
itil_candidate = {
    "candidate_name": "Goodyear Ebele",
    "certificate_name": "ITIL 4 Foundation",
    "issuing_body": "PeopleCert",
    "credential_id": "ITIL123456",
    "badge_url": "https://www.axelos.com/certifications/itil-certifications/verify-itil-certification",
    "issue_date": "2020-02-10",
    "expiry_date": "2027-02-10",
}
itil_result = verify_itil(itil_candidate)
save_verification(itil_result)
add_to_review_queue(itil_result)

#TDS
tds_candidate = {
    "candidate_name": "Oseni Samuel",
    "certificate_name": "Tableau Desktop Specialist",
    "issuing_body": "Tableau",
    "credential_id": "TAB03168927",
    "badge_url": "https://www.tableau.com/verify",
    "issue_date": "2024-03-01",
    "expiry_date": "2029-03-03",
}

tds_result = verify_tds(tds_candidate)
save_verification(tds_result)
add_to_review_queue(tds_result)

# RHCSA
rhcsa_candidate = {
    "candidate_name": "Modashola Abisade",
    "certificate_name": "Red Hat Certified System Administrator (RHCSA)",
    "issuing_body": "Red Hat",
    "credential_id": "RHCSA27893485",
    "badge_url": "https://www.redhat.com/en/services/certification/rhcsa",
    "issue_date": "2012-03-01",
    "expiry_date": "2028-08-01",
}

rhcsa_result = verify_rhcsa(rhcsa_candidate)
save_verification(rhcsa_result)
add_to_review_queue(rhcsa_result)

#VCP
vcp_candidate = {
    "candidate_name": "Fashina Rebecca",
    "certificate_name": "VMware Certified Professional (VCP)",
    "issuing_body": "VMware",
    "credential_id": "VMW2022007764",
    "badge_url": "https://cp.certmetrics.com/vmware/",
    "issue_date": "2023-04-14",
    "expiry_date": "2028-08-25",
}
vcp_result = verify_vcp(vcp_candidate)
save_verification(vcp_result)
add_to_review_queue(vcp_result)

#Ecc
ecc_candidate = {
    "candidate_name": "Ajeigbe William",
    "certificate_name": "Certified Ethical Hacker (CEH)",
    "issuing_body": "Ec-Council",
    "credential_id": "ECC2022002845",
    "badge_url": "https://aspen.eccouncil.org/Verify",
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