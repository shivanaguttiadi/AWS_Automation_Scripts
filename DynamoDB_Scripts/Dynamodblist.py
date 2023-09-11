import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the DynamoDB service
dynamodb = boto3.client('dynamodb')

# List DynamoDB tables
response = dynamodb.list_tables()

# Get the list of table names from the response
table_names = response['TableNames']

# Initialize a counter for the total count of tables
total_table_count = len(table_names)

# Create a table for displaying the results
table = PrettyTable()
table.field_names = ["Table Name", "Status", "Total Size (Bytes)", "Read Capacity Mode", "Write Capacity Mode"]

# Populate the table with DynamoDB table information
for table_name in table_names:
    table_description = dynamodb.describe_table(TableName=table_name)['Table']
    status = table_description['TableStatus']
    total_size_bytes = table_description['TableSizeBytes']
    read_capacity_mode = table_description['ProvisionedThroughput']['ReadCapacityUnits']
    write_capacity_mode = table_description['ProvisionedThroughput']['WriteCapacityUnits']

    table.add_row([table_name, status, total_size_bytes, read_capacity_mode, write_capacity_mode])

# Print the table of DynamoDB table information and the total count
print(table)
print(f"Total DynamoDB tables: {total_table_count}")
