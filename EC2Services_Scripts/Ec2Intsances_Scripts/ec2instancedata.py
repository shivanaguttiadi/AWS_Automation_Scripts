import boto3
from tabulate import tabulate

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# List all EC2 instances
response = ec2.describe_instances()

# Create a list to store the instance information
instance_info = []

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        instance_launch_time = instance['LaunchTime'].strftime('%Y-%m-%d %H:%M:%S')
        instance_key_name = instance.get('KeyName', 'N/A')
        
        # Retrieve instance name from tags (if available)
        instance_name = 'N/A'
        for tag in instance.get('Tags', []):
            if tag['Key'] == 'Name':
                instance_name = tag['Value']
                break
        
        # Retrieve attached volumes
        attached_volumes = ', '.join([vol['Ebs']['VolumeId'] for vol in instance.get('BlockDeviceMappings', [])])

        instance_info.append([
            instance_name,
            instance_id,
            attached_volumes,
            instance_type,
            instance_launch_time,
            instance_key_name,
        ])

# Create a table and print it
table_headers = ["Instance Name", "Instance ID", "Attached Volumes", "Instance Type", "Launch Time", "Key Pair"]
table = tabulate(instance_info, headers=table_headers, tablefmt="grid")
print("List of EC2 Instances:")
print(table)
