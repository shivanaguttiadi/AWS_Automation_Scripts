import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the Auto Scaling service without specifying credentials or region
autoscaling = boto3.client('autoscaling')

# Describe all Auto Scaling groups
response = autoscaling.describe_auto_scaling_groups()

# Create a table with proper formatting for Auto Scaling groups
table = PrettyTable()
table.field_names = ["Auto Scaling Group Name", "Launch Configuration", "Min Size", "Max Size", "Desired Capacity", "VPC Zone Identifier"]

# Populate the table with Auto Scaling group information
for group in response['AutoScalingGroups']:
    group_name = group['AutoScalingGroupName']
    launch_configuration = group['LaunchConfigurationName']
    min_size = group['MinSize']
    max_size = group['MaxSize']
    desired_capacity = group['DesiredCapacity']
    vpc_zone = ', '.join(group['VPCZoneIdentifier']) if 'VPCZoneIdentifier' in group else 'N/A'

    table.add_row([group_name, launch_configuration, min_size, max_size, desired_capacity, vpc_zone])

# Print the formatted table
print(table)
