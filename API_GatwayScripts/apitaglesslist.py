import boto3
from tabulate import tabulate

# Initialize a Boto3 session
session = boto3.Session()

# Create an API Gateway client
apigateway_client = session.client('apigateway')

# List the APIs
apis = apigateway_client.get_rest_apis()

# Create a table to store the API information
table_data = []

# Iterate through the APIs and gather information for tagged APIs
for api in apis['items']:
    api_id = api['id']
    api_name = api['name']
    api_description = api.get('description', '-')
    
    # Check if the API has tags
    tags = apigateway_client.get_tags(resourceArn=f'arn:aws:apigateway:{session.region_name}::/restapis/{api_id}')
    if tags.get('tags'):
        tag_string = ', '.join([f'{key}: {value}' for key, value in tags['tags'].items()])
        table_data.append([api_id, api_name, api_description, tag_string])

# Define table headers
headers = ["API ID", "API Name", "Description", "Tags"]

# Print the table with increased spacing
print(tabulate(table_data, headers, tablefmt="pretty"))
