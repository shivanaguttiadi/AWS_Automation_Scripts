import boto3

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Define a list of security group IDs to delete
security_group_ids = [
    'sg-040e5cba227e9bb15',
    'sg-0648d820b733c22d1',
    'sg-049ed7251b64135e0',
    'sg-086094dd6a67d431d',
    'sg-0fe6b35ef645494e1',
    'sg-0443ba805eb7707ec',
    'sg-04e8ce6897a7bf595',
    'sg-022890c9fd25d7fdd',
    'sg-0adfc8217e627456e',
    'sg-0e5ea83ccd12e206d',
    'sg-07c2e64fe382a551b',
    'sg-029d1893b5b60be1c',
    'sg-0c6c73b1ae24c9d0c',
    'sg-06ccd1863a0046fd2',
    'sg-0da7020f0a978c02b',
    'sg-0f4a6f93cee33dd7e',
    'sg-0fc88887bdff21bef'
]   # Replace with your security group IDs

# Initialize a variable to count deleted security groups
deleted_count = 0

# Loop through the list of security group IDs and delete each one
for sg_id in security_group_ids:
    try:
        ec2.delete_security_group(GroupId=sg_id)
        deleted_count += 1
        print(f'Security group with ID {sg_id} has been deleted.')
    except Exception as e:
        print(f'Failed to delete security group with ID {sg_id}: {e}')

# Print the total count of specified security groups deleted
print(f'Total {deleted_count} specified security groups have been deleted.')
