import boto3
from tabulate import tabulate

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Replace with your desired EC2 instance details
instance_count = 1
ami_id = 'ami-051f7e7f6c2f40dc1'  # Replace with a compatible AMI ID for the instance type
instance_type = 't2.micro'  # Choose an instance type that matches the AMI architecture
key_name = 'Learn_Devops'  # Replace with the name of your key pair
tag_name = 'Adi_AWS_Admin'
tag_value = 'Implement'
instance_name = 'Adi_AWS_Admin_ec2'  # Replace with your desired instance name

# Create EC2 instances with tags
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    MinCount=instance_count,
    MaxCount=instance_count,
    KeyName=key_name,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': instance_name,
                },
                {
                    'Key': tag_name,
                    'Value': tag_value,
                },
                {
                    'Key': 'Owner',
                    'Value': 'Adi',
                },
                {
                    'Key': 'Email_Id',
                    'Value': 'adi.shiva@zapcg.com',
                },
            ],
        },
    ],
)

# Extract the instance IDs of the newly created instances
instance_ids = [instance['InstanceId'] for instance in response['Instances']]

print(f"Created {instance_count} EC2 instances with tags and Name '{instance_name}':")
for instance_id in instance_ids:
    print(f"Instance ID: {instance_id}")

# Describe the instances to get their details
response = ec2.describe_instances(InstanceIds=instance_ids)

# Create a table for instance details
instance_info = []

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        tags = instance.get('Tags', [])

        # Get the instance name from tags (if available)
        for tag in tags:
            if tag['Key'] == 'Name':
                instance_name = tag['Value']
                break

        instance_info.append([instance_id, instance_name])

# Create a table and print it for instance details (instance ID and name)
table_headers = ["Instance ID", "Instance Name"]
table = tabulate(instance_info, headers=table_headers, tablefmt="grid")
print("\nInstance Details:")
print(table)
