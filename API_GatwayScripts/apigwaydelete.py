import boto3
from tabulate import tabulate

# Initialize a Boto3 session
session = boto3.Session()

# Create an API Gateway client
apigateway_client = session.client('apigateway')

# Replace the list below with the names of the APIs you want to delete
apis_to_delete = ['TransactionApis', 'sam-app', 'oserverless-swagger-demo','oserverless-swagger-demo','orders_opensearch_crud']

# Delete the specified APIs by name
deleted_apis = []

for api_name in apis_to_delete:
    try:
        api_to_delete = apigateway_client.get_rest_api(restApiId=api_name)
        apigateway_client.delete_rest_api(restApiId=api_to_delete['id'])
        deleted_apis.append(api_name)
        print(f"Deleted API: {api_name}")
    except apigateway_client.exceptions.NotFoundException:
        print(f"API {api_name} not found")

# List the remaining APIs
apis = apigateway_client.get_rest_apis()

# Create a table to store the API information
table_data = []

# Iterate through the remaining APIs and gather information
for api in apis['items']:
    api_id = api['id']
    api_name = api['name']
    api_description = api.get('description', '-')
    table_data.append([api_id, api_name, api_description])

# Calculate the total count of remaining APIs
total_apis = len(table_data)

# Append the total count as a separate row
table_data.append(['Total APIs:', total_apis])

# Define table headers
headers = ["API ID", "API Name", "Description"]

# Print the table
print(tabulate(table_data, headers, tablefmt="grid"))

# Display the list of deleted APIs
if deleted_apis:
    print("\nDeleted APIs:")
    for api_name in deleted_apis:
        print(api_name)
