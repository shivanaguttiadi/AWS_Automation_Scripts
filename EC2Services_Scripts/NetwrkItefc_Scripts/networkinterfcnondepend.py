import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Describe all network interfaces in your AWS account
network_interfaces = ec2.describe_network_interfaces()['NetworkInterfaces']

# Create a table to display the non-dependent network interfaces
non_dependent_interfaces_table = PrettyTable()
non_dependent_interfaces_table.field_names = ["Network Interface ID", "Status", "VPC ID", "Subnet ID"]

# Iterate through the network interfaces and filter out non-dependent ones
for interface in network_interfaces:
    interface_id = interface['NetworkInterfaceId']
    status = interface['Status']
    vpc_id = interface['VpcId']
    subnet_id = interface['SubnetId']
    
    # Check if the network interface is not attached to any instance
    if 'Attachment' not in interface:
        non_dependent_interfaces_table.add_row([interface_id, status, vpc_id, subnet_id])

# Print the table of non-dependent network interfaces
print("Non-Dependent Network Interfaces:")
print(non_dependent_interfaces_table)
