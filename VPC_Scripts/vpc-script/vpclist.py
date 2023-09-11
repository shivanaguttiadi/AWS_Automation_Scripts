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
    
    # Retrieve VPC name from tags (if available)
    vpc_name = 'N/A'
    for tag in vpc.get('Tags', []):
        if tag['Key'] == 'Name':
            vpc_name = tag['Value']
            break
    
    vpc_details.append([vpc_id, vpc_name])

# Create a table and print it for VPC information
table_headers = ["VPC ID", "VPC Name"]
table = tabulate(vpc_details, headers=table_headers, tablefmt="grid")

# Print the list of VPCs with details in tabular format
print("List of VPCs with IDs and Names:")
print(table)
