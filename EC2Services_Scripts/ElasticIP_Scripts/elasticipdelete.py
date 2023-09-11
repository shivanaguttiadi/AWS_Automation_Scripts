import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Replace 'your_allocation_id' with the Allocation ID of the Elastic IP you want to delete
allocation_ids_to_delete = ['44.197.35.29', '44.209.88.222']

# Initialize a table for displaying the results
table = PrettyTable()
table.field_names = ["Allocation ID", "Status"]

# Delete the specified Elastic IP addresses and record the results in the table
for allocation_id in allocation_ids_to_delete:
    try:
        ec2.release_address(AllocationId=allocation_id)
        table.add_row([allocation_id, "Deleted"])
    except Exception as e:
        table.add_row([allocation_id, f"Error: {str(e)}"])

# Print the table with the results
print(table)
