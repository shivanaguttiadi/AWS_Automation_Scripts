import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Retrieve a list of all snapshots
snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']

# Create a table with proper formatting for the output
table = PrettyTable()
table.field_names = ["Snapshot ID", "Volume ID", "Description", "State", "Progress"]

# Populate the table with snapshot information
for snapshot in snapshots:
    snapshot_id = snapshot['SnapshotId']
    volume_id = snapshot['VolumeId']
    description = snapshot.get('Description', 'N/A')
    state = snapshot['State']
    progress = snapshot.get('Progress', 'N/A')

    table.add_row([snapshot_id, volume_id, description, state, progress])

# Print the table
print(table)
