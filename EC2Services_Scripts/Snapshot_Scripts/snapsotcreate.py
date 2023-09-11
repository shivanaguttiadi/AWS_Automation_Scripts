import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Define a list of EBS volume IDs that you want to create snapshots for
volume_ids_to_snapshot = ['vol-0690f4ed13c534a26']  # Replace with your volume IDs

# Create an empty table for the snapshots
snapshot_table = PrettyTable()
snapshot_table.field_names = ["Snapshot ID", "Volume ID", "Description", "Status", "Progress", "Start Time"]

# Iterate through the list of volume IDs and create snapshots for each volume
for volume_id in volume_ids_to_snapshot:
    # Specify a description for the snapshot
    snapshot_description = f'Snapshot for volume {volume_id}'

    # Create the snapshot
    response = ec2.create_snapshot(
        VolumeId=volume_id,
        Description=snapshot_description
    )

    # Retrieve snapshot details from the response
    snapshot_id = response['SnapshotId']
    volume_id = response['VolumeId']
    description = response['Description']
    status = response['State']
    progress = response['Progress']
    start_time = response['StartTime']

    # Add snapshot details to the table
    snapshot_table.add_row([snapshot_id, volume_id, description, status, progress, start_time])

# Print the table of created snapshots
print(snapshot_table)
