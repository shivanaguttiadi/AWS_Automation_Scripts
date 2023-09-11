import boto3
from tabulate import tabulate

# Initialize the Lambda client
lambda_client = boto3.client('lambda')

# Get a list of Lambda functions
response = lambda_client.list_functions()

# Initialize a list to store the table data
table_data = []

# Iterate through the Lambda functions
for function in response['Functions']:
    function_name = function['FunctionName']
    
    # Get the tags for the Lambda function
    try:
        tags_response = lambda_client.list_tags(Resource=function['FunctionArn'])
        tags = tags_response.get('Tags', [])
        
        # Check if the Lambda function has any tags
        if not tags:
            table_data.append([function_name, "No tags found"])
        else:
            tag_rows = [f"{key}: {value}" for key, value in tags.items()]
            table_data.append([function_name, "\n".join(tag_rows)])
    
    except lambda_client.exceptions.ResourceNotFoundException:
        table_data.append([function_name, "Lambda function not found"])
    except Exception as e:
        table_data.append([function_name, f"An error occurred: {str(e)}"])

# Define the table headers
headers = ["Function Name", "Tags"]

# Print the table with wider columns
print(tabulate(table_data, headers, tablefmt="pretty", stralign="left", numalign="left"))
