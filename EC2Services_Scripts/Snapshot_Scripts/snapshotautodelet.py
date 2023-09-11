import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Describe all snapshots
snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']

# Create a table to display snapshot information
snapshot_table = PrettyTable()
snapshot_table.field_names = ["Snapshot ID", "Description", "Volume ID", "Start Time", "Progress", "State"]

# Initialize a counter for deleted snapshots
deleted_snapshot_count = 0

# Iterate through snapshots
for snapshot in snapshots:
    snapshot_id = snapshot['SnapshotId']
    description = snapshot['Description']
    volume_id = snapshot['VolumeId']
    start_time = snapshot['StartTime'].strftime('%Y-%m-%d %H:%M:%S')
    progress = snapshot['Progress']
    state = snapshot['State']

    # Check if the snapshot is unattached (no volume ID)
    if not volume_id:
        # Delete the unattached snapshot
        ec2.delete_snapshot(SnapshotId=snapshot_id)
        deleted_snapshot_count += 1
    else:
        # Add the attached snapshot to the table
        snapshot_table.add_row([snapshot_id, description, volume_id, start_time, progress, state])

# Print the table of attached snapshots
print(snapshot_table)

# Print the count of deleted snapshots
print(f"Deleted {deleted_snapshot_count} unattached snapshots.")
