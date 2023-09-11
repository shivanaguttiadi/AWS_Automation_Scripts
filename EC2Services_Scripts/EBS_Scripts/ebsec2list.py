import boto3
from tabulate import tabulate

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# List all EBS volumes
response = ec2.describe_volumes()

# Create a list to store the volume information
volume_info = []

for volume in response['Volumes']:
    attachments = volume.get('Attachments', [])
    for attachment in attachments:
        instance_id = attachment.get('InstanceId', 'N/A')
        instance_name = "N/A"
        
        # Get the EC2 instance name if available
        instance = ec2.describe_instances(InstanceIds=[instance_id])
        if 'Reservations' in instance and len(instance['Reservations']) > 0:
            instances = instance['Reservations'][0]['Instances']
            if len(instances) > 0:
                tags = instances[0].get('Tags', [])
                for tag in tags:
                    if tag['Key'] == 'Name':
                        instance_name = tag['Value']
                        break
        
        volume_info.append([
            volume['VolumeId'],
            volume['Size'],
            volume['AvailabilityZone'],
            volume['State'],
            instance_id,
            instance_name
        ])

# Create a table and print it
table_headers = ["Volume ID", "Size (GiB)", "Availability Zone", "State", "Instance ID", "Instance Name"]
table = tabulate(volume_info, headers=table_headers, tablefmt="grid")
print("List of EBS Volumes with Attached EC2 Instances:")
print(table)
