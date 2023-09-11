import boto3
from tabulate import tabulate

# Initialize the IAM client
iam_client = boto3.client('iam')

# Initialize variables to store counts
total_users = 0
total_groups = 0
total_roles = 0
total_policies = 0

# Paginate through IAM users
paginator = iam_client.get_paginator('list_users')
for page in paginator.paginate():
    total_users += len(page['Users'])

# Paginate through IAM groups
paginator = iam_client.get_paginator('list_groups')
for page in paginator.paginate():
    total_groups += len(page['Groups'])

# Paginate through IAM roles
paginator = iam_client.get_paginator('list_roles')
for page in paginator.paginate():
    total_roles += len(page['Roles'])

# Paginate through IAM policies
paginator = iam_client.get_paginator('list_policies')
for page in paginator.paginate(Scope='All'):
    total_policies += len(page['Policies'])

# Create a table to display counts
table_data = [
    ["IAM Users", total_users],
    ["IAM Groups", total_groups],
    ["IAM Roles", total_roles],
    ["IAM Policies", total_policies]
]

# Define the table headers
headers = ["Entity Type", "Count"]

# Print the table
print(tabulate(table_data, headers, tablefmt="pretty"))
