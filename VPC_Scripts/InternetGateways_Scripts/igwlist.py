import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Retrieve a list of Internet Gateways
igws = ec2.describe_internet_gateways()['InternetGateways']

# Create a table with proper formatting for IGW details
table = PrettyTable()
table.field_names = ["Name", "Internet Gateway ID", "State", "VPC ID"]

# Populate the table with IGW information
for igw in igws:
    igw_id = igw['InternetGatewayId']
    state = igw['Attachments'][0]['State'] if igw['Attachments'] else 'Detached'
    vpc_id = igw['Attachments'][0]['VpcId'] if igw['Attachments'] else 'N/A'
    igw_name = None

    # Check if the IGW has tags and retrieve the 'Name' tag if available
    for tag in igw.get('Tags', []):
        if tag['Key'] == 'Name':
            igw_name = tag['Value']
            break

    table.add_row([igw_name, igw_id, state, vpc_id])

# Print the formatted table
print(table)
