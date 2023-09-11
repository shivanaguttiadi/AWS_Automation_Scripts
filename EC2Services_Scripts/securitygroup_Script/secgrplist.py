import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Retrieve a list of all Security Groups
security_groups = ec2.describe_security_groups()['SecurityGroups']

# Create a table with proper formatting
table = PrettyTable()
table.field_names = ["Security Group ID", "Security Group Name", "Description"]

# Set column alignment and width
table.align["Security Group ID"] = "l"
table.align["Security Group Name"] = "l"
table.align["Description"] = "l"
table.max_width["Description"] = 40  # Adjust the maximum width for the Description column

# Populate the table with Security Group information
for sg in security_groups:
    sg_id = sg['GroupId']
    sg_name = sg['GroupName']
    description = sg['Description']
    
    table.add_row([sg_id, sg_name, description])

# Print the properly formatted table
print(table)

# Print the total count of Security Groups
print(f"Total Security Groups: {len(security_groups)}")
