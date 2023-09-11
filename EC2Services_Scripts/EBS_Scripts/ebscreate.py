import boto3
from prettytable import PrettyTable
from datetime import datetime

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Define the parameters for the new EBS volumes
availability_zone = 'us-east-1a'  # Replace with your desired availability zone
volume_size = 10  # Replace with the desired size in GiB
volume_type = 'gp2'  # Change to the desired volume type (e.g., 'gp2', 'io1', 'standard')

# Define tags for the EBS volumes
tags = [{'Key': 'Name', 'Value': 'MyEBSTest1'},
        {'Key': 'Environment', 'Value': 'Production'}]

# Create the first EBS volume
response1 = ec2.create_volume(
    AvailabilityZone=availability_zone,
    Size=volume_size,
    VolumeType=volume_type,
    TagSpecifications=[{'ResourceType': 'volume', 'Tags': tags}]
)

# Create the second EBS volume
response2 = ec2.create_volume(
    AvailabilityZone=availability_zone,
    Size=volume_size,
    VolumeType=volume_type,
    TagSpecifications=[{'ResourceType': 'volume', 'Tags': tags}]
)

# Retrieve the volume IDs, names, created dates, volume sizes, and volume types from the responses
volume_id1 = response1['VolumeId']
volume_id2 = response2['VolumeId']
volume_name1 = tags[0]['Value']
volume_name2 = tags[0]['Value']
created_date1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
created_date2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
volume_size1 = volume_size
volume_size2 = volume_size
volume_type1 = volume_type
volume_type2 = volume_type

# Create a table with proper formatting for the EBS volumes
table = PrettyTable()
table.field_names = ["Volume Name", "Volume ID", "Created Date", "Volume Size (GiB)", "Volume Type"]

# Add the volume details to the table
table.add_row([volume_name1, volume_id1, created_date1, volume_size1, volume_type1])
table.add_row([volume_name2, volume_id2, created_date2, volume_size2, volume_type2])

# Print the formatted table
print(table)
