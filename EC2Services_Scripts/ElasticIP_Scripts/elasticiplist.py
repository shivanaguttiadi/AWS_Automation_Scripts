import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Retrieve a list of Elastic IP addresses
eip_addresses = ec2.describe_addresses()['Addresses']

# Create a table with proper formatting for the EIPs
table = PrettyTable()
table.field_names = ["Elastic IP", "Instance Name", "Private IP"]

# Helper function to get the instance name from tags
def get_instance_name(tags):
    for tag in tags:
        if tag['Key'] == 'Name':
            return tag['Value']
    return 'N/A'

# Populate the table with EIP information
for eip in eip_addresses:
    elastic_ip = eip['PublicIp']
    instance_id = eip.get('InstanceId', 'N/A')
    private_ip = eip.get('PrivateIpAddress', 'N/A')

    if instance_id != 'N/A':
        instance = ec2.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]
        instance_name = get_instance_name(instance.get('Tags', []))
    else:
        instance_name = 'N/A'

    table.add_row([elastic_ip, instance_name, private_ip])

# Print the formatted table
print(table)
