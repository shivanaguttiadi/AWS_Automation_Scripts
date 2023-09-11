import boto3
from tabulate import tabulate

# Initialize the Boto3 EC2 client
ec2 = boto3.client('ec2')

# Specify VPC parameters
vpc_cidr_block = '10.0.0.0/16'
vpc_name = 'MytestVPC2'

# Create the VPC
response = ec2.create_vpc(CidrBlock=vpc_cidr_block)
vpc_id = response['Vpc']['VpcId']

# Add a name tag to the VPC
ec2.create_tags(Resources=[vpc_id], Tags=[{'Key': 'Name', 'Value': vpc_name}])

# Create a table for VPC information
table_headers = ["VPC Name", "VPC ID"]
table_data = [[vpc_name, vpc_id]]
table = tabulate(table_data, headers=table_headers, tablefmt="grid")

print("VPC Created:")
print(table)
