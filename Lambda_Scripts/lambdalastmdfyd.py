import boto3
from datetime import datetime, timedelta
from tabulate import tabulate

# Initialize the Lambda client
lambda_client = boto3.client('lambda')

# Calculate the date one month ago
one_month_ago = datetime.now() - timedelta(days=30)

# List all Lambda functions
response = lambda_client.list_functions()

# Initialize a list to store the table data
table_data = []

for function in response['Functions']:
    function_name = function['FunctionName']
    last_modified = function['LastModified']
    
    # Parse the last modified date into a datetime object
    last_modified_date = datetime.strptime(last_modified, '%Y-%m-%dT%H:%M:%S.%f+0000')
    
    # Check if the function was modified more than one month ago
    if last_modified_date < one_month_ago:
        table_data.append([function_name, last_modified])

# Define the table headers
headers = ["Function Name", "Last Modified"]

# Print the table
print(tabulate(table_data, headers, tablefmt="pretty"))
