import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the DynamoDB service
dynamodb = boto3.client('dynamodb')

# Define a list of DynamoDB table names to delete
table_names_to_delete = ['test']  # Replace with your table names

# Initialize a counter for deleted tables
deleted_table_count = 0

# Create a table for displaying the results
table = PrettyTable()
table.field_names = ["Table Name", "Status"]

# Iterate through the list of table names and delete each table
for table_name in table_names_to_delete:
    try:
        dynamodb.delete_table(TableName=table_name)
        deleted_table_count += 1
        table.add_row([table_name, "Deleted"])
    except Exception as e:
        table.add_row([table_name, f"Error: {str(e)}"])

# Print the table of deleted tables and the total count
print(table)
print(f"Total tables deleted: {deleted_table_count}")
