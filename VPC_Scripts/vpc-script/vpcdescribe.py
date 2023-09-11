import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Retrieve a list of all VPCs
vpcs = ec2.describe_vpcs()

# Create a table with proper formatting and specify column widths
table = PrettyTable()
table.field_names = ["VPC Name", "VPC ID", "Subnets", "Route Tables", "Network Connections"]
table.align = 'l'
table.max_width = 50  # Adjust this value to your preferred column width

# Function to get VPC Name from Tags
def get_vpc_name(tags):
    for tag in tags:
        if tag['Key'] == 'Name':
            return tag['Value']
    return ''

# Iterate through each VPC
for vpc in vpcs['Vpcs']:
    vpc_id = vpc['VpcId']
    vpc_name = get_vpc_name(vpc['Tags'])

    # Retrieve the subnets in the VPC
    subnets = ec2.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
    subnet_ids = ', '.join([subnet['SubnetId'] for subnet in subnets['Subnets']])
    
    # Retrieve the route tables associated with the VPC
    route_tables = ec2.describe_route_tables(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
    route_table_ids = ', '.join([rt['RouteTableId'] for rt in route_tables['RouteTables']])
    
    # Retrieve the network connections associated with the VPC
    network_connections = ec2.describe_vpn_connections(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
    connection_ids = ', '.join([conn['VpnConnectionId'] for conn in network_connections['VpnConnections']])
    
    table.add_row([vpc_name, vpc_id, subnet_ids, route_table_ids, connection_ids])

# Print the formatted table
print(table)
