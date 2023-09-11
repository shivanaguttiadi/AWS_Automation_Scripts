import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the Elastic Load Balancing service without specifying credentials or region
elbv2 = boto3.client('elbv2')

# Describe all load balancers in your AWS account
load_balancers = elbv2.describe_load_balancers()['LoadBalancers']

# Create a table to display the load balancers
load_balancers_table = PrettyTable()
load_balancers_table.field_names = ["Load Balancer Name", "DNS Name", "Scheme", "VPC ID"]

# Iterate through the load balancers and populate the table
for lb in load_balancers:
    lb_name = lb['LoadBalancerName']
    dns_name = lb['DNSName']
    scheme = lb['Scheme']
    vpc_id = lb['VpcId']
    
    load_balancers_table.add_row([lb_name, dns_name, scheme, vpc_id])

# Print the table of load balancers
print("Load Balancers:")
print(load_balancers_table)
