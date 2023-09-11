import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Define a list of network interface IDs to delete
network_interface_ids_to_delete = ['eni-12345678', 'eni-87654321']  # Replace with your network interface IDs

# Create a table to display the deleted network interfaces
deleted_interfaces_table = PrettyTable()
deleted_interfaces_table.field_names = ["Network Interface ID", "Status"]

# Loop through the list of network interface IDs and delete each one
for interface_id in network_interface_ids_to_delete:
    try:
        ec2.delete_network_interface(NetworkInterfaceId=interface_id)
        deleted_interfaces_table.add_row([interface_id, "Deleted"])
    except Exception as e:
        deleted_interfaces_table.add_row([interface_id, f"Failed to delete: {str(e)}"])

# Print the table of deleted network interfaces
print("Deleted Network Interfaces:")
print(deleted_interfaces_table)
