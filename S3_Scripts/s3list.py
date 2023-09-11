import boto3
from tabulate import tabulate

# Initialize the Boto3 S3 client
s3 = boto3.client('s3')

# List all S3 buckets
response = s3.list_buckets()

# Extract bucket names
bucket_names = [bucket['Name'] for bucket in response['Buckets']]

# Calculate the total bucket count
total_bucket_count = len(bucket_names)

# Create a table and print it for bucket information
table_headers = ["Bucket Name"]
table = tabulate([[bucket_name] for bucket_name in bucket_names], headers=table_headers, tablefmt="grid")

# Print the list of buckets and the total count
print("List of S3 Buckets:")
print(table)
print("\nTotal Bucket Count:", total_bucket_count)
