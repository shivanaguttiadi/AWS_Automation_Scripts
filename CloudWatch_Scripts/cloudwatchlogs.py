import boto3
from tabulate import tabulate

# Initialize a Boto3 session
session = boto3.Session()

# Create a CloudWatch Logs client
logs_client = session.client('logs')

# List all CloudWatch Log Groups
log_group_info = []

# Initialize parameters for pagination
paginator = logs_client.get_paginator('describe_log_groups')
for page in paginator.paginate():
    for log_group in page['logGroups']:
        log_group_name = log_group['logGroupName']
        creation_time = log_group['creationTime']
        log_group_info.append([log_group_name, creation_time])

# Get the total count of log groups
total_log_groups = len(log_group_info)

# Define table headers
headers = ["Log Group Name", "Creation Time"]

# Print the table of log groups
print("\nList of CloudWatch Log Groups:")
print(tabulate(log_group_info, headers, tablefmt="grid"))
print(f"Total Log Groups: {total_log_groups}")
