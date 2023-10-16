import boto3
from tabulate import tabulate

# Initialize the DynamoDB client
dynamodb_client = boto3.client('dynamodb')

# List DynamoDB tables
response = dynamodb_client.list_tables()

# Initialize a list to store the table data
table_data = []

# Iterate through the DynamoDB tables
for table_name in response['TableNames']:
    # Get the tags for the DynamoDB table
    try:
        tags_response = dynamodb_client.list_tags(ResourceArn=f"arn:aws:dynamodb:::table/{table_name}")
        tags = tags_response.get('Tags', {})
        
        # Format tags as a string
        tags_str = ', '.join([f"{tag['Key']}: {tag['Value']}" for tag in tags])
        
        table_data.append([table_name, tags_str])
    
    except dynamodb_client.exceptions.ResourceNotFoundException:
        table_data.append([table_name, "Table not found"])
    except Exception as e:
        table_data.append([table_name, f"An error occurred: {str(e)}"])

# Define the table headers
headers = ["Table Name", "Tags"]

# Print the table with wider columns
print(tabulate(table_data, headers, tablefmt="pretty", stralign="left", numalign="left"))
