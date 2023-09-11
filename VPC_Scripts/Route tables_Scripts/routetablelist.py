import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Retrieve a list of all route tables
route_tables = ec2.describe_route_tables()['RouteTables']

# Create a table with proper formatting
table = PrettyTable()
table.field_names = ["Route Table Name", "Route Table ID", "Attached VPC"]

# Function to get the attached VPC ID
def get_attached_vpc(route_table):
    for association in route_table.get('Associations', []):
        if not association.get('Main'):
            return association.get('VpcId', 'N/A')
    return 'N/A'

# Populate the table with route table information
for route_table in route_tables:
    route_table_id = route_table['RouteTableId']
    route_table_name = ''

    # Check if the route table has a name tag
    for tag in route_table.get('Tags', []):
        if tag['Key'] == 'Name':
            route_table_name = tag['Value']
            break

    # Get the attached VPC ID
    attached_vpc_id = get_attached_vpc(route_table)

    table.add_row([route_table_name, route_table_id, attached_vpc_id])

# Set the alignment for all columns to 'l' for left-aligned
table.align = 'l'

# Print the formatted table
print(table)
