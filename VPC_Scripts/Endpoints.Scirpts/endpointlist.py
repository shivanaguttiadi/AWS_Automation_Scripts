import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Retrieve a list of all VPC endpoints in the AWS account
endpoints = ec2.describe_vpc_endpoints()['VpcEndpoints']

# Create a table with proper formatting and increased column spacing
table = PrettyTable()
table.field_names = ["Endpoint ID", "Service Name", "VPC ID", "State", "DNS Entries"]

# Set column max width to provide more space
table.max_width["Endpoint ID"] = 20
table.max_width["Service Name"] = 30
table.max_width["VPC ID"] = 20
table.max_width["State"] = 15

# Populate the table with endpoint information
for endpoint in endpoints:
    endpoint_id = endpoint['VpcEndpointId']
    service_name = endpoint['ServiceName']
    vpc_id = endpoint['VpcId']
    state = endpoint['State']
    dns_entries = ', '.join(entry['DnsName'] for entry in endpoint['DnsEntries'])
    
    table.add_row([endpoint_id, service_name, vpc_id, state, dns_entries])

# Set the alignment for all columns to 'l' for left-aligned
table.align = 'l'

# Print the formatted table
print(table)
