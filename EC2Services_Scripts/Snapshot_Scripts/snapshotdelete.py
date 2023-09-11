import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Define a list of snapshot IDs that you want to delete
snapshot_ids_to_delete = ['snap-063d3902a47931807']  # Replace with your snapshot IDs

# Create a table to display snapshot deletion information
deletion_table = PrettyTable()
deletion_table.field_names = ["Snapshot ID", "Deletion Status"]

# Initialize a counter for deleted snapshots
deleted_snapshot_count = 0

# Iterate through the list of snapshot IDs and delete each one
for snapshot_id in snapshot_ids_to_delete:
    try:
        # Delete the snapshot
        ec2.delete_snapshot(SnapshotId=snapshot_id)
        deletion_table.add_row([snapshot_id, "Deleted"])
        deleted_snapshot_count += 1
    except Exception as e:
        # Handle exceptions (e.g., snapshot not found)
        deletion_table.add_row([snapshot_id, f"Error: {str(e)}"])

# Print the table of snapshot deletion information
print(deletion_table)

# Print the count of deleted snapshots
print(f"Deleted {deleted_snapshot_count} snapshots.")
