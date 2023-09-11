import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the Elastic Load Balancing service without specifying credentials or region
elbv2 = boto3.client('elbv2')

# Describe all load balancers in your AWS account
load_balancers = elbv2.describe_load_balancers()['LoadBalancers']

# Create a table to display the load balancer details
load_balancer_table = PrettyTable()
load_balancer_table.field_names = [
    "Load Balancer Name", "DNS Name", "State", "VPC ID",
    "Availability Zones", "Type", "Date Created"
]

# Iterate through the load balancers and populate the table
for lb in load_balancers:
    lb_name = lb['LoadBalancerName']
    dns_name = lb['DNSName']
    state = lb['State']['Code']
    vpc_id = lb['VpcId']
    azs = ', '.join([az['ZoneName'] for az in lb['AvailabilityZones']])
    lb_type = lb['Type']
    create_time = lb['CreatedTime'].strftime('%Y-%m-%d %H:%M:%S')
    
    # Check if 'Reason' exists in the state dictionary
    reason = lb['State'].get('Reason', 'N/A')
    
    # Convert dictionary fields to string representation
    state_str = f"{state} ({reason})"
    
    load_balancer_table.add_row([lb_name, dns_name, state_str, vpc_id, azs, lb_type, create_time])

# Print the table of load balancer details
print("Load Balancer Details:")
print(load_balancer_table)
