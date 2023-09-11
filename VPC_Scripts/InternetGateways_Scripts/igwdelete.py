import boto3
from prettytable import PrettyTable
# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Replace the list of IGW IDs with the IDs of the Internet Gateways you want to delete
igw_ids = ['igw-09a22dab83ece3da0']

# Loop through the list of IGW IDs and delete each one without confirmation
for igw_id in igw_ids:
    try:
        # Delete the Internet Gateway
        ec2.delete_internet_gateway(InternetGatewayId=igw_id)
        print(f'Internet Gateway with ID {igw_id} has been deleted.')
    except Exception as e:
        print(f'Failed to delete Internet Gateway with ID {igw_id}: {str(e)}')
