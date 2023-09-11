import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Retrieve a list of network interfaces
network_interfaces = ec2.describe_network_interfaces()['NetworkInterfaces']

# Create a table with proper formatting
table = PrettyTable()
table.field_names = ["Interface ID", "Status", "VPC ID", "Subnet ID", "Private IP", "Public IP", "Security Groups"]

# Populate the table with network interface information
for interface in network_interfaces:
    interface_id = interface['NetworkInterfaceId']
    status = interface['Status']
    vpc_id = interface['VpcId']
    subnet_id = interface['SubnetId']
    private_ip = interface.get('PrivateIpAddress', 'N/A')
    public_ip = interface.get('Association', {}).get('PublicIp', 'N/A')
    security_groups = ', '.join([group['GroupName'] for group in interface.get('Groups', [])])

    table.add_row([interface_id, status, vpc_id, subnet_id, private_ip, public_ip, security_groups])

# Print the formatted table
print(table)
