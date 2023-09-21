import boto3
from tabulate import tabulate

# Initialize a Boto3 session
session = boto3.Session()

# Create an AWS Config client
config_client = session.client('config')

# Specify the tag key you want to check for deactivation
tag_key_to_check = 'Project_Name'

# Get a list of resources and their tags
resource_tags = []

paginator = config_client.get_paginator('list_discovered_resources')
for page in paginator.paginate(resourceType='AWS::AllSupported'):
    for resource in page['resourceIdentifiers']:
        resource_id = resource['resourceId']
        resource_type = resource['resourceType']
        tags_response = config_client.list_tags_for_resource(ResourceId=resource_id)
        tags = tags_response.get('Tags', [])
        resource_tags.append({'Resource ID': resource_id, 'Resource Type': resource_type, 'Tags': tags})

# Identify resources without the specified tag key
deactivated_tags = []

for resource in resource_tags:
    tags = resource['Tags']
    tag_key_found = any(tag['Key'] == tag_key_to_check for tag in tags)
    
    if not tag_key_found:
        deactivated_tags.append({'Resource ID': resource['Resource ID'], 'Resource Type': resource['Resource Type']})

# Define table headers
headers = ['Resource ID', 'Resource Type']

# Print the table of deactivated tags
print("\nList of Deactivated Tags (Tags removed from resources):")
print(tabulate(deactivated_tags, headers, tablefmt="grid"))
