from models import create_tables
from verification import save_verification

from verifier.microsoft import verify_microsoft
from verifier.cisco import verify_cisco
from verifier.aws import verify_aws
from verifier.ican import verify_ican
from verifier.icu import verify_icu
from verifier.rn import verify_rn
from verifier.aacn import verify_aacn

# Create the database table
create_tables()

# Microsoft
microsoft_result = verify_microsoft()
save_verification(microsoft_result)

# Cisco
cisco_result = verify_cisco()
save_verification(cisco_result)

# AWS
aws_result = verify_aws()
save_verification(aws_result)

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

print(microsoft_result)
print(cisco_result)
print(aws_result)
print(ican_result)
print(rn_result)
print(icu_result)
print(aacn_result)