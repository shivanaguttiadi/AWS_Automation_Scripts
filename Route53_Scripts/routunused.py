import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the Route 53 service without specifying credentials or region
route53 = boto3.client('route53')

# List hosted zones
response = route53.list_hosted_zones()

# Extract the hosted zones from the response
hosted_zones = response['HostedZones']

# Create a table with proper formatting for unused hosted zones
table = PrettyTable()
table.field_names = ["Hosted Zone ID", "Name", "Private Zone", "Resource Record Set Count"]

# Flag to check if any unused hosted zones are found
unused_zones_found = False

# Iterate through hosted zones and filter unused ones (with no domains)
for hosted_zone in hosted_zones:
    zone_id = hosted_zone['Id'].split('/')[-1]  # Extract the zone ID
    name = hosted_zone['Name']
    private_zone = hosted_zone['Config']['PrivateZone']
    resource_record_set_count = hosted_zone['ResourceRecordSetCount']

    # Check if the hosted zone has no associated domain names
    if resource_record_set_count == 0:
        table.add_row([zone_id, name, private_zone, resource_record_set_count])
        unused_zones_found = True

# If unused hosted zones are found, print the table of unused hosted zones
if unused_zones_found:
    print(table)
else:
    print("No unused hosted zones found.")
