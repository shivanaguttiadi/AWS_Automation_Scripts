import boto3
from tabulate import tabulate

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# List all EBS volumes
response = ec2.describe_volumes()

# Create a list to store the volume information
volume_info = []

for volume in response['Volumes']:
    volume_info.append([
        volume['VolumeId'],
        volume['Size'],
        volume['AvailabilityZone'],
        volume['State']
    ])

# Create a table and print it
table_headers = ["Volume ID", "Size (GiB)", "Availability Zone", "State"]
table = tabulate(volume_info, headers=table_headers, tablefmt="grid")
print(table)
