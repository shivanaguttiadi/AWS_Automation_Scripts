import boto3

# Initialize the Boto3 S3 client
s3 = boto3.client('s3')

# Replace 'your-bucket-name' with your desired bucket name
bucket_name = 'shivanaguttibucket'

try:
    # Create the S3 bucket without specifying a location constraint
    s3.create_bucket(
        Bucket=bucket_name
    )
    
    print(f"Bucket '{bucket_name}' created successfully.")
except Exception as e:
    print(f"Failed to create bucket '{bucket_name}': {e}")
