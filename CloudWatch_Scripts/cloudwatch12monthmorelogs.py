import boto3
from datetime import datetime, timedelta
from tabulate import tabulate

# Initialize a Boto3 session
session = boto3.Session()

# Create a CloudWatch Logs client
logs_client = session.client('logs')

# Calculate the cutoff date for logs older than 3 months
cutoff_date = datetime.now() - timedelta(days=90)

# List all CloudWatch Log Groups
log_groups = logs_client.describe_log_groups()

# Create a list to store log group information
log_group_info = []

for log_group in log_groups['logGroups']:
    log_group_name = log_group['logGroupName']
    retention_in_days = log_group.get('retentionInDays', 0)

    # Check if the log group has data older than 3 months
    if retention_in_days > 90:
        log_group_info.append([log_group_name, retention_in_days])

# Define table headers
headers = ["Log Group Name", "Retention (Days)"]

# Print the table of log groups with data older than 3 months
print("\nList of CloudWatch Log Groups with Data Older Than 3 Months:")
print(tabulate(log_group_info, headers, tablefmt="grid"))
