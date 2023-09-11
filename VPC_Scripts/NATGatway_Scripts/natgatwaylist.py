import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Describe NAT Gateways
response = ec2.describe_nat_gateways()

# Extract NAT Gateway information
nat_gateways = response['NatGateways']

# Create a table for the output
table = PrettyTable()
table.field_names = ["NAT Gateway ID", "State", "VPC ID", "Subnet ID"]

# Populate the table with NAT Gateway information
for nat_gateway in nat_gateways:
    nat_gateway_id = nat_gateway['NatGatewayId']
    state = nat_gateway['State']
    vpc_id = nat_gateway['VpcId']
    subnet_id = nat_gateway['SubnetId']

    table.add_row([nat_gateway_id, state, vpc_id, subnet_id])

# Print the formatted table
print(table)
