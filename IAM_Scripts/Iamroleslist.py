import boto3
from tabulate import tabulate

# Initialize a Boto3 session
session = boto3.Session()

# Create an IAM client
iam_client = session.client('iam')

# List IAM roles
roles = iam_client.list_roles()

# Create a table to store the role information
table_data = []

# Iterate through the roles and gather information
for role in roles['Roles']:
    role_name = role['RoleName']
    creation_date = role['CreateDate'].strftime('%Y-%m-%d %H:%M:%S')
    
    # Get role last activity timestamp
    role_last_activity = "N/A"
    
    # Query CloudTrail logs to find the last activity for the role
    # You'll need to implement the CloudTrail log query separately
    
    table_data.append([role_name, creation_date, role_last_activity])

# Define table headers
headers = ["Role Name", "Creation Date", "Last Activity"]

# Print the table
print(tabulate(table_data, headers, tablefmt="grid"))
