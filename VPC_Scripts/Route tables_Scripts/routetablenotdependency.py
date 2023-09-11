import boto3

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Retrieve a list of all route tables
route_tables = ec2.describe_route_tables()['RouteTables']

# Function to check if a route table is associated with any subnet
def is_route_table_associated(route_table_id):
    associations = ec2.describe_route_tables(RouteTableIds=[route_table_id])['RouteTables'][0]['Associations']
    return len(associations) > 0

# List to store route table IDs that are not dependent
independent_route_table_ids = []

# Find route tables that are not associated with any subnet
for route_table in route_tables:
    route_table_id = route_table['RouteTableId']
    
    if not is_route_table_associated(route_table_id):
        independent_route_table_ids.append(route_table_id)

# Print the list of independent route table IDs
print("Route Tables with No Subnet Dependencies:")
for route_table_id in independent_route_table_ids:
    print(route_table_id)
