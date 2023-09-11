import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the AWS Lambda service without specifying credentials or region
lambda_client = boto3.client('lambda')

# Retrieve a list of Lambda functions
response = lambda_client.list_functions()

# Get the list of Lambda functions and their count
lambda_functions = response['Functions']
function_count = len(lambda_functions)

# Create a table with proper formatting for Lambda functions
table = PrettyTable()
table.field_names = ["Function Name", "Runtime", "Handler", "Memory (MB)", "Timeout (s)"]

# Populate the table with Lambda function information
for function in lambda_functions:
    function_name = function['FunctionName']
    runtime = function['Runtime']
    handler = function['Handler']
    memory_size = function['MemorySize']
    timeout = function['Timeout']

    table.add_row([function_name, runtime, handler, memory_size, timeout])

# Print the formatted table of Lambda functions and the total count
print(table)
print(f"Total Lambda functions: {function_count}")
