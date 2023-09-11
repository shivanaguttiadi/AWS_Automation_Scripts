import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the Elastic Load Balancing service without specifying credentials or region
elbv2 = boto3.client('elbv2')

# Define the name of the load balancer to delete
load_balancer_name = 'MyLoadBalancer'  # Replace with your load balancer name

# Delete the load balancer
elbv2.delete_load_balancer(
    LoadBalancerName=load_balancer_name
)

print(f'Load Balancer {load_balancer_name} has been deleted.')

# Get a list of deleted load balancers
deleted_load_balancers = [load_balancer_name]

# Create a table with the deleted load balancers
table = PrettyTable()
table.field_names = ["Deleted Load Balancers"]

# Populate the table with the deleted load balancers
for lb in deleted_load_balancers:
    table.add_row([lb])

# Print the formatted table
print(table)
