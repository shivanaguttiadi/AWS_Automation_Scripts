import boto3
from prettytable import PrettyTable

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

# List all the tables in your DynamoDB
response = dynamodb.list_tables()

# Create a PrettyTable for the output
table = PrettyTable()
table.field_names = ["Table Name", "Read Capacity Units", "Write Capacity Units", "Total Data Size (MB)"]

# Loop through each table and get read and write capacity units
for table_name in response['TableNames']:
    # Describe the table to get read and write capacity settings
    table_info = dynamodb.describe_table(TableName=table_name)
    
    # Extract the read and write capacity units
    read_capacity_units = table_info['Table']['ProvisionedThroughput']['ReadCapacityUnits']
    write_capacity_units = table_info['Table']['ProvisionedThroughput']['WriteCapacityUnits']
    
    # Calculate the total data size in KB
    total_data_size_mb = 0
    
    # Check if the 'LocalSecondaryIndexes' key exists
    if 'LocalSecondaryIndexes' in table_info['Table']:
        for index in table_info['Table']['LocalSecondaryIndexes']:
            total_data_size_mb += index['IndexSizeBytes'] / 1024
    
    total_data_size_mb += table_info['Table']['TableSizeBytes'] / 1024
    
    # Add a row to the PrettyTable
    table.add_row([table_name, read_capacity_units, write_capacity_units, total_data_size_mb])

# Print the formatted table
print(table)
