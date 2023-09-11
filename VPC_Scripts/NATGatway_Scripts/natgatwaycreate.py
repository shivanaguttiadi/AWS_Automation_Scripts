import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Define the VPC ID where you want to create the NAT Gateway
vpc_id = 'vpc-0b8f53f49951033fb '  # Replace with your VPC ID

# Define the Subnet ID in which you want to create the NAT Gateway
subnet_id = '	subnet-0fcc8b21701a44b62'  # Replace with your Subnet ID

# Define the name for the NAT Gateway
nat_gateway_name = 'MyNATGatewaytest'  # Replace with your desired name

# Create the NAT Gateway
response = ec2.create_nat_gateway(
    SubnetId=subnet_id
)

# Retrieve the NAT Gateway ID from the response
nat_gateway_id = response['NatGateway']['NatGatewayId']

# Add a tag to the NAT Gateway with the specified name
ec2.create_tags(
    Resources=[nat_gateway_id],
    Tags=[
        {'Key': 'Name', 'Value': nat_gateway_name}
    ]
)

# Print the NAT Gateway information in a table format
table = PrettyTable()
table.field_names = ["Name", "NAT Gateway ID", "Subnet ID", "State"]

# Retrieve NAT Gateway information
nat_gateways = ec2.describe_nat_gateways(NatGatewayIds=[nat_gateway_id])['NatGateways']
if nat_gateways:
    nat_gateway_info = nat_gateways[0]
    name = nat_gateway_name
    nat_gateway_id = nat_gateway_info['NatGatewayId']
    subnet_id = nat_gateway_info['SubnetId']
    state = nat_gateway_info['State']

    table.add_row([name, nat_gateway_id, subnet_id, state])
else:
    print(f'NAT Gateway with ID {nat_gateway_id} not found.')

# Print the table
print(table)
