import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Retrieve a list of all Security Groups
security_groups = ec2.describe_security_groups()['SecurityGroups']

# Retrieve a list of all EC2 instances
instances = ec2.describe_instances()

# Create a set to store Security Group IDs associated with instances
used_sg_ids = set()

# Populate the used_sg_ids set with Security Group IDs associated with instances
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        for sg in instance.get('SecurityGroups', []):
            used_sg_ids.add(sg['GroupId'])

# Filter and store only the unused Security Groups
unused_security_groups = [sg for sg in security_groups if sg['GroupId'] not in used_sg_ids]

# Create a table with proper formatting for unused Security Groups
table = PrettyTable()
table.field_names = ["Security Group ID", "Security Group Name"]

# Set column alignment
table.align["Security Group ID"] = "l"
table.align["Security Group Name"] = "l"

# Populate the table with unused Security Group information
for sg in unused_security_groups:
    sg_id = sg['GroupId']
    sg_name = sg['GroupName']
    
    table.add_row([sg_id, sg_name])

# Print the properly formatted table of unused Security Groups
print(table)
print(f"Total Security Groups: {len(security_groups)}")