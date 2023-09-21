import boto3
from tabulate import tabulate

# Initialize a Boto3 session
session = boto3.Session()

# Create a CloudFormation client
cf_client = session.client('cloudformation')

# List active CloudFormation stacks
stacks = cf_client.list_stacks(StackStatusFilter=['CREATE_COMPLETE', 'UPDATE_COMPLETE'])

# Create a table to store the stack information
table_data = []

# Initialize a dictionary to store tag counts
tag_counts = {}

# Iterate through the stacks and gather information
for stack in stacks['StackSummaries']:
    stack_name = stack['StackName']
    creation_time = stack['CreationTime'].strftime('%Y-%m-%d %H:%M:%S')
    
    # Get stack tags
    stack_tags = cf_client.list_stack_resources(StackName=stack_name)
    
    # Count tags
    for tag in stack_tags['StackResourceSummaries']:
        if tag['ResourceType'] == 'AWS::CloudFormation::Stack':
            continue  # Skip the stack itself
        for key, value in tag['Tags'].items():
            tag_key_value = f"{key}: {value}"
            if tag_key_value in tag_counts:
                tag_counts[tag_key_value] += 1
            else:
                tag_counts[tag_key_value] = 1
    
    table_data.append([stack_name, creation_time, ', '.join(tag_counts.keys())])

# Define table headers
headers = ["Stack Name", "Created Date", "Tags"]

# Print the table
print(tabulate(table_data, headers, tablefmt="grid"))

# Print the total count of stacks
print(f"Total Stacks: {len(stacks['StackSummaries'])}")
