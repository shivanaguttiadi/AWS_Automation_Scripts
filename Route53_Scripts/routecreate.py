import boto3

# Create a Boto3 client for the Route 53 service without specifying credentials or region
route53 = boto3.client('route53')

# Define the hosted zone name, comment, DNS record name, and value
hosted_zone_name = "example.com"
comment = "This is an example hosted zone"
dns_record_name = "example.com"
dns_record_value = "192.168.1.1"

# Create the hosted zone
response = route53.create_hosted_zone(
    Name=hosted_zone_name,
    CallerReference="unique-identifier",  # Replace with a unique reference
    HostedZoneConfig={
        'Comment': comment
    }
)

# Extract the hosted zone ID
hosted_zone_id = response['HostedZone']['Id'].split('/')[-1]

# Create a change batch to add the A record
change_batch = {
    'Changes': [
        {
            'Action': 'CREATE',
            'ResourceRecordSet': {
                'Name': dns_record_name,
                'Type': 'A',
                'TTL': 300,
                'ResourceRecords': [{'Value': dns_record_value}]
            }
        }
    ]
}

# Update the hosted zone with the new DNS record
response = route53.change_resource_record_sets(
    HostedZoneId=hosted_zone_id,
    ChangeBatch=change_batch
)

print(f"Hosted Zone {hosted_zone_name} created with ID: {hosted_zone_id}")
print(f"A record added for {dns_record_name}")
