import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Describe Elastic IP addresses
response = ec2.describe_addresses()

# Filter out Elastic IPs that are not associated with instances
unused_elastic_ips = [ip for ip in response['Addresses'] if 'InstanceId' not in ip]

# Create a table with proper formatting for unused Elastic IPs
table = PrettyTable()
table.field_names = ["Elastic IP Address", "Domain", "Allocation ID"]

# Populate the table with unused Elastic IP information
for ip in unused_elastic_ips:
    elastic_ip_address = ip['PublicIp']
    domain = ip['Domain']
    allocation_id = ip['AllocationId']

    table.add_row([elastic_ip_address, domain, allocation_id])

# Print the formatted table of unused Elastic IPs
print(table)
