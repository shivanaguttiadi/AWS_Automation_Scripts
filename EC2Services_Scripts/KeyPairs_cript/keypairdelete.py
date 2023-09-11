import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Define the name of the Key Pair you want to delete
key_pair_name = 'MyKeyPair'  # Replace with your Key Pair name

# Delete the Key Pair
response = ec2.delete_key_pair(KeyName=key_pair_name)

# Create a table for the output
table = PrettyTable()
table.field_names = ["Key Pair Name", "Status"]

# Check if the deletion was successful
if response['ResponseMetadata']['HTTPStatusCode'] == 200:
    table.add_row([key_pair_name, "Deleted"])
    print(table)
else:
    table.add_row([key_pair_name, "Failed to delete"])
    print(table)

