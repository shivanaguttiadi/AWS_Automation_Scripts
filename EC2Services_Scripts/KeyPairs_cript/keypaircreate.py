import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Define the name for your Key Pair
key_pair_name = 'MyKeyPair'

# Define the tags for your Key Pair (optional)
tags = [{'Key': 'Environment', 'Value': 'Production'}, {'Key': 'Owner', 'Value': 'John Doe'}]

# Create the Key Pair with optional tags
response = ec2.create_key_pair(KeyName=key_pair_name, TagSpecifications=[{'ResourceType': 'key-pair', 'Tags': tags}])

# Retrieve the Key Pair's private key material
private_key_material = response['KeyMaterial']

# Save the private key material to a file (optional)
with open(f'{key_pair_name}.pem', 'w') as key_file:
    key_file.write(private_key_material)

# Create a table with the Key Pair name
table = PrettyTable()
table.field_names = ["Key Pair Name"]
table.add_row([key_pair_name])

# Print the table with the Key Pair name
print(table)
