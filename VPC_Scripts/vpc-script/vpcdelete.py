import boto3

# Initialize the Boto3 EC2 client
ec2 = boto3.client('ec2')

# Replace 'your-vpc-id' with the ID of the VPC you want to delete
vpc_ids = ['vpc-0f08c672b32ad775a']

# Delete the VPCs
for vpc_id in vpc_ids:
    try:
        ec2.delete_vpc(VpcId=vpc_id)
        print(f"VPC '{vpc_id}' deleted successfully.")
    except Exception as e:
        print(f"Failed to delete VPC '{vpc_id}': {e}")
