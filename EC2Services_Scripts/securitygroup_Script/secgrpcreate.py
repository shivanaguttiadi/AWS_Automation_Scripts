import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Define the parameters for the security group
group_name = 'Testmysg'
description = 'My security group description'
vpc_id = 'vpc-0b8f53f49951033fb'  # Replace with your VPC ID

# Create the security group
response = ec2.create_security_group(
    GroupName=group_name,
    Description=description,
    VpcId=vpc_id
)

# Retrieve the security group ID from the response
security_group_id = response['GroupId']

# Create a table with proper formatting for the security group details
table = PrettyTable()
table.field_names = ["Security Group Name", "Security Group ID"]

# Set column alignment
table.align["Security Group Name"] = "l"
table.align["Security Group ID"] = "l"

# Add the security group details to the table
table.add_row([group_name, security_group_id])

# Print the properly formatted table
print(table)
