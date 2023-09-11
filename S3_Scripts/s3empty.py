import boto3
from tabulate import tabulate

# Initialize the Boto3 S3 client
s3 = boto3.client('s3')

# List all S3 buckets
response = s3.list_buckets()

# Create a list to store empty bucket names
empty_bucket_names = []

# Iterate through the list of buckets
for bucket in response['Buckets']:
    bucket_name = bucket['Name']
    
    # List objects in the bucket
    objects_response = s3.list_objects_v2(Bucket=bucket_name)
    
    # Check if the bucket is empty (no objects)
    if 'Contents' not in objects_response:
        empty_bucket_names.append(bucket_name)

# Calculate the total empty bucket count
total_empty_bucket_count = len(empty_bucket_names)

# Create a table and print it for empty bucket information
table_headers = ["Empty Bucket Name"]
table = tabulate([[bucket_name] for bucket_name in empty_bucket_names], headers=table_headers, tablefmt="grid")

# Print the list of empty buckets with details and the total count
print("List of Empty S3 Buckets:")
print(table)
print("\nTotal Empty Bucket Count:", total_empty_bucket_count)
