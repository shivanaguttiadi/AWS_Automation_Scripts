import boto3
from tabulate import tabulate

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# List all EBS volumes
response = ec2.describe_volumes()

# Create a dictionary to store instance information
instance_info = {}

# Get EC2 instance information
for reservation in ec2.describe_instances()['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_name = 'N/A'
        
        # Get the instance name from tags
        for tag in instance.get('Tags', []):
            if tag['Key'] == '':
                instance_name = tag['Value']
                break
        
        instance_info[instance_id] = instance_name

# Create a list to store the volume information
volume_info = []

for volume in response['Volumes']:
    tags = volume.get('Tags', [])
    volume_tags = ", ".join([f"{tag['Key']}={tag['Value']}" for tag in tags])
    
    attachments = volume.get('Attachments', [])
    instance_id = 'N/A'
    instance_name = 'N/A'
    
    # Get the EC2 instance information if attached
    if attachments:
        attachment = attachments[0]
        instance_id = attachment['InstanceId']
        instance_name = instance_info.get(instance_id, 'N/A')
    
    volume_info.append([
        volume['VolumeId'],
        volume_tags,
        volume['Size'],
        volume['AvailabilityZone'],
        volume['State'],
        instance_id,
        instance_name
    ])

# Create a table and print it
table_headers = ["Volume ID", "Tags", "Size (GiB)", "Availability Zone", "State", "Instance ID", "Instance Name"]
table = tabulate(volume_info, headers=table_headers, tablefmt="grid")
print("List of EBS Volumes with Tags, Instance ID, and Instance Name:")
print(table)
