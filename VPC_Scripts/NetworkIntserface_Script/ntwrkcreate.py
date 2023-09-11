import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Define the VPC ID where you want to create the network interface
vpc_id = 'vpc-040d82414abbbfebe '  # Replace with your VPC ID

# Define the subnet ID where you want to create the network interface
subnet_id = 'subnet-0dd6e978b589442b4'  # Replace with your Subnet ID

# Define the security group IDs to associate with the network interface
security_group_ids = ['	sg-0c659cbd3eb329939', '	sg-0161b1d2cdb240352']  # Replace with your Security Group IDs

# Create the network interface
response = ec2.create_network_interface(
    SubnetId=subnet_id,
    Groups=security_group_ids,
    Description='My Network Interface'  # Replace with your desired description
)

# Retrieve the network interface details
network_interface = response['NetworkInterface']

# Create a table with proper formatting for the network interface details
table = PrettyTable()
table.field_names = ["Attribute", "Value"]

# Populate the table with network interface information
table.add_row(["Network Interface ID", network_interface['NetworkInterfaceId']])
table.add_row(["Status", network_interface['Status']])
table.add_row(["VPC ID", network_interface['VpcId']])
table.add_row(["Subnet ID", network_interface['SubnetId']])
table.add_row(["Private IP", network_interface.get('PrivateIpAddress', 'N/A')])
table.add_row(["Public IP", network_interface.get('Association', {}).get('PublicIp', 'N/A')])
table.add_row(["Description", network_interface['Description']])

# Print the formatted table
print(table)
