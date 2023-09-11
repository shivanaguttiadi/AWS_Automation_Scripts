import boto3

# Initialize the Boto3 S3 client
s3 = boto3.client('s3')

# List of valid S3 bucket names to delete
buckets_to_delete = ['shivanagutti1', 'shivanagutti2']

# Create a list to store the names of successfully deleted buckets
deleted_buckets = []

# Iterate through the list of bucket names
for bucket_name in buckets_to_delete:
    try:
        # List all versions of objects in the bucket
        versions_response = s3.list_object_versions(Bucket=bucket_name)

        # Delete all versions of objects in the bucket
        for version in versions_response.get('Versions', []):
            s3.delete_object(
                Bucket=bucket_name,
                Key=version['Key'],
                VersionId=version['VersionId']
            )
            print(f"Deleted version '{version['VersionId']}' in bucket '{bucket_name}'")

        # Delete the S3 bucket
        s3.delete_bucket(Bucket=bucket_name)

        # If deletion is successful, add the bucket name to the list of deleted buckets
        deleted_buckets.append(bucket_name)
        print(f"Deleted bucket '{bucket_name}'")
    except Exception as e:
        print(f"Failed to delete bucket '{bucket_name}': {e}")

# Print the list of deleted buckets
print("\nList of Deleted S3 Buckets:")
for deleted_bucket in deleted_buckets:
    print(deleted_bucket)
