import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Describe network interfaces
network_interfaces = ec2.describe_network_interfaces()['NetworkInterfaces']

# Create a table for the output
table = PrettyTable()
table.field_names = ["ID", "Name", "Status", "Subnet ID", "VPC ID", "Security Groups", "Instance ID"]

# Iterate through network interfaces and extract details
for interface in network_interfaces:
    network_interface_id = interface['NetworkInterfaceId']
    name = ""
    status = interface['Status']
    tags = interface.get('TagSet', [])
    subnet_id = interface['SubnetId']
    vpc_id = interface['VpcId']
    security_groups = ', '.join([group['GroupName'] for group in interface.get('Groups', [])])
    
    # Check if there is an attachment
    attachment = interface.get('Attachment')
    if attachment:
        instance_id = attachment.get('InstanceId', "N/A")
    else:
        instance_id = "N/A"

    # Find the 'Name' tag for the interface
    for tag in tags:
        if tag['Key'] == 'Name':
            name = tag['Value']
            break

    table.add_row([network_interface_id, name, status, subnet_id, vpc_id, security_groups, instance_id])

# Print the table
print(table)
