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
        retention_in_days = log_group.get('retentionInDays', 'Never Expire')
        log_group_info.append([log_group_name, retention_in_days])

# Filter log groups that never expire (retentionInDays is None)
never_expire_log_groups = [info for info in log_group_info if info[1] == 'Never Expire']

# Define table headers
headers = ["Log Group Name", "Retention"]

# Print the table of log groups that never expire
print("\nList of CloudWatch Log Groups with Never Expire Retention:")
print(tabulate(never_expire_log_groups, headers, tablefmt="grid"))
