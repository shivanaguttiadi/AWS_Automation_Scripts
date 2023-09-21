import boto3
from tabulate import tabulate

# Initialize a Boto3 session
session = boto3.Session()

# Create a CloudFormation client
cf_client = session.client('cloudformation')

# List the names of the stacks you want to delete
stack_names_to_delete = ["sam", "sam", "sam","chandana-test","sssssssss"]  # Replace with the names of your stacks

# Initialize variables to track deleted and failed stacks
deleted_stacks = []
failed_stacks = []

# Delete the specified stacks
for stack_name in stack_names_to_delete:
    try:
        cf_client.delete_stack(StackName=stack_name)
        deleted_stacks.append(stack_name)
    except Exception as e:
        failed_stacks.append({"StackName": stack_name, "Error": str(e)})

# Create a table to display the results
table_data = []

# Add deleted stacks to the table
for stack_name in deleted_stacks:
    table_data.append([stack_name, "Deleted", "-"])

# Add failed stacks to the table
for failed_stack in failed_stacks:
    table_data.append([failed_stack["StackName"], "Failed", failed_stack["Error"]])

# Define table headers
headers = ["Stack Name", "Status", "Error Message"]

# Print the table
print(tabulate(table_data, headers, tablefmt="grid"))

# Print the total number of deleted stacks
print(f"Total Deleted Stacks: {len(deleted_stacks)}")
