import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Create the Internet Gateway
response = ec2.create_internet_gateway()

# Retrieve the Internet Gateway ID from the response
igw_id = response['InternetGateway']['InternetGatewayId']

# Add a name tag to the Internet Gateway
ec2.create_tags(Resources=[igw_id], Tags=[{'Key': 'Name', 'Value': 'MyInternetGateway'}])

print(f'Internet Gateway created with ID: {igw_id}')
print('table')