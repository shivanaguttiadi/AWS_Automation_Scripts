import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Retrieve a list of network interfaces
network_interfaces = ec2.describe_network_interfaces()['NetworkInterfaces']

# Filter out network interfaces that are not attached to any EC2 instance and have no security groups
unused_interfaces = []
for interface in network_interfaces:
    attachment = interface.get('Attachment')
    if not attachment and not interface.get('Groups'):
        unused_interfaces.append(interface)

# Create a table with proper formatting for unused network interfaces
table = PrettyTable()
table.field_names = ["Interface ID", "Status", "VPC ID", "Subnet ID", "Private IP", "Public IP"]

# Populate the table with unused network interface information
for interface in unused_interfaces:
    interface_id = interface['NetworkInterfaceId']
    status = interface['Status']
    vpc_id = interface['VpcId']
    subnet_id = interface['SubnetId']
    private_ip = interface.get('PrivateIpAddress', 'N/A')
    public_ip = interface.get('Association', {}).get('PublicIp', 'N/A')

    table.add_row([interface_id, status, vpc_id, subnet_id, private_ip, public_ip])

# Check if there are any unused network interfaces
if unused_interfaces:
    # Print the formatted table of unused network interfaces
    print(table)
else:
    print("No unused network interfaces found.")
