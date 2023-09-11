import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the Route 53 service without specifying credentials or region
route53 = boto3.client('route53')

# List hosted zones
response = route53.list_hosted_zones()

# Extract the hosted zones from the response
hosted_zones = response['HostedZones']

# Create a table for the hosted zone information
table = PrettyTable()
table.field_names = ["Hosted Zone ID", "Name", "Resource Record Set Count", "Private Zone"]

# Populate the table with hosted zone details
for hosted_zone in hosted_zones:
    hosted_zone_id = hosted_zone['Id'].split("/")[-1]
    name = hosted_zone['Name']
    rrset_count = hosted_zone['ResourceRecordSetCount']
    is_private_zone = hosted_zone['Config']['PrivateZone']

    table.add_row([hosted_zone_id, name, rrset_count, is_private_zone])

# Print the table
print(table)
