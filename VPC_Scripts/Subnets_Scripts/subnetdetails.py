import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Retrieve a list of all subnets
subnets = ec2.describe_subnets()

# Create a table to store subnet details
table = PrettyTable()
table.field_names = ["VPC ID", "Subnet ID", "Subnet Name", "State", "Route Tables", "Network ACL ID"]

# Function to get Subnet Name from Tags
def get_subnet_name(tags):
    for tag in tags:
        if tag['Key'] == 'Name':
            return tag['Value']
    return ''

# Function to get associated route tables
def get_route_tables(subnet_id):
    route_table_ids = []
    route_tables = ec2.describe_route_tables(Filters=[{'Name': 'association.subnet-id', 'Values': [subnet_id]}])
    for rt in route_tables['RouteTables']:
        route_table_ids.append(rt['RouteTableId'])
    return ', '.join(route_table_ids)

# Iterate through each subnet
for subnet in subnets['Subnets']:
    vpc_id = subnet['VpcId']
    subnet_id = subnet['SubnetId']
    subnet_name = get_subnet_name(subnet.get('Tags', []))
    state = subnet['State']
    
    # Check if NetworkAclId key exists
    network_acl_id = subnet.get('NetworkAclId', '')
    
    # Retrieve the associated route table(s)
    route_tables = get_route_tables(subnet_id)
    
    table.add_row([vpc_id, subnet_id, subnet_name, state, route_tables, network_acl_id])

# Set the alignment for all columns to 'l' for left-aligned
table.align = 'l'

# Print the formatted table
print(table)
