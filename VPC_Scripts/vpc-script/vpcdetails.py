import boto3
from tabulate import tabulate

# Initialize the Boto3 EC2 client
ec2 = boto3.client('ec2')

# List all VPCs
response = ec2.describe_vpcs()

# Create a list to store VPC details
vpc_details = []

# Iterate through the list of VPCs
for vpc in response['Vpcs']:
    vpc_id = vpc['VpcId']
    cidr_block = vpc['CidrBlock']
    
    # Determine if the VPC is a default VPC
    is_default = vpc['IsDefault']
    
    # Retrieve VPC name from tags (if available)
    vpc_name = 'N/A'
    for tag in vpc.get('Tags', []):
        if tag['Key'] == 'Name':
            vpc_name = tag['Value']
            break
    
    vpc_details.append([vpc_id, cidr_block, 'Default' if is_default else 'Custom', vpc_name])

# Create a table and print it for VPC information
table_headers = ["VPC ID", "IPv4 CIDR", "State", "VPC Name"]
table = tabulate(vpc_details, headers=table_headers, tablefmt="grid")

# Print the list of VPCs with details in tabular format
print("List of VPCs with IDs, IPv4 CIDR, State, and Names:")
print(table)
