import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Retrieve a list of Elastic IP addresses
eip_addresses = ec2.describe_addresses()['Addresses']

# Create a table with proper formatting for the EIPs
table = PrettyTable()
table.field_names = ["Elastic IP", "Instance ID", "Allocation ID", "Association ID", "Private IP"]

# Populate the table with EIP information
for eip in eip_addresses:
    elastic_ip = eip['PublicIp']
    instance_id = eip.get('InstanceId', 'N/A')
    allocation_id = eip.get('AllocationId', 'N/A')
    association_id = eip.get('AssociationId', 'N/A')
    private_ip = eip.get('PrivateIpAddress', 'N/A')

    table.add_row([elastic_ip, instance_id, allocation_id, association_id, private_ip])

# Print the formatted table
print(table)
