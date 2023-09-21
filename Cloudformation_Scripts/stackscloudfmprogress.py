import boto3
from tabulate import tabulate

# Initialize a Boto3 session
session = boto3.Session()

# Create a CloudFormation client
cf_client = session.client('cloudformation')

# List the CloudFormation stacks
stacks = cf_client.list_stacks(StackStatusFilter=['CREATE_IN_PROGRESS', 'ROLLBACK_IN_PROGRESS', 'UPDATE_IN_PROGRESS'])

# Create a table to store stack information
table_data = []

# Iterate through the stacks and gather information
for stack in stacks['StackSummaries']:
    stack_name = stack['StackName']
    stack_status = stack['StackStatus']
    creation_time = stack['CreationTime'].strftime('%Y-%m-%d %H:%M:%S')
    description = stack.get('Description', '-')
    table_data.append([stack_name, stack_status, creation_time, description])

# Define table headers
headers = ["Stack Name", "Status", "Creation Time", "Description"]

# Print the table of in-progress stacks
print(tabulate(table_data, headers, tablefmt="grid"))
