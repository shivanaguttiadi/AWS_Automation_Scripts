import boto3
from tabulate import tabulate
from datetime import datetime, timedelta

# Initialize a Boto3 session
session = boto3.Session()

# Create a CloudWatch Logs client
logs_client = session.client('logs')

# Calculate the start date for 12 months ago
start_date = datetime.now() - timedelta(days=365)

# List all CloudWatch Log Groups
log_groups = logs_client.describe_log_groups()

# Create a list to store log group information
log_group_info = []

for log_group in log_groups['logGroups']:
    log_group_name = log_group['logGroupName']
    retention_policy = log_group.get('retentionInDays')
    
    if retention_policy == 90:
        log_group_info.append([log_group_name])

# Define table headers
headers = ["Log Group Name"]

# Print the table of Log Groups with a 12-month retention policy
print("\nList of CloudWatch Log Groups with 3-Month Retention Policy:")
print(tabulate(log_group_info, headers, tablefmt="grid"))
