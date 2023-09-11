import boto3
from tabulate import tabulate

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# List all EBS volumes with the "available" state
response = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])

# Create a list to store the volume information
volume_info = []

for volume in response['Volumes']:
    volume_id = volume['VolumeId']
    volume_size = volume['Size']
    volume_type = volume['VolumeType']
    volume_status = volume['State']

    # Get the volume name from the tags
    volume_name = ""
    for tag in volume.get('Tags', []):
        if tag['Key'] == 'Name':
            volume_name = tag['Value']
            break

    volume_info.append([
        volume_id,
        volume_name,  # Include the volume name
        volume_size,
        volume_type,
        volume_status,
    ])

# Create a table and print it
table_headers = ["Volume ID", "Volume Name", "Size (GiB)", "Volume Type", "Volume Status"]
table = tabulate(volume_info, headers=table_headers, tablefmt="grid")
print("List of Available EBS Volumes:")
print(table)
