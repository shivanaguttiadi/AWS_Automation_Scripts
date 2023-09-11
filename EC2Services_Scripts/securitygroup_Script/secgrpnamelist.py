import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Retrieve a list of all Security Groups
security_groups = ec2.describe_security_groups()['SecurityGroups']

# Create a table with proper formatting
table = PrettyTable()
table.field_names = ["Security Group Name", "VPC ID", "Name", "Description"]

# Set column alignment and width
table.align["Security Group Name"] = "l"
table.align["VPC ID"] = "l"
table.align["Name"] = "l"
table.align["Description"] = "l"
table.max_width["Description"] = 40  # Adjust the maximum width for the Description column

# Populate the table with Security Group information
for sg in security_groups:
    sg_name = sg['GroupName']
    vpc_id = sg['VpcId']
    
    # Initialize Name and Description to empty strings
    name = ""
    description = ""
    
    # Check for tags with Name and Description keys
    for tag in sg.get('Tags', []):
        if tag['Key'] == 'Name':
            name = tag['Value']
        elif tag['Key'] == 'Description':
            description = tag['Value']
    
    table.add_row([sg_name, vpc_id, name, description])

# Print the properly formatted table
print(table)
