import boto3
from tabulate import tabulate

# Initialize the Lambda client
lambda_client = boto3.client('lambda')

# Specify the names of the Lambda functions you want to delete (replace with your function names)
function_names_to_delete = ['TransactionProcessor', 'Post_sign_in', 'offers_generateoffer-dde-lm-ue1-dev', 'dev-delete-function', 'offers_getoffer-dde-lm-ue1-dev']

# Initialize a list to store the table data
deleted_functions_data = []

for function_name in function_names_to_delete:
    try:
        # Delete the Lambda function
        lambda_client.delete_function(FunctionName=function_name)
        deleted_functions_data.append([function_name, "Deleted"])
    except lambda_client.exceptions.ResourceNotFoundException:
        deleted_functions_data.append([function_name, "Not found"])
    except Exception as e:
        deleted_functions_data.append([function_name, f"Error: {str(e)}"])

# Define the table headers
headers = ["Function Name", "Status"]

# Print the table
print(tabulate(deleted_functions_data, headers, tablefmt="pretty"))
