import boto3
from tabulate import tabulate

# Initialize a Boto3 session
session = boto3.Session()

# Create a resource groups tagging client
tagging_client = session.client('resourcegroupstaggingapi')

# List resources and their tags
resources = tagging_client.get_resources()

# Create a list to store the resource and tag information
table_data = []

# Extract and add resource types and their tags to the list
for resource in resources['ResourceTagMappingList']:
    resource_type = resource.get('ResourceARN').split(':')[5]
    tags = resource.get('Tags', [])
    
    # Filter out the 'aws:' prefix tags as they are AWS-generated
    custom_tags = [tag for tag in tags if not tag['Key'].startswith('aws:')]

    if custom_tags:
        row = [resource_type]
        for tag in custom_tags:
            row.extend([tag['Key'], tag['Value']])
        table_data.append(row)

# Define table headers
headers = ["Resource Type", "Tag Key", "Tag Value"]

# Print the table
print(tabulate(table_data, headers, tablefmt="grid"))
