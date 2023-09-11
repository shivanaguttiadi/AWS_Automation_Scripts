import boto3
from tabulate import tabulate
from datetime import datetime

# Initialize the Boto3 S3 client
s3 = boto3.client('s3')

# List of S3 bucket names to create
buckets_to_create = ['shivanagutti1', 'shivanagutti2', 'shivanagutti3']

# Create a list to store bucket details
bucket_details = []

# Create the S3 buckets
for bucket_name in buckets_to_create:
    try:
        # Create the S3 bucket without specifying a location constraint
        s3.create_bucket(
            Bucket=bucket_name
        )
        print(f"Bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print(f"Failed to create bucket '{bucket_name}': {e}")

# List all S3 buckets
response = s3.list_buckets()

# Iterate through the list of buckets
for bucket in response['Buckets']:
    bucket_name = bucket['Name']
    
    # Get bucket creation date
    creation_date = bucket['CreationDate']
    creation_date_str = creation_date.strftime('%Y-%m-%d %H:%M:%S')
    
    # Combine information into a list
    bucket_info = [bucket_name, creation_date_str]
    
    bucket_details.append(bucket_info)

# Calculate the total bucket count
total_bucket_count = len(bucket_details)

# Create a table and print it for bucket information
table_headers = ["Bucket Name", "Created At"]
table = tabulate(bucket_details, headers=table_headers, tablefmt="grid")

# Print the list of buckets with details and the total count
print("List of S3 Buckets with Details:")
print(table)
print("\nTotal Bucket Count:", total_bucket_count)


