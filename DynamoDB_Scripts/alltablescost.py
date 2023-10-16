import boto3
from datetime import datetime, timezone
from prettytable import PrettyTable

# Initialize AWS clients
dynamodb_client = boto3.client("dynamodb")

# Fetch a list of DynamoDB table names
table_list = dynamodb_client.list_tables()
table_names = table_list["TableNames"]

# Create a table to display the results
table = PrettyTable()
table.field_names = ["Table Name", "Creation Date", "Total Cost ($)"]

# Define your pricing for read and write capacity units per hour
cost_per_read_capacity_unit = 0.00013  # Replace with your pricing for read capacity units per hour
cost_per_write_capacity_unit = 0.00065  # Replace with your pricing for write capacity units per hour

# Iterate through the table names
for table_name in table_names:
    # Get the provisioned capacity details for the DynamoDB table
    response = dynamodb_client.describe_table(TableName=table_name)
    # Extract the creation date of the table
    creation_date = response["Table"]["CreationDateTime"].astimezone(timezone.utc)
    
    current_date = datetime.now(timezone.utc)  # Ensure current_date is offset-aware

    # Calculate the total cost for read and write capacity units
    days_since_creation = (current_date - creation_date).days
    total_read_cost = cost_per_read_capacity_unit * response["Table"]["ProvisionedThroughput"]["ReadCapacityUnits"] * days_since_creation * 365 # Assuming 30 days in a month
    total_write_cost = cost_per_write_capacity_unit * response["Table"]["ProvisionedThroughput"]["WriteCapacityUnits"] * days_since_creation * 365 # Assuming 30 days in a month
    total_cost = total_read_cost + total_write_cost

    # Add the table data to the PrettyTable
    table.add_row([table_name, creation_date.strftime("%Y-%m-%d"), f"${total_cost:.2f}"])

# Print the table
print(table)
