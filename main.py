from models import create_tables
from verification import save_verification

from verifier.microsoft import verify_microsoft
from verifier.cisco import verify_cisco
from verifier.aws import verify_aws

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

print(microsoft_result)
print(cisco_result)
print(aws_result)