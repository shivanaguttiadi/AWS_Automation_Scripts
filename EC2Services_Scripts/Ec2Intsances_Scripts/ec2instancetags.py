import boto3
from tabulate import tabulate

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# List all EC2 instances
response = ec2.describe_instances()

# Create a list to store the instance tag information
instance_tags_info = []

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']

        # Retrieve instance tags
        instance_tags = instance.get('Tags', [])

        # If there are tags, extract the key-value pairs
        if instance_tags:
            tag_info = ', '.join([f"{tag['Key']}={tag['Value']}" for tag in instance_tags])
            instance_tags_info.append([
                instance_id,
                tag_info,
            ])

# Create a table and print it
table_headers = ["Instance ID", "Tags"]
table = tabulate(instance_tags_info, headers=table_headers, tablefmt="grid")
print("List of EC2 Instances and Their Tags:")
print(table)
