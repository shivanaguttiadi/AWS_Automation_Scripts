import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Create an Elastic IP address
response = ec2.allocate_address(Domain='vpc')  # Use 'vpc' for VPC, 'standard' for EC2-Classic

# Retrieve the Elastic IP address from the response
eip_address = response['PublicIp']

# Set the name and tags for the Elastic IP
eip_name = 'AadigsIP'  # Replace with your desired name
tags = [{'Key': 'Name', 'Value': eip_name}]  # You can add more tags as needed

ec2.create_tags(Resources=[response['AllocationId']], Tags=tags)

# Retrieve the tags for the Elastic IP
tags_response = ec2.describe_tags(Filters=[{'Name': 'resource-id', 'Values': [response['AllocationId']]}])
tags_dict = {tag['Key']: tag['Value'] for tag in tags_response['Tags']}

# Create a table with proper formatting
table = PrettyTable()
table.field_names = ["Elastic IP Address", "Name", "Tags"]

# Populate the table with Elastic IP details
table.add_row([eip_address, eip_name, tags_dict])

# Print the formatted table
print(table)
