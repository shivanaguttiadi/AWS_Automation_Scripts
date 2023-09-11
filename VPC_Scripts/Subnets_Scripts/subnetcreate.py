import boto3

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Define the VPC ID where you want to create the subnet
vpc_id = 'vpc-0b8f53f49951033fb'

# Define the subnet parameters
subnet_cidr_block = '10.0.2.0/16'  # Replace with your desired CIDR block
availability_zone = 'us-east-1c'  # Replace with your desired availability zone
subnet_name = 'Mytestsubnet'  # Replace with your desired subnet name

# Create the subnet
response = ec2.create_subnet(
    VpcId=vpc_id,
    CidrBlock=subnet_cidr_block,
    AvailabilityZone=availability_zone
)

# Retrieve the subnet ID from the response
subnet_id = response['Subnet']['SubnetId']

# Create a tag for the subnet with the name
ec2.create_tags(
    Resources=[subnet_id],
    Tags=[
        {'Key': 'Name', 'Value': subnet_name}
    ]
)

# Print the subnet ID
print(f'Subnet created with ID: {subnet_id}')
