import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Specify the ID of the network interface you want to delete
network_interface_id = 'eni-03f91f21160aadc26'

# Delete the network interface
ec2.delete_network_interface(NetworkInterfaceId=network_interface_id)

print(f'Network interface with ID {network_interface_id} has been deleted.')
