import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Define a list of Subnet IDs that you want to delete
subnet_ids_to_delete = ['subnet-05e842f480fc912d5', 'subnet-05e842f480fc912d5', 'subnet-0e2fbc82552d34312', 'subnet-0678b324909b3129d']  # Replace with your subnet IDs

# Create a table with proper formatting
table = PrettyTable()
table.field_names = ["Subnet ID", "Status"]

# Loop through the list of subnet IDs and delete each subnet
for subnet_id in subnet_ids_to_delete:
    try:
        ec2.delete_subnet(SubnetId=subnet_id)
        table.add_row([subnet_id, "Deleted"])
    except Exception as e:
        table.add_row([subnet_id, f"Error: {e}"])

# Print the formatted table
print(table)
