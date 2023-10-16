import boto3
from prettytable import PrettyTable

# Initialize the AWS DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='us-east-1')  # Replace with your AWS region

# Define your AWS pricing for DynamoDB capacity units for September
read_capacity_cost_per_unit = 0.00013  # Replace with your pricing for read capacity units per hour
write_capacity_cost_per_unit = 0.00065  # Replace with your pricing for write capacity units per hour

# Fetch a list of DynamoDB table names
table_list = dynamodb.list_tables()
table_names = table_list['TableNames']

# Initialize variables to accumulate total read and write capacity units
total_read_units = 0
total_write_units = 0

# Calculate the total read and write capacity units for all tables
for table_name in table_names:
    # Describe the table to get its provisioned throughput settings
    table_description = dynamodb.describe_table(TableName=table_name)
    provisioned_throughput = table_description['Table']['ProvisionedThroughput']
    read_capacity_units = provisioned_throughput['ReadCapacityUnits']
    write_capacity_units = provisioned_throughput['WriteCapacityUnits']

    # Accumulate the capacity units
    total_read_units += read_capacity_units
    total_write_units += write_capacity_units

# Calculate the estimated cost for total read capacity units
total_read_cost = total_read_units * read_capacity_cost_per_unit * 30 * 24  # Assuming 30 days in a month

# Calculate the estimated cost for total write capacity units
total_write_cost = total_write_units * write_capacity_cost_per_unit * 30 * 24  # Assuming 30 days in a month

# Calculate the total estimated cost
total_estimated_cost = total_read_cost + total_write_cost

# Create a table to display the results
table = PrettyTable()
table.field_names = ["Metric", "Total"]
table.add_row(["Total Read Capacity Units", total_read_units])
table.add_row(["Total Write Capacity Units", total_write_units])
table.add_row(["Total Estimated Read Cost ($)", f"${total_read_cost:.2f}"])
table.add_row(["Total Estimated Write Cost ($)", f"${total_write_cost:.2f}"])
table.add_row(["Total Estimated Cost ($)", f"${total_estimated_cost:.2f}"])

# Print the table with the results
print(table)
