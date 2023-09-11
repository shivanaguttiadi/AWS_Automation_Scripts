import boto3
from tabulate import tabulate

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Replace 'your-instance-id' with the actual EC2 instance IDs to delete (you can add multiple IDs)
instance_ids_to_delete = [
    'i-0c51211db8a6af7c3', 'i-0fbcaba166b3f9ae2', 'i-06cca74db04186662',
    'i-0b3a2cc6b3b7c5d72', 'i-0d24b173d7b8af36b', 'i-0f267061c3aba08dd',
    'i-01ccd888f0ac7f911', 'i-0071c78e659ff0bb1', 'i-0a2eb1289c559210e',
    'i-04fe065bbb5053863'
]

# Delete the EC2 instances
ec2.terminate_instances(InstanceIds=instance_ids_to_delete)

# Wait for the instances to be terminated (optional but recommended)
ec2.get_waiter('instance_terminated').wait(InstanceIds=instance_ids_to_delete)

# List all EC2 instances after deletion
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

# Calculate the total instance count
total_instance_count = len(instance_info)

# Create a table and print it for instance information
table_headers = ["Instance Name", "Instance ID", "Attached Volumes", "Instance Type", "Launch Time", "Key Pair"]
table = tabulate(instance_info, headers=table_headers, tablefmt="grid")
print("List of EC2 Instances:")
print(table)

# Print the total instance count
print("\nTotal Instance Count After Deletion:", total_instance_count)
