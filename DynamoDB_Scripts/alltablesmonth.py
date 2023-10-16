import boto3
import pandas as pd

# Initialize AWS clients
dynamodb_client = boto3.client("dynamodb")

# Fetch a list of DynamoDB table names
table_list = dynamodb_client.list_tables()
table_names = table_list["TableNames"]

# Define your pricing for read and write request units
cost_per_read_request = 0.00013  # Replace with your pricing for read request units
cost_per_write_request = 0.00065  # Replace with your pricing for write request units

# Create a list to store cost data for each table
cost_data = []

# Initialize a total cost variable
total_cost = 0

# Iterate through the table names with a serial number
for i, table_name in enumerate(table_names, start=1):
    # Describe the table to get provisioned capacity details
    response = dynamodb_client.describe_table(TableName=table_name)
    provisioned_throughput = response["Table"]["ProvisionedThroughput"]
    read_capacity_units = provisioned_throughput["ReadCapacityUnits"]
    write_capacity_units = provisioned_throughput["WriteCapacityUnits"]

    # Calculate the monthly cost based on provisioned capacity
    read_cost_sep = read_capacity_units * 30 * cost_per_read_request  # 30 days
    write_cost_sep = write_capacity_units * 30 * cost_per_write_request  # 30 days

    # Calculate the total cost for the table
    total_cost_sep = read_cost_sep + write_cost_sep

    # Append the cost data to the list
    cost_data.append({
        "Serial": i,
        "Table Name": table_name,
        "Read Cost (Sep)": read_cost_sep,
        "Write Cost (Sep)": write_cost_sep,
        "Total Cost (Sep)": total_cost_sep
    })

    # Add the cost to the total
    total_cost += total_cost_sep

# Create a DataFrame from the cost data
df = pd.DataFrame(cost_data)

# Print the formatted table
print(df.to_markdown(index=False))

# Print the total cost
print(f"Total Cost for All Tables: {total_cost:.2f}")
