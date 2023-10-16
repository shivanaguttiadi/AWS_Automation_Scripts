import boto3
from tabulate import tabulate

# Initialize the CloudWatch Logs client
client = boto3.client('logs', region_name='us-east-1')

# List all log groups
log_groups = client.describe_log_groups()

# Define the retention policy in days (1 day in this case)
retention_days = 1

# Initialize a list to store the results in a table format
table_data = []

# Loop through each log group and set the retention policy
for log_group in log_groups['logGroups']:
    log_group_name = log_group['logGroupName']
    
    # Set the retention policy to 1 day
    client.put_retention_policy(
        logGroupName=log_group_name,
        retentionInDays=retention_days
    )
    
    # Append log group name and retention policy to the table data
    table_data.append([log_group_name, retention_days])

# Print the results in a table format
print(tabulate(table_data, headers=['Log Group Name', 'Retention (Days)'], tablefmt='grid'))

print("Retention policy set for all log groups to one day.")
