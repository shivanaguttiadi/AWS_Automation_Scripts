import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the Route 53 service without specifying credentials or region
route53 = boto3.client('route53')

# List hosted zones
response = route53.list_hosted_zones()

# Extract the hosted zones from the response
hosted_zones = response['HostedZones']

# Create a table with proper formatting for hosted zones
table = PrettyTable()
table.field_names = ["Hosted Zone ID", "Name", "Private Zone", "Resource Record Set Count"]

# Populate the table with hosted zone information
for hosted_zone in hosted_zones:
    zone_id = hosted_zone['Id'].split('/')[-1]  # Extract the zone ID
    name = hosted_zone['Name']
    private_zone = hosted_zone['Config']['PrivateZone']
    resource_record_set_count = hosted_zone['ResourceRecordSetCount']

    table.add_row([zone_id, name, private_zone, resource_record_set_count])

# Print the formatted table
print(table)
