import boto3
from tabulate import tabulate

# Initialize a Boto3 session
session = boto3.Session()

# Create a resource groups tagging client
tagging_client = session.client('resourcegroupstaggingapi')

# List tags for resources
tags_response = tagging_client.get_tag_keys()

# Create a list to store the active tags
active_tags = []

# Iterate through the tags to find active tags
for tag_key in tags_response['TagKeys']:
    # Check if the tag key is associated with any resources
    resources_response = tagging_client.get_resources(
        TagFilters=[{'Key': tag_key}]
    )
    if resources_response['ResourceTagMappingList']:
        active_tags.append(tag_key)

# Define table headers
headers = ["Active Tag Key"]

# Print the table of active tags
print("\nList of Active Tags:")
print(tabulate([[tag] for tag in active_tags], headers, tablefmt="grid"))
