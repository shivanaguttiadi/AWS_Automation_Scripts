import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Get a list of all VPCs in the AWS account
vpcs = ec2.describe_vpcs()['Vpcs']

# Create a table with proper formatting
table = PrettyTable()
table.field_names = ["VPC ID", "Subnet ID", "Subnet Name"]

# Function to check if a subnet has dependencies
def has_dependencies(subnet_id):
    response = ec2.describe_network_interfaces(Filters=[{'Name': 'subnet-id', 'Values': [subnet_id]}])
    return len(response['NetworkInterfaces']) > 0

# Iterate through each VPC
for vpc in vpcs:
    vpc_id = vpc['VpcId']
    
    # Get a list of subnets in the VPC
    subnets = ec2.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])['Subnets']
    
    # Filter subnets that have no dependencies
    independent_subnets = [subnet for subnet in subnets if not has_dependencies(subnet['SubnetId'])]
    
    # Add rows to the table for independent subnets
    for subnet in independent_subnets:
        subnet_id = subnet['SubnetId']
        subnet_name = subnet.get("Tags", [{"Key": "Name", "Value": "N/A"}])[0]["Value"]
        table.add_row([vpc_id, subnet_id, subnet_name])

# Set the alignment for all columns to 'l' for left-aligned
table.align = 'l'

# Print the formatted table
print(table)
