import boto3
from tabulate import tabulate
from datetime import datetime

# Initialize the Boto3 S3 client
s3 = boto3.client('s3')

# List all S3 buckets
response = s3.list_buckets()

# Create a list to store bucket details
bucket_details = []

# Iterate through the list of buckets
for bucket in response['Buckets']:
    bucket_name = bucket['Name']
    
    # Get bucket creation date
    creation_date = bucket['CreationDate']
    creation_date_str = creation_date.strftime('%Y-%m-%d %H:%M:%S')
    
    # Get bucket location (AWS region)
    location_response = s3.get_bucket_location(Bucket=bucket_name)
    region = location_response.get('LocationConstraint', 'us-east-1') or 'us-east-1'
    
    # Get bucket ACL (Access Control List)
    acl_response = s3.get_bucket_acl(Bucket=bucket_name)
    
    # Extract the owner and permissions from the ACL response
    owner = acl_response.get('Owner', {}).get('DisplayName', 'N/A')
    grants = acl_response.get('Grants', [])
    access_permissions = [grant['Grantee'].get('DisplayName', 'N/A') for grant in grants]
    
    # Combine information into a dictionary
    bucket_info = {
        'Bucket Name': bucket_name,
        'Region': region,
        'Created At': creation_date_str,
        'Owner': owner,
        'Access Permissions': ', '.join(access_permissions),
    }
    
    bucket_details.append(bucket_info)

# Calculate the total bucket count
total_bucket_count = len(bucket_details)

# Create a table and print it for bucket information
table_headers = ["Bucket Name", "Region", "Created At", "Owner", "Access Permissions"]
table = tabulate(bucket_details, headers=table_headers, tablefmt="grid")

# Print the list of buckets with details and the total count
print("List of S3 Buckets with Details:")
print(table)
print("\nTotal Bucket Count:", total_bucket_count)
