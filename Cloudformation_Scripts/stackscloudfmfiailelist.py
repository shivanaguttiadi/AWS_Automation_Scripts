import boto3
from tabulate import tabulate

# Initialize a Boto3 session
session = boto3.Session()

# Create a CloudFormation client
cf_client = session.client('cloudformation')

# List the names of the stacks you want to delete
stack_names_to_delete = ["StackName1", "StackName2"]  # Replace with the names of your stacks

# Initialize a variable to track failed stacks
failed_stacks = []

# Delete the specified stacks and track any failures
for stack_name in stack_names_to_delete:
    try:
        cf_client.delete_stack(StackName=stack_name)
    except Exception as e:
        failed_stacks.append({"StackName": stack_name, "Error": str(e)})

# Create a table to display the failed stacks
table_data = []

# Add failed stacks to the table
for failed_stack in failed_stacks:
    table_data.append([failed_stack["StackName"], failed_stack["Error"]])

# Define table headers
headers = ["Stack Name", "Error Message"]

# Print the table of failed stacks
if failed_stacks:
    print(tabulate(table_data, headers, tablefmt="grid"))
else:
    print("No stacks failed to delete.")
