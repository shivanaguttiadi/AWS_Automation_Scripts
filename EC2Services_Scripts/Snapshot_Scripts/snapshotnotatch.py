import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Describe all snapshots
snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']

# Create an empty table for unattached snapshots
unattached_snapshot_table = PrettyTable()
unattached_snapshot_table.field_names = ["Snapshot ID", "Description", "Volume ID", "Start Time", "Progress", "State"]

# Iterate through snapshots and filter unattached ones
for snapshot in snapshots:
    snapshot_id = snapshot['SnapshotId']
    description = snapshot['Description']
    volume_id = snapshot['VolumeId']
    start_time = snapshot['StartTime'].strftime('%Y-%m-%d %H:%M:%S')
    progress = snapshot['Progress']
    state = snapshot['State']

    # Check if the snapshot is unattached (no volume ID)
    if not volume_id:
        unattached_snapshot_table.add_row([snapshot_id, description, "N/A", start_time, progress, state])

# Print the table of unattached snapshots
print(unattached_snapshot_table)
